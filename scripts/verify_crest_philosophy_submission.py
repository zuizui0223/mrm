from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TARGET = Path("manuscript/crest_philosophy_biology_philosophy.md")
REPORT = Path("artifacts/crest_philosophy_submission_report.json")


def section(text: str, start: str, end: str | None = None) -> str:
    try:
        body = text.split(start, 1)[1]
    except IndexError as exc:
        raise ValueError(f"missing section marker: {start}") from exc
    if end is not None:
        try:
            body = body.split(end, 1)[0]
        except IndexError as exc:
            raise ValueError(f"missing section marker: {end}") from exc
    return body.strip()


def visible_text(markdown: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", markdown, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_>#|]", " ", text)
    text = re.sub(r"^\s*[-+]\s+", " ", text, flags=re.M)
    text = re.sub(r"^\s*\d+[.)]\s+", " ", text, flags=re.M)
    return re.sub(r"\s+", " ", text).strip()


def word_count(markdown: str) -> int:
    # Repository-defined reproducible count. Journal/Word processors may tokenize
    # equations and punctuation differently, so this is a version-controlled gate,
    # not a claim about the publisher's production count.
    text = visible_text(markdown)
    return len(re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()

    text = TARGET.read_text(encoding="utf-8")

    abstract = section(text, "## Abstract", "**Keywords:**")
    keywords_line = section(text, "**Keywords:**", "## 1.").splitlines()[0].strip()
    keywords = [part.strip() for part in keywords_line.split(";") if part.strip()]
    pre_reference = text.split("## References", 1)[0]

    abstract_words = word_count(abstract)
    manuscript_words_before_references = word_count(pre_reference)

    identifying_patterns = {
        "github": r"github(?:\.com)?",
        "owner_handle": r"zuizui0223",
        "email": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "pull_request": r"\b(?:PR|pull request)\s*#?\d+\b",
        "repository_phrase": r"\bour repository\b",
    }
    blind_hits = {
        name: sorted(set(re.findall(pattern, pre_reference, flags=re.I)))
        for name, pattern in identifying_patterns.items()
    }
    blind_hits = {name: hits for name, hits in blind_hits.items() if hits}

    reference_text = section(text, "## References", "## Submission-control note")
    excluded_unpublished = [
        name
        for name in ("Swanson", "Huang", "PhilArchive", "arXiv")
        if re.search(re.escape(name), reference_text, flags=re.I)
    ]

    blockers: list[str] = []
    if not 150 <= abstract_words <= 250:
        blockers.append(f"abstract word count {abstract_words} is outside 150-250")
    if not 4 <= len(keywords) <= 6:
        blockers.append(f"keyword count {len(keywords)} is outside 4-6")
    if manuscript_words_before_references > 10_000:
        blockers.append(
            f"repository word count before references {manuscript_words_before_references} exceeds 10,000"
        )
    if blind_hits:
        blockers.append(f"potential double-blind identifiers found: {sorted(blind_hits)}")
    if excluded_unpublished:
        blockers.append(
            "submission reference list contains unpublished/preprint audit sources: "
            + ", ".join(excluded_unpublished)
        )

    author_controlled = {
        "competing_interests_placeholder": "AUTHOR INPUT REQUIRED BEFORE SUBMISSION" in text,
        "funding_placeholder": text.count("AUTHOR INPUT REQUIRED BEFORE SUBMISSION") >= 2,
        "ai_disclosure_requires_final_human_review": True,
        "title_page_metadata_required": True,
    }

    report = {
        "target": str(TARGET),
        "repository_word_count_definition": "visible markdown tokens before References; publisher count may differ slightly",
        "abstract_words": abstract_words,
        "keyword_count": len(keywords),
        "keywords": keywords,
        "manuscript_words_before_references": manuscript_words_before_references,
        "development_target_5500_7500_met": 5500 <= manuscript_words_before_references <= 7500,
        "hard_cap_10000_met": manuscript_words_before_references <= 10_000,
        "blind_hits": blind_hits,
        "excluded_unpublished_reference_hits": excluded_unpublished,
        "automated_blockers": blockers,
        "author_controlled_blockers": author_controlled,
        "automated_checks_pass": not blockers,
        "submission_ready": False,
        "submission_ready_reason": "author-controlled metadata, final human source/claim/text review, and final policy recheck remain required",
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))

    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
