#!/usr/bin/env python3
"""
Motadata Blog Validator
Run locally before submitting a PR to catch format errors early.

Usage:
    python scripts/validate_blog.py blogs/draft/your-blog.md
    python scripts/validate_blog.py blogs/draft/  # validate all drafts
"""

import sys
import re
import os
from pathlib import Path


REQUIRED_YAML_FIELDS = [
    "title", "source_url", "updated", "meta_title",
    "meta_description", "focus_keyword", "secondary_keywords", "funnel_stage"
]

FORBIDDEN_WORDS = [
    "robust", "powerful", "cutting-edge", "next-gen", "next generation",
    "leverage", "utilize", "game-changer", "revolutionary",
]

VALID_FUNNEL_STAGES = {"TOFU", "MOFU", "BOFU"}

REQUIRED_SECTIONS = [
    "Key Takeaways",
    "Frequently Asked Questions",
]

MIN_WORDS = 1500
MAX_WORDS = 2600
MIN_INTERNAL_LINKS = 2
MIN_FAQ_COUNT = 4


def validate_blog(filepath: str) -> dict:
    """Validate a single blog file. Returns dict with issues and score."""
    path = Path(filepath)
    if not path.exists():
        return {"error": f"File not found: {filepath}"}

    content = path.read_text(encoding="utf-8")
    issues = []
    warnings = []
    passed = []

    # --- YAML Frontmatter ---
    yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not yaml_match:
        issues.append("YAML frontmatter block (--- ... ---) not found")
    else:
        yaml_content = yaml_match.group(1)
        for field in REQUIRED_YAML_FIELDS:
            if f"{field}:" not in yaml_content:
                issues.append(f"Missing YAML field: '{field}'")
            else:
                passed.append(f"YAML field '{field}' present")

        # Meta title length
        meta_title_match = re.search(r'meta_title:\s*"([^"]+)"', yaml_content)
        if meta_title_match:
            mt = meta_title_match.group(1)
            if len(mt) > 60:
                issues.append(f"meta_title is {len(mt)} chars (max 60): '{mt}'")
            else:
                passed.append(f"meta_title length OK ({len(mt)} chars)")

        # Meta description length
        meta_desc_match = re.search(r'meta_description:\s*"([^"]+)"', yaml_content)
        if meta_desc_match:
            md = meta_desc_match.group(1)
            if len(md) > 155:
                issues.append(f"meta_description is {len(md)} chars (max 155)")
            else:
                passed.append(f"meta_description length OK ({len(md)} chars)")

        # Funnel stage
        funnel_match = re.search(r'funnel_stage:\s*"?(\w+)"?', yaml_content)
        if funnel_match:
            fs = funnel_match.group(1).upper()
            if fs not in VALID_FUNNEL_STAGES:
                issues.append(f"Invalid funnel_stage '{fs}' — must be TOFU, MOFU, or BOFU")
            else:
                passed.append(f"funnel_stage '{fs}' is valid")

        # Source URL format
        if "source_url:" in yaml_content:
            url_match = re.search(r'source_url:\s*"([^"]+)"', yaml_content)
            if url_match:
                url = url_match.group(1)
                if not url.startswith("https://www.motadata.com/blog/"):
                    issues.append(f"source_url should start with https://www.motadata.com/blog/ — got: {url}")
                else:
                    passed.append("source_url format correct")

    # --- Body Content ---
    body = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

    # H1 present
    if re.search(r"^# .+", body, re.MULTILINE):
        passed.append("H1 title present")
    else:
        issues.append("H1 title (# Title) not found in body")

    # Definition blockquote
    if re.search(r"^> \*\*.+\*\*", body, re.MULTILINE):
        passed.append("Definition blockquote present")
    else:
        warnings.append("Definition blockquote (> **keyword** is ...) not found — required for TOFU blogs")

    # Required sections
    for section in REQUIRED_SECTIONS:
        if f"## {section}" in body or f"## {section}" in body:
            passed.append(f"Section '## {section}' present")
        else:
            issues.append(f"Missing required section: '## {section}'")

    # How Motadata section
    if re.search(r"## How Motadata", body):
        passed.append("'## How Motadata' section present")
    else:
        issues.append("Missing '## How Motadata ...' section")

    # Word count
    words = len(re.findall(r"\b\w+\b", body))
    if words < MIN_WORDS:
        issues.append(f"Word count too low: {words} words (minimum {MIN_WORDS})")
    elif words > MAX_WORDS:
        warnings.append(f"Word count high: {words} words (target max {MAX_WORDS})")
    else:
        passed.append(f"Word count OK: {words} words")

    # Focus keyword in H1 and first 150 words
    if yaml_match:
        yaml_content = yaml_match.group(1)
        kw_match = re.search(r'focus_keyword:\s*"([^"]+)"', yaml_content)
        if kw_match:
            kw = kw_match.group(1).lower()
            h1_match = re.search(r"^# (.+)", body, re.MULTILINE)
            if h1_match and kw in h1_match.group(1).lower():
                passed.append(f"focus_keyword in H1")
            else:
                issues.append(f"focus_keyword '{kw}' not found in H1")

            first_150 = " ".join(body.split()[:150]).lower()
            if kw in first_150:
                passed.append("focus_keyword in first 150 words")
            else:
                warnings.append(f"focus_keyword '{kw}' not found in first 150 words")

    # Internal links to motadata.com
    internal_links = re.findall(r"\(https://www\.motadata\.com[^\)]+\)", body)
    if len(internal_links) >= MIN_INTERNAL_LINKS:
        passed.append(f"Internal links: {len(internal_links)} found (min {MIN_INTERNAL_LINKS})")
    else:
        issues.append(f"Not enough internal links: found {len(internal_links)}, need {MIN_INTERNAL_LINKS}+")

    # FAQ count
    faq_count = len(re.findall(r"### Q:", body))
    if faq_count >= MIN_FAQ_COUNT:
        passed.append(f"FAQ count: {faq_count} Q&As (min {MIN_FAQ_COUNT})")
    else:
        issues.append(f"Not enough FAQs: {faq_count} found, need {MIN_FAQ_COUNT}+")

    # Forbidden words
    body_lower = body.lower()
    for word in FORBIDDEN_WORDS:
        if word in body_lower:
            issues.append(f"Forbidden word found: '{word}'")

    # Exclamation marks
    exclamation_count = body.count("!")
    if exclamation_count > 0:
        issues.append(f"Exclamation marks found: {exclamation_count} (remove all)")

    # Comparison table
    if re.search(r"^\|.+\|", body, re.MULTILINE):
        passed.append("Comparison table present")
    else:
        warnings.append("No comparison table found — consider adding one if topic supports it")

    total_checks = len(passed) + len(issues)
    score = len(passed) / total_checks * 100 if total_checks > 0 else 0

    return {
        "file": filepath,
        "score": round(score, 1),
        "passed": passed,
        "issues": issues,
        "warnings": warnings,
        "word_count": words if "words" in locals() else "unknown",
    }


