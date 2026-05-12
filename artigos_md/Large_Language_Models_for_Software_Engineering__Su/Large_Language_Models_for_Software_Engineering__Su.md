<!-- Página 1 -->

## Large Language

## Models

## for

## Software

## Engineering:

## Survey

## and

## Open

## Problems

Angela FanBeliz GokkayaMark Harman Generative AITeamPyTorchTeamInstagram ProductFoundation Meta PlatformsInc.MetaInc.MetaInc. New York, NY, USAMenlo Park,CA,USALondon, UK

Mitya LyubarskiyShubho SenguptaShin YooJie M.Zhang Developer InfrastructureFAIRSchool ofComputingDepartment ofInformatics Meta PlatformsInc.MetaInc.KAISTKing’s College London London, UKMenlo Park,CA,USADaejeon, KoreaUK

**Abstract—This paper**providesasurveyoftheemergingareaIn particular,wearealreadyabletodiscernimportant **of Large**LanguageModels(LLMs)forSoftwareEngineeringconnections to(andresonancewith)existingtrendsandwell- **(SE). It also sets out open research challenges for the application**established approaches and subdisciplines within Software En- **of LLMs**totechnicalproblemsfacedbysoftwareengineers. gineering. Furthermore, although we find considerable grounds**LLMs’ emergent**propertiesbringnoveltyandcreativitywith for optimism,thereremainimportanttechnicalchallenges,**applications right**acrossthespectrumofSoftwareEngineering **activities including**coding,design,requirements,repair,refac- which arelikelytoinformtheresearchagendaforseveral **toring, performance improvement, documentation**andanalytics.years. Manyauthorshavehighlighted,bothscientificallyand **However,**theseverysameemergentpropertiesalsoposesignif-anecdotally,thathallucinationisapervasiveproblemfor **icant technical**challenges;weneedtechniquesthatcanreliably LLMs [1]andalsothatitposesspecificproblemsforLLM-**weed out**incorrectsolutions,suchashallucinations.Oursurvey based SE [2]. As with human intelligence, hallucination means**reveals the**pivotalrolethathybridtechniques(traditionalSE **plus LLMs)**have toplayinthedevelopment anddeploymentoftheLLMcancreatefictitiousoutput.Inthecontextof **reliable, efficient**andeffectiveLLM-basedSE.software engineering,itmeansthattheengineeringartefacts **Index Terms****—Automated Program**Repair,Documentationcreated couldbeincorrect,yetappearplausible;LLMsmay **generation, Generative**AI,GeneticImprovement,Human- introduce bugs. **Computer Interaction,**LargeLanguageModels,Refactoring, However,unlike many other applications of LLMs, software**Requirements engineering,**SearchBasedSoftwareEngineering engineers aretypicallyblessedwithautomatablegroundtruth**(SBSE), Software**Analytics,EngineeringEducation, **Software Processes,**MaintenanceandEvolution,Soft-(software execution), against which most software engineering **ware Testing.**artefacts canbeevaluated.Also,thesoftwareengineering research communityhasalreadydevotedagreatdealoftime to producingautomatedandsemi-automatedtechniquesforI. INTRODUCTION checking the potentially incorrect results produced by humans. This papersurveystherecentdevelopments,advancesandThis means that, for the discipline and the research community, empirical resultsonLLM-basedSE;theapplicationofLargethere isagreatdealofexperienceandexpertiseonwhich Language Models(LLMs)toSoftwareEngineering(SE)ap-to draw,whentacklingthechallengesposedbyissueslike arXiv:2310.03533v4 [cs.SE] 11 Nov 2023plications. We usethesurvey tohighlightgapsinthisrapidlyhallucination. developing, butasyetembryonic,researchliterature.BasedClearly,automatedtestingtechniques[3]–[5]willhavea on gapsintheliteratureandtechnicalopportunities,wecentral role to play in ensuring correctness, just as they already also identifyopenproblemsandchallengesforthesoftwaredo forhuman-engineeredartefacts.Whengeneratingentirely engineering researchcommunity.new featuresandsystems,automatedtestdatageneration suffers fromthelackofanautomatableoracle[6](anau-While anysurveyofsucharapidlyexpandingareacan neither aspire nor claim to be comprehensive, we hope that thistomated techniquefordeterminingwhetheroutputbehaviour is correct for a given input stimulus). Given LLMs’ propensitysurvey willprovideausefulandrelativelycompletesnapshot to hallucinate, the Oracle Problem will remain highly relevant,of theearlyuniverseofthisexcitingnewsubdisciplineof toitwillbecomeallthemoreimpactful[7].Software Engineering:LLM-basedEngineering.Al-and solutions some SE applications concern adaption, improve-though thescientificandtechnicalstructureofthefieldisstill However, emerging, itisalreadypossibletoidentifytrends,productivement and development ofexisting software systems, for which avenues for future research, and important technical challengesthereisa readily-availableautomatableoracle:thefunctional behaviour oftheoriginalsystem.that needtobeaddressed.

1


---

<!-- Página 2 -->

