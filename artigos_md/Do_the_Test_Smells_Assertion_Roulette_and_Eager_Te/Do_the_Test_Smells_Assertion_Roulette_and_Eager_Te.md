<!-- Página 1 -->

# PREPRINT

## Do the

## Test

## Smells

## Assertion Roulette

## and

## Eager Test

## Impact

## Students' Troubleshooting

## and

## Debugging

## Capabilities?

yzWajdiAljedaani, MohamedWiemMkaouer, AnthonyPerumaand StephanieLudi University ofNorthTexas. Emailf wajdi.aljedaani, [Stephanie.Ludi@unt.edug](mailto:Stephanie.Ludi@unt.edug) yRochester InstituteofTechnology. Emailf [mwmvse@rit.edug](mailto:mwmvse@rit.edug) zUniversity ofHawaiiatManoa.Emailf [peruma@hawaii.edug](mailto:peruma@hawaii.edug)

**AbstractTo**ensurethequalityofasoftwaresystem,devel-ranges fromlackofpropertestingdiscipline(i.e.,mistakes/- **opers perform**anactivityknownasunittesting,wheretheycarelessness andnon-removalofdebuggingcode)totesting **write code**(knownastestcases)thatveriestheindividualknowledge gaps[33]. **software units**thatmakeupthesystem.Likeproductioncode, As describedabove,throughaseriesofempiricalstudies**test cases**aresubjecttobadprogrammingpractices,knownas and developerinterviews,theresearchcommunityhasshown**test smells,**thathurtmaintenanceactivities.Anessentialpart **of most**maintenanceactivitiesisprogram comprehension whichthat testsmellsimpactasystem'sinternalquality,thereby **involves**developersreadingthecodetounderstanditsbehaviorimpacting maintenanceactivities.Tofurthervalidatethese **to x**issuesorupdatefeatures.Inthisstudy,weconductandings andexpandthebodyofknowledgeontestsmells, **controlled experiment**with96undergraduatecomputerscience our studyinvestigatestheeffectoftestsmellsoncodecom-**students to**investigatetheimpactoftwocommontypesoftest prehension activities.To thisextent,weconductedasizeable**smells, namely****Assertion Roulette****and****Eager Test, on**astudent's **ability to debug and troubleshoot test case failures. Our ndings**human-based studywithundergraduatestudentsenrolledina **show that**studentstakelongertocorrecterrorsinproductioncomputer scienceprogramatauniversityinNorthAmerica. **code when**smellsarepresentintheirassociatedtestcases,Similar to code smells, there are multiple types of test smells **especially Assertion Roulette. We envision our ndings supporting** dened in published literature [3]. However, as this is a human-**academia in**betterequippingstudentswiththeknowledgeand based studyandinvolvesstudents,examiningeachsmellin**resources in writing and maintaining high-quality test cases. Our** 1**experimental materials**areavailableonlinethe testsmellscatalogisnotfeasibleduetotimeconstraints. **Index TermsTest**smells,unittesting,softwareengineeringTherefore, inthisstudy,wefocusouranalysisononlytwo **education, computer**sciencesoftwaretestingsmell typesAssertion RouletteandEager Test. Wearrived at thesetwosmelltypesbyreviewingmultiplestudies[10], **I. Introduction** [24], [33],[39]andcomparingthedistributionofsmelltypes An essentialactivityinensuringthequalityofasoftwarethat thesestudieshaveincommon;bothofsmelltypes system isunittesting,wheredeveloperswritecodetoverifyfrequently occur in the test suites of open-source Java systems. the behavioroftheimplementedsystem'sproduction(i.e., **A. Motivation**&Goal source) code[35].Byusingunittests,organizationsand While thereexiststudiesthatevaluatedtheimpactoftestproject teamsautomatethediscoveryofawsintheirsystem smells onthecodecomprehensioncapabilitiesofstudents,that would otherwise go unnoticed or consume developer time these studieseitherinvolvedstudentswritingcompletetest[25]. Giventhisinvaluablebenetinimprovingtheoverall cases [8],[9],[13]orevaluatingthetestsuitesfromlarge,quality ofasoftwaresystem,many projectsandorganizations well-established open-sourcesystemswithwhichtheyhavemandate thatdeveloperswriteunittestsaspartoftheir no priorexperience[11].Incontrast,asweelaborateinsoftware developmentprocess[29],includingtheadoptionof arXiv:2303.04234v1 [cs.SE] 7 Mar 2023 Section III,ourworkinvolves studentsexaminingpre-writtena test-drivendevelopmentapproach[12]. test casescorrespondingtosimplisticuseandmakingHowever,aswithproductioncode,testcodeisalsosubject updates totheproduction(i.e.,systemundertest)codetoto badprogrammingpracticesbydevelopers,knownastest correct failing test cases. Hence, to a large extent, we eliminatesmells [41].Likewise,similartocodesmells,testare any inuence placed on the student's cognitive load caused byalso anindicatorofdeeperproblems,suchasbaddesign understanding (or being overwhelmed by) the overall behavioror implementationchoicesinthetestsuite.Priorresearch and technicaldesign/architectureofacomplexandunfamiliarhas shownthattestsmellsnegativelyimpactthesystem's system. Therefore,thendingsfromourstudyaremoremaintainability.Specically,testsmellshavebeenshownto closely alignedwiththeactualimpactoftestsmellsoncodeincrease thechange-anddefect-pronenessofthesystem's comprehension. Furthermore,thisstudyalsoallowsustocodebase [38],increasetheakinessoftestcases[14],and compare our ndings against the work by Bai et al. [7], whichnegativelyimpacttestcodereadabilityandunderstandability states thatAssertion Rouletteshould notbeconsideredabad[41]. Furthermore,developers'injectionofthesetestsmells smell forstudents. 1In thisstudy,ourgoalistodeterminethe extenttowhich[https://wajdialjedaani.github.io/testsmellstd/](https://wajdialjedaani.github.io/testsmellstd/)


---

<!-- Página 2 -->

# PREPRINT

