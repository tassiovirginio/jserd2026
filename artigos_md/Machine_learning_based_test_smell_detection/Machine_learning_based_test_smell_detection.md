<!-- Página 1 -->

Empirical Software Engineering (2024) 29:55 [https://doi.org/10.1007/s10664-023-10436-2](https://doi.org/10.1007/s10664-023-10436-2)

### Machine

### smell

**1,2****Valeria**·**Dario** **1****Dario**·**Filomena**

Accepted:Published online: 5 March 2024 ©

**Abstract** Testcases. Previouseffectiveness. Therefore, them.dependent thresholds. design experimentsmell machinesmells. validated smellstrain machine andcross-project ML-basedÞndings study signiÞcantly anfurtherreasons negativechallenges prevent appropriatenext steps thatsmell

**Keywords**Test·Test engineering

**1**

Test the ing2011). worth 2017). individual developer’s

Communicated MariaCarver Neil Ernst

This article

ValeriaB [valeria.pontillo@vub.be](mailto:valeria.pontillo@vub.be)

Extendedpage

**3**·**Fabiano** **1****1**·**Fabio**

·Machine·Empirical

2015)

*Registered*

0123456789().: V,-vol

**1**·

### 123


---

<!-- Página 2 -->

55agef4Empirical Software Engineering (2024) 29:55

thedefectsMesbah timely2017). testcould test2012), testing debuggingShihab symptoms represent of et2016). stand2016) 2018;Bavotaetal.2015;2019) effectiveness showingpresence softwaretest For smellsKüçük2018). particularcompare extracted codeinstance, Rompaey2007) metricscase) combines detectionbeing the smelllimitations. detection et2007;2013;2018). inßuenced and2016; threaten practical ofneed combine of heuristic-based In ofperformance an textualbeing is forsmell*Eager*,*Mystery* and*Test*.performance detector*Java*projects—which manually theKüçük compare our be betterit ineffective test As issues challenges investigation catalog andpractical examples thespeciÞcally inaccuratemeasurement

### 123

2015)andthe

2015). 2001), 2017;Tufano

2019),

2018).

,*Resource*,

2018)—and


---

<!-- Página 3 -->

Empirical Software Engineering (2024) 29:55Pagef455

of inappropriate weactionable

*Structure*Section2overviewsexplains the In3, elaboratestudy, while4reportssmell learning5, evaluation6and7. study8,9 concludesoutlines future

**2**

Investigations theBeck2003). Van2001)2007) their refactoring2013)devisedTestHound,aheuristic- based Palomba2018)devisedTaste,leverages thePoshyvanyk2005) viousidentify smell detection et2018)Darts(Lambiase2020),Intellijplugin thatTasteusable2020)tsDe- tect,*Assertion*, *Eager*,and*Lazy Test*. Felderer Felderer2023) SniffTest, Þve*Anonymous*,*Long*,*Conditional*,*Assertion* *Roulette*,and*Rotten*.2020)VITRuM,aJavaplu- gindynamicidentify smell2021)PyNose,aPythonplugin testGarousi2010)TeReDetect, uses rules and*Test*, impacting test2019)SoCRATES, tooltest smellsScalasoft- ware systems. methodsmells; proposedrequire multiple empiricalinvestigation smell Otherempirical2016) investigated2015)test highlyunderstandability results2023) icallycases2019) combinationofScalaandScalaTest(De2019). et2023) highlypotentially2018) smellsand2019)also

### 123


---

<!-- Página 4 -->

55agef4

discovered test-driven code. these provided smellsshould beaim for on smells therefore, on tion of (iii) a detection As data imbalanceshown smells more around classes limitationsmells. Nevertheless, toadditional Concerningand this Section4maysubjectivityvalidation; inmanual performeddataset.predictors, existing identifying

**3**

The*goal*ofsuitabilitytest smell detection,*purpose* design*perspective* thetest smell SpeciÞcally, paper

**RQ****.***Which*1 *smell*

**RQ****.***What**smell*2

**RQ****.***How does*3 *heuristic-based*

With the tribute mostsmells. predictiveidentify most machine-learning ually

### 123

Empirical Software Engineering (2024) 29:55

2019b).

2015)

2016).the

2016).

ofcode is researchers practitioners

**RQ**),1

**RQ**, run2

2019).test

*Eager*instances

**RQ**s),

4)


---

<!-- Página 5 -->

Empirical Software Engineering (2024) 29:55

to pare based learningshould be To report empirical guidelines

**4**

CreatingÞrst step of tigation.test collection

**4.1**

Wedata from GitHub, cases. International First,casesnot labeled this test quality.sizes, ideal source detailed this study,asmell 2020) casesusesmell diffuseness thoseresulted we the *Eager*,*Mystery*

**4.2**

Insmells learning with the smells wouldrequirements: been basedbe metric,have this

1Available[https://github.com/acmsigsoft/EmpiricalStandards](https://github.com/acmsigsoft/EmpiricalStandards) 2[https://mir.cs.illinois.edu/ßakytests/](https://mir.cs.illinois.edu/ßakytests/)

2012),

,and*Resource*

Pagef455

**RQ**, aimed3

1*ACM/SIGSOFT*.

Javaprojects,

2Thedriven

2023).rationale using 2021,2022). their VITRuM(Pecorelli

VITRuMfor was 7%, respectively.

**RQ**and**RQ**; their12

.

### 123


---

<!-- Página 6 -->

55agef4

supported tool—otherwise, requirements, smellsstarted list smell studysmellthe they programmingonly and ofdo Javaas target approachsmells. Afterward,test detect theforextracted testfurthertest been deÞnedmetrics reported select smell *Equality*,*Resource*,and*Test* detection secondtool) guaranteedsmells detectedselected more However, and*Sensitive*); lead computational *Empty*is*“a**have* *ments”*; this *Test*instancesTsDetect, applies*Sensitive*, *the*. 2020) one instances methodtoString Bavota2012)atoString tion. According et2020) ofdecidedsmells, resulting smells Another it likely forwe aimedextentsmell. Theseperformance compares with novel,

### 123

Empirical Software Engineering (2024) 29:55

**RQ**.3

2021).

Javaas Javaas

4.2), *Empty*,*Eager*,*Mystery*,*Sensitive* .

2023). *Empty*

2020)*Empty*

*“an**an*