In thispaper,wecallthisthe‘Automated RegressionOra-For example,well-studiedtechniques,suchasparametric and non-parametricinferentialstatistics,arenowroutinelycle’, anapproachthathasalreadyproved advantageous inthe used toproviderobustscientificconclusionsinthepresencefield ofGeneticImprovement [8].TheAutomatedRegression of highly non-deterministic algorithms in the SBSE discipline.Oracle simply uses the existing version of the software system as areferenceagainstwhichtobenchmarkoutputfromany subsequent adaptionsandchanges.TABLE A (ALL)DENOTESCSOf course,thereisariskof‘bakingin’functionalincor- (C OMPUTERS CIENCE ). L (LLM)DENOTESrectness, since the Automated Regression Oracle cannot detect ABSTRACT“LLM”,ARGEL ANGUAGEM ODEL”, OR “GPT”. what thesystemshoulddo, butonlycapturewhatitcurrentlyL ∩ SDENOTES.SEOR.PLCATEGORY OR. N OTEdoes. Therefore,theAutomatedRegressionOraclecantest 2023ONLY27ULY 2023.only forfunctionalregressions soitisbestsuitedtousecases where theexistingfunctionalityistobemaintained.Forex- | L || L ∩S| Year| A |L |L ∩ S|(%)(%) | A || L |ample, fornon-functionalimprovementssuchasperformance 2007optimisation andforsemantics-preservingrefactoring. 2008The inputprovidedtoanLLMwillbeanaturalfocusof 2009 growing research,andwecanexpectarapiddevelopmentof2010 2011the literatureonpromptengineeringandoptimisation 2012[9]. Inthissurvey,wehighlightexistingworkandopen 2013 challenges forpromptengineeringwithregardtoseveral2014 2015specific aspectsofsoftwareengineering. 2016The outputfromanLLMneednotbeconfinedpurelyto 2017 code, butcanalsoincludeothersoftwareengineeringarte-2018 facts, suchasrequirements,testcases,designdiagrams,and2019 2020documentation. Ingeneral,thelanguage-basednatureofan 2021 LLM, allows ittogenerateany linguistically-definedsoftware2022 engineering artefact.2023 Wetypicallythinkofthesoftwareengineeringartefactas the primaryoutputoftheLLM,butitisnottheonlyoutput.In order to understand the growth trends within LLM-based Theexplanationprovided withtheprimaryoutputisalsoanSoftware Engineering, we performed a manual analysis of data important outputofany LLM.Oursurvey highlightstheneedon thenumberofpublicationsonspecifictopicsfromarXiv. for muchmoreresearch,notonlyintooptimisingprompt1TableIcontainstherawdata, whichwasmanuallyextracted engineering (whichfocusesontheinputtotheLLM)but alsofrom thearXivmetadatadumpmadepubliclyavailablevia the need for work on the optimisation of explanations providedKaggle ([https://www.kaggle.com/datasets/Cornell-University/](https://www.kaggle.com/datasets/Cornell-University/) with theprimaryoutput.th.arxiv), accessedonthe27July 2023.Wefirstfiltered LLMs areinherentlynondeterministic:thesamepromptout publicationsforwhichtheclassificationcodedoesnot produces differentanswersoninferenceexecutionsstart withthe csprefix (i.e.,ComputerScience),resultingin (unless thetemperatureissettozero,whichhasoftenbeencolumnA . found to be suboptimal over multiple executions) [10]. Further-ToidentifyComputerSciencepapersthatarerelevantto more, irrespectiveofthetemperaturesetting,subtlechangesLLMs, wefilteredthepublicationsintosubcategorieson in thepromptcanleadtoverydifferentoutputs[10].Aswellartificial intelligence (cs.AI), machine learning (cs.LG), neural as motivating ‘prompt engineering’ and output processing, thisand evolutionarycomputation(cs.NE),softwareengineering nondeterministic behaviourraiseschallengesforthescientific(cs.SE), andprogramminglanguage(cs.PL)usingthequeries evaluation ofLLM-basedSoftwareEngineering:“Large LanguageModel”,“LLM”,and“GPT”ineitherthe If resultscanvaryeachtimeweruntheprocess,title ortheabstract(wemanuallyexcludedinstancesofover- how can we determine whether a proposed techniqueloaded acronymssuchasGPTforGeneralPlanningTool), achieves anadvanceoverthestateoftheart?resulting incolumnL . Finally,weusedthesamequeriesto This isaproblemthathasalreadybeenwellstudiedintheidentify LLM-basedSoftwareEngineeringpapersinsoftware context ofEmpiricalSoftwareEngineering[11]andSearchengineering (cs.SE) and programming language (cs.PL). These Based Software Engineering (SBSE) [12]. In particular, SBSEqueries areinherentlyapproximate,soweconfineourselves bears manysimilaritiestoLLM-basedSoftwareEngineering,only toconclusionsbasedonoveralltrendsforwhichthere sharing withittheneedtoachieve robust scientificevaluationis strongevidenceratherthanspecificdetailsofthenumbers in thepresenceofnoisy,non-deterministic,andincompleteobserved. Nevertheless,wereporttherawnumbersobserved results [13],[14].Thereis,therefore,alreadyamaturesoft-to supportreplicationbyothers. ware engineering literature on just the kind of robust scientific evaluation techniques needed to cater for LLM-based scientific1The Julyevaluation.

2


---

<!-- Página 3 -->

. . . . . .

# of preprints% of preprints

010 01 0

Fig.

Also, giventherecentupsurgeinattentionforLLMs,the exponential rise in the number of papers on LLMs is relatively unsurprising. Perhaps moreinterestingistherapiduptakeofSoftware Engineering applicationsofLLMs,asrevealed bythegrowth trend, picturedingreenonthisfigure.Inordertoexamine this trendinmoredetail,weplottheproportionofLLMpub- lications (L) toallCSpublicationsA( inblue,aswellasthe proportions ofLLM-basedsoftwareengineeringpublications Fig. ( L ∩ S) toallLLMpublicationsinorangeinFigure3.Asof can beseen,theproportionofLLMpapersonLLM-basedpreprints ComputingSoftware Engineering has been rising dramatically since 2019. guage Already,more than 10% of all papers on LLMs are concerned“LLM”, with LLM-basedSoftwareEngineering.PL “LLM”,As a result of this growth, we can expect many other surveys of LLM-Based SE. The rapid expansion of the literature makes it unlikelythatfurthercomprehensive SE-widestudieswillfit the space constraints of a single paper, but we can expect many specific comprehensivesurveysofsub-areasofinterest,and # in CS categoryalso Systematic Literature Reviews (SLRs) that tackle SE-wide # w/ LLM in title or abstractcrosscutting issuesbyaskingspecificresearchquestionsof% of LLM papers in CS category 10the primaryliteratureinthesystematicreview. Already, such# in cs.SE or cs.PL w/ LLM in title or abstract % of SE papers out of LLM papersSLRs areappearing.Forexample,Houetal.[15]provided an excellentrecentSLRcovering229researchpapersfrom8 2017 to2023reportingSEtaskstackled,datacollectionand Fig. preprocessing techniques,andstrategiesforoptimisingLLMLLMs”,6performance (suchaspromptengineering).“LLM”, percentageTheremainder2018ofthispaperisorganisedfollowthetop-2008201020122014201620202022 to all 4level software development activities andresearchdomainsasthe preprintsdepicted inFigure1. 2 II. PRELIMINARIES Figure 2,showsthegrowthinthenumberofarXiv- A. LargeLanguageModels0published papersonComputerScience|A( | , inBlue),andon A LargeLanguageModel(LLM)referstoanArtificialLLMs (|L|, inorange).ThosepapersspecificallyonSoftware20082010201220142016201820202022 Intelligence (AI) model that has been trained on large amountsEngineeringandLLMs aredepictedinGreen| L∩S | ). of dataandisabletogeneratetextinahuman-likefashion.Given therapidriseinoverallpublicationvolumes,weuse a logarithmicscalefortheverticalaxis.Unsurprisingly,weTableIII provides a glossary of LLM terminology to make the paper self-contained.see anoverallriseinthenumberofCSpublications.

3

# O

# r

# i

# g

# i

# n

# d

# a t

# a s e t

# M

# i

# r

# r

# o

# d

# a t

# a s e t

# d

# a t

# a s e t

# s

# p

# r

# o

# b

# l

# e m

#

# d

# e s c r

# i

# p

# t

# i

# o

# n

# a l

#

# r

#

# p

# r

# o

# m

# p

# t

# e s t

#

# s u

# i

# t

# e

# t

# C

# h

# a t

# O

# r

# i

# g

# i

# n

# a l

#

# m

# o

# d

# e l

# M

# i

# r

# r

# o

# r

#

# m

# o

# d

# e l

# r

# e s p

# r

# e s p

# G

# P

# T

# r

# e s p

# o

# n

# s e

# o

# n

# s e

# o

# n

# s e

# 1

# 2

# n

# p

# p

# p

# r

# o

# r

# o

# r

# o

# g

# g

# g

# r

# a m

# r

# a m

# r

# a m

#

# 1

#

# 2

#

# n

# e x e cu

# t

# e x t

# A

# s s e ssi

# t

# e s t

#

# t

# i

# o

# r

# e s u

# l

# t

# s

#

# a n

# a l

# y s i

# A

# S

# T

# n

# n

# g

#

# s

#

# T r

# u s t

# w

# o r

# t

# h i

# o f

#

# c o d e

# S

# e m

# a n

# t

# i

# c

# s i

# m

# i

# l

# a r

# i

# t

# y

# S

# y n

# t

# a c t

# i

# c

# s i

# m

# i

# l

# a r

# i

# t

# y

# S

# t

# r

# u

# c t

# u

# r

# a l

# s i

# m

# i

# l

# a r

# i

# t

# y

# U

# n

# d

# e r

# n e s s

#

# s t

# a n

# C

# o r

# r

# e c t

# n e s s

# a n d

# P

# e r

# f

# o r

# m

# a n c e

# B

# e f

# o r

# e

# c o d e

# P

# r

# o m

# p t

#

# g e n er

# a t

# i

# o n

# e n g i

# n e e r

# i

# n g

# S

# e c u r

# i

# t

# y ,

#

# F a i

# r

# n e s s,

#

# a n d

# P

# r

# i

# v a c y

# I

# n f

# l

# u e n ce

# o n

# P

# i

# l

# o

# t

# i

# n

# g

# A

# s s u

# r

# i

# n

# g

# t

# h e

# s o c i

# e t

# y

# C

# o d e

# t

# e s t

# i

# n g

# R

# o b u st

# n e s s

# a n d

# A

# f

# t

# e r

#

# c o d e

# S

# t

# a b i

# l

# i

# t

# y

# g e n er

# a t

# i

# o n

# C

# o d e

# U

# n d e r

# s t

# a n d abi

# l

# i

# t

# y

# o p t

# i

# m

# i

# s a t

# i

# o n

# a n d

# E

# v o l

# v a b i

# l

# i

# t

# y

## a l

## g o r

## i

## t

## h m

##

## i

## m

## p r

## o v e m

## e n t

## L e a r

## n i

## n g

## p r

## o g r

## a m

## E

## x p l

## a i

## n a b i

## l

## i

## t

## y

## C

## o n v er

## s a t

## i

## o n a l

##

## A

## I

##

## O

## f

## f

## l

## i

## n e

## O

## n l

## i

## n e

## i

## m

## p r

## o v e m

## e n t

##

## v i

## a

## m

## o d e l

##

## b u i

## l

## d i

## n g

## v a l

## i

## d a t

## i

## o n

## d e p l

## o y m

## e n t

## p e r

## -

## m

## u t

## a t

## i

## o n

## a n d

## T r

## a i

## n i

## n g

## d a t

## a

## c a u sal

##

## a n a l

## y s i

## s

## O

## r

## i

## g i

## n a l

##

## b o t

##

## U

## s e r

##

## i

## n p u t

##

## d a t

## a

## r

## e s p onse

## a u g em

## e n t

## a t

## i

## o n

## c h a t

## b o t

## O

## n l

## i

## n e

## f

## a i

## r

## n e s s

## u s e r

##

##

##

## d a t

## a

## t

## e s t

## i

## n g

## g e n er

## a t

## i

## o n

## O

## n l

## i

## n e

## f

## a i

## r

## n e s s

## F a i

## r

##

## b o t

##

## e n h ancem

## e n t

## r

## e s p onse

## a u g m

## e n t

## e d

## W

## P

## 4 :

##

## D

## a t

## a

## a u g m

## e n t

## a t

## i

## o n

## d a t

## a

## a n d

## f

## i

## n e -

## t

## u n i

## n g

## f

## i

## n e -

## t

## u n i

## n g

## c h a t

## b o t

## o r

## i

## g i

## n a l

##

## b o t

##

## u s e r

##

## i

## n p u t

## r

## e p o nse

## m

## u t

## a t

## i

## o n

## f

## a i

## r

## n e s s

## f

## i

## n a l

##

## b o t

##

## u n f

## a i

## r

## n e s s?

## m

## u t

## a n t

##

## a n a l

## y s i

## s

## r

## e s p onse

## c a n di

## d a t

## e s

## f

## i

## l

## t

## e r

## i

## n g

## Y e s

## c h a t

## b o t

## b e s t

##

## a n d

## f

## a i

## r

##

## r

## e s o nse

## f

## o r

##

## f

## i

## l

## t

## e r

## e d

## r

## e s p onse

## m

## u t

## a n t

## s

## m

## u t

## a n t

## s

##

## e n s em

## b l

## e

##

## W

## P

## 1 :

##

## t

## e s t

##

## i

## n p u t

##

## a n d

## o r

## a c l

## e

## d e s i

## g n

## W

## P

## 2 :

##

## a u t

## o m

## a t

## i

## c

## f

## a i

## r

## n e s s

## t

## e s t

## i

## n g

##

## W

## P

## 3 :

##

## a u t

## o m

## a t

## i

## c

## f

## a i

## r

## n e s s

## e n h ancem

## e n t

## B

## l

## a c k -

## b o x

## o p t

## i

## m

## i

## s a t

## i

## o n

## W

## P

## 1 :

##

## B

## u g

## p r

## e d i

## c t

## i

## o n

## W

## P

## 3 :

##

## W

## P

## 4 :

##

## G

## e n e r

## a t

## e d

## O

## p t

## i

## m

## i

## s e d

## B

## u g s

##

##

##

##

## Y e s

## A

## u t

## o m

## a t

## i

## c

## b u g

## A

## u t

## o m

## a t

## i

## c

## c o d e

## c o d e

## e x i

## s t

## e n c e?

## l

## o c a l

## i

## s a t

## i

## o n

## b u g

## r

## e p a i

## r

## W

## P

## 2 :

##

## A

## I

##

## c o d e

## A

## u t

## o m

## a t

## i

## c

## D

## e v e l

## o p e r

## s

## g e n er

## a t

## o r

## N

## o

## t

## e s t

## i

## n g

## B

## u g

## c o r

## p u s

## R

## e t

## u r

## n

## o r

## i

## g i

## n a l

##

## c o d e

## t

## o

## d e v el

## o p e r

## s

## A

## u t

## o m

## a t

## i

## c

## b u g

## d e t

## e c t

## i

## o n

## A

## u t

## o m

## a t

## i

## c

## b u g

## r

## e p a i

## r

##

##

## W

## P

## 5 :

##

## T o o l

##

## a n d

## d a t

## a s e t

##

## d e v el

## o p o m

## e n t

## C

## o r

## r

## e c t

## n e s s

## a n d

## P

## e r

## f

## o r

## m

## a n c e

## W

## 1 :

##

## S

## e c u r

## i

## t

## y ,

##

## F a i

## r

## n e s s,

##

## a n d

## P

## r

## i

## v a c y

## B

## e f

## o r

## e

## c o d e

## W

## 3 :

##

## P

## r

## o m

## p t

##

## C

## a p a bi

## l

## i

## t

## i

## t

## e s

## R

## o b u st

## n e s s

## a n d

## S

## t

## a b i

## l

## i

## t

## y

## g e n er

## a t

## i

## o n

## e n g i

## n e e r

## i

## n g

## a n d

## r

## i

## s k s

## U

## n d e r

## s t

## a n d abi

## l

## i

## t

## y

## a n d

## E

## v o l

## v a b i

## l

## i

## t

## y

# d

# i

# n

# g

# A

# s s u

# r

# i

# n

# g

## W

## 4 :

##

## C

## o d e

## a s s essm

## e n t

## I

## n d u st

## r

## y

## A

## f

## t

## e r

##

## c o d e

## g e n er

## a t

## i

## o n

## W

## 2 :

##

## I

## n f

## l

## u e n ce

## W

## 5 :

##

## C

## o d e

## E

## d u c at

## i

## o n

## o n

## t

## h e

## s o c i

## e t

## y

## o p t

## i

## m

## i

## s a t

## i

## o n

## R

## e s e ar

## c h

## m

## a c h i

## n e

## t

## r

## a n s l

## a t

## o r

## o r

## i

## g i

## n a l

##

## o r

## i

## g i

## n a l

##

## t

## r

## a n s l

## a t

## i

## o n

## s e n t

## e n c e

## c o n t

## e x t

## -

## s i

## m

## i

## l

## a r

##

## m

## u t

## a t

## i

## o n

## s i

## m

## i

## l

## a r

## i

## t

## y

## f

## i

## n a l

##

## m

## u t

## a n t

##

## I

## n c o nsi

## s t

## e n c y?

## a n a l

## y s i

## s

## t

## r

## a n s l

## a t

## i

## o n

## c a n di

## d a t

## e s

## s t

## r

## u c t

## u r

## a l

##

## f

## i

## l

## t

## e r

## i

## n g

## m

## a c h i

## n e

## Y e s

## t

## r

## a n s l

## a t

## o r

## b e s t

##

## m

## u t

## a n t

##

## f

## i

## l

## t

## e r

## e d

## t

## r

## a n s l

## a t

## i

## o n

## t

## r

## a n s l

## a t

## i

## o n s

## m

## u t

## a n t

## s

## p r

## o b a bi

## l

## i

## t

## y

## o r

##

##

## c r

## o s s

## r

## e f

## e r

## e n c e

## a u t

## o m

## a t

## i

## c

## t

## e s t

##

## i

## n p u t

##

## g e n er

## a t

## i

## o n

## a u t

## o m

## a t

## i

## c

## t

## e s t

##

## o r

## a c l

## e

## g e n er

## a t

## i

## o n

##

## a u t

## o m

## a t

## i

## c

## i

## n c o nsi

## s t

## e n c y

## r

## e p a i

## r

### m

### a c h i

### n e

### t

### r

### a n s l

### a t

### o r

### I

### s

### t

### h e

### s i

### m

### i

### l

### a r

### i

### t

### y

### b e t

### w

### e e n

### t

### h e

### t

### w

### o

### t

### r

### a n s l

### a t

### i

### o n s

### S

### t

### (

### S )

### s m

### a l

### l

### e r

###

### t

### h a n

### t

### h r

### e s h ol

### d

### r

### ?

### o r

### i

### g i

### n a l

###

### t

### r

### a n s l

### a t

### i

### o n

### i

### n p u t

###

### t

### r

### a n s l

### a t

### i

### o n

### o u t

### p u t

###

### f

### o r

###

### S

### s i

### m

### i

### l

### a r

### i

### t

### y

### a n a l

### y s i

### s

## s i

## m

## (

## t

## (

## S

## )

## ,

##

## t

## (

## S

## '

## )

## )

##

## <

## r

## ?

### b e t

### w

### e e n

### t

### (

### S )

###

### a n d

### t

### (

### S '

### )

### m

### a c h i

### n e

### t

### r

### a n s l

### a t

### o r

## Y e s

### S ?

### t

### (

### S ?

### )

### t

### r

### a n s f

### o r

### m

### e d

### t

### r

### a n s l

### a t

### i

### o n

### o u t

### p u t

###

### f

### o r

###

### S ?

###

### t

### r

### a n s l

### a t

### i

### o n

### i

### n p u t

###

### r

### e p a i

### r

###

### r

### e s u l

### t

### s

### R

### (

### t

### (

### S )

### )

### r

### e p a i

### r

###

### t

### (

### S )

## s i

## m

## (

## R

## (

## t

## (

## S

## )

## )

## ,

##

## R

## (

## t

## (

## S

## '

## )

## )

## )

##

### s i

### m

### i

### l

### a r

### i

### t

### y

### a n a l

### y s i

### s

### b e t

### w

### e e n

## N

## o

## e n d

## <

## r

## ?

### R

### (

### t

### (

### S )

###

### )

### a n d

### R

### (

### t

### (

### S '

### )

### )

### R

### (

### t

### (

### S '

### )

### )

### r

### e p a i

### r

###

### t

### (

### S '

### )

### I

### s

### t

### h e

### s i

### m

### i

### l

### a r

### i

### t

### y

### b e t

### w

### e e n

### t

### h e

### r

### e p a i

### r

###

### w

### i

### t

### h

### t

### h e

### b e s t

###

### t

### w

### o

### r

### e p a i

### r

### e d

### t

### r

### a n s l

### a t

### i

### o n s

### D

### o e s

### t

### (

### S '

### )

###

###

### h a v e

### m

### u t

### a n t

###

### m

### u t

### a n t

###

### t

### r

### a n s l

### a t

### i

### o n

### s m

### a l

### l

### e r

###

### t

### h a n

### t

### h r

### e s h ol

### d

### r

### ?

### t

### r

### a n s l

### a t

### i

### o n s

### t

### h a t

###

### h a v e

### n o t

###

### b e e n

### u s e d

### ?

## Y e s

## t

## (

## S

## '

## )

##

## h a s

## o t

## h e r

##

## m

## u t

## a n t

##

### r

### e p a i

### r

###

### t

### (

### S '

### )

###

### w

### i

### t

### h

### a n o t

### h e r

###

## Y e s

## t

## r

## a n s l

## a t

## i

## o n s ?

### m

### u t

### a n t

###

### t

### r

### a n s l

### a t

### i

### o n

### r

### e p a i

### r

###

### w

### i

### t

### h

### t

### h e

### n e x t

### -

### b e s t

###

## N

## o

### m

### u t

### a n t

###

### t

### r

### a n s l

### a t

### i

### o n

## a u g m

## e n t

## e d

## d a t

## a

## f

## i

## n e -

## t

## u n i

## n g

## c h a t

## b o t

## o r

## i

## g i

## n a l

##

## b o t

##

## u s e r

##

## i

## n p u t

## r

## e p o nse

## m

## u t

## a t

## i

## o n

## b e s t

##

## a n d

## f

## a i

## r

##

## f

## a i

## r

## n e s s

## f

## i

## n a l

##

## b o t

##

## m

## u t

## a n t

##

## u n f

## a i

## r

## n e s s?

## Y e s

## r

## e s p onse

## a n a l

## y s i

## s

## r

## e s p onse

## c a n di

## d a t

## e s

##

## e n s em

## b l

## e

## f

## i

## l

## t

## e r

## i

## n g

## c h a t

## b o t

## r

## e s o nse

## f

## o r

##

## f

## i

## l

## t

## e r

## e d

## m

## u t

## a n t

## s

## m

## u t

## a n t

## s

# I

# n d u st

# r

# y

# E

# d u c at

# i

# o n

# R

# e s e ar

# c h

# G

# o v e r

# n m

# e n t

## S

## o f

## t

## w

## a r

## e

## d e v el

## o p m

## e n t

## a c t

## i

## v i

## t

## i

## e s

## R

## e s e ar

## c h

## D

## o m

## a i

## n s

##

## R

## e q u i

## r

## e m

## e n t

##

## E

## n g i

## n e e r

## D

## e s i

## g n

## &

##

## P

## l

## a n n i

## n g

## C

## o d e

## I

## m

## p l

## e m

## e n t

## a t

## i

## o n

## T e s t

## i

## n g

## M

## a i

## n t

## a i

## n a n ce

## D

## e p l

## o y m

## e n t

## i

## n g

## S

## e c t

## i

## o n

## S

## e c t

## i

## o n

## S

## e c t

## i

## o n

## S

## e c t

## i

## o n

## S

## e c t

## i

## o n

## S

## e c t

## i

## o n

## M

## i

## n i

## n g

## S

## e c t

## i

## o n

## S

## e c t

## i

## o n

## S

## e c t

## i

## o n

## S

## e c t

## i

## o n

## I

## I

## I

## :

##

## R

## e q u i

## r

## e m

## e n t

##

## E

## n g i

## n e e r

## i

## n g

## &

##

## D

## e s i

## g n

## I

## V :

##

## C

## o d e

## G

## e n e r

## a t

## i

## o n

## &

##

## C

## o m

## p l

## e t

## i

## o n

## V :

##

## S

## o f

## t

## w

## a r

## e

## T e s t

## i

## n g

## V

## I

## :

##

## M

## a i

## n t

## a i

## n a n ce,

##

## E

## v o l

## u t

## i

## o n ,

##

## &

##

## D

## e p l

## o y m

## e n t

## V

## I

## I

## :

##

## D

## o c u m

## e n t

##

## G

## e n e r

## a t

## i

## o n

## V

## I

## I

## I

## :

##

## S

## o f

## t

## w

## a r

## e

## A

## n a l

## y t

## i

## c s

## a n d

## R

## e p o si

## t

## o r

## y

## I

## X

## :

##

## H

## u m

## a n

## C

## o m

## p u t

## e r

##

## I

## n t

## e r

## a c t

## i

## o n

## X

## :

##

## S

## o f

## t

## w

## a r

## e

## E

## n g i

## n e e r

## i

## n g

## P

## r

## o c e ss

## X

## I

## :

##

## S

## o f

## t

## w

## a r

## e

## E

## n g i

## n e e r

## i

## n g

## E

## d u c at

## i

## o n

## X

## I

## :

##

## C

## r

## o s s cut

## t

## i

## n g

## O

## p e n

## R

## e s e ar

## c h

## T o p i

## c

## P

## a p e r

##

## S

## t

## r

## u c t

## u r

## e

## C

## o d e

## G

## e n e r

## a t

## i

## o n

## M

## o d e l

## s

## P

## r

## o m

## p t

##

## E

## n g i

## e e r

## i

## n g

## f

## o r

##

## I

## m

## p r

## o v e d

## C

## o d e

## G

## e n e r

## a t

## i

## o n

## H

## y b r

## i

## d s

## o f

##

## L L M

## s

## a n d

## o t

## h e r

##

## T e c hni

## q u e s

## S

## c i

## e n t

## i

## f

## i

## c

## E

## v a l

## u a t

## i

## o n

## o f

##

## L L M

## -

## b a s ed

## C

## o d e

## G

## e n e r

## a t

## i

## o n

## G

## e n e r

## a t

## i

## n g

## N

## e w

##

## T e s t

## s

## U

## s i

## n g

## L L M

## s

## T e s t

##

## A

## d e q uacy

## E

## v a l

## u a t

## i

## o n

## T e s t

##

## M

## i

## n i

## m

## i

## s a t

## i

## o n

## T e s t

##

## O

## u t

## p u t

##

## P

## r

## e d i

## c t

## i

## o n

## T e s t

##

## F l

## a k i

## n e s s

## D

## e b u ggi

## n g

## a n d

## R

## e p a i

## r

## P

## e r

## f

## o r

## m

## a n c e

## I

## m

## p r

## o v e m

## e n t

## C

## l

## o n e

## D

## e t

## e c t

## i

## o n

## a n d

## R

## e -

## u s e

## R

## e f

## a c t

## o r

## i

## n g

t e st i n g

a u t o m a t i c

r e p a i r

i n co n si st e n cy

a u t o m a t i c

e d i t i n g

r e s p o n s e

m a p p i n g

t r a n s l a t i o n

e d i

r e s p o n s e

t i n g


---

<!-- Página 4 -->

LLMs are typically based on deep learning techniques, suchPopular examplesofdecoder-onlymodelsaretheGPT as transformers,andhavethecapabilitytogenerateuseful(Generative Pre-trained Transformer) series developed by Ope- language output.Asaresult,they have beenfoundcapableofLLaMAfromMeta,ClaudefromAnthropic,andPaLM performing awiderangeoflanguage-relatedtasks,includingfrom Google[1]. text generation [16], answering questions [17], translation [18], C. LargeLanguageModelsforSoftwareEngineeringsummarization [19],andsentimentanalysis[20]. Rumelhart etal.[21]introducedtheconceptofRecurrentWhile LLMshavebeenwidelyappliedtotasksinvolving Neural Network,openingupthepossibilityofprocessingnatural languages,theirapplicationtosoftwaredevelopment sequential data.LongShortTermMemory(LSTM)archi-tasks, involving programminglanguages,hasalsogainedsig- tecture, anextensionoftheRNNarchitectureintroducedbynificant recentattention. Hochreiter and Schmidhuber [22], significantly improved theirIn 2021,OpenAIintroducedCodeX,afined-tuneddescen- performance inmanyapplications.dant ofGPT-3.CodeXisusedbyGitHub’sCopilot,which In 2017,Vaswanietal.[23]introducedtheTransformerprovides usersofVisual StudioCode,Studio,Neovim, architecture, whichcaptureswordrelationshipswiththeself-and JetBrains with code completion. The new version of Copi- 2attention mechanism.Thetransformerarchitecturehadapro-lot, GitHub Copilot X, is based on GPT-4. In February 2023, 3found impactonlanguagemodellingandtriggeredanexplo-GitHub reportedthat,onaverage,46%of thedevelopers’ sion ofactivityonLLMs.code waswrittenbyCopilot[25].ForJava only, thatnumber In 2018, OpenAI released the Generative Pre-trained Trans-is 62%.ThomasDohmke,CEOofGitHub,saidCopilotwill former (GPT) model, followed by subsequent iterations (GPT-write 80%ofcode“soonerthanlater”inJune2023[26]. 2, GPT-3,GPT-3.5, andGPT-4). WithGPT-3 and3.5,manyIn 2022,DeepMindintroducedAlphaCode[27],trained observers noticedasignificantstepchangeingenerativewith 40B parameters on selected public GitHub repositories. It performance, thereby attracting a great deal of interest in GPTachieved onaverage arankinginthetop54%incompetitions (and ChatGPT) in particular, and also in LLMs more generally.with morethan5,000participantsinsimulatedevaluations. LLMs achievethisperformance,inpart,duetothelargeThe mostrecentGPTmodel,GPT-4,alsoperformscode corpora onwhichtheyaretrained:Forexample,GPT-3isgeneration. AccordingtoGPT-4’stechnicalreport[28],the trained on45TBoftextdataandhas175billionparameters.zero-shot pass@1 accuracy is 67% with GPT-4 on HumanEval, Meta launched open-sourced LLaMA in February 2023, whichan open-sourcedatasetfromOpenAIconsistingof164pro- is trainedon1.4trilliontokenswithavarietyofmodelsizesgramming problems. ranging from7billionto65parameters[24].On abenchmarkof100LeetCodeproblems,GPT-4has comparable performancewithhumandevelopers[29].On th.the24August 2023,Metareleasedopen-sourcedCodeB. CategoriesofLargeLanguageModels Llama [30],astate-of-the-artforpubliclyavailableLLMson There arethreecategoriesoflargelanguagemodels:coding tasks. 1)**Encoder-only model**: alsoknownasanautoencoder, TableIIliststherepresentativeLLMsthataredesigned consists ofanencodernetworkbutdoesnothaveaseparate for codegeneration/completionbasedonnaturallanguage decoder network.Ittakesaninputsequenceandmapsittoa descriptions. lower-dimensional representation.Thepurposeofanautoen- coder istolearnanencodingoftheinputdata.ExamplesofIII. REQUIREMENTSE NGINEERINGD ESIGN Encoder-only LLMsareBERT fromGoogle,RoBERTa from Requirements engineeringisanimportantdisciplineinMeta, andDeBERTa fromMicrosoft[1]. software engineering.Itformsthefundamentallinkbetween2)**Encoder-decoder model: in**additiontotheencodernet- the technical attributes of the system software engineers build,work, thereisadecodernetworkthatgeneratesanoutput and thepurposeforwhichthesystemsarebuilt.Thereisasequence by iteratively generating tokens or symbols based on mature literature,andalargeresearchcommunityconcernedthe contextvectorandpreviouslygeneratedtokens.Itcanbe specifically withproblemsassociatedwithrequirementsengi-adopted fortaskslikemachinetranslationortextgeneration. neering problems[31].Examples ofEncoder-decoder LLMsareT5fromGoogleand There hasalsobeenprevious workonartificialintelligenceBARTfromMeta[1]. approaches tosupportrequirementsengineering,notablyin3)**Decoder-only model : Unlike**theprevioustwotypesof the form of computational search for requirements engineeringLLMs, decoder-only LLMs do not have an encoder component [32]. However,hitherto,thedisciplineofrequirementsengi-to processtheinputdata,butonlyadecodercomponent neering has received less attention from the emerging literaturethat directlygeneratesanoutputsequencebasedonagiven on LLM-basedsoftwareengineering.context orinput.Decoder-onlymodelsareoftenbasedon architectures suchasautoregressive models,wheretheoutput 2GitHubis generatedtoken-by-token.Eachtokenbythe on decoder isconditionedontheprevioustokensgeneratedand3In the context.digits.

