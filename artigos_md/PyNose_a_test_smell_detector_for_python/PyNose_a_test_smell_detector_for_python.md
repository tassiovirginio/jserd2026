<!-- Página 1 -->

## P Y NOSE: A

## Test

## Smell

## Detector

## For

## Python

TongjieWang*YaroslavGolubev*Oleg Smirnov University ofCalifornia,IrvineJetBrains Research Irvine, CA,UnitedStatesSaint Petersburg,RussiaPetersburg StateUniversity [tongjiew@uci.edu](mailto:tongjiew@uci.edu)[yaroslav.golubev@jetbrains.com](mailto:yaroslav.golubev@jetbrains.com)Saint Petersburg,Russia [oleg.smirnov@jetbrains.com](mailto:oleg.smirnov@jetbrains.com)

Jiawei LiTimofeyBryksinIftekhar Ahmed University ofCalifornia,IrvineJetBrains Researchof Irvine, CA,UnitedStatesSaint Petersburg StateUniversityCA, [jiawl28@uci.edu](mailto:jiawl28@uci.edu)Saint Petersburg,Russia[iftekha@uci.edu](mailto:iftekha@uci.edu) [timofey.bryksin@jetbrains.com](mailto:timofey.bryksin@jetbrains.com)

**AbstractSimilarly to production code, code smells also occur**Similarly totestcodecanalsohavecode **in test**code,where theyare called**test smells. Test**have asmells, inwhichcasethey aretest. Van Deursen **detrimental effect not only on test code but also on the production**et al.[9]denedtestsmellsasbeingcausedbypoordesign **code that is being tested. To date, the majority of the research on** choices (similarly to regular code smells) when developing test**test smells has been focusing on programming languages such as** 1cases.Just like the code smells, test smells make the impacted**Java and Scala. However, there are no available automated tools** **to support**theidenticationoftestsmellsforPython,despitetest codehardertomaintainandcomprehend[10].Moreover, **its rapid**growth inpopularityinrecentyears.Inthispaper, westudieshaveshownthattestsmellsalsoimpactthe **strive to extend the research to Python, build a tool for detecting**quality ofproductioncode[11]. **test smells**inthislanguage,andconductanempiricalanalysis Since testsmellshaveanegativeimpactonthequalityof**of test**smellsinPythonprojects. production code, it is of great interest and importance to study**We**startedbygatheringalistoftestsmellsfromexistingre- and detectthem.To date,themajorityoftheresearchontest**search and selecting test smells that can be considered language-** **agnostic or**havesimilarfunctionalityinPython'sstandardsmells hasbeenfocusingonstaticallytypedlanguageslike **Unittest****framework. In**total,weidentied17diverse testsmells.Java andScala[10],[11],[12],[13],[14],[15].However, in **Additionally, we**searchedforPython-specictestsmellsby recent years,Pythonhasbeengrowinginpopularitydueto**mining frequent code**changepatternsthatcanbeconsidered as being the primary language used in Data Science and Machine**either xing**orintroducingtestsmells.Basedonthesechanges, Learning inparticular[16],[17].Furthermore,despitethe**we proposed**ourowntestsmellcalled**Suboptimal Assert . To** **detect all**thesetestsmells,wedevelopedatoolcalled**Y N**OSEempirical evidenceagainsttestdeveloperstendnotto **in the**formofaplugintoPyCharm,apopularPythonIDE.be awareofthesmellsthatexistintheirtests[13],andthe **Finally, we conducted a large-scale empirical investigation aimed** lack ofefcienttoolscanbeoneofthereasonsforit.To**at analyzing**theprevalenceoftestsmellsinPythoncode.Our the bestofourknowledge,therearenoworksthatstudythe**results show that 98% of the projects and 84% of the test suites in** existence andprevalenceoftestsmellsinPythoncode,and**the studied**datasetcontainatleastonetestsmell.Ourproposed **Suboptimal Assert****smell was detected in as much as 70.6% of the**no tools exist that specically aim at identifying test smells in **projects, making**itavaluableadditiontothelist.this language. **Index Terms****Test**smells,codePython,empirical In thispaper,weaimtollthesegapsbycuratingalist**studies, code**changepatterns,miningsoftwarerepositories arXiv:2108.04639v1 [cs.SE] 10 Aug 2021of possibletestsmellsforPython,atoolfortheirdetection, and anempiricalstudyoftheirpervasiveness inPythoncode.I. INTRODUCTION Westartedbyconductingasmall-scalemappingstudytondCode smellswere introducedtoidentifypotentialmain- different testsmellsstudiedintheliteratureandselectingtainability issuesinsoftwaresystems[1],however, laterthey test smellsthatcanbeconsideredlanguage-agnosticorhavehave beenusedasameasureofdesignqualityofsoftware analogous functionalityinPython'sstandardUnittestframe-projects [2],[3],[4].Researchersfoundthatcodesmellsare work. Intotal,weidentied17diversetestsmells.Theseassociated withbugs[3],[5],fault-proneness[6],[7],and test smellswerealladoptedfromotherpapersdedicatedtomaintainability issues in the code base [1]. While investigating different programminglanguages,butitisnaturaltoassumethe underlying reasons for introducing code smells, researchers that Pythonhasitsownspecictestsmells.Todiscoverattributed variousfactorstothis,includingdevelopersstrug- them, weusedatoolcalledYTHONPC HANGEMINER[18] togling withdeadlines[8]ornotcaringabouttheimpactofthe 1applied designchoices[1].To languages *teststestand.The


---

<!-- Página 2 -->