2012),*Sensitive* 2020) detector method

2012)

4together *Resource*smell.


---

<!-- Página 7 -->

Empirical Software Engineering (2024) 29:55

**4.3**

Oncetest smell potentialtomanual The section. the tosmells, empirical software manually-built was Given impracticabilitycases, process conductedcases =sample,distribution cases software that same willthat take the assmells. ideawillingness smellinesspopulation notsmells intended validation.sample,actual approached at

*Step* 963third paper) tasksinspectors

1.method inthey were 2.smells the thetest method itor data, e.g., project acquiremore method.

**Table**Number

#1

#2cases

#3

As

Inspector

963

1reportsanalyzed

IntelliJusers.

200

480

Pagef455

### 123


---

<!-- Página 8 -->

55agef4Empirical Software Engineering (2024) 29:55

3.Þrst, *Method’*,second to*Eager*,*‘Mystery*,*‘Resource* *Redundancy’*,test containedsmells; wasobservations might for

Uponresults κ(Cohen1960),*inter-rater*of outcome, two inspectors agreement2012). meetingvalidationcaseschallenges faced, annotations*‘Notes’*Þeld of with cornerSkypeand hours. result aset

*Step*AsunclassiÞed between themeetings. inoperations performedSkypeand paperspeciÞcinspection reviewed test Skype) round double-checked validationsrobustness AsCohen’sκmeasured agreement2012).

*Step*While formal mitigatesmellinessmay jective smellthis reason, planned smellsapproached such an*coherence*of extensiveexternal of extentsmelliness the thereliability constructed entire caseseffort requiredcases of cases strategy itspreferred onsmellsmanual rationalecases their own experience aim ofown validation.

### 123

*‘Test*

,and*‘Test*

*‘Notes’*,

*substantial*

*almost*


---

<!-- Página 9 -->

Empirical Software Engineering (2024) 29:55

**2**List**Table**

Section

#1What

#2How many have with theJavaprogramming guage?

#3Please your level the

#4How many have in

#5To the projects?

#6How familiar of optimal developing cases?

On hand, false negativesby practitioners ual cases of atcasesreached as selected cases hence thekept asmells We*Eager*instancescases *tery*instances*Resource* instancestest validation.*Eager* *Mystery*instancescases, 8%,*Test*the non-smelly cases—Table3reports terms, randomnotrepresentativeness non-smelly cases. Table2reports for academic,which theytheirsmells. We ment topossible response mitigateresponse

3Prolificwebsite:[https://www.proliÞc.co/](https://www.proliÞc.co/).

instances 2

instancescases,

Prolific

Type

Multiple source,

Paragraph

5-point

Paragraph

Multiple-choice tion, System, testing

5-point

*Resource*

platform,

Pagef455

*Mys-* *Test*

instances

3a

### 123


---

<!-- Página 10 -->

55agef4

as ies1990;2016). appropriate practitioners of smellsaskedsmellinesscases, i.e., validation,cases tocases, they orcases. limitingdictated foremost,cognitive task: wecases andhigher impactedchoice motivated response 10validation cases.cases pation,validity200 developers,several of cases Upon less year ofexperienced provideanalyzed data directlyProlific, ticipants. focusedSex.lowest age whileis respondents2% English Portuguese 32%),contributeand 1%. anonymously 81% of and pants50% declared they perform testing*frequently* ground theirtesting appendix2023). Afterward, age, smellsame result assessed that with speciÞc of evaluationsthe by was identify ing*good*agreement2012). notcase where

### 123

Empirical Software Engineering (2024) 29:55

2023).

Java.

—

2016).

κcoefÞcient

κmeasured


---

<!-- Página 11 -->

Empirical Software Engineering (2024) 29:55

recommendations didoriginal tionquestion potential validation; Thesmell to3reportsobtained 2,699*Eager*(of cases smell), of*Mystery*413 *Resource*(of cases smell), 40 *Test*(17*Test* in2023).smell, alsoanonymizedhope dataset willsmell and

### 5

###

###

Weapproach based

*Dependent*Aspresence thepresence/absence

**Table**Diffusenesscases) in entirereported various presentcases no-smelly, lasttest casessmellsthe

TestTotal

000

000

001

001

010

010

011

011

100

100

101

101

110

110

111

111

0

1

0

1

0

1

).

Ext.

307

103

22

14

23

8

Pagef455

,

5,976

2,082

413

391

513

207

7

3

### 123


---

<!-- Página 12 -->

55agef4

smell considered dependent

*Independent*Tosmell eration, identiÞcationin performing deÞned used forsmellused to machine includes

*Selecting* thesmellmost ishave familiesevo-

**Table**Testthe investigation

Test

EagerA ing object

Mystery resources or

Resource resources ing

Test removed ing suite.

### 123

Empirical Software Engineering (2024) 29:55

4to smells,

Towork

Metric

NMC

TMC the larity methods method

TSthe extent within conceptually

NRF Number Þles

NRDB database

ERNC which checked

FRNC checked

PR ratio between covered and covered

SR ratio between coveredbyatestcompared andthosecoveredbyall other suite

4reports list

4as

2023)also

Structural/textual

Textual

Textual

Structural

Structural

Structural

Structural

Structural

Structural


---

<!-- Página 13 -->

Empirical Software Engineering (2024) 29:55Pagef455

lution2018;2019;2019; Nucci et2017;2019a,b). understandbest for(ii) increase generalizabilitycapabilities of*Decision*(Freund Mason1999),*Naive*(Duda Hart1973),*Multilayer* *Perceptron*(Taud Mas2018),*Support*(Noble2006), basic siÞer. also considered ensemble*Ada*(Schapire2013)and *Random*(Breiman2001).

*Model**Training*When mentedover-samplingdata to howtestunder- sampling,*NearMiss*,,andalgorithms and2006).minority classes.have distanceremove removing mostdiversity therefore, aalso experimented with a*Random*approach, ityunder-samplesover-sampling,*Synthetic* *Minority*,*SMOTE*(Chawla2002), sions*Adaptive*,*ADASYN*(He 2008)andthe*Borderline-SMOTE*(Han et2005).*SMOTE*uses k-nearest*ADASYN* over-samples*Borderline-SMOTE* selects instances.Randomapproach, exploresover-samples Finally,experimented parameters*Random*strategyBengio2012): thishyper-parametersbest combination CoefÞcient). developed entireScikit-library et2011)inPython.

