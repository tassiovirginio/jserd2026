<!-- Página 1 -->

2018 ACM/IEEE 40th International Conference on Software Engineering

### Sentiment

### Software

### Engineering:

### How Can Go?

### Bin

Software Università Switzerland

### Massimiliano

DepartmentUniversityItaly

**ABSTRACT** Sentimentbeen ingreviews ers’ analysis since notsilver let datasets Weexperiencemender

To goal, sentences/words sentiment effort- time-consumingresultstive.focus performedofSEimpactdatasets

community strong ysis

**CCS CONCEPTS** •→;

**KEYWORDS** sentiment

**ACM** Bin Lanza, Rocco ing:ICSE 40th International on New York, USA,

Permission classroom is forthat copies notice the on author(s)republish,

and/orICSE ’18,©

2018 Copyright AssociationACM[https://doi.org/10.1145/3180155.3180195](https://doi.org/10.1145/3180155.3180195)

### Fiorella

DepartmentUniversityItaly

### Michele

### Lanza

SoftwareInstitute Università Switzerland

**1** Recenttoolscally mine

of expressedsummarize viewers’

its tomers’ Theadopted menttheet [

27]), APIs [38].et [

5] emotions openal. impactissue resolution et [ of Mostdesigned to box” usage beento achievedthey have

Stanford[32]been reviews.thesuccessful

their customization. Thus, tools The [ 34].SentiStrength ingpositive/negative thento

besentiment ForZibran which

94

### Gabriele

Software Università Switzerland

### Rocco

STAKEUniversityItaly

26].

32]).26]isafrequentlyaffective

6]et[

35]distressal.[

24]

31]sentiment

16,23,35].

15,36]. SentiStrength assesses sentiment

SentiStrengthcan

15]SentiStrength −,


---

<!-- Página 2 -->

ICSE MayB.

Inspired and developers.quality exploiting ionscomponent a developers’usabilitywarning

wassentiment tool Stack mining based sentimentby positive/negative byway wordsmeaning We to total∼40kOverflow. Despite performed els aactual performance engineeringgoal of toexperimentedniques

as ingSentiStrength− three dataseton trackers reviews Our a the approachesprecision on sentences).marginally reviews in the scenarios The ourcurrent sentimentefforts

alsoa analysis assuming that theto performance.large allthe to**Structure**

ment andoriginalSectionnegative

when Sectiondesign results to performance engineeringthreats could validity lessonspaper.

Sectionavailable

[ 15]).

**2** We toolsapplications engineering the datasets. tools used**Table**SE 16,23,35]

**Tool****Technique****Trained** SentiStrengthRule-basedMySpace[7–11][36]NLTK/VADERRule-basedMicro-Blog[30]StanfordRecurs.MovieworkEmoTextLexicalSentiStrength − SentiStrengthJIRA[15]Uddin

**2.1** There several areMeaningCloud WatsonNaturalLanguageUnderstanding ment 4such asRapidMinerorWeka[ 12], well extension

engineeringSentiStrength [ 34] 5oncomments.

and strengthasing for

assigns undersentenceming

SentiStrengthmakes text atedZibran adoptedNLTK [ 14]rule-based ingVADER(ValencesEntimentat VADERiscorporating

microblog-like 18], independentStanford [ 32] work,SentiStrength itssentiment how wordsmeaningby summing trained 1[https://www.meaningcloud.com/developer/sentiment-analysis](https://www.meaningcloud.com/developer/sentiment-analysis) 2[https://getsentiment.3scale.net/](https://getsentiment.3scale.net/) 3[https://www.ibm.com/watson/services/natural-language-understanding/](https://www.ibm.com/watson/services/natural-language-understanding/) 4[https://rapidminer.com](https://rapidminer.com) 5[https://myspace.com/](https://myspace.com/)

95

12,GetSentiment,or 3.also

SentiWordNet[ 1]an WordNet[ 20])ment

