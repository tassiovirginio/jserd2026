<!-- Página 1 -->

2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE) | 978-1-6654-0337-5/21/$31.00 ©2021 IEEE | DOI: 10.1109/ASE51524.2021.9678615

2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE)

## P

## Y

## N

## OSE

Tongjie University Irvine, [tongjiew@uci.edu](mailto:tongjiew@uci.edu)

Jiawei University Irvine, [jiawl28@uci.edu](mailto:jiawl28@uci.edu)

**Abstract****—Similarly** **in called** **detrimental only**also on **code that**majority **test** **Java and Scala.**no **to**Python, **its** **strive**researchdetecting **test** **of** **We** **search** **agnostic have**Python’s **Unittest****framework.**identiﬁed **Additionally,** **mining** **either** **we** **detect**developed **in** **Finally,** **at** **results**suites **the** **Suboptimal****smell** **projects,** **Index****—Test** **studies,**

I.NTRODUCTION

Codewere introduced tainability have been projects associated maintainability While the attributed glingcaring impact applied

*The

978-1-6654-0337-5/21/$31.00©2021 DOI 10.1109/ASE51524.2021.00059

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

## :

##

## Python

**test**

IEEE

Yaroslav JetBrains Saint [yaroslav.golubev@jetbrains.com](mailto:yaroslav.golubev@jetbrains.com)

Timofey JetBrains Saint Saint [timofey.bryksin@jetbrains.com](mailto:timofey.bryksin@jetbrains.com)

Similarlycode also have **.**smells, et deﬁned choices 1Justsmellscases. test recent quality Since productionimportance andmajority smells Java recent beingMachine Learning**Suboptimal****.To** **Y****N****OSE**empiricalsmells,to be lackit. theno existence nosmells this In aim to ofPython,their and We different test analogous work.identiﬁed diverse test differentit thatowndiscover them, used

1To languageswill always tests or

593

Oleg Smirnov   Saint [oleg.smirnov@jetbrains.com](mailto:oleg.smirnov@jetbrains.com)

Iftekhar   [iftekha@uci.edu](mailto:iftekha@uci.edu)

YTHON

testand

test

CHANGE

.

Unittestframe-

MINER[18]

test.


---

<!-- Página 2 -->

