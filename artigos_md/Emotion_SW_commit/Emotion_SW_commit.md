<!-- Página 1 -->

2025 IEEE International Conference on Collaborative Advances in Software and COmputiNg (CASCON) | 979-8-3315-9948-5/25/$31.00 ©2025 IEEE | DOI: 10.1109/CASCON66301.2025.00072

2025 IEEE International Conference on Collaborative Advances in Software and COmputiNg (CASCON)

## Pushing Feelings:

## Emotion

## and

## Sentiment

## in

## Software Commit

## Messages

∗†‡∗Krishno Dey, JagannathSingh, HungCao, FrancisPalma ∗SE+AI Research Lab,Faculty ofComputerScience,UniversityofNewBrunswick,NB,Canada †School ofComputerEngineering,KalingaInstituteofIndustrialTechnology, India ‡Analytics EverywhereLab,Faculty ofComputerScience,UniversityofNewBrunswick,NB,Canada { krishno.dey,hcao3,francis.palma} @unb.ca, [jagannath.singhfcs@kiit.ac.in](mailto:jagannath.singhfcs@kiit.ac.in)

**Abstract—Software repositories**aretheprimarysourceofcommunity [2 ], [3 ], analyzingcommitmessagesremains **information for**softwareartifactsandcontainalargeamountchallenging duetotheinconsistentandinformalnatureof **of unstructured data, including commits, issue reports, and code**these messages[4 ]. Mostpriorstudiesincludelexicon-based **comments. Mining**information for different tasks,suchassenti- approaches [5 ], [6 ]. Assuch,wordsorlexiconsplayeda**ment and emotion analysis, has been studied on several artifacts.** crucial roleinidentifyingemotions,ratherthanrelyingon**While significant**progresshasbeenmadeinsentimentanalysis **on various**artifacts,thestudyofemotionanalysisremainscontextual information.Theadvancementofnaturallanguage **under-researched**duetoalackofresources,suchasrelevantprocessing andmachinelearningtechniqueshaspavedthe **and labeled**datasets.Thisstudypresentsamanuallyannotatedway for groundbreaking research in identifying emotions from **dataset comprising**12,005commitmessagesfromtheopen- software artifacts.Researchershave conductedseveral studies**source Apache Tomcat project, exploring emotion and sentiment** to identifyemotionsincommitmessagesusingtraditional**analysis through**theapplicationofnaturallanguageprocessing **and machine**learning techniques.We studiedtraditionalmodelsapproaches[7 ]. **(SVM and**randomforest),deeplearningmodels(bidirectional-There hasbeenagrowingresearchinterestinsentiment **LSTM), and pre-trained language models (LMs), as well as their**analysis on software artifacts [8]–[10]. However, due to several **ensemble, to**evaluateandcomparetheirperformanceonthe challenges, veryfewstudies(e.g.,[1 ]) focusonemotion**curated dataset.**Ourfindingssuggestthatsoftwareengineering identification. Oneofthemainchallengesisthelackofwell-**domain-specific pretrained**LMsconsistentlyoutperformtradi- **tional and deep learning models. The ensemble of pretrained LMs**designed annotation guidelines, which may result in unreliable **performs better**onsentimentanalysis.Additionally,identifying[ 11 ] andlow-agreement datasetsthatcausebiasesinlearning. **sentiment from**commitmessagesoutperformsemotionanalysisThe contentofanartifact(e.g.,commitmessagesandcode **tasks. We**havemademodelimplementationsandthecurated comments) sometimesbelongstomultipleclasses[12 ], mak-**dataset available.** ing it difficult to categorize them into a single class and posing**Index Terms —Emotion and**sentimentanalysis,Pretrained **language model,**Ensemblelearning,Commitmessages.challenges forthemodeltodifferentiateamongclasses.An- other challengeisdistinguishingbetweendifferentemotions I. INTRODUCTIONin similar content within the project. Developers often express their emotions and sentiments through commit messages, issueSentiment analysisinsoftwareengineeringiscrucialfor comments,andteamconversations; however,identifying developersentimentsoremotions[1 ] expressedresponses, code challengingtodeterminesentimentandemotionfromthrough varioussoftwareartifacts.Althoughdevel-it is most artifacts.opment isalogicalandsystematicendeavor,theindividuals Further, theperformanceofthemodelsusedtoclassifybehind it bring emotions, perspectives, and experience. Under- sentiment andemotionvariesacrossthedatasets[12 ]. Al-standing theunderlyingemotionsandsentimentsofsoftware though afewopen-sourcedatasetsforemotionandartifacts iscrucialforunderstandingtheimpactofsentiment 5 ], [8 ], [9 ], [13 ] existintheliterature,mostareand emotiononsoftwarequalities,workenvironment,and analysis [ annotated basedonthelexiconsandlackmanualvalidation.team dynamics. Analyzing emotions and sentiments in commit The limitationsofthemethodsandmodelsincapturingmessages mayprovideearlyindicationsofdevelopers’state the underlyinginterpretationsfromtextsmakeitdifficulttoof mind,whichteamleadsandmanagerscanleveragefor analyze sentimentandemotion.resource allocation. In thisstudy,wedevelopedanannotationguidelinetoSoftware repositories,suchasGitHubandGitLab,contain facilitate emotion and sentiment analysis in commit messages.a vastamountofunstructureddata,andminingthisdatahas guideline,wecreatedthelargestmanuallyan-become inevitableforthesoftwareengineeringcommunity.Following this Most developers’workingnotesontheirprojectsaredoc-notated dataset. The dataset has undergone several iterations of umented incommitmessages,codecomments,andprojectpre-processing andvalidation tomakeitusableforqualitative emotionandsentimentanalysistasks.We definedocumentation. Althoughanalyzingandreviewingcodehas research and twoquestionstoexaminethestate-of-the-artmodelsreceived more attention from the software engineering research

979-8-3315-9948-5/25/$31.00 ©2025 IEEE429 DOI 10.1109/CASCON66301.2025.00072 Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.


---

<!-- Página 2 -->

for automaticemotionandsentimentanalysisofsoftwareand NLTK [23 ] havebeenadoptedfromgeneraltexts,where commit messages.some tools,i.e.,SentiStrength-SE[8 ], Senti4SD[24 ], and SentiSW [9 ] weredesignedforsoftwareengineeringtext.RQ1: Howwelldostate-of-the-artmachinelearningand deep learningpredictemotionsandsentimentsoncommit A. SentimentAnalysis messages? The simplestsentimentanalysistaskinvolvesclassifyingRQ2: How does an ensemble of pretrained language models a textintooneoftwocategories(PositiveorNegative)orperform onemotionandsentimentdata? three categories(Positive,Negative,orNeutral).ToextractWepresentacomparativeanalysisusingpretrainedlan- developer sentiment,thetextmustbefromsourceswherede-guage models(LMs),includingclassicalanddeeplearning velopers communicateorupdatetheirdailytasks.Asaresult,models. Theperformanceofthemodelsshowsthatthepre- GitHub isoneofthelargest informationrepositories,contain-trained languagemodelsoutperformdeeplearningmodels, ing various software artifacts, suchascommitmessages,codewhile classicalmodelsshowanotableperformanceonthis comments, and issues. Although most of the commit messagesdataset. Ourcontributioncanbesummarizedasfollows:(1) collected fromGitHubbelongtoneutralclasses[25 ] duetowe builtthelargestmanuallyannotateddatasetforemotion open-source collaboration,itisstillworthwhiletoinvestigateanalysis oncommitmessages;(2)weinvestigatedthepre- developer sentiment.trained LMsbyfine-tuningthemodelswiththedata;(3) The earlystudiesinthisarearelyonalexicon-basedwe investigatedensemblelearningusingpretrainedLMsto approach to extract sentiment, which involves developing lexi-compare and improve the performance of individual pretrained cons, such as SentiStrength [ 22] and Senti4SD [ 24]. AlthoughLM; (4)wearethefirsttoprovideacomparativeanalysis the SentiStrengthlexiconwasmainlydevelopedfromsocialamong theclassical,deeplearning,pretrainedmodels,and media texts,itgainedpopularityamongresearchersduetoensemble learning;and(5)weprovidedacomparisonofthe its performanceinsoftwareengineering.Theuseoflexi-performances betweenemotionandsentimenttasks. cons involves analyzing the relationship between programmingThe summaryofourfindingsincludes(1)fine-tunedsoft- languages anddevelopersentiments,aswellaschangesinware engineeringdomain-specificLMsprovidebetterresults sentiment acrossthedaysofaweekanddevelopercompared toothermodels;(2)thepretrainedmodel,Commit- over aday[21 ].BART[14 ], trainedoncommitmessagesyieldsthebestper- formance foremotiontaskwhileensemblelearningprovidesB. EmotionAnalysis the bestperformanceonsentimenttask;(3)allthemodelsResearchers havedoneafewstudies,e.g.,[1 ], [10 ], [13 ] except CommitBART andrandomforeststruggledtopredict1to identifytheemotionsfrom commitmessagesandissue the surpriseclass,whileXLM-RoBERTa [15 ] onlypredictedcomments. Although emotions are categorized into eight types, neutral andtrustclassesforemotionanalysis;and(4)alltheresearchers haveusedthree,four,six,andeighttypesof models areperformingbetteronsentimenttasksduetotheemotions intheliterature[1 ]. Lexicon-basedapproachesare dimensionality oftheclasses.also followedinextractingemotions,whichincludeafew For the rest of the paper, Section II discusses an overview ofemotion lexicons,i.e.,NRCWord-Emotion AssociationLex- related work. Section III presents our research method and theicon [10 ], DEVA[13 ], TensiStrength[26 ], etc.Usingthese implementation strategies employed. Section IV presents a de-lexicons resultsindifferenttypesofemotionoverasingle tailed performance analysis of the two experimental strategies,text. For example, the NRC word-emotion association lexicon, along withtheproposedensembleapproaches,whileSectionDEVA,andTensiStrength have eight,four, andthreetypesof V discussestheperformanceanalysisandchallenges.Finally,emotions, respectively. Althoughtheemotionswereextracted Section VIconcludesthepaper.using alexicon,inmostcases,onlyonewordisusedto identify the emotion of a text [ 10]. The study in [ 13] proposedII. RELATEDW ORK an automatic tool named DEVA to extract emotions from com- Sentiment analysisenablesonetoidentifytheemotions mit messagesandissuecommentsusingthevalence-arousal from texts, which helps variously, i.e., quality of products [ 16], model, whichcalculatesfourtypesofemotions.Althoughthe identifying requirementsfromuserfeedback[17 ], relating study providesaninsightfultoolforemotionextraction,the sentiment tothedeveloper performance[18 ], andtrustamong comparison withothertoolswasambiguous. team members[19 ]. DevelopersexpresstheiremotionsandMachine learning-basedapproacheshaverecentlybeen sentiments duringthesoftwaredevelopmentprocessthroughstudied toextractdevelopersentimentsforsoftwarearti- commit messages, issue comments, and other software artifactsfacts, e.g.,[7 ]. Supportvectormachines,naiveBayes,ran- [ 1 ]. Therefore,researchersbecameinterestedinextractingdom forests,decisiontrees,andextremegradientboosting emotions andsentimentsfromsoftwareartifacts.are amongthemostpopularalgorithmsstudied.Amachine Researchers havebeenattemptingtoextractemotionsandlearning-based sentimentextractiontoolwascreatedinthe developing lexicon-basedtoolstoidentifybothsentimentandstudy byIslametal.[7 ], whichoutperformsexistinglexicon- emotions insoftwareartifactssincetheearly2010s[6 ], [20 ],based sentimentextractiontools.Imranetal.[27 ] primarily [ 21 ]. Asaresult,researchershavedevelopedseverallexicon- 1based tools. Most of the lexicon tools, i.e., SentiStrength [ 22],anger,

430

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.


---

<!-- Página 3 -->

addressed thedatascarcityprobleminemotionanalysisinduplicate commit messages to handle the duplicates and URLs SE textbyautomaticallycreatingnewtrainingdatausingathecommitmessageswithoutfurtherpreprocessing. data augmentationtechniquebyanalyzingtheerrorsmadebyThese filtering and removing duplicate steps resulted in 12,005 popular SE-specificemotionclassificationtools.Theauthorscommit messages. investigatedtheeffectiveness ofanemotionclassifier,SEnti- B. FilteringCommitMessagesMoji[ 28 ], indetectingemotionsinGitHubcomments. Commit messagescontainURLs,commitIDs(i.e.,hash C. EmotionAnalysisusingLLMsvalues), andinvisiblecharacters.Asapartofthepreprocess- Among the very few studies that investigated large languageing steps,wefirstremovedthenoisyportion(commitIDs, models (LLMs)foremotionspredictioninSEtext,likeissueinvisible characters,andblankspaces)ofthedata.Wethen comments, include[29 ], [30 ]. In[29 ], theauthorsexploredremoved aspecificwordgit-svn-id() duetoitshighfrequency zero-shot LLMsfordetectingemotionsinsoftwaredevel-and lack of meaningful relevance to the emotion identification oper communication.ThoseLLMsarepre-trainedonmassivetask. Wealsotokenizedandperformedcaseconversion(i.e., datasets butnotfine-tunedfordetectingemotionsinSE.Theconvertingallcharacterstolowercase)beforetraining. authors found that the LLMs perform well in the emotion clas- C. ManualAnnotationsification taskcomparedtostate-of-the-artmodels.However, this comeswithasignificantcostintermsofcomputationGiven a commit message, we want to categorize its intended required. Topal etal.[30 ] exploredtheperformanceofopen-emotion, i.e.,whetheritisanger,fear, joy,neutral,sadness, source LLMs in sentiment analysis. The authors also exploredsurprise, ortrust. the impactofvariousinstructionmethodsandfine-tuning **Data Annotation Scheme:As the data annotation scheme for**techniques onthemodels’performanceandanalyzedtheir emotions, weadoptedsixemotionclasses,mergingdisgustsensitivity to different prompts. The authors considered BERT- and anticipationwithangersuggestedbyShaveretal.[31 ]based modelsastheirbaselineandfoundLlama3andMistral from thewheelofeightemotions[32 ]. Forasignificantto betop-performinginsentimentanalysistasks. number ofcommitmessages,itischallengingtofindtheExisting studiesmostlyrelyonalexicon-basedapproach appropriate emotionlabelfromthesixclasses.Asaresult,to extractsentiment.Moreover, thereisascarcityofdatasets we alsointroduceda neutralclass totackletheannotationavailable forevaluatingemotionandsentimentfromcommit issue, resultinginsevenemotionclasses.messages. Inthisstudy,weconstructamanuallyannotated In thefollowing,wediscussthetaxonomyofemotionswedataset and employ machine learning and pre-trained language provide duringtheannotation.models toanalyzesentimentandemotion. **Angeris an intense emotion that intends to show irritability,** III. RESEARCHM ETHODOLOGYI MPLEMENTATIONdisgust, envy,jealousy,andannoyance.Itdeliberatelyex- presses astrong,uncomfortable,andnon-supportiveresponseThis sectiondetailstheresearchmethodologyandimple- to astatement.mentation asdepictedinFigure1. **Fearis an unpleasant emotion expressed during a dangerous** A. DataCollectionor badsituationtoshownervousness,anxiety,worry,panic, 2and dread.Tocollectcommitmessages,wechooseApacheTomcat. **Joy**is apositiveemotiontoshowhappiness,satisfaction,During the data collection, we collected commit IDs, commit- pleasure, andamusement.Thepurposeofjoyistoexpresster usernames,dates,andmessages.WeselectedtheTomcat andsuccessofanaction.open-source systembecauseitiswidelyknown,activelythe well-being **Sadness**is anegativeemotionwithasenseofdepression,maintained, andusedintheempiricalSoftwareEngineering rejection,andsympathy.research community.Tomcathasawell-documentedcommitregret, embarrassment, **Surprise**is anemotionthatexpressespositivitytoshowhistory.Moreover,wealsodidnotwanttoselectalargeor amazement andastonishment.small system,optinginsteadforamoderate-sizeddatasetto be annotated.Ourprimaryfocuswastoselectanopen-source Trust is anemotionofastrongbeliefinreliabilitytoshow project with numerous commit messages from developers whoconfidence, admiration,andagreementwithastatement. have contributedoveralongperiod.Wecollectedatotalof Neutralis usedfortextsnotrepresentingemotionsorthe 313,000 recentcommitmessages.WeoptedtousePyDrillerannotators are unable to understand the emotion from the text. to extractcommitmessagesfromGitHubsinceitiswell- **Data Annotation**Guideline:Weasked annotators to read the documented and provides all the necessary information related given commitmessagefirsttounderstandthecontextofthe to commit messages. Although eachis unique with its text andtheemotionexpressedbythewriterofthemessage. commit ID,themessagescanbethesame,andeachmessage Based onthe Data AnnotationScheme, theannotatordecides can befoundinmultiplecommits;forexample,we the appropriateemotionclassoncetheannotatorunderstands thatfix typooccurs inmultiplecommits.We removed the the expressedemotion.Thedetailedannotationguidelineand 2the supplementalmaterialsareavailableat[https://doi.org/10](https://doi.org/10).[https://github.com/apache/tomcat](https://github.com/apache/tomcat) 3[http://dl.acm.org/citation.cfm?doid=3236024.3264598](http://dl.acm.org/citation.cfm?doid=3236024.3264598)5281/zenodo.14449706.

431

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.


---

<!-- Página 4 -->

###  ' S Q Q M X 

Fig. 1:Theoverview oftheresearchmethodology.

disagreement amongtheannotators,thecuratorsorganizeda discussion toselectthefinallabel.Thismethodoffershigh accuracy,whichiscriticalforanyannotationtask.However, this processiscostlyandtime-consumingforlargerdatasets.

**Annotation Quality:**WecalculatedtheInter-Annotator Agreement (IAA)tomeasuretheannotationquality. First,we calculated theFleissKappaκ( ) [33 ] scoreontheunconsoli- dated labeled dataset, yielding a value of. 14 , indicatingslight agreementamong theannotators.Thisannotationscoreindi- cates thedisagreementamongannotatorsforalargenumber of datapoints,i.e.,therewasnomajoritylabelforemotions among theannotators.Thecuratorsconsolidatedthefinal labels for the commit messages with disagreement. Afterward,Fig. 2: The distribution of sentence length associated with each we againcalculatedtheκscore andobtainedavalue of0 . 52 ,emotion label. indicating amoderate agreementamong annotatorswiththe 7 G V E T I V help ofthecurator’s group.

**Annotation Process:**Weusedapoolofannotatorscon-D. Pre-processing sisting of14computer scienceundergraduateandgraduate Wepre-processthedatabyremovingunnecessarytextandstudents. Alloftheannotatorsaredividedintotwogroups: prepare itfortrainingandevaluation.annotators andcurators.Inthegroup,weselected 1) DataAnalysis:Weanalyzedthesentencedistributions12students; therest(thosewithpreviousdataannotation by the number of words for each class label presented in Figureexperience) wereusedascurators.Studentsintheannotator 2 . Basedonthedistribution,neutralandtrustare themostgroups had low to moderate experience in data annotation and common emotionsdevelopersexpressincommitmessages,sentiment/emotion analysisfromtext.Incontrast,researchers i.e., around58%of thedatafallswithinthetrustandneutralin thecuratorsgroupwereexperiencedindataannotation classes.Surpriseandfearare theleastoccurringemotionsand sentiment/emotionanalysisinthesoftwareengineering in ourdataset,comprisingaround11%of thedataset.Wedomain. Theprimarytaskoftheannotatorgroupwasto also incorporatedifferentrangesofsentencelengthbucketsannotate the commit messages, while the curators concentrated to investigate the optimal sequence length for pretrained LMs.on consolidatingthefinallabels.Eachcommitmessagewas Wefoundthataround80%data belongswithinthesentenceindependently annotatedbythreeannotators,followingour length of20words.annotation guidelinesthatdescribethesteps.We conducted aweeklyreviewmeetingtoalignanddiscuss2) DataSplit:Wedivided the dataset into train, validation,

