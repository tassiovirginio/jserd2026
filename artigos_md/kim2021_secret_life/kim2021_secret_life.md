<!-- Página 1 -->

**Noname manuscript** (will be

### The Secret

### on Test

**Dong Jae** **Chen**

Received:

**Abstract** the impact empirical evidence nance and we conduct the evolution to software instances increases, ever, our test smell 45% of while developers of largely shows that post-release defects crease in post-release defects. test smells focusing on the speci c with defect-proneness

**Keywords**

**1 Introduction**

In modern changes to

Dong Department E-mail: fk

No. insertedbytheeditor)

### Life

### of

### Test

### Smells

### -

### An

### Empirical

### Study

### Smell

### Evolution

### and

### Maintenance

Kim**Tse-Hsun (Peter)** **Jinqiu Yang**

In recentyears,researchersandpractitionershavebeenstudying oftestsmellsintestmaintenance.However,thereisstilllimited onwhydevelopersremovetestsmellsinsoftwaremainte- themechanismemployed foraddressingtestsmells.Inthispaper, anempiricalstudyon12real-world open-sourcesystemsto andmaintenanceoftestsmellsandhowtestarerelated quality. Resultsshowthat:1)Althoughthenumberoftestsmell testsmelldensitydecreasesassystemsevolve.2)How- qualitativeanalysisonthoseremovedtestsmellsrevealsthatmost removal(83%)isaby-productoffeaturemaintenanceactivities. theremoved testsmellsrelocatetoothertestcasesduetorefactoring, deliberatelyaddresstheonly17%oftestsmells,consisting ExceptionCatch/ThrowandSleepyTest. 3)Ourstatisticalmodel testsmellmetricscanprovideadditionalexplanatorypoweron over traditionalbaselinemetrics(anaverage of8.25%in- AUC).However, mosttypesoftestsmellshaveaminimale ecton Ourstudyprovides insight into developers'perceptionof andcurrentpractices.Future studiesontestmayconsider types of test smells that may have a higher correlation whenhelpingdeveloperswithtestcodemaintenance.

TestSmellEmpirical StudySoftwareQuality

software development, developersneedtocontinuously implement thesoftwaresystemtokeepupwiththeconsumers'ever-growing

 Tse-Hsun Jinqiu  dongja,g @encs.concordia.ca


---

<!-- Página 2 -->

2

demands. Asasoftware systemevolves, tremendouscollaborativee orttakes place todeliverfeaturesandperformmaintenanceactivities.Duetotheim- portance of software quality, automated regression testing has played a pivotal role insoftwaredevelopment.Newtestcodeisdevelopedtotestthenewly- added SUTcodeandisexecutedaftercodechangestoensurethatthenew changes donotintroducedefects(Aliet al., 2019). Toensurethee ectivenessofregressiontesting,developersneedtomain- tain asetofhigh-qualitytestcasestovalidate software qualitycontinuously. Unfortunately,similartosourcecode,testcodemayalsocontaindefectsand design issues that hinder the quality of the test code.For example, prior stud- ies (Lamet al., 2019;Luoet al., 2014)havefoundthattheresultsofsome test cases may beunreliable (e.g., aky tests) due to defects in test code.Thus far, researchers and practitioners have started to notice recurring design prob- lems in the test code(Spadiniet al., 2018; Van Deursenet al., 2001) and have coined the termtest smell. Like code smells in source code, testindicate potential designproblemsintestcode.Bavotaet al.(2015) foundthattest smells areprevalent insoftwaresystemsandmayhindertestcomprehension and maintenance. Despite thendingsachieved sofar,thereislimitedempiricalevidenceon the awareness oftestsmells.Oneresearchfoundthatdevelopersareaware of test smells and their potential consequences (Perumaet al., 2019), while others found thatdevelopersdonotbelievethebene tofremovingtestsmells(Ju- nioret al., 2020a,b;Tufanoet al., 2016).Therefore,bystudyingwhydevel- opers removetestsmellsfromhowtestareaddressedduringsoftware maintenance, wecanimprovetestcodequalityanddevelopane ectivetest code refactoringrecommendationtool.Studyingthemaintenancewillhelp (1) expandfutureresearch onunderstandingwhatmay promptdevelopersto maintain testcode,and(2)provideevidenceonthemostpaidattentiontest smells. In thispaper,weconductanempiricalstudyonthemaintenanceoftest smell in12large-scaleopen-sourcesystems.Westudyatotalof18di erent types oftestsmellsthatwerede nedandstudiedinpriorresearch(Garousi and Kucuk,2018;Junioret al., 2020a,b;Perumaet al., 2019;Qusefet al., 2019; Spadiniet al., 2018). In particular, we seek to answer the three following research questions: **RQ1: How**dotestsmellsevolveovertime?Weconductaquantitative analysis tostudyhowtestssmellevolveoverthreeyears(from2016tothe beginning of2019)inthestudiedsystems.Althoughwendthatthetotal number oftestsmellinstancesincreasesovertime,thetestdensityre- mains relatively stable in the 12 studied systems after normalizing by the total number oftestcodelines. **RQ2: What**isthemotivationbehindremovingtestsmells?Wecon- duct aqualitativeanalysisofastatisticallysigni cantsampleofthecommits that removedtestsmells.We ndthatinonly17%ofthesampledcommits, developers directlyaddressthetestsmells.Inparticular,aremore likely toaddresstwotestsmells:ExceptionCatch/ThrowandSleepyTest.


---

<!-- Página 3 -->

Title

However,in83%ofthestudiedcommits,thetestsmellsareremoveddueto the deletionoftestcodeorarerelocatedtoothertestcasesduetofeature refactoring activities.Inshort,wendthatdevelopersoftendonotdirectly address thetestsmellswhenmaintainingtestcode. **RQ3: What**istherelationshipbetweentestsmellsandsoftware **quality?Similar to prior work (Chen**et al., 2017; de Paduaand Shang, 2018; Moseret al., 2008;MunsonandKhoshgoftaar,1992),webuildalogisticre- gression modelto study the relationship between test smell and software qual- ity.Sometestsmells(e.g.,Conditional TestLogic,ExceptionCatch/Throw, andMystery Guest) haveanincreasingrelationshipwithasourcecodele's defect-proneness whencontrollingforconfoundingfactorslikethetraditional product, process and coupling metrics. However, most types of test smells have minimal e ectonthedefect-proneness. In summary, ourndingsshowthat,asasystemevolves,developersmay allocate resourcesonmaintainingtestcode,buttheymaynotbeawareof the testsmells.Moreover,sometestsmellshaveaminimale ectondefect- proneness, whileonlyafewtestsmellshaveapositiveimpactondefect- proneness. Futurestudiesontestsmellsmayconsiderfocusingonthetypes of testsmellsthatmayhave ahighercorrelationwithdefect-pronenesswhen helping developerswithtestcodemaintenance.

**Paper Organization.**The rest of the paperis organized as follows. Section 2 describes anoverview oftestsmells.Section3presents ourresearch questions and results.Section4discussestheimplicationsofourndings.5dis- cusses the threats to validity. Section 6 surveys related work. Finally,7 summarizes thepaper.

**2 Background**

2.1 ABriefOverviewofTest Smells

Softwaretestingisavitalcomponentofmodernsoftware development. Test- ing identi esdefectsinsourcecodeearlyonbeforethecouldincur substantial impact(Spnolaet al., 2019).Itiswidelyadoptedtoutilizeunit testing frameworkssuchasJUnitorTestNG toenabletestautomation,i.e., test casesarewrittenintestcode,whichcanbeexecuted.Likesource test codemayalsohavedesignproblemsorevendefectsthathindertest- ing e ectiveness.Therefore,therehasbeenanincreasinginteresttoproperly maintain and improve the design of test code(Levin and Yehudai, 2017; Pinto et al., 2012;Shamshiriet al., 2018).Therefore,researchersandpractitioners havestartedtostudythequalityoftestcasesandidentifyvariousproblems in testcode(Bavotaet al., 2015;Spadiniet al., 2018;VanDeursenet al., 2001). Inparticular,researchershavecoinedthetermtest smellto charac- terize therecurringtestdesignproblemsthatmay impairtestcomprehension and maintainability.


---

<!-- Página 4 -->

4

Table1:Anoverviewofthestudiedtestsmells.Therstsetoftestsmells was rstproposedby Deursenet al.(2001), andinvestigated furtherby other studies onitsdi usionDF[] insoftware systems(Bleseret al., 2019;Palomba et al., 2016), impact on software test codecomprehension**CO**[ ] (Bavotaet al., 2012; Tufanoet al., 2016), developers' awareness of test smells**AW**[] (Peruma et al., 2019; Spadiniet al., 2020; Tufanoet al., 2016) and relation with software quality [QT] (Athanasiouet al., 2014). The remaining test smells are recently studied test smells by Perumaet al.(2019) and investigated on their di usions and developers'perceptions.

**Test****Abbrev.****Description**

