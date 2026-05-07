# Motadata Blog Format Reference
**Source: Analysis of 130 Enhanced Blogs | 2026-05-07**

Every blog written for motadata.com/blog/ follows this exact structure. Do not deviate.

---

## YAML Frontmatter (required — all 8 fields)

```yaml
---
title: "[Full blog title — descriptive, keyword-rich, 60-80 chars]"
source_url: "https://www.motadata.com/blog/[url-slug]/"
updated: "[Month DD, YYYY]"
meta_title: "[SEO title ≤60 chars | Motadata]"
meta_description: "[Benefit-led description ≤155 chars — what reader learns, include keyword]"
focus_keyword: "[primary keyword exactly as it appears in the title]"
secondary_keywords:
  - [secondary keyword 1]
  - [secondary keyword 2]
  - [secondary keyword 3]
  - [secondary keyword 4]
  - [secondary keyword 5]
funnel_stage: "[TOFU / MOFU / BOFU]"
---
```

**Funnel stage guide:**
- `TOFU` — Educational, definitional ("What Is X", "How X Works", best practices) — widest audience
- `MOFU` — Evaluation, comparison ("X vs Y", "How to Choose", guides) — considers buying
- `BOFU` — Decision ("Why Motadata for X", case studies, ROI) — ready to buy

---

## Body Structure (7 blocks in order)

### Block 1 — Title + Source Line
After the YAML, repeat the full title as an H1 and include the source URL and updated date as plain text lines.

```markdown
# [Blog Title]

Source: https://www.motadata.com/blog/[slug]/
Updated: [Month DD, YYYY]
```

---

### Block 2 — Definition (required for TOFU, optional for others)
Use a blockquote with a **bolded definition** of the focus keyword. One sentence, plain language, 20–35 words.

```markdown
> **[Focus keyword]** is [plain-language definition in 20-35 words].
```

---

### Block 3 — Hook (2–4 paragraphs, no heading)
Opens with the reader's problem or pain point. Speaks directly to the persona. No jargon. Builds urgency or curiosity. Ends with the promise of what the post delivers.

Do NOT use a heading for this block — it runs immediately after the definition.

---

### Block 4 — Key Takeaways
Bold bullet list of 5–8 takeaways. Each bullet starts with a **bolded phrase** followed by a supporting clause. Scannable — readers can read just this section and understand the article's value.

```markdown
## Key Takeaways

- **[Bold phrase]** — supporting detail.
- **[Bold phrase]** — supporting detail.
```

---

### Block 5 — Main Content (H2/H3 structure)
The body. Length: 1,500–2,500 words total across all sections.

**Patterns by blog type:**

| Type | H2 Pattern | Example |
|------|-----------|---------|
| Best practices / tips | "N [Topic] Best Practices" then numbered H3s | "8 Network Security Monitoring Best Practices" |
| How-to / step-by-step | "How to [Verb] [Topic]" then numbered H3 steps | "How to Build an Observability Practice" |
| Definition / explainer | "What Is [Term]?" then H2 sections deepening the topic | "What Is Observability? A Definition That Works" |
| Comparison | "X vs Y: [Difference]" then H2 by criteria | "Observability vs Monitoring: Why the Distinction Matters" |

**Required elements inside main content:**
- At least 1 **comparison table** (use `| Col | Col |` format) where the topic supports it
- **Internal links** to Motadata product pages and glossary entries using natural anchor text
- **Bold sub-points** inside long bullet lists
- No paragraph longer than 5 lines

**Comparison table format:**
```markdown
| Aspect | Option A | Option B |
|--------|----------|----------|
| Row    | Value    | Value    |
```

**Internal link targets** (always use real motadata.com URLs):
- Product pages: `https://www.motadata.com/[product-slug]/`
- Blog posts: `https://www.motadata.com/blog/[slug]/`
- Glossary: `https://www.motadata.com/it-glossary/[term]/`
- Solutions: `https://www.motadata.com/solutions/[audience]/`

