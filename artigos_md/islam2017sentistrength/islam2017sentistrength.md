<!-- Página 1 -->

### Accepted Manuscript

SentiStrength-SE: Exploiting Sentiment Analysis

Md Rakibul

PII: S0164-1212(18)30167-5 DOI: [https://doi.org/10.1016/j.jss.2018.08.030](https://doi.org/10.1016/j.jss.2018.08.030) Reference: JSS

To appear

Received date: Revised date: Accepted date:

Please cite SpeciÞcity for *Software*

This is to our copyediting, typesetting, and review of the resulting proof before it is published in its Þnal form. Please note that all legal

###

DomainSpeciÞcityforImproved inSoftwareEngineeringText

Islam,MinhazF.Zibran

10209

in:*The Journal**of**Systems**&**Software*

3July2017 18June2018 10August2018

thisarticleas:MdRakibulIslam,MinhazF.Zibran,SentiStrength-SE: ImprovedSentimentAnalysisinSoftwareEngineeringText,*The Journal* (2018), doi:[https://doi.org/10.1016/j.jss.2018.08.030](https://doi.org/10.1016/j.jss.2018.08.030)

aPDFÞleofanuneditedmanuscriptthathasbeenacceptedfor customersweareprovidingthisearlyversionofthemanuscript.The

duringtheproductionprocesserrorsmaybediscoveredwhichcould disclaimersthatapplytothejournalpertain.

Exploiting *of**Systems*

publication. manuscript

affectthe

Domain *&*

Asaservice willundergo

content,and


---

<!-- Página 2 -->

### ACCEPTED MANUSCRIPT

### SentiStrength-SE:

### Exploiting Domain Specicity for

### Improved

### Sentiment Analysis in

### Software Engineering Text

Md Rakibul Islam

University

MinhazF. Zibran

University

Abstract

Automatedsentiment analysis in software engineering textual artifacts has long been

sueringfrom inaccuracies in those few tools available for the purpose. We

an in-depth qualitative study to identify the diculties responsible for such low accu-

racy.Majority of the exposed diculties are then carefully addressed through building

a domain dictionary and appropriate heuristics. These

then realizedSentiStrength-SEin, a tool we have developed for improved sentiment

analysisin text especially designed for application in the software engineering domain.

Usinga benchmark dataset consisting of 5,600 manually annotated JIRA issue com-

ments,we carry out both qualitative and quantitative evaluations of our tool. We

separatelyevaluate the contributions of individual major components (i.e., domain dic-

tionaryand heuristics)SentiStrength-SEof. The empirical evaluations conrm that

the domain specicity exploited in our

outperformtheexistingdomain-independenttools/toolkits

and StanfordNLP) in detecting sentiments in software engineering text.

Keywords:Sentiments,Emotions, Software Engineering, Empirical Study,

Automation,Domain Dictionary

Email[mislam3@uno.edu](mailto:mislam3@uno.edu)(Md[zibran@cs.uno.edu](mailto:zibran@cs.uno.edu)

# ACCEPTED MANUSCRIPT

Preprint

domain-specic techniques are

enablesit to substantially

SentiStrength(

(Minhaz

, NLTK,

conduct

also


---

<!-- Página 3 -->

### ACCEPTED MANUSCRIPT

11. Introduction

2Emotionsareaninseparable partofhuman nature, which inuence people's ac-

3tivitiesand interactions, and thus emotions aect task quality, productivity, creativity,

4grouprapport and job satisfaction [1]. Software development, being highly dependent

5on human eorts and interactions, is more susceptible to emotions of the practitioners.

6Hence,a good understanding of the developers' emotions and their inuencing factors

7can be exploited for eective collaborations, task assignments [2], and in devising mea-

8suresto boost up job satisfaction, which, in turn, can result in increased productivity

9and projects' success.

10Severalstudies have been performed in the past for understanding the role of human

11aspectson software development and engineering. Some of those earlier studies address

12whenand whyemployeesget aected by emotions [1, 3, 4, 5, 6], whereas some other

13workaddresshow[7, 8,9,10,11,12,13,14]theemotions impact the

14performanceat work.

15Attemptsare made to capture the developers' emotions in the workplace by means

16of traditional approaches such as,interviews, surveys [13],and

17ments[15]. Capturingemotions with the traditional approaches is more challenging

18forprojects relying on geographically distributed team settings and voluntary contribu-

19tions(e.g., open-source projects) [3, 16]. Moreover, the traditional approaches involv-

20ing direct observations and interactions with the developers often hinder their natural

21workow.Thus, to supplement or complement those traditional approaches, recent at-

22temptsdetect sentiments from the software engineering textual artifacts such as issue

23comments[3,5, 8, 9, 11, 17, 18, 19], email contents [6, 20], and forum posts [4, 21].

24For automated extraction ofsentiments from textual artifacts in

25gineeringdomain, threetoolsSentiStrength(i.e.,[22],NLTK(NaturalLanguage

26Toolkit)[23], andStanfordNLP[24])areusedwhile theuseSentiStrengthof

27is found dominant [25, 26]. However, software engineering studies [5, 6, 8, 18, 19, 25,

2827, 28] involving sentiment analysis repeatedly report concerns about the accuracy of

29thosesentiment analysis tools in the detection of sentimental polarities (i.e., negativ-

30ity,positivity, and neutrality) of plain text contents. Forexample, when applied in the

# ACCEPTED MANUSCRIPT

2

employees'

biometric measure-

thesoftware en-


---

<!-- Página 4 -->

31softwareengineering domain,

32haveonly 29.56% and 52.17% precision in identifying positive sentiments, and

33lowerprecision of 13.18% and 23.45% respectively in the detection of negative senti-

34ments[6, 25].

35Thosesentiment analysis tools

36technicalsocial networking media (e.g., twitter posts, forum

37whenoperated in a technical domain such as software engineering, their accuracy sub-

38stantiallydegrades largely due to domain-specic variations in meanings of frequently

39usedtechnical terms. Although

40dicultyagainst automated sentiment analysis in textual content, we need a deeper un-

41derstandingof why and how such domain dependencies aect the performance of the

42tools,and how we can mitigate them. Indeed, the software engineering community de-

43mandsa more accurate automatic sentiment analysis tool [5, 6, 9, 18, 19, 27, 29, 30].

44In this regard, this paper makes three major contributions:

45Usinga large benchmark dataset, we carry out an in-depth exploratory study for

46exposingthe diculties in automatic sentiment analysis in textual content in a

47technicaldomain such as software engineering.

48Wedevelop adomain

49bestof our knowledge, this is the rst domain-specic sentiment analysis dictio-

50nary for the software engineering domain.

51Wepropose techniques and realize those

52that we develop for improved sentiment analysis in software engineering textual

53content.The tool is also made freely available online [31].

54is the rst domain-specic sentiment analysis tool especially designed for soft-

55wareengineering text.

56Insteadof building a tool from scratch, we develop

57of SentiStrength[22],

58sentimentanalysis in software engineering [32]. From

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

SentiStrength

dictionary

which, till date, is the most widely used tool for automated

are

such a

specic

3

and NLTKare respectively reported to

developed and

domain dependency is indicated as a

for software engineering text. To

SentiStrength-SEin

SentiStrength-SE

trained using

, a prototype tool

our

quantitative comparison with

data

movie reviews) and

on top

even

fromnon-

general

the


---

<!-- Página 5 -->

59the originalSentiStrength

60wareengineering domain, we nd that our domain-specic

61icantlyoutperforms those domain independent tools/toolkits. We also separately eval-

62uatethe contributions of individual major components (i.e., the domain dictionary and

63heuristics)of SentiStrength-SE

64text.Ourevaluations demonstrate that, for software engineering text, domain-specic

65sentimentanalysis techniques perform substantially better in detecting sentiments accu-

66rately.We further conduct a qualitative evaluation of our tool. Based on the exploratory

67studyand the qualitative evaluation, we outline plans for further improvements in au-

68tomatedsentiment analysis in the software engineering area.

69Thispaper is a signicant extension to our recent work [32]. This

70new evidence and insights

71sentimentanalysis in software engineering text. The techniques applied in the develop-

72mentof SentiStrength-SE

73of the tool is substantially extended

74isonswithNLTKandStanford

75with the originalSentiStrength. We

76majorcomponents (i.e., the domain dictionary and heuristics)

77The quantitative comparisons are validated in the light of statistical tests of signicance.

78Outline:The rest of the paper is organized as follows. Section 2 describes a qualitative

79empiricalstudy that reveals the challenges in automated sentiment analysis in software

80engineering.InSection 3, we introduce

81we have developed by addressing the identied diculties. Section

82titativeand qualitative evaluation of our tool. In

83validityof the empirical evaluation. In Section 5, we discuss scopes for further improve-

84mentsand future research directions. Related

85Section7 concludes the paper.

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

[22],

by including

are described in

NLP

NLTKand Stanford

in sentiment analysis in software engineering

deeperaanalysis

deeperwithqualitative analyses and direct compar-

in addition to the previously published comparison

include separate evaluations of the individual

SentiStrength-SE, the prototype tool, that

4

NLPas operated in the soft-

SentiStrength-SE

of the diculties in automated

detail. The empirical evaluation

SentiStrength-SE

Section 4.9 we discuss the threats to

work is discussed in Section 6. Finally,

signif-

of.

4, presents quan-

presents


---

<!-- Página 6 -->

### ACCEPTED MANUSCRIPT

862. ExploratoryStudy of the Diculties in Sentiment Analysis

87Toexplore the diculties in automated sentiment detection in text, we conduct our

88qualitativeanalysis aroundJavatheversionof SentiStrength[22].ThisJavaver-

89sionis the latest releaseSentiStrengthof, while the older version, strictly for use

90on Windows platform, isstill available. AsmentionedSentiStrengthbefore,is a

91state-of-the-artsentiment analysis tool most widely adopted in the software engineer-

92ing community. Thereasons for choosing this particular tool are further justied in

93Section6.

94Englishdictionaries consider the words `emotion' and `sentiment' as synonymous,

95and accordingly the words are often used in practice. Although there is arguably a subtle

96dierencebetween the two, in describing this work, we consider them synonymous. We

97formalizethat, aside from subjectivity, a human expression can have two perceivable

98dimensions:sentimentalpolarityandintensity. Sentimentalindi-

99catesthe positivity, negativity, or neutrality of expression while sentimental

100capturesthe strength of the emotional/sentimentalexpression, which sentiment analysis

101toolsoften report in numeric emotional scores.

1022.1.BenchmarkData

103In our work, we use a Gold Standard" dataset [29, 33], which consists of 5,992 issue

104commentsextracted from JIRA issue tracking system. Theentire dataset isdivided

105in three groups named as Group-1, Group-2 and Group-3 containing 392, 1,600 and

1064,000issue comments respectively. Eachof the 5,992are manually

107interpretedby distincthuman raters [29] and annotated with emotional expressions

108as found inthose comments. ForGroup-1,n= 4whilefor Group-2 andGroup-3,

109n= 3. Thisistheonly publicly available such dataset inthesoftware engineering

110domain[29, 32].

111A closed setEof emotionalexpressionsare usedintheannotation oftheissue

112commentsin the dataset, whereE= { joy,love, surprise, anger, sad,}. Thefearhuman

113raterslabeled each of the issue comments depending on whether or not they found the

# ACCEPTED MANUSCRIPT

5


---

<!-- Página 7 -->

### ACCEPTED MANUSCRIPT

114sentimentalexpressions in the comments. Formally,

h 1 ;if emotionEis found inCby raterr .nrijj.C / =FlEi0 ;otherwise.n j

115An example of human annotations of an issue comment from the dataset is shown in

116Table1.

Table

Issuecomment(CommentID-53257):Thanksforthepatch;Michale.

Appliedwithafewmodifications.

HumanEmotions(E)i

Raters() JoyLoveSurpriseAngerSadnessFearj

Rater-1( )1 10 0001

Rater-2( ) 0000002

Rater-3( )10 00003

Rater-4( )10 00004

Interpretation:rater-1found `joy' and `love' inthecomment, while rater-3 and

rater-4found thepresence ofonly `love' butrater-2 didnotidentify any of

emotionalexpressions.

1172.2.EmotionalExpressions to Sentimental Polarities

118Emotionalexpressionsjoy andloveconveypositivesentimentalpolarity, while

119anger, sadness, andf earexpressnegativepolarity.Insome cases, an expression of + 120surprisecan be positive in polarity, denoted as, while other cases can convey * 121a negativesurprise, denoted as. Thus the issue comments in the benchmark

122dataset,which are annotatedsurprisewithexpression,need to be further distinguished

123basedon the sentimental polarities they convey. Hence, we get each of such comments

124reinterpretedby three additional human (computer science graduate students) raters,

125who independently determine polarities of the surprise expressions in each comments.

126Weconsider aexpressionin a comment polarized negatively (or positively),

127if two of the three rates identify negative (or positive) polarity in it. We found 79 issue

# ACCEPTED MANUSCRIPT

6

the


---

<!-- Página 8 -->

### ACCEPTED MANUSCRIPT

128commentsin the benchmark dataset, which were annotated with theexpres-

129sion.20 of them expresssurprisewith positive polarity and the rest 59 convey negative

130surprise.

131Thenwe split theEof emotional expressions into two disjointE sets=as+

+* 132^ joy; love; surprise`and E= ^anger; sad; f ear;` . Thus,Econtains*+

133onlythe positive sentimental expressionsEcontainsandonly the negative*

134expressions.Asimilar approach isalso used inother studies [25, 34]tocategorize

135emotionalexpressions according to their polarities.

1362.3.Computationof emotional scores from human rated dataset

137For each of the issue comments in the Gold Standard" dataset, we compute sen-

138timentalpolarity using thelabels assessed by the human raters. Foran issue rrjj 139commentCratedbyn humanraters, we compute a pair; ë of values for each ofcc

140then ratersr(where1 fj fn ) using Equation 1 and2:j

³rhj1 ;ifF.C / >0 EnrijE  Ei+=(1)lc n0 ;otherwise.j

³rhj1 ;ifF.C / >0 EnrijE  Ei*=(2)lc n0 ;otherwise.j

141Thus,if a raterrndsthe presence of any of the positive sentimental expressions inj rrjjthe commentC, then142= 1, otherwise= 0. Similarly,ifany ofthenegativecc rrjj 143sentimentalexpressions are found in the comment, then= 1 , otherwise= 0 .cc

144An issue commentCis considered neutral insentimental polarity, ifweget the rrrrjjjj 145= 0. If= 0and ë forat leastn * 1(i.e.,majority) raterswhere; pairsêcccc

146the comment is not neutral, then we determine the positive and negative sentimental

147polaritiesof that issue comment. Todo that, using the following equations, we count

148the number of human raters,R.C / who found positive sentiment in the commentC+

149and also the number of raters,R.C /, who found negative sentiment in the commentC .*

# ACCEPTED MANUSCRIPT

7


---

<!-- Página 9 -->

### ACCEPTED MANUSCRIPT

nnÉÉrrjj150andR.C / =R.C / =cc*+ j =1j =1

151An issue commentCis considered exhibiting positive sentiment,n *if1 at least

152man raters found positive sentiment in the message. Similarly, we consider a comment

153havingnegative sentiment if atn *least1ratersfoundin it. Finally, hh 154we compute the sentimental polarities of an issueC commenta pairê;  ëusingcc

155Equation3 and4.

h 0 ;ifCis neutraln nh=(3)+1 ;ifR.C / gn * 1lc+ n *1 ;otherwise.n j

h 0 ;ifCis neutraln nh(4)=+1 ;ifR.C / gn * 1lc* n *1 ;otherwise.n j

hh 156Thus,= 1, only if the commentChas positive sentimentand= 1onlyifcc

157the comment contains negative sentiment. Note that, a givencan exhibit both

158positiveandnegative sentiments atthesame time. Acomment isconsidered senti- hh 159mentallyneutral when the pair;  ëforthe comment appear toê0be0 ë. Anissuecc

160commentis discarded from our study ifnat* 1leasthumanraters (i.e., majority) could

161not agree on any particular sentimental polarity of the comment. Wehave found 33

162suchcomments in Group-2 dataset that are excluded from our study. Similar approach

163is also followed to determine sentiments of comments in another study [25].

1642.3.1.Illustrative Example of Computing sentimental Polarity

165Considerthe issue comment in Table 1. Forthiscomment, we compute the rrjj 166pairê; ë forall four ratersn(i.e.,= 4 ). Asfor only one (the second rater) out ofcc

167fourraters we get the pairê0 ;0 ëasthe comment is not considered neutral. Hence, we

168computethe valuesRof .C / andR.C /, which are three and zero respectively.R.C /+*+

# ACCEPTED MANUSCRIPT

8


---

<!-- Página 10 -->

### ACCEPTED MANUSCRIPT

h 169beingthree satises the conditionR.C / gn * 1. Thus,= 1 , which means that+c

170the comment in Table 1 has positive sentiment. For the sameR.C / < n* 1*

h 171and so= *1, which signies that the comment has no negative sentiment.c

1722.4.SentimentDetection UsingSentiStrength

173WeapplySentiStrengthto determine the sentiments expressed in the issue com-

174mentsin Group-1 of the Gold Standard" dataset. Sentiment analysisSentiStrengthusing

175on a given piece of text (e.g., an issueCcomment)computesa pairê;  ë of integers,cc

176where+1ff+5and *5ff*1 . Here,and respectivelyrepresent thecccc

177positiveand negative sentimental scores for theC givenAtexttextCis consid-

178eredto have positive sentiment> if. Similarly, a text is held containing negativec

179sentimentwhen<*1 . Besides, a text is considered sentimentally neutral when thec

180sentimentalscores for the text appearê1 ;*1toë.be

181Hence,for the pairê;  ë of sentimental scores for an issue commentCcomputedcc

tt 182by SentiStrength, we compute another pair of integersê;  ë as follows:cc

hh 1 ;if<*1 :1 ;if>+1 :nn183andcctt==llcc 0 ;0 ;otherwise.nn jj

tt 184Here,= 1signiesthat the issue commentChas positive sentiment,and= 1cc

185impliesthat the issue commentChas negative sentiment.

186WeapplySentiStrengthto compute sentimental scores for each of the issue com-

187mentsin the Group-1 portion of the Gold Standard" dataset and then for each issue tt 188commentC , wecompute thepairê;  ë, which represents thesentimental polaritycc

189scoresforC .

1902.5.Analysisand Findings

191For each of the 392 issue commentsCin Group-1, we compare the sentimental po- tthh 192larityscoresê;  ë producedfromSentiStrengthand theê;  ë computedcccc

193usingour approach described in Section 2.3. We nd a total of 151 comments, for which

# ACCEPTED MANUSCRIPT

9


---

<!-- Página 11 -->

### ACCEPTED MANUSCRIPT

tthh 194theê;  ë scoresobtained fromSentiStrengthdo not match withê;  ë. This im-cccc

195pliesthat for those 151 issue commentsSentiStrength'scomputation of sentiments

196are probably incorrect.

197Upondeveloping asolidunderstanding ofthesentiment detection algorithm of

198SentiStrength, wethencarefully gothrough allofthose151issue comments to

199identifythereasons/diculties, whichmisleadin itsidentication

200of sentiments in textual content. Weidentify 12 such diculties. Beforediscussing

201the diculties, werst briey describe the highlightsSentiStrengthof'sinternal

202workingmechanism to develop necessary context and background for the reader.

TableSentiStrength's

Sent. SampleDictionary sentencelistcc

The`good'wordis It'sgoodSentimental pre-assigned2 feature.words signed

As`very'is It'svery timental3Booster good itive

Sentimental

isIt'snot a 1Negations tion`not'beforegood

sentimental

killeris

with It'skiller `kill'carries2 feature. overridden

phrase.

2032.5.1.InsightsSentiStrength'sInternal Algorithm

204SentiStrengthis a lexicon-based classier that also uses additional (non-lexical)

205linguisticinformation and rules to detect sentiment in plain text written in English [22].

206SentiStrengthmaintainsa dictionary of several lists of words and phrases as its key

207dictionariesto compute sentiments in texts. Amongthesesentimentallists, thewords

# ACCEPTED MANUSCRIPT

10


---

<!-- Página 12 -->

### ACCEPTED MANUSCRIPT

Table

DicultiesFrequency

D:Domain-specicmeanings of words 1231

D:Context-sensitivevariations in meanings of words 352

D:Misinterpretationof the letter `X' 123

D:Sentimentalwords in copy-pasted content (e.g., code) 124

D:Dicultiesin dealing with negations 085

D:Missingsentimental words in dictionary 026

D:Spellingerrors mislead sentiment analysis 027

D:Repetitivenumeric characters considered sentimental 018

D:Wrongdetection of proper nouns 019

D:Sentimentalwords in interrogative sentences 0110

D:Dicultyin dealing with irony and sarcasm 0111

D:Hardto detect subtle expression of sentiments 0712

*Here,SEDS = Software Engineering Domain Specic, SAG = Sentiment Analysis in General,

SST= Specic to theSentiStrength

208list,list of booster words, list, andphrases

209the computation of sentiments. Theentries in all these lists except the list of negation

210wordsare pre-assigned with sentimental scores. The

211are used to invert the sentimental polarity of a term when the term is located after a

212negationword in text.

213For an input sentence,SentiStrengthextracts

214and searches for each of the individual words

215correspondingsentimental scores. Similar search is made

216strengthenor weaken the sentimental scores.

217groupsofwords ascommonly usedphrases. When

218sentimentalscore of the phrase overrides

219whichconstitute the phrase. Theexamples in Table 2 articulate

220dependson the dictionary of lists for computing sentimental scores in plain texts.

# ACCEPTED MANUSCRIPT

11

(% )Scope*

(60.00) SEDS

(17.07) SAG

(05.85) SEDS

(05.85) SEDS

(03.90) SAG

(00.97) SAG

(00.97) SAG

(00.49) SST

(00.49) SST

(00.49) SST

(00.49) SAG

(03.41) SAG

Tool.

of negations wordsplaya vital role in

negationin the fourth list

individual words from the sentence

sentimentalin thelistretrieve the

ofinboosterthewordsto

listThephrasesis used to distinguish

such aphrase isidentied, the

scores of the individual words,

SentiStrengthhow


---

<!-- Página 13 -->

### ACCEPTED MANUSCRIPT

2212.5.2.Dicultiesin Automated Sentiment Analysis in Software Engineering

222Table3 presents the number of times weSentiStrengthfoundbeingmislead by

223the 12 diculties as discovered during manual investigation.It is evident in Table 3 that

224domain-specicmeanings of wordsis the most prevalent among all the diculties that

225are liable for low accuracy of the lexical approachSentiStrengthof. However, not

226all the diculties are specic to software engineering domain, rather some

227impactsentiment analysis in general (including software engineering) while a few are

228actuallyspecic limitations ofthetool. Theright-most column in

229Table3 indicates the scopes of the identied diculties. We now describe 12 diculties

230with illustrative examples.

231(D) Domain-specic meanings ofwords:In atechnical eld, textual artifacts in-1

232cludemany technical jargons, which have polarities in terms of dictionary meanings,

233but do not really express any sentiments in their technical context. For

234words`Super', `Support', `Value' and `Resolve' are Englishwith known positive

235sentiment,whereas `Dead', `Block', `Default', and `Error' are known to have negative

236sentiment,but none of these words really bear any sentiment in software development

237artifacts.

238AsSentiStrengthwasoriginally developed and trained for non-technical texts writ-

239ten in plain English, it identies those words as sentimental words, which is incorrect in

240the context of a technical eld such as software engineering. In the following comment

241fromthe Gold Standard" dataset,SentiStrengthconsiders`Error' as negative sen-

242timentalword and detects `Support' and `Refresh' as positive sentimental words. Thus,

243it assigns both positive and negative sentimental scores to the comment, although the

244commentis sentimentally neutral.

245"ThiswasprobablyfixedbyWODEN-86whichintroducedsupportfor

246the curlybracesyntaxinthehttplocationtemplate.ThisJIRA

247can nowbeclosed.Thistestcaseisnowpassing...Thereare

248now 12errorsreportedforWodenonthistestcaseregenerated the

249resultsinr480113.I'llhavetheW3Creportsrefreshed."(Com-

250ment ID: 18059)

# ACCEPTED MANUSCRIPT

12

example, the


---

<!-- Página 14 -->

### ACCEPTED MANUSCRIPT

251(D) Context-sensitivevariations in meanings ofApartwords:from domain-specic2

252meaningsof words, in natural language, some words have multiple

253on the context in which they are used. For example, the word `Like' expresses positive

254sentimentwhen it is used in a sentenceIsuchlikeasyou". Onthe other hand, that

255sameword expresses nosentiment inthe sentenceI would like to beasailor, said

256GeorgeWashington". Again,SentiStrengthidentiesthe word `Please' as positive

257sentimentalword, although we nd the word is used as neutral to express request in

258the training dataset. Forexample, in the comment below, the word `Please' does not

259expressany emotion.

260"Updatedin1.2branch.David;pleasedownloadandtry1.2beta

261when itisreleasedinaweekorso.."(CommentID: 4223)

262Again,words that are considered inherently sentimental often do not carry sentiments

263whenused to express possibility and uncertainty. Distinguishing the context-sensitive

264meaningsof such words is a big challenge for automated sentiment analysis in text and

265the lexical approachSentiStrengthofalsofalls short in this regard.

266For example, in the following issue comment, the sentimental word `Nice' is used sim-

267plyto express possibility regarding change of something,SentiStrengthbutincor-

268rectlycomputes positive sentiment in the message.

269"The changeyouwantwouldbenice;butissimplynotpossible.

270The formdata...JakartaFileUploadlibrary."(CommentID: 51837)

271

272Similarly,in the comment, the sentimental word `Misuse' is used in a conditional sen-

273tence,which does not express any sentiment,SentiStrengthbutinterpretsotherwise.

274"Addedacoupleofsmallpoints...ifanyonenoticesanymisuses

275of thedocumentformatting..."(CommentID: 2463)

276(D) Misinterpretationof the letterIn informal computer mediated chat, the3

277`X' is often used to mean an action of `Kiss', which is a positive sentiment, and thus

278recordedinSentiStrength'sdictionary. However, in technical domain, the letter is

# ACCEPTED MANUSCRIPT

13

depending


---

<!-- Página 15 -->

### ACCEPTED MANUSCRIPT

279oftenused as a wildcard. Forexample, the sequence `1.4.x' in the following comment

280is used to indicate a collection of versions/releases.

281"IntegratedinApacheWicket1.4.x..."(Comment

282SinceSentiStrengthusesdot(.)asadelimiter to

283`x' is considered a one-word sentence and is misinterpreted to have expressed positive

284sentiment.

285(D) Sentimental words in copy-pasted content (e.g.,4

286opersoften copy-paste code snippets, stack traces, URLs, and camel-case words (e.g.,

287variablenames) in their issue comment. Such copy-pasted contents often include sen-

288timentalwords in the form of variable names and the like, which do not convey any

289sentimentof the committer,SentiStrengthbutdetects

290incorrectlyassociates those sentiments with the issue comment and the committer. Con-

291siderthe following issue comment, which includes a copy-pasted stack trace.

292"... Stack:[main]FATAL...org.apache.xalan.templates

293.ElemTemplateElement.resolvePrefixTables..."

294The words `Fatal' and `Resolve' (part of the camel case word `resolvePrexTables'),

295positiveand negative sentimental words respectively in the

296Hence,SentiStrengthdetectsboth positive and negative sentiments in the issue com-

297ment,but the stack trace content certainly does not represent the sentiments of the de-

298veloper/committer.

299(D) Diculties in dealing with negations:For automated sentiment detection, it is5

300crucialto identify the presence of any negation term preceding a sentimental word, be-

301causethe negation terms invert the polarity of

302the sentenceI am not in good mood"is equivalentI

303negationof the positive word `Good' cannot be identied as equivalent to the negative

304word`Bad', then detection of sentimental polarity goes wrong. The

305rationofSentiStrengthenablesit to detect negation of a sentimental

306the negation term is placedimmediatelybeforethe sentimental word. In all other cases,

307SentiStrengthfailsto detect negations correctly and often detects sentiments exactly

# ACCEPTED MANUSCRIPT

14

ID: 20748)

split atext into sentences, the

Atcode):commit, the devel-

those sentimental words and

(CommentID: 9485)

SentiStrength'sdictionary of.

the sentimental words. Forexample,

toam in bad. When the

default congu-

onlyifword

are


---

<!-- Página 16 -->

### ACCEPTED MANUSCRIPT

308oppositeof what is expressed in the text. During our investigation, we nd substantial

309instanceswhereSentiStrengthis misled by complex structural variations of nega-

310tionspresent in the issue comments.

311For example, in the following two comments,SentiStrengthcannotdetect negation,

312whichare used before the word `Bad' (in rst comment) and `Good' (in second com-

313ment)correctly and thus misclassied sentiments of those comments.