4


---

<!-- Página 5 -->

TABLE E XISTINGL ARGEL ANGUAGEM ODELSC ODEG ENERATION

TABLE K EY TERMINOLOGYR ELATEDL ARGEL ANGUAGEM ODELS

**Term**

Chain

Encoder space.

Few-shot labelled

Fine-tuning to

Generative

Parameters Weights for parameters

Prompt

Prompt

ReAct **Name**Typethe **CodeBERT**FebruaryYES **InCoder**April **AlphaCode**FebruaryTemperature **CodeX**August>11content,Github**Copilot**October12B>11 **CodeT5**NovToken**CodeT5+**May **PolyCoder**Octcharacters,>11 **CodeWhisperer**April **WizardCoderJune**Top-N, **CodeGeeX**Sepof **CodeGen**March programming**StarCoder**May>80 **phi-1**June Zero-shot**Code**August>7 the Zhang etal.[33]conductedapreliminaryevaluationofA. OpenProblemsinLLMsforRequirementEngineering ChatGPT’szero-shotrequirementretrievalperformanceonUnlike othersoftwaredevelopmentactivities,wedidnot two requirementsanalysistasksoverfourdatasets.Althoughfind muchworkonLLM-basedrequirementsengineeringor these resultsareonlypreliminary, theyprovideoptimismthaton LLM-baseddesign.Indeed,therewasevenevidencethat LLMs canbeusedasasupportforefficientandeffectivepractising engineersarereluctanttorelyonLLMsforhigher- requirements engineering.Luoetal.[34]conductedpromptlevel designgoals[36].Thereisthusagreatopportunityto engineering withBERTforautomaticrequirementclassifica-expand onthisopenfieldofresearch. tion. Luiteletal.[35]focusedonrequirementscompletenessThe majority of LLM applications are focused on tasks such and used BERT to generate predictions for filling masked slotsas codegeneration,testing,andrepair.Thesetasksbenefit in requirements.from LLM’s capabilitytogeneratecode.Nevertheless, LLMs also havesignificantpotentialtosupportrequirementsengi- neering activities,thankstotheirnaturallanguageprocessing capabilities.

5


---

<!-- Página 6 -->

For example,traceabilityisalong-standing,cross-cuttingTheir empiricalstudyprovidedevidencefortheefficacy of approach,butalsounderlinedtherepetitiveconcern insoftwareengineering.Inparticular,identifying this scavenging natureofsoftware.Inalargerrepositorytraceability linksbetweenrequirementsandotherengineeringand predictable (sourceforge), GabelandSu[47]foundthataprogrammerartefacts, suchascodeandtests,areespeciallychallenging towritemorethansixlinesofcodeinordertobecause requirementsareoftenwritteninnaturallanguage;would have natural fitforLLMs.create anovelcodefragment. These researchfindingsoncodenaturalness,reusability IV. CODEG ENERATIONC OMPLETIONand predictability, makeitunsurprisingthatLLMshavebeen able toexploitthatsamepredictablereusabilitytoproduceOf all the Software Engineering application areas for LLMs, effectiverecommendationsforcodegeneration.Theseob-code completionistheareathathasbeenmostthoroughly servations haveunderpinnedthegrowthofgenerate-and-testexplored hitherto.EvenpriortotheadventofLLMs,itwas approaches torepairandgeneticimprovement[8],[46].Thesuggested thatlearningfromexistingcoderepositoriesisthe generate-and-test approachoffersgreatercodetransformationkey tosuccessfulandintelligentcodecompletion[37]:pre- freedom (compared to more traditional correct-by-constructiontrained LLMsdeliverontheseearlyaspirationsforcode approaches [48]),preciselybecausethegeneratedcodemaycompletion. Whilehallucinationhasbeenpointedoutasthe not preservestrict,mathematically-defined(andnotalwaysweakness ofLLMsmoregenerally,thespecifictaskofcode appropriate, noruseful)interpretationsofcorrectness.completion sidestepshallucinationproblemsbyactingasa This freedomtoexploreawiderspaceof“semanticnearrecommender systemtothedeveloper.Thedeveloperthus neighbours” allowsGeneticImprovementtofinddramaticbears theresponsibilitytoweedoutanyhallucinatedLLM optimisations (seeSectionVI-C).TheGeneticImprovementoutput beforeitleaksintothecodebase. approach, nomenclature,andevaluationmethodologiesalsoOf course,ahighdegreeofhallucinationwouldhave provide a scientific framework within which to understand andmade codecompletionrecommendersystemsineffective. The evaluate LLM-based code generation. Both technologies sharewidespread and rapid adoption, and the positive results already the ‘generate-and-test’approachtoprogramtransformationreported forcodecompletion,provideearlyindicationsthat and codegeneration,potentiallymakingmuchoftheexistingthis has not happened. For example, Murali et al. [38] reported work ongeneticimprovementdirectlyapplicabletoLLM-the experience of deploying CodeCompose, a code completion based codegeneration.toolontheIncoderLLM[39],atMeta.During15 In 2021, Chen et al. [49] introduced CodeX, a GPT languagedays, 4.5millioncodecompletionsuggestionsweremadeby model fine-tuned on publicly available code from GitHub, andCodeCompose, andtheacceptanceratefromdeveloperswas evaluated its Python code-writing capabilities. They released a22%. Thequalitative feedbackwashighlypositive, with92% new evaluation setcalled‘HumanEval’tomeasurefunctionalpositive. Similarly, Peng et al. [40] reported that programmers correctness forsynthesizingprogramsfromdocstrings,andcould completeanon-trivialtask(implementinganHTTP found that CodeX outperformed GPT-3 and GPT-J when tack-server inJavaScript)56%fasterwhenpairedwithGitHub ling these problems. Since then there has been an explosion inCopilot, comparedtothecontrolgroupthatdidnotreceive research onLLM-basedcodegenerationandtheHumanEvalany suchsupport. dataset hasbeenusedinmanysubsequentstudies.Many softwareengineersalreadyappeartohavedecided In 2022,Lietal.[27]introducedAlphaCode,asystemforthat benefitsoutweighanynecessaryhumanfiltrationeffort, code generationthatcreatesnovelsolutionstocompetitivewith enthusiasticlevelsandratesofadoptionalreadybeing programming problems. They found that three key componentsreported. OnceLLM-basedcodecompletionisfullyadopted, were criticaltoachievingreliableperformance:there areexpectations thatprogrammerswillspendmoretime 1) Anextensive programming dataset for training and eval-reviewing ratherthanwritingcode[41]. uation. A. CodeGenerationModels2) Largeandefficient-to-sampletransformer-basedarchi- tectures.Automated codegenerationhasalonghistory,tracingits 3) Large-scalemodel sampling to explore the search space,origins backtoearlyvisionsofautomatedprogramsynthesis followed bybehaviour-basedfiltering.[42], whichhavecontinuedtodevelopandhavegenerated impressive results[43].In simulatedevaluationsonprogrammingcompetitionson From the pioneering work of Hindle et al. on the naturalnessthe Codeforcesplatform,AlphaCodeachieved,onaverage,a of software[44],weknowthatprogrammerswritecode(andranking ofthetop54%incompetitionswithmorethan5,000 languages enforcecodewritingstyles),thatmake codehighlyparticipants. Several papersalsointroducedcodesynthesisLLMs[50]–predictable. Furthermore,Barretal.[45]foundthat43% basedondatasetswithlittlepre-filteringoftheof commitstoalargerepositoryofJavaprojectscouldbe reconstituted from existing code. They called this ‘The Plastictraining data. However, in 2023, Gunasekar et al. [54] reported trainingwithonlyatextbook-qualitycodecorpus,Surgery Hypothesis’becauseofthewayautomatedrepairthat, by LLMs with lower parameter counts could achieve performanceproceeds byscavengingforexistingcodetopatchupissues comparable tomuchlargermodels.elsewhere [46].