search for frequent change patterns in test suites. We manuallyand productioncode.Spadinietal.[11]investigatedthe evaluated 159patternsthatoccurinatleastthreedifferentrelationship betweenthepresenceoftestsmellsandthe projects andidentied32possiblechangesthatarerelatedtoanddefect-pronenessoftestcode,aswellasthe assertfunctions inUnittestand areaimedatmakingthetestsdefect-proneness ofthetestedproductioncode.Theyfound more specicandsimplifytheunderstandingofthetestingthat sometestsmellsaremorechange-pronethanothers,and logic. We bundled the less specic versions of these assertionsthey alsofoundthatproductioncodetestedbysmellytestsis together intoasingleSuboptimal Asserttest smell.Thus,acomparatively more defect-prone. Tufano et al. [13] found that total of18smellswereidentiedforPython.testare usually introduced when the corresponding test code is committed to the repository for the rst time, and theyWedevelopedPY N OSE, apluginforPyCharm[19]thatis ´tend to remain in a system for a long time.nioVirget al. [26]able todetectthesesmellsinthePythoncode.Usingthetool, investigatedcorrelations between test coverage and test smells,we performedanempiricalstudyontheprevalenceoftest and foundthattestsmellsinuencecodecoverage.in248Pythonprojects.Ourresultsindicatethattest smells areindeedcommoninPythontestcode,with98%of Investigatingways for an automated detection of test projects and84%oftestsuiteshavingatleastonetestsmell.has alsoreceived attentionfromtheresearchcommunity. Van Rompaey et al. [27] proposed a set of metrics dened in termsOverall, ourcontributionsareasfollows: of unittestconceptsandcomparedtheproposeddetectionWeconducted a small-scale mapping study and compiled techniques effectiveness with human review. Greiler et al. [14]a listoftestsmellsthatareapplicabletoPython. analyzed therelationshipbetweenthedevelopmentofatestWeidentiedanewPython-specictestsmellbyana- xture andpossibletestsmellswithinit.Theyalsodesignedlyzing Pythontestcodechanges. a staticanalysistooltoidentifyxture-relatedtestsmellsandWedevelopedatoolcalledPN OSEas apluginfor evaluated thembydiscoveringtestinthreeindustrialPyCharm that can detect test smells from Python projects projects. Palombaetal.[28]developed anautomatedtextual-that usethestandardUnittestframework. PY N OSEis fordetectingseveraltypesoftestsmells.available forresearchersandpractitionersonGitHub:based approach Compared withthecode metrics-based techniquesproposed[https://github.com/JetBrains-Research/PyNose](https://github.com/JetBrains-Research/PyNose). by Greileretal.andVanRompaeyetal.,thetextual-basedWereport the ndings pertaining to the pervasiveness of technique proved tobemoreeffective indetectingcertaintesttest smellsfromanempiricalstudyconductedon248 smells. Peruma et al. [25], [29] recently developed a tool calledPython projects. D ETECTcapable ofdetecting19testsmellsinJava.The restofthepaperisorganized asfollows. InSection TSII, havebeeninvestigating waystowe discusstheexistingworksintheeldoftestsmells More recently, researchers help testers refactor test smells. Lambiase et al. [30] presenteddetection andanalysis.SectionIIIdescribesthechoiceof an IntelliJ-basedpluginthatenablesanautomatedidentica-test smellsforPythonandthesearchforPython-specic tion andrefactoringoftestsmellsusingIntelliJPlatform'stest smells.InSectionIV,wedescribethedevelopmentof APIs. Santanaetal.[31]proposedanothertoolthatcanbeP Y NOSEand itsevaluation,andinSectionV,wedescribe used inanIDE,providingtesterswithanenvironmentforthe empiricalstudythatweconductedusingthetool,aswell automated detectionoflinesofcodeaffectedbytestsmells,as itsresults.InSectionVI,wediscussthreatstothevalidity as wellasasemi-automatedrefactoringforJavaprojects.of ourstudy,and,nally,inSectionVII,weconcludeour ´Virgnio etal.[32]presentedatooldesignedtoanalyzetestpaper anddiscusspossiblefuturework. suite qualityintermsoftestsmells.Theirtoolistherst II. RELATEDW ORKone thatreliesonbothcodecoverage andthepresenceoftest Similarly toproductioncode,testcodeshouldbedesignedsmells tomeasurethequalityoftests. following properestablishedprogrammingpractices[20].VanOverall, themajorityofthementionedresearchhasbeen Deursen etal.[9]denedthetermtest smellsas codefocusing onJava.However, inrecentyears,Pythonhasbeen that arecausedbypoordesignchoiceswhendevelopingtestgrowing morepopularbecauseofitsimportantroleinData cases and also dened a catalog of 11 test smells. Later, severalScience andMachineLearninginparticular[16],[17].To the researchers extendedthiscatalog[14],[21],[22],[23].Whilebest ofourknowledge,notoolsexistthatspecicallyaimat the majorityoftheresearchfocusedontestsmellsoccurringidentifying Pythontestsmells.P N OSEaddresses thisgap. in Java,severalresearchersinvestigatedotherlanguagesandFurthermore, thereisnolarge-scaleanalysisregardingthe domains. For example, Bleseretal.investigated testsmellsinoftestinPythoncode,andourstudyis Scala [15],[24],whilePerumaetal.[25]exploredunitteststhe rsttowardsllingthisgapinresearch. in mobileapplicationsandidentiedseveralnewtestsmells. III. SELECTINGT ESTS MELLSResearchers havealsobeeninvestigatingthenegativeim- The goalofourstudyistobuildatoolthatcanidentifypacts oftestsmellsonsoftwaredevelopment[10],[11], [12], [13],[26].Byconductingtwoempiricalstudies,Bavotatest smellsinPythoncodeaswellastoassesstowhat extent testareprevalentinPythontestsuites.Theet al.[10],[12]showedthattestsmellsarewidelyspread pipelineofourstudyisdemonstratedinFigure1.Inthroughout softwaresystems,andmosttestsmellshavea Section III,wecuratethelistofappropriatetestsmellsbystrong negative impactonthecomprehensibilityoftestsuites


---

<!-- Página 3 -->

##  'H£

Fig.

conducting asystematicmappingstudy(SectionIII-A)andTABLE I NCLUSION.then augmentingthelistbyidentifyingPython-specictest smells (SectionIII-B).

A. Systematicmappingstudyoftestsmells

As arststep,weconductedasmall-scalesystematicmap- ping study on test smells to curate a list of testdiscussed in the literature. According to Kitchenham et al. [33], the goal of themappingstudyistosurveytheavailableknowledge about atopic. SearchQuestion.Our searchquestionwasphrasedasfol- lows: What test smells have been studied in literature to date? SearchKeywords.Todeterminetheoptimalsetofsearch keywords, weconductedapilotsearchontwowell-known digital libraries,IEEEandACM.Thisprocesswasintendedselected studyunderwentanagreementprocess,andincase **Inclusion**Criteriato identifyrelevantwordsutilizedintestsmellpublications.of uncertaintyanddisagreement,wediscussedituntilwe Weconductedourqueryonlyonthetitleandabstractofthereachedconsensus.Wemethodologies,endedupwithwithasetof1.Publicationsthat implementsoftwareengineering approaches,and practicesin test smell detectionand refactoring.publication to avoid false positives. The nalized search string29 studies. Next, wemerged the lists of testsmells mentioned 2.Availablein digitalformat.is presentedbelow.in thesepapers,whichresultedinalistof33differenttest **Exclusion**Criteriasmells encounteredinJava,Scala,andAndroidsystems.The **Title : (test**smellORtestsmells)AND**Abstract:** full listofpapersandtestsmellsisavailableonlineinthe1.Publicationsthat are not writtenin English.(test smellORtestsmells). 2.Websites,leaets,andgrey literature.supplementarymaterials[36]. 3.Publishedin 2021.Data Source.Todiscoverrelevantpublications,weusedNext, weconsideredthepossibilityofimplementingeach 4.Full-textnot availableonline.three ofthemostpopularonlinepapersearchengines:ACMtest smellforPython.Therewereseveralreasonswhysome 5.Toolsnot associatedwith peer-reviewedpapers. Digital Library, IEEEXplore,andScopus.of thetestsmellscouldnotbeimplemented:6.Duplicatedpublications. SearchPeriod.Toobtain as many related works as possible,The test smell is not applicable to Python.For example, the

#  ®¯

# Huj U U U

# Huj U Ù

we queriedallrelatedstudiesbefore2020.Thisresultedin ResourceaOptimism[9] testsmellinJavaoccursif Filea list ofpapersthatwerepublishedbetween2006to2020.object isusedwithoutcheckingforitsexistence.However, Initial Results. Our initial search of the three digital librariesin Python,lesalwaysassociatewithresources,because, resulted in 54 publications. To narrow down the search results,according tothePythonofcialdocumentation,open()is

##  

## ¯u

## 9Ï

##  ñHu·£¯

## £

next,weltered ñ_H£outpublicationsthatwerenotpartofourthe standardwaytoopenlesforreadingandwritingwith

##  Uh_

## hj¯ £

## Ö uu£S ñ¯

## uu_9

inclusion criteria.AsummaryoftheandexclusionPython [37]. criteriaused£9to lterthe retrievedliteratureis shownin Table I.The test smell detection relies on the production code that is

## £h__

## uh¯

## B_H¯

## 

##  ñ¯·

##  ñj

The ltering process helped us to reduce the number of studiesbeing tested.For example, to identifyEager Test [9] andLazy

## ¯

## ¯

## Hj: ñ__£_

## ¯

## £

## ¯£h__

signicantly,however,thismayhaveresultedinleavingoutTest [9], weneedtoknowwhatthecorrespondingproduction

## £_

## ¯ ñ

## uH ñ¯

## uj£

some relevantstudies.Thus,weconductedbackwardsnow-les andproductionclassesare.Alotofrecentworksstudy balling [34] (looking for additional studies in the referencetest-to-code traceability[38],[39],[40]andalotofdifferent lists of the selected studies, as suggested by Keele et al. [35]).approaches havebeensuggested.However,reliablymaking In ourwork,weimplementedasingleiterationofbackwarda strictone-to-oneconnectionbetweenatestmethodand snowballing.a productionmethodinthestaticanalysisenvironmentis Toensurethereliabilityoftheselectedstudies,eachdifcult [39],whichiswhyleavethesupportofsuchtest

## u

## Ï

##  £

## Ö

## ¯

## Bujh

## £H¯

## £

## ¯£h__

## £

smells forfuturework.study wasevaluatedbythreeauthorsofthispaper.Each

##  Ù

##  ñ_H ñ¯

##  £

## Ö uu£

## Öh ñj· ñ__

## 

## Ö£

## ¯·ÖHj:u·_ ñB ñj:£Hj

## 

## Ï

##  ñ_· ñ¯

## Hj:¯

## ¯

## ¯

## £

## ¯£h__

## h ñ¯·

##  £

## Ö

## ¯

## Buj

## uX¯£

## u

## £

## Ö

## £

##  ®

## ¯·Ö¯

## £h__

##  ®

## ¯·Ö¯

## £h__

# Huj Ù

## B

## 

## Ï

##  ñ_

## j

## u

## 9¯

## £

## ¯

## £Hj £

## Ö

## ¯

## Buj

## u

## B

## u

## h

## u

## ·

## j

## u

## 9¯

## £

## ¯

## £Hj £

## Ö

## ¯

## Buj

## u


---

<!-- Página 4 -->

The testsmelldetectionispossibleonlywhenthetestisresponsibilitiesofaclassaretiedtogether. Iftestcasesin executed.For example, for theTestRun War[9], it is necessarya suitearenotcohesive, thiscancausecomprehensibilityand to actuallyrunthetestcase,whichisnotpossibleinastaticmaintainability issues[14]. analysis environment. Even after running, identifying such test**Magic Number Test**occurs when assert statements in a test smells isnon-trivial,andforpracticalpurposeswehadtocase containnumericliterals i.e.(, magicnumbers)asparam- exclude them.eters insteadofmoredescriptiveconstantsorvariables[25]. Finally,weselected17testsmellsforimplementing.We**Obscure In-Line**Setupoccurs whenthetestcasecontains list thembelow.too manysetupsteps.Thiscanhinderinferringtheactual **Assertion Roulette**occurs whenatestcasehasmulti-purpose oftheassertioninthetest.Ideally,suchpreparation ple non-documentedassertions.Multipleassertionstatementsshould bemovedtoaxtureoraseparatemethod[14]. without adescriptivemessageimpactthereadability,under-**Redundant Assertion**occurs whenatestcasecontains standability,andmaintainability,asitbecomesmoredifcultassertion statements that are either always true orfalse, to understandthereasonwhythistestfails[9].and arethereforeunnecessary[25]. **Conditional Test Logicruns against the rule that test cases****Redundant Print**occurs whenthereisaprintstatement need to be simple and execute all statements in the productionwithin the test. Print statements are considered to be redundant code. Conditionswithinthetestcasealterthebehaviorofthein unittestsasunitareusuallyexecutedasapartofan test andleadtosituationswherethetestfails todetectdefectsautomated processwithlittletonohumanintervention[25]. in theproductioncodeundersomeconditions[25].**Sleepy Test**occurs whendevelopersneedtopausethe **Constructor Initialization**is madebydevelopers whoareexecution ofstatementsinatestcaseforacertainduration unaware of the purpose of thesetUp()method that contains( i.e. , simulateanexternalevent)andthencontinuewiththe the preparationneededtoperformtestcases.Asaresult,theyexecution. Explicitlycausingathreadtosleepcanleadto would dene a constructor for the test suite, which is not idealunexpected resultsastheprocessingtimeforataskcanvary in practice[25].on differentdevices[25]. **Default Test occurs when an IDE creates default test suites****Test**Maverickwas derivedfromthe General Fixturede- when theprojectiscreatedanddeveloperskeepthedefaultscribed above.Ifthetestsuitehasaxturewithsetup,but name. For example, PyCharmbydefault namesthetestsuitesa testcaseinthissuitedoesnotusethissetup,thistestcase MyTestCase. These suites are meant to serve as an exampleis amaverick(outlier).Thesetupprocedurewillbeexecuted for developers when writing unit tests and should be renamed.before thetestcaseisexecuted,butitisnotneeded[14]. Not renamingthemupfrontcausesdeveloperstostartadding**Unknown Test**occurs whenthetestcasehasnoassertion test casesintotheseles,makingthedefaulttestsuiteain it.Itispossibletocreateatestcasethatdoesnotuse container of all test cases. Thiscan also cause problems whenassertions, however, suchatestismoredifcult tounderstand the suitesneedtoberenamedinthefuture[25].and interpret[25]. **Duplicate Assert**occurs when a test case tests for the same During thisselection,wealsodecidedtofocusspecically condition multipletimes[25]. on theUnittesttesting framework[41]thatisincludedinto **Empty Test**occurs whenatestcasedoesnotcontain the PythonStandardLibrary.alsohasalotofpopular executable statements.Suchtestsarepossiblycreatedfor third-party testing frameworks likePyTest[42] andRobot [43], debugging purposesandthenforgottenaboutorcontaincom- however,certain test smells would look differently in different mented outcode[25]. frameworks, anditisoutofthescopeofthispapertosupport **Exception Handling**occurs whenpassingorfailingofa them all.Therearetworeasonsforchoosingspecically test caseisdependentontheproductionmethodexplicitly Unittest. Firstly,itremainsoneofthemostpopulartesting throwing anexception.Instead,developers shouldutilizespe- frameworks inPythonwhilealsobeingthedefaultone[44]. cial functionalityoftestingframeworksforthat,suchasan Secondly,accordingtoitsdocumentation,Unittest wasorigi- assertRaises()function [25]. nally inspiredbyJUnit[41], whichallowsustodetectsome **General Fixture**occurs whenatestsuitextureistoo test smells from the literature that were originally proposed for general and some test cases only access a part of it. The xture JUnit, forexample,xture-relatedtestsmells.Additionally, of atestsuiteisaspecialmethodthatisexecutedbeforethe several otherframeworkssupportlaunchingtestsuitesfrom test casesinthesuiteandservesasasetupstep.Adrawback Unittest, andcanthereforealsobedetectedinthiscase. of itbeingtoogeneralisthatunnecessaryworkisdone when atestsuiteisrun[9]. B. IdentifyingPython-specictestsmells **Ignored Test**is causedbyignoredtestcaseswhenitis In additiontothetestsmellsidentiedabove,ourgoalpossible tosuppresssometestcasesfromrunning.Theseig- nored testcasesaddunnecessaryoverhead byincreasingcodewas toincludePython-specictestsmells.Todiscover complexity andmakingcomprehensionmoredifcult[25].Python-specic testsmells,weusedatoolcalledYTHONP- C HANGEMINER[18] to search for frequent change patterns in**Lack of**CohesionofTestCasesoccurs iftestcasesare the histories of test suites. We explain the steps of this processgrouped togetherinonetestsuitebutarenotcohesive. Cohe- in detailinthissection.sion of a class is a metric that indicates how well various parts


---

<!-- Página 5 -->

1) Projectselection: Tocarryoutthisresearch,weneededof PYTHONCHANGEMINERis similartothatofthetoolby to collect a dataset of mature open-source Python projects. AsNguyen etal.Here,webrieyexplaintheprocedure. a startingpoint,wetookGHTorrent [45],alarge collectionof P YTHONCHANGEMINERworks intwostages:building GitHub data,morespecically,theirlatestdumpatthetimechange graphsandminingpatterns.Intherststage,the of thecompilation,compiledinJuly2020[46].Toprocessversions ofcodebeforeandafterthechangeareparsedinto it, weusedatoolcalledPGA-create[47]thathadbeena specialrepresentationintroducedbyNguyenetal. previously used to create Public Git Archive (PGA) [48]. Thisne-grained Program Dependence Graphs(fgPDGs). fgPDGs tool processestheSQLdumptocreateaCSVlewithalistgraphswiththreetypesofnodes:datanodes (variables, of projectsthatfacilitatestheirconvenientltering.Next,weliterals, constants,etc.),operationnodes (arithmetic,bit-wise selected all projects with at least 50 stars, which allowed usoperations,toetc.),andcontrolnodes (controlsequenceslike lter outtoyprojects.We alsoonlyconsideredprojectswithif ,while,for , etc.).Thesenodesareconnectedusingtwo Python asthemainlanguagethatarenotforks.Thisresultedtypes ofedges:control edges representaconnectionbetween in identifying 26,072 projects. Of them, we randomly selecteda controlnode and a node that it controls anddata edges show 10,000. The reason for not simply picking top projects by starsthe ow of the data in the program, such edges also have labels is thattestingmightbeorganizedverydifferentlyinprojectsspecifying theowofdata. of differentscale,andsimplypickingthelargestorthemostThen, unchangednodesinthetwofgPDGsofcodebefore popular repositoriescouldskewourdatatowardsaspecicand afterthechangeareconnectedtogetherbyspecialmap type ofprojects.edges, resulting in new graphs calledchange. We used Next, weanalyzedthehistoryoftheprojectstondall[51] to detect corresponding unchanged nodes in the versions beforeandafterthechangeandconnectthemwithacommits whereatleastonePythontestlewaschanged.We map edge. This is carried out on a function level and therefore,dened aPythontestleasanylewith.pytheextension change graphthat represents eachthat hasthewordtestin itslename,sinceUnittesthasa this way, we obtain a special naming conventionofhavingthewordtestin thenameofchange toeachtestingfunctionfromthehistoryofprojectsin the testle[41].We have conductedasmallmanualanalysisour dataset. You can nd an example of fgPDGs and a change graph inthesupplementarymaterials[36].by selecting100randomPythonleswiththewordtest The secondstageofPYTHON CHANGE MINERinvolvesin theirnameandcheckingwhethertheyareactuallyrelated thesechangegraphsforpatterns.Thispartisalsoto tests.Inthisrandomsample,all100leswererelated searchingto done similarly to the work of Nguyen et al. [50]. First, all pairstesting, with 96 explicitly containing test suites and test cases, and another4containingauxiliarymethodsandtestingutils.of nodesrepresentingfunctioncallsthatarealsoconnected 4,580 oftheprojectshadatleastonecommitthatwith themap edge are considered to be the initial patterns that are thenrecursively expandedtocontainnewnodes.Thepat-such les.Aswewerelookingforcodechanges,weselected tern is dened by two thresholds:minimum size, indicating thethese 4,580projects.Sinceourgoalwastoanalyzethe changes themselves,forpracticalpurposes,wedecidedto minimum number of graph nodes in the pattern, and frequency, indicatingtheminimumnumberofrepetitionsofselect a smaller set of projects using the criteria recommended in literature[49].Weselectedprojectswithatleast1,000the pattern in the corpus. Changing these parameters inuences commits, 10contributors,2yearssincetherstcommitandwhat isconsideredtobeapatternand,therefore,howmany aredetected.Thisway, thepatternsareexpandingtono morethan1yearsincethelastpush.Thisresultedin450 isomorphicsubgraphswithinourcorpusofgraphs.projects. Forthepurposesofthispaper,wewillcallthisthe In ourwork,weusethesamethresholdsasNguyenetPrimarydataset; thelistisavailableonline[36]. al.:minimum sizeof 3andfrequencyof 3.Itis2) Changepatternmining:ToidentifyPython-specictest smells, westartedbyminingthehistoriesofthecollectedpossible thatstudyingspecicallythetestingcoderequires projects andndingpatternsinthechangesmadetotestlesdifferent thresholds,weleavesuchanalysisforfuturework. additionallyadda maximum sizethreshold of20.Thisisthat mightbeconsideredaseitherxingorintroducinga done tomaketheprocessfasterbystoppingthepatternsfromtest smell.We extractedallchangesmadetoPythontestles growing toolarge.Ourownpreliminaryexperimentsandourfrom the identied 450 projects and processed these les using P YTHONCHANGEMINER[18].analysis oftheresultsofNguyenetal.demonstratedthatthe P YTHONCHANGEMINERis atoolthatwedevelopedfor majority ofdiscoveredpatternsaresmall.Morespecically, Depthpattern corpusprovidedbyNguyenetal.[50]mining codechangepatternsinPythoncode.Thetoolis contains atotalof9,289patterns,ofwhich8,697(93.6%)based onthealgorithmdevelopedbyNguyenetal.[50]for patterns are20nodesorsmaller.SincesmallerareJava. Theparserintheirtooliswrittenspecicallyforthe much morefrequentandareeasiertoanalyze,wedecidedtosyntax oftheJavalanguage,andtheirtoolstoresgraphsand works withthemasJavaobjects,sowecouldnotdirectlyfocus on them. An example of a discovered pattern is presented reuse thetool.Atthesametime,thealgorithmitselfisnotFigure2. 3) Testsmells detection:In total, PYTHON CHANGE MINERlanguage-specic, because it relies only on the abstract syntax abletodiscover8,239differentpatternsinthetrees (AST)ofcodebeforeandafterthechange,whichis dataset. Ofthem,652patternswerecross-project, meaningwhy weimplementeditforPython.Theoperationprocess