searchand evaluatedrelationshippresence projects identiﬁedarechange- assertfunctionsUnittestanddefect-proneness more speciﬁcunderstandingthat smells logic.they production togetherSuboptimaltestcomparatively totaltest code istime, theyYNOSE,isWe tendable investigatedcoverage testwe and testsmells smellscode,Investigating projects 84%testhas RompaeyOverall, contributions ofproposed•Wecompiled techniquesaare analyzed relationshipdevelopment•Wesmell ﬁxture possible smellslyzingcode asmells•WeYNOSEas plugin evaluatedsmellsPyCharm can smells projects.YNOSEisthat standardUnittestframework. baseddetectingavailable researchers Compared[https://github.com/JetBrains-Research/PyNose](https://github.com/JetBrains-Research/PyNose). bytextual-based•We techniquetest smells.Python TSDETECTcapableThe Moreweexisting helpsmells.detectionchoice antestPython search Python-speciﬁc tiontestwedevelopment APIs.beYNOSEandP usedthewe automatedaswe asJavaofconclude ´Virgpaper discuss suite quality II.ELATEDWORKonethe Similarlycodesmells followingOverall, majoritybeen Deursentestassmellsfocusingbeen thatgrowing cases alsosmells.Science Machine researcherscatalogbest knowledge, theidentifyingsmells. inFurthermore, domains. example,smellsprevalencestudy Scalathegap inidentiﬁed smells. III.Researchersnegative Theidentifypacts ofsoftware test[12], [13],empirical extent prevalentetwidely generalthroughout Section welistsmellsstrong

594

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

code metrics

ELECTING

´

-based

YNOSEaddresses

TESTSMELLS


---

<!-- Página 3 -->

**®�������UUU**

**�������ñ����������ñ����������** **���������������������ñ�����ñ��** **�������ñ�������ñ�������**

**’��������£�������������������������** **�����������������ñ����ñ�������** **�ñ�����£��������������**

conducting thenlist smells

A. As ping in ofavailable about SearchOur lows:What smells SearchTooptimal keywords, conducted digitalACM. to Wequeryabstract publicationﬁnalized is

**Title**: (“test “test

Data Source.Toused three of DigitalScopus. SearchTo we list were InitialOur resulted next, wepublications part of inclusionexclusion criteria The signiﬁcantly, some ballingi.e.,looking lists In snowballing. To study

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

**U���������£�u�����ñ���������** **����������ñ�����������������������**

**Ùñ���ñ���£�u��������ñ��ñ���** **��ñ��ñ�������������������������**

Fig.

**Abstract**

**®�������UÙ****®�������Ù**

**®�������������ñ�������������** **����������£����������**

**®������������������������������** **����������£����������**

TABLE I NCLUSION

**Inclusion**

1.implement approaches, practicesrefactoring. 2.

**Exclusion**

1.are 2.grey 3. 4.available 5. associated 6.

selected ofdiscussed reachedﬁnally 29 inof smellsAndroid: fullsmells supplementary Next,possibility test of smells be The Resource[9] objectits in according the Python” Theis beingForEager Test[9], ﬁles test-to-codea approaches a a difﬁcultsupport smells

595

.

For

open()

[9]

File

is

Lazy


---

<!-- Página 4 -->

Thetest executed.ForTest tothe analysis smellspracticalhad to exclude Finally, selectedimplementing. list **Assertion**occurs ple withoutreadability, standability, maintainability, totest **Conditional**runstest need to execute code. test in **Constructor**is unawaresetUp() thecases. wouldsuite, in **Default**occurssuites when projectdefault name. example, MyTestCase. fortests and Not testdefault container cases. also cause the **Duplicate**occurs condition **Empty**occurscontain executablepossibly debuggingthen forgotten mented code **Exception**occurs test throwing cial assertRaises()function **General**occurs general some cases ﬁxture of test test serves of being when **Ignored**is possiblecases nored cases unnecessary complexity making **Lack** groupedsuite sionindicates

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

[9],necessary

method contains

occurs

and acan maintainability **Magic**occurs casei.e., eters instead **Obscure**occurs tooactual purpose should **Redundant**occurs assertionare or and **Redundant**occurs within in automated **Sleepy**occurs executioncase ( i.e., execution. unexpectedvary on **Test**was scribed suite a ause test is beforeit needed **Unknown**occursno inuse assertions, and During selection, onUnittesttesting thea third-partyPyTest however, smells frameworks, it out them all.two reasons choosing Unittest. frameworks[44]. Secondly, nally inspired[41], which testwere JUnit, severalsuites Unittest, therefore

B.smells

In asdiscoverw Python-speciﬁc smells, HANGEMINER[18]C the in

596

General

[42]

Unittest

de-

Robot[43],

YTHON-


---

<!-- Página 5 -->

1)To to a GitHub of it, previously toolwith of selected ﬁlter outalso only Pythonare in 10,000. reason is ofsimply populardata type Next, analyzed history commitsPython ﬁle deﬁnedﬁle ﬁle that wordtestina naming the [41]. have byword in checking to testing,suites test andtesting 4,580at commit such these 4,580 changespracticaldecided select inselected commits,ﬁrst commit no projects. thethis Primarydataset;[36]. 2)To smells, startedhistories projects ﬁnding that test extractedﬁles from theprojects processed YTHONCHANGEMINER[18].P YTHONCHANGEMINERisdevelopedP mining based Java. The parserthe syntaxtheir worksdirectly reuse tool.algorithm language-speciﬁc, trees (AST)change, why

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

test

.pyextension

inof

test

changed

ofYTHONCHANGEMINERis Nguyen YTHONCHANGEMINERworksP change versionsafter change parsed a ﬁne-grained(fgPDGs). aredatanodes literals,operationnodes operations,controlnodes if,while,for, typescontroledges acontrolnode and itdataedges the specifying Then,fgPDGs and change connectedmap edges,change. GumTree versions afterconnect mapedge.therefore, thischangethat change ourﬁnda graph YTHONCHANGEMINERinvolvesThe searching done similarly ofalso connected withmapedge are are ternminimum, minimum frequency,minimum the what is patterns detectcorpus In use al.:minimumof andof possibletesting different Weamaximumthreshold done to growing large.our analysisthe majoritysmall. theDepthpattern contains patterns 20 muchare focus in YTHONCHANGEMINER3)In wasPrimary dataset.cross-project,