Literature(Deursenet,

Assertion explanation. sion[DF/AW/QT]. Eager under maintenance[DF/AW/QT/CO]. General only cute **[DF/AW/CO]**. Lazy method the**[DF/AW]**. Mystery ing tain, them[DF/AW/QT/CO]. Resource the causeaky**[DF/AW/QT]**. SensitivetoStringmethod in implementationtoString[DF/AW/QT/CO].

Recently(Perumaet,

Conditional behavior ConstructorCI tionsetUp(). class structor Empty ExceptionECT Catch/Throwtion using problems

Print tests do thermore, veloper print Redundant either Sleepy testaky Duplicate tiple Unknown ment. IgnoredTest@Ignore. Magic mented which


---

<!-- Página 5 -->

Title

Table1showsthe18di erenttypesoftestsmellsthatweincludeinour study.These test smells are studied in prior work (Bavotaet al., 2012; Bavota et al., 2015;GarousiandKucuk,2018;Junioret al., 2020a;Knuth,1981;Pe- rumaet al., 2019).Inparticular,thecurrentknowledgeoftestsmellsthat we knowfromtheliteraturewasrstproposedbyDeursenet al.(2001), and these wereexpandedasabasisforfurtherinvestigation inrecentstudies.For instance, somestudies(Bavotaet al., 2015;Bleseret al., 2019;Tufanoet al., 2016) foundahighdi usionoftestsmellsinsoftware systems,andsuchtest smells maynotberemoved assystemsevolve. Otherstudiesinvestigated the impact oftestsmelloncodecomprehensionbymeasuringthetimetakenfor understanding thetestcodeinthepresence/absenceoftestsmells(Bavota et al., 2012).Moreover,Athanasiouet al.(2014) studiedtheimpactoftest smell on software quality (correlation with post-releasedefect) to ll the miss- ing gap from numerous prior studies that only underlines its e ects on software maintainability. Numerous researchers also surveyed software engineers to understand their awareness,perception,oridenti cation.Forinstance,arecentstudybyPe- rumaet al.(2019) proposedanewsetoftestsmellsandinvestigatedtheir di usion and awareness. Their result suggests that developers are aware of test smells and their potential consequences. On the contrary, others give evidence that developersdonotbelievesoftware systemscouldgenuinelybene tfrom addressing test smells (Junioret al., 2020a; Tufanoet al., 2016). Nevertheless, there is a lack of empirical evidence on what types of test smell developers pay attention to the most and thereby maintain software evolution. Similarly, there is also missing evidence on the common reasons and mechanisms in which test smells areaddressed.Hence,inthispaper,westudyhowtestevolve and howdevelopersmanagetestsmellsduringsoftwaremaintenance.More- over,wealsoexplorewhethertheexistenceandmaintenanceoftestsmells correlate withsoftwarequality.Therefore,ourworkusesthedetectiontool implemented byPerumaet al.(2019) whichincludethemostcomprehensive type oftestsmellsuptodate,encompassingboththetestfromthe literature andtheirnewlyproposedtestsmells.

2.2 IdentifyingTest Smells

In thispaper,wefocusonstudyingtheevolutionandmaintenanceoftest smells. To identifytestsmells,weadoptatestsmelldetectiontoolcalledts- Detectorimplemented by Perumaet al.(2019) to analyze the studied systems. WechoosetsDetectorbecause it candetect acomprehensive listof testsmells (i.e., 18testsmellsintotal,asdescribedinTable1)andhasanaverageF- score of 96.5% (Perumaet al., 2019). We focuson these 18 test smells because they arerelatedtounittestingpracticesinJava (Perumaet al., 2020),advo- cated inxUnitguidelines(Meszaros,2007),andextensivelystudiedinprior researches intestcodemaintainabilityanddevelopers'perception(Bavota et al., 2012;Junioret al., 2020a).AlthoughGarousiandKucuk(2018)sum-


---

<!-- Página 6 -->

6

marized acatalogof198testsmells,manyaregeneralcodesmellsspeci cto TCN language,comefromgreyliterature(i.e.,blogposts),anddicultto generalize (e.g.,complicatedsetup,long-runningtest,longtestle).tsDetec- toruses JavaParser todetecttestsmellgiven thelistsofthetestlesandthe corresponding sourcecodeundertest(i.e.,CUT). TheCUTlesarerequired to detect speci c types of test smells, suchEagerasTestand LazyTest, whose primary concernsareabouttestingmultiple CUTlesinonetestcase,which may negativelyimpactcodecomprehension. Toidentify each test le's correspondingCUT les, we follow prior studies and utilizethenamingconvention(Chenet al., 2017;Perumaet al., 2019; Spadiniet al., 2018; Tufanoet al., 2016; Zaidmanet al., 2008). In particular, for each testle,weidentifythecorrespondingCUTlesbyremovingthepre x or thesuxof "[Tt]est(s*)"from thenamesofthetestles.Wemanually verify thebuildcon gurationles(e.g.,MavenorGradlele)ofthe studied systems to use the default heuristic speci edby Maven/Gradle plugin to identify test les. The default heuristic matches with the pre x that we use to determinethetestles.ThetestsmelldetectortsDetectortakes thelists of testles,andtheirassociatedCUTlesandreportsany occurrencesofthe 18 typesoftestsmells. AlthoughtsDetectoroutputs testsmellsatale-level,mostreportedtest smells arealine-levelandmethod-level,whichareaggregatedperle.Inthe rest ofouranalysis,westudyeachtestsmellindividually, therefore,attheir respective lineandmethod-level.Furthermore,wemodifythetsDetectorto output therawcountoftestsmellsinsteadofthedefaultbooleanvalue.To encourage thereplicationofourresults,wehavemadethedatasetpublicly 1available.

**3 Case**StudyResults

Werstintroduceourstudiedsystems.Wethendiscusstheresultsofour research questions.For eachquestion,wediscussitsmotivation, the approach weusetoaddressthequestion,andtheresults.

3.1 CaseStudySystems

Table2showsanoverviewofthestudiedsystems.We conductourstudyon several versions ofthe12open-sourceJava systems.Inparticular,we conduct our research in all ocial releases from the beginningof 2016 to the of 2019. We chose the studied systems based on the following selection criteria. First, we selected the top 1,000 Java projectson GitHub ordered by popularity (i.e., stargazercount).We alsomadesurethattherepositoriesarenotforks. Second, wediscardedprojectsthatarebelowthe90thpercentileintermsof size (i.e.,linesofcode),repositorypopularitystars),andthenumberof

1[https://github.com/SPEAR-SE/TestSmellEmpiricalData](https://github.com/SPEAR-SE/TestSmellEmpiricalData)


---

<!-- Página 7 -->

Title

Table2:Anoverview ofthestudiedsystems.

SystemsLOC (2016

Kafka Groovy Camel Zookeeper Cxf Karaf Flink Accumulo Hive Bookkeeper Wicket Cassandra Hadoop

Total

commits. We also remove systems that do not use issue reportsystems. In the end, weareleftwiththese12systems.AsshowninTable3,thereare998 active contributorsintotal(rangesfrom15toover200contributors)inthe studied systemswithawiderangeofexperiences(i.e.,intermsofnumberof commits). In some systems, such as Kafka and Flink, the contributors' median number of commits is relatively high (i.e., 306 and 278 commits, respectively), which shows thatmany contributors areactively contributing tothesystems. In Karaf,ontheotherhand,themediannumber ofcommitsisonlytwo. The studied systemsarewidelyusedbypractitioners,usedinmanycommercial settings, andarelargeinscale,withthenumberoflinesofcode(LOC)in source coderangesfrom6.9Mto9.1M,andtheLOCintestcodefrom 1.1M to 1.6M. Moreover, the studied systems maintain a set of comprehensive test casesandadoptthecontinuousintegrationpracticebyrunningthetest cases dailybasis(Apache, 2020).Thestudiedsystemsalsocover di erent do- mains, from big data processing and data warehousing solutions to distributed databases andprogramminglanguages.

3.2 RQ1:Howdotestsmellsevolve overtime?

Motivation:Prior studies (Bavotaet al., 2015; Tufanoet al., 2016) reveal that test smellsareprevalent insoftwaresystems,andtheirpresencehindersthe comprehension andmaintenanceoftestcode.Inlightofthesendings,there is limitedempiricalevidenceofhowthepervasivenessoftestsmellchanges overtimeanditsrelationtosoftware maintenance. Namely, whilemany other softwareartifacts should inevitably grow as the system evolves, we believe that an interestingimplicationcanbeinvestigatedbystudyingthepervasiveness of testsmellsfromtheaspectofwhetherdevelopersresolvetestdur-


---

<!-- Página 8 -->

8

Table3:Anoverview ofthedeveloperexperienceandthenumberofcontrib- utors inthestudiedsystems.

# SystemsMinContributor Accumulo126 Bookkeeper1835 camel1204 Cassandra2102 Cxf147 Flink1175 215Groovy Hive5112 Kafka20188 Karaf138 Wicket120 Zookeeper336 1373Hadoop

ing softwareevolution.Hence,inthisRQ,wequantitativelyinvestigatethe evolution oftestsmells.

Approach:Tostudytheevolutionoftestsmells,wefollowtheapproach described inSection2.2todetecttestsmellsineach studiedsoftware version. In particular,weapplyatestsmelldetectiontoolcalledtsDetector(Peruma et al., 2019) to analyze the studied systems based on six-month windows from 2016 to2019.Intotal,weobtainsevensnapshotsperstudiedsystem.We consider asix-monthwindowbecausestudyingtheevolutionoftestcodeon a commitbybasisisexpensiveanddilutethemodi cationsoftest smells. Moreover, since the studied systems have di erent sizes and test smells may co-evolve withtheamount ofaddedtestcodeandtheraw number ofthe test smellinstances,wealsoreporttestdensity. We calculatetest density by dividingthenumber oftestsmellinstancesby thetotalof code lines.We usecodelinesasournormalizationmetricsbecausemanytest smells aredetectedatthelinelevel.We alsonormalizedusingothermetrics such asthenumberofmethodsinale,andwefoundasimilartrendinthe result.

Results:Figure 1 shows the time series plots of the averaged test smell density in the studied systems from 2016 to 2019. We present thewith a similar scale of test smell densities in one plot for visualization ease. Averaged test smell density is the normalized testmetrics that is averaged over all studied systems.Weaveragedthetestsmelldensitiestoshowageneralized trend amongst the studied systems. Although not shown, we observe that test smell densityeitherremainsstable(i.e.,BookeeperandGroovy)ordecreases (i.e., Kafka,Camel,Accumulo,Wicket,Hive,Cassandra,andCXF)inmost of thestudiedsystems.WhenobservingindividualmetricsasinFigure1, we ndthatmosttestsmelldensitiesalsostayrelativelystable.However, ignored testsmellsincreasedfargreaterover-timecomparedtoothertest


---

<!-- Página 9 -->

0.0013

0.0011

0.0009

Density

0.0007

0.0005

0.04

0.03

Density 0.02

0.01

Title

l ll0.0015l l

l l

ll0.0012l

l

0.0009l l l Densityl l l

lll l l0.0006 lll lll

lFig. 1: Time series plots that show the evolution of the test smell density (nor-l

llmalized average)of the studied systems. The test smell densities are calculatedllll 0.0003based onsevensnapshotsthataretakeneverysixmonthsbetween2016and 2019.

1/1/20167/1/20161/1/20177/1/20171/1/20187/1/20181/1/2019 TimeTime smells. Figure2showstheevolutionoftherawtestsmellmetricsaveraged overallofthestudiedsystems.Ingeneral,we observe thatalloftheaveraged CIMGPSRASEraw testsmellmetricsincreaseover-time, butnormalizedtestdensities remain relativelystable. Wefurtherinvestigate thechange inthemagnitudeoftestsmellinstanceslll lll(i.e., rawcounts)andtestsmelldensitybetweenthetwosnapshotstakeninlll llLTDAROl2016 and2019.Table 4showsthechangeinthemagnitudeofthetestsmelll ldensity,andsimilarly, Table 5showsthechangeinthenumberoftestsmell0.006 instances (rawcounts).AsshowninTable 4,thetestsmelldensitydecreases for mosttypesoftestsmells.Onthecontrary,wendthatthetestsmell instances' raw counts increase for most types of test smells (Table 5). Namely, l llllllll l l0.004 ll Densityll

lllllll0.002

lllllllllll

1/1/20167/1/20161/1/20177/1/20171/1/20187/1/20181/1/2019 TimeTime

EGECTARGFUTMNT

l

l

l

l

ST

l

l

l

l

l

l

l

l

l

IT

l l

l

l

l

l

l

l

l

l l

l

l

l


---

<!-- Página 10 -->

150

100 Density

50

5000

4000

3000

Density

2000

1000

10

l

ll

l200 l

l

l

l l l lll150 l

l l ll Densitylll lll100 l

l

l ll 50Fig. 2: Time series plots that show the evolution of the averaged raw test smell lll llof the studied systems. The test smells are aggregated from on seven snapshotslllllll taken everysixmonthsbetween2016and2019.

1/1/20167/1/20161/1/20177/1/20171/1/20187/1/20181/1/20191/1/2018 TimeTime190 (81%) out of 234 (i.e., 18 test smell types times 12 studied systems) of the test smelltypes(acrossallstudiedsystems)haveanincreaseinthenumber detected testsmellinstances,which indicatesthattestsmellsareprevalent in CIMGPSRASEST the software andgraduallygrowover time.However, afternormalizedbythe LOC ofthetestcode,121outof234(51%)ofthetestsmelltypes(acrossall studied systems) have a decreased test smell density. The ndings may indicatel lthat whilethenumber ofaddedtestsmellinstancesarehigherasthesystems LTDAROevolve,testsmelladditionmaybeslowerthanthatoftestcodeaddition.In ll other words,eitherdevelopermayintroducefewertestsmellinstanceswhenl ll900ladding newtestcodeoractivelymaintaintestcode,whichresultsinthe l llremovaloftestsmellinstances.WefurtherstudythereasonfortestllllremovalinRQ2.llll lll l l600ll

l Density ll ll lll lll l l l300 l

ll l l llllllll

1/1/20167/1/20161/1/20177/1/20171/1/20187/1/20181/1/20191/1/2018 TimeTime

EGECTARGFUTMNT

l

ll

l

l l

ll

7/1/20181/1/2019

IT

l l

l l

l

l

l l

ll

7/1/20181/1/2019


---

<!-- Página 11 -->

Title

Table4:Thecomparisonofthetestsmelldensity(numberoftestsmellin- stances per1000linesoftestcode)foreachtypeoftestsmellinthestudied systems from2016and2019.

Discussion: Since developerswithhigherexperiencemayxmoretestsmells,wefur- ther studythecorrelationbetweendevelopers'experienceandtestsmellre- moval/addition.FollowingapriorstudyRahmanandDevanbu(2011),we use thenumberofpreviouscommitsasaproxyfordevelopers'experience. Fromthebeginningof2016totheof2019,weminedallthecom- mits thatmodi edthetestleandcalculatedthetestsmellremoval/addi- tion foreach uniquecontributor. Thenwe studytherelationshipbetween test smell removal/addition anddevelopers'experience(i.e.,intermsofthenum-TestBookkeeperAccumuloCamelSmell ber ofpriorcommits)byemployingSpearman'srankcorrelationcoecient.2016 AR%6.17&12.58&8.18&14.67WechooseSpearman'srankcorrelationsinceitisanon-parametriccorrela- CTL&7.97&3.47&7.96%4.16& CI%2.34%0.21&0.06&0.79% ET%0.000.00&0.06% ECT%19.46&33.55&21.85%29.11% GF%5.79&2.05&1.37&4.26% MG%1.87%1.09% 1.17&1.40% PS%0.06&0.08% 0.35%0.08& RA%0.06&0.10% 0.25&0.12 SE%0.03&0.85% 0.28&2.16% ST%3.01%1.32% 0.87%0.47& EG&1.96&3.11&5.12&6.71% LT%6.01&11.92&29.79&24.74% DA%3.73&2.04&2.98&3.03% UT%0.85&3.46&7.59%7.63% IT&0.70&0.86&2.08&0.94% RO%2.18%0.85&1.22&1.12% MNT&3.04&6.15&5.45&6.35& GroovyHiveFlinkKafka 2016 AR&19.52&13.17% 16.67& CTL%7.84%5.06% 4.55% CI%0.77%0.64&0.17% ET&0.51%0.03% 0.06% ECT&64.35%23.08&13.70% GF&5.01&5.68&3.90& MG&1.03%0.43&2.04% PS% 3.21%0.50% 0.00& RA%3.08%0.93% 0.06& SE&3.73%2.89% 0.17& ST%0.000.12% EG&9.38&7.30% 17.25& LT&43.42&34.12%78.91& DA%5.39%4.49%4.31% UT&15.29%6.99&4.43& IT&0.64%0.60&0.29& RO&2.57%0.53&2.10% MNT&11.43%8.70% 11.07% ZookeeperKaraf 2016 AR&17.36% 8.50&9.70& CTL%2.09% 8.30%5.61% CI%1.29%0.56&0.41& ET%0.11% 0.04% 0.04% ECT%13.56% 22.19&21.41 GF&5.31% 4.27&6.15& MG%0.20%2.75% 1.07& PS&0.13% 0.16% 0.58% RA%0.59% 0.68% 0.18% SE&4.52% 0.84% 1.15& ST&0.00&2.00% 1.03% EG&12.86% 3.87&4.93& LT%57.07% 13.09&22.38& DA%5.07% 4.23%3.58& UT&5.41% 6.62% 4.48% IT&0.17&0.44&1.09% RO%0.33% 2.91%1.23& MNT&5.52% 4.55&5.62&


---

<!-- Página 12 -->

12

Table5:Thecomparisonoftheprevalence oftestsmells(i.e.,theraw number of testsmellinstances)forthestudiedsystemsfrom2016to2019.

tion testthatdoesnotassumetheunderlyingdatadistribution.Wefound a positivecorrelation(i.e.,0.53)betweentestsmelladditionanddevelopers' experience andfoundanegativecorrelation(i.e.,-0.57)betweentestsmell removalanddevelopers'experience.Thecorrelationanalysissuggestsanon- negligible correlationthatexperienceddevelopersaremorelikely toaddmore test smells and remove fewer test smells. One potential explanation for our re- sult is that even highly experienced developers often do not refactor test smells due to lack of awareness or bene ts,which aligns with a prior survey (Peruma TestBookkeeperAccumuloCamelet al., 2019).AnotherreasonmaybethatmostexperienceddevelopersworkSmell 2016on themostoftenexercisedandmostcomplexpartofthesystem(Zeller, AR%195%4740%585%2845%2009). Tocorroborateourresult,westudytherelationshipbetweenthesizeCTL%252%1309%569%807% CI&74%81%4% 153% ET&00 ECT&615%12641%1562%5644% GF%183%773%98% 826% MG&59%409%84%271% PS&2%29%25%16% RA&2%37& 18%23% SE&1%321%20% 418% ST%95%496&62%91% EG%62%1171%366%1302% LT%190%4490%2130%4797% DA%118%770%213%588% UT%27%1305%543%1479& IT%22%324%149%183& RO&69%320%87%218% MNT%96%2318%390%1232% GroovyHiveFlinkKafka 2016 AR%152%1721%286% CTL%61&662%78% CI%6%84%3% ET% 4&4%1% ECT%501%3017%235% GF% 39%743%67% MG%835% PS&25&65%0% RA%24&121%1% SE% 29%378%3% ST%02% EG% 73%954%296% LT%338%4460%1354% DA%42&587%74% UT% 119%914%76% IT% 55% RO%20&69%36% MNT%89%1137%190%

ZookeeperKaraf 2016 AR%941& 213%4057% CTL%113& 208%2344% CI14%170% ET1 ECT%735& 556%8953% GF%288& 107%2571% MG%11&69%449% PS%7& 4%242% RA17 SE%245& 21%480% ST% 0%50%432% EG%697& 97%2062% LT%3093& 328%9358% DA%275& 106%1499% UT%293& 166%1872% IT%9%11%455% RO%18& 73%516% MNT%299& 114%2351%


---

<!-- Página 13 -->

Title

of codechanges(i.e.,linesofcodeanddeleted)anddevelopers'experience. Weemploy quantile-based correlation,wherewe splitdevelopersinto fourdif- ferent quantilesbasedonexperiencesandstudiedtheircorrelationwithcode size. Ourresultshowsanincreaseinthecorrelationbetweenexperienceand code size(i.e.,0.26,0.50,0.67,and0.70).Therefore,we observe thatthehigh expertise team may not necessarily remove more test smells becausethey may be responsibleforlargerandmorecomplexchanges.

Although thenumberoftestsmellsincreasesasthesystemsevolve, after normalization againstTest, thetestsmelldensitygenerallyremainsLOC stable. Wealsondthatsometypesoftestsmell,suchEagerasTest, IgnoredTest,Unknown Test,LazyTest, andSleepyTest, haveoneofthe largest increaseintermsoftestsmelldensityinmoststudiedsystems.In contrast,ExceptionCatch/Throw,RedundantAssertion, andPrint State- menthavethe largest decrease in terms of test smell density in most studied systems.

3.3 RQ2:Whatisthemotivation behindremovingtestsmells?

Motivation:A recent study (Garousi and Kucuk,2018) claims that develop- ers perceive test smell as harmful in software systems. In contrast, other studies reveal thatdevelopersareunaware oftestsmellsanddonotacknowledge the bene ts ofrefactoringthem(Junioret al., 2020a;Tufanoet al., 2016).Never- theless, there is limited empirical support on test smell removals, whether a test smell vanishesasaside-e ectofcodeevolutionorisadeliberaterefactoring target. Such evidenceisnecessarytoreveal thecurrent perceptiondevelopers may haveontestsmells.Hence,weperformaqualitativestudyonthetest smell removing commitstoidentify reasonsthatpromptdeveloperstoxthe test code with test smells and the mechanisms employed to address test smells.

Approach:Weconduct a qualitative study on commits removing test smells. WeleverageGittoextractallthecommitsexceptforthemergebe- tween2016 and 2019. We only keep the commits that include test le modi ca- tions and discard the other commits from further analysis. A commit modi es a test le if the involved les have the extension\.java"and have a pre x or a sux of"[Tt]est(s*)". For each ofthecommits,we runtsDetectoron thetwo versions ofthesoftware(i.e.,everytwoconsecutivecommits)andcalculate the rawtestsmelldi erences. Tounderstand why developers remove test smells, we look at a combination of bug reports, commit messages, test code, and thehistory of relevant test code.Inthestudiedsamples,241commits(80%)includesissueIDfrom the Jirabugreport,and25commits(8%)useGitHub'spullrequest/issue tracking. Theremaining34commits(11%)onlycontainedcommitmessages, which containedsucientinformationtounderstandthereasonbehindtest


---

<!-- Página 14 -->

14

Table6:Asummaryofourmanualanalysisonthecommitsoftestsmell removal,i.e.,304sampledcommitsminus12thatareincorrectly agged by the test smell detection tool.Our analysis focuseson the context of each commit and how the test smell is addressed in the commit. In particular, we showtheassociationbetweentestcodechangesandthecorresponding maintenance activitiesthatdevelopersapply.

Maintenance code changes. Such commit messages may include keywords likeor RefactoringFeatureBugOthers"Fix testspeed."Using theartifactsabove, we answer two typesofquestions: TestprovementAddition Code1) What kind of maintenance activity initially prompted developers to address TESTtest smells(i.e.,themainpurposeofthecommit)?2)Howisthetestsmell Exceptionaddressed (e.g.,deliberaterefactoringorby-productofothermaintenance ac- Sleepy tivities)?WeusedthetwopreliminaryinquiriestogainfurtherinsightintoUnknown Assertiondevelopers' awareness ofthemostcommonreasonforremovingtestsmell.Sensitive Magic In theanalysis,wetakeastatisticallysigni cantsampleofthecommitsConditional Totalweremoving testsmells.Inparticular,applystrati edrandomsamplingon TESTthese commitswitha95%con dencelevelanda5%interval. We Persistenceadopted strati edsamplingtosamplethetestsmellsineachstudiedsystem By-Product independently,whichcanbeadvantageoustoreducesamplingerrorwhena Total subpopulation within the overall population varies (Zhaoet al., 2019). The rst OTHER twoauthors examine the sample independently. Any disagreement is discussed Test Adduntil reaching a consensus. To assist our qualitative study, we leveraged a tool Revert called RefactoringAwareCommitReview(Tsantaliset al., 2018),whichis Total a codedivisualizationtoolforshowingtherefactoringactivitiesapplied #Total between two commits.


---

<!-- Página 15 -->

Title

Results:In total,wemanuallyanalyzed304commitsfromatotalof1,452 commits (achievinga95%con dencelevelwitha5%interval). Table6 shows a two-dimensional summary illustrating the association between the maintenance activities that initially prompted developers to maintain test code (horizontal dimension) and the type of speci c test code changes (vertical dimension) thatdevelopersappliedwhenremoving testsmells.We alsofound 12 incorrectlydetectedtestsmellinstancesbytsDetector, i.e.,a4%false- positive rate,andexcludedtheminTable 6. Forthe maintenance activities (horizontal), we uncover ve categories that prompted developerstomaintaintestcode.Fourofthevecategoriesare: refactoring testcode(65commits),featureimprovement(87bug xing (76commits),andaddingnewfunctionality (55commits).Theremain- ing ninecommits(i.e.,thefthcategory-\others")consistoftheonesthat we cannotidentifyclearmotivesduetoinsucientdocumentation(e.g.,low- quality commit messages and bug reports). As an example, in CXFbcb6385a(), the developer addresses a test smell (i.e.,IgnoredTest) by completing the test implementation. However,thetestcasewasignoredwhenitwasrstintro- duced tothecodebaseyearsagoanddidnotreferenceanybugreport.Thus, it isdiculttolabelthecorrectmaintenancemotives. Weclassifythetypeoftestcodechanges(vertical)intothreecategories: TestSmellAwareRefactoring(50 commits),TestUnawareRefactor- ing(133 commits),andOther CodeChanges(109 commits).Weclassifya commit in the category ofTestSmellAware Refactoringif developers directly addressed the test smell. We classify a commit as a SmellUnaware Refac- toringif thetestsmellsareremovedasaside-e ectofotheractivities.Test Smell UnawareRefactoringconsists oftwosubcategories:TestPersis- tenceandBy-productRemoval. TheTestSmellPersistence(58 commits) shows instances ofapplyingstandardcoderefactoring,suchasextractingcommon test code,where test smells are transiently relocatedto another test class. The By-productRemoval(75 commits)representsthecaseswhenthetestsmellis removeddue to refactoring and maintenance of other tasks (e.g., removing du- plicate source code).We group the remaining commits that remove test smells but are not test smell speci crefactoring into \Other Code Changes"(109 commits). Thesecommitsmadechangessuchasdeletingtestcode,disabling tests (commentingorignoringcode),andrevertingacommit. In thefollowingsubsections,wediscussourqualitativeanalysisresultsof the threehigh-leveltestsmellremoval categories.

TestSmellAwareRefactoring

Although lessfrequent, wendthatdevelopers directly refactor speci c test smells in50outof292(17%)studiedcommits.As showninTable6,these commits are related to removingExceptionCatch/Throw(21 commits),Sleepy Test(15 commits),Unknown Test(7Assertion Roulette(2 com- mits),Sensitive Equality(2 commits),Magic Number(2andCon- ditional TestLogic(2 commits).Bylookingintotheverticaldimension(i.e., the contextofthecommits),wendthatTestSmellAware Refactoringhap-


---

<!-- Página 16 -->

16

pen morefrequentlyduringtestrefactoringcommits(20/50),butdevelopers also deliberatelyaddresstestsmellsduringothermaintenance activities(e.g., feature improvement andbugxing). However,notalltestsmellremovingcommitsaredeliberatelyxedby developers. Therefore,wealsoreporttheproportionoftestsmell" xing" commits (i.e.,deliberatelyxedbydevelopers)over thenumberoftestsmell removing commitsinourstrati edsamples(i.e.,allthatremove the speci c testsmell),whichshowsthetrueproportionofthexedtestsmells. In thiscase,eventhoughExceptionCatch/Throwhas thehighestnumber of testsmellremovingcommits,only31%werexedtestinstances. SleepyTesthas thehighestnumberofintentionalxes(60%)comparedto other testsmells.21%ofUnknown Test, 12.5%ofSensitive Equality, 5.1% ofMagic Number, 2.9%of Assertion Roulette, and1.9%of Conditional Test Logicare deliberatelyxedbydevelopers.Ourndingsshowthat,inthe studied systems,developersaremorelikelytoxTestandException Catch/Throwdue totheexistenceoftestsmellinsteadofothermaintenance activities. **Refactor Sleepy**Test.15 outofthe292(5%)commitsarerelatedtorefac- toring theSleepyTesttest smell.Thisndingshowsthatdevelopersdeliber- ately xed 60% of removedSleepyTest. This test smell occurs when developers explicitly cause a thread to sleep, leading to unexpected results as the process- ing timeforataskcandi erondi erentdevices(Meszaros,2007).Wend that developers often removeSleepyTestdue to unexpectedtest behavior and increased testtime.Forexample,inKafka7b7c4a7(), adevelopermentions that: \The timeouts are oftenlarge (e.g.,10seconds) andstilloccasionally they trigger prematurely. Theyneed tobe replaced bywaitUntilTrue andsomelogic that checkswhenprocessing instreams iscomplete". In another example, a developer in Camel722e590c() mentions that\[u]se awaitility fortestingwhere weotherwiseusethread sleep whichcan be speeded up." . We nddevelopersoftenapplytwoapproachestoaddressSleepyTest. One istousewaitFor() condition intheJavaAwaitilitylibrary andtheother is torefactorthetestsmellusingJava'sFuture library.Thesetwo approaches allow thetestcasetorunasynchronouslywithoutblocking. As presentedinTable 4(RQ1),whileSleepyTestaccounts foroneofthe most prevalent testsmells,wendinourmanualstudythatdevelopersalso allocate somee ortstorefactorsuchsmells.TheawarenessforTest may bearesultoftheincreaseinattentionfortheunreliabilityintestcode qualities (e.g., aky tests) (Ecket al., 2019; Lamet al.,Shi et al., 2019). Moreover,wendthatdevelopersmayalsobeconcernedwithanincreased test executiontimecausedby callingthread.sleep(). Future research isneeded to understandfurtherdevelopers'awareness andopinionontheconsequences ofSleepyTest. **Refactor Exception**Catch/Throw.Wendthat21outofthe292(7.2%) commits are related to refactoring theExceptionCatch/Throwtest smell. This nding shows that developers deliberatelyxed 31% of the removedException


---

<!-- Página 17 -->

Title

Catch/Throw. As discussed in a previous paper (Perumaet al., 2019), this test smell occurswhenthepassingorfailingofthetestisdependentoncustom exception handlingcodeorthrowinginsteadofusingJUnit'sex- pected attribute.Inthiscategory, developersdeliberatelyrefactoredthetest smell in10commits,andtheremainingwererefactoredduringothermain- tenance activities:featureimprovement (3commits),bugxing(3 and featureaddition(5commits).AsshowninListing1,developersremove the codelogicinthecatchblockthatdeterminesthepassingandfailingof the testcase.Thedevelopersmentionedinthebugreportthatusingfailin the catch blockisabadprogrammingstyle andmasksthedetailsofthestack 2trace. Afterremovingthetestsmell,anewtestsmell(i.e.,unknowntest)is introduced. We havealsoseenothersimilarcasesinourstudy, whereanew test smellisintroducedafterdevelopersresolvedthecurrenttestsmell.Our nding shows thatdevelopersaresometimesunaware ofthetestsmells;thus, they arelikelytointroducenewtestsmellswhenaddressingexistingones.In short, ourmanualstudyndsthatdevelopersaremorelikelytorefactorthe ExceptionCatch/Throwtest smellduringvarious maintenance tasks.We also nd thatthesetestsmellsremovalisoftennotassociatedwithtestfailures but improves futuremaintainability.

Listing 1:Developersremovedthedependencyoftestoutcomeonexception handling code(Flink-e83217bd). 1@Test 2public 3-{ 4MemorySegmentnew[0]); 5testZeroSizeBuffer(segment); 6testSegmentWithSizeLargerZero(segment); 7- 8- 9- 10- 11- 12}

**Unknown Test.7 out of 292<**( 3%) commits are removal of test smell called Unknown Test. Thisndingshowsthatdevelopersdeliberatelyxed21%of the removedUnknown Test. Thistestsmelloccurswhentestcasesdonot contain anylogicorassertionsstatements.Thus,itischallengingtocompre- hend whattheroleofthetestcaseis.Asanexample,inKafka7d6ca52a(), the testclasscalledJmxReporterTest.javais addedthreeyears ago.However, three yearsafteritscreation,thedevelopersnoticedmissingtestcodewhile working onothertasksandimmediatelyaddressedit.Similarly, asmentioned in CXF(bcb6385), developerscompletedthemissingtestimplementation two years ago.Thus,ourndingsuggeststhattheremightbeotherinstancesof

2[https://github.com/apache/](https://github.com/apache/) ink/pull/4446


---

<!-- Página 18 -->

18

theUnknown Test, wheredevelopersmay onlynoticethemwhilemaintaining other tasks.OnepotentialreasonforaddingUnknown Testcode may bethat in featureadditions,the Unknown Testgets addedtoprepareforthefuture implementation. ThisisillustratedinCXF2705f4d(),[CXF-7525] Complet- ing thesystemtest, wheredevelopersinitiallyonlyprovidedemptytestcases when implementing the feature and later complete the test case. While adding Unknown Testsmay serve ascodedocumentationtodescribewhattestcases should beimplementedinthefuture;developersmayforgettocompletethe test caseandbecometechnicaldebt(PhamandYang,2020;Spnolaet al., 2019). **Refactor Sensitive Equality.We**nd that developers refactor the Equalitytest smell in 2 out of 292< 1%)(commits. The nding shows that de- velopers deliberatelyxed12.5%oftheremovedSensitive Equality. Thistest smell occurswhenthetestmethodveri esobjectsbyinvokingtoString()the method. Thepotentialconsequenceofthetestsmellisthatthechangein the implementation oftoString()might resultintestfailure(Meszaros,2007). WendasimilardiscussioninFlink390d3613(), \ rerollercoastingthrough abstractionlayer;wedon'treallyknowwhattheimplementationisbycall- ing tostring? ". Thus,ourndingsshowthatdevelopersmaybeawareofthe inherent issuesassociatedwithusingadefaultmethodwithunknownimple- mentation. In thecommits,whiletherewereatotalof16samplesoftheremoved Sensitive Equality, only2outof16commits(12%)re ectedanawarenessof the test smell (in other cases, developers delete the entire test methodor move the wholetestcodetoanothertestcase).Itmaybebecausetheuseofthe defaulttoString()is intuitivefrombothitspurposeandnamingconvention, and thus, developersmay nothave animmediateincentive toaddressthetest smell untilthetestfails. **Refactor Magic**Number.WendthatdevelopersrefactorNumber in 2 out of 292<(commits. This nding shows that developers deliberately xed 5.1%oftheremovedMagic number. Thistestsmelloccurswhenassert statements inatestmethodcontainnumericliterals(i.e.,MagicNumbers) as parameters.Magic Numberdoes notindicatethemeaning/purposeofthe number. Hence,theyshouldbereplacedwithconstantsorvariables,thereby providing adescriptivenamefortheinput(Meszaros,2007).Asanexample in Kafka(7ebc5da6), thetestsmellwasrefactoredafterafeatureaddition, which involved explicitlyreplacingtheMagic Numberwith avariable witha more meaningfulvariable nametoimprove codecomprehension. **Refactor Assertion**Roulette.Wendthat2outof292<(commits are from refactoringAssertion Roulette(AR). The nding shows that develop- ers deliberatelyxed2.9%oftheremovedAssertion Roulette. Thistestsmell occurs whenthetestmethodhasseveral assertionstatements makingitchal- lenging todeterminewhichassertionhadfailed(Meszaros,2007).Although prior work(Deursenet al., 2001;Meszaros,2007)proposesusinganasser- tion explanationtorefactorthetestsmell,wendthatdevelopersmayalso removethetestsmellusinganotherassertionstatement.Figure3showsan


---

<!-- Página 19 -->

Title

Fig. 3:Assertionrefactoring,removingduplicateassertionand Roulettetest smells.Locatedinthecommit3b42fb5fromApacheKaraf.

example whereassertContainis usedtoremovebothAssertion Rouletteand duplicate assertion test smell. In this case, developers attempt to mitigate the test code'sverbosenessbyrefactoringwithassertions,whichhelpstoremove the testsmells. **Conditional Test Logic.We**ndthat1outof292< 1%)(commitsrefactor Conditional TestLogic. Thendingshowsthatdevelopersdeliberatelyxed 1.9% oftheremovedUnknown Test. Thistestsmelloccurswhenthetest case's successorfailuredependsontheassertionmethodwithinthecontrol ow blocks and thus not predictable (Meszaros, 2007). A prior survey (Garousi and Kucuk,2018)notedthatdevelopersprefertoconsideritissmellyornot on a \case-by-case basis". Our study also nds that developers typically do not refactorConditional TestLogic. For theonlycasethatwefound,developers refactored thetestsmellwhentherearenestedconditionalstatements.In Kafka( 7ebc5da6), showninthecodesnippetbelow,thedevelopersimpli es the testsmell'sverbositywithassertionstatements.Namely,assertThat() & is()is usedtoimprove thereadabilityofthetestlogic.

1@Test 2public 3..... 4-(tupleType.isTupleType()) 5-(!((TupleTypeInfo<?>)tupleType).equals(testTupleType)) 6-" Tuple! " ); 7- 8- -" Type! " );9

10- 11+true)); 12+ 13..... 14}