---

<!-- Página 6 -->

#  V H O I 

#  V H O I 

ii.**Assertion changes**thatdonotalterthelogicanduse **more****appropriate functions.** (a)A largeportionofthepatternsinvolved keepingtheasser- tion logicthesame,butreplacingtheassertionfunctionwith a moreappropriateonetomakethecodesuccinct.Intotal, eight such patterns were identied. These changes are Python- (b) specic inthesensethattheyrelyheavily onawiderangeof assertion functionsthat Unittestsupports. The mostpopularpatternisshowninFigure2.Itoc- curs insevendifferentprojectsandmovesfromusing(c) assertTrue(X inY)toassertIn(X, Y). Onecom- Fig. mit messagedescribesthischangeingreatdetail:Use moreGitHub. specic assertionsfor`in'checks.Alotofoldcodeused they wereencounteredinatleasttwodifferentprojects,and`assertTrue(blahin blah)', or variants on that, which didn't tell 159 appeared in at least three different projects. Three authorsyou muchiftherewasafailure. Nowadays,wehaveassertIn of thepaperindependentlymanuallylabeledall159ofsuchand assertNotIn,whichwecanuseinstead.Thisswitchesour changes todiscoverthateitherxorintroducepossi-tests tousethese[54]. Thiscommitmessageindicatesthat ble test smells. The reason for focusing on these changes is thatthe originalcode(beforethechange)canbeconsideredatest they are inherently more universal among different developers.smell sinceusinggeneralassertionscanmakeitdifcultto Along with analyzing the code changes themselves, the authorsinfer thereasonoffailurebyhidingtheactualassertionin also lookedatthecorrespondingcommitmessages,sinceits body, whereasusingspecicassertionscanmakeiteasier. commit messagesmaycontaintherationaleforachange.Another changethatstrivestoremovetheambigu- After individuallabeling,theauthorsdiscussedtheirlabelsity ofageneralassertionoccursinfourrepositories, and reachedaperfectagreement.and itmovesfromusingassertFalse(X ==Y)to Of thestudied159patterns,70(44%)constitutedvariousassertNotEqual(X, Y). SometimesassertTrueis changes toassertionfunctionality,similartotheexamplechanged toanotherspecicassertion.Forexample,inthree shown inFigure2.Threeauthorsofthepaperindependentlydifferent projectsassertTrue(X <=Y)is changedto came toaconclusionthatthecandidatesforpossiblePython-Unittest'sassertLessEqual(X, Y). Onecommitmes- specic testsmellscanbefoundonlywithinthisgroup,sage expectedlycommentsthis:Use morespecicassertsin because othercommonchangesintestingcodecorrelatetounit tests[57]. various otheraspectsofsoftwareengineering:datastructures,In Python, it is considered bad practice to check the equality data processing,etc.,thatarenotdirectlyrelatedtotestingof abooleanvaluewhenyoucanchecktheitself, itself. For example, popular changes include changing the levelso inthiscaseabooleanassertionismorecorrectand of thelogger(error,info,debug,etc.)orchangingtheshapemore interpretable,whichisreectedinacommonchange of anumpyarray.Suchpatternsareimportant,butarenotpattern whereassertEqual(X, False)is changedto directly relatedtotestingortestsmells.assertFalse(X). Wecategorizedassert-relatedchangepatternsintothreeIn thissection,wehavegivenexamplesofsomecommit categories, whichwedescribebelowwithspecicexamples.messages thatdescribethechangesalongwiththechange i.**Assertion changes**thatalterthelogic.Often, whende-pattern. Webelievethatthesecommitmessagesjustifycon- velopers change an assertion in a test case, they do it to updatesidering thewrongchoiceofanfunctionUnittestin the logicbehindthetest.Forexample,apatternthatoccurredas atestsmell.We calledthissmellSuboptimal Assert. in sixdifferentprojectsischangingfromassertEqualiii.**Assertion changes**thatdonotalterthelogicanduse toassertRegex. Thisway,insteadofcheckingforan**less****appropriate functions.** exact equalitybetweenanobjectandastring,aregularInterestingly,wealsodiscovered seven changepatternsthat expression is passed that can support variations in strings. Onemove from an appropriate assertion function to a more general commit message reads:Use a more permissive comparison forone. Following thelogicoftheprevioussection,thesecanbe jsonschema.ValidationErrormessages[55].treated asintroducingatestsmell. Another commonpatterninvolvedchangingfromThe mostpopularsuchchangeismovingfroma assertEqualtoassertIn, whereinsteadofonemore specicassertIsNotNone(X)to amoregeneral correct result,thereisalistofvalues.Conversely,anotherassertNotEqual(X, None). Onecommitmessagede- common exampleischangingfromassertIsNonetoscribes thischangeasaintestforPython2.6compatibil- another functionassertIsInstance. Thismakestheity[58]. However,thechangesinthispatternweremadein check morespecic:theobjectisnotcomparedto20142015, andsincePython2isdeprecatedfrom2020,this but ratherneedstobeanobjectofanewspecicclass.Oneis nolongeraproblem. commit messageconveysasimilaridea:NullSort insteadofAdescribedcommitsintwodif- None. Amoredescriptiveplaceholderfordon'tsort[56].ferent projectsthatmovedfromassertNotIn(X, Y)