314"I haven'tseenanybadbehavior.Iwasusingopensshto

315testthis.Iusedthe....withopensshtodisconnect;"

316(CommentID: 6688)

317"3.0.0hasbeenreleased;closing...Ididn'tchangethejute

318- don'tthinkthisisagoodidea;espasalsoeffectsthe........

319Andrewcouldyoutakealookatthisone?"(CommentID: 1725)

320In addition, we nd thatis unable to recognized shortened forms of

321negationssuch as, haven't", havent", hasn't", hasnt", shouldn't", shouldnt", and

322not"since these terms are not included in the dictionary.

323(D) Missing sentimental words in dictionary:Sincethe lexical approachSentiStrengthof6

324is largely dependent on its dictionary of lists of words (as discussed in Section 2.5.1),

325the tool often fails to detect sentiments in some texts when the sentimental words used

326in the texts are absent in the dictionary. For example, the words `Apology'

327the following two comments express negative sentiments,SentiStrengthbutcannot

328detectthem since those words are not included in its dictionary.

329"...Thisisindeednotanissue.Myapologies..."

330(CommentID: 20729)

331"Oops;issuecommenthadwrongticketnumberinit..."

332(CommentID: 36376)

333(D) Spelling errors mislead sentiment analysis:Misspelledwords are common in7

334informaltext, and the writer often deliberately misspells words to express intense senti-

335ments.For example, the misspelled word `Happpy' expresses more happiness than the

# ACCEPTED MANUSCRIPT

15

and `Oops' in


---

<!-- Página 17 -->

### ACCEPTED MANUSCRIPT

336correctlyspelled word `Happy'. AlthoughSentiStrengthcan detect some of such

337intensiedsentiments from such misspelled sentimental words, its ability is limited to

338onlythose intentional spelling errors where repetition of certain letters occur in a sen-

339timentalword. Mostother types (unintentional) of misspelling of sentimental words

340causeSentiStrengthfailto nd those words in its dictionary and consequently lead

341to incorrect computation ofsentiments. Forexample, theword `Unfortunately' was

342misspelledas `Unforunatly' in an issue comment (comment ID: 11978) and I'll" was

343writtenas `ill' in another (comment ID:SentiStrength927).'sdetection sentiments

344in both of these comments are found incorrect.

345(D) Repetitive characters considered sentimental:As described before,SentiStrength8

346detectshigher intensity of sentiments by considering deliberately misspelled sentimen-

347tal word with repetitive letters. Thetool also uses the same strategy for the same pur-

348poseby taking into account repetitive characters intentionally typed in words that are

349not necessarily sentimental by themselves. IfanybodyI amwritesgoooing to watch

350movie"insteadofI am going to watch, then the former sentence is considered

351positivelysentimental due to emphasis on the word `Going' by repetition of the letter

352`O' for three times.

353However,this strategy also misguidesSentiStrengthin dealing with some numeric

354values.For example, in the following comment,SentiStrengthincorrectlyidenties

355the number `20001113' as a positive sentimental word encountering repetition of the

356digits`0' and `1'.

357"See bug5694forthe...20001113/introduction.html ...Zip

358file withtestcase(javasourceandXMLdocs)1.Doyouusedeferred

359DOM? 2.CanyoutrytorunitagainstXerces2beta4(orthelatest

360code inCVS?)3.Canyouprovideasamplefile?Thankyou."

361(CommentID: 6447)

362(D) Incorrect detection of proper nouns:Anoun can rightly be considered9

363neutralin sentiment.SentiStrengthdetectsa word starting with a capital letter as

364a proper noun, when the word is located in the middle or end of a sentence. Unfortu-

# ACCEPTED MANUSCRIPT

16


---

<!-- Página 18 -->

### ACCEPTED MANUSCRIPT

365nately,grammar rules are often ignored in informal text and thus, sentimental words

366placedin the middle or end of asentence often end upstarting with a

367whichcauseSentiStrengthmistakenlydisregard the sentiments in those sentimental

368words.The following issue comment is an example of such a case, where the sentimen-

369tal word `Sorry' starting with a capital letter is placed in the middle of the sentence and

370SentiStrengtherroneouslyconsiders `Sorry' as a neutral proper noun.

371"Cool.Thanksforconsideringmybugreport!...Aboutthetitle

372of thebug;inthedescription;Iput:Sorryforthevagueticket

373title.Idon'twanttomakepresumptionsabouttheissue...work

374for passwords."(CommentID: 76385)

375However,the olderWindowsversionof SentiStrengthdoesnot have this shortcom-

376ing.

377(D) Sentimental words in interrogative sentences:Typically,negative sentimental10

378wordsin interrogative sentences (i.e., in questions) either do not express any sentiment

379or at least weaken the intensity of sentiment [22]. However, we have found instances

380whereSentiStrengthfailstocorrectly interpret thesentimental polarities of

381interrogativesentences. Forexample,SentiStrengthincorrectlyidenties negative

382sentimentinthecomment below, although themerely includes a

383expressingno negative sentiment as indicated by the human raters.

384"... DidIsubmitsomethingwrongorduplicate?..."

385(CommentID: 24246)

386(D) Diculty in dealing with irony and sarcasm:Automaticinterpretation of11

387in text written in natural language is very challenging,SentiStrengthandalsooften

388failsto detect sentiments from texts, which express irony and sarcasm [22]. For exam-

389ple,due to the presence of the positive sentimental words Dear God!" in the comment

390below,SentiStrengthdetectspositive sentiment in the sentence, although the com-

391mentposter used it in a sarcastic manner and expressed negative sentiment only.

392"The otherprecedencesareOK;asfarasIcantell...`zzz';

393Dear God!Youmeantheintenthereis...gottaconfessIjust

# ACCEPTED MANUSCRIPT

17

capital letter,

question

such


---

<!-- Página 19 -->

### ACCEPTED MANUSCRIPT

394saw thepatternandjumpedtoconclusions;hadn'texaminedthecode

395at all.Butyou'vejustmadethejobtougher...?"

396(CommentID: 61559)

397(D) Hard to detect subtle expression of sentiments:Textwritten in natural lan-12

398guagecanexpress sentiments without using any inherently sentimental words. The

399lexicalapproach offailsto identify sentiments in such a text due to

400its high dependency on the dictionary of lists of words, and not being able to properly

401capturesentence structure and semantic meanings. Consider the following issue com-

402ment,which was labeled with negative sentiment by three human raters although there

403is no sentimental words in it. Without surprise,incorrectlyinterprets

404it as a sentimentally neutral text.

405"Brian;Iunderstandwhatyousayandspecification about

406`serialization'inXSLTnot`indenting'.AsIsaiedbefore;

407indentingisjustthethingthatweeasilyseethestructureand

408data ofXMLdocument.Xalanoutputisnoteasytoseethat.The

409last;Ithinktheexampleofnon-whitespace charactersisno

410relationshiptoindenting.non-whitespacecharactersmustnotbe

411stripped;butwhitespacecharacterscouldbestripped.Regards;

412TetsuyaYoshida."(CommentID: 10134)

4133. LeveragingAutomated Sentiment Analysis

414Weaddress thechallenges identied from ourexploratory study as

415Section2.5.2 and develop a tool particularly crafted for application in the software en-

416gineeringdomain. Wecall ourSentiStrength-SEtool, which is built on top of the

417originalSentiStrength. We now describe how we mitigate the identied diculties

418in developingSentiStrength-SEforimproved sentiment analysis in textual artifacts

419in software engineering.

4203.1.Creatinga New Domain Dictionary for Software Engineering

421As reported inTable 3,ourexploratory study (Section 2.5.2) found the domain-

422specicchallenges (dicultiesD, D, D) as the most impeding factors against sen-136

# ACCEPTED MANUSCRIPT

18

described in


---

<!-- Página 20 -->

### ACCEPTED MANUSCRIPT

FigureSentiStrength-SE

423timentanalysis in software engineering text. Hence, the accuracy of sentiment

424can be improved by adopting a domain-specic dictionary [35, 36, 37]. We, therefore,

425rstcreate a domain dictionary for software engineering text to address the issues with

426domaindiculty.

427Figure1 depicts the steps/actions taken to develop the domain dictionary for soft-

428wareengineering text. Wecollect alarge dataset used inthe work of

429bran[9]. This dataset consists of 490 thousand commit messages drawn from 50 open-

430sourceprojects from GitHub. UsingStanfordtheNLPtool[38], we extract a set of

431lemmatizedforms of all the words in the commit messages, which is

432Toidentify the emotional words from the,setexploitSentiStrength'sw

433istingdictionary. We chooseSentiStrength'sexisting dictionary as the basis for our

434newone, because, in a recent studySentiStrength[39],'sdictionary building method

435is found superior to other approachesAFINN[40],(MPQA[41],andVADER[42])

436creationof software engineering domain-specic dictionaries. We identify those words

437in SentiStrength'soriginal dictionary, which have wild-card forms (i.e., words that

438havesymbol * as sux) and transform them to their corresponding lemmatized forms

439usingthe AFINN [40] dictionary. For example, the entry `Amaz*' in

440dictionaryistransformed tothewords `Amaze', `Amazed', `Amazes' and `Amazing'

441as those are found as emotional wordsAFINNin thedictionarycorresponding to that

442particularentry. Theare mainly two reasons forAFINNusingdictionary:the

443dictionaryis very similarSentiStrengthto theas both use the same nu-

