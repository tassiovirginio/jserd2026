<!-- Página 1 -->

## arXiv:2604.13826v1  [cs.SE]  15 Apr 2026

## Sentiment

## analysis

## for

## software

## engineering:

## How

## far

## can

## zero-shot

## learning

## (ZSL)

## go?

### Reem Alfayez

### Manal Binkhonain

### Department of

### Software

### Engineering,

### College

### of

### Computer

### and

### Information Sciences,

### King Saud

### University, P.O.

### Box

### 51178,

### Riyadh

### 11543,

### Saudi

### Arabia

### reealfayez@ksu.edu.sa

### Received: date

### /

### Accepted:

### date

**Abstract**

**Context: Sentiment**analysisinsoftwareengineeringfocuseson understanding emotionsexpressedinsoftwareartifacts.Previousre- search highlighted the limitations of applying general off-the-shelf sen- timent analysistoolswithinthesoftwareengineeringdomainand indicated theneedforspecializedtoolstailoredtovarioussoftware engineering contexts.Thedevelopmentofsuchtoolsheavilyrelies on supervisedmachine learningtechniques thatnecessitateannotated datasets. Acquiringsuchdatasetsisasubstantialchallenge,asit requires domain-specificexpertiseandsignificanteffort.Objective: This studyexploresthepotentialofzero-shotlearning(ZSL)toad- dress thescarcityofannotateddatasetsinsentimentanalysiswithin softwareengineeringMethod:Weconductedanempiricalexperi- ment to evaluate the performanceof various ZSL techniques, including embedding-based, naturallanguage inference (NLI)-based, task-aware representation ofsentences(TARS)-based, andgenerative-basedZSL techniques. Weassessedtheperformanceofthesetechniquesunder different labelssetupstoexaminetheimpactoflabelconfigurations. Additionally,wecomparedtheresultsoftheZSLtechniqueswith

1


---

<!-- Página 2 -->

state-of-the-art fine-tunedtransformer-basedmodels.Finally,weper- formed an error analysis to identify the primary causes of misclassifica- tions. Results:OurfindingsdemonstratethatZSLtechniques,par- ticularly those combining expert-curatedlabelswith embedding-based or generative-basedmodels,canachievemacro-F1scorescomparable to fine-tunedtransformer-basedmodels.Theerroranalysisrevealed that subjectivityinannotationandpolarfactsarethemaincontribu- tors toZSLmisclassifications.Conclusion:Thisstudydemonstrates the potentialofZSLforsentimentanalysisinsoftwareengineering. ZSL canprovideasolutiontothechallengeofannotateddataset scarcity byreducingrelianceonannotateddataset.

Keywords: SentimentAnalysis,SoftwareEngineering,NaturalLan- guage Processing,Zero-shotLearning,Text Classification

### 1 Introduction

Over theyears,sentimentanalysishasevolvedasapowerfultoolforex- tracting subjectiveinformationfromtextdata[1].Insoftwareengineering, it providesinsightsintosoftwaredevelopmentandusagebyanalyzingapp reviews, developercommunications,discussionsontechnicalQ&Awebsites, and more[1,2,3,4,5,6,7,8]. Utilizing sentiment analysis within the software engineering domain presents significant challenges. General-purposesentiment analysis toolsoften demon- strate suboptimalperformancewhenusedinsoftwareengineeringcontexts [9, 10]. Thislimitation has led researchers to develop specialized tools tailored to theuniquecharacteristicsofsoftwareengineeringcontexts.Despitethese efforts, ithasbeenobservedthatevensentimentanalysistoolsthatperform well inonesoftwareengineeringcontextlackgeneralizabilityacrossdifferent contexts, wheretheyunderperforminthenewcontexts.Thecontext-bound limitation highlightstheneedforcontext-specifictools[3,4,11]. Developing context-basedtoolsisnotaneasyfeat,asmostsentiment analysis toolsinsoftware engineeringarebasedonsupervisedmachine learn- ing techniques thatframesentiment analysistasksastextclassificationprob- lems. Thesetoolsareheavilyreliantonannotateddatasetsfortraining, which iscostly,time-consuming,error-prone,andrequiresdomain-specific expertise toobtain[2,4,11,12]. This relianceonannotateddatasetsisparticularlyproblematicduetothe context-bound limitationthatrequiresthedevelopmentofseparatemodels and datasetsforeachspecificcontext[4,11].Theneedtocurateanno- tated datasetfortrainingineachcontextfurtherintensifiesthechallenge

2


---

<!-- Página 3 -->

of datasets analysis models Zero-shot learning to address fication tasks. to specific between words, of ZSL, trained on process. The other datasets task [13, This study ware engineering ence (NLI)-based, generative-based ZSL pact of performing ZSL An error The rest for text the study them. Section the paper.

### 2 Zero-shot

ZSL text enables models posed to class, ZSL dict previously labeled data through four and generative-based nique.

scarcityandcomplicatesthedevelopmentofeffectivesentiment [2,4,11]. (ZSL)isapromisingapproachthathasthepotential thechallengeofrequiringcontext-specifictrainingdataforclassi- AZSL-basedmodelcanclassifydatawithoutpriorexposure labels,whereitinsteadreliesonitsunderstandingofrelationships phrases,andconceptstomakeclassifications.Inthecontext amodelgeneratespredictionsfortasksithasnotbeenexplicitly byleveragingdatafromother,relatedtaskstoaiditslearning modelutilizesknowledgeacquiredthroughpre-trainingon andtransfersrelevantinformationtothenewclassification 14]. exploresthepotentialofZSLforsentimentanalysisinsoft- byevaluatingembedding-based,naturallanguageinfer- task-aware representation ofsentences (TARS)-based, and techniquesacrossvariouscontexts.Weassesstheim- labelconfigurationsonmodelperformanceandcomparethebest- modelswithstate-of-the-artfine-tunedtransformermodels. analysisisalsoconductedtounderstandmisclassificationcauses. ofthepaperisorganizedasfollows:Section2summarizesZSL classification.Section3reviewsrelatedstudies.4describes setup.Section5presentstheresults,and6discusses 7outlinespotentialvaliditythreats,and8concludes

### learning

### (ZSL)

### text

### classification

classificationisanaturallanguageprocessing(NLP)approachthat toclassifytextintounseenclassesduringtraining.Asop- traditionalsupervisedlearning,whichrequireslabeleddataforeach leveragestransferlearningandsemanticunderstandingtopre- unseenclasses.Thiscapabilityisparticularlyusefulwhen isscarce[13,14].ZSLtextclassificationcanbeachieved maintechniques:embedding-based,NLI-based,TARS-based, techniques.Belowisabriefdescriptionofeachtech-

3


---

<!-- Página 4 -->

### 2.1 Embedding-based

Embedding-based ZSL the semantic While the opted for these models syntactic and 16]. Figure 1 tion. Both pre-trained LLM culating the class label selected as

### 2.2 Natural

NLI-based ZSL where it other hypothesis. candidate label tailment and The text [14, 17]. As Figure class labels entails or The input probability,

### ZSL