#  D V V H U W 7 U X H

#   
 * 5    

#   L Q

#   O O Y P B E F 

#   U H V X O W V 

#   D F F R X Q W  G D W D 

#  D V V H U W , Q

#   
 * 5    

#  

#   O O Y P B E F 

#  

#   U H V X O W V 

#  

#   D F F R X Q W  G D W D 


---

<!-- Página 7 -->

Fig.YPN OSEoperation

which allowsP Y NOSEto identifytestsmells.Forex-toassertTrue(X notinY)and twomoredif- ferent projectsthatmovedfromassertLess(X, Y)ample, fortheMagic NumberTest, weuseacustom visitor ofPyCallExpressionto ndallassertions,toassertTrue(X <Y) . Thesamechangescanbe and thencheckifoneoftheprovidedargumentsisafound forfunctionslikeassertGreater(X, Y)and PyNumericLiteralExpression. If there is a match, theassertIsNone(X), withonecommitmessagesaying:re- Magic NumberTestsmell isdeclaredtobefound.move fancytestassertionsthatareunavailableon[59]. For thetestsmellsfromtheliterature,weimplementedIn total, we encountered 12 different suboptimal asserts (ei- their detectioninthesamewayastheyaredescribedinthether xed, introduced, or both). We extrapolated them to simi- original papers,usingthementionedthresholds.Forlar functions and opposite cases where necessary: for example, we detectObscure In-LineSetupthe samewayasGreilerif thereisasuboptimalassertthatcontainsassertLess, et al.[14],bycountingthenumberoflocalvariablesinait canalsobeformulatedforassertGreater, etc.This test caseandaggingthecaseassmellyifthisnumberisresulted inatotalof32differentassertionsthatcanbe larger thanathresholdof10,anddetectLack ofCohesionconsidered apartoftheSuboptimal Asserttest smell,thefull of TestCasesthe samewayasPalombaetal.[28],bylist isavailableonline[36]. calculating pairwisecosinesimilaritiesbetweentestcases. IV. PY N OSEDetection rulesforallthesupportedtestsmellsarepresented in TableII,thecitationsmarktheworks,fromwherethe Once wecuratedthelistoftestsmells(explainedinSec- detection ruleswereadaptedfrom.Wherenecessary, weused tion III), our next goal was to implement a tool to identify them code entitiesanalogoustotheircounterpartsinJava,for in actualPythoncode.WedevelopedatoolcalledY NP example, @unittest.skip() decorator in the place of the that currentlyidenties18testsmells(17language-agnostic @Ignoreannotation. If there were several different heuristics from the existing literature and one Python-specic elicited by to detectthesamesmellindifferentpapers,weselectedone us asdescribedinSectionIII-B),andcanberunfromboth based onitsrecencyanditsconveniencetoimplementusing the graphicaluserinterfaceandthecommandline.Figure3 the PSIandtheIntelliJplatfrom. shows theoperatingpipelineofYPN OSE. Inthissection,we When theanalysisisdone, YPN OSEcan show thedetected explain itingreaterdetails. test smellsinsidetheIDEorsavethemtoaJSONlefor further analysis.A. Toolinternals B. EvaluationP Y NOSEis implementedasapluginforPyCharm[19],a popular IDEforPythondevelopedbyJetBrains.ThepluginWeconductedanexperimentalevaluationoftheeffective- supports twodifferentmodesofoperation:Graphical Userness ofP Y NOSEin correctlydetectingtestsmells.Asthere Interface (GUI)modeandCommand Line(CLI)are no existing datasets containing information for all the sup- mode. Internally,P Y NOSEuses ProgramStructureInterfaceported smells,wedecidedtoconstructourown validation set. (PSI) [60]fromJetBrains'IntelliJPlatform(thatPyCharmisWerandomlyselectedeightprojectsthatdidnotmakeitinto built upon)toparsePythonsourcecodeandbuildsyntacticthe Primary dataset. We then used the denitions of test smells and semanticcodemodelsforanalysis.Whentheprojectisto identify and tag test les with the information regarding the opened and the interpreter is set up, the tool uses PSI and othertypes ofsmellstheyexhibit.Thisprocessresultedinatotal related PyCharmAPItogatherall.pyles intheprojectinof 37annotatedles.Thelistofprojects,togetherwithsome the formof PSIFileobjects.statistics abouttheirtestingles,isshowninTableIII.To Next, thetoolextractsallPythonclassesthatare ensure anunbiasedannotationprocess,threeauthorsofthe