###

and testsplits,containing70%,10% , and20%of thedata,specific annotationcases.Themajorityagreementforeach We usedstratifiedsamplingtoensureabalancedcommit messageselectedthefinallabel.However, incasesof

###  ) Q S X M S R 

###  % R R S X E X M S R 

###  ( E X E W I X

###  ) Q S X M S R W

###  4 ] ( V M P P I V

###  + Y M H I P M R I

###  * M V W X  7 X V E X I K ]

432

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.

###  K

###  7 I G S R H  7 X V E X I K ] 

###  + M X , Y F 

###  1 I W W E K I W

###  6 I T S W M X S V ]

###  4 V I T V S G I W W M R

###  7 I R X M Q I R X 

###  ( E X E W I X

###  8 L M V H  7 X V E X I K ]

###  ) \ T I V M Q I R X E P 

###  * M P X I V M R K

###  ( E X E  ' S P P I G X M S R

###  1 E R Y E P 

###  7 X V E X I K M I W

###  % R R S X E X M S R

###  ) Z E P Y E X M S R


---

<!-- Página 5 -->

##  8   ' S Q Q M X 

**Class**

Anger Fear Joy Neutral

TABLEI:Classlabeldistributionacrossthedatasplits.

distribution ofclasslabelsacrossthedatasplits.We provided the detaileddatadistributionofthedatasplitsinTable I. 3) SentimentDataPreparation: Anger,Fear, andSadness emotions areexpressedinanegativesituationwhileJoy Fig. 3:ConcatenationofhiddenoutputsfollowedbyfusionandTrustshow positivity.Moreover,Surpriseemotion can and outputlayer.be expressedinpositiveandnegativesituations.However, we choseSurpriseemotion asapositivesentimentsincewe found positive textual representations in the commit messages. As aresult,toconsolidatethesentimentdata,wecombined { Anger,Fear,Sadness}emotions asNegativesentiments and { Joy ,Surprise,Trust}emotions asPositivesentiments while considering neutralemotionsassentiments.

