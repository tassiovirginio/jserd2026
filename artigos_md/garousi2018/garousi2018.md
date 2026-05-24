<!-- Página 1 -->

### Accepted Manuscript

Test Prioritization

Alireza Haghighatkhah,

PII: S0164-1212(18)30173-0 DOI: [https://doi.org/10.1016/j.jss.2018.08.061](https://doi.org/10.1016/j.jss.2018.08.061) Reference: JSS

To appear

Received date: Revised date: Accepted date:

Please cite oritization in [https://doi.org/10.1016/j.jss.2018.08.061](https://doi.org/10.1016/j.jss.2018.08.061)

This is to our copyediting, typesetting, and review of the resulting proof before it is published in its Þnal form. Please note that all legal

###

inContinuousIntegrationEnvironments

MikaMantyla, MarkkuOivo,PasiKuvaja

10216

in:*The Journal**of**Systems**&**Software*

5March2018 20August2018 28August2018

thisarticleas:AlirezaHaghighatkhah,MikaantylMa, MarkkuOivo, ContinuousIntegrationEnvironments,*The Journal**of**Systems*

aPDFÞleofanuneditedmanuscriptthathasbeenaccepted customersweareprovidingthisearlyversionofthemanuscript.

duringtheproductionprocesserrorsmaybediscoveredwhich disclaimersthatapplytothejournalpertain.

PasiKuvaja, *&**Software*

forpublication. Themanuscript

couldaffect

TestPri- (2018), doi:

Asaservice willundergo

thecontent,and


---

<!-- Página 2 -->

Highlights

Historical failure ments

History-based TCP

Diversity-based

Diversity-based e ectiveness

History-based diversity performance

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

knowledgeseemstohavestrongpredictive

doesnotnecessarilyrequirealargeamount

TCPcanbeusede ectivelywhennohistorical

TCPcanbecombinedwithHistory-basedTCP

usingNCDMultisetachievedhighest

1

powerinCIenviron-

ofhistoricaldata

dataisavailable

toimproveits

APFDbutlowest


---

<!-- Página 3 -->

### ACCEPTED MANUSCRIPT

### Test

### Prioritization

### in

### Continuous

### Integration

### Environments

a,aaaAlireza Haghighatkhah, Mika Mantyla, MarkkuOivo, PasiKuvaja

aEmpirical Technology

Abstract

Two heuristicsnamelydiversity-based(DBTP)andhistory-basedtestprioritization (HBTP) havebeenseparatelyproposedintheliterature.Yet,theircombinationhas not beenwidelystudiedincontinuousintegration(CI)environments.Theobjective of thisstudyistocatchregressionfaultsearlier,allowingdeveloperstointegrateand verify theirchangesmorefrequentlyandcontinuously. Toachievethis,weinvestigated six open-sourceprojects,eachofwhichincludedseveralbuildsover alargetimeperiod. Findings indicatethatpreviousfailureknowledge seemstohave strongpredictive power in CIenvironments andcanbeusedtoe ectivelyprioritizetests.HBTPdoesnotnec- essarily needtohavelargedata,anditse ectivenessimprovestoacertaindegreewith larger historyinterval. DBTPcanbeusede ectivelyduringtheearlystages,whenno historical dataisavailable, andalsocombinedwithHBTPtoimproveitse ectiveness. Among theinvestigatedtechniques,wefoundthathistory-baseddiversityusingNCD Multiset issuperiorintermsofe ectivenessbutcomeswithrelativelyhigheroverhead in termsofmethodexecutiontime.TestprioritizationinCIenvironmentscanbeef- fectively performedwithnegligibleinvestment usingpreviousfailureknowledge,andits e ectiveness canbefurtherimproved byconsideringdissimilaritiesamongthetests.

Keywords:Testcaseprioritization,regressiontesting,continuous integration,build history, testdiversity

1. Introduction

The softwareindustryismovingtowardanagile,continuousdeliveryparadigmin which changestosoftwarearereleasedmorefrequentlyandconsiderablyfasterthan before [1,2].Tomaketherapidevolutionofsoftwarecost-e ectiveandreliable,the 5industry hasadoptedcontinuous integration (CI)[3].CIaimstoprevent the problem knownas\integrationhell"andautomatethebuildprocessandveri cationof changes. Eachintegration cycle is calledbuild.aThecomprises a set of automated activities andisfollowedbyregressiontesting(RT).Inanutshell,RTaimstoensure that recent changes to the system have not impacted negatively on any previously veri ed

Corresponding E-mail(Alireza

# ACCEPTED MANUSCRIPT

Preprint


---

<!-- Página 4 -->

### ACCEPTED MANUSCRIPT

10functionality.RTiswidelyusedinpractice;itiscommontohave adedicatedregression test suitethatisoftenruninitsentirety [4]. A testsuiteforenterprise-sizedapplicationsoftenincludesthousandsoftestcases, the execution of which requires several hours or even days. Forinstance, the JOnAS Java EE middleware comprises2,689testcases[5].Applyingthemalltoits16con gurations 15results inrunning43,024testcases.Furthermore,thecostofRT increasesover thetime with theincreaseinsystemsize.Memonet.al[6]observedlineargrowthinbothcode submission rate and size of regression test suite, soincurring signi cant expensesto keep the RT running.Thesoftwareengineeringliteraturehasproposedmanytechniquesto improveRTprocesses.Testsuiteminimization(TSM)[7]aimstoeliminatetestcases 20from a test suite with a speci cobjective,i.e., removing obsolete or redundant test cases. Several experimentshavebeenreportedintheliteraturewithdi eringconclusionsre- garding the impact of TSM on the fault detection capability of a test suite, e.g., [8, 9, 10]. However,the common understanding is that TSM may compromise such capability. Test case prioritization (TCP) [11], onthe other hand, isconcerned with the ideal ordering of 25test cases to maximize desirable properties (i.e., early fault detection). Fromthe perspec- tive offaultdetection,TCPseemstobeasafeapproachbecauseitdoesnoteliminate test casesandsimplypermutesthemwithinthetestsuite. The intersection of CI and RT poses great challenges for the software development in- dustry.Thetesting budget is often limited and RT needs to make the most of sometimes 30limited resources. ForRT improvement techniques to beuseful and easy for the industry to adopt,theymustconsidercontextualfactorsrelatedtoenterprise-leveltestingenvi- ronments [12].SeveralTCPtechniqueshave beenproposedthatcanbeappliedinaCI environment[13,14, 15, 16, 17, 18, 19]. Eventhough di erences exist among the proposed techniques, theyallshareacommonassumption:testswhich previouslyfailedaremuch 35more likelytofailagain.Empiricalstudiestosupportsuchaheuristicareemergingin the literature.Forinstance,in2017,Hemmatietal.[18]investigatedthee ectiveness of threeblack-boxTCPtechniquesonFirefoxbeforeandafterthetransitiontorapid releases. Theauthorsconcludedthathistory-basedtestprioritization(HBTP)isfar more e ective thanothercomparabletechniques inrapidrelease,althoughthisdoesnot 40hold intraditionaldevelopmentenvironments.TCPusingpreviousfailureknowledge, however,comeswithitsownlimitations.Forinstance,notallregressionfaultscanbe captured e ectively, iftherehasbeennopreviousfailure,e.g.,newlyaddedtestcasesor those whichhave notpreviouslyrevealedanyfailure.Toincreasethelikelihoodofcap- turing faults,onepotentialstrategymight betospreadthetestingbudgetevenly across 45di erent parts of the system by performing a diverse set of test cases [20]. Theunderlying assumption isthatsimilartestcaseswilllikely exercisethesamepartofthesystemand detect thesamefault;thus,adiversesetoftestcasesshouldbeperformedtoa greater numberoffaults[21].Diversity-basedTCPrequiresminimalinformation,since the onlyrequiredinformationisalreadyencodedinthetestsuite[20]. 50In thiswork,weclassifyregressionfaultsaccordingtotheirpastverdictsandstudy the extent to which they can be captured using previous failure knowledge. Toe ectively deploy HBTP, one might assume that a large amount of historical data is required. More speci cally,historyinterval size(e.g.,thenumber ofpreviousverdicts used)isoftennot reported inpreviousworks,anditsimpactonthee ectivenessofHBTPhasnotbeen 55studied. Inthis work, we perform HBTP using di ering numbers of previous verdicts and

# ACCEPTED MANUSCRIPT

investigatewhetheritse ectivenesschangesbyvaryingthesizeofthehistoryinterval. 3


---

<!-- Página 5 -->

### ACCEPTED MANUSCRIPT

Toincrease the likelihoodof capturing faults, onepotential strategy is to assign a higher priority to those test cases which are most di erent compared toalready prioritized. Even though diversity-based TCP has been proposed and used previously, it has not been 60widely studied in combination with HBTP and in a CI environment. Hemmatiet al. [18] investigatedahistory-baseddiversityapproachinFirefoxproject.Theyusedprevious failure knowledgeincombinationwithasinglesimilaritymetric,Manhattandistance, using theEnglishtextsofmanualtestcases.Incontrasttotheirstudy, weinvestigated history-based diversityusingthreedi erentsimilaritymetrics(Manhattan,normalized 65compression distance(NCD),andNCDMultiset)withdi erenthistoryintervalsizes, overa large number of automated builds extracted from six open-sourceprojects.Inthis study,weexaminewhetherthee ectivenessofHBTPisimpactedwhenitiscombined with diversity-basedTCP. For thehistory-baseddiversity techniquetobeapplicablein a CIenvironment, bothe ectivenessandperformancearecritical.Thus,inadditionto 70e ectiveness, weinvestigatedthemethodexecutiontimewithinandacrossthestudied projects. The mainobjectiveofourstudyistocatchregressionfaultsearlier,allowingdevel- opers to integrate and verify their changes more frequently and continuously. Toachieve this, weinvestigatedsixopen-sourcesoftwareprojects;eachprojectincludedseveral 75builds over alongperiodoftime.Findingsfromourstudyindicatethat:

Only a small proportionof tests has ever failed with our subjects(less than 11% in four projects,and3{52%overall). ThisindeedraisestheimportanceofTCPinCI environmentsin which RT is performed more frequently and continuously. Further- more, themajorityofregressionfaults(57{97%)amongallinvestigatedprojects 80can becapturedsolelyby usingpreviousfailureknowledge. Thisimpliesthatpre- vious failureknowledgeseemstohave strongpredictivepowerinCIenvironments and canbeusedtoe ectivelyprioritizetests.

HBTP doesnotnecessarilyrequirealargeamount ofhistoricaldata,anditse ec- tiveness improves toacertaindegreewithalargerhistoryinterval. Evenwiththe 85last verdict(current  1), improvement (Vargha{Delaney Ameasure:0.53{0.82)in terms ofaverage percentageoffaultsdetectedwas observed inallstudiedprojects in comparisontorandomordering.

Diversity-basedTCPcanbeusede ectivelyduringtheearlystages,inwhichno historical dataisavailable(Vargha{DelaneyAmeasure:0.68{0.91,improvement 90observed using NCD Multiset), or combined with HBTP to improve its e ectiveness (Vargha{DelaneyAmeasure:0.51{0.73usingNCDMultiset).

Among theinvestigatedhistory-baseddiversitytechniques,i.e.,pairwiseManhat- tan, pairwise NCD, and NCD Multiset, we found that the latter is superior in terms of e ectivenessbutcomeswithrelativelyhigheroverhead intermsofmethodexe- 95cution time.

Fromacademicpointofview,weprovideempiricalevidenceinsupportoftwopre- viously proposedheuristicsnamelyhistory-basedanddiversity-basedTCPinCIenvi- ronments. Fromtheperspectiveofpractitioners,ourndingsindicatethatHBTPcan be employed withnegligibleinvestment anditse ectiveness canbefurtherimproved by

# ACCEPTED MANUSCRIPT

4


---

<!-- Página 6 -->

### ACCEPTED MANUSCRIPT

100considering distances (dissimilarities) among the tests. Therest of this paper is organized as follows: thebackground and related work is presented in Section 2.3 describes the researchmethodology,whileSection4presentstheresultsofourstudy. discusses the ndings and their implications, including a discussion of the validity of this research andconcludingremarksaregiveninSection6.

1052. BackgroundandRelatedWork

In thissection,webrie yreviewvariousRTimprovementtechniques,explainthe related work,andhighlightourowncontributioninsection2.2.2.

2.1. Background A numberofRTtechniquesandtoolshavebeendevelopedandproposedasap- 110proaches to reducing expensesand improving processes.Yooand Harmans [22] compre- hensive surveyreviewedRT techniquesoriginallyintroducedbyRothermelandHarrold [7, 23,8,24].Figure1depictsageneralmodelofRT techniques.

Figure

0Let Pbe aprogram,Pbe amodi edversionoftheTbe atestsuite 0developed forP . InthetransitionfromPtoP, apreviouslyveri edbehaviorP of 00 115may havebecomefaultyinP. RTseekstovalidatePto ensurethatrecentchanges to thesystemhavenotimpactednegativelyonanypreviouslyveri edfunctionalities.

# ACCEPTED MANUSCRIPT

During RT, severaltechniquesmaybeemployed inpractice.TSMseekstoidentifyand 5

5


---

<!-- Página 7 -->

### ACCEPTED MANUSCRIPT

permanently eliminateobsoleteorredundanttestcasesfromthetestsuite.Regression test selection(RTS)aimstoselectonlythesubsetoftestcasesa ectedbytherecent 120changes. TCPisconcernedwiththeidealorderingoftestcasestomaximizedesirable properties (i.e.,earlyfaultdetection),whiletestsuiteaugmentationaimstoidentify newly addedsourcecodeandtogeneratenewtestcasesaccordingly. There isalargebodyofresearchonRT, withagreatdealofpioneeringworkpub- lished inthe1990s[7,23,8,24].In2016,GarousiandMantyla[25]conductedatertiary 125study of systematic literature reviews of software testing and identi ed 11 published sec- ondary studiesonvariousaspectsofRT.Themostrecentsystematicliteraturereview on TCPtechniqueswasprovidedbyKhatibsyarbinietal.[26]in2017.Theauthors classi ed existingTCPapproachesintoninecategories.TheyconcludedthatTCPap- proaches arestillbroadlyopenforimprovement;eachapproachhasspeci cpotential 130values,advantages, andlimitations.Despitethelargebodyofknowledge onRT andthe many academicadvancements, thereisrelativelylittleevidenceregardingthepractical application ofRT techniquesinindustrialsettings[27].Theindustrypracticeseemsto be based mostly on experiencerather than on any systematic approach to RT [4]. Toen- sure RT techniques areusefulandeasilyadopted,theymust considercontextual factors 135related toenterprisetestingenvironments [12].

2.2. RelatedWork 2.2.1. TestPrioritizationinCIEnvironments Several TCPtechniques have beenproposedthatcanbeappliedinCIenvironments [13, 14, 15, 16, 17, 18, 19]. Eventhough di erences exist among the proposedtechniques, 140they allshareacommonheuristicandrelyonpreviousfailureknowledge. Elbaumetal. [14] arguedthattraditionalRT techniques tendtorelyoncodeinstrumentation andare applicable onlytodiscrete,completesetsoftestcases.However,RT inCIenvironments is performed more frequently and continuously. Thus,approaches that require exhaustive analysis areoverlyexpensiveandinecientduetothehighfrequencyofchanges;this 145makes thedatagatheredbysuchapproachesimpreciseandobsolete.Elbaumetal.[14] conducted anempiricalstudyonalargedatasetobtainedfromGoogleandpresented novelRTSandTCPtechniques.Theproposedapproachesarebasedonthenotionof time windows totrack how recently testsuiteswere executedandrevealed failures.This information wasutilizedtoselecttestsuitestobeexecutedduringpre-submittesting 150and toprioritizetestsuitesthatmustbeperformedduringpost-submittesting. Marijan etal.[15]proposedaTCPtechnique which reliesonpreviousfailureknowl- edge, testexecutiontime,anddomain-speci cheuristicstocomputethetestpriority using aweightedfunction.Strandbergetal.[16]presentedanexperiencereportand proposed anautomatedtoolwhichaimedtocombineprioritiesofmultiplefactorsasso- 155ciated withtestcases.Spiekeretal.[19]conductedindustrialcasestudiesandproposed an approachthatusedreinforcementlearningtoselectandprioritizetestcasesaccord- ing totheirduration,previouslastexecution,andfailurehistory.Srikanthetal.[17] conducted anempiricalstudyonTCPforthebuildacceptancetestprocessofalarge enterprise software-as-a-serviceapplication.Findingsindicatedthatorderingbuildac- 160ceptance testscansigni cantly impacteciencyoftestingandthattheuseofhistorical data isagoodheuristicfortestprioritization. Hemmati etal.[18]investigated thee ectiveness ofthreeblack-box TCPtechniques

# ACCEPTED MANUSCRIPT

on Firefoxbeforeandafterthetransitiontorapidreleases.Theauthorsconcludedthat 6


---

<!-- Página 8 -->

### ACCEPTED MANUSCRIPT

HBTP is farmore e ective than othercomparable techniques inrapid releases,although 165the sameconclusiondoesnotholdintraditionaldevelopment environments. Therefore, the teststhatfailedinpreviousreleaseshave amuch higherprobabilityoffailingagain in thecurrent release.Thisisperhapsduetotherecencyofhistoricalknowledge, which explains its e ectiveness in a rapid-release environment, rather than other changes in the developmentprocess[18]. Thereis also a number of studies that are particularly focused 170on HBTP. For instance, Kim and Porter [13] proposed a TCP technique that relies on test execution history, itsfaultdetection,andtheprogramentitiesitcovers.Followingthis study,others[28,29,30]investigatedHBTPandproposedvariousmodelstocompute the priorityoftestcasesusingpreviousfailureknowledgeandothercomplementary information.

1752.2.2. Diversity-basedTest Prioritization Coverage-basedTCPhasbeenextensivelystudiedintheliterature(seethelatest systematic literaturereviewonTCP[26]).Onecommonheuristicistoassignahigher rank tothetestcasesthatcover apartofthesystemthathasnotbeenexaminedearlier by othertestcases[11].Toincreasethelikelihoodofcapturingfaults,onepotential 180strategy istospreadthetestingbudgetevenlyacrossdi erentpartsofthesystemby performing a diverse set of test cases. Diversity-basedTCP has been previously proposed in the literature. Forinstance, Leon and Podgurski [31], proposeda TCP technique using automatic cluster analysis to partition the poolof test cases based on how their execution pro les aredistributedinthepro lespace.ThistechniquewaslaterextendedbyYoo 185et al.[32]toincorporatethedomainexpertknowledge.Morerecently, Ledruetal.[20] employedstringmetricstomeasurethesimilaritiesamongtestcases. The underlyinghypothesisisthatsimilartestcaseswilllikelyexercisethesame part ofthesystemanddetectthesamefault;thus,adiversesetoftestcasesmustbe performed todetectmorefaults[21].Thishypothesishasbeenfurtherinvestigatedby 190other researchers,e.g.,[33,34,35,36,18,20,37,38].TheimplicationforTCPisthat higher prioritymustbeassignedtothosetestcasesthataremostdi erentfrom already prioritized.Diversity-basedTCPcanbeimplementedusingdi erentmethods and ondi erentlevels,e.g.,source-codebehindtestcases[20],methodcalls[36],topic models extractedfromtestcases[38],orEnglishtextsofmanualtest[18]. 195Toachievediversity-basedTCP,thedissimilarityamongtestcasesmustbecalcu- lated usingaparticularmethod;thisinformationmustthenbeleveragedtoprioritize test cases.Thereareseveralsimilaritymetricsproposedintheliteratureandusedin diverse areas,e.g.,classi cationproblems,plagiarismdetection,andimageandDNA analysis. Itis commonly understoodthat similarity metrics have di erent characteristics 200and are typically speci cto a certain type of data. Ledruet al. [20]conducted a compre- hensive experimenton\SiemensTest Suite"andevaluatedfourclassicalstringmetrics for thepurposeofTCP,includingCartesian,Levenshtein,Hamming,andManhattan distance. Theirndings indicated that TCP using string metrics is more e ective than a randomly ordered test suite, and Manhattan distance yields betterresults than the other 205investigatedmetrics. Tocalculate the distance between a testand set of test cases 0T, Ledruetal.proposedthefollowingfunctionwhichusesdistanced :measure

00AllDistances(t; T ; d) =minf d (t; t)jt2T; t 6tgiii

# ACCEPTED MANUSCRIPT

7


---

<!-- Página 9 -->

### ACCEPTED MANUSCRIPT

Ledru etal.usedtheminoperationbecauseanempiricalstudybyJiangetal.[21] showedthatmaximize-minimumismoreecientincomparisontomaximize-average and maximize-maximum. Ledruetal.alsoproposedagreedyalgorithmthatiteratively 210picks atestcasehaving maximum distance(i.e.,ismostdissimilar)tothesetofalready prioritized testcases.NCDisanothersimilaritymetricwhichisuniversalandcanbe applied toanystringsofdata,regardlessofdatatypeinvestigated[39,40].NCDhas been extensivelyusedinawiderangeofapplicationareas(seethemanyreferencesin Google Scholar to [39, 40]). NCDis given as follows,Ciswherea function that calculates 215the approximate Kolmogorov complexity andreturnsthelengthoftheinputstringafter its compression,usingachosencompressionprogram:

C (xy )  minf C (x ); C (y )g N CD(x; y) = maxf C (x ); C (y )g

In 2015,CohenandVitanyi[41]extendedtheapplicationofNCDformultisets(a particular type of set which allows multiple instances). NCDMultiset provides similarity measurement at the level of entire sets of elements rather than between pairs. Feldtet al. 220[42] performedthe rst study in software engineering literature that used NCD Multiset. They conductedanexperiment,theresultsofwhich show thattestselectionusingNCD Multiset leads to higher structural and fault coverage in comparison to random selection. NCD Multisethasalsobeenusedrecently inTCPliterature[43]andtheresultsseemto be promising.

2252.2.3. ResearchGap In comparison to previous studies, we make three contributions. First,we thoroughly investigatetheimpactofthehistoryinterval sizeonthee ectiveness ofHBTP. Itmight be assumedthatalargesetofhistoricaldataisrequiredtoe ectivelydeployHBTPin practice. Speci cally,historyinterval size(i.e.,thenumberofpreviousverdictsused)is 230often notreportedinpreviousworksanditsimpactonthee ectivenessofHBTPhas not beenstudied.Inthiswork,weperformHBTPusingdi eringnumbersofprevious verdicts and investigate whether its e ectiveness changes by varying the size of the history interval.Furthermore,weclassifyregressionfaultsaccordingtotheirpastverdictsand study theextenttowhichtheycanbecapturedusingpreviousfailuresknowledge. 235Second, toimprovethee ectivenessofHBTP,wecombinepreviousfailureknowl- edge withdiversity-basedTCP. Priorworkshaveusedpreviousfailureknowledgewith code-coverage [44,45],multiplefactorsassociatedwithtestcasesandrecentmodi ca- tions [16],servicecompositioninteractions[17],ordomain-speci cheuristics[15].Even though diversity-basedTCPhasbeenproposedandusedpreviously,ithasnotbeen 240widely studiedincombinationwithHBTPandinCIenvironments.Hemmatietal. [18] previouslyinvestigated ahistory-baseddiversity approachinFirefoxproject.They used previousfailureknowledge incombination withasinglesimilarity metric,Manhat- tan distance,usingtheEnglishtextsofmanualtestcases.Incontrast,weinvestigated history-based diversityusingthreedi erentsimilaritymetrics(Manhattan,NCD,and 245NCD Multiset)withdi erenthistoryintervalsizes,overalargenumberofautomated builds extractedfromsixopen-sourceprojects.Thishasnotbeenstudiedinthepast, to thebestofourknowledge. Third, forthe history-based diversity approach to beapplicable in a CI environment,

# ACCEPTED MANUSCRIPT

8


---

<!-- Página 10 -->

### ACCEPTED MANUSCRIPT

both e ectivenessandperformancearecritical.Inthisstudy, apartfrome ectiveness, 250we investigated themethodexecutiontimewithinandacrossthestudiedprojects.

3. ResearchMethod

The study'sobjectiveandresearchquestions,datapropertiesanddataextraction procedure, studydesign,andanalysismethodsarediscussed,inthatorder.

3.1. ObjectiveandResearch Questions 255The mainobjectiveofourstudyistoshortentheRT feedbackcycleforcontinuous integration of software systems. Inother words, we aim to catch regression faults earlier, allowing developerstointegrateandverifytheirchangesmorefrequentlyandcontinu- ously.Toachievethatend,weinvestigatedsixopen-sourcesoftwareprojects,eachof which includedseveralbuildsoveralargeperiodoftime.Theresearchquestionsand 260their rationalesareasfollows:

RQ1: Towhatextentcanregressionfaultsbecapturede ectivelyby using previousfailureknowledge?This researchquestionisdesignedtoana- lyze regression faults according to their past verdicts and study the extent to which they canbecapturedusingknowledgeoftheirpreviousfailures.

265RQ2: Doesthee ectivenessofHBTPchangeovertimewithalarger history interval?This researchquestionisdesignedtostudywhethertheef- fectiveness ofHBTPchangesovertimeifalargerhistoryintervalsizeisused. In thisquestion,weperformHBTPusingadi eringnumberofpreviousverdicts and investigate whetheritse ectivenesschanges by varying thesizeofthehistory 270interval.

RQ3: Doesthee ectivenessofHBTPchangewhencombinedwith diversity-basedprioritization?This researchquestionisdesignedtostudy whether thee ectivenessofHBTPchangesbyre-orderingtestsbasedontheir distances (i.e.,theirdissimilarity)tothesetofalreadyprioritizedtests.

275RQ4: Amongtheinvestigatedtestprioritizationtechniques,whichis most e ectiveandhasthebestperformancecomparedtotheothers? This research question is designed to compare the e ectiveness and performanceof investigatedTCPtechniqueswithinandacrossthestudiedsubjects.

3.2. SoftwareSubjects 280Toperformourexperiment,weusedTravisTorrent [46],afreelyavailabledatabase based onTravis CIandGitHub,thatprovides accesstothebuildinformationofseveral projects. TravisTorrents databaseincludesseveralpropertiesandinformationabouta 1projects Travisbuildhistory. However,TravisTorrents databasedoesnotinclude information aboutthelistofexecutedtestsortheirverdicts(i.e.,passedorfailed)

1A[https://travistorrent](https://travistorrent).

# ACCEPTED MANUSCRIPT

testroots.org/page_dataformat/. 9

for


---

<!-- Página 11 -->

### ACCEPTED MANUSCRIPT

285each revision.Toextracttherequireddataforourstudy,wedownloadedallavailable 2build logsforthestudiedprojectsandautomaticallyanalyzed. Thethemfollowing data propertieswereextracted:

Commit-ID: Theuniqueidenti eroftheoriginalcommitextractedfromTravis- Torrent.

290Files modi ed:Thelistofmodi edles,extractedfromGitHubforaparticular commit.

Testresults: Thelist of executed tests and their verdicts, extracted from build logs.

Build time:Theoriginalbuildtime,extractedfromTravisTorrent.

The buildlogstypically includealistofexecutedtestlesandtheirverdicts. There- 295fore, thegranularitylevelinthisstudyisatthelelevel,althoughtheinvestigated prioritization techniques canbeappliedtoany level ifdataisavailable. Inpractice, softwareprojectmightbeacandidatesubjectifitsbuildlogsareavailable andinclude information onthelistofexecutedtestsandtheirverdicts. Thestructureandformat build logs varies among software projects,dependingon theand testing framework 300used duringthedevelopment. Forthepurposeofthisstudy, weselectedsixJava-based softwareprojectsinordertominimizethee ortinthedatacollectionphase.However, the above-mentioneddatapropertiescanbegatheredeasilyfromanyCIdevelopment environment,independentofitsunderlyingtechnologies. Table1 represents the characteristics of analyzed projects.Therst column indicates 305the projectname and abbreviated identi er. Thesecond column is a range and indicates the analyzedbuildtimeperiod.Thethirdcolumnshowstheactualnumberof builds; theparenthesesindicatethenumberofbuildswhichincludedRToutput.The fourth columnshowsthenumberofbuildsinwhichatleastonetestfailed.Thefth column showsthenumberofuniquetestsidenti edfrombuildlogs,whilethesixth 310column is a range that refers to the number of executed tests during builds (each of which might includeseveral testcases).Thelastcolumnshows thesourceline-of-code(SLOC) 3for themostrecentstudiedversion,asreportedbySLOCCount. TheabbreviatedID is usedintheremainingsectionswhenwerefertotheseprojects.

2Tohttps:// travistorrent.testroots.org/buildlogs/ 3SLOCCount[https://www.dwheeler.com/](https://www.dwheeler.com/) sloccount/

# ACCEPTED MANUSCRIPT

10

any

of


---

<!-- Página 12 -->

### ACCEPTED MANUSCRIPT

Table Name (ID)Time FrameBuildsFaultyTestsTestSLOC BuildsSuite Size Google Guava (GUV)2014/11/05-46541411365-404247,497 2016/08/29(458) MyBatis (MYB)2013/02/14-98827278198-24186,549 2016/08/23(923) Apache Tajo(TAJ)2014/05/08-467056431330-241248,155 2016/08/29(3908) AWSJava SDK (AWS)2013/05/01-8638514458-1141,411,875 2016/08/31(449) DSpace (DSP)2013/07/25-3813718016-61289,703 2016/08/31(3327) Apache Storm(STM)2015/04/23-21965421356-60214,437 2016/09/01(1962)

3.3. StudyDesign

3153.3.1. RQ1:Towhatextentcan regression faultsbe captured e ectively byusingprevious failureknowledge? The objectiveofthisresearch questionwas toinvestigate theextent towhich regres- sion faultscanbecapturedusingpreviousfailureknowledge.Toanswerthisquestion, we classi ed regression faults according to their past verdicts, i.e., those that can becap- 320tured using previous failure knowledge (T1) and those without any(T2). In otherwords,T1includesregressionfaultsthataredetectedbytestcaseswhichhave been failedearlier(i.e.,failurestatusobservedintheexecutionofthetestcase). In contrast,T2includesfaultsthataredetectedbytestcaseswhichhaveneverbeen failed earlier(i.e.,nopreviousverdictsexistorexecutionofthetestcasehave 325been always passed).Thisinformationmightbehelpfulinunderstandingthenatureof regression faultsintheinvestigatedprojects,e.g.,whethertheycanbepredictedand captured usingpreviousfailureknowledge. ForT1regressionfaults,we furthercalculatedthegap(number ofverdicts) between the observedfailureandthepreviousfailure.Thisinformationhelpsustounderstand 330the distancesamongregressionfaultsandmightbeusefulinadjustingtheinterval size of HBTP, thatis,thenumberofpreviousverdictsweshouldtaketocaptureregression faults e ectively. ForT2regressionfaults,wecalculatedthegap(numberofverdicts) between anobservedfailureandtherstavailableverdict.Thisinformationmightbe an indicationoftheageoffault-revealingtestswithinourhistoricaldata.

3353.3.2. RQ2:Doesthee ectivenessofHBTPchangeovertimewithalargerhistory interval? The objectiveofthisresearchquestionwastoinvestigatewhetherthee ectiveness of HBTPchangesbyvaryingthesizeofthehistoryinterval(i.e.,thenumberofpast verdicts taken into account). Thee ectiveness of HBTP was measured using the average 340percentage offaultsdetected(APFD),whichisacommonmetricusedintheliterature

# ACCEPTED MANUSCRIPT

11


---

<!-- Página 13 -->

### ACCEPTED MANUSCRIPT

and elaboratedinsection3.4.TheHBTPusedinthisstudyissimilartothecluster- based technique proposed by Hemmati et al. [18].Therationale is that such an approach only requirespreviousfailureknowledgeandthatwehave accesstosuchinformation. In ourstudy,wecalculatedthecumulativepriorityforeachtestusingitsprevious 345failures overthelastNbuilds (dependingontheintervalsize).Thehighestweight corresponds to the failure exposed in a previous build (currentand thein every preceding buildisweightedlowerthanthefailureinitssuccessivebuild.Speci cally, failures are weighted by their distanceW, that re ect the impact of the failure occurredn in thepastandisbuilds farfromthecurrentbuildsession.Thefollowingvalues were 350assigned totheweights. 8 0 :9 ; ifn= 1>>>>>0 :8 ; ifn= 2>>>>>0 :7 ; ifn= 3>>>>>0 :6 ; ifn= 4< W=0 :5 ; ifn= 5n >>>0 :4 ; ifn= 6>>>>>0 :3 ; ifn= 7>>>>>0 :2 ; ifn= 8>>: 0 :1 ; ifn9

Thereafter, weaggregatedtestsintoclustersbasedontheirweight andsortedthese clusters indescendingorder.Toanswerthisresearchquestion,wecomparedthee ec- tiveness ofHBTPwithrandompermutation(RND)andwitheachotherusingdi erent intervalsizes(V1,V10,V100,V500).UsingHTBPapproach, testcaseswithouthistori- 355cal failure are groupedin a single cluster and remain in their original order (i.e, the in whichtheyexecutedandappearedinthebuildlogs).Therewasalsothepossibility that theinvestigatedprojectsmighthavealreadyusedTCPtechniques.Toavoidthe impact of this and create a fair comparison with random ordering, we simply randomized the intra-clustertestsforthepurposeofthisresearchquestion.Thistechniqueiscalled 360history-based random(HBR)inourstudy. Coverage-basedTCPisanimportantbaselineintheliterature,butexcludedinour experiment duetothedicultiesassociatedwithcollectingcoveragedataforthesub- ject programs.Thecoveragedatacanbeondi erentlevel(e.g.,statement,branch, method coverage)andobtainedusingdynamicallyanalyzingtheprogramexecutionor 365by staticallyanalyzingthetestandsource-code.Gatheringcoverage datawaschalleng- ing withoursubjects,becausetestinformationhavebeenextractedfromarchival data (build logs),andnotfromactualtestexecutions.Furthermore,thehighfrequencyof changes inCIenvironmentquicklymakesthedatagatheredbycodeinstrumentation imprecise andobsolete[14].Thechallengesassociatedwithcoverage-basedTCPinCI 370environmentsarediscussedintheliterature,e.g.,byElbaumetal.[14]andHemmati et al.[18].Futurestudiesarerequiredtoaddressthesechallengesanddevelopecient instrumentation toolsforCIenvironment.

# ACCEPTED MANUSCRIPT

12


---

<!-- Página 14 -->

### ACCEPTED MANUSCRIPT

3.3.3. RQ3:Doesthee ectiveness ofHBTPchangewhencombined withdiversity-based prioritization? 375Due tothelack ofpreviousfailureknowledge, many testsinourapproach cannotbe e ectively prioritized.Thesetestsendupinasingleclusterifwesolelyprioritizethem based on previous failure knowledge. Thisincludes both newly added tests or those which havenotrevealed any failureinpreviousbuilds.Furthermore,withineach cluster,there might beseveral testswiththesameweight. Tobreakthetie,theintra-clustercan 380be randomizedorotherTCPtechniquescanbeemployed incombinationwithHBTP. The mainobjectiveofthisresearch questionwas toinvestigate whetherthee ective- ness of HBTP changes when it is combined with diversity-based prioritization. Toanswer this researchquestion,westudiedhistory-baseddiversity(HBD)overdi erentinterval sizes andcompareditse ectivenesswithHBR.Thelattertechniquesimplyrandomizes 385tests withineachcluster.Incontrast,HBDiterativelyprioritizestheintra-cluster on thebasisoftheirdistance(dissimilarity) tothesetofalreadyprioritizedtests.Apart from theinterval sizesusedinRQ2(V1,V10,V100,V500),wealsostudiedtheinitial stage (V0),wheretherewasnohistoricaldataavailable athandandthetestsuitewas completely prioritizedusingtestdistances. 390Toanswerthisresearchquestion,weimplementedHBDusingthreesimilaritymet- rics, includingManhattan,NCD,andNCDMultiset.Theseapproacheswereselected because of their promising results reportedin recent studies [20, 43, 42]. Tocalculate the distances, we automatically downloaded source code from Github for all studied revisions 4and usedthesourcecodebehindthetestsattheirexactrevisionWeimplemented the 395Manhattan andNCDapproachesusingapairwisealgorithmproposedbyLedruetal. [20]. FortheNCDMultiset,weimplementedthefollowingalgorithm,whichiteratively picks atestthathasmaximumdistance(ismostdissimilar)totheentiresetofalready prioritized tests(ratherthanbetweenpairs).NoteCisthatafunctionthatcalculates the approximate Kolmogorov complexity andreturnsthelengthoftheinputstringafter 400its compression,usingachosen compressionprogram.Inthisstudy, we usedLZ4,which is ahigh-speedlosslessdatacompressionalgorithmandiswidelyusedinsearchengines 5and databasemanagementsystems.

Algorithm 1:TestPrioritizationUsingNCDMultiset Data: TestSuiteTand PrioritizedSetP S Result:P S whileTis notemptydo FindTwhich maximizesC (P S; T);ii AppendTto P S;i RemoveTfromT ;i end

4Github[https://github.com/{username}/{projectname}/](https://github.com/{username}/{projectname}/) archive/{sha}.zip 5The[http://lz4.github.io/lz4/](http://lz4.github.io/lz4/)

# ACCEPTED MANUSCRIPT

13


---

<!-- Página 15 -->

### ACCEPTED MANUSCRIPT

4053.3.4. RQ4:Amongthe investigated test prioritization techniques, which is most e ective and hasthebestperformance compared totheothers? FortheHBDapproachtobeapplicableinaCIcontext,bothe ectivenessandper- formance arecritical. Thus,apartfromassessing thee ectiveness interms ofAPFD, we studied theperformanceofHDBtechniquesintermsofmethodexecutiontime.Dur- 410ing theinitialstagesofthisresearch,weobservedthatcalculatingdistancesconstitutes the largestportionofmethodexecutiontime.Toimprove theperformanceofHBD,we implemented asimplecachingsystemwheredistancesamongthetestsarecalculated upon requestandretained.Thedistancevalueisupdatedonlyifoneoftherelevant tests is observed in the change list. Thisapproach greatly reduced the methodexecution 415time whenweprioritizedtestsoverseveralrevisionsusingpairwisealgorithms(NCD and Manhattan).However,suchacachingsystemisine ectivewiththeNCDMultiset algorithm becausethedistanceiscalculatedatthelevel ofentire setsofelements rather between pairs.Tospeeduptheprocess,we parallelizedbothpairwiseandmultiset algo- rithms usingconcurrentutilitiesproposedbyJava speci cationrequest(JSR)166.The 420above-mentionedmethodsgreatlyimproved theperformanceofourHBDtechniques.

3.4. Evaluation

Toassessthee ectivenessofTCPtechniques,weusedAPFDmetricthatwasorig- inally introducedbyRothermeletal.[11]andiswidelyusedintheliterature.TLet be anorderedtestsuite,containingntest cases,andFbe asetofmfaults detectedby 425T ; thenT Findicates thenumberoftestcasesexecutedTbeforeincapturingfaulti.i APFD indicatestheaverage percentageoffaultsdetectedandisde nedasfollows:

1T F+T F+:::+T F12M +)AP F D= 100 (1   nm2n In ordertoproperlycomparetheinvestigatedTCPtechniques,weconductedsta- tistical analyses.TheMann{WhitneyUtest[47],anon-parametricsigni cancetest, was appliedtodeterminewhetherthedi erencebetweentwocomparedtechniqueswas 430statistically signi cant(p-valueislessthan0.05).Thenullhypothesisofthistestindi- cates thatthereisnosigni cantdi erencebetweenAPFDsofthetwo techniquesunder evaluation.TheMann{WhitneyUtestwasselectedbecausethestudieddatamaynot follow normaldistribution.Thesigni cancetestindicateswhetherthedi erencebe- tweentwo comparedtechniquesisstatisticallysigni cant,butdoesnotshowthesizeof 435the di erencebetweenthem.Thus,weusedtheVargha{Delaney Ameasure[47],which is anon-parametrice ectsize.TheVargha{Delaney Ameasureisanumberbetween0 and 1.WhentheAmeasureis0.5,thetwocomparedtechniques,XandY,areequal. When the A measure is higher than 0.5, it means that X outperformedY, and vice versa. Furthermore,when comparing TCP techniques, we also provided violin plots to visualize 440the distributionofAPFDs.

4. Findings

This sectionisstructuredtoaddresstheresearchquestionsandincludestheaggre- gated analysisofresultsfromourexperiments.Theexperimentswereconductedona computer withIntel2.7GHzXeonE5-2680(8cores)and16GBinstalledRAM.

# ACCEPTED MANUSCRIPT

14


---

<!-- Página 16 -->

### ACCEPTED MANUSCRIPT

4454.1. RQ1:Towhatextentcanregression faultsbecaptured e ectivelybyusingprevious failureknowledge?

Table2showstheaggregatednumberoffault-revealingtests,regressionfaults,and the ratiooftwodi erenttypesofregressionfaults.Itcanbeseenthatinthemajority of investigatedprojects,onlyasmallproportionoftestshaseverfailed(lessthan11% 450in fourprojects,and3{52%overall).ThisindeedunderscorestheimportanceofTCP in CIenvironments,whereRT isperformedmorefrequentlyandcontinuously. Froma historical perspective,regressionfaultscanbeclassi edintotwo groups:thosethatcan be captured using previous failure knowledge (T1), and those without any (T2). Ourndingsindicatethatthemajorityofregressionfaultsamongallinvestigated 455projects are T1 (57{97%) and can be captured solely by using previous failure knowledge. In four of the investigated subjects,only a small proportion(less than 13%) of regression faults are classi ed as T2 and cannot becaptured using previous failure knowledge. This number ishigherintheMYB(43%)andGUV(23%)projects.

Table Project# Tests# Fault-revealing# FaultsT1T2 MYB27826 (9.3%)6057%43% GUV41113 (3.1%)5677%23% AWS14414 (9.7%)12389%11% DSP8042 (52.5%)35388%12% STM13514 (10.3%)56497%3% TAJ313136 (43.4%)108787%13%

Togainabetterunderstandingoftheregressionfaults,weconductedadeeperanal- 460ysis. ForT1regressionfaults,wecalculatedthegap(numberofverdicts)betweenthe observed failureandthepreviousfailure.ForT2regressionfaults,wecalculatedthe gap between theobserved failurewiththerstavailable verdict. Table3shows theve- number summary of gaps for T1 and T2 regression faults. Thegap between two observed failures varies amongthestudiedprojectsandcanbeusedtoadjustthee ectivenessof 465HBTP.Fromtheresults,itcanbeseenthat50%ofT1regressionfaultswithinthree investigatedprojects(MYB,GUV,andAWS)canbecapturedonlybyusingthelast verdict (current  1). FortheAWSproject,only16previousverdictsarerequiredto capture 100%ofT1regressionfaults,whichconstitute89%oftotalfaults. ForT2 regression faults, a small portionoffaults occurredwhen a test was in- 470troduced tothetestsuite(25%inthecaseofAWS). However, themajorityofT2faults were introducedduetothechangeinthesystemandpreviousfailureknowledgewas not available. Thus,extrainformationisrequiredtoe ectivelycapturetheseregression faults.

# ACCEPTED MANUSCRIPT

15


---

<!-- Página 17 -->

### ACCEPTED MANUSCRIPT

Table T1 RegressionFaultsT2 Project MinP25P50P75MaxMinP25P50P75Max MYB111942680114192289900 GUV1111162053127371376 AWS1111.5160079367384 DSP12262511023184407487481989 STM113644704.7517.5191600 TAJ13181082243014765015593241

4.2. RQ2:Doesthee ectiveness ofHBTPchangeovertimewithalarger historyinter- 475val?

Foreachfaultybuildwithintheinvestigated projects,weprioritizedtestsusingdif- ferent history interval sizes, i.e.,thenumber of previous verdicts (V1, V10,V100,V500). The ndings presented in this section are based on the aggregated results of all execution rounds. Foreachproject,wehadaccesstoadi erentnumberoffaultybuilds.Thus, 480the aggregatedresultsarebasedondi erent numbers ofobservations (seethenumber of faulty buildspresentedinTable 1). Table4shows thee ectiveness ofHBTPusingdi erent interval sizes.Itcanbeseen that HBTPdoesnotnecessarilyneedtohavealargeamountofhistoricaldata.Even with the last verdict (current  1), improvement (0.53{0.82) was observed in all projects in 485comparison to random ordering. Whenwe took the last 10 verdicts, greater improvement (0.53{0.61) wasobservedinvestudiedprojectsincomparisontoHBTP-V1.Whenwe extended ourinterval sizetothelast100verdicts,thee ectivenessofHBTPimproved (0.61{0.67) infourinvestigatedprojects.Takingthelast500verdictswouldleadto negligible improvement(0.51and0.54)inonlytwosubjects.Theremainingprojects 490show a negligible decline (0.47{0.49) on APFD. Our ndings imply that the e ectiveness of HBTPchangesovertimebytakingalargerhistoryinterval.However,theimpact of thephenomenonvariesamongprojectsandisperhapsassociatedwiththenatureof regression faults and their distances (see RQ1). Overall,within the investigated projects, we observedthat,toacertaindegree,changingtheinterval sizewouldleadtopositive 495improvementintermsofAPFD.Figure2illustratesthefulldistributionofAPFDsfor RND andHBRover di erentinterval sizes.

Table MeanE ect-size (Xvs-Y) Project RNDV1V10V100V500V1-RNDV10-1V100-10V500-100 MYB48.9367.1471.1366.4467.390.680.530.440.48 GUV53.1584.4588.9587.8588.320.820.540.460.49 AWS52.5762.0169.6486.0183.320.600.580.640.47 DSP50.8662.8058.6477.9981.480.620.470.640.48 STM49.7553.2457.8177.6884.190.530.540.670.54 TAJ49.5153.5965.6278.8583.380.530.610.610.51

# ACCEPTED MANUSCRIPT

16


---

<!-- Página 18 -->

### ACCEPTED MANUSCRIPT

Figure

4.3. RQ3:Doesthee ectivenessofHBTPchangewhencombinedwithdiversity-based prioritization?

Toanswerthisquestion,wecomparedthee ectivenessofHBRwithHBDoverdif- 500ferent interval sizes. Thelatter technique prioritizes the intra-cluster tests based on their distance (dissimilarity)tothesetofalreadyprioritizedtests.Incontrast,HBRsimply randomizes tests within each cluster. Threedi erent similarity metrics were used, includ- ing NCD,NCDMultiset(NCD-MS),andManhattan(MNH).Apartfromtheinterval sizes used in RQ2, we also studied the initial stage (V0), whenthere is no historical data 505availableathand,andthetestsuiteiscompletelyprioritizedusingtestdistances.Table 5 to10presenttheAPFDmeanande ectsizeofdi erenttechniquesforeachproject using di erentintervalsizes.FiguresA.3toA.8presentedinAppendixAshowthe violin plotsforeachprojectover di erentinterval sizes. The resultsindicateanoticeableimprovement whennohistoricaldatawasavailable 510(V0) andthetestsuitewasprioritizedsolelybyusingtestdistances.Thisimpliesthat

# ACCEPTED MANUSCRIPT

diversity-basedTCP can be used e ectively during the early stages of HBTP deployment, 17


---

<!-- Página 19 -->

### ACCEPTED MANUSCRIPT

when nohistoricaldataisavailable. Amongtheinvestigatedtechniques,NCD-MSwas the bestandgreatlyimprovedthee ectivenessofHBTP-V0(0.68{0.91)incomparison to MNH(0.47{0.91)andNCD(0.51{0.92).Whenwecombinedthediversity-based 515approach withHBTP(V1,V10,V100,V500),positiveimprovement wasalsoobserved in the majorityof cases (19/24for NCD and Manhattan, and24/24 for NCD-MS). Among theinvestigatedtechniques,NCD-MSwasthebestandconsistentlyimproved the e ectiveness of HBTP (0.51{0.73) using di erent interval sizes. Thesedi erences are also statisticallysigni cantinthemajorityofthecasesforNCD-MS. 520Our ndingsindicatethatthee ectivenessofHBTPchangeswhencombinedwith diversity-basedTCP.Inotherwords,re-orderingintra-clustertestsbasedontheirdis- similarity to the set of already prioritized tests has a positive impact on the e ectiveness of HBTP. Thisimpactseemstoberelativelysmallerwhenwetakealargerhistoryin- tervalintoaccount.Thisisperhapsduetothefactthattakingmoreverdictsleadsto 525more clusters,withasmallernumber ofintra-cluster tests.Thus,moreregressionfaults can bepotentiallycapturedandthereisahigherchanceofadrawbetweenHBTPand HBD. Ontheotherhand,moreclustersofasmallersizemeansthatlessexibilityis given tothediversity-based approachinre-orderingtheseintra-clustertests.Theviolin plots presented in AppendixAshow that HBD not only improved e ectiveness, but also 530tended tohave lessvariance intheresults.

Table APFD MeanE ect-size Xvs.HBR MYB HBRNCDNCD-MSMNHNCDMNH V045.1366.9469.6266.370.720.740.72 V167.1477.680.3277.550.570.610.57 V1071.1378.9281.0477.950.570.590.56 V10066.4478.4180.675.250.580.610.57 V50067.3978.7181.1276.330.550.580.55

Table APFD MeanE ect-size Xvs.HBR GUV HBRNCDNCD-MSMNHNCDMNH V048.0187.6584.5883.030.920.910.91 V184.4593.8494.5894.50.550.530.54 V1088.9594.0695.0094.920.510.510.52 V10087.8593.894.8994.750.510.510.51 V50088.3293.5194.8894.780.520.520.52

# ACCEPTED MANUSCRIPT

18


---

<!-- Página 20 -->

### ACCEPTED MANUSCRIPT

Table APFD MeanE ect-size X AWS HBRNCDNCD-MSMNHNCD V049.6551.3568.5649.290.51 V162.0158.8772.555.10.45 V1069.6469.0877.9465.160.48 V10086.0187.0987.9286.220.52 V50083.3286.9287.6986.220.54

Table APFD MeanE ect-size X DSP HBRNCDNCD-MSMNHNCD V052.0554.9469.6368.550.51 V162.861.2572.1671.560.47 V1058.6467.4575.6575.360.57 V10077.9978.0483.0983.030.49 V50081.4882.685.3984.980.51

Table APFD MeanE ect-size X STM HBRNCDNCD-MSMNHNCD V051.2372.9577.4768.540.73 V153.2473.4877.8469.080.7 V1057.8175.279.5571.520.64 V10077.6883.1184.0378.380.52 V50084.1988.1590.6886.720.5

Table APFD MeanE ect-size X TAJ HBRNCDNCD-MSMNHNCD V050.1265.4369.1265.860.66 V153.5968.0671.3368.380.64 V1065.6274.0977.4374.250.56 V10078.8582.6985.3484.280.52 V50083.3885.5887.7687.480.51

4.4. RQ4:Amongtheinvestigatedtestprioritization and hasthebestperformance compared totheothers? FortheHBDapproachtobeapplicableinaCIcontext,

# ACCEPTED MANUSCRIPT

of APFD)andperformance(intermsofaveragemethod 19

vs.HBR MNH 0.700.47 0.600.42 0.560.45 0.530.50 0.550.52

vs.HBR MNH 0.680.65 0.580.58 0.640.63 0.530.53 0.530.52

vs.HBR MNH 0.760.67 0.730.65 0.670.61 0.520.50 0.510.50

vs.HBR MNH 0.700.66 0.670.64 0.590.56 0.530.53 0.520.52

techniques,whichismoste ective

bothe ectiveness(interms executiontime(AMET))are


---

<!-- Página 21 -->

### ACCEPTED MANUSCRIPT

535critical. Table11 compares the e ectiveness of investigated techniques within and across the studiedprojects.Foreach project,we calculatedthesumofAPFDsachieved across all interval sizes(V0{V500).Table12,ontheotherhand,comparestheperformanceof investigatedtechniqueswithinandacrossthestudiedprojects. In terms of e ectiveness, the HBD techniques achieved higher scores in comparison to 540HBR (68.47 average APFD across all projects).Manhattanand NCD achieved very close overallscores in terms of average APFD across all projects (77.17 and 76.99, respectively). NCD Multisetwasasuperiortechniquewithinandacrosstheinvestigated projectsand achievedthehighestscore(81.25average APFDacrossallprojects).Intermsofperfor- mance, HBRwasthefastestandalways scoredaverylowAMET(0.1second).Among 545HDB techniques, NCDwas the bestin terms of AMET (4.55 seconds), followed by Man- hattan andNCDMultiset(17.58and57.58seconds,respectively).Overall,ourndings indicate thatNCDMultisetoutperformsbothpairwiseNCDandManhattaninterms of e ectiveness buthasrelatively higheroverhead intermsofaverage methodexecution time (approximately 3.2 times higher than Manhattan and 12.6than NCD).

Table ProjectHBRHBD NCDHBD NCD-MSHBD MNH MYB317.23380.58392.7373.45 GUV397.58462.86463.93461.98 AWS350.63353.31394.61341.99 DSP332.96344.28385.92383.48 STM324.15392.89409.57374.24 TAJ331.56375.85390.98380.25 TotalAPFD2054.112309.772437.712315.39 Average APFD68.4776.9981.2577.17

Table ProjectHBRHBD NCDHBD NCD-MSHBD MNH MYB0.014.8317.7113.09 GUV0.0116.93288.4960.89 AWS0.011.271.641.41 DSP0.010.121.030.83 STM0.010.030.490.28 TAJ0.014.1336.1428.99 TotalAMET0.0627.31345.5105.49 Average AMET0.014.5557.5817.58

5505. Discussion

WeconductedthisresearchwiththeobjectiveofimprovingtheRTfeedbackcycle for continuousintegrationofsoftwaresystems.Inotherwords,ouraimwastocatch regressionfaultsearlier,allowingdeveloperstointegrateandverifytheirchangesmore

# ACCEPTED MANUSCRIPT

20


---

<!-- Página 22 -->

### ACCEPTED MANUSCRIPT

frequently andcontinuously. Toachievethataim,weinvestigatedsixopen-sourcesoft- 555ware projects,eachofwhichincludedseveralbuildsover alargeperiodoftime.

5.1. OverviewofFindingsandTheirImplications

RQ1: Towhat extent can regression faults becaptured e ectively by using previous failureknowledge?ToaddressRQ1,weaggregatedthenumberoffault- revealing tests,regressionfaults,andtheratiooftwo di erent typesoffaults. 560Our resultsshow thatonlyasmallproportionoftestshasever failedwithinthestudied subjects (11% infourprojects,and3{52%overall). Thisindeedraisestheimportance of TCPinCIenvironments,whereRT isperformedmorefrequentlyandcontinuously. Weclassi edregressionfaultsaccordingtotheirpastverdicts,i.e.,thosethatcanbe captured usingpreviousfailureknowledge(T1),andthosewithoutany 565(T2). Ourndingsindicatethatthemajorityofregressionfaults(57{97%)amongall investigatedprojectscanbecapturedsolelybyusingpreviousfailureknowledge.This implies thatpreviousfailureknowledgeseemstohavestrongpredictivepowerinCI environmentsandcanbeusedtoprioritizetestse ectively. TCP usingpreviousfailureknowledgeinCIenvironmentshasbeenpreviouslypro- 570posed [18,14,15,17,13,16];itse ectivenessisperhapsmainlylinkedtothenatureof developmentenvironment,inwhichdevelopersperformautomatedbuildsatfrequent, short intervals.Therefore,theteststhatfailedinpreviousbuildshaveamuchhigher probability offailingagaininthecurrentbuild.Thisisinlinewiththeexperiment conducted byHemmatietal.[18],wheretheauthorsarguethatHBTPisparticularly 575e ective inrapid-releaseenvironments duetotherecencyofhistoricalknowledgerather than otherchanges intheprocess.Thegap(number ofverdicts) between two regression faults variesamongtheprojectsandcanbeusedtoadjustthee ectivenessofHBTP. The majorityofT2regressionfaultsoriginatedfromoldtestsandwereintroduceddue to the change in the system without having any previous failure. Thus,extra information 580is requiredtoe ectivelycapturetheseregressionfaults. RQ2: Doesthee ectivenessofHBTPchangeovertimewithalarger history interval?ToaddressRQ2,weinvestigatedthee ectivenessofHBTPwith random orderingandwitheachotherusingdi erentinterval sizes.TheHBTPmethod used inourstudywassimilartothecluster-basedtechniqueproposedbyHemmatiet 585al. [18]andwassolelybasedonpreviousfailureknowledge.Ourndingsshowthat HBTP doesnotnecessarilyneedtohavealargeamountofhistoricaldata.Evenwith the lastverdict(current  1), improvement (Vargha{Delaney Ameasure:0.53{0.82)was observed inallstudiedprojectsincomparisontorandomordering.Wealso that thee ectivenessofHBTPchangesbyvaryingthehistoryintervalsize.Within 590the investigatedsubjects,ourresultsindicatethat,toacertaindegree,changingthe intervalsizeleadstopositiveimprovementintermsofAPFD.However,theimpact of thephenomenonvariesamongprojects.Thisvariationisperhapslinkedwiththe nature ofregressionfaultsandthegapsamongthem.Thehigherthegapbetween twofailures,thelargertheinterval sizethatisrequiredtoe ectivelycaptureregression 595faults. Overall,ourresultsimplythatHBTPcanbedeployedeasilyinpractice,with negligible investment. Theonlyrequiredinformationispreviousfailuredata,which can be collectedeasilyinanyCIenvironment,independentofthedevelopmenttechnology used.

# ACCEPTED MANUSCRIPT

21


---

<!-- Página 23 -->

### ACCEPTED MANUSCRIPT

RQ3: Doesthe e ectiveness of HBTP change when combined with diversity- 600based prioritization?ToaddressRQ3,weinvestigatedthee ectivenessofHBDvs. HBR overdi erentintervalsizes.Forthepurposeofthisresearchquestion,weimple- mented history-based diversity using three di erent similarity metrics, including Manhat- tan, NCD,andNCDMultiset.TheManhattanandNCDapproaches were implemented using apairwisealgorithmproposedbyLedruetal.[20],andNCDMultisetwasim- 605plemented byusingthealgorithmdescribedinsection3.3.Thee ectivenessofHBTP changes whencombinedwithdiversity-based prioritization.Inotherwords,re-ordering intra-cluster testsbasedontheirdissimilaritytothesetofalreadyprioritizedhas a positiveimpactonthee ectivenessofHBTP.Weobservethattakinglargerhistory intervalrelativelyreducesthemagnitudeofsuchimpact.Thisisduetothefactthat 610taking larger history interval leads to more clusters with a smaller number of intra-cluster tests. Thus,HBDhasalessexibilityinre-orderingtheseintra-clustertestsandthere is ahigherchanceofdrawbetweenHBTPandHBD.Overall,ourndingsimplythat diversity-basedprioritizationcanbeusede ectivelyduringtheearlystagesofsoftware development,whenhistoricaldataarenotyet available orarescarce,andalsocombined 615with HBTPtoimprove itse ectiveness. RQ4: Amongthe investigated test prioritizationtechniques, which is most e ective andhasthebestperformancecomparedtotheothers?Toachieve diversity-basedTCP,thedistance(dissimilarity)amongtestcasesmustbecalculated using aparticularmethod;thisinformationmustthenbeleveragedtoperformTCP. 620Toassessthedissimilaritiesamongthetests,weusedtheirsourcecode;thisincluded test input,testprocedure,andassertstatements.However,anysourceofinformation about testcasescanbeusedinpractice.Duringtheinitialstagesofthisresearch,we observed thatcalculatingdistancesconstitutedthelargestportionofmethodexecution time, andhinderedHBDapplicationintheCIenvironment.FortheHBDapproachto 625be applicableinaCIcontext,bothe ectivenessandperformancearecritical.Thus, apart fromassessingthee ectivenessintermsofAPFD,westudiedtheperformanceof HDB techniquesintermsofmethodexecutiontime. 2Both pairwiseandmultiset algorithmshaveO (n) complexity andtheirperformance is directlyproportionaltothesquareofthesizeoftheinputdata.Usingapairwise 630algorithm, thedistancesamongthetestscanbecalculateduponrequest,retained,and updated onlyifoneoftherelevant testsappearsinthechange list.However,duetothe nature of the NCD Multiset algorithm, a caching system such as this is ine ective. Inthis study,weparallelizedbothalgorithmsusingconcurrentutilitiesproposedbyJSR166. Among theinvestigated HBDtechniques,wefoundthatpairwiseManhattanandNCD 635achievedverycloseoverallscoresintermsofaverageAPFDacrossallprojects(77.17 and 76.99,respectively).HBDusingNCDMultisetissuperiorintermsofe ectiveness (81.25) butcomeswithrelativelyhigheroverhead intermsofmethodexecutiontime. Futurestudiesarerequiredtoinvestigate possibleapproachestoimprovingtheper- formance of distance calculation for the large number of test cases. Similaritymetrics like 640NCD have a wide range of application areas and are frequently used outside software en- gineering literature (see the many references in GoogleScholar to [39, 40]). Toeciently apply themtosoftwareengineeringproblems,theexistingbodyofknowledgemustbe explored systematicallyandpotentialapproachesneedtobeadapted.Thee ectiveness and performanceof boththe NCD pairwise and the NCD Multiset algorithms are partly

# ACCEPTED MANUSCRIPT

645linked to the chosen compression library. Inthis study, we used LZ4, a high-speed lossless 22


---

<!-- Página 24 -->

### ACCEPTED MANUSCRIPT

data compressionalgorithm.Futureresearchshouldalsoinvestigatedi erentcompres- sion algorithmsandbenchmarktheire ectivenessandperformanceforthepurposeof TCP.

5.2. ThreatstoValidity

650In thecontextofempiricalsoftwareengineering,validitythreatsareclassi edinto four distinctcategories,includingconstructvalidity, internalexternal and reliability[48]. Threats toconstructvalidityhavetodowithwhetherwearemeasuringwhatwe intend tomeasureandcorrespondtotheuseofpropermeasures.Toassessthee ec- 655tiveness ofTCPtechniques,severalmetricshavebeenproposedintheliterature(see the latestsystematicliteraturereviewonTCPbyKhatibsyarbinietal.[26]).These metrics weredevelopedtoaddressvariousTCPobjectives.Toassessthee ectiveness of TCPtechniques,weusedAPFD;originallyintroducedbyRothermeletal.[11],this is themostfrequentlyusedmetricinTCPliterature[26].Apartfrome ectiveness, 660we alsomeasuredaveragemethodexecutiontimeinordertoassesstheperformanceof investigatedtechniques. Threats tointernalvalidity have todowiththerelationshipbetweenconstructsand proposed explanations.Theycorrespondtothepotentialfaultsinourimplementation, e.g., datacollection,distancecalculation,prioritizationalgorithm,andthemeasures 665used, suchasAPFD.Tominimizethelikelihoodoferrorsinourimplementation,we took severalcountermeasuresintoconsideration.Duringtheimplementationphase,we followedaniterative,incrementalapproach,usingsmallexamples.Forinstance,toval- idate thedatagatheredfrombuildlogs,werandomlyselectedseverallogsfrom each projectand manually veri ed the extracted data. Furthermore,our implementation 670and resultswere discussedandreviewed inregularmeetings,which were heldamongthe co-authors ofthisstudy.Inourimplementation,wealsostrovetoreusereliablecom- ponents asmuchaspossible,i.e.,librariestocalculatesimilaritymetrics.TheHBTP algorithm and the pairwisewere adopted and implemented based on the exist- ing studies [18, 20]. Theonly algorithm that we designed from scratch was NCD Multiset 675for TCP, whichhasbeenexplainedindetailinthispaperandissimpletoimplement. Overall, ourimplementationwentthroughseveraliterationsandvalidationsbeforethe actual experimentwasconducted.ThestatisticalanalysiswasdoneinR,usingreliable packages. Threats toexternalvalidityhavetodowiththegeneralizabilityoftheresultsand 680correspond towhetherthesubjectsofourstudyarerepresentativeofrealprograms. In ourstudy, weinvestigatedsixdi erentopen-sourcesoftwareprojects,eachofwhich included severalbuildsoveralargeperiodoftime(seeTable1).Thus,thesubjects of ourexperimentarereal-worldprojectsandincludeCIbuilds,testsuites, and regressionfaults.Testsuitesizeforacoupleoftheinvestigatedprojectsseemed 685rather small,butweremorecomparabletoenterprise-sizedapplicationsinthecasesof the GUV,MYB,andTAJprojects.Testsuitesizewasextractedfrombuildlogsand indicated the number of test les executed during the builds (each of which might include several test cases). Weshould also emphasize that we had access only to the speci c build time periodprovidedbyTravisTorrent, andourdatadoesnothavefullcoverageofall 690revisions. Overall,ourndingsarevalidwithintheinvestigatedprojects;itisdicult

# ACCEPTED MANUSCRIPT

23


---

<!-- Página 25 -->

### ACCEPTED MANUSCRIPT

to generalizeourresultsbeyondthescopeofthestudy. Thismotivates ourfuturework to applytheinvestigated techniquesinindustryandtolargersystems. Apart fromtheAPFDmetric,wealsomeasuredaveragemethodexecutiontimeto assess theperformanceofinvestigatedtechniques.Themethodexecutiontimeinour 695study didnotincludetestsuiteexecutiontime.Toperformacomprehensive assessment of theeciencyofTCPtechniques,end-to-endtime,i.e.,TCPexecutionmustbe considered inadditiontotestsuiteexecutiontime.Testtimecanbe extracted automaticallyby analyzingbuildlogs.However,such informationhasnorele- vance,asthetestsuiteisexecutedinadi erent environment. Tohave afairassessment 700of TCP techniques, bothTCP method and test suite execution time need to be measured under thesameenvironment. Thisisonlypossiblebydownloadingallstudiedrevisions from Github,buildingthesourcecode,andrunningthetestsuite.Suchaprocedure involvesmanuale ortandautomatingtheentireprocedurewasnotfeasiblewithinthe scope andconstraintsofthisstudy. 705Threats toreliabilityhavetodowiththerepeatabilityoftheresearchandcorre- spond tothepossibilityofreachingthesameconclusionreachedbytheoriginalstudy. Repeatability requiredaccesstothedatathatwasusedandathoroughreportofthe research processthatwas applied.Thedatausedinourstudywas extractedfromTrav- isTorrentandGithub,andarepubliclyavailable.Ourexperimentwasdesignedbased 710largely onexistingresearch[20,18,42].Nevertheless,thestudydesign,alongwiththe careful explanationofourimplementation,werereportedinthispaper.

6. ConcludingRemarks

Agile softwaredevelopmenthasbecomeasourceofcompetitiveadvantageinthe industry.Thisdevelopment paradigmcalls formore frequent andcontinuous integration 715of changes; asaconsequence,thedemandforoptimizedregressiontestinghasincreased. The mainobjectiveofthisresearch was toshortentheRT feedback cycleforcontinuous integration ofsoftwaresystems.Inotherwords,ouraimwastocatchregressionfaults earlier, allowingdeveloperstointegrateandverifytheirchangesmorefrequentlyand continuously.Toachievethatend,weinvestigatedsixopen-sourcesoftwareprojects, 720each ofwhichincludedseveralbuildsover alargeperiodoftime. In summary,theresultsfromourexperimentssuggestthefollowing:(1)Historical failure knowledgeseemstohavestrongpredictivepowerinCIenvironmentsandcan be usedtoe ectivelyprioritizetestcasesforexecution;(2)HBTPdoesnotnecessarily require a large amount of historical data, and its e ectiveness improves to a certain degree 725with alargerhistoryinterval;(3)Diversity-basedTCPcanbeusede ectivelyduring the earlystagesofsoftwaredevelopment,whenhistoricaldataarenotyetavailableor are scarce,andalsocombinedwithHBTPtoimproveitse ectiveness;(4)Amongthe investigatedTCPtechniques, we foundthathistory-baseddiversity usingNCDMultiset is superiorintermsofe ectivenessbutcomeswithrelativelyhigheroverheadin 730of methodexecutiontime. Takentogether,theseobservationsimplythatHBTPcanbeemployedinpractice with negligibleinvestment anditse ectivenesscanbefurtherimprovedbyconsidering distances (dissimilarities)amongthetests.Ourstudycontributestotheliteratureby providing empiricalevidenceinsupportoftwopreviouslyproposedheuristicsnamely

# ACCEPTED MANUSCRIPT

24


---

<!-- Página 26 -->

### ACCEPTED MANUSCRIPT

735history-based anddiversity-basedTCPinCIenvironments.Inthefuture,weplanto replicate ourstudyinindustryandtolargersystems.

References

References

[1] 740vonen, and [2] testing: (2015) 745[3] ing [4] Software [5] 750ceedings pp. [6] continuous Software 755[7] Transactions [8] on International 760[9] e ectiveness: 79{89. [10] based 765[11] IEEE [12] (2016) [13] 770source engineering, [14] integration Symposium 775[15] trial IEEE, [16] Automated 780Engineering [17] enterprise 122{135. [18] 785environments, [19] prioritization International

# ACCEPTED MANUSCRIPT

25


---

<!-- Página 27 -->

### ACCEPTED MANUSCRIPT

[20] 790Automated [21] ings Computer [22] 795Testing, [23] software [24] in: 8001999, [25] Information [26] regression 805[27] on [28] to Improvement, 810[29] environments Technology, [30] incorporating 815[31] tering [32] tisation on 820[33] selection (2011) [34] diversity, 82563{78. [35] similarity-based IEEE [36] 830sity, [37] Testing, 2013, [38] 835models, [39] tion [40] 51 840[41] transactions [42] cases, on, 845[43] prioritization,

# ACCEPTED MANUSCRIPT

on, 26


---

<!-- Página 28 -->

### ACCEPTED MANUSCRIPT

[44] test 850Symposium [45] objective on [46] 855research software [47] in IEEE, 860[48] Engineering:

Appendix A.E ectivenesscomparison-violinplots

Figure

# ACCEPTED MANUSCRIPT

27


---

<!-- Página 29 -->

# ACCEPTED MANUSCRIPT

FigureGoogle

### ACCEPTED MANUSCRIPT

28

di erent


---

<!-- Página 30 -->

### ACCEPTED MANUSCRIPT

FigureA.5:di erent

# ACCEPTED MANUSCRIPT

29


---

<!-- Página 31 -->

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

Figuredi erent

30


---

<!-- Página 32 -->

# ACCEPTED MANUSCRIPT

FigureApache

### ACCEPTED MANUSCRIPT

31

di erent


---

<!-- Página 33 -->

# ACCEPTED MANUSCRIPT

FigureApache

### ACCEPTED MANUSCRIPT

32

di erent


---

<!-- Página 34 -->

### ACCEPTED MANUSCRIPT

Biography Alireza Haghighatkhahis aPhDcandidateatM3SResearchUnitintheFaculty 865of InformationTechnology andElectricalEngineering(ITEE)attheUniversity ofOulu, Finland. HereceivedB.Sc.inAppliedComputingfromSouthernCrossUniversity; Australia in2010andM.Sc.inInformationProcessingSciencefromUniversity ofOulu, Finland in2014.Hehasve years ofindustrialexperienceinJ2EEplatform,designand developmentoflarge-scaleenterprisesolutions.Hisresearchinterestsincludeempirical 870softwareengineering,qualityandprocessimprovement, releaseas well asevidence-basedsoftware engineering. MikaMntylis professorofSoftwareEngineeringattheUniversityofOulu,Fin- land. HereceivedaD.Sc.degreein2009insoftwareengineeringfromtheHelsinki UniversityofTechnology, Finland.Hisresearchinterestsincludeempiricalsoftware en- 875gineering, softwaretesting,miningrepositories,andbehavioralengi- neering. Hehaspreviouslyworkedasapost-docattheLundUniversity, Swedenand as anassistantprofessorattheAaltoUniversity,Finland.Hispreviousstudieshave appeared in journals such as IEEE Transaction on Software Engineering, Empirical Soft- ware Engineering,andInformationandSoftwareTechnology. Formoreinformation, 880visit: [http://mikamantyla.eu/](http://mikamantyla.eu/). Markku Oivois fullprofessorofsoftwareengineeringattheUniversityofOulu (Finland) since2002.HeisheadoftheM3Sresearch unit.Hehas30+years ofresearch, R&D andmanagementexperienceinacademyandindustryinFinland,US,France, Germany,ItalyandSpain.During20002002hewas VicePresident anddirectorofR&D 885at SolidInformationTechnologies. HehasheldseveralpositionsatVTTin19862000 including ProfessorandHeadofEmbeddedSWR&D.Hehasheldvisitingpositions at theUniversityofMaryland(199091),SchlumbergerLtd.(Paris199495),Fraunhofer IESE (19992000), University of Bolzano (201415), and Universidad Politcnica de Madrid (2015). Hehasworked atKoneCo.(198286)andattheUniversity ofOulu(198182). 890Pasi Kuvajais viceheadofM3SResearch UnitintheFaculty ofInformationTech- nology andElectricalEngineering(ITEE)attheUniversityofOulu,Finland.Hisre- search interestsareinSoftwareEngineeringincluding:continuousdeploymentandde- livery,DevOps,agileandleansoftware development,quality,process, softwareprocessassessmentandimprovement,embeddedsystems,andmea- 895surement. HeisoneofthedevelopersoftheBOOTSTRAPmethodologyandproduct quality- driven software processimprovement approach PROFES.Hehasbeenactively contributing theSPICEprojectandwasco-editorofISO/IEC15504Part7Process ImprovementGuide.Hehasworkedthreedecadesincloseresearchco-operationwith European industry. Hehasover 100publicationsandhasauthoredseveralbooks.

# ACCEPTED MANUSCRIPT

33


---

