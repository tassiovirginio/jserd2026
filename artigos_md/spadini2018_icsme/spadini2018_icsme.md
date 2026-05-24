<!-- Página 1 -->

**AbstractTest** **implementation of test code. As reported by recent studies, their** **presence might** **test suites** **in nding** **toward understanding test smells, there is still a notable absence** **of studies** **In this** **presence of** **test code, as well as the defect-proneness of the tested production** **code. To this aim, we collect data on 221 releases of ten software** **systems and we analyze more than a million test cases to investi-** **gate the association of six test smells and their co-occurrence with** **software quality.** **smells are more change- and defect-prone, (ii) `Indirect Testing',** **`Eager Test',** **smells for** **defect-prone when**

Automated testing has become software systems out defects many usage conditions [12], [16]. Writing tests, however, is as challenging as maintain test code [11]. Nevertheless, recent and treat thus generating [82]. This nding is in line with the experience reported by van Deursenet al. was not was not refactored as mercilessly as our production code [74]. In the same work, van Deursen test smells, inspired by Fowler smells were when refactoring Since its signicant traction the software [76]. Bavota results advancing test smells laboratory experiment on program

## On The

## Relation

## of

## Test

## Smells

## to

## Software Code

## Quality

zxzxDavide Spadini,Fabio PalombaAndy Zaidman,Magiel Bruntink,Alberto Bacchelli zxSoftware ImprovementGroup,Delft UniversityofTechnology,ofZurich zxf d.spadini, [a.e.zaidmang@tudelft.nl](mailto:a.e.zaidmang@tudelft.nl),[m.bruntink@sig.eu](mailto:m.bruntink@sig.eu),f palomba, bacchellig@i.uzh.ch

ofanegativeimpactoftestonbothsmellsaresub-optimaldesignchoicesinthe found evidence comprehensibility andmaintainabilityoftestcode[7]. notonlynegativelyaffectthecomprehensionof Although thestudybyBavotaet al.[7] madearst,butcanalsoleadtotestcasesbeinglesseffective necessary steptowardtheunderstandingofmaintainabilitybugsinproductioncode.Althoughsignicantsteps aspects oftestourempiricalknowledgeonwhether assessingtheirassociationwithsoftwarequality.and howtestsmellsareassociatedwithsoftwarequality paper,weinvestigatetherelationshipbetweentheaspects isstilllimited.Indeed,vanDeursenet al.[74] based testsmellsandthechange-anddefect-pronenessof their denitionoftestsmellsonanecdotalexperience, without extensiveevidenceonwhetherandhowsuchsmells are negatively associatedwiththeoverallsystemquality.