---

### Block 6 — "How Motadata [Delivers/Helps]" (required)
Soft CTA section — not a hard sell. 2–4 bullet points of specific platform capabilities relevant to the blog topic. End with 2 CTAs: demo link + free trial link.

```markdown
## How Motadata [Delivers / Helps Teams with] [Topic]

[1–2 sentences setting up the pitch naturally.]

- **[Feature]** — [what it does for the reader]
- **[Feature]** — [what it does for the reader]
- **[Feature]** — [what it does for the reader]

[Request a demo](https://www.motadata.com/demo) to see how [platform] supports [topic] at scale, or [start a free 30-day trial](https://www.motadata.com/free-trial/) to test it with your own [workflows/environment/team].
```

---

### Block 7 — FAQ (required)
4–6 questions. Use H3 for each question. Answer in 2–4 sentences. FAQs should match the "People Also Ask" queries that appear on Google for the focus keyword — practical, specific questions real searchers ask.

```markdown
## Frequently Asked Questions

### Q: [Question?]
[Answer in 2–4 sentences.]

### Q: [Question?]
[Answer in 2–4 sentences.]
```

---

## Word Count by Blog Type

| Type | Target word count |
|------|------------------|
| Definition / "What Is X" | 1,500–2,000 words |
| Best Practices (8–10 items) | 2,000–2,500 words |
| How-to / Step-by-step | 1,800–2,200 words |
| Comparison ("X vs Y") | 1,500–2,000 words |
| Process guide | 2,000–2,500 words |

---

## Style Rules

- **Voice**: Direct, second person ("your team", "you need"), no passive voice
- **Tone**: Expert but accessible — not academic, not marketing-speak
- **Sentences**: Short. Average 15–20 words. Cut everything that doesn't serve the reader.
- **Jargon**: Define on first use. Don't assume the reader knows acronyms.
- **Formatting**: Use bold for key terms on first use. Use numbered lists for steps, bullet lists for features/traits.
- **No fluff openers**: Never start with "In today's fast-paced world" or similar. Open with the problem.

---

## Slug Formula

```
/blog/[focus-keyword-with-hyphens]/
```

Examples:
- focus_keyword: "network security monitoring best practices" → `/blog/best-practices-of-network-security-monitoring/`
- focus_keyword: "what is observability" → `/blog/what-is-observability/`

---

## Complete Blank Template

```markdown
---
title: ""
source_url: "https://www.motadata.com/blog/"
updated: ""
meta_title: " | Motadata"
meta_description: ""
focus_keyword: ""
secondary_keywords:
  - 
  - 
  - 
  - 
funnel_stage: "TOFU"
---

# [Title]

Source: https://www.motadata.com/blog/[slug]/
Updated: [Date]

> **[Focus keyword]** is [definition].

[Hook paragraph 1 — the problem]

[Hook paragraph 2 — what this post delivers]

## Key Takeaways

- **[Phrase]** — [detail].
- **[Phrase]** — [detail].
- **[Phrase]** — [detail].
- **[Phrase]** — [detail].
- **[Phrase]** — [detail].

## [Why / What / How — Setup Section]

[Body paragraph]

## [Main Content Section 1]

### [H3 point 1]

[Content]

### [H3 point 2]

[Content]

## [Comparison Table Section — if applicable]

| Aspect | A | B |
|--------|---|---|
| Row | Value | Value |

## How Motadata [Helps / Delivers] [Topic]

[Setup sentence.]

- **[Feature]** — [benefit].
- **[Feature]** — [benefit].
- **[Feature]** — [benefit].

[Request a demo](https://www.motadata.com/demo) or [start a free trial](https://www.motadata.com/free-trial/).

## Frequently Asked Questions

### Q: [Question]?
[Answer.]

### Q: [Question]?
[Answer.]

### Q: [Question]?
[Answer.]

### Q: [Question]?
[Answer.]
```
