Dear Tássio Virgínio, Márcio Ribeiro, Ivan Machado,

\n

A decision has been made regarding your paper "More than one million test smells: how are Dart projects and their sentiments?", submitted to the Journal of Software Engineering Research and Development.

\n

The decision is: Resubmit for Review

\n

The revised version of the paper must be submitted by May 24, 2026.

\n

The reviewers found the extended manuscript relevant and improved, but request revisions in two main areas. First, the authors should clarify the dataset/tool changes that led to the increased number of detected test smells despite the use of the same repositories. Second, they should strengthen or reframe the sentiment analysis, better justifying the link between test smells and commit-message sentiment and explicitly discussing related construct-validity threats.

\n

The reviewers’ comments are attached below.  When preparing the revised version of your paper, please consider them carefully. In addition to the revised version of your paper, you MUST submit an answer letter providing responses to the reviewers’ questions and indicating the changes made in the paper to address the reviewers’ comments. In the revised version of your paper, you MUST highlight the changes by using a different font color (e.g., blue or red).

\n

Best regards, 

\n

Rohit

\n

Editor - Journal of Software Engineering Research and Development



------------------------------------------------------
Reviewer A:

This paper is an extended version of a work previously presented at the 10th Brazilian Symposium on Systematic and Automated Software Testing (SAST 2025).

The main goal of the study is to evaluate the quality of test code in Dart-based projects by analyzing test smells identified in test suites. To this end, the authors developed the DNose tool, designed to detect test smells in the Dart language. The paper then presents an evaluation of the tool’s accuracy, followed by a large-scale analysis of test smells in open-source Dart projects. Finally, the study investigates the relationship between the presence of test smells and developers’ sentiments.

Compared to the initial version, this extended paper introduces relevant contributions, including: (i) the addition of 208,372 new occurrences of test smells, and (ii) the incorporation of sentiment analysis based on commit messages.

Overall, the paper is well written and easy to follow. The extended version represents a clear improvement over the previous one, particularly due to a more structured introduction and better-defined experimental design.

However, the paper would benefit from minor revisions to address the following points:

1) Both versions of the paper rely on the same dataset, comprising 5,410 open-source projects and 4,154 clones. Why, then, does the number of detected test smells differ between the original and extended versions? Has the DNose tool been updated or modified? This should be clarified.

2) The study is based on the hypothesis that the presence of test smells leads to developer frustration, reflected as negative sentiment in commit messages. However, developers are typically unaware that they are introducing test smells. Given this, it is unclear how the sentiment expressed at commit time can be directly associated with the introduction of test smells. The authors should further justify or clarify this assumption.

Recommendation: Revisions Required

------------------------------------------------------



------------------------------------------------------
Reviewer B:

This expanded version of the paper presents a threefold study: (i) an empirical evaluation of a tool designed to identify test smells in Dart test code, (ii) a large-scale empirical investigation aimed at assessing the overall quality of test code in Dart projects, and (iii) what the authors describe as an analysis of the relationship between developers’ sentiments and the identified test smells. Within this context, the presence and distribution of test smells are used as primary proxies for test code quality. The study is based on the analysis of 4,154 repositories (after filtering), yielding a dataset comprising more than one million occurrences of test smells. The results indicate that test smells are present in the vast majority of analyzed test files, highlighting their widespread prevalence in the ecosystem.

One of the main strengths of the paper lies in its well-structured research design, which combines tool development, validation, and large-scale empirical analysis. Although not strongly emphasized, the introduction of the DNose tool for detecting test smells in Dart represents a meaningful contribution, particularly given the limited tooling support available for this ecosystem. Moreover, the tool’s accuracy is evaluated through an empirical study involving manual validation by multiple developers with varying levels of experience, which strengthens confidence in the reliability of the reported results.

That said, the description of the dataset expansion in the extended version remains insufficiently detailed. The earlier version of the paper reports approximately 907,566 instances of test smells, whereas the current version reports 1,115,938 occurrences—an increase of roughly 23%. However, both versions appear to rely on the same set of 4,154 cloned repositories (derived from 5,410 Dart projects). It is therefore unclear how this increase was achieved. The manuscript does not explicitly state whether the expansion results from a "deeper" mining strategy (e.g., analyzing additional commits or historical revisions), changes to the detection pipeline (e.g., new or "relaxed" heuristics), or other modifications in the data extraction process.
I believe that clarifying this point is important to assess the comparability between versions (and to ensure the reproducibility of the study). The authors are encouraged to provide a more detailed account of the steps leading to the expanded dataset.

My main concern with the extended version relates to the analysis of the relationship between developers’ sentiments and test smells.
The latent construct of interest (developer frustration or negative perception associated with technical debt) is only weakly and indirectly reflected in the chosen proxy, namely sentiment polarity in commit messages.
This raises several threats to construct validity that are not sufficiently discussed (in the threats to validity section). Commit messages are not designed to capture developers’ emotional states. Rather, they are typically used to document code changes. As such, they tend to be short, technical, and mostly neutral, often following standardized templates (e.g., “fix bug”, “refactor test”, “update config”), and in some cases are automatically generated (e.g., merge commits or CI/CD operations). Even when sentiment is present, it is rarely attributable to a single, well-defined cause.
Consequently, there is a fundamental inference gap in the experimental design. The analysis does not allow one to determine whether developers were aware of the presence of test smells, whether such smells caused any form of frustration, or whether the expressed sentiment (if any) is actually related to those smells. This introduces unobserved confounding factors and limits the interpretability of the results. In my opinion, the sentiment analysis part appears methodologically disconnected from the rest of the study.

Overall, setting aside the sentiment analysis part, which in my view feels somewhat misplaced, the paper presents a relevant and methodologically sound contribution. It successfully combines tool development, validation, and large-scale empirical evaluation, and the results are likely to be of interest to the journal’s audience. Additionally, the overall presentation has improved compared to the earlier version.

Recommendation: Accept Submission

------------------------------------------------------




________________________________________________________________________
Journal of Software Engineering Research and Development