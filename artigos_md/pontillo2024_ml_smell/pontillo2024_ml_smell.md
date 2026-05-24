<!-- Página 1 -->

### An

###

###

###

### Anomaly

###

###

###

12322ValeriaLuanaIvan Machado,FabioFilomena 1Software [valeria.pontillo@vub.be](mailto:valeria.pontillo@vub.be) 2Software [lalmeidamartins@unisa.it](mailto:lalmeidamartins@unisa.it),↵[errucci@unisa.it](mailto:errucci@unisa.it) 3Federal [ivan.machado@ufba.br](mailto:ivan.machado@ufba.br)

**Abstract**

Testcases.demonstrated their harmfulness↵ectiveness,such, quality of↵ectedqualitya↵ mightanomalies. this paper, challenge approachesstatistics↵ectiveness smells,Eager,Mystery,Resource,Testonavaprojects. compare resultsmachineOur that↵ectiveness keyF-MeasureofEager using statisticalRecallisclusteringNevertheless, anomalyRecallthansmells. TheF-Measurevaluescurrent detectionWestudy qualitative the

Keywords:Test

**1.**smellycases can↵ecting detection theTheIn heuristicmaintaining to smells,this, deÞned implemented.predeÞnedor rules and thresholds besoftware capture fullresolution that↵ectivenesscontext Toor iescode defects tectionplore smells. piricalqualityTestsymptoms suite [11, 22]. Consequently, hypothesize qualitychoices Several of↵ectede↵ects smellse↵ective- thea↵ectedness tosmellsthe code quality. aThis paperuse methodssmellsanomalysmells. Mostcally, thatestablisheddi

PreprintDecember 2024

The detection

SpeciÞ-

↵er


---

<!-- Página 2 -->

icantly norm. prior [11, argue cases hibit notable cation applying techniques pervised extensiverisk of balanced Hence, paper e↵ectivenessidentifying four Mystery,Resource goal form when opposed ingintention thesebetter to their e↵ectiveness ate niques, and proaches heuristics machine TheÞndings. observethree forof the higher didstate-of-the-art ciallyRecall cates that test proachpotential developing approach.Lastly,qualitative for e↵ective All oursmells the ducesgroundwork forresults pos- itiveperformance lowerour valuable forguide ies anomalytest ologies, To this

1.An detection

2.Aresults de- lineate

3.Anscripts tostudyuse tobuild empirical

avaprojects: ,Test

Towe ↵erent anomaly

.

Eager

F-Measure

**Structure** lated work. byanalysis Theseare tionSection paper outlines

**2.**

This sectionreferences to, discussing smells be.Our

2.1. Anomaly datato viation majority Þnds extensive in fraud intrusioncyber-security software A regionclassify data pointHowever, ap- proach nature notion ferentthe that Accordingstarting the formulation the dataeach attribute ferent point ularnormal dataset.been plored thatcollec- tive have anomalously co-occurrence Another point to onlabels available, detectionbe tectiondataset labeled foranomaly tectionthelabeled for groups of structing unsupervised Lastly, anomaly nary ordata in- stances

3

Section


---

<!-- Página 3 -->

TablesmellsThe **DeÞnition** as threshold **Test** EagerA method2.2. ing TestsymptomsMysteryA Þles).choicesSeveral ResourceAnegative↵ectsexistencestate thekeyTestA studiesdi↵usion e↵ects smells suite.softwaredi↵u- sion smellssuites. basedperspectiveisdini↵ect from bothformer inter-quality, estedbetweenthedefect-proneness testlatter interestedboth test and production feasibilityan ically,appliedsmells. proaches identifyingvestigate↵usion their ware projects evaluatedstructural ings, demonstrating smells highly↵used in **RQ****1**classes, theirreduce code comparedTo anomalysmells? On↵orts pose methodsSince analyzed↵erent anomaly 16].proaches impact↵erently, tectingconsidered basedsmells the**RQ****.**To machine1 . gory ofeReDetect[14]detection smells? andeCReVis[33]),etector[34], Elec- tricTest[35], TEDDraDeTolDet[38]),**RQ****.**To cluster1 . testestHound[39]estEvoHound[40]).detection smells? tools focus↵erent categories↵ect ferentraclePolish[41], Taste[42], **RQ****.**To1 . tsDetect[15], JNoseTest[16]). tion smells? thecalculation (VITRuM JTDog[44]).Upon newmethods, compared andapproaches Complementary, somewesecond chinesmells. a**RQ****2** detect smells structural How do anomalytins heuristic-chinesmells. Kacemagreement Figureempiricalamong detection suggested sistedContextcationsmells. of**RQ**,1 Detection**3.** -**RQ**,**RQ**and**RQ**.212 report empiricalThegoalofper- engineeringtheACM/formance↵erent anomaly 1SOFT.i.e., statistical-basedtest smell 1detection,purposeofAvailable[https://github.com/acmsigsoft/](https://github.com/acmsigsoft/) proachesEmpiricalStandards.

4


---

<!-- Página 4 -->

### (1) Context Selection

### (2) Detection of test smells

### (3)

### Detection of test smells using

### Anomaly Detection

### Execution of heuristic-

### Execution of anomaly

### Execution of classical

### 66 open-source

### based approaches

### detection approaches

### approaches

### Java projects

### est smell detection

### Script to collect readability

EagerMysteryResourceOCSVM

### tsDetect

### and metrics calculation

### size and complexity

estGuestOptimismest

### with VITRuM

### metrics

### Machine

MysteryGuest

### models

Eager

### DAR

Resource

### [Metrics,

### est Smell label]

estOptimismK-meansDBSCAN

### Eager

### est

### est Redundancy

estest

### eReDetect

Redundancy

### Clustering

### algorithms

### Mystery Guest

### Resource Optimism

### (4) Data analysis

Boxplot

### Statistical

### Manual data

### Calculation of

### Calculation

### Execution of

### 9,633 test cases

### method

### Dataset

### validation

### performance

### projects

### overlap

### [metrics, label]

### evaluation

### metrics

### analysis

Figure

3.1.Whenperspective, adoption detectionThecontextof worththat thecollectedmanuallycases tered onnotfrom 66avaprojects. necessarilymation anomaly↵ermetricsexperimentation cantlybased**RQ**),1 . work foundationaltheir detectiontool to**RQ**.2 studiesqualityThe of↵ectedperform thea↵ectedthe tifyingMoredataset This datasetlargest,each test case, dataset allysmell