the presence oftestsmellsinthetestsuiteimpactsastudent'sin education,wherewefocusoncurrentapproachesusedto troubleshooting anddebuggingcapabilities. Specically,ourexamine thetestingineducation;Students'programmingand work compares the effect that smelly and non-smelly test suitestesting activities, which focus particularly on unitinside have onstudentswhentaskedwithxingfailingtestcasesby classroom.Finally,TableIpresentsasummaryofthe only correctingdefectsintheproductioncodeofasystemsystematic analysisstudiesintherelatedwork. they arefamiliarwith.Wetheorizethattestlesexhibiting **1) Software**Testing inEducation test smells cause an increase in code comprehension time than Educators have examined a variety of assessment integrationthose withouttestsmells,resultinginstudentsspendingmore strategies forcomputersciencecourses.Forinstance,sometime onmaintenanceactivities. researchers instructstudentstosubmittheirsoftwaretests**B. Contribution** and solutions[19],[23],whileothersinvolvestudentsin The results of our study show that test smells negatively im-peer testing[36],[22].Fraseretal.[20]proposedaCode pact a student's code comprehension capabilities. Furthermore,Defenders gamethatisutilizedtoengagestudents'activities the Assertion Roulettesmell causes students to take more timein the test suite. Aniche and colleagues [4] conducted a survey to addressissuesintheproductioncodethanEager Testinvolving84rst-yearcomputersciencestudentsregarding smell. Ourstudyhighlightstheneedforacademiatoinvest inthe difculties associatedwithlearningsoftware testing.They and prioritizeteachingstudentsaboutalltypesoftestsmells,also investigatedtheerrorsthatweremadeinthelabwork their harmfulimpactonmaintenanceactivities,andtoolsthatof 230students.Accordingtotheirndings,thereareeight can be used to automatically detect and eliminate these smellsdifferent typesoftypicalerrors.Theseincludetestcoverage, from thetestsuiteofasoftwaresystem.maintainability oftestcode,understandingoftestingprinci- ples, boundarytesting,state-basedassertions,mock**II. Test**SmellDenitions&RelatedWork objects, andtools. This sectionprovides denitionsofthetwo testsmelltypes Previous studieshaveinvestigated boththelevelofquality (i.e.,Assertion RouletteandEager Test) utilizedinourstudy of student-writtentestcode[4],[15],[16],[18]andtheview- and anoverview oftherelatedworkinthisarea. points of students on unit testing [4], [22]. These studies utilize **A. Test**SmellDenitionsseveral metrics,suchasthefrequencyofdefectsidentiedby student-created testcasesandbranchcoverage.ToevaluateAssertion Roulette.The passing/failingofatestcaseisdeter- the incrementaltestingproceduresofsoftwaredevelopmentmined bytheexecutionoftheassertionmethoditcontains. projects, Kazerounietal.[28]developednewmetrics:theThese assertionmethodsallowdeveloperstoincludeanop- balance andsequencingofthetestingeffort.Accordingtotional textualmessageindicatingthereasonforthefailureof an evaluationconductedbyCarverandKraft[15],studentsthe assertion.Thissmelloccurswhenatestmethodcontains in thesenioryearofcomputersciencedonothavethetwo or more assertions without an explanation message. Trou- skills necessary to make good use of test-coverage techniques.bleshooting thefailureofatestcasebecomeschallengingas These experiments were performed in a classroom setting, andthe developerisunawareofthecauseofthefailure. participants weregivengradesfortheirparticipation.Eager Test.This smelloccurswhenatestmethodveries multiple functionalitiesoftheproductioncodebyinvoking**2) Students'**programmingandtestingactivities several productionmethods.Thissmellmakesithardtoun- Several approaches [2], [17] have been developed for assess-derstand the true purpose of the test. Furthermore, it increases ing student-created test suites. Bai et al. [8] studied the impactthe couplingbetweenthetestmethodandproductioncode, of achecklistonthestudentswritingtestcases.Thewhich, inturn,negatively impactsmaintenance. anticipated thattheywoulddevelopJUnitteststocheckthe **B. Related**Workfunctionality ofaprogramthathadbeenimplementedto Several automatedtechniquesandtoolsfordetectingtestevaluate thestudentcompleteness,effectiveness,andmain- smells havebeenpublishedintheliterature[3].Inaddition,tainability.Inrecentwork,BuffardiandAguirre-Ayal[13] researchers haveidentiedacollectionoftestsmells[21],analyzed students'workontestingassignmentstoexamine while othershaveconcentratedontheeffectsoftestsmellstheir adoptionoftestsmells.Theauthorsalsoinvestigated the and removaltechniques[30].Forexample,VanBladelandrelationship betweenthreetypesoftestsmellsandthetest Demeyer suggestedeliminatingtestsmellsinthecontextofaccuracy ofthestudents'work.Baietal.[9]performedan refactoring testcode[40],andVan Deursenetal.highlightedexperimental study to learn how students understand unit test- harmful testsmellsandtechniquestoeliminatethem[41].Inand what obstacles they face when engaging in unit testing. addition, theyofferedconceptualandtechnicalexplanationsBavota etal.[11]performedacontrolexperiment onstudents for evaluatingstudents'activitybyidentifyingtestsmellsinand industrialdevelopersonsixtestsmells.Theyexecute their codeandofferingtestsmell-relatedobservations.Thissoftware comprehensiontasksontestsuiteswithandwithout section highlights several prior studies that particularly shapedtest smellsandmeasureperformanceusingcorrectnessand our methodology.Next,wedividetherelatedworkintotwotime. Participantscannotconductthenecessarymaintenance different aspectsoftestsmellineducation:softwaretestingwhen thistestispresent.Thus,thesignicantly


---

<!-- Página 3 -->

# PREPRINT

TABLEI:Summaryofthesystematicanalysisstudiesinrelatedwork.

