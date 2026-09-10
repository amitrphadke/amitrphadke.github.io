---
layout: front
key: page-home
---

<div class="band band--sheet">
  <div class="band__inner">
    <div class="hero">
      <div class="hero__grid">
        <div>
          <p class="hero__kick">Software Architect · DevSecOps</p>
          <h1 class="hero__title">I build things that have to <em>hold</em> — in code, and in oak.</h1>
          <p class="hero__lede">Twenty-two years designing the delivery platforms other teams ship on. Right now that means <b>secure-by-default pipelines, infrastructure as code and observability</b> for Wolters Kluwer, from UST in Pune.</p>
        </div>
        <img class="hero__portrait" src="{{ '/assets/images/amit-portrait.jpg' | relative_url }}" alt="Amit Phadke" width="720" height="720">
      </div>
      <div class="facts">
        <span><b>Now</b> — DevSecOps platform, UST</span>
        <span><b>Since</b> 2004</span>
        <span><b>Based</b> Pune, India</span>
      </div>
    </div>
  </div>
</div>

<div class="band band--dark">
  <div class="band__inner">
    <div class="statrow">
      <div class="stat"><div class="stat__n">22</div><span class="stat__l">Years in IT</span></div>
      <div class="stat"><div class="stat__n">18</div><span class="stat__l">Enterprise clients</span></div>
      <div class="stat"><div class="stat__n">4</div><span class="stat__l">Countries worked in</span></div>
      <div class="stat"><div class="stat__n">{{ site.data.certifications.achieved | size }}</div><span class="stat__l">Certifications held</span></div>
    </div>

    <div style="padding:38px 0 44px">
      <p class="seclabel">Currently</p>
      <div class="panel">
        <div class="panel__top">
          <h2 class="panel__title">DevSecOps platform · Wolters Kluwer</h2>
          <span class="badge">Live</span>
        </div>
        <span class="panel__meta">UST · Mar 2025 – present</span>
        <p>Standardising secure CI/CD, infrastructure as code and observability across product teams, with security and compliance gating built into every release.</p>
        <div class="pipe">
          <span class="pipe__node"><i></i><span>Build</span></span><span class="pipe__link"></span>
          <span class="pipe__node"><i></i><span>Test</span></span><span class="pipe__link"></span>
          <span class="pipe__node"><i></i><span>Scan</span></span><span class="pipe__link"></span>
          <span class="pipe__node"><i></i><span>Policy gate</span></span><span class="pipe__link"></span>
          <span class="pipe__node"><i></i><span>Deploy</span></span><span class="pipe__link"></span>
          <span class="pipe__node"><i></i><span>Observe</span></span>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="band band--sheet">
  <div class="band__inner" style="padding-top:42px;padding-bottom:44px">
    <p class="seclabel">Selected work</p>
    <div class="worklist">
      <div class="workrow">
        <span class="workrow__yr">2025 — now</span>
        <span class="workrow__t">Wolters Kluwer<em>Enterprise DevSecOps platform, landing zones, policy-as-code</em></span>
        <span class="workrow__s">UST</span>
      </div>
      <div class="workrow">
        <span class="workrow__yr">2023 — 2025</span>
        <span class="workrow__t">Cisco dCloud<em>Greenfield rebuild on EKS and Terraform, ADOT observability</em></span>
        <span class="workrow__s">Infosys</span>
      </div>
      <div class="workrow">
        <span class="workrow__yr">2021 — 2023</span>
        <span class="workrow__t">Adidas e-commerce<em>SRE and on-call for the hype-sales launch platform</em></span>
        <span class="workrow__s">Infosys</span>
      </div>
      <div class="workrow">
        <span class="workrow__yr">2020</span>
        <span class="workrow__t">Li &amp; Fung Logistics<em>Database DevOps — reference pipelines and gating</em></span>
        <span class="workrow__s">Infosys</span>
      </div>
    </div>
    <p style="margin-top:20px"><a href="{{ '/projects.html' | relative_url }}" class="btn">All work in detail</a></p>
  </div>
</div>