SentiStrengthison sentimenta

SentiStrength

15]

andNLTKthanks


---

<!-- Página 3 -->

SentimentCan WeICSE MayEmoTxt

[ 2].that combineset [24] lexical lexicon ,, putedSentiStrength) uncertainty . ofEmoTxtrelies as anger. been on

**2.2** Sentimentbeen neeringe.g., commit messages) crowd-generated users’ Sentiment mitissues17].et [9]senti- ment projects tiveauthors found more et [31] 28,466 results thatmost Also, authors numbersentiment mits et [24]correlation between sentimenttimefixissue

Silva [33]relation builds thatis the Analyzing polarity support3,6,11,27]. et [ 6] observingaddress tothat certain toet [3] niqueSentiment extractpresent ions et [8,11]use SentiStrengthtoet [27]used a to “sentiment isto the etc.). Sentimentalso been related7]. indicatedrelevanteven if

softwarecontinuous applications Asimpact tionsatisfaction,also been

used topsychological and10]role of emotional et [4] angeret [

security-relatedet [ tionemotions activity Open tors positive deviate expected Sentiment also deficienciesement or

**2.3****Software**

While authors uationother analysis classification. researchers texts under Tourani et [35]SentiStrength

successful Tomcat Ant. very lowi.e.,13.1% negative technical difficulty tive/negativeet [

niquesaffective con, Jongeling et [16]widelysentiment SentiStrength andAlchemyAPI. labeledet [ 21]provide expressedobservedonly between

ysis thealso between analysis thatresult results Thefortechnique

the Following softwareZibran SentiStrength −based major other toolSentiStrength.

96

30].

28]evidence

5]rela-

29]

toinformation

SentiStrengthachieved

23]andchallenges

,NLTK,Stanford,

15]oped SentiStrengthto


---

<!-- Página 4 -->

ICSE MayB.

Uddin Khomh36]polarity neutral) version

aboutKhomh the knowledge,authors tomizesoftware engineering

**3** Weinitialsoftwaretaskoffunctional

developer paramount not Themining

websitesto resultsthis reason, ing overall

8

**Developer****Front-end** stack overﬂow 93

opinionﬁne-grainedminerlinker

45 67

database

**Figure**

Thedependencies 1and3), fullofcomponent

miner mines maven libraries1in description, link tojaroflicense, (v)list information in2. fine-grained mines discussionslibraries stored4and discussions3.

6[http://central.maven.org/maven2/maven/](http://central.maven.org/maven2/maven/)

13].wassummarize

Maven

1 librariesminer

2

6all

Knowing sentencesopinion miner component6,expressedsentimentsneutral ,or ),one.g.,

usability,store them7. Finally, developer abouttask

quirements8.This information identify most functional Inworkopinion component,report theresults

**3.1****Datasets**

Previous 23,35]Using ing results .reviewsdomain-specific example, wordhas

positive notresearchers

ingsentiment terms SentiStrength − by Despite effort tomized analysisSentiStrength tools sentiment words and thesentenceexam- ple,I recommend though fast aspresence tivebeenby Stanford[ 32]sentiment

sivesentiment basedmeaning

requiredIndeed, sufficient plypolarity ahow positive/negativegrammaticallyofpolarity

intermediate Weexample (sequencesneutral polarity, ones negative sentiment, positive sentiment.sen- tence aroot of despite presence intermediate

97

9to

16,

34]).

32].Clearly,


---

<!-- Página 5 -->

SentimentCan WeICSE MayGothenburg,

I would

recommend

**Figure****ford CoreNLP**

To sentencetheFig. RNNfast

hasoverall expressinglibrary to notlibrary ” GivenStack

tool32],customized training for 23,35], reviews

3.1.1from the

list oflibrary /libraries, API ). original goal i.e., opinions), possible discussions theStanford

score The now on, Thesentence)withindicating