*Model*To cross-project intwowerethe performance where(ii) datathe a1974) partitions innon-smelly aFor adopted*Leave-One-Out*strategy2009), case*K*-fold cross-validation*K*equal*N*,We trained*N*−1used

### 123


---

<!-- Página 14 -->

55agef4Empirical Software Engineering (2024) 29:55

project set.*N*times in set

**6**

This sectionresearchthree questions

**6.1****-****1** **Detection**

*Research*As4, focused researchersinvestigated solution previous4listssmell independent variables smellinesstest cohesionmethods composing suites. quantiÞed *information*(Quinlan1986).*probing*method, allowedcontribution gain**RQ**,and**RQ**: indeed23 aswe metrics didexpected the placedmost top.*Gain*algorithm1986) theScikit-library2016).

*Analysis*Table5reports results**RQ**,within-1 cross-project*Eager*smell, could provide to the2018). considered of*Eager*isresults report number numbera previous*Eager* smells. As*Mystery*,most especially impactful. case, conceptually hence Þles, inßuencing results.

### 123


---

<!-- Página 15 -->

Empirical Software Engineering (2024) 29:55

**5**The*information*obtained consideredwithin-**Table** cross-project

TestMetric

EagerNMC:

TMC:the textual ods method

TS:text within method

Mystery

NRDB:

Resource not

FRNC:

Testratio theand by

SR: Redundancy thecompared those covered suite

When*Resource*,both considered This resultdeÞnition yet Oursuggest furthertherefore Finally,*Test*, metrics informationhand, Þnding the40 66 problem,smell

**Answer****.**Overall,the1 mightsmell Weeffects following

**6.2****-**Performance**2** **Detector**

*Research*When ceeded We*ablation*studytrain- ingexperimented i.e., step, thehyper-parameter performance

Within-projectCross-project

0.037

0.428

0.428

0.661

0.012

0.001

0.001

Pagef455

0.007

0.559

0.559

0.042

0.001

0.007

0.022

0.000

0.001

### 123


---

<!-- Página 16 -->

55agef4Empirical Software Engineering (2024) 29:55

also performanceaddress**RQ**, computed2 eral*precision*,*recall*,*F-Measure*(Baeza-Yates *Matthews*(*MCC*)(Baldietal.2000),*Area Under* *-*. Weconclusions Nemenyi1963) overtest used the between MCC used latter Multiple2004). level,grayothers. Inthe theindicated thethe different.lastnemenyifunction

*Analysis*Our both within-theÞrst discuss results informedsplit analysis strategy. *Ablation*To outcomewhich have been**RQ**reported1 a*non-null*information features ablationnot of These sidering metricsbuilt detectorsconÞgurations for smells. foreach *Leave-One-Out*.detailed reported2023), detectors inghand, Þnding metrics whenthe Þnding theorthogonal fashionstep, observethat includes and reason,

4[https://www.r-project.org/](https://www.r-project.org/)

### 123

2011),

1996)and

4

**RQ**: the1


---

<!-- Página 17 -->

Pagef455Empirical Software Engineering (2024) 29:55

*Within-project*Theuseach project—7,128run smellsonlybest conÞgurationsmell appendix2023). Looking1, couldmedian*Random* on*Eager*,*Mystery*,and*Resource*isother algorithms0.09 andonline appendix2023). contrast,*Test*,*Naive*seems tosmell0.01. Friedman showed the*Eager*and*Resource*do signiÞcantto smells to2 plots thesmells Wefor smells,*Eager*and*Resource*, performed*Mystery*, *Random*and*Decision*areothers with a following*Random*for*Eager*,*Resource*,and*Mystery* *Guest*.*Naive*will*Test*. Concerning statisticallydistributions*Mystery*.

0.75

0.50

0.50

0.25

0.25 MCC − Eager Test

MCC − Mystery Guest

0.00

0.00

teststyesyesrtronsvmsvmapbaedaboostrceptronomforesomfoiveadabooaapepercndnaivebnrdecisiontredecisiontreerandr ultilayemmultilayer

0.8

0.60.06

0.4 0.04

0.2 MCC − Test Redundancy

MCC − Resource Optimism

0.0

0.00

tstmeseyesytreetsvsvmaboostfores vomivebadaboostadaerceptronppercepndnainarrdecisiontreedecisionrrayelayetiulmmultila

**Fig.**BoxplotMCCall within-project

### 123


---

<!-- Página 18 -->

55agef4Empirical Software Engineering (2024) 29:55

3.5

2.5

2.0

Likelihood MCC Eager Test

Likelihood MCC Mystery Guest

svm − 3.07

svm − 3.05

adaboost − 3.59

adaboost − 3.50

naivebayes − 2.64

naivebayes − 3.59

decisiontree − 4.11

decisiontree − 3.63

randomforest − 4.11

randomforest − 3.70

multilayerperceptron − 3.48

multilayerperceptron − 3.53

8

46

2

2.5

Likelihood MCC Test Redundancy

Likelihood MCC Resource Optimism

svm − 3.00

svm − 3.22

adaboost − 3.00

adaboost − 3.67

naivebayes − 6.00

naivebayes − 2.93

decisiontree − 3.78

decisiontree − 3.00

randomforest − 3.87

randomforest − 3.00

multilayerperceptron − 3.54

multilayerperceptron − 3.00

**Fig.**Thesmells MCC. theerror95% 60% ofa

Figures3and4show distributionsNemenyi each We the*Eager*and*Resource*—*BorderlineSMOTE*seems higher*Mystery*,the*Random*classiÞer, any vation*Test*,performance notin Þndings tions showing balancing detection2019a). Therefore, best machinesmells(i) *Random*with*Borderline-SMOTE*for*Eager*,for*Mystery* *Guest*,*Random*with*Borderline-SMOTE*for*Resource*,*Naive* *Bayes*for*Test*. The performancewithout whether to It importantthat, consideredneeded aggregate results performance2002). cesMCC. outproduceall By someequal

### 123

3.5  3.5  4.5


---

<!-- Página 19 -->

Empirical Software Engineering (2024) 29:55Pagef455

0.75

0.50

0.50

0.25 0.25

MCC − Eager Test

MCC − Mystery Guest0.00 0.00

−0.25

