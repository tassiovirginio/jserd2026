# Answer Letter

**Manuscript:** "More than one million test smells: how are Dart projects and their sentiments?"
**Authors:** Tássio Virgínio, Márcio Ribeiro, Ivan Machado
**Journal:** Journal of Software Engineering Research and Development (JSERD)
**Decision:** Resubmit for Review

---

Dear Editor and Reviewers,

We sincerely thank the editor and the reviewers for the careful and constructive evaluation of our manuscript. The feedback has been invaluable in strengthening both the clarity and the methodological rigor of our study. Below, we provide a point-by-point response to each reviewer's comments. All changes in the revised manuscript are highlighted in **blue**.

---

## Reviewer A

### Summary

We thank Reviewer A for the positive assessment of the manuscript's writing quality and structure, and for recognizing the contributions of the extended version.

---

### Comment A1 — Dataset Growth Clarification

> *"Both versions of the paper rely on the same dataset, comprising 5,410 open-source projects and 4,154 clones. Why, then, does the number of detected test smells differ between the original and extended versions? Was the DNose tool updated or modified? This should be clarified."*

**Response:**

Yes, the DNose tool was substantially updated. The discrepancy in the dataset size is not due to the addition of new repositories or new types of test smells. Instead, it is the direct result of a major architectural overhaul in DNose to address severe underreporting caused by previous technical limitations. The main improvements are:

1. **Complete Refactoring for Native AST Traversal (`RecursiveAstVisitor`):** The previous version relied on a manual, ad-hoc loop to traverse the Abstract Syntax Tree (AST), which frequently failed on deeply nested structures. The core of all detectors was completely rewritten to natively inherit the `RecursiveAstVisitor` from the official Dart Analyzer, ensuring exhaustive traversal.

2. **Robust Concurrent Processing and Fault Tolerance:** We implemented a highly robust concurrent processing pipeline using semaphores and isolated `try-catch` blocks. This ensured that parser failures on individual files no longer silently aborted the analysis of entire directories.

3. **Parser Upgrade to Dart SDK 3.11.0:** The internal analyzer was upgraded to be fully compatible with modern Dart syntax features (such as pattern matching and records), which previously caused parser failures.

4. **Refinement of Specific Detection Heuristics:** We corrected false negatives in specific detectors (e.g., the *Unknown Test* heuristic no longer confuses mock verification methods with actual test logic).

**Changes in the manuscript:** Section 4.2 (Design) — A new paragraph (highlighted in blue) details the architectural evolution of DNose and justifies the dataset expansion.

---

### Comment A2 — Sentiment and Test Smell Association

> *"The study is based on the hypothesis that the presence of test smells leads to developer frustration, reflected as negative sentiment in commit messages. However, developers typically are not aware that they are introducing test smells. Given this, it is not clear how the sentiment expressed at the time of commit can be directly associated with the introduction of test smells. The authors should further justify or clarify this assumption."*

**Response:**

We fully agree with the reviewer that developers are typically unaware of the test smells they introduce, and that assuming a direct causal link between a test smell and the expressed sentiment constitutes an inference gap. We have addressed this concern comprehensively in the revised manuscript:

1. **Elimination of Causal Claims:** We reformulated all claims to frame our investigation strictly as an observational study of **co-occurrence**, not cause-and-effect. We do not assert that developers were aware of the test smells or that the smells directly caused frustration. Instead, we propose that the development context that fosters the introduction of test smells (e.g., tight deadlines, accumulated technical debt, high complexity) is the same context that often manifests as negative polarity in commit messages.

2. **Revised Research Questions:** The wording of RQ5 was changed from *"How do different types of test smells impact..."* to *"What is the exploratory relationship between the occurrence of different test smells and the overall sentiment score..."* — removing language that suggested causality.

3. **Exploratory Framing:** We explicitly acknowledge that our sentiment extraction relies on an exploratory methodology. While recent studies propose using domain-specific pre-trained Language Models to accurately identify emotions in software artifacts (Dey et al., 2025), our approach serves as an initial exploratory step to establish baseline data regarding the co-occurrence of test smells and sentiments in Dart.

**Changes in the manuscript:**
- Section 4.1 (Research Questions): RQ5 and RQ6 reformulated (highlighted in blue).
- Section 6.2 (Sentiment Analysis): Introductory paragraph expanded with literature grounding (highlighted in blue).
- Section 7 (Threats to Validity), Construct Validity: Explicitly acknowledges the inference gap and restricts claims to co-occurrence (highlighted in blue). A new paragraph citing Dey et al. (2025) recognizes the exploratory nature of the methodology (highlighted in blue).

---

## Reviewer B

### Summary

We sincerely thank Reviewer B for the thorough and insightful evaluation, for recognizing the DNose tool as a significant contribution to the Dart ecosystem, and for the positive assessment of the research design, validation methodology, and overall presentation improvements. We address each concern below.

---

### Comment B1 — Dataset Expansion Details

> *"The description of the dataset expansion in the extended version remains insufficiently detailed. [...] The manuscript does not explicitly state whether the expansion results from a 'deeper' mining strategy (e.g., analyzing additional commits or historical revisions), changes in the detection pipeline (e.g., new or 'relaxed' heuristics), or other modifications in the data extraction process."*

**Response:**

We appreciate this precise framing of the possible hypotheses. The expansion results exclusively from changes in the **detection pipeline**, not from deeper mining or relaxed heuristics. Specifically:

