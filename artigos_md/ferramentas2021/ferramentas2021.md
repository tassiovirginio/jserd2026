<!-- Página 1 -->

### Test

### Smell

### Detection

### Tools:

### A

### Systematic

### Mapping

### Study

### Wajdi

### Aljedaani

### Anthony Peruma

### Ahmed Aljohani

[wajdialjedaani@my.unt.edu](mailto:wajdialjedaani@my.unt.edu)[axp6201@rit.edu](mailto:axp6201@rit.edu)[ama1177@rit.edu](mailto:ama1177@rit.edu) University of North TexasRochester Institute of Technologyof Denton, Texas, USARochester, New York, USANewUSA

### Mazen Alotaibi

### Mohamed Wiem Mkaouer

### Ali Ouni

[mfa2886@rit.edu](mailto:mfa2886@rit.edu)[mwmvse@rit.edu](mailto:mwmvse@rit.edu)[ali.ouni@etsmtl.ca](mailto:ali.ouni@etsmtl.ca) Rochester Institute of TechnologyofETS Montreal, University of Quebec Rochester, New York, USANewUSAMontreal, Quebec, Canada

### Christian D. Newman

### Abdullatif Ghallab

### Stephanie Ludi

[cnewman@se.rit.edu](mailto:cnewman@se.rit.edu)[Abdullatif.Ghallab@unt.edu](mailto:Abdullatif.Ghallab@unt.edu)[Stephanie.Ludi@unt.edu](mailto:Stephanie.Ludi@unt.edu) Rochester Institute of TechnologyUniversity of North Texasof Rochester, New York, USADenton, Texas, USAUSA