##  i ñ·jB £

## Ö  B ñh

sub-classes ofunittest.TestCase. Withthehelpofpaper individually didthelabellinganddiscussedtheirresults PSI, PY N OSEcan dealwithimportingunittestorafterwards toreachaconsensus.Allthethreeauthorshave

## Hj I Â Uhu

unittest.TestCaseunder aliasortestcasesthatare experience withPythondevelopment rangingfromtwo tove

##  j¯

## B

##  £

##  ñ

## £ ñ__R

## Ö_

not directsub-classesof unittest.TestCase. Aftercol-years, whichincludesexposuretodevelopingunittests. lecting individualtestsuites,eachdetectorclass(correspond-Next, we ran PNOSEon the same set of projects and com-

## j

## ££ ñ

## Ö

## uX¯

## Hj¯

## u £ ® U H

## H_

## uX¯£

pared ourresultsagainsttheoracle.We calculatedprecision,ing toeachtestsmell)invokesPsiElementVisitorto recall, andF1scoreforeachtestsmell.Wealsocalculatedcreate acustomvisitorforthenecessaryPsiElement,

##  i ñ·jB £

## Ö  B ñh

## Hj

## ¯

## B ñ[

## :

## u·j

#    i Uhu

## £

##  £

##  ñ

## £¯