Tollthisgap,inthispaperwequantitativelyinvestigate Keyresultsofourstudyinclude:(i)testswith the relationship between the presence of smells in test methods and thechange-anddefect-pronenessofboththesetestand`AssertionRoulette'arethemostsignicant change-pronenessand,(iii)productioncodeismoremethods andthecodetheyintendtotest.Similar testedbysmellytests.to severalpreviousstudiesonsoftwarequality[24],[62],we employ theproxymetricschange-pronenessi.e.(, numberof I. INTRODUCTIONtimes amethodchangesbetweentworeleases)anddefect- proneness (i.e., number of defects the method had between two(hereafterreferredtoasjust) releases). Weconductanextensiveobservationalstudy[15],anessentialprocessforimprovingthequalityof collecting datafrom221releasesoftenopensourcesoftware[12],[47].Infact,testingcanhelptopoint systems, analyzemorethanamilliontestcases,andinves-andtoensurethatproductioncodeisrobust under tigate theassociationbetweensixtestsmelltypesandthe aforementioned proxymetrics.writingproductioncodeanddevelopers should Based ontheexperienceandreasoningreportedbyvancodewiththesamecaretheyuseforproduction Deursen et al.[74], we expect to nd tests affected by smells to beassociatedwithmorechangesanddefects,i.e. , higherstudiesfoundthatdevelopersperceive maintenance effortsandlowersoftwarequality.Furthermore,productioncodeasmoreimportantthantestcode, since testsmellsindicatepoordesignchoices[74]andprevi-qualityproblemsinthetests[9],[10],[57], ous studiesshowed thatbettertestcodequalityleadsto productivity whenwritingproductioncode[4],weexpectto[74], who described how the quality of test code nd productioncodetestedbysmellyteststobeassociatedashighastheproductioncode[because]testcode with moredefects. et al. introduced the concept ofOur resultsmeettheseexpectations:Testswithsmellsare et al. 'scode[23]. Thesemore change-anddefect-pronethantestswithoutand recurrentproblemsthatvanDeursenet al.foundproduction codeismoredefect-pronewhentestedbysmelly theirtroublesometests[45].tests. Amongthestudiedtestsmells,`Indirecttesting',`Eager Test'and `Assertion Roulette' are those associated with highestinception,theconceptoftestsmellshasgained change-proneness; moreover,thersttwoarealsorelatedtobothamongpractitioners[18],[42]and a higherdefect-pronenessoftheexercisedproductioncode.engineeringresearchcommunity[7],[26],[74], Overall, ourresultsprovideempiricalevidencethatdetectinget al.presented theearliestandmostsignicant ourempiricalknowledgeontheeffectsoftest smells is important to signal underlying software issues as well asstudyingtheinterplaybetweentestdesignqualityand[7].Theresearchersconductedtherstcontrolled effectivenessondetectingdefectsisofparamountimportancetoestablishtheimpactoftestsmells researchcommunity.comprehensionduringmaintenanceactivitiesand for the


---

<!-- Página 2 -->

II. RELATEDW ORKFinally,PalombaandZaidman[56]investigatedtheextent to whichtestsmellscanbeexploitedtolocateakytests, Over thelastdecadetheresearchcommunityspentacon- i.e. , testcaseshavinganon-deterministicbehavior[40].The siderable effort in studyinge.g.(, [1], [3], [32], [39], [51], [55], main ndings of the work showed that (i) almost 54% of aky [59], [61], [66], [72], [78][80]) and detectinge.g.(, [33], [36], tests containatestsmellthatcancausetheakinessand(ii) [41], [43],[46],[49],[52],[54],[70])designawsoccurring the refactoringoftestsmellsremovedboththedesignaws in productioncode,alsoknownascode smells[23]. Atthe and testcodeakiness[56]. same time,problemsconcerningthedesignofcodehave The workwepresentinthispaperiscomplementarytoonly beenpartiallyexploredandourliteraturesurveyshowed the onesdiscussedsofar:Weaimatmakingafurtherstepus thatourempiricalknowledgeisstilllimited. ahead byinvestigatingthechange-anddefect-pronenessofIn thissection,werstdiscusstheliteraturerelatedto test smells, as well as the defect-proneness of production codetest smells,thenwediscusspreviousworkthatanalyzedthe tested bysmellytests.change- anddefect-pronenessofcodesmells,asitcanshed light onwhytestsmellscanalsobeproblematic.

A. TestSmellsB. Change-andDefect-pronenessofCode

The importanceofhavingwell-designedtestcodewas The softwareengineeringresearchcommunityhascon-initially putforwardbyBeck[8].Beckarguedthattestcases ducted extensiveworkinthecontextofcodesmellsinrespecting gooddesignprinciplesaredesirablesincethese production code. More specically, Khomhet al.[31] showedtest casesareeasiertocomprehend,maintain,andcanbe that thepresenceofcodesmellsincreasesthecode's change-successfully exploitedtodiagnoseproblemsintheproduction proneness. Lateron,theyalsoshowedthatcodecomponentscode. Inspiredbythesearguments,vanDeursenet al.[74] affected bycodesmellsaremorefault-pronethannon-smellycoined thetermtestsmellsanddenedtherstcatalogof11 components [32].TheirresultswereconrmedbyPalombapoor designchoicestowritetests,togetherwithrefactoring et al.[50], whofoundthatcodesmellsmakeclassesmoreoperations aimedatremovingthem.Suchacataloghas change- and defect-prone; in addition, they also found that thebeen thenextendedmorerecentlybypractitioners,suchas class' change-pronenesscanbenetfromcodesmellremoval,Meszaros [42]whodened18newtestsmells. while thepresenceofcodesmellsinmanycasesisnotFrom thesecatalogs,Greileret al.[25], [26]showedthat necessarily thedirectcauseoftheclassdefect-proneness,buttest smells affecting test xtures frequently occur in a company rather aco-occurringphenomenon[50].setting. Motivated by this prominence, Greileret al.presented Gatrell andCounsell[24]conductedanempiricalstudyT ESTHOUND, a tool able to identify xture-related test smells aimed at quantifying the effect of refactoring on class change-such as`GeneralFixture'or`Vague HeaderSetup'[25].Van and defect-proneness.Inparticular,theymonitoredacom-Rompaeyet al.[76] devisedaheuristiccodemetric-based mercial projectforeightmonthsandidentiedtherefactoringtechnique thatcanidentifytwotestsmelltypes,i.e. , `General operations appliedbydevelopers duringtherstfourmonths.Fixture' and`EagerTest'. However, theempiricalstudycon- Then, theyexaminedthesameclassesforthesecondfourducted to assess the performance of the technique showed that months toinvestigatewhethertherefactoringresultsinait oftenmissesinstancesofthetwosmells. decrease ofchange-anddefect-proneness.TheycomparedTurning theattentiontotheempiricalstudiesthathadtest against classesofthesystemthatwerenotrefactoredduringsmells as their object, Bavotaet al.[7] studied (i) the diffusion the sameperiod.Resultsrevealedthatclassessubjecttoof testsmellsin18softwareprojects,and(ii)theireffects refactoring havealowerchange-anddefect-proneness.on softwaremaintenance.Theyfoundthat82%ofJUnit classes areaffectedbyatleastonetestsmellandthattheLi andShatnawi[38]empiricallyevaluatedthecorrelation presence oftestsmellshasastrongnegativeimpactonthebetween theofcodeandtheprobabilitythat comprehensibility of the affected classes. The high diffusenessthe classcontainserrors.Theystudiedthepost-releaseevo- of testsmellswasalsoconrmedinthecontextofthetestlution processshowingthatmanycodearepositively cases automaticallygeneratedbytestingtools[53].correlated withclasserrors.Olbrichet al.[48] studiedthe Tufanoet al.[71] conductedanempiricalstudyaimedat maintainability oftwospeciccodesmelltypes,i.e. , `God measuring theperceivedimportanceoftestsmellsandtheirClass' and`BrainClass',reportingthatclassesaffectedby such smellschangelessfrequentlyandhaveafewernumberlifespan duringthesoftwarelifecycle.Keyresultsofthe thannon-smellyclasses.D'Ambroset al.[20]investigationindicatedthatdevelopersusuallyintroducetest of defects studied how`FeatureEnvy'and`ShotgunSurgery'instancessmells intherstcommitinvolvingtheaffectedtestclasses, and inalmost80%ofthecasesthesmellsarenever removed,are relatedtosoftwaredefects,reportingnoconsistentcorre- primarily because of poor awareness of developers. This studylation betweenthem.Finally,Sabouryet al.[63] empirically investigatedthe impact of code smells on the defect-pronenessstrengthened thecaseforhavingtoolsabletoautomatically of JAVAS CRIPTmodules, conrmingtheadverseeffectofdetect testsmellstoraisedevelopers'knowledgeaboutthese smells onsourcecodemaintainability.issues.


---

<!-- Página 3 -->