def print_report(result: dict):
    """Print a formatted validation report."""
    print(f"\n{'='*60}")
    print(f"Blog Validation Report")
    print(f"File: {result['file']}")
    print(f"Score: {result['score']}% ({len(result['passed'])} checks passed)")
    print(f"Word Count: {result.get('word_count', 'unknown')}")
    print(f"{'='*60}")

    if result.get("error"):
        print(f"\n❌ ERROR: {result['error']}")
        return

    if result["issues"]:
        print(f"\n❌ ISSUES ({len(result['issues'])} — must fix before merging):")
        for issue in result["issues"]:
            print(f"   ❌ {issue}")

    if result["warnings"]:
        print(f"\n⚠️  WARNINGS ({len(result['warnings'])} — recommended fixes):")
        for warning in result["warnings"]:
            print(f"   ⚠️  {warning}")

    if result["passed"]:
        print(f"\n✅ PASSING ({len(result['passed'])}):")
        for p in result["passed"]:
            print(f"   ✅ {p}")

    print(f"\n{'='*60}")
    if result["issues"]:
        print(f"❌ VALIDATION FAILED — fix {len(result['issues'])} issue(s) before submitting PR")
    else:
        print(f"✅ VALIDATION PASSED — ready to submit PR")
    print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_blog.py <blog-file.md or directory>")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isdir(target):
        # Validate all .md files in directory
        files = list(Path(target).glob("*.md"))
        if not files:
            print(f"No .md files found in {target}")
            sys.exit(0)
        for f in files:
            result = validate_blog(str(f))
            print_report(result)
    else:
        result = validate_blog(target)
        print_report(result)
        if result.get("issues"):
            sys.exit(1)


if __name__ == "__main__":
    main()