##  ñB_

## £·H¯

## B £ ® U¯

## ¯

## uj ñ__¯

## £

##  ñj

## u

## 

##  ñ££

## 9

## £

## ¯

##  £

##  ñB

## j

## ££ ñ

##  ñ£¯

## Ö¯

## u¯

## £

## ¯£h__

## ¯

## £

#  I Â Uhu

##  iH£

## ¯¯

## ¯

## £h__

## £Hj £

##  ® ñ

## Ï

## ¯

## Bu·¯·¯

## Hj¯

## u ñ e ®  u_

## ¯

## Ö  B ñh

## £

## ¯

## 


---

<!-- Página 8 -->

TABLE T HE. C ITATIONS.

**Assertion**A **Conditional**Ai.e. , (, for, while). **Constructor**A__init__ method). **Default**AMyTestCase.[29] **Duplicate**A **Empty**A **Exception**Atry/exceptstatementraisestatement. **General**NotsetUp()method **Ignored**A@unittest.skipdecorator. **Lack**The0.4. **Magic**A **Obscure**A **Redundant**A same,e.g. ,assertEqual(X,ore.g. , assertTrue(True).[29] **Redundant**Aprint()function. **Sleepy**Atime.sleep()function **Suboptimal**A **Test**ASetUp()method. **Unknown**A

TABLE T HE. I NST. STANDSE IGHTP Y NOSE.THE INDICATESCOLUMNS, SUITES , AND THE.WITHUnittest.

**Test**SmellInst.PrecisionRecallF1**Project T.**FilesT.SuitesT.Cases

Assertion Roulette42100%97.6%98.8%ali1234/vhs-teletext 122356 Conditional Test Logic2080%100%88.9%cea/secivre 1113 Constructor Initialization1100%100%100%davidhalter/jedi 3417 Default Test 2100%100%100%demisto/content 910203 Duplicate Assertion6100%100%100%justiniso/polling 114 Empty Test 1100%100%100%Lagg/steamodd 61345 Exception Handling10100%100%100%plamere/spotipy 317114 General Fixture11100%100%100%pygridtools/drmaa-python 2416 Ignored Test 3100%100%100% **Total**37 73468 Lack ofCohesion1378.6%84.6%81.5% Magic NumberTest 23100%82.6%90.5% Obscure InlineSetup3100%100%100%the weightedaverage ofthesethreemetricsforalltestsmells Redundant Assertion2100%100%100%with theweightsbeingthenumberofinstancesofeachtest Redundant Print2100%100%100% smell intheprojects.TheresultsoftheconductedevaluationSleepy Test 1100%100%100% are presentedinTable IV.Suboptimal Assert10100%100%100% TestMaverick 5100%100%100%Several testsmellswereencounteredveryrarelyinthe Unknown Test 1083.3%100%90.1%validation projects,withthreeofthemhavingonlyasingle **Weighted**average**94.0% 95.8%**94.9%example. This has to do with the fact that these test smells are just rareinPythoningeneral(seeSectionV-C2).However, these testsmellshaveveryrobustdenitionsthatareeasyhaving theAssertion Roulettetest smell,however,PY N OSE to detect:Default Testrequires thetooltosimplycheckthefailed todoso.P N OSEalso incorrectlyidentiedseveral name ofthetestsuite,Constructor Initializationrequires theConditional TestLogictest smells.Test tool tosimplycheckthepresenceofanmethod,is detectedbythepresenceofcontrolstatementsi.e.(if , andSleepy Testsimply looksforthe sleep()function infor , etc.)irrespectiveoftheirimpactontheassertion.For the bodyofthetestcase.example, theforstatement canbeusedsimplytoassigna As showninTableIV,PN OSEachieves ahighlevelofvariable andsuchcasesareincorrectlytaggedas correctness withF1scoresrangingfrom81.5%to100%forTestLogicby PY N OSE.Lack ofCohesionrelies onthe different testsmells.Forthecaseswherethetooldidnotcohesiveness oftestinatestsuite.Y NPOSEmeasures achieve 100%,weinvestigated themismatch.cohesiveness usingcosinesimilarity,whereashumanraters In one instance,Assertion Roulettewas not detected becauseused their subjective judgement, which resulted in a mismatch of anon-conventional nameofthetestcase,wherethenamebetween theoutputofP N OSEand theopinionofthehuman started witha_symbol insteadofthewordtestas israters inseveralcases.SeveralMagic NumberTestswere* the convention.Ahumanratercouldtagsuchatestcaseas detectednotbecausethecomparisontoaliteraloccurredin


---

<!-- Página 9 -->

suites withatleastonetestcaseandtestleswithatassertions with complex parameters that are not yet supported. one testsuite.TestsmellscanoccuronvariouslevelsofFor example,assertEqual(df.shape, (1,))was Constructor Initialization,Default Test,Generaltagged asa Magic NumberTesttest smellbyahumanrater, granularity: Fixture, andLack ofCohesion manifest atthelevelofatesthowever,P Y NOSEfailed to do so, because the literal is located suite asawhole,whileothertestsmellssuchConditionalasin a tuple. Finally, two cases ofTestturned out to be TestLogicare formulatedatthetestcaselevel.false positives.Thetoolconsideredthetestcasetonothave analyzed the test smells using their appropriate granular-assertions, when in reality an assertion was present, but it wasWe ity.Atestsuiteisconsideredsmellyifitcontainsatleastonefrom theunsupportedpytestframework. test case with a given smell. A test le can also be consideredFor alltestsmellstogether,YPN OSEachieves theprecision a valid object for comparison, however, even though in Pythonof 94% and the recall of 95.8%. Table V shows the comparison and inUnittestit ispossibletohave several testsuitesinonebetween theobtainedvaluesandthereportednumbersof test le,thisgranularityisstilllargelysimilartoatestsuite,TS DETECT[29], atoolforJava.Itcanbeseenthat and often a test le contains just one or two test suites. We alsothe valuesaresimilar,however,weplantoconductamore calculated the distribution of test smells among projects to getthorough anddirectcomparisonoftoolsinthefuture. a morecoarse-grainedpictureofthetestsmellsprevalence. TABLEWestudiedthemostcommonandtheleasttest T HEP Y NOSED ETECT. smells, aswellastheprevalenceofthenewlyproposed Suboptimal Assert. Additionally, we studied the co-occurrence**Detector Language**PrecisionRecallF1 of differenttestsmellsinindividualtestsuitesanddiscussed **TS DETECT**[29] Java96.0%97.1%96.5% the correlationsbetweentestsmells.**P Y NOSE**Python 94.0%95.8%94.9% C. Results V.PREVALENCET ESTS MELLSIn this section, we discuss the results of the empirical study of thetestsmellsprevalence inPythoncode.After developing andvalidating PNOSE, weconductedan 1) Generalinformation:In total,atleastone Unittestempirical study on test smell prevalence in open-source Python test casewasfoundin248projectsoutofthe450intheprojects. Inthissection,wepresentthedetailsandtheresults Primarydataset (55.1%). From here on out, all percentages areof thisstudy. calculated basedonthese248projects.Intotal,in248 A. Selectingprojectstoanalyzeprojects, PYNOSEdetected 9,158testles,16,681testsuites, and 96,736testcases.MoredetailedstatisticsarepresentedThe goalofourstudywastoanalyzetestsmellprevalence in TableVI.Itcanbeseenfromthetablethatevenmaturein PythonprojectsusingY N OSE. Thiswasdonetoincrease projects vary greatlybytheamountoftestingwithinthem.Inthe subjectdiversityamongtheexistingempiricalstudieson our dataset,onetestleonaveragehad1.8testsuites,andtest smells,aswellastogainanunderstandingofhowtest one testsuiteonaveragehad5.8testcases.smells arediffusedinPythoncode.Wedecidedtostudythe presence oftestsmellsinthesamePrimarydataset thatwasTABLE .used forminingcodechangepatterns.Wedecidedtodoso T HE because thePrimarydataset representsmatureopen-source **Test**lesTestsuitesTestcasesPython projectsthatusetestingwithinthem. However,tomakesurethattheresultsofthestudyare**Minimum**1 11 robust anddonotdependontheresultsfromSectionIII-B3,**Mean**36.9 67.3390.1 we decidedtoalsorunthetoolonanadditionaldataset.**Maximum**323 8705,121 Togatherit,weusedthesameprocedureasdescribedin 2) Testsmellsdistribution:The distributionof18detectedSection III-B1,butwithoneconditionbeingslightlyrelaxed: test smellsispresentedinFigure4.Ingeneral,itcanbeseenwe gathered projects with the number of commits between 500 the studied test smells are prevalent in Python code. Thereand 1,000,insteadofatleast1,000commits.Thisresultedin are only5projects(2%)thathavenosmells,however, allof239 additional projects; the full list is available online [36]. We them areverysmallprojects,withthelargesthavingonly13will refertothisdatasetastheSecondarydataset. Whilewe test cases.Alltheotherprojects(98%)havetestssmellsindraw ourgeneralconclusionsfromthePrimarydataset, since wayoranother.TestsmellssuchAssertion Rouletteit containsmoreprojectswithlargerhistories,thepurposeof andConditional Test Logicare amongthemostcommontesttheSecondarydataset istomake surethatthereportedresults smells and occur in almost 90% of projects thatUnittestuseinare unbiased. thePrimarydataset. Alsoamongthemostpopulartestsmells B. MethodologyareMagic NumberTest,General Fixture, andUnknown Test. WeranP Y NOSEon alltheprojectsinthePrimaryandOn the other end of the spectrum, we can see test smells that inPythoncode.Empty Testoccurs injust0.7%Secondarydatasets separately.Wedroppedtheresultswhererarely occur not asingletestsuitewasfound,andonlyconsideredtestof thetestsuites,although,interestingly, even theseinstances