III. RESEARCHM ETHODOLOGYTABLE S UBJECT' DETAILS The goalof our study is to increase our empirical knowledge on whetherandhowtestmethodsaffectedbysmellsare associated withhigherchange-anddefect-pronenessofthe test codeitself,aswellastoassesswhetherandtowhat extent testmethodsaffected bytestsmellsareassociatedwith the defect-pronenessoftheproductioncodetheytest.The perspectiveis thatofbothresearchersandpractitionerswho are interestedinunderstandingthepossibleadverseeffectsof test smellsontestandproductioncode.Westructuredour #Classes#Methods#KLOCstudy aroundthetwooverarchingresearchquestionsthatweSystem(Min-Max) describe inthefollowing. Apache Apache **RQ2.2:**Is theco-occurrence oftestsmellassociatedwiththeThe rstresearchquestioninvestigatestherelationshipApache Apachedefect-proneness ofthetestedproductioncode?between thepresenceoftestsmellsintestcodeandits Eclipse change/defect proneness:**RQ2.3:**Are certaintestsmelltypesmore associatedwiththeElasticSearch Hibernatedefect-proneness ofproductioncode? Sonarqube **RQ1.**Are testsmellsassociatedwithchange/defectprone-SpringSimilarly to**RQ1, we**aimatprovidinganoverview ofthe VRaptor4ness oftestcode? role oftestsmellsinthedefect-pronenessofproductioncode, Total by investigating singletestsmellsandtheirco-occurrence. We,thus,structure**RQ1**in threesub-researchquestions. A. SubjectsoftheStudyFirst, we aim at providing a broad overview of the relationship of test smells and their co-occurrence with change- and defect-In ourstudy,wehavetoselecttwotypesofsubjects: proneness oftestcode:software systemsandtestsmells. **Software systems.**WeconsidertenOSSprojectsand**RQ1.1:**Towhatextentaretestsmellsassociatedwiththe their 221majorreleasesassubjectsystemsforourstudy.change- anddefect-pronenessoftestcode? Specically,Table Ireportsthecharacteristicsoftheanalyzed **RQ1.2:**Is the co-occurrence of test smells associated with the systems concerning(i)thenumberoftheconsideredreleases change- anddefect-pronenessoftestcode? and (ii)size,intermsofthenumberofclasses,methods, and KLOCs.Twomainfactorsdrivetheselection:rstly,Then, weaimatverifyingwhethersomeparticulartest since wehave torunstaticanalysistoolstodetecttestsmellssmells haveastrongerassociationwithchange-anddefect- and computemaintainabilitymetrics,wefocusonprojectsproneness oftestcode: whose sourcecodeispubliclyavailablei.e.( , OSS);secondly, **RQ1.3:**Are certaintestsmelltypesmore associatedwiththewe analyzesystemshavingdifferentsizesandscopes.After change- anddefect-pronenessoftestcode?ltering on these criteria, we randomly select ten OSS projects 1from thelistavailableonGhaving differentsize,Considering thatdefect-pronenessasbeenwidelyusedin scope, and with a number of JUnit test cases higher than 1,000previous literatureasaproxymetricforsoftwarequality in allthereleases.( e.g. , [20],[24],[32],[50]),inthesecondresearchquestion, For eachsystem,weonlyconsidertheirmajorreleases.Inwe aimatmakingacomplementaryanalysisintotheassocia- fact, (i)detectingtestsmellsatcommit-levelisprohibitivelytion oftestwiththedefect-pronenessoftheexercised expensiveintermsofcomputationaltimeand(ii)minorproduction code.Infact,ifthecodeexercisedby releases aretooclosetoeachother(insomecasesthereistests withtestsmellsismoredefect-pronethiswouldbean more thanoneminorreleaseperweek),soveryfewchangeseven strongersignalontherelevance oftestsmells.Thisgoal are madeinthesourceandtestcode.Weminethesemajorleads tooursecondresearchquestion: releases directlyfromthesystems'Grepositories. **RQ2. Is the production code tested by tests affected by test****Test**smells.As subject test smells for our study, we consider smells moredefect-prone?those describedinTable II.Whileothertestsmelltypeshave been denedinliterature[42],[74],weselectthesmellsin TableIIbecause:(1)Identifyingtestin221projectThe expectationisthattestcodeaffectedbytestsmells releases throughmanualdetectionisprohibitivelyexpensive,might belesseffectiveindetectingdefects[4],thusbeing thus areliableandaccurateautomaticdetectionmechanismassociated withmoredefect-proneproductioncode.We struc- must be available; (2) the selected test smells have the greatesttured**RQ2**in threesub-researchquestions: diffusion inindustrialandOSSprojects[7];and(3)the**RQ2.1:**Are testsmellsassociatedwiththedefect-proneness of thetestedproductioncode?1[https://github.com](https://github.com)


---

<!-- Página 4 -->

TABLE S UBJECT

**Test****Description****Problem** `Mystery using someone `ResourceAIt state/existencesituation other `Eager use on `AssertionAIf `IndirectThis anotherhiding `SensitiveAIt quotes, is

selected onescomposeadiverse catalogoftestsmells,which3) Weparsethesourcecodeofthetestclasstoidentify are relatedtodifferentcharacteristicsoftestcode.the testmethodscontainedinthecurrentandinthe previous commit.Then,wecomparethesourcecodeof each testmethodfromthecurrentcommitagainstalltheB. DataExtraction test methodsofthepriorversion: Toanswer**RQ1 , we**extractdataabout(i)thetestsmells a) ifwendthesamemethod,itmeansthatitisnot affecting thetestmethodsineachsystemreleaseand(ii)the changed (i.e., both signature and content of the method change/defect pronenessofthesetestcases.To answer**RQ2 ,** inrare thesameas r);jj   1we extractdataaboutthedefectpronenessoftheproduction b) ifwe nd a different method, it means that it is changed code exercisedbythetestcode.Theobtaineddataandthe ( i.e. , thesignatureofthemethodisthesame,butthe Rscript usedtoanalyzetheresultsarebothavailableinour source codein ris notequalto r);jj   1online appendix[14]. c) ifwedonotndthemethodi.e.(thesignatureof **Detecting test**smells.Weadoptthetestsmelldetectorbythe methoddoesnotexistinthepreviousversionof Bavotaet al.[7] (widelyadoptedinpreviousresearch[7],the le),itmeansthatithasbeenaddedorrenamed. [53], [56],[71]),whichisabletoreliablyidentifythesixTocapturethelatter,weadoptatechniquesimilarto smells consideredinourstudywithaprecisioncloseto88%the oneproposedbyBiegelet al.[13], basedonthe and arecallof100%,byrelyingoncodemetrics-basedrules.use oftextualanalysistodetectrenamerefactoring operations. Specically,ifthecosinesimilarity[5]**Dening the**change-pronenessoftestcode.Tocom- between thecurrentmethodandthatofthemethodspute change-anddefect-pronenessoftestcode,wemine in thepreviousversionishigherthan95%,thenwethe changehistoryinformationofthesubjectsystemsusing consider amethodasrenamed(hence,itinheritedallR EPODRILLER[2], a Java framework that allows the extraction the informationoftheoldtestcase).of informationsuchascommits,modications,diffs,and **Dening the**defect-pronenessoftestTocomputesource code.Explicitely, foreachtestmethodTof aspecici the defect-pronenessofeachtestcase,wefollowasimilarreleaserwe computeitschange-pronenessasfollows:j procedure to the one for change-proneness, with the exceptionchangeproneness(T; r) = #commits(T)ijir! rj   1jthat to calculatethebuggy commits we reliedonSZZ [67].In where# commits(T)represents thenumberofiparticular, werstdeterminewhetheracommitxed adefectr! rj   1j changes performedbydevelopersonthetestmethodTiemploying the technique proposed by Fischeret al.[22], which between thereleasesrandr. Giventhegranularityofj   1jis basedontheanalysisofcommitmessages.Ifa our analyses (, release-level), we only compute the change-message matchesanissueIDpresentinthetrackerorit proneness oftestmethodsthatwereactuallypresentinacontains keywords such as`bug', `x', or `defect', we consider releaser; ifanewmethodwasaddedandremovedbetweenjit asabugxingactivity. Thisapproachhasbeenextensively randr, itdoesnotappearinourresultset.To identifyj   1jused in the past to determine bug xing changes [29], [34] and which testmethodchangedwithinacommit,weimplementit hasanaccuracy closeto80%[22],[55],thuswedeemitas the followingalgorithm:being accurateenoughforourstudy.Oncewehavedetected all the bug xing commits involving a test method, we employ1) Werstidentifyalltestclassesmodiedinthecommit. SZZ toobtainthecommitswherethebugwasintroduced.In linewithpastliterature[71],[81],weconsideraclass Toestimatethemomentwhenabugwaslikelyintroduced,to beatestwhenitsnameendswith`Test' or`Tests'. 2) Foreach test class, we obtain the source code of the classthe SZZalgorithmreliesontheannotation/blamefeatureof versioning systems[67].Inshort,givenabug-xactivityin boththepresentcommitandthepreviousone.