6


---

<!-- Página 7 -->

They classifiedanexistingPythoncodecorpuswiththeHybrid approacheshavealsousedsoftwareengi- GPT-4model,bypromptingittodeterminetheeducationalneering and/or AI techniques to select the best candidate from value ofthegivencodeforastudentwhowantstolearnan LLM’s top-n outputs. For example, Chen et al. [71] use test programming. Second,theyusedGPT-3.5 tocreatesyntheticgeneration tochoosecandidatesandreportedimprovement of textbooks aboutPython.Specificcodegenerationusecasesapproximately 20% on five pre-trained LLMs; Inala et al. [72] have alsobeentackled,suchasnumericalalgorithmcodeuse aneuralnetwork-basedrankertopredictcodecorrectness generation [55],andofcodefrombehaviouraland potentialfaults.Jainetal.[73]proposedJigsaw,which descriptions [56].MoreexamplesoftheexistingLLMsforpost-processes thegeneratedcodebasedonprogramanalysis code generationandthecodeleaderboardcanbeand synthesistechniques. Dong etal.[74]treatedLLMsasagents,lettingmultiplefound inTable IIandFigure4. LLMs playdistinctrolesinaddressingcodegenerationtasksB. PromptEngineeringforImproved CodeGeneration collaboratively andinteractively. Theyreportedimprovements Prompt engineeringhasbeenextensivelyusedasawayto of approximately30%-47%. improve codegeneration.Forexample,Lietal.[57]reported EvaluationofLLM-basedCodeGenerationpass@1 improvementsofbetweenapproximately50%and D. Scientific 80% on CodeX, CodeGeeX, CodeGen, and InCoder on severalThere isapressingneedformorethoroughscientific benchmarks (MBPPforPython,MBJPforJava,andMBJSPevaluation. Manyauthorshaveanecdotallyreportedoncases for JavaScript).D oderlein etal.[58]reportedtheprompt-where LLMsfailedtogeneratecorrect,secure,andreliable engineered improvementofCopilotandCodeXsuccessratescode. Poldrack et al. [75] also highlight the need for substantial from approximately1/4to3/4onHumanEvalandLeetCode.human validation.Inthissection,wesurveytheliteratureon He andVechev [59]usedpromptengineeringtoimprovethethe empiricalevaluationofLLM-basedcodegenerationin security ofLLM-generatedcode,reportinganimprovementterms ofcorrectness,robustness,explainability,determinism, in securityfrom59%(ofcasesconsidered)to92%.Whiteand security. et al.[60]providedacatalogueofpromptengineeringdesign1) CorrectnessEvaluation:The GPT-4TechnicalRe- patterns for various software engineering tasks, including codeport [28] evaluated the correctness of GPT-4’s code generation generation. Dennyetal.[61]arguedthatpromptengineeringon theHumanEvaldataset,reportingazero-shotaccuracyof is ausefullearningactivitythatfosterssoftwareengineering67%, amodestimprovement onthe(earlierChatGPT)results students’ computationalthinking.reported byYetistiren etal.[76]. Other authorshaveconsideredwaystodecomposepromptBorji [77]presentedarigorous,categorisedandsystematic engineering intoiterativeandmultiphaseconversationswithanalysis of LLM code generation failures for ChatGPT. Eleven the LLM,movingitclosertoChainofThoughtreasoning.categories offailures,includingreasoning,factualerrors, For example,Lietal.[62],[63]reportedan18%increaseinmathematics, coding,andbias,arepresentedanddiscussed ChatGPT Pass@1usingatwo-stagesketch-basedapproach,in theirwork. SkCoder, inwhichtheLLMfirstcreatesasketchandthenFigure 4showstheleaderboardofcodegenerationcorrect- subsequently implementsthesesketches. Jianget.al.[64]andness in terms of the pass@1 (i.e., the test pass rate for the top-1 Zhang et al. [65] also sought to deploy Chain-of-Thought-stylecode candidate) on the HumanEval dataset according to Papers reasoning bypromptingLLMstoreflectandself-edit.With Code, a platform that highlights trending AI research and Existing softwareengineeringanalysistechniquescanalso4the codebehindthemethodandmodels.The LLMmodels provide additionalinformationforfine-tuningandpromptbehind eachmethodareshowninbrackets.Atthetimeof engineering. For example, Ahmed et al. [66] show how simplewriting, thebestcodegenerationmodel,Reflexion[78],can static analysiscanbeusedintheprompttoimprovethegenerate correctcodeforover90%ofthegenerationtasks. performance ofcodegenerationwithfew-shotlearning.However,thesenumbersandtherelative rankingsofdifferent Shin etal.[67]comparedpromptengineeringandfinelanguage modelsareinherentlysubjecttochangeinsucha tuning withGPT-4forcodegenerationtasks,demonstratingrapidly developingfield.Forexample,thefiguregivenfor that fine-tuningworksbetterthanpromptengineering.correct code on HumanEval in the original GPT-4 Report [28] C. HybridsofLLMsandotherTechniqueswas only67%,sotheupdatedfigureof80%(atthetimeof writing, whichisfive monthslater)retrieved fromthePapers-Throughout oursurveyoftheliterature,wefoundstrong With-Code websitepresumablyrepresentstheevolutionofevidence thatsomeofthemostpromisingresultscanbe GPT4 sincethen.achieved by hybridising; combining LLMs with other existing Despite thepromisingresultsintheliteratureoncodesoftware engineering techniques. This section surveys work on generation andcompletion,Dinetal.[79]reportedthatthehybrid LLMsforcodegeneration. performance ofcodecompletiondroppedbymorethan50%Several authors have developed hybrids of LLMs combined on HumanEvalwhenthecontextcontainsbugs.with planningandsearch.Forexample,Zhangetal.[68], [69] reported improvements over baselines of between approx- 4The imately 11% and 27%, while Zhang et al. [70] hybridized codecode-generation-on-humaneval/; generation withAPIsearchtechniques.2023.

7


---

<!-- Página 8 -->

Fig.

Mohammadkhani etal.[85]usedtheattentionmechanism2) RobustnessEvaluation:LLM codegenerationrobust- to studyCodeBERT andGraphCodeBERT ontasksincludingness is the degree to which similar prompts elicit semantically code documentationgeneration,coderefinement,andcodeand syntacticallysimilarcodegeneration.Treude[80]intro- duced GPTCOMPARE, a prototype tool for visually highlight-translation. 4) DeterminismEvaluation:LLMs arenondeterministic.ing similaritiesanddifferencesbetweenLLMcodeoutputs. Ouyang et al. [10] empirically studied the non-determinism ofYanetal.[81]introducedCOCOtotesttherobustnessand ChatGPT incodegeneration,foundingthatover 60%oftasksconsistency ofLLM-basedcodegenerationsystems. had zeroequaltestoutputacrossdifferent requests.Neverthe-3) ExplainabilityEvaluation:One considerableadvantage less, their study of the literature in LLM-based code generationof LLMs,overpreviousmachinelearningtechniques,isthe demonstrate that only 21.1% of these papers consider the non-way inwhichthecodegenerationartefactsareaccompa- determinism threatintheirexperiments.nied byexplanations.Suchexplanationshavethepotential 5) SecurityEvaluation:Hajipour et al. [86] proposed a few-to increaseadoption,byprovidingadditionalconfidenceand shot promptingapproachtodetectingsecurityvulnerabilities,faster understanding.Moreworkisneededtoevaluateand reporting thattheirapproachautomaticallyfindsthousandsofoptimise explanationsthataccompanygeneratedcodeand 3 D V V #   I R U  F R G H  J H Q H U D W L R Q  R Q  + X P D Q ( Y D Osecurity vulnerabilitiesinseveralmodels.Khouryetal.[87]other softwareengineeringartefacts. found thatthecodegeneratedbyChatGPToftenfellway / / 0  E D V H G  F R G H  J H Q H U D W L R Q  P H W K R GInitial evaluation byMacNeiletal.[82]ontheirinteractive below evenminimalstandardsofsecurecoding.Risseand        Webdevelopment e-book, suggested  a majority  of students B ome [88]reportedresultsthatindicatedvulnerabilityde- perceived LLM-generatedcodeexplanationstobehelpful. tection accuracymaybeover-reported,duetothemodel Noever andWilliams[83]alsoshowedthepotentialfor / D 0 ' $     % overfitting tounrelatedtrainingsetfeatures. explanations to help human engineers, particularly where code In addition, Yetistiren et al. [76] presented a comprehensive / / D 0 $    % is obfuscatedorlackssufficientexistingdocumentation.In evaluation of the performance of Copilot, CodeWhisperer, and this way,theabilitytoproduceinsightandexplanationmay & R G H [    % ChatGPT,coveringdifferentaspectsincludingcodevalidity, go beyondsimplyjustifyingthecodegeneratedbytheLLM code correctness,codesecurity,codereliability,andTheir & R G H 7      % itself, butmaybecomeavaluablesourceofeducationand results showawidedegreeofdivergenceinperformance, documentation (SeeSectionXI). & R G H * H Qmotivating theneed forfurtherresearch andinvestigation. For Sun etal.[84]focusonusers’explainability needsforgen-example, theyfound65%,46%,and31%oftheprograms , Q V W U X F W & R G H 7     %  erative AIinthreesoftwareengineeringusecases:codegen-generated byChatGPT, Copilot,andCodeWhisperer(respec- eration basedonnaturallanguagedescription(withCopilot), * 3 7      ] H U R  V K R Wtively) werecorrect. translation betweendifferentprogramminglanguages(with6) Benchmarks:As withotherscientificevaluations,soft- S K L       %Transcoder), andcodeautocompletion(withCopilot).Theirware engineeringevaluationreliesonpubliclyavailableand investigationwasconductedas9workshopswith43software : L ] D U G & R G H Urepresentative benchmarksuites.Anumberofthesehave engineers andidentified11categoriesofexplainabilityneedsalready emergedandcansupportsoftwareengineeringevalu- & R G H  / O D P D    X Q Q D W X U D O in thecontextofGenerativeAI(GenAI)forcode.Italsoation of LLM-based applications. The Papers-With-Code plat- proposed 4 types of features for generative AI: AI documenta-5 & 2 ' (  7    F R G H  G D Y L Q F L     formprovides asummaryof15benchmarksforevaluating tion, model uncertainty, attention distribution, and social trans-code generation. * 3 7   parency (i.e.,makingvisiblethesocio-organizationalfactors 5[https://paperswithcode.com/task/code-generation](https://paperswithcode.com/task/code-generation)that governtheuseofAI). 0 H W D * 3 7

 3 D U V H O    * 3 7    & R G H 7 