444meric scale to express sentimental polarities of words,AFINN dictionarythe

# ACCEPTED MANUSCRIPT

19

Islam and Zi-

M denoted.asw

ex-

for the

(i)the

is also


---

<!-- Página 21 -->

### ACCEPTED MANUSCRIPT

Table Disagreementsbetween Human Raters

SentimentalPolarity A,B B,C C,A

Positive17.32%11.81%19.68%

Negative09.41%08.62%10.19%

Neutral15.69%18.13%11.81%

445widelyused in many other studies [43, 44, 45, 39]. Ifany wild-card form word is not

446foundin AFINN dictionary, we use our own wisdom to convert that word to its lem-

447matizedforms. Thus, by converting all short forms words to fulland combining

448thosewith remaining wordsSentiStrengthindictionarywe obtain aset of

449S. Then, we distinguish a setof words such thatC=Mã S. The setCendswwwwww

450up containing 716 words, which represent an initial sentimental vocabulary pertinent

451to the software engineering domain.

452Werecognize that some of these 716 words are simply software engineering domain-

453specictechnical terms expressing no sentiments in software engineering context, which

454otherwisewould express emotions when interpreted in a non-technical area such as so-

455cialnetworking. Therealso remain other words`Decrease'such as,`Eliminate'and

456`Insucient', which are unlikely to carry sentiments in the software engineering do-

457main.We,therefore, engage three human raters (enumerated as A, B, C) to indepen-

458dentlyidentify these non-sentimental domain words. Eachin ofthree humanw

459ratersare computer science graduate students having at least three years of software de-

460velopmentexperience. Ahuman rater annotates a word as neutral if the word appears

461to him/her as highly unlikely to express any sentiment when interpreted in the software

462engineeringdomain.

463In Table 4, we present sentiment-wise percentage of cases where the human raters

464disagreepair-wise. Wealso measure the degree of inter-rater agreement in terms of

465Fleiss-[46]value. The obtainedvalue0.739 signies substantial agreement

466amongthe independent raters.

467Weconsider a word as a neutral domain word when two of the three raters identify

# ACCEPTED MANUSCRIPT

20


---

<!-- Página 22 -->

### ACCEPTED MANUSCRIPT

468the word as neutral. Thus, 216 words are identied as neutral domain words, which we

469excludefrom the setresultingin anotherD setof the remaining 500 words. Suchww

470neutralizationof words for a particular domain is also suggested in several studies [5,

4716, 8, 9] in the literature.

472Next,we adjust the wordsDinby reverting them to their wild-card forms (if avail-w

473able)to comply withSentiStrength'soriginal dictionary. This

474calledas preliminary domain dictionaryP), which(has 167 positively and 310 neg-w

475ativelypolarized words. Thispreliminary dictionary is further enhanced according to

476the description below to createSentiStrength-SEthedictionary

4773.1.1.FurtherEnhancements to the Preliminary Domain Dictionary

478Wefurther extend the newly developed preliminary dictionary in the light of our

479observationsduring the exploratory study described in Section 2.

480Extensionwith new sentimental words and negations:During

481we nd several informal sentimental words such as, `Woops', `Uhh', `Oops' and `zzz',

482whichare not included in the original dictionary. The

483missingfrom the dictionary. We have added to the dictionary

484all these missing words as sentimental terms with appropriate

485whichmitigate the dicultyD.6

486In addition, we also add to the dictionary the missing shortened from of negation

487wordsas mentioned in the discussion of dicultyDin Section 2.5.2.5

488Discardingthe letter `X' from dictionary:Weexclude the

489dictionaryofto save lexical sentiment analysis from the diculty

490Das described in Section 2.5.2.3

4913.2.Inclusionof Heuristics in Computation of Sentiments

492Whilethe creation of the new domain dictionary is a vital step towards automated

493sentimentanalysis in software engineering text, we realize that the computations for

494sentimentdetection also need improvements.Thus, in the implementation of our domain-

495specicSentiStrength-SE, we incorporate a number of heuristics in the computa-

496tion,which we describe below.

# ACCEPTED MANUSCRIPT

21

new set of words is

F( ).w

our exploratory study,

formal word `Apology' is also

SentiStrength-SEof our

`X' from our domain

polarities,


---

<!-- Página 23 -->

### ACCEPTED MANUSCRIPT

4973.2.1.Additionof Contextual Sense to Minimize Ambiguity

498Recallthat,inthecreation ofourinitial domain dictionary, we

499wordson the basis of the judgements from three independent human raters. However,

500the neutralization of words is not always appropriate. For example, in the software en-

501gineeringdomain, the word `Fault' typically indicates a program error and expresses

502neutralsentiment. However, the same word can also convey negative sentiment as found

503in the following comment.

504"As WING...Myfault:Icannotreproduce

505I mightaddthatone;too"theword`Fault'

506of thecommentposter."(CommentID: 4694)

507Again,the word `Like' expresses positive sentiment if it

508like", He likes", andThey. Inthe most other cases the word `Like' is used as

509prepositionor subordinatingconjunctionand the word can safely be considered senti-

510mentallyneutral. Forexample, the following comment used the word `Like' without

511expressingany sentiment.

512"Lookslikeauserissuetome..."(Comment

513Wecan observe from the above examples that some of the 216 neutralized words

514can actually express sentiments when those are preceded

515personor agroup of persons, e.g., `I', `We', `My', `He', `She', `You' and possessive

516pronounssuch as `My' and `Your'. Thiscontextual information is taken into account

517in SentiStrength-SEto appropriately deal with the contextual use of those words

518in software engineering eld tominimize the

519listofsuch words isgiven inthe

520iedTermsLookupTable',which are also vetted by the

521terminethe Part-Of-Speech (POS) of words in sentences, we apply the Stanford POS

522tagger[38].

5233.2.2.BringingNeutralizers in Eect

524Our observations from the exploratory study (as presented in Section 2) reveal that

525sentimentof a word can be neutralized if that word is preceded by any of the neutralizer

526wordssuch as, `Would', `Could', `Should', and `Might'. For

# ACCEPTED MANUSCRIPT

22

neutralized 216

afterholidays...

expressesnegativesentiment

like"is usedWe as

ID: 40844)

pronounsbyreferringtoa

dicultiesDand D. Thecomplete12

dictionarylenamed `Mod-

three raters. Notethat to

example in the sentence

de-


---

<!-- Página 24 -->

527It would be good if the test could be completed

528`Good'does not express any sentiment as neutralized by the preceding word `Would'.

529Weaddamethod in

530neutralizerwords in sentences to be more accurate in sentiments detection. This

531in minimizing the diculty

5323.2.3.Integration of a Preprocessing Phase

533Tominimize the diculties

534includea preprocessing phase

535putationfor any given input

536to lter out numeric characters and certain copy-pasted contents such as code snippets,

537URLsand stack traces. To locate code snippets, URL's and

538regularexpressions similar to the approach proposed by Bettenburg et al. [47]. In

539dition,a spellchecker [48] is also included to deal with

540and rectifying misspelled English words. Spell

541lar expression based method in approximate identication of identier names in code

542snippets.

543Tomitigate the diculty

544the letters of a comment to small letters. However, converting all the

545letterscan also cause failure of the detection of the proper nouns such as the names of

546developersand systems, which is also important as discussed in the description of di-

547cultyDin Section 2.5.2. From our exploratory study, we have observed that the devel-9

548operstypically mention their colleagues' names in comments immediately after some

549sort of salutation words such as `Dear', `Hi', `Hello', `Hellow' or after the character `@'.

550Hence,in addition to converting all letters to lower case, the preprocessing phase also

551discardsthose words, which are placed immediately after any of

