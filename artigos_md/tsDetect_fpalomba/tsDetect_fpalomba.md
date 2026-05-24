<!-- Página 1 -->

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

### tsDetect: An

### Open

### Source

### Test

### Smells

### Detection

### Tool

## Anthony Peruma

## Khalid Almalki

## Christian D. Newman

### axp6201@rit.edu

### ksa8566@rit.edu

### cnewman@se.rit.edu

### Rochester Institute of Technology

###

### of

###

### of

### Rochester, New York, USA

### New

### USA

### New

### USA

## Mohamed Wiem Mkaouer

## Ali Ouni

## Fabio Palomba

### mwmvse@rit.edu

### ali.ouni@etsmtl.ca

### fpalomba@unisa.it

### Rochester Institute of Technology

### ETS Montreal, University of Quebec

### SeSa Lab -

### of Salerno

### Rochester, New York, USA

### Montreal, Quebec, Canada

### Fisciano (SA), Italy

## ABSTRACT

### Hence,

### this process requires developers writing test code to exercise72

### production code.

### The test code, just like production

### source

### is subject

### to bad

### Even though the unit test code will not be executed in produc-

### design and programming practices, also known as smells. The pres-

### tion, it is essential that developers follow standard programming

### ence of test smells in a software project may affect the quality, main-

### practices

### when implementing a test suite. This practice ensures that

### tainability, and extendability of test suites making them less effec-

### the production code is effectively exercised and enables developers

### tive in finding potential faults and quality issues in the project’s pro-

### to easily identify defects in the system. Similar to traditional code

### duction code. In this paper, we introduce

### tsDetect,an automated

### smells, i.e., bad programming practices, unit tests may also suffer

### test smell detection tool for Java software systems that uses a set of

### from smells that are exclusive to the testing domain

### 16 ].

### [

### detection

### rules to locate existing test smells in test code. We evaluate

### more, just like how traditional

### code smells

### cause a system

### to be

### the effectiveness oftsDetecton a benchmark of 65 unit test files

### more prone to changes and defects

### 20

### [ it has been shown that test

### containing

### instances of 19 test smell types. Results show that

### smells may negatively impact the quality of the system [30].

### tectachieves

### a high detection accuracy with an average precision

### Therefore, there is a growing need to incorporate

### the verifica-

### score of 96% and an average recall

### of 97%.

### is pub-

### tion of bad testing practices into modern code reviews. While there

### licly available, with a demo video, at: https://testsmells.github.io/

### exist open-source quality assurance tools, such as PMD

### 3 ], Check-

### style [1], and FindBugs [], which primarily focus on detecting a

## KEYWORDS

### variety of quality issues in production code, the number of open-

### Software Quality, Test Smells, Detection Tool

### source tools that detect a wide variety of test smells and supports

**ACM**

### integration with continuous

### frameworks is limited.

Anthony

### This paper introducestsDetect, an open-source tool that cur-

Mkaouer, Ali Ouni, and Fabio Palomba. 2020.tsDetect:An Open Source

### rently supports the detection of 19 common test smells,

### i.e. , devia-

Test SmellsDetectionTool. InProceedings of The 28th ACM JointEuro-

### tions from good unit testing programming practices, as advocated

pean

### in xUnit guidelines [

### , 17 ]. These 19 smells are part of the catalog

Software Engineering (ESEC/FSE 2020).ACM, New York, NY, USA, 6 pages.

### of unit test smells, and details about their definitions, rationale, and