8 5 H I O H [ L R Q    * 3 7   

           


---

<!-- Página 9 -->

Evaluations haveoftenreliedonsmallprogrammingprob-For example,transferlearninghasbeenproposedasaway lems fromprogrammingcourses[89],syntheticallygeneratedto improvecodecompletionperformancewhenthevolume problem sets[90],andonlinejudgingplatformssuchasof trainingexamplesforaspecificprogramminglanguageis Leetcode [29],[65],[91].Althoughresultsreportednaturallyinadequate [96]. vary byLLMintrainingsets,theoverall conclusionsoftheseThe currentfocusofresearchisonthecodeproducedby evaluations indicatesuccessratesofbetween20%and80%.LLMs. However,theexplanationsproducedbyLLMsmay Nevertheless, existingcodegenerationbenchmarkstendto turn outtobeatleastasimportant.Onecouldimaginemany rely ontestsuitestoautomaticallyjudgecodecorrectness,scenarios inwhichanengineerwouldprefertoaccepta which canbeinadequate,leadingtofalsejudgements[92].(possibly) suboptimal software engineering artefact that comes This highlightstheneedformoreworkonevaluationbench-with acompellingexplanation,overapotentiallymoreper- marks thatarespecificallytailoredtoLLM-basedcodegener-formant solution with a less compelling explanation. After all, ation evaluation. Liuet al.[93]draw attentionto theproblem,engineers regularly make thesamejudgementcallforhuman- showing howexistingtestsuitescanleadtohighdegreesdesigned engineeringartefacts,sowhywouldweexpectitto of falsepositiveconclusions(alsoaseriousproblemforbe anydifferentforthoseproducedbymachines?Aswith online judgeplatforms[92]).Toalleviatethisproblem,theyprompt engineering,whichfocusesonoptimisingtheinputto propose EvalPlus–acodesynthesisbenchmarkingframe-the LLM,explanationengineeringisalsolikelytobecomean work thatautomaticallygeneratestestinputsandrigorouslyarea ofstudyinitsownright. evaluates thefunctionalcorrectnessofLLM-generatedcode. V.SOFTWARET ESTINGTheir evaluationof14popularLLMs(includingGPT-4and ChatGPT) demonstrated that with the newly generated tests for Software testingisawell-establishedresearchdiscipline, HumanEval, theassessmentofpass@kdropsbyupto15%, the origins of which can be traced back to Turing’s pioneering averaged overproblemsconsidered. work in the late 1940s [97]. Much of the focus of this research Jimenez etal.[94]introducedSWE-benchwiththeaimof has beenontheautomatedgenerationoftestsuites,ableto evaluating LLMsoncodegenerationproblemsinarealistic achieve highfaultrevelationpotentialatlowcomputational software engineeringsetting.SWE-benchcontains2,294soft- cost [3]–[5].Thisprovidesuswith,notonlytechniquesable ware engineeringproblems,drawnfromrealGitHubissues. to weedoutincorrectLLM-generatedcode,butalsoamature The resultssuggestthatClaude2andGPT-4 solveonly4.8% baseline againstwhichtocomparenovelLLM-basedand and 1.7%ofthecodingtasks,respectively. hybrid techniquesfortestsuitegeneration. There is already a sufficiently large body of work to warrantE. OpenProblemsinCodeGenerationandCompletion a surveyspecificallyonLLM-basedSoftwareTesting:WangAssessing the generated code remains a critical problem for et al.[98]presentedasurveyofpapersprimarilyontesting,LLM-based code generation and completion: while much work but alsoincludingdebuggingandrepair.Theyreportedonalready started applying existing software testing knowledge to 52 papers(33publishedsince2022)ofwhichapproximatelythis problem, we expect closer integration of automated testing one-third concernedtest-basedLLMfine-tuning,whilethetechniques withcodegenerationandcompletiontechniques. remainder relieduponpromptengineering.Fortunately,thereisalargebodyofexistingworkon automated testdatageneration[3]–[5],muchofwhichwill A. GeneratingNewTests UsingLLMs have animportantroletoplayinensuringthecorrectness In thissection,wereviewexistingworkonLLMsforof theengineeringartefactsgeneratedbyLLMs.Arecurring test datageneration,beforehighlightingopenproblemsandtheme ofthechallengescoveredinthispaper,isthatcode challenges forthedevelopmentofthisemergingfield.Theexecution provides precisely the ‘ground truth’ needed to filter generated may not be executable because the LLM is nothallucinated responses. It can also provide guidance as part of guaranteed togeneratecompilablecode.Nieetal.[99]reportinteractive reasoning/action (‘ReAct’) dialogue [95], both with 29% of tests generated using TeCo are executable, while Yuanand withinLLMs. et al.[100]foundthatapproximatelyone-quarterofthetestsAutomated test data generation allows the software engineer generated byChatGPTwereexecutable,risingtoone-thirdto targettheexplorationofthemostrelevantregionsof with suitablepromptengineering.this run-timegroundtruth.Thistest-basedtargetingcanhelp filter, fine-tuneandtooptimiseprompts,therebyminimisingOf thoseteststhatdocompile,severalauthorshavere- problems posed by hallucination. LLMs also have considerableported onthecodecoverageachieved.Forexample,Bareiß potential forautomatingtheprocessofconstructingeffectiveet al.[101]reportedanincreasefromthe10%achieved using and efficientsoftwaretestsuites.Randoop [102]to14%withCodeX.Hashtroudietal.[103] Another importantproblemishowtoefficientlyfine-tunereported a50%increaseinlinecoveragefortheteststhey pre-trained LLMssothattheyperformbetterforaspecificgenerated by fune-tuning CodeT5. Siddiq et al. [104] reported programming language, codebase, or domain: this is especially80% coverageontheHumanEvaldatasetusingCodeX,but important becausetraininganLLMfromscratchrequiresalso foundthatneitherthestudiedLLMscouldachievemore significant computationalresources.than 2%coverageontheEvoSuiteSF110dataset.

9


---

<!-- Página 10 -->

Hybrid approaches that combine existing test generation andFeng andChen[114]demonstratedareplicabilityrateof evaluation techniques,suchasfuzz-basedtestingandsearch-80% onbugreportswithnatural-language-definedstepsto based testing,withLLMshavealreadydemonstratedpromis-reproduce, usinganLLMoutofthebox(ChatGPT)with ing results.Forexample,Lemieuxetal.[105]introducedChain ofThoughtpromptengineeringalone. CODAMOSA, an algorithm that combines Search-Based Soft-Several authorshave consideredpromptengineeringtoim- ware Testing (SBST) [5] and CodeX to generate high-coverageprove theresultsoftestgeneration[115],[116].Forexample, test casesforprogramsundertest.WhenSBST’scoverageSchafer etal.[116]proposedTESTPILOT, whichre-prompts improvements stall,CODAMOSAasksCodeXtoprovidewith failingtestsandassociatederrormessages,achieving example testcasesforunder-coveredfunctions.Thishelpsreported averagestatementcoverageof68%.Xieetal.[117] SBST redirectitssearchtomoreusefulareasofthecreate promptsfortestgenerationbyparsingtheprojectand space. Inanevaluationof486benchmarks,CODAMOSAcreating anadaptivefocalcontextthatincludesthe achieved significantlyhighercoveragecomparedtoSBSTmethod anditsdependencies.Theyfurtherusedrule-based and LLM-onlybaselines.Huetal.[106]introducedChat-repair tofixsyntacticandsimplecompileerrorsinthetests. Fuzz, whichaugmentsthewidelystudiedfuzzer,AFL,withAlthough theoutcomesofLLM-basedtestingmaybeun- ChatGPT,inordertogetmoreformat-conformingmutants.certain, researchershaveexploredcrossreferenceormajority In anevaluationof12targetprogramschosenfromthreeof votes[118],[119]methodstoestimatetheconfidenceof benchmarks, ChatFuzzachievedhigherbranchcoveragethanLLMs, basedonthenotionof‘self-consistency’[120].For AFL by13%.Dakheletal.[107]usedmutationtestingtoexample, theLibrointroducedbyKangetal.[113]uses help LLMstogeneratetests.Inparticular,theyaugmentedCodeX togeneratetestsfrombugreportsthatcanreproduce prompts forCodexandLlama-2-chatwithsurvivingmutants.failures. Ifmultipletestsshowsimilarfailurebehavior, Libro They reportthattheirapproachdetects28%morehuman-estimates thatLLMis“confident”initspredictions.Further- written faults. Xia et al. [108] recently demonstrate that LLMsmore, wherethereispartialoracleinformation,thiscanalso can serveasauniversalfuzzerforsystemsacrossdifferentbe usedtoaugmentconfidenceestimates.Suchpartialoracle application domainsandprogramminglanguages,includinginformation isoftenavailablewhenthegoaloftheoverall C/C++ compilers,JDK,SMTsolvers,andevenquantumprocesses toimproveonexistingcode.Forexample,when computing systems.improving theefficiency ofanexistingtest,automatedpartial Deng etal.[109]proposeTitanFuzz,whichusesLLMsoracle informationcanbegatheredfromobservingwhether (i.e., Codex)togeneratevalidinputDLprogramstotestDLthe testbehavessimilarlytotheoriginal(passingandfailing libraries. TheresultsonPyTorchandTensorFlow revealthatin thesamesituations),andisalsofastertoexecute. TitanFuzz canachieve30%/51%highercodecoveragethan state-of-the-art fuzzers.Lateron,theyfurtherintroducedFuz- zGPT [110],whichsynthesizesunusualprogramsforfuzzingB. TestAdequacyEvaluation DL libraries. Their results indicated that CodeX and CodeGen Testeffectivenessistypicallymeasuredintermsof‘ade-could outperform TitanFuzz on PyTorch and TensorFlow when quacy criteria’[121],[122].Sincetestingcannotexhaustivelyre-targeted forfuzz-basedtesting. explore everypossibility, adequacycriteriaprovideaformofLi etal.[111]usedahybridofdifferentialtestingand lower boundontheeffectiveness achieved byasuiteoftests.ChatGPT toelevatethelatter’sabilitytogeneratefailure- Mutation testingisawidely-studiedtechniqueforassessinginducing testcasesofbuggyprograms.Theyreportatest the adequacyofsoftwaretestsuites[123],[124],inwhicheffectivenessimprovementfrom29%to78%. synthetic faults(called‘mutants’),aredeliberatelyinjectedA promisingareaforLLM-basedtestgenerationisGUI in ordertoassesstestadequacy.Mutationtestinghasbeentesting, becausethemanipulationoftheapplicationstatevia shown toprovidemorestringentadequacycriteriathanotherGUI oftenrequiresasemanticunderstandingofboththeuser structural coverage-based criteria such as statement and branchinterface aswellastheapplicationdomain.Sunetal.[112] coverage [125].described userinterfaceviatext,andaskedChatGPTwhich action itwouldliketoperformnextbasedonthetext,thenOne ofthechallengingopenproblemsformutationtesting convertthe answer into actual GUI interaction. This resulted is togeneratemutantsthatfaithfullymodelimportantclasses 32% higheractivity coverage comparedtothestate-of-the-art.of real-worldfaults.Khanfiretal.[126]usedCodeBertto One particularlyimportantproblemthatischallengingforgenerate developer-like mutantsandfoundthattheirapproach classical techniquesistheconstructionoftestcasesfromuserhas better fault revelation ability than PiTest. Garg et al. [127] reports. Theuserreportsarewritteninnaturallanguage.Thisapplied CodeBERT togeneratemutantsthatfaithfully capture has presentedconsiderablechallengesforexistingtechniques,vulnerabilities. They evaluation found that 17% of the mutants but isideallysuitedtoLLMs.Kangetal.[113]introducedfail theteststhatarefailedby89%oftherespectivevulner- Libro, afew-shotlearningfailurereproductiontechniquethatabilities. Brownlee[128]usedGPT-3.5togeneratemutants automatically generatestestsfromgeneralbugreports,basedfor geneticimprovemntandobservedthatrandomlysampled on CodeX.Librosuccessfullyreproducedapproximatelyone LLM-based editscompiledandpassedunittestsmoreoften third ofthefailures.compared tostandardGIedits.

10


---

<!-- Página 11 -->

C. TestMinimisationTestaugmentationandregenerationcanexploitfew-shot learning and/orcanfine-tune(onanexistingsuiteoftestdataTestminimisationimprovestheefficiencyofsoftwaretest- and historicalfaults),togenerateaugmentedtestsuites.ing byremovingredundanttestcases.Panetal.[129]ap- More work is needed on LLMs for generating additional testplied CodeBERT, GraphCodeBERT, and UniXcoder to extract assertions that capture corner cases, historical faults, and likelyembeddings oftestcodetoconducttestminimisation.Their programmer errors,drawingonthetrainingdataavailable.approach achievesa0.84faultdetectionrateandrunsmuch Hybridization betweenLLMsandexistingautomatedtestfaster (26.73minutesonaverage)thanthebaseline. generation techniquesisalsoaproductivetheme[105]. 3) TestCorrectness:Traditional softwaretestgenerationD. TestOutputPrediction has sufferedfromtheOracleProblem[6],i.e.,theyare Liu et al. [130] proposed CodeExecutor, a pre-trained Trans- inhibited bythelackofanautomatedoraclethatdetermines former model, to predict the program’s whole execution trace. whether atestoutcomeiscorrect.TwocasespertaintoAI- The purposeistoimitatethereal-worldarbitraryprogram generated tests: execution behaviour. Their evaluation compares CodeExecutor 1)**The generated**testpassesonthecurrentrelease: Wewith CodeX,andshowsthatCodeExecutorsignificantlyout- might assumethatthefunctionalityiscorrectlytestedperforms Codexinexecutiontraceprediction(e.g.,76%vs. and thatthegeneratedtestthusactsasaregression test,13% outputaccuracyfortheTutorialdataset). against whichfuturechangescanbechecked. 2)**The generated**testfailsonthecurrentrelease: WeE. TestFlakiness need to know whether the assertion is wrong or A testisflakyifitcanpassonsomeoccasionsandfail the generatedtesthasfoundabug. on otherswithoutanyapparent(tester-controllable)change Both cases can have pernicious consequences when they arein theexecutioncontext.Testflakinessisoneofthemost not imbuedwithself-regulation.Atestcasethatpassesmaypressing andimpactfulproblemsthatinhibittesteffectiveness merely reflectcoincidentalcorrectness[137],[138].Worse, itin industry[131].LLMshavebeenusedtopredictflakiness might bethecasethatthecodeis,infact,(and thatwith highaccuracy (with73%F1score[132],[133]and97% the test is equally incorrect yet captures, and thereby enforces,accuracy [134]reported). the incorrectbehaviour).Insuchcases,thegenerationof the testwilltendtoinhibitfault remediation,byfailingonF.OpenproblemsinLLMsforSoftwareTesting future fixes.ThisproblemalsoaffectsLLM-generatedtest There aremany openproblemsinLLM-basedsoftware test cases, andmaybemoreperniciousincaseswheresuchtests data generation,mostofwhichliewellwithinthegraspof hallucinate oracleproperties,bakingintothegeneratedtests existing softwaretestingtechniques.Wecanthusexpectan these incorrectoracleassertions. exciting explosioninLLM-basedsoftwaretestgenerationin On the other hand, when a generated test case fails, this may the comingyears.Thissectionoutlinessomedirectionsfor indicate abug.Thisbugrevelationwoulddenotea‘win’for this researchagenda. LLM-based testing.However, shoulditturnoutthattheratio 1) PromptEngineering:There aremanyaspectsofagood of false positives to trueare high, then the cost (e.g., software testthatcouldbefavoured bysuitablepromptengi- in humanassessment)maymakethetechniqueimpractical, neering. For example, weneedtounderstandhow toengineer even whenitdoesreveal truepositive bugs [131].Morework prompts that is neededonself-assessmentofconfidence,self-checkingfor •Predict andreducegeneratedtestflakiness;correctness, consistency,androbustnessofgeneratedtests. •Reveal likelyfaults,forexampleviatrainingonhistoricWeneedtodeveloptechniquesforautomaticallyassessing, fault data;augmenting andfilteringrawoutcomesfromexecutionof •Optimise thebalancebetweenmockingandintegrationLLM-based tests,beforepresentingthe‘testsignal’tothe testing;developer. •Make realisticdatabuilders,mockobjects,parametersThe interaction between LLM hallucination and test correct- and inputs;ness isanimportanttopicinitsownright.SinceLLM-based •Predict teststhataremostlikelytoelicitthatcovercode generationisgenerallydrivenbywhatismostlikely, corner cases;rather thanwhatismostcorrect,hallucinationposesthreats •Tailortestgenerationtofocusbehaviour thatisprevalentto anyquestionsofcorrectness.However, interestingly,Feldt in production.et al.[139]reportedacaseofhallucinationbeinghelpfulfor 2) AugmentingExistingTests:WorkonLLM-basedtestsoftware testing,becauseitmayreveal discrepanciesbetween generation hasfocusedontheautomatedofnovelthe actual program semantics and the programmer’s perception test suites. However, given the array of existing test generationof thesemantics.Theysuggestedaformofconversational techniques, there remains an important (and comparatively lesstesting agents(i.e.,anygeneratedtestsarefilteredbythe well-studied) openproblemofaugmentationandregenerationprogrammer viatheconversation)toharnessthiscapability based onexistingtestsuites[135],[136].without posinganythreatstooveralltestcorrectness.