<div class="band band--paper">
  <div class="band__inner" style="padding-top:42px;padding-bottom:46px">
    <p class="seclabel">Career, to scale</p>
    <div class="dim">
      <span class="dim__label">2004 — 2026 · 22 years 3 months</span>
      <div class="dim__axis"></div>
      <div class="dim__ticks">
        <span class="dim__tick"><i></i><span>2004</span><b>J &amp; J</b></span>
        <span class="dim__tick"><i></i><span>2006</span><b>TCS</b></span>
        <span class="dim__tick"><i></i><span>2010</span><b>Infosys</b></span>
        <span class="dim__tick"><i></i><span>2019</span><b>Sonora</b></span>
        <span class="dim__tick"><i></i><span>2020</span><b>Infosys</b></span>
        <span class="dim__tick is-now"><i></i><span>2025</span><b>UST</b></span>
      </div>
    </div>
    <p style="margin-top:26px;color:var(--muted);font-size:14.5px;max-width:64ch">Fourteen of those years were spent in the Microsoft stack — C#, ASP.NET, SharePoint — before the move to platform engineering. <a href="{{ '/employers.html' | relative_url }}" style="color:var(--teal)">Full history →</a></p>
  </div>
</div>

<div class="band band--sheet">
  <div class="band__inner" style="padding-top:42px;padding-bottom:44px">
    <p class="seclabel">Learning in public</p>
    {%- for c in site.data.certifications.in_progress %}
    <div class="panel" style="background:var(--sheet);border-color:var(--rule);color:var(--ink)">
      <div class="panel__top">
        <h2 class="panel__title" style="color:var(--ink)"><a href="{{ c.journey_url | relative_url }}" style="color:var(--ink);text-decoration:none">{{ c.name }}</a></h2>
        <span class="badge badge--amber" style="background:rgba(180,118,42,.1);color:var(--ochre);border-color:rgba(180,118,42,.3)">{{ c.status }}</span>
      </div>
      <span class="panel__meta">{{ c.vendor }} · {{ c.code }} · exam {{ c.exam_date | date: "%-d %b %Y" }}</span>
      <p style="color:var(--muted)">{{ c.format }}</p>
      <div class="meter"><i style="width:{{ c.progress_pct }}%"></i></div>
      <p class="meter__note">{{ c.progress_pct }}% of the study plan complete · <a href="{{ c.journey_url | relative_url }}" style="color:var(--teal)">the journey</a> · <a href="{{ c.tracker_url | relative_url }}" style="color:var(--teal)">the tracker</a></p>
    </div>
    {%- endfor %}
  </div>
</div>

<div class="band band--paper">
  <div class="band__inner" style="padding-top:42px;padding-bottom:48px">
    <p class="seclabel">Away from the keyboard</p>
    <div style="display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center">
      <div>
        <p style="margin:0;color:var(--muted);font-size:15.5px;max-width:52ch">I design furniture and small machines in SketchUp and then cut them myself — corded tools and hand tools both. It is the same job as the day job: get the drawing right, and the assembly stops being an argument.</p>
      </div>
      <div>
        <p class="quote">Good infrastructure is joinery. If the fit is right, nothing needs glue.</p>
        <p class="quote__attr">On why the two hobbies are one hobby</p>
      </div>
    </div>
  </div>
</div>

<div class="band band--dark">
  <div class="band__inner" style="padding-top:40px;padding-bottom:46px">
    <p class="seclabel">Get in touch</p>
    <h2 style="font-family:var(--serif);font-weight:400;font-size:26px;margin:0 0 10px;letter-spacing:-.015em">Email is the quickest way to reach me.</h2>
    <p style="margin:0;color:var(--dark-mute);max-width:56ch;font-size:15px">I am also on LinkedIn and GitHub.</p>
    <div class="cta">
      <a class="btn" href="mailto:amitphadke1001@gmail.com">Email me</a>
      <a class="btn btn--ghost" href="https://www.linkedin.com/in/amitrameshphadke/">LinkedIn</a>
      <a class="btn btn--ghost" href="https://github.com/amitrphadke">GitHub</a>
    </div>
  </div>
</div>