---

<!-- Página 10 -->

Fig.Primaryand Secondary datasets. use Unittest,thedataset.

are spreadoutamongasmuchas17.7%oftheprojects. Constructor Initializationoccurs in9.7%oftheprojectsand 0.3% of the test suites. Finally, the rarest of all test smells that occurs inonlytwoprojectsandonlythreetestsuiteswithin them, isDefault Test. Figure4alsoshows thatourintroduced Suboptimal Assertsmell constitutesanimportantadditionto Python testsmells:itoccursatleastoncein70.6%ofthe projects and15.4%ofthetestsuites. In comparison with previous works that study Java and An- droid code [25], it can be said that the lists of the most popular test smellsgenerallylooksimilar.ItseemsthatPythoncode has larger percentages by projects, however, direct comparison here shouldbecarriedoutinfuturework.Onespecictest smell thatseemstobelessprevalentinPythonExceptionis Fig.Handlingthat occurs in 64.9% of the projects and only in 8.6% individual of thetestsuites.Unittestsupports aconvenientlistofas- sertions likeassertRaises,assertRaisesRegexandeach otheranddoesnotfullydescribetheactualsmelliness others thatmaypreventtheusersfromusingtry/exceptof code.To getabetterunderstanding,wealsoanalyzedthe keywords intests.co-occurrence oftestsmells. It canalsobeseenthattheresultsforPrimarythedatasetFigure 5 shows the distribution of how many different smells and theSecondarydataset aresimilartoeachother,withtheco-exist withinindividualtestsuites.Itcanbeseenthatonly only noticeableexceptionbeingtheObscure In-LineSetup,16% of all test suites are free from smells. The remaining 84% which israrerinthe Secondarydataset. Thevaluesforof thetestsuiteshaveatleastonesmell:23.1%haveexactly Suboptimal Assertare alsosimilar. Thisdemonstratesthatourone smell,20.6%havetwosmells,16.3%havethree results obtainedforthe Primarydataset areunbiased.and thisnumbergraduallydecreaseswiththeamountofco- Overall, ourresultsshow thatvarious testsmellsarepreva-occurring testsmells.Thehighestnumberinthe lent inPythoncode,even someoftherareronesstilloccurinPrimarydataset appearsinasingletestsuitewith12distinct more than a quarter of all projects. While some of them can betest smells.Thislarge testsuitewith25testcases,inaddition considered more subjective, others make it signicantly harderto allthemostpopulartestsmells,containscommentedout to maintain the code base and to interpret the results of testingempty testcases,catchingerrorswithtry/exceptinstead in caseoffailure.We hopethatinthefutureY NPcan beof usingspecicassertionsoferrormessages,andsleepy used tohelpdevelopersandresearcherstocombatthespreadtests. ItalsousesassertEqual(X, True)instead of of testsmellsintheirrepositories.assertTrue(X). Webelievethathelpingdevelopersnd such suites might be useful for the maintenance of the project.3) Co-occurrenceof test smells:In the previous section, we discussed howprevalentdifferenttestsmellsare.However,Figure 5alsoshedsanewlightontheprevalenceoftest such anapproachconsiderstestsmellsindependentlyfrominPythoncode.Withmorethanhalfofalltestsuites


---

<!-- Página 11 -->