11


---

<!-- Página 12 -->

More workisalsorequiredonthescientificfoundationson Much oftheworkonautomatedrepairhasusedthe which evaluationsofLLM-basedsoftwaretestingrest.Moregenerate-and-test approachwidelyadoptedinthefieldof care and attention are clearly needed to heed the ‘best practice’Genetic ImprovementandreadilyapplicabletoLLM-based advice forthescientificanalysisandreportingfromprevioustechniques. As a result, LLMs are certain to have a positive im- work onfoundationsofEmpiricalandSearchBasedSoftwarepact onautomatedsoftwarerepair,butthereremaintechnical Engineering [11],[13],[14].challenges intamingthehallucinationproblemandmanaging aswereportinthissection.4) MutationTesting:More workisneededtoexplorethe scalability, In ordertoachievescalability,allgenerate-and-testap-adequacy achievable with LLM-based test generation, and also proaches needtoaddressthebuild timeproblem[149].LLM-to useLLM-basedtechniquestosupportandenhancetest isnoexception;thepropensitytohallucinateadequacy investigationandassessment.LLMscanbefine-based repair makes itallthemoreimportantthatthetestphasecantuned onafaultmodel,andtherebyusedtosuggestmutants be executedregularly.ItislikelythatusingReActdeploy-that arehighlycoupledtorealfaults,andcanthusbeusedto ment models[95]willhelptofindefficientandeffectiveassess testadequacy. engineering trade-offs.WhenReActisappliedtorepair,the VI. MAINTENANCE, E VOLUTIOND EPLOYMENToverall approachwouldalternatebetweenthe‘Reason’phase (generating candidate fixes) and the ‘Action’ phase (evaluatingSoftware maintenanceandevolutionhavebeenimportant fixes throughtesting,whichinvolves thebuildproblem).topics ofstudyformanydecades.Theyareconcernedwith Toaddressthisissue,wecanrefertothewell-establishedexisting codebasesfromwhichweseekunderstandingand literature on software repair [46], [150], grounded in over twobusiness logicextraction,andforwhichweseektore- decades ofthedevelopmentofsearch-basedapproachestoengineer, repairandrefactor.Maintenanceproblems,suchas software engineering[12],[151].Thisliteratureprovidesthethese, allresidewithinlanguage-richproblemdomains.Itis research communitywithafirmfoundationofexperience andtherefore unsurprisingthatthisareafindsmanyapplications expertise, makingitverywell-placedtodevelopof LLM-basedtechniques,aswereview inthissection. generate-and-test approachestotheproblem. A. DebuggingRecent workonrepairhasstartedtouseneuralAImodels, Kang et al. [140] studied GPT-3.5’s fault localisation ability,such as the seminal work of Tufano et al. [152]. More recently, and foundthatLLMcouldoftenidentifythefaultymethodsince 2022,therehasbeenarapiddevelopmentofemergent on thefirsttry.Wuetal.[141]presentacomprehensiveembryonic researchliteratureonLLM-basedrepair.Forex- investigationinto the capability of GPT-3.5 and GPT-4 for faultample, Xiaetal.[153]proposedAlphaRepair.Itredefines localisation accuracy, stability, andexplainability. Theresultsthe APRproblemasacloze(orinfilling)task,wherethe demonstrate that GPT-4 achieves 47% higher fault localisationLLMs areleveragedtodirectlyfill-incorrectcodebasedon accuracy over the state-of-the-art, but the performance declinesthe bi-directional context of the potential buggy code portions. dramatically withalongercodecontext.AlphaRepair also demonstrates for the first time that LLMs can outperform allpriorAPRtechniques.Feng andChen[142]proposedAdbGPT, whichreproduces They furtherconductedanempiricalstudy[154]onnineAndroid bugsfrombugreportsthroughpromptengineering LLMs acrossfivedatasetsinthreedifferentlanguages.Theirwith ChatGPT.Withadatasetof88bugreports,AdbGPT findings notonlyaffirmed thesuperiorityofLLM-basedAPRwas abletosuccessfullyreproduce81%,outperformingthe (especially the cloze-style approach) but also offered a numberbaselines andablations.Joshietal.[143]focusedonmul- of practicalguidelines.Weietal.[155]synthesizeapatchtilingual debuggingandproposedRING,whichproposesa interactionbetweenanLLMandaCompletionprompt-based strategythatconceptualizesrepairaslocaliza-through the Engine, andfoundthattheapproachsurpassesthebest-tion, transformation,andcandidateranking. performing baselineby14and16bugsfixed.Toaddressthedataleakeagethreatinfaultlocalisationand Program repairnaturallyfitsaconversationalmodelofprogram repair,Wuetal.[144]introducedConDefectswith prompt engineering.Xiaetal.[156]proposedconversational1,254 Javabugsand1,625Pythonbugsthatwereproduced APR, whichalternatespatchgenerationandvali-between October2021andSeptember2023.Researchers dation inaconversationalmanner.Theirevaluationontenare allowedtoselectcodesamplesbasedontheircreation LLMs demonstrated that their approach has superiority in bothperiod, therebyallowingthemtoevaluate theeffectiveness of andefficiency.different LLMs according to their training data cut-off date. In proposedChatRepair[157],showingthataddition, therehasbeenworkonpredictingbugseverity with They further the conversationalapproachfixes162outof337bugsforLLMs [145]. only $0.42perbug,therebyalsoaddressingpotentialcon- B. ProgramRepaircerns aboutthecomputationalresourcesrequired.Chenet Repairing bugs hasbeenatopicofmuchinterestforovera [158]al.introducedSELF-DEBUGGING,whichteachesan decade in the software engineering research community [146],LLM to debug its predicted code via few-shot learning, SELF- [147], andhasalreadyfounditswayintoinitialindustrialDEBUGGING reportsbaselineaccuracyimprovementsofup deployment [148].to 12%.

12


---

<!-- Página 13 -->

Studies havealsoreportedresultsforparticularclassesofC. PerformanceImprovement bugs, forexample,Pearceetal.[159]reportedrepairresults Since theinceptionofcomputerprogramming,thefrom fivecommercialLLMsonsecuritybugs,Charalambous paramount importanceofperformanceoptimisationhasbeenet al.[160]combinedChatGPTwithwithformalverification recognised. Indeed,performanceoptimisationisevenmen-strategies toverifyandautomaticallyrepairsoftwarevulner- tioned byAdaLovelaceinhernineteenth-centurynotesonabilities. Caoetal.[161]reportChatGPTresultsforDeep the analyticalengine[170].MuchinitialpracticaldeploymentLearning (DL)programrepair. of optimisationtookplaceincompilerdevelopment,through Repair doesnotalwaysstartwithanexistingfailingtestwork onoptimisingcompilers[171].Thisisthebedrockon case, butcanstartwithanaturallanguagedescriptionofawhich current practical and efficient computation rests, but it is failure inproduction.Automationopensthedoortofasternecessarily aone-size-fits-allapproach;widelyapplicabledue responses touser-generatedbugreports.Thisisaroutetoto itsgenerality, yetsuboptimalforbespoke problemdomains repair thathasalsobeenexploredforLLMsintheworkoffor thesamereason.Therehas,therefore,alsobeenmuch Fakhoury et al. [162], who generated functionally correct codework onspecificsource-to-sourcetransformationstoimprove edits fromnaturallanguageissuedescriptions.Theyproposeoptimisation, datingbacktothe1970s[172],[173]. Defects4J-Nl2fix, adatasetof283JavaprogramsfromtheFor alongtime,thefocusofthisworkwasonfinding Defects4J dataset with high-level descriptions of bug fixes. Thesuitable setsofmeaning-preservingtransformations,themoti- state-of-the-art LLMs evaluated on this benchmark achieve upvation beingthatacorrectprogramcanbetransformedintoa to 21%Top-1 and36%Top-5 accuracy.more efficient version of itself,while retaining itscorrectness. However,morerecently,researchonprogramsynthesistookAutomated repaircanalsoreducetheburdenonengineers, a differentturn:InspiredbyGeneticProgramming[174],andmanaging DevOps-styleon-callforproductionsystems.For early resultsfromAutomatedProgramRepair[146],[175],itexample, Ahmedetal.[163]studiedtheuseofLLM-based considered awidersetoftransformationsinanapproachthatroot causing and remediation of 40,000 incidents on Microsoft has cometobeknownas‘GeneticImprovement’[8],[176].cloud services.TheauthorsevaluatedmultipleLLMsusing The widersetoftransformationsmayproduceincorrectsemantic and lexical metrics in zero-shot, fine-tuned, and mul- code, butautomatedtestingcanfilterthese,toensuresuffi-titask settings,showing thatfine-tuningsignificantlyimproves cient faithfulnesstotheintendedsemantics.Furthermore,theincident responseeffectiveness. freedom totreatexistingcodeasakindof‘geneticmaterial’ The abilitytoperformfine-tuningforaspecifictaskorproduced dramatic improvements in non-functional properties, domain cansignificantlyimprovethemodelperformanceinsuch as execution time, memory and power consumption (e.g., program repair.Jiangetal.[164]empiricallyevaluatedthe70x speedupofanon-trivialgenesequencingsystem[177]). performance of10differentCodeLanguageModels(CLMs) Although thepotentialforartificialintelligencetechniques, and 4faultbenchmarks,andshowedthatrepair-specificfine- such asevolutionaryalgorithms,toimproveperformancehas tuning couldsignificantlyimprovesuccessrates.Onaver- been well studied, researchers have only just begun to consider age, the10CLMsalreadysuccessfullyrepaired72%more the potential for LLM-based performance improvement. In the faults thanstate-of-the-artDL-basedAPRtechniques.After work byMadaanetal.[178],theauthorsuseCODEGEN fine-tuning, thenumberincreasedto160%.Jinetal.[165] and CodeXtosuggestfunctionallycorrect,Performance- proposed InferFix,whichcontainsaLLM(CodexCushman) Improving Edits(PIEs),improvingexecutiontimeofPython finetuned onsupervisedbug-fixdata.InferFixachievesa and C++(alreadypre-optimisedwiththemaximallyopti- 76% Top-1repairaccuracyonJava,andover65%onC# mising compileroption-O3 ). Similarly,Gargetal.[179] using theInferredBugsdataset.Berabietal.[166]introduced proposed DeepDev-PERF,aperformanceimprovementsug- TFix, aT5modelfine-tunedonbug-fixingdata,reporting gestion approachforC#applicationsthat.DeepDev-PERF that itoutperformedexistinglearning-basedapproaches.Xia took theEnglish-pretrainedBART-largemodelandfurther et al.[167]combinesLLMfine-tuningandpromptingto pretrained it on Source code. Kang and Yoo [180] proposed the automate theplasticsurgeryhypothesisanddemonstrated use ofLLMstosuggestobjective-specificmutationoperators that theirapproachfixes89and44bugs(outperformingthe for geneticimprovement,andprovideddemonstrationson baseline by15and8). improving efficiencyanddecreasingmemoryconsumption. Garg etal.[181]proposedRAPGen,whichgenerateszero-LLMs canalsohelptoexplainthepatchesthatthey shot prompts for LLMs to improve performance. Thegenerate. Kangetal.[168]proposedAutoSDtoprovide are generatedviaretrievingapromptinstructionfromapre-debugging explanationwithLLMstohelpdevelopersjudge constructed knowledge base of previous performance improve-the correctnessofpatches.They foundthatAutoSDproduced comparable resultstoexistingbaselineswithhigh-qualityments. Chenetal.[182]usedGPTmodelsasfor repair explanations.Sobania[169]studiedthecapabilityoftheir sourcecodeoptimisationmethod,Supersonic,andfound that Supersonicimprovesrunningtimefor26.0%oftheGPT 3.5inexplainingthepatchesgeneratedasearch-based programs, comparedtoonly12.0%forGPT-3.5-Turboandrepair tool,ARJA-e,on30bugsfromDefects4J.84%ofthe 4.0% forGPT-4.LLM explanationsarefoundtobecorrect.

13


---

<!-- Página 14 -->

## ÒCorrect by

Despite thesecorrectnesschallenges,inherentinLLM-Cummins etal.[183]focusedontheperformanceofcom- Based SE,thereisalargepooloftrainingdata,andLLMspilers andpresentedresultsonLLMsforoptimisingcompiler have a propensity to exhibit emergent behaviour. These obser-instructions. Theirresultsdemonstratethatarelativelysmall toyieldsurprisingresultsthat,althoughnot(7B-parameter) LLM,trainedtogenerateinstructioncountsvations combine guaranteed tobecorrect,canpotentiallydramaticallychangeand optimizedcompilerLLVMcode,cangenerate3%im- inusefulways.provements inreducingcompilerinstructioncounts,outper-performance characteristics Of course,asweincreasinglyallow morepermissive trans-forming thestate-of-the-art.Theirresultsarealsopromising formation palletsinthehopeofoptimisingmultiplenon-in termsofcorrectness,with91%compilableand70%func- functional properties,wesimultaneouslyplacefargreatertionally correctwrttheoriginalcompileroutput. reliance upontheabilityoftestingtoprovidereassurance of functionalfaithfulness.Testingisalsovitaltocheckfor regressions inthosenon-functionalpropertiesthatarenot targeted bytheimprovementprocess.Asaresult,software testing in general (and automated high coverage test generation in particular),willbecomeevermoreimportant.

D. CloneDetectionandRe-use There hasbeenmuchpreviousworkonmanagedsoftware reuse [184]inordertoextractvalueandavoidduplication, a topicalsotackledusingLLMs[185].Softwaretypically contains largenumbersofclones,arisingfromadhocre-use, resulting inmuchworkonautomatedclonedetection[186], a topicforwhichfuzz-basedfine-tunedLLMshave alsobeenFig. applied [187]. Over aperiodofsome50years,thesoftwareengineering E. Refactoring community hasevolveditsconceptionofwhatitmeans

## optimisation)

When we refactor code, we generally expect its behaviour toto transformanexistingsoftwaresystemintoanequivalent remain unchanged. This is particularly attractive for automatedsystem thatimprovesperformancewhileretainingfunctional

## (e.g., peephole

approaches (suchassearch-basedrefactoring[188])becausebehaviour.In the 1970s, the strongest concern was correctness, it meansthatwecansimplyrelyontheAutomatedRegres-so transformationpalettesweredefinedtoconsistsolelyof sion Oracle.This‘automatableoracleforfree’advantageistransformation stepsthatwere(functionally)correctbycon- significant andwillalsoapplytoLLM-basedrefactoring.

## ConstructionÓ

struction. Poldrack et al. [75] show that GPT-4 refactoring of existingHowever,by2010thecommunitywasalreadyexploring code can significantly improve code quality according to long-

## 2010s

the application of considerably more relaxed notions of equiv- established structuralmetricssuchasHalstead[189]andMc-alence thatmerelyretainsufficientoperationalfaithfulness

## 1970s

Cabe [190]complexity. NoeverandWilliams[83]emphasizeto thebehaviouroftheoriginal.Thetightsemanticstrait-

## ÒSyntactically CorrectÓ

## Transformations

## Transformations

the valueofAI-drivencodeassistantsinrefactoringlegacy

## (e.g., Neural Machine Translations,

jacket ofthe1970swastherebyconsiderablyrelaxed toallow

## (e.g., Genetic Improvements,

## Large Language Models)

code andsimplifyingtheexplanation orfunctionalityofhigh-

## Automated Program Repair)

transformations thatmightevenfailsome testcases.During value repositories.the same period, operational performance became increasingly important. Akey underlyingprincipleofthisresearchagendaF.OpenProblemsinMaintenanceandEvolution is thatnooverall software systemcanbedeemedfunctionallySince somanyofthesubdomainsofsoftwaremaintenance correct, whenitisexecuted onasysteminwhichinefficiencyand evolutionareconcernedwithexistinglegacysystem has left insufficient remaining resources. This principle appliessource code,wecanexpectrapidgrowthintheapplication even inthe(comparatively rare)caseswherethesoftwarehasof LLMs.Thissectionoutlinessomeexistingopenproblems been fully proven to be functionally correct. As the more pithyin thisnascentsub-areaofresearch. slogan hasit:1) OpenProblemsinPerformanceImprovement:Much “There isnothingcorrectaboutaflatbattery”[8].more work is needed on the development of LLM-based tech- This evolutionofthecommunity’s approachtocodetrans-niques forautomaticallyfindingperformanceimprovements. formation and synthesis is depicted in Figure 5 (red and yellowAs withGeneticImprovement,theseneednotbeconfined regions).merely toexecutiontime,butcanalsoconsiderothernon- In thecontextofthisincreasingrelaxationofsemanticfunctional attributessuchaspowerconsumption[191]–[193] constraints, wecanviewLLM-basedcodeoptimisationasamemoryfootprint[194]aswellasmulti-objective, trade- further developmentofthisoveralldirectionoftravel:Codeoffs betweensetsofnon-functionalproperties[195].We optimised byLLMsmaynotbeevensyntacticallycorrect, letexpect moreworkonGeneticImprovement-styleLLM-based alone semanticallycorrect(depictedbythegreenregionofcode optimisationtechniques,withthepotentialformany Figure 5).dramatic advancesandbreakthroughs.

