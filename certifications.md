---
layout: page
permalink: /certifications.html
key: page-certifications
titles:
  en: Certifications / Education
---

## In progress

{% for c in site.data.certifications.in_progress %}
**[{{ c.name }}]({{ c.journey_url }})** — {{ c.vendor }} · {{ c.code }}
<span style="display:inline-block;padding:1px 8px;border-radius:999px;background:#c2711c;color:#fff;font-size:12px;vertical-align:middle">{{ c.status }}</span>

{{ c.format }} · exam {{ c.exam_date | date: "%a %-d %b %Y" }}{% if c.exam_time %}, {{ c.exam_time }}{% endif %}{% if c.funded_by == "employer" %} · employer-funded{% endif %}

<div style="height:8px;background:#e6eaf1;border-radius:999px;overflow:hidden;max-width:420px;margin:6px 0 2px"><div style="width:{{ c.progress_pct }}%;height:100%;background:#0b7a75"></div></div>
<small>{{ c.progress_pct }}% of the study plan complete as of {{ c.last_update | date: "%-d %b %Y" }} · [study journey]({{ c.journey_url }}) · [open the tracker]({{ c.tracker_url }})</small>

{% endfor %}

## Achieved

{% for c in site.data.certifications.achieved -%}
- {{ c.name }}{% if c.vendor != "" %} — {{ c.vendor }}{% endif %}{% if c.year %} ({{ c.year }}){% endif %}
{% endfor %}

## Education

| Degree | Institute | Years |
|---|---|---|
{% for e in site.data.certifications.education -%}
| {{ e.degree }} | {{ e.institute }} | {{ e.years }} |
{% endfor %}