552or the character `@'. In addition,

553the user to instruct the tool to consider any particular words as neutral in sentiment, in

554casean inherently sentimental word must be recognized as proper noun, for example,

555to deal with the situation where a sentimental word is used as a system's name.

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

 the positive sentimental word

SentiStrength-SEto enable itcorrectly detect uses

Ddescribedbefore.2

D, D, D, andD(as described in Section 2.5.2), we4789

SentiStrength-SEtoas its integral part. Before com-

SentiStrength-SEtext,appliesthis preprocessing phase

traces in text, we use

Dthein identifyingdiculty7

checking also complements our regu-

Din particular, the preprocessing phase also converts all9

SentiStrength-SEmaintainsthe exibility to allow

23

ofsuch

salutation words

helps

ad-

to


---

<!-- Página 25 -->

### ACCEPTED MANUSCRIPT

Figure

5563.2.4.Parameter Conguration for Better Handling of Negations

557Wecarefully set a number of conguration parameters as defaults

558toolas shown in Figure 2. This default conguration

559ent from that of the originalSentiStrength. Particularly, to

560Din dealing with negations, the5

561blackrectangle in Figure 2 is setSentiStrength-SE

562detectingnegations over a larger range of proximity allowing zero to ve intervening

563wordsbetween a negation and a sentimental word, as was also suggested in a previous

564study[36].

5654. EmpiricalEvaluation of

566Whilemaking the design and tuning decisions to

567remaincareful about thepossibility that

568improvementin one area might have side-eects causing performance degradation in

569anothercriteria. We empirically evaluate our domain-specic techniques and the accu-

570racyof domain-specicSentiStrength-SE

571questions.

# ACCEPTED MANUSCRIPT

negation's conguration parameter marked with a

to ve in

in several phases around seven research

24

SentiStrength-SE

SentiStrength-SEto our

SentiStrength-SEofis dier-

mitigate the diculty

, which enables the tool

SentiStrength-SEdevelop, we

theapplication ofaparticular heuristic for


---

<!-- Página 26 -->

### ACCEPTED MANUSCRIPT

572Dataset:For empirical evaluation of

573commentsin Group-2 and Group-3 of the Gold Standard" dataset introduced in Sec-

574tion2.1. Theground-truthabout

575are determined based on the manual evaluations by human raters as described in Sec-

576tion2.3. Before conducting evalution, we present textual characteristics of Group-2 and

577Group-3datasets in Table 5, which indicates no substantial dierences in the charac-

578teristicsof the two datasets.

Table NumberComplexity

ofFactor Datasets Distinct(Lexical

WordsDensity)

Group-25,29521.00%

Group-35,52724.30%

579Metrics:The accuracy of sentiment analysis is measured in

580and F-scorecomputedfor each of the three sentimental polarities (i.e., positivity, neg-

581ativityand neutrality). Given

582F-score.¾/fora particular sentimental polarity

¨Ý SãSÝee}=; ¨Ý SÝe

583whereSrepresentsthe set of texts having sentimentale

584set of texts that are detected (by tool) to have the sentimental

585StatisticalTest ofSignicance:

586verifythe statistical signicance in the dierence of the results obtained by two tools,

587say Tand T. Asthe non-parametric test does not require normal distribution of data,ab

588this test suits well for our purpose. WeMcNemar's

589tablederived from the results obtained from

590contingencytable is shown in Table 6.

# ACCEPTED MANUSCRIPT

SentiStrength-SEour, we use the 5,600 issue

the sentimental polarities of those issue comments

Average Number Sentenceof of LengthSentences Sentences (in words)per Comment

5,6718.233.54

4,0008.261.00

precisionterms ofrecall,

Sofa textual contents,precision.}/, recall.R/, and

is calculated as follows:

¨Ý SãSÝ2 }ReeR=;¾ = Ý SÝ}+Re

¨e, andpolaritySdenotesthee e.polarity

Weapply non-parametricMcNemar'stest[49] to

perform ateston2  2contingency

TandtoolsT. Thestructure of such aab

25


---

<!-- Página 27 -->

### ACCEPTED MANUSCRIPT

Table2contingencyT andTab # of comments misclassied# of nn0001 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly nn1011 by Tbut not byTclassiedby bothTand Tabab

591Let,Fand Fdenotethesets ofmisclassied commentsTandbyTrespec-abab

592tively.In the contingency table (Tablenrepresents6),the number of issue comments00

593misclassiedby bothTand T(i.e.,n=ðFãFð),nrepresentsthe number ofab00ab01

594commentsmisclassied byTbut not byT(i.e.,n=ðF*Fð),nrepresentstheba01ba10

595numberof comments misclassiedTbybut not byT(i.e.,n=ðF*Fð), andnab01ab11

596representsthe number of comments correctly classied by both theS de-

597notethe set of all the issue comments correctly classied according to the ground-truth.

598Thus,n=S* . FäF/. Thesuperiority ofTtooloverthe toolTis observed, if11abba

599n> n. Otherwise,Tis considered superiornif> n. Such observed superior-1001a0110

600ity is considered statistically signicant,p-valueif thefrom atest

601is less than a pre-specied signicance. Inlevelour work, weset= 0 :001 , which a

602reasonablesetup widely used in the literature.

6034.1.Head-to-headComparison Using a Benchmark Dataset

604Wecompare our software engineering domain-specicSentiStrength-SEwith

605the originalSentiStrength[22]tool and two other toolkitsNLTK[23]andStanford

606NLP [24].To the best of our knowledge, these aredomainthe onlytools/-

607toolkitsattempted in the past for sentiment analysis in software engineering text [5, 17,

60827, 50]. In particular, we address the following research question:

609 RQ1:Doesour domain-specicSentiStrength-SEoutperformthe existing domain 610 independenttools for sentiment analysis in software engineering text? 611

612Wewrite a Python script to importNLTKsentimentanalysis package [51, 23] and

613run it on texts to determine the sentimental polaritiesNLTKof those.the

# ACCEPTED MANUSCRIPT

26

Let,


---

<!-- Página 28 -->

### ACCEPTED MANUSCRIPT

614probabilityof positivity, negativity and neutrality of a text. In

615videsa compound valueC, which ranges between -1 to +1. Av

616sentimentsif>0 , a text will have negativev

617is considered sentimentally neutral

618anotherstudy [51] to determine sentiments of texts

619Wedevelop a Java program using the JAR of

620on texts to determine their sentimental polarities.

621sentimentscoreSbetweenzero to four wherev

6223 fSf4 indicatespositive sentimentv

623text[52].

624Weseparately operate each of the selected tools

625the Group-2 and Group-3 portions of the Gold Standard" dataset. Recall that

626and Group-3 datasets contain 1,600 and 4,000 issue comments respectively.

627the three sentimental polarities (i.e., positivity, negativity, and neutrality), we compare

628the tools' outcome with the ground-truth and separately compute precision, recall, and

629F-scorefor all the tools with respect to each dataset. Table 7 presents

630recallR( ), andF-score¾ )ofall the tools in

631neutralsentiments, and also the average over all these three sentimental polarities. The

632highestmetric values are highlighted in bold.

633Noticethat for the Group-2 dataset,

634the highest precision, recall and F-scored compared to the rest other tools.

635For the Group-3 dataset,SentiStrength-SE

636scorein detecting negative sentiments and it achieves the highest recall and F-score in

637the detection of neutral sentiments. In those few cases, where

638not achieve the best results, it remains at the second best or marginally close to the best.

639In thedetection ofpositive sentiments in

640the highest precision and recall, where

641results.Similarly,theoriginalSentiStrength

642tectionof negative sentiments in Group-3 dataset, and

643obtainsthesecond best result. The

644inalSentiStrength) forneutral sentiments is

# ACCEPTED MANUSCRIPT

addition, its also pro-

text contains positive

C<0 .ifOtherwise, a textv

Cwhen0 . Similar procedure is also followed inv

NLTK.using

StanfordtheNLPtoolto apply it

StanfordFor aNLPtextprovidesa

0 fSf1 indicatesnegative sentiment,v

Sand= 2neutralof thev

SentiStrength-SEand ouron

For each of

}),the precision (

the detection ofpositive, negative and

SentiStrength-SEourconsistentlyachieves

achievesthe highest precision and F-

does

Group-3Satnforddataset,NLPachieves

SentiStrength-SEouryieldsthe second best

achivesthe highest recall inthe de-

SentiStrength-SEagain our

highest precision (91.28% achieved by theorig-

only0.64%higherthanthatofour

27


---

<!-- Página 29 -->

Met.

Data

Group-2

Group-3

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

Table

Senti- mentsStrength-SE

}

PositiveR

¾

}

NegativeR

¾

}

NeutralR

¾

}

PositiveR

¾

}

NegativeR

¾

}

NeutralR

¾

}Overall

averageR

accuracy¾

88.86%

98.81%

93.57%

53.42%

97.66%

69.06%

98.14%

83.00%

89.94%

41.80%

82.04%

55.39%

68.61%

71.00%

69.78%

90.64%

80.05%

85.02%

73.58%

85.43%

79.06%

Strength

74.48%

84.93%

28.22%

43.78%

96.83%

52.42%

68.01%

31.69%

87.79%

46.58%

47.61%

78.40%

59.25%

91.28%

56.16%

69.54%

61.69%

78.54%

62.02%

28

NLTKStanford NLP

69.47%79.77%

81.55%71.67%

75.0%75.50%

40.46%13.28%

54.69%88.28%

46.51%23.08%

69.53%63.70%

50.86%25.57%

58.75%36.49%

20.32%69.47%

86.33%81.55%

32.89%75.03%

50.65%40.46%

70.24%54.69%

58.86%46.51%

91.17%69.53%

45.78%50.86%

60.96%58.74%

56.93%56.04%

64.91%62.10%

55.50%52.56%


---

<!-- Página 30 -->

### ACCEPTED MANUSCRIPT

645SentiStrength-SE.

646Thus,if we consider the overall average accuracy, as presented at the bottom of the

647table,it becomes evident thatSentiStrength-SEourperformsthe best, followed by

648the originalSentiStrengthand NLTK. Notice that the overall precision, recall and F-

649scoreof ourSentiStrength-SEare substantially higher than those of the second-best

650performingtool (i.e., the originalSentiStrength).

TableSentiStrengthand

SentiStrength-SE # of comments misclassied# of 748 365 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly 1,5272,924 by Tbut not byTclassiedby bothTand Tabab

Here,T= originalSentiStrengthand T=SentiStrength-SEab

651Toverify whether the observed performance dierenceSentiStrength-SEbetween

652and the originalSentiStrengthis statistically signicant, we performMcNemar'sa

653testbetween the results of these two tools. For both datasets Group-2 and Group-3, we

654computen, n, nand naccordingto their specications described in Table 6.00011011

655In Table 8, we present the contingency matrix computedMcNemar'sfor thetest.We

656observesuperiorityT of(SentiStrength-SE) in the contingency tablenasn.b1001

*16 657Accordingto thep -value( = 2:2  10; p < obtained from the test, the observed

658dierencein the superior performanceSentiStrength-SEofis statistically signi-

659cant.Based on these observations and statistical test, we now derive the answer to the

660researchquestion RQ1 as follows:

661 Ans.to RQ1:In the detection of sentiments in software engineering text, our domain-

specicSentiStrength-SEsignicantlyoutperforms the domain independentNLTK,662

StanfordNLP, and the originalSentiStrength.

# ACCEPTED MANUSCRIPT

29


---

<!-- Página 31 -->

### ACCEPTED MANUSCRIPT

6634.2.Comparisonwith respect to Human Raters' Disagreements

664Recallthat the issue comments in the Gold Standard" dataset are annotated with

665sentimentsas identied by independent human raters. There are disagreements among

666humanraters in the identication of sentiments in some issue comments. While humans

667disagreeabout sentiments in some issue comments, it is likely that the automated tools

668willalso produce dierent outcomes resulting in varied precision and recall.

669We,therefore, investigate to what extend the agreements and disagreements of anno-

670tationsamong human raters cause deviation of results of the head-to-head comparison

671of tools as described in the previous section. Particularly, we want to verify whether our

672domain-specicSentiStrength-SEstilloutperforms the other domain-independent

673toolswhen the rater' agreements and disagreements are taken into account. Here,

674addressthe following research question:

675 RQ2:Doestheaccuracy of

676mainindependent counterparts when the agreements and disagreements

ratersare taken into account? 677

678For this investigation, we use the Group-2 dataset where each issue comment was

679independentlyannotated by three human raters. We distinguish two sets of issue com-

680mentsfrom this Group-2 dataset.

681i) Set-A: containing those issue comments for which all the three human raters agreed

682on thesentiments expressed inthose

683comments.

684ii)Set-B: consisting of those issue comments for which two of the three raters agreed

685on the sentiments expressed in those comments. This set contains 357 issue com-

686ments.

687Weformulate the following null and alternative hypotheses to determine the statis-

688ticalsignicance of improved performances of the best tool. 1 689NullHypothesis-1H(): Thereisnosignicant dierence ino

690SentiStrength-SEcomparedtotheother tools in

# ACCEPTED MANUSCRIPT

30

largely

comments. This

vary

sentiment detection in

compared toits

among human

setcontains 1,210 issue

theperformance of

do-

theissue

we


---

<!-- Página 32 -->

### ACCEPTED MANUSCRIPT

691commentsin Set-A. 1 692AlternativeHypothesis-1H():Thereexist signicant dierences in the performancea

693of SentiStrength-SEcomparedto the other tools in sentiment detection in the issue

694commentsin Set-A. 2 695NullHypothesis-2H(): Thereisnosignicant dierence ino

696SentiStrength-SEcomparedtotheother tools in

697commentsin Set-B. 2 698AlternativeHypothesis-2H():Thereexist signicant dierences in the performancea

699of SentiStrength-SEcomparedto the other tools in sentiment detection in the issue

700commentsin Set-B.

701Wenow examine whether these hypotheses hold true with respect to the four tools

702we compare. Inthe similar way as of the head-to-head comparison described in the

703previoussection, we separately run all the four tools

704on Set-Aand Set-Bissuecomments. Foreach of the three sentimental polarities (i.e.,

705positivity,negativity, and neutrality), we compute

706(¾ ) for each of the tools separately over the issue comments

707For the issue comments in bothandSet-B

708icantlyimproved performances compared to other tools. For testing our hypotheses, in

709eachofSet-Aand Set-Bdatasets,we rst identify the two tools producing better results

710amongall the four tools. Then, we examine if there is any signicant dierence in the

711performancesof the best tool and the second best one. If

712encesbetweenthe accuracies of the top performing two tools, discovering such would

713sucefor demonstrating the existence of signicant dierence of the best performing

714toolagainst the other tools.

715Table9presents themetrics' values of

716negativeand neutral sentiments for each set of

717ble 9, for the issue commentsSet-Ain, SentiStrength-SE

718highestprecision, recall and F-score in the detection of positive, negative and neutral

719sentiments.Theoverall average accuracies indicate that

720achievesthe second best accuraciesSet-Ain the

721Now,we perform atestbetween the accuracies

# ACCEPTED MANUSCRIPT

31

, the best tool

all

theperformance of

sentiment detection in

SentiStrength-SEincluding our

}),precisionrecallR),( (F-score

Set-Aandin Set-Bboth.

mustexhibitthe signif-

there exist signicant dier-

thetools inthedetection of

theissue comments. As

consistentlyachieves the

SentiStrengththe original

SentiStrength-SEof

theissue

positive,

seen inTa-


---

<!-- Página 33 -->

Met.

Data

Set-A

Set-B

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

Table

Senti- mentsStrength-SE

}90.15%

PositiveR95.33%

¾92.67%

}53.66%

NegativeR100.00%

¾69.84%

}99.44%

NeutralR91.15%

¾95.12%

Overall}81.08%

averageR95.49%

¾85.88%accuracy

}72.48%

PositiveR96.89%

¾82.92%

}51.75%

NegativeR96.72%

¾67.42%

}83.92%

NeutralR40.87%

¾54.97%

Overall}69.38%

averageR78.16%

accuracy¾68.44%

Set-AandSet-Bissue

NLTKStanford StrengthNLP

70.46%67.9%83.39%

91.20%61.58%76.66%

79.50%64.17%79.89%

28.17%49.45%9.66%

54.55%86.36%

43.96%51.87%17.38%

99.43%77.00%67.61%

58.84%54.08%28.40%

73.93%63.53%40.00%

66.02%64.78%53.55%

83.35%56.74%63.81%

65.79%59.86%45.76%

63.64%67.32%64.91%

97.92%70.46%57.13%

77.14%68.86%60.98%

21.63%50.74%20.83%

60.65%55.73%90.16%

31.89%53.12%33.85%

86.21%38.24%38.88%

21.74%33.91%12.17%

34.72%35.94%18.54%

57.16%52.10%41.54%

60.10%53.37%53.15%

58.59%52.72%37.79%

32


---

<!-- Página 34 -->

### ACCEPTED MANUSCRIPT

TableSentiStrength-SEand

originalSentiStrengthin Set-Adataset # of comments misclassied# of 84 22 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly 511593 by Tbut not byTclassiedby bothTand Tabab

Here,T= originalSentiStrengthand T=SentiStrength-SEab

722and the originalSentiStrengthforthe issue commentsSet-Aindataset.The contin-

723gencytable for the test is presented in Table 10. Accordingto the contingency table,

724SentiStrength-SE(T) performs betternas > n. Theperformance dierenceb1001

*16 725is found tobestatistically signicantp= 2 with2  10and p <. Thus,the 1 726McNemar'stestrejects our rst null hypothesisH). Therefore,(the rst alternative 0 1 727hypothesisH() holds true.a

728Again,asseen in Table 9, for the issue commentsSet-B, SentiStrength-SEin

729achievesthehighest F-score indetecting sentiments ofallthethree polarities. The

730precisionand recallSentiStrength-SEofis also the highest in all cases except for

731onlytwo. TherecallSentiStrength-SEofforpositive sentiments is 96.89%, which

732is the second best and only 1.03% lower than the highest. Similarly, the precision of

733our SentiStrength-SEin detecting neutral sentiments is 83.92%, which is also next

734to the best and only 2.29% lower than the best. Also,with respect to the overall aver-

735ageaccuracies,SentiStrengthcan be considered to have achieved the second best

736performancefor theSet-Bdataset.

TableSentiStrength-SEand

originalSentiStrengthin Set-Bdataset # of comments misclassied# of 97 20 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly 135105 by Tbut not byTclassiedby bothTand Tabab

Here,T= originalSentiStrengthand T=SentiStrength-SEab

# ACCEPTED MANUSCRIPT

33


---

<!-- Página 35 -->

### ACCEPTED MANUSCRIPT

737Similarto theSet-Adataset,for Set-B, we carry outMcNemar'satestbetween

738the accuracies ofand the originalSentiStrengthto determine

739whetheror not there is any statistical signicant dierences between the performances

740of these two tools. Thecontingency matrix for the test is presented in Table 11. Ac-

741cordingto the contingency matrix,SentiStrength-SE(T) outperforms the originalb

742SentiStrength(T) withn> n. TheMcNemar'stestwith the contingency ma-a1001

*16 743trix ofTable 11obtainsp= 2:2 10and thusp <. Thus,oursecond null 22 744hypothesis() isrejected andthesecondalternativeH) holds (a0

745whichindicates that the superior performanceSentiStrength-SEofoverthe original

746SentiStrengthis statistically signicant for the issue commentsSet-Bdataset.in the

747Thus,for both theand Set-Bdatasets,SentiStrength-SEsignicantlyout-

748performsthenext best performerSentiStrength. Basedonourobservations and

749resultsfrom the statistical tests overSet-Abothandthedatasets,we now derive

750the answer to the research question RQ2 as follows:

751 Ans.to RQ2:Whenthe agreements and disagreements among human raters are taken

intoaccount, our domain-specicSentiStrength-SEstillmaintains signicantly su- 752 perior(compared to its domain independent counterparts) accuracies in detecting sen-

timentsin software engineering text.

7534.3.Evaluatingthe Contribution of Domain Dictionary

754The newly developed software engineering domain dictionary is amajor compo-

755nentofSentiStrength-SE. Here, we carry out a quantitative evaluation to verify the

756contributionof the domain dictionary in detecting sentiments in software engineering

757textsaccurately. Especially, we address the following research question:

758 RQ3:Doesthe domain-specic dictionarySentiStrength-SEinreallycontribute 759 to improved sentiment analysis in software engineering text? 760

761For this particular evaluation, we again use the Group-2 and Group-3 datasets in-

762troducedbefore. Weinvoke the originalSentiStrengthfordetecting sentiments in

763issuecomments inthese datasets. Then,we SentiStrengthoperatemakingituse

# ACCEPTED MANUSCRIPT

34


---

<!-- Página 36 -->

### ACCEPTED MANUSCRIPT

764our newly developed domain dictionary andinvoke itfor sentiment detection in

765sameissue comments. We useSentiStrength* to refer to the variant of the original

766SentiStrengththat is forced to use our domain dictionary instead of its original one.

767For each of the three sentimental polarities, we separately compute and compare the

768precision,recall, and F-score resulting from the tools in each dataset.

7694.3.1.Comparisonbetween the originalSentiStrengthand

770If our domain dictionary actually contributes to improved sentiment analysis in soft-

771wareengineering text,SentiStrength* must perform better than the original

772In Table 12, we present the precision}), recall(R),( and F-score¾ )(

773tionof each sentimental polarity. In the table, substantial (i.e., more that 1%) dierences

774are marked in bold.

775As seen in Table 12, in everySentiStrengthcase,* achieves higher F-score than

776the originalSentiStrength. Moreover,* showsmuchhigher preci-

777sionin all cases except for neutral comments in Group-3 dataset. For

778mentsin Group-3 dataset, the precision of theSentiStrengthoriginalis marginally

779higherby only 0.06%. In all the cases across datasets the precision, recall, and F-score

780of SentiStrength* is higher or comparable to those of the original

781Onlyintwoofthe18cases (i.e., therecall for positive and

782Group-3dataset), theoriginalSentiStrength'sperformance is perceived (substan-

783tially)betterSentiStrengththan*. These observations are also reected

784averageaccuraciespresentedin the bottom three rows of the table.overall

785ageaccuraciesindicatesuperior performanceSentiStrengthof* over the original

786SentiStrength. Hence,the observed accuracy of* is substantially

787higherwhen it is forced to use our new domain dictionary instead of its original one.

788Todetermine the statistical signicance of our observations, we perform another

789mar'stestbetween the resultsSentiStrengthof* and the original

790As such, we formulate our null and alternative hypotheses as follows: 3 791NullHypothesis-3H(): Thereis nosignicantdierencebetween the accuracies of 0

792the originalSentiStrengthand*. 3 793AlternativeHypothesis-3H (): Thereexistsignicantdierencesbetween the accu-a

# ACCEPTED MANUSCRIPT

35

*

in detec-

the

.

negative sentiments in

overallin the

Theaver-

.

.

the

com-


---

<!-- Página 37 -->

Group-2

Group-3

# ACCEPTED MANUSCRIPT

Table

Data Sentiment

Positive

Negative

Neutral

Positive

Negative

Neutral

Overall

average

accuracy

Here,SentiStrength*

### ACCEPTED MANUSCRIPT

SentiStrength

Met.SentiStrength

}74.48%87.56%

R98.81%98.28%

¾84.93%

}28.22%

R97.66%97.65%

¾43.78%

}96.83%

R52.42%

¾68.01%

}31.69%

R87.79%

¾46.58%

}47.61%

R78.40%

¾59.25%

}91.28%91.22%

R56.16%

¾69.54%

}61.69%

R78.54%

¾62.02%

36

SentiStrength*

and SentiStrength*

92.61%

53.19%

68.87%

97.94%

81.85%

89.18%

40.44%

82.01%

54.16%

69.10%

72.65%

70.83%

79.54%

84.98%

73.24%

85.33%

76.77%


---

<!-- Página 38 -->

### ACCEPTED MANUSCRIPT

794raciesof the originalSentiStrengthand*.

TableMcNemar'stestSentiStrengthand* # of comments misclassied# of 748 334 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly 1,5272,955 by Tbut not byTclassiedby bothTand Tabab

Here,T= originalSentiStrengthand T=SentiStrength*ab

795The contingency matrix forMcNemar'sthetestis presented in Table 13. As seen in

796the contingency matrix,SentiStrength*(T) exhibits higher accuracies (comparedb

*16 797to the originalSentiStrength) asn> n. The test obtainsp = 2:2  10where1001

3 798p < . Thus, the test rejects our null hypothesisH). Hence(the alternative 0 3 799(H) holds true indicating that the dierence is statistically signicant. Based on thesea

800observationsand the statistical test, we conclude that our newly created domain dictio-

801nary indeed contributes to statistically signicant improvements in sentiment analysis.

802Hence,we answer the research question RQ3 as follows:

803 Ans.toRQ3:Our newly created domain dictionary makes statistically signicant

804contributionstothe improvement ofsentiment analysis insoftware engineering do-

main. 805

8064.4.OurDomain Dictionary vs.'sOptimized

807The originalSentiStrengthhas a feature that facilitates optimizing its dictionary

808fora particular domain [53]. Wewant to verify how ourdictionary perform

809in comparison withSentiStrength'sdictionary optimized for software engineering

810text.In particular, we address the following research question:

811 RQ4:CanSentiStrength'sdictionary optimized for software engineering text per- 812 formbetter thanSentiStrength-SE'sdomain-specicdictionary we created? 813

# ACCEPTED MANUSCRIPT

37


---

<!-- Página 39 -->

### ACCEPTED MANUSCRIPT

8144.4.1.OptimizingSentiStrength'sDictionary

815SentiStrength'soriginal dictionary can be optimized for a particular domain by

816feedingit with a set of annotated pieces of texts. ToSentiStrengthoptimize the's

817dictionaryfor software engineering domain, we use a dataset consists of Stack Over-

818owposts/comments related to software engineering. This Stack Overow posts (SOP)

819datasetcontains total 4,423 comments [54, 55]. Eachcomment in the SOP

820assignedappropriate sentimental polaritiespositive(i.e.,, negative, neutral) depending

821on which ones it expresses. Thus, 35% of posts are labeled with positive sentiment and

82227% are labeled with negative sentiment while 38% of the posts are

823in sentiment [54].

824Simpleannotations with sentimental polarity labels isSentiStrengthnot enough

825to be able to use the dataset for optimizing its dictionary.SentiStrengthFor this purpose,

826requiresapair ofinteger sentimentê%scores;  ëpre-assignedtoeach commentCcc

827where+1f%f+5and *5ff*1 . Theinterpretation of these score is similarcc

828to what is described in Section%and respectivelyrepresent the positive andcc

829negativesentimental scores pre-assigned to theCgivenAtexttextClabeledto

830havehave positive sentiment, must be assigned asentimental%>+1 .scorec

831A higher%indicatesaintensity/strength of the positive emotion. Similarly, ac

832textlabeled to have negative sentiment must be assigned asentimental score

833<*1 . Alowersigniesa higher intensity/strength of the negative emotion ex-cc

834pressedin textC . Atext labeled as neutral in sentiment, must be assigned sentimental

835scoresê1 ;*1 ë.

Table

SentimentsLabeled SentimentalScores CommentText byHuman Ratersê%;  ëcc

@DrabJay:excellent suggestion! Positiveê+3 ;*1 ë Codechanged. :-)

Thatreally stinks! Iwas afraid of that... Negativeê+1 ;*3 ë

A few but they all seem proprietary Neutralê+1 ;*1 ë

# ACCEPTED MANUSCRIPT

38

as neutral

is


---

<!-- Página 40 -->

### ACCEPTED MANUSCRIPT

836Accordingto the requirements described above, we derive the sentimental scores for

837eachof the comments in the SOP dataset. For a commenthavingpositive sentiment,

838we set% = +3. Similarly, weset= *3fora comment expressing negative sentiment.

839Insteadof using extreme values from the domains% andof, we choose the ones at

840the medians. In Table 14, we present examples demonstrating how we assign sentiment

841scorestothelabeled comments intheSOPdataset. Thisdataset isthenfed to

842originalSentiStrengthforoptimizing its dictionary for software engineering text.

843Thus,weproduce another variant oftheoriginal. Werefer tothis O 844variantwith the optimized dictionarySentiStrengthas.

O 8454.4.2.ComparisonbetweenSentiStrengthand*

OO 846SentiStrengthand* only dier in their dictionaries.

847usesthe optimized dictionary while* uses thewe created O 848forSentiStrength-SE. Thus, comparing betweenSentiStrengthand*

849impliesa comparison betweenSentiStrength'soptimized dictionarySentiStrength-SEand's

850softwareengineering domain dictionary we created. O 851WeinvokeSentiStrengthfordetecting sentiments in issue comments in Group-

8522 and Group-3 datasets and compute the values of precision), recallR(),( and F-score

853(¾ ) in detection of each sentimental polarity. Wepresent the computed metrics values O 854forSentiStrengthand* side by side in Table 15.

855In Table 15,weseethatSentiStrength* always achieves higher F-score than O 856SentiStrength. Moreover,* achievesmuchhigher precisionin

857all cases except for neutral comments in Group-3 dataset. For the O 858Group-3dataset, the precisionSentiStrengthof* lower than that of

859marginallyby only 0.49%. The recallSentiStrengthof* is also substantially higher O 860than or nearly equal to thatSentiStrengthofin 16 of 18 cases. Finally, the overall

861averageaccuracies, as presented at the bottom three rows of the table, indicate that the

862overallprecision, recall, and F-scoreSentiStrengthof* are substantially higher than O 863SentiStrength.

864Todetermine the statistical signicance of our observations, we perform another O 865McNemar'stestbetween the resultsSentiStrengthofand*. Thus,

# ACCEPTED MANUSCRIPT

39

the

in


---

<!-- Página 41 -->

Group-2

Group-3

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

OTableSentiStrengthand SentiStrength* OData SentimentMet.SentiStrengthSentiStrength*

}74.45%87.56%

PositiveR98.68%98.28%

¾84.87%92.61%

}30.12%53.19%

NegativeR97.66%97.65%

¾46.04%68.87%

}96.69%97.94%

NeutralR54.29%81.85%

¾69.53%89.18%

}26.00%40.44%

PositiveR86.90%82.01%

¾40.02%54.16%

}47.13%69.10%

NegativeR76.77%72.65%

¾58.40%70.83%

}91.71%91.22%

NeutralR58.02%79.54%

¾71.07%84.98%

Overall}61.02%73.24%

averageR78.72%85.33%

accuracy¾68.74%78.82%

OHere,SentiStrengthuses

SentiStrength*

40


---

<!-- Página 42 -->

### ACCEPTED MANUSCRIPT

OTableMcNemar'stestSentiStrengthand* # of comments misclassied# of 942 140 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly 1,0463,436 by Tbut not byTclassiedby bothTand Tabab

OHere,T=SentiStrengthand T=SentiStrength*ab

866we formulate our null and alternative hypotheses as follows: 4 867NullHypothesis-4H(): Thereis no signicant dierence between the accuracies of 0 O 868SentiStrengthand*. 4 869AlternativeHypothesis-4H (): Thereexist signicant dierences between the accu-a O 870raciesofSentiStrengthand*.

871The contingency matrix forMcNemar'sthetestis presented in Table 16. As seen in

872the contingency matrix,SentiStrength*(T) exhibits higher accuracies (comparedb

O*16 873to theSentiStrength) as n> n. Thetestobtainsp= 2:2 10where1001

44 874p <and rejects our null hypothesisH). (the alternativeH)(a0

875holdstrue indicating that the dierence is statistically signicant. The signicantly su-

876perioraccuraciesSentiStrengthof* implies that the domain dictionary we created

877forSentiStrength-SEoutperformsthe originalSentiStrength'soptimized dictio-

878nary.We, therefore, answer the research question RQ4 as follows:

879 Ans.toRQ4:The domain dictionary we createdSentiStrength-SEforperforms 880 signicantlybetter than the optimized dictionary ofSentiStrengththe original. 881

8824.5.Comparisonwith a Large Domain-independent Dictionary

883As mentioned before, domain diculty is among the major reasons why domain-

884independentsentiment analysis techniques are found to have performed poorly when

885operatedon in technical texts. This work of ours reveals the same as described in Sec-

886tion2.5.2. Forovercoming the domain diculties, wehave created domain-specic

887dictionaryand heuristics in our. However, compared to the exist-

# ACCEPTED MANUSCRIPT

41


---

<!-- Página 43 -->

### ACCEPTED MANUSCRIPT

888ing domain-independentdictionaries available out there, our domain-specic dictionary

889is small in size with 167 positively and 310 negatively polarized entries. One might ar-

890gue that a substantiallylargedomain-independentdictionary might not suer from the

891domaindiculties we are concerned about and may perform equally, if not better than

892our relatively small domain-specic dictionary. Toverify this possibility, we compare

893the performances of our domain-specic dictionary with a large domain-independent

894dictionary.Particularly, we address the following research question:

895 RQ5:Can a large domain-independent dictionary perform better than the domain- 896 specicdictionary we createdSentiStrength-SEfor? 897

8984.5.1.Choosinga Domain Independent Dictionary for Comparison

899Thereare several domain independent dictionariesAFINN(e.g.,[40],MPQA[41],

900VADER[42],SentiWordNet[56],SentiWords[57],and the dictionary of Warriner et

901al. [58]) available for sentiment analysis in general. Islamand Zibran [39] compared

902the performances of[40],MPQA[41]andVADER[42]dictionaries in sentiment

903analysisof software engineering text. However, all those used dictionaries in the work

904of Islam and Zibran [39] can be consideredlowto coverage.haveOnthe other hand,

905SentiWordNet[56],SentiWords[57],and theextendedANEW(AectiveNorms for

906EnglishWords) dictionary ofWarriner etal.[58] arelarger insize and

907coveragecompared toAFINN,MPQAandVADERdictionaries.

908Amongthese three high coverage large dictionaries, we opt forANEWthe extended

909dictionaryof Warriner et al. [58], which includes 13,915 English lemmas having 67%

910reportedcoverage [57]. We choose this dictionary for two main reasons: (i) this dictio-

911nary has already been used in software engineering studies [59, 60]; (ii) Use of parts-

912of-speech(POS) as context to determine words' polarities is found to show low accu-

913racyin detecting sentiments in software engineering texts [39]. Therefore, we exclude

914SentiWordsand SentiWordNetas these two dictionaries usePOSasacontext to

915determinewords' polarities.

# ACCEPTED MANUSCRIPT

42

have higher


---

<!-- Página 44 -->

### ACCEPTED MANUSCRIPT

Table

Scorein [+1,+9]+1 +2+3+4+5+6+7+8+9

Scorein [-5, +5]-5 -4-3-2+/-1 +2+3+4+5

9164.5.2.RangeConversion

917In the extendedANEWdictionaryof Warriner et al. [58], each!is assigned a

918valencescorev, which is a real number between+1 :0 and+9:0 signifyingthe senti-!

919mentalpolarity and strength/intensity of!theThewordsentimentalof the

920word!, denoted assentiment.! /, is interpreted according to Equation 5 below.

h P ositive;ifv>+5 :0n! n (5)sentiment.! / =Negative;ifv<+5 :0l! n Neutral;otherwise.n j 921In contrast, both the originalSentiStrengthand ourSentiStrength-SEuses

922integerrange [-5, +5] and a dierent interpretation for the same purpose. To

923extendedANEWdictionaryinSentiStrength, weconvert the valence score ofeach

924wordin the extendedANEWdictionaryfrom [+1.0, +9.0] range to [-5, +5] range. In

925doingthat, the fractional valuevisofrounded to its nearestvinteger. Then,!!

926usingthe conversion scale in Table 17, we convert each integervvalencein the score!

927range[+1, +9] toin the integer[-5, +5]. For example, if the original valence!

928scoreof a word rounded to the closest integer is +2, it is converted to -4, according to

929the mappings shown in Table 17. Such a conversion between ranges does not alter the

930originalvalence strength/intensity of the words [60]. Asimilar approach was adopted

931in a recent work [60] for range conversion of arousal scores.

W 9324.5.3.ComparisonbetweenSentiStrengthand*

933Wecreate another variant of the originalSentiStrengthby replacing its

934dictionarywith the one created based on theof Warriner et al., and call this WW 935newvariantSentiStrength.is invoked for detecting sentiments

936in issue comments in Group-2 and Group-3 datasets. Thenwe compute the precision W 937(}), recallR),( and F-score¾ )(SentiStrengthin detection of each sentimental

# ACCEPTED MANUSCRIPT

43

use this


---

<!-- Página 45 -->

### ACCEPTED MANUSCRIPT

W 938polarity.Thecomputed metrics valuesSentiStrengthforand*

939are presented side by side in Table 18.

940As seen in Table 18, in 16 of the 18 cases* achieves higher preci- W 941sion,recall, and F-score compared toSentiStrengththose of.*'s W 942recallsfor positive sentiments only are slightly lowerSentiStrengththan those of. W 943Noticethat,forthosesamecase,SentiStrengththe's precisionis substantially

944lowercompared toSentiStrength*. Inevery case,* maintains a

945nicebalance between precision and recall indetecting sentimental and neutral com-

946ments.Suchbalancing between precisions and recalls results inhigher F-scores for

947SentiStrength* inallcases.Theoverall accuracies, aspresented inthe

948threerows of the table indicates signicantly higher precision, recall, and F-score of W 949SentiStrength* compared to. Todetermine the statistical sig-

950nicanceoftheobserved dierences intheaccuracies, weperformtest W 951betweenthe resultsSentiStrengthofand*. Forthe statistical

952test,we formulate our null and alternative hypotheses as follows: 5 953NullHypothesis-5H(): Thereis no signicant dierence between the accuracies of 0 W 954SentiStrengthand*. 5 955AlternativeHypothesis-5H (): Thereexist signicant dierences between the accu-a W 956raciesofSentiStrengthand*.

957The contingency matrix forMcNemar'sthetestis presented in Table 19. As seen in

958the contingency matrix,SentiStrength*(T) exhibits higher accuracies (comparedb

*16W 959to theSentiStrength) as n> n. Thetest obtainsp= 2:2 10where1001

5 960p < . Thus, the test rejects our null hypothesisH). Hence(the alternative 0 5 961(H) holds true indicating that the dierences in the accuracies ofa W 962and SentiStrengthare statistically signicant. Therefore, we answer the research

963questionRQ5 as follows:

964 Ans.to RQ5:Forsentiment analysis in software engineering text, the domain-specic

dictionarywecreated forperformssignicantly better than a965

largedomain-independent dictionary. 966

# ACCEPTED MANUSCRIPT

44

bottom


---

<!-- Página 46 -->

Group-2

Group-3

# ACCEPTED MANUSCRIPT

Table

Data Sentiment

Positive

Negative

Neutral

Positive

Negative

Neutral

Overall

average

accuracy

Here,SentiStrength

SentiStrength*

### ACCEPTED MANUSCRIPT

SentiStrength WMet.SentiStrength

}50.17%87.56%

R99.60%

¾66.73%

}16.52%

R85.94%

¾27.71%

}91.11%

R05.86%

¾11.01%

}10.40%

R96.79%

¾18.79%

}28.33%

R70.29%

¾40.38%

}75.94%

R08.23%

¾14.84%

}45.41%

R61.12%

¾52.10%

WusesANEWdictionary

45

Wand SentiStrength*

SentiStrength*

98.28%

92.61%

53.19%

97.65%

68.87%

97.94%

81.85%

89.18%

40.44%

82.01%

54.16%

69.10%

72.65%

70.83%

91.22%

79.54%

84.98%

73.24%

85.33%

78.82%

SentiStrength-SE

)


---

<!-- Página 47 -->

### ACCEPTED MANUSCRIPT

WTableMcNemar'stestSentiStrengthand* # of comments misclassied# of 1,01468 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly 3,2701,212 by Tbut not byTclassiedby bothTand Tabab

WHere,T=SentiStrengthand T=SentiStrength*ab

9674.5.4.ManualInvestigation to Reveal Cause

968Weconduct an immediate qualitative investigationto reveal why the large dictionary

969of Warriner et al., having higher coverage, performs worse than our smaller domain- W 970specicdictionary. We identify a set of CfromGroup-2 dataset, which arem WW 971misclassiedbySentiStrength. Fromthe setCwe distinguish another subsetm S 972C, which are correctly classiedSentiStrengthby*. Thenwe randomly pick 50c S 973commentsfrom the setCformanual investigation.c

974Fromthe manual investigation, we nd the domain-specic variations in the mean-

975ing of words (i.e., the dicultyDrevealedin Section 2.5.2) as the main reason for the1

W 976lowaccuracies of. Forexample, the following neutral comment is W 977identiedto have both negative and positive sentimentsSentiStrengthby.

978"... crashforthesamereason.Madesomelocalfixeshere."

979(CommentID: 149494)

980The above comment is misclassied to have both positive and negative sentiments

981due to the presence of the words `Crash' and `Fix', which are negatively and positively

