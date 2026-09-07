---
layout: page
permalink: /learning/
key: page-learning
titles:
  en: Learning
---

Certifications I am preparing for, in public: the plan, the tracker, and a weekly journal for each. Finished ones move to the [certifications page](/certifications.html).

{% for c in site.data.certifications.in_progress %}
### [{{ c.name }}]({{ c.journey_url }})
{{ c.vendor }} · {{ c.code }} · exam {{ c.exam_date | date: "%-d %b %Y" }} · <span style="display:inline-block;padding:1px 8px;border-radius:999px;background:#c2711c;color:#fff;font-size:12px">{{ c.status }}</span>

<div style="height:8px;background:#e6eaf1;border-radius:999px;overflow:hidden;max-width:420px;margin:6px 0 2px"><div style="width:{{ c.progress_pct }}%;height:100%;background:#0b7a75"></div></div>
<small>{{ c.progress_pct }}% complete · [journey]({{ c.journey_url }}) · [tracker]({{ c.tracker_url }})</small>

{% endfor %}
