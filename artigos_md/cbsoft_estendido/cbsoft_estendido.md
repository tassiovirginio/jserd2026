<!-- Página 1 -->

**1. Introduction**

The design ever, evolutionary smells and increasing the technical debt of a system. Indeed, sign decisions Izurieta and Bieman 2007, de the application code but also on the testing assets. The cation code though recent not only but also Tufano

Peruma et al. 2020] Pizzini 2022]. For Assertions TASTE tool and structural al. presented for detecting Cohesion of Test Methods comprehensive number JN OSE trees of test cases and identify 19 and 21 types of test smells, respectively.

### TestAXE:

### Automatically

### Refactoring

### Test Smells

### Using JUnit

### 5

### Features

11**Estevan Alexander de Paula****, Rodrigo Bonifácio**

1Computer Science Department University of Brasília (UnB) Brasília – Brazil

**[estevan.paula@aluno.unb.br](mailto:estevan.paula@aluno.unb.br),[rbonifacio@unb.br](mailto:rbonifacio@unb.br)**

**Abstract.**Testsmells have been proven to deteriorate the quality of the test suite of a system, to the point where several different tools have been devised with the objective ofdetectingorsometimesevenfixingthesesmells.Havebeenex- tensively studiedinmorerecentyears,thesesmellshavebeencatalogedand researchershaveproposedaseriesofsourcecodetransformationscapableof eliminating thesesmells.OurgoalinthispaperistopresentT ESTAXE, atool to refactor testsmellsusingthelatestfeatures ofJUnit5.We present anempir- ical assessment ofTESTAXEaccuracy and highlight its current limitations.

andimplementationofasoftwaresystemmightevolvegradually.How- existingreports[Izurietaand Bieman 2007, Eicket al. 2001]show thatduringsuch efforts,wrongdesigndecisionsmighthappen,eventuallyleadingtocode the accumulation of bad de- mightcause thesoftware’s designtodecay [Parnas 1994, Eicket al. 2001, Silva and Balasubramaniam 2012], reflectingnotonlyon impact of code smells in the appli- hasbeenextensively studiedinthelast20years(e.g.,[Sjoberget al. 2013]), researchhasspecificallyinvestigated thenegative impactoftestsmells— onthecomprehensionandmaintenanceoftestsuites[Bavotaet al. 2015], onthequalityofthetestingandapplicationcode[Spadiniet al. 2018, et al. 2016].

