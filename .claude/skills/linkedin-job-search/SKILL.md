---
name: linkedin-job-search
description: Search and read LinkedIn job listings in the user's Chrome using targeted JS extraction instead of full-page snapshots. Works with Claude in Chrome (preferred) or the Chrome DevTools MCP. Use whenever the user asks to search/browse LinkedIn for job offers, or to pull details from a specific LinkedIn job posting URL.
---

# linkedin-job-search

LinkedIn pages are enormous (nav, ads, "gente que podrías conocer", footer with 30 language
options...). Screenshots, accessibility snapshots or `read_page` on a LinkedIn page burn
thousands of tokens on noise. This skill runs a small JS snippet in the page to pull only the
fields needed, straight from the DOM.

## Step 0 — which browser tool is available?

Check your tool list (load deferred tools with `ToolSearch` if needed) and use the first that
exists:

| Option | Navigate | Run JS | How to pass the snippets below |
|---|---|---|---|
| **A. Claude in Chrome** (preferred) | `mcp__claude-in-chrome__navigate` | `mcp__claude-in-chrome__javascript_tool` (`action: "javascript_exec"`, `tabId`, `text`) | Paste the snippet **as-is** in `text` (they are IIFEs; the tool returns the value of the last expression and supports top-level `await`). Get a `tabId` first with `tabs_context_mcp`. |
| **B. Chrome DevTools MCP** | `mcp__chrome-devtools__navigate_page` | `mcp__chrome-devtools__evaluate_script` | Pass **only the arrow function** in `function` — drop the leading `await (`, the wrapping `(` and the final `)()`; the tool calls it itself. Use `list_pages`/`select_page` to reuse an open LinkedIn tab. |

**If neither exists**, don't improvise with WebFetch (LinkedIn blocks it). Tell the user, in
plain language, that the browser connection isn't set up and point them to the README section
*"Conectar Claude con Chrome"*. Meanwhile they can paste the offer text or URL by hand, which
is enough for everything else in this repo.

**Login:** the user must be logged into LinkedIn in that Chrome. If the page shows a login
wall, ask them to log in themselves — never type credentials.

## Searching job listings

Build the search URL directly instead of clicking through the UI:

```
https://www.linkedin.com/jobs/search/?keywords=<url-encoded keywords>&location=<url-encoded location>&f_TPR=<r604800|r2592000>
```

- `f_TPR=r604800` → last 7 days, `r2592000` → last 30 days. Omit for no date filter.
- `f_WT=2` → remote only (`1` on-site, `3` hybrid; combine as `f_WT=2%2C3`).
- Boolean `OR` in `keywords` is unreliable — LinkedIn sometimes collapses results. Prefer
  **one keyword per search** and run several.
- Navigation may report a timeout even when the page loaded (LinkedIn keeps background
  requests open) — run the extraction anyway and check the result.

LinkedIn only renders the cards you have scrolled to (~7 of 25 at first). **Scroll the results
list first** with this snippet (it finds the scrollable pane itself):

```js
await (async () => {
  const first = document.querySelector('li[data-occludable-job-id], div.job-card-container');
  let pane = first && first.parentElement;
  while (pane && pane !== document.body && !(pane.scrollHeight > pane.clientHeight + 50 && getComputedStyle(pane).overflowY !== 'visible')) pane = pane.parentElement;
  const target = (pane && pane !== document.body) ? pane : document.scrollingElement;
  for (let y = 0; y <= target.scrollHeight; y += 400) { target.scrollTop = y; await new Promise(r => setTimeout(r, 250)); }
  return new Set([...document.querySelectorAll('a[href*="/jobs/view/"]')].map(a => a.href.split('?')[0])).size;
})()
```

Then extract job cards (covers both the logged-in and the logged-out page; dedupes by URL because
LinkedIn often renders each card twice):

```js
(() => {
  const results = [];
  document.querySelectorAll('div.job-card-container, li.jobs-search-results__list-item, li[data-occludable-job-id], div.base-card').forEach(card => {
    const title = card.querySelector('a.job-card-list__title, .job-card-list__title, .base-search-card__title, a[href*="/jobs/view/"]');
    const company = card.querySelector('.job-card-container__primary-description, .artdeco-entity-lockup__subtitle, .job-card-container__company-name, .base-search-card__subtitle');
    const location = card.querySelector('.job-card-container__metadata-item, .artdeco-entity-lockup__caption, .job-search-card__location');
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
})()
```

LinkedIn loads ~25 cards per page; add `&start=25`, `&start=50`... for more. If a search
returns 0 results it usually means there are genuinely no matches — only suspect the selectors
if **every** search returns 0 (then fall back to `get_page_text` / reading `main.innerText`).

## Reading a single job posting

Navigate to `https://www.linkedin.com/jobs/view/<id>/`, then extract the text (not the page):

```js
(() => {
  const main = document.querySelector('main');
  const text = main ? main.innerText : document.body.innerText;
  return JSON.stringify({text: text.slice(0, 4000)});
})()
```

4000 chars covers title, company, "Acerca del empleo", requirements and benefits for almost
every posting. Increase the slice only if requirements are cut off at the tail.

## Workflow in this repo

1. Show the user a short list (title, company, location, why it fits or not according to
   `kb/profile.md` → `## Criterios de búsqueda`). Don't dump every card.
2. Log the ones worth tracking in `applications.md`.
3. For an offer they want to pursue, save the **literal** text + URL in
   `applications/<empresa-rol>/oferta.md` (postings disappear), and put `% Oferta: <url>`
   near the top of the CV's `main.tex`.
4. Close the browser tabs you opened when done.