597


---

<!-- Página 6 -->

**V****HOI�****DVVHUW7UXH****��*5����****�LQ** **V****HOI�****DVVHUW,Q**

(a)

**V****HOI�****DVVHUW7UXH****��IRR�** **V****HOI�****DVVHUW,Q**

(b)

**V****HOI�****DVVHUW7UXH****��SDVVZRUG�****�LQ** **V****HOI�****DVVHUW,Q**

(c)

Fig. GitHub.

they 159 of changeseither ble reason they Along also commitrationale a Afterauthors and Of changes shown camethe speciﬁc because various datanot itself. example, of ofnumpyarray.important, are directly We categories, i.**Assertion**logic.Often, veloperscase, theexample,occurred inassertEqual toassertRegex.an exact equality expressioncan commitUse jsonschema.ValidationError[55]. Another assertEqualtoassertIn,one correct of commonassertIsNone anotherassertIsInstance. checkobject but commitNullSort None.

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

ii.**Assertion**logic **more****appropriate** A tionreplacing acode eight such speciﬁc they rely heavily assertionUnittestsupports. The curs assertTrue(X Y)toassertIn(X,. mitchangeUse speciﬁc‘in’ checks. ‘assertTrue(blah you andinstead. tests these[54]. This thebe smellmake infer the itsmake Another ity andassertFalse(X Y)to assertNotEqual(X,.assertTrueis changedexample, differentassertTrue(X Y)is Unittest’sassertLessEqual(X,. sageUse unit[57]. Inpractice of boolean value so more interpretable, patternassertEqual(X,is assertFalse(X). In messageschanges change pattern. believe sideringUnittest as testcalled smellSuboptimal. iii.**Assertion**logic **less****appropriate** Interestingly, move one.be treated The amore speciﬁcassertIsNotNone(X)to assertNotEqual(X,. scribes changeFix forto ity[58]. However, changes 2014–2015, sinceNone is Atwo ferentassertNotIn(X,[56].

598


---

<!-- Página 7 -->

**IÂU�����**

**iñ�����£� �ñ��****i������������������** **���IÂU�����****����������£� �ñ��****£ñ��������£®U���������** **€��������****£ñ����ñ������������** **�ñ����ñ�������������****�ñ��������������ñ��������** **������ñ����������****�����£®UH�����������** **������ñ��������������****�������ñ����ñ���****iñ�����£� �ñ��****®ñ�������������** **��������ñ��������****�����ñ�e®€u����**

**iU�����**

Fig.YNOSEoperationCLI mode.

toassertTrue(X Y)andYNOSEtowhich ferentassertLess(X,ample,Magic, toassertTrue(X.visitorPyCallExpressionto assertions, foundassertGreater(X,andand assertIsNone(X), commitre-PyNumericLiteralExpression. move fancy assertions unavailable[59].Magicsmell For literature, implementedIn theirdescribedther originalexample,laropposite weObscuretheifassertLess, etnumberitassertGreater, testcaseresulted largerLack ofconsideredSuboptimaltest ofthelist calculating YNOSEIV.Detectionsmells inworks,Oncelist smells detectiontionto code entities YNOSEindeveloped example,@unittest.skip()decoratorthatlanguage-agnostic @Ignoreannotation.from theone touscan from baseditsthethe the the YNOSE.shows YNOSEcanWhenexplain testIDEfor furtherA. B.YNOSEisP popularWe supportsGraphicalnessYNOSEinsmells. InterfaceandCommandare YNOSEusesmode.portedown validation (PSI)Wedid builtthePrimarydataset. andprojecttotag opened theuses PSItypes related.pyﬁlesof thePSIFileobjects.statisticsTo Next,Pythonensure sub-classesunittest.TestCase. helppaperdiscussed YNOSEcanunittestorPSI,afterwardsthe unittest.TestCaseunderexperienceto notunittest.TestCase.years, lectingsuites,YNOSEoncom-Next, ingPsiElementVisitortopared resultscalculated createthePsiElement,recall,smell. also calculated

599

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.


---

<!-- Página 8 -->

TABLE THE.CITATIONS.

**Assertion**Aassertion **Conditional**Aori.e.,if,for,while). **Constructor**A__init__method). **Default**AMyTestCase. **Duplicate**Aassertion **Empty**A contain **Exception**Atry/exceptstatementraisestatement. **General**NotsetUp()method suitecases suite. **Ignored**A@unittest.skipdecorator. **Lack**Thecases suite≤0.4. **Magic**Acontains **Obscure**A **Redundant**Athethe same,e.g.,assertEqual(X,or assertionone.g., assertTrue(True). **Redundant**Aprint()function. **Sleepy**Atime.sleep()function **Suboptimal**Aof **Test**Atest does useSetUp()method. **Unknown**A contain

TABLE HETHE.**I NST****.**STANDSTIGHTPYNOSE.THEE INDICATESTESTCOLUMNSTESTING,SUITES,AND THE.WITHUnittest.

**Test****Project**

Assertionali1234/vhs-teletext Conditionalcea/secivre1 Constructordavidhalter/jedi Defaultdemisto/content Duplicatejustiniso/polling EmptyLagg/steamodd Exceptionplamere/spotipy Generalpygridtools/drmaa-python Ignored **Total**37Lack of Magic Obscurethesmells Redundantwithnumber Redundant smellSleepy areSuboptimal TestSeveral Unknownvalidation **Weighted**—**94.0%**example. tothese smells just these test smellseasyhavingAssertiontestYNOSE toDefaultrequires tool tofailed PYNOSEalso name suite,ConstructorrequiresConditionaltest tool__init__method,isi.e.,if, andSleepysimply thesleep()functionfor, the case.example,forstatement be AsPYNOSEachievesvariable suchConditional correctnessYNOSE.Lack ofrelies theTestby differentcases tool didYNOSEmeasurescohesivenesssuite. achievecohesiveness usedInAssertionwas YNOSEandbetweenof non-conventional case, ratersMagicwerestarted_symboltestas* notcomparisonthesuch

600

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.


---

<!-- Página 9 -->

assertionsare ForassertEqual(df.shape, taggedMagictest YNOSEfailedhowever, incasesUnknownturned false positives.test assertions,present, from thepytestframework. For smellsYNOSEachieves of the between obtained reported TSDETECT[29], a the similar, thorough direct

TABLE THEPERFORMANCEPYNOSE AND

**Detector**

**TS****D****ETECT**[29] **P****Y****N****OSE**Python

V.REVALENCETESTSMELLS

AftervalidatingYNOSE, conducted empirical projects.the of

A. Thesmell YNOSE.in the test smellsdecided presencePrimarydataset useddecided becausePrimarydataset Pythonuse However,results robust do wetool on Tosame Sectioncondition we and 239 willSecondarydataset. draw ourPrimarydataset, it theSecondarydataset the are

B. YNOSEon projectsPrimaryWe Secondarydatasetsdropped results not

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

suitescase ﬁles with wasone granularity:Constructor Fixture,Lack ofmanifest suite as smells Testarecase level. We ity. suite test a andUnittestitsuites test granularity suite, andone test calculated asmells Wemostleast DETECT. smells, Suboptimal. ofsmellssuites discussed thesmells.

C. In of smells 1)In testof Primarydataset calculated YNOSEdetected ﬁles, suites,projects, andcases.presented in Ittable projects ourﬁletest one5.8

TABLE THETHETESTING

**Test**

**Minimum**11 **Mean**36.9 **Maximum**323

2)The test that smells are them are test the one andConditionalare smells occuruse thePrimarydataset.smells areMagic,General andOn of rarelyEmpty of suites,

601

,Default,General

Conditional

Unittest

.

Assertion

Unittestin

,Unknown.

occurs


---

<!-- Página 10 -->

**Assertion Roulette****52.4****89.9** **Conditional Test Logic****31.9****89.5** **Magic Number Test****26.9****79.8** **General Fixture****24.1****75.4** **Unknown Test****22.5****81.5** **Duplicate Assertion****17.4****78.2** **Suboptimal Assert****15.4****70.6** **Test Maverick****11.4****68.5** **Lack of Cohesion****10.5****74.2** **Exception Handling****64.9****8.6** **Obscure Inline Setup****5.9****46.0** **Ignored Test****3.0****29.4** **Redundant Print****2.9****37.9** **Sleepy Test****1.4****23.8** **Redundant Assertion****26.2****1.0** **Empty Test****0.7****17.7****Primary dataset** **Constructor Initialization****0.3****9.7****Secondary dataset** **Default Test****0.02****0.8**

**0****0**

**% of test suites****% of projects**

Fig.smellstestPrimaryandSecondarydatasets. useUnittest, numbersPrimarydataset.

**25**areamong Constructoroccurs **20**0.3% of suites.smells occursonly suites **15**them,Default.our Suboptimalsmell Python smells:**10** projects 15.4% suites. **% of test suites** Instudy An-**5** droidthe test **0** **0123456789101112**has **Number of different t****est smells in a test suite**herein smellException Fig. Handlingthatonly inindividual suites. of suites.Unittestsupportsof each doessertionsassertRaises,assertRaisesRegexand ofothersuserstry/except co-occurrencekeywords FigureItPrimarydataset co-existsuites.onlyandSecondarydataset 16%remainingonlyObscure, of suitessmell:whichSecondarydataset. oneSuboptimalareour andamountresultsPrimarydataset occurringOverall, results various smells Primarydatasetsuitelent occur testsuitemore than abe to mostsmells,considered empty cases,try/excepttoto ofYNOSEcaninhope in tests. ItassertEqual(X,usedresearchers assertTrue(X).of such3)In Figurediscussed smellssuitessuch

602

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

instead

instead


---

<!-- Página 11 -->

havingsmellsbothreproducibility maintainabilitybecomeof Weco-occurrenceItYNOSEto pairs of allits thesynthetic performed test smelldata completelyisEmpty( i.e.,One noUnknown( i.e.,test hasTeston in testaGeneralis ture.TestoccursasetUp()this method thecase use of VII.ONCLUSIONSANDFUTUREWORKthere is method does whichGeneral. Test prevalentconnectedAssertiondue languageshavetosuite aDuplicate, onanAssertionin InYNOSE, ﬁrst tool forbeexplicit smellAssertionis 18messages), since from testmessages,become inwe testSuboptimalsame goesRedundant,suites AssertbymostwithAssertion. ﬁlessense, YNOSEisashouldis capablesmells95.8%This recall, withsmells testexplored smells HREATSVALIDITYVI.and suitessmell them.smellsAssertionWhilestudy Roulette,Conditional,Magic.Weworked alsoproposedSuboptimalthat Assertsmellsection asIt possible systematic Futuretestmissed applicable •Supporting smells,relyto productionbeingYTHONCHANGEMINERdoes •Discoveringsupportit awe parametersof also relied •ConductingYNOSEthe to example,TSDETECTthatthatfor withHowever, tool supports tools togetherand andstandpointYNOSEisaddition, distribution.add smells •Analyzing smellThe datasetinPython-speciﬁcprevalence ittest correlate coveragesourcemight generalize allPYNOSEisuse IDE twoPrimaryandSecondary) ourfor tasks thatall thebelieve similarityable: [https://zenodo.org/record/5156098](https://zenodo.org/record/5156098).

603

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.


---

<!-- Página 12 -->

[22]

### R

EFERENCES relativesmell,” Conference[1] K.Refactoring: [23]code. andsuites,”[2]Shepperd, Roumeliotis, Internationalempirical Techniques.tainability,”JournalSoftware, [24]C.2003. testProceedings[3]smells class Scala,error probability [25]W.Journalsoftware, anddistribution [4] android commitusProceedings Annual the. Engineering, ACM, ´ R.[26] [5]N. I. and ceedings inProceedings international 2019, softwaremeasurement. [27] pp. detection [6]Y.andIEEE signiﬁcant smallACM Transactionsno. Engineering Methodology,[28]A.smell [7]C.tion impactProceedingsConference Workshop.2018, [8][29]W. andandsmells (andsmellsIEEEinProceedings Engineering,EngineeringSymposium [9]G.Engineering, toring code,”Proceedings[30] onﬂexible“Just-in-time smellrefactoring: (XP2001).Proceedings [10]hension, empiricalsmells their[31] on2012 28th IEEEI.assertion on.identiﬁcation [11]Symposium “On2018´ L.[32] IEEEEvolutionI.smell (ICSME).Brazilian [12][33]P. testEmpiricalengineering systematic Engineering,[34] [13]and andinternationalevaluation smells,”Proceedingsengineering, on,[35]et, [14]inEBSE ofsmells,”2013 IEEEReport. Conference.[36] 2013,[Online]. [15] Bleser,[37] and2019 IEEE/ACM[Online]. 16th.[38]oth, IEEE,conceptual [16]6th Mainin learning, artiﬁcialInformation,A.acs,[39] 2020.method [17]17th python,”App. Systems.,[40]K. methods[18] tionalManipulationfrom the trenches:arXiv (SCAM).arXiv:2105.10157, [41]python.[19]professional [Online].developers. [42][20]The Available:O’Reillypractices. [43][21]xUnit. [Online].Education,

604

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

2006 22nd .

WASDeTT-1:

Proceedings

2018 IEEE

´ A.

Proceedings ,

Proceedings , Evidence-based .

Proceedings

acs,beneﬁts 2018 IEEE/ACM

. othy, “Testroutes: Proceedings

2015 IEEE

Pro- ,

,

.

,


---

<!-- Página 13 -->

[44]Python [45] the MSR233–236. [Online]. [46] [Online]. [47]tool create dataset. master/PublicGitArchive/pga-create [48] forProceedings Software, [49] D.92–101, 2014. [50]M. “Graph-based patterns,”2019 IEEE/ACM Engineering, [51]Martinez, Monperrus, “Fine-grained International Vasteras, [52] Obspy.diff the project.

Authorized licensed use limited to: Access paid by The UC Irvine Libraries. Downloaded on January 26,2023 at 01:26:18 UTC from IEEE Xplore. Restrictions apply.

.

,

7719290b8dd6940dd195a195120c075a4f94cf42 Proceedings[53] Numba.diff the ,project. edbb26caad50cd0cc6352e6fe5b84fbd6edaaf9b [54] viewboard reviewboard/commit/1758bf53057ee7b648ace1c557031d9460c88c00 [55] project. f4b6040618dbe9a7edca99d8f6344a316b5b1f10 [56] project. 2b921b19fd5a23bc2e86060c2c12137d63dfe1db [57] python-chess python-chess/commit/944a0e682174ff32a6f9689176aa9016bab44a31 [58] project. gensim/commit/342f10a2472fb22d811a398f5a6d49d1b6a88ab0 [59] requestsACM/IEEE commit/a8555d811df0a4aaf2dd1f083ba0bc71679101ca [60] intellij intellij/psi.html

605


---