14

## ÒUnconstrainedÓ

## 2020s


---

<!-- Página 15 -->

2) Open ing does can rely surprising that refactoring. In Design patterns software engineering for three decades [196]. LLMs may help engineers to refactor existing code to use design patterns, while providing developer-friendly explanations and Refactoring also nologies emerge. new API becomes available. Although they can be (sometimes automatically [197]) source of of refactoring for new APIs is less challenging than other code transformations, because Regression Oracle. Finally, enable more bespoke refactoring. The emergent work on LLM- based refactoring to well-known often have a third repetitive, tedious, tivities that implement these project-specific refactoring needs. The few-shot generalise from ‘bespoke’ refactoring. niques for

Most of focused on able potential Sun et summarisation of compared ChatGPT with NCS, CodeBERT, and CodeT5. They adopted three ROUGE-L. Surprisingly, performance is in terms Ahmed et summarisation on GPT-3.5, while Geng et al. [199] performed experiments on two Java language datasets, Funcom and TLC, using Codex: al. [200] ficient context from different

A. Open Summarization

Many existing code summarization techniques are retrieval- based: the a neural representation, which is subsequently used to retrieve the most

ProblemsinRefactoring:By definition,refactor-There isaclearlimitationtothisapproachduetothefact notchangesemantics,soLLM-basedrefactoringthat the set of summaries that can be generated are constrained ontheAutomatedRegressionOracle.Itisthereforeby thetrainingcorpus.LLMsmayenableautomatedcode thereisnotalreadymoreworkonLLM-basedsummarization thatisnotrestrictedtothistrainingcorpus, thissubsection,weoutlinepossibledirections.assisted bytheirnaturallanguageprocessingcapabilities. While thismayresultinricherandmoresemanticallyrele-haveplayedacriticalroleinpractical vant summaries,wealsonotethatexistingevaluation metrics are often lexical in nature, hindering our ability to compare and evaluate richersummariesgeneratedbyLLMs[198].Recentdocumentation. advances inReAct-basedapproaches[95]mayopenupotherbecomesnecessarywhenevernewtech- for greater assurance in the documentation generated,Forexample,whenanAPIisupdatedor avenuesa even whenitcannotbeexecuted. repaired,APImisuseremainsacommon VIII. SOFTWAREA NALYTICSR EPOSITORYM INING softwareengineeringbugs.Automatingtheprocess There isawell-establishedfieldofsoftwareanalytics;how to yieldinsightforhumanengineersfromexistingsoftwareofthepresenceoftheAutomated artefacts [201].Thelargeamountofsoftwareartefactinfor- mation publiclyavailableonlinehasstimulatedthegrowththefew-shotlearningcapabilitiesofLLMsmay of scientificinsightsgainedbyMiningSoftwareRepositories (MSR) [202],[203].WhileMSRtendstofocusonscientifichasfocusedonglobalaccording research insightsfromsuchmining,softwareanalyticstendsrefactoringpatterns.However,programmers to focus on opportunities for organisations to gain insight fromproject-specificrefactoringrequirements.Upto the analysisoftheirownrepositories,whichcanalsobenefitofsoftwareengineeringeffortisspentonlargely AI understandability[204].andpotentiallyerror-pronerefactoringac- Hitherto, inbothcases,muchofthecollection,curation and analysisofdatahasrelieduponlabour-intensivehumanlearningpotentialofLLMsmayautomatically analysis. WefoundnoworkontheuseofLLMstosupportspecificexamples,automatingwhatwecall this activity. Nevertheless,becausemanyLLMshavealreadyMoreworkisneededtodeveloptech- ingested this software artefact data, and are capable of provid-reliablefew-shot-learntbespokerefactorings. ing reasoningandinsight,itseemsnaturaltoexpectthemto play asignificantrole.VII. DOCUMENTATION For example,LLMsmayidentifyinterestingnewMSR theworkonLLM-basedsoftwareengineeringhas research questions,basedontheirabilitytoingestlarge thegenerationofcode,butthereisalsoconsider- amounts ofdata,includingresearchquestionsandhypotheses forLLM-baseddocumentationgeneration. that havepreviouslyprovedinterestingtoresearchers.They al.[198]exploredhowChatGPTperformsoncodemay alsoassistwithtraceability,whichsoftwareengineers Pythoncode.TheyusedCSN-Pythonandhave greatdifficultymaintaining[205],[206].

widely-usedmetrics:BLEU,METEOR,andIX. HUMANC OMPUTERI NTERACTION theresultsshowthatChatGPT’sFinding productiveinterfacesbetweenhumanengineers significantlyworsethanthebaselinemodelsand softwareinfrastructurehasremainedarecurringtheme ofBLEUandROUGE-L.throughout thelifetimeofthedevelopmentofsoftwareen- al.[66]conductedpromptengineeringforcodegineering [207],[208],datingbacktotheinceptionofthe discipline inthe1960s[209]. Wefoundevidenceofmanyinterestingresearchques- togeneratemultiple-intentcomments. Gentettions. Forexample,Vaithilingametal.[210]reportedon demonstratethatpre-trainedLLMsalreadyhave suf-the difficulties24participantshadinunderstanding,editing, togeneratemultipledifferentcodesummariesand debuggingtheCopilot-generatedcode,whileFeldtet technicalperspectives.al. [139] proposed a hierarchy of design architecture for LLM- based softwaretestingagents.Liangetal.[36]surveyed410 ProblemsinDocumentationGenerationandCodepractising software engineers, finding widespread use of LLMs to facilitatelow-levelprogrammingtasks,butalsoresistance to usingLLMsformoredesign-levelsoftwareengineering activities. Fengetal.[211]collected316Ktweetsand3.2Kgivencodeisrepresentedinavectorformatusing Reddit postsaboutChatGPT’scodegenerationtounderstand social media’s attitudestowardAI-assistedcodingtools.relevant textualsummarizationfromthecorpus.

15


---

<!-- Página 16 -->

They foundthatfearisthedominantemotionassociatedMore workisneededonnewformsofLLMs,specifi- with ChatGPT’scodegeneration,overshadowingotheremo-cally tailoredforsoftwareengineeringthattakeadvantageof tions suchashappinessandsurprise.Ahmadetal.[212]software’suniquepropertiesanddistinguishitfromnatural explore thewayinwhichanovicesoftwarearchitectcouldlanguage. Dynamicinformationisonesuchkeydifferentiator interact withChatGPT.currently missingfrommostofthework.We expectthenext generation ofSE-specificLLMstoaddressthis. X. SOFTWAREE NGINEERINGP ROCESS An importantaspectofbuilding andtrainingLLMsistheir Software engineeringconcerns,notonlysoftwareproducts,energy consumption.LLMcapabilitieshavebeenassociated but alsotheprocessbywhichtheyareconstructed[213].with theirsize[226],resultinginrapidgrowthofmodel Previous researchonsoftwareassistants[207],[214]–[217]size [227], [228]. The training and developing of larger models is clearlyofparticularrelevancetoLLM-basedsoftwaremay have direct environmental impact [229]. While it has been engineering, atopicsomeauthorshavealreadystartedtosuggested thatthemodelperformancedependsnotonlyon consider.Forexample,Rossetal.[218],introducedanLLM-model sizebutalsoonthevolumeoftrainingdata[230],the based programmers’assistant,evaluating itsdeploymentwithquestion of the right model size required to achieve the desired 42 participants while Tian et al. [219] highlighted the attentionperformance remainsunclear. span limitationsofChatGPT.Lighter modelsmayalsowidenadoption,therebyleading to enhanceddeployability.Recently,techniquessuchaslow-XI. SOFTWAREE NGINEERINGE DUCATION rank adaptation (lora) [231] and model quantization [232] have Teachershaveexpressedconcernatthedifficultiesof shown potential,buttheyremaintobeempiricallyevaluated identifying caseswherestudentshavereliedonLLMsto with respecttospecificapplications. construct theirassignments[220],whileotherauthorshave argued thatthelong-termimpactofLLMsoneducationwillB. TheNeedforDynamicAdaptivePromptEngineeringand be beneficial[221].However,ourpresentfocusrestsmoreParameterTuning narrowly onthespecificimpactofLLMsonthefieldof Initial workonpromptengineeringhasdemonstratedits software engineeringeducation, wherethecurrentliterature potential toconsiderablyimprovethesoftwareengineering focuses onLLM-basedtutorialsupport. artefacts generatedbyLLMs.However,asalreadyfound For example,Jaliletal.[222]exploredopportunitiesfor [58], theresultsarehighlyproblem-specific,soaone-size- (and issueswith)ChatGPTinsoftwaretestingeducation. fits-all approachisunrealistic.Furthermore,veryfewpapers Savelka et al. [223] analysed the effectiveness of three models report modelparametersettings,yetweknowthatmanyof in answeringmultiple-choicequestionsfromintroductoryand these, suchasthetemperaturesetting,playacrucialrolein intermediate programmingcoursesatthepostsecondarylevel. determining thenatureofthegeneratedLLMoutput. Several otherauthors[82],[83],[224]exploredthecapa- As an immediatestarting point,it isimperative thatauthors bilities ofCodeXforgeneratingprogrammingexercisesand make apointofconspicuouslyreportingtheseparameter code explanations. Theirgeneralfindingwas thatthemajority settings tosupportreplication.However,wealsoneedmore of thegeneratedcontentwasnovel,sensible,anduseful(see research ondynamicadaptivepromptengineeringandmodel also SectionIV-D3). parameter tuning.Thisresearchagendamaydrawinspiration XII. CROSSCUTTINGO PENR ESEARCHT OPICSfrom existingworkonparametertuningforotherdynamic adaptive tasks,suchasfuzzing[233].Dynamicpromptopti-A numberofpatternsemerge fromtheembryonicliterature misation mayalsoexploittechniquesassociatedwithSBSEon LLM-basedsoftwareengineering.Inthissection,weout- [12], reformulatingpromptoptimisationasamulti-objectiveline those that raise open research questions that cut across all computational searchprocess.software engineeringapplications

C. HybridisationA. BuildingandTuning LLMsforSE LLMs areseldommosteffectivewhenusedinisolation,Most ofthepreviousworkhastreatedLLMsasatomic but canbehighlyeffectiveaspartofanoverallSEprocess.components, with a focus on incorporating these in wider soft- More workisneededtounderstandthedesignpatternsforware engineeringworkflows.Whiletherehavebeenattempts SE workflowsintowhichLLMscansafely,efficientlyandto tailorthebehaviour, thesehavetendedtofocusonprompt effectivelyreside.WebelievethatexistingSEtheoryandengineering, withafewexamplesoffine-tuning. practice associatedwithgenerate-and-testapproaches,suchA morechallengingbutpotentiallyimpactfulproblemlies as AutomatedRepairandGeneticImprovement,arealreadyin trainingandfine-tuningmodels,specificallyforsoftware highly amenabletoLLMs.engineering tasks.Dingetal.[225]trainaBERT-like LLM with executioninputsanddynamictraces.TheyWeexpecttoseemuchmoreworkincorporatingLLMs show how this dynamic information improves (up to 25%) theinto these existing software engineering frameworks. However, more workisrequiredtotailorandextendtheseframeworks,accuracy ofthemodelfordownstreamsoftwareengineering to besttakeadvantageoftheopportunitiesofferedbyLLM-predictive tasks:vulnerabilityandclonedetectionandcover- based softwareengineering.age prediction(fullexecutionpathandbranchcoverage).

16


---

<!-- Página 17 -->