982polarizedwords respectively in the domain-independentANEWdictionaryof Warriner et

983al. [58]. In software engineering domain, both the words are neutral in sentiments. Due

984to the same reason, in detection of neutral comments, the performance of the dictionary

985of Warriner et al. iseven worse thanoptimizedboth theand defaultdictionaryof the

986originalSentiStrength.

# ACCEPTED MANUSCRIPT

46


---

<!-- Página 48 -->

### ACCEPTED MANUSCRIPT

9874.6.Comparisonwith an Alternative Domain Dictionary

988Recallthat our domain dictionarySentiStrength-SEforis developed using com-

989mit messages only. Thereis a possibility that a domain dictionary built on text from

990diversesources may oer better performance. Thus, to verify this possibility, we create

991a second domain dictionary using text from diverse sources and compare this new alter-

992nativedictionary with theSentiStrenght-SEof. In particular, we address

993the following research question:

994 RQ6:Can a domain dictionary developed using texts from diverse sources perform

substantiallybetter than'sdomain dictionary developed based995

on commit messages only? 996

9974.6.1.Buildingan Alternative Domain Dictionary

998In addition to the 490 thousand commit messages used to develop

999dictionary,weobtain 1,600CodeReview Comments(CRC)[61],1,795JIRAIssue

1000Comments(JIC)[60] and 4,423 Stackoverow posts (SOP) [54]. We use software en-

1001gineeringtexts from these diverse datasets to build the alternative domain dictionary.

1002Figure3 depicts the steps/actions performed to develop this new dictionary. Here,

1003in the rst three steps (i.e., step-1 through step-3), we rstthatproduceincludesa set

1004all distinct words from all the four datasets. Then,we deriveCofanother1,198setw

1005wordsthat are common in bothSand the domain-independentdictionary of the original

1006SentiStrength. Thesethree steps aresimilar totherst(Figure 1)

1007developingthe domain dictionary of our. However, here in step-

10081, we use four datasets instead of commit messages only.

1009In step-4, we transform the wild-card formed words in'sdic-

1010tionaryto their full forms. The set of full-formed wordsE is. Indenotedstep-5,aswew

1011derivea set of wordsDfromthe setCsuchthatDcontainsonly thosethatwww

1012are common betweenCand E. Mathematically,D=CãE. Wealso derivewwwww

1013anothersetU, which contains the words thatCarebutinnot inE. Mathematically,www

1014U=C-E.www

# ACCEPTED MANUSCRIPT

47

in


---

<!-- Página 49 -->

### ACCEPTED MANUSCRIPT

Figure

1015All the words incan safely be considered sentimental as thoseare alsow

1016presentinthedictionarySentiStrength-SEof. We needtoidentify thosewords

1017in Uthat areneutral insoftware engineering domain, butcould besentimental inw

1018general.Hence,instep-6, weinvolve three human raters (enumerated asA,B,and

1019C) to independently identify those contextually neutral domain words. Thesehuman

1020ratersare the same threeused in the development of the domain dictionary of

1021SentiStrength-SE.

1022In Table 20, we present sentiment-wise percentage of cases where the human raters

1023disagreepair-wise. Wealso measure the degree of inter-rater agreement in terms of

1024Fleiss-[46]value. The obtainedvalue0.691 signies substantial agreement

1025amongthe independent raters. We consider a word as a neutral domain word when two

1026of the three raters identify the word as neutral. Thus, 373 words are identied as neutral

1027domainwords, which we exclude from theUsetresultingin another set of sentimentalw

1028wordsG. Then,instep-7, bytaking aunion oftheGin andtheD setswww

1029we form another set of wordsM, which contains all the sentimental words. Finally,w

1030in step-8, weadjust the wordsMin reverting them totheir wild-card forms (ifw

1031available)to comply with'sdictionary. This new set of words form

1032our new domain dictionaryN(Atthis stage, we also make sure the words, whichw

1033are manually added in the dictionarySentiStrength-SEof's(see Section 3.1.1), are

# ACCEPTED MANUSCRIPT

48


---

<!-- Página 50 -->

### ACCEPTED MANUSCRIPT

1034includedin the set of words of the new domain dictionary. Thisalternative dictionary

1035contains225 positively and 495 negatively polarized sentimental entries.

10364.6.2.Comparisonbetween the New DictionarySentiStrength-SEand's

1037Wecreate a variantSentiStrength-SEofby replacing its domain dictionary with N 1038the newly created alternative domain dictionary. We callSentiStrength-SEthis variant. N 1039Thenwe compare the performanceSentiStrength-SEofagainst,

1040whichactually implies a comparisonSentiStrength-SEof'sdictionary withnewthe

1041domaindictionary we have created.

Table Disagreementsbetween Human Raters

SentimentalPolarity A,B B,C C,A

Positive12.22%11.32%12.18%

Negative10.21%12.25%11.19%

Neutral13.42%12.15%10.53%

N 1042WeinvokeSentiStrength-SEfordetecting sentiments inissue comments in

1043Group-2and Group-3 datasets. Thenwe compute the precision}), recall( R (and W 1044F-score() ofSentiStrengthin detection of each sentimental polarity. We present N 1045the computed metrics values obtainedSentiStrength-SEbyand N 1046sideby side in Table 21. As seen in SentiStrength-SE21,performsslightly

1047betterthanSentiStrength-SEin detection of negative sentiments. On the other hand,

1048by observing precision and F-score values, we canSentiStrength-SEsay thatper- N 1049formslittle better in detecting positive and neutral comments,SentiStrength-SEalthough

1050achievesslightly higher recall values inthosepositive andneutral comments. The

1051overallaccuracies, aspresented atthebottom threerows ofTable 21,indicate that N 1052the performances betweenSentiStrength-SEanddo not dif-

1053fersubstantially. Toverify the statistical signicance of the observed dierences, we N 1054performanotherMcNemar'stestbetween theresultsSentiStrength-SEofand

1055SentiStrength-SE. For the statistical test, we formulate our null and alternative hy-

1056pothesesas follows:

# ACCEPTED MANUSCRIPT

49


---

<!-- Página 51 -->

Group-2

Group-3

# ACCEPTED MANUSCRIPT

Table

Data Sentiment

Positive

Negative

Neutral

Positive

Negative

Neutral

Overall

average

accuracy

Here,SentiStrength-SE

SentiStrength-SE

### ACCEPTED MANUSCRIPT

NSentiStrength-SEand NMet.SentiStrength-SE

}87.82%

R98.81%

¾92.99%

}53.45%

R97.68%

¾69.09%

}98.13%

R82.57%

¾89.68%

}39.16%41.80%

R82.62%

¾53.13%

}70.44%

R72.25%

¾71.33%

}90.71%

R78.94%

¾84.42%

}73.28%

R85.47%

¾78.91%

Nuses

uses

50

88.86%

93.57%

53.42%

97.66%

69.06%

98.14%

83.00%

89.94%

82.04%

55.39%

68.61%

71.00%

69.78%

90.64%

80.05%

85.02%

73.57%

85.43%

79.06%


---

<!-- Página 52 -->

### ACCEPTED MANUSCRIPT

6 1057NullHypothesis-6H(): Thereis no signicant dierence between the accuracies of 0 N 1058SentiStrength-SEand. 6 1059AlternativeHypothesis-6H (): Thereexist signicant dierences between the accu-a N 1060raciesofSentiStrength-SEand.

NTableMcNemar'stestSentiStrength-SEand # of comments misclassied# of 1,03349 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly 83 4,399 by Tbut not byTclassiedby bothTand Tabab

NHere,T=SentiStrength-SEand T=ab

1061The contingency matrix forMcNemar'sthetestis presented in Table 22. Asseen N 1062in the contingency matrix,SentiStrength-SE(T) and(T)ab

1063exhibitalmost equal accuraciesnüasn. The test obtainsp = 0:0040wherep > .1001

