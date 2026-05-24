<!-- Página 1 -->

### On the

### Distribution

### of

### Simple

### Stupid

### Bugs

### in

### Unit

### Test Files:

### An

### Exploratory

### Study

Anthony PerumaChristian D.Newman Rochester InstituteofTechnologyof Rochester, NewYork, USANewUSA [axp6201@rit.edu](mailto:axp6201@rit.edu)[cnewman@se.rit.edu](mailto:cnewman@se.rit.edu)

**AbstractA key**aspectofensuringthequalityofasoftware **system is**thepracticeofunittesting.Throughunittests,devel- **opers verify**thecorrectnessofproductionsourcecode,thereby **verifying the**system'sintendedbehaviorundertest.However, **unit test**codeissubjecttoissues,rangingfrom bugs inthecode **to poor test case design (i.e., test smells). In this study, we compare** **and contrast**theoccurrencesofatypeofsingle-statement-bug- **x known**assimplestupidbugs(SStuBs)intestandnon- **test (i.e.,**production)lesinpopularopen-sourceJavaMaven **projects. Our**resultsshowthatSStuBsoccurmorefrequently **in non-test**lesthanintestles,withmostx-relatedcode **associated with**assertionstatementsintestles.Further,most **test les**exhibitingSStuBsalsoexhibittestsmells.Weenvision **our ndings**enablingtoolvendorstobettersupportdevelopers Fig. 1: Overview of our data extraction and collection process.**in improving**themaintenanceoftestsuites. SStuBs torepresentthefunctionalqualityaspectsofthetest I. INTRODUCTIONsuite, and test smells for the non-functional quality aspects. As an exploratory study, we aim to have a better understanding ofUnit testing is an essential strategy employed by developers this problem and determine the feasibility of further research into ensurethequalityoftheirsoftwaresystem.Underthis this area. Our ndings provide developers with insight to betterstrategy,write code (i.e., test cases) that veries the design, implement,andmaintaintestsuites.Additionally, ourbehavior ofindividualunitsofworkofthesystemundertest ndings canimprovethesupportprovidedbyrefactoringand[1]. However, the test code written by developers is vulnerable other codequalitytools.Hence,ourstudyaimsatansweringto issues such as bugs (i.e., functional defects) and smells the followingresearchquestions(RQs):bad programming practices), which impact not only the quality of thesystembutalsothesystem's maintenance;specically,**RQ****: To**whatextentdoSStuBsoccurintestles1 the maintenanceoftestcases[2].**as they**doinnon-testles?This RQcomparesthe However,correcting these software issues might not alwaysoccurrence ofSStuBsintestlesandnon-testles.We be acomplicatedtask,withsomebugsbeingmucheasierexamine thevolumeandtypesofSStuBsoccurringin to correctthanothers;oftenrequiringachangetoasingleles alongwiththedevelopersresponsibleforxing statement. ThesearesometimesreferredtoassimplestupidSStuBs inthetwogroupsofletypes. bugs (SStuBs)[3].Whilethereexiststudiesthatinvestigate **RQ****: To**whatextentdotestlescontainingSStuB2 defects insourcecode,thesestudiesonprogramrepair[4]do **xes also**exhibittestsmells?This RQexploresthe not differentiatedefectsoccurringintestandnon-testles, existence oftestsmellsinlescontainingxesfor nor dothesestudiesfocusexclusivelyonSStuB-likedefects. SStuBs. ThisRQaimstounderstandifSStuBscanbe These studiesmostlyfocusonatestcase's abilitytoidentify arXiv:2103.09388v1 [cs.SE] 17 Mar 2021an indicatorforthepresenceoftestsmellsinthecode. defects inthesystemundertest[5][7].Furthermore,studies that focusonthequalityoftestcasesontestsmellsII. DATA EXTRACTIONC OLLECTION [8] exhibitedbytestlessuchasinvestigatingtheakiness Figure 1showsageneraloverviewofourdatacollection(i.e., non-deterministicoutcome)oftestcases[9],[10].In and extraction process. In the below subsections, we elaboratethis paper,wefocusonSStuBsintestles.Weexplore, on theactivitiesinvolvedintheprocess.Thedatasetwecompare, andcontrasttheexistenceofSStuBsintestles utilize/generate isavailableat[12]forreplication/extension.against non-testles.Furthermore,ourstudyalsolooksatthe co-occurrence betweenSStuBsandtestsmells. A. SourceDataset A. Goal&Research QuestionsOur studyutilizestheManySStuBs4Jdataset,whichcon- tains bug-xing details of SStuBs extracted from popular open-The goalofthisstudyistoexplorethequalityoftest source Java Maven projects[3].Containedwithinthisdatasetsuites fromafunctionalandnon-functionalperspective,and is therelativepathofthelecontainingthex,thecommitthe relationshipbetweentheseviewpoints.Hence,weutilize