_RF_RFr_RF2er_RFForestvoounder_RFunder1_RFadasyn_RFadasynmsunder3_RFsssunderlinesmote_RFsmoteosmoteover_RFRandom ForestRandommissunder2_RFmissmimissunder3_RFrandomrrmirrandoearearmissunder1_RFborderlinesmote_RFbordernneaneannearnear

0.75

0.06 0.50

0.25 0.04

MCC − Test Redundancy

MCC − Resource Optimism0.00

0.02

−0.25

FBFFFFFBFstesNRRRNBRy_RF___R_aorene_NBrer_rBver_Rver_der3er2_syn_NBdedm Fveindender3_NodadasysmotsuaaeeomomunNandnnssunder1_RssalilindrrsmoteoaRrrmissunrmirandoarmissundordeeaeeabbordennearminnnearmissunea

**Fig.**Boxplotsmells in

wetested*Eager*, *Mystery*, projects*Resource*,*Test*. Table6shows achieved*Precision*,*Recall*,*Accuracy*,*F-* *Measure*,*MCC*,and*AUC-PR*.the approachesmaximum*Eager*(i.e., 51%). Analyzing MCC,performance*Test*) to*Mystery*).hyper-parameternot improve

*Cross-project*Regarding cross-projectperformed same *ablation*study our2023),discuss Nemenyi distributionsmellvarious techniques. Differently within-projectfound*Ada*to best classiÞer*Eager*and*Support*for*Resource*in project*Mystery*and*Test*, best classiÞers as*Random*and*Naive*, Figure5reports rithmsobserve, performance with MCC theandfound

### 123


---

<!-- Página 20 -->

55agef4Empirical Software Engineering (2024) 29:55

6

5.0

4

2

3.5

Likelihood MCC Eager Test Balanc.

Likelihood MCC Mystery Guest Balanc.

adasyin_RF − 4.97 adasyin_RF − 4.69

smoteover_RF − 5.60

smoteover_RF − 5.00

Random Forest − 5.76

Random Forest − 5.55

randomover_RF − 4.88 randomover_RF − 5.14

randomunder_RF − 5.56 randomunder_RF − 4.38

borderlinesmote_RF − 5.59 borderlinesmote_RF − 5.36 nearmissunder2_RF − 5.45 nearmissunder1_RF − 5.52

nearmissunder2_RF − 4.36 nearmissunder1_RF − 4.39 nearmissunder3_RF − 4.70 nearmissunder3_RF − 3.10

8

68

6

24

24

0

Likelihood MCC Test Red. Balanc.

Likelihood MCC Resource Opt. Balanc.

adasyin_RF − 5.92

adasyin_NB − 5.67

Naive Bayes − 5.67

smoteover_RF − 5.42

smoteover_NB − 4.67

Random Forest − 5.54

randomover_RF − 3.42

randomover_NB − 4.67

randomunder_RF − 4.54

randomunder_NB − 4.67

borderlinesmote_RF − 6.38

nearmissunder2_RF − 4.08 nearmissunder1_RF − 4.81 nearmissunder3_RF − 4.88

borderlinesmote_NB − 5.67 nearmissunder1_NB − 5.67

nearmissunder2_NB − 3.67 nearmissunder3_NB − 4.67

**Fig.**Thethe Nemenyitheerror95% conÞdencerank of

**Table**Aggregate*Precision*,*Recall*,*Accuracy*,*F-Measure*,*MCC*,and*AUC-PR*without “w/o HT”) with (i.e., setting

PrecisionRecallAccuracy

Testw/ow/ow/w/ow/

Eager0.47

Mystery

Resource

Test0.08 0.01

F-MeasureMCCAUC-PR

Testw/ow/ow/w/ow/

Eager0.50

Mystery

Resource

Test0.01 0.01

### 123

6.5


---

<!-- Página 21 -->

Empirical Software Engineering (2024) 29:55

0.4

0.2

0.0

MCC − Eager Test Cross −0.2

−0.4

ver_ABder_ABooda BoostAadasyn_AB smotemissunder2_ABrandomrrmissunder1_ABrandomun borderlinesmote_ABneaneanearmissunder3_AB

0.50

0.25

0.00

MCC − Resource Optimism Cross −0.25

MM SVM_SV over adasyn_SVM rlinesmote_SVMsmoterandomover_SVrandomunder_SVM bordenearmissunder1_SVMnearmissunder2_SVMnearmissunder3_SVM

**Fig.**Boxplot dationsmells

experimented butions several some resultsmore than*Test* any reported can thus Based with*NearMiss2*for*Eager*detection, *Mystery*detection,*SVM*with*Random* detection, (iv)*Naive*for*Test* Table7reports *MCC*,and*AUC-PR*of The maximum*Mystery* 0.01 to Finally,

Pagef455

0.6

0.4

0.2

0.0

MCC − Mystery Guest Cross

−0.2

RF er_r3_RFForestvver_RFeounder_RFunder1_RFadasyn_RF ssandomismoteoandomRmissunder2_RFrrrmissundra borderlinesmote_RFneneanearm

0.04

0.02

0.00

MCC − Test Redundancy Cross −0.02

esNBNBNBNBy_NBrr1_NBveee Ba nder2_NBadasyn_NBNaivnesmote_ssulindomover_smoteondomunder_rara bordernearmissunder3nearmissundnearmi

6, canthe *Eager*.*Mystery*shows

.

*Ada* *Random*with*NearMiss1*for for*Resource* detection. *Precision*,*Recall*,*Accuracy*,*F-Measure*,

(40%),

*Mystery*.

### 123


---

<!-- Página 22 -->

55agef4

6.0

4.0

MCC Eager Test Balanc. Cross

Ada Boost − 5.05

adasyn_AB − 5.16

smoteover_AB − 4.87

randomover_AB − 5.05

randomunder_AB − 5.13

borderlinesmote_AB − 4.51 nearmissunder3_AB − 4.75

nearmissunder1_AB − 5.17 nearmissunder2_AB − 5.31

4.0

MCC Resource Opt. Balanc. Cross

SVM − 4.48

adasyn_SVM − 5.29

smoteover_SVM − 5.33

randomover_SVM − 5.34

randomunder_SVM − 5.39

nearmissunder2_SVM − 4.43 nearmissunder3_SVM − 4.63 borderlinesmote_SVM − 4.82 nearmissunder1_SVM − 5.30

**Fig.**Thethe Nemenyitheerror95% conÞdencerank of

It importantthat also forhyper-parameter optimization not

**Answer****.**Thesmell2 generally better ter ofhyper-parameternot the

**-****6.3****3** **Smell**

*Research*While results learning-based smellnot

### 123

5.0  6.0  5.0  6.0 Empirical Software Engineering (2024) 29:55

4.5

3.0

MCC Mystery Guest Balanc. Cross

adasyn_RF − 5.21

smoteover_RF − 5.37

Random Forest − 5.15

randomover_RF − 5.39

randomunder_RF − 5.47

borderlinesmote_RF − 5.22

nearmissunder2_RF − 3.72 nearmissunder3_RF − 3.92

nearmissunder1_RF − 5.55

5.0

4.0

MCC Test Redund. Balanc. Cross

adasyn_NB − 5.12

Naive Bayes − 5.12

smoteover_NB − 5.12

randomover_NB − 5.12

randomunder_NB − 4.90

borderlinesmote_NB − 5.12

nearmissunder1_NB − 4.81 nearmissunder2_NB − 4.81 nearmissunder3_NB − 4.87

**RQ**reported2


---

<!-- Página 23 -->

Empirical Software Engineering (2024) 29:55

**7**Aggregate*Precision*,*Recall*,*Accuracy*,*F-Measure***Table** HT”) with (i.e., “w/

PrecisionRecall

Testw/ow/ow/w/ow/

Eager0.27

Mystery

Resource

Test0.004

F-MeasureMCC

Eager0.38 0.39

Mystery

Resource

Test0.01 0.01

markthe could real usefulnessmodel thanwould recommend ofthecouldextent which technique weaknessessmell ularly, studysmell the

tsDetect(Peruma2020)tool as art smell2021) detect highest smell of smells of*Eager*,*Mystery*,and*Resource* detectednumbermethod production instancesdatabase testFileinstance ornotExist(). TeReDetect(Koochakzadeh Garousi2010)tool as to*Test*smell coverage analyzingtests Darts(Lambiase2020)*Eager* metric this an Darts(Lambiase2020). et2018).*Eager*instances calls aremethod; theconstituent and,metric