JuneACM,**ABSTRACT** [https://doi.org/10.1145/3463274.3463335](https://doi.org/10.1145/3463274.3463335)Test smells are defined as sub-optimaldesign choices developers make when implementing test cases. Hence, similar to code smells, **1 INTRODUCTION**the research community has produced numerous test smell detec- Software testing is an essential part of the software developmenttion toolsto investigatethe impactof test smellson the quality life cycle. As part of the software developmentprocess, develop-and maintenance of test suites. However, little is known about the ers create and update their system’stest suite to ensure that thecharacteristics, type of smells, target language, and availability of system under test adheresto the requirementsand providesthethese published tools. In this paper, we provide a detailed catalog expected output. However, test code, similar to productionof all known, peer-reviewed, test smell detection tools. is subject to bad programming practices (i.e., smells), which ham-We startwithperformingacomprehensivesearchofpeer- per the quality and maintainability of the test suite48 ].[reviewed scientific publications to construct a catalog of 22 tools. defined in 2001 [], the catalogof test smellshas beensteadilyThen, we perform a comparative analysis to identify the smell types growing throughouttheyears.Whilemosttestsmellsfocusondetected by each tool and other salient features that include pro- traditional Java systems, researchers have also studied the impactgramminglanguage, testing framework support, detection strategy, of these smells on other programminglanguages,and platformsand adoption, among others. From our findings, we discover tools [ 27 , 55,59]. With the growth of the test smell catalog, the researchthat detect test smells in Java, Scala, Smalltalk, and C++ test suites, community, in turn, has utilized these smells to study the impactwith Java support favored by most tools. These tools are available test smells have on the maintainability of test suites. These studiesas command-line and IDE plugins, among others. Our analysis also show that test smellsnegativelyimpactthe comprehensionof ashowsthat most tools overlap in detecting specific smell types, such test suiteand increasechange-and defect-pronenessof the testas General Fixture. Further, we encounter four types of techniques suite, thereby increasing its flakiness63[]. In addition to definingthese tools utilize to detect smells. We envision our study as a one- test smells,researchershave also providedthe communitywithstop source forand practitionersin determiningthe various tools to detect such test smells. Furthermore, research hastool appropriatefor their needs.Our findingsalso empowerthe shownthat early detection of bad smells reduces maintenance costs,community with information to guide future tool development. highlighting the importance of such detection tools. **ACM**With the growth of test smells studies, recent literature reviews Wajdi Aljedaani, Anthony Peruma, Ahmed Aljohani, Mazen Alotaibi, Mo-[ 35 , 36] have been proposedto study various dimensionsrelated hamed to these anti-patterns. These literature reviews have explored the and various definitionsof test smells,empiricalanalysisof their sur-Study. In Evaluation and Assessment in Software Engineering (EASE 2021), vival, spread, refactoring, and their relationship with change and bug proneness of source code. However, little is known about the Permission toolsets used to detect test smells. The availability of tools is vitalclassroom for software engineering researchers and practitioners. In research,for ontools facilitate the reproducibility of studies while developers bene- must fit from improved productivity through tool adoption. Without ato fee.thoroughunderstanding of available tools and how thesecom- EASEpare to one another, it will be difficult to conduct future research © 2021 that uses the right toolset for a given research problem. Therefore,ACM [https://doi.org/10.1145/3463274.3463335](https://doi.org/10.1145/3463274.3463335)our work complements these reviews by not only extracting all the

170


---

<!-- Página 2 -->

EASE

**Table 1: The digital libraries queried in our study.**test smell detection tools published in peer-reviewed venues, but also providing more in-depth details about them. To facilitate their**Digital****URL** ACM[https://dl.acm.org/](https://dl.acm.org/)adoption, wecompareandcontrastmultipleattributesofthese IEEE[https://ieeexplore.ieee.org/](https://ieeexplore.ieee.org/)tools, such as supported smell types, target environment, detection Science[https://www.sciencedirect.com/](https://www.sciencedirect.com/)mechanisms,etc. Hence, our work provides a catalog for developers Scopus[https://www.scopus.com/](https://www.scopus.com/)and researchers to support the adoption of these tools. Springer[https://link.springer.com/](https://link.springer.com/) Web[https://webofknowledge.com/](https://webofknowledge.com/)**1.1 Goal**& Research Questions detection-based tools,wereassociatedwithtechnicaldebt,bad The goalofthisstudyistoprovidedevelopersandresearchers smells, bug localization,and architecturalsmells.Further, while with a one-stopsourcethatoffersa comprehensiveinsightinto Garousi and Küçük [] provide a list of test smell detection tools test smell detection tools. The information in this study will as part of their SMS on test smells, our study aims to expand on researchers to select the right tool for their research task and provide this listing. Hence, in this section, we describe the procedurewe data-driven advice on how test smell tools can be advanced through adopt to search and selectthe relevantpublicationsfor analysis. future work . Throughthisstudy,thecommunitywillbebetter In brief, our methodologyconsists of three phases– (1) planning, equipped to determine the correct tool they need to utilize to satisfy (2) execution,and (3) synthesis.In the following subsections,we their requirement, along with the shortcomings of these tools. This elaborate on these phases. work also provides the research community with insight into areas that require improvedautomation.Hence, we aim at addressing**2.1 Planning** the following research questions (RQs): In this phase, we detail our publications search strategy. In confor- **RQ****: What test smell detection tools are available to the**1mance with systematic mapping studies, we utilize a specific set of **community,**and what are the common smell types they sup- domain-specific(i.e., test smell related) keywords to search, in pop- **port? This RQ investigates the volume of test smell detection tools** ular digital libraries, for publications that meet our requirements. released by the research community. We answer this RQ by per- **Digital Libraries.**Tolocate publications for our study, we searchforming an extensiveandcomprehensiveon six popular six digitallibraries.Theselibraries,listedin Table 1, eithercon-libraries among the software engineeringcommunity. We tain orindexpublicationsfromcomputerscienceandsoftwareinvestigate the frequency of tool release, and the spectrum of test engineering venues and are utilized by similar studies (e.g., [32]).smells detected by the tools.

**RQ****: What are the main characteristics of test smell de-**2**Inclusion/Exclusion Criteria.**Inclusion andexclusioncriteria **tection tools?**In this RQ, we examinethe design-levelfeaturesare crucial in pruning our search space, reducing bias, and retrieving that are commonto testsmelldetectiontools,suchas platformrelevantpeer-reviewed scientific publications. Selected publications supportand smell detection mechanisms. This RQ provides us withof these criteria become our starting point for manual filtering, to details into how the research community constructs such tools andsee whether they fit in our study, i.e., propose or adopt a test smells provides insight into the development of future tools.tool. The initial pool of publications also serves for: (1) backward snowballing, i.e., analyzing publications cited by the selected pool; **1.2 Contributions**and (2) forward snowballing, i.e., analyzing publications citing our Through this study, we provide the community of researchers andpool publications. Table 2 lists the inclusion and exclusion criteria practitionerswith a view and insights on the history of the availabil-considered in this study. With regards to the time range, we did ity of test smell detection tools. More specifically, our contributionsnot set a starting date. However, our end date was set to the end of are outlined below:December2020. Hence, the date range criterion allows the selection of any tool as long as it appeared before December 31, 2020.•A catalog of 22, peer-reviewed, test smell detection tool publica- tions, and publications that utilize these tools. These provide an initial platform for future research in this area.**Table 2: Our inclusion and exclusion search criteria.** •A series of experimentshighlightingthe growth of such tools, along with a comparison of key tool attributes. •A discussionofhowourfindingsprovideinsightintofuture research areasinthisfieldalongwithdetailsthatneedtobe considered when selecting a test smell detection tool. •A replication package of our survey for extension purposes [1].**Search Keywords.**To determinethe optimalset of searchkey- words, weconductedapilotsearchontwowell-knowndigital **2 RESEARCH**METHODOLOGYlibraries, i.e., IEEE and ACM. This process intends to identify rel- Being a SystematicMappingStudy (SMS), our research exploresevant words or synonymsutilizedin test smell publications.We publishedscientific literature to gather information about a specificperformed multipleinstancesof the pilot search,where each in- topic in software engineering,and to provide a high-level under-stance involvedrefinementofthekeywordtermsinthesearch**Inclusion****Exclusion** standingand/or answering exploratory research questions21[ Toquery. We conduct our query only on the title and abstract of thePublishedWebsites, WrittenPublishedthis extent, our SMS aims at proving a high-levelunderstandingpublication.We decided to apply the search on a publication’s meta- AvailableFull-textof the existence of test smell detection tools, their characteristics,data instead of on the full-text to avoid false positives. The finalizedProposeTools and their adoption in academic studies. Prior studies in catalogingsearch string is presented below.

171


---

<!-- Página 3 -->

Test

publication.We decided to apply the search on a publication's3 meta-Findings data instead of on the full-text to avoid false positives. The nalized TestIn this section, we present the ndings for our proposed RQs based search string is presented below. on the synthesis of the nalized set of 47 test smell tool detection- relatedpublications, which are composed22 publicationsofthat**3 RESEARCH**FINDINGS Title:("tool*" OR"detect*"OR"testsmell"ORproposenew tools and 25 publications that adopt these tools. In this section, we present the findings for our proposed RQs based"test smells")ANDAbstract:("testsmell"OR on the synthesis of the finalized set of 47 test smell tool detection-3.1RQ: What testdetection tools are available to the1smells" OR"testcode"OR"unittestsmell") relatedpublications, which are composed of publications thatcommunity,and what are the common smell types they **propose**new tools and 25 publications that adopt these tools.support? 2.2 Execution This RQcomprisesoffourparts.Intherstpart,weprovidea**3.1 RQ****: What test smell detection tools are**1In this phase, we detail how we process and lter the publicationsbreakdown of the publicationsby publicationdate and venue. In**2.2 Execution****available to the community, and what are**we obtain from our digital library search. Our initial search of thethe second part, we present the tools identied in our systematic **the common smell types they support?**In this phase, we detail how we process and filter the publicationssix digital libraries results in 436 publications, with ScienceDirectsearch,while in the third part, we provide insight into the types of we obtain from our digital library search. Our initial search of theresultingin the highest number of publications (126). Next, we em-This RQcomprisesoffourparts.Inthefirstpart,weprovideatest smells detected by the identied tools. Finally, the fourth part sixdigitallibraries resultsin 436 publications,withScienceDirectploya four-stagequalityprocessto lterout publicationsbreakdown of theby publicationdate and venue. Inlooks at the programming languages supported by the test smells. resultingin not highestnumberof publications(126). Next,weem-that werepartofour inclusioncriteria.Figure1depictsthethe second part, we present the tools identified in our systematic 3.1.1 PublicationYears & Venuesploy a four-stagequality controlprocessto filter outof publicationslteredat eachThissearch, while in the third part, we provide insight into the types of Figure 2 depicts the yearly breakdown of tool publications. Thethatwerenot partof ourinclusioncriteria.1 the publicationstheprocessinvolvesthreeauthorsmanuallyreviewingtest smells detected by the identified tools. Finally, the fourth part rst test smell tool, TRex], appeared[in 2006. Since then, therevolumeof publicationsfiltered ateachstage.Thisqualityto determineif a publicationcanpassfromonestage controlanother. Thelooks at the programming languages supported by the test smells. was a steady trend of one or two tools appearing every one or twoprocessinvolvesthreeauthorsmanuallyreviewingthepublicationsrst stagestartswithremovingduplicateandretractedpublications; 3.1.1**Publication Years & Venues**.years, until 2018. The years 2019 and 2020 witnessed a notable in-to determineif a publicationcan passone stage to another. Thepublicationswere removed,and fromcandidatemade Figure 2 depicts the yearly breakdown of tool publications. Thecreasein tool-based publications compared to the prior years, withfirststagestartswithremovingduplicateretractedpublications;it tothenextstage.In thesecond stage,we applyour inclusion and first test smell tool, TRex20[], appeared in 2006. Since then, thereapproximately51% of tool development and adoption publications74were removed,362candidatemadeexclusioncriteriato the titleandabstract.For instance,we discard was a steady trend of one or two tools appearing every one or twooccurringin these two years. There can be many factors inuencingitto publicationsnext stage.In thesecondinclusionandallthatwerenot stage, we apply ourdidnot proposeor years, until 2018. The years 2019 and 2020 witnessed a notable in-this recenthype. We have observedthe following:The dynamicexclusionto thetitle andabstract. Forinstance,wediscardadopt a tool. Thisthoroughprocedureresultedinonlyincluding creasein tool-based publications compared to the prior years, withnatureof detection mechanisms of traditional state-of-the-art toolsallpublications.thatwerenot peer-reviewedor adidnot proposeor54Thethirdinvolvesfull-textanalysisof each approximately51% of tool development and adoption publicationsmade them require compilable projects with constraints over howadopt a tool. This thorough procedure resulted in only includingselectedpublication. Using our inclusion and exclusion criteria, we occurringin these two years. There can be many factors influencingtest les should be written and located. Therefore, traditional tools54 publications. The third stage involves a full-text analysis of eachretain only 30In the last stage, we performthe for- this recent hype. We have observedthe following:The dynamicare implementedto run as standaloneapplicationsor pluginsinselected publication. Using our inclusion and exclusion criteria, weward and backward snowball sampling, resulting in 17 publications. natureof detection mechanisms of traditional state-of-the-art toolsIntegrated Development Environments (IDEs). Besides being con-retain only 30 publications.In the last stage, we perform the for-Therefore, we ended up with a nal set of 47 made them require compilable projects with constraints over howstrained to theirenvironments,they are not intendedto run onward and backward snowball sampling, resulting in 17 publications. 2.3 Synthesistest files should be written and located. Therefore, traditional toolslarge-scale software systems. However, the tools that appeared inTherefore, we ended up with a final set of 47 publications. are implementedto run as standaloneapplicationsor pluginsinThis phase synthesizes the extracted data to answer our RQs.recentFirst,years were developed as APIs, facilitating their deployment Integrated Development Environments (IDEs). Besides being con-we classify the primary set of publications into one of two types,to minei.e.,software repositories. While their detection strategies carry strained to theirenvironments,they are not intendedto run ontool development or tool adoption. Toolpublicationsthe false-positiveness of static analysis, they allowed the analysis**2.3 Synthesis**large-scale software systems. However, the tools that appeared inare studies that propose a test smell detectiontool, eitherof a widepartvarietyof softwaresystems.Therefore,the numberof This phase synthesizes the extracted data to answer our RQs. First, recent years were developed as APIs, facilitating their deploymentof proposinga new catalogof smellsor detectingexistingempiricalsmellpublications,adoptingthese tools, has signicantlyin- we classify the primary set of publications into one of two types, i.e.,to mine software repositories. While their detection strategies carrytypes. Tool adoption publications are studies that utilize ancreased,existingreachingup to 16 in two years, higher than the number tool development or tool adoption. Toolpublicationsthe false-positiveness of static analysis, they allowed the analysistest smell detection tool as part of their study design. Additionally,of all previoustool adoptionpublicationscombined.These stud- are studies that propose a test smell detection tool, either as partof a wide varietyof softwaresystems.Therefore,the numberofwe also classify studies by publicationyear and venue; thisieshelpshave explored various characteristicsof test smells, including of proposinga new catalogof smellsor detectingexistingsmellempirical publications,adoptingthese tools, has significantlyin-with partly answering RQ. For the remainder of RQRQ, weco-occurrence, survivability, severity, refactoring, impact on aky112 types. Tool adoption publications are studies that utilize an existingcreased, reaching up to 16 in two years, higher than the numbermanuallyreview the full-text of each tool development publication.tests,proneness to changes and bugs, etc. Next, in Figure 3, we pro- test smell detection tool as part of their study design. Additionally,of all previous tool adoptionpublicationscombined.These stud-As part of this review, we evaluate each study based on concretevide a pictorial representation, in the form of a timeline, depicting we also classify studies by publication year and venue; this helpsies have explored various characteristicsof test smells, includingevidence present in the publication (and its supporting artifacts,the releaseifof the 22 test smell detection tools. Analyzing the with partly answering RQ. For the remainder of RQand RQ, weco-occurrence, survivability, severity, refactoring, impact on flaky112any) withoutany vague assertions.For each tool, we extracttypesthedetected by eachwe specify, in green, the total number manuallyreview the full-text of each tool development publication.tests, proneness to changes and bugs, etc. Next, in Figure 3, we pro-types of test smells the tool detects and other tool features,of smellasdetected by each tool. Additionally, we also indicate, As part of this review, we evaluate each study based on concretevide a pictorial representation, in the form of a timeline, depictingsupported programming language, testing framework, correctness,in red, the number of net new test smell types and theof evidence present in the publication (and its supporting artifacts, ifthe release of the 22 test smell detection tools. Analyzing theetc. We elaborate further on the tool features in Section 3.2existingwhensmelltypesin blue.ReadingFigure3 fromleftto right any) without any vague assertions.For each tool, we extract thetypes detected by eachwe specify, in green, the total numberpresenting our ndings for.RQ(i.e., the oldest tool to newest), a smell type rst introducedby a2 types of test smells the tool detects and other tool features, such asof smelldetected by each tool. Additionally, we also indicate,Finally, all RQ-related data collected during the publicationtool isre-in blue text, while its subsequent appearance in another tool supported programming language, testing framework, correctness,in red, the number of net new test smell types and theofview task was peer-reviewedto ensure bias mitigation, withiscon-in red. For example,the GeneralFixturesmell rst appearsin etc. We elaborate further on the tool features in Section 3.2 whenexisting smelltypesin blue.ReadingFigure3 fromleftto righticts resolvedthroughdiscussions.We utilizeda spreadsheetTestQto(henceit is shown in blue text), this smell next appearsin presenting our findings for RQ.(i.e., the oldest tool to newest), a smell type first introducedby a2hold the manually extracted data to facilitate collaborationtheduringunnamed tool (hence it is shown in red text), and so on. Finally, all RQ-related data collected during the publication re-tool is in blue text, while its subsequent appearance in another toolthe author-review process. The authors, participating in the lter-In terms of venues, looking at the complete set of primary pub- view task was peer-reviewed to ensure bias mitigation, with con-is in red. For example,the GeneralFixture smell first appearsining stages and manual review, are experienced with this research.lications, 40 publicationsare associatedwith a conference/work- flicts resolvedthroughdiscussions.We utilizeda spreadsheettoTestQ (hence it is shown in blue text), this smell next appears inThey have published work in this area, including dening testshop/symposium,smellwhile seven publications appear in journals. Look- hold the manually extracted data to facilitate collaboration duringthe unnamed tool (hence it is shown in red text), and so on.types, tool development, and adoption [55, 56].ing at just tool development publications, 20 of these publications the author-review process. The authors, participating in the filter-In terms of venues, looking at the complete set of primary pub- ing stages and manual review, are experienced with this research.lications, 40 publicationsare associatedwith a conference/work- They have published work in this area, including defining test smellshop/symposium,while seven publications appear in journals. Look- types, tool development, and adoption [55, 56].ing at just tool development publications, 20 of these publications

172


---

<!-- Página 4 -->

Count

Publication

EASEEASE

**Figure 1: Overview of the volume of publications resulting from our filtering process.**Figure 1: Overview of the volume of publications resulting from our ltering process.

14releasedTestQ[27]. The tool provides a visual interface for develop-releasedTestQ[27]. The tool provides afor ToolDevelopmentToolAdoptioners to explore test suites and detects 12 test smells in C++ test suites.ers to explore testand12 testin C++ test The tool facilitates customizations such as smell prioritization.The tool facilitatessuch as 12In 2009 Koochakzadeh and Garousi released**TeReDetect**[ 45 ]In 2009 Koochakzadeh and Garousi releasedTeReDetect[45] (TestRedundancy Detection), a test redundancy detection tool for(TestRedundancy Detection), a testtool for JUnit tests that work in conjunction with a code coverage tool. TheJUnit tests that work inwith a codeThe10 authors then releasedTeCReVis(Test Coverage and Test Redun-authors then releasedTeCReVis(Test Coverage and Test Redun- dancy Visualization) in 201044[ ], an Eclipse plugin that providesdancy Visualization)in 201044], [Eclipse plugin that9 developerswith a visualization of a project’s test coverage and test8developerswith a visualization of a project's testand test 7redundancy.**Bavota et al. [ 22] released**anunnamedtestsmellredundancy.Bavota etal.[22] releasedanunnamedtestsmell detectiontool in 2012. The tool detects nine test smell types in Javadetectiontool inThe toolnine testin Java 6test suites. The tool prioritizes recall over precision resulting in atest suites. The tooloverin a long list of potential issues and thereby require manual reviews.long list of potentialand 2013 sawthereleaseoftwodetectiontools.Greileretal.in-2013 sawthereleaseoftwodetectionetal.in-4 troduce TestHound[39]. This static analysis tool focuses on testtroduceTestHound[39]. This statictoolon test smells related to test fixtures in Java test suites and recommendssmells related to test xtures in Java testand11 refactorings toaddressthedetectedissues.Inauserstudy, the2refactorings totheInauserthe244 311authors show that developers are appreciative of the tool with re-authors show that developers areof the tool with re-22222 gards to understanding test fixture code. Greiler et al. improve ongards to understanding test xtureet al.on1111 0their prior tool by releasing**TestEvoHound [ 40]. This improved**their prior tool byTestEvoHound[40]. This improved200620072008201020122013201420152016201820192020 tool analyzes Git or SVN repositories to analyze the evolution of atool analyzes Git or SVN repositories totheof aYear system’s test fixture code. As part of the analysis process, the toolsystem's test xtureAs part of thethe tool Figure 2: Yearly breakdown of tool publications.does a checkout and build of each revision of the project and then**Figure 2: Yearly breakdown of tool publications.**does a checkout and build of eachof theand then passes the revision to TestHound to detect test fixture smells.passes the revision tototest xture Zhang et al. released**DTDetector , a JUnit supported test depen-**are associatedwitha conference/workshop/symposium.Finally,Zhang et al. releasedDTDetector, a JUnit supported testare associatedwitha conference/workshop/symposium.Finally, dency detection tool in 201475[]. Also released in 2014 by Huo etthe most popular venue for a tool development publication is thedency detection tool in 201475]. Also released in 2014 by Huo et al.the most popular venue for a tool development publication is the al. [ 42], isOraclePolish, which utilizes a dynamic tainting-basedJoint European Software Engineering Conference and Symposium[42], is,a dynamic tainting-based tech-Joint European Software Engineering Conference and Symposium technique for the detectionof two testsmelltypesin JUnitteston the Foundations of Software Engineering, with four publications.nique for theof two test smell types in JUnit test suites.on the Foundations of Software Engineering, with four publications. suites. Thetool’sempiricalevaluationdemonstratesthatitcanThe complete breakdown is available in our replication package.The tool'sthat it can detect bothThe complete breakdown is available in our replication package. detect both brittle assertionsand unused inputs in real tests at aandin realat a reasonable 3.1.2**Test**Smell Detection Tools.In this part of the RQ, basedTestSmell Detection Toolsreasonable cost. In 2015, Bell et al. released**ElectricTest [ 24 ], an-**InBell et al.[24], another depen- on availabledocumentation(i.e., full-textof the publicationandIn this part of the RQ, basedonother dependency detection tool for JUnit test suites. The authorsdencytool fortestThedemonstrate any of its supportingartifacts),we providean overviewof eachfull-text of the publication and any of itswedemonstrate that their tool outperforms DTDetector in test paral-thattoolin test parallelization. Also tool, from the oldest to the most recent.providean overview of eachfrom theto the mostlelization. Also released in 2015 was**PolDetby Gyori et al.41**[ ],in 2015 wasbyet al.41],[ a test pollution Releasedin 2006 is**TRex by Baker et al. 20**[ ]. This tool analyzesReleasedin 2006TRexisby Baker et al.20].[ This tool analyzesa test pollution smell detection tool. The tool analyses heap-graphsThe tooland le-system for TTCN-3 test suites for issues specific to this testing framework.for TTCN-3 test suites forspecic to thisand file-system states during test execution for instances of statetestforofpollution(e.g., The tool also provides developers with the ability to correct identi-The tool also provideswith thetopollution (e.g., tests reading/writing shared resources). fied issues. TestLint, released by Reichhart et al.59[ in 2007, is aed issues.TestLint, released by Reichhart et59al.in [is aPalomba et al. [] released**Taste(Textual AnalySis**for TestPalomba et al.52] releasedTaste(Textual AnalySisfor Test rules-based tool that detects 27 quality violations in the unit testrules-based tool that27in the unit testsmEll detection)in 2018.ThistoolutilizesinformationretrievalsmEll detection)inThistool code in Smalltalk systems. In 2008, Breugelmans and Van Rompaeycode in Smalltalk systems. Inand Van

173

### I

### n i

### t

### i

### a l

###

### p o o l

###

### o f

###

### p u b l

### i

### c a t

### i

### o n s

# A

# C

# M

# 2 4

##

# I

# E

# E

# E

# 7 5

# W

# e b

# o f

#

# 3 3

# s c i

# e n c e

# S

# c o p us

# 9 3

# 1 2 6

# S

# c i

# e n c eD

# i

# r

# e c t

# 8 5

# S

# p r

# i

# n g e r

# 4 3 6

### R

### e m

### o v a l

### r

### e t

### r

### a c t

# -

# 7 4

## S

## t

## a g e

###

### o f

###

### d u p l

### e d

### p u b l

# 3 6 2

## 1

### i

### c a t

### e

###

### &

###

### i

### c a t

### i

### o n s

### F u l

# -

# 3 0 8

# -

# 2 4

# 5 4

## S

## t

## a g e

## 2

###

### T i

### t

### l

### e

### &

###

### a b s t

### r

### a c t

### f

### i

### l

### t

### e r

### i

### n g

## S

## t

## a g e

## 3

### l

### -

### T e x t

###

### f

### i

### l

### t

### e r

### i

### n g

# +

# 1 7

# 3 0

# 1 7

## S

## t

## a g

## e

## 4

###

### S n o w

### b a l

### l

###

### s

### a m

### p l

### i

### n g

# 4 7

### F i

### n a l

###

### s e t

###

### o f

###

### p u b l

### i

### c a t

### i

### o n s


---

<!-- Página 5 -->

Test

**Figure 3: Timeline of the release of test smell detection tools by the research community.**

techniquesto detect three test smell types in Java test suites. ResultsFinally,when compared against the catalog of Garousi and Küçük from an empirical study show that the tool is 44% more effective[36], our dataset containsten of the 12 listed tools. The tools ex- in detecting test smells when compared to structural-based detec-cluded from our study are not proposed in peer-reviewed literature. tion tools. Also released in 2018PraDeTis, by Gambi et al.34[].The common set of tools are indicated in RQ2. This tool detects manifest test dependencies and can analyze large projects containing a vast quality of tests.3.1.3**Detected Test Smell Types**. There were four test smell detection tools released in 2019.**ts-**Next, we examine the types of test smells detected by the identi- **Detect, released by Peruma et al.**56[ detects a total of 19 testfied tools in our set. For completeness, we provide, in Table 3, brief smell types. Thetypes comprise of 11 newly introduceddefinitions for each unique smell type detectedby the identified and 8 existingtypes.The tool utilizesan abstractsyntaxtree totools. We also provide their references for more details. When ana- analyzes JUnit test suites and reports an average F-score of 96.5%lyzing the definitionsof these smell types, we observe that there for each smell type. Further, onetype (i.e.,Default Test ) isare smells that are associated with more than one name, but with a exclusiveto Android applications, while the remaining types applysimilar description of its symptoms. For example,Assertionless, As- to all Java systems.**SoCRATES(SCala RAdar for TEst Smells) by**sertionless Test, andUnkown Testdefine the absence of an expected De Bleser et al.30[ ] detects the presence of six smell types in Scalaassert in the test method. Similarly,Duplicated Code and TestCode systemsusing static analysis. Virginio et al. released**JNose Test**, aDuplication define the same issue of the existence of code clones. tool with the ability to detect 21 test smell types in Java systems.Looking at our list of tools, TestLint detects the highest number Additionally,the tool also provides ten metrics around code cover-of smell types (26). JNose Test is the second highest with 21 detected age. Biagiola et al. released**TEDD (Test Dependency Detector), a**smell types, followed bytsDetect(19types). Furthermore, tool to detect test dependencies in end-to-end web test suites25 ]. [from Figure 3, it is common to see various tools detecting the same The tool presents a list of manifest dependenciesas output fromsmell types. Per analogy to code smells, while there is an agreement its execution.Delplanqueet al.31[ ] released**DrTest**, a tool thaton the meaningsof smells,there is no consensuson identifying detects Rotten Green Testsmell in the Pharo ecosystem.them. Therefore, it is evident to see various tools containingdif- 2020 saw the release of two IDE plugins and one command-lineferent detectionstrategiesfor similar smell types. Hence, in this tool. Lambiase et al.46[ ] released DARTS(Detection And Refac-analysis,we look at the overlap of detected smell types by the tools toring of Test Smells), a plugin that utilizes information retrieval toin our dataset. The smells, detectedby the toolsTestLint , Oracle- detect three smell types. The tool also offers refactoringsupport.Polish , TRex , andPolDetare uniqueto therespectivetool.The **RAIDE , an Eclipse plugin was released by Santana et 60**al.]. Thisremaining 16 tools share the detection of some overlapping smells. plugin detects and provides semi-automatedrefactoringsupportIn Table 4, we identify the overlapping of smells across 16 tools. for twotestsmelltypesin JUnittestsuites.Martinezet47al. [For each tool, we indicate if the tool detects a specific smell by the √releasedRTj,a command-line tool that supports the detection andsymbol. From this table, we observe that the three most common refactoring ofRotten Green Testsmells.smell types areGeneral Fixture, Eager Test, and Assertion Roulette, which are respectively detected by 9, 7, and 6 tools.

174

# 2 7

# 0

# 2 7

# T e s t

# L

# i

# n

# t

## -

##

## A

## b n o r

## m

## a l

##

## U

## T F -

## U

## s e

## -

##

## A

## n o n ym

## o u s

## T e s t

## -

##

## A

## s s e r

## t

## i

## o n l

## e s s

## T e s t

## -

##

## C

## o m

## m

## e n t

## s

## O

## n l

## y

## T e s t

## -

##

## C

## o n t

## r

## o l

##

## L o g i

## c

## -

##

## E

## a r

## l

## y

## R

## e t

## u r

## n i

## n g

## T e s t

## -

##

## E

## m

## p t

## y

## S

## h a r

## e d -

## F i

## x t

## u r

## e

## -

##

## E

## m

## p t

## y

## M

## e t

## h o d C

## a t

## e g o r

## y

## -

##

## E

## m

## p t

## y

## T e s t

## -

## M

## e t

## h o d C

## a t

## e g o r

## y

## -

##

## G

## u a r

## d e d

## T e s t

## -

##

## L i

## k e l

## y

## i

## n e f

## f

## e c t

## i

## v e

## O

## b j

## e c t

## -

## C

## o m

## p a r

## i

## s o n

## -

##

## L o n g

## T e s t

## -

##

## M

## a x

## I

## n s t

## a n c e

## V a r

## i

## a b l

## e s

## -

##

## M

## i

## x e d

## S

## e l

## e c t

## o r

## s

## -

##

## O

## v e r

## c o m

## m

## e n t

## e d

## T e s t

## -

##

## O

## v e r

## r

## e f

## e r

## e n c i

## n g

## -

##

## P

## r

## o p e r

##

## O

## r

## g a n i

## z a t

## i

## o n

## -

##

## R

## e t

## u r

## n i

## n g

## A

## s s e r

## t

## i

## o n

## -

##

## T e a r

## d o w

## n

## O

## n l

## y

## T e s t

## -

##

## T e s t

## -

## C

## l

## a s s

## N

## a m

## e

## -

##

## T e s t

## -

## M

## e t

## h o d C

## a t

## e g o r

## y

## N

## a m

## e

## -

##

## T r

## a n s cr

## i

## p t

## i

## n g

## T e s t

## -

##

## U

## n c l

## a s s i

## f

## i

## e d

## M

## e t

## h o d C

## a t

## e g o r

## y

# 1

# 0

# 1

## -

##

## U

## n d e r

## -

## t

## h e -

## c a r

## p e t

##

## A

## s s e r

## t

## i

## o n

## -

##

## U

## n d e r

## -

## t

## h e -

## c a r

## p e t

##

## f

## a i

## l

## i

## n g

## A

## s s e r

## t

## i

## o n

# T

# R

# e x

## -

##

## U

## n u s ed

## S

## h a r

## e d -

## F i

## x t

## u r

## e

## V a r

## i

## a b l

## e s

# -

#

## T T C

## N

## -

## 3

## S

## m

## e l

## l

## s

## -

##

## U

## n u s ual

##

## T e s t

##

## O

## r

## d e r

# 2

# 0

# 0

# 7

# 2

# 0

# 1

# 2

# 0

# 0

# 6

# 2

# 0

# 0

# 8

## -

##

# A

# s s e r

# t

# i

# o n l

# e s s

## -

##

## T e s t

##

## R

## e d u ndancy

## -

##

# A

# s s e r

# t

# i

# o n

# R

# o u l

# e t

# t

# e

## -

##

# D

# u p l

# i

# c a t

# e d

# C

# o d e

## -

##

# E

# a g e r

#

# T e s t

# T e C

# R

# c V

# i

# s

## -

##

# E

# m

# p t

# y

# T e s t

## -

##

# F o r

#

# T e s t

# e r

# s

# O

# n l

# y

# 1

# 0

# 1

## -

##

# G

# e n e r

# a l

#

# F i

# x t

# u r

# e

## -

##

# I

# d e n t

# e d

# T e s t

## -

##

# I

# n d i

# r

# e c t

#

# T e s t

## -

##

# M

# y s t

# e r

# y

# G

# u e s t

## -

##

# S

# e n s i

# t

# i

# v e

# E

# q u a l

# i

# t

# y

## -

##

# V e r

# b o s e

# T e s t

# T e s t

# Q

# 1 2

# 0

# 1 2

# 1

# 8

# 9

# U

# n

# n

# a m

# e d

# -

#

# A

# s s e r

# t

# i

# o n

# R

# o u l

# e t

# t

# e

# -

#

# E

# a g e r

#

# T e s t

# -

#

# F o r

#

# T e s t

# e r

# s

# O

# n l

# y

# -

#

# G

# e n e r

# a l

#

# F i

# x t

# u r

# e

# -

#

# I

# n d i

# r

# e c t

#

# T e s t

# i

# n g

# -

#

# L a z y

# T e s t

# -

#

# M

# y s t

# e r

# y

# G

# u e s t

# -

#

# T e s t

#

# C

# o d e

# D

# u p l

# i

# c a t

# i

# o n

# -

#

# S

# e n s i

# t

# i

# v e

# E

# q u a l

# i

# t

# y

# 0

# 2

# 0

# 1

# 2

## -

##

## T e s t

##

## R

## e d u ndancy

# T e R

# e D

# e t

# e c t

# 0

# 1

# 1

# 2

# 0

# 2

# O

# r

# a c l

# e P

# o

# l

# i

# s h

## -

##

# B

# r

# i

# t

# t

# l

# e

# A

# s s e r

# t

# i

# o n

## -

##

# U

# n u s ed

# I

# n p u t

# s

# 2

# 0

# 1

# 3

## -

##

# D

# e a d

# F i

# e l

# d

## -

##

# G

# e n e r

# a l

#

# F i

# x t

# u r

# e

## -

##

# L a c k

# o f

#

# C

# o h e si

# o n

# o f

#

# T e s t

#

# M

# e t

# h o d

## -

##

# O

# b s c ur

# e

# I

# n -

# L i

# n e

# S

# e t

# u p

## -

##

# T e s t

#

# M

# a v e r

# i

# c k

## -

##

# V a g ue

# H

# e a d er

#

# S

# e t

# u p

# T e s t

# H

# o

# u

# n

# d

# 5

# 1

# 6

# L

# e

# g

# e

# n

# d

# N

# u m

# b e r

#

# o f

#

# n e w

#

# t

# e s t

#

# s m

# e l

# l

#

# t

# y p e s

# N

# u m

# b e r

#

# o f

#

# e x i

# s t

# i

# n g

# t

# e s t

#

# s m

# e l

# l

#

# t

# y p e s

# T o t

# a l

#

# n u m

# b e r

#

# o f

#

# d e t

# e c t

# e d

# t

# e s t

#

# s m

# e l

# l

#

# t

# y p e s

# 0

# S

# O

# 1

# 0

# 1

# 1

# 1

# 0

# 1

# 1

# 0

# -

#

# A

# s s e r

# -

#

# E

# a g e r

# E

# l

# e c t

# r

# i

# c T e st

# P

# o

# l

# D

# e t

# D

# T

# D

# e t

# e c t

# o

# r

# -

#

# G

# e n e r

# -

#

# L a z y

# -

#

## T e s t

##

## P

## o l

## l

## u t

## i

## o n

# -

#

## D

## e p e ndent

##

## T e s t

##

# -

#

## D

## e p e ndent

##

## T e s t

##

# -

#

# M

# y s t

# -

#

# S

# e n s i

# 2

# 0

# 1

# 4

# 2

# 0

# 1

# 5

# 2

# 0

# 1

## -

##

# E

# a g e r

#

# T e s t

## -

##

# D

# e a d

# F i

# e l

# d

## -

##

# G

# e n e r

# a l

#

# F i

# x t

# u r

# e

## -

##

# G

# e n e r

# a l

#

# F i

# x t

# u r

# e

## -

##

# L a c k

# o f

#

# C

# o h e si

# o n

## -

##

# L a c k

# o f

#

# C

# o h e si

# o n

# o f

#

# o f

#

# T e s t

#

# M

# e t

# h o d

# T e s t

#

# M

# e t

# h o d

## -

##

# O

# b s c ur

# e

# I

# n -

# L i

# n e

# S

# e t

# u p

## -

##

# T e s t

#

# M

# a v e r

# i

# c k

# T A

# S

# T

# E

## -

##

# V a g ue

# H

# e a d er

#

# S

# e t

# u p

# 0

# 3

# 3

# T e s t

# E

# v o

# H

# o

# u

# n

# d

# 0

# 6

# 6

# 6

# 6

# C

# R

# A

# T

# E

# S

# 0

# t

# i

# o n

# R

# o u l

# e t

# t

# e

#

# T e s t

# a l

#

# F i

# x t

# u r

# e

# T e s t

# -

#

## T e s t

# e r

# y

# G

# u e s t

# t

# i

# v e

# E

# q u a l

# i

# t

# y

# 8

## -

##

## T e s t

##

## R

## e d u ndan

## c y

# P

# R

# A

# D

# E

# T

# 1

# 0

# 1

# 1

# T

# E

# D

# D

##

## R

## e d u ndancy

# 2

# 1

# 0

# 1

# 1

# 1

# 0

# D

# r

# T e s t

# -

#

## R

## o t

## t

## e n

## G

## r

## e e n

## T e s t

# 9

# 2

## -

##

# E

# a g e r

#

# T e s t

## -

##

# G

# e n e r

# a l

#

# F i

# x t

# u r

# e

## -

##

# L a c k

# o f

#

# C

# o h e si

# o n

# o f

#

# T e s t

#

# M

# e t

# h o d

# D

# A

# R

# T

# S

# 0

# 3

# 3

# 1 1

# 8

# 1 9

# t

# s D

# e t

# e c t

# -

#

# A

# s s e r

# t

# i

# o n

# R

# o u l

# e t

# t

# e

# -

#

# C

# o n d i

# t

# i

# o n a l

#

# T e s t

#

# L o g i

# c

# -

#

# C

# o n s t

# r

# u c t

# o r

#

# I

# n i

# t

# i

# a l

# i

# z a t

# i

# o n

# -

#

# D

# e f

# a u l

# t

#

# T e s t

# -

#

# D

# u p l

# i

# c a t

# e

# A

# s s e r

# t

# -

#

# E

# a g e r

#

# T e s t

# -

#

# E

# m

# p t

# y

# T e s t

# -

#

# E

# x c e pt

# i

# o n

# H

# a n d l

# i

# n g

# -

#

# G

# e n e r

# a l

#

# F i

# x t

# u r

# e

# -

#

# I

# g n o r

# e d

# T e s t

# -

#

# L a z y

# T e s t

# -

#

# M

# a g i

# c

# N

# u m

# b e r

#

# T e s t

# -

#

# M

# y s t

# e r

# y

# G

# u e s t

# -

#

# R

# e d u ndant

#

# A

# s s e r

# t

# i

# o n

# -

#

# R

# e d u ndant

#

# P

# r

# i

# n t

# -

#

# R

# e s o ur

# c e

# O

# p t

# i

# m

# i

# s m

# -

#

# S

# e n s i

# t

# i

# v e

# E

# q u a l

# i

# t

# y

# -

#

# S

# l

# e e p y

# T e s t

# -

#

# U

# n k n ow

# n

# T e s t

# 0

# 2

# 0

# -

#

# A

# s s e r

# t

# i

# o n

# R

# o u l

# e t

# t

# e

# -

#

# D

# u p l

# i

# c a t

# e

# A

# s s e r

# t

# R

# A

# I

# D

# E

# 0

# 3

# 3

# 0

# 2 1

# 2 1

# J N

# o

# s e

# T e s t

# -

#

# A

# s s e r

# t

# i

# o n

# R

# o u l

# e t

# t

# e

# -

#

# C

# o n d i

# t

# i

# o n a l

#

# T e s t

#

# L o g i

# c

# -

#

# C

# o n s t

# r

# u c t

# o r

#

# I

# n i

# t

# i

# a l

# i

# z a t

# i

# o n

# -

#

# D

# e p e ndent

#

# T e s t

# -

#

# D

# e f

# a u l

# t

#

# T e s t

# -

#

# D

# u p l

# i

# c a t

# e

# A

# s s e r

# t

# -

#

# E

# a g e r

#

# T e s t

# -

#

# E

# m

# p t

# y

# T e s t

# -

#

# E

# x c e pt

# i

# o n

# C

# a t

# c h i

# n g

# T h r

# o w

# -

#

# G

# e n e r

# a l

#

# F i

# x t

# u r

# e

# -

#

# I

# g n o r

# e d

# T e s t

# -

#

# L a z y

# T e s t

# -

#

# M

# a g i

# c

# N

# u m

# b e r

#

# T e s t

# -

#

# M

# y s t

# e r

# y

# G

# u e s t

# -

#

# R

# e d u ndant

#

# P

# r

# i

# n t

# -

#

# R

# e d u ndant

#

# A

# s s e r

# t

# i

# o n

# -

#

# R

# e s o ur

# c e

# O

# p t

# i

# m

# i

# s m

# -

#

# S

# e n s i

# t

# i

# v e

# E

# q u a l

# i

# t

# y

# -

#

# S

# l

# e e p y

# T e s t

# -

#

# U

# n k n ow

# n

# T e s t

# -

#

# V e r

# b o s e

# T e s t

# -

#

## R

## o t

## t

## e n

## G

## r

## e e n

## T e s t

# R

# T

# j

# 0

# 1

# 1

# i

# n g


---

<!-- Página 6 -->

EASE

### Table 3:

**No.****Test** **01****Abnormal** **02****Anonymous** **03****Assertion** **04****Assertionless** **05****Assertionless** **06****Brittle** **07****Comments** **08****Conditional** **09****Constructor** **10****Control** **11****Dead** **12****Default** **13****Dependent** **14****Duplicate** **15****Duplicated** **16****Eager** **17****Early** **18****Empty** **19****Empty** **20****Empty** **21****Empty** **22****Exception** **23****For** **24****General** **25****Guarded** **26****Ignored** **27****Indented** **28****Indirect** **29****Lack** **30****Lazy** **31****Likely** **32****Long** **33****Magic** **34****Max** **35****Mixed** **36****Mystery** **37****Obscure** **38****Overcommented** **39****Overreferencing** **40****Proper** **41****Redundant** **42****Redundant** **43****Resource** **44****Returning** **45****Rotten** **46****Sensitive** **47****Sleepy** **48****Teardown** **49****Test** **50****Test** **51****Test** **52****Test** **53****Test** **54****Test-Class** **55****Test-Method** **56****Transcripting** **57****TTCN-3** **58****Unclassified** **59****Under-the-carpet** **60****Under-the-carpet****Assertion** **61****Unknown** **62****Unused** **63****Unused** **64****Unusual** **65****Vague** **66****Verbose**

W.

### Definition of the test smells detected by the tools in our dataset.

**Abbreviation** **AUU** **AT** **AR** **AL** **ALT** **BA** **COT** **CTL** **CI** **ConL** **DF** **DT** **DepT** **DA** **DC** **ET** **ERT** **EMC** **ESF** **EmT** **ETMC** **EH** **FTO** **GF** **GT** **IgT** **InT** **IT** **LCM** **LT** **LIOC** **LoT** **MNT** **MIV** **MS** **MG** **OISS** **OCT** **OF** **PO** **RA** **RP** **RO** **RA** **RT** **SE** **ST** **TOT** **TCD** **TM** **TP** **TR** **TRW** **TCN** **TMC** **TT** **TTCN** **UMC** **UCA** **UCFA** **UT** **UI** **USFV** **UTO** **VHS** **VT**

**Definition****Ref.** Overriding[59] A[59] A[22] A[27] A[59] A[42] A[59] A[56] A[56] A[59] When[39] [56] A[72] Occurs[56] A[27] A[22] A[59] A[59] A[59] A[56] A[59] Occurs[56] A[22] ThissetUp()fixture[22] AifTrue:aCodeorifFalse:aCode.[59] A[56] A[27] A[22] When[39] Occurs[22] A[59] A[59] A[56] A[59] Violates[59] A[22] A[39] A[59] A[59] Bad[59] A[56] A[56] A[22] A[59] Occurs[31] OccurstoStringmethod.[22] Occurs[56] Exists[59] Occurs[22] Exists[39] Test[41] Occurs[44] A[22] A[59] A[59] A[59] Collection[20] A[59] A[59] A[59] A[56] Inputs[42] Occurs[59] A[59] A[39] Test[27]

### 175


---

<!-- Página 7 -->

Test Test

Table 4: Distribution of test smells detected by the test smell detection tools. Test**Table 4: Distribution of test smells detected by the test smell detection tools.** ToolALARCICTLDADCDepTDFDTEHEmTETFTOGFIgTInTITLCMLTMGMNTOISSRARORPRTSESTTMTRTRWUTVHSVT pppTable 4: Distribution of test smells detected by the test smell detection tools.DARTS[46] p DrTest[31] p DTDetector [75] p ElectricTest[24] ppppppppppppppppppppp JNose[72] p PraDeT[34] pp RAIDE[60] p RTj [47] pppppp SoCRATES[30] ppp Taste[52] p TeCReVis[44] p TEDD[25] p TeReDetect[45] pppppp TestEvoHound[40] pppppp TestHound[39] pppppppppppp TestQ[27] ppppppppppppppppppp tsDetect[56] pppppppppp Unnamed[22] Total2622325222372911244522222252221222 3.1.4 SupportedProgramming Languages(2)Test Framework- These frameworks provide an Next, we look at the programming languages supported by theenvironmentfor developers to write unit tests. As part of the detec-3.1.4**Supported Programming Languages**.detection strategy the tool may be depended on the presence of on the meaningsof smells,there is no consensuson identifying3.2 RQ: What are the main characteristics of2various smelltypesweidentifyinthisstudy. FromTabletion5,westrategy the tool may be depended on the presence of specicNext, we look at the programming languages supported by thespecific framework API’s in the test code. them. Therefore,it is evidentto see varioustools containingdif-test smell detection tools?observe that thetypes support four programming languages,framework API's in the test code.various smellweidentifyinthisstudy. FromTable 5,we(3)**Correctness**- Providesinsightintohowaccuratelythetool ferent detectionstrategiesfor similarsmell types.Hence, in thisspecically Java, Scala, Smalltalk,and C++. From this set,(3)JavaCorrectnessis- Providesinsightinto how accuratelythe toolThis RQ comprises of two parts that examine the common charac-observe that the smell types support four programming languages,can detect smells. We look for instances where the tool authors analysis,we look at the overlap of detected smell types by the toolsthe mostpopularprogramminglanguagefor testsmellsupport,can detectsmells.We lookfor instanceswherethe toolauthorsteristicsof testdetection tool. The rst part examines specicspecifically Java, Scala, Smalltalk, and C++. From this set, Java isprovide values for precision and recall or F-measure. in our dataset.The smells,detectedby TestLinttools, Oracle-supporting39 smell types, followed by Smalltalk (28types).provideInvalues for precision and recall or F-measure.high-levelfeatures of such tools, while the second part looks at thethe mostpopularprogramminglanguagefor testsupport,(4)**Detection Technique - Strategy the tool utilizes to analyze test** Polish, TRex, andPolDetare uniqueto therespectivetool.TheTable5, we also list the publications (tool and tool adoption)(4)in ourTechnique- Strategythe tool utilizesto analyzetypesof the presencedetectiontechniques implemented by the tools.supporting39 smell types, followed by Smalltalk (28types). Incodeof smells. remaining16 tools share the detection of some overlapping smells.datasetthat analyze these smell types. From this, we observetestthatcodeafor the presence of smells.Table5, we also list the publications (tool and tool adoption) in our(5)**Interface - Indicates how developers interact with the tool.** In Table 4, we identify the overlapping of smells across 16 tools.(5) Interface- Indicates how developers interact with the tool.subsetof the Java-supported test smells also support Scala unittest**Usages Guide Availability**datasetthat analyze these smell types. From this, we observe that a-if documentation on how3.2.1Common Characteristics.For each tool, we indicate if the tool detects a specic smell by the(6)code. Although the developed XUnit guidelines can be appliedtoUsages Guide Availability- Indicatesif documentationonsubset of the Java-supported test smells also support Scala unit testto usethetoolis available(eitherin thetool’spublicationorWhile the number and types of test smells detected by the toolssymbol.From this table, we observe that the three most commonvarious languages48[including dynamically typed ones such ashow to use the tool is available (either in the tool's publication orcode. Although the developed XUnit guidelines can be applied towebsite).are essential in selecting an appropriate tool, there are other featuressmell types areGeneral Fixture, Eager Test, andAssertion Roulette,JavaScript and Python,we did not locate tools that analyzeswebsite).testvarious languages [], including dynamically typed ones such as(7)**Adoption in Research Studies**- This provides insight into thethat can be considered to make a more informed decision. Similarwhich are respectively detected by 9, 7, and 6 tools.suites writtenin theselanguages,whichrepresentsa noticeable(7) Adoption in ResearchStudies- This provides insightintoJavaScript and Python, we did not locate tools that analyzestestpopularity of the tool in the research community.to prior literature32, 36[], we review our set of test smell detection limitation in terms of supporting the high quality of test suites.popularity of the tool in the research community.(8)**Tool**Website - Supplementarysuites writtenin these languages,whichrepresentsa noticeabledocumentationabout the tool,tools with respect to the following characteristics: Website- Supplementary documentation about the tool,(8) Toollimitation in terms of supporting the high quality of test suites.such as(whereavailable)itssourcecoderepository,installa- such as (where available) its source code repository, installation/ex-3.1.4Supported Programming Languages.tion/execution instructions, etc.(1) Programming Language- This feature comprises of the pro- ecution instructions, etc.Whiletherehas been a steady releaseof testNext, we lookatthe programmingsupportedby smellthelanguagethat the eachtoolis In case we cannotwith locatetheTable6 detailour findingstool. detectiontoolsovertheyears,hasbeen anuptickin 5,varioussmelltypesweidentifyinthisstudy.FromTableweprogramminglanguage(s)the it as supports.theneeded information,we labelin the table. Table6 detail our ndings for each tool. In case we cannot locatetool developmentandadoptionrecently,specicallyin 2019observethe smelltypessupportfour programminglanguages,(2) It is evidentTestFramework-frameworksanfromTable 6 thatthe majorityof test smell detection the needed information, we label it as `UNK' in the table.and 2020. Java, most ofthe tools detecttestsmellsoccurringspecicallySmalltalk,and C++.Fromthisset, Java isenvironment for developersto writeunittests.As partof thetools (≈ 86%) focuson detectingtest smellsexclusivelyfor Java- It is evident from Table 6 that the majority of test smell detectioninJavatest suites,there isa lack of supportfor otherthemostpopularprogramminglanguagetestsupport,detection strategy the tool may be depended on the presence ofbased systems and are mostly focused on identifying any deviation tools (86%) focuson detectingtest smellsexclusivelyfor Java-languages, such as JavaScript and Python.supporting39 smell types, followed by Smalltalk (28types). Inspecic framework API's in the test code.from the guidelines of JUnit testing framework. This further cor- based systems and are mostly focused on identifying any deviationTable5, we also list the publications (tool and tool adoption) in our(3) Correctness- Providesinsightintohowaccuratelythetoolroboratesour prior RQ finding where we show that most test smell from the guidelinesof JUnit testing framework.This further cor-datasetthat analyze these smell types. From this, we observe that acan detect smells. We look for instances where the tool authorstypes are geared towards Java systems, and thereby most research**3.2 RQ****: What are the main characteristics of**2roboratesour prior RQ nding where we show that most test smellsubsetof the Java-supported test smells also support Scala unit testprovide values for precision and recall or F-measure.around test smells focuses on datasets composed of Java systems.3.2RQ: Whatarethemaincharacteristicsoftestsmell2types are geared towards Java systems, and thereby most research**test smell detection tools?**code. Although the developed XUnit guidelines can be applied to(4) DetectionTechnique- Strategy the tool utilizes to analyze testAdditionally,there are three tools, namely TestQ, TestHound, anddetection tools?around test smells focuses on datasets composed of Java systems.various languages48[including dynamically typed ones such asThis RQ comprises of two parts that examine the common charac-code for the presence of smells.TestEvoHound,which support two or more testing frameworks. In Additionally,there are three tools, namely TestQ, TestHound, andJavaScript and Python,we did not locate tools that analyzestestThis RQ comprises of two parts that examine the common charac-teristicsof test smell detection tool. The first part examines specific(5) Interface- Indicates how developers interact with theterms of correctness, most tools do not publish details around their TestEvoHound, whichsupporttwo or more testingframeworks.suites writtenin theselanguages,representsa noticeableteristicsof test smell detection tool. The rst part examines specichigh-levelfeatures of such tools, while the second part looks at the(6) UsagesGuide Availability- Indicates if documentation on howaccuracy.Additionally, the majority of tools do not report on perfor- In terms of correctness,most tools do not publish details aroundlimitation inof supporting the high quality of test suites.high-levelfeatures of such tools, while the second part looks at thetypes of smell detection techniques implemented by the tools.to usethetoolisavailable(eitherinthetool'spublicationmance speeds and execution times. Our findings show that only six their accuracy. Additionally, the majority of tools do not report ontypes of smell detection techniques implemented by the tools.website).tools published their detection accuracy, in terms of precision, recall3.2.1**Common Characteristics.**While the numberand typesperformance speeds and execution times. Our ndings show that(7) Adoptionin Research Studies- This provides insight into theor F-measure.From this set, only DARTS,Taste, andtsDetectof testsmellsdetectedbythetoolsareessentialinselectinganonly six tools published their detection accuracy, in terms of preci-3.2.1 CommonCharacteristicspopularity of the tool in the research community.report values for each smell type it supports; hence the correctnessappropriatetool, there are other features that can be considered torecall or F-measure. From this set, onlyTasteDARTS,, andWhile the number and types of test smells detected by the tools(8) Tool Website- Supplementarydocumentationabout the tool,score is reported as a range. From our set of 22 detection tools, onlymake a more informed decision. Similar to prior literature32 , [ ],tsDetectreport values for each smell type it supports; hence theare essential in selecting an appropriate tool, there are otherfeaturessuch as(whereavailable)itssourcecoderepository,installa-five tools provide refactoring support. TestHound provides textualwe review our set of test smell detection tools with respect to thecorrectness score is reported as a range. From our set of 22 detec-that can be considered to make a more informed decision. Similartion/executioninstructions,etc.informationon smellscorrection.WhileRAIDE provides a semi-following characteristics:tion tools, only ve tools provide refactoring support. TestHoundto prior literature32, 36[], we review our set of test smell detectionToolALARCI CTLDADCDepT DFDTEHEmT ETFTOGFIgTInTITLCMLTMGMNTOISSRARORPRTSE STTMTRTRWUTVHS VTpp(1)**Programming Language - This feature**comprisesof theppro-automatedcorrection, RTj, DARTS and TRex provide theDARTS[46]provides textual informationon smells correction.While RAIDEtools with respect to the following characteristics:DrTest[31]Table6 of their ourndingsfor each tool.In of thesewe cannot locategramming language that the tool is implementedwith and therefactoringdetectedsmells.nonepDTDetector[75]provides a semi-automated correction, RTj, DARTS and TRex pro-pneededinformation,we label it ofas`UNK'in the table.ElectricTest[24]programming language(s) the tool supports.providedetailsconcerning thetheirrefactoringcapa-pppppppppppppppppppppJNose[72](1) Programming Language- This feature comprises of the pro-vide the automated refactoring of their detected smells. However,p(2)**Supported Test Framework - These**frameworksprovideanbilities. From detection standpoint, we observe that tools, focusingPraDeT[34]ppgramming languagethatthetoolisimplementedwithandthenone of these tools provide details concerning the accuracy of theirRAIDE[60]penvironment for developersto writeunit tests.As part of theon test dependencyand rottengreentest smells,use a dynamicRTj[47]ppppppprogramminglanguage(s) the tool supports.refactoringcapabilities.From detection standpoint, we observe thatSoCRATES[30]pppTaste[52]pTeCReVis[44]pTEDD[25]pTeReDetect[45]ppppppTestEvoHound[40]176ppppppTestHound[39]ppppppppppppTestQ[27]ppppppppppppppppppptsDetect[56]ppppppppppUnnamed[22] Total2622325222372911244522222252221222

or


---

<!-- Página 8 -->

### EASE

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### EASE

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

## Table 5: Distribution of Test Smells Per Programming Languages.

## Table 5: Distribution of Test Smells Per Programming Languages.

ProgrammingSupportedLiterature (01)[20,**Programming****Supported****Literature** (02)[22,(01)[20, (03)(02)[22, (04)[34,(03)[23, Java(05)[25,(04)[34, (06)[46,**Java**(05)[25, (07)[26,(06)[46, (08)[33,(07)[26, (09)[45,(08)[33, (10)(09)[45, Scala(01)(03)(05)[29,(10) (02)(04)(06)**Scala**(01)(03)(05)[29, (01)(02)(04)(06) (02)(01) (03)(02) (04)(03) SmallTalk(05)[31,(04) (06)**SmallTalk**(05)[31, (07)(06) (01)(04)(07)(10)(07) C++(02)(05)(08)(11)[27](01)(04)(07)(10) (03)(06)(09)(12)**C++**(02)(05)(08)(11)[27] (03)(06)(09)(12)

## Table 6: Characteristics of test smell detection tools.

## Table 6: Characteristics of test smell detection tools.

### Programming

### Supported

### Detection

### Usage

### Adoption

### Tool

### Tool

### Correctness

### Interface

### Implemented

### Analyzed

### Test

### Technique

### Guide

### Studies

### Website

### F-Measure:

### DARTS

### [46]

###

###

### Information

###

###

###

###

###

### Rule

r

### DrTest[31]

### Smalltalk

### Pharo

### SUnit

### UNK

###

### Yes

### 

### [4]

### Dynamic

¢ 

### DTDetector

### [75]

###

###

###

###

###

###

###

###

###

### ElectricTest

### [24]

### Java

### Java

### JUnit

### UNK

### Dynamic

### Command-line

### No

### 

### UNK

### JNose

### [70]

###

###

###

###

###

###

###

###

###

###

###

¢

### OraclePolish

### [42]Java

### Java

### JUnit

### UNK

### Dynamic

### Command-line

### Yes

### 

### [7]

### PolDet

### [41]

###

###

###

###

###

###

###

###

###

### PraDeT

### [34]

### Java

### Java

### JUnit

### UNK

### Dynamic

### Command-line

### Yes

### 

### [8]

### RAIDE

### [60]

###

###

###

###

###

###

###

###

###

### Rule

### RTj

### [47]

### Java

### Java

### JUnit

### UNK

### Command-line

### Yes

### 

### [11]

### Dynamic

### Precision:

### SoCRATES

### [30]

###

###

### Rule

###

###

###

###

### Recall:

### Precision:

### Taste

### [52]

### UNK

### Java

### JUnit

### Information

### UNK

### No

### [54]

### UNK

### Recall:

### Metrics

¢

### TeCReVis

### [44]

###

###

###

### Eclipse

### Yes

###

### Dynamic

### Precision:

### TEDD

### [25]

### Java

### Java

### JUnit

### Information

### Command-line

### Yes

### [26]

### [13]

### Recall:

### Metrics

¢

### TeReDetect

### [45]

###

###

###

### Eclipse

### Yes

###

### Dynamic

### TestEvoHound

### [40]Java

### Java

### JUnit,

### UNK

### Metrics

### UNK

### No

### 

### UNK

¢

### TestHound

### [39]

###

###

###

###

###

###

###

###

###

###

### Rule

¢

### TestLint

### [59]

### Smalltalk

### Sunit

### UNK

### UNK

### Yes

### 

### [16]

### Dynamic

### CppUnit,

¢

### TestQ

### [27]

###

###

### UNK

###

###

###

###

###

### Qtest

 ¢

### TRex

### [20]

### Java

### Java

### TTCN-3

### UNK

### Rule

### Eclipse

### Yes

### [49,

###

###

### [18]

### [43,

###

###

### Precision:

### [19]

### Rule

###

### tsDetect

### [56]

###

###

### [33,

###

###

### Recall:

### Precision:

### [23,

###

###

### Unnamed

### [22]

### UNK

### Java

### JUnit

### Rule

### Command-line

### No

### UNK

### Recall:

### [37,

###

###

###

###

### Provides

###

###

### 

### Embedded

###

###

###

###

###

###

###

###

###

###

###

### ¢

### Included

###

###

###

###

###

###

###

###

###

###

###  Also

###

###

###

###

###

###

###

###

### r

### Pharo

###

###

###

###

###

## detection strategy, while most static analysis-based

## smells prefer

## contacted the publication’s

## corresponding

## author. From these 22

## It is evident from Table 6 that the majority of test smell detection

## which

## support

## two or more testing

## frameworks.

## to utilize a rules-based approach. We discuss in detail the different

## publications,

## we were able to only locate 17 tools. It should be noted

## tools (86%) focus

## on detecting

## test smells

## exclusively

## for In

## Java-

## terms of correctness,

## most

## do not publish details around

## techniques later on. In

## of adoption in research studies, only

## that, except for TestLint, the website for these 17

## points to the

## based systems and are mostly focused on identifying any deviation

## their accuracy. Additionally, the majority of tools do not report on

## seven

## of the

## have been utilized by the research community totool’s source code repository. Further, when examining the project

## from the guidelines

## of JUnit testing framework.

## This further

## performance

## cor-

## speeds and execution times. Our ndings show that

## study test smells.

## repositories,

## we observe that

## tsDetectwas the most forked reposi-

## roborates

## our prior RQ nding where we show that most test smell

## only six tools published their detection accuracy, in terms of preci-

## Next, in

## of how developers run/interact with these tools,

## tory (21 forks). Furthermore, an examination of a tool’s publications,

## types are geared towards Java systems, and thereby most research

## sion, recall or F-measure. From this set, only

## Taste

## DARTS,

## , and

## there are

## two

## categories–

## graphical

## user

## interface

## (GUI)

## and

## website,

## and the README file in the source code repository (where

## around test smells focuses on datasets composed of Java systems.

## tsDetect

## report values for each smell type it supports; hence the

## command-line (i.e., non-GUI)

## tools. Most of the GUI tools are in

## available)

## yields only 16

## presenting guidelines on how to setup

## Additionally,

## there are three tools, namely TestQ, TestHound, and

## the form of IDE plugins or web and desktop applications. In termsand/or execute the tool. Finally, from this set, only

## tsDetectand

## of tool availability, we searched

## for a link to the tool website

## or the tool by Bavota

## et al.

## 22

## [ show a high adoption

## rate, having

## binaries. In

## case

## the

## link

## is

## absent

## or

## no

## longer

## functional,

## we been used in at least eight other studies. The majority of the tools

## are only limited to the studies to which they were first introduced.

## 177


---

<!-- Página 9 -->

Test

Test 3.2.2 SmellDetection Techniquesdenition for most smells are based on well-dened48,rules].[ Each toolrepresentsanimplementationofasmelldetectionThe metric-based mechanism is less frequently utilized due to: (1) 3.2.2**Smell Detection Techniques**.The metric-based mechanism is less frequently utilized due to: (1) strategy. Each detection strategy reects an interpretationnotof all known metrics proposed27by, 39[, 68, 69] have the ability Each toolrepresentsanimplementationofasmelldetectionnot all known metrics proposed by27[ 39 ,68,69] have the ability the smelltypemanifestsinthesourcecode,i.e.,howthetodetect all test smells, since they can go beyond traditional design strategy. Each detection strategy reflects an interpretation of howto detect all test smells, since they can go beyond traditional design symptoms can be identied. Our analysis shows that, while mostanomalies, and (2) the reliance on determining an appropriate set the smelltypemanifestsinthesourcecode,i.e.,howtheanomalies, and (2) the reliance on determining an appropriate set of thetoolsinourstudyrelyonstaticanalysisofsourceof thresholdscode,is considered to be a signicant challenge. Looking at symptoms can be identified. Our analysis shows that, while mostof thresholds is considered to be a significant challenge. Looking at some tools identify smells through dynamic analysis. These detec-that utilize a dynamic-based detection technique, we observe of thetoolsinourstudyrelyonstaticanalysisofsourcecode,that utilize a dynamic-based detection technique, we observe tion strategies can be grouped into four categories, namely Metrics,that mosttestdependencyand rottengreentestdetectiontools some tools identify smells through dynamic analysis. These detec-that mosttest dependencyand rottengreentest detection Rules/Heuristic,Information Retrieval, and Dynamic Tainting.utilizeWiththistechnique.Finally,TasteDARTS,, andTEDD tion strategies can be grouped into four categories, namely Metrics,utilize thistechnique.Finally, DARTS,Taste, andTEDD this clustering of strategies, we aim to familiarize future smellInformationdetec- Retrieval techniques. However, as these tools rely on Rules/Heuristic,Information Retrieval, and Dynamic Tainting. WithRetrieval techniques. However, as these tools rely on tion tool researchers/developers with smell detection techniques.source code feature extraction, the lack of such information could this clustering of strategies, we aim to familiarize future smell detec-source code feature extraction, the lack of such information could Metrics.The use of metrics to prole smells, is one of theaectearlythe detection accuracy [52]. tion tool researchers/developers with smell detection techniques.affect theaccuracy [52]. techniques, and popularones, for all code smells in general.In a **Metrics. The use of metrics to profile smells, is one of the early** nutshell, the smell symptoms are measured through their impactSummary. JUnit is the most popular testing framework sup-techniques, andones, for all code smells in general. In a on structural and semantic measurements,where their values goported by test smell detection tools, with most static analysisnutshell, thesymptoms are measured through their impact beyondpre-dened threshold. These metrics, and their correspond-based tools opting to utilize a rules-based detection strategyon structural and semantic measurements,where their values go ing threshold values, are combined into a rules-based tree to maketo identify smells. Even though most of the tools publish theirbeyondpre-defined threshold. These metrics, andcorrespond- a binary decision, of whether the code under analysis suers fromsource code, information about the tool's accuracy is seldoming threshold values, are combined into a rules-based tree to make a smell or not. In a typical metrics-baseddetection approach,available.Our analysis only shows that only six tools publisha binary decision, of whether the code undersuffers from the sourcecodeis parsedand convertedintoan abstractsyntaxtheir scores related to correctness.a smell or not. In a typical metrics-baseddetection approach, tree (AST). This AST is then subjected to a metrics-based analysis the sourcecodeis parsedand convertedinto an abstractsyntax to identify and capture the test smells. For instance, Van Rompaey tree (AST). This AST is then subjected to a metrics-based analysis4 Discussionet al. [69], utilize metrics such as Number of Object Used in setup,**4 DISCUSSION**to identify and capture the test smells. For instance, Van Rompaey Number of Production-Type,of Fixture Objects,As a systematic mapping study, our ndings provide a high-level et al. [69], utilize metrics such as Number of Object Used in setup,As a systematic mapping study, our findings provide a high-level Of Fixture Production Types, and AverageUsage to detectunderstanding ofthecurrentstateoftestsmelldetectiontools. Number of Production-Type,of Fixture Objects,understanding ofthecurrentstateoftestsmelldetectiontools. smells such asGeneral Fixtureand Eager Test. The threshold usedIn brief,as seenfromour RQ ndings,the researchcommunity Of Fixture Production Types, and AverageUsage to detectIn brief,as seenfromour RQ findings,the researchcommunity are chosen by the user or empirically derived from a representativehas producedmanytestsmelldetectiontoolsthatsupportthe smells such asGeneral Fixture and Eager Test. The threshold usedhas producedmanytestsmelldetectiontoolsthatsupportthe set.detectionof various test smell types. These tools, in turn, have been are chosen by the user or empirically derived from a representative detectionof various test smell types. These tools, in turn, have been Rules/Heuristic.Rules or heuristics smell detection augmentsutilized in studies on test smells to understand how they inuence set.utilized in studies on test smells to understand how they influence the metrics-basedtechniqueswith patternsthat can be foundsoftwareindevelopment.However, ourndingsalsodemonstrate **Rules/Heuristic. Rules or heuristics smell detection augments**software development.However, ourfindingsalsodemonstrate the source code. The smell is detectedwhen the input matchesareasa of concern and expansion in this eld. In this section, through the metrics-basedtechniqueswith patternsthat can be found inareas of concern and expansion in this field. In this section, through pre-dened setofmetricthresholdswiththeexistenceof asomeseries of takeaways, we discuss how our ndings can support the the source code. The smell is detectedwhen the input matches aa series of takeaways, we discuss how our findings can support the code patterns. For example,AssertiontheRoulettesmell is detectedresearch and developercommunityin selectingthe right tool as pre-defined setof metricthresholdswiththeexistenceof someresearch and developercommunityin selectingthe right tool as by dening a heuristic that checks whether a test method containswell as provide future directions for implementing and maintaining code patterns. For example, theAssertionRoulette smell is detectedwell as provide future directions for implementing and maintaining several assertion statements without an explanation messagefutureas atest smell tools. by defining a heuristic that checks whether a test method containsfuture test smell tools. parameter for each assertion method.Takeaway1: Standardization of smell names and denitions. several assertion statements without an explanation message as a**Takeaway 1: Standardization of smell names and definitions.** Information Retrieval.In this technique,the main steps in-From RQ, we observean overlap of the smell types detectedby1parameter for each assertion method.From RQ, we observean overlap of the smell types detectedby1clude extracting information/contentfrom the test code andthenor-tools. For instance,Assertion Rouletteis detectedby six JUnit **Information Retrieval.**In this technique,the mainstepsin-the tools. For instance,Assertion Rouletteis detectedby six JUnit malizing it. As part of the extractionprocess, the textualsupportedcontent tools. However, the implementation of the detection rules clude extracting information/contentfrom the test code and nor-supportedtools. However, the implementation of the detection rules from each JUnit test class (e.g., source code identierandmayvary between these tools. Additionally, there can be instances malizing it. As part of the extraction process, the textual contentmay vary between these tools. Additionally, there can be instances comments) are taken as the necessary features for identifyingwherethesome test smell types with the same/similar denitions are from each JUnit test class (e.g., source code identifier andwhere some test smell types with the same/similar definitions are knownby dierent names. This fragmentation of smell denitionstest smells. These characteristics are normalized via multipletext comments) are taken as the necessary features for identifying theknown by different names. This fragmentation of smell definitions is notuniqueto testsmells;Sobrinho28etexperienceal.[thispre-processingsteps. These steps include stemming, decomposing test smells. These characteristics are normalized via multiple textis notuniqueto testsmells;Sobrinhoet al.] experiencethis in codesmells.Thisphenomenonprovidestheopportunityforidentier names, stop word, and programming keyword removal. pre-processing steps. These steps include stemming, decomposingin codesmells.Thisphenomenonprovidestheopportunityfor future researchin thisareato compareandcontrastsuchsmellThe normalizedtext is then weighted using Term Frequency and identifier names, stop word, and programming keyword removal.future researchin thisareato compareandcontrastsuchsmell types. The agreementon smells denitions,does not necessarilyInverse Document Frequency. The end-result is applying machine The normalized text is then weighted using Term Frequency andtypes. The agreementon smells definitions,does not necessarily induce similar interpretations. Since there is no consensus on howlearningalgorithms to extract textual features that can discriminate Inverse Document Frequency. The end-result is applying machineinduce similar interpretations. Since there is no consensus on how to measure smells, eachtype can be identied using dierentbetween classes, i.e., smell types. learningalgorithms to extract textual features that can discriminateto measure smells, each smell type can be identified using different detectionstrategies, and the choice of the strategy becomes part ofDynamic Tainting.It monitorsthe source-codewhile it exe- between classes, i.e., smell types.detectionstrategies, and the choice of the strategy becomes part of thedeveloper's preferences.cutes.Dynamic tainting enables the analysis of the actual datafrom **Dynamic Tainting. It monitors**the source-codewhile it exe-the developer’s preferences. 2:Improvesupportfornon-Javaprogrammingthe codebasedonrun-timeinformation.Inparticular,it Takeawayworks cutes. Dynamic tainting enables the analysis of the actual data from Takeaway 2:Improvesupportfornon-Javaprogramming and testingframeworks.While our ndingsfromin two steps: (1) run the source-codealong with predenedlanguagestaint the codebasedonrun-timeinformation.Inparticular,itworks**languages and**testingframeworks.While ourfindingsfrom RQvalue/mark (i.e., user input), and (2) reason which executionsare the existence of multiple test smell detection tools, our1in two steps: (1) run the source-codealong with predefinedtaintRQshow the existence of multiple test smell detection tools, our1aected by that value/mark.RQndings show that most of these tools are limited to support-2value/mark (i.e., user input), and (2) reason which executions areRQfindings show that most of these tools are limited to support-2ingsystems that utilize the JUnit testing framework, therebyOur categorization of the tools, in our study, based on thefour affected by that value/mark.ing Java systems that utilize the JUnit testing framework, thereby narrowingtestresearch to Java systems. Hence, restricting re-smell detection techniques are shown in Table 6. The Rule/Heuristic- Our categorization of the tools, in our study, based on the fournarrowingtest smell research to Java systems. Hence, restricting re- based technique is a frequently adopted detectionas the to a single environment/language will not accurately reect smell detection techniques are shown in Table 6. The Rule/Heuristic- searchto a single environment/language will not accurately reflect based technique is a frequently adopted detectionas thereality.While it can be argued that as most test smells areon definition for most smells are based on well-defined rules48 , [ ].xUnit guidelines [] research findings on Java systems can carry

178


---

<!-- Página 10 -->

EASE

### over to other similar

### languages

### (e.g., C#), actual

### practitioners

### of

### reviewed

### scientific publications. As part of our analysis, we identify

### non-Java systems

### gain

### no

### benefit

### without

### a tool

### to

### use

### in

### their the smell

### types

### detected

### by

### these

### tools

### and

### highlight

### the

###

### development workflow. Furthermore, recent trends have shown a

### types that

### overlap.

### Additional

### comparisons

### between

### these

### tools

### rise in the popularity of dynamically typed programming languages

### show that most of these tools support

### the JUnit framework,

### and

### (e.g., Python

### and JavaScript) 9

### [ giving

### more urgency

### for the re-

### while the source code is made available, details around the tool’s

### search community to construct tools that support non-traditional

### detection

### correctness are not always made public. We envision our

### research languages.

### findings act as a one-stop source for test smell detection tools and

### Takeaway 3:

### Do

### not

### reinvent

### the

### wheel.

### Re-

### empower

### researchers/practitioners in selecting the appropriate tool

### searchers/practitioners need

### to

### evaluate

### if

### implementing

### for their requirements. Future work in this area includes a hands-on

### another detection

### tool

### is necessary

### for their

### specific

### needs

### or if

### evaluation

### of each tool to determine the extent to which tools detect

### modifying an existing

### tool

### would

### suffice.

### Reusing

###

### tools

### common smell types and create a benchmark for such

### types.

### will not

### only

### save

### effort,

### but

### also

### develops

### more

### mature

### and

## REFERENCES

### robust frameworks.

### For

### instance,

### Spadini

### et

### al.

### 61

### [ integrate

[1] [2]

### tsDetect

### into a code quality monitoring

### system,

### while the tool

[3]

### implemented by Tufano et al.

### 66

### [

### ], HistoryMiner, utilizes the tool

[4] [5]

### of Bavota et al.22

### [ ] to detect test smells in the lifetime of a project.

[6]

### Additionally, some of the tools in our dataset are based on other

[7]

### tools in the dataset. For instance, JNose Test and RAID are built on [8]

[9]

### top of

### tsDetect

### and DARTS is based

### on

### Taste. It is important

[10]

### that, when introducing new tools, tool maintainers should design

[11] [12]

### their tools

### to

### be

### ready

### for

### customization.

### For

### instance,

### Spadini

[13][n.d.].

### et al.

### [ 64 ] customize

### tsDetect

### by introducing

### thresholds

### to

TEDD.

### meet their research objective. This can help reduce the release of

[14] [15]

### near-duplicate tools.

### It also

### further

### strengthens

### the case

### for the

[16]

### importance of public availability

### of a tool’s source code. Having

[17]

### access to the code enables the improvement of the tool’s quality. It[18]

[19]

### also facilitates extensions in improving current detection strategies

[20]Paul

### or introducing the detection of new smell types, which, in the long

Zeiss.

### run, improves the tool’s usefulness.

In Testing: (TAIC. IEEE,

### Takeaway 4: Improve transparency on the quality of tools.

[21]Balbir

### As reported in RQ

### , only a few tools report on the correctness of the

2eratureProceedings Innovations(Jaipur,(ISEC. Associa-

### tool. Furthermore, clarity around bias mitigation is not completely

tion

### addressed

### for the tools that do report correctness scores. While our

[22]Gabriele

### objective here is not to discredit the validity of the current set of

Binkley. their2012

### test smell detection

### tools, we only highlight

### inconsistencies

### that

on. IEEE,

### might lead to research studies obtaining varying results based on

[23]Gabriele

### the tool in use. As stated by Panichella et

### 53

### al.

### ], there is a need for

Binkley.Empirical Software20,

### a community-maintained

### gold-set/standard

### of smelly test files to

Jonathan[24]

### validate

### the current and future smell detection tools. We understand

dependencyProceedingsIn 10th. 770–781.

### that the process involved in the creation of a community-curated

[25]Matteo

### gold-set might

### be time-consuming.

### Hence,

### in the meantime,

### we

2019.Proceedings

### recommend that

### the peer-review

### process

### be

### adjusted,

### such

### that

Meeting Foundations. 154–164.

### providing metrics for precision

### and recall at the smell type level

[26]M.

### (instead

### of an overall tool accuracy score) along with the evaluation

Test2020

### dataset is made mandatory.

Validation. 175–185. [27]Manuel

### Takeaway 5: Expand from just detecting test smells to inter-

turalWASDeTT-1:

### active refactoring.

International. [28]E.

### Granted that the primary purpose of these tools is the detection

atureIEEE

### of test

### smells,

### developers

### will

### also

### immensely

### benefit

### from

### sug-

Transactions47,

### gested refactoring templates for each smell type. While there have

[29]Jonas and2019

### been initial efforts to include such functionality in detection tools,

Conference. IEEE,

### it does not generalize to the current popular detected smells, and

[30]Jonas

### more research is needed to elaborate on their ability to appropri-

radarProceedings Scala . 22–26.

### ately change the test files without introducing any regression.

[31]J. Tests.2019

## 5 CONCLUSION

## AND FUTURE

## WORK

(ICSE) . 500–511. [32]Eduardo

### This study identifies 22 test smell detection tools made available by

Figueiredo.

### the research community through a comprehensive search of peer-

In Proceedings

### 179


---

<!-- Página 11 -->

Test

in. 1–12.SmellsProceedings [33]G.Software Code2020Engineering (Virtual(ESEC/FSE. Association InternationalMachinery, (ICSTW) . 461–464.[57]Anthony [34]Alessioand dency2018FilesProceedings Verification. IEEE,Conference(Seoul,(IC- [35]V.SEW’20) . Association SoftwareIEEE36,[https://doi.org/10.1145/3387940.3392189](https://doi.org/10.1145/3387940.3392189) [36]Vahid[58]Abdallah knowledgeJournal(2018).Study [37]GiovanniIEEE7 [59]Gall.Stefan automaticallyJournal156ment6, [38]G.[60]Railana CaseIEEEHeitor Software(2019),DuplicateProceedings [39]Michaelaian(Natal,(SBES. Association detection2013InComputing [61]Conference. IEEE,Martin [40]MichaelaInvestigating 2013.2013progress.2019 10th. IEEE,Evolution,. [41]Alex[62]Elvys DetectingProceedingsInAlessandro 2015. 223–233.Smells: [42]ChenBrazilian(Natal, assertions(SAST. Association International. 621–631.[63]D. [43]D.2020the2018 IEEE/ACMConference. 1–12. Proceedings. 149–151.Davide[64] [44]Negarand ageInternationalProceedings Conference. Springer,(Seoul,(MSR. Association [45]NegarYork, forAdvances2010[65]Amjed [46]Stefanostudy2016 Palomba.Asia-Pacific. IEEE, Project.Proceedings[66]Michele hension . 441–445.Oliveto, [47]MatiastionProceedings 2020.Conference. 4–15. Cases.Proceedings[67]Arie Engineering:(Seoul,(ICSE. AssociationRefactoringProceedings forprogramming. 92–95. [48]GerardxUnit. Pearson[68]Bart tion.relative [49]HelmutSoftware. IEEE, Quality[69]Bart ing, Alexandrethe GrieskampeagerIEEE33, [50]Helmut[70]Tássio toInternationalHeitor Software4Proceedings. 564–569. [51]Fabio[71]Tássio DeHeitor An2016generatedProceedingsIn Software. IEEE,Brazilian. 92–96. [52][72]FabioTássio smellHeitor Conference. IEEE,TestProceedings [53]A.Engineering . 467–471. RevisitingEdith[73] Opportunities.2020and and. 523–533.niquesSDL, [54]FabianoEmmanuel VITRuM:ProceedingsBerlin, [74]of(Salerno,(AVIBenjamin ’20) . AssociationBaker.System Anthonyand, Reinhard[55] Mkaouer,Berlin inProceedingsIn[75]Sai ofErnst, Engineering (Toronto,(CASCON. IBMassumption.Proceedings [56]AnthonyTesting. 385–396. Mkaouer,

### 180


---