E. ExperimentalStrategies

Weemployedtwoexperimentalstrategiestoinvestigate the two researchquestions. 1) FirstStrategy:As partofthisstrategy, weaddressRQ1 to comparetheperformanceoftraditionalmachinelearning, deep learning,andpretrainedLMsusingbothemotionandFig. 4:Concatenationofhiddenoutputsfollowedbyfusion sentiment datasets.Indeed,weselectedwidelyusedmodelslayer, feed-forwardnetwork,andoutputlayer. effectiveforsentimentandemotionanalysis.

**Baseline Model**:WeincorporatemultinomialnaiveBayes 4erator, andCommitBART[ 14 ] pretrainedmodelsforour(MNB) asourbaseline,asithasbeenwidelyconsidered study becausetransformer-basedpretrainedLMshaveexhib-the standardmodelintheliterature.Wecapturecontextual ited notableperformanceforvariousNLPdownstreamtasks.information forMNBbyusingaweightedn − gram (uni,bi, Wemaintainthesamehyper-parametersforfine-tuningfortri, andquadri-gram). fair evaluationacrossthemodels.Wefine-tuneourmodels **Classical Models:**In priorstudies,classicalmachinelearningfor upto3epochs tomitigateoverfitting,usinganAdam − 5models such as the support vector machine (SVM) and randomoptimizer with a learning rate ofe, a batch size of16 , and forest have beenwidelyusedduetolimitedcomputationalre-a maximumsequencelengthof256 . sources [ 13].Toinvestigate classical machine learning models,2) SecondStrategy:ToaddressRQ2,weexplorethree we selectedSVMandRFtoconductourexperiments.Wedifferent approachesforensemblelearning.Weutilizefour used thestandardparametersettingsandaweightedn − gramdifferent pre-trainedLMs,trainedonsoftwareartifacts,in