---

<!-- Página 20 -->

20

Although lessfrequent,wendthatdevelopersdeliberatelyrefactorspe- ci c testsmellsin50outof292(17%)studiedcommits.Inparticular, ExceptionCatch/Throwand SleepyTest are the two most commonly refac- tored test smells. Based on the discussion in bug reportsand commit mes- sages, we ndthatdevelopersareoftenaware ofthesub-optimalpractice of usingThread.sleepand spent e orts on improving the design of exception handling mechanisms.Eventhoughthenumberisless,wealsondsome refactoring of other test smells, such as theUnknown Test, Magic Number, Sensitive Equality,Conditional Test Logic, andAssertion Roulette.

TestSmellUnawareRefactoring

Most testsmells(133/292,45%)are notremoved bydevelopers butare either relocatedordeletedasconsequences ofotherrefactoringactivities.Weclas- sify suchcommitsas TestSmellUnawareRefactoringsince developerswere unawareof the test smells and removed them as a by-product of other mainte- nance tasks, such as refactoring, feature improvement,addition, or bug xing. Inourmanualanalysis,wendthatTestSmellUnawareRefactoring may a ectthetestsmellsintwoways:1)Thetestarerelocatedto another codebase,i.e.,testsmellpersistence.2)Thetestsmellsareremoved unintentionallyduetocascadingresultsofothersourcecoderefactoringac- tivities. Belowwediscussthetwo categoriesindetail. **Test**SmellPersistence.Wend that for 58 out of 292 (20%) commits, test smells wererelocatedtoothercodebaselocations.Inthiscase,testcodemay undergo various refactoring activities such as introducing inheritance (19 com- mits), extracting method(25 commits),class (10replac- ing methodwith the existing helper(2 commits), and moving method/class(2 commits). For example, in CXF31a4a55(), developers applied two refactorings (i.e., extractsuperclassandpullupmethod)tothetestcase DataProviderTestto extractcommontestcode.However,fourexistingtest smells (i.e.,Assertion Roulette,Conditional TestLogic,Duplicate, andMagic Number) inthetestcodearerelocatedtothenewtestcaseasa result oftherefactoring.Namely,developersdidnotremovethetestsmells during test code refactoring. In some cases, relocation may magnify test smell's e ect. For example, in Hive14e92703(), while the developer xes a bug associ- ated with test failure, the developer extracts a reusable methodthat explicitly causes athreadtosleepandrelocatescodetoamethodinatestutilityle. The methodwas thenusedinthreeothertestcases,thus magnifyingthetest smell's impact. **By-Product Removal.**Wendthatfor75outof292commits(25%),test smells are removed by developers as a cascading e ect of source codechanges. Such maintenance activities include feature improvement, adding features, and bug xing(i.e.,thehorizontalviewinTable6).Forexample,acommitin Accumulo (9dadca0f) implements a new feature and refactors the source code using a builder design pattern. As a result of the source codechanges, one test smell instance ofeagertest(i.e., calling multiple source codemethodsin a test


---

<!-- Página 21 -->

Title

case) isremovedsincethetestcasenowcallsthebuildermethodinsteadof invokingfourdistinctmethods. In summary, we nd that developers may refactor test codewhile perform- ing othermaintenanceactivities.Developersmayrefactorforfuturemain- tainability orasanecessaryprecursorforchangeinfeaturerequirement.For example, tosupportnewfeaturesinthesourcecode,developersmay refactor test codetoaccommodatecommonlogicintestcodeandapplycodereuse. However,inmostcases,testsmellswere unintentionally removed by testcode relocation or di usion as aside-e ect of thesemaintainability tasks.Our nd- ings showthatdevelopersareunawareoftestsmellsandmaynotactively removetestsmellsassystemsevolve.

Wend that developers often refactor test code,but they may not directly removetest smells. Many manually studied test smells (133/292, 45%) are relocated orremovedunintentionallybydeveloperswhilerefactoringtest code.

Other MaintenanceActivities

We ndthattestcode maybe deleted asasystemevolves.Themajorityoftest smell removals are related totestcode deletion.109 outof 292(37%) commits belong tothecategoryOther CodeChanges. Weclassifyacommitintothis category when the removed test smell results from deleting test code, disabling test (ignoring/commentingout),orrevertingacommit. **Test**CodeDeletion.In ourstudy, wendthatforanon-trivialnumberof commits (97/292 commits, 33%), the test smells are removed becausethe test code isdeleted.Developersmay deleteatestcasewhenitbecomesredundant or obsolete.Forexample,inFlinke671f34(), whileportingsourcecodeto another le,developersdiscusstheremovaloftestcasessincetheotherle already hassimilartestcases.Developerssometimesalsodeletetestcases when theybecomeobsoleteorhardtomaintainasthesystemevolves.For example, inAccumuloc265ea5b), thetestcodebecomesirrelevant sincethe corresponding featuresundertestareunstableandremoved.Therefore,the test smellsinthetestcodearealsoremoved. **Add Comment/@Ignore.**7 outof292(2%)commitsarerelatedtocom- menting outorignoringthetestcode.Thiscategoryrepresents removing test smells asaresultoftemporarilydisablingthetestcode.Ingeneral,wend that developersmaycommentouttheentiretestcasetobypasstestfailure. Forexample,inKafka(), developerscommentedoutthetestcodeto temporarily make the test pass since the test would only work after developers migrate toJava 9.Asanotherexample,inCamel9ad68066(), thetestcaseis ignored duetotestfailurecausedbyarecentupgradetojetty9.3.Although the testsmellisremovedduetocommentingorignoringthetestcode,the test smellisnotaddressed.Lastly,wealsoseecaseswherethecommented out test case was only brought back a few months later. Future studies should