positive, +2 sentimentrandom, driven vationby

7tool. intermediatenodeword).bias,did

thenode knowing context duce a 7[https://nlp.stanford.edu/sentiment/trainDevTestTrees_PTB.zip](https://nlp.stanford.edu/sentiment/trainDevTestTrees_PTB.zip)

this

toolkit

Stanford

,even

though

it

is

robust

StanfordCoreNLP

19].sentences

[ 32]

Web application thus reducing subjectivity working the from the×node). Once labeling conflicts differentconflicts completeIndeed,

fastdouble-checked theand approach.intermediate/leaf ofdecidedstrongfor a

≥2( one gave 1, -1),2,076 havingpoint. assignedoneother expected scores,evaluators, whileround[(+)2]12 roundis thisievaluator.

**4** 16, Beforeopinion assessin recommendationassessment of are131performed adivided 1,500 different composed a the set, allremaining 1,350used for 8. between negative ,, positive opinions, sentiment setwith “-2” and “-1” are

“0”“+2” as Weoutput same Weaccuracy andoverall would bevast majority neutral opinions inneutral classifier accuracy,negative andopinions). Tableresults 9NLPon

8TheStanfordCoreNLPtooltraining so development set the 300development 9Stanfordis newmodel OverflowStanfordCoreNLPis ofStanfordCoreNLPwith the

98

Stanford

∼90

si

-


---

<!-- Página 6 -->

ICSE MayB.Oliveto**Table****discussions.**

**batch #****prediction**

**1**113

**Overall**1139

The positive/neutral/negative the the concrete

Sentence

It

Anyway,allow want.

Thespecific training,Stanford inIndeed, precision is of correctlysmall

identified. sentences Based theStanford

besides huge spent with alarge effectivethis reason, tooriginal perform curacy datasets.aim tospecificaccuracy

**#****positive positive****sentences precision recall**

10 15 15 9 10 11 6 17 18 20 131

StanfordSO.**Table****CoreNLP**

OraclePrediction

PositiveHope PositiveNegativeThereAPI. NeutralHow is NeutralNegativeI able toApp Engine Negative NegativeNeutral

does

Stanford

anforwill

Stanford

**#****neutral neutral**

118 118 121 122 119 118 130 116 113 116 1191 0.836

sentimentwhether timentable to engineeringmanually flowalso help uscurrent analysis

**5****SOFTWARE**

The ofaccuracy sis purpose ofimpact fectiveness. context ofthree

mobile reviews,

**5.1** Thefollowing**RQ** **:**How does1 other sentimentWe state-of-the-art Stack limitationscan choice Stanford existing**RQ** **:**Do2 ofWe which, e.g.,app would posts. example, sentences app the

The threei.e., i.e.,users’ onissue i.e.,

99

**#****negative negative**

**2**112 **3**116 **4**123 **5**110 **6**129 **7**93 **8**117 **9**111 **10**115

Stanford

Stanford Stanford wasother

22 17 14 19 21 21 14 17 19 14 178

perform

. and


---

<!-- Página 7 -->

SentimentCan WeICSE May

We es studie sis2,24,27,36]. goal is sentiment theeach contain. Thecess and•

thed evaluateStanford• Wereviewstheet [

main bug suggestionre non-functional( p other (meaning,b categories).random sure categories oftheselesele

reviews confidence ± Once view.cessof (fromto where the involve• We dataset et [25], resp elove joy , sadness . dataset b d several evaluating labele with emotions: love joyanger, sadness, fear Among sixlove joy , sadness are Aset [ with the or intothose lab anger orinto Table for tracte

**Table**d**in**

Datasetpneutral negative

StackApp341JIRA issue926 •.

**5.2** Onerimente following p

We ground

37],containsbasisof

15,16].

16],

do give sentiment of instead, twosentiment scores analyze expresse text from negative), other 1sum scores, map theb neutral,•. Base d four“neutral”,“comp“neutral”, “p