---

<!-- Página 5 -->

identied bythebugIDk , theapproachworksasfollows:C. DataAnalysis Toanswer**RQ1 , we**analyzethepreviously extractedinfor-For eachlef,i= 1: : : minvolvedinthebug-xik mation regardingtestsmellsandchange-anddefect-prone-k( mis thenumberofleschangedinthebug-xk )k ness of test code. In particular, in the context**RQ1.1**of, we testand xedinitsrevisionrel-x, weextractedthelei;k whether JUnittestmethodsthatcontainatestsmellaremorerevision justbeforethe bugxing(  1 ).i;k likely tobechange-ordefect-prone.To thisaim,wecomputeStarting fromtherevisionrel-x  1 , foreachsourcei;k the Relative Risk(RR)[37],anindexreportingthelikelihoodline infchanged toxthebugk , weidentiedthei that aspeciccause(inourcase,thepresence/absenceofproduction methodMto which the changed linej a testsmell)leadstoanincreaseintheamountatestcasebelongs. Furthermore,the blamefeature ofGitis used is subjecttoaparticularproperty(inourcase,numberofto identifytherevision wherethelastchangetothatline changes ordefects)[30],[58].TheRRisdenedastheratiooccurred. Indoingthat,blanklinesandthatonly of theprobabilityofaneventoccurringinanexposedgroupcontain comments are identied using an island grammar ( e.g. , theprobabilityofsmellytestsbeingdefective),totheparser [44].Thisproduces,foreachproductionmethod probability oftheeventoccurringinanon-exposedgroupM, asetofnbug-inducing revisionsrel-bug,j=ji;ki;j;k ( e.g. , theprobabilityofnon-smellytestsbeingdefective)and1 : : : n. Thus,morethanonecommitcanbeindicatedi;k it iscomputedusingthefollowingequation:by theSZZalgorithmasresponsibleforinducingabug.