Existing toolshavebeendesignedtoidentify[Palombaet al. 2018, andrefactortestsmells[Lambiaseet al. 2020,Santanaet al. instance,theOP OLISHtool identifiesthesmellsBrittle andUnused Inputin JUnittestcases[Huoand Clause 2014]; whilethe [Palombaet al. 2018]leveragesinformationretrieval techniquesontextual featuresoftestcasestoidentifytestsmells.Morerecently,Lambiaseet DARTS(DetectionAndRefactoringofTestSmells),anIntelliJplugin andrefactoringthetestsmellsGeneral Fixture,Eager Test, andLack of [Lambiase et al. 2020].Examplesof tools able to detect a more oftestsmellsinclude(a) DETECTOR[Peruma et al. 2020]and [Virgínioet al. 2020].Thesetoolsusepatternmatchingontheabstract-syntax


---

<!-- Página 2 -->

**smell detection** the literature. **toring. As** types of al. [Santana Although these tools show evidence of the importance of automatic JUnit test smell refac- toring, they do not consider the recent catalog of refactoring recommendations that benefit from the new JUnit 5 features [Soares et al. 2022].

tool that features of using the Section 3 presents the design and implementation of empirical assessment final remarks. T

**2. Background**

According to choices in test smells Virgínio Spadini et al. 2018, the source the smells [Spadini et al. 2018]. prone [Kim et al. 2021].

with a taxonomy and a catalog of test smells [Garousi and Küçük 2018]. Their groups test pendencies. Listing lead the test execution to not run specific assertions [Soares et al. 2022]. compromise the and patterns design and Peruma et al. 2020,

from JUnit describes seven cluding Conditional authors also for our Santana et al. 2020], T AXE—the first catalog [Soares et al. 2022]

Aljedaani etal.presentasystematicmappingstudyonthefieldtestof [Aljedaani et al. 2021],reportingatotalof22toolsavailablein Differently,therearenotsomanytoolstargeting**test smell**refac- alreadymentioned,theDARTStoolidentifiesandrefactorsthree testsmells[Lambiaseet al. 2020];whiletheresearchtoolofSantanaet et al. 2020]refactorthetestsmellsAssertion RouletteandDuplicate Assert.

The goalofthispaperistopresentthedesignandevaluationESTofAXE,Ta (a)supportsdevelopersinthetaskofmigratingJUnittestcasestousethenew theJUnit5testframeworkand(b)identifiesandrefactorsfivetestsmells newfeaturesofJUnit5.Wepresentsomebackgroundinthenextsection. ESTTAXE. We present details of an ofTEST AXE inSection4.Finally,in5wepresentsome EST AXE isavailable at [https://github.com/PAMunb/JUnit5Migration/](https://github.com/PAMunb/JUnit5Migration/)

andrelatedwork

Spadinietal.[Spadiniet al. 2018],“testsmellsaresub-optimaldesign theimplementationoftestcode”andseveralstudiesbringevidencethat mightcompromisenotonlythequalityofthetestsuites[Bavotaet al. 2015, et al. 2019]but alsothe general qualityof software systems[Tufano et al. 2016, Kimet al. 2021,Wu et al. 2022].Forinstance,etal.mined codehistoryoftenopenprojectsandobservedacorrelationbetween Indirect TestingandEagerand theerror-proneness ofproductioncode Kimetal.alsoreportthattestsmellsmakethecodemoreerror-

Garousi andKüçükpresentacomprehensivesurveyontestsmells,contributing  smellsintosixcategories, includingTest Execution, Test Logic,andTest De- 1 shows an example of the Conditional Test Logic smell, which might Sincetest smells qualityofthesystems,itisfundamentaltoprovideguidelines,idioms, thatmighthelpdeveloperstoavoidtakingbaddesigndecisionsaswellas implementtoolsfordetectingandremovingtestsmells[Palombaet al. 2018, Lambiase et al.Santana et al.Pizzini 2022].

The workofSoaresetal.hasshownpromisingresultsofusingnewfeatures 5toremovetestsmells[Soareset al. 2022].Morespecifically,theirpaper featuresofJUnit5thatcanaiddeveloperstoremove13testsmells,in- Test LogicandAssertionRoulette[Soareset al. 2022]smells.The definenewrefactoringsintermsoftemplates,whichweuseasthebasis TEST AXE implementation.Similarlytopreviousworks[Lambiaseet al. 2020, we use pattern matching on abstract syntax trees to implementES -T toolthatimplementsfour(ofseven) refactoringsfromtheSoaresetal.


---

<!-- Página 3 -->

**1** **_****2****void****first****test()** **3****if****(lastContainerId****null)** **4** **5****else****{**

**6** **7** **8** **9**

**Listing 1. Example**of the Conditional Test Logic smell [Soares et al. 2022]

**3. TestAXE**

T ESTAXE wasdevised asatooltoautomaticallydetectandremove codesmellspresent in Javasoftwaretests,especiallythosethatusestheJUnit5testframework without takingadvantageofitsnewestfeatures.ESTTAXE iscomposedoftwosepa- rate parts:aPythonCLIapplicationtopreparetheenvironment,andaprogramtrans- formation tool(hereaftertransformer)—implemented intheRascalmeta-programming language [Klint et al. 2009]-that is responsible for transforming the test code.

**3.1. The**CLI Component

T ESTAXE makes available a CLI application with a thin Python “shell” script to perform a fewbasicstepsbeforecallingtheactualRascalimplementation—thattransformsJava test code.ThisPythonscriptrecognizestwoCLIoptions:thepathoftherepositoryto be transformed,andthenumberofmaximumfilestowhichthetransformationswillbe applied. Therepositoryisassumedtousethegitversioningsystem,astheapplication creates, ifitdoesnotalreadyexist,junit5-migrationabranch andchecksouttoit. After checkingoutthenewbranch,theapplicationfinallycallstheRascaltransformer meta-program implementation.Asthetransformationfinishes,theCLIgetsthemodified 1file list from git and applies an external code formatting tool from Google.

**3.2. The**Rascal Transformer Component

The secondandmaincomponentof ESTTAXE isameta-programthatleveragesRas- cal’spowerfulparsetreegeneratoranditstraversalfunctionstodetectandrefactortest smells, especiallyasetofsmellswhoserefactorwasproposedon[Soareset al. 2022]. These refactoringproposalsarebasedmainlyonnewJUnit5features,suchasnewtest annotations, assertionmethods,andhelpermethods.Thiscomponentalsoimplements transformations forhelpingdeveloperstomigratefromlegacyJUnitcodetoadoptnew features of JUnit 5.

The transformercollectsthefilesofinterestbytraversingthedirectorystructure of therepositoryrecursively. Itthenparsesthefilecontentsgeneratingparsetreesand executes apipelineoftransformations.Transformationsarefunctionsthatcomprisetwo steps: (a)averifyingstepthatcheckspreconditionsand(b)atransformationstepthat refactors atestsmell.Astheoutermostgrammaticalelementisa, transformations areessentiallyfunctionsthattakein**CompilationUnit**aas anargument

1[https://github.com/google/google-java-format](https://github.com/google/google-java-format)


---

<!-- Página 4 -->

and also collects metrics a test case.

**3.3. The**

As mentioned tions. Indeed, metrics during over an names to integers, representing the number of times a transformation has been applied.

is assembled were implemented deals with a sequence of assertion statements grouped together. These are the **Assertion Roulette**

the difference could look of the test is that all of them be executed, if the first one fails, the two last would not even run, making it difficult to test the class as intended.

**1** **2****public** **3** **4**

**5** **6**

offers a method that receives multiple lambda functions and runs all of them, disregarding individual assertion failures while the test method is running. After an adequate results in the code in Listing 3.

**1** **2****public** **3**

**4** **5** **6** **7** **8**

for this

returna**CompilationUnit. As**thetransformerappliesthepipelinefunctions,it todeterminewhichandhowmanytransformationseffectively modified

Transformation Pipeline

before,thetransformationpipelineiscomprisedofacollectionoffunc- weassignnamestothesefunctionsinahashmap,sothatwecancollect thepipelineexecution. Thetransformationisappliedbyiterating associativemappingofnamesandfunctions,whilealsoaggregatingamapof

As transformationsmayinterferewitheachother, theorderinwhichthepipeline mayyielddifferentresults.Forinstance,twoofthetransformationsthat

**AssertAll**and**ParameterizedTest**transformations, whichfix,respectively, the and theTest CodeDuplicationsmells.

Supposing thereisa**Calculator**class witha diffstatic method,whichreturns ofthetwonumbersreceivedasparameters.Atestcaseforthismethod like Listing2.Asthereisacollectionofassertionsbeingmadeandtheintent

**testCalculatorDiff()**

**Listing 2. A**test method for a calculator class.

One possiblesolutionwouldbetoapplythetransformation. JUnit5

it finishes, it provides reportonfailedassertions,ifany. ApplyingthistransformationtoListing2

**testCalculatorDiff()**

**Listing 3.**AtestmethodforacalculatorclassrefactoredwiththeAssertAll **transformation.**

Nonetheless, thereisanother,arguablymoreadequate,solutiontransformation case:the**ParameterizedTest**refactoring. Aparameterizedtestreceives thetest


---

<!-- Página 5 -->

OrderSmell T1

T2

T3

T4

T5

T6

T7

data asparameters,whosevaluescancomefromdifferentsources.Itisthemostade- quate refactoringconsideringrepeatedassertionsofidempotentmethodsusingdifferent argument values. ApplyingthisrefactoringtothecodeinListing2resultsinthecodein Listing 4.

**1** **2****5,****" ,****10,****" ,****3,****"**

**3****public****testCalculatorDiff(int****a,****int****b,****int****c)** **4** **5** **6**

**Listing 4.**Atestmethodforacalculatorclassrefactoredwiththe **ParmeterizedTest**transformation.

With listings4and3,itbecomesclearthatbothtransformationsaremutually exclusive,andthereforetheorderofthetransformationsinthepipelineisdecisivefor the endresult.Table1liststhecurrentsetofAXE transformations,aswellasthe execution order of the pipeline.

TransformationDescription **Table**1. Setof ESTExceptionHandling**ExpectedException**Transformstests transformationswithexceptionparametersto **assertThrows**assertions -**ExpectedTimeout**TransformstestswithtimeoutparameterstoThese transformations are implemented in a modular fashion, each within its own **assertTimeout**assertions module. Intotal,TEST AXE iscomprisedof24files,ofwhich22areRascalsourcecodeAssertionRoulette**AssertAll**Groupssequentialassertionsinsidean**assertAll**call, guaranteeingeveryassertionwillbeverifiedfiles, eachoneisamodule,oneisthePythondriver, andthelastoneisthegooglesource ConditionalTest**ConditionalAssertion**transformsteststhatruntheirassertionsconditionally,withcode formatter. TEST AXE hasover 3750 lines of code.anifstatementwrappingtheirbody,toteststhatarecondi- tionallyrun,byusingthe**@EnableIf("methodName")**anno- tation**3.4. How**transformation works TestCodeDuplication**RepeatedTest**Transformsteststhatarewrappedwithinaforloop,to thathavethe**@RepeatedTest(iterationCount)**annotationTransformations arefunctionsthataCompilationUnitandreturnaCompilatio- MysteryGuest**TempDir**Addsatestparameterannotatedby**@TempDir**,whichisre-nUnit thatmayornothavebeenmodified.ACompilationUnitisasyntaxdefinition solvedintoatemporarydirectory,toteststhatusetempo- reflecting theabstractsyntaxofaJava sourcecode,whichinvolve manystructures(e.g.,raryfiles -**SimpleAnnotations**MigratesJUnit4annotations,including**@Before**,package declaration,imports,classdefinitions).Thesestructuresaretraversedinorder **@BeforeClass**...,intotheirJUnit5counterparts,asto gettothetestmethoddeclarations,sodetectingandfixingsmellsispossible.Thewellasaddingthenecessaryimportsfortheothertransfor- structures are traversed from CompilationUnit to MethodDeclaration.mations


---

<!-- Página 6 -->

This istheunderlyingpaththatistraversedwhenitisnecessarytomodifyor extract data from test declarations, but Rascal enables skipping several intermediate steps in this path through its**visitexpression. In**order to, from a root node, modify or extract information fromanothernodenestedinitshierarchy, onecanuse**visit**theexpression. For instance,Listing5showsanexampleofamethodthatsearchesforthefirst declaration within a class declaration, returning a maybe structure that may or not contain this method declaration.

**1****public****Maybe[MethodDeclaration]** **2** **3****case****MethodDeclaration****return****just(methodDeclaration);** **4**

**5****return****nothing();** **6**

**Listing 5. Visit**expression to access deep nested values inside a node.

Listing 5 shows how, despite how nested a node may be in the parse tree, accessing it isaconcisetaskbyusingtheRascal**visit**expression andpatternmatchingfeatures. When anodematchesthepattern,therearetwodifferentkindsofexecutionsthatmay take place,dependingonhowthecaseiswritten:adirectreplacementofthematched node with the=>operator, or arbitrary code execution, with the ":"which may resolve intoareplacementaswell(whenusinginsertstatement). Bothofthese approaches appear on TEST AXE code.

Listing 6 shows a simplified version of thetransformation that helps developers to migrate test code to JUnit 5. Thistransformation uses the first kind of pattern matching,meaningthatthereisthereplacementofthematchednodebyanother one ofthesametype.Itisalsocommonthatamorecomplex controlflow maybeneces- sary for some transformations, though. Forinstance,**TempDirtransformation requires** two changes in the test code: thereplacement of all of**createTempFile**themethod invo- cations directlyfromtheFileclass,toaFileinstancereceived asamethodparameteron the test method and the addition of a parameter to the testwith this instance as its value. Forthis, a boolean variable may be used to dictate whether**File.createTempFile** method invocationswerefoundsothattheadditionofthetestparametermaybedone later.Listing7 shows the segment of the code that does exactly this.

Another important aspect is that the pattern matching can be done in the AST form or intheconcretesyntaxform,whichisextensivelyusedbyTThe syntax formallowsfortheextractionofnodeelementswithinaformthatresemblesthe actual parsed source and can be seen throughout all of the listings.

**1****public****CompilationUnit** **2****if (verifySimpleAnnotations(unit))** **3** **4****case****(MethodModifier)**` @BeforeClass`**=>**` @BeforeAll` **5****case****(MethodModifier)**` @Before`**=>**` @BeforeEach` **6**

**7** **8****return****unit;** **9**

**Listing 6. Direct**replacement example in the SimpleAnnotation transformation


---

<!-- Página 7 -->

**1****private****MethodDeclaration** **2****false;** **3** **4****case****(MethodInvocation)**` File.createTempFile(<ArgumentList` : **5****true;** **6**` tempDir.createTempFile(<ArgumentList` ); **7** **8** **9****if (tempDirUsed)** **10**` @TempDir` ); **11****return****method;**

**12**

**Listing 7.**ArbitrarycodeexecutioninthepatternmatchintheTempDir **transformation.**

**4. Empirical**Assessment The goalofthisempiricalstudyistoassesstheaccuracyESTof AXETtransformations. Overall, we pose the following research questions: 1. Outof all the transformations that were applied, how often were they correct? 2. Wereany of the transformations applied when they should not? 3. Outof all the refactoring opportunities, how often were they detected? These questionscanbeansweredbytwometricsthatweremeasuredconsidering the output files TEST AXE produce:P recision, which measures how correctly the trans- formations were applied, andRecall, which measures how frequently were the refactoring opportunities taken. Thecomputation of these metrics is as follows:

T PT P ; Recall=P recision= T P +F PT P +F N

In whichT Pstands fortruepositives,F Pfor falseandF Nfor negatives.Foran overall performance, we calculate the F1-ScoreF),(is computed1 as follows:

P recision×Recall F= 21 P recision+Recall

WeapplytheTEST AXE transformationoveracurateddatasetof38JUnittest cases. ThesetestcasescomefromastudybasedonpullrequestsfromSoaresetal. 2[Soares et al. 2022].

**4.1. Results** Table2showstheresultsofourempiricalstudy. Notethatouroutlineacareful, in thesenseofnottakinganyrisks,butnotacompletesetoftransformations.Since P recisionis1 , itmeansthattherewerenofalsepositivecases,butthedownsideof this carefulnessappearswhenlookingatthemeasuredvalueRecallof, showingroom for improvementsinsmelldetection.Thatisespeciallytruefor**ParameterizedTest**the transformation, which was frequently present on the false negative transformations, while not appearing once on the true positive. 2[https://github.com/easy-software-ufal/refactoring-test-smells-with-junit5](https://github.com/easy-software-ufal/refactoring-test-smells-with-junit5).


---

<!-- Página 8 -->

**Table**2. Smell/Transformations metrics

SmellTransformationTPFPFNPrecisionRecallF1**4.2. Limitations** AssertionRoulette**AssertAll**9704110.700.83 ConditionalTest Logic**ConditionalAssertion1**0210.340.5The detection of smells can be rather naive. Forinstance, theof the DuplicateAssert**ParameterizedTest**0021000**Test Logic**smell isasimpleverificationofamethodbodywrappedinsideanif.Even MysteryGuest**TempDir**100111if theassertionsareallinsideifstatements,asshowninlisting8,therefactoringwon’t TestCode Duplication**RepeatedTest**400111apply if there are any statements outside the if statement. OverallResult-10306410.620.76 **1** **2****public****conditionalTestWithPrecedingStatements()** **3** **4****if ( true)** **5****" something",****" );** **6**

**7**

**Listing 8. Undetected**conditional test logic due to method invocations before the **if statement**

That is also true for the**Test Code**Duplicationsmell, if there are any statements outside the for loop, the smell is not detected and therefore, the refactoring is not applied. For this same smell, for test correctness sake, the transformation is not applied if there are any methodcalls,oreven valuesthatarenotliterals**integers**(,**booleans,****strings, ...).** Listing 9 shows an example of smell that would not be detected.

**1**

**2****public****testCodeDuplicationWithMethodInvocationAssertion()** **3** **4** **5** **6**

**Listing 9.**UnconsideredTest CodeDuplicationsmellduetomethodinvocation **inside the assertions**

**5. Final**RemarksandFutureWork

This paperdetailsthedesignandimplementationofESTT AXE, atoolthatrefactors legacy JUnit code smells using the new features of5. Currently,EST AXETsupports five (of seven) refactorings that Soares at al. detailin their paper [Soares et al. 2022].We empirically evaluated TEST AXE andfoundthatitpresentsareasonableaccuracyFof(1 0.76), thoughthereareblindspotsthatleadESTTAXE tomisssomeopportunitiesfor removing test smells.


---

<!-- Página 9 -->

First, we want to improve the accuracy of cases that implement the remaining transformations detailed in [Soares et al. 2022]. at conducting a case study with one of our industry patterns.

**Declaration** Most of this work has been conducted by the first author of this paper (Estevan Alexander de Paula), neering (at the University of Brasília).

**References** Aljedaani, W., Peruma, man, C. mapping study. In page 170–180, New York, NY, USA. Association for Computing Machinery.

Bavota, G., smells really harmful? an

de Silva, L. A survey. Testing

Eick, S., assessing the evidence from change management data. Engineering, 27(1):1–12.

Garousi, V. and in industry and academia.

Huo, C. and unused Symposium on York,

Izurieta, C. and Bieman, J. M. (2007). How tern evolution. In and Measurement (ESEM 2007)

Kim, D. study on test smell evolution and maintenance.

Klint, P., van der Storm, T., and Vinju, J. J. (2009). RASCAL: for source code analysis and manipulation. In ference on Canada, September 20-21, 2009

Lambiase, S., time test smell detection and refactoring: The International Conference on Program Comprehension York,

As futurework,weintendtocomplementthisresearchinthreemaindirections. ESTTAXE, so that it could deal with the corner areharmingitsoverallperformanceonfixingtestsmells.Second,wewantto Finally, we aim

duringhisfinalyearprojectasanundergraduatestudentinComputerEngi-

A.,Aljohani,A.,Alotaibi,M.,Mkaouer, M.W., Ouni,A.,New- D.,Ghallab,A.,andLudi,S.(2021).Testsmelldetectiontools:Asystematic Evaluation andAssessmentinSoftware Engineering, EASE2021,

Qusef,A.,Oliveto,R.,Lucia,A.D.,andBinkley,D.W.(2015).Aretest empirical study.Empir.Softw. Eng., 20(4):1052–1094.

andBalasubramaniam,D.(2012).Controllingsoftware architectureerosion: Journal ofSystemsandSoftware, 85(1):132–151.DynamicAnalysisand of Embedded Software.

Graves,T.,Karr,A.,Marron,J.,andMockus,A.(2001).Doescodedecay? IEEE Transactions on Software

Küçük,B.(2018).Smellsinsoftwaretestcode:Asurvey ofknowledge J. Syst. Softw., 138:52–81.

andClause,J.(2014).Improvingoraclequalitybydetectingbrittleassertions inputsintests.InProceedingsofthe22ndACMSIGSOFTInternational Foundations ofSoftwareEngineering, FSE2014,page621–631,New NY, USA. Association for Computing Machinery.

software designs decay: Apilot study of pat- FirstInternationalSymposiumonEmpiricalSoftwareEngineering , pages 449–451.

J.,Chen,T. P., andYang, J.(2021).Thesecretlifeoftestsmells-anempirical Empir.Softw. Eng., 26(5):100.

A domain specific language IEEE International Working Con- Source CodeAnalysisandManipulation,SCAM2009,Edmonton,Alberta, , pages 168–177. IEEE Computer Society.

Cupito,A.,Pecorelli,F.,DeLucia,A.,andPalomba,F.(2020).Just-in- darts project.ProceedingsInof the 28th , ICPC ’20, page 441–445, New NY, USA. Association for Computing Machinery.


---

<!-- Página 10 -->

Palomba, F., Zaidman, A., and De Lucia, A. (2018). Automatictest smell detection using information retrieval techniques.In2018 IEEEInternationalConference onSoftware Maintenance and Evolution (ICSME), pages 311–322.

Parnas, D.(1994).Softwareaging.InProceedingsof16thInternationalConference on Software Engineering, pages 279–287.

Peruma, A.,Almalki,K.,Newman,C.D.,Mkaouer,M.W., Ouni,A.,andPalomba, (2020). Tsdetect:Anopen source test smells detection tool.ProceedingsInof the 28th ACM JointMeetingonEuropeanSoftwareEngineeringConferenceandSymposium on theFoundations ofSoftware Engineering, ESEC/FSE2020,page1650–1654,New York,NY, USA. Association for Computing Machinery.

Pizzini, A. (2022). Behavior-based test smells refactoring : Toward an automatic approach to refactoringeagertestandlazytestsmells.2022InIEEE/ACM44thInternational Conference onSoftwareEngineering:CompanionProceedings(ICSE-Companion), pages 261–263.

Santana, R.,Martins,L.A.,Rocha,L.,Virgínio,T.,Cruz,A.,Costa,H.A.X., Machado, I.(2020).RAIDE:atoolforassertionrouletteandduplicateassertidentifi- cation andrefactoring.In 34th BrazilianSymposiumonSoftwareEngineering,SBES 2020, Natal, Brazil, October 19-23, 2020, pages 374–379. ACM.

Sjoberg, D.I.,Yamashita, A.,Anda,B.C.,Mockus,A.,andDybå,T. (2013).Quantify- ing theeffectofcodesmellsonmaintenanceeffort.IEEE Transactions onSoftware Engineering, 39(8):1144–1156.

Soares, E.,Ribeiro,M.,Gheyi,R.,Amaral,G.,andSantos,A.M.(2022).Refactoring test smellswithjunit5:Whyshoulddeveloperskeepup-to-date.IEEE Transactions on Software Engineering, pages 1–1.

Spadini, D.,Palomba,F., Zaidman,A.,Bruntink,M.,andBacchelli,A.(2018).On relation of test smells to software code quality.2018InIEEE International Conference on Software Maintenance and Evolution (ICSME), pages 1–12.

Tufano,M., Palomba, F., Bavota, G., Di Penta, M., Oliveto, R., De Lucia, A., and Poshy- vanyk, D.(2016).Anempiricalinvestigationintothenatureoftestsmells.Pro-In ceedings ofthe31stIEEE/ACM InternationalConference onAutomated Software En- gineering, ASE2016,page4–15,NewYork, NY, USA.AssociationforComputing Machinery.

Virgínio,T.,Martins,L.,Rocha,L.,Santana,R.,Cruz,A.,Costa,H.,andMachado, (2020). Jnose: Java test smell detector. Inof the 34th Brazilian Symposium on Software Engineering, SBES ’20, page 564–569, New York, NY, USA. Association for Computing Machinery.

Virgínio,T., Santana, R., Martins, L. A., Soares, L. R., Costa, H., and Machado, I. (2019). On theinfluenceoftestsmellsontestcoverage.ProceedingsInoftheXXXIIIBrazil- ian SymposiumonSoftware Engineering, SBES2019,page467–471,New York, NY, USA. Association for Computing Machinery.

Wu,H.,Yin,R.,Gao,J.,Huang,Z.,andH.(2022).Towhatextentcan quality beimproved byeliminatingtestsmells?InInternationalConference on Code Quality (ICCQ), pages 19–26.

F.

and

the

I.

code


---