## M

## a n y S

## S

## t

## u B

## s 4 J

## C

## l

## o n e

## T e s t

##

## F i

## l

## e

## D

## a t

## a s e t

##

## (

## M

## a v e n

## R

## e p o si

## t

## o r

## i

## e s

## D

## e t

## e c t

## i

## o n

## P

## r

## o j

## e c t

## s )

## T e s t

##

## S

## m

## e l

## l

##

## R

## e s e ar

## c h

## Q

## u e s t

## i

## o n

## D

## e t

## e c t

## i

## o n

## A

## n a l

## y s i

## s


---

<!-- Página 2 -->

TABLEI:SummaryofthetestsmelldetectionrulesutilizedTSbyD ETECT[11].

**Test**

Assertion Conditional Constructor Duplicate Empty Exception Generalmethod Ignored@Ignoretheannotation Magic Mystery RedundantprintorprintlnorprintforwritemethodSystemclass Redundantislimitedto16smelltypes.Detailsabouttheid associatedwiththex,andthetypeofSStuBxedbythe Resourceclassexists(), isFile()ornotExists()methods types, alongwithexamples,areavailablein[14].developer,amongotherdetails. SensitivetoString()method SleepymethodB. RepositoryCloning&FileExtractionE. ResearchQuestionAnalysis Unknown@Test(expected)annotation In this stage of the process, we clone the Maven repositoriesToanswerourresearchquestions,weexecuteaseries that containbug-xingcommitsforSStuBs.Thepurposeofof databasequeriesandcustomscriptsonthemineddata. this activityistwofold.First,weextractmetadataassociatedAdditionally,whereapplicable,weprovideexamplesfrom with the commit, such as the author (i.e., developer) of the x.our datasettosupplementourndings.Whenreportingon Second, weextractthesourcecodelesassociatedwitheachour researchquestions,werstprovidedetailsaboutthe SStuB-xing commit.TheoriginalMavendatasetcontainsexperiment'smethodologybeforepresentingthendings. 10,231 SStuB-xinginstancesdistributedover84projects. III. EXPERIMENTALR ESULTSHowever,atthetimeofcloningtheserepositories,only83of the repositorieswerepubliclyavailable.Hence,inthisstudy,A. RQ: To whatextentdoSStuBsoccurintestlesasthey1 we analyze10,225SStuB-xinginstances.do innon-testles?