With thelistofbuginducingcommitsinvolving everytestpevent RR =method, wecomputeitsdefect-pronenessinareleaserasjpevent the numberofbug inducingactivities involving themethodin A relative riskof1meansthattheevent isequallylikely in the periodbetweenthereleasesrandr.j   1jboth samples.ARRgreaterthan1indicatesthattheeventis **Dening the**defect-pronenessofproductioncode.Formore likelyintherstsamplee.g.( , whenthetestissmelly), each testmethodintheconsideredprojects,werstneedtowhile aRRoflessthan1pointsoutitismorelikelyin retrieve what is the production method it exercises. For this, wethe secondsample(, whenthetestisnotsmelly).We exploit atraceabilitytechniquebasedonnamingconvention,prefer usingthisratherthanalternativestatistical i.e. , it identies the methods under test by removing the stringtests adoptedinpreviousworke.g.(, analysisofboxplots `Test'from themethodnameoftheJUnittestmethod.This[50] or Odds Ratios [6], [32]) because of the ndings reported technique has been previously evaluated by Sneed [68] and byin thestatisticeldthatshowedhowthismethod(i)should VanRompaeyandDemeyer[75],demonstratingthehighestbe preferredwhenperformingexploratorystudiessuchasthe performance (bothintermsofaccuracyandscalability)withone conductedherein[21],[83]and(ii)isequivalent toOdds respect toothertraceabilityapproachese.g.(, slicing-basedRatios analysis[64]. approaches [60]).Change- anddefect-pronenessofJUnittestmethodsmight Once we detect the links between test and production meth-also beduetootherfactorsratherthanthepresenceofatest ods, wecancomputethedefect-pronenessofsuchproductionsmell. Indeed, Kitchenhamet al.[35] found that both size and methods. Sincewecalculatetestsmellsatthereleaselevelnumber ofpreviouschangesmightinuencetheobservations ( i.e. , weonlyhave informationregardingwhichtestissmellyon thedefect-pronenessofsourcecode;additionally,Zhou at thespeciccommitoftherelease),wehavetodetecthowet al.[84], reportedtheroleofsizeaspossibleconfounding many defectsproductionmethodshavewithinthatparticulareffect whenstudyingthechange-pronenessofcodeelements. release. Tothisaim,werelyagainontheSZZalgorithm.Based ontheevidenceabove,wecontrolourndingsfor Todetectdefectsofproductioncodeinaspecicrelease,wechange-proneness bycomputingtheRRachieved considering only considerbugxingactivitiesrelatedtobugsintroducedthe sizeofthetestmethodintermsoflinesofcode(LOC). before the releasedate.Moreformally, wecomputethefault-Moreover,we control the phenomenon of defect-proneness by proneness ofaproductionmethodMin arelease ras theconsidering LOCoftestmethodsandnumberoftimestheij number ofchangestoMaimed atxingabugintheperiodmethod changedfromthelastreleasei.e.( , priorchanges).i between rand r, where the bug was introduced before theMore specically, theaimistounderstandwhetherthelikeli-jj +1 release date,intheperiodbetweenrandr. Theobtainedhood ofatestcasebeingsmellyandmore change-ordefect-j   1j list ofbugs aretheonesthatwerepresentinthesystemwhenprone varies when controlling for size and number of changes. it wasreleased,hencenotcapturedusingtests.In otherwords,ifsmellytestsareconsistentlymoreproneto By employing SZZ, we can approximate the time periods inand defects than non-smelly tests, independently from which eachproductionmethodwasaffectedbyoneormoretheir size or number of times they changed in the past, we have bugs. We exclude from our analysis all the bugs occurring inahighercondence that the phenomena observed are associated production methodMafter thesystemwasreleased,because with testsmells.i answer**RQ1.2**and analyzetheroleoftestco-in thiscasethetestsmellcouldhavebeensolvedbeforeTo occurrences, wesplitthepreviouslyextracteddatasetintothe introductionofthebug.We alsoexcludebug-introducing seven groups,eachonecontainingtestmethodsaffectedbychanges thatwererecordedafterthebugwasreported,since exactlyismells, where0i6 . Then,wecomparethey representfalsepositives[19].


---

<!-- Página 6 -->

# 1

## 1.47 size

## average overall

## small

### 1.46-1.50

change- anddefect-pronenessofeachgroupusing(i)the Wilcoxon ranksumtest[77](withcondencelevel95%) and (ii)Cohen'sd[65] toestimatethemagnitudeofthe observed difference.WechoosetheWilcoxontestsinceitis a non-parametrictest(itdoesnothave anyassumptiononthe underlying datadistribution),whileweinterprettheresults of Cohen'sdrelying onwidelyadoptedguidelines[65]:The effect sizeisconsideredsmallfor0.2 d <0.5, mediumfor 0.5 d <0.8, andlargefor d 0.8. Toanswer**RQ1.3, we**adoptthesameprocedureasfor **RQ1.2, but**weconsidereachsmelltypeseparately,i.e. , we compare change- and defect-proneness of different smell types by means of Wilcoxon rank sum test [77] and Cohen'sd[65], Fig.vsnon-smellycontrolling forsizeandnumberofpreviouschanges(onlyin tests,<0 : 0001.case ofdefect-proneness).Itisimportanttonotethat,asdone in earlierwork[32],[50],inthisanalysisweconsidertest (LOC) andnumberofchanges,whichhavebeenreportedto cases affectedonlyby asingletestsmell,e.g. , onlyEager correlate withcodecomplexity[17].Asshownintheresults test , withtheaimofunderstandingtheeffectofsingletest section, theresultsgenerallydonotchangewhencontrolling smells onchange-andfault-pronenessoftestcode. for othermetrics.Furthermore,atthebeginningofthisstudy For**RQ2**we adoptaprocesssimilartothatRQ1. In we alsobuiltaLogisticRegressionModeltodetectwhether particular, for**RQ2.1**we computetheRR:inthiscase,we our explanatoryvariablewas(not)statisticallysignicantin aim toinvestigate thelikelihoodthatthepresence/absenceof the model.SimilarlytoThongtanunamet al.[69], webuilta a testsmellisassociatedwiththedefect-pronenessofthe logistic regressionmodeltodeterminethelikelihoodofatest production codebeingtested.Similarlyto**RQ1 , we**control being defective(orchangeprone)usingLOC,priorchanges, for sizeandnumberofchanges.Analogously,inwe production changes as control variables and being smelly (our use (i)theWilcoxonranksumtest[77]and(ii)Cohen's new variable)asabinaryexplanatoryvariable.WeusedR d[28] toassesstheassociationoftestsmellco-occurrences scripts providedbyThongtanunamet al.[69] tobuildthe to thedefect-pronenessofproductioncode.Finally, toanswer model, and we discovered that test code smelliness was indeed **RQ2.3, we**comparethedistributionofthenumberofdefects statistically signicantforthemodel.However, wepreferred related totheproductioncodetestedbydifferenttestsmell to proceed with RR instead of the model, for better readability types (consideringsingletest smelltypes). of theresults. D. ThreatstoValidity**External validity.**Threats toexternalvalidityconcernthe Our researchmethodposessomethreatstothevalidityofofresults.We conductedourstudytakinginto the resultsweobtain.account 221 releases of 10 Java systems having different scope **Construct validity.**Threats toconstructvalidityconcernand characteristicstostrengthenthegeneralizabilityofour our researchinstruments.To obtaininformationregarding testndings. However, astudyinvestigating different projectsand smells weusethetestsmelldetectordevisedbyBavotaetprogramming languagesmayleadtodifferingconclusions. al.[7]. Eventhoughthistoolhasbeenassessedinprevious IV. RQ1RESULTS : TESTS MELLST ESTC ODEstudies [7],[56]asbeingextremelyreliable,somefalse positives canstillbepresentinourdataset.This sectiondescribestheresultsto**RQ1 .** Another threatisrelatedtohowwedetectedwhichpro- RQ1.1: Towhatextentaretestsmellsassociatedwiththeduction methodisexercised byatestmethod:specically, we change- anddefect-pronenessoftestcode?exploited a traceability technique based on naming convention that hasbeenheavilyadoptedinthepast[6],[53],[71],[81].Figure 1depictstheRelativeRiskoftestsmellstobe This techniquehasalsobeenevaluated bySneed[68]andbyassociated withhigherchange-pronenessoftestcases(label VanRompaeyandDemeyer[75],andtheresultsreportedanOverall) aswellashowtheriskisconnectedwiththe average precisionof100%andarecallof70%.control factoranalyzed,i.e. , size.Inparticular,weshow how RRvarieswhenthetestmethodhas(i)smallsize**Internal validity.**Threats tointernalvalidityconcernfac- LOC <30 ), (ii)averagesize30(< LOC<60 ), and(iii)tors thatcouldaffectthevariablesandtherelationsbeingin- large size (>60 ). The thresholds used to identify small,vestigated. When we look into the relation between test smells medium, andlargetestmethodswereidentiedbyapplyingand testdefects,manyfactorscaninuencetheresults.For theMaintainability Modelproposed byHeitlager et al.[27],example, a test could contain more defects than others because which cuts the distribution of all the method LOCs at the 70th,more complex, bigger, or more coupled, while the studied vari- 80th and90thpercentiles.We alsorepresentthep -value andable (testsmells)couldbeinsignicant.To mitigatethis,we the condenceintervalforeachcategory.control forsomeofthesemetrics,namelysizeofthemethod

## large

### Conf. Int.


---

<!-- Página 7 -->

12.5 40

10.0

30

7.5

20

5.0

Number of changes 10 2.5

0.0

# 1

# 1.45

## 1.74-1.89 average

## overall

## yes

## no

## size small large

### 1.50-1.63

Fig.non-smelly controlling< 0 : 0001.

Wemake two main observations from the results in Figure 1. Fig. On theonehand,testmethodsaffectedbyatleastonesmellchanges are morechange-pronethannon-smellymethods,withan RR of1.47;fromapracticalperspective,thismeansthata smelly testhastheriskofbeing47%morechange-prone than anon-smellytest.Ontheotherhand,wecannotice that smellytestswithhighersizearemorechangeprone: this isintuitivesincelargermethodsaremoredifcultto maintain (hencemorechangeprone)andthey aremorelikely to containsmells.Animportantresulttonoticeisthatlarge smelly tests(>60 ) aremorethantwicemorelikelyof being changepronethannotsmellylargetests.Thisnding is agoodincentiveforpractitionersanddeveloperstowrite small andconcisetests,asrecommendedbyBeck[8]. Concerning defect-proneness,Figure2showshowtheRR varies when considering (i) the presence of test smells (Over- all), (ii)thesizeoftestcasessplitinthesameway asdone for change-proneness, and (iii) the number of previous changes applied totestcases(wediscriminatedbetweenmethodsthat Fig.change frequentlyvs.methodsthatinfrequentlychange,by adopting theheuristicproposedbyRomanoandPinzger[62], **Finding 1. Tests affected**bytestsmellsareassociated Number of bugs methodsi.e. , weconsideredfrequentlyevolvingtohavea with higherchange-anddefect-pronenessthantestsnumber ofchangeshigherthanthemedianofthedistribution not affectedbysmells,alsowhencontrollingforbothof all the changes that occurred in test cases  2, in our case). the testsizeandthenumberofprevious changes.From Figure2,weobservethatthepresenceoftestsmells is associatedwiththedefect-pronenessoftestcases.Indeed, RQ1.2 Istheco-occurrenceoftestsmellsassociatedwiththemethods affectedbyatleastonedesignawhavetherisk change- anddefect-pronenessoftestcode?of being81%moredefect-pronethannon-smellyones.Addi- tionally,theresultdoesnotchangewhencontrollingforsizeWhile in the previous research question we did not discrim-

## C.P.

and numberofchanges.Indeed,thedifferenceisevenmoreinate ontheoftestsmellsatestmethodcontained, prominent forlargetests:thesmellyonesare3.5timesmorethe goalofthisanalysisistoassesswhethertestsmell defect pronethanthenotsmelly.Instead,changepronenessco-occurrences isassociatedwiththechange-anddefect- seems notrelevantwhendiscriminatingthedefect-pronenessproneness oftestcases.Figures3and4reportboxplots of testcases.Inbothcases,theRRofsmellytestsofbeingshowing change-anddefect-pronenessoftestcasesaffected more defectproneis50%higher.by adifferentnumberoftestsmells,respectively. Overall, theresultsofthisrstanalysisprovideempiricalFor change-proneness,themedianofthedifferentgroups evidence thattestsmellsdenedwiththeaimofdescrib-very low (around one) for all test cases: to some extent, this is ing asetofbadpatternsinuencingtestcodemaintain-in line with the ndings by Zaidmanet al.[82], who found that developers generallydonotchangetestcasesassoonastheyability [74]areindeedassociatedwithhigherchange-and defect-proneness oftheaffectedtestcases.implement new modications to the corresponding production

001122334 456 Number of test smellsNumber of test smells

## Conf. Int.


---

<!-- Página 8 -->

RQ1.3 Arecertaintestsmelltypesmoreassociatedwiththe change- anddefect-pronenessoftestcode?

The nalstepoftherstresearchquestioninvestigates the association tochange-anddefect-pronenessofdifferenttest smell types.Figure5showstwoboxplotsforeachtype, depicting itschange-anddefect-proneness.Whenanalyzing the change-proneness,weobservethatalmostallthetest smells haveasimilartrendandindeedthemagnitudeof their differencesisnegligible,asreportedbyCohend . The only exceptionregardsthe Indirect testingsmell: whilethe median change-pronenessissimilartoothersmells,itsbox plot showsseveraloutliersgoingupto55changes.Inthis case, themagnitudeofthedifferences withalltheothersmell types ismedium.Thisresultisduetothecharacteristicsof the smell.Bydenition,anIndirect testingsmell ispresent when amethodperformstestsonotherobjectse.g.( because of externalreferencesintheproductioncodetested)[74]: Fig. as aconsequence,itnaturallytriggersmorechangessincetypes developers may need to modify the test code more often due to changes occurring in the exercised external production classes. code. Atthesametime,Figure3showsthatthehighertheIn thecaseofdefect-pronenessthediscussionissimilar. number oftestsmells,themoredispersedthedistributionofIndeed, the number of defects affecting the different test smell changes is,thusindicatingthattestcasesaffectedbymoretypes issimilar:eventhoughthedifferencesbetweenthem e   16design problems tend to be changed more often by developers.are statistically signicant (-value <2), they are mostly This observationissupportedbytheresultsofthestatisticalnegligible. However, wecanseesomeexceptions,alsointhis tests, wherewefoundthatthedifferencebetweenallgroupscase. Theboxplotsshowthatthedistributionof`Indirect e   16was statisticallysignicant( value <2), withaTesting',`EagerTest' and`Assertion Roulette'smellsslightlyNumber of bugs negligible effectsizebetweentherst5groupsd(0 : 2 )differ fromtheothers,andindeedthesearethesmellshaving and amediumonebetweentherst5andthelast2groupsthe highestnumberofoutliers.Thisresultisduetothefact ( 0 : 5  d  0:8).that thesetestsmellstendtotestmorethanrequired[74] ( i.e. , atestmethodsufferingfrom`IndirectTesting' exercisesWhen consideringdefect-pronenessinFigure4,wenotice60 other objectsindirectly,an`EagerTest'testmethodchecksthat testmethodshavinguptofourtestsmellsdonotshow several methods of the object to be tested, while an `Assertionsignicant differences with respect to methods affected by ve Roulette' contains several assertions checking different behav-or sixdesignaws.Indeed,themedianofthedistributionis ior of the exercised production code). Their nature makes themalmost identicalinallthegroups,andeventhoughthedif-Number of changes intrinsically morecomplextounderstand[7],likelyleadingference isconsideredstatisticallysignicantbytheWilcoxon developers tobemorepronetointroducefaults.rank sumtest,ithasasmalleffect sized <(0 : 2 ). Thus,these ndings suggestthattheco-occurrenceofmoretestsmellsAssertion RouletteEager TestIndirect TestingMystery GuestSensitive Equality Smell Typeis notdirectlyassociatedwithhigherdefect-proneness;we**Finding 3. Test methods**affectedby`Indirect Testing', hypothesize thattheyareinsteadaco-existingphenomenon,40`Eager Test', and `Assertion Roulette' are more change similarly towhatPalombaet al.reported forcodesmellsinand defectpronethanthoseaffectedbyothersmells. production code[50].

V.RQ2RESULTS : TESTS MELLSP RODUCTIONC ODEIn the context of this research question, we controlled for the size ofthetestmethodandthenumberofitschanges,ndingThis sectiondescribestheresultstooursecondresearch that thesefactorsarenotassociatedwiththeinvestigatedquestion. outcome. Weincludeareportofthisadditionalanalysisin RQ2.1 Are testsmellsassociatedwiththedefect-proneness ofour on-lineappendix[14]. the testedproductioncode? 20 Figure 6 reports the RR that a smelly test case is exercising a Relation with maintainability more defect-proneproductionmethod(label`Overall'),along**Finding 2. Test**methodsaffectedbymoresmellsare with the RR obtained when considering size as a control factor.associated withaslightlyhigherchange-proneness In therstplace,Figure6showsthatsmellytestshaveathan methodswithlesssmells.Conversely,theco- higher likelihoodtotestdefectivecodethannon-smellytestspresence ofmoretestsmellsinatestmethodisnot ( i.e. , theRR=1.71statesthatproductioncodeexecutedbyassociated withhigherdefect-proneness. smelly testshas71%higherchancesofbeingdefectivethan

0


---

<!-- Página 9 -->

# 1

## 2.17 size

## average overall

## small

### 1.52-1.60

Fig. testedvs. non-smelly< 0 : 0001.

Fig.

results achievedsofar:indeed,our**RQ2.1**meant tobea coarse-grained investigationaimedatunderstandingwhether the presenceofdesignawsintestcodemightsomehowbe associated with thedefectiveness of productioncode. Thus,in this researchquestionwedidnotfocusonthereasonsbehind the relationship,i.e. , ifitholdsbecausetheproductioncode is ofpoorquality(thusdifculttotest)orbecausethetests are ofpoorquality(thustheydonotcaptureenoughdefects). Our**RQ2.3**makes arststepinprovidingadditionalinsights on sucharelationship.

Fig.vstestsnon- smelly**Finding 4. Production**codethatisexercisedbytest

### 10.0

code affectedbytestsmellsismoredefect-prone, also production codeexecutedbynon-smellytests).Zoominginwhen controllingforsize. on thisresult,Figure7depictstheboxplotsreportingthe distribution ofthenumberofproductioncodebugs,when Number of bugs in the production methods RQ2.2 Istheco-occurrenceoftestsmellassociatedwiththeexercised bysmellytestmethodsvs.non-smellyones.The defect-proneness ofthetestedproductioncode?difference betweenthetwodistributionsisstatisticallysignif- e   16icant (p-value <2 : 2) withalargeeffect sized = 1:40).