Pagef455

,*MCC*,and*AUC-PR*without

Accuracy

AUC-PR

tsDetectcould .Þrst is

exists(),isFile(),

relies

### 123


---

<!-- Página 24 -->

55agef4Empirical Software Engineering (2024) 29:55

We heuristicsame**RQ**to2 athey couldparameter: ensured the wrongemployed same the*Precision*,*Recall*,*F-Measure*,and*MCC*.**RQ**,2 wemachine detector baseline(Nemenyi1963) the of

*Analysis*Similarly**RQ**, split analysis2 strategycouldmachine techniques*Within-project*Figure7reports outcome obtainedcomparing that*Eager*, better*Mystery*,*Resource*,and*Test* *Redundancy*,higherno statistically Tables8and9show aggregate*Eager*,*Mystery*,and*Resource* *Optimism*over

2.4

3.0

2.2

2.5

2.0

1.8

Likelihood MCC Eager Test Smell

1.6

Likelihood MCC Mystery Guest Smell

darts − 2.26

tsdetect − 1.99

tsdetect − 1.93

ML_cross − 2.59

ML_cross − 1.86

ML_within − 3.16

ML_within − 2.21

2.6

0.5

1.4

Likelihood MCC Test Redundancy Smell

Likelihood MCC Resource Optimism Smell

tsdetect − 1.75

ML_cross − 1.33

teredetect − 1.67

ML_within − 3.00

ML_cross − 1.94

ML_within − 2.31

**Fig.**Themachinefour test rankedtheerror indicate 95% top

### 123

3.5  2.0  1.8  2.2  1.5  2.5  3.5


---

<!-- Página 25 -->

Empirical Software Engineering (2024) 29:55

**8**Aggregate**Table** approachTsDetect

Test

Eager

Mystery

Resource

Test

Eager

Mystery

Resource

Test

Eager

Mystery

Resource

Test

Eager

Mystery

Resource

TsDetectandDarts formance machine

**Table**Aggregate *Precision*,*Recall*,*F-Measure* and*MCC*, machine Darts

*Precision*,*Recall*,*F-Measure*

Precision

ML

0.470.37

0.42

0.21

F-measure

ML

0.500.23

0.43

0.27

Precision

MLTSDETECT

0.270.35

0.40

0.18

F-measure

MLTSDETECT

0.380.22

0.40

0.25

).three smells *Precision*

Precision, Test

Eager 0.47

F-Measure

Test

Eager 0.50

Precision

Test

Eager 0.27

F-measure

Test

Eager 0.38

,and*MCC*,machine

Recall

0.53

0.34

0.31

MCC

0.27

0.39

0.24

Recall

0.64

0.37

0.32

MCC

-0.01

0.30

0.22

,*F-Measure*,and *Recall*, notice

0.33

0.32

0.30

0.30

Pagef455

0.17

0.44

0.37

0.06

0.29

0.15

0.16

0.40

0.37

0.06

0.29

0.17

, *MCC*compared

Recall

0.31

MCC

0.04

Recall

0.31

MCC

0.03

### 123


---

<!-- Página 26 -->

55agef4

theTsDetecthas of*Mystery*and*Resource*. TheDartsconÞrmed the formed vs. To analysisprediction and, computed*j* and The conÞrms previous machine more smells heuristic-based *Redundancy*.For*Mystery*and*Resource* isheuristic-based

*Cross-Project*Different While terms Moreover,notice machine is, conÞguration, thegenerate The deserves reported10.performance (close particularly Looking resultsmachinesmells heuristic-basedsmells. *Test*,

**Table**Aggregate*Precision*,*Recall*,*F-Measure* approachTeReDetect

Precision

TestMLTeReDetect

Test0.010.00

F-Measure

TestMLTeReDetect

Test0.010.00

Precision

TestMLTeReDetect

Test0.010.00

F-Measure

TestMLTeReDetect

Test0.010.00

### 123

Empirical Software Engineering (2024) 29:55

andmissedbym*i*

, amount

*Test*

,and*MCC*,machine

Recall

ML

1.00

MCC

ML

0.01

Recall

ML

0.97

MCC

ML

0.01

*i* and*i**j* .*j* 11.

*Eager*and*Test*

TsDetectin

,

TeReDetect,

12),