6 1064Thus,the test fails to reject our nullHhypothesis). Therefore,(we conclude that the 0

1065performanceof the newly created domain dictionary does not signicantly dier from

1066that ofSentiStrength-SE'sdomain dictionary. We now formulate the answer to the

1067researchquestion RQ4 as follows:

1068 Ans.toRQ6:Thereisnostatistically signicantdierencebetweentheper-

formancesofthenewlycreateddomaindictionaryandtheof1069

SentiStrength-SE. 1070

10714.6.3.ManualInvestigation to Determine Reasons

1072The result of the aforementionedcomparison appear surprising to us, as we expected

1073the newly created alternative dictionary to perform betterSentiStrength-SEthan that of.

1074Recallthat the newly created dictionary is larger than the domainSentiStrength-SEof .

1075SentiStrength-SE'sdictionary has 167 positively and 310 negatively polarized sen-

1076timentalwords while the newly created one includes 225 positively and 495 negatively

1077polarizedwords. While large number of entries in a dictionary can be helpful in achiev-

# ACCEPTED MANUSCRIPT

51


---

<!-- Página 53 -->

### ACCEPTED MANUSCRIPT

1078ing high recall, they can also misguide the sentiment analysis for a particular domain

1079resultingin low precision. Hence,

1080phasesand identify two reasons why the newly created alternative dictionary failed to

1081outperformthat of

1082Phase-1Investigation: Werandomly select a N 1083SentiStrength-SEmisclassies

1084classies.One such comment is as follows:

1085"I disagree."

1086(CommentID: 1787887_1)

N 1087SentiStrength-SEincorrectly

1088tionalsince the word `disagree' recorded as a negatively polarized word in the newly

1089createddictionary.SentiStrength-SE

1090the word is not included in its dictionary. We identies similar scenarios for all the ve

1091randomlypicked issue comments.

1092Cause-1: Someemotional words present in the new domain dictionary also appear in

1093manyneutral comments of the ground-truth datasets. Which

1094endedup misclassifying those neutral comments as sentimental ones. This

1095knownproblem of high coverage dictionaries [57].

1096Phase-2Investigation: Werandomly pick 20

1097newdomain dictionary, which are not present in the dictionary

1098Then,we search for those words in the ground-truth dataset and nd ve

1099the selected 20 words) (i.e., `abhor', `agony', `appalling', `crime' and `delight') do not

1100appearin any comments in the dataset.

1101Cause-2: Thisimplies, although the new domain dictionary includes more sentimen-

1102tal words compared to the dictionary

1103wordsare unable to create any contribution in sentiment analysis due to their absence

1104in the ground-truth datasets in use.

1105

# ACCEPTED MANUSCRIPT

we manually investigate these possibilities in two

.

set of

their sentiments but

identies the above comment negatively emo-

correctlyidenties the comment as neutral as

inherently emotional words from

SentiStrength-SEof

52

ve issue comments for which

SentiStrength-SEis why

SentiStrength-SE

, those new sentimental

correctly

of

N

is a well-

the

.

(among


---

<!-- Página 54 -->

### ACCEPTED MANUSCRIPT

11064.7.Evaluatingthe Contributions of Heuristics

1107In addition tothedomain dictionary,SentiStrength-SEalsoincludes aset of

1108heuristicstoguidethesentiment detection process towards higher accuracies. The

1109heuristics,particularly designed for software engineering text, are also among the major

1110contributionsof this work. Here,we carry out a quantitative analysis to determine to

1111whatextent these heuristics contribute in the detection of sentiments in software engi-

1112neeringtext. In particular, we address the following research question:

1113 RQ7:Do theheuristics integratedSentiStrength-SEinreallycontribute toim- 1114 provedsentiment analysis in software engineering text? 1115

1116Wecompare the performances ofand SentiStrength* to

1117determinethe contributions of the heuristics.SentiStrengthRecall that* refers to the

1118variantof the originalSentiStrengththat is forced to use our initial domain dictio-

1119nary instead of its original one.SentiStrength-SEThus,and SentiStrength* use

1120the same domain dictionary and the only dierence between them is the set of heuris-

1121ticsthat are includedSentiStrength-SEin. Hence, the heuristics are liable for any

1122dierencesbetween the performancesSentiStrength-SEofand SentiStrength*.

1123Wepresent the performancesSentiStrength-SEofand SentiStrength* in Ta-

1124ble 23. Fordetermining the eects of heuristics included in, let

1125us compare the right-most two columns in Table 23. Weobserve that the precision,

1126recall,and F-score achieved bySentiStrength-SEourare consistently higher than

1127thoseof SentiStrength* inmostcases.Inafew casesfortheGroup-3 dataset,

1128SentiStrength-SE'saccuracy isnearly equal tothoseSentiStrengthof*. The

1129overallaverage accuracies, aspresented atthebottom ofTable 23, alsoindicate the

1130superiorityof SentiStrength-SEoverSentiStrength*, which implies that the

1131heuristicsincorporatedSentiStrength-SEinreallycontribute to higher accuracy in

1132the detection of sentiments in software engineering text.

1133However,asseen inTable 23,although theaccuracySentiStrength-SEofis

1134highercompared toSentiStrength*, they do not dier by a large margin. Thus,it

1135appearsthat the contributions of heuristics, in this particular case, are not substantial

# ACCEPTED MANUSCRIPT

53


---

<!-- Página 55 -->

Group-2

Group-3

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

TableSentiStrength-SE

Data SentimentMet.SentiStrength-SESentiStrength*

}88.86%87.56%

PositiveR98.81%98.28%

¾93.57%92.61%

}53.42%53.19%

NegativeR97.66%97.65%

¾69.06%68.87%

}98.14%97.94%

NeutralR83.00%81.85%

¾89.94%89.18%

}41.80%40.44%

PositiveR82.04%82.01%

¾55.39%54.16%

}68.61%69.10%

NegativeR71.00%72.65%

¾69.78%70.83%

}90.64%91.22%

NeutralR80.05%79.54%

¾85.02%84.98%

Overall}73.58%73.24%

averageR85.43%85.33%

accuracy¾79.06%78.82%

*Here,SentiStrength*

54


---

<!-- Página 56 -->

### ACCEPTED MANUSCRIPT

1136and unlikely to be statistically signicant. Toverify our observations, we perform a

1137McNemar'stestbetween the resultsSentiStrengthof* andSentiStrength-SE. For

1138the test, we formulate our null and alternative hypotheses as follows: 7 1139NullHypothesis-5H(): Thereis no signicant dierence between the accuracies of 0

1140SentiStrength-SEand SentiStrength*. 7 1141AlternativeHypothesis-5H (): Thereexist signicant dierences between the accu-a

1142raciesofSentiStrength-SEand SentiStrength*.

TableMcNemar'stestSentiStrength-SEand SentiStrength* # of comments misclassied# of 993 78 by bothTand Tby Tbut not byTabba

# of comments misclassied# ofcorrectly 814,433 by Tbut not byTclassiedby bothTand Tabab

Here,T=SentiStrength-SEand T=SentiStrength*ab

1143The contingency matrix forMcNemar'sthetestis presented in Table 24. As

1144in the contingency matrix,SentiStrengthSE(T) andSentiStrength* (T) exhibitab

1145almostequal accuraciesnasün. The test obtainsp = 0:874 wherep > . Thus, the1001

7 1146testfails to reject our null hypothesisH). Therefore,(we conclude that the contribution 0

1147of the heuristics in the tool is not signicant in this particular case.

1148Basedon our observations from the quantitative analysis and the statistical test, we

1149nowformulate the answer to the research question RQ5 as follows:

1150 Ans.toRQ7:Althoughthe set of heuristics integratedSentiStrength-SEincon-

tributetowards improved sentiment analysis in software engineering text, the perceived1151

improvementis not statistically signicant for the given datasets. 1152

1153Recallthat, from the exploratory study (Section 2) using the Group-1 portion of the

1154GoldStandard" dataset, we found that the majority of the misclassications of senti-

1155mentalpolarities are due to the limitations (diculties, D, D) of the dictionary136

1156in use (Table 3). Hence, the majority of misclassications are to be corrected by using

1157a domain dictionary,leavinga relatively narrow scope for further contributions from

# ACCEPTED MANUSCRIPT

55

seen


---

<!-- Página 57 -->

### ACCEPTED MANUSCRIPT

1158the heuristics, atleast for this Gold Standard" dataset. Ourmanual investigation of

1159the datasets used in this study conrms the existencevery few ofcomments within

1160operationalscope of the heuristics.

11614.7.1.FurtherManual Investigation

1162AlthoughSentiStrength-SEis found to have performed better in most cases, as

1163seenin Table 23, in four cases for the Group-3SentiStrength-SEdataset'saccuracy

1164is marginallylowerthanSentiStrength*. Animmediate qualitative investigation

1165revealstwo reasons for this, which we discuss now.

1166First, our parameter setting to identify negations of sentimental words falls short in

1167capturingnegations in some cases. Forexample, in the following issue comment, the

1168negationword Don't" preceding the word `Know' neutralizes the negatively polarized

1169word`Hell' due to the negation conguration parameter set to ve in

1170"I don'tknowhowthehellmydiffprogramdecidetoaddseemingly

1171randomCRchars,buti'veremovedthemnow"(CommentID: 306519_2)

1172A lower negation parameter could work better for this particular issue comment, but

1173mightperform worse for negations in others. Other possible solutions are discussed in

1174Section4.9.

1175Second, we also found instances of incorrect annotations for negative sentiments for

1176someissue comments in the Group-3 dataset, which caused the SentiStrength-SE

1177appearto go down. Consider the following two issue comments.

1178"Insertingtimestampsautomagically wouldbebadbecauseit

1179limitawholeswathofusecases"(CommentID: 1462480_2)

1180"If thatwouldbethecase,thisbebaddesign"

1181(CommentID: 748115_2)

1182In the above two issue comments, the author stated merely the possibilities of neg-

1183ativescenarios that hadn't happened yet. These comments do not convey negative sen-

1184timents.But the human raters annotated with negative sentiments possibly due consid-

1185ering the use of negatively polarized word `Bad' in the sentences.

# ACCEPTED MANUSCRIPT

56

.

of


---

<!-- Página 58 -->

### ACCEPTED MANUSCRIPT

1186Theseobservations inspire us to conduct a deeper qualitative investigation of the

1187successscenarios and especially the failureSentiStrength-SEcases ofmainly

1188ploreopportunities for further improvements to the tool. Hence, a qualitative evaluation

1189of SentiStrength-SEis presented in the following section.

11904.8.QualitativeEvaluation of SentiStrength-SE

1191Althoughfrom the comparative evaluations we foundSentiStrength-SEour

1192periorto the all selectedSentiStrength-SEtools,is not a foolproof sentiment anal-

1193ysistool. Indeed, 100% accuracy cannot be a pragmatic expectation. Nevertheless, we

1194carry out another qualitative evaluationSentiStrength-SEofwith two objectives:

1195rst,toconrm that the achieved accuracy found in the comparative evaluations did

1196not occur by chance, and second, toidentify failure scenarios and scopes for further

1197improvements.

1198Werst randomly pick 150 issue comments (50 positive, 50 negative, and 50 senti-

1199mentallyneutral) from theGroup-2 and Group-3 oftheGold Standard" dataset for

1200whichSentiStrength-SEcorrectlydetected thesentimental polarities. From

1201manualverication over these 150 issue comments, we are convinced that the design

1202decisions,heuristics, and parameter congurationSentiStrength-SEadopted in

1203positiveimpacts on the accurate detection of sentimental polarities.

1204Next,we randomly choose another 150 issue comments (50 positive, 50 negative,

1205and 50 sentimentally neutral) forSentiStrength-SEwhichfailedto correctly detect

1206the sentimental polarities. Upon manual investigation of those 150 issue comments, we

1207nd a number of reasons for the inaccuracies, a few of which are within the scope of

1208the design decisions appliedSentiStrength-SEto, and the rest falls beyond, which

1209we discuss in Section 4.9. Oneof the reasons for failure is missing sentimental terms

1210in our newly created domain dictionary. For example,incorrectly

1211identiedthe following comment as neutral in sentiment by misinterpreting the senti-

1212mentalword `Stuck' as a neutral sentimental word, since the word was not included in

1213the dictionary, which we add to the dictionarySentiStrength-SEof'srelease.

1214"For thefirstpart,Igotstuckontwopoints"(CommentID: 1610758_3)

# ACCEPTED MANUSCRIPT

57

to ex-

su-

have

our


---

<!-- Página 59 -->

### ACCEPTED MANUSCRIPT

1215Someother cases we have found inconsistencies in human rating of sentiments in

1216issuecomments, which are liable for inaccuracySentiStrength-SEin. For example

1217the following comment is rated as neutral in sentiment by human raters, although that

1218containsthe positive sentimental term `Thanks' along with the exclamatory sign `!'.

1219"And manythankstoyouOliverforapplyingthissoquickly!"

1220(CommentID: 577184_1)

1221Our investigation reveals that 200 issue comments are wrongly interpreted in Group-3

1222by human raters that cause low accuracySentiStrength-SEinfordetecting positive

1223sentiment,which is aligned with our earlier ndings of such wrong interpretation of

1224sentiments.

1225Althoughthe additional preprocessing phaseSentiStrength-SEofltersout un-

1226wantedcontent such as source code, URL, numeric values from the input texts, we found

1227severalinstances where such contents escaped the ltering technique and misguided the

1228tool.

1229In a few cases, we found that our heuristics to identify proper nouns fell short for

1230not taking into account probable cases. ForSentiStrength-SEexample,incorrectly

1231computednegative sentiment in the following issue comment. As seen in the

1232commenta developer thanked his colleague name `Harsh'.

1233"ThanksHarsh,thepatchlooksgood...SincethisisanewAPI,

1234we arenotsureifwanttochangeit.Let'sleaveitas-isfor

1235the moment."(CommentID: 899420)

1236For failing to identify `Harsh' as a properSentiStrength-SEnoun,consideredthe

1237wordsentimentally negative anderroneously detectssentiment in

1238sage.Our immediate future plan includes further extension to our heuristics for locating

1239propernouns in text.

12404.9.Threatsto Validity

1241In this section, we discuss the threats to the validity of the empirical evaluation of

1242SentiStrength-SEand our eorts in mitigating them.

# ACCEPTED MANUSCRIPT

58

themes-


---

<!-- Página 60 -->

### ACCEPTED MANUSCRIPT

12434.9.1.ConstructValidity and Internal

1244Threatsto construct validity relate to the suitability of the evaluation metrics. We

1245use three metrics:precision, recalland F-score

1246mancesof SentiStrength-SEand other tools. All

1247monlyused for similar purposes insoftware engineering studies [61, 62,

1248quantitativeanalysis may notportray the

1249formedboth quantitative and qualitative evaluation

1250The accuracies inthecomputations of

1251in the manual annotation of the issue comments with sentimental polarities. Hence,

1252we have manually checked the annotations of issue comments in the Gold Standard

1253dataset.Weidentied around 200 issue comments that are incorrectly labelled with

1254wrongsentimental polarities. Nevertheless, we did not exclude those misclassied issue

1255commentsbecause they equally aect all the tools without favoring one over another.

1256Tocompare the performanceSentiStrength-SEof

1257NLTK, andStanfordNLP), we have used their default settings. Dierent

1258thosetools might provide dierent results, however we adhered to their default settings

1259due to their uses in earlier software engineering studies [3, 4, 5, 6, 17, 18, 19, 20, 25,

126050, 63].

1261WhileoptimizingSentiStrength'sdefault

1262domain,we assigned three constant values +3,

1263tralcomments, respectively.One may question the reasons for choosing those particular

1264valuesinstead of otherin the domains. For example, we could have used +2, +4

1265or +5 instead of +3 and -2,-4 or -5

1266onlyindicate polarities of sentiments but also their intensities/strength

1267putationof precision, recall and F-score, only the sentimental polarities are considered.

1268Henceany value from +2 to +5 for positively polarized comments and any

1269-2 to -5 for negatively polarized comments could be used in the process of optimiza-

1270tion.Wesimply picked the values in the median, instead of choosing extreme ones at

1271the domain boundaries.

1272Wechanged the range of valence scores of the words from [+1, +9] to [-5, +5] in the

# ACCEPTED MANUSCRIPT

59

to evaluate the classication perfor-

the three metrics have been com-

whole picture, which is

SentiStrength-SEof

themetrics are

againstother tools SentiStrength,

dictionary for software engineering

,1-3toand

of -3. Recall

.

subject to

negative and neu-

that those integer values not

54]. Only

why wehave per-

thecorrectness

settings of

[53]. In the com-

from


---

<!-- Página 61 -->

### ACCEPTED MANUSCRIPT

1273ANEWdictionaryof Warriner et al. [58] to compare its performance against the domain

1274dictionaryofSentiStrength-SE. One might argue that the range conversion

1275havealtered the original sentimental polarities of some words. We have considered this

1276possibilityand carefully designed the conversion scheme to minimize such possibili-

1277ties.Arandom sanity check after the range conversion indicates absence of any such

1278occurrence.

12794.9.2.ExternalValidity

1280The use of only one benchmark dataset (i.e., the Gold Standard" dataset) can be

1281consideredalimitation oftheempirical evaluationSentiStrength-SEofour

1282outcomeof the work could be more generalizable if more than one benchmark datasets

1283couldbe used. At the time of rst releaseSentiStrength-SEof, this Gold Standard"

1284datasethas been the only publicly availableespecially crafted for the software

1285engineeringdomain [29, 32]. Afew newer datasets are available, but those are either

1286not software engineering domain specic or they are even more

1287context(e.g., codereview, product review). Theissue comments in

1288datasetare collected from open-source systems and thus one may question whether or

1289not the tools including ours will perform dierently if applied on datasets drawn from

1290industrial/proprietaryprojects. Producinga large dataset with human annotations is a

1291tediousand time consuming task. We are working towards creating a second benchmark

1292datasetfor sentiment analysis in software engineering text. Once

1293releasethe dataset for the community.

1294Althoughthere are diverse sources of textual content produced at dierent stages

1295of software development andmaintenance, thebenchmark dataset we

1296onlyJIRA issue comments. Hence,onemay argue that theresults of

1297comparisonof tools might substantially vary if a dataset with a dierent type of text

1298is used. Recallthat thedictionarySentiStrength-SEofourtooliscreated based

1299on commit comments. Thus,itssuperior performances onissue comments give us

1300condencethat the tool will also perform well on other types of textual content.

# ACCEPTED MANUSCRIPT

60

. The

to a narrower

thebenchmark

completed, we will

used contains

theempirical


---

<!-- Página 62 -->

### ACCEPTED MANUSCRIPT

13014.9.3.Reliability

1302The methodology of this study including the procedure for data collection and anal-

1303ysisis documented in this paper. The Gold Standard" dataset [29] and all the tools (i.e.,

1304SentiStrength-SE[31],SentiStrength[22],

1305are available freelyonline. Therefore,

1306empiricalevaluation of our tool.

13075. Limitationsofand Future Possibilities

1308In thissection, wediscuss thelimitations in

1309SentiStrength-SEas well as some directions for further improvements to our tool.

1310In the development of, we have addressed the diculties identi-

1311ed from the exploratory study described in Section 2. Still there are scopes for further

1312improvements,as we also found from the qualitative evaluation of the tool. For

1313ple,wehave observed inSection 4.8 that missing of

1314the SentiStrength-SE. We have created an

1315SentiStrength-SEusingtexts from diverse sources. Surprisingly,

1316ateddomain dictionary do not oer signicant performance improvements. We plan to

1317furtherextend our domain dictionary by integrating with dierent

1318approaches[62, 64, 65].

1319Our adopted approach for domain dictionary creation is unique from other attempted

1320approaches[62, 64, 65]. Wehave deliberately chosen this approach for two reasons.

1321First,we wanted to introduce a new approach, and second, it was not possible to adopt

1322existingapproached due to limitation of resources such as sentiment-annotated texts in

1323softwareengineering [29]. Through the empirical evaluations, we have shown that our

1324createddomain dictionary is eective for sentiment analysis in software engineering.

1325Moreover,in the process of development of the dictionary the identication of domain

1326terms by three human raters might cause a subjectivity bias. However, we have mea-

1327suredthe inter-rater agreements, and found reasonable

1328the threat substantially.

1329In thecreation ofournewdomain dictionary, we

# ACCEPTED MANUSCRIPT

61

NLTK[23]

alternative new domain dictionary for

andStanfordNLP[38])