### 10

Figure 8presentstheresultsconcerningtheassociationof Number of bugs

### 7.5

The results still hold when controlling for size: Size does nottest smellco-occurrencestothedefectiveness oftheexercised impact theRRconcerningthedefect-pronenessofproductioncode.Inthiscase,theofproduc- code exercisedbysmellytestsvs.non-smellyones,actually,tion code remains almost constant among the different groups, as showninthepreviousRQ,itmakesitworst.Forinstance,meaning thathavingmoredesignissuesintestcodeisnot methods havingalargenumberoflinesofcodehaveanassociated withahigherofdefectsinproduction. RR = 2:17. Two mainfactorscanexplainthisresult:Onthe This resultledtotwomainobservations:asobservedin one hand,wesupposethatalargesizeofthetestimplies**RQ2.1, test**smellsarerelatedtothedefect-pronenessofType

### 5.0

a largevolumeoftheproductioncode,andourresearchthe exercisedbutdonotfullyexplainthis community widelyrecognizedsizeasavalidproxymeasurephenomenon. Secondly,whilethespecicnumberoftest for softwarequality[35];ontheotherhand,ourresultssmells isnotassociatedwiththedefectivenessofproduction

### 5

corroborate previous ndingsreportedbyPalombaet al.[50],code, theoverallpresenceoftestsmellsis.Itisreasonable who showedthatlargemethodse.g.(, theonesaffectedbyato thinkthatsomespecictest smellscouldcontributemore Long Methodcode smell[23])arestronglyassociatedwithto thefoundassociationtodefect-proneness;thisreasoning

