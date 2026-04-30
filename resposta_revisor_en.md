# Reviewer Response: Dataset Growth Explanation

**Reviewer Comment (or Question):**
*The authors need to clarify why the dataset of test smells grew so significantly (from 907,566 to 1,115,938 occurrences) despite using the exact same set of 4,154 cloned repositories as the original SAST 2025 paper.*

**Authors' Response:**
We sincerely thank the reviewer for highlighting this point. We agree that the significant increase in the number of detected test smells within the same set of repositories requires a clear technical explanation. 

The discrepancy in the dataset size is not due to the addition of new repositories or new types of test smells. Instead, it is the direct result of a major architectural overhaul of our detection tool, DNose. Between the original SAST submission and this extended JSERD version, we heavily refactored the core engine of DNose to address severe underreporting issues caused by the tool's previous technical limitations. The increase in occurrences reflects a much more accurate and exhaustive mining process. The main technical improvements that led to this increase are:

**1. Complete Refactoring to Native AST Traversal (`RecursiveAstVisitor`):**
In the previous version, DNose relied on a manual, ad-hoc loop to traverse the Abstract Syntax Tree (AST) of the Dart files (e.g., iteratively calling `childEntities`). This manual approach was inherently flawed, as it frequently failed to traverse deeply nested syntactic branches or complex structural patterns, causing the tool to silently ignore large portions of the test code. For the JSERD version, we completely rewrote the core of all detectors to natively inherit and implement the `RecursiveAstVisitor` class provided by the official Dart Analyzer. This structural change guarantees a 100% accurate, exhaustive, and recursive traversal of the AST. By properly visiting every single node, statement, and expression, the tool was able to identify over 200,000 occurrences of test smells that were previously "invisible" to the old traversal method.

**2. Robust Concurrent Processing and Fault Tolerance:**
The initial version of the tool processed files sequentially. When it encountered a particularly large, malformed, or highly complex file, the parser could crash or time out, silently aborting the analysis for that specific file or even skipping entire directories to prevent the execution from halting. To solve this, we implemented a highly robust concurrent processing pipeline utilizing semaphores and isolated `try-catch` blocks for every analyzed file. This fault-tolerant architecture ensured that the failure to parse one specific file would no longer impact the extraction pipeline. Consequently, the tool successfully analyzed thousands of files that were inadvertently skipped during the SAST 2025 mining process.

**3. Parser Upgraded to Dart SDK 3.11.0:**
Since the original study, the Dart language and the Flutter framework have evolved significantly. We upgraded DNose’s internal analyzer to be fully compatible with Dart 3.11.0. This allowed the tool to properly generate the AST for repositories that employ modern Dart syntax features (such as pattern matching and records). Previously, encountering unrecognized modern syntax caused the parser to fail, whereas the updated engine successfully processes these files, exposing the test smells within them.

**4. Refinement of Specific Detection Heuristics:**
Finally, we patched false negatives in specific detectors. For instance, the heuristic for the *Unknown Test* smell was corrected so that it no longer confuses mock verification methods (such as Mockito's `verify`) with actual test logic. 

In summary, the 1,115,938 occurrences represent a much more mature, realistic, and complete picture of the test smells present in the original 4,154 repositories. We have added a new subsection in the **Methodology** to explicitly detail this evolution of the detection tool and properly justify the dataset expansion to the readers.

---

# Reviewer Response: Sentiment Analysis and Construct Validity

**Reviewer Comment (or Question):**
*The latent construct of interest (developer frustration or negative perception associated with technical debt) is only weakly and indirectly reflected in the chosen proxy, namely the sentiment polarity in commit messages. This raises several threats to construct validity that are not sufficiently discussed. Commit messages are not designed to capture developers' emotional states. They are typically short, technical, and mostly neutral, and in some cases, automatically generated. Consequently, there is a fundamental inference gap. The analysis does not allow one to determine if the developers were aware of the test smells, if such smells caused frustration, or if the expressed sentiment is actually related to those smells.*

**Authors' Response:**
We deeply appreciate the reviewer's insightful critique regarding construct validity. We fully agree that commit messages are primarily technical artifacts and that assuming strict causality—i.e., that a test smell *directly caused* the negative sentiment expressed in a commit—constitutes an inference gap. 

In this extended version, we have refined our methodology and discussion to align with established literature in Empirical Software Engineering, rather than claiming direct causation. Seminal studies, such as those by Guzman et al. (2014), have demonstrated that commit messages, despite their technical nature, can serve as a valid proxy for extracting developer sentiment and correlating it with software artifacts. More recently, Lin et al. (2018) and Kaur et al. (2022) have explored the limitations of this approach, explicitly questioning how far sentiment analysis can go and discussing the various factors that influence developer emotions. Furthermore, Dey et al. (2025) provide modern guidelines for extracting emotions from commit messages.

Building upon these foundational works, we have significantly reformulated our claims in the manuscript. We now frame our investigation not as a cause-and-effect relationship, but as an observational study of *co-occurrence*. We seek to understand whether the degradation of test code quality (indicated by the presence of test smells) co-occurs with negative emotional polarity during the commit timeframe.

To properly address the reviewer's concern in the manuscript:
1. We expanded Section 6.2 (Sentiment Analysis) to include a theoretical foundation citing Guzman et al. (2014), Lin et al. (2018), Kaur et al. (2022), and Dey et al. (2025), justifying the use of commit messages as an established, albeit imperfect, proxy in software engineering research.
2. We have completely rewritten the Construct Validity subsection in Section 7 (Threats to Validity). We now explicitly acknowledge the "inference gap" pointed out by the reviewer. We state that our analysis measures co-occurrence rather than causality, recognizing that commit messages are often brief or auto-generated, and that negative sentiment can be multi-causal. By limiting our claims, we believe the sentiment analysis is now methodologically sound and firmly connected to the rest of the study.