createtwovariantsofthesametestsuite:Theaffects it(bachelorstudentsscored48%correctness,whileSuite N), we rst variant (referredtoasSuiteA)hasthesametestinglogicindustrial developersscored42%). Researchers andeducatorscommonlyusetestcase/suiteof SuiteN,butwithtestmethodsinfectedwithassertionthe success ratestoevaluate thequalityofstudent-writtensourceroulettesmell. Similarly,thesecondvariant(referredtoas code [6],[27],[42].Incontrast,students'productivityisSuite E) hasN 'smethodsinfectedwiththeeager test. generally measuredinlinesofcodeperhour[5]orworkThese suitesaredescribedasfollows: session [27].Unfortunately,therehasbeenalackoffocus **Suite N. It**encompasses(N)on-Smellytest cases.Each on theimportanceoftestsmellsintheclassroom.Inastudyproduction methodisassociatedwithoneormultiple similar toours,Baietal.[7]examinedhowthetest methods,testingmultiplescenariosandensuringthe Roulette smell affects students' productivity and conduct whilecoverage of all the method's execution paths. We followed **Study****Year****Purpose****Evaluation****Test****Participant****#**writing code. The authors employed the Bowling Score Keeperthe guidelinesbyXUnit[31].TCD,Students49 project,andthestudentwastaskedwithwritingsystemsJava appto[11]2015UnderstandingExperimentLT,Developers12**Suite A. We**introduced(A)ssertion Roulettesmell into [20]2019EngagingSurveyGameStudents123calculate thescoreofasinglebowlinggameaccordingtoaSuiteN test casesbytestingStudentsmultiplescenarios,forone[13]2021ExploringUnitMA,246 set ofspecicationsand JUnittests.[9]2021DiscoveringSurveyN/AStudents54given productionmethod,underthesametestmethod. [8]2022AssessingSurveyN/AStudents32 This inducesatestmethodwithmultipleassertstate-**III. Study**Design**Abbreviation**(AR) (TCD)ments, coveringalltheproductionmethod'sexecution The primaryobjectiveofthisstudyistoassesstowhat paths. Accordingtotheliterature,ithinderscomprehen- extentAssertion RouletteandEager Testhinder students' sion bymakingitdifculttodeterminewhichassertion program comprehension.Todoso,weevaluatetheimpact has triggeredthetestfailure[32]. of thesesmells'existenceonthedebuggingprocesswhen **Suite E**. Weintroduced(E)ager Testsmell into students usesmellytestlestolocateerrors.Therefore,our Ntest casesbytestingmultiplescenarios,for main ResearchQuestionis: production methods,underthesametestmethod.This **RQ: To**whatextentdo**Assertion Roulette****and****Eager**induces atestmethodwithmultipleassertstatements, **Test****impact the**timespentbystudentsindebuggingcovering alltheproductionmethod'sexecutionpaths. **failing test**cases?According totheliterature,ithinderscomprehension by makingitdifculttodeterminewhichmethodhas Bydebugging time, wemeanthetimeneededforastudenttriggered thetestfailure[32]. to troubleshootafailingtestmethodandxitscorresponding Toensure each suite contains (or not) the intended test smellerror intheproductionmethodundertest.Basedonexisting type, we run TS-Detect, one of the popular state-of-the-art teststudies, smellytestleshinderprogramcomprehension,i.e., smell detectors[34],foreachsuite,asasanitycheck.we hypothesizethatstudentsshouldtakealongertimeto locate an error raised by a smelly test method, as it is harder to**A. Project**Overview read, incomparisontothetimeneededtondanerrorraised Since wearemeasuringstudents'debugging time,weneedby anon-smellytestmethod.Toaddressthishypothesis,we to avoidanybiasthatcanbeintroducedduetomisun-create acontrolledexperimentwhereweselectoneproject, derstanding theprogram'sbehavior.Therefore,thechosenwhich alreadycontainsaunittestsuitewith100%path application shouldbeintuitiveforanyonetounderstand.Forcoverage. Then, we inject errors in production methods, which this purpose,wecreatedabasiccalculatorapplicationusingare going to be caught by the tests, i.e., for each error injected Java programminglanguage.Thelanguagewaschosentointo theproductioncode,itscorrespondingtestmethodis match students'familiaritywithobject-orientedprogramminggoing tofail.Forasetofcreatederrors,thetimeneededto at theirlevel.Similarly,thechoiceofcalculatorisdrivenbydebug theirfailingtestmethodsisexpectedtotakelonger intuitiveness andstudents'familiaritywithitsfeaturesunderif thesetestmethodsaresmelly.Thiscanbeempirically test. Thecalculatorwasdesignedwitheightfunctionslistedvalidated if,forthesamesetoferrors,thetimeneededto below:debug themwouldtakelongerifthetestsuiteissmelly, in comparisonwiththedebuggingtimewhenthesametest**Summation (Sum):**is aproductionmethodthattakes as inputtwovariablesoftypedouble, andreturnstheirsuite isnotsmelly.Sinceweareinterestedincomparingthe summation, e.g.,10 + 2 = 12.debugging time, outofanon-smellytestsuite(referredtoas


---

<!-- Página 4 -->

# PREPRINT

TABLEII:Summaryoftestcasesforeachcategory.andtest01()(resp.test05andtest06) aremerged, since theyaretestingthesameproductionsummation(resp. subtraction) method.Themergedmethodshavetheassertion roulettesmell, sotheybelongtoSuite A. AsforListing4, all methodsfromListing2aremergedintoonetestmethod, constituting theeager test. Themergedmethodhasthe testsmell, soitbelongstoSuite E. Thisprocesshasresulted in 40testmethodsinSuite N, 8testinA , and 9 testmethodsinSuite E. Thecountoftestforeach test suiteissummarizedinTable II

**C. Errors**Generation **Subtraction (Sub):**is aproductionmethodthattakes**#**3Tocreate the errors, we used PITest, a Java mutation testing**Suite**as inputtwovariablesoftypedouble, andreturnstheir**Method** **Non-Smelly****Assertion****Earger**framework, to generate faults (or mutations) that are purposelysubtraction, e.g.,10  2 = 8.**Summation**51seeded intotheproductionmethods.Foragivenmutated**Subtraction**51**Multiplication (Mult):**is a production method that takes **Multiplication**71production method,ifoneormanyofitscorrespondingtestas inputtwovariablesoftypedouble, andreturnstheir**Division**519method(s) fail(s),thentheerroriscaught.Otherwise,ifthe**Square**51multiplication, e.g.,10 2 = 20. tests pass,thentheerrorismissed.PITistypicallyused**Modulo**51 **Division (Div): is a production method that takes as input****Average**41to evaluatethequalityoftestsbythepercentageofcaughttwo variablesoftype double, andreturnstheirdivision,**Factorial**41 errors. Inourcontext,weusePITtogeneratearbitraryerrors**Total****40****8****9**e.g.,10 5 = 2. throughout theproductionmethods.Thenweselectederrors **Square Root**(SQRT):is afactorthat,whenmultiplied while making sure each production method would have at leastby itself,equalstheoriginalvalueofthegiveninteger. pone error, andtheselectederrorswereallcaughtbythe3testA squarerootisrepresentedbyaradicalsymbol( suites.1and canbedeterminedbythevalue ofthepowerof an2pFigure 1presentstwoproductionmethods,i.e.,summation integer,e.g.,25 = 5. method,and subtraction,containingtwoerrors.Inthesum **Modulo (Mod):**is thesignedresidueofadivision, the summationoperation(+)isreplacedwiththesubtraction which occursafterdividing twonumbers.Itiscomputed operation (-),resultinginafaultybehavior.Likewise,the by subtractingthedivisorfromthedividenduntilthe subtract operation (-) is replaced with the summation resulting islessthanthedivisor, e.g.,5 (mod2)= 1 (+), inthe dif f. **Average**(Avg):is amathematicaloperationtocompute **p u b l i c c**l a s a l c u l a t f rthe mean of a given set of numbers. It is the ratio of sum **p u b l i c d**o u b l e( d o u b l e ] ar r f)of allnumbersinagivensettothenumberofvalues / / Cr e a t i o n of Ar r a ypresent intheset,e.g.,avgofnumbersinset **d o u b l e**= 0;1+2+3+4+5A = f1;2;3;4;5gcan becomputedas= 3 .**f o r**( i n ti =0 ; i<a r r .l e n g t h ; if ++)5 **Factorial (Fact): is a function that outputs the product of**sum= ar r [ i ]; gall positive integerslessthanorequaltoagiven / / ad d i n g al l el e m e n t s in anar r a yinteger.Itisindicatedbyanexclamation markpreceding System. o u t . pr i n t l n (  A d d i t i o n ;+sumthat integer, e.g.,4!=24. **r e t u r n**; g**B. Test**SuitesCreation

For eachproductionmethod,weneedtocreateitscorre-**p u b l i c d**o u b ub t r a cdt o( u b l e ] ar r f) / / Cr e a t i o n of Ar r a ysponding testmethods,ensuring100%pathcoverage.These 2**d o u b l e i f f**= 0;test methodswereautomaticallygeneratedbyEvoSuiteand **f o r**( i n ti =0; i<a r r .l e n g t h ; if ++) labeled asSuite N. Sincethegeneratedtestmethods'names d i f f+= ar r [ i ]; are not descriptive, for each test method, we added a commentg to indicatewhichproductionmethodittests.Itiscriticalfor/ / Su b t r a c t i n g al l el e m e n t s in anar r a y System. o u t . pr i n t l n (  S u b t r a c t i o n : +our experimentstoensurethatthemappingbetweentestand d i f f) ;production methodsismaintained.Otherwise,theoverhead **r e t u r n**d i f f; of studentssearchingforsuchmappingswouldinatethe g debugging time.To createSuite AandE , weduplicateg Suite N, andwemanuallyintroducethesmellsbasedontheir Listing 1:Examplefortwoproductionmethodswithseededdenitions thatweoutlinedabove. errors.Toillustratehowthesesuitesdiffer,Listing2shows4 test methodsfromSuite N. Listing3showshowtest00()