### 2.5

the defect-pronenessofproductioncode.represented theinputfor RQ2.3. Thus, from our analysis we have empirical evidence that theIn this research question, we controlled the ndings for size presence oftestsmellscontributestotheexplanationoftheand numberofchanges,ndingthatnoneoftheminuence Weincludeareportofthisadditionalanalysisdefect-proneness ofproductioncode.Givenourexperimentalthe outcome. setting, wecannotspeculateonthemotivationsbehindthein ouron-lineappendix[14].

### 0

### 0.0

## large

### Non-smelly

### Smelly

### 0

### 1

### 2

### 3

### 4

### 5

### 6

Number of test smells

### Conf. Int.


---

<!-- Página 10 -->

**Finding 6. `Indirect**Testing'and`EagerTest'smells are associatedwithhigherdefect-pronenessinthe exercisedproductioncode.Alikelymotivationisthe lack of focus of the tests on the target production code.

VI. CONCLUSION Automated testing is nowadays considered to be an essential process forimprovingthequalityofsoftwaresystems[12], [47]. Unfortunately,pastliteratureshowedthattestcodecan often beoflowqualityandmaycontaindesignaws,also known as test smells [7], [73], [74]. In this paper, we presented an investigationontherelationbetweensixtestsmelltypes and testcodechange/defectpronenessonadatasetofmore than amilliontestcases.Furthermore,wedelvedintothe relation betweensmellytestsanddefect-pronenessofthe exercised productioncode. The resultsweobtainedprovideevidencetowardseveral ndings, includingthefollowingtwolessons:Fig. **Lesson 1.**Testsmells and their relation with test code quality. Corroborating what van Deursenet al.[74] conjectured in their **Finding 5. The**co-occurrence ofmore testsmellsina study,webringempiricalevidencethattestsmellsarenega- test caseisnotstrongly associatedwithhigherdefect- tively associatedwithtestcodequality. Specically, wefound proneness oftheexercised productioncode. that asmellytesthasan81%higherriskofbeingdefective than anon-smellytest.Similarly,theriskofbeingchange- prone is47%higherintestsaffectedbysmells.Thisresult is complementarytothendingsbyBavotaet al.[7], whoRQ2.3 Arecertaintestsmelltypesmoreassociatedwiththe found thattestsmellscanhave anegative impactonprogramdefect-proneness ofproductioncode? comprehension duringmaintenanceactivities.Moreover,we Figure 9depictstheboxplotsreportingtheassociationof Number of bugs in the production methodsfound that test methods with more, co-occurring smells tend to different test smell types to the defect-proneness of productionbe morechange-pronethanmethodshavingfewersmellsand code. Weobservedthatthe`IndirectTesting'and`Eagerthat `IndirectTesting', `EagerTest', and`Assertion Roulette' Assertion RouletteEager Test relatedIndirect TestingSensitive Equality codeTest'smellsaretotheproductionbeingmoreare thoseassociatedwiththemostchange-pronetestcode.Smell Typedefect-prone withrespecttotheothertestsmelltypes.The**Lesson 2.**Testsmellsandtheirrelation withsoftware quality. differences observed between the `Indirect testing' and `EagerWith ourstudy,weprovidedempiricalevidencethatthe Test'andtheotherdistributionsareallstatisticallysignicantpresence ofdesignawsintestcodeisassociatedwiththe e   1610.0( p   value <2) with medium effect size, while we founddefect-proneness oftheexercised productioncode;indeedthe the othersmellstobenotstatisticallyassociatedwithmoreproduction codeis71%morelikelytocontaindefectswhen production codedefect-proneness.tested bysmellytests.`IndirectTesting' and`EagerTests' are As alsoexplainedinthecontextof**RQ1.3, the**`Indirectrelated toahigherdefect-pronenessinproductioncode. Testing'and`EagerTest' smellsleadtotestcasesthatare(i)This paper provides initial evidence on the relation between less cohesive and(ii)poorlyfocusedonthetargetproduction7.5test smellsandbothchange/defectpronenessoftestcodeand code [74].Theformerimpliesthetestingofotherobjectsdefect-proneness ofexercisedproductioncode.Assuch,it indirectly,thelatterchecksseveralproductionmethodsofrepresents acalltoarmstoresearchersandtoolvendors.We the classundertest.Thelack offocusof suchsmellsmaycall uponresearchersandtool vendorstodeveloppractically explain whythecorrespondingproductioncodeisassociatedautomatic test smell detection tools. We call upon the research with defect-proneness: It seems reasonable to consider that thecommunity tofurtherinvestigatetheinterplaybetweentest5.0greedynature of these two smells makes them less able to nddesign qualityandtheeffectivenessoftestcodeindetecting defects intheexercisedproductioncode.defects. From a practical point of view, our results provide evidence VII. ACKNOWLEDGMENTthat developersshouldcarefullymonitortestandproduction D. Spadinigratefullyacknowledges thesupportoftheprojectcode involvedwithIndirect TestingandEager Test. Infact, SENECA -EUMSCA-ITN-2014-EIDno.642954.A.Bac-these arethesmellsthatnotonlyarerelatedtomorechange-2.5 chelli andF.Palombagratefullyacknowledgethesupportand defect-pronetestcode,butalsotomore of theSwissNationalScienceFoundationthroughtheSNFproduction code. Project No.PP00P2170529.