it should be possible to replicate the

thedesignandimplementation of

sentimental words can mislead

thisnewly cre-

which minimizes

usedgraduate students as

exam-

building

the


---

<!-- Página 63 -->

1330humanraters, rather than expert software developers from industry. However, all the

1331participantshave at least three years of software development experience, which miti-

1332gatesthis threat. Moreover, it is reported that only minor dierences exist between the

1333performancesof graduate students and professional software developers especially at

1334smalltasks involving simple judgements [66].

1335The use of only three human raters may be argued as a

1336pants.However, two to three raters have been common practice in successful software

1337engineeringstudies [61, 62, 54, 67]. Moreover, through the empirical evaluations (both

1338quantitativeand qualitative), we have shown that our created domain dictionary is ef-

1339fectivefor sentiment analysis in software engineering text.

1340Severalmethods have been proposed and discussed to identify the scope of the nega-

1341tionsof polarized words in sentiment analysis [68, 69], which can be applied to improve

1342the performance of our negation handling approach. Many sophisticated approaches to

1343identifythe negation's scope include machine learning techniques [68, 70], complex

1344rules [71], and identifying negated words using semantics of phrases [72]. However,

1345manyexisting sentiment analysis approaches have relatively simple methods to identify

1346scopeof negation [73, 74]. Interestingly, performance of a

1347can be improved by domain adaptation [75]. In

1348tionedmethods by applying in software engineering contexts to identify the best method

1349to detect scope of negation.

1350Althoughour approach for ltering out code snippets may not correctly locate all

1351codeportions, but the ltering indeed minimizes them. Indeed, isolating inline source

1352codefrom plain text content is a challenging task, especially when the text can have code

1353writtenin diverse undeclared programming language. Such a code separation problem

1354can be a separate research topic and limited scope attempts are made in the past [76]. We

1355alsoplan to invest eorts along this direction to further

1356At this stage, we did not address the diculties

1357cludedin our future plan. The detection of irony, sarcasm, and subtle emotions hidden

1358in text is indeed a challenging research topic in NLP and not only related to software en-

1359gineeringtexts. Even human interpretations of sentiments in text often disagree as such

1360we also found in the Gold Standard" dataset. Combining the dictionary-based lexical

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

62

small number of partici-

future, we will evaluate all the men-

SentiStrength-SEimprove

D; D; andD, which are in-101112

detection method

.


---

<!-- Página 64 -->

### ACCEPTED MANUSCRIPT

1361methodwith machine learning [77] and other specialized techniques [78] can lead to po-

1362tentialmeans to address these diculties. We also plan

1363the capability to identify interrogative sentences correctly mitigate

13646. Relatedwork

1365Tothe best of our knowledge, the

1366that analyzespublicbenchmark dataset

1367sis in software engineering. And,

1368SentiStrength-SE, crafted especially for software engineering domain, which

1369expectto produce superior performance in other technical domains as well.

1370Asidefrom our tool, there are only four prominent tools/toolkits

1371StanfordNLP[38],NLTK[23],

1372mentanalysis inplain texts. The

1373mentanalysis insoftware engineering domain,

1374frequentlyin the studies as presented in Table 25. We categorize those

1375ter understanding of the uses of those tools and the contributions of

1376softwareengineering domain. Those tools, which are previously used in

1377neeringarea, but for sentiment analysis

1378of the studies used any domain specic tool to detect sentiments.

1379Alchemy[79]isacommercial toolkit that oers limited sentiment analysis as

1380servicethrough its published APIs. According to the study of Jongeling et al. [34] the

1381performanceofAlchemyis lower than

1382StanfordNLP[38]are general purpose natural language processing (NLP) library/-

1383toolkit,which expect the user to have some NLP background and to write scripting code

1384forcarrying out sentiment analysis in plain text.

1385catedtool that applied a lexical approach for automated sentiment analysis and is ready

1386to operate without needing to write any scripting code (for natural language process-

1387ing).Perhaps,these are among the reasons why, in software engineering community,

1388SentiStrengthhas gained popularity over the alternatives. The

1389madeus choose this particular tool as the basis of our

# ACCEPTED MANUSCRIPT

qualitative study (Section 2), is

to expose the challenges to sentiment analy-

we have developed the rst sentiment analysis tool,

andAlchemy[79],

rst three of

, are excluded from the table. Notably, none

SentiStrength

63

SentiStrength-SEto add to

D. the diculty10

SentiStrengthnamely,

which facilitate automatic senti-

these tools have been used for senti-

SentiStrengthwhileis used most

[22]andNLTK[23].NLTKand

SentiStrengthIn contrast,is a dedi-

same reasons also

SentiStrength-SEwork. Our

the rst

we

[22],

for bet-

studies in

engi-

a


---

<!-- Página 65 -->

### ACCEPTED MANUSCRIPT

Tablesentimentand

ToolsTypeof Work

Analyzingsentiments in

softwareengineering (SE) SentiStrength[22] Applicationsof

sentimentsin SE

Benchmarkingstudy [25,

Analyzingsentiments in SE NLTK[23] Benchmarkingstudy [25,

Applicationsof

StanfordNLP[38]sentimentsin SE

Benchmarkingstudy [25,

1390reusesthe lexical approach of theSentiStrengthoriginal

1391o the shelf.

1392All of the aforementionedfour toolsSentiStrength(i.e.,

1393NLTK[23],andAlchemy[79])are developed and trained to operate on non-technical

1394textsdrawn from social interactions, web pages, and they do not perform well enough

1395whenoperated in a technical domain such as software engineering. Domain-specic

1396(e.g.,software engineering) technical uses of inherently emotional words seriously mis-

1397leadthe sentiment analyses of those tools [5, 6, 25, 27] and limit their applicability in

1398softwareengineering area. Wehave addressed this issue by developing the rst soft-

1399wareengineering domain-specic dictionary included in

1400Alongthis direction Mäntylä et al. [11] developed a

1401arousalin the software engineering texts.

1402Apart from creating domain dictionary, a variety of machine learning (ML) tech-

1403niquessuch as, Naive Bayes classier (NB), Support Vector Machine (SVM) [73], and

1404LogisticRegression (LR) [84] have been explored in an attempt to minimize the domain

1405diculty.However, the performances of all these three classiers are reported lower

# ACCEPTED MANUSCRIPT

64

Usesin Software

EngineeringResearch

[3, 6, 8, 9, 19, 27, 80, 81]

[4, 17, 18, 20, 28, 82, 83]

34]

[5, 63]

34]

[50]

34]

and is also ready to be used

[22],StanfordNLP[38],

SentiStrength-SEour tool.

dictionaryemotionalto capture


---

<!-- Página 66 -->

### ACCEPTED MANUSCRIPT

1406whenoperated on domain-specic texts [85]. Nonetheless, recently Murgia et al. [86]

1407appliedseveral ML techniques (e.g., NB, SVM) to identifyloveemotions, joyand sad-

1408ness onlyin contrast to ourSentiStrength-SEtoolthat can dierentiatepositivity

1409negativityand neutralityof software engineering texts. Again,Panichella et al. [67]

1410usedNB classier to detect sentiments in software users' reviews. However,

1411curacyof their classier was not reported. Thosetwo tools are not publicly available

1412to compare against our tool. Moreover, we avoided to apply ML

1413techniqueto implementSentiStrength-SEdue to the limitations of ML for sentiment

1414analysisthat include its diculty to integrate into a classier and learned models often

1415havepoor adaptability between dierent text genres or domains as they often rely on

1416domainspecic features found in their training data [85].

1417Blazand Becker [62] proposed three almost equally performingDictio-methods, a

1418nary Method (DM), aTemplate(TM)and aHybrid(HM)forsentiment

1419analysisin Brazilian Portuguese texts in IT (Information Technology) job submission

1420tickets.TheDM is a pure lexical approach similar toSentiStrength-SEthat of our

1421Althoughtheir techniques might be suitable for formally structured texts, those may not

1422performwell in dealing with informal texts that are frequently used in software engi-

1423neeringartifacts such as commit comments. Incontrast, from the empirical evaluation

1424overcommit comments, ourSentiStrength-SEis found to have high accuracy in de-

1425tectingsentiments in those informal software engineering texts. The proposed methods

1426of Blaz and Becker [62] are developed and evaluated against text written in Brazilian

1427Portugueselanguage instead of English. Thus, their approach and reported results are

1428not directly comparable to ours.

1429Similarto the qualitative study included in our work, Novielli et al. [27] also con-

1430ducteda relatively brief study of the challenges against sentiment analysis in social pro-

1431grammerecosystem". Theyalso usedSentiStrengthforthe detection of emotional

1432polaritiesand reported only domain diculty as a key challenge. In

1433manuallystudied only 100 questions and their follow-up comments as well as 100 an-

1434swersand their follow-up discussions obtained from Stack Exchange Data Dump [87].

1435In contrast, based on a deeper analysis over a publicly available benchmark dataset, our

1436studyexposes 12 diculties including the domain dependency. In addition, we address

# ACCEPTED MANUSCRIPT

65

,

.

their work, they

theac-


---

<!-- Página 67 -->

### ACCEPTED MANUSCRIPT

1437a portion of those diculties and develop a domain-specic tool for improved sentiment

1438analysisin software engineering text.

1439OurSentiStrength-SEis therstsoftwareengineering domain specic senti-

1440mentanalysis tool. Soon after the releaseSentiStrength-SEof, four domain-specic

1441tools/toolkits(i.e.,Senti4SD[54],SentiCR[61],EmoTxt[88],andSentiSW[89])

1442haveappeared over the last few months. SimilarSentiStrength-SEto our,Senti4SD

1443is also a software engineering domain specic sentiment analysisSenti4SDtool.ap-

1444pliesmachine learning based on lexicon and keywordfeatures for detecting sen-

1445timents.SentiSWalsoapplies machine learning techniques todetect sentiments at

1446entity-levels. EmoTxt[88]is an open-source toolkit for detecting six basic emotions

1447(i.e.,love, joy, anger, sadness, fear, and surprise)technicalfrom. Theauthors of

1448SentiCRdeclaredthe scope of this tool limited to code review comments only. Again,

1449the applicabilitySentiSWofis limited to only JIRA issue comments. Thereported

1450scopeof EmoTxtis technical domain, which iswider than software engineering do-

1451main.Onthe contrary, the scopesSentiCRofand SentiSWare limited to narrower

1452domainsof code review comments and JIRA issue comments, respectively.

1453Twoseparate studies were conducted to compare the performances of those domain

1454specicsentiment analysis tools. Inthe rst study, Islam and Zibran [90] compared

1455the performances of, Senti4SDand EmoTxtand found no con-

1456vincingwinner among the tools for sentiment analysis in software engineering. In

1457laterstudy, Novielli etal.[91] compared theperformancesSentiStrength-SEof,

1458Senti4SDandSentiCRand found the unsupervised approachSentiStrength-SEof

1459had provided comparable performance to that of supervised techniquesSenti4SD(i.e.,

1460and SentiCR).SentiSWwasnotavailable atthetimeofconducting thetwo

1461parativestudies. However, developersSentiSWofcomparedits performance against

1462SentiStrength-SEand found their tool's superiority overin de-

1463tectingsentiments expressed in JIRA issue comments. Whileall those studies com-

1464paredthe performances of domain specic tools, for the rst time, Jongeling et al. [25,

146534] compared theperformances ofdomain independentSentiStrengthtools[22],

1466NLTK[23],StanfordNLP[38]and Alchemy[79]tomeasure their applicability in

1467softwareengineering domain.

# ACCEPTED MANUSCRIPT

66

com-

the


---

<!-- Página 68 -->

1468Wedo not claim

1469availablefor sentiment analysis in software engineering text. Instead,

1470and evaluating the

1471mentanalysis in software engineering

1472icantlybetter compared to its

1473our SentiStrength-SE

1474wareengineering. Other

1475in attempting domain-specic solutions resulting in several

1476cussedabove.

14777. Conclusion

1478In this paper, we have rst presented an in-depth qualitative study to identify the

1479dicultiesin automated sentiment analysis in software engineering texts. Among

1480diculties,the challenges due to domain dependency are found the most dominant. To

1481addressmainly the

1482especiallydesigned for sentiment analysis in software engineering text.

1483Wealso develop a number of heuristics to address some of the other identied di-

1484culties.Our new domain dictionary and the heuristics are

1485a tool we have developed for improved sentiment analysis in textual contents in a tech-

1486nicaldomain, especially in software engineering. Our

1487of SentiStrength

1488sentimentanalysis technique.

1489timentanalysis tool especially designed for software engineering text.

1490Overalarge dataset (i.e., Group-2 and

1491ments,we carry out quantitative comparisons

1492with the three most popular

1493NLP[24],and the original

1494that our domain-specic

1495dependentcounterparts

1496Usingboth quantitative and qualitative evaluations, we also separately verify the

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

SentiStrength-SE

SentiStrength-SE, we demonstrate that, for senti-

is the rst domain-specic tool for sentiment analysis in soft-

researches might have taken motivations from our work [32]

domaindiculty, we have developed a domain-specic dictionary

[22],which, in software engineering, is the most widely adopted

SentiStrength-SEOur

domainindependent

SentiStrength

SentiStrength-SE

in detecting emotions in software engineering textual contents.

to be the best tool among all the few tools

domain-specictext, atechniqueperforms signif-

counterparts.As mentioned before,

SentiStrength-SEintegrated in

tool reuses the lexical approach

is the rst domain-specic sen-

Group-3) consisting of

domain-specicof ourSentiStrength-SE