**Methodology. In this**RQ,wegroupthelescontainingxesC. TestFileDetection for SStuBsintotwogroupstestlesandnon-testles.The In thisstudy,weonlyconsiderprojectsthatutilizeJUnit test les represent JUnit based unit testing les, while the non- [13] asthetestingframeworksincepriorunitbased test les represent the set of production les. We examine and research has frequently focused on JUnit (e.g., test smells [8]). compare detailssuchasthedistributionofSStuBsbetween JUnit recommendsthatdeveloperseitherprependorappend the twogroups,thedevelopersresponsibleforapplyingthe the term`Test' tothenameoftheproductionletobetested x, andtheclusteringofletypesinabug-xingcommit. (i.e., Test*.java or*Test.java). However, thismechanismcan **Results.First, we look at the projects containing SStuBs xing**lead tofalsepositives.Forourstudy, weutilizetheapproach commits. Fromthesetof83projectsinthedataset,57(by [14] and [11] to detect test les. In this approach, we utilize 68.67%) projectscontainSStuBsoccurringinbothtestandJavaParser[15] to build an abstract syntax tree for each source non-test les,while25(30.12%) projectscontainSStuBsle. We markaleasaunittestleifthelecontainsJUnit occurring inonlynon-testles,andonlyoneprojectcontainsimport statements(i.e., org.junit.orjunit.) anda** SStuBs occurringinonlytestles.Ournextexaminationtest method.Tobeatestmethod,themethodshouldhave shows thatdevelopersapplySStuBxesto5,587Javales.an annotationcalled@Test(JUnit 4),orthemethodname From thisset,1,066(19.08%) aretestlesand4,521(should startwith`test'(JUnit3). 80.92%) arenon-testles.Moreover,fromatotalof10,225 D. TestSmellDetectioninstances of SStuB xes, 1,946( 19.03%) of these were intestles,while8,279( 80.97%) wereinnon-testFor thedetectionoftestsmellsweutilizeTS DETECT[11], les. Furthermore, we observe, on average, 2.20 SStuBs occuran open-sourcetestsmellsdetectiontool.TS DETECTdetects in testles,and2.37occurinnon-testles.19 testsmelltypesandhasbeenutilizedinmultiplestudies analysisfocusesonSStuBcategories.Intotal,[14], [16][20].ProvidedinTableIisasummaryofthe Our next there are16SStuBcategories,thedetailsofwhichareavail-detection rulesforeachsmelltype.However,forthisstudy, [3].InTableII,weprovidethetopvefrequentlywe ignorethe Default Testsmell asthisisexclusive toable at Android applications.WealsoignorethesmellsEager Testoccurring SStuB categories in test and non-test les. From this table, we observe that even though the categories are the sameandLazy Testas thesesmellsrequiretheclassundertestto for bothletypes,theratioofoccurrencesofthesecategoriesbe known;whichisnotknownforthisdataset.Hence,our


---

<!-- Página 3 -->

