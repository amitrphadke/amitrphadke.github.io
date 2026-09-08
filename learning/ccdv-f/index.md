---
layout: article
permalink: /learning/ccdv-f/
key: learning-ccdv-f
title: "CCDV-F — the study journey"
aside:
  toc: true
---

{% assign c = site.data.certifications.in_progress | where: "id", "ccdv-f" | first %}

**Claude Certified Developer – Foundations** (Anthropic, exam code CCDV-F). Exam booked for **{{ c.exam_date | date: "%A %-d %B %Y" }}**, {{ c.exam_time }}. {{ c.format }}.

<div style="height:10px;background:#e6eaf1;border-radius:999px;overflow:hidden;max-width:480px;margin:8px 0 2px"><div style="width:{{ c.progress_pct }}%;height:100%;background:#0b7a75"></div></div>
<small>{{ c.progress_pct }}% of the plan complete · last updated {{ c.last_update | date: "%-d %b %Y" }}</small>

<a class="button button--primary button--rounded" href="{{ c.tracker_url }}">Open the study tracker</a>

## Why this one

I have spent twenty years automating other people's delivery pipelines. Over the last year the interesting problems on my projects have moved to a different layer: how to put a model like Claude into a CI/CD pipeline, a review bot, an incident-summariser, an internal agent — safely, cheaply, and in a way an SRE can operate. The CCDV-F blueprint is essentially a syllabus for exactly that, and my employer is funding the attempt, so it became the first certification I am doing in public.

## The plan

{{ c.plan }}. Every day has a reading list, numbered build steps and a "done when" line; every Sunday is a review day with a domain quiz and a short retrospective — that retrospective is what becomes the weekly post below.

| # | Chapter | Dates | Exam domain |
|---|---|---|---|
| 0 | Setup, accounts and the eligibility gate | 5–6 Sep | — |
| 1 | Messages API foundations | 7–13 Sep | Applications & Integration |
| 2 | Tool use, prompt caching, batches, production plumbing | 14–20 Sep | Applications & Integration · Tools & MCPs |
| 3 | Model selection, cost, prompt and context engineering | 21–27 Sep | Model Selection · Prompt & Context Engineering |
| 4 | Agents and workflows | 28 Sep – 4 Oct | Agents & Workflows |
| 5 | Tools and MCP | 5–11 Oct | Tools & MCPs |
| 6 | Claude Code on a real project | 12–18 Oct | Claude Code |
| 7 | Security, safety, evals, testing and debugging | 19–25 Oct | Security & Safety · Eval, Testing & Debugging |
| 8 | Practice exams and final revision | 26 Oct – 2 Nov | All domains |
| ★ | Exam day | 3 Nov | — |

## Exam blueprint

| Domain | Weight |
|---|---|
{% for d in c.domains -%}
| {{ d.name }} | {{ d.weight }}% |
{% endfor %}

## What is in the tracker

The [tracker]({{ c.tracker_url }}) is a single self-contained page: the day-by-day plan with study material per chapter, an 80-question practice bank, a spaced-repetition deck of exam traps, a per-domain readiness dashboard, a printable cheat sheet, and a library of 62 digests of the official documentation the exam draws on. This public copy is read-only in spirit — anything you tick saves only in your own browser — but the material is free to use if you are preparing for the same exam. Corrections are welcome by [email](mailto:amitrameshphadke@gmail.com).

## Mind maps

I learn best from mind maps, so the whole plan and study material also exist as FreeMind files that open in SimpleMind (File → Import → FreeMind) or any mind-map app that reads `.mm`: a [master map](mindmaps/00%20CCDV-F%20master%20map.mm) of the exam, and one map per chapter with the daily plan, study material, documentation digests, self-check questions and traps as branches.

{% assign maps = site.static_files | where_exp: "f", "f.path contains '/learning/ccdv-f/mindmaps/'" | sort: "path" %}
<ul>
{% for f in maps %}<li><a href="{{ f.path | relative_url }}">{{ f.basename }}</a></li>
{% endfor %}</ul>

## Weekly journal

{% assign posts = site.tags[c.tag] | sort: "date" | reverse %}
{% if posts.size > 0 %}
<ul>
{% for p in posts %}
<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a> <small>— {{ p.date | date: "%-d %b %Y" }}</small></li>
{% endfor %}
</ul>
{% else %}
The first entry lands on Sunday 13 September, at the end of Chapter 1.
{% endif %}