*Eager* Darts

0.00

−0.01

0.00

-0.01


---

<!-- Página 27 -->

Empirical Software Engineering (2024) 29:55

**11**Thereported results each**Table** comparing

Eager

ML∩Darts*corr**corr* 26%

ML∩TsDetect*corr**corr* 12%

Mystery

ML∩TsDetect*corr**corr* 72%

Resource

ML∩TsDetect*corr**corr* 60%

Test

ML∩TeReDetect*corr**corr* 0%

and for*Mystery*and*Resource* infeasible learning

**Table**Thereported results each comparing

Eager

ML∩Darts*corr**corr* 26%

ML∩TsDetect*corr**corr* 15%

Mystery

ML∩TsDetect*corr**corr* 14%

Resource

ML∩TsDetect*corr**corr* 11%

Test

ML∩TeReDetect*corr**corr* 0%

ML\*corr**corr* 53%

ML\*corr**corr* 76%

ML\*corr**corr* 5%

ML\*corr**corr* 13%

ML\*corr**corr* 100%

TsDetect.be ,*Test* TereDetect 12).

ML\*corr**corr* 60%

ML\*corr**corr* 78%

ML\*corr**corr* 67%

ML\*corr**corr* 71%

ML\*corr**corr* 100%

Pagef455

\ML*corr**corr* 21%

\ML*corr**corr* 12%

\ML*corr**corr* 23%

\ML*corr**corr* 27%

\ML*corr**corr* 0%

, but

\ML*corr**corr* 14%

\ML*corr**corr* 7%

\ML*corr**corr* 19%

\ML*corr**corr* 18%

\ML*corr**corr* 0%

### 123


---

<!-- Página 28 -->

55agef4

**Answer****.**The3 thanin within-project thatheuristic most testmachine approach *Test*, approaches be

**7**

Ourdiscussion, orate on section.

**7.1**

According heuristic-basedseems toresult tigationlow performance terms evaluation eredcross-project itproblem themachine learning-based dictions within-empirical such as*Optimistic* smelly; the*Pessimistic* non-smelly; (iii)*Random* non-smelly.comparison,as deÞnition effectivesmell thethose ifsolution, might indicatedifignores inputbasedwould themselves Following Type Ifalse respectively. Table13reports themachine *Constant*and*Random* smells. instance, false lower*Optimistic* same

### 123

Empirical Software Engineering (2024) 29:55

*Eager*and *Mystery*and*Resource*both

*dummy*classiÞers, classiÞers

, , ,

2012),

*Optimistic* , *Eager*was20% and*Random*, *Pessimistic*was


---

<!-- Página 29 -->

Empirical Software Engineering (2024) 29:55

**13**Comparisonsmellthe**Table** classiÞers

ML-based

TestType IType II

Eager1,524

Mystery817

Resource481

Test2,302

Pessimistic

TestTypeType

Eager02,648

Mystery1,487

Resource688

Test040

especiallyabsolute *Redundancy*, Basedtheeager to Whenthe to*Random*for considered smells, indicatinginterpretingcould machine test thanfeatures conÞgurationcorrectly of Thecross-project shown14, I machine *Constant*and*Random*alternatives. *Eager*:false previous*Random* waspresenceType couldsimilarmachine and*Random*. Onthe detectornegatives: suggests eithersuitable forresults suggest research reachingcurrent toothe ensemble*Random*)three of smells. the and*AdaBoost*) best classiÞersof smells.

Optimistic

Type

6,118

5,576

3,169

Random

Type

2,995

2,089

,the

Pagef455

Type

Type

*Test*

*Optimistic*

*Random*

### 123


---

<!-- Página 30 -->

55agef4Empirical Software Engineering (2024) 29:55

**14**Comparisonsmellthe**Table** classiÞers

ML-based

TestType IType II

Eager4,578

Mystery955

Resource492

Test9,105

Pessimistic

TestTypeType

Eager02,699

Mystery1,534

Resource730

Test040

Randomis Bootstrapthe trees isensemble learning help achievetheirleverage obtained*Naive*,*Multi-layer* *Machine*). thiswork targetingnatural which data

∠**Take**Oursmell ter whenargue thatclassifying at tivelyoffeatures exploited—which topresence advances and

**7.2**

The the concerns andmultiple orsmellablation studies**RQ**and**RQ**)12 to

### 123

Optimistic

Type

6,934

8,099

8,903

9,593

Random

Type

4,462

4,822

,and

Type

Type

*Support*


---

<!-- Página 31 -->

Empirical Software Engineering (2024) 29:55Pagef455

performance couldorthogonalityfeatures.results for**RQ**suggest performance3 possiblysmell Indeed, ofwereperformance in2020;2010; et2020).for aspects provideshould addressed thefalseheuristic-based approaches. Ourclassify root causes smell To4. Þrst the potentialerrors. false positive discussed—this towas implementedSkypemeet- ing examplesreasonsfailures approach.Þnally additional for smell,additional analysis, assmell surement othermay provide to

*Eager*Whentest the

*1.*First andtest serious*Eager*enclosedDeursen ettest*“test method* *tested”*(Van Deursen2001). considering conceptualmachine approach explicitlydifference*intra-method*and*intra-class*unit and2008).cases, should1992; Young2008; Silva1998). the*individual*methods code,*intra-method*(Pezzè Young2008)or*basic-unit*(Orso Silva1998).

### 123


---

<!-- Página 32 -->

55agef4Empirical Software Engineering (2024) 29:55

On ofbe covered*intra-class*(Pezzè Young2008)or*unit*(Orso Silva 1998).that exercises productionthemore productionshould be Unfortunately, deÞnition2001) account unitinterpretation detectors.vast majority presence*Eager*, should be

