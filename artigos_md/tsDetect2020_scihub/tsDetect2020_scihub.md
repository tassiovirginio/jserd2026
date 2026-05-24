<!-- Página 1 -->

### tsDetect: An

### Open

### Source

### Test

### Smells

### Detection

### Tool

### Anthony Peruma

### Khalid Almalki

### Christian D. Newman

[axp6201@rit.edu](mailto:axp6201@rit.edu)[ksa8566@rit.edu](mailto:ksa8566@rit.edu)[cnewman@se.rit.edu](mailto:cnewman@se.rit.edu) Rochester Institute of Technologyofof Rochester, New York, USANewUSANewUSA

### Mohamed Wiem Mkaouer

### Ali Ouni

### Fabio Palomba

[mwmvse@rit.edu](mailto:mwmvse@rit.edu)[ali.ouni@etsmtl.ca](mailto:ali.ouni@etsmtl.ca)[fpalomba@unisa.it](mailto:fpalomba@unisa.it) Rochester Institute of TechnologyETS Montreal, University of QuebecSeSa Lab -of Salerno Rochester, New York, USAMontreal, Quebec, CanadaFisciano (SA), Italy

of the widely-acknowledged techniques that are of paramount im-**ABSTRACT** portance for quality assurance. There are different types of testingThe test code, just like productionsourceis subjectto bad strategies that can be adoptedto test a softwaresystem,such asdesign and programming practices, also known as smells. The pres- unit testing []. Unitinvolves developersthe small-ence of test smells in a software project may affect the quality, main- est unit in the productioncodebase, which is typically a method.tainability, and extendability of test suites making them less effec- Hence,this process requires developers writing test code to exercisetive in finding potential faults and quality issues in the project’s pro- production code.duction code. In this paper, we introducetsDetect,an automated Even though the unit test code will not be executed in produc-test smell detection tool for Java software systems that uses a set of tion, it is essential that developers follow standard programmingdetectionrules to locate existing test smells in test code. We evaluate practiceswhen implementing a test suite. This practice ensures thatthe effectiveness oftsDetecton a benchmark of 65 unit test files the production code is effectively exercised and enables developerscontaininginstances of 19 test smell types. Results show that to easily identify defects in the system. Similar to traditional codetectachievesa high detection accuracy with an average precision smells, i.e., bad programming practices, unit tests may also sufferscore of 96% and an average recallof 97%.is pub- from smells that are exclusive to the testing domain16 ].[licly available, with a demo video, at: [https://testsmells.github.io/](https://testsmells.github.io/) more, just like how traditionalcode smellscause a systemto be more prone to changes and defects20[ it has been shown that test**CCS CONCEPTS** smells may negatively impact the quality of the system [30]. •**Software and**itsengineering→testingandde- Therefore, there is a growing need to incorporatethe verifica- **bugging;Software notations and tools**;maintenance. tion of bad testing practices into modern code reviews. While there exist open-source quality assurance tools, such as PMD3 ], Check- **KEYWORDS**style [1], and FindBugs [], which primarily focus on detecting a Software Quality, Test Smells, Detection Toolvariety of quality issues in production code, the number of open- source tools that detect a wide variety of test smells and supports **ACM** integration with continuousframeworks is limited.Anthony This paper introducestsDetect, an open-source tool that cur-Mkaouer, Ali Ouni, and Fabio Palomba. 2020.tsDetect:An Open Source rently supports the detection of 19 common test smells,i.e. , devia-Test Smells Detection Tool. InProceedings of the 28th ACM Joint European tions from good unit testing programming practices, as advocatedSoftware ware Engineering (ESEC/FSE ’20), November 8–13, 2020, Virtual Event, USA.in xUnit guidelines [, 17 ]. These 19 smells are part of the catalog ACM,of unit test smells, and details about their definitions, rationale, and examples appear in published literature22[]. tsDetect takes, as input, software project source code and first separates the set of unit**1 INTRODUCTION** test files from production source files, then generates their Abstract Quality assurance is a crucial driver in any software project, and Syntax Trees (ASTs) in order to search for any predefined patterns the success of the project depends on the quality aspects it exhibits, of bad test programmingpracticessyntacticallyusingdetection meaningwe need to optimize these aspects. Software testing is one rules.tsDetectgenerates, as output, a file containing all detected violations. tsDetect has been designed to be easy to extend,i.e. , Permissiondevelopers can easily calibrate the predefined rules and add their classroom own customizedrulesif needed.Moreover, althoughtsDetectfor oncurrently detects 19 test smells, it is designed with a high level of must flexibility to incorporate new smell types easily, and also permitsto the customizationof the existing smell detectionrules as shownfee. ESEC/FSElater in Section 3 , where we discuss the architecture of the tool. © 2020Toevaluate the correctness oftsDetect,we performed a qual- ACM itative analysison a benchmarkof 65 unit test files that contain[https://doi.org/10.1145/3368089.3417921](https://doi.org/10.1145/3368089.3417921)

1650


---

<!-- Página 2 -->

ESEC/FSE

instancesfrom various smell types. Analysis of our tool has shown we provide the community with a tool that can be integrated into that tsDetectis able to correctly detect test smells with a precisionthe development workflow to automate the identification of bad unit score ranging from 85% to 100% and a recallfrom 90% to 100%testing practices early during the system’s development lifecycle. with an average F-score of 96.5%. **3****TSDETECTARCHITECTURE**Furthermore,we have utilizedtsDetectto perform a large-scale empiricalstudy on open-source Android applications (apps) and tra-tsDetectis implemented as an open-source, command line-based ditional Java systems []. Our study investigated the occurrencestool that is availableas a standaloneJavajar file. By providing and distribution of the 19 test smells on 656 open-source AndroidtsDetectas a self-contained executable file rather than a plugin apps, including a comparison of smell type occurrence with tradi-(whichis part of our future work), users are not required to have a tional Java systems.In a subsequentstudy26[ we explored thespecific IntegratedDevelopmentEnvironment(IDE) installed on impact and relationshipbetweenrefactoringoperationsand testtheir machine in order to detect smells intest code. Similar to smells, detected bytsDetect, in 250 open-source Android apps.other code smell and defect detection tools such as PMD and Find- **Open source**toolanddocumentation.ThetsDetectBugs, offering tsDetect as an executable through the command project’s website[4 ] includesthetoolsourcecode,alongwithline facilitates its integration with modern continuous a demonstrationvideo and documentationon how to use it. Theframeworks,as well as its adoption in mining software repositories website also contains examples and general information about testand empirical studies in software engineering. smells. Additionally,tsDetecthas receivedincreasinginterestIn additiontothetsDetectdetection mechanism,weincor- on GitHubfromthedevelopmentandresearchcommunitiesinporate supplementarymodulesto automatethe entire detection the form of forks and feedbackon how to improve our tool andworkflow.These modules support the detection process by parsing make it more practical. We encourage the community to contributethe input source files to detect unit test(and their correspond- improvements and extensions totsDetect.ing production files) in the project hierarchy. A high-level overview of the architecture oftsDetectis depicted in Figure 1.Inand②, **2 BACKGROUND**AND MOTIVATION the test and production files are identified from the project structure. Testsmells represent deviations from well-established testing prac-In ③and④,tsDetectchecks if the test files exhibits test smells. In tices andguidelinesonhowtestcasesshouldbedesigned,im-⑤ , the results from the test smell detection process are saved. In the plemented, andhowtheyshouldinteractwitheachother.Thefollowingsubsections, we describe the detector and the mechanism detectionof such potential deviations is typically a tedious, manual,to distinguish test files and their corresponding production files. and error-prone task for developers and testers. Effective detection of test smells requires expertise from developers to inspect, under- stand, and run the test to be able to correctly detect the violations. The goal of implementingtsDetectis to provide developers with an automated approach for optimizing the quality of their test suites. tsDetecthas the ability to detect 19 smells occurringin JUnit based unit test files, some of which have been highlighted in existing literature as being problematic9[ 17 , 30, 32]. The list of detected smells supported bytsDetectis reported in Table 1 along with their definitions/detection rules. In summary,tsDetectana- lyzes the test suite for the existence of certain violations to xUnit testing guidelines [, 17 ]. Even though all test smells detected by the tool apply to any Java-based system, one smell, namely Default **Figure 1: High-level architecture of****tsDetect**Test,is specific to Android applications. For the sake of space limi- tations, we provide the necessary background information about **4 TEST**SMELL DETECTIONthe smells supportedbytsDetectin our prior study22[ ]. Addi- tionally,our project’s website4[ contains examples of real-worldWefollowed a strategy design pattern in implementing the detection code snippets that exhibit each of the supported smell types.mechanismfor test smells (UML class diagrams are available on the The detected test smells bytsDetectprovidesvaluable supportprojectwebsite). Each smell is implemented and runs independently for developers. Our prior work22[] has shown the prevalence ofof other smells. The detectionstrategy of each smell type is self-

### TS

## DETECT

these smellsin open-sourcesystems,indicatingthe difficultyofcontained within its own module. This design pattern also enables

## CSV

## 2

## 3

developers to remove them from the codebase during the lifetimethe seamless addition of new smell detectors in the future. Internally,

# Assertion

## Path to unit

# Eager Test

# Empty Test

## test files

## Test File

# Roulette

of the project.Furthermore,in our previousqualitativeanalysistsDetectcalls the JavaParser [] library to parse the source code

## Detection

[ 22 ] in which we reached out to developers whose test files exhibitfiles. JavaParser builds an AST from the unit test file that is under

# Redundant

# Lazy Test

# ...

## 1

## 4

a test smell detected bytsDetect, most of the surveyed developersanalysis. The AST is then analyzed by each of the available

# Print

## JAVA

confirmed that the test files identifiedbydid containdetection modules based on therules defined in Table 1 .

## Project

## Production

# Test Smell Detector Modules

## source code

instances of bad unit testing programming practices. Additionally,Depending on the type of smell beingdetected,we overridethe

## File

## Detection

based on the outputof our tool,5some of these developersmade appropriatevisit()method to perform the detection. For example,

# JavaParser

necessarycorrections to their code based on the findings. Hence, toin the case of detecting theRedundantPrint smell, we first create a

## CSV

ensurethat unit tests aretsDetectof high-quality and maintenance-friendly,MethodDeclarationvisitor to identify all test methods in the class.

## results

1651


---

<!-- Página 3 -->

**Test**

Assertion Conditional Constructor Default Duplicate Eager Empty Exception GeneralsetUpmethod Ignored@Ignoretheannotation Lazy Magic Mystery Redundantor printlnor printfor writemethodSystemclass Redundant Resourceclassexists(), isFile()or notExists()methods SensitivetoString()method SleepyThread.sleep()method Unknown@Test(expected)annotation

tsDetect:An

## Table 1: Summary of the test smell detection rules built-in

## tsDetect

## Next, for each detected test method, we create

## MethodCallExpr

## a

## 5

## TSDETECTAPPLICABILITY

## visitor to examine the methods being called within the test method.

## developers

## integrating

## tsDetect

## Practitioners.We envision

## Finally,

## for each called method, we check if the name of the method

## into their development toolset and workflow. For example, by in-

## matches a Java print method to determine if the file is smelly.

## tegrating it into their build process, developers will be notified of

## On completion,

## the results are saved into a Comma-Separated

## smells in their test code before either committing the file into the

## Values

## (CSV) file. For each smell type,

## tsDetectoutputs

## a boolean

## repository or generating a production release. Furthermore, in our

## value indicating if the smell is present or not in the file. We decided

## previous work [

## ], we reported smells detected by

## tsDetectto

## on a CSV format for output as this

## is technology independent

## 120 developers,

## from various

## open-source

## systems.

## We received

## and permits users to import the data into a database system of their

## responses from 50 developers,

## with most developers

## confirming

## choice for ease of analysis.

## that the programming constructs we highlighted in their code are

## Test

## File Detection.JUnit recommends that developers follow

## indeed examples of test smells, and that they will take corrective

## the naming convention [

## ] of either pre-pending or appending the

## actions to fix them.

## word ‘Test’ to the name of the production

## file that is to be tested

## tsDe-

## Researchers.With the capability of batch-based analysis,

## ( i.e. , Test*.java and *Test.java). Our tool first identifies all ‘.java’ files

## tectcan be used by researchers in empirical studies on software

## where the filename either starts or ends with the word ‘test’. Next,

## quality and maintenance.

## As previously

## stated,

## we have utilized

## for each of the identified Java source files, the tool parses its AST

## tsDetect

## in empirical

## studies

## of

## open-source

## systems

## 22

## [

## 26 ].

## using JavaParser. The purpose of

## the AST is twofold. First,

## Additionally,tsDetecthas also been utilized by the research com-

## we are able to eliminate Java files that contain syntax errors, and

## munity

## in the study of test smells. Schvarcbacher et

## 29

## al.

## ] integrate

## [

## secondly,

## we are able to accurately detect if the file contained JUnit-

## tsDetectinto a code quality monitoring system to study reactions

## based unit test methods. For a file to contain a unit test method, the

## to test smells.

## Spadini

## et al.

## 31

## [ use

## tsDetect

## in their study

## of

## method should have a

## publicaccess modifier, and either has an

## severity

## rating of test smells and their impact on the maintainability

## annotation

## called@Test(JUnit 4) or the method name should start

## of test suites. In a study on the evolution of test smells,14

## Kim

## ]

## [

## with ‘test’ (JUnit 3).

## uses

## tsDetect

## to show

## that

## test smells

## persist

## in systems

## even

## Production File Detection.In order to detect some test smells,

## though developers refactor the code.

## e.g., Eager Test and Lazy Test, the production

## file associated

## with

## Educators.tsDetectcan also be used by software engineering

## the unit

## test

## file

## is

## required.

## To identify

## the

## production

## file,

## we

## educators in

## the

## classroom

## to

## teach

## students

## the

## importance

## of

## explore the project structure to search for files that have the same

## designing high

## quality,

## maintenance-friendly

## test

## suites.

## As

## an

## name as the test file, but without

## the word ‘test’. Next, for each

## example,tsDetectis being used as part of an activity in a software

## production file we identified, the tool generates its corresponding

## testing course offered by the Department of Software Engineering

1

## AST to ensure that the file is syntactically correct.

## at Rochester Institute of Technology

## .

## tsDetectUsage.As a command line tool,

## can be exe-

## cuted via the following command:

## 6 EVALUATION

## We

## conducted an empirical study on the effectiveness

## tsDetect

## of

## java -jar

## .\TestSmellDetector.jar

## <path_to_test_files>

## in correctly detecting test smells, in terms of precision and recall.

## Once

## tsDetect

## has been

## started,

## it

## requires

## no

## further

## user

## As there are no existing datasets containing information for all the

## intervention. After the detection process is completed, a CSV file

## supported smells, we decided to construct our own validation set.

## containing the results of the detection process will be created and

1

## returned as output.

[https://www.se.rit.edu/](https://www.se.rit.edu/)

## 1652


---

<!-- Página 4 -->

ESEC/FSE

**Table 2: Test smell detection correctness tsDetect**Westart by randomly selecting test files (and their corresponding production files) from 656 open-source Android apps, hosted on F- Droid [8]. We ensured that these apps were not duplicated or forked by verifying the uniquenessof the source URL and commit SHA. Due to space constraints, we provide the details of these projects on ourwebsite[ ]. We thenusethedefinitionoftestsmellsto identify them in the source files. Upon the identification of smells in a testfile,wetagit alongwithitscorrespondingproduction file and the typesof smellsits exhibits.We keepthis processof manually analyzingfiles and annotatingthem until we reach 20 infected instances per smell. This process resulted in a total of 65 annotated files. Next, to ensure an unbiased annotation process, we performed a manualanalysis by involving another set of reviewers to review the **#****#**| correctedexistingannotated set. We involved 39 graduate and undergraduate**Smell****Precision****instances** studentsfrom the Department of Software Engineering at Rochester Assertion| 18 Institute of Technology to manually review the samefiles for theConditional| 20 **7 RELATED**WORKConstructor| 20existence of test smells. All participants volunteered to participateDefault| 20 Researchon test smellshas proposedtestsmells, conducted empir-Duplicatein the experiment and were familiar with Java programming, unit Eager| 20ical studies on projects related to test smells, and proposedtoolstesting, and quality assuranceconcepts.The experienceofEmptythese| 20 Exception| 20for the detectionof test smells. In this section,we focus only onparticipants withJavadevelopmentrangedfrom2to11years,General| 20 peer-reviewedstudiesthat are relatedtotest smell detection tools.Ignored| 20100%which includes exposure to developing unit tests. Prior to the review Lazy| 20Breugelmanset al. [] built a tool,TestQ,which allows develop-process, the participants were provided with a 75-minutetutorialMagic| 20 Mystery| 19ers to visually explore test suites and quantify test smells. Similarly,on test smells along with reference materials. To reduce the effectRedundant| 20 Koochakzadehet | al.[] builtaplugin,theRedundant93.02%TeCRevis, forof bias, participants were randomly grouped into groups of three, Resource| 20visualization of redundant tests. Neukirchenet al.18 [ created T-resultingin a total of 13 groups. Each group was providedwithten| 18 Sleepy| 18Rex , a tool that detects violations of test cases to the Testing andtest files. The number of smell types exhibited by each file rangedUnknown| 18 TestControl Notation (TTCN-3). In other studies, Greiler et9al. [**Average**−**96.01%**from one to six. On average, each file contained three smell types. introduced new test smells related to test fixtures and also built aHowever,the participants were not informed of the type or count detection tool,TestHound, as part of their research. In a subse-of smells contained in their set of test files. quent study [], the authors extended the tool to mine Git and SVNTofurther protect from bias, we provided each smell type to at repositories for test fixture smells. Reichhart et al.] proposedleast two groups.Each group was askedto annotateeach of the a tool for the detection of test smells in Smalltalk. Zang et]al. [assignedfiles with the smell they think it contains. The participants builtDTDetectorto detect dependent tests. Bavota et al.6 ] [were offered a period of three days to submit their survey results. a tool that can detect nine types of test smells, while Palomba etWhen reviewing the survey results, we noticed two cases from the al. [ 21] deviseda tool for detectingthree typesof test smellsbysame groupwheretherewasno agreementaboutthe existence means of textual analysis.As described,there exist multipletestof aMystery Guest . There was no consensusbetweenthe group smell detection tools; hence a single tool that can detect a varietymembers onwhethertheyshouldconsideraserviceAPIcalla of smells will help with developer productivity.guest in part because it is not mentioned in the provided definition. Therefore,we decided to filter out these two cases, and we replaced **8 CONCLUSION**AND FUTUREWORKthem withtwo othermanuallyidentifiedmysteryguestswhich werereviewed again by the group. This process generated a revised In this paper, we introducedtsDetect, an open-sourcetool that annotated set that we use as our oracle for testing the detection can detect19typesoftestsmellsoccurringinJUnit-basedtest accuracy.We next ran our tool on the same set of test files and thensuites. We also described the architecture of, the ease of compared our results against the oracle. For each smell type, weintegrating newtypes into the tool, and its use in research constructeda confusion matrix and calculated the precision, recall,studiesby the community. To evaluate our tool, we conducted a set accuracy,and F-Score.of experimentson the soundness of. The results show Table 2reportsthedetectionresultsforeachsmelltype.Asthat our tool achieves a high performance in terms of F-score with shown in the table,tsDetectachieves a high level of correctnessan average of 96.5% on all the considered test smells types. with F-Scoresrangingfrom87.8%to100%.ForthecaseswhereOur future work includes improvements/extensions to the tool. the tool did not achieve 100%, we investigate the slight mismatchThe next step will be to integratetsDetectwith common IDEs in between the tool and the human decision. We had only one casethe form of a plugin. We aim to extendtsDetectto new types of where ourtooldidnotdetecta smell,andwe hadto refineourtest smells, such as those showing up in the naming practicesof detectionrule. The other cases were related to the human interpre-the test. This will leverage existing research on naming practices tation of the smell definition, and that is why developers can update[5, 11, 19, 23–25] to studytestsand determinewhentheseprac- the default rules to better match what they consider as problematic.tices are smelly. Finally, we encourage the community to download The dataset used in this experiment is available on our website4 ].[tsDetectand contribute to its improvement and extension.

1653


---

<!-- Página 5 -->

tsDetect:An

## REFERENCES

empiricalEmpirical, 23(3):1188–1221, [21]F.[1]. ingInternational[2]. Maintenance, pages[3]. [22]A.[4]. On[5]V. ploratoryProceedingsareEmpirical, 21(1):104–158, Computer, CASCONFeb. ton,[6]G. [23]A.harmful?Empirical, 20(4):1052–1094, investigationInternationalIn2015. Workshop, 2018.[7]M. [24]A.characteristicsInternational renamedevelopment, 2008. the[8]. Manipulation . IEEE,[9]M. [25]A.strategiesInternational renameJournaland, pages of, 169:110704,[10]M. [26]A.text ploratorySoftware, pages Proceedings, IWoR[11]E.Proceedings York,23rd, Genoa, [27]R.Software. McGraw-Hill,pages New[12]. [28]S.[13]. Journal, 6(9):231–251,[14]D.Proceedings [29]M.42nd, oper2019ICSE Seminar[15]N. 2019 , 2019.redundancyTesting–Practice, pages D.[30]136, ofInternationalIn[16]xUnit. Pearson Maintenance, pages [17]G. [31]D. In International tigating Languages, 2010. Conference, MSR H.[18] [32]M. ttcn-3Testing, pages D.Int. 2007. Conf., pages [19]C. [33]S. identifier2019 Empirically Maintenance, pages Software, pages [20]F. the

## 1654


---