###  , M H H I R  W X E X I W

tf-idf representationtopreparethedata.all threeapproaches.Inthefirstapproach,weconcatenate

##  ' S H I & ) 6 8

the outputofthehiddenstateofCodeBERTandthe**Deep Learning :**Although deeplearningmodelsareexten- of theencoder’slasthiddenlayeroftheotherthreemodelssively usedforsentimentandemotionanalysisonsocial (CommitBART,T5CommitGenerator,andCodeReviewer).media data,theyhavenotbeenwidelyappliedtosentiment

###  , M H H I R  7 X E X I W

Then, wefeedtheconcatenatedoutputtothefusionlayer,

##  ' S H I & ) 6 8

or emotionidentificationforsoftwareartifactstodate.We followed bytheoutputand softmaxlayer.Forthesecondincorporate bidirectionallongshort-termmemory(LSTM)as approach, wemaintainasimilararchitecturetothefirsta deeplearningalgorithmtoexploretheperformanceofthe approach and incorporate a feed-forward network between the

###  ) R G S H I V  P E W X 

deep learningmodel.ThemotivationforchoosingLSTMis

###  L M H H I R  W X E X I

##  ' S Q Q M X & ) 6 8

fusion andoutputlayers.Theprimarydifferencebetweenthethat itcancapturealongsequenceandextractmeaningful first andsecondapproachesliesinthesoftmaxlayer. Fortheinformation. We use an embedding dimension of 128, as more third approach,weselectthebestlogitsbased onthethan 95 confidence andfeedthebestlogitsto thesoftmaxlayer.We

