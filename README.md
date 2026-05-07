# Motadata Blog Automation

**Claude-powered blog generation for [motadata.com/blog](https://www.motadata.com/blog/)**

This repository automates the creation, validation, and management of Motadata blog posts using Claude Code GitHub Actions. It contains 96 Ahrefs-validated blog topics and generates complete, SEO-optimized, brand-consistent blog posts on demand.

---

## How It Works

```
Topic request (issue / workflow dispatch)
        ↓
Claude reads CLAUDE.md + format/blog-format.md + brand/brand-voice.md
        ↓
Generates complete blog post (1,500–2,500 words, 7-block format)
        ↓
Saves to blogs/draft/ and opens a PR
        ↓
Claude validates the PR against format spec + posts review
        ↓
Approve → merge → move to blogs/published/
```

---

## Three Ways to Request a Blog

### 1. @claude Mention (Fastest)
Open an issue or comment on an existing one and tag `@claude`:

```
@claude Write a blog about "Observability vs Monitoring" targeting the keyword 
"observability vs monitoring" (vol 1,200, KD 8). It should be TOFU, 
link to the APM product page, and target NOC Engineers and SREs.
```

Claude will generate the full blog and open a PR automatically.

### 2. Issue Template (Structured)
Use the **Blog Request** issue template for a guided form. Claude picks it up when assigned.

### 3. Workflow Dispatch (Direct)
Go to **Actions → Generate Blog Post → Run workflow** and fill in:
- Topic title
- Focus keyword
- Funnel stage (TOFU/MOFU/BOFU)
- Target module (APM, ITSM, etc.)
- Word count target

---

## Repository Structure

```
motadata-blog-automation/
├── CLAUDE.md                          ← Claude's full project context (read this first)
├── .github/
│   ├── workflows/
│   │   ├── claude.yml                 ← Interactive: responds to @claude mentions
│   │   ├── generate-blog.yml          ← Automated: workflow_dispatch generation
│   │   └── validate-blog.yml          ← Auto-validates new blogs on PRs
│   └── ISSUE_TEMPLATE/
│       └── blog-request.yml           ← Structured blog request form
├── blogs/
│   ├── draft/                         ← Claude-generated drafts (awaiting review)
│   └── published/                     ← Approved blogs ready for CMS upload
├── planned/
│   ├── blog-gaps.md                   ← 45 capability-linked topics (Ahrefs-validated)
│   └── knowledge-base.md              ← 51 knowledge-base topics (Ahrefs-validated)
├── format/
│   └── blog-format.md                 ← 7-block format spec + blank template
├── brand/
│   ├── brand-voice.md                 ← Tone, vocabulary, sentence patterns
│   └── products.md                    ← Motadata product descriptions + URLs
└── scripts/
    └── validate_blog.py               ← Local validation script (run before PR)
```

---

## Topic Pipeline

**96 Ahrefs-validated topics ready to write:**

| File | Topics | Focus |
|------|--------|-------|
| `planned/blog-gaps.md` | 45 | Blogs that link directly to capability pages |
| `planned/knowledge-base.md` | 51 | Foundational/educational knowledge-base content |

**Top Priority 1 topics (KD ≤ 5, highest TP):**
- Network Security Monitoring Best Practices (KD 2, TP 32,000)
- APM Tool Comparison (KD 2, TP 4,800)
- Mean Time to Resolve / MTTR (KD 4, TP 4,400)
- ITIL Change Management Process (KD 5, TP 3,000)
- IT Asset Lifecycle Management (KD 3, vol 700)
- Microservices Monitoring Guide (KD 2, vol 600)
- Vulnerability Remediation Process (KD 2, vol 900)
- MSP Automation Guide (KD 0, TP 1,500)

---

## Setup

### Required Secrets

Add these to your repository secrets (Settings → Secrets and variables → Actions):

| Secret | Description |
|--------|-------------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key from [console.anthropic.com](https://console.anthropic.com) |

### Install Claude GitHub App

Install the official [Claude GitHub App](https://github.com/apps/claude) to enable @claude mentions in issues and PRs.

---

## Blog Format

Every generated blog follows the **7-Block Motadata Blog Format**:

1. **YAML frontmatter** — title, source_url, updated, meta_title, meta_description, focus_keyword, secondary_keywords, funnel_stage
2. **Title + Source line** — H1 + motadata.com/blog/[slug] URL
3. **Definition blockquote** — bold definition of the focus keyword
4. **Hook** — 2–4 paragraphs on the reader's pain point (no heading)
5. **Key Takeaways** — 5–8 bold bullet points
6. **Main content** — H2/H3 sections, comparison tables, numbered lists, internal links
7. **How Motadata Helps + FAQ** — product pitch + 4–6 Q&As

See `format/blog-format.md` for the complete specification and blank template.

---

## Validation

Every PR with a new blog in `blogs/draft/` or `blogs/published/` is automatically reviewed by Claude, which checks:

- [ ] All 8 YAML fields present
- [ ] focus_keyword in H1, meta_title, meta_description
- [ ] All 7 blocks present
- [ ] Word count 1,500–2,500
- [ ] No forbidden brand words (robust, powerful, cutting-edge, leverage, etc.)
- [ ] Minimum 2 internal links to motadata.com
- [ ] FAQ section with 4+ Q&As
- [ ] Appropriate funnel stage classification

---

## Motadata Products Quick Reference

| Suite | Products |
|-------|---------|
| **ObserveOps** | APM, Real User Monitoring, SLO, Log Monitoring, Network Observability, NCCM, Hybrid Infrastructure |
| **ServiceOps** | Service Management (ITSM), ITAM & CMDB, Patch Management, Agentic AI, MSP |

---

*Powered by [Claude Code GitHub Actions](https://github.com/anthropics/claude-code-action) · Built for [Motadata](https://www.motadata.com)*