---

<!-- Página 22 -->

22

also investigateifsuchcommentedouttestcasesarere-enabledorbecomea technical debtinthesystem(PhamandYang, 2020). **Revert a**Commit.5 outof292( 2%) commitsarerelatedtoreverting the testcode.Thiscategoryrepresentsremovingtestsmellsasaresultof temporarily reverting software to the previous versions. For example, in Wicket ( 266c90037), thesystemwasrevertedduetoadefectcausedbyaddingnew features. Thus,thenewlyintroducedtestsmellwasalsoreverted.

Wend that as the system evolves, test codeand its associatedtest smells may bedeletedduetotheobsoletenessandmaintenancedicultyofthe source/test code.Developers may also temporarilycomment out test cases to bypasstestfailurescausedbyrecentcodechanges.However,wesee instances wheredevelopersonlybringthecommentedouttestcodeback after severalmonthsoryears.

**Summary &**Implication.Our manual studyshows that,inmostcases, developers maynotbeawareofthetestsmells.Wendthat82.9%ofthe studied testsmellsareremoved, relocated,ordisabled(e.g.,commentedout) as aby-productofothermaintenanceactivities.Duringtheserefactoringac- tivities, developersmayrelocatethetestsmelltoanothertestcase,andthe test smellremainsunchanged.Insomecases,asdiscussed,theimpactoftest smell may become larger, as the test code that contains test smells is extracted to becomeautilitymethod.Nevertheless,westillndthatdevelopersdelib- erately removedtestsmellsin16%ofthestudiedcommits.Inparticular,we nd thatdevelopersaremorelikelytoremoveExceptionCatch/Throwand SleepyTest. Ourndingsuggeststhat,althoughdevelopersmayrefactortest code, theyoftendonotdeliberatelyremovetestsmells.InthenextRQ,we further investigate therelationshipbetweentestsmellsandsoftware quality.

3.4 RQ3:Whatistherelationshipbetweentestsmellsandsoftware quality?

Motivation:Although researchershavemadeanecessarysteptowardsun- derstanding themaintainabilityaspectsoftestsmells(Bavotaet al., 2015; Bleseret al., 2019;Junioret al., 2020a;Perumaet al., 2019),itisstillnot clear whetherremovingtestsmellshasane ectonthequalityofsoftware. In thepreviousRQ,wendthatinadditiontodeliberatelyresolvingtest smells, testsmellsarecommonlyremovedasby-productsofothermainte- nance activities,such asdeletingthetestcodeentirely. Regardlessofhow the test smellsareremovedorrelocated(RQ2),thetestareno longer impactingthesourcecodeles.However, itremainsunknown whether test smellshave any relationshipwiththecodequality. Hence,inthisRQ, we aim tounderstandfurthertherelationshipbetweentestsmellsandsoftware quality,particularlythepost-releasedefect.Ourndingmay helpidentify the types of test smells that correlate with a post-releasedefect and inspire future research thathelpsdevelopersecientlyaddressmoretestsmells.


---

<!-- Página 23 -->

Title

Approach:Our goalisnottopredictdefectsbuttostudytheadditiveef- fect oftestsmellmetricsonpost-releasedefectsover-controlledusing 3logistic regressionmodels.Logisticmodelsarecommonlyusedin prior researchtostudythee ectofvarioussoftwaremetricsonpost-release defect (Bird et al., 2011; Chenet al., 2012; de Paduaand Shang, 2018). Below, we de ne the metrics that we use and the modelbuilding process.The are extractedfrom197totalocialreleases.

**Studied Metrics**&DataCollections

