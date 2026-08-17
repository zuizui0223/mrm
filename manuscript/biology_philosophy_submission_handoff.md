# Biology & Philosophy submission handoff — CREST philosophy paper

> **Target:** Biology & Philosophy — Original Research
>
> **Status:** scientific/automated submission gates are complete on the current main. Actual submission remains blocked by author-controlled metadata, final human responsibility review, and current-policy recheck.

## A. Review-manuscript front matter

### Title

**What Counts as the Same Ecological State? A Contract-Relative Account of State-Representation Adequacy**

### Abstract

Repository verifier count: **227 words**.

Ecology routinely compresses heterogeneous configurations into shared states used for prediction, comparison, and management. Existing work already provides mature accounts of ecosystem identity, ecological model adequacy, intervention-sensitive states, predictive state abstraction, partial observability, causal abstraction, and purpose-sensitive scientific representation. We ask a narrower question: when several ecological configurations are assigned the same coarse state, what scientific commitments are being made by that equivalence? We distinguish four adequacy questions in the current program: whether the equivalence remains sufficient under declared future operations, preserves inherited meaning after structural change, supports prediction across retained mechanism alternatives, and is licensed by the available evidence. These questions are anchored respectively by an open-future interface lower bound, a unique coarsest source-relative repair, mechanism-safe deterministic/typed/set-valued reporting, and an evidence-relative reportability criterion with a required target-safe refinement. The same coarse state can therefore fail for different reasons, and the appropriate response differs: retain additional predictive information, repair inherited semantics, preserve or resolve mechanism ambiguity, or withhold a distinction that the evidence has not earned. Contract-relative adequacy is not unrestricted relativism: once a scientific contract is declared, proposed state merges can be tested and can fail for explicit formal reasons. We present CREST as a theorem-grounded synthesis for making ecological state-equivalence commitments explicit; no claim is made that these four audits are exhaustive, commuting, jointly minimal, or the first general theory of representational adequacy.

### Keywords — 6

**philosophy of ecology; ecological state; scientific representation; model adequacy; causal abstraction; uncertainty**

## B. Current automated manuscript status

The reproducible verifier is:

```bash
python scripts/verify_crest_philosophy_submission.py --write-report
```

Current verified state:

- abstract: **227 words**;
- keywords: **6**;
- repository-defined manuscript words before References: **4,955**;
- hard cap `<=10,000`: **PASS**;
- potential double-blind identifiers before References: **0**;
- excluded unpublished/preprint audit references in submission reference list: **0**;
- automated blockers: **0**;
- full MRM theorem tests: **PASS**;
- deterministic theorem replay: **PASS**;
- claim-ledger reverse audit: **PASS**;
- expanded-section citation-to-claim audit: **PASS**;
- automated blind scrub: **PASS**.

`4,955` is the exact repository-defined visible-Markdown count, not a claim about the publisher's own word processor. It is below the earlier internal 5,500–7,500 development band but is not treated as a scientific blocker. `雅` takes precedence over padding the article with redundant theory, examples, or references.

## C. Use of generative AI — PROPOSED WORDING ONLY

> OpenAI ChatGPT was used during manuscript development to assist with literature triage, organization of claim and citation audits, and drafting and revision of portions of the text. All cited sources, mathematical claims, interpretations, and final wording were reviewed by the human author(s), who take responsibility for the manuscript.

**AUTHOR FINAL REVIEW REQUIRED BEFORE THIS WORDING MAY BE USED.**

The second sentence describes a submission-state responsibility that must actually be true at submission. Until the human author(s) complete that review, this remains proposed wording rather than an accomplished declaration.

Before submission:

1. recheck the current journal / publisher AI policy;
2. human-review every cited source relied on by the manuscript;
3. human-review mathematical claims against the proof ledger;
4. human-review interpretations and final prose;
5. approve the complete manuscript;
6. only then promote the disclosure above to final submission text.

## D. Author-controlled declarations

### Competing Interests

**AUTHOR INPUT REQUIRED.**

Do not infer a no-conflict statement.

### Funding

**AUTHOR INPUT REQUIRED.**

Do not infer funding status from repository history or unrelated projects.

### Data availability