###  ) R G S H I V  P E W X 

###  L M H H I R  W X E X I

##  ' S Q Q M X & ) 6 8

**Pretrained Language**Models:WechooseXLM-RoBERTa 4[ 15 ],CodeBERT[ 2 ],CodeReviewer[ 3 ], T5commitgen-[https://huggingface.co/mamiksik/T5-commit-message-generation](https://huggingface.co/mamiksik/T5-commit-message-generation)

##  * I I H  * S V [ E V H 

##  2 I X [ S V O

433

###  ) R G S H I V  P E W X 

##  + I R I V E X S V

###  L M H H I R  W X E X I

##  * Y W M S R  0 E ] I V

##  ' S R G E X I R E X M S R

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.

###  ) R G S H I V  P E W X 

##  + I R I V E X S V

###  L M H H I R  W X E X I

##  ' S R G E X I R E X M S R

##  * Y W M S R  0 E ] I V

##  3 Y X T Y X  0 E ] I V

###  ) R G S H I V  P E W X 

##  ' S H I 6 I Z M I [ I V

###  L M H H I R  W X E X I

###  ) R G S H I V  P E W X 

##  ' S H I 6 I Z M I [ I V

###  L M H H I R  W X E X I

##  3 Y X T Y X 

##  0 E ] I V

##  7 S J X Q E \  0 E ] I V

##  7 S J X Q E \ 


---

<!-- Página 6 -->

##  ' S H I & ) 6 8

# 1

##  ' S Q Q M X & ) 6 8

##  8   ' S Q Q M X 

##  + I R I V E X S V

##  ' S H I 6 I Z M I [ I V

**Model**

**Baseline**

MNB

**Classical**

SVM**26.51** RF**28.65**

**Deep**

Bidirectional**27.42**

**Pretrained**

XLM-RoBERTa-large Fig. 5:Thirdensembleapproach:selectthebestlogitsbasedCodeBERT**30.71** CodeReviewer**29.97**on thelogits’confidence. CommitBART**32.70** T5**28.11**

**Model**provide adetailedarchitectureofthefirst,second,andthird **Baseline**approaches inFigures3, 4, and5, respectively.Wetrainall the ensemblemodelsforuptoepochs withalearningrateMNB − 5of2 efor theAdamoptimizer,abatchsize32 , anda **Classical** maximum sequencelengthof 256. Moreover,weusedthe SVM**49.06** CrossEntropyLossfunction tocalculatethetrainingandRF**51.57** validation loss. **Deep** Toevaluateandcomparethemodels,wecomputedtheir Bidirectional**50.07**accuracy,weightedprecision,recall,andF1macroscoreto **Pretrained**measure allperformanceacrossthedifferentexperimental settings. Considering the imbalanced data, we chose the macroXLM-RoBERTa-large CodeBERT**53.36**version oftheF1score. CodeReviewer**49.29** CommitBART**51.77**IV. EXPERIMENTALR ESULTS T5**49.89** This section details the results of the two strategies address- TABLEII:Performanceondifferentmodelsforthefirstex-ing theircorrespondingresearchquestions. periment strategy to address RQ1 using emotion (top) and sen- A. RQ1:Performance of Machine and Deep Learning Models timent (bottom)datasets.Boldindicates modelsoutperformed In TableII(top),wepresenttheresultsofourfirstex-baseline; Underlineindicates thebestperformingmodel. periment strategywiththeoriginaltrainsetoftheemotion dataset. Inourfirstexperiments,wefoundthatallthemodels outperformed thebaseline,exceptfortheXLM-RoBERTa-LMs (CodeReviewer andT5-Commit-Generator)despitehav- large model.Classicalmodelsoutperformthebaselineand ing lessmodelcomplexityandfewertrainableparameters. XLM-RoBERTa-largemodel,whiletherandomforestoutper-However,CodeBERT andCommitBART exhibit superiorper- forms the bidirectional LSTM and T5 commit generator. Whileformance comparedtotheothermodels,withCodeBERT most pre-trainedLMsoutperformclassicalanddeeplearningbeing the best-performing model, achieving an F1-macro score models, XLM-RoBERTa-large failedtodemonstratesuperiorof53 . 36. performance oncommitmessages.ThereasonforperformingTherefore, thecurrentstate-of-the-artmachinelearning, poorly oncommitmessagesisthatthemodelistrainedondeep learning,andpre-trainedLMsdidnotperformwell newspapers, Wikipedia,andformaltext,whichdiffersfromfor emotionanalysis,mostlikelyduetothehighnumber commit messages.Amongthemodelstrainedonsoftwareof emotionclasses(i.e.,seven)andpoorannotationquality. artifacts, CommitBARTisthebest-performingmodel,whileHowever,the performance on the sentiment dataset (with only CodeBERTshowsprominentperformanceoverthetestset.three classes)iscomparabletostate-of-the-artresults. Wepresenttheresultsonthesentimentdatasetforthe B. RQ2:Performance ofEnsembleLearningfirst strategyinTable II(bottom).Thisusedoriginal training datatotrainthemodelandtestdataforevaluation.TableIII (top) presents the performance of the second strat-

###  0 S K M X W

In ourfirstexperimentalstrategy,wefoundthatalltheegy usingtheemotiondataset.Theperformanceofensemble models outperformed the baseline except the XLM-RoBERTa-learning didnotperformwellontheemotiondataset.We large model.Classicalmodelsprovidedcomparableperfor-achieved anF1-macroscoreof20.26%forthefirstensemble mances, whiletherandomforestoutperformedbidirectionalapproach, whichcouldnotsurpassthebaseline.Althoughthe LSTM, CodeReviewer,andtheT5commitgenerator.More-other two ensemble approaches outperformed the baseline, the over,thebidirectionalLSTMoutperformstwopre-trained pretrained LMs(trainedonsoftwareartifacts)andrandom

###  0 S K M X W

434

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.

###  0 S K M X W

##  7 I P I G X  X L I  F I W X 

##  7 S J X Q E \  0 E ] I V

##  P S K M X W  F E W I H  S R 

##  G S R» H I R G I

###  0 S K M X W


---

<!-- Página 7 -->

### Joy

**Model**

Baseline

Approach Approach**27.62** Approach**28.30**

### Fear

**Model**

Baseline

Approach**54.67** Approach**52.85** Approach**52.35**

TABLEIII:Performanceonproposedensembletechniques to addressRQ2foremotion(top)andsentiment(bottom)

### Neutral

datasets.

Fig. 7:Class-wiseperformancesonselectedmodelsforthe first experimentstrategyontheemotiondataset.

Surpriseclass wasthemostchallengingforemotionanalysis. The XLM-RoBERTa-large modelcorrectlypredictedonlythe 102030 NeutralandTrustclasses, butfailedtopredicttheother classes correctly.BidirectionalLSTMperformedpoorlyin theSurpriseclass whilestrugglingwiththeSadnessandJoy classes. ThepretrainedmodelT5CommitGeneratorcould not predictanySurpriseclass correctlywhiledeliveringthe best performanceforthe Neutralclass andthesecond-best performance forthe Trust class. WhileCodeBERT performed inadequately intheSurpriseclass, itachievedthebestper-Fig. 6:Emotionclass-wisebest-performingmodels. formance fortheSadnessandTrustclasses andthesecond- best performanceinthe Fearclass. Amongallthemodels, forest exhibitsuperiorperformancesinemotionanalysis.WeCommitBARToutperformed the others in four classes:Anger,

### Sadness

achieved F1-macroscoresof27.62%and28.30%fortheFear,Joy , andSurprise. We providedthedetailedclass-wise second andthirdensembleapproaches,respectively.performances onselectedmodelsinFigure7. Wepresent class-wise best-performingmodelsforemotionanalysisinTableIII(bottom)presentstheperformanceofthethird Figure 6.strategy onthesentimentdataset.Despitethepoorperfor- mance ontheemotiondataset,thethirdstrategydeliversFigure 8andTableIVpresentthedetailedclass-wise good performance on the sentiment dataset. The first ensembleresultsfortheselectedmodels.Wealsoana- approach outperformedalltheexperimentswithanF1-macrolyzed theclass-wiseperformanceforthefirstexperimental score of54.67%,whiletheothertwoensembleapproachesstrategy onthesentimentdataset.Wenoticedthatallthe outperformed allthemodelsexceptCodeBERT. We achievedperformed better,for the XLM-RoBERTa-large

### Trust

F1-macro scoresof52.85%and52.35%forthesecondandmodel, comparedtotheemotiondatasetperformance.The third ensemble approaches. Therefore, the performance on theXLM-RoBERTa-largemodelpredictsonlythepositiveclass. emotion datasetafterapplyingensemblelearningdecreasedHowever,the classical model and random forest show the best by4%−12% . However,ensemblelearningprovidestheperformance ontheNegativeandNeutralclasses, whereas

### Surprise

best performanceonthesentimentdataset.TheobservedCodeBERTexhibitssuperioronthepositive decrease in performance for the emotion dataset and the slightclass. Moreover,theonthesentiment improvement forthesentimentdatasetsuggestthatensembleis superiortothatontheemotiondataset;specifically,the learning isnotalwaysbeneficial,anditseffectivenessmayhigher numberofclassesintheemotiondatasetleadsto vary dependingonthechosenapproach.poorer performance. We expect that a well-balanced and better human-annotated dataset will yield good performance for both V.DISCUSSIONSemotion andsentimentanalysis,asevidencedbytheresults. explored three different ensemble learning approaches toFor thefirststrategy, allthemodelsstruggledtopredictthe We understand the performance of emotion and sentiment analysis.Fear,Joy , andSadnessclasses, whilethepredictionforthe

435

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.

40

### RF

### Bidirectional LSTM

### CommitBART

### CodeBERT

### XLM-RoBERTa-large

### T5-Commit-Generator

50

### Anger

60


---

<!-- Página 8 -->

TABLEIV: Class-wise performances on selected models for the first experiment strategy on the emotion dataset.indicates the bestperformancefortheclass.

**Model**

Anger FearFear JoyJoy RandomNeutralXLM-RoBERTa-large Sadness Surprise Trust Anger

### Neutral

FearFear JoyJoy BidirectionalNeutralT5**54.83** Sadness Surprise Trust Anger**40.16** FearFear**27.89** Joy**24.85**Joy NeutralCommitBARTCodeBERT **25.05**Sadness Surprise**13.14** Trust**51.72**

TABLEV:Exampleofcontradictorydataannotationinthe training set.

**hash**

d4c330cfdc2610f86d1cbfda8244797461804577 a15025606e31db384d1ec23f5ac17c4a49bd9579 cea7a21e61fe55220bda12ace665c33028ed2d02 2704d89e3aa279bf791ef4a7c793a30d5d53e55c

1020304050

### Negative

In ourexperiments,theensemblelearningapproachesdid not performasexpectedontheemotiondataset,whereas they exhibitedsuperiorperformanceonthesentimentdataset. This demonstratesthatensemblelearningiseffectivefor performance improvement in sentiment analysis. For the emo- tion dataset,thefirstensembleapproachonlypredictsthe Anger,Neutral, andTrustclasses, whileitprovidesthebest Fig. 8:Class-wiseperformancesonselectedmodelsfortheperformance onthesentimentdataset.Theon first experimentstrategyonthesentimentdataset.the emotiondatasetsignificantlydecreasedduetothelarge number of emotion classes compared to the sentiment dataset. Although deeplearningandpre-trainedLMsprovidecom-Weidentifiedthatcapturinghumanfeelingsischallenging parative results, their performances are below 33% for emotionif thetextcontainsinsufficientinformation.Forexample, analysis inourstudy. We investigated thedataqualitytogetafixing animportantbugorfeaturemightleadtojoy(posi- more insightfulconclusion.We foundthatthemanualannota-tive), whereasfixingsomeminorissuesmightleadtoanger tion process yielded conflicting labels for similar kinds of data.(negative).However,thecommitmessagesforbothcases TableV presents an example of contradictory annotation fromare similar.Wealsonoticedthatmosttextscontainnoise, our training data. Also, due to the biases among the annotators,such asclassnames,methodversions,andpackage the qualityofdataannotationisflawed.Furthermore,weinformation. Thesenoisesaffecttheoverallperformanceof found that15%of thetrainingdataconsistsoftwoorthreethe models because they occur in multiple emotion categories. words. AlthoughcapturingtheemotionsandsentimentfromRemoving suchnoisesrequiresmanualeffortsbecauseofthe a sentenceoftwoorthreewordsischallenging,wedidnotunstructured representationoftexts.

### Positive

remove thosetexts.Wedidnotthetwo-orthree- A. Comparisonword textstounderstandtheperformancesacrossthemodels because a significant number of commit messages are of shortTableVIshowsaperformancecomparisonamongvarious text length.studies intheliterature.Somehavenotevaluatedau-

436

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.

### RF

### Bidirectional LSTM

### CommitBART

### CodeBERT

### XLM-RoBERTa-large

### T5-Commit-Generator

6070


---

<!-- Página 9 -->

Studies AnalysisDatasetClassesBestF1Score

(2014) Guzmanetal.[21 ] SentimentGitHubcommitcomments2- (2016) Sinhaetal.[25 ] SentimentGitHubcommitcomments3- (2017) Thelwall [26 ] EmotionTweets254.45% (2018) IslamandZibran[12 ] EmotionJiraissuecomments478.43% (2019) Islametal.[7 ] EmotionJiraandstackoverflow comments580.90% (2021) Venigalla andChimalakonda[10 ] EmotionGithubcommitcomments8- (2022) Imranetal.[27 ] EmotionGitHubcomments648% (2024) Imranetal.[29 ] EmotionGitHub,Jira,andStackoverflow comments659.20% (2024) Topal etal.[30 ] EmotionTweets436.5%-56.3% Our StudyEmotionGitHubcommitcomments632.70% Our StudySentimentGitHubcommitcomments354.67%

TABLEVI:ComparisonofExistingStudiesonEmotionandSentimentAnalysisinSE.

annotations aresubjective,andtheannotatorsbasetheiran-tomated methodsforidentifyingemotionandsentiment,e.g., notations ontheirunderstanding,whichmayintroducebiases[ 10 ], [21 ], [25 ]. Overall,studiesconsideringfeweremotion or sentimentclassesperformedwell,e.g.,[12 ]. Dependinginto our dataset. Therefore, it is crucial to account for annotator bias whendevelopingmodelsutilizingcurateddatasets.Theon thedataset,theperformanceofmachinelearningand hyper-parameters weusedtotrainourmodelsrequirefur-deep learning,aswellaslargelanguagemodels,alsovaries ther investigationandexperimentsforoptimalperformance.significantly.Thus,benchmarkingisextremelychallenging Investigatingoptimalhyper-parameterswasnotwithinthein emotionandsentimentanalysisintheSEdomain.Early thisstudy,i.e.,weaimedtoexploreemotionsandstudies (e.g.,[7 ], [12 ]) usedtraditionalmachinelearningscope of models, whereas more recent studies (e.g., [ 29], [ 30]) exploredsentiments inthecommitmessages.Ourexperimentsmay yield betterresultswithoptimalhyper-parameters.Wehavethe ability of computationally expensive large language models made model implementations and the curated dataset availableand fine-tuned them. However, researchers should consider the for replication.trade-off betweencostandbenefitswhileanalyzingemotion and sentimentinthesoftwareengineeringdomain. VI. CONCLUSIONF UTUREW ORK B. ImplicationsforResearchers andDevelopersThis studypresentsthelargestmanuallyannotateddataset The literature on emotion and sentiment analysis of commitforandonmessagesand messages lacksmanuallyannotateddata.Asaresult,studiesreports the performance of pre-trained language models (LMs), on emotionandsentimentanalysisusingcommitmessagesdeep learning,traditionalmachineandtheensemble have notattractedmanyresearchers.Ourstudyprovidedtheof pre-trainedLMsinpredictingemotionandsentiment. largest human-annotateddatasetforemotionandsentimentOur firstexperimentalstrategytoaddressRQ1showedthat analysis, which may attract the research community to explorestate-of-the-art machinelearningmodelsperformbetteron this area.Moreover, ourfindingssuggestthatagoodannota-the sentimentdatasetthantheemotiondataset.TheRQ2 tion guideline is required for constructing a better dataset usingdemonstrated that the oversampling technique in our study did commit messages.Thisstudyaimstoexploredevelopers’not perform well. Furthermore, findings in RQ2 suggested that emotions and sentiments expressed in commit messages; thus,incorporating ensemblelearningimproves theperformanceof devising high-performingmachinelearningmodelswasnot the sentimentdatasetwhilenegativelyimpactingtheperfor- the primarygoalofthisstudy.mance oftheemotiondataset.Wealsoprovidedadetailed performance comparisonamongthemodels.Our studyshowsthatdevelopersmostlyuseneutraland Weconducted all the experiments using the proposed datasettrustemotions whilewritingcommitmessages.However,a and providedanin-depthanalysis.Ourresultsindicatethatsignificant numberofcommitmessagescontainangerand pre-trainedLMsoutperformedtheclassicalandsadness, indicatingthatdevelopersoftenwritecodewithwhile the deep learning algorithms, their performance was insufficient tonegativeemotions,whichcanimpacttheproject’squality. identify emotionsaccurately.AlthoughtheannotationoftheMoreover,wefoundthatdevelopersdonotwritelongtext ( ∼ 80% ofcommitmessagesarewithin20words)indataset showedmoderateagreement,theadvancementofpre- trained LMs for commit messages has yet to be studied. More-messages. Thus, we strongly recommend that developers write adetailedannotationguidelineisrequiredtoconstructamore expressiveandmeaningfulcommitmessages,which over, new datasetforthisarea.Wealsoidentifiedthechallengesoffer severalbenefits(e.g.,issuetracking),duringbothsoft- of determiningtheunderlyingmeaningofthetext,whichware development andmaintenanceandevolution phases.We also foundthatdevelopers expressdifferentemotionswithoutcaused low performance across the models. In addition, further significant changesinthecommitmessages.Themanualstudy ofthepre-trainedmodelrepresentsanotherpromising direction, andwewillincorporatenewpre-trainedmodelsannotation ofthedatasetishighlyimbalanced,whichmay messagesinourfuturestudies.Wealsoaimtosignificantly impactthemodel’sperformance.Moreover,the for commit

437

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.


---

<!-- Página 10 -->

develop amorediversedatasetthatwouldbetterdemonstrate[16] Recommendingthe robustnessoftheproposedapproach. sourced2015 ence, pagesA CKNOWLEDGMENT IEEE, This studyissupportedbytheNewBrunswickInnovation[17] usFoundation (NBIF)throughtheGrantTRF2023-003.The KSII, 13(8),authors would like tothankMd.AridHasanforinitiatingthis [18] work andtheannotatorsforlabelingthedataset.the national, R EFERENCESpages [19][1] ValeriaNovielli, basedProceedingsment:ACM Conference, pagesEngineering, 31(3):1–41, 464–471.[2] [20]Ming inProceedingsCodebert: meeting, pagesarXiv, 2020. [21]ocar,[3] commitJenks, 11th, pagesFu, 355,In Proceedings [22]Conference, Kappas.Jour-pages nal,[4] 61(12):2544–2558,processing [23]software.Applied, 12(21):10773, model[5] the, volumefor2017 pagesference [24]and, pages Novielli.Pro-In[6] ceedings,Do pagessoftwareProceedings [25]mining, pages sentimentProceedings[7] conference, pagesValous: [26]arousalProceedings tionInformation,ACM/SIGAPP, pages 53(1):106–121,2019. [27][8] Damevski.domain inProceedingsingJournal, 145:125–146, IEEE/ACM[9] ing , pagessentimentProceedings [28]International, Liu.pages AnalysisProceedings[10] ACMemotions symposium, pages2021 2019.ing:, pages [29]2021. Uncovering[11] cationProceedingsHill. International, pagesare [30]Workshop, pages Analysis2018. gies,Proceedings[12] Conferenceengineering (CASCON),2024.international [31]ing, pages EmotionJour-[13] nal, 52(6):1061,theProceedings [32]of, pages Theories, pages1543, [33][14] andtrainedarXiv, Educational, 33(3):613–619,2022. [15] ´hary,an, Luke representationarXiv, 2019.

438

Authorized licensed use limited to: University of New Brunswick. Downloaded on February 13,2026 at 02:39:02 UTC from IEEE Xplore. Restrictions apply.


---