**{**Post-ReleaseDefects.The post-releasedefectisourresponsemetricin the regressionmodel.Thepost-releasedefectisde nedasthedefectsre- ported withinaxedtimeframeafteracertainversionofasoftwareis released (Moseret al., 2008;MunsonandKhoshgoftaar,1992;Piotrowski and Madeyski,2020).For each sourcecodele,we labelitasdefectprone if the le is modi edat least once in bug xing commits within six months after thereleaseofthesoftware system(Zimmermannet al., 2007).Devel- opers inthestudiedsystemsarerequiredtoentertheissueIDincommit messages. Thus,werstquerytheissuetrackertoobtainalistofbug reporting issues within six-month of each release date. We then nd all the bug- xing commitsbasedonwhetherthecommitmessagescontain oneof the obtainedissueIDs.At theendofthestep,we obtainthelistofsource code les that contain post-release defects (e.g., TRUE or FALSE). Finally, if atestletestsasourcecodelethatcontainsapost-releasedefect,we label thetestleasdefect-prone. **{**TraditionalProductandProcessMetric.Similar topriorstudies, we controlfortraditionalproductandprocessmetricsinourregression model. Previousstudiesfoundthattraditionalproductmetrics(e.g.,lines of code)andprocessmetrics(e.g.,codechurnandpre-releasedefect)are good explainersforpost-releasedefects(Moseret al., 2008;Nagappanand Ball, 2005;Nagappanet al., 2006)andarecommonlyusedasbaseline metrics (Birdet al., 2011;Chenet al., 2012;D'Ambroset al., 2010).We collect these metrics at the test- le level and use them as a baseline to build a BASEmodel.We lateraddtestsmellmetricstotheBASEmodeland study whether the test smell metrics may further explain a source code le's defect-proneness. Althoughourmetricsmaynotrepresentallofthemet- rics, theyareshown tohave ahighcorrelationwithothercomplexity met- rics andusedforbenchmarkinginpriorproposalsofnewmetrics(Biyani and Santhanam,1998;Chenet al., 2017;D'Ambroset al., 2010).For the traditional productmetric,weusedCLOC(AlDanial, 2019)toextract the LOCmetricinthetestle.Fortraditionalprocessmetrics,weuse commands \git follows" and\git di " toextractthreedi erent codechurn metrics: lechurn, codeanddeletedlinesofcode.Filechurn isthe number ofcommitsthatmodi edthele.Codechurn isthetotal of codelines,suchascodedeletion,addition,andmodi cation.Finally,

3Logistic


---

<!-- Página 24 -->

24

code deletionisthetotallinesofcodedeleted.For theotherprocessmet- ric, namelythepre-releasedefectmetric,wefollowasimilarapproachto extracting post-releasedefectsusingasix-monthtimewindowbeforeone softwarerelease. **{**Coupling Metric.In additiontothetraditionalproductandprocess metrics, wealsoaddtwocouplingmetrics(namelyCOUPLING)asour controlled metricstotheBASEmodeltoreducethee ectsofconfound- (i.e., atesting variables.Wemeasuretwocouplingmetrics,ts case tosourcecode)andttcoupling(i.e., testcasestotestcases),intest cases, whichareusedinpriorstudiestoassessthequalityoftestcode design (Childet al., 2019).Weexcludethedependencieswithexternal frameworks orlibrarieswhencalculatingthecouplingmetrics. **{**TestSmellProduct andProcess Metrics.Weconsider both test smell PROD-product andprocessmetrics.Testsmellmetrics(TEST UCT) are the number of detected test smells present in the system's current PROCESS) arethenumberofrelease. Test smellprocessmetrics(TEST test smells added and removed six months before releasing the system. Note that weextractthetwometricsforeachtypeoftestsmells(18typesin total). Calculating test smell processmetrics can bechallenging due to le deletion andrename.To addressthesechallenges,weusethegit follow\" to keeptrackofpackagechangeandlerenaming.Sincetestsmellsare detected at di erent granularities, such as line, method,and class level, we aggregated thetestsmellsatthele-level.

**Model Construction** Weusealogisticregressionmodeltopost-releasedefectbecauseitis easier tointerpret andiswidelyusedinpriorstudies(Chenet al., 2017;Har- rell Jr,2015;KuhnandJohnson,2013;NagappanandBall,2005).Logistic regression canbetterisolate(withapredominantly additive e ect)thee ects of the test smell metrics on explaining post-release defect over the BASE model (i.e., an improvement on the model tness) (Harrell Jr, 2015). In particular, we build aninitialmodelusingthebaselinemetrics(i.e.,traditionalprocessand product metricsandcouplingmetrics).Then,we buildaseriesofnewmodels to addTESTPRODUCT andTESTPROCESS overtheBASEmodel.By studying the explanatory power of a series of modelsand their additive e ects of testsmellmetrics,weexplorewhethertestcontributestoabetter explanation of post-releasedefect. We build three modelsfor each studied sys- tem:

**BASE (LOC+CHURN+PRE+COUPLING): The**baselinemodeluses the traditionalproduct,process,andcouplingmetrics. **BASE+TEST****PRODUCT: We add TEST**to the BASE model and measure the improvement in the explanatory power over the BASE model. **BASE+TEST****PRODUCT+TEST****PROCESS: The**thirdmodelmea- sures the combined e ect of TESTPRODUCT and TESTPROCESS metrics overtheBASEmodel.


---

<!-- Página 25 -->

Title

Foreachmodelthatweconstruct,werstapplydatatransformationto reduce the data skewness. We follow prior studies using log-transformation on the metricstonormalizethedata(Chenet al., 2012;dePaduaandShang, 2018). Second, we remove the metrics with a zero variance becausethese met- rics donotcontributetothemodel(i.e.,thevaluesareconstant).Third,we apply redundancyanalysistodroppredictorsthatcanbepredictedbasedon a modelcomposedofallotherpredictorswithanadjustedR2ofhigherthan 40.9.Since somemetricsmaybecorrelatedandcausetheproblemofmulti- collinearity andover tting(HarrellJr,2015;Jiarpakdeeet al., 2018;Wang et al., 2018),we useVariance In ationFactors (VIFs)todetectthecollinear- ity amongthemetrics(KuhnandJohnson,2013).AhighVIFvaluere ects an increaseinthevarianceduetocollinearityinthedata.Ifametrichasa VIF valuelargerthan10,weremovethemetricfromthemodel(Kuhnand 5Johnson, 2013).

**Model Assessment**Process Our goalisnottopredict post-release defect,butrathertostudytheexplana- tory power ofthetestsmellmetrics.Thus, we adoptthreedi erent modelas- 2sessment techniques(probabilityofdefect-proneness,Waldtest, andarea under thecurve; AUC) tounderstandtherelationshipbetween testsmelland post-release defect. PRODUCT and TEST-First, we study the contribution of individual TEST 2PROCESS metricbylookingatproportionsoffor eachrelativeto 22the totalof themodel. is alikelihoodratiotesttoidentifyhowmuch 2a metriccontributestothemodel'stness.Thehigherindicates a explainability of the metric (i.e., more important) in the model(de Paduaand Shang, 2018;HarrellJr,2015).Finally, weuseAUC,theareaundertheRe- ceiver OperatingCharacteristics (ROC), to compare nested logistic regression to capturetherelationshipbetweentheexplanatorymetricsandthesource code's defect-pronenessle(HarrellJr,2015).AUCmeasuresthetnessof the model.AnincreaseinAUCwhennewmetricsareaddedtothemodel indicates thatthenewmodelhasahigherabilitytocapturetherelationship and abettertness(i.e.,thereisacorrelationbetween theaddedmetricsand defect-proneness, aftercontrollingforthebaselinemetrics). Second, westudythee ectsizeoftestsmellmetricsontheprobability of defect-proneness(Moser et al., 2008;Shang et al., 2015).Toquantifythe e ect, we set all of the model's metric values to their mean value and record the probability ofdefect-proneness.Then,weincreasethevalue ofthemetricsin which we want to measure the e ect (i.e., test smell metrics). For each subject metric, weincreasethevalueby125%and150%ofitsmeanandre- calculate theprobability ofdefect-pronenessaftertheincreaseandreportthe percentage di erence.Apositivevalueindicatesthatincreasingthemetric's valueincreasestheprobabilityofthepost-releasedefect.Anegative

4Redundancy 5VIF


---

<!-- Página 26 -->

26

indicates that increasing the value of the metric decreases the likelihoodof the post-release defect.Theintuitionbehindtheanalysisistounderstandwhich metric contributesmoretotheexplainabilityofthesoftwaredefectswhile controlling forothermetrics(dePaduaandShang,2018). Results:**The explanatory**poweroftestsmellmetricsinregression **models.**Addingtestsmellmetricsincrease theAUCofthemodelbyanav- erageof8.25%overtheBASEmodel.Table9{13showthedetailsofthe regression models,whereweshowtheadditivee ectsoftestsmellfeatures overthe baseline metrics. We move the tables to the appendixto make the pa- 2per more concise. We show the proportionof to understand the importance of including the metric on the modeltness. We show the AUC to understand whether ourtestsmellmetriccontributestoahigherabilitytocapturethe relationship onthepost-releasedefectoverbaselinemetrics.We ndthatin all ofthemodels,theAUCincreasesby5.1%overthebaselinewhenadding PRODUCT metrics;andthereisaround8.25%increaseinAUCoverTEST the baseline when addingbothof theTESTPRODUCT and TESTPROCESS metrics. Althoughtheincreaseissmall,weseeaconsistentresultinallthe studied systemsexceptWicket (asdiscussedinRQ1,experiencedma- jor refactoringin2019,whichmaya ectthemodelingresults).Ourresults PROCESS metricshave onlyasmallincreaseinalso show thataddingTEST the model'sexplainabilityafterconsideringthebaselinemetricsandTEST- PRODUCT. Thepotentialreasonmaybethat,asshowninRQ2,developers may removeoraddatestsmellasaby-productofotherrefactoringactivi- ties. Therefore,theremaybenoisesintheTESTPROCESS metrics.Lastly, 2for theproportionof , wendthattheexplainabilityoftestsmellmetrics variesfromsystemtosystem.However,weseethattestsmellmetricssuch as Conditional Test Logic, Constructor Initialization,ExceptionCatch/Throw, Mystery Guest,ResourceOptimism,Assertion Roulette,Eager Test, andLazy Testhavehigher explainability across the studied systems. In short, these test smells may have ahighercorrelationwiththedefect-pronenessofsourcecode les.

**The e ect**sizeoftestsmellmetricsondefect-proneness.Most test smell metricshaveminimale ectondefect-proneness.The analysismen- tioned above shows the explainability of the metrics but not the e ect. Hence, we furtherstudythee ectofeachtestsmellmetric.Table14{15showthe PRODUCT andTEST PROCESS metricsonpost-e ect sizeoftheTEST release defectsforthestudiedsystems.Asdiscussedintheapproachsection, we measurethee ectsizebyincreasingindividualtestsmellmetricswhile keeping allothermetricsatthemeanvalue.We ndthatthee ectsizeand direction (i.e.,positiveornegative)ofthee ectvary fromsystemtosystem. However,thee ectsofmosttestmetricsonthedefect-pronenessareminimal (i.e., lessthan1%increaseintheprobabilityofdefect-pronenesswhen150% increases thevalueofthetestsmellmetric).ComparedtoTESTPROCESS metrics, TESTPRODUCTingeneral,have aslightlylargerpositive relationship withsourcecodedefect-proneness.Amongalltestsmellmetrics,


---

<!-- Página 27 -->

Zookeeper

Wicket

Karaf

Kafka

Hive

Hadoop

Groovy

Flink

Cxf

Cassandra

Camel

Bookkeeper

Accumulo

Title

we ndthatExceptionCatch/ThrowandConditional TestLogicshow the highest positiverelationshipinthemajorityofthestudiedsystems.Thend- ings imply that moreExceptionCatch/Throwand Conditional Test Logicin a test case may lead to a higher probability of having a post-releasedefect in its corresponding source codele. Theanalysis resultonCatch/Throw also echoesourndinginRQ2.We foundthatdevelopersaremorelikelyto refactorExceptionCatch/Throwwhen maintainingtestcode.Ontheother hand, inRQ2,weonlyobservedonecommitthataddressedConditional Test Logic. Priorresearch(Perumaet al., 2019)foundthatdevelopersdonotnat- urally thinkofConditional TestLogicas aproblem.Hence,futurestudies are neededtoevaluatefurtherthee ectofthistestsmellonsoftwarequal- ity.Finally,onepossiblereasonforthehighvariabilityine ectsizeofthe PROCESS metriccomparedtotheTESTPRODUCTcouldbeTEST that manyofthetestsmellswereremovedasaby-productinthee ortto improvetestcodemaintainability(asfoundinRQ2).Thus,futureresearch on testsmellshouldconsiderthoseby-productremovals andrelocationwhen designing thestudy.

Table7:Thecomparisonoftheareaunder(aROC)curveforthestudied systems. Themodelistrainedusingthesystemintherstcolumn,andAUC is calculatedusingthesystemdepictedintheremainingcolumns.

Accumulo0.73 Bookkeeper0.620.87 **The comparison**ofareaunder(aROC)curveforthestudiedsys-Camel0.600.75 Cassandra0.670.78**tems.**The cross-systemAUCislowerthanwithin-systemAUC.Wefur- Cxf0.620.78ther investigate whether di erent systems share a similar relationship betweenFlink0.660.77 Groovy0.600.97test smellanddefectproneness(i.e.,whetherthemodelsareapplicablecross- Hadoop0.600.58systems). Table 7showstheresultsofourcross-systemAUCusingcombinedHive0.610.67 Kafka0.640.82(i.e., productandprocess)testsmellfeatures.Ingeneral,wendthatthe Karaf0.540.82results ofcross-systemAUCarelowerthanthewithin-systemAUC.Inpar-Wicket0.530.82 Zookeeper0.510.83ticular, somemodelstrainedononesystem(e.g.,Accumulo)performworse when applied on some systems (e.g., AUC is 0.53 when the model ison


---

<!-- Página 28 -->

28

Camel) but 0.67 when ferent systems havea more similar relationship between test smells and defect-proneness. Fu- ture studies from di erent

The studied average rics such Catch/Throw ger Test, and proneness, while model tness. Contrarily, the e ect size of test smell metrics have minimal e ect on the defect-proneness

arerelatively betterwhenappliedonothersystems(e.g.,AUC is appliedonCassandraandKafka). Ourresultsshow thatwhiledif- havedi erentdevelopmentcharacteristics,somemay

areneededtofurtherstudye ectoftestsmellsacrosssystems domains.

testsmellmetricsincreasetheAUCofthemodelbyan of8.25%overtheBASEmodel.Thetestsmellproductmet- as Conditional TestLogic,Constructor Initialization,Exception , Mystery Guest,ResourceOptimism,Assertion Roulette,Ea- LazyTestmay haveahighercorrelationwiththedefect- processmetricshavelittleornoimprovementstothe

defect-proneness,anddi erent testsmellhasaon ofsourcecodelesacrossthestudiedsystems.


---

<!-- Página 29 -->

Title

**4 Implications**ofourFindings

Table8summarizestheresultsandimplicationsforeachresearchquestion.

Table8:Summaryofourndingsandtheirimplications.

**Findings****Implications** **F.1**Although**I.1**As overamount linesvelopers tivelyresults **Findings****refactor-Implications** **ings** **F.1 Sleepy**& Exceptionare**I.1**Our twoon addressing **F.2 Developers****I.2 There** movesertion maydevelopers search assertion **Findings****refac-****Implications** **torings** **F.1**58**I.1 Although** totask tenancefor tiontest addressing some smells **F.2**70**I.2**Test whileand not moved

**Findings****Implications** **that** **F.1 Most****I.1 Our** deletiontest maybe coderefactoring code,reduce **F.2**Developer**I.2**Future ortest in Spnolaet, 2019). **Findings****Implications** **and** **F.1**Test**I.1 Our** inrelation ditionimprovement **I.2 Future****F.2**TheConditional, mentionedConstructor,Exception, Mystery,Resource,Assertiondefect Roulette, Eager, andLazyhave defect **F.3 The****I.3**FutureConditionalof defect-pronenessTestandExceptionon Conditionaland Exceptionpractitioners have


---

<!-- Página 30 -->

30

**5 Threats**toValidity

External Validity:The studiedsystemsareallopensourceimplemented in Java, sotheresultsmaynotbegeneralizabletoallsystems.To minimize the threat,westudysystemsthatarelargeinscale,covervariousdomains, frequently usedincommercialsettings,anddiversify thepooloftestcodeun- der analysisbasedontheexpertiseofthedeveloper.Eventhoughourresults are consistent among the studied systems, other developers/systems might ex- hibit a di erent awareness level about the test smells. Therefore, future studies must evaluatetheresultsonadditionalsystemsandimplementedin di erent programminglanguages. Internal Validity:There maybeconfoundingmetricsthatmaya ectthe result ofourlogisticregressionmodel.Tomitigatethis,weincludebaseline metrics, such aslinesoftestcode,codechurn, andtwo couplingmetrics(i.e., source code to test code dependencies and test code to test code dependencies) in the model.Moreover, our modeldoesnot indicate a causal relationship, but rather thatthereisapossibilityofarelationshipthatmay befurtherinvesti- gated infutureresearch. Furthermore, ourstudyaimstounderstandtherela- tionship between test smell metrics to software post-release defects by studying the e ectoftestsmellsonpost-releasedefects.Therefore,webuildalogistic regression modelto study the relationship between test smell and post-release defects, becauselogistic regression modelsprovide betterinterpretability com- pared tomoreadvanced machine learningmodel.Future studiesinvestigating the e ectoftestsmellonpredictionperformanceshouldstudyjust-in-time prediction andcross-systemprediction. Construct Validity:There may be false positives in the tool,tsDetector, that we used for identifying test smells. However, we found that false positive rate to be low in our manual study. We found 12 false positives (4%positive rate), which is consistent with the number reported in the prior study (Perumaet al., 2019). Moreover,theremaybebiasesinourmanualstudyoncharacterizing the commitsthatremovetestsmells.Tominimizethebiases,twoauthors independently inspectevery commit and then merge the results. Furthermore, we examineallavailablesoftwareartifacts,suchascommitmessages,code changes, andbugreports.Asforthereasonsforremovingtestsmells,many non-technical factorsmay play arole,such asalack ofknowledge andlack of time. However, in the bug reportwe analyzed, we did not nd that developers mention such non-technical aspectsthatchallenge testcode'smaintainability. Futurestudies should further dedicateon such non-technical factors. A recent paperSpadiniet al.(2020) reportedaseverity thresholdfortsDetector to makearecommendationwhentestsmellsareprevalent. Suchresultshave a lowimpactonourresultsbecausewestudytestsmellsremoval atamore general level,notonlywhentherearetoomanytestssmells.Finally,inour time seriesplot(RQ1), we plottheaveraged testsmellmetricsofallsystems. Toensurethatonesystemdoesnotoverestimate theaverage, leadingtofalse trends, we veri ed that the individual systems' time series has the same trend as theaverage.


---

<!-- Página 31 -->

Title

**6 Related**

There is their impact Bavotaet al., 2015; Yehudai, describe related prior research in two areas: (1) awareness and maintenance of test smells, Awareness the importance designed test refactoring production gested di erent dependencies and et al. design decisions a study The result test code understand what quantitative result shows mostly introduced Tufanoet al.(2017) studied the reasons behind code smells in production code. They also or comment. Another survey by Junior professional experience test smells in test code. Similarly, we believe that not all test in problems, require more that prompt new catalog tion of test smells in Android applications. They concluded that test widely distributed domains. Subsequently, they test smells. sequences of tool devised from the to uncover di erent the most test smells. report, commit sis). Consequently, we the impact re ects developers'

Work

ongoingresearchintothediscovery, classi cationoftestsmells,and onsoftware quality andmaintainability (Athanasiouet al., 2014; GarousiandKucuk,2018;Junioret al., 2020a;Levinand 2017;Spadini et al., 2018;Tufanoet al., 2016).Inthissection,we

and(2)software defectmodelling. andMaintenanceofTestSmells.Akiyama (1971)discuss ofhavingawell-designedtestcode.Hearguedthatwell- casesareeasiertocomprehendandmaintain. Heproposedthat codeisdi erentfromtestcodeandsug- typesoftestsmellrefactoringoperations,suchasremoving makingresourcesunique.Motivated bythiswork,Deursen (2001) introduced11catalogsoftestsmells,whicharepatternsofpoor associatedwithtestcode.Sincetheproposaloftestsmells, by Tufanoet al.(2016) surveyed developers'awareness oftestsmells. showsthatmostdevelopersdonotrecognizedesignproblemsin anddonotperceivetestsmellsasactualproblems.Furthermore, to kindoftoolsupportisrequired,thestudyalsoconducted research to observe when test smells are introduced and xed. The thattestsmellshavelongsurvivability(i.e.,100days)andare thersttimethetestcodeiswritten.Similartoourwork,

ndthatcodesmellisnoremoved asaby-productofcodedeletion et al.(2020a) suggests that developers' cannotbeconsideredarootcausefortheinsertionof may result andperhapstheremaybespeci ctypesoftestsmellsthatmay attentionasaresultofotherfactors.We alsostudythereasons developerstoremove testsmells.Perumaet al.(2019) proposea oftestsmellsandadetectiontool,elucidatealackofinvestiga- are andaresimilarinbothmobileandnon-mobileapplication surveyed developers'awareness ofthesedetected Theyfoundthatdevelopersareoftenawareofthenegativecon- testsmellsinthesoftwaresystem.Similarly, ourstudyusesthe byPerumaet al.(2019) tominetestsmellremovingcommits 12large-scalesoftwaresystems.Inparticular,ourstudyattempts typesoftestsmellsthatdevelopersmaypayattentionto insoftware development andwhatmaybethereasonsforremoving We uncover thesebystudyingthecodereviewartifacts(i.e.,bug message,pullrequest)andcodecontext(manualcodeanaly- believethisisanecessarysteptowardsunderstanding oftestsmellsandbuildingabettertestsmellrefactoringtoolthat needs.Spadiniet al.(2020) usestsDetectortoproposea


---

<!-- Página 32 -->

32

severitythresholdfordetectionrules.Thenewthresholdshavebeendeter- mined afterinvestigating developers'perceptionoftestsmellseverity. Unlike their work,westudythegeneraltrendonhowdevelopersremove testsmells. Using suchathresholdmayunder-estimatesituationswheredevelopersmay removetestsmells.Duetotheincreasingimportanceoftestcodemainte- nance, Garousi and Kucuk(2018) conducted a large-scale systematic study to summarize acatalogof196testsmellinstances.However, mostofthestudied test smellsarerelatedtogeneralcode(e.g.,longparameterlist,god class, nocomments,andbadnaming),codesmellsspeci ctoTCNlanguage, and codesmellsfromgreyliterature(i.e.,blogposts)ordiculttogeneral- ize (e.g.,complicatedsetup,long-runningtest,longtestle).Di erentfrom their research,wefocuson18othertestsmellsbecausetheyarerelatedto unit testingpracticesinJava(Perumaet al., 2020)andadvocatedinxUnit guidelines Meszaros(2007).These18testsmellshavealsobeenhighlighted as problematicandextensivelystudiedinpriorresearchintestcodemain- tainability anddevelopers'awarenessabouttestsmellsBavotaet al.(2012); Junioret al.(2020a).

Yuet al.(2019) istherstworktoinvestigatetheprocessinvolvedin comprehending testcode.Theysurveyeddevelopers'timespentreadingand extending thetestcodeatvarioustestcasedesignsteps.Althoughtheirre- search place a necessary step towards understanding factors that in uence test code comprehension,itisdiculttogainactionableinsights fortoolsupport. The studydoesnotprovide empiricalevidenceonthecomplexcharacteristics of testcodeevolution.Motivatedbylimitationsofcurrentrepairtechniques to designtestcasesaccurately, thestudybyPintoet al.(2012) analyzestest code evolutionintermsoftheirmodi cation,additionanddeletiontoeluci- date complicatedevolution oftestcasestosuggestbetterrepairtechniques in the future.Similarly, we attempttollthemissingempiricalevidenceinhow developers may remove test smells in practice. We also analyze the relationship between test smell metrics and software quality. Our modelinganalysis identi- es typesoftestsmellsthathave ahigherrelationshipwithdefect-proneness.

SoftwareDefect Modelling.defect modeling has been proposed to ensure high quality by understanding the relationship between various software metrics (e.g., lines of code, McCabe's Cyclomatic complexity) and the software defects (Moseret al., 2008; Munson and Khoshgoftaar, 1992). So far, there are twomainapproachesinsoftwaredefectmodeling.Therstistousequality metrics topredictwherethedefectmay occur,allocatingmaintenance e orts in thespeci ccodeartifacts(Moseret al., 2008;PiotrowskiandMadeyski, 2020). Anotherapproachisbystudyingtherelationshipbetweenthestudied metrics andtheprobabilityofapost-releasedefect(dePadua andShang, 2018; Shanget al., 2015;Shihabet al., 2010).Thetwo shareadi erent defect labeling processinthemodel.SZZisusedintheformalapproachtopredict defect introducingcodechanges(Kameiet al., 2016;Rodrguez-Perezet al., 2020). Sincedefectmodelingatthecommit-level may missrelevant bugs(i.e., bugs introduced in one version but not found until much later), we use a more


---

<!-- Página 33 -->

Title

interpretable processlike thepost-releasedefecttolabelourdata.The post-release defectsprovideadi erentindicationofthesoftware quality. Motivatedbytheirwork,numerousresearchershavebeguntouseanti- pattern orcodesmellsasaqualitymetricfordefectmodeling.For instance, the work by dePaduaandShang(2018)usesexceptionhandlinganti-pattern to characterizepost-releasedefect.Palombaet al.(2014) foundthatthere is acorrelationbetweencodesmellremovalanddefect-proneness.Sincetest smell is becoming an important and ongoing research interest, researchers have also startedtoinvestigatetestsmellmetricsinthedefectmodelling(Qusef et al., 2019;Spadiniet al., 2018).Inparticular,priorresearchesstudythe relationship bylookingonlyatthetestsmellproductmetric,whichisthe presence of test smells in software systems (Spadiniet al., 2018). However, this may not be an accurate assessment as software evolution involve complex code changes. To llthisgap,Palombaet al.(2019) proposedadefectprediction model basedonbothprocessandproductmetrics.Theyclaimedthattheir combined metricsimprovetheperformanceofpredictionaccuracy. Similarly, we studytestprocessmetricstogainfurtherinsightsintohowthetestsmell addition and removal in software evolution may provide additional explanatory power totheprobabilityofapost-releasedefect.We alsocontrolforvarious baseline metrics(e.g.,traditionalprocess,product,andcouplingmetrics)in our model.We foundthattestsmellprocessmetricsprovidelessexplanatory power thantestsmellproductmetrics.We alsofoundthatsometestsmells, such asConditional TestLogicandExceptionCatch/Throw, havealarger correlation withsoftware defect-proneness.

**7 Conclusion**

First andforemost,theprimaryvalue ofourresearch work comesfromrecog- nizing the importance of understanding why developers remove test smells and the mechanismsinwhichtheyareaddressed.Webelievethisisanecessary corequisite tovalidatecurrentperceptionoftestsmellstowardsdeveloping a moreusefulrefactoringrecommendationtool.Withoutsuchknowledge,fu- ture studiesmay progresstoproposenewtestsmellsanddetectiontoolswith minor applicabilityinthewildandmayevenhampersoftwaremaintenance e ort. To thatend,we attempttotackle thisprobleminthreefolds.First,we nd thatdevelopersmayallocateresourcesinthemaintenanceoftestcode. The testsmelldensitydecreasesovertime,eventhoughthetotalnumberof test smellincreasesinthesoftwaresystems.Second,wendthatdevelopers are more likely to address a subset of test smells (i.e.,Catch/Throw andSleepyTest) andtherestwereusuallyremoved indirectlyasaside-e ect of accomplishingothernon-trivialmaintenancetasksrelatedtoxingbugs or changeinfeaturerequirements.Similarly,weidentifyothercodechanges besides refactoringthatrelocate,di use,delete,disableandreverttestcode that causedtheremoval oftestsmells.Finally, we applyregressionmodelsto understand the relationship between test smell metrics and post-release defect.


---

<!-- Página 34 -->

34

After controlling for baseline metrics (i.e., LOC, code churn, pre-release defect, and couplingintestcode),wendthattestsmellmetricsprovideadditional defect explanatory power, although the increase is small. Our modelalso nds that testsmellssuchasExceptionCatch/ThrowandConditional TestLogic havealargere ectonpost-releasedefect.Insummary, ourstudyhighlights that developersmay allocateresourcesonmaintaining testcode,buttheyof- ten do not address test smells. However, we nd that some test smells do have some relationshipbetweenpost-releasedefect.Futurestudiesareneededto better assistdeveloperswithprioritizingtheresourcestoaddresstestsmells and refactoringtestcode.

**References**

Akiyama, F.(1971).Anexampleofsoftwaresystemdebugging.InC.V. Freiman,J. E. Grith, and J. L. Rosenfeld, editors,Information Processing, ProceedingsofIFIP,1971, pages353{359.North-Holland. AlDanial (2019).Countlinesofcode.[https://github.com/AlDanial/cloc](https://github.com/AlDanial/cloc). Ali, N.B.,Engstrom, E.,Taromirad,M.,Mousavi,M.R.,Minhas,N.M., Helgesson, D.,Kunze,S.,andVarshosaz,M.(2019).Onthesearchfor industry-relevantregressiontestingresearch.EmpiricalSoftwareEngineer- ing ,**24 (4), 2020{2055.** Apache (2020).jenkins.[https://builds.apache.org/](https://builds.apache.org/). Last accessed April 32020. Athanasiou, D.,Nugroho,A.,Visser,J.,andZaidman,A.(2014).Testcode quality anditsrelationtoissuehandlingperformance.IEEE Transactions on SoftwareEngineering,**40 (11), 1100{1125.** Bavota,G., Qusef, A., Oliveto, R., Lucia, A. D., and Binkley, D. W. (2012). An empirical analysis of the distribution of unit test smells and their impact on softwaremaintenance.In 28th IEEEInternationalConference onSoftware Maintenance,ICSM , pages56{65.IEEEComputerSociety. Bavota,G.,Qusef,A.,Oliveto,R.,DeLucia,A.,andBinkley,D.(2012).An empirical analysisofthedistributionofunittestsmellsandtheirimpact on softwaremaintenance.In 2012 28thIEEEInternationalConference on SoftwareMaintenance(ICSM), pages56{65. Bavota,G.,Qusef,A.,Oliveto, R.,DeLucia,A.,andBinkley, D.(2015).Are test smellsreallyharmful?anempiricalstudy.EmpiricalSoftwareEngi- neering,**20 (4), 1052{1094.** Bird, C.,Nagappan,N.,Murphy, B.,Gall,H.,andDevanbu, P. (2011).Don't touch mycode!:Examiningthee ectsofownershiponsoftwarequality. InProceedingsofthe19thACMSIGSOFTsymposiumandthe13thEu- ropeanconference onFoundations ofsoftwareengineering, SIGSOFT/FSE '11, pages4{14. Biyani, S. and Santhanam, P. (1998). Exploringdefect data from development and customerusageonsoftwaremodulesovermultiplereleases.NinthIn


---

<!-- Página 35 -->

Title

International Symposium on Software Reliability Engineering, ISSRE, pages 316{320. IEEEComputerSociety. Bleser, J.D.,Nucci,D.D.,andRoover,C.D.(2019).Assessingdi usion and perceptionoftestsmellsinscalaprojects.InM.D.Storey, B.Adams, and S.Haiduc,editors,Proceedingsofthe16thInternationalConference on Mining SoftwareRepositories, MSR, pages457{467.IEEE/ACM. Chen, T.,Thomas,S.W.,Hemmati,H.,Nagappan,M.,andHassan,A.E. (2017). An empirical study on the e ect of testing on code quality using topic models: A case study on software development systems.IEEE Transactions on Reliability,**66 (3), 806{824.** Chen, T., Shang, W., Nagappan, M., Hassan, A. E., and Thomas, S. W. (2017). Topic-basedsoftware defectexplanation.J. Syst.Softw.,**129 , 79{106.** Chen, T.-H.,Thomas,S.W.,Nagappan,M.,andHassan,A.(2012).Explain- ing software defectsusingtopicmodels.InProceedingsofthe9thWorking ConferenceonMiningSoftwareRepositories, MSR'12. Child, M.,Rosner,P., andCounsell,S.(2019).Acomparisonandevaluation of variantsinthecouplingbetweenobjectsmetric.J. Syst.Softw.,**151 ,** 120{132. D'Ambros, M., Lanza, M., and Robbes, R. (2010). Anextensive comparison of bug predictionapproaches.InJ.WhiteheadandT.Zimmermann,editors, Proceedingsofthe7thInternationalWorkingConferenceonMiningSoft- wareRepositories,MSR2010(Co-located withICSE),CapeTown,South Africa,May2-3,2010,Proceedings, pages31{41.IEEEComputerSociety. de Padua,G.B.andShang,W.(2018).Studyingtherelationshipbetween exception handlingpracticesandpost-releasedefects.InProceedingsof the 15thInternationalConference onMiningSoftwareRepositories, MSR, pages 564{575. Deursen, A.,Moonen,L.M.,Bergh,A.,andKok,G.(2001).Refactoringtest code. Technicalreport,Amsterdam,TheNetherlands,TheNetherlands. Eck, M., Palomba, F., Castelluccio, M., and Bacchelli, A. (2019). Understand- ing aky tests: the developer's perspective.InM. Dumas, D. Pfahl, S. Apel, and A.Russo,editors,ProceedingsoftheACMJointMeetingonEuro- peanSoftwareEngineeringConference andSymposiumontheFoundations of SoftwareEngineering,ESEC/SIGSOFTFSE, pages830{840.ACM. Garousi, V.andKucuk,B.(2018).Smellsinsoftwaretestcode:Asurvey of knowledgeinindustryandacademia.Journal ofSystemsandSoftware, **138 , 52{81.** Harrell Jr,F.E.(2015).Regressionmodelingstrategies:withapplications to linearmodels,logisticandordinalregression,andsurvivalanalysis. Springer. Jiarpakdee, J.,Tantithamthavorn, C.,andHassan,A.E.(2018).Theimpact of correlatedmetricsondefectmodels.CoRR,**abs/1801.10271.** Junior, N. S., Soares, L. R., Martins, L. A., and Machado, I. (2020a). Asurvey on testpractitioners'awareness oftestsmells.CoRR,**abs/2003.05613.** Junior, N. S., Soares, L. R., Martins, L. A., and Machado, I. (2020b). Asurvey on testpractitioners'awareness oftestsmells.CoRR,**abs/2003.05613.**


---

<!-- Página 36 -->

36

Kamei, Y., Hassan, A. project models. Knuth, D. Computer Programming. Addison-Wesley, Reading, Kuhn, M. Springer. Lam, W., (2019). Root D. Zhang International Symposium 101{111. ACM. Levin, S. code maintenance through the lens of ne-grained semantic changes. IEEE International ICSME, pages Luo, Q., Hariri, F., Eloussi, L., and Marinov, D. (2014). An of aky tests. In of the Software Meszaros, G. ucation. Moser, R., eciency of In W. Conference Munson, J. programs. Nagappan, N. predict system ference Nagappan, N., component failures. editors, pages 452{461. Palomba, Do they smells. In and Evolution, pages Palomba, On the empirical study. InProceedings Based Palomba, Toward **45 (2), 194{218.**

Fukushima,T.,McIntosh,S.,Yamashita,K.,Ubayashi,N.,and E.(2016).Studyingjust-in-timedefectpredictionusingcross- Empir. Softw.Eng.,**21 (5), 2072{2106.** E.(1981).SeminumericalAlgorithms , volume2of The Artof MA,2ndedition. andJohnson,K.(2013).Appliedpredictivemodeling, volume26.

Godefroid,P.,Nath,S.,Santhiar,A.,andThummalapenta,S. causingakytestsinalarge-scaleindustrialsetting.In andA.Mller,editors,Proceedingsofthe28thACMSIGSOFT onSoftwareTestingandAnalysis,ISSTA, pages

andYehudai, A.(2017).Theco-evolutionoftestmaintenanceand 2017In ConferenceonSoftwareMaintenanceandEvolution, 35{46.IEEEComputerSociety. empirical analysis S. Cheung, A. Orso, and M. D. Storey, editors,Proceedings 22ndACMSIGSOFTInternationalSymposiumonFoundationsof Engineering,(FSE-22), pages643{653.ACM. (2007).xUnit testpatterns:Refactoringtestcode. PearsonEd-

Pedrycz,W.,andSucci,G.(2008).Acomparativeanalysisofthe change metricsandstaticcodeattributesfordefectprediction. Schafer, M.B.Dwyer,andV.Gruhn,editors,30th International onSoftwareEngineering(ICSE),pages181{190.ACM. C.andKhoshgoftaar,T.M.(1992).Thedetectionoffault-prone IEEE Trans. SoftwareEng.,**18 (5), 423{433.** andBall,T.(2005).Useofrelativecodechurnmeasuresto defectdensity. InProceedingsofthe27thinternationalcon- onSoftwareengineering, pages284{292. Ball,T.,andZeller,A.(2006).Miningmetricstopredict InL.J.Osterweil,H.D.Rombach,andM.L.So a, 28th InternationalConferenceonSoftwareEngineering(ICSE, ), ACM. F.,Bavota, G.,Penta, M.D.,Oliveto,R.,andLucia,A.D.(2014). reallysmellbad?Astudyondevelopers'perceptionofbadcode 30th IEEEInternationalConferenceonSoftwareMaintenance 101{110.IEEEComputerSociety. F., Nucci, D. D., Panichella, A., Oliveto, R., and Lucia, A. D. (2016). di usionoftestsmellsinautomaticallygeneratedtestcode:an of the 9th International Workshop on Search- SoftwareTesting, SBST@ICSE, pages5{14.ACM. F., Zanoni, M., Fontana, F. A., Lucia, A. D., and Oliveto, R. (2019). asmell-awarebugpredictionmodel.IEEE Trans. SoftwareEng.,


---

<!-- Página 37 -->

Title

Peruma, A., Palomba, droid applications: An exploratory study. In International Conference on CASCON '19, Peruma, A., Palomba, Proceedings gineering neering, ESEC/FSE 2020, New York, NY, USA. Association for Computing Machinery. Pham, T. M.-T. and Yang, J. (2020). The code. In hension, ICSE. Pinto, L. ities of editors, Engineering Piotrowski, P. and code smells: Applications, pages Qusef, A., of the Access Rahman, F. and Devanbu, P. T. (2011). Ownership, ne-grained study of authorship. In dovic, editors, Proceedings Engineering, pages 491{500. Rodrguez-Perez, and Gonzalez-Barahona, J. identify how Eng., Shamshiri, S., (2018). How tenance? In i cation Shang, W., Nagappan, M., and Hassan, A. E. (2015). Studying the relationship between logging Empirical Shi, A., on mutation testing. 28th ACM Analysis, ISSTA, pages Shihab, E., (2010). Understanding

Almalki,K.,Newman,C.D.,Mkaouer,M.W.,Ouni,A.,and F.(2019).Onthedistributionoftestsmellsinopensourcean- Proceedingsofthe29thAnnual ComputerScienceandSoftwareEngineering, pages193{202. Almalki,K.,Newman,C.D.,Mkaouer,M.W.,Ouni,A.,and F.(2020).tsdetect:Anopensourcetestsmellsdetectiontool.In ofthe202028thACM JointMeeting onEuropean Software En- Conference andSymposium ontheFoundations ofSoftware Engi-

secret life of commented-out source 28th IEEE/ACMInternationalConferenceonProgram Compre-

S.,Sinha,S.,andOrso,A.(2012).Understandingmythsandreal- test-suiteevolution.InW.Tracz, M.P. Robillard,andT.Bultan, 20th ACMSIGSOFTSymposiumontheFoundationsofSoftware (FSE-20), page33.ACM. Madeyski,L.(2020).Softwaredefectpredictionusingbad Asystematicliteraturereview.InData-Centric Businessand 77{99. Elish,M.O.,andBinkley,D.W.(2019).Anexploratorystudy relationshipbetweensoftware testsmellsandfault-proneness.IEEE ,**7 , 139526{139536.** experienceand defects: a R. N. Taylor, H. C. Gall, and N. Medvi- ofthe33rd InternationalConference onSoftware ICSE2011,Waikiki,Honolulu,HI,USA,May21-28,2011 ACM. G., Robles, G., Serebrenik, A., Zaidman, A., German,D. M., M.(2020).Howbugsareborn:amodelto bugsareintroducedinsoftwarecomponents.Empir. Softw. **25 (2), 1294{1340.** Rojas,J.M.,Galeotti,J.P.,Walkinshaw, N.,andFraser,G. doautomaticallygeneratedunittestsin uencesoftware main- 11th IEEEInternationalConference onSoftware Testing, Ver- andValidation, ICST, pages250{261.IEEEComputerSociety.

characteristicsandthecodequalityofplatformsoftware. SoftwareEngineering,**20 (1), 1{27.** Bell,J.,andMarinov,D.(2019).Mitigatingthee ectsofakytests InD.ZhangandA.Mller,editors,Proceedingsofthe SIGSOFTInternationalSymposiumonSoftwareTestingand 112{122.ACM. Jiang,Z.M.,Ibrahim,W.M.,Adams,B.,andHassan,A.E. theimpactofcodeandprocessmetricsonpost-


---

<!-- Página 38 -->

38

release defects:Acasestudyontheeclipseproject.ProceedingsInofthe 2010 ACM-IEEE International Symposium on Empirical Software Engineer- ing andMeasurement, page4.ACM. Spadini, D., Palomba, F., Zaidman, A., Bruntink, M., and Bacchelli, A. (2018). On therelationoftestsmellstosoftwarecodequality.2018InIEEEIn- ternational Conference onSoftwareMaintenanceandEvolution(ICSME), pages 1{12. Spadini, D.,Schvarcbacher,M.,Oprescu,A.,Bruntink,M.,andBacchelli, A. (2020).Investigatingseveritythresholdsfortestsmells.InS.Kim, G. Gousios,S.Nadi,andJ.Hejderup,editors,MSR '20:17thInternational ConferenceonMiningSoftwareRepositories, Seoul,RepublicofKorea, 29- 30 June,2020, pages311{321.ACM. Spnola,R.O.,Zazworka, N.,Vetro, A.,Shull, F.,andSeaman,C.B.(2019). Understanding automatedandhuman-basedtechnicaldebtidenti cation approaches-a two-phase study.J. Braz.Comp.Soc.,**25 (1), 5:1{5:21.** Tsantalis, N.,Mansouri,M.,Eshkevari,L.M.,Mazinanian,D.,andDig,D. (2018). Accurateandecientrefactoringdetectionincommithistory.In Proceedingsofthe40thInternationalConference onSoftwareEngineering, ICSE '18,pages483{494,NewYork, NY,USA.ACM. Tufano,M.,Palomba, F.,Bavota, G.,Penta, M.D.,Oliveto, R.,Lucia,A.D., and Poshyvanyk, D.(2016).Anempiricalinvestigationintothenatureof test smells. InProceedingsofthe31stIEEE/ACM InternationalConference on Automated SoftwareEngineering, pages4{15. Tufano,M.,Palomba, F.,Bavota, G.,Oliveto, R.,Penta, M.D.,Lucia,A.D., and Poshyvanyk, D.(2017).Whenandwhyyourcodestartstosmellbad (and whetherthesmellsgoaway).IEEE Trans.SoftwareEng.,**43 (11),** 1063{1088. VanDeursen, A., Moonen,L., Van Den Bergh, A., and Kok, G. (2001). Refac- toring testcode.In Proceedingsofthe2ndinternationalconference onex- tremeprogramming and exible processes in software engineering (XP2001), pages 92{95. Wang,S.,Chen,T.-H.,andHassan,A.E.(2018).Understandingthefactors for fast answers in technical q&a websites.EmpiricalSoftware Engineering, **23 (3), 1552{1593.** Yu,C.S.,Treude, C.,andAniche,M.F.(2019).Comprehendingtestcode: An empiricalstudy.CoRR,**abs/1907.13365.** Zaidman, A.,Rompaey,B.V.,Demeyer,S.,andv.Deursen,A.(2008).Min- ing softwarerepositoriestostudyco-evolutionofproductiontestcode.In 2008 1stInternationalConferenceonSoftwareTesting,Veri cation,and Validation, pages220{229. Zeller, A. (2009).Why Programs Fail -AGuidetoSystematicDebugging,2nd Edition. AcademicPress. Zhao, X., Liang, J., and Dang, C. (2019). A strati ed sampling based clustering algorithm forlarge-scaledata.Knowl. BasedSyst.,**163 , 416{428.** Zimmermann, T.,Premraj,R.,andZeller,A.(2007).Predictingdefectsfor eclipse. InProceedingsoftheThirdInternationalWorkshoponPredictor


---

<!-- Página 39 -->

Title

ModelsinSoftwareEngineering, PROMISE07,page9.


---

<!-- Página 40 -->

40


---

<!-- Página 41 -->

Title

**8 Appendix**

Table9:Thestatisticsoftheregressionmodelsshowingadditivedefectex- plainability ofPD(TESTPRODUCT) +PR(TESTPROCESS) metricsover 2the BASE(LOC+CHURNS+PRE+COUPLING).Tot.shows thetotalex- 2planatory powerofthestudiedmodel.Wealsoshowtheproportion of contributed byeachmetric.

22projectTot.AUC

Camel pre bug codeChurn ts coupling BASE+PDcoupling Assertion.Roulette Conditional.Test.Logic General.Fixture Mystery.Guest Redundant.Assertion Duplicate.Assert Resource.Optimism couplingBASE+PD+PR Assertion.Roulette Conditional.Test.Logic General.Fixture Mystery.Guest Redundant.Assertion Duplicate.Assert Resource.Optimism Print.Statement.Added Print.Statement.Removed Eager.Test.Removed

Cassandra pre bug codeChurn leChurn ts coupling tt coupling BASE+PDcoupling tt coupling BASE+PD+PRcoupling tt coupling IgnoredTest.Added Conditional.Test.Logic.Removed Exception.Catching.Throwing.Removed

Flink pre bug codeChurn deletedLine leChurn ts coupling BASE+PDcoupling Conditional.Test.Logic Exception.Catching.Throwing General.Fixture Mystery.Guest Lazy.Test Unknown.Test Magic.Number.Test couplingBASE+PD+PR Conditional.Test.Logic Exception.Catching.Throwing General.Fixture Mystery.Guest Lazy.Test Unknown.Test Magic.Number.Test EmptyTest.Added Mystery.Guest.Added Duplicate.Assert.Removed Magic.Number.Test.Removed


---

<!-- Página 42 -->

42

Table10:Thestatisticsoftheregressionmodelsshowingadditivedefectex- PR(TESTPROCESS) metricsoverplainability ofPD(TESTPRODUCT) + 2the BASE(LOC+CHURNS+PRE+COUPLING).Tot.shows thetotalex- 2planatory powerofthestudiedmodel.Wealsoshowtheproportion of contributed byeachmetric.

22projectTot.AUC

Accumulo pre bug deletedLine leChurn ts coupling tt coupling BASE+PDcoupling tt coupling Conditional.Test.Logic Constructor.Initialization Redundant.Assertion Eager.Test Duplicate.Assert couplingBASE+PD+PR tt coupling Conditional.Test.Logic Constructor.Initialization Redundant.Assertion Eager.Test Duplicate.Assert Duplicate.Assert.Added Unknown.Test.Added Eager.Test.Removed

Bookkeeper pre bug codeChurn leChurn ts coupling BASE+PDcoupling Assertion.Roulette Constructor.Initialization Lazy.Test Unknown.Test Resource.Optimism BASE+PD+PRcoupling Assertion.Roulette Constructor.Initialization Lazy.Test Unknown.Test Resource.Optimism Exception.Catching.Throwing.Added Lazy.Test.Added Unknown.Test.Added Magic.Number.Test.Added General.Fixture.Removed Sleepy.Test.Removed


---

<!-- Página 43 -->

Title

Table11:Thestatisticsoftheregressionmodelsshowingadditivedefectex- PR(TESTPROCESS) metricsoverplainability ofPD(TESTPRODUCT) + 2the BASE(LOC+CHURNS+PRE+COUPLING).Tot.shows thetotalex- 2planatory powerofthestudiedmodel.Wealsoshowtheproportion of contributed byeachmetric.

22projectTot AUC

Hive pre bug codeChurn ts coupling tt coupling BASE+PDcoupling tt coupling Conditional.Test.Logic EmptyTest General.Fixture Lazy.Test Duplicate.Assert Unknown.Test IgnoredTest Resource.Optimism couplingBASE+PD+PR tt coupling Conditional.Test.Logic EmptyTest General.Fixture Lazy.Test Duplicate.Assert Unknown.Test IgnoredTest Resource.Optimism Conditional.Test.Logic.Added Mystery.Guest.Added Duplicate.Assert.Added IgnoredTest.Added Redundant.Assertion.Removed Sensitive.Equality.Removed Eager.Test.Removed Duplicate.Assert.Removed Unknown.Test.Removed Magic.Number.Test.Removed

Wicket leChurn tt coupling BASE+PDcoupling Conditional.Test.Logic Eager.Test Unknown.Test BASE+PD+PR Eager.Test Unknown.Test Assertion.Roulette.Added Conditional.Test.Logic.Added Exception.Catching.Throwing.Added

Zookeeper pre bug codeChurn BASE+PD BASE+PD+PR Unknown.Test.Removed


---

<!-- Página 44 -->

44

Table12:Thestatisticsoftheregressionmodelsshowingadditivedefectex- PR(TESTPROCESS) metricsoverplainability ofPD(TESTPRODUCT) + 2the BASE(LOC+CHURNS+PRE+COUPLING).Tot.shows thetotalex- 2planatory powerofthestudiedmodel.Wealsoshowtheproportion of contributed byeachmetric.

22projectTot AUC

Kafka pre bug codeChurn leChurn ts coupling tt coupling couplingBASE+PD tt coupling Exception.Catching.Throwing Mystery.Guest Redundant.Assertion Lazy.Test Duplicate.Assert Unknown.Test Magic.Number.Test couplingBASE+PD+PR tt coupling Exception.Catching.Throwing Mystery.Guest Redundant.Assertion Lazy.Test Duplicate.Assert Unknown.Test Magic.Number.Test Exception.Catching.Throwing.Added Exception.Catching.Throwing.Removed Print.Statement.Removed

Karaf tt coupling BASE+PDcoupling General.Fixture Print.Statement Sleepy.Test Unknown.Test BASE+PD+PRcoupling General.Fixture Print.Statement Sleepy.Test Unknown.Test Eager.Test.Added IgnoredTest.Added Magic.Number.Test.Added General.Fixture.Removed

Hadoop BASE+PD BASE+PD+PR Duplicate.Assert.Added


---

<!-- Página 45 -->

Title

Table13:Thestatisticsoftheregressionmodelsshowingadditivedefectex- PR(TESTPROCESS) metricsoverplainability ofPD(TESTPRODUCT) + 2the BASE(LOC+CHURNS+PRE+COUPLING).Tot.shows thetotalex- 2planatory powerofthestudiedmodel.Wealsoshowtheproportion of contributed byeachmetric.

22projectTot AUC

Cxf pre bug deletedLine leChurn ts coupling tt coupling BASE+PDcoupling tt coupling Assertion.Roulette Constructor.Initialization Exception.Catching.Throwing couplingBASE+PD+PR tt coupling Assertion.Roulette Constructor.Initialization Exception.Catching.Throwing Sensitive.Equality.Added Exception.Catching.Throwing.Removed Eager.Test.Removed IgnoredTest.Removed

Groovy BASE+PD BASE+PD+PR Duplicate.Assert.Added


---

<!-- Página 46 -->

46

Table14: The e ect size of the test smell metrics on post-release defects. E ect is measured by setting the subject while othermetricsarekept at positive increaseine ect.

project

AccumuloPRODUCT Constructor.Initialization Redundant.Assertion Eager.Test Duplicate.Assert TESTPROCESS Duplicate.Assert.Added Unknown.Test.Added

HivePRODUCT EmptyTest General.Fixture Lazy.Test Duplicate.Assert Unknown.Test IgnoredTest Resource.Optimism TESTPROCESS Sensitive.Equality.Removed Eager.Test.Removed Duplicate.Assert.Removed Unknown.Test.Removed Magic.Number.Test.Removed Conditional.Test.Logic.Added Mystery.Guest.Added Duplicate.Assert.Added IgnoredTest.Added

WicketPRODUCT Eager.Test Unknown.Test TESTPROCESS Conditional.Test.Logic.Added Exception.Catching.Throwing.Added

CassandraPROCESS Exception.Catching.Throwing.Removed IgnoredTest.Added

BookkeeperPRODUCT Constructor.Initialization Lazy.Test Unknown.Test Resource.Optimism TESTPROCESS Sleepy.Test.Removed Exception.Catching.Throwing.Added Lazy.Test.Added Unknown.Test.Added Magic.Number.Test.Added

CamelPRODUCT Conditional.Test.Logic General.Fixture Mystery.Guest Redundant.Assertion Duplicate.Assert Resource.Optimism TESTPROCESS Eager.Test.Removed Print.Statement.Added

GroovyPRODUCT TESTPROCESS

KarafPRODUCT Print.Statement Sleepy.Test Unknown.Test TESTPROCESS Eager.Test.Added IgnoredTest.Added Magic.Number.Test.Added

HadoopPRODUCT TESTPROCESS

metric to 110 % and 150 % of it mean value, theirmeanvalues. Bolded

numbers indicate

^150^

**0.12**      **0.01**

**0.08** **0.01** **0.05**  **0.05** **0.12** **0.01** **0.07**  **0.01** **0.01** **0.01** **0.06**   **0.01** **0.01** **0.01**

**0.01** **0.01** **0.01**   **0.01**

**0.01**

**0.33**   **0.07**  **0.01** **0.01**

**0.01**   **0.01** **0.01** **0.01** **0.01** **0.01**

**0.01**

**0.01** **0.01** **0.01**   **0.01**  **0.01**

**0.01**

a


---

<!-- Página 47 -->

Title

Table15: The e ect size of the test smell metrics on post-release defects. E ect is measured by setting the subject while othermetricsarekept at positive increaseine ect.

project

CxfPRODUCT Constructor.Initialization Exception.Catching.Throwing TESTPROCESS Eager.Test.Removed IgnoredTest.Removed Sensitive.Equality.Added

FlinkPRODUCT Exception.Catching.Throwing General.Fixture Mystery.Guest Lazy.Test Unknown.Test Magic.Number.Test TESTPROCESS Magic.Number.Test.Removed EmptyTest.Added Mystery.Guest.Added

ZookeeperPROCESS Unknown.Test.Removed

KafkaPRODUCT Mystery.Guest Redundant.Assertion Lazy.Test Duplicate.Assert Unknown.Test Magic.Number.Test TESTPROCESS Print.Statement.Removed Exception.Catching.Throwing.Added

metric to 110 % and 150 % of it mean value, theirmeanvalues. Bolded

numbers indicate

^150^

**0.01**  **0.02** **0.01**  **0.01**

**0.04**  **0.01** **0.02**       **0.01**

**0.36** **0.06**   **0.17**  **0.33**   **0.03**

a


---