tools/toolkits(i.e.,[23],Stanford

[22].Theempirical comparisons suggest

is signicantly superiordomainto its

67

5,600 issue com-

in-

by developing

tools dis-

,

the


---

<!-- Página 69 -->

### ACCEPTED MANUSCRIPT

1497eectivenessofthedesign decisions including the

1498we have included in ourdomain-specic

1499we found that our newly created domain dictionary makes statistically signicant con-

1500tributionsto improved sentiment analysis in software engineering text. However, the

1501heuristicswe developed to minimize the issues beyond the domain diculties are found

1502not to have substantial impacts on sentiment analysis of the chosen datasets. The

1503substantialimpact of the heuristics further validates that the improvements in the ac-

1504curaciesofSentiStrength-SE

1505demonstratethat, for sentiment analysis in software engineering text, a domain-specic

1506techniqueperforms substantially better than domain independent techniques.

1507In future, we plan to further verify these ndings by extending

1508and operating it on industrial/proprietary datasets. Both from the exploratory study and

1509qualitativeevaluation of our sentiment analysis tool, we have also identied scopes for

1510furtherimprovements of the tool, which remain within our future research plans. Using

1511SentiStrength-SEand its future releases, we also plan to conduct large scale studies

1512of emotional variations and their impacts using both public and proprietary datasets in

1513softwareengineering domain. The current release

1514freelyavailable [31] for public use.

# ACCEPTED MANUSCRIPT

are attributed to itsdomain-specic

SentiStrength-SE. From the evaluations,

68

domain dictionary and

being

SentiStrength-SEof our

. Thus,

is made

we

heuristics

non-


---

<!-- Página 70 -->

### ACCEPTED MANUSCRIPT

1515References

1516[1] M.Choudhury, S. Counts, Understanding aect in the workplace via social media,

1517in: Proceedings of the Computer supported cooperative work, 2013, pp. 303316.

1518[2] P.Dewan, Towards emotion-based collaborative software engineering, in:

1519ceedingsof the International Workshop on Cooperative and Human Aspects of

1520SoftwareEngineering, 2015, pp. 109112.

1521[3] E.Guzman, D. Azócar, Y. Li, Sentiment analysis of commit comments in github:

1522An empirical study, in: Proceedings of the International Conference on Mining

1523SoftwareRepositories, 2014, pp. 352355.

1524[4] E.Guzman, B. Bruegge, Towards emotional awareness in software development

1525teams,in:ProceedingsoftheInternational Symposium on

1526SoftwareEngineering, 2013, pp. 671674.

1527[5] D.Pletea, B. Vasilescu, A. Serebrenik, Security and emotion: Sentiment analysis

1528of security discussions on github, in: Proceedings of the International Conference

1529on Mining Software Repositories, 2014, pp. 348351.

1530[6] P.Tourani, Y. Jiang, B. Adams, Monitoring sentiment in open source mailing lists

1531 exploratory study on the apache ecosystem, in: Proceedings of the Conference

1532of the Centre for Advanced Studies on Collaborative Research, 2014, pp. 3444.

1533[7] D.Graziotin, X. Wang, P. Abrahamsson, Are happy developers more productive?

1534The correlation of aective states of software developers and their self-assessed

1535productivity,in: Proceedings of the International Conference on Product-Focused

1536SoftwareProcess Improvement, 2013, pp. 5064.

1537[8] M.Islam, M. Zibran, Exploration and exploitation of developers'

1538ationsin software engineering, International Journal of Software Innovation 4 (4)

1539(2016)3555.

1540[9] M.Islam, M.Zibran, Towards understanding and

1541tionalvariations insoftware engineering, in:

# ACCEPTED MANUSCRIPT

69

exploiting developers' emo-

Proceedings

theFoundations of

sentimental vari-

oftheInternational

Pro-


---

<!-- Página 71 -->

### ACCEPTED MANUSCRIPT

1542ConferenceonSoftware Engineering Research Management and

15432016,pp. 185192.

1544[10]T.Lesiuk, The eect of music listening on work performance, Psychology of Mu-

1545sic 33 (2) (2005) 173191.

1546[11]M.Mäntylä, B.Adams, G.

1547arousal,and dominance  possibilities for detecting burnout and productivity, in:

1548ProceedingsoftheInternational Conference on

15492016,pp. 247258.

1550[12]A.Murgia, P. Tourani, B.

1551exploratoryanalysis of emotions in software artifacts, in: Proceedings of the In-

1552ternationalConference on Mining Software Repositories, 2014, pp. 261271.

1553[13]M.Wrobel, Emotions in the software development process, in: Proceedings of the

1554InternationalConference on Human System Interaction, 2013, pp. 518523.

1555[14]M.Wrobel, Towards the participant observation of emotions in software develop-

1556mentteams, in: Proceedings of the Federated Conference on Computer Science

1557and Information Systems, 2016, pp. 15451548.

1558[15]D.McDu, A. Karlson, A. Kapoor, A. Roseway, M. Czerwinski, Aectaura: an

1559intelligentsystem for emotional memory, in: Proceedings of the Conference on

1560HumanFactors in Computing Systems, 2012, pp. 849858.

1561[16]G.Destefanis, M. Ortu, S. Counsell, M. Marchesi, R. Tonelli, Software develop-

1562ment:do good manners matter?, PeerJ PrePrints (2015) 117.

1563[17]M.Ortu, B. Adams, G. Destefanis, P. Tourani, M. Marchesi, R. Tonelli, Are bul-

1564liesmore productive? Empirical

1565ProceedingsoftheInternational Conference on

15662015,pp. 303313.

1567[18]F.Calefato, F. Lanubile, Aective trust as a predictor of successful collaboration

1568in distributed software projects, in: Proceedings of the International Workshop on

# ACCEPTED MANUSCRIPT

Destefanis, D.

Adams, M.

study of aectiveness vs. issue xing time, in:

70

Graziotin, M.

Ortu, Do

Mining Software Repositories,

developers feel emotions? An

Mining Software Repositories,

Applications,

Ortu, Mining valence,


---

<!-- Página 72 -->

### ACCEPTED MANUSCRIPT

1569EmotionAwareness in Software Engineering, 2016, pp. 35.

1570[19]S.Chowdhury, A.Hindle, Characterizing energy-aware software projects: Are

1571theydierent?, in: Proceedings of the International Conference on Mining Soft-

1572wareRepositories, 2016, pp. 508511.

1573[20]D.Garcia, M. Zanetti, F. Schweitzer, The role of emotions in contributors activ-

1574ity:Acase study on the gentoo community, in: Proceedings of the International

1575Conferenceon Cloud and Green Computing, 2013, pp. 410417.

1576[21]N.Novielli, F. Calefato, F. Lanubile, Towards discovering the role of emotions in

1577stackoverow, in: Proceedings of the International Workshop on Social Software

1578Engineering,2014, pp. 3340.

1579[22]M.Thelwall, K. Buckley, G. Paltoglou, Sentiment strength detection for the social

1580web,Journal of the American Society for Info. Science and Tech. 63(1) (2012)

1581163173.

1582[23]NLTK,NaturalLanguage

1583[http://www.nltk.org/api/nltk.sentiment.html](http://www.nltk.org/api/nltk.sentiment.html),

1584[24]R.Socher, A.Perelygin, J.

1585cursivedeep models for semantic compositionality over a sentiment treebank, in:

1586Proceedingsof the Conference on Empirical Methods in Natural Language Pro-

1587cessing,2013, pp. 16311641.

1588[25]R.Jongeling, S.Datta, A.

1589analysistools for software engineering research, in: Proceedings of the Interna-

1590tionalConference on Software Maintenance and Evolution, 2015, pp. 531535.

1591[26]N.Novielli, ListofTools Used

1592[http://www.slideshare.net/nolli82/the-challenges-of-aect-detection-in-the-](http://www.slideshare.net/nolli82/the-challenges-of-aect-detection-in-the-)

1593social-programmer-ecosystem,

1594[27]N.Novielli, F. Calefato, F. Lanubile, The challenges of sentiment detection in the

1595socialprogrammer ecosystem, in: Proceedings of the International Workshop on

# ACCEPTED MANUSCRIPT

Toolkit

Wu, J.

Serebrenik, Choosing your weapons: On

last access: June 2018.

71

forSentiment

last access: June 2018.

Chuang, C.Manning, A.

inSoftware Engineering to

Analysis,

Ng,C.Potts, Re-

sentiment

DetectEmotions,


---

<!-- Página 73 -->

### ACCEPTED MANUSCRIPT

1596SocialSoftware Engineering, 2015, pp. 3340.

1597[28]P.Tourani, B. Adams, The impact of human discussions on just-in-time quality

1598assurance,in: Proceedings of the International Conference on Software Analysis,

1599Evolution,and Reengineering, 2016, pp. 189200.

1600[29]M.Ortu, A. Murgia, G. Destefanis, P. Tourani, R. Tonelli, M. Marchesi, B. Adams,

1601The emotional side of software developers in JIRA, in: Proceedings of the Inter-

1602nationalConference on Mining Software Repositories, 2016, pp. 480483.

1603[30]V.Sinha, A. Lazar, B. Sahrif, Analyzing developer sentiment in commit logs, in:

1604ProceedingsoftheInternational Conference on

16052016,pp. 520523.

1606[31]SentiStregth-SE, Sentiment

1607[http://laser.cs.uno.edu/Projects/Projects.html](http://laser.cs.uno.edu/Projects/Projects.html),

1608[32]M.Islam, M. Zibran, Leveraging automated sentiment analysis in software engi-

1609neering,in: Proceedings of the Mining Software Repositories, 2017, pp. 203214.

1610[33]GoldStandardDataset

1611[http://ansymore.uantwerpen.be/system/les/uploads/artefacts/alessandro/](http://ansymore.uantwerpen.be/system/les/uploads/artefacts/alessandro/)

1612MSR16/archive3.zip,last access: June 2018.

1613[34]R.Jongeling, P. Sarkar, S. Datta, A. Serebrenik, On negative results when using

1614sentimentanalysis tools for software engineering research, Empirical Software

1615Engineering(2017) 142.

1616[35]N.Godbole, M. Srinivasaiah, S. Skiena, Large-scale sentiment analysis for news

1617and blogs, in: Procceding of the First International AAAI Conference on Weblogs

1618and Social Media, 2007.

1619[36]M.Hu, B.Liu, Mining and summarizing customer reviews, in: Proceedings

1620the International Conference on Knowledge Discovery and Data Mining, 2004,

1621pp. 168177.

1622[37]G.Qiu, B. Liu, J. Bu, C. Chen, Expanding domain sentiment lexicon through dou-

# ACCEPTED MANUSCRIPT

Analysis

Labeled

72

Mining Software Repositories,

Tool,freely

last access: June 2018.

withManually

available

Annotated

for

Emotions,

download,

of


---

<!-- Página 74 -->

### ACCEPTED MANUSCRIPT

1623ble propagation., in: Proceedings of the International Jont Conference on Artical

1624Intelligence,2009, pp. 11991204.

1625[38]StanfordCoreNLP, Stanford

1626[http://stanfordnlp.github.io/CoreNLP/sentiment.html](http://stanfordnlp.github.io/CoreNLP/sentiment.html),

1627[39]M.Islam, M. Zibran, A comparison of dictionary building methods for sentiment

1628analysisin software engineering text, in: Proceedings of the ACM/IEEE Interna-

1629tionalSymposium on Empirical Software Engineering and Measurement, 2017,

1630pp. 478479.

1631[40]F.Nielsen, Anew ANEW: Evaluation of

1632microblogs,in: Proceedings of the ESWC 2011 Workshop on 'Making Sense of

1633Microposts',2011, pp. 9398.

1634[41]T.Wilson, J. Wiebe, P. Homann., Recognizing contextual polarity: An

1635rationof features for phrase-level sentiment analysis, Journal of Computational

1636Linguistics35 (3) (2009) 399433.

1637[42]C.Hutto, E. Gilbert, Vader: A parsimonious rule-based model for sentiment anal-

1638ysisof social media text, in: Proceedings of the

1639nationalAAAI Conference on Weblogs and Social Media, 2014, pp. 216225.

1640[43]E.Rilo, A. Qadir, P. Surve, L. Silva, N. Gilbert, R. Huang, Sarcasm as contrast

1641betweena positive sentiment and negative situation, in: Proceedings of the Confer-

1642enceon Empirical Methods in Natural Language Processing, 2013, pp. 704714.

1643[44]Q.Gan, Y. Yu, Restaurant rating: Industrial

1644miningand multi-dimensional sentiment analysis, in: Proceedings of the Hawaii

1645InternationalConference on System Sciences, 2015, pp. 13321340.

1646[45]F.Koto, M. Adriani, A comparative study on twitter sentiment analysis: Which

1647featuresare good?, in: Proceedings of the International Conference on Applica-

1648tionsof Natural Language to Information Systems, 2015, pp. 453457.

1649[46]J.Fleiss, Measuring nominal scale agreement among many raters, Psychological

# ACCEPTED MANUSCRIPT

Core

73

NLPSentiment

aword list for sentiment analysis in

standard and word-of-mouth a text

last access: June 2018.

Annotator,

of the Eighth Inter-

explo-


---

<!-- Página 75 -->

### ACCEPTED MANUSCRIPT

1650bulletin76 (5) (1971) 378.

1651[47]N.Bettenburg, B. Adams, A. Hassan, A lightweight approach to uncover technical

1652informationin unstructured data, in: Proceedings of the International Conference

1653of Program Comprehension, 2011, pp. 185188.

1654[48]Jazzy-The Java Open Source Spell Checker, [http://jazzy.sourceforge.net](http://jazzy.sourceforge.net),

1655cess:June 2018.

1656[49]T.Dietterich, Approximate statistical tests for comparing supervised classication

1657learningalgorithms, Journal of Neural Computation 10 (7) (1998) 18951923.

1658[50]M.Rahman, C. Roy, I. Keivanloo, Recommending insightful comments for source

1659codeusing crowdsourced knowledge, in: Proceedings of the International Work-

1660ing Conference on Source Code Analysis and Manipulation, 2015, pp. 8190.

1661[51]V.Sinha, Sentiment analysis on java source code in large sofyware repositories,

1662Master'sthesis, Youngstown State University, USA (2016).

1663[52]R.Socher, A.Perelygin, J.

1664cursivedeepmodels for

1665in: Conference on Empirical Methods in Natural Language Processing, 2013, pp.

166616311642.

1667[53]SentiStregth-SE, Automatic Domain Independent Tool for Sentiment Analysis,

1668[http://sentistrength.wlv.ac.uk](http://sentistrength.wlv.ac.uk),

1669[54]F.Calefato, F. Lanubile, F. Maiorano, N. Novielli, Sentiment polarity detection

1670forsoftware development, Empirical Software Engineering (2017) 3521382.

1671[55]N.Novielli, F. Calefato, F. Lanubile, A gold standard for emotion annotation in

1672stackoverow, in: Proceedings of the International Conference on Mining Soft-

1673wareRepositories, 2018, pp. 1417.

1674[56]S.Baccianella, A. Esuli, F. Sebastiani, Sentiwordnet 3.0: An enhanced lexical re-

1675sourcefor sentiment analysis and opinion mining, in: Procceding of the Interna-

1676tionalConference on Language Resources and Evaluation, 2010, pp. 22002204.

# ACCEPTED MANUSCRIPT

semantic compositionality over a

Wu, ,

last access: May 2018.

74

J.Chuang, C.Manning, A.

sentiment treebank,

Ng, C.

last ac-

Potts, Re-


---

<!-- Página 76 -->

### ACCEPTED MANUSCRIPT

1677[57]M.G. L. Gatti, M. Turchi, Sentiwords: Deriving

1678eragelexicon for sentiment analysis, IEEE Transactions on Aective Computing

16797 (4) (2016) 409421.

1680[58]A.Warriner, V. Kuperman, M. Brysbaert, Norms of valence, arousal, and domi-

1681nancefor 13,915 english lemmas, Behavior research methods 45 (4) (2013) 1191

16821207.

1683[59]M.Mäntylä, N. Novielli, F. Lanubile, M. Claes, M. Kuutila, Bootstrapping a lex-

1684iconfor emotional arousal in software engineering, in: Proceedings of the Inter-

1685nationalConference on Mining Software Repositories, 2017, pp. 15.

1686[60]M.Islam, M.Zibran, deva: Sensing

1687softwareengineering tex, in: proceedings of the 33rd ACM/SIGAPP Symposium

1688On Applied Computing (SAC), 2018, pp. 1536 1543.

1689[61]T.Ahmed, A. Bosu, A. Iqbal, S. Rahimi, Senticr: a customized sentiment analysis

1690toolfor code review interactions, in: Proceedings of the 32nd IEEE/ACM Inter-

1691nationalConference on Automated Software Engineering, 2017, pp. 106111.

1692[62]C.Blaz, K. Becker, Sentiment analysis in tickets for it support, in: Proceedings

1693of the International Conference on Mining Software Repositories, 2016, pp. 235

1694246.

1695[63]A.Rousinopoulos, G. Robles, J. Barahona, Sentiment analysis of free/open source

1696developers:preliminary ndings from a case study, Revista Eletronica de Sistemas

1697de Informacao 13 (2) (2014) 121.

1698[64]E.Dragut, C. Yu, P. Sistla, W. Meng, Construction of a sentimental word dictio-

1699nary,in: Proceedings of the International Conference on Information and Knowl-

1700edgeManagement, 2010, pp. 17611764.

1701[65]L.Passaro, L. Pollacci, A. Lenci, Item: A vector space model to bootstrap an ital-

1702ian emotive lexicon, in: Proceedings of the Second Italian Conference on Com-

1703putationalLinguistics CLiC-it, 2015, pp. 215220.

# ACCEPTED MANUSCRIPT

75

emotions in

a high precision and high cov-

thevalence arousal space in


---

<!-- Página 77 -->

### ACCEPTED MANUSCRIPT

1704[66]M.Host, B. Regnell, C. Wohlin, Using students as subjects: A

1705of students and professionals in lead-time impact assessment, Empirical Software

1706Engineering5 (3).

1707[67]S.Panichella, A. Sorbo, E. Guzman, C. Visaggio, G. Canfora, H. Gall, How can i

1708improvemy app? Classifying user reviews for software maintenance and evolutio,

1709in: Proceedings of the IEEE International Conference on Software Maintenance

1710and Evolution, 2015, pp. 281290.

1711[68]N.Prollochs, S. Feuerriegel, D. Neumann, Detecting negation scopes for nan-

1712cialnews sentiment using reinforcement learning, in: Proceedings of the Hawaii

1713InternationalConference on System Sciences, 2016, pp. 11641173.

1714[69]A.Asmi, T. Ishaya, Negation identication and calculation in sentiment analysis,

1715in: Proceedings of the Second International Conference on Advances in Informa-

1716tionMining and Management, 2012, pp. 17.

1717[70]R.Morante, A. Liekens, W. Daelemans, Learning the scope of negation in biomed-

1718icaltexts, in:Proceedings

1719LanguageProcessing, 2008, pp. 715724.

1720[71]L.Jia, C.Yu, ,W. Meng, The

1721trievaleectiveness, in: Proceedings of the ACM Conference on Information and

1722KnowledgeManagement, 2009, pp. 18271830.

1723[72]Y.Choi, C.Cardie, Learning with compositional semantics as

1724encefor subsentential sentiment analysis, in: Proceedings of the Conference on

1725EmpiricalMethods in Natural Language Processing, 2008, pp. 793801.

1726[73]B.Panga, L.Lee,S.Vaithyanathan, Thumbs

1727ing machine learning techniques, in: Proceedings of the Conference on Empirical

1728Methodsin Natural Language Processing, 2002, pp. 7986.

1729[74]A.Kennedy, D.Inkpen, Sentiment classication of

1730usingcontextual valence shifters, Computational Intelligence 22 (2) (2006) 110

1731125.

# ACCEPTED MANUSCRIPT

oftheConference on

eect of

76

negation on

up?

Empirical Methods in

sentiment analysis and re-

Sentiment

movie and product reviews

comparative study

structural infer-

classication us-

Natural


---

<!-- Página 78 -->

### ACCEPTED MANUSCRIPT

1732[75]S.Wu, T. Miller, J. Masanz, M. Coarr, S. Halgrim, D. Carrell, C. Clark, Negation's

1733not solved: Generalizability versus optimizability in clinical natura, PLoS ONE

17349 (11) (2014) e112774.

1735[76]A.Bacchelli, A. Cleve, M. Lanza, A. Mocci, Extracting structured data from nat-

1736urallanguage documents with island parsing, in: Proceeding of the International

1737Conferenceon Automated Software Engineering, 2011, pp. 476479.

1738[77]A.Reyes, P. Rosso, D. Buscaldi, From humor recognition to irony detection: The

1739gurativelanguage of social media, Data and Knowledge Engineering 74 (2012)

1740112.

1741[78]A.Balahur, J. Hermida, A. Montoyo, Detecting implicit expressions of sentiment

1742in text based on commonsense knowledge, in: Proceedings of the Workshop on

1743ComputationalApproaches to Subjectivity and Sentiment Analysis, 2011, pp. 53

174460.

1745[79]AlchemyLanguage: Natural

1746ysis,[http://www.alchemyapi.com/products/alchemylanguage/sentiment-analysis](http://www.alchemyapi.com/products/alchemylanguage/sentiment-analysis),

1747lastaccess: June 2018.

1748[80]E.Guzman, Visualizing emotions in software development projects, in: Proceed-

1749ingsof the Conference on Software Visualization, 2013, pp. 14.

1750[81]M.Ortu, G. Destefanis, S. Counsell, S. Swift, R. Tonelli, M. Marchesi, Arsonists

1751or reghters? Aectiveness in agile software development, in: Proceedings of

1752the International Conference on Extreme Programming, 2016, pp. 144155.

1753[82]E.Guzman, W. Maalej, How do users like this feature? A

1754analysisof app reviews, in: Proceedings of the International Requirements Engi-

1755neeringConference, 2014, pp. 153  162.

1756[83]J.Jiarpakdee, A.Ihara, K.

1757aectiveaspect in Q&A site, in: Proceedings of the International Workshop on

1758EmotionAwareness in Software Engineering, 2016, pp. 1217.

# ACCEPTED MANUSCRIPT

language

Matsumoto, Understanding question quality through

77

processingforadvanced

ne grained sentiment

textanal-


---

<!-- Página 79 -->

1759[84]M.Choudhury, M. Gamon, S. Counts, Happy, nervous or surprised? Classica-

1760tionof human aective states in social media, in: Proceedings of the International

1761AAAIConference on Weblogs and Social Media, 2012, pp. 435438.

1762[85]A.Muhammad, N. Wiratunga, R. Lothian, R. Glassey, Domain-based lexicon en-

1763hancementfor sentiment analysis, in: Proceedings of the SGAI International Con-

1764ferenceon Articial Intelligence, 2013.

1765[86]A.Murgia, M. Ortu, P. Tourani, B. Adams, An exploratory qualitative and quan-

1766titativeanalysis of

1767EmpiricalSoftware Engineering (2017) 144.

1768[87]StackExchange Data

1769cess:June 2018.

1770[88]F.Calefato, F. Lanubile, N. Novielli, EmoTxt: A

1771fromtext, in: Proceedings of the Aective Computing and Intelligent Interaction,

17722017.

1773[89]J.Ding, H. Sun, X. Wang, X. Liu, Entity-level sentiment analysis of issue com-

1774ments,in: Proceeding of the Third International Workshop on Emotion Awareness

1775in Software Engineering, 2018.

1776[90]M.Islam, M. Zibran, A comparison of software engineering domain specic sen-

1777timentanalysis tools, in:

1778Evolutionand Reengineering, 2018, pp. 487491.

1779[91]N.Novielli, D. Girardi, F. Lanubile, A benchmark study on sentiment analysis for

1780softwareengineering research, in: Proceedings of the International Conference on

1781MiningSoftware Repositories, 2018, pp. 799808.

# ACCEPTED MANUSCRIPT

### ACCEPTED MANUSCRIPT

emotions in

Dump,

issue report comments of

[https://archive.org/details/stackexchange](https://archive.org/details/stackexchange),

IEEEInternational Conference on Software Analysis,

78

toolkit for emotion recognition

open source systems,

lastac-


---