### 1,534

### 730

mation↵erent testEa- ture. The dataset↵erent characteristics,ger,Mystery,Resource,Test hencedancy.deÞnitionsmells. softwareprovidetotal number onfurtherscope

### 40

37.9% cases.cases

### 2,699

miningreadmeÞlesdoes not

### T

### T

thesmellcase be↵ected ricstiple testdataset wenumberploited.smell

### T

numberobservedtypes, haveEagerinstancesMys- theteryinstancesResource lateHTTPrequests responses,(7%),Testinstances

### Leaning

trationsequence, 61

###

testtotal smallest105

### 40

ual+1534+730=5,003) hasmediansmelly cases

### T

### ,

values1,875It also importantstudy 103, respectively fulltestindeed eredtionbaselines ofEager,Mystery,Resource,Test 3.2.Redundancy.split problem smellwhich amountThe ofglobalsencesmell testEager=28%;Mystery=15%;anomaly,

### using

Resource=7%;Test=0.4%).,Testindependently.

5

,

IF

### Approaches

LOF

### T

### TS

T

T

T

###

### baseline approaches

### ML

T

###

T

###


---

<!-- Página 5 -->

3.3.

To smellstructural tex- tual machine readyused proaches for Eager, analyzed testthe cohesion whether test i.e., by without ablesTestRedundancy lyzetests In↵ortcode perspectives, with two research

**Test** lines of complexityquality from the computed McCabe [55], whichlogical turn, can↵ect

**Test**Accordingprevious represents assessing code and [57]. Weenlarged ricspaper abrino siveencompass pects, methodThis integratesmetrics theWeimer [58], and (2) of

On hand,categories ricsoverall bilitiesthe sessing role of ablesmell tors. Metricsreadabil- ity plementing teststudy onlinedeÞnitions of

Resource

Mystery

the

Wenumber

,analyzed

,

↵er

**4.**

This section dress

4.1.

Before formedsuit- ability thepresence ingdata Indata each featurepotentially improve ability interpretation Asvalues whenskewness rics, proaches. sakereport skewness of We Cohesion, icantly↵erent from notpresence offurtherassumption ering smellsanomalies. whentest code, metrics,dataset anomalies may be

Table

**Test****Metric**

EagerNMC TMC MysteryNRDB NRF ResourceERNC FRNC TestPR SR

4.2.**RQ**:1 .

ThedeÞnition chine cusedOneClassSVM LocalOutlierFactor.algorithms sons: gorithms, anomalybe accordingthe stable ple62]. Particularly, are

6

standard

**Value**

4.06 -0.13 11.03 7.69 10.92 9.03 7.23 8.22

,IsolationForest

↵erent class

scaling.

,


---

<!-- Página 6 -->

**OneClassSVM**This algorithm the deÞnesinitial futurein belonging or outside frontier, anomalous

**IsolationForest**This isensemble basedExtremelymodel randomlya imum splits the ing forestparticular samples,

**LocalOutlierFactor**The local density sity densityits the↵erent from of sample

It important ically erate underanomalous fewer dataSMOTE, used in ance, not based pling distributionaccu- racy Wehyper-parameters ÞersRandomstrategy randomly plesbest combination ofF- Measure). learnlibrary thereported Toperformance anomalycomputed the-artPrecision,Recall,F-Measure Matthews cient(MCC)

4.3.**RQ**:1 .

Chandolacategories anomalystarts tion while sumes normal centroid, centroid. analyzed algorithm

technique

scikit

[69], and

**DBSCAN.**The tions with worksclose gorithmradius( ✏) minimumto sample). ahasThen, algorithm✏from the point.✏distance, the Alternatively, algorithm chosen if✏distance.

**K-means.**This is thatdistance centroid aims toK meanswithin-cluster (WCSS),sum of tween meansas- signs

To methods,algorithm di↵erent valuescorresponding for Krate of KWCSS reduction ered based culating standardthe di↵erent KidentiÞed K signiÞcantlyclustering threshold

Finally,performance anomalycomputed the-artprecision,recall,F-Measure[69], and Matthews cient(MCC) - 4.4.**RQ**:1 . Concerning**RQ**,1 . weboxplotas detect anomalies representationsummary including smallestmin), lowerQ1),upperQ3), themax).↵erence betweenQ3andQ1isInterquartile (IQR).thresholds anyinstance moreIQRlowerQ1orIQRhigherQ3 is Finally,statistical-based tionpreci- sion,recall,F-Measure[69], andMCC[70].

7


---

<!-- Página 7 -->

4.5.**RQ**:2 After tioncompared them tostrengths weaknesses tion we experimented make ofpredeÞned inate theex- ploited leveragelearn identify smells tionships As heuristic-basedselected proaches

**ts****D****etect****[15].**Wetool as state of smell to smells Eager,Mystery,Resource ticular, Þrst isnumber multiple method methods. test Finally, third methodFileinstance exists(),isFile(),notExist().The previously the ableoseTest[16] exactly same Detectensuredessential shared

**T****e****R****e****D****etect****[14].**We alongeCReVis[33], to dundancysmell.Thesmell code coverage analyzing paths.Whilesame TeCReVispresents

**D****arts****[48].**The TASTEThese the metrics instead similaritySpeciÞcally,Eager stances areactual by method; conceptual computed,constituent whether metric these, ofthus provided