[https://doi.org/10.1145/nnnnnnn.nnnnnnn](https://doi.org/10.1145/nnnnnnn.nnnnnnn)

### examples appear in published literature

### 22

### [

### ]. tsDetect takes, as

### input, software project source code and first separates the set of unit

## 1 INTRODUCTION

### test files from production source files, then generates their Abstract

### Quality assurance is a crucial driver in any software project, and

### Syntax Trees (ASTs) in order to search for any predefined patterns

### the success of the project depends on the quality aspects it exhibits,

### of bad test programming

### practices

### syntactically

### using

### detection

### meaning

### we need to optimize these aspects. Software testing is one

### rules.tsDetectgenerates, as output, a file containing all detected

### of the widely-acknowledged techniques that are of paramount im-

### violations. tsDetect has been designed to be easy to extend,

### i.e. ,

### portance for quality assurance. There are different types of testing

### developers can easily calibrate the predefined rules and add their

### strategies that can be adopted

### to test a software

### system,

### such as

### own customized

### rules

### if needed.

### Moreover, although

### tsDetect

### unit testing [

### ]. Unit

### involves developers

### the small-

### currently detects 19 test smells, it is designed with a high level of

### est unit in the production

### codebase, which is typically a method.

### flexibility to incorporate new smell types easily, and also permits

### the customization

### of the existing smell detection

### rules as shown

Permission

### later in Section 3, where we discuss the architecture of the tool.

classroom

### To

### evaluate the correctness of

### tsDetect,we performed a qual-

for on

### itative analysis

### on a benchmark

### of 65 unit test files that contain

must

### instances

### from various smell types. Analysis of our tool has shown

to

### that tsDetectis able to correctly detect test smells with a precision

fee. ESEC/FSE

### score ranging from 85% to 100% and a recall

### from 90% to 100%

© 2020

### with an average F-score of 96.5%.

ACM [https://doi.org/10.1145/nnnnnnn.nnnnnnn](https://doi.org/10.1145/nnnnnnn.nnnnnnn)

1

59

60

61

62

63

64

65

66

67

68

69

70

71

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116


---

<!-- Página 2 -->

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

ESEC/FSE

175Furthermore,we have utilizedtsDetectto perform a large-scale**3****TSDETECTARCHITECTURE** 176empiricalstudy on open-source Android applications (apps) and tra-tsDetectis implemented as an open-source, command line-based177 ditional Java systems []. Our study investigated the occurrences178tool that is availableas a standaloneJavajar file. By providing 179and distribution of the 19 test smells on 656 open-source AndroidtsDetectas a self-contained executable file rather than a plugin 180 apps, including a comparison of smell type occurrence with tradi-(whichis part of our future work), users are not required to have a181 tional Java systems.In a subsequentstudy26[ we explored the182specific IntegratedDevelopmentEnvironment(IDE) installed on 183impact and relationshipbetweenrefactoringoperationsand testtheir machine in order to detect smells intest code. Similar to184 smells, detected bytsDetect, in 250 open-source Android apps.185other code smell and defect detection tools such as PMD and Find- 186**Open source**toolanddocumentation.ThetsDetectBugs, offering tsDetect as an executable through the command 187project’s website[4 ] includesthetoolsourcecode,alongwithline facilitates its integration with modern continuous188 a demonstrationvideo and documentationon how to use it. The189frameworks,as well as its adoption in mining software repositories 190website also contains examples and general information about testand empirical studies in software engineering. 191 smells. Additionally,tsDetecthas receivedincreasinginterestIn additiontothetsDetectdetection mechanism,weincor-192 on GitHubfromthedevelopmentandresearchcommunitiesin193porate supplementarymodulesto automatethe entire detection 194the form of forks and feedbackon how to improve our tool andworkflow.These modules support the detection process by parsing195 make it more practical. We encourage the community to contribute196the input source files to detect unit test(and their correspond- 197improvements and extensions totsDetect.ing production files) in the project hierarchy. A high-level overview 198 of the architecture oftsDetectis depicted in Figure 1. Inand②,199 200the test and production files are identified from the project structure. **2 BACKGROUND**AND MOTIVATION201In ③and④,tsDetectchecks if the test files exhibits test smells. In 202 Testsmells represent deviations from well-established testing prac-⑤ , the results from the test smell detection process are saved. In the203 tices andguidelinesonhowtestcasesshouldbedesigned,im-204followingsubsections, we describe the detector and the mechanism 205plemented, andhowtheyshouldinteractwitheachother.Theto distinguish test files and their corresponding production files.206 detectionof such potential deviations is typically a tedious, manual,207 208and error-prone task for developers and testers. Effective detection 209of test smells requires expertise from developers to inspect, under- 210 stand, and run the test to be able to correctly detect the violations.211 212The goal of implementingtsDetectis to provide developers 213 with an automated approach for optimizing the quality of their test 214 suites. tsDetecthas the ability to detect 19 smells occurringin215 216JUnit based unit test files, some of which have been highlighted in 217 existing literature as being problematic9[ 17 , 30, 32]. The list of218 219detected smells supported bytsDetectis reported in Table 1 along 220with their definitions/detection rules. In summary,tsDetectana- 221 lyzes the test suite for the existence of certain violations to xUnit222 223testing guidelines [, 17 ]. Even though all test smells detected by 224 the tool apply to any Java-based system, one smell, namely Default**Figure 1: High-level architecture of****tsDetect**225 Test,is specific to Android applications. For the sake of space limi-226 **3.1 Test**Smell Detection227tations, we provide the necessary background information about 228 the smells supportedbytsDetectin our prior study22[ ]. Addi-Wefollowed a strategy design pattern in implementing the detection229 230tionally,our project’s website4[ contains examples of real-worldmechanismfor test smells (UML class diagrams are available on the 231code snippets that exhibit each of the supported smell types.projectwebsite). Eachis implemented and runs independently 232 The detected test smells bytsDetectprovidesvaluable supportof other smells. The detectionstrategy of each smell type is self-233 234for developers. Our prior work22[] has shown the prevalence ofcontained within its own module. This design pattern also enables 235 these smellsin open-sourcesystems,indicatingthe difficultyofthe seamless addition of new smell detectors in the future. Internally, 236 developers to remove them from the codebase during the lifetimetsDetectcalls the JavaParser [] library to parse the source code237 238

### TS

## DETECT

of the project.Furthermore,in our previousqualitativeanalysisfiles. JavaParser builds an AST from the unit test file that is under

## CSV

## 2

239 [ 22 ] in which we reached out to developers whose test files exhibitanalysis. The AST is then analyzed by each of the available smell240

# Assertion

## Path to unit

# Eager Test

# Empty Test

## test files

## Test File

241

# Roulette

a test smell detected bytsDetect, most of the surveyed developersdetection modules based on therules defined in Table 1.

## Detection

242confirmed that the test files identifiedbydid containDepending on the type of smell beingdetected,we overridethe 243

# Redundant

# Lazy Test

# ...

## 1

instances of bad unit testing programmingpractices. Additionally,appropriatevisit()method to perform the detection. For example,

## 4

244

# Print

## JAVA

245based on the outputof our tool, some of these developersmade in the case of detecting theRedundantPrint smell, we first create a

## Project

## Production

# Test Smell Detector Modules

246

## source code

necessarycorrections to their code based on the findings. Hence, toMethodDeclarationvisitor to identify all test methods in the class.

## File

247

## Detection

## 5

ensurethat unit tests are of high-qualityand maintenance-friendly,Next, for each detected test method, we createMethodCallExpra248

# JavaParser

249we provide the community with a tool that can be integrated intovisitor to examine the methods being called within the test method.

## CSV

250 the development workflow to automate the identification of bad unitFinally,for each called method, we check if the name of the method

## tsDetect

251

## results

252testing practices early during the system’s development lifecycle.matches a Java print method to determine if the file is smelly. 253 2 254


---

<!-- Página 3 -->

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

292

293

294

295

296

297

298

299

300

301

302

303

304

305

306

307

308

309

310

311

312

**Test**

Assertion Conditional Constructor Default Duplicate Eager Empty Exception GeneralsetUpmethod Ignored@Ignoretheannotation Lazy Magic Mystery Redundantor printlnor printfor writemethodSystemclass Redundant Resourceclassexists(), isFile()or notExists()methods SensitivetoString()method SleepyThread.sleep()method Unknown@Test(expected)annotation

tsDetect:An

## Table 1: Summary of the test smell detection rules built-in

## tsDetect

313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339

## On completion,

## the results are saved into a Comma-Separated

## 4

## TSDETECTAPPLICABILITY

340

## Values

## (CSV) file. For each smell type,

## tsDetectoutputs

## a boolean

## developers

## integrating

## tsDetect

## Practitioners.We envision

341

## value indicating if the smell is present or not in the file. We decided

342

## into their development toolset and workflow. For example, by in-

343

## on a CSV format for output as this

## is technology independent

## tegrating it into their build process, developers will be notified of

344

## and permits users to import the data into a database system of their

## smells in their test code before either committing the file into the

345 346

## choice for ease of analysis.

## repository or generating a production release. Furthermore, in our

347

## Test

## File Detection.JUnit recommends that developers follow

## previous work [

## ], we reported smells detected by

## tsDetectto

348

## the naming convention [

## ] of either pre-pending or appending the

349

## 120 developers,

## from various

## open-source

## systems.

## We received

350

## word ‘Test’ to the name of the production

## file that is to be tested

## responses from 50 developers,

## with most developers

## confirming

351

## ( i.e. , Test*.java and *Test.java). Our tool first identifies all ‘.java’ files

## that the programming constructs we highlighted in their code are

352

## where the filename either starts or ends with the word ‘test’. Next,

353

## indeed examples of test smells, and that they will take corrective

354

## for each of the identified Java source files, the tool parses its AST

## actions to fix them.

355

## using JavaParser. The purpose of

## the AST is twofold. First,

## tsDe-

## Researchers.With the capability of batch-based analysis,

356 357

## we are able to eliminate Java files that contain syntax errors, and

## tectcan be used by researchers in empirical studies on software

358

## secondly,

## we are able to accurately detect if the file contained JUnit-

## quality and maintenance.

## As previously

## stated,

## we have utilized

359

## based unit test methods. For a file to contain a unit test method, the

360

## tsDetect

## in empirical

## studies

## of

## open-source

## systems

## 22

## [

## 26 ].

361

## method should have a

## publicaccess modifier, and either has an

## Additionally,tsDetecthas also been utilized by the research com-

362

## annotation

## called@Test(JUnit 4) or the method name should start

## munity

## in the study of test smells. Schvarcbacher et

## 29

## al.

## ] integrate

## [

363

## with ‘test’ (JUnit 3).

364

## tsDetectinto a code quality monitoring system to study reactions

365

## Production File Detection.In order to detect some test smells,

## to test smells.

## Spadini

## et al.

## 31

## [ use

## tsDetect

## in their study

## of

366

## e.g., Eager Test and Lazy Test, the production

## file associated

## with

## severity

## rating of test smells and their impact on the maintainability

367 368

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

## of test suites. In a study on the evolution of test smells,14

## Kim

## ]

## [

369

## explore the project structure to search for files that have the same

## uses

## tsDetect

## to show

## that

## test smells

## persist

## in systems

## even

370

## name as the test file, but without

## the word ‘test’. Next, for each

371

## though developers refactor the code.

372

## production file we identified, the tool generates its corresponding

## Educators.tsDetectcan also be used by software engineering

373

## AST to ensure that the file is syntactically correct.

## educators in

## the

## classroom

## to

## teach

## students

## the

## importance

## of

374

## tsDetectUsage.As a command line tool,

## can be exe-

375

## designing high

## quality,

## maintenance-friendly

## test

## suites.

## As

## an

376

## cuted via the following command:

## example,tsDetectis being used as part of an activity in a software

377

## testing course offered by the Department of Software Engineering

378 1379

## at Rochester Institute of Technology

## .

380 381

## java -jar

## .\TestSmellDetector.jar

## <path_to_test_files>

382

## 5 EVALUATION

383

## We

## conducted an empirical study on the effectiveness

## tsDetect

## of

384 385

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

386

## As there are no existing datasets containing information for all the

387

## intervention. After the detection process is completed, a CSV file

## supported smells, we decided to construct our own validation set. 388

## containing the results of the detection process will be created and

389 1390

## returned as output.

[https://www.se.rit.edu/](https://www.se.rit.edu/) 391 3 392


---

<!-- Página 4 -->

393

394

395

396

397

398

399

400

401

402

403

404

405

406

407

408

409

410

411

412

413

414

415

416

417

418

419

420

421

422

423

424

425

426

427

428

429

430

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

ESEC/FSE

**Table 2: Test smell detection correctness tsDetect**Westart by randomly selecting test files (and their corresponding production files) from 656 open-source Android apps, hosted on F- Droid [8]. We ensured that these apps were not duplicated or forked by verifying the uniquenessof the source URL and commit SHA. Due to space constraints, we provide the details of these projects on ourwebsite[ ]. We thenusethedefinitionoftestsmellsto identify them in the source files. Upon the identification of smells in a testfile,wetagit alongwithitscorrespondingproduction file and the typesof smellsits exhibits.We keepthis processof manually analyzingfiles and annotatingthem until we reach 20 infected instances per smell. This process resulted in a total of 65 annotated files. Next, to ensure an unbiased annotation process, we performed a manualanalysis by involving another set of reviewers to review the **#****#**| correctedexistingannotated set. We involved 39 graduate and undergraduate**Smell****Precision****instances** studentsfrom the Department of Software Engineering at Rochester Assertion| 18 Institute of Technology to manually review the samefiles for theConditional| 20 Constructor| 20existence of test smells. All participants volunteered to participateDefault| 20 Duplicate| 18in the experiment and were familiar with Java programming, unit

### 6 RELATED

### WORK

Eager| 20 testing, and quality assuranceconcepts.The experienceofEmptythese| 20Researchon test smells has proposed test smells, conducted empir-Exception| 20participants withJavadevelopmentrangedfrom2to11years,General| 20ical studies on projects related to test smells, and proposed Ignored| 20which includes exposure to developing unit tests. Prior to the reviewfor the detectionof test smells. In this section,Lazy| 20 process, the participants were provided with a 75-minutetutorialMagic| 20peer-reviewed studies that are related to test smell detection tools.Mystery| 19on test smells along with reference materials. To reduce the effectRedundant| 20Breugelmanset al. [] built a tool,TestQ,which allows develop- Redundant| 20of bias, participants were randomly grouped into groups of three,ers to visually explore test suites and quantify test smells. Similarly,Resource| 20 resultingin a total of 13 groups. Each group was providedwithten| 18Koochakzadeh etal.[] builtaJavaplugin,Sleepy| 18test files. The number of smell types exhibited by each file rangedUnknown| 18visualization of redundant tests. Neukirchen **Average**−**96.01%**from one to six. On average, each file contained three smell types.Rex , a tool that detects violations of test cases to the Testing and However,the participants were not informed of the type or countTestControl Notation (TTCN-3). In other studies, Greiler et9al. [ of smells contained in their set of test files.introduced new test smells related to test fixtures and also built a Tofurther protect from bias, we provided each smell type to atdetection tool,TestHound, as part of their research. In a subse- least two groups.Each group was askedto annotateeach of thequent study [], the authors extended the tool to mine Git and SVN assignedfiles with the smell they think it contains. The participantsrepositories for test fixture smells. Reichhart et al.] proposed were offered a period of three days to submit their survey results.a tool for the detection of test smells in Smalltalk. Zang et] When reviewing the survey results, we noticed two cases from thebuiltDTDetectorto detect dependent tests. Bavota et al. same groupwheretherewasno agreementaboutthe existencea tool that can detect nine types of test smells, while Palomba et al. of aMystery Guest . There was no consensusbetweenthe group[ 21 ] devised a tool for detecting three types of test smells by means members onwhethertheyshouldconsideraserviceAPIcallaof textual analysis. guest in part because it is not mentioned in the provided definition. Therefore,we decided to filter out these two cases, and we replaced

### 7 CONCLUSION

### AND FUTURE

them withtwo othermanuallyidentifiedmysteryguestswhich werereviewed again by the group. This process generated a revised In this paper, we introducedtsDetect, an open-source annotated set that we use as our oracle for testing the detection can detect19typesoftestsmellsoccurring accuracy.We next ran our tool on the same set of test files and thensuites. We also described the architecture of compared our results against the oracle. For each smell type, weintegrating newtypes into the tool, and its use in research constructeda confusion matrix and calculated the precision, recall,studiesby the community. To evaluate our tool, we conducted a set accuracy,and F-Score.of experimentson the soundness of Table 2reportsthedetectionresultsforeachsmelltype.Asthat our tool achieves a high performance in terms of F-score with shown in the table,tsDetectachieves a high level of correctnessan average of 96.5% on all the considered test smells types. with F-Scoresrangingfrom87.8%to100%.ForthecaseswhereOur future work includes improvements/extensions to the tool. the tool did not achieve 100%, we investigate the slight mismatchThe next step will be to integratetsDetectwith common IDEs in between the tool and the human decision. We had only one casethe form of a plugin. We aim to extendtsDetectto new types of where ourtooldidnotdetecta smell,andwe hadto refineourtest smells, such as those showing up in the naming practices detectionrule. The other cases were related to the human interpre-the test. This will leverage existing research on naming practices 524 tation of the smell definition, and that is why developers can update[5, 11, 19, 23–25] to studytestsand determine the default rules to better match what they consider as problematic.tices are smelly. Finally, we encourage the community to download The dataset used in this experiment is available on our website4 ].[tsDetectand contribute to its improvement and extension. 4

451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 tools479 480we focus only on 481 482 483 484 485 TeCRevis, forthe486 487et al.18 [ created T- 488 489 490 491 492 493 494 495 496 al. [497 4986 ] [ 499 500 501 502 503 504 505

### WORK

506 507tool that 508 inJUnit-basedtest509 510, the ease of 511 512 513 514. The results show 515 516 517 518 519 520 521 522 of 523

525whentheseprac- 526 527 528 529 530


---

<!-- Página 5 -->

531

532

533

534

535

536

537

538

539

540

541

542

543

544

545

546

547

548

549

550

551

552

553

554

555

556

557

558

559

560

561

562

563

564

565

566

567

568

569

570

571

572

573

574

575

576

577

578

579

580

581

582

583

584

585

586

587

588

tsDetect:An

589

## REFERENCES

empiricalEmpirical, 23(3):1188–1221, 590[21]F.[1] 591ingInternational[2] 592Maintenance, pages[3] 593[22]A.[4] 594On[5]V. 595ploratoryProceedingsareEmpirical, 21(1):104–158, 596Computer, CASCONFeb. 597ton,[6]G. 598[23]A.harmful?Empirical, 20(4):1052–1094, 599renameJournal2015. 600of.[7]M. 601[24]A.characteristicsInternational 602investigationInternationalIndevelopment, 2008. 603Workshop, 2018.[8] 604[25]A.[9]M. 605renamestrategiesInternational 606theand, pages 607Manipulation . IEEE,[10]M. 608[26]A.text 609ploratorySoftware, pages 610Proceedings, IWoR[11]E.Proceedings 611York,23rd, Genoa, 612[27]R.Software. McGraw-Hill,pages 613New[12] 614[28]S.[13] 615Journal, 6(9):231–251,[14]D.Proceedings 616[29]M.42nd, 617oper2019ICSE 618Seminar[15]N. 6192019 , 2019.redundancyTesting–Practice, pages 620D.[30]136, 621ofInternationalIn[16]xUnit. PearsonMaintenance, pages622 [17]G.[31]D.623 In Internationaltigating624 Languages, 2010. Conference, MSR625 [18]H. [32]M.626 ttcn-3Testing, pages D.Int.627 2007. Conf., pages628 [19]C. [33]S.629 between Empirically630 Conference. IEEE, Software, pages631 [20]F. 632 the 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 666 667 5 668


---

<!-- Página 6 -->

669

670

671

672

673

674

675

676

677

678

679

680

681

682

683

684

685

686

687

688

689

690

691

692

693

694

695

696

697

698

699

700

701

702

703

704

705

706

707

708

709

710

711

712

713

714

715

716

717

718

719

720

721

722

723

724

725

726

ESEC/FSE

## APPENDIX

## As requested by the submission guidelines, we are providing an Appendix that contains a walkthrough tsDetect

## sources/artifacts.

## Source Code

## The source code for

## tsDetectis available in a publicly accessible GitHub repository: https://github.com/TestSmells/TestSmellDetector

## Project Website

## In addition to resources around the 19 test smells, our project website contains details

## tsDetect

## , including links to the relevant datasets. Additionally, we also maintain a running list of research publications that use.

## The project website is available at: https://testsmells.github.io

## Demonstration Video

## A video demonstration

## on how to use tsDetect to identify test smells in JUnit based unit test files is available on YouTube (https://www.

## youtube.com/watch?v=kzRSadHo5YA)

## and also on our project website.

## tsDetectWalkthrough

## (1) Download

## the latest release from: https://github.com/TestSmells/TestSmellDetector/releases

## Before executing the tool, a CSV file needs to be created. The CSV file specifies the list of test files (and their associated production

## (2)

## file). This file will be used as input to the tool. The format of the file should be:

## appName,pathToTestFile,pathToProductionFile

## Example:

## myCoolApp,F:\Apps\myCoolApp\code\test\GraphTest.java,F:\Apps\myCoolApp\code\src\Graph.java

## myCoolApp,F:\Apps\myCoolApp\code\test\EmployeeTest.java,F:\Apps\myCoolApp\code\src\Employee.java

## myCoolApp,F:\Apps\myCoolApp\code\test\EmployeeRelationship.java

## Note: In the event a production file is not associated with a test file, then detection for test smells that require

## (3)

## Once the CSV file has been created, the path to the CSV file needs to be passed as an argument when executing the jar. The format of

## the file should be:

## java -jar

## .\TestSmellDetector.jar

## pathToInputFile.csv

## Example:

## java -jar

## .\TestSmellDetector.jar

## "F:\Projects\TestSmellDetector\inputFile.csv"

## (4)

## The tool outputs a CSV file containing the results of the execution. The output CSV file will be created in the same location as the jar.

## The CSV file contains the path of the test files (and their associated production file) along with the detection status for each smell. A

## detection status of ‘true’ indicates that the associated smell exists in the test file.

6

## the studies that we have performed

## using

## and other related

727 728 729 730 731 732 733 734 735 736 737

## using

738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755 756 757 758 759 760 761 762

## files are not run

763 764 765 766 767 768 769 770 771 772 773 774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791 792 793 794 795 796 797 798 799 800 801 802 803 804 805 806


---