In particular, we expect to see a rapid development of workNevertheless, LLMshave theirown uniqueproperties,such as theabilitytoprovideexplanations,whichwillrequireon staticanddynamicanalysesforpromptengineeringand domain-specific theoreticalandempiricalscientificfounda-post-processing ofLLMresponses.Wealsoexpecttosee tions.hybrid softwareengineeringprocesses,adaptingContinuous Integration pipelinestoincorporateLLMs.LLMs inherentlyexhibitnon-deterministicbehaviour.Re- searchers need to carefully design their experiments, configure D. HarnessingHallucinationtheir LLMs (e.g., evaluating the effects of different distribution While hallucination has widely been regarded as a problem,sampling strategies),andtakeintoaccountnon-determinism as reportedinthissurvey,itmayalsoprovetoprovidewhen drawing their conclusions on LLMs. The SBSE literature benefits whenappliedtosoftwareengineeringdomains.LLMprovides advice on the inferential statistics required to support hallucinations are seldom entirelyrandom incorrect responses.such evaluation [13],[14]. Rather, becauseoftheirinherentstatisticalproperties,theyWewillwitnessarapidgrowth inthenumberanddiversity would bebettercharacterisedas‘plausiblefutures’,andthisof language models for software engineers in the coming years. may oftenmakethemusefulwhensetintherightcontext.Both practitionersandpractisingsoftware engineerswillneed Hallucination canberepurposedtoprovidepotentiallyuse-reliable, efficientandcomprehensivebenchmarkingsystems. ful suggestionsfor softwareenhancement.For example, when Benchmarking platformssuchasTESTPILOT [116]andplat- hallucinating atestcase,theLLMmayberepurposedtoforms suchasPapers With Code([https://paperswithcode.com/](https://paperswithcode.com/) suggest new features, while a hallucinated code summarisationsota/code-generation-on-humaneval/) willbecomeincreas- might indicatepotentialfor(human)codemisunderstanding;ingly important. if the LLM ‘misunderstood’ the code, might not a human alsoAs wellasgenericscientificfoundations,benchmarksand misunderstand it? When the LLM hallucinates an non-existentevaluation platforms,wealsoexpecttoseelongitudinalstud- API, itmayberepurposedasaway suggesttorefactoring toies ofdeveloperbehaviourwhenprogrammingwithLLM simplify orextendexistingAPIs.Moreworkisneededtoassistance, sothatwecanunderstandtheprogrammer-LLM exploit thispositive potential,andtoharnesshallucinationforinteraction better and design more effective use case scenarios. software improvement. F.ThoroughTesting E. Robust,Reliable,andStableEvaluationThe problemofhallucinationhasalreadybeenwidely Hort et al. [234] conducted a review of 293 papers on LLMsstudied. Itwillcontinuetobeatopicofgreatinterest,both for code generation, to determine the degree to which sufficientwithin thesoftwareengineeringcommunityandinthewider information was shared to support replication. They found thatcomputer sciencecommunity. Whileitislikely greatprogress only 33% shared source code and 27%trained artefacts.will bemade,theinherentriskofhallucinationisunlikelyto They alsoevaluated thepapersfromtheperspective ofenergybe completelyeradicated,sinceitisasgermanetotheLLM consumption, assessingthedegreetowhichitwaspossibletechnology,asitistohumanintelligence.Fortunately,over for anindependentresearchertoassesstheenergyconsumedmore thansixdecades,softwareengineershavedeveloped during training.Theyreportthatapproximately38%(30 robust automatedverificationandtestingtechnologiesthat out of79publicationswhichinvolvemodeltraining)sharedhelp toreducetheimpactofhumanmistakes.We expectthat sufficient informationtoestimatetheirenergyconsumptionsuch technologieswillalsocarryover toartificialintelligence during training.mistakes. Further evidencethattheremaybeagrowingissuewith G. HandlingLongerTextual Inputsscientific evaluationqualityintheliteratureonLLM-Based Software EngineeringcanbefoundinthesurveyofLLM-The performanceofLLMsonlarge-sizedinputpromptsis Based Testing by Wang et al. [98]. In their survey, they filteredlikely to be a topic of great interest in the artificial intelligence an initialpoolofpapersonLLM-BasedTestingtoremovecommunity [236].Advancesinthisareawillhaveastrong those that did not meet standard evaluation quality constraints.impact onsoftwareengineering,becauseoftheconsiderable These constraintsrequiredpaperstoincludeaclear,defined,size of software systems and the consequent opportunities that repeatable evaluationmethodologythatincludesacontroloradditionally openwhenlargerpromptsaretobeeffectively baseline against which to measure effectiveness. This filtrationhandled. criterion removedmorethan90%ofthepapersthatinitially H. LessWell-covered SubdomainsofSoftwareEngineeringmet keywordsearchcriteria. As theseanalysesoftheliteraturedemonstrate,moreworkAs oursurveyreveals,somesubdomainsofsoftwareengi- is clearlyneededtoestablishfirmscientificfoundationsforneering arenotablyunder-representedintheliterature;some the emergingdisciplineofLLM-basedSoftwareEngineering.surprisingly so.Forexample,RequirementsEngineeringand Such foundationsmaydrawonexistingforEm-Design (SectionIII),andRefactoringVI-E)enjoy pirical Software Engineering in general and, more specifically,very littlecoverage, yetthey aresurelyripeforconsideration, on AI-based Software Engineering, such as SBSE (where theresince theyrelyheavilyuponlinguisticformsofanalysisand is anaturalsimilarity[105],[235]).the recognitionandpredictionofpatterns.

17


---

<!-- Página 18 -->

R EFERENCES[20] sentiment [1]2023, “Harnessing[21] andsentationsnature,vol. [2]533–536, Y.[22]Neural investigation,”computation,vol. [3][23] W.Gomez, H.arXiv:1706.03762. wareJournal, vol. [24] no. T.ere, [4] A. decadesCommunications, vol. foundation Feb. [25][5] andthchallenges8in 2023-02-14-github-copilot-now-has-a-better-ai-model-and-new-capabilities/IEEE [26]Validation, Graz, later,”[6] 2023-07-27.oracleIEEE [27]Software, vol. T.[7] C.ricsarXiv, S.2023. P.[8] LevelScience,vol.and pp.siveIEEE, vol. [28]no. [9][29] [Online].E. prompt-engineering-tips-and-tricks/M. Early[10] box[30]ere, arXiv, 2023.Y. [11]J.efossez, inProceedingsJ. Automated, ser.G. AssociationarXiv:2308.12950. [12][31] engineering:ACMtheIEEE, vol. Surveys,vol.[32] [13]optimisation:International rdto33Conference International. NewQuality, vol. York,2008, [14][33] engineering:Empiricaltion engineering, B.arXiv:2304.12562. dio, [34] [15] requirement D. els,”Proceedings softwarearXiv on, 2022, arXiv:2308.10620,2023. [35][16] completeness:in arXiv, 2023.[17] [36]S. thSuccesses46InternationalG. ware, April“Webgpt: [37]2022, toProceedings[18] Meetingwal, ACMA. neering,ser.D. ComputingS. [38]I. bani,in Advances, H. scaleM. arXiv:2305.12050.Associates, [39][19] W.text modelarXiv:2304.08763.

18


---

<!-- Página 19 -->

[40][63] languageAI arXiv:2302.06590.[64] frameworkarXiv,[41] 2023.T. [65]andQueue, editorvol. [66][42] ShotCommunications, vol. arXiv:2304.06815.[43]et, “ProgramFoun- [67]dations, vol. “Prompt1–119, languagearXiv[44] preprint, 2023.naturalnessInternational [68]Engineering, Zurich, “PlanningarXiv[45] ndprnote, 2023,surgery22ACM [69]on, Hong planningChina, arXiv:2303.06689.[46] [70]repair,”Communications, vol. generation[47] th[71]in18ACM “CODET:software. Santa [72]on,ACM, M.[48] arXiv:2206.03865.opingJ., vol. [73][49] jamani,Code,” synthesis,”Proceedings [50] Software. Pittsburgh S. pp. for [74] 2023. ation [51] [75]s, “Codegen2: with languages,”¨[76]Ozsoy,un, [52] Code evaluationProceedingsin Study ACM. Apr. San [77] [53]arXiv:2302.03494. Cai,[78] LanguageCHIS. Conference. NewLearning,” LA[79] [54]G. S.with A.[80] Kalai,type arXiv:2306.11644.[81] [55]“Coco: Methods,”2023, [56][82] andstein, cations:Generated [57]E-Book,”Proceedings LearningComputer [58]oderlein,2023, loting[83] Magic?”breakthrough [59][84] Secureand [60]Code27th “ChatGPTence. Helsinki ing,2022, arXiv:2303.07839.[85] [61]plainable ExploringtheyarXiv, 2022. language,”Proceedings[86]onherr, Computering Feb.[62] sketch-basedarXiv[87] arXiv:2302.06144,2023.is

19


---

<!-- Página 20 -->

[88][112] vulnerabilityS. “Automatic[89] arXiv:2305.12865.erative Education[113] shot[90] IEEE/ACMation (ICSE),2023,arXiv:2303.13547. [114][91] thLanguage46InternationalcodeProceedings Engineering, Aprilon, ser. Association[115] “No[92] generation,”and tests,”ACM[116]afer, and, Jan.Using [93][117] byChatGPT-based ModelsarXiv:2305.04764. [94][118] K.“Automatic githubarXiv, 2023.ICSE Seoul,, G.[95] D.“ReAct: [https://doi.org/10.1145/3377811.3380420](https://doi.org/10.1145/3377811.3380420)arXiv:2210.03629. [96][119] pletion2022L. Conferencereplacement,”44th (ICSE-SEIP),2022,on 25-27,. ACM,[97]Report [https://doi.org/10.1145/3510003.3510206](https://doi.org/10.1145/3510003.3510206)High. Cambridge, University[120] hery,[98] soningtesting 2023,[121] ysisSymposium[99] and, Victoria,deep [122][100] dreams,”Future. IEEE,“No pp.Test [123][101] mutationIEEE, vol.tools no.modelsarXiv, 2022. [124][102] “MutationAdvancestestingCompanion Computers,vol.on, 2007,[125] ical[103] thatgenerationarXiv ofarXiv:2308.08033,2023. 2017,,[104] V.[126] inmutationarXiv arXiv:2301.03543,2023.[105] Escaping[127] LanguageMimicking [106][128] generativeJ. mutationsSSBSE[107] Track. SanDesmarais, modelsarXiv, pp.[129] Similarity-based[108] , 2023.fuzzingarXiv, 2023.[130] daresan,[109] Models,”Models Large[131] nities[110] th(keynote18IEEE“Large Source, Madrid,ing September[111] “Finding[132] arXiv:2304.11686.“FlakyCat:

20


---

<!-- Página 21 -->

[133]

[134]

[135]

[136]

[137]

[138]

[139]

[140]

[141]

[142]

[143]

[144]

[145]

[146]

[147]

[148]

[149]

[150]

[151]

[152]

[153]

[154]

[155]

[156]

2023[157] Test, 2023,$0.42 [158]arli, languageIEEEModels Software, 2022.[159] ining testarXiv:2112.02125. [160] rdM.23L. Automated. L’Aquila,softwarearXiv 2008,preprint, 2023. [161] dataJournalAdvantages and, vol.Repair,” [162] correctnessSoftwareGenerating and, vol.Issue [163] “AnS. thfailed36Internationalfor Conference, Hyderabad,arXiv:2301.03797. June[164] models testing[165] arXiv:2306.05152.A. Mar. faultarXiv, 2023.[166] fix “Largethe 18-24, ser. Research,Android 780–791.arXiv:2306.01987. [167] hypothesisASE, 2023.I.cek, withProceedings[168] Intelligence,vol.debugging arXiv:2304.02195. address[169] programarXiv, 2023.M. forSSBSEin severity2023:, ser. Dec genericIEEE[170] Software, vol.Babbage with italianequeeve,vey 82. [171]Compilers:A. niques, 1986.in International Engineering, Montreal,[172] improvesActa, vol. repair3rd[173]The, 1984, AutomatedPepper May. IEEE,[174]Genetic ACMby. Cambridge, Computing, vol.[175] M. Information, vol.F. ndDec.patchingProceedings22 Symposium Systems, OctoberD. in[176] and th(keynote9InternationalautomatedProceedings neering. Newthe York,Symposium, 2022, 959–971.[177] neticIEEE (TEVC),vol.of [178] Y.Language ImprovingRepair,”FSE, 2023. [179] C.Jan.

21


---

<!-- Página 22 -->

[180]

[181]

[182]

[183]

[184]

[185]

[186]

[187]

[188]

[189] [190] [191]

[192]

[193]

[194]

[195]

[196]

[197]

[198]

[199]

[200]

[201]

[202]

softwareProceedings[203] Software of, 2022, [204] through [205] proacharXiv arXiv:2306.17077,2023. [206] toarXiv [207]arXiv:2309.14846,2023.  [208]J. “Large [209]ACM, vol.  [210]Chain: on2023 on, 2023,  [211]M. similarity andJournal, p.  [212]ingarXiv arXiv:2305.13592,2023.  [213]refactoring,”Information, vol. 2017. Elements. Elsevier,  [214]  andIEEE Software, vol.  more36th Conference. New USA:[215]  resource-efficient erators,”2008 (GECCO, Atlanta, [216] optimisation,”Genetic (GECCO, Madrid, [217] J. surface thpaper),”27IEEE/ACM[218] Software, Essen, pp. Design. Addison-Wesley, [219] automaticIEEE Transactions, vol. 2022.[220]  Y.[221] Code arXiv:2305.12865.[222]  X. Multi-Intent[223]  thment46International ference, April[224] IEEE Software,vol.  2008. IEEE,

22

appIEEE Software, vol.  IEEE, vol.  Handbook recent. World et,Software traceability.Springer, IEEE Software,vol. ACM SIGSOFT, vol.  lessonsComputer,vol. 2008.  perience: byCHI in. New ACM,  “Investigating sourcing2023 and, 2023,  T. ing Software, 3rd Maidenhead, Europe, ISBN  M. ment deployment inACM/IEEE neering, October given  C. assistant, Recherche 0177,  study,”International ’92) ,Los  International, Los Alamitos,  “The LanguageProceedings 28th. Sydney NSW  Bissyande, far  afterThe, December  MIT, April  and arXiv:2302.03287.  Models Code,”  tion LanguageProceedings International. Lugano Event


---

<!-- Página 23 -->

[225]

[226]

[227]

[228]

[229]

[230]

[231]

[232]

[233]

[234]

[235]

[236]

th46 International, April 2024,  R. for  pathways,”  insights  “Towards ofJ., vol.  E. T. A. and arXiv:2203.15556.  and 2021,  distillation es, and CoRR,vol.  on arXiv:2307.02443.  tive  W. dardized arXiv:2201.03533.

23


---