- **Not a deeper mining strategy:** Both versions analyze the same snapshot of the same 4,154 repositories. No additional commits or historical revisions were analyzed.
- **Not relaxed heuristics:** The detection thresholds and definitions for all 14 test smell types remain identical. We did not lower any bar for detection.
- **Changes in the detection pipeline:** The DNose tool underwent a major architectural overhaul between versions, including: (1) complete refactoring of all detectors to use native `RecursiveAstVisitor` for exhaustive AST traversal, (2) implementation of a fault-tolerant concurrent processing pipeline using semaphores, (3) upgrade to Dart SDK 3.11.0 for modern syntax compatibility, and (4) correction of false negatives in specific heuristics (e.g., *Unknown Test* detector). These improvements resolved severe underreporting, yielding a 23% increase in detected occurrences from the same codebase.

We believe this clarification directly addresses the comparability and reproducibility concerns raised by the reviewer.

**Changes in the manuscript:** Section 4.2 (Design) — A new paragraph (highlighted in blue) provides a detailed account of the pipeline changes that led to the expanded dataset.

---

### Comment B2 — Construct Validity and Inference Gap

> *"The latent construct of interest (developer frustration or negative perception associated with technical debt) is only weakly and indirectly reflected in the chosen proxy [...] There is a fundamental inference gap in the experimental design. [...] The sentiment analysis part appears methodologically disconnected from the rest of the study."*

**Response:**

We deeply appreciate this critical observation, which we consider the most important feedback for improving the manuscript. The reviewer is correct that the previous version did not sufficiently articulate the structural connection between the technical analysis (RQ1–RQ4) and the sentiment analysis (RQ5–RQ6). We have addressed this in three complementary ways:

**1. Narrative Bridge — Connecting the Two Dimensions of the Study:**

We added an explicit transitional paragraph at the end of Section 6.1 (after the co-occurrence analysis) that articulates *why* the sentiment analysis belongs structurally in this paper:

- RQ1–RQ4 establish the **technical landscape** of test smells: distribution, frequency, and co-occurrence patterns.
- However, test smells are not merely static code artifacts — they are introduced, tolerated, and accumulated by developers working under real-world conditions. Prior research has shown that developer affect and code quality are intertwined (Guzman et al., 2014; Lin et al., 2018).
- Therefore, RQ5–RQ6 extend the investigation to the **human dimension of technical debt**, providing a complementary, human-centered lens to the technical findings.

This paragraph makes the structural connection explicit and transforms the sentiment analysis from an appendage into a natural extension of the study.

**2. Co-occurrence Framing — Eliminating Causal Claims:**

We reformulated all claims to eliminate any suggestion of causality. The revised manuscript frames the sentiment analysis strictly as an observational study of co-occurrence. The Research Questions themselves were revised:
- **RQ5 (revised):** *"What is the exploratory relationship between the occurrence of different test smells and the overall sentiment score in the analyzed projects?"*
- **RQ6 (revised):** Description adjusted to emphasize co-occurrence rather than direct association.

We do not assert that developers were aware of the test smells or that the smells caused frustration. Instead, we observe that the degradation of test code quality co-occurs with negative sentiment at the moment of the commit, possibly driven by shared underlying factors such as high complexity or schedule pressure.

**3. Exploratory Nature and Future Work with Advanced Models:**

We explicitly acknowledge that our sentiment extraction methodology is **exploratory** and represents an initial baseline. Recent studies, such as Dey et al. (2025), propose using domain-specific pre-trained Language Models (LLMs) to accurately identify emotions in software artifacts. While our work does not employ these advanced techniques, it establishes the initial data regarding the co-occurrence of test smells and sentiments in the Dart/Flutter ecosystem, serving as a foundation for future studies applying these more sophisticated models.

**Changes in the manuscript:**

| Change | Location | Highlight |
|---|---|---|
| Transitional paragraph connecting technical analysis (RQ1–RQ4) to sentiment analysis (RQ5–RQ6) | Section 6.1, end of co-occurrence subsection | Blue |
| Reformulation of Research Questions RQ5 and RQ6 with exploratory tone | Section 4.1 (Research Questions) | Blue |
| Literature grounding and acknowledgment of technical nature of commit messages | Section 6.2 (Sentiment Analysis), introductory paragraph | Blue |
| Explicit acknowledgment of inference gap and restriction to co-occurrence | Section 7 (Threats to Validity), Construct Validity | Blue |
| Acknowledgment of exploratory nature and citation of Dey et al. (2025) as future work | Section 7 (Threats to Validity), new paragraph | Blue |

---

## Summary of All Changes

| Section | Change | Motivated by |
|---|---|---|
| 4.1 — Research Questions | RQ5 and RQ6 reformulated to exploratory/co-occurrence framing | A2, B2 |
| 4.2 — Design | New paragraph detailing DNose architectural evolution | A1, B1 |
| 6.1 — Analysis and Discussion | Transitional paragraph bridging technical and sentiment analyses | B2 |
| 6.2 — Sentiment Analysis | Expanded introduction with literature grounding | A2, B2 |
| 7 — Threats to Validity | Construct Validity expanded: inference gap, co-occurrence framing, exploratory acknowledgment with Dey et al. (2025) | A2, B2 |

All changes are highlighted in **blue** in the revised manuscript.

We believe these revisions comprehensively address all concerns raised by both reviewers. We are grateful for the opportunity to improve our work and remain available for any further clarifications.

Sincerely,
Tássio Virgínio, Márcio Ribeiro, Ivan Machado
