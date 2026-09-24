---
name: linkedin-job-search
description: Search and read LinkedIn job listings via Chrome DevTools MCP using targeted JS extraction instead of full accessibility-tree snapshots. Use whenever the user asks to search/browse LinkedIn for job offers, or to pull details from a specific LinkedIn job posting URL.
---

# linkedin-job-search

LinkedIn pages are enormous in the accessibility tree (nav, ads, "gente que podrías conocer", footer with 30 language options...). `take_snapshot` on a LinkedIn page burns thousands of tokens on noise. This skill uses `evaluate_script` to pull only the structured fields needed, directly from the DOM.

## Prerequisites

- Chrome DevTools MCP tools loaded: `navigate_page`, `evaluate_script`, `list_pages`, `select_page` (load via `ToolSearch` if deferred).
- An existing Chrome tab already logged into LinkedIn (check with `list_pages` — if a LinkedIn tab exists, `select_page` it instead of opening a new one and re-authenticating).
- **Never use `take_snapshot` on a LinkedIn page.** Always use `evaluate_script`.

## Searching job listings

Build the search URL directly instead of clicking through the UI:

```
https://www.linkedin.com/jobs/search/?keywords=<url-encoded keywords>&location=<url-encoded location>&f_TPR=<r604800|r2592000>
```

- `f_TPR=r604800` → last 7 days, `r2592000` → last 30 days. Omit for no date filter.
- Boolean `OR` in `keywords` is unreliable — LinkedIn sometimes collapses results. Prefer **one keyword per search call** over combining with OR; run multiple searches instead.
- `navigate_page` to the URL. It may report a navigation timeout even when the page actually loaded (LinkedIn keeps background XHRs open) — proceed to extraction anyway and check the result.

Extract job cards with this script (dedupes by URL, since LinkedIn often renders each card twice in the DOM):

```js
() => {
  const results = [];
  document.querySelectorAll('div.job-card-container, li.jobs-search-results__list-item, li[data-occludable-job-id]').forEach(card => {
    const title = card.querySelector('a.job-card-list__title, .job-card-list__title, a[href*="/jobs/view/"]');
    const company = card.querySelector('.job-card-container__primary-description, .artdeco-entity-lockup__subtitle, .job-card-container__company-name');
    const location = card.querySelector('.job-card-container__metadata-item, .artdeco-entity-lockup__caption');
    const link = card.querySelector('a[href*="/jobs/view/"]');
    if (title || link) {
      results.push({
        title: title ? title.innerText.trim() : null,
        company: company ? company.innerText.trim() : null,
        location: location ? location.innerText.trim() : null,
        url: link ? link.href.split('?')[0] : null
      });
    }
  });
  const seen = new Set();
  const dedup = results.filter(r => { if (seen.has(r.url)) return false; seen.add(r.url); return true; });
  return JSON.stringify({count: dedup.length, results: dedup});
}
```

Pass this as the `function` argument to `evaluate_script`. If a search returns 0 results, it usually means the keyword genuinely has no matches in that location/window — don't assume the selector broke unless every search returns 0.

## Reading a single job posting

`navigate_page` to `https://www.linkedin.com/jobs/view/<id>/`, then extract the description text (not the full page):

```js
() => {
  const main = document.querySelector('main');
  const text = main ? main.innerText : document.body.innerText;
  return JSON.stringify({text: text.slice(0, 4000)});
}
```

4000 chars covers title, company, "Acerca del empleo", requirements, and benefits for almost every posting. Increase the slice only if a posting is unusually long and you're missing requirements at the tail.

## Workflow with the job-applications repo

When this is used inside a `job-applications`-style repo (tracker + per-company CV folders):

1. Log every candidate offer in `applications.md` (title, company, match strength, status, URL) — this is the single source of truth for what's been found.
2. When building a CV for a specific offer, save the offer URL **next to the CV itself**, not only in the tracker: the literal offer text + URL in `applications/<empresa-rol>/oferta.md` (postings disappear), plus a `% Oferta: <url>` comment near the top of `main.tex`. The tracker can get regenerated or filtered; the CV folder should be self-contained enough to know what it was written for without cross-referencing `applications.md`.