score andauthor 10of, use tosentiment p−0 < .scor ≤− .•. ByStanford sentimenty ative,yare interestepitive opinions,ver

p•. As and samed sentimentsame SentiStrength.• Similarly,adopte Stanfordtothre

and sentences Weaccuracy pre p

**5.3** Table thefive senti- ment table reppre

sentences. eachb highlighte**b**. aimingresearch

5.3.1:Stanford1

we AsStanford moStanford, tencesStanfordachieves etter re almost same sentencesStanfordis crement cision. 10[https://github.com/cjhutto/vaderSentiment](https://github.com/cjhutto/vaderSentiment) 11Ind development

100

NLTKrep

scor ≥0. 5:

rep

SentiStrength,

11.

ppare , analyzethefive Stack1

with the


---

<!-- Página 8 -->

ICSE MayB.**Table**sentimentbest

**#****dataset****prediction**

SentiStrength1,043**Stack**

SentiStrength213**App reviews**

SentiStrength**714****JIRA**

However,increment toStanfordprovides Stanford. andStanfordshould theStanfordmodellabeledsentences >215k nodes).Stanford smallerThus, couldStanford as Whenanalysisthat experimented

more assess whileable to neutralandexample,toolhaving highest identifying

SentiStrength) spot aof willbeThe33.3%chance

touse sentiment Stack**RQ** **main**(i)1 SOprovide pared dictionbiasedmajority (neutral)recall achieved; all impossible a Stack

Stanford

is

.

Stanford

**positive positive****neutral neutral****negative negative****precision recall**

0.200 0.3590.8580.397NLTK1,168 **0.317 0.244**0.815 0.941**0.625 0.084**Stanford604 0.231**0.884 0.344**0.177 0.837SentiStrength-SE**1,170** 0.3120.8260.500Stanford1,139 **0.317 0.145**0.8360.365

0.745 0.8660.1130.815NLTK184 0.7510.093 0.440**1.000 0.169**Stanford**237** **0.831 0.715****0.176 0.240**0.667 0.754SentiStrength-SE201 0.7410.1060.929Stanford142 0.7700.0840.470

0.850 0.921--0.993NLTK276 0.840--**1.000 0.269**Stanford626 0.726--0.945SentiStrength-SE704 **0.948 0.883**--0.996 0.704Stanford333 0.635--0.724

5.3.2: different2 formanceTo, compare2 thestudy.that,

differently tools values.results in better.Stanfordis identifying tools. datasets, reviews be reviews, originalStanford trained. exhibitto that, itive and negative presence/absence bugcase formore vocabulary When SentiStrengthand−have betterother SentiStrength −providing recalltwo categories andmostly experimentedsomeissueson

First, absenceprovide and shown reviews, theto that they represent that Second, in

101

is


---

<!-- Página 9 -->

SentimentCan WeICSE May**Table**

**SentiStrength**positive

positiveneutralnegative

**NLTK**positive

positiveneutralnegative

**Stanford**positive

positiveneutralnegative

**SentiStrength-SE**positive

positiveneutralnegative

**Stanford**positive

positiveneutralnegative

However,always instance, tivealwaysor ( thanksthus partial Toimportanceitems of sentimentconfusion obtaineddifferent Overflow All effectivenegative example, Stanford classified tencesNLTKonly misclassifies negative as **RQ**areto and .issueset [ SentiStrengthon this sentimentcontaining tences theperformance neutral

**main**2 is,claim because positive/negativeaccuracy onacceptable app reviewsaccuracylow,JIRAbe

consideredto

**6**VALIDITY **Threats** ory sentiment terpretedlabeling jective conflictguaranteed manually assigned Anotheri.e.,five-scaleexpressednegativetake then

theneutral negative sentiment be**Threats**

notvariables the investigated.to of usethreshold forNLTK. increase sentiment**Threats**

theoutcome. randomly from Stackapp dataset37].significant wesamples representative whole**Threats**

monly less lotsnaturalguagefew of

andgoal is toin only tools

only mis- softwarelimited quently otherchats,

**7**35]whenusing **No**real**pressed**