23[https://www.evosuite.org/](https://www.evosuite.org/)[https://pitest.org/](https://pitest.org/)


---

<!-- Página 5 -->

# PREPRINT

**D. Target**Courseinvestigation,we conducted a pilot study with four undergrad- uate studentswhowerelaterexcludedfromthecontrolled This experimenthasbeenconductedinanundergraduate experiment. Thegoalofthepilotstudywastoguaranteethat4senior-levelsoftwareengineeringcourse. Beforejoiningthis the experiment'sinstructionswereclearandtoestablishan course, students have about two years of programming experi- approximate durationforthelabsession.Followingthepilot ence. Thisprovidesthemwiththebackgroundtoperformthe study,wedecidedtoprovideallupcomingparticipantswith debugging neededinthisexperiment.Also,theyarefamiliar documentation onhowtosetuptheprogrammingenviron- with theprocessofsearchingfortherooterrorsinafaulty ment. Also, we would only allow students to participate in the code. experiment whentheyhavetheirenvironmentreadytoavoid **p u b l i c c**l a s a l c u l a t o S T e s t x t e n d sskewing ourmeasurements. C a l c u l a t E S T e s t c a f f o l d i n g **p u b l i c c**l a s a l c u l a t o S T e s t x t e n d s/ / Te s t Ca s e s fo r SumMethod C a l c u l a t E S T e s t c a f f o l d i n g@Test ( t i m e o u t =40 0 0 ) / / Te s t Ca s e s fo r SumMethod**p u b l i c v**o i e s t 0 0 (throws)T h r o w a b l e @Test ( t i m e o u t =40 0 0 )C a l c u l a t o r ca l c u l a t o r 0 = **p u b l i c v**o i e s t 0 0 (throws)T h r o w a b l eC a l c u l a t o r () ; C a l c u l a t o r ca l c u l a t o r 0 =**d o u b l e d**o u b l e A r r a y 0 =**d**o u b l 2 ] ; C a l c u l a t o r () ;**d o u b l e o u b l e 0 =**ca l c u l a t o r 0 .sum ( **d o u b l e d**o u b l e A r r a y 0 =**d**o u b l 2 ] ;d o u b l e A r r a y 0 ) ; **d o u b l e o u b l e 0 =**ca l c u l a t o r 0 .sum (a s s e r t E q u a l s (0 . 0 , do u b l e 0 ,0. 0 1 ) ; d o u b l e A r r a y 0 ) ;g a s s e r t E q u a l s (0 . 0 , do u b l e 0 ,0. 0 1 ) ;@Test ( t i m e o u t =40 0 0 ) **p u b l i c v**o i e s t 0 1 (throws)T h r o w a b l e **d o u b l e d**o u b l e A r r a y 1 =**d**o u b l 2 ] ;C a l c u l a t o r ca l c u l a t o r 0 = d o u b l e A r r a y 1 [ 0 ] =(1 . 0 ) ;C a l c u l a t o r () ; **d o u b l e o u b l e 1 =**ca l c u l a t o r 0 .sum (**d o u b l e d**o u b l e A r r a y 0 =**d**o u b l 2 ] ; d o u b l e A r r a y 1 ) ;d o u b l e A r r a y 0 [ 0 ] =(1 . 0 ) ; a s s e r t E q u a l s ( ( 1 . 0 ) ,do u b l e 1 ,0. 0 1 ) ;**d o u b l e o u b l e 0 =**ca l c u l a t o r 0 .sum ( gd o u b l e A r r a y 0 ) ; / / Te s t Ca s e s fo r Su b t r a c t Methoda s s e r t E q u a l s ( ( 1 . 0 ) ,do u b l e 0 ,0. 0 1 ) ; @Test ( t i m e o u t =40 0 0 )g **p u b l i c v**o i e s t 0 1 (throws)T h r o w a b l e/ / Te s t Ca s e s fo r Su b t r a c t Method C a l c u l a t o r ca l c u l a t o r 0 =@Test ( t i m e o u t =40 0 0 ) C a l c u l a t o r () ;**p u b l i c v**o i e s t 0 5 (throws)T h r o w a b l e **d o u b l e d**o u b l e A r r a y 0 =**d**o u b l 2 ] ;C a l c u l a t o r ca l c u l a t o r 0 = **d o u b l e o u b l e 0 =**ca l c u l a t o r 0 .su b t r a c t (C a l c u l a t o r () ; d o u b l e A r r a y 0 ) ;**d o u b l e d**o u b l e A r r a y 0 =**d**o u b l 2 ] ; a s s e r t E q u a l s (0 . 0 , do u b l e 0 ,0. 0 1 ) ;**d o u b l e o u b l e 0 =**ca l c u l a t o r 0 .su b t r a c t ( d o u b l e A r r a y 0 ) ; **d o u b l e d**o u b l e A r r a y 1 =**d**o u b l 5 ] ;a s s e r t E q u a l s (0 . 0 , do u b l e 0 ,0. 0 1 ) ; d o u b l e A r r a y 1 [ 2 ] =93 ;g **d o u b l e o u b l e 1 =**ca l c u l a t o r 0 .su b t r a c t (@Test ( t i m e o u t =40 0 0 ) d o u b l e A r r a y 1 ) ;**p u b l i c v**o i e s t 0 6 (throws)T h r o w a b l e a s s e r t E q u a l s ( ( 9 3 ) ,do u b l e 1 ,0. 0 1 ) ;C a l c u l a t o r ca l c u l a t o r 0 = gC a l c u l a t o r () ; g**d o u b l e d**o u b l e A r r a y 0 =**d**o u b l 5 ] ; d o u b l e A r r a y 0 [ 2 ] =93 . 0 ;Listing 3:ExampleoftestcasesourcecodeforAssertion **d o u b l e o u b l e 0 =**ca l c u l a t o r 0 .su b t r a c t ( Roulette testsuite.d o u b l e A r r a y 0 ) ; a s s e r t E q u a l s ( ( 9 3 . 0 ) ,do u b l e 0 ,0. 0 1 ) ; g**F.**Procedure g Following theresultsofthepilotstudy, weconductedtwo Listing 2: Example of test case source code for Non-test Smellsessions: apreparationsessionandacontrolledexperiment test suite.session. Duringthepreparationsession,wesuppliedstudents with a video tutorial for both Windows and Mac to show them how toinstallsetuptheprogrammingenvironmentontheir**E. Pilot**Study 5computers and run test cases on their IntelliJIDEApanels. We A pilotstudyistheinitialphaseoftheentireresearchalso gave the students written instructions outlining a step-by- 6protocol andisgenerallyasmaller-scalestudythatservestostep procedureforinstallingJava ontheirsystems. We made solidify themainstudy[26].Therefore,priortotheprimarysure allstudentshadtheirenvironmentreadyandknewhow

54[https://www.jetbrains.com/idea/](https://www.jetbrains.com/idea/)Some 6Theseomitted


---

<!-- Página 6 -->

# PREPRINT

## N

## N

we collecteddatafrom45participantsintherstsemester and 51participantsinthesecondsemester.Figure1depicts each group's nal arrangement in the classroom, and Table III contains thedistributionofparticipantsineachcategory. Upon theexperiment'scompletion,therewere29partici- pants inGroupN( Non-Smelly Test), 33participantsin A( Assertion Roulette), and34participantsinGroupE( Eager Test).

**p u b l i c c**l a s a l c u l a t o S T e s t x t e n d s C a l c u l a t E S T e s t c a f f o l d i n g @Test ( t i m e o u t =40 0 0 ) **p u b l i c v**o i e s t 0 0 ()**throws**T h r o w a b l e Fig. 1:Studentsarrangementintheclassroom.C a l c u l a t o r ca l c u l a t o r 0 = C a l c u l a t o r () ; **d o u b l e d**o u b l e A r r a y 0 =**d**o u b l 2 ] ; **d o u b l e o u b l e 0 =**ca l c u l a t o r 0 .sum (to runtestcasespriortoourexperiment.Also,weprovided d o u b l e A r r a y 0 ) ; students withthebug-freeversionoftheproject,alongwitha s s e r t E q u a l s (0 . 0 , do u b l e 0 ,0. 0 1 ) ; some test cases fromSuite N, as we want to increase student's familiarity withtheproductionmethods.Students'**d o u b l e d**o u b l e A r r a y 1 =**d**o u b l 2 ] ; d o u b l e A r r a y 1 [ 0 ] =(1 . 0 ) ;with theproductioncodeisimportant,assomestudentsmay **d o u b l e o u b l e 1 =**ca l c u l a t o r 0 .sum (exercise more effort to read and comprehend source code [43]. d o u b l e A r r a y 1 ) ; Code comprehensionisalsoanoisethatwemitigatethrougha s s e r t E q u a l s ( ( 1 . 0 ) ,do u b l e 1 ,0. 0 1 ) ; their exposure to the project before the session. The supporting material relatedtothecurrentexperimentcanbeaccessed**d o u b l e d**o u b l e A r r a y 2 =**d**o u b l 2 ] ; **d o u b l e o u b l e 2 =**ca l c u l a t o r 0 .su b t r a c t (through thelink:[1].Finally,weconductedapresentation d o u b l e A r r a y 2 ) ;of thecalculatorproject,itsfeatures(operations),itssource a s s e r t E q u a l s (0 . 0 , do u b l e 2 ,0. 0 1 ) ; methods, andtheexecutionofsampledtestcases. The secondsessionwascarriedoutinpersontoavoidany**d o u b l e d**o u b l e A r r a y 3 =**d**o u b l 5 ] ; collusion. At the start of the controlled experiment session, wed o u b l e A r r a y 3 [ 2 ] =93 ; **d o u b l e o u b l e 3 =**ca l c u l a t o r 0 .su b t r a c t (randomly splitstudentsintothreegroups,basedonwhichtest d o u b l e A r r a y 3 ) ;they will be using:N , E , and A. The entire session was 2 hours a s s e r t E q u a l s ( ( 9 3 ) ,do u b l e 3 ,0. 0 1 ) ; (120 minutes)long.Theexperimentstartedatthesametimeg for everystudent.Thetaskassignedtothestudentswastog identify and x the issues raised by the failing test methods in Listing 4:ExampleoftestcasesourcecodeforEagerTesttheir corresponding suite. The use of online resources was also suite.permitted. Studentswereinstructedtosubmittheirupdated 7code immediatelytoCanvasonce theyaredonexingthe **H. Data**Collectionerrors. WechosetouseCanvassincestudentsarefamiliar with it.Wedetermineddebugging timefor eachstudentbyData collection,inthisstudy,istwo-fold.First,wecon- examining theirsubmissiontimestamponCanvas. Finally, weducted acontrolledexperimenttodeterminehowmuchtime shared anonlinepost-surveytogathertheirfeedbackabouteach participantincurreddebuggingthegivensourcecode. their debuggingexperiences.WeusethissurveytogaugeThe participantsbeganthelabsessionatthesametimeand if studentshaveexperiencedanydifcultieswhendebuggingsubmitted theircorrespondingsourcecodeaftercompleting their code.Itisimportanttonotethatstudentsarenotawarethe debuggingtask.Second,wecreatedasurveytogather of theunderlyingexperiment,i.e.,themultipletestsuitesanddetails onparticipants'experiencesinrelationtodebugging the existenceoftestsmells.test cases.Thesurveyquestionsweremadeavailableonce they had nishedidentifying andxing the bugs in thesource**G. Participants** 8code. Google Formswas used to supply the participants with The controlled experiment was carried out in two semesterssurvey questionsandcollectthedata.Twomultiple-choice and involved96undergraduatestudents.Theseparticipantsquestions andoneopen-endedquestionwereincludedinthe were enrolledinasoftwareengineeringclass.Studentswerequestionnaire. asked tocompletethetwosessionstoobtainextracredit, **I. Survey**but theyweregiventheoptiontochoosetohavetheirdata examined aspartofthisstudy. Basedonthatconsent,outofThe initial survey had eleven questions. Then, it was revised 56 participantsfromsemesteroneand65fromtwo,to eliminatequestionsthatwerefoundrepetitive,irrelevant,