0.0


---

<!-- Página 11 -->

R EFERENCESConference, pages 331, [1][26] studyforProceedings programProceedingsof, Conference, CSMRpages pages[27] [2]maintainability.Quality 2012.nology,, [3]3039. of[28] Proceedings, pagesSizes: 3336.Non-normalityAmerican [4]Research, nov andIEEE[29] Software, 40(11):11001125,and [5]Modern,assurance. IEEE, 39(6):757773, volumeJune [6][30]ehGueneuc, experimental´studyEcole refactoring.Journal, 107:114,Polytechniqueeal,, 2009. [7][31]ehGueneuc. testEmpiricalof Engineering,20(4):10521094,16th [8]Test. Addison-Wesley16, pages Publishing2009. [9][32]eh eneuc, A.exploratory behavior.IEEE. Tofault-proneness.Empirical, 17(3):243275, [10][33]eh eneuc, andProceedingsapproachProceedings thethe, pages (ESEC/FSE),pagesHong [11][34] fromProceedingschanges:IEEE, on, pages34(2):181196, [12][35] dreams.2007, pagesandIEEE, 12(4):5262, Computer[36]Object-Oriented [13]Software parisonProceedingsObject-Oriented. Springer, of, pages[37] 5362.ratio:Proceedings [14]ACM [15]FoundationsSystems,PODS Empirical. Springer[38] [16]error service.Proceedings,Journal, pages pages[39] [17]ofNinth Journal, 8(3):185197,workshop [18]6th, IWPSE com/?RefactoringTestCode.USA, [19][40] Hassan.ofProceedings identifyingIEEESymposium, pages Engineering,43(7):641657,ACM, [20][41] awsProceedingsdesign20th Conference(ICSM, pages July, pagesIEEE [21][42]xUnit. Addison logisticBMC, 12(1):14,Wesley, [22][43]eh eneuc, databasemethod Maintenance,IEEE, 36(1):2036, on , pages[44] [23]Proceedings ImprovingXtemp01,pagesWCRE'01,, page [24][45] andSciencethe Programming, 102(0):44programSoftware [25] Evolution,pages of2013


---

<!-- Página 12 -->

[46][65] thProcedures.Technometrics, 46(3):369370,smell11 International. IEEE[66] Press,tifyingSoftware Engineering,, 39(8):11441156,[47]The, volume [67][48] xes?Proceedingsharmful? Software. ACM,three26th [68]Software testing.SoftwareRomania,pages Proceedings., pages[49]eheneuc. [69]signatures thparticipationR.Proceedings14Conference Qt,Empirical,on. IEEE 22(2):768817,Press, [70][50] refactoringIEEE,A. 35(3):347367,codeEmpirical [71]Engineering,pages and[51] smells.Proceedingsthey on, ASEsmells.In 2016.Maintenance, pages [72][52] andA. whetherTransactionsSoftware, 41(5):462489, (TSE),43(11):10631088,[53] [73]On Code.empiricalProceedings [74]Search-Based, pages code.Proceedings[54] Programming,A2016 pagesInternational, [75]10, between[55] andThe pagesstructuralIEEE, 2017. [76][56] detectionxingProceedings andIEEE, 33(12):800Software, pages 817,[57] [77]detectionProceedings methods.Journal, 39(6):269,the [78](ICSME).IEEE, maintainabilityProc.[58] (ICSM),pagesStudy2017 [79]IEEE/ACM relations(ICPC),pages Conf., pages[59] [80]usingEuropean relationsMaintenance, pages comparativeProceedings[60] Conference, pagesRecovering 121130.Journal, 88:147168, [81][61] Mininginformation8th &2008Conference, pages Verication,, volume223232. [82][62] Studyingchange-proneSoftware industrialEmpirical27th, pages Software, 16(3):325364,[63] [83]study correctingJama,tional 280(19):16901691,(SANER),pages [84][64] effectrelativeInternational, 53(3):165167, andIEEE,2008. 35(5):607623,


---

