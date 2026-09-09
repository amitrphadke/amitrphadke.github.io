// ==UserScript==
// @name         CCDV-F tracker — Claude Academy auto-tick
// @namespace    https://www.amitphadke.com/
// @version      1.1.0
// @description  When a lesson on academy.claude.com shows as completed, tick it in the study tracker on amitphadke.com (writes progress.json in the site repo through the GitHub API).
// @author       Amit Phadke
// @match        https://academy.claude.com/*
// @grant        GM_xmlhttpRequest
// @grant        GM_getValue
// @grant        GM_setValue
// @grant        GM_registerMenuCommand
// @connect      api.github.com
// @connect      www.amitphadke.com
// @run-at       document-idle
// @updateURL    https://www.amitphadke.com/learning/ccdv-f/tracker/academy-sync.user.js
// @downloadURL  https://www.amitphadke.com/learning/ccdv-f/tracker/academy-sync.user.js
// ==/UserScript==

(function () {
  'use strict';
  const GH = { owner: 'amitrphadke', repo: 'amitrphadke.github.io', branch: 'master', path: 'learning/ccdv-f/tracker/progress.json' };
  const COURSES_URL = 'https://www.amitphadke.com/learning/ccdv-f/tracker/courses.json';
  const API = `https://api.github.com/repos/${GH.owner}/${GH.repo}/contents/${GH.path}`;

  const gm = (opts) => new Promise((res, rej) => GM_xmlhttpRequest({ ...opts, onload: r => res(r), onerror: e => rej(e), ontimeout: () => rej(new Error('timeout')) }));
  const b64enc = s => btoa(unescape(encodeURIComponent(s)));
  const b64dec = s => decodeURIComponent(escape(atob(String(s).replace(/\n/g, ''))));

  // ---------- token ----------
  // Token is kept in the userscript manager's storage AND in this site's localStorage (some managers do not persist GM values between pages).
  const LS_KEY = 'ccdvf-tracker-gh-token';
  function lsGet(k) { try { return localStorage.getItem(k) || ''; } catch (e) { return ''; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function gmGet(k, d) { try { const v = GM_getValue(k, d); return v == null ? d : v; } catch (e) { return d; } }
  function gmSet(k, v) { try { GM_setValue(k, v); } catch (e) {} }
  function getToken() { const g = gmGet('ghToken', ''); if (g) { if (!lsGet(LS_KEY)) lsSet(LS_KEY, g); return g; } const l = lsGet(LS_KEY); if (l) gmSet('ghToken', l); return l; }
  function setToken(v) { gmSet('ghToken', v); lsSet(LS_KEY, v); }
  function askToken(msg) {
    const box = document.createElement('div');
    box.style.cssText = 'position:fixed;right:16px;bottom:16px;z-index:999999;background:#14213d;color:#fff;padding:12px 14px;border-radius:8px;font:13px system-ui;max-width:320px;box-shadow:0 6px 24px rgba(0,0,0,.3)';
    box.innerHTML = `<div style="font-weight:600;margin-bottom:6px">CCDV-F tracker sync</div><div style="color:#b9c3d9;margin-bottom:8px">${msg || 'Paste the GitHub token (Contents: read & write on the site repo). Stored only in Tampermonkey.'}</div><input type="password" style="width:100%;padding:6px;border-radius:5px;border:1px solid #2a3757;background:#1b2540;color:#fff"><div style="margin-top:8px;display:flex;gap:6px"><button style="padding:5px 10px;border-radius:5px;border:0;background:#0b7a75;color:#fff;cursor:pointer">Save</button><button style="padding:5px 10px;border-radius:5px;border:1px solid #2a3757;background:transparent;color:#fff;cursor:pointer">Later</button></div>`;
    document.body.appendChild(box);
    const [save, later] = box.querySelectorAll('button'); const inp = box.querySelector('input');
    const doSave = () => { const v = inp.value.trim(); if (!v) return; setToken(v); box.remove(); toast('Token saved — syncing…'); sync(true); };
    save.onclick = doSave; inp.addEventListener('keydown', ev => { if (ev.key === 'Enter') { ev.preventDefault(); doSave(); } }); setTimeout(() => inp.focus(), 50);
    later.onclick = () => box.remove();
  }
  GM_registerMenuCommand('Set GitHub token for tracker sync', () => askToken());
  GM_registerMenuCommand('Sync tracker now', () => sync(true));
  GM_registerMenuCommand('Forget GitHub token', () => { setToken(''); toast('Token removed.'); });

  // ---------- ui ----------
  function toast(msg, ms = 3500) {
    const t = document.createElement('div');
    t.textContent = msg;
    t.style.cssText = 'position:fixed;left:16px;bottom:16px;z-index:999999;background:#0b7a75;color:#fff;padding:9px 13px;border-radius:6px;font:13px system-ui;box-shadow:0 4px 16px rgba(0,0,0,.25)';
    document.body.appendChild(t); setTimeout(() => t.remove(), ms);
  }

  // ---------- data ----------
  let coursesMap = null, coursesAt = 0;
  async function loadCourses() {
    if (coursesMap && Date.now() - coursesAt < 3600e3) return coursesMap;
    const r = await gm({ method: 'GET', url: COURSES_URL + '?t=' + Date.now() });
    coursesMap = JSON.parse(r.responseText).courses; coursesAt = Date.now(); return coursesMap;
  }
  function completedFromDoc(doc, slug) {
    const seen = new Set(); const done = [];
    doc.querySelectorAll(`a[href^="/courses/${slug}/"]`).forEach(a => {
      const ls = a.getAttribute('href').split('/').pop(); if (!ls || seen.has(ls)) return; seen.add(ls);
      if (/\(completed\)/i.test(a.textContent) || a.querySelector('[aria-label*="ompleted" i]')) done.push(ls);
    });
    return done;
  }
  const pageCache = {};
  async function completedFromCoursePage(slug) {
    const c = pageCache[slug]; if (c && Date.now() - c.at < 20e3) return c.done;
    try {
      const r = await gm({ method: 'GET', url: `${location.origin}/courses/${slug}?t=${Date.now()}`, headers: { Accept: 'text/html' } });
      const doc = new DOMParser().parseFromString(r.responseText, 'text/html');
      const done = completedFromDoc(doc, slug); pageCache[slug] = { at: Date.now(), done }; return done;
    } catch (e) { return []; }
  }
  async function scanPage() {
    const m = location.pathname.match(/^\/courses\/([^\/]+)/); if (!m) return null;
    const slug = m[1];
    const done = new Set(completedFromDoc(document, slug));
    (await completedFromCoursePage(slug)).forEach(x => done.add(x));   // lesson pages don't show the markers; the course page does
    return { slug, done: [...done].sort() };
  }

  // ---------- github ----------
  async function readProgress(tok) {
    const r = await gm({ method: 'GET', url: `${API}?ref=${GH.branch}&t=${Date.now()}`, headers: { Authorization: 'Bearer ' + tok, Accept: 'application/vnd.github+json' } });
    if (r.status === 404) return { sha: null, data: { state: {} } };
    if (r.status !== 200) throw new Error('GitHub ' + r.status);
    const j = JSON.parse(r.responseText); return { sha: j.sha, data: JSON.parse(b64dec(j.content) || '{}') };
  }
  async function writeProgress(tok, sha, data, msg) {
    const body = { message: msg, content: b64enc(JSON.stringify(data, null, 1)), branch: GH.branch }; if (sha) body.sha = sha;
    const r = await gm({ method: 'PUT', url: API, headers: { Authorization: 'Bearer ' + tok, Accept: 'application/vnd.github+json', 'Content-Type': 'application/json' }, data: JSON.stringify(body) });
    if (r.status !== 200 && r.status !== 201) throw new Error('GitHub write ' + r.status);
  }

  // ---------- sync ----------
  let busy = false, lastKey = '';
  async function sync(force) {
    if (busy) return; if (!location.pathname.startsWith('/courses/')) return;
    busy = true; let scan; try { scan = await scanPage(); } finally { busy = false; } if (!scan) return;
    const key = scan.slug + ':' + scan.done.join(','); if (!force && key === lastKey) return; lastKey = key;
    if (busy) return;
    const tok = getToken(); if (!tok) { if (force || !gmGet('askedOnce', false) && !lsGet('ccdvf-tracker-asked')) { gmSet('askedOnce', true); lsSet('ccdvf-tracker-asked', '1'); askToken(); } return; }
    busy = true;
    try {
      const courses = await loadCourses(); const course = courses[scan.slug];
      if (!course) { if (force) toast('This course is not in the tracker.'); return; }
      const wanted = scan.done.map(ls => course.lessons[ls]).filter(Boolean);
      if (!wanted.length) { if (force) toast('No completed lessons found on this page yet.'); return; }
      const { sha, data } = await readProgress(tok);
      data.state = data.state || {};
      const newly = wanted.filter(id => !data.state[id]);
      if (!newly.length) { if (force) toast('Tracker already up to date for this course.'); return; }
      newly.forEach(id => { data.state[id] = true; });
      data.savedAt = new Date().toISOString();
      await writeProgress(tok, sha, data, `tracker: ${newly.length} lesson${newly.length > 1 ? 's' : ''} completed on Claude Academy (${scan.slug})`);
      toast(`Tracker: ticked ${newly.length} lesson${newly.length > 1 ? 's' : ''} ✓`);
    } catch (e) {
      console.warn('[ccdvf-sync]', e); toast('Tracker sync failed: ' + e.message, 6000);
      if (/401|403/.test(e.message)) askToken('GitHub rejected the token — paste a new one.');
    } finally { busy = false; }
  }

  // run on load, on SPA navigation, and when the sidebar changes (a lesson just got marked complete)
  let debounce = null; const schedule = () => { clearTimeout(debounce); debounce = setTimeout(() => sync(false), 4000); };
  new MutationObserver(schedule).observe(document.documentElement, { childList: true, subtree: true, characterData: true });
  let lastPath = location.pathname; setInterval(() => { if (location.pathname !== lastPath) { lastPath = location.pathname; lastKey = ''; schedule(); } }, 1000);
  schedule();
})();