78Web-based[https://www.google.com/forms/about/](https://www.google.com/forms/about/)

## A

## E

## A

## A

## N

## N

## E

## E

## A

## N

## A

## A

## E

## E

## N

## E

## L e g end

## A

## N

## E

### S u i

### t

### e

### N

### S u i

### t

### e

### A

### S u i

### t

### e

### E

### E a g er

###

### T e s t

### N o n -

### S m

### e l

### l

### y

### T e s t

### A s s er

### t

### i

### o n

### R o u l

### e t

### t

### e


---

<!-- Página 7 -->

# PREPRINT

TABLEIII:Summaryofthenumberofparticipantsinthestudy.

TABLEIV:Setofsurveyquestions.Ehave spent a signicantly larger amount of time locating the errors, incomparisonwithstudentswhowereusingSuiteN . **Observations.**The timespenttolocateanerrordiffers depending onthetestsuitereportingit.Forinstance,when using SuiteN , eachfailingtestmethodcontainsonlyone failing assertstatement.Thisstatementwouldeven- tually indicatetothestudenttheinconsistencybetweentheor confusing.Thisrevisionreducedthenumberofquestions expected valueandtheactualofthemethodunderto nine.Thepilotstudyofthefourundergraduatestudents test. Thestudentswouldtheninvestigatethecorrespondingrevealed concernsaboutthelengthofthesurvey,theredun- method. Whentheerrorisfoundandthenxed,notonlythedancy of some questions,and the need for logicalarrangement.**Question****Type** investigatedtesting method would pass, but also any other testWereMultipleWereducedtheninequestionstothreeaccordingly. Thenal Themethods thatwerefailingforthesamereason.Ontheothersurvey contains three questionstwo multiple-choice and onewasMultiple hand, whenusingSuiteA, eachfailingtestmethodcontainsIfopen-endedthat canbeseeninTable IV. pleaseOpen-endedmultiple assertstatements,inwhichasubsetisfailingwithSurvey questions were made for extra credit and only for the more than one assert statement to be investigated. The studentsstudents whoparticipatedindebuggingthecode.Thesurvey tend toexaminethemtounderstandthecommoncauseforrespected data privacy and protection guidelines. For instance, their failure before switching to the method under test to searchwe protecttheprivacy oftherespondentswhoparticipatedin for the error. Therefore, the investigation of the multiple assertsthe studybyanonymizingallresponses.Additionally,pass- seems to increase the debugging time, and therefore,Asser-thewords wereusedtosecuretheresearcher's laptopwithallthe tion Rouletteis negatively impactingthestudents'debuggingresearch materials,includingparticipantresponses.Further-**Categories****#****#****#****#**process. Ourobservationbringsanalternateperspectivewith**Non-Test****Assertion****Eager**more, respondents' consent was obtained prior to participation **Semester**561145141615respect to the recent ndings of Bai et al. [7], who conjecturesfor theutilizationoftheirdataforresearchpurposes.**Semester**651451151719 thatAssertion Roulettemay nolongerbeconsideredacode**Total****121****25****96****29****33****34** smell. In fact, Bai et al. [7] demonstrated, through a controlled**IV.**StudyResults classroom experiment, thatAssertion Roulettedoes impact nei- In thissection,wepresenttheimpact AssertionofRoulette ther the frequency of testing nor the accuracy of the test cases. andEager Teston students'debuggingskills(SectionIV-A) Weargue thatAssertion Rouletteis aprogramcomprehension and theirexperiencewiththedebuggingprocessforeachtest problem. Therefore,acontrolledexperimentwherestudents' suite (SectionIV-B).Further,wediscusstheresultsof programming performance and testing behaviors are measured test foreachgroupN,E , andA . may notrevealthenegativesymptomsofRoulette. As fortheEager Test, thesmelliscausedbyatestcase**A. Experiment**Results involvingmultipleproductionmethods,therebyincreasing coupling between the test and production code. Such situations**RQ: To**whatextentdo**Assertion Roulette****and****Eager** result inparticipantsreviewingmultipleproductionmethods**Test impact the time spent by**in debugging and continuallyswitchingbetweenmultiplecodelesaspart**failing test**cases? of theirtroubleshootingtask,whichpotentiallyincreases **Method. The answer to this RQ, Figure 2 reports**debuggingcognitive loadandtime. timeboxplots ofeachgroup.Totestthesignicanceof **Summary:**The presenceoftestsmells,namelyAssertion the differencebetweeneachpairofgroupvalues,weuse RouletteandEager Test, inthetestsuitecauseparticipants the Mann-WhitneyUtest,anon-parametrictestthatchecks to spendmoretimetroubleshootingtestcasefailures,in continuous or ordinal data for a signicant difference between comparison withperformingthesamedebuggingprocess two independentgroups.Ourhypothesisisformulatedtotest using anon-smellysuite. whether groupAvalues aresignicantlyhigherthanN . The differenceisconsideredstatisticallysignicantifthep- **B. Survey**Resultsvalue islessthan0.05.Thesametestisrepeatedfor(group E , groupN ) and(groupA,E ) pairs.**Method. We**also wanted to know if the debugging task was **Results.**As showninFigure2,groupAvalues aresig-challenging or straightforward for the participants to complete. nicantly higherthanthevaluesofgroupN( i.e. , p<0.05).Thus, weanalyzedtheparticipants'surveyresponsesafter Similarly,groupEvalues are signicantly higher than the val-they submittedthem.Figure3presentstheresponsesby the participantsdividedbasedoneachgroup.Weaskedtheues ofgroupN( i.e. , p<0.05). Thetwo pairwisecomparisons indicate howstudentswhowereusingeitherSuiteAorparticipants threequestions.


---

<!-- Página 8 -->

(Minutes)

Time

# PREPRINT

that thehighestratio(55%n= 16) ofparticipantsagree with the smoothness and straightforwardness of the underlying debugging task. Following this, 28%n(8 ) of the participants selected the Agree option,whichmakesanoverall83% ( n= 24) oftheparticipantswhoagreedwiththesimplicity of locatingandxingbugsinNon-Smelly Testtest suite.On the contrary,onlyasmallportionofparticipants,i.e.,3% ( n= 1 ), stronglydisagreedhence,referringtotheprocedure as difcult,whilenoneoftheparticipantsdisagreedwiththe statement. Ontheotherhand,14%n ( 4) oftheparticipants remained neutraltotheaskedquestion.Therefore,itisfairto say thattheabsenceoftestsmellsinthetestcasesmakesthe participants' taskofdebugging easytounderstandandsimple to x. Figure 3(B)showcasestheresponsesreceivedbytheFig. 2:Distributionofthetimespentbyparticipantstodetect participants ofAssertion Roulettetest suitetothesurveyand debugeachtestsuite. question #2.Unlikethepreviouslydiscussedcase,only67% ( n = 22) participants ofAssertion Roulette test suite coincided with theprocessoflocatingandxingthebugstobeeasy **Results.**Wequestionedtheparticipants,**Were**youableto and smooth,amongwhich40%n( = 13) participantswere **x all**theerrorsdetectedbythetestcases?, toinvestigate in strongagreementwiththestatementand27%n( 9) the impactoftestsmellsontheperformanceofparticipants' of theparticipantsagreed.Moreover, theratioof detection anddebuggingskillsofthesourcecode.Asthe who disagreed and stronglywith the stated question proportion ofsuccessfulparticipantsnishingthetaskwithin amounted to 15% (= 5 ), among which 9%n( = 3 ) disagreed the giventimeframesignicantlyimpactstheirperformance, and 6%(= 2 ) oftheparticipantsstronglydisagreed.These this question is essential to the generalizability of the analysis.120 numbers mayhaveformedduetothetestcases'inclusionof Wecompiled the responses, and we veried them with the les numerous untitledassertions,whichconfusedtheparticipants. that weresubmitted.We foundthatatotalof13participants100The participantsspentmoretimelocatingtheassertionthat were unable to locate and x the source code, with the number caused thetestcasetofail, makingitmoredifcult tohandle. of participantsassignedtothe Assertion Roulettetest suite80Therefore, themostdifculttestsmelltoaddressinthetest failing bythebiggestmarginn(= 7). Threeparticipants cases canberuledoutasAssertion Roulette. who wereprovidedthe Non-Smelly Testtest suitedidnot60Figure 3(C)presentsthestatisticaldataregardingpartici- manage tocompletetheassignment.Similarly,3participants pants' responsestosurvey question#2intermsEagerofTest in thetestsuitefortheEager Testfailed tocompletethe40test suite. Overall, 82%n( = 28) of the underlying participants task. Thesestatisticsillustratetheconsiderabledetrimental voted inconjunctionwiththestatedquestion.Where,50% impact ofAssertion Rouletteon participants'abilitytodebug20( n= 17) stronglyagreedwiththeeaseandsimplicityof source code.Itshouldbehighlightedthatparticipantswere the processand32%n(= 11) oftheparticipantsresponded uninformed ofthetestsmellsexistenceinthesuites. 0with Agree option.Ontheotherhand,only3%n( 1 )EagerNon-SmellyAssertion**Summary:**Although theparticipantswereunawareoftheof theparticipantsdisagreedwiththeprocessoflocatingandTesttest smellstheywereassigned,mostofthemmanagedtoxing bugsinEager Testtest suitbeingeasyandsmooth. locate and x all the issues in the source code. Additionally,InEager Testtest suit,thetestcasesfromNon-Smelly Test participants assignedwiththe Assertion Roulettetest suiteandAssertion Roulettetest suitesweremergedinto9test had thehighestpercentagethatwasunabletocompletecases. Moreover, this smell induces multiple production codes the assignmentwithinthegiventimeframerevealingthewhen onemethodisinvoked, causingasignicantimpacton negativeimpactofthisparticularsmell.the debugging skillsoftheparticipants.However, participants found itcomparativelyeasytohandleastheywereableto Figure 3showcasestheresponseofparticipantsregardingfollow uponthelogicoftheoperationandlocatethebugin the secondmultiplechoicequestionofthesurvey;**The**the sourcecode. **process of**ndingtheerrorsdetectedbythetestcaseswas Observations.Overall, studentsfromallgroupsexhibit **smooth and**easy?Five optionsStronglyAgree,similar levels of satisfaction with their testing experience, with Neutral, Disagree,orStronglyDisagreeweregiventothea slightincreaseforthoseusingnon-smellytests,and participants. Themajorityofparticipants,ingeneral,stronglyusingEager Tests. Noneoftheparticipantshave reportedany agreed that the process of identifying and debugging test casesissues theyexperienced,despitethesmellinessofSuiteAand is simpleandstraightforward.E . We argue thatAssertion Roulette and Eager Testare hard to be soughtasproblematic,asthey areintuitive bynature.ThisFigure 3(A)correspondstotheresponsesreceivedby is alignedwiththeirhighfrequencyinopensourcesystems,the participantsfromNon-Smelly Testtest suite.Itisclear


---

<!-- Página 9 -->

# PREPRINT

The processofndingtheerrorsdetectedbythetestcaseswassmoothandeasy?

Fig. 3:Distributionofstudents'responsestosurveyquestion#2.

Ê Comment 7:I founditeasytotondtheaccording torecentstudies[10],[24],[33],[39]. issues becausethecodewaswellformattedand **Summary: Non-Smelly Testand Eager Testtest suites were**commented. When I saw the error was with subtrac- equally rated to be simple and straightforward to handle. Intion Iwenttothesubtractionfunction.There Iread contrast, Assertion Roulette test smell was rendered to makethe commentsonwhateachpartofthecodewas the processdifcultfortheparticipants.supposed todo,whenitwasdifferent Ijustchanged the codetodowhatthecommentssaid. Finally,wesuppliedtheparticipantswithanopen-endedAmong thesepositivecomments,We notehowcomment 6 question:**If you**agreedorstronglywiththeprevioushas mentionedthetestofmorethanonemethodwithoutnec- **question, please**explainwhy.Responses received from groupessarily considering it to be problematic. It is apparent that the Nparticipants showtheirhighsatisfactionwiththeoverallsuccessful xofallerrorsraisedasenseofaccomplishment testing experience:among studentsandpositivelyinuencedthem. Ê Comment 1:The structurewaseasiertodi-**Summary:**Assertion Roulette, andEager Testsmells are agnose witheachtestcases.OnceIwasabletotransparent tostudentsaslongastheyaresuccessfulin diagnose where the errors were, it got easier to clearlocating andxingerrors. all theerrors. Ê Comment 2:Once Ifoundwhichtestcasewas **V.**Discussionwhich, itwaseasytondwhatfunctiontheywere using (after I realized the equate function was a builtThe analysis of the current investigation has revealed signif- in one).Thatinturnmadeiteasytogure outthaticant informationregardingtheimpactofAssertion Roulette the error was limited in scope to that function aloneandEager Teston theparticipants'debuggingtime. [...]As wepreviouslydiscussed,Baietal.[7]advocatesfor Moreover,some participants who were not previously famil-Assertion Rouletteto benolongerconsideredastestsmell. iar withtheJavaprogramminglanguageexpressedapositiveHowever,theaforesaidstatementisnotconsistentwithour experience, asoneoftheparticipantssaid:ndings. Ourexperimentrevealedthatspentsig- nicantly moretimesortingtheassertionsthatarestackedÊ Comment 3:Haven't touched javabefore, once in theAssertion Roulettetest methods.Furthermore,wewit-I understoodwhatwasgoingon,wasn'tdifcultto nessed asimilarpatternoflongerdebuggingtime,whennd students useEager Testtest methodstolocateerrors.Responses received from groupA participants did not differ Therefore, educatorsneedtoraisethestudents'awarenessfrom thepreviousgroup,asstudentsexpressedtheirsatisfac- Strongly55%40%50%of writingsmell-freetestcases.Studentsneedtobetaughttion withthedebuggingprocess: Agree28%27%32%how toavoidwritingmultipleassertsunderthesametest Ê Comment 4: [...]BecauseIcanseetheex-14%18%15%Neutral methods, ortotestmultipleproductionusingtheDisagree0%9%3%pected resultandtheactualandtraceback same testmethod.thiscontext,Buffardietal.examinedStronglyIn3%6%0%where thecodeiswrong. students' testmethodsontheirassignments,andindicated0% 20%40%60%80%100%0% 20%40%60%80%100%0% 20%40%60%80%100%Responses receivedfromgroupEparticipants didnotde-potential problemsintheirunittests.Infact,thetopthree**(A)** viate fromthepreviousones,asstudentspositivelydescribedcommon patternsdetectedintheirtestmethods:multiple their debugging:member functioncalls,multipleassertions,andconditional Ê Comment 5:The printoutstatementandthelogic [13].Thereby,takinganactiontoeducatestudentson expected outputhelpedmeidentiedwhereinthehow toavoidtheseanti-patterns,woulddecreasetheearly code tolookandwhatIneededtox.propagation ofthesesmells. Ê Comment 6:The testcasespointedoutsomeAdditionally,thecurrentresearchdiscovered thattest functions beingusedandgavetheexpectedandwith descriptivenamesandcommentedassertsincreasetheir actual values.Thishelpedmetopinpointwhatwasreadability [37].Thus,weencouragestudentstodevelopthe wrong andwhere.practice ofdocumentingtheirtestmethods.


---

<!-- Página 10 -->

# PREPRINT

**A. Lessons**Learned:**VII. Conclusion**andFutureWork Throughout theexperiment,severallessonswerelearned,In thisstudy,weexploredtheimpactoftestsmellsona and perceptualobservationswereconducted.student'sprogramcomprehensionability. Theresultsindicate Ï Lesson #1:In additiontoteachingstudentsaboutdesignthat theparticipantsinourstudywhowereassignedtest and codesmells,academiamustalsoinstillinstudentsthesuites containingtestsmellstookmoretimetocompletethe importance of writing quality test cases, specically test smellsassigned task of xing errors in the production code than those and theharmcausedbytheintroductionandexistenceofgiven testsuiteswithouttestsmells.Furthermore,thesmell test smellsinthesystemscodebase.Furthermore,teachingAssertion Roulettehad agreaterimpactontroubleshooting students aboutcodereviewsshouldnotbelimitedtotheand debugging than theEager Test smell. For future work, we production code but should also include the test suites, as suchplan to conduct a similar study with additional test smell types code isvitaltothesystem's overallquality.to determinehowthesenewsmellsimpactastudent's ability Ï Lesson #2:The researchcommunityhasproducedtoolsto comprehendcodewhenperformingmaintenanceactivities. to aiddevelopers withdetecting(and,insomecases)correct- **Veriability**andReplicabilitying test smells for various programming languages, and testing frameworks [3].ThesetoolshavebeenutilizedinmultipleToenablefullveriability andreplicability, ourexperimen- empirical studiesandhavebeeneffectiveintheirdetection9tal materialsareavailable[1]. mechanism. Academia should promote using these tools in the classroom to better equip students with means of evaluating the**References** quality ofthetestcasestheyproduceforclassassignments. [1] In addition,theautomaticdetectionoftestsmellswillhelp [2]al a. students totroubleshootissuesmuchfaster.code ProceedingsÏ Lesson #3:Even thoughmostresearchontestsmells oriented,focuses onJavasystems,testsmellsarenotuniquetoJUnit- pages based testsuites.Therefore,theresearchandacademiccom-[3] A.munity shouldinvest inexploring thetypesoftestsmellsthat tools:Evaluationare uniquetospecicprogramminglanguagesandparadigms Software, pages and passingthatknowledgetostudentsintheclassroomso[4] education.Proceedingsthat theyarebetterpreparedwhenenteringtheworkforce. Computer, pages **VI. Threats**toValidity[5] programming The applicabilityofthendingsinthisresearchissuscep-Workshop,, pages [6]tible toanumberofthreats. Stolee.**Internal Validity.**The studentswhoparticipatedinthis composition2019 experiment werefromthesameuniversity,makingthepar-on, pages ticipant poolrelativelycoherent.To mitigatethis,werunour[7] rouletteexperiments intwosemesters.Anotherpertinentthreatrelates education.2022 to thechoiceoftheprojectundertest.ThecomplexityofCentric, pages the projectfeaturesmayrequireadvanceddebuggingskills,[8] off:which maycrateasignicantoverheadinourexperiment. student-authoredProceedings Tomitigatethisissue,wedevelopedacalculatorapplicationon with eightoperations.Thechoiceofthecalculatorensuresits1 , pages [9]intuitiveness tothestudents.Althoughsomestudentsmight practices,Proceedingsnot befamiliarwiththesourcecode,wegavethemdetailed Innovation, pages instructions anddocumentationtofamiliarize themselves with248254, [10]the projectandsourcecodeinordertominimizethethreat empiricaland potentialmisunderstandings. on2012 **External Validity.This study is exclusively focused on two**on, pages [11]test smells. However, given the prevalence of test smells, there testEmpiricalmay beachancethatwemissedanimportantsmellthatis Engineering,20(4):10521094, typically writtenbydevelopers.Tomitigatethisthreat,we[12]Test-driven. Addison-Wesley signaturereviewed variousresearchpapersthathaveconductedsimilar [13]types ofexperiences.Weconcludedthatthemostpopular softwareProceedings and frequentsmellsare Assertion Roulette, andEager Test.ACM Moreover,itisessentialtoreplicatethestudywithabroaderEducation, pages and more varied range of test smells along with a wider 9of codebases.[https://wajdialjedaani.github.io/testsmellstd/](https://wajdialjedaani.github.io/testsmellstd/)


---

<!-- Página 11 -->

# PREPRINT

[14]Software Approach.McGraw-HillsmellsProceedings Symposium, SAST[36]e pageengineering Machinery.ACM, 26(1):106110, [37][15] Improvinglevel2011 24th,Software, pages pages178. [38][16] On2018studentsJournal IEEEComputing, 3(3):1es, (ICSME),pages[17] [39]and-errorProceedings chelli.technical, pages of,2004. MSR[18] ComputingwriteProceedings [40]on, pages CEUR, volume176, [41][19] toringProceedingsstudents' ongimmick.Proceedings (XP2001),pagesComputer, pages [42][20] programming.ACM, 33(1):327331,testingProceedings [43]Technical, pages source2019. experiment.International, pages [21]uk. 120131. knowledgeJournal, 138:5281, [22] of working annual, pages [23] theACM, 34(1):271275, [24] since generatedJournal, 156:312327, 2019. [25]Unit Development.O'Reilly [26]Korean, 70(6):601605, [27] mental Proceedings Education, pages [28] InProceedings Science, pages [29]Unit. Manning, 2020. [30] anEmpirical Software, 26(5):147, [31]xUnit. Pearson Education, [32] Hellendoorn. reliability.Empirical, 2022. [33] and androidProceedings Annual Engineering,CASCON [34] and InProceedings Engineering Engineering,pages


---