1@Test 2publictestSetDataWithVersion()throwsException 3ZKUtil.createWithParents(ZKW,"/s1/s2/s3"); 4intv0"/s1/s2/s3"); 5assertEquals(0, 6

7ZKUtil.setData(ZKW"/s1/s2/s3", 8intv1"/s1/s2/s3"); 9assertEquals(1, 10

11ZKUtil.multiOrSequential(ZKW, 12ImmutableList.of(ZKUtilOp.setData("/s1/s2/s3", toBytes(13L),false); 13intv2"/s1/s2/s3"); 14assertEquals(2, 15}

**Listing**Example*Eager*.

TheZKUtilofHBaseproject, a mentingprovide synchronization.issetDataand forexercises ductionsetData, i.e.,createWithParentsandmultiOrSequential. the classiÞedcalls performedrequiredsetData methodbe withoutthis*Eager* Basedargue deÞnition revisited *2.*Whentest cies’ expected2000). tocases, of have to yetmetrics practices.

### 123

.


---

<!-- Página 33 -->

Empirical Software Engineering (2024) 29:55

1@Test 2publictestWhenValidPreProcessorsSet() 3createManager(); 4

5configureValidUriLocators(mockFilterConfig); 6Mockito.when(mockFilterConfig.getInitParameter( ConfigurableProcessorsFactory.PARAM_PRE_PROCESSORS)). thenReturn("cssUrlRewriting"); 7assertEquals(1, size()); 8}

**Listing**Example*Eager*due

AstesttestWhenValidPreProcessorsSet 5framework,abehavior ConfigurableProcessorsFactoryclass andtest. Inthis call. deÞnitionsmell *3.*The impacted itedno class related methodmetrics characterize*Eager*instances under toamountmethod putecase. Unfortunately,reliable. tors and ingname testDoubleConverterTest.java class having DoubleConverter.java). searchtest theindividual methods suite nique. detectiontwo considerations traceabilityhas imented2014; 2014), lessslicing-based Ofsmell of provideÞeld discussingthe informationdetection. reason

5TheMockitoframework:[https://site.mockito.org](https://site.mockito.org).

)

Pagef455

leveragesMockito

Test(e.g.,

*Eager*

2009;

2014)).

### 123


---

<!-- Página 34 -->

55agef4Empirical Software Engineering (2024) 29:55

1publictestCacheInstanceWithManyThreads() BrokenBarrierExceptionInterruptedException 2

3//ppressedsakedability. 4}

**Listing**Example*Eager*due

TheEmbeddedJSPResultTest been classiÞed*Eager*instance. tiontestEmbeddedJSPResult class.another i.e.,JSPRuntime,the testCacheInstanceWithManyThreadsmethod.code EmbeddedJSPResultclass is

1publicEmbeddedJSPResultextends StrutsResultSupport 2protectedvoiddoExecute(String ActionInvocationinvocation)throwsException 3JSPRuntime.handle(StringUtils.removeStart( finalLocation"/")); 4} 5}

**Listing**Productiontraceability naming

AsEmbeddedJSPResultjust doExecute,handle class.EmbeddedJSPResultdoes notmethod linkedtestCacheInstanceWithManyThreadstest this reason, testcompute metrics In may*conceptual* givenlink isthe is actualthe use test-to-code2014;Parizietal. thesmellthe example inform possible patternnaming theEmbeddedJSPResultclass (Listing (Fowler Beck1999), operationscomplexity costsBeck1999). other analysisthe presence thetest our

*Mystery*When *mism*, the

*1.*Thefalse both testand for*Eager*.

### 123

throws

and

production

ofJSPRuntime

link

2014)

*Middle*

and*Resource*


---

<!-- Página 35 -->

Empirical Software Engineering (2024) 29:55

mistakenly*Mystery*, instancespresent. of*Resource*,detect mechanism existence/status mocksbehavior hence

1@Test 2publicshouldReturnNullValueFromSession 3IfNoEntryWithSpecifiedKeyExists() 4StringtedKey"FooBar"; 5

6when(mockSession.get(anyString())).thenReturn( 7when(mockRouteContext.getSession()).thenReturn( mockSession); 8when(mockPippoWebContext.getRouteContext()).th mockRouteContext); 9

10PippoSessionStorenew (); 11

12assertThat(sessionStore.get(mockPippoWebContext expectedKey), 13

14verify(mockSession 15verify(mockRouteContexttimes(1)).getSession(); 16verify(mockPippoWebContexttimes(1)).getRouteContext() ; 17}

**Listing**Example*Mystery*and*Resource*due

Aperformance *Guest*and*Resource*detection of testshouldReturnNullValueFromSessionof a*Java*—makesof navigation instance. erroneously*Resource*instance. thatperformance therefore, the *2.*As aincomplete *tery*(919 test*Resource*(453 test handling2001): deÞnition provide aof et2001) examplessuppose original deÞnition open theless, external databases Therefore,numberexample Listing

Pagef455

null);

enReturn(

*Mystery*

Pippo—

*Mystery*

*Mys-*

### 123


---

<!-- Página 36 -->

55agef4Empirical Software Engineering (2024) 29:55

1@Test 2publicshouldFindValidWebjar()throwsException 3assertNotEmpty(victim.locate("webjar:jquery.js")); 4assertNotEmpty(victim.locate("webjar:jquery jquery.js")); 5assertNotEmpty(victim.locate("webjar:/jquery jquery.js")); 6}

**Listing**Example*Mystery*and*Resource*due incomplete operationalization

ThecaseshouldFindValidWebjartestWro4J project. checksthenot tifypotential smell. better prehensive*Mystery*and*Resource*instances

*Test*The*Test* *dancy*smell closethey could ofclose In

*1.*As4,instances *Test*. letproperties terizing test machine the *2.*The smellredundancy whichcases). usexample Listing

1@Test 2publicshouldParseSingular() 3finalTimeSpanspanTimeSpan.valueOf("1); 4assertThat(span.to(SECONDS), 5} 6

7@Test 8publicshouldParseNonLowerCase() 9finalTimeSpanspanTimeSpan.valueOf("17); 10assertThat(span.to(SECONDS), 11}

**Listing**Example*Test*.

TheshoudParseSingularandshoudParseNonLower CasetestRiptideproject. TeReDetectandcases the aimvalueOfmethodis suppliedcase may look like *Test*,thevalueOfmethod

### 123


---

<!-- Página 37 -->

Empirical Software Engineering (2024) 29:55

two with ansecond of anseconds).two methods asbetest would tunately, pair redundancy test wesemantic discriminate

Concluding argumentation identiÞedchallenges researchers inanalysis currently detection may failanalysis. Overall,the of This observation mocking, naturally codeassessed. hope that researchersrealistic current

∠**Take** of how test smells,incomplete tion revealedpossible should

**8**

Multiple sectionmainhow we based

*Construct* Þrsttest smellrelied In casesopted theprovide toapproached dataset through to smelliness inspectors Þndsmelliness the process

shouldParseSingular

OurdeÞnition

Whenrelationship

shouldParseNonLowerCase

exercises

Pagef455

with

### 123


---

<!-- Página 38 -->

55agef4

coherence similarmethods was smells measure manualone by and tooverallthe lackan subjectivethis reason, that the toevolution. Athe consideredheuristic the speciÞcallyrelied research.comparison based smellheuristic was and analyses,limitations with insightssmell

*Conclusion*Astooutcome, a providing models: machine this computed informationmodels 1986).independent contributing possiblemachine learningopted an 2019)contribution identifying We have work webest algorithm. the readability,discuss et2023)use impact In**RQ**,2 undercase ing.scopeprovide therelied validation tion2009).