These to test

demonstrated su ciently them. selectingwere ablee↵ectiveness↵ort detection heuristic-based As machineselection process previous uated performance forsame webest-performing each test smellparticular, previous [21]evaluated gorithmsthe four the EagerdetectiondaBoostwith NearMiss2 ancingMysterydetectionandom estwith NearMiss1;Resourcedetection portVectorMachineswith random. par- TestdetectionaiveBayeswith no These to and It important detectors cuted adjustments, and Similarly, thefollowed sames- To metricsanomaly precision,recall,F-Measure,MCC.

4.6.**RQ**-RQ:12Test In ducted the↵erences approaches validaterobustness Morestatistical byapplication↵er menyi used to↵erencesat- tempts,assumptionsin- normality notis sisFriedman to di↵er onver- iÞed normality Shapiro-Wilk [76]andfoundAmong the normallyp-value<0.05). we the[74], ple↵erent observations per testing[75],

8

For- up-


---

<!-- Página 8 -->

whichcontrols wise error determinestatistically inF-Measure experimented the↵erences anomalybaseline

**5.**

This section searchsub-research

5.1.

In of smelldis- tribution niquessmells. can allperformancemedian orallmachine learning-basedseem for

isolationforest

0.75

0.50

F1 Score 0.25 isolationforest

0.00Figure allsmells.

Concerning5 present performance est,Local 0.6 thatwhen run ing the to0.4 forTest Þrming previousfor sion, performance tohighest F1 Score0.2Recallis

0.0

Overall, **RQ**, testsnotperformancehigh1 ↵erencescomputational scores 5.2.**RQ**,2 F-MeasurescoresIn**RQ**, aimed1 . of smell uesallCluster (royal the TheEager Test, forMystery, forResource, sevenTest.Eager, NMC of**RQ**, aimed1 . theClusterandmethods oneNMC=1) valuesx=0. 82x=0. 98F-Measureobtained ter↵erenceclusters metrics; higherOn test odsNMC=0) 5 lowestTMC=0), highestx=0. 08, =0. 01). toMystery,eagerTestmysteryGuest ÞlesNRF=0NRDB=0) are intoFor example, ( tloc=7)tmcCabe=1) oth- ers.appliedResource. Finally,Test, dancyPR=0. 0)PR=0. 0).↵erently,isolationforest Clusterx=0. 02 =0. 0), 0.754x=0. 03, =0. 02), 12x=0. 81, =0. 0) redundancyx=0. 0, =0. 16). 0.50In othercantheF- F1 ScoreMeasurerangesto 0.25Eager).MCCreachedResource isolationforest Optimismdetection.Precisionis valueEager),Recallis 0.00smells,100%. Turning attentionLOFOCSVMLOFOCSVM shows distribution testoptimal resourceOptimismtestRedundancyIsolationmethod.Cluster(pastel ,One-Class. observesidered With respectEager,0.15 MCCrang-uesx=1. 18,x=1. 99) F-Measure,higherx=0. 21, x=0. 17).Mystery, 0.10andEager,uesx=0. 18,x=0. 75)x=0. 54, Preci-x=3. 34)↵erently,Resource, Clusterx=0. 18, F1 Score Test.x=0. 75)x=0. 74,x=2. 49)0.05

9

0.00

LOFOCSVMLOFOCSVM


---

<!-- Página 9 -->

Table hyper-parameter

Table the

Table parameter

IsolationinPrecision,Recall,Accuracy,F-Measure,MCCwithout/ o with/HT”)

**Precision****Recall****Accuracy****F-Measure**MCC **Test****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT**

Eager Mystery0.140.150.600.870.360.190.230.25-0.06-0.08 Resource Test0.0040.750.920.330.100.010.010.010.005

LocalinPrecision,Recall,Accuracy,F-Measure,MCCwithout/ o with/HT”)

**Precision****Recall****Accuracy****F-Measure**MCC **Test****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT**

Eager Mystery0.150.150.560.560.420.420.230.23-0.03 Resource Test0.0040.0050.700.700.400.400.010.010.010.01

OCSVMinPrecision,Recall,Accuracy,F-Measure,MCCwithout/ o with/HT”)