TABLEII:Top veSStuBcategoriesin(non-)testles.differs betweenletypes.Further,wealsoobservethatthe **SStuB**categoriesChange Numeric LiteralandModier occur at differentpositionsrelativetotheothercategories.TheseTest Changetop vecategoriescontributeto88.23%and81.83%ofthe Change complete setofoccurrencesintestandnon-testletypes,Wrong respectively.Additionally, we also observe that while the non-Same Changetest lescontaininstancesofall16categories,thetestles Non-Test do notexhibitthe Change Operandcategory.Ingeneral,weChange observe 314 (16.13%) SStuB instances in test les are asso-Change Wrongciated with assertion statements. Examining the code statement Same containing thexforChange NumericLiteralin testles,weChange observe that 112 (20.4%) of the instances occur with an as- volume ofSStuBsoccurringinindividualtestandnon-testsertion statement(e.g.,assertEquals(2,map.size())! les areverysimilar(2 instances).WealsoobservethatassertEquals(3,map.size())[21]). Furthermore, 116 ( the majorityofdevelopersworkonxingSStuBsinnon-test21.13%) instancesarerelatedtonumericvaluesassoci- les thantestles.Additionally,ThetopvepopularSStuBated withtime-relatedidentiers(e.g.,timeout=2000! categories for test and non-test les are the same. However, thetimeout=1000[22]). Incontrast,lescontainve ratio ofoccurrencesofthesecategoriesdiffers.Furthermore,instances ofSStuBsinassertionstatementsand31time- the codeassociatedwithSStuBxesdiffersbetweentestandrelated SStuBs. For cases under theChange Modiercategory, non-test les;assertionstatementsintestlesarefrequentlywe observethatdeveloperseitherremoveorincludethe updated duetoSStuBxes.statickeyword withaclassormethodintestles.We observe 14casesfallingundertheSame FunctionMoreArgs B. RQ: TowhatextentdotestlescontainingSStuBxes2category arerelatedtoassertionmethodsintestles.In also exhibittestsmells? most ofthesecases,developersincludeatextualmessage **Methodology.**SStuBs representthefunctionalqualityofarelated totheassertioncondition'sfailure(e.g.,[23]).Ad- system. Incontrast,testsmellsrepresentthenon-functionalditionally,wealsoencounterinstances,intestles,where quality ofasystem,bothofwhichareimportanttothethe methodsthatareupdatedarerelatedtomocking;ei- maintenance ofthesystem'stestsuite.InthisRQ,welookther API'srelatedtoMockitoorcustommethodsthatac- at theexistenceoftestsmellsintestlesexhibitingSStuBs.cept mockedobjectsasarguments(e.g.,Mockito.any()! Additionally,we also investigate if the xing of SStuBs causesMockito.any(ProducerRecord.class)[24]). a change in the number of test smell types exhibited by the le. Our subsequent analysis is on the grouping of test and non- Tothisextent,weutilizeTS DETECTto analyzethetestles test lesinasinglecommit.SinceSStuBscanoccurinboth containing SStuBxesandthepriorversion(i.e.,commit)of test and non-test les of a project, we are interested in knowing the lefortheexistenceoftestsmells. whether developers make xes (i.e., commit) for both le types **Results.**From thesetof1,066testlescontainingSStuBin unison or prioritize xing one le type over another. Hence, xes, 1,064lesshowthepresenceoftestsmells,witheachfor this analysis, we only focus on the 57 projects that contain le exhibiting, on average, 15.41 smell types. Examining eachSStuBs in test and non-test les. Our analysis shows that only smell type, we observe that each of the 16types occur inone projectmeetsthiscriterion.Furthermore,thishad over 80% of the test les exhibiting SStuB xes. Furthermore,only onecommitoperationthatcontainedatestandnon-test the smelltypesAssertion RouletteandException Handlingle. Thisphenomenonshowsthatdevelopersprefertotreat occur inallthetestles.IntermsofSStuBcategories,weSStuBs inisolation,mostlikely sothatthey cankeep trackof observe thatChange NumericLiteralandIdentierthe changesandrevertthechangeifnecessary. Usedare thetoptwocategoriesoccurringin375and356Finally,weexaminethedistributionofdevelopersthatx smelly testleinstances,respectively.ThisisincontrasttoSStuBs. Hence,weperformthisanalysisonthesetof57 the popularityresultsshowninTable II.projects containingtestandnon-testles.Todetectunique Next, welookattheco-occurrenceofeachSStuBcategorydevelopers, we utilize the same approach as [25]. The with eachsmelltype.InTableIIIwepresentthenumberofutilizes theSStuBxingcommitauthor'semailtoidentify instances (i.e., test les) where a SStuB bug category co-occursunique developersforaproject.Intotal,weencounter1,116 with atestsmell.Duetospaceconstraints,weonlypresentunique bugxingdevelopers.Fromthisset,84 ( the topveoccurringSStuBbugcategories.Ouranalysisdevelopers areresponsibleforxingSStuBsoccurringonly shows that the smellsAssertion Roulette, Exception Handling,in testles,while789 ( 70.70%) xSStuBsoccurringonly andMagic NumberTest are thethreesmelltypesthatmostin non-testles.DevelopersthatxSStuBsinbothtestand frequently co-occur with each of the SStuB categories. In con-non-test lesaccountfor243 ( 21.77%). trast, the least co-occurring smell typeRedundantisAssertion. Finally,welookattheversionofthetestlethedeveloper**Summary.**This RQshowsthatnon-testlescontainmore modies just before the commit containing the SStuB x. OurSStuBs thantestles.Additionally,weobservethatthe


---

<!-- Página 4 -->

TABLEIII:Co-occurrencebetweenthetopvefrequentlyoccurringSStuBbugcategoriesandtestsmelltypes.

objective istodetermineifthesmellcountdecreaseswhentheChange NumericLiteralSStuB category.Thefrequent the developerxesaSStuB.Ourndingsshowthatmostoccurrence ofissuesrelatedtoassertionstatementsshould SStuB xesdonotresultinadecreaseinsmellcount.Morenot besurprisingasassertsareoneofthemostfundamental specically,853 (80.17%) instances do not show a change inparts ofatestcase.Furthermore,in**RQ**, weobservethe2 smell count, while 182(17.11%) instances show a decreasefrequent occurrenceoftheAssertion Roulette; which and 29(2.73%) instancesshow anincrease.Lookingatthecorroborates withndingsfrompriortestsmellstudies[2], instances thatshowadecrease,weobservethat,onaverage,[9]. Thesendingsshowthattheoccurrenceofaspecic 3.22, smelltypesareremovedbetweenthetwoversionsofSStuB categoryinthetestsuiteindicatestheoccurrence the le.WeobservethatthesmellsAssertion Rouletteandof specictestinthesamele,andtherebyhelp Exception Handlingdo notshowareduction,whilethesmelldevelopers in addressing multiple issues in the code that would Redundant Assertionis apopularsmellthatreduces.otherwise bemissed.AsimilarndingreportedbySpadiniet al. [9]showsanassociationbetweensmellytestsanddefect-**Summary.**TestlesexhibitingSStuBsareverylikelyto proneness oftheproductioncodeundertest.Forexample,incontain testsmells,withtheAssertion RouletteandException our dataset,weobserveinstanceswheretheChange NumericHandlingsmell typesfrequentlyoccurringinsuchles.Ad- LiteralSStuB categoryoccursduetochangesmadetotheditionally,testlesthatexhibitcertaintypesofSStuBs,such Thread.sleep()value, whichisalsoanindicatoroftheasChange NumericLiteral, alsoexhibit testsmells.However, Sleepy Testsmell (e.g.,[28]).Thisspeciccanleadtodevelopers rarelyxthesesmellswhenaddressingSStuBs. unexpected resultsastheprocessingtimeforataskdiffers when executedinvariousenvironmentsandcongurations;IV. DISCUSSION most likely, the developer experienced this situation due to the As an exploratory study, our research aims to understand the sleep duration change. Lastly, our ndings on the non-removal extent to which SStuBs occur in test les and their relationship of smellsalsocorroboratewithresearchbyTufano etal.[29]. to testsmellsoastoprovidedirectiontoresearchareasthat Once more,allourndingscanhelptool/IDEvendorsbetter support developersindesigningandmaintainingtestsuites. equip their devices to better support developers to improve the From**RQ**, weobservethatSStuBstendtooccurmore1functional andnon-functionalaspectsoftheirtestsuites. frequently in non-test les than test les. However, this should not signifythattestlesareofbetterqualitythannon-testV.THREATSVALIDITY les; thismightbeasituationwheredevelopersnotEven though the projects in our dataset are some of the most always beaddressingthesetypesofdefectsintestsuites.Itpopular open-sourceMaven-basedJavasystems,theresults is interestingtonotethatdevelopersusuallyaddresstestandmay notgeneralizetosystemswritteninotherlanguages. non-test SStuBs in separate commits. This is interesting since aFurthermore, weconneouranalysistotheJUnittesting change incodeinanon-testlewouldrequireanappropriateframework. However,priorunittesting-basedresearchhas change tothetestcodetoensurethatthetestcasepassesfrequently focusedonJUnit[8].Ourselectionof D ETECT [26]. Committinganon-testchangeindependentlyofatestis duetoitsabilitytodetectmultiplesmelltypesandbetter change wouldmostusuallycausethetestcasetofailinandetection performance [20]. Finally, even though non-test les automated build/test environment. Hence, it is most likely thathave more SStuBs than test les, the per-le rate ofof such systemseitherdonotuseanautomatedbuildsystemortest and non-test les are very similar. This aspect is interesting lack sufcient code coverage. Additionally, our observation ofand requires more in-depth analysis, such as the possibility that most developersworkingonxingnon-testSStuBsovertestSStuBs are not found at the same rate in test and non-test les. SStuBs canbeafurtherindicatorthatdevelopersprioritize VI. CONCLUSION& F UTUREW ORK**SStuB****Assertion****Conditional****Constructor****Empty****Exception****General****Mystery****Redundant****Sensitive****Sleepy****Duplicate****Unknown****Ignored****Resource****Magic**non-test les over test les; and might need to adhere to a test-**Category****Roulette****Test****Initialization****Test****Handling****FixtureGuest****Print****Assertion****Equality****Test****Assert****Test****Test****Optimism****Number** drivendevelopmentapproach[27].However,furtherIn thisstudy,weexploretheoccurrenceSStuBsintest**Change****Literal**375344researchof **Change**356 **Wrong**192into thisareaiswarrantedtounderstandtherationaleastoandtheirrelationtotestsmells.We observethatSStuBs **Same**110 **Change**95why developerstreattestlesdifferentlyfromnon-testles.occur morefrequentlyinlesthantestlesandthat **Other**164 Additionally,there needs to be research into tools that supportmost ofthexrelatedcodediffersbetweentestandnon-test developers withautomaticallynding/recommendingchangesles. Finally,weshowthattestlesexhibitingSStuBsalso to testlesbasedonSStuBxesappliedtonon-testles.exhibit testsmellsandtendtoco-occurwithspecictypes **RQ**also shows that the code related to SStuB xes tend toSStuBs.Thesendingsshow thatthereisindeedscopefor1 differ between test and non-test les. We observe that the codefuture research in this area, especially around the maintenance of testsuites.Futureworkinthisareaincludesinvestigatingusually associatedwithSStuBxes intestlesarefrequently the akinessoftestsuitesbroughtaboutbySStuBs.associated withassertionstatements,suchasinthecaseof


---

<!-- Página 5 -->

R EFERENCES[21] [https://github.com/spring-projects/spring-boot/commit/0757d24](https://github.com/spring-projects/spring-boot/commit/0757d24). [1]Software[22] tioner's. McGraw-Hillcommit/cb6f6e2. [2][23] empirical7fa8196. on2012[24] on, pp.82bd0ba. [3][25] occur?ProceedingsContextualizing Conference, 2020.andJournal, vol. [4]2020. AIEEE, vol.[26]Hudson. pp.McGraw-Hill [5][27]Test-driven. Addison-Wesley learned2013signature ference, pp.[28] apache/storm/commit/9134320.[6] [29]Do Lucia,study2015 badIEEEInternational, Engineering,vol.pp. [7] An in2017 Conference Track, pp. ¨¨[8]uk, knowledgeJournal, vol. [9] On2018 IEEE (ICSME),pp. [10] Scented automaticallyJournal, vol. [11] and inProceedings Engineering Engineering,(New Computing [12] [13] [14] and androidProceedings Annual Engineering,CASCON [15] [16] gating in2019 for, 2019. [17] chelli,Proceedingsin of, MSR [18]Pro- ceedings Companion, ICSE [19] An applications,Proceedings Conference, ICSEW'20, York, 2020. [20] Hellendoorn, Limitations,2020 Conference, pp. 533,


---