### 123

Empirical Software Engineering (2024) 29:55

2012).allowed

2023);

2014).

**RQ**towe1

*ablation*study

6; online

1974)

2007).

κ=0.67)


---

<!-- Página 39 -->

Empirical Software Engineering (2024) 29:55

ÞnallyNemenyi (Nemenyi from a

*External*As generalizabilitydataset based hold when thisbe madesmell Wang2021). appendix2023).

**9**

The smellsource of whichinvestigated the (1) 28,248 14,256cross- project(3) tosmellÞndings of though We qualitativeperformance based smell view of(2)root-causes prevent smell insightschallenges the nity To 1. researchers tosmells 2. smelluse the 3. insights practical to 4. empirical beextend Theinput researchconceptualizing deÞnitions designingconcept Furthermore,natural languagesmell analyze

1963),Þndings

*Java*.our

Python

2023)

code (VavrováZaytsev

Pagef455

2017;

### 123


---

<!-- Página 40 -->

55agef4

forthey should and tomostalso plan production performance ourwork

**Acknowledgements**Fabiosupport through SNFwork been EMELIOTMUR funded PRIN 2020W3A5FY).

**Author****Valeria**: Original**Dario** idation,**Fabiano** Writing**Dario**: **Ferrucci**: Writing

**Funding**Open ment.

**Data Availability**Thedata included ular: datasetsanalyzedadditional resourcesstudy, available github.com/darioamorosodaragona-tuni/ML-Test-Smell-Detection-Online-Appendix

### Declarations

**Competing**The relationships

**Open**This article permitsreproduction appropriatethe and article’s notyouris regulationwill need To[http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)

### References

Aljedaani (2021) Antoniol and Azeemcode systematicmeta-analysis. Baeza-Yates England: Baldi for Bavota testtheir software

### 123

Empirical Software Engineering (2024) 29:55

: :

**Fabio**

*Python*

:

.

.

code.

**Filomena**

https://


---

<!-- Página 41 -->

Empirical Software Engineering (2024) 29:55

votasmellsempiricalBa study. Beck Bellertests with Github. Bergstra13(Feb):281– 305 Breiman Catolinomobile empiricalsystems. pp Catolino J Catolino developer-related Chawla Bowyer Kegelmeyer (2002) J Cohen De projects. Detest smells. symposium Di prediction Duda Wiley Fentonpractical Fernandes detectionassessment p18 Fowler Freund99. 124–133 Garousicode:academia. Syst Gousioschallenges opment: integrator’s1. Press, Grano(2019) ofcode. Grano(2019) quality Greilersmells. Softwarevalidation Haiduc during on Han learning. HarroldFitzpatrick Proceedings He Y,Li International IEEE, Heckmanself-selection. Koochakzadeh Eng Kramer Kruchten 29(6):18–21

Pagef455

### 123


---

<!-- Página 42 -->

55agef4

S,Lambiase refactoring: Lipton ßawsstymie Mackinnon Examined Maierits In: IEEE, Maldonadoquantifying In: Marcus maintenance. Martinsthecode quality McHugh (2012) McMinn 14(2):105–156 Meszarospatterns:code. Myers Sandler Nemenyi Noble (2006)Biotechnol O’brienvariance 41(5):673–690 Orso A,research 4th society Palomba maticallycode: testing. Palombasmell niques.evolution. Parizi Dabbaghchallenges between and Pecorelli metrics. Pecorelli based for Pecorellimachine for Press, Pedregosa R,Perrot Duchesnay Scikit-learn:12:2825–2830 Perez approaches. Perumasmells detectionsymposium the Pezzèanalysis:techniques. Sons Pontillo based smell Smell-Detection-Online-Appendix Pontilloßakiness national Pontilloßakiness 27(7):187 Quinlan

### 123

[https://github.com/darioamorosodaragona-tuni/ML-Test-](https://github.com/darioamorosodaragona-tuni/ML-Test-)

Empirical Software Engineering (2024) 29:55


---

<!-- Página 43 -->

Empirical Software Engineering (2024) 29:55

A,Qusef slicing textual Refaeilzadeh 532–538 Rwemalika tests. Sakshaugpassive (opt-out) Method Samarthyam(2017)debt. Springer, Schapire (2013) SheldonThompson usein ofInt Spadini empirical Spadini code quality.evolution. 1–12 StoneB (Methodol) Taud H, narios. Tufano tigation nature pp VanBerghcode. onßexible Vancases units In:reengineering. Vanthe approacheager Vavrovájava? arXiv:1703.10882 Wang In: 593–605 WohlinOhlsson engineering. Yen ancedautomation. Zhangsuite on

**Publisher’s**Springer institutional

[https://doi.org/10.1016/j.jss.2013.10.019](https://doi.org/10.1016/j.jss.2013.10.019)

Pagef455

### 123


---

<!-- Página 44 -->

55agef4

### Authors

**1,2****Valeria**·**Dario** **1****Dario**·**Filomena**

Dario dario.amorosodaragona@tuni.Þ

Fabiano [fpecorelli@unisa.it](mailto:fpecorelli@unisa.it)

Dario [ddinucci@unisa.it](mailto:ddinucci@unisa.it)

Filomena [fferucci@unisa.it](mailto:fferucci@unisa.it)

Fabio [fpalomba@unisa.it](mailto:fpalomba@unisa.it)

1Software 2Software 3Tampere

### 123

**1**·**Fabio**

Empirical Software Engineering (2024) 29:55

**3**·**Fabiano** **1**

**1**·


---