**Precision****Recall****Accuracy****F-Measure**MCC **Test****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT****w****/ o****w****/****HT**

Eager Mystery0.130.180.380.500.500.550.190.26-0.070.04 Resource Test0.0050.650.620.520.510.010.010.020.02

Figuresmells

10


---

<!-- Página 10 -->

TablePrecision,Recall,Accuracy,F-Measure,MCC.

**Confusion****Precision****Recall****Accuracy****F-Measure**MCC **Test****TP****FP****TN****FN**

Eager2,5920.27 0.96 Mystery1,4437,99798840.150.950.160.26-0.11 Resource7230.07 0.99 Test409,40617600.0041.00.020.008

ForTest,sameTablemetrics uesAsapproach. contributeF-MeasureandMCCreached 17%, clearerbevol-EagerandMystery,smells, umeentropysmells.thetoPrecisionis Eager,Posnettentropy<6(x=4. 88,testRecallis andx=0. 2)Posnettvolume>19x=489, andx=465)Finally,Accuracyranges40%. are 5.4.Finally,performance theeach smell. this algo-InFriedmanF-Measure rithm, performanceF-MeasureandMCCscoresto reachingEagerportedsmells Test. termsRecall, observedered—Eager,Mystery,Resource—the and maximumPrecisionreachedp-valuethere waysEagerdetection.onlysigniÞcant↵erences theAccuracy:95%.Concerning Nemenyi results depicted InperformanceFigure erally K-meansods—boxplotLOF—show terDBSCANniÞcant↵erencesEagerandMystery. lyzeThe cluster-internalthat↵erent performance computedSilhouette[77],Homogeneity[78],Com-metricsblue pleteness[78],V-Measure[79], andAdjustedtheRe- Score[80]. While entirereportedsourcedetection,DBSCAN linepresent↵erences.blue forSilhouette,bars centralthese within clusters.cluster-performTest basedworkdetection,↵erences observed techniques. central the↵erent techniques5.3. statistically↵erences Figureboxplot anomaliessmell,￿**Answer****.**The1 wedistributionreachedF-Measurein used inpresencebasedEagerdetection, orsmells.0% all areallMysteryInRecall, Guest,Resource,Test. addition,achieved highest100% forout-forsmells, liers. The data seemvary between andTest with minimalsecondRedundancy, approaches↵erences. This indicates for↵erent discussion be 5.5.forEager. smell,TMCmetric basedoutlier,NMCdis- tribution. candata for lessTableresultprecision,recall,F- homogeneoussmells.Measure,MCCbyresults

11


---

<!-- Página 11 -->

Table

**Test**

Eager Mystery Resource Test

**Test**

Eager Mystery Resource Test

Table

**Test**

Eager Mystery Resource Test

Figuresmells

Precision,Recall,Accuracy,F-Measure,MCC.

**Confusion****Precision****Recall****Accuracy** **TP****FP****TN****FN**

3400.78 0.13 1093237,7721,4180.250.070.82 440.11 0.06 14319,151390.0020.020.95

TablePrecision,Recall,Accuracy,F-Measure

**Confusion****Precision****Recall****Accuracy** **TP****FP****TN****FN**

2,5310.31 0.93 1,5276,8041,29100.181.00.30 7280.09 1.0 408,0941,48800.0051.00.16

theheuristic- machine proaches.machine- p**-value**p12learning  14 15than9. 5902e3. 1696e  09 09particular, classical5. 8132e8. 4323e  06larstatis-9. 9534e0. 00049182 tical0. 072078704. 8242e 06 stratesEager sourcecompared

12

**F-Measure**MCC

0.110.05

0.004-0.006

,MCC.

**F-Measure**MCC

0.310.17

0.010.03

,MysteryGuest,Re-


---

<!-- Página 12 -->

Table ResultsPrecision,Recall,F-Measure,MCCforML-based **Clustering****Statistical****Heuristic** IFLOFOCSVMDBSCANK-meansBoxplotTsDetectTeReD **Precision** **Anomaly****Machine**0.31 **Test**DARTS0.140.150.130.150.250.180.40 Eager Test0.180.270.350.090.18 Mystery0.0040.0050.040.0020.00 Resource0.070.07 Test**Recall** **Clustering****Statistical****Heuristic** IFLOFOCSVMDBSCANK-meansBoxplotTsDetectTeReD**Anomaly****Machine** **Test**DARTS 0.93 Eager Test0.430.960.160.600.560.380.940.071.00.40 Mystery 1.00.37Resource0.610.99 0.750.700.651.000.021.00.00Test **F-Measure** **Anomaly****Machine****Clustering****Statistical****Heuristic** **Test**DARTS IFLOFOCSVMDBSCANK-meansBoxplotTsDetectTeReD Eager Test0.250.430.22 0.47Mystery 0.230.230.190.260.110.310.40Resource0.120.14 Test0.160.25 0.010.010.010.0080.0040.160.00MCC **Anomaly****Machine** **Test**DARTS **Clustering****Statistical****Heuristic** Eager Test-0.30-0.090.06 IFLOFOCSVMDBSCANK-meansBoxplotTsDetectTeReDMystery Resource-0.030.020.16 Test -0.06-0.03-0.07-0.110.050.170.29 0.110.17 0.010.010.020.008-0.0060.03-0.01 inmachine results forEagerdetection. As anomalyEagerin termssDetectachieves forMysteryandesource.Re- call, heuristic-based tisticalF-MeasureandMCC, performancetheMystery Guest,sDetectperforms↵erent discussion caneReDetect, anomalyRecall, shows

5.6. The Figureoutlierssmellallp-value contextstatistically↵erences detection proaches. identify basedK-meanscally signiÞcant↵erences, performed Nemenyi F-Measure,As ofEagerandMys-techniques tery,F-MeasurescorestestEagerandMystery, OCSVM, comparableclassical

13

0.30 0.18 0.13 0.003

0.60 0.75 0.62 0.17

0.40 0.29 0.22 0.01

0.07 0.10 0.16 -0.004


---

<!-- Página 13 -->

− 3.23 − 4.48 − 3.39 − 4.33 − 3.55 − 4.01 − 3.41 − 3.73

5.0

4.0

3.0

2.0

4.5

3.5

2.5

**F1 Eager Test**

isolationforest

**F1 Resource Optimism**

isolationforest

Figuresmellstheerror indicaterank

signiÞcant↵erences. signiÞcant↵erencesMystery other graphdot.

OCSVM ! 2.86In KMEANS ! 2.39 tion↵ectivesmells. ample,generally performers ingEager tery. Mystery,smells.

￿**Answer****.**The2 better heuristic- niques,Recall. terms thesimilarEager Guest,Test, theResource we↵erences ing

LOF ! 3.53

OCSVM ! 3.41

KMEANS ! 2.73

boxplot

boxplot

**6.** , the Ourthe work LOF ! 3.82 tionalre- sults better strive DBSCAN ! 4.21 ticular, how parethe hand,impactandMys- on↵ective otheradditional imentation proachescomplement Incomplementarity of an↵ort extent F-Measure,potentially ,MysterysectionsÞndings two . 6.1. pact The proachesmachine

14 DBSCAN ! 3.78

**F1 Mystery Guest**

**F1 Test Redundancy**

4.0

t

3.0

2.0

Recall. same

4.2

3.8

3.4

3.0

**RQ**suggest anomaly2

KMEANS ! 2.52

KMEANS ! 3.32

OCSVM ! 3.22

LOF ! 3.42

LOF ! 3.61

OCSVM ! 3.47

DBSCAN ! 3.92

DBSCAN ! 3.65


---

<!-- Página 14 -->

− 4.72 − 4.73 − 6.67 − 4.18 − 5.02 − 5.45 − 4.50 − 5.11 − 3.73 − 4.37 − 4.55 − 4.94

7

6

5

4

3

5.0

4.0

3.0

**F1 Eager Test**

DARTS

isolationforest

**F1 Resource Optimism**

isolationforest

Figuresmellstheerror indicaterank

basedone hand, to enough, F-Measure,MCCarethe lowparticularly Ourthe OCSVM ! 4.27workmachine KMEANS ! 3.51

TsDETECT ! 3.94proachesthe

To served atexperimented scenario. intorobustness ods natives scopeclassical machine ent thebest ingindeed di↵erent than perform exploited RandomForestwith Borderline-SMOTE detecting TestandResource,RandomForest LOF ! 4.48

SVM ! 4.49

OCSVM ! 4.35

KMEANS ! 3.55

with no

**F1 Mystery Guest**

boxplot

randomforest

**F1 Test Redundancy**

boxplot

6

naivebayes

TeReDETECT

5

t

4

3

ingMysterydetection, NaiveBayeswith no Precision,ancingTestdetection.re- sults achieved. table, mances↵erences.**RQ**the2 LOF ! 5.43 anomaly OCSVM ! 3.95ter, within-projectexperimented adaboost ! 5.38

DBSCAN ! 6.34

KMEANS ! 3.14 achieved

SpeciÞcally,PrecisionandMCC, machine learningEager (76%),MysteryResource(58%). ForF-Measure, showedEagerwith scores signiÞcantly between 45%.be theMysteryandResource: 5.0 results the ↵er-performed 4.0 InRecall, DBSCAN estsmells,the 3.0detectsPrecision forthe may

EagerFinally,Test, can most all

15 DBSCAN ! 4.86

KMEANS ! 4.41

TsDETECT ! 4.66

LOF ! 4.44

TsDETECT ! 4.89

OCSVM ! 4.57

DBSCAN ! 4.95

LOF ! 4.57


---

<!-- Página 15 -->

**Test** Eager Test Mystery Resource Test

**Test** Eager Test Mystery Resource Test

**Test** Eager Test Mystery Resource Test

**Test** Eager Test Mystery Resource Test

projectoverallthe test ing In ods performanceconsistently within- project formed ingmay support of smell textthea the ing for ousmachine using only metrics based smell48] code metricsreadability. enhancedincorporating characterize codeim- prove detection this work community,way learning Additionalbe ing projectanalyzed potential

Table Results

IF

**Anomaly** 0.16 0.23 0.008 0.10

IF**Anomaly**

0.550.62

0.63 0.73

**Anomaly**

IF 0.32

0.260.17

0.01 **Anomaly**

-0.8 IF -0.03

-0.06

0.01

LOF

0.17

0.007

LOF

0.68

0.65

LOF

0.28

0.01

LOF

-0.02

-0.01

Precision,Recall,F-Measure,MCCfor **Clustering** OCSVMDBSCANK-means **Precision**

0.160.150.16 0.27 0.010.0040.001 0.08

**Clustering** OCSVMDBSCANK-means

0.970.430.950.23

1.0 0.681.00.05

**F-Measure** **Clustering** OCSVMDBSCANK-means 0.43

0.260.200.110.14

0.020.0080.001MCC

**Clustering** -0.1 OCSVMDBSCANK-means 0.03

-0.04-0.120.01

0.030.007-0.03 reasons  ciently↵erent,baselines,limited son. fyingnorm. scenario, variability therelatively tentsame challenging anomaly tween this wesemantic lishtest classes projects.Þrst extracted set classes↵ered we theclasses; ods assertions testof methods; the packages; (7) orcomputed (1)method cosine(2) ture cases,adherence arrangement-act-assert ods documentation methods.

16

**Statistical** BoxplotTsDetect

0.31 DARTS0.180.42 0.370.090.21 0.005

**Recall** **Statistical** BoxplotTsDetect DARTS 0.83 0.170.870.44 0.870.37 1.0

**Statistical** DARTS BoxplotTsDetect 0.23 0.45 0.300.44 0.160.27 0.01

DARTS **Statistical** 0.06 BoxplotTsDetect

0.11 0.110.29 0.080.15 0.04

↵erent testthe

**Heuristic** TeReD

**Machine**

0.00

**Heuristic** TeReD**Machine**

0.00

**Machine****Heuristic** TeReD

0.00 **Machine**

**Heuristic** TeReD

↵ectively. verify

setupandteardown ↵erent

0.76 0.76 0.58 0.01

0.75 0.49 0.39 0.43

0.75 0.60 0.46 0.02

0.66 0.55 0.41 0.04


---

<!-- Página 16 -->

can↵ectively similaritywithin vidual the izedconventions Uponanalyzed distribu- tion various ing individual of of medians,few suggests test consistencysemantic inforcing argument limited the↵ectivenessdistinguish- inganomalous As reportmetrics such an

6.2.Anomaly Qualitative To served, performed false positives proaches, twosystematically alyzed setnegative approach. thenature smells(2) consistencymetricsthe tent testtwo inspectors identify elementsproperly measured inspection authors torsresults discussion lowedto of Starting implement ofmethod, the rics, textual pieces thecase. aresmell, not two

¥Test testing additional setupinstance, tingconÞguring vices.not

Eager,

17

core thelead to false positivesEager detection di↵erentiate actual ofan the projectis all 1@Test 2publicvoidtestDoFilterInDEPLOYMENTMode() 3throwsException 4when(mockRequest.getRequestURI()). thenReturn("/g2.js"); 5victim.setWroManagerFactory( createValidManagerFactory()); 6setConfigurationMode( FilterConfigWroConfigurationFactory. PARAM_VALUE_DEPLOYMENT); 7victim.init(mockFilterConfig); 8victim.doFilter(mockRequest mockFilterChain); 9}

ListingEager

Inanomaly properly smelliness the could identify tribution testthe based biased of

¥Existingdi between method within same volves same smelly cases ing. methods ior even thoughfocused ality. An example JFreeChartproject it shown 1@Test 2publicvoidtestPrune() 3DefaultTableXYDataset DefaultTableXYDataset(); 4dataset.addSeries(createSeries1()); 5dataset.removeSeries(1); 6dataset.prune(); 7assertEquals(4,dataset.getItemCount()); 8}

Listing

According ased all resenting

smells

wro4j

due

↵erence

smell,

new

Eager.


---

<!-- Página 17 -->

Abesmells consideredResource, involves their status,not count thisof simulatedmimic trolledbe of calculation lead toResource timismsmells, testing sources. example case that was wrongly by

1@Test 2publicvoidtestAggregatedComputedFolder2() 3throwsException 4finalHttpServletRequest (HttpServletRequest.class); 5finalHttpServletResponse get().getResponse(); 6Mockito.when(request.getRequestURI()). thenReturn("/wro4j/wro/path/to/g1.css"); 7Context.unset(); 8Context.set(Context.webContext(request responseclass))); 9

10managerFactory.create().process(); 11

12Assert.assertEquals("/wro4j/wro/path/to/", Context.get().getAggregatedFolderPath()); 13}

ListingResourcedue

Wedetection performance, rect OnMystery, ing within test if ables nottest, current metricsMys- terysmell,use of mightproperly theexample Listingdropwizardproject. thesetupmethod servlets server,certain extensions. Looking case, code i.e.,foo.mp4,server ports

1@BeforeClass 2publicstaticvoidstartServletTester()throws Exception 3SERVLET_TESTER.addServlet(DummyAssetServlet .class,DUMMY_SERVLET+’*’); 4SERVLET_TESTER.addServlet( NoIndexAssetServlet.class,NOINDEX_SERVLET+ ’*’);

5SERVLET_TESTER.addServlet( NoCharsetAssetServlet.class, NOCHARSET_SERVLET’*’); 6SERVLET_TESTER.addServlet(RootAssetServlet. class,ROOT_SERVLET+’*’); 7SERVLET_TESTER.start(); 8SERVLET_TESTER.getContext().getMimeTypes(). addMimeMapping("mp4","video/mp4"); 9SERVLET_TESTER.getContext().getMimeTypes(). addMimeMapping("m4a","audio/mp4"); 10}

1@Test 2publicvoidsupportsByteRangeForMedia()throws Exception 3request.setURI(ROOT_SERVLET"assets/foo. mp4"); 4response SERVLET_TESTER.getResponses(request.generate ())); 5assertThat(response.getStatus()).isEqualTo (200); ACCEPT_RANGES)).isEqualTo("bytes"); 6request.setURI(ROOT_SERVLET"assets/foo. m4a"); 7response SERVLET_TESTER.getResponses(request.generate ())); 8assertThat(response.getStatus()).isEqualTo (200); ACCEPT_RANGES)).isEqualTo("bytes"); 9}

ListingMystery.

Our(1)prop- erlysituation; (2) focused setup↵erentiate useactualMysterysmells. Finally,Test, tests cover same rics aprovide view on duction↵erent aspects of inputsinstance, reportedthey exercise production↵erent edge may 1@Test 2publicvoidtestGlobFilter()throwsException 3createHttpFSServer(false,); 4String getHadoopUsers()[0]; 5URL urlnewURL(TestJettyHelper.getJettyURL() , 6MessageFormat.format( 7"/webhdfs/v1/tmp?user.name={0}&op= liststatus&filter=f*",user)); 8HttpURLConnection url.openConnection(); 9Assert.assertEquals(conn.getResponseCode(), HttpURLConnection.HTTP_OK); 10BufferedReadernewBufferedReader( 11newInputStreamReader(conn.getInputStream() ));

18


---

<!-- Página 18 -->

12reader.readLine(); 13reader.close(); 14} 15

16

17@Test 18publicvoidtestHdfsAccess() 19createHttpFSServer( 20

21String getHadoopUsers()[0]; 22URL urlnewURL(TestJettyHelper.getJettyURL() , 23MessageFormat.format( name={0}&op=liststatus 24

25HttpURLConnection url.openConnection(); 26Assert.assertEquals(conn.getResponseCode(), HttpURLConnection.HTTP_OK); 27BufferedReader 28newInputStreamReader(conn.getInputStream() )); 29reader.readLine(); 30reader.close(); 31}

Listing

Also inaspect perimenteda of assessed.of tegrating redundant(1) novel and the tary smell be discriminateintra-class cases, ducing risk of same nity unchangedoriginal Eagerindeed worth developnuanced Upon approaches, also inquired potential hind the↵erent performance heuristic-based ations on two

¥Most scale. ofcases, acontrast, study provides proaches

throwsException false,);

"/webhdfs/v1/?user. ", user));

newBufferedReader(

Test.

↵erences

sDetectwas

experimental served↵erences

¥RegardingeReDetect, original themutation measure fault↵ectiveness testavaproject. tion↵erent, mutation racywork↵ers sessmentdetection this

Thesedi↵erences mance di↵erent experimental

6.3.Anomaly of

Ouranomaly could less, we may whether tarities Tothe di↵erences proaches themandi m,thej**T** dictedmandm( mm), amountijij smellsmonly andm( m\m),ijij and amountmj only and missedm( m\m).fouriji experimentedm,m,m,m,ijkp (1)monlyi**S****S** andmj,m,m( m\( mjmkmp)),kpi the **T****T****T****S****S****S** ((mimjmkmp) \( mmjmkmp)).i Tableresults overlap,results tarity servemost ofcommon statisticalEa- ger,Mystery,Resource timism,Test. between other↵erent for Itdetection onmachine basedheuristic- basedEager Test,smells. Considering anomaly tic tion plementEager,Mys- tery.contribution

19


---

<!-- Página 19 -->

**T****T****T** StatsCluster\\\\\ Table Overlapheuristic-based **T****T****T** Stats\\\\\**Eager****Mystery****Resource****Test** **T****T****T** 90.16%3.78%94.49%5.50%93.31%0.68%100.00%StatsML\MLML\ML\MLML\ML\ML Heur. 37.18%60.64%0.00%**T****T****T** StatsML-C\ML-CML-C\ML-C\ML-CML-C\ML-C\ML-C 18.68%80.65%27.30%72.69%38.04%61.95%32.65%67.5% **T****T****T**54.82%41.73%67.25%32.74%36.26%63.73%22.50%77.50%Cluster\\\\\Heur. 37.47%61.23%0.00% **T****T****T** ClusterML\MLML\ML\MLML\ML\ML18.79%81.01%28.18%71.26%37.74%61.84%32.50%67.50% **T****T****T**56.97%41.80%61.86%32.69%35.76%63.68%22.50%77.50% ClusterML-C\ML-CML-C\ML-C\ML-CML-C\ML-C\ML-CHeur. 13.01%63.12%0.00% Heur.**T****T****T** ML\ML\ML\MLML\ML\ML28.27%23.03%0.00% ML

16.15%12.19%23.52%12.14%16.09%43.34%22.22%50.00%**T****T****T** ML-C\ML-CML-C\ML-C\ML-CML-C\ML-C\ML-C

Table Complementarityheuristic-based**T****T****T** MLML-CML\ML-CML-C\MLMLML-CML\ML-CML-C\MLMLML-CML\ML-C **Eager****Mystery** **S****S****S****S****S****S****S****S****S****S****S****S** Stats\(ClusterHeur.MLML-C)\(StatsClusterML\ML\ML 1.74%0.06%**S****S****S****S****S****S****S****S****S****S****S****S** Cluster\(StatsHeur.MLML-C)ML\\MLML\ 1.63%0.00%**S****S****S****S****S****S** ML-C\(Heur.MLStatsCluster)(ML-C\ML 0.00%**T****T****T****S****S****S****T****T****T****S****S****S** (StatsClusterHeur.ML)\ML)ML)\ML) 0.00% **Resource****Test** **S****S****S****S****S****S****S****S****S****S****S****S** Stats\(ClusterHeur.MLML-C)\(StatsClusterML\ML\ML 0.0%0.00%**S****S****S****S****S****S****S****S****S****S****S****S** Cluster\(StatsHeur.MLML-C)ML\\MLML\ 0.00%**S****S****S****S****S****S** ML-C\(Heur.MLStatsCluster)(ML-C\ML 0.00%**T****T****T****S****S****S****T****T****T****S****S****S** (StatsClusterHeur.ML)\ML)ML)\ML) 0.00%

notsmellsofto gestsnature.Acomputation anomalydent thespeciÞcallyutilizedBased the tablishedproaches tweenanomalythe ods.selectssmells, table evaluation↵erent detectionpendingcase. ourlimitationsmeta-approach ofdeveloptechnique,smell smellstudye↵ective tionalcode variousoverall **7.**capabilities evaluated role of This sectionmay a↵ectisting validityapproaches,advanc- ing**Construct**The testbased in-**External**As generalizability vestigationcuratedclusions, mainsubject viouscasesstudy.avaopen-source of cases.However,projectsitHub,only thatentirelyplete picturecannot

20

\

\

ML\

ML-C\

\

ML\

ML-C\

ML\

ML-C\

ML-C\ML

**T**

**T**

**T** ML

**T** ML-C

**T**

**T** ML

**T** ML-C

**T** ML

**T** ML-C

**T** MLML-C

\

\

\ML

\ML-C

\

\ML

\ML-C

\ML

\ML-C

ML\ML-C

\

\

ML\

ML-C\

\

ML\

ML-C\

ML\

ML-C\

ML-C\ML


---

<!-- Página 20 -->

ensure Þndings programming gard,scripts pendix Þndings↵erent contexts In keyonly ableava[17, is exploited, also for employedanalytical compute currentprovide andsmell study↵erent programming Consequently, mingunfeasible, ing required While need to 2JetBrains,J avaremains of languages, that tion softwareJ widespread, our↵er thestudy onava,rooted process mingMystery in not Therefore,study likely more↵erent languages needed, Þndings taldetection. Another projects.di open-source industrial velopment ence the emphasize performed acteristicsstructural seman- tic solid foundationapplicability to stance,the reusescale size, whetheruse testingpresence methods fundamental gardless **Conclusion**This category tweennot

2[https://www.jetbrains.com/lp/devecosystem-2023/](https://www.jetbrains.com/lp/devecosystem-2023/) languages/

↵erentthe represents Þrst attempttest smell niquesOur [24]use avaforderstandimpact forWeinherent lenges↵erent approaches how detected ated. For thresholds, liers di cult. Additionally, ferentTo ourthe plieddi↵erences tween**RQ**1 and anomalyheuristic- ma- chine**RQ**.Þrst2 veriÞed normalityShapiro-Wilk [76]. Then, computed theNemenyi were any↵erencesF- ava’sMeasurescores **Internal**This categoryse- lection proachesempirical Towell-known detectionare , deÞned

**8.**

In performed the smells. consideredcases from 66avaprojects,Ea- ger,Mystery, ↵erencesResource,Test. First,**RQ**,1 tects test smells. ing notEager, Mystery,ResourceandTest dancy.Then,**RQ**,anomaly2 ↵ertection machine tectionPrecisionandRecall, theF-MeasureisMysteryand Resourcedetection. sespromising setupandteardownlutionsThis has implications binationsmell welow precision lead shouldresults. cial out

21


---

<!-- Página 21 -->

Furthermore, low performancethe basedtheirim- plementations TheF-Measure as starting anomaly identiÞcationthe feasibilitysmell wellaccurate On thosepromises and researchproblem the the ment. such asteam’s thesuite. factors,provide anddetection processexam- ple,exe- cution oftested adjust cur ora gratingtypically together, algorithm higher inmethods isolated, algorithm threshold tential This adaptive, cision project’squality more,signiÞcantly incorporating speciÞc patterns better↵erentiate This could learn from project’s continuouslydetection ing ally,impact the↵ectiveness approaches,robust variousdevelopment Another anomaly or detection, terns in metrics. orcombining other canintent test,

shouldas

Future

Eagerinstances,

Eagersmells.

↵ectively.

↵erent contextual

↵ectiveness.

↵erentparts

.

For tectioncritical smells otherwise In systems(including industry-scale wouldrelevanceÞndings di↵erent contexts.Finally, plan asanomalysmells scalability

**Acknowledgements**

Thehandling the anonymousthe ing qualityThis study theao perior grants/ 2020 supported S000323N). also been ropean researchbeen PNRR

**Declaration**

The nancial peared

**Data**

Thedata included tary asreproducing study, [https://doi.org/10.6084/m9.figshare.24466336](https://doi.org/10.6084/m9.figshare.24466336)

**Credits**

**Valeria**: tion, Validation, **Martins**: dation, Conceptualization, &**Fabio**: Validation, Supervision,

**References**

[1]G.the same:classifyingwith ofSoftware [2]V. computing

22

↵orts and

/ 2022.

RECHARGE

**Ivan Machado**

**Filomena**

« Su-

.

**Luana**

:

:


---

<!-- Página 22 -->

[3]K. as 12 [4]P.Silic, prediction (2020) [5]F. anomaly?of diction, 2022 andUSA, pp. [6]V.cybersecurity, Distributed [7]M. detectionComputer (2016) [8]A. TechnicalComputer NLD, [9]G.empirical analysissmells their maintenance, 2012 Maintenance56–65. [10]G.Di perimental refactoring,Software [11]D.the relation2018 tionalEvolution, pp. [12]G. since beginning: di generated code, 327. [13]G. e↵ectiveness Software [14]N.tester-assistedtest redundancy 1–13. [15]A.Almalki,W.Ouni, F. Proceedings gineering Engineering, 1650–1654. [16]T.Cruz, Costa, I.smellProceedings Brazilian USA, [17]W.Alotaibi, W. A. tools:Proceedings tional ing, [18]D.Schvarcbacher,Bruntink, chelli,Proceedings of MSR [19]L. toringscode, Brazilian Engineering, [20]M. detecting smells Computer Information [21]V. F.smell ware Engineering [22]G.smells really (2015) [23]D.

/ FSE

↵usenesssmells

inarydealing defectProceedings onAssessment1–10. [24]V. investigation capabilities test 10.6084/m9.figshare.24466336 [25]E. database the/ IAFE (CIFEr), 220–226. [26]C. in model, biomedicalUSA, pp. [27]L. the Conference pp. [28]N. tionP. ÿÿT.Smuc,zeroski(Eds.), Publishing, 493–508. [29]C.-L. forlocalization, 2021 onPattern TN, 9659–9669. [30]F.the di↵usioncode: empirical study, Software [31]A.Almalki,W.Ouni, F.distribution applications: exploratory Proceedings International ing, [32]L.the relationship code Evolution Process [33]N.test coverage test –Research Heidelberg, 129–136. [34]S. Empirically ofAnalysis, ISSTA [35]J.Dattatreya, tectionacceleration, Proceedings Joint Meeting ACM, [36]M.de- pendencyProceedings ing the York, [37]G. defendersimprovements, 2020 InternationalValidation Workshops461–464. [38]A. pollutingdependency, Proceedings InternationalAnalysis, ACM, [39]M. Þxturesmells,Vali- dation322–331. [40]M. avoiding Þxture ference

23

[https://doi.org/](https://doi.org/) .

/ CVF Conference

↵usion their

 cient dependency

/ FSE

/ FSE


---

<!-- Página 23 -->

CA, 387–396. [41]C. andProceedings International 2014, [42]F.smell usingInternational Software 311–322. [43]F. theProceedings tional1–3. [44]M. dynamic International IEEE [45]Y. detectingsmells, neering Methodology [46]C.ost,Wessl Experimentation Media, ¬¬[47]V.ucüuk,code: edge in (2018) [48]S. time testrefactoring: ings 28th ACM, [49]F. matic caseInter- nationalAnalysis, 130–141. [50]S.asquez, prehensive code and [51]R. Transactions [52]F. to Engineering [53]Y.themetric Empirical [54]V.glu, ing: (2015) [55]T. Engineering [56]G.the perception measurabilitycode ternationalevolution IEEE, 336–347. [57]G.empirical ongenerated cases, the 348–351. [58]R. Transactions [59]J. from (http://www./weimer 5 [60]J. on publications,

/ students/ dorn-mcs-paper.

[61]S. techniques, [62]S.Mohammadi, DiA. gling odd ones inACM International Quality 2020, [63]K.-L. H.-K.Xu, Improving forProceedings ferencecybernetics volume3077–3081. [64]F.Proceedings the/ ACM 2008, 413–422. [65]P. learning [66]Z. local outlier Adaptive Convergenten, [67]J. Journal [68]F.Varoquaux, Gramfort, Michel, Thirion, O.Blondel, Scikit-learn: Research [69]R. ACM 2011. [70]P. ing Bioinformatics [71]M. for 1996, 226–231. [72]J. gorithm, 28 [73]M.main- tenancesuites, WASDeTT-1: Interna- tional niques, [74]M.and tion friedman in measures 228. [75]P. sity, [76]S.B.normality (complete [77]K. score, 2020 International advanced747–748. [78]A.validating preprint [79]A. ternal ference putational Republic, 410–420. [80]S. cluster [81]F. ity, international technology,

24


---