The manuscript is conceptual/theoretical and introduces no empirical dataset. Final wording should be checked against the submission system at submission time.

## E. Separate title page — author-controlled fields

Do **not** place these items in the blinded review manuscript.

- Title: *What Counts as the Same Ecological State? A Contract-Relative Account of State-Representation Adequacy*
- Author name(s): **AUTHOR INPUT REQUIRED**
- Affiliation(s): **AUTHOR INPUT REQUIRED**
- Corresponding author: **AUTHOR INPUT REQUIRED**
- Corresponding-author email: **AUTHOR INPUT REQUIRED**
- ORCID(s): **AUTHOR INPUT REQUIRED / if used**
- Acknowledgements: **AUTHOR INPUT REQUIRED**
- Funding information: **AUTHOR INPUT REQUIRED**
- Competing interests / disclosures: **AUTHOR INPUT REQUIRED**

## F. Double-blind finalization

Automated pre-reference scanning is clean. Before actual upload, the final review file must additionally remove development-only material after the references, including:

- `Submission-control note`;
- author-input placeholders;
- any proposed disclosure marker that has not yet been finalized.

Then perform one final human read-through for identifying prose and self-citation voice.

## G. Reference-list boundary

The current Biology & Philosophy target version excludes the two unpublished/preprint-only novelty-audit sources:

- Swanson (2026), PhilArchive manuscript;
- Huang (2026), arXiv preprint.

They remain in internal novelty/literature audits, so their removal from the submission bibliography does **not** raise CREST's priority claim.

## H. Remaining blockers

### Scientific / automated

**None known.**

Any further manuscript expansion is optional and must add philosophical substance rather than word count alone.

### Author-controlled / final human

Required before submission:

- author list;
- affiliation(s);
- corresponding-author details;
- ORCID(s), if used;
- acknowledgements;
- funding statement;
- competing-interest statement;
- full human source/claim/interpretation/text review;
- final AI-disclosure approval;
- final double-blind cleanup of development-only controls;
- final visual/read-through approval;
- current journal-policy recheck immediately before submission.

## I. Fallback routing

If Biology & Philosophy rejects primarily on fit/article type rather than the substantive argument:

1. retarget to **Philosophy, Theory, and Practice in Biology**;
2. preserve the theorem-grounded, priority-robust synthesis;
3. recheck PTPBio's current submission rules before conversion;
4. do not broaden CREST into a general philosophy-of-science grand theory merely to chase a venue.

## Current verdict

**The repository-controlled scientific manuscript is clean enough to hand over for final human authorship review. No further theorem development or automated manuscript repair is currently justified.**


## G2. CREST-O1 integration status — 2026-08-18

Completed repository-controlled work:

- one O1 diagnostic paragraph integrated into the Biology & Philosophy manuscript;
- no new theorem section, acronym family, external citation, or priority claim;
- C37–C40 added to the claim ledger;
- theorem suite and submission verifier passed after integration.

Verifier report:

```json
{
  "abstract_words": 227,
  "author_controlled_blockers": {
    "ai_disclosure_requires_final_human_review": true,
    "competing_interests_placeholder": true,
    "funding_placeholder": true,
    "title_page_metadata_required": true
  },
  "automated_blockers": [],
  "automated_checks_pass": true,
  "blind_hits": {},
  "development_target_5500_7500_met": false,
  "excluded_unpublished_reference_hits": [],
  "hard_cap_10000_met": true,
  "keyword_count": 6,
  "keywords": [
    "philosophy of ecology",
    "ecological state",
    "scientific representation",
    "model adequacy",
    "causal abstraction",
    "uncertainty"
  ],
  "manuscript_words_before_references": 5094,
  "repository_word_count_definition": "visible markdown tokens before References; publisher count may differ slightly",
  "submission_ready": false,
  "submission_ready_reason": "author-controlled metadata, final human source/claim/text review, and final policy recheck remain required",
  "target": "manuscript/crest_philosophy_biology_philosophy.md"
}
```

Remaining blockers are author-controlled: final human source/claim/text review, author and affiliation metadata, funding, competing interests, acknowledgements, final AI-disclosure approval, policy recheck, and visual read-through.