textclassificationuseswordembeddingstomeasure similaritybetweeninputtextandpotentialclasslabels[15]. originalapproach[15]reliedonskip-gramstaticembeddings,we transformer-basedlargelanguagemodels(LLMs)embeddings,as generatecontextualwordembeddingsthatcaptureboththe semanticpropertiesofwords,alongwiththeircontext[13,14,

illustratestheprocessofembedding-basedZSLtextclassifica- theinputtextandpotentialclasslabelsarepassedthrougha togenerateembeddings.Classificationisperformedbycal- cosinesimilaritybetweentheinputtextembeddingandeach embedding.Thewiththehighestsimilarityscoreisthen thepredictedlabel(i.e.,1intheexample).

Figure 1:Anillustrationofembedding-basedZSL

### language

### inference

### (NLI)-based

### ZSL

framestextclassificationasatextualentailmentproblem, determineswhetheragiventext(i.e.,premise)logicallyfollowsan- TheinputtextistreatedastheNLIpremise,andeach forms a hypothesis. Themodelcalculates probabilities for en- contradiction, whicharethenconverted into labelprobabilities. isclassifiedunderthelabelwiththehighestentailment probability

2presents,theinputtextservesasthepremise,andpotential arehypotheses.TheNLImodelassesseswhetherthepremise contradictseachhypothesisandassignsaprobabilitytoeachcase. textisclassifiedbasedonthelabelwiththehighestentailment inthiscase,label1.

4


---

<!-- Página 5 -->

Figure 2:AnillustrationofNLI-basedZSL

### 2.3 Task-aware

### representation

### of

### sentences

### (TARS)-

### based ZSL

TARSformulatestheclassificationtaskasauniversalbinary problem, wherethemodellearnstopredictwhetheragiventextbelongsto a particularlabelornot.Insteadoftrainingseparatemodelsforeachlabel, TARSsimultaneouslyevaluatestherelevanceofthetextforalllabelsby adapting LLMrepresentationsthroughlabel-conditionedembeddings[18]. As Figure3illustrates,theinputtoTARSconsistsofthetexttobe classified andasetofcandidatelabels.TARSgeneratesembeddingscondi- tioned onboththetextandeachlabelbyappendingthetothetextto form queries.Thesequeriesareprocessedbyasharedtransformerencoder to producetask-specificembeddingsthatcapturethesemanticrelationships between thetextandthelabels.Abinarypredictionoftrueorfalseisthen performed foreachlabel.Thelabelwiththehighesttrueconfidenceisse- lected asthefinalclassification(i.e.,label1intheexample)[18].

Figure 3:AnillustrationofTARS-based ZSL

### 2.4 Generative-based

### ZSL

Transformer-basedgenerativemodels,suchasOpenAI’sGenerativePre- 1TrainedTransformers(GPTs), arecapabletoperformZSLtextclassifica-

1[https://openai.com/](https://openai.com/)

5


---

<!-- Página 6 -->

tion bygeneratingtextinresponsetoprovidedinput[19]. In thisapproach,asFigure4depicts,themodelreceivesapromptthat provides specificinstructions on how to classify input text and thetext. The providedinstructionisinnaturallanguage,anditmaynotincludeany demonstrations. Themodelthengeneratesaresponsethatindicatesthe most appropriateclassbasedontheprovidedprompt[14,19].

Figure 4:Anillustrationofgenerative-basedZSL

### 3 Related

### work

Many studieshaveassessedsentimentanalysistools,exploredtheimpact of sentimentonsoftwaredevelopmentpractices,andmore.Duetospace constraints, wefocusonsummarizing(1)systematicreviewsrelatedtosen- timent analysistoolsinsoftwareengineeringand(2)researcheffortsonthe developmentofsuchtools.

### 3.1 Systematic

### reviews

### on

### sentiment

### analysis

### tools

### for

### software

### engineering

S´anchez-Gord´onandColomo-Palacios[20]conductedasystematicliterature review (SLR)onsoftwaredevelopers’emotions.Thestudyhighlightedthe limited researchinthisdomainandnotedthatalthoughcurrentapproaches are recognizedasunreliable,manytechniqueswiththepotentialtoenhance the detectionofdevelopers’emotionsremainunderutilizedorunexplored. Obaidi andKl¨under[3]conductedanSLRonsoftwareengineeringsen- timent analysistools.Thestudyfoundthatmostresearchreliesonusing existing tools,supportvectormachine(SVM)isthemostutilizedtechnique, and open-sourcesoftware(OSS)projectsarethemaindatasource.The study highlightedthechallengesoftrainingdatascarcity,inconsistenttool performance, andthesubjectivityofannotateddata.Thestudyalsonoted that sarcasmandironydetectionremainsamajorchallengeinsentiment analysis forsoftwareengineering.

6


---

<!-- Página 7 -->

In afollow-upsystematicmappingreview(SMR),Obaidietal.[21] expanded the previous analysis to include recent sentimentstudies in softwareengineering.Thestudyconfirmedthatresearchstillpredominantly applies existingsentimentanalysistoolsratherthandevelopingnewones, OSS dataremainsthemostusedsoure,SVMandgradientboostingtree (GBT) wereidentifiedasthemostcommonsupervisedlearningtechniques, and thatfine-tunedtransformermodelsoutperformotherapproaches.The study alsohighlightedtheunreliabilityofgeneralsentimentanalysistools and theneedforcustomizationtospecificsoftwareengineeringcontexts. Lin etal.[12]conductedanSLRthatidentifiedsentimentanalysistools currently inuseandraisedconcernsabouttheirapplicationinunintended domains withoutpropervalidation.Thereviewsummarizedcomparisonsof these tools,identifiedpubliclyavailable datasets,andhighlightedchallenges in softwareengineeringsentimentanalysis,suchasidentifyingneutralsenti- ment. Thestudyemphasizedthatmodelquality dependsontrainingdataset quality andnotedtheconsiderableeffortneededtotrainsupervisedmachine learning models.

### 3.2 Sentiment

### analysis

### tools

### for

### software

### engineering

Several sentiment analysis toolshave beendeveloped for software engineering utilizing avariety ofNLPandmachinelearningapproaches.Heuristic-based methods wereemployed byIslametal.[22]andandZibran[23].SVM were utilizedbyCalefatoetal.[8],Islametal.[24],Murgiaetal.[25],and Cagnoni etal.[26].EnsembleapproacheswereadoptedbyUddinetal.[27], Ahmed etal.[28],andDingetal.[29]. Aiming toleveragetransformer-basedmodels,Biswasetal.[30]intro- duced BERT4SentiSE, a BERT-based sentiment classifier fine-tuned on Stack Overflow(SO)posts.Zhangetal.[1]assessedtheperformanceofBERT, RoBERTa,XLNet,andALBERT pre-trainedtransformermodelsacrossvar- ious softwareengineeringcontexts,andtheyfoundthatfine-tuningthese models outperformsstate-of-the-artsentimentanalysistools.Similarly,Ba- tra etal.[31]evaluatedfine-tunedBERT,ensembleBERTmodels,and compressed BERT forsentiment analysisonSOposts,GitHubcommitcom- ments, andJiraissuecomments.ThestudyfoundthatcompressedBERT and ensembleBERTproducedbettersimilarresults,withthecompressed version recommendedforresourceconservation.Bleyletal.[32]developed a fine-tunedBERT modelfordetectingemotionsinSOposts.Additionally, Sun etal.[33]introducedEASTER,asentiment analysistoolthatintegrates RoBERTaastheembeddinglayerinTextCNN.EASTERwasevaluatedon app reviews,Jiraissuecomments,andSOposts.

7


---

<!-- Página 8 -->

Shafikuzzaman etal.[34]evaluated theperformanceoftwelve pretrained language models,includingfine-tunedSentiStrength-SE,andSen- tiCR [28]ontheGerrit,GitHub,GooglePlay, Jira,andSOpostsdatasets. The studyfoundthatmodelperformancevariedacrossdatasets,withfine- tuned modelsperformingbetteronlargerdatasets.Tounderstand models’ behavior,thestudyusedShapleyAdditiveExplanations(SHAP) to conducterroranalysis.Leveraginggenerative-basedmodels,Zhanget al. [2]exploredthepotentialofLlama2-Chat;Vicuna;andWizardLM,re- ferred toaslargerlanguagemodels(bLLMs),forsentimentanalysis.The study assessedtheirperformanceusingZSLandfew-shotlearning(FSL)on sentimentanalysistasksacrossfivedatasets:Gerrit,GitHub,GooglePlay, Jira, andSO.Duetocostconcerns,thestudywasconductedonastrati- fied representativesampledrawnfrom10%ofeachdatasetthatrepresents the testset.Thefindingsindicatednosignificantperformancedifference between ZSLandFSLandthatFSLdidnotnecessarilyoutperformZSL. The analysiswasextendedbyfine-tuningBERT, RoBERTa, ALBERT, XL- Net, andDistilBERT, referredtoassmallerlanguagemodels(sLLMs).The comparison ofthesLLMstothebLLMsrevealedthatoutperformed sLLMs onimbalanceddatasetsorthosewithlimitedtrainingdata,while fine-tuned sLLMsperformedbetterwhenampletrainingdataandbalanced distributions wereavailable.

### 4 Study

### setup

This sectiondescribesthesetupofthestudy, includingthegoalandresearch questions (RQs),datasets,selectedLLMs,labelcurationandconfiguration, performance measures,statisticalanalysis,andimplementationdetails.

### 4.1 Goal

### and

### research

### questions

### (RQs)

The goalofthisstudyisdefinedusingtheGoal-Question-Metric(GQM) template [35],asfollows: Assessing theperformanceofZSLinsentimentclassificationwithinthe context ofAPIreviews,codereviewcomments,pullrequestsandcommit comments, developermessages,mobileappreviews,issueand posts ontechnicalquestion-and-answerwebsitesinthesoftwareengineering domain. Toachievethisgoal,weformulatedthefollowingRQs:

• RQ1:WhichZSLtechniqueismosteffectiveforsentimentclassifica- tion, andamongthetechniquesthatevaluatemultiplemodels,which model demonstratesthebestperformance?

8


---

<!-- Página 9 -->

• RQ2:Dodifferentlabelconfigurationshaveanimpactontheperfor- mance ofZSL-basedsentimentclassification?

• RQ3:HowdoestheperformanceofZSL-basedmodelscomparewith that ofthestate-of-the-artfine-tunedtransformer-basedmodelsinsen- timent classification?

• RQ4:Whatfactorscontributetothemisclassificationofsentiment labels inZSL-basedmodels,andhowdothesecomparewiththose shared withthestate-of-the-artfine-tunedtransformer-basedmodels?

### 4.2 Datasets

ToaddresstheRQs,weutilizedsevenpubliclyavailable datasetscommonly used for sentiment analysis in software engineering. Table1 summarizes these datasets, andadescriptionofeachisprovidedbelow. API reviews:Thedataset,curatedbyUddinandKhomh[7],contains 4,522 sentencesfrom1,338SOpostsacross71threadstaggedwith18Java API-related keywords.Thedatasetincludes890positive,496negative,and 3,136 neutralsentences. Gerrit: Thedataset,curatedbyAhmedetal.[28],includes1,600code review commentsminedfromthecoderepositoriesof20open-source projects, with398labeledasnegativeand1,202asnon-negative. GitHub: Thedataset,curatedbyNoviellietal.[6],consistsof7,122 GitHub pullrequestandcommitcomments,labeledas2,013positive,2,087 negative, and3,022neutral. Gitter: Thedataset,curatedbySajadietal.[5],contains400developer messages from10Gittercommunities. Messageswere annotatedforsixbasic emotions (i.e.,anger,love, fear,joy, sadness,andsurprise)andsubcategories based onShaver’semotiontaxonomy[36].Followingtheapproachof[4],we mapped love andjoy topositive,andangerandsadnesstonegative, resulting in 201messageswith127positiveand74negative. Google Play:Thedataset,curatedbyLinetal.[4],contains341 Android appreviewsfromGooglePlay, with186labeledaspositive,130as negative, and25asneutral. Jira: Thedataset,curatedbyLinetal.[4],contains926sentencesfrom Jira issuecomments,with636labeledasnegativeand290aspositive. SO: Thedataset,curatedbyCalefatoetal.[8],includes4,423SOposts, with 1,527positive,1,202negative,and1,694neutral.

9


---

<!-- Página 10 -->

Table1:Summaryofutilizeddatasets

**Dataset**

API Gerrit GitHub Gitter Google Jira SO

### 4.3 Large

### language

### model

### (LLM)

### selection

Toaddresstheaforementionedresearchquestions(RQs),weselectedthe models below.Table2summarizesthesemodels,withuniqueidentifierfor easy referencethroughoutthestudy. Our selectionwasguidedbyfourkeyconsiderations.First,weprior- itized reproducibilityandaccessibilitybyincludingpubliclyavailableand widely adoptedpretrainedmodelssuchasBERT, RoBERTa, andALBERT, which arewell-establishedbenchmarksinZSLandtransferlearningresearch [2, 16]. Second,to ensure architectural diversity, we selected transformer vari- ants trainedwithdistinctpretrainingobjectives,includingmaskedlanguage modeling, permutationandnext-sentenceprediction.Third,we sought domainvariationbyincorporatingbothgenericanddomain-specific models. Forinstance,BERTOverflowfortechnicalQ&A,RoBERTa-base- emotions foremotions,andTwitter-RoBERTa forsocialmediasentimentgo analysis. Finally,tocaptureabroadavailability spectrum,weincludedboth paid andunpaidmodels.

• Embedding-basedZSL:Weselectedthefollowingunpaid,generic- 23embeddings: BERT-base-uncased, RoBERTa-base, DistilBERT- 456base-uncased, ALBERT-base-v2, XLNet-base-cased:, andAll- 7MiniLM-L12-v2.

Besides theaforementionedunpaid,genericmodels,weutilizedthe 8following unpaid,domain-specificmodels:BERTOverflow,RoBERTa- 2[https://huggingface.co/google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) 3[https://huggingface.co/FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base) 4[https://huggingface.co/distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) 5[https://huggingface.co/albert/albert-base-v2](https://huggingface.co/albert/albert-base-v2) 6[https://huggingface.co/xlnet/xlnet-base-cased](https://huggingface.co/xlnet/xlnet-base-cased) 7[https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) 8[https://huggingface.co/jeniya/BERTOverflow](https://huggingface.co/jeniya/BERTOverflow)

10


---

<!-- Página 11 -->

910base-goemotions, andTwitter-RoBERTa-base-sentiment. 11WealsoincludedthreepaidOpenAIembeddings: Text-embedding- ada-002, Text-embedding-3-small, andText-embedding-3-large.

• NLI-basedZSL: ToevaluatetheperformanceofZSL,we selected thefollowingfourmodelsthatarespecializedforNLItasks: 1213RoBERTa-large-mnli,Cross-encoder/nli-deberta-base, BART-large- 1415mnli, andDeBERTa-v3-large-mnli-fever-anli-ling-wanli.

• TARS: Weusedthemodelimplementationfromtheoriginalpaper that introducedthetechnique[18].

• Generative-basedZSL: Forgenerative-basedZSL,weusedGPT- 163.5 Turbo(gpt-3.5-turbo-0125), asitwasthemostviableoptionin terms ofefficiencyandcostatthetimeofconductingthestudy(i.e., May 2024).

Table2:SelectedmodelsforeachZSLtechnique

**Approach**

Embedding-basedM1 RoBERTa-baseM2 DistilBERT-base-uncasedM3 ALBERT-base-v2M4 XLNet-base-casedM5 All-MiniLM-L12-v2M6 BERTOverflowM7 RoBERTa-base-goemotionsM8 Twitter-RoBERTa-base-sentimentM9 Text-embedding-ada-002M10 Text-embedding-3-smallM11 Text-embedding-3-largeM12

NLI-basedM1 Cross-encoder/nli-deberta-baseM2 BART-large-mnliM3 DeBERTa-v3-large-mnli-fever-anli-ling-wanliM4

TARS-basedM1

Generative-basedM1

9[https://huggingface.co/SamLowe/roberta-base-goemotions](https://huggingface.co/SamLowe/roberta-base-goemotions) 10[https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) 11[https://openai.com/index/new-embedding-models-and-api-updates/](https://openai.com/index/new-embedding-models-and-api-updates/) 12[https://huggingface.co/FacebookAI/roberta-large-mnli](https://huggingface.co/FacebookAI/roberta-large-mnli) 13[https://huggingface.co/cross-encoder/nli-deberta-base](https://huggingface.co/cross-encoder/nli-deberta-base) 14[https://huggingface.co/facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) 15[https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli](https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli) 16[https://platform.openai.com/docs/models#gpt-3-5-turbo](https://platform.openai.com/docs/models#gpt-3-5-turbo)

11


---

<!-- Página 12 -->

### 4.4 Label

### curation

### and

### configuration

Toinvestigatetheimpactoflabelconfigurationsonsentimentanalysis,we compare threedistincttypes:theoriginaldataset,expert-curated,andLLM- generated labels.Theseconfigurationsdifferinphrasing,contextualspeci- ficity,anddescriptivegranularity.Whiletheoriginallabelsperformwell on standardbenchmarks,weaimtoexplorewhetherenrichingthemwith descriptions andcontextualcuescanimprovemodelperformanceinaZSL setting. Specifically,includingcontextualinformationaboutthedatasetin- stance typemayhelpmodelsbetterinterprettheinput,whileaddingsenti- ment descriptorscanenhancethesemantic richness ofthelabelsandimprove embedding quality. Weincludebothexpert-curatedandLLM-generatedlabelstoinvestigate twoapproachestoenrichinglabelsemantics.Expert-curatedlabelsoffer human-leveldomaininsight, withthepotentialtocapturesubtledistinctions and contextualrelevancethatmaybeoverlookedintheoriginallabels.In contrast, LLM-generatedlabelsprovideascalable,automatedalternative that reflectsthemodel’sowninterpretationofsentiment.Comparingboth approaches allowsustoassessthetrade-offsbetweenhumanjudgmentand automated labelgenerationandtoexaminewhethereitherleadstoimproved performance inZSLsettingsovertheoriginallabels. Table3summarizestheselabelswithidentifiers andexamples.Moreover, 17our onlineappendixincludesthefullsetofutilizedlabels. Itisimportant to notethatallalternativelabelswerederivedbymappingtotheoriginal label set,withnoreannotationofthedatasetinstancesinvolved.

• Originallabels:Weused the original sentiment labels from the datasets as describedinSection4.2.

• Expert-curatedlabels:Thetwoauthorsindependentlycreatedla- bels basedontheirunderstandingofthesentimentclassesanddataset context. Theselabelswerethenreviewedandconsolidatedinajoint meeting, wheretwotypesofdisagreementsemerged.Phrasedisagree- ments, inwhichoneauthorused“with”whiletheotherused“has” to describeinstances.Afterdiscussion,theauthorsdecidedthatusing “with” was moreappropriate.Theothertypeiscontent disagreements, where oneauthorusedtheoriginalsetofemotionsmappedtosenti- ments, whiletheotherdidnot.Theauthorsdecidedtoretainthese labels, astheycouldimproveunderstandingoftheimpactoflabels. 17[https://osf.io/gzt9r/?view_only=afd4a24f2d724413aa5423eac0cdcfa6](https://osf.io/gzt9r/?view_only=afd4a24f2d724413aa5423eac0cdcfa6)

12


---

<!-- Página 13 -->

• LLM-generatedlabels:Weused ChatGPT-3.5 to generate labelsus- ing thefollowingprompt:“Generatealistofwordsthatbestdescribe positivesentiment.”. Theterm“positive”wasreplacedwith“nega- tive” togeneratewordsfornegativesentiment,andtheresultsofboth were negatedtogenerateneutrallabels.Theresultformedtwolabel configurations: L6usingChatGPT-suggestedwordsandL7a combination ofsuggestedwordsandcorrespondingsentimentclasses.

### 4.5 Performance

### measures

Toevaluatetheperformanceofthemodels,wecalculatedbothmacro-F1 and micro-F1scores,whicharevariationsoftheF1score[37],followingthe approach ofprevious,relatedwork[2,6].Macro-F1calculatestheF1score for eachclassindependentlyandaveragesthem,whilemicro-F1aggregates the contributionsofallclassestocomputetheaverage.

### 4.6 Statistical

### analysis

Merely comparingperformancemeasuresisinsufficient,asobserveddiffer- ences mayariseduetorandomvariability[38].Toassessthesignificanceof these differences,weusethenon-parametricScott-KnottEffectSizeDiffer- ence (ESD)test,whichproducesdistinct,non-overlapping groupsandquan- tifies themagnitudeofmeaningfulmediandifferences[39].Thetestisrobust against outliersanddoesnotassumehomogeneity, normality, orsamplesize [40], andithasbeensuccessfullyappliedinsimilarcontexts[39]. While wereportbothmacro-F1andmicro-F1scoresforcomprehensive evaluation,webaseourcomparisonsonthemacro-F1score,asitbetter handles imbalanceddatasetsbygivingequalweighttoallclasses,aligning with previousstudies[2,6,37].

### 4.7 Implementation

Toimplementtheempiricalassessment,wefollowed aseriesofstepsforeach RQ. ForRQ1andRQ2,weusedalldatasets,models,andlabelconfigurations as describedabove.Forthegenerative-basedZSL,weusedthetemplate: “What isthesentimentofthefollowingappreview,whichisdelimitedwith triple backticks?”Giveyouransweraseither‘positive’,‘negative’,or‘neu- tral’.”Wereplacedtheterm“appreview”withthetypeofeachexamined dataset andsubstitutedthelabels“positive,”“negative,”or“neutral”with

13


---

<!-- Página 14 -->

**Identifier**

L1

L2

L3

L4

L5

L6

L7

## Table

## 3:

## Summary

dataset, corresponding love ative).

describe dataset, negations

stances “with” where of

stances sociated sentiment tive; ing where of emotions.

stances the tive; ing negating emotions.

stances LLM scribed ciated

stances ated tral timents

## of

## label

## configurations

Positive

A

An tive

An itive, ments

An love

An fulness, ment, gaiety, ality, ment, elation, zest, ment, ration, sure, ments

An positive, happiness, satisfaction, glee, joy, gladness, tion, zest, citement, exhilaration, pleasure, sentiments

## 14


---

<!-- Página 15 -->

the specificlabelsbeingassessed.Weusedthedefaultparametersprovided by thegenerative model’sAPI,withtheexceptionofsettingthetemperature to zerotoreducevariability intheoutputs. Toensureconsistencybetweenthemodeloutputsandthegoldlabels, we appliedsimplepost-processingrules.Fortheshorterlabels,wechecked whether thegeneratedoutputexplicitlymentionedthesentiment name(i.e., positive, negative,neutral)andmappedittothecorrespondinglabel.For the longerlabels(i.e.,L6andL7),themodeloccasionallyproducedpartial matches byomittingcertainparts;inthesecases,wepost-processedthe outputs toalignthemwiththeoriginallabels. ForRQ3,following[2],wepartitionedeachdatasetintotraining,valida- tion, andtestsetsinan8:1:1ratiowithstratifiedsplitting.Wefine-tuned state-of-the-art transformermodelslistedinTable 4. Wenote that our evaluation doesnot include earlier SE-specificsentiment analysis tools,suchasSentiStrength-SE.Thisdecisionissupportedbythe findings ofZhangetal.[1],whodemonstratedthatfine-tunedtransformer- based modelsoutperformthesetoolsandconcludedthatsuchshould be regardedasthestateoftheartforsentimentanalysisintheSEdomain. Furthermore,inamorerecentwork[2],Zhangetal.followedthisconclusion by excludingtheseearliertoolsentirelyandfocusingtheirevaluationsolely on fine-tunedtransformer-basedmodels.Inlinewiththisdirection,we adopt a similarapproachandbenchmarkourresultsagainststate-of-the-arttrans- former models. − 5Weusedalearningrateof2×10, 5epochs,batchsizeof32,anda max sequencelengthof256tokens.Themodelwiththehighestmacro-F1 score onthevalidationsetwasevaluatedonthetestsetwithoriginallabels (i.e., L1).Wecomparedtheperformanceoffine-tunedmodelswiththebest- performing ZSLmodel-labelcombinations andthebest-performingmodelfor each ZSLtechniquewhenpairedwithL1. ForRQ4,weconductedquantitative andqualitativeanalysesonmisclas- sifications fromRQ3.Thequantitativeanalysisidentifiedcommonmisclas- sified instancesamongZSL-basedandfine-tunedmodels.Thequalitative analysis categorizedthesemisclassificationsusingtheframeworkofNovielli et al.[11].Weindependentlycategorizedthecommonlymisclassifiedin- stances oftheZSL-basedmodels.Thenwecomparedtheresultsinajoint session andcalculatedCohen’skappacoefficient,whichwas0.71,indicating moderate agreement[41].Disagreementswereresolvedthroughdiscussion, with eachauthorprovidingjustificationuntilconsensuswasreached.

15


---

<!-- Página 16 -->

Table4:Selectedmodelsforfine-tuning

**Model**

BERT-base-casedM1 RoBERTa-baseM2 DistilBERT-base-uncasedM3 ALBERT-base-v1M4 XLNet-base-casedM5

### 5 Results

This sectionsummarizestheresultsofthestudy,andouronlineappendix includes moredetailedresultsforeachRQ.

### 5.1 RQ1:

### Which

### ZSL

### technique

### is

### most

### effective

### for

### sentiment

### classification,

### and

### among

### the

### techniques

### that evaluate multiple

### models,

### which

### model

### demon-

### strates the

### best

### performance?

The resultsoftheexaminedZSLtechniquesoneachdatasetaresummarized in Table5.The“Mac”and“Mic”columnsrefertothemacro-F1scoreand micro-F1 scorevalues,respectively,withthehighestvaluesofthemacro-F1 and micro-F1scoresforeachdatasetarebolded. As presentedinthetable,generative-basedZSLachievedthehighest macro-F1 scoresacrossmostdatasets,withexceptionsintheGitter,Google M4 andN M2 outperformedothersontheGit-Play,andJiradatasets.N M9achievedthehighestter andGooglePlaydatasets,respectively,andE macro-F1 scorefortheJiradataset. M9 achievedthehighestWithin theembedding-basedZSLmodels,E macro-F1 scoresacrossmostdatasets(i.e.,5outof7).AmongtheNLI- based models,N M2 canbeconsideredthebestperformer,whereitachieved the highestmacro-F1scorein5outof7datasets. The resultsofthestatisticaltestconfirmedtheabovefindings,where Figure 5depictstheresults.Thegenerative-basedZSLmodelwasranked as thebestperformingmodelamongallexaminedmodels.Thesecondrank predominantly comprisedNLI-basedZSLmodelsandoneembedding-based thirdrankincludedtheremainingNLI-basedZSL model(i.e.,E M9). The ZSL model(i.e.,N M3), theTARS-basedmodel,andanotherembedding- based model(i.e.,E M11). Therestoftheembedding-basedmodelswere distributed fromthefourthranktothelastrank(i.e.,rank9). The resultshighlightthedominanceofgenerative-basedandNLI-based

16


---

<!-- Página 17 -->

## ZSL techniques,

## with

## a

## few

## embedding-based

## models

## demonstrating

## compet-

## itive performance.

## Table

## 5:

## Summary

## of

## the

## performance

## of

## ZSL-based

## models

**Model** **reviews**

**Mac**

Embedding-based

EM1 EM2 EM3 M4E EM5 M6E EM7 EM8 EM9 EM10 EM11 EM12

NLI-based

NM1 NM2 NM3 NM4

TARS-based

TM1

Generative-based

GM1

### 5.2 RQ2:

### Do

### different

### label

### configurations

### have

### an

### im-

### pact on

### the

### performance

### of

### ZSL-based

### sentiment

### classification?

## The results

## of

## varying the

## utilized

## labels

## within

## each embedding-based

## model

## are presented

## in

## Table

## 6,

## where

## the

## highest

## values

## for

## both

## macro-F1

## and

## micro-F1 scores

## for

## each

## dataset

## are

## bolded.

## We

## note

## that,

## due

## to

## space

## limitations, the

## table

## only

## includes

## model-label

## combinations

## that

## yielded

## the highest

## macro-F1

## score

## for

## a

## dataset

## within

## each

## model.

## We

## provide

## the

## results of

## all

## model-label

## combinations

## in

## our

## online

## appendix.

## M9 achieved

## the

## highest

## macro-F1

## scores

## Two label

## combinations

## of

## E

## in the

## majority

## of

## datasets,

## with

## the

## exception

## of

## Google

## Play,

## where

## the

## combination E

## M12

## L3 attained

## the

## highest

## macro-F1

## score.

## Specifically,

## E

## M9

## L1 achieved

## the

## highest

## value

## on

## the

## Jira

## dataset,

## while

## M9

## E L3

## 17


---

<!-- Página 18 -->

1.00

0.75

0.50

Macro-F1 score

0.25

0.00

Figure 5:Scott-KnottESDrankingforZSLmodelsbasedonmacro-F1score

achievedthehighestmacro-F1scoresacrosstheremainingfivedatasets. Toidentifytheoverallbestembedding-basedmodel-labelcombination,

## Rank

we conductedastatisticalanalysis.Figure6presentstheresults,whereonly the topfiverankedcombinationsareincludedduetospaceconstraints.As 12345M9the figuredemonstrates,theanalysisconfirmsthesuperiorityofE L3, M9L2. Additionally,as itwasrankedasthetop-preformeralongwithE EM8L2, EM8L3, EM9L4, andEM9L5 wererankedinsecondplace while EM9L1 wasrankedthird.Othercombinationsfollowedinthere- M8andE M9 achievedmaining ranks.TheanalysisrevealedthatbothE higher resultswithvaryinglabelcombinationscomparedtoothers. Table7summarizestheresultsofcombiningeachNLI-basedmodelwith label configurations, where the highest macro-F1 and micro-F1 scores for each L1 hascontributedtothehighestmacro-F1scoredataset arebolded.N M2 across allNLI-model-labelcombinationsin3outof7datasets.Moreover, M4L3 achievedthehighestvaluesin2datasets.ThecombinationsofN M3L2, NM3L3, NM3L5, NM4L2, andN M4L5 wereabletoachieveN the highestmacro-F1scoreonadataset. Figure 7presentstheresultsoftheScott-KnottESDtest,whereonlythe top 5ranksareincludedduetospacelimitations.Theresultsdemonstrate the superiorityoftheNM4L3 combination,whichwasrankedfirstamong all NLI-basedcombinations.BoththecombinationsofM4NwithL2and L5 labelswererankedsecond,alongwiththeM1NL2 andN M2L1 combi- nations. Theremainingcombinationsweredistributedacrossthe ranks.

18

T_M1E_M9E_M8E_M6N_M1N_M2N_M4N_M3G_M1E_M11E_M10E_M12

### Model

E_M3

6

E_M7E_M1

7

E_M5

8

E_M2

9

E_M4


---

<!-- Página 19 -->

## Table

## 6:

## Summary

## of

## the

## performance

## binations of

## each

## embedding-based

**M&L** **reviews**

**Mac**

EM1L2 M1L3E EM1L4 M1L7E

EM2L2 EM2L3 EM2L4 EM2L5

EM3L1 EM3L2 EM3L5

EM4L2 EM4L3 EM4L4 EM4L5

EM5L2 EM5L3 EM5L5 EM5L6 EM5L7

EM6L3 EM6L4 EM6L7

EM7L1 EM7L2 EM7L3 EM7L4 EM7L5

EM8L2 EM8L3

EM9L1 EM9L2 EM9L3 EM9L4 EM9L6 EM9L7

EM10L1 EM10L2 EM10L3 EM10L4 EM10L5 EM10L6

EM11L1 EM11L2 EM11L3 EM11L4

EM12L2 EM12L3 EM12L4 EM12L5 EM12L6

## of

## best-performing

## model

## across

## 19

## each

## dataset

## model-label

## com-


---

<!-- Página 20 -->

1.001.00

0.750.75

0.50

Macro-F1 score 0.25

0.00

E_M9_L2

Figure 6: binations based

1

### 1

Figure 7: based on

E_M9_L3E_M8_L2N_M4_L3

Scott-KnottESDranking onmacro-F1score

2

### 2

### 3

Scott-KnottESDranking macro-F1score

E_M8_L3E_M9_L4E_M9_L5E_M9_L1E_M8_L1N_M1_L2N_M2_L1N_M4_L2N_M4_L5

forembedding-based

forNLI-based

20

E_M8_L4N_M1_L1N_M1_L3E_M10_L2

model-label

## Rank

3

### 4

model-labelcombinations

N_M2_L2 E_M10_L3N_M3_L2N_M4_L1N_M2_L3E_M11_L1E_M11_L2E_M12_L2

### Model

com-

E_M12_L4

4

E_M12_L5 N_M3_L1E_M12_L6N_M3_L3E_M11_L3E_M11_L4

5 5

N_M4_L4E_M12_L3E_M12_L7


---

<!-- Página 21 -->

## Table

## 7:

## Summary

## of

## the

## performance

## binations of

## each

## NLI-based

## model

**M&L** **reviews**

**Mac**

NM1L1 NM1L2 NM1L3 NM1L4 NM1L5 NM1L6 NM1L7

NM2L1 NM2L2 NM2L3 NM2L4 NM2L5 NM2L6 NM2L7

NM3L1 NM3L2 NM3L3 NM3L4 NM3L5 NM3L6 NM3L7

NM4L1 NM4L2 NM4L3 NM4L4 NM4L5 M4L6N NM4L7

## of

## best-performing

## across

## each

## 21

## dataset

## model-label

## com-


---

<!-- Página 22 -->

## The results

## of

## combining

## TARS model

## with

## different

## label

## configurations

## are presented

## in

## Table

## 8,

## with

## the

## highest

## macro-F1

## and

## micro-F1

## score

## for

## each dataset

## are

## bolded.

## The

## results

## revealed

## the

## superiority

## of

## L2,

## which

## was able to produce

## the highest macro-F1 score for four datasets. L1

## followed

## closely,

## achieving the highest scores for three datasets. The

## other labels

## failed

## to produce

## the

## highest

## values

## for

## any

## dataset.

## Table

## 8: Summary

## of the performance

## of the TARS model-label

## combinations

## across each

## dataset

**M&L** **reviews**

**Mac**

TM1L1 TM1L2 TM1L3 TM1L4 TM1L5 TM1L6 TM1L7

## The results

## of

## the

## statistical

## test,

## presented

## in

## Figure

## 8,

## confirm

## these

## findings. The

## model

## combinations

## with

## L1

## and

## L2

## were

## ranked

## as

## the

## top

## performers, followed

## by

## L3

## in

## second,

## L4

## in

## third,

## L5

## and

## L7

## in

## fourth,

## and

## L6 in

## fifth.

## Table

## 9 presents the results of combining the generative-based model

## with

## the label

## configurations,

## with

## the

## highest

## macro-F1

## and

## micro-F1

## score

## for

## each dataset are bolded.

## The

## results demonstrate the superiority of L1, which

## achieved

## the

## highest

## performance

## on

## three

## datasets.

## All

## other

## labels,

## except

## for L3,

## were

## able

## to

## achieve

## the

## highest

## value

## on

## one

## dataset,

## while

## L3

## did

## not produce

## the

## highest

## value

## on

## any

## dataset.

## Table

## 9:

## Summary

## of

## the

## performance

## of

## the

## generative

## model-label

## combi-

## nations across

## each

## dataset

**M&L** **reviews**

**Mac**

GM1L1 GM1L2 GM1L3 GM1L4 GM1L5 GM1L6 GM1L7

## The statistical test produced three ranks, as Figure 9 presents. Combining

## G

## M1 with

## L1,

## L2,

## or

## L4

## resulted

## in

## the

## top

## performance.

## Pairing

## the

## model

## 22


---

<!-- Página 23 -->

1.00

0.75

0.50

Macro-F1 score 0.25

0.00

T_M1_L1

Figure 8: based on

with L3 1placed the The results across all Figure 10, results confirm the superior model was L3. Combining generative-based model the NLI-based L3. Other followed was ranked

T_M1_L2

Scott-KnottESDrankingfortheTARS model-labelcombinations macro-F1score

## Rank

andL5placeditinthesecondrank,whileL6andL7combinations 23modelinthethirdrank. ofcomparingtheperformanceofallmodel-labelcombinations ZSLtechniquesusingtheScott-KnottESDtestarepresented withonlythetop5ranksincludedduetospacelimitations. Specifically,theperformanceof theM9E model. rankedasthetopperformerwhencombinedwithbothL2 themodelwithL4placeditinsecondplace,alongside whencombinedwithbothL1andL4.Additionally, M4) wasrankedsecondwhencombinedwithmodel(i.e.,N combinationsofembedding,NLI,andgenerative-basedmodels insubsequentranks.Notably,onlyoneTARS-basedcombination fifth,withotherZSLtechniquecombinationssurpassingit.

23

T_M1_L3T_M1_L4T_M1_L5

### Model

4

in The

and the

T_M1_L7T_M1_L6

5


---

<!-- Página 24 -->

1.00

1.00

0.75

0.75

0.50 0.50

Macro-F1 score

Macro-F1 score0.25 0.25

0.000.00

E_M9_L2G_M1_L1

Figure 9: tions based

Figure 10: macro-F1 score

Scott-Knott onmacro-F1

1

1

Scott-Knott

E_M9_L3G_M1_L2G_M1_L4

ESDranking score

ESDranking

E_M9_L4

forthegenerativemodel-label

2

## Rank

2

formodel-labelcombinations

24

N_M4_L3G_M1_L1G_M1_L4G_M1_L3G_M1_L5

### Model

E_M8_L2

combina-

## Rank

3

basedon

E_M8_L3E_M9_L5N_M4_L2N_M4_L5G_M1_L6G_M1_L2

3

N_M1_L1G_M1_L3G_M1_L7N_M1_L2N_M2_L1N_M2_L2

4

N_M3_L2N_M4_L1G_M1_L5E_M9_L1 E_M12_L5 N_M1_L3

5

N_M2_L3N_M3_L1T_M1_L1


---

<!-- Página 25 -->

### 5.3 RQ3:

### How

### does

### the

### performance

### of

### ZSL-based

### models compare

### with

### that

### of

### the

### state-of-the-art

### fine-tuned transformer-based

### models

### in

### sentiment

### classification?

The resultsofthestate-of-the-artfine-tunedtransformer-basedmodelsand the best-performingmodel-labelcombinationsforeachZSL-basedtechnique are presentedinTable10,wherethehighestvaluesofthemacro-F1and micro-F1 scoresforeachdatasetarebolded. As thetabledepicts,FM2L1 achieved thehighestmacroscoresin3out of the7datasets,andGM1L4 attainedthehighestscoresin2datasets. Furthermore,FM1L1, FM3L1, andEM9L1 eachachievedthehighest score inonedataset. The resultsofthestatisticalanalysisarepresentedinFigure11.The M1L1 ,F M4L1 ,andEM9L3 arethestatistical analysisrevealedthatF top performers.Theremainingfine-tunedmodelsalongwithM9EL2 and M1L4 ,wererankedsecond.NM1L1, NM2L1, andEM9L1 wereG ranked third.TM1L1 precededN M4L3 andG M1L1 ,withthelatter twomodelsrankedlast,inthefifthrank. The aboveresultsrevealedthatembedding-basedandgenerative-based ZSL modelshavecompetitiveperformancecomparedtothatoffine-tuned models onthetestingset.

### 5.4 RQ4:

### What

### factors

### contribute

### to

### the

### misclassifi-

### cation of

### sentiment

### labels

### in

### ZSL-based

### models,

### and how

### do

### these

### compare

### with

### those

### shared

### with

### the state-of-the-art

### fine-tuned

### transformer-based

### models?

The resultsofthequantitativeerroranalysisaresummarizedinTable11, where the lowest number of misclassified instances for each dataset are bolded. M9L3 yieldedthefewesterrorsacrosstheAmong theZSL-basedmodels,E majority ofdatasets(i.e.,3outof7datasets),followedbyGM1L1 and GM1L4, in2outof7datasets,and M9EL1 inonlyonedataset.More- over,commonmisclassificationsacrosstheZSL-basedmodelsincluded35 API reviews,19GitHubcomments,3app1Jiracomment,and10 SO posts. When comparingtheperformanceofthefine-tunedmodelstotheZSL- based models,thefine-tunedmodelsproducedfewermisclassificationsthan

25


---

<!-- Página 26 -->

## Table

## 10:

## Summary

## transformer-based models

## for each

## ZSL-based

## technique

**M&L** **reviews**

**Mac**

EM9L1 EM9L2 EM9L3

NM1L1 NM2L1 NM4L3

TM1L1

GM1L1 GM1L4

FM1L1 FM2L1 FM3L1 FM4L1 FM5L1

## of

## the

## performance

## of

## state-of-the-art

## and

## the

## best-performing

## model-label

Embedding-based

NLI-based

TARS-based

Generative-based

Fine-tuned

## 26

## fine-tuned

## combinations


---

<!-- Página 27 -->

1.00

0.75

0.50

Macro-F1 score

0.25

0.00

F_M1_L1

Figure 11:Scott-KnottESDrankingforthestate-of-the-artfine-tuned transformer-based modelsandthebest-performingmodel-labelcombinations for eachZSL-basedtechniquebasedonmacro-F1score

## Rank

all oftheexaminedZSL-basedmodelsin4outof7datasets.Thefine-123 tuned modelswereabletoreducemisclassificationsonAPIreviews,Gerrit code reviewcomments,GitHubandSOposts.Thecommon misclassifications by the fine-tuned modelsincluded 25 API reviews, 11 Gerrit code reviewcomments,16GitHub1Gitterdevelopermessage,5 app reviews,1Jiracomment,and25SOposts. Both ZSL-basedmodelsandfine-tunedfailedtoclassify9API reviews, 5GitHubcomments,3app1Jiracomment,and1SO post. The analysisofthecommonlymisclassifiedinstancesbytheZSL-based models revealed thatamongthetotal68misclassifiedinstances,64.71%were originally annotatedasneutral,22.06%aspositive,and13.24%asnegative. The categorizationoferrorsindicatedthatsubjectivityinannotation resulting fromdifferentannotators’perceptionsofemotionsaccountsfor 60.29% ofthecommonlymisclassifiedinstances.Polarfactswereidenti- fied asthesecondmostcommonsourceofmisclassification,whereitrep- resents 22.06%oftheerrors.Polarfactsarethosethatdescribeinherently desirable orundesirablesituations,expressedinaneutraltone,suchasthe comment “thisdoesn’twork”.Politenesserrorsaccountedfor8.82%ofthe misclassified instances.Theseerrorsarosewhenpoliteexpressions,suchas “Thanks!”, ledtoinconsistentclassifications.Misclassificationsduetofigu-

27

F_M4_L1F_M2_L1F_M3_L1F_M5_L1E_M9_L3E_M9_L2E_M9_L1N_M1_L1N_M2_L1G_M1_L4

### Model

T_M1_L1

4

N_M4_L3

5

G_M1_L1


---

<!-- Página 28 -->

rative language,suchashumor,irony,orsarcasm,contributedto4.41%of the errors.AnexampleistheAPIreviewstatement:“Soinitializinghighis better thantoolow”,whichwasannotatedasnegativebyhumanannotators but incorrectlyclassifiedaspositiveorneutralbythemodels.Finally,prag- matic errors,suchasstatementsreportingthird-partyopinionsoremotions, were anothersourceofmisclassification,accountingfor4.41%oftheerrors. In thesecases,sentencesthathumansidentifyasneutralaremisclassifiedas positive ornegativebythemodelsduetothepresenceofemotion-related words. AnexampleofthisistheAPIreviewstatement:“Iknowmanyde- velopers wouldliketohavethis”,whichwasannotatedasneutral,butthe majority ofmodelsclassifieditaspositive. The commonmisclassifiedinstancesamongbothZSL-basedandfine- tuned modelswereoriginallylabeledasfollows:57.89%neutral,26.32% positive, and15.79%negative.Theerrorcategorizationrevealedthatsub- jectivity inannotationwasthemaincontributor,accountingfor73.68%of these instances.Politenesserrorsaccountedfor15.79%,followedbypolar facts with5.26%,andfigurativelanguagewith5.26%. Table11:Summaryofmissclassifiedsinstances

**M&L** **reviews**

Test

ZSL-based

EM9L1 EM9L2 EM9L3 NM1L1 NM2L1 NM4L3 TM1L1 GM1L1 GM1L4

Common

Fine-tuned

FM1L1 FM2L1 FM3L1 FM4L1 FM5L1

Common

Common

28


---

<!-- Página 29 -->

### 6 Discussion

The resultsofRQ1revealedthatgenerative-basedZSLoutperformedother ZSL techniquesusingoriginallabels,withNLIrankedsecond.Despitebeing pre-trained forsentimentanalysisintweets,M9 performedwellonsoft- ware engineeringsentimentanalysis.Although,thepaidembedding(i.e., EM10) outperformedmostembeddings,itwasbysomeNLI- based modelsandEM9. Therefore,we recommendexploringfreelyavailable models beforeinvesting inapaidone,astheformermayyieldbetterresults. RQ2 revealed that no single labelconfiguration consistently outperformed others acrossallmodels.WhiletheoriginallabelL1performedwellwith TARSandgenerative-basedZSL,embedding-basedandNLI-basedmodels performed betterwith expert-curatedlabels,particularlythose incorporating the sentimentterm(i.e.,L2andL3).CombiningM9E withL3yieldedthe best results,suggestingthatincludingtaskcontextinlabelconfigurations withL3yieldedmay enhanceperformance.Additionally,combiningE the bestresultsacrossallZSLtechniques.Thissupportstheearlierobser- vationthatpre-trainedmodelsfromotherdomainsareaviableapproachfor ZSL. M9In RQ3,whencomparedtofine-tunedstate-of-the-artmodels,E paired withL3rankedasthetopperformer,achievingresultscomparable to somefine-tunedmodels,whilesurpassingothers.Thisfindingcontra- dicts previousresearch,whichobservedthatgeneralsentiment analysistools underperform insoftwareengineeringcontexts[9,10],asthefindingdemon- strates thatpre-trainedmodelstrainedonsentimentanalysisinotherdo- mains canachieveperformancesimilartoorexceedingfine-tunedmodels without theneedforadditionaltrainingorfine-tuning,therebyaddressing the issueofdatascarcity. RQ4 revealedthatmostmisclassificationsinZSL-basedmodelsoccurred in theneutralclass,consistentwiththeobservationsof[12]and[3]that neutral sentiments arechallenging toclassify. Subjectivityinannotationand polar factswereidentifiedastheprimarycausesofthesemisclassifications. Subjectivity inannotationwas alsohighlighted by [3]asoneofthechallenges in sentimentanalysis. Another observationisthatwhileRQ3demonstratedthatsomeZSL- based modelsperformedsimilarlytofine-tunedmodels,thelatter were moreeffectiveatreducingmisclassificationsintechnicaldatasets(i.e., API reviews,codeGitHubcomments,andSOposts),asevidenced by theresultsofRQ4.Incontrast,ZSL-basedmodelsperformedbetteron more conversationaldatasets,suchasdeveloperchatmessages,appreviews, and Jiracomments.

29


---

<!-- Página 30 -->

When comparingourresultswithprevious,relatedstudies,our can becomparedwiththeworkof[1],whichwasperformedinRQ3.The other workthatcanbecomparedtooursistheworkof[2].Specifically, we comparetheperformanceofourZSL-basedmodelswiththeir and FSL-basedmodelsonthecommondatasetsfrombothstudies.Akey difference between ourstudyand[2]isthatwhilewe evaluated themodelson all testsetsinRQ3andRQ4,[2]selectedastratifiedrepresentativerandom sample duetothehighcostofrunninggenerativemodels. In ourstudy,combiningEM9 withbothL2andL3resultedina0.79 macro-F1 scoreontheGerritdataset,higherthanthe0.76best score achievedby[2]throughFSL,wheretheirZSL0.75.For GitHub, ourhighestmacro-F1scoreis0.79,achievedbyEM9L3, while [2] achieved0.72withbothFSLandZSL.[2]aperfectmacro- F1 scoreontheGooglePlaydatasetwithFSLand0.98withZSL,whereas M1L4) achievedonly0.61.EM9L1our bestZSLmodel(i.e.,G an almostperfectmacro-F1score(i.e.,0.99)ontheJiradataset,where[2] achieved0.91throughFSLand0.85ZSL. Although [2]focusedsolelyongenerative-basedmodels,thecomparison M9, whichachievedhigherresultson3outhighlights thesuperiorityofE of the4commondatasets.Thisconfirmsourobservationthatapplying ZSL withamodelpre-trainedonasimilarcontextcanyieldcompetitive performance.

### 7 Threats

### to

### validity

Several threatsmayaffectthevalidityofthisstudy.Thissectiondiscusses external, construct,internal,andconclusionvalidity threats,alongwithcor- responding mitigationstrategies,whereapplicable[42].

### 7.1 External

### validity

A potentialthreattoourstudy’sexternalvalidity isthegeneralizability ofits findings. Althoughourresultsarederived fromseven sentiment classification datasets representing diverse software engineering contexts, thegeneralizabil- ity ofthesefindingscannotbeclaimedbeyonddatasets. Another potentialexternalvaliditythreatarisesfromthemodelsand labels utilized.Sinceourfindingsareconfinedtothemodelsand examined, theymaynotgeneralizetoothersthatwerenotincludedinthis study.Consequently,weacknowledgethisasalimitationtoourstudy’s external validity.

30


---

<!-- Página 31 -->

### 7.2 Construct

### validity

A potentialthreattothisstudy’sconstructvalidityliesintheperformance measures employed.Toaddressthisthreat,wereportbothmacro-F1and micro-F1 scores,withtheformerbeingthebasisforcomparison.Thisap- proach alignswiththeapproachof[2,6]. Another potentialconstructvalidity threatstemsfromtheannotationof the utilized datasets. Werely on datasets annotated in prior work and widely utilized inrelatedstudies[1,2,4].Whileeffortshavebeenmadetoensure annotations accuracy,wecannotguaranteethecompleteabsenceoferrors. Consequently,thislimitationisinheritedfromthedatasets. An additional potential construct validity threat is the manual categoriza- tion ofmisclassifiedinstances,which may introducesubjectivity. Tomitigate this threat,weindependentlycategorizedtheerrorsthenresolvedinconsis- tencies throughdiscussionuntilaconsensuswasreached.

### 7.3 Internal

### validity

A potentialthreattoourstudy’sinternalvalidity isthepossibilityofimple- mentation errors.Tomitigatethis,weusedwidelyacceptedandvalidated model implementationsandfollowedguidelinesandtutorialsforapplying these modelsinsimilarcontexts,suchas[13,14].

### 7.4 Conclusion

### validity

Conclusion validity concernstheappropriateuseofstatisticaltests[42].Be- sides usingcommonstatisticalmeasures,suchaspercentages,toconveythe study’s findings,weonlyemployedCohen’sKappacoefficienttomeasure inter-rater agreementandthenon-parametricScott-KnottESDtesttocom- pare theperformanceofmodels. The useofCohen’sKappacoefficientalignswithitsintendedpurpose and isrecommendedbyempiricalstandardsinsoftware engineeringresearch [43]. TheScott-Knott ESD test was selected for its ability to producedisjoint groups withnon-negligiblemagnitudesofdifference,itsapplicationinprior studies withinsimilarcontexts,anditshightoleranceforoutliers[39,40].

### 8 Conclusion

Aiming to address the challenge of data scarcity within sentiment analysis for softwareengineering,thisstudyexploredthepotentialofZSLforsentiment analysis in software engineering. Weempirically evaluated the performance of

31


---

<!-- Página 32 -->

embedding-based, NLI-based,TARS-based,andgenerative-basedZSLtech- niques acrossmultiple software engineeringcontexts. Weexpandedthescope of ouranalysisbyincludingvariouslabelconfigurationstounderstandtheir impact onmodelperformance.Wethencomparedthebest-performingZSL- based modelsandlabelcombinationswiththestate-of-the-artfine-tuned transformer-based models.Finally,weconductedanerroranalysistobetter understand thecausesofsentimentmisclassificationsbyZSL-basedmodels. The resultsdemonstratedthatZSLisaviableapproachforsentiment analysis within the software engineering domain, achieving performancecom- parable toorexceedingstate-of-the-artfine-tunedtransformer-basedmodels without requiringfine-tuning.Specifically,anembedding-basedmodel,fine- tuned toanalyzesentimentswithintweets,achievedtopperformancewhen paired withexpert-generatedlabelsthatcontextualizedthedatasetandin- corporated theterm“sentiment”.Thecombinationofthemodelandlabel was statisticallyrankedasthetopperformer,whereiteithermatchedor surpassed fine-tunedmodels.Similarly,thegenerative-basedmodelwhen paired withexpert-generatedlabelsthatelaboratedondescribingemotions with sentimentswasrankedasthesecond-bestperformeralongsidesomeof the fine-tunedmodels.Theerroranalysisrevealedthatmostmisclassified instances were originallyannotatedasneutralsentiment, andthefurthercat- egorization ofthemisclassifiedinstancesidentified subjectivityinannotation and polarfactsastheprimarycausesofmisclassification. These findingsunderscorethepotentialofZSLinaddressingthechal- lenges oftrainingdatashortagesforsentiment analysisinsoftware engineer- ing. Byeliminatingtheneedforannotateddata,ZSLprovidesapractical solution forsentimentanalysisacrossdiversesoftwareengineeringcontexts. Futureworkcouldexplorehowlinguisticvariationinlabelphrasingim- pacts sentimentclassificationperformance.Additionally,investigatingthe influence of different prompting strategies on modeleffectiveness in sentiment classification representsapromisingavenue forfutureresearch.Moreover,a deeper erroranalysisthatleveragesexplainableartificialintelligence(XAI) and examines differences between developer-oriented and user-generated datasets could providemorenuancedinsightsintoZSLperformancewithinsentiment analysis insoftwareengineering.

32


---

<!-- Página 33 -->

### Declaration of

### Generative

### AI

### and

### AI-assisted

### Technologies

### in

### the

### Writing

### Process

The authorsusedChatGPTtoimprovethereadabilityandlanguageofthe manuscript, withfullresponsibilityforthefinalcontent.

### References

[1] T.Zhang,B.Xu,F.Thung,S.A.Haryono,D.Lo,L.Jiang,Sentiment analysis forsoftwareengineering:Howfarcanpre-trainedtransformer models go?,in:2020IEEEIntealefato2018sentimentrnationalConfer- ence onSoftwareMaintenanceandEvolution(ICSME),IEEE,2020, pp. 70–80.

[2] T.Zhang,I.C.Irsan,F.Thung,D.Lo,Revisitingsentimentanaly- sis forsoftwareengineeringintheeraoflargelanguagemodels,ACM TransactionsonSoftwareEngineeringandMethodology34(3)(2025) 1–30.

[3] M.Obaidi,J.Kl¨under,Developmentandapplicationofsentiment anal- ysis toolsinsoftwareengineering:Asystematicliteraturereview,in: Proceedings ofthe25thInternationalConferenceonEvaluationand Assessment inSoftwareEngineering,2021,pp.80–89.

[4] B.Lin,F.Zampetti,G.Bavota,M.DiPenta,M.Lanza,R.Oliveto, Sentimentanalysisforsoftwareengineering:Howfarcanwego?,in: Proceedings of the 40th international conference on software engineering, 2018, pp.94–104.

[5] A.Sajadi,K.Damevski, P. Chatterjee, Towards understanding emotions in informaldeveloperinteractions:Agitterchatstudy, in:Proceedings of the31stACMJointEuropeanSoftwareEngineeringConferenceand Symposium on the Foundations of Software Engineering, 2023, pp. 2097– 2101.

[6] N.Novielli,F.Calefato,D.Dongiovanni,D.Girardi,F.Lanubile,Can we usese-specificsentimentanalysistoolsinacross-platformsetting?, in: Proceedingsof the 17th International Conference on Mining Software Repositories, 2020,pp.158–168.

33


---

<!-- Página 34 -->

[7] G.Uddin,F.Khomh,Automaticminingofopinionsexpressedabout apis in stack overflow, IEEE Transactions on Software Engineering 47 (3) (2019) 522–559.

[8] F.Calefato,F.Lanubile,F.Maiorano,N.Novielli,Sentimentpolarity detection forsoftwaredevelopment,in:Proceedingsofthe40thInter- national ConferenceonSoftwareEngineering,2018,pp.128–128.

[9] R.Jongeling,S.Datta,A.Serebrenik,Choosingyourweapons:Onsen- timent analysistoolsforsoftwareengineeringresearch,in:2015IEEE International ConferenceonSoftwareMaintenanceandEvolution(IC- SME), IEEE,2015,pp.531–535.

[10] P.Tourani,Y.Jiang,B.Adams,Monitoringsentimentinopensource mailing lists: exploratorystudy on the apache ecosystem., in:CASCON, Vol.14,2014,pp.34–44.

[11] N.Novielli,D.Girardi,F.Lanubile,Abenchmarkstudyonsentiment analysis forsoftwareengineeringresearch,in:Proceedingsofthe15th International ConferenceonMiningSoftwareRepositories,2018,pp. 364–375.

[12] B.Lin,N.Cassee,A.Serebrenik,G.Bavota,N.Novielli,M.Lanza, Opinion miningforsoftwaredevelopment:asystematicliteraturere- view, ACMTransactionsonSoftwareEngineeringandMethodology (TOSEM) 31(3)(2022)1–41.

[13] L.Tunstall,L.VonWerra,T.Wolf,Naturallanguageprocessingwith transformers, ”O’ReillyMedia,Inc.”,2022.

[14] J.Alammar, M.Grootendorst,Hands-OnLarge Language Models:Lan- guage UnderstandingandGeneration,”O’ReillyMedia,Inc.”,2024.

[15] S.P.Veeranna,J.Nam,E.L.Mencıa,J.F¨urnkranz,Usingsemantic similarity formulti-labelzero-shotclassificationoftextdocuments,in: Proceeding ofeuropeansymposiumonartificialneuralnetworks,com- putational intelligenceandmachinelearning.bruges,belgium:Elsevier, 2016, pp.423–428.

[16] W.Alhoshan,A.Ferrari,L.Zhao,Zero-shotlearningforrequirements classification: Anexploratorystudy, InformationandSoftware Technol- ogy 159(2023)107202.

34


---

<!-- Página 35 -->

[17] W.

[18] K.

[19] T.

[20] M.

[21] M.

[22] M.

[23] M.

[24] M.

[25] A.

[26] S.

Yin,J.Hay,D.Roth,Benchmarkingzero-shottextclassifica- tion: Datasets,evaluationandentailmentapproach,arXivpreprint arXiv:1909.00161 (2019).

Halder,A.Akbik,J.Krapac,R.Vollgraf, Task-aware representation of sentencesforgenerictextclassification,in:Proceedingsofthe28th International ConferenceonComputationalLinguistics,2020,pp.3202– 3213.

Brown,B.Mann,N.Ryder,M.Subbiah,J.D.Kaplan,P. Dhariwal, A. Neelakantan, P. Shyam, G.Sastry, A.Askell, etal.,Languagemodels are few-shot learners, Advances in neural information processingsystems 33 (2020)1877–1901.

S´anchez-Gord´on,R.Colomo-Palacios,Taking theemotionalpulseof softwareengineering—asystematicliteraturereviewofempiricalstud- ies, InformationandSoftwareTechnology 115(2019)23–43.

Obaidi,L.Nagel,A.Specht,J.Kl¨under,Sentimentanalysistools in softwareengineering:Asystematicmappingstudy,Informationand softwareTechnology 151(2022)107018.

R.Islam,M.F.Zibran,Sentistrength-se:Exploitingdomainspeci- ficity forimproved sentiment analysisinsoftware engineeringtext,Jour- nal ofSystemsandSoftware145(2018)125–146.

R. Islam, M.F. Zibran, Deva: sensingemotions in the valence arousal space insoftwareengineeringtext,in:Proceedingsofthe33rdannual ACM symposiumonappliedcomputing,2018,pp.1536–1543.

R.Islam,M.K.Ahmmed,M.F.Zibran,Marvalous:Machinelearn- ing baseddetectionofemotionsinthevalence-arousal spaceinsoftware engineering text,in:Proceedingsofthe34thACM/SIGAPPSympo- sium onAppliedComputing,2019,pp.1786–1793.

Murgia,M.Ortu,P. Tourani, B.Adams,S.Demeyer, Anexploratory qualitative andquantitativeanalysisofemotionsinissuereportcom- ments ofopensourcesystems,EmpiricalSoftware Engineering23(2018) 521–564.

Cagnoni,L.Cozzini,G.Lombardo,M.Mordonini,A.Poggi, M. Tomaiuolo,Emotion-basedanalysisofprogramminglanguageson stack overflow, ICTExpress6(3)(2020)238–242.

35


---

<!-- Página 36 -->

[27] G.

[28] T.

[29] J.

[30] E.

[31] H.

[32] D.

[33] K.

[34] M.

[35] V.

Uddin,Y.-G.Gu´eh´enuc,F.Khomh,C.K.Roy, Anempiricalstudy of theeffectivenessofanensembleofstand-alonesentimentdetection tools forsoftwareengineeringdatasets,ACMTransactionsonSoftware Engineering andMethodology(TOSEM)31(3)(2022)1–38.

Ahmed,A.Bosu,A.Iqbal,S.Rahimi,Senticr:Acustomized sentimentanalysistoolforcodereviewinteractions,in:201732nd IEEE/ACM International Conference on Automated Software Engineer- ing (ASE),IEEE,2017,pp.106–111.

Ding,H.Sun,X.Wang,X.Liu,Entity-levelsentimentanalysisof issue comments,in:Proceedingsofthe3rdInternationalWorkshopon Emotion AwarenessinSoftwareEngineering,2018,pp.7–13.

Biswas, M.E.Karabulut,L.Pollock, K.Vijay-Shanker, Achieving re- liable sentiment analysisinthesoftware engineeringdomainusingbert, in: 2020IEEEInternationalconferenceonsoftwaremaintenanceand evolution (ICSME),IEEE,2020,pp.162–173.

Batra,N.S.Punn,S.K.Sonbhadra,S.Agarwal,Bert-basedsen- timent analysis:Asoftwareengineeringperspective,in:Databaseand Expert SystemsApplications:32ndInternationalConference,DEXA 2021, VirtualEvent,September27–30,Proceedings,PartI32, Springer, 2021,pp.138–148.

Bleyl,E.K.Buxton,Emotionrecognitiononstackoverflowposts using bert,in:2022IEEEInternationalConferenceonBigData(Big Data), IEEE,2022,pp.5881–5885.

Sun,X.Shi,H.Gao,H.Kuang,X.Ma,G.Rong,D.Shao,Z.Zhao, H. Zhang,Incorporatingpre-trainedtransformermodelsintotextcnn for sentimentanalysisonsoftwareengineeringtexts,in:Proceedingsof the 13thAsia-PacificSymposiumonInternetware, 2022,pp.127–136.

Shafikuzzaman,M.R.Islam,A.C.Rolli,S.Akhter,N.Seliya,An empirical evaluationofthezero-shot,few-shot,andtraditionalfine- tuning basedpretrainedlanguagemodelsforsentimentanalysisinsoft- ware engineering,IEEEAccess(2024).

R.B.-G.Caldiera,H.D.Rombach,Goalquestionmetricparadigm, Encyclopedia ofsoftwareengineering1(528-532)(1994)6.

36


---

<!-- Página 37 -->

[36] M.

[37] C.

[38] I.

[39] C.

[40] M.-T.

[41] M.

[42] F.

[43] P.

M.Imran,Y.Jain,P. Chatterjee,K.Damevski,Dataaugmentation for improvingemotionrecognitioninsoftwareengineeringcommunica- tion, in:Proceedingsofthe37thIEEE/ACMInternationalConference on AutomatedSoftwareEngineering,2022,pp.1–13.

D.Manning,P.Raghavan,H.Sch¨utze,Introductiontoinformation retrieval,Cambridgeuniversitypress,2008.

H.Witten,E.Frank,M.A.Hall,C.J.Pal,M.Data,Practicalma- chine learningtoolsandtechniques,in:Datamining,Vol.2,Elsevier Amsterdam, TheNetherlands,2005,pp.403–413.

Tantithamthavorn, S.McIntosh,A.E.Hassan,K.Matsumoto,The impact ofautomatedparameteroptimizationondefectpredictionmod- els, IEEETransactions onSoftwareEngineering45(7)(2018)683–711.

Puth,M.Neuh¨auser,G.D.Ruxton,Effectiveuseofspearman’s and kendall’scorrelationcoefficientsforassociationbetweentwomea- sured traits,AnimalBehaviour102(2015)77–84.

L.McHugh,Interraterreliability:thekappastatistic,Biochemia medica 22(3)(2012)276–282.

Shull,J.Singer,D.I.Sjøberg,Guidetoadvancedempiricalsoftware engineering, Springer,2007.

Ralph, N. b. Ali, S. Baltes, D. Bianculli, J. Diaz, Y. Dittrich, N. Ernst, M. Felderer, R.Feldt, A.Filieri,etal.,Empiricalstandardsforsoftware engineering research,arXivpreprintarXiv:2010.03525(2020).

37


---