having twodifferenttestsmellsormore,theireffectontheboth datasetsdemonstratesthereproducibilityoftheresults maintainability ofcodecanbecomemorecomplex.of theempiricalstudy. Wealsoadditionallystudiedtheco-occurrenceofspecicIt ispossiblefor PNOSEto have someunnoticed errorsin pairs oftestsmells.Foralloftestsmells,wecalculatedits implementation.However, wetestedthetoolrigorouslyon the followingvalue:whatpercentageoftestsuitesthathavesynthetic data and performed manual evaluation on real-world test smell X also have testY. Two pairs of test smells aredata tominimizetheriskasmuchaspossible. completely connected. Firstly, if the testEmptyis( i.e. , containsOne threattovalidityisrelatedtothedetectionofspecic no executablestatements),itisautomaticallyUnknown( i.e. ,test smells.Someoftheimplementationsoftestsmellsrely has nodirectassertions).Secondly, ifthereisTesta Maverickon specicthresholdsthatwerepickedfromtheliterature.It in atestsuite,thistestsuiteautomaticallyhasGeneralaFix-is possiblethatthesethresholdsaredifferentforPython,and ture . TestMaverickoccurs when the test suite hassetUp()athis requiresfurtherstudy. method witheldsandthegiventestcasedoesnotuseany of theeldsinit.Ofcourse,thisautomaticallymeansthat VII. CONCLUSIONSF UTUREW ORKthere isatleastonemethodthatdoesnotusealloftheelds, which isthedenitionofaFixture. Otherstrongly Testsmellsareprevalentincommonlyusedprogramming connected pairsareallassociatedwithAssertion Roulettedue languages suchasJava andhave adetrimentaleffect notonly to itspopularity.IfatestsuitehasDuplicateaAssert, ithas on the quality of test code but also on the production code [11]. anAssertion Roulettein 93.1%ofthecases.Itmightnot In thiswork,wepresentedPN OSE, thersttoolfortestbe thecaseiftheduplicationhasexplicitmessages(because smell detectioninPythoncodethatiscapableofidentifyingAssertion Rouletteis onlyconsideredifassertionshaveno 18 testsmells.17outofthese18testsmellswereadaptedmessages), butsinceitisverycommontonotwriteerror from testsmellsforotherprogramminglanguagesdescribedmessages, duplicatedassertionscanbecomearoulette.The in the literature, and we added one test smell calledSuboptimalsame goesfor Redundant Assertion, 83.5%ofthetestsuites Assertby analyzingthemostfrequentchangesmadetotestwith whichalsohaveanAssertion Roulette. Thisalsomakes les in450open-sourcePythonprojects.Experimentsonsense, because if there is a redundant assertion,probably a setofeightreal-worldprojectsshowedthatY P OSEisshould besomeotherassertionthatismoremeaningful. capable of detecting test smells with 94% precision and 95.8%This co-occurrenceoftestsmellsdemonstratesthattest recall, whichisonparwithotherpubliclyavailabletoolsforsmells haverelationshipwithoneanotherthatshouldbe test smelldetection.Ourempiricalanalysisshowsthattestexplored ingreaterdetailinthefuture. smells areprevalent inPythoncode,with98%oftheprojects VI. THREATSVALIDITYand 84%ofthetestsuiteshavingatleastonetestsmellin them. ThemostfrequentdetectedtestsmellswereAssertionWhile we structured our study to avoid introducing bias and Roulette, Conditional Test Logic, andMagic Number Test. Weworked toeliminatetheeffects ofrandomnoise,itispossible also observedthattheproposedPython-specicSuboptimalthat our mitigation strategies may not have been effective. This Assertsmell occursinthecoderatheroften,beingpresentinsection reviews thethreatstovaliditytoourstudy. as muchas70.6%oftheprojects.It ispossiblethatduringthesystematicmappingstudyof Future researchdirectionsforthisworkinclude:test smellswemissedsometestthatareapplicable Supporting more test smells, including those that rely onto Python.Also,Pythongrammarisratherlarge,andis production code.being actively updated,soYTHONCHANGEMINERdoes not Discovering more Python-specic smells, which requiressupport allPythonlanguageconstructs,anditispossiblethat a specicanalysisoftheoptimalpatternsearchingwe mayhavemissedpotentialtestsmellchangesbecause parameters forPython.of this.Wealsoreliedonpatterndetectionthresholdsfrom Conducting amorethoroughcomparisonofYPN OSEthe originalpaperbyNguyenetal.[50],whileitispossible to othertools,forexample,toTS DETECTthat worksthat theycouldbedifferentforPythonandfortestingcode. with Java.ItwouldalsobeofinteresttoemploytheHowever,thetoolsupportsallthemainfeaturesofPython tools togethertocarryoutacomparisonoflarge Pythonand stillproducedanumberofcodechangepatterns.In and Javadatasetsfromthestandpointoftestsmelladdition, PYNOSEis builtinsuchawaythatitissimpleto distribution.add newtestsmellsinthefuture. Analyzing testsmellprevalenceinPythononalargerThe resultsofbothpartsofourstudysearchingfor dataset of projects and in other dimensions, for example,Python-specic testsmellsandanalyzingtheprevalenceof it wouldbeofgreatinteresttoseehowtestsmellstestinPythoncoderelyonaspecicsetofopen- correlate withtestcoverage[26].source projectsthatweselectedandmightnotgeneralizeto all projects, including proprietary ones. However, we analyzedP Y NOSEis availableonGitHubforuseintheIDEand for research:[https://github.com/JetBrains-Research/PyNose](https://github.com/JetBrains-Research/PyNose),two moderately large datasetsPrimary(and Secondary) for our all theresearchartifactsofthisstudyarealsopubliclyavail-tasks thatwerecuratedusingvariousconditionssuggestedin able: [https://zenodo.org/record/5156098](https://zenodo.org/record/5156098).the literature.Webelievethatthesimilarityofresultsfrom


---

<!-- Página 12 -->

[22]R EFERENCES relative2006 Conference. IEEE,[1]Refactoring: [23]code .Addison-Wesley andWASDeTT-1:in[2] Internationalempirical Techniques. Citeseer,tainability,Journal, vol. [24]2003. testProceedings[3] Scala,2019,error [25]Journal, vol. and[4] androidProceedingscommit Annualthe. Engineering,2019,ACM, ´[26][5] I.Pro-and ceedings,inProceedings 2019,software. IEEE [27]pp. detection[6] andIEEE, vol.signicantACM no.Engineering, vol. [28] [7] tion2018 impact Conference. IEEE, Workshop. ACM, 2018, [8] [29] and and (andIEEE inProceedings Engineering,vol. Engineering [9]Engineering,2020, toringProceedings [30] on Just-in-time (XP2001).Citeseer, Proceedings [10]hension,2020, empirical[31]´ on2012I. on. IEEE,identicationProceedings [11]Symposium, 2020, On2018´[32] IEEEI.Proceedingsin (ICSME).IEEE,Brazilian, 2020, [12][33]Evidence-based testEmpiricalengineering. CRC Engineering,vol.[34] [13]andProceedings andinternational smells,Proceedingsengineering,2014, on, 2016,[35]et, Guidelines [14]in of2013Report. Conference. IEEE,[36] 2013,[Online]. [15][37] and[Online]. 16th.[38]oth,acs, IEEE,conceptual2018 [16]6th Mainin. IEEE, learning,Information,vol.[39]acs,othy, 2020.method [17]17th, 2020, python, App. Systems., 2018.[40] [18]methods2015 fromarXivtional arXiv:2105.10157, 2021.(SCAM).IEEE, [19][41] developers.[Online]. [20]The[42] practices. O'ReillyAvailable: [21]xUnit. Pearson[43] Education,[Online].


---

<!-- Página 13 -->

7719290b8dd6940dd195a195120c075a4f94cf42[44]Python. Packt [45]Proceedings[53] the, ser.project. MSRedbb26caad50cd0cc6352e6fe5b84fbd6edaaf9b [Online].[54] [46]viewboard [Online].reviewboard/commit/1758bf53057ee7b648ace1c557031d9460c88c00 [47][55] dataset.project. master/PublicGitArchive/pga-createf4b6040618dbe9a7edca99d8f6344a316b5b1f10 [48] [56] forProceedings project. Software, 2018, 2b921b19fd5a23bc2e86060c2c12137d63dfe1db [49] [57]D. python-chess2014. python-chess/commit/944a0e682174ff32a6f9689176aa9016bab44a31[50] [58]Graph-based project.patterns,2019 gensim/commit/342f10a2472fb22d811a398f5a6d49d1b6a88ab0Engineering, 2019, [59][51] requestsFine-grainedACM/IEEE commit/a8555d811df0a4aaf2dd1f083ba0bc71679101caInternational [60]Vasteras,, 2014, intellij[52] intellij/psi.htmlproject.


---