ones specifically isrecall tool

102

The

concern relation

concern

concern relation

concern generalizabilityourevaluation considered most

No


---

<!-- Página 10 -->

ICSE MayB.

By ommendationsato

ways buildingexample, Khomh36] opinionsaccuracy the tive/negative**Specific****silver improving**

hasthat sentiment of-the-box cases,cope with specificarenegative( the bugcarries

be shown, in customization tool words,for makeit.such as

case, theintoa

clear improvement Stanfordaccuracy.**Some****analysis**

better cases,opinion ana problem.tools aretools’thecategorybesides lack ofse

the playdifferent mostlyandlineswhether

code pattern expressingapplicability of**Should****tools?**

No,of1,500

279not **Text reporting****ficient** This iset [ mining: joyhard todo

said usable

Sentiment

Previous

15,16,23,35]. some

21]emotion

most difficult tweenvsquite effectivenegativeThis isthat we,

in analysis hopedataset more

**8** Some that the workwith consider wanted and ments. thatStack was recurrentwork noticednotopinion componentThe

machine a completelyblackdesign

garbage notbe produced.might is placehigh: developers opinion ourmore evident,problem accuracy

analysis In we Walter important lesssear for approaches ”. appreciateinsights work. arecompletepackage.wedismissing

but the that a mining practice.

**ACKNOWLEDGMENTS** Wefinancial tionalthe No.JITRA172479), CHOOSE sponsoring trip conference.

103

15,16], not

**write**

As

18]

.As


---

<!-- Página 11 -->

### Sentiment

###

###

### Can We

### ICSE May

###

###

###

## REFERENCES

[1]Stefano 3.0:Opinion In Evaluation).[2] Fabio for ConferenceIntelligent.[3] L.proach

International.[4] Daviti brenik. In Engineering) .[5] DavidFrank Emotions In Computing)[6] MichaelKaren aging Enterprise ported International.[7] EmitzaNorbert exploratory TwitterRequirements22, (2017),[8]

ions SymposiumMeasurement) .[9] EmitzaYang comments Conference.[10] Emitza software on.[11] Emitza fineProceedings International.[12] MarkandSIGKDD

Explorations 11,[13] Minqing andsummarizing Proceedings discovery data.[14] ClaytonProceedings InternationalSocial .[15] Md analysisConference.[16]

2017.software engineeringEmpirical(2017),[17] Francisco software [21]issues. JournalSoftware 104[18] BinLanza,

github.io/replication.zip. d.]).[19] Christopher Bethard, Processing Demonstrations .[20] GeorgeCommun. 38,

Alessandro developers emotions? facts. Repositories) .[22] NicoleFilippo theInternational Workshop.[23] NicoleSentimentProceedings

SSE. 33–40.[24] Marco esi, ofProceedings Conference.[25] MarcoTonelli,Bram

developers Mining.[26] Bo LillianSentiment Founda- tions and2[27] Sebastiano GerardoHaraldApp? fyingProceedings ICSMEEvolution) (ICSME .[28] Daniel emotion:Proceedingsof.

348–351.[29] MohammadIman ommending In Code Analysis Manipulation).[30] Athanasios-Ilias Barahona.findings,

1–6.[31] Vinayak Bonita ment on.[32] Richard ning, semantic 2013 (2013. Citeseer.[33] RodrigoIn

Repositories) .[34] Mike 2010. tionTechnology61,[35] Parastou in Proceedings Science Software.[36] Gias Uddin FoutseAspects.Report.

[37]LorenzoMassimil- iano Di Proceedings. 14–24.[38] Yingying DaqingFeatures Forum Program.

104


---

