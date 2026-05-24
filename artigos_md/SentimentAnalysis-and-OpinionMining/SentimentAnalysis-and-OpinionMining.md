<!-- Página 1 -->

#

# Sentiment Analysis and

# Opinion Mining

## Draft :

Bing Liu. Sentiment Analysis and Opinion Mining , Morgan &Claypool Publishers, May 2012.

###

*Due to copyediting, the publis hed version is slightly different*

**April 22, 2012**

## Bing Liu

## liub@cs.uic.edu


---

<!-- Página 2 -->

Sentiment Analysis and Opinion Mining

2

### Table of Contents

Preface ..............................................................................................5

Sentiment Analysis: A Fascinating Problem...................................7

1.1Sentiment Analysis Applications ..........................................8

1.2Sentiment Analysis Research ..............................................10 1.2.1Different Levels of Analysis ......................................................... 10 1.2.2Sentiment Lexicon an d Its Issues ................................................. 12 1.2.3Natural Language Pro cessing Issues............................................. 13

1.3Opinion Spam Detection .....................................................14

1.4What’s Ahead ......................................................................14

The Problem of Sentiment Analysis ..............................................16

2.1Problem Definitions ............................................................17 2.1.1Opinion Defintion ......................................................................... 17 2.1.2Sentiment Analys is Tasks............................................................. 21

2.2Opinion Summarization ......................................................24

2.3Different Types of Opinions ................................................25 2.3.1Regular and Compara tive Opinions.............................................. 25 2.3.2Explicit and Implic it Opinions...................................................... 26

2.4Subjectivity and Emotion ....................................................27

2.5Author and Reader Standing Point ......................................29

2.6Summary .............................................................................29

Document Sentiment Classification ...............................................30

3.1Sentiment Classification Using Supervised Learning .........31

3.2Sentiment Classification Using Unsupervised Learning .....34

3.3Sentiment Rating Prediction ................................................36

3.4Cross-Domain Sentiment Classification .............................38

3.5Cross-Language Sentiment Classification ...........................41

3.6Summary .............................................................................43

Sentence Subjectivity and Se ntiment Classification ......................44


---

<!-- Página 3 -->

Sentiment Analysis and Opinion Mining

4.1Subectivity Classification ....................................................45

4.2Sentence Sentiment Classification ......................................49 3 4.3Dealing with Conditional Sentences...................................51

4.4Dealing with Sarcastic Sentences ........................................52

4.5Cross-language Subjectivity a nd Sentiment Classification.53

4.6Using Discourse Information for Sentiment Classification55

4.7Summary .............................................................................56

Aspect-based Sentiment Analysis ..................................................58

5.1Aspect Sentiment Classification ..........................................59

5.2Basic Rules of Opinions and Compositional Semantics.....62

5.3Aspect Extraction ................................................................67 5.3.1Finding Frequent Nouns and Noun Phrases.................................. 68 5.3.2Using Opinion and Ta rget Relations............................................ 71 5.3.3Using Supervised Learning........................................................... 71 5.3.4Using Topic Models..................................................................... 73 5.3.5Mapping Implicit Aspects............................................................ 77

5.4Identifying Resource Usage Aspect ....................................78

5.5Simutaneous Opinion Lexicon Expansion and AspectExtraction ............................................................................79

5.6Grouping Aspects into Categories .......................................81

5.7Entity, Opinion Holder and Time Extraction ......................84

5.8Coreference Resolution and Wo rd Sense Disambiguation .86

5.9Summary .............................................................................88

Sentiment Lexicon Generation ......................................................90

6.1Dictionary-based Approach .................................................91

6.2Corpus-based Approach ......................................................95

6.3Desirable and Undesirable Facts .........................................99

6.4Summary ...........................................................................100

Opinion Summarization ...............................................................102

7.1Aspect-based Opinion Summarization ..............................102

7.2Improvements to Aspect-based Opinion Summarization ..105

7.3Contrastive View Summarization .....................................107

7.4Traditional Summarization ................................................108

7.5Summary ...........................................................................108


---

<!-- Página 4 -->

Sentiment Analysis and Opinion Mining

Analysis of Comparative Opinions ..............................................110

8.1Problem Definitions ..........................................................110 4 8.2Identify Comparative Sentences ........................................113

8.3Identifying Preferred Entities ............................................115

8.4Summary ...........................................................................117

Opinion Search and Retrieval ......................................................118

9.1Web Search vs. Opinion Search ........................................118

9.2Existing Opinion Retrieval Techniques ............................119

9.3Summary ...........................................................................122

Opinion Spam Detection ..............................................................123

10.1Types of Spam and Spamming ..........................................124 10.1.1Harmful Fake Reviews............................................................... 125 10.1.2Individual and Grou p Spamming ................................................ 125 10.1.3Types of Data, Features and Detec tion ....................................... 126

10.2Supervised Spam Detection ...............................................127

10.3Unsupervised Spam Detection ..........................................130 10.3.1SpamDetection based on Atypical Beha viors ............................ 130 10.3.2Spam Detection Using Review Graph ........................................ 133

10.4Group Spam Detection ......................................................134

10.5Summary ...........................................................................135

Quality of Reviews......................................................................136

11.1Quality as Regression Problem .........................................136

11.2Other Methods ...................................................................138

11.3Summary ...........................................................................140

Concluding Remarks ....................................................................141

Bibliography ................................................................................143


---

<!-- Página 5 -->

## Preface

Opinions are central to almost all human activities and are key influencers ofour behaviors. Our beliefs and perceptions of reality, and the choices wemake, are, to a considerable degree, conditioned upon how others see andevaluate the world. For this reason, when we need to make a decision weoften seek out the opinions of others. Th is is not only true for individuals butalso true for organizations.Opinions and its related concepts such as sentiments, evaluations, attitudes,and emotions are the subjects of studyof sentiment analysis and opinion*mining . The inception andrapid growth of the field coincide with those of*the social media on the Web, e.g., reviews, forum discussions, blogs, micro-blogs, Twitter, and social networks, because for the first time in humanhistory, we have a huge volume of opinionated data recorded indigitalforms. Since early 2000, sentiment analysis has grown to be one of the mostactive research areas in natural language processing. It is also widely studiedin data mining, Web mining, and textmining. In fact, it has spread fromcomputer science tomanagement sciences and social sciences due to itsimportance to business and society as a whole. In recent years, industrialactivities surrounding sentiment analysis have alsothrived. Numerousstartups have emerged. Many large corporations have built their own in-house capabilities. Sentiment analysis systems have found their applicationsin almost every business and social domain.The goal of this book is togive an in-depthintroduction to this fascinatingproblem and to present a comprehensive surveyof all important researchtopics and the latest developments in the field. As evidence of that, this bookcovers more than 400 references fro m all major conferences and journals.Although the field deals with the natural language text, which is oftenconsidered the unstructured data, this book takes a structured approach inintroducing the problemwith the aim of bridgingthe unstructured andstructured worlds and facilitatingqualitative and quantitative analysis ofopinions. This is crucial forpractical applications. In this book, I first definethe problem in order to provide an abstraction or structure to the problem.From the abstraction, we will naturally see its key sub-problems. Thesubsequent chapters discuss the existingtechniques for solving these sub-problems.This book is suitable for students, researchers, and practitioners who areinterested insocial media analysis in general and sentiment analysis inparticular. Lecturers can readily use it in class for courses on natural

Sentiment Analysis and Opinion Mining

5


---

<!-- Página 6 -->

Sentiment Analysis and Opinion Mining

language processing, socialmedia analysis, text mining, and data mining.Lecture slidesare also available online.

6 **Acknowledgements**

I would like to thank my former and current students—Zhiyuan Chen,Xiaowen Ding, Geli Fei, Murthy Ganapathibhotla, Minqing Hu, Nitin Jindal,Huayi Li, Arjun Mukherjee, Guang Qiu (visiting student from ZhejiangUniversity), William Underwood, Andrea Vaccari, Zhongwu Zhai (visitingstudent from Tsinghua University), and Lei Zhang—for contributingnumerous research ideas over the years. Discussions with many researchersalso helped shape the book: Malu G. Castellanos, Dennis Chong, UmeshDayal, Eduard Dragut, Riddhiman Ghosh, Natalie Glance, Meichun Hsu,Jing Jiang, Birgit König, Xiaoli Li, Tieyun Qian, Gang Xu, Philip S. Yu,Clement Yu, and ChengXiang Zhai. I am also very grateful to twoanonymous reviewers. Despite their busy schedules, they read the book verycarefully and gavememany excellent suggestions. I have taken each andevery one of theminto consideratio n while improving this book. On thepublication side, I thank the Editor, Dr. Graeme Hirst, and the President andCEO of Morgan & Claypool Publishers, Mr. Michael Morgan, who havemanaged toget everythingdone on time and provided me with many piecesof valuable advice. Finally, my greatestgratitude goes tomy own family:Yue, Shelley, and Kate, who have helped in so many ways.

##


---

<!-- Página 7 -->

### CHAPTER 1

## Sentiment Analysis: A Fascinating

## Problem

Sentiment analysis, also called opinion mining , is the field of study thatanalyzes people’s opinions, sentiments, evaluations, appraisals, attitudes,and emotions towards entities such as products, services, organizations,individuals, issues, events, topics, and their attributes. It represents a largeproblemspace. There are also many names and slightly different tasks, e.g.,*sentiment analysis ,*,,,*subjectivity analysis ,*,,, etc.However, they are now all under the umbrella of sentiment analysis oropinion mining. While in industry, the term sentiment analysis is morecommonly used, but in academia both sentiment analysis andare frequently employed. They basically represent the samefield of study.The term sentiment analysis perhaps first appeared in (Nasukawa and Yi,2003), and the term opinion mining first appeared in (Dave, Lawrence andPennock, 2003). However, the research on sentiments andappearedearlier (Das and Chen, 2001; Morinaga et al., 2002; Pang, Lee andVaithyanathan, 2002; Tong, 2001; Turney, 2002; Wiebe, 2000). In thisbook, weuse the terms sentiment analysis and opinion mininginterchangeably. To simplify the presentation, throughout this bookwe willuse the term opinion to denote opinion, sentiment, evaluation, appraisal,attitude, and emotion. However, these concepts are not equivalent. We willdistinguish them when needed. The meaning of opinion itself is still verybroad. Sentiment analysis and opinion mining mainly focuses on opinionswhich express or imply positive or negative sentiments.Althoughlinguistics and natural language processing (NLP) havea longhistory, little research had been done about people’s opinions and sentimentsbefore the year 2000. Sincethen, the field has become a very active researcharea. There are several reasons for this. First, ithas a wide arrange ofapplications, almost in every domain. The industry surrounding sentimentanalysis has also flourished due to the proliferation of commercialapplications. This provides a strong motivation for research. Second, itoffers many challenging research problems, which had never been studiedbefore. This book will systematically define and discuss these problems, anddescribe the current state-of-the-art techniques for solving them. Third, for

Sentiment Analysis and Opinion Mining

7


---

<!-- Página 8 -->

Sentiment Analysis and Opinion Mining

the first time in human history, we now have a huge volume of opinionateddata in the social media on the Web. Without this data, a lot of researchwould not have been possible. Not surprisingly, the inception and the rapidgrowth of sentiment analysis coincide w ith those of the social media. In fact,sentiment analysis is now right at the center of the social media research.Hence, research in sentiment analysis not only has an important impact onNLP, butmay also have a profound impact on management sciences,political science, economics, and social sciences as they are all affected bypeople’s opinions. Although the sentiment analysis research mainly startedfrom early 2000, there were some earlier work on interpretation ofmetaphors, sentiment adjectives, subjectivity, viewpoints, and affects(Hatzivassiloglou and McKeown, 1997; Hearst, 1992; Wiebe, 1990; Wiebe,1994; Wiebe, Bruce and O'Hara, 1999). This book serves as an up-to-dateand comprehensive introductory text, as well as a survey to the subject. 8

## 1.1

Opinions are central to almost all human activities because they are keyinfluencers of our behaviors. Whenever we need tomake a decision, wewant to know others’ opinions. In the real world, businesses andorganizationsalways want to findconsumer or public opinions about theirproducts andservices. Individual consumers also want toknow the opinionsof existing users of a product before purchasing it, and others’ opinionsabout political candidates before making a voting decision in a politicalelection. In the past, whenan individual needed opinions, he/sheaskedfriends and family. When an organization or a business needed public orconsumer opinions, it conducted surveys, opinion polls, and focus groups.Acquiring public and consumer opinionshas longbeena huge business itselffor marketing, public relations, and political campaign companies.With the explosive growth of social media (e.g., reviews, forum discussions,blogs, micro-blogs, Twitter, comments, and postings in social network sites)on the Web, individuals and organizations are increasingly using the contentin these media for decisionmaking. Nowadays, if one wants to buy aconsumer product, one is no longer limited to asking one’s friends andfamily for opinions because there are many user reviews and discussions inpublic forums on the Web about the product. For an organization, it may nolonger be necessary to conduct surveys, opinion polls, and focus groups inorder to gather public opinions because there is an abundance of suchinformation publicly available. However, finding andmonitoringopinionsites on the Web and distilling the information contained in them remains a


---

<!-- Página 9 -->

formidable task because of the proliferation of diverse sites. Each sitetypically contains a huge volume of opinion text that is not always easilydecipheredinlong blogs and forum pos tings. The average human reader willhave difficulty identifying relevant sites and extracting and summarizing theopinions in them. Automated sentiment analysis systems are thus needed.In recent years, we have witnessed that opinionatedpostings in socialmediahave helped reshape businesses, and sway public sentiments and emotions,which have profoundly impacted on our social and political systems. Suchpostings have also mobilized masses forhappened in some Arab countries in 2011. It has thus become a necessity tocollect and study opinions on the Web. Of course, opinionateddocumentsnot only exist on the Web (called external data), many organizations alsohave their internal data, e.g., custom er feedback collected from emails andcall centers or results from surveys conducted by the organizations.Due to these applications, industrial activities have flourished in recentyears. Sentiment analysis applications have spread to almost every possibledomain, from consumer products, services, healthcare, and financial servicesto social events and political elections. I myself have implemented asentiment analysis system called Opinion Parser , and worked on projects inall these areas in a start-up company. There have been at least 40-60 start-upcompanies inthe space in the USA alon e. Many big corporations have alsobuilt their own in-house capabilities, e.g., Microsoft, Google, Hewlett-Packard, SAP, and SAS. These practical applications and industrial interestshave provided strong motivations for research in sentiment analysis.Apart fromreal-life applications, many application-oriented research papershave also been published. For example, in (Liu et al., 2007), a sentimentmodel was proposed to predict sales performance. In (McGlohon, Glanceand Reiter, 2010), reviews were used to rank products and merchants. In(Hong and Skiena, 2010), the relationships between the NFL betting line andpublic opinions in blogs and Twitter were studied. In (O'Connor et al.,2010), Twitter sentiment was linked with public opinion polls. In (Tumasjanet al., 2010), Twitter sentiment was also applied to predict election results.In (Chen et al., 2010), the authors studied political standpoints.

Sentiment Analysis and Opinion Mining

9

Smith, 2010), a method was reported for predicting comment volumes ofpoliticalblogs. In (Asur and Huberman, 2010; Joshi et al., 2010; Sadikov,Parameswaran and Venetis, 2009), Twitter data, movie reviews and blogswere used to predict box-office revenues for movies. In (Miller et al., 2011),sentiment flow in social networks was investigated. In (Mohammad andYang, 2011), sentiments inmails were used to find how genders differed onemotional axes. In (Mohammad, 2011), emotions in novels and fairy taleswere tracked. In (Bollen, Mao and Zeng, 2011), Twittermoods were used to In (Yano and


---

<!-- Página 10 -->

Sentiment Analysis and Opinion Mining

predict the stock market. In (Bar-Haimet al., 2011; Feldman et al., 2011),expert investors in microblogs were identified and sentiment analysis ofstocks was performed.

10

## 1.2

As discussed above, pervasive real-life applications are only partof thereason why sentiment analysis is a popular research problem. It is alsohighly challenging as a NLP research topic, and covers many novel sub-problems as we will see later. Additionally, there was little research beforethe year 2000 in either NLP or in linguist ics. Part of the reason is that beforethen there was little opinion text available indigital forms. Since the year2000, the field has grown rapidly to become one of themost active researchareas in NLP. It is also widely researched in data mining, Web mining, andinformation retrieval. In fact, it has spread from computer science tomanagement sciences (Archak, Ghose and Ipeirotis, 2007; Chen and Xie,2008; Das and Chen, 2007; Dellarocas, Zhang and Awad, 2007; Ghose,Ipeirotis and Sundararajan, 2007; Hu, Pavlou and Zhang, 2006; Park, Leeand Han, 2007).

### 1.2.1 Different Levels of Analysis

I now give a brief introduction to the main research problems based on thelevel of granularities of the existing research. In general, sentiment analysishas been investigated mainly at three levels:**Document level: The task at this level is to classifywhether a whole opinion**document expresses a positive or negative sentiment (Pang, Lee andVaithyanathan, 2002; Turney, 2002). For example, given a productreview, the system determines whether the review expresses an overallpositive or negative opinion about the product. This task is commonly

In (Zhang and Skiena, 2010), blogand newssentiment was used to study trading strategies. In (Sakunkoo and Sakunkoo,2009), social influences inonline book reviews were studied. In (Groh andHauffa, 2011), sentiment analysis was used to characterize social relations.A comprehensive sentiment analysis syst em and some case studies were alsoreported in (Castellanos et al., 2011). My own group has tracked opinionsabout movies on Twitter and predicted box-office revenues with veryaccurate results. We simply used our Opinion Parser system to analyzepositive and negative opinions about each movie with no additionalalgorithms.


---

<!-- Página 11 -->

known as document-level sentiment classification . This level of analysisassumes that each document expresses opinions on a single entity (e.g., asingle product). Thus, it is not applicable to documents which evaluate orcompare multiple entities.**Sentence level: The taskat this level goesto thesentences and determines**whether each sentence expressed a positive, negative, or neutral opinion.Neutral usuallymeans no opinion.to(Wiebe, Bruce and O'Hara, 1999), whichdistinguishes sentences (called objective sentences ) that express factualinformation from sentences (called subjective sentences) that expresssubjective views and opinions. However, we should note that subjectivityis not equivalent to sentiment as many objective sentences can implyopinions, e.g., “ We bought the car last month and the windshield wiper*has fallen off .” Researchers have also analyzed clauses (Wilson, Wiebe*and Hwa, 2004), but the clause level is still not enough, e.g., “Apple is*doing very well inthis lousy economy .”***Entity and Aspect level: Boththe document level and the sentence level**analyses do not discover what exactlypeople liked and did not like.Aspect level performs finer-grained analysis. Aspect level was earliercalled feature level ()(Hu and Liu, 2004). Instead oflooking at language constructs(documents, paragraphs, sentences, clauses or phrases), aspect leveldirectly looksat the opinion itself. Itis based on the idea that an opinionconsists of a sentiment (positive or negative) and a target (of opinion).An opinion without its target being identified is of limited use. Realizingthe importance of opinion targets also helps us understand the sentimentanalysis problem better. For example, although the sentence “although*the service is not that great, I still love this restaurant” clearly has a*positive tone, we cannot say that this sentence is entirely positive. In fact,the sentence is positive about the restaurant (emphasized), but negativeabout its service (not emphasized). In many applications, opinion targetsare described by entities and/or their different aspects. Thus, the goal ofthis level of analysis is to discover sentiments on entities and/or theiraspects. For example, the sentence “ The iPhone’s call quality is good, but*its battery life is short ” evaluatestwo aspects, call quality and battery**life iPhone (entity). Thesentiment on iPhone’s call qualityis positive,*but the sentiment on its battery life is negative. Thecall quality andof iPhone are the opinion targets. Based on this level ofanalysis, astructuredsummary of opinions about entities and theiraspects can be produced, which turns unstructured text to structured dataand can be used for all kinds of qualitative and quantitative analyses.Both the document level and sentence level classifications are already

Sentiment Analysis and Opinion Mining

11


---

<!-- Página 12 -->

Sentiment Analysis and Opinion Mining

highly challenging. The aspect-level is even more difficult. It consists ofseveral sub-problems, which we will discuss in Chapters 2 and 5.To make things even more interesting and challenging, there are two typesof opinions, i.e., regular opinions and2006b) .or an aspect of the entity, e.g., “ Coke tastes very good,” which expresses apositive sentiment on the aspect tastecompares multiple entities based on some of their shared aspects, e.g., “Coke*tastes better than Pepsi ,” whichcompares Coke and Pepsi based ontheir*tastes (an aspect) and expresses a pr eference for Coke (see Chapter 8). 12

### 1.2.2 Sentiment Lexicon and Its Issues

Not surprisingly, the most importa nt indicators of sentiments are sentiment*words , also called opinion words . These are words that are commonly used*to express positive or negative sentiments. For example, good,,andare positive sentiment words, and bad poorterrible arenegative sentiment words. Apart from individual words, there are alsophrases and idioms, e.g., cost someone an arm and a leg. Sentiment wordsand phrases are instrumental to sentiment analysis for obvious reasons. A listof such words and phrases is called a sentiment lexicon (or).Over the years, researchers have de signed numerous algorithms to compilesuch lexicons. We will discuss these algorithms in Chapter 6.Although sentiment words and phrases are important for sentiment analysis,only using them is far fromsufficient. The problem is much more complex.In other words, we can say that sentiment lexicon is necessary but notsufficient for sentiment analysis. Below, we highlight several issues:1.different application domains. For example, “suck” usuallyindicatesnegative sentiment, e.g., “ This camerasucks ,” but it can also implypositive sentiment, e.g., “ This vacuum cleaner really sucks.”2.This phenomenon happens frequently in several types of sentences.Question (interrogative) sentences and conditional sentences are twoimportant types, e.g., “ Can you tell me whichSony camerais good?”and “ If I can find a good camera in the shop, I will buy it.” Both thesesentences contain the sentiment word “ good ”, but neither expressesapositive or negative opinion on any specific camera. However, not allconditional sentences or interrogative sentences express no sentiments,e.g., “ Does anyone knowhow to repair this terrible printer” and “If you


---

<!-- Página 13 -->

*are looking for a good car, get Toyota .” We will discuss such*sentences in Chapter 4.3.with, e.g., “ What a great car! It stopped working in two days.” Sarcasmsare not so common in consumer revi ews about products and services,but are very common in political discussions, which make politicalopinions hardto deal with. We will discuss such sentences in Chapter 4.4.Many of these sentences areactually ob jective sentences that are usedtoexpress some factual information. Ag ain, there are many types of suchsentences. Here we just give two examples. The sentence “This washer*uses a lot of water ” implies a negative sentiment about the washer since*it uses a lot of resource (water). The sentence “ After sleeping on the*mattress for two days, a valley has formed inthe middle” expresses a*negative opinion about themattress. This sentence is objective as itstates a fact. All these sentences have no sentiment words.These issues all present major challenges . In fact, these are just some of thedifficult problems. More will be discussed in Chapter 5.

### 1.2.3 Natural Language Processing Issues

Finally, we must not forget sentiment analysis is a NLP problem. It touchesevery aspectof NLP, e.g., coreference resolution, negation handling, andword sense disambiguation, which add more difficulties since these are notsolved problems in NLP. However, it is also useful to realize that sentimentanalysis is a highly restricted NLP problem because the system does notneed to fully understand the semantics of each sentence or document butonlyneeds to understand some aspects of it, i.e., positive or negativesentiments and their target entities or topics. In this sense, sentiment analysisoffers a great platform for NLP researchers to make tangible progresses onall fronts of NLP with the potential of making a huge practical impact. Inthis book, I will describe the core problems and the current state-of-the-artalgorithms. I hope to use this book to attract researchers from other areas ofNLP to join force to make a concer ted effort to solve the problem.Prior to this book, there were amulti-author volume*and Affect in Text: Theory and Applications ” edited by*Wiebe (2006), and also a survey article/book by Pang and Lee (2008). Bothbooks have excellent contents. However, theywere published relativelyearly in the development of the field. Since then, there have been significantadvancements due to much more activ e researchin the past 5 years.

Sentiment Analysis and Opinion Mining

13


---

<!-- Página 14 -->

Sentiment Analysis and Opinion Mining

Researchers now also have a much better understanding of the wholespectrum of the problem, its structure, and core issues. Numerous new(formal) models and methods have been proposed. The research has not onlydeepened but also broadened signifi cantly. Earlier research in the fieldmainly focused on classifying the sentiment or subjectivity expressed indocuments or sentences, which is insufficient for most real-life applications.Practical applications often demand more in-depth and fine-grained analysis.Due to the maturityof the field, thebook is also written in a structured formin the sense that the problem is now better defined and different researchdirections are unifiedaroundthe definition. 14

## 1.3

A key feature of socialmedia is that it enables anyone from anywhere in theworld to freely express his/her views and opinions without disclosing his/hertrue identify and without the fear of undesirable consequences. Theseopinions are thus highly valuable. However, this anonymity also comes witha price. It allows people with hidden agendas or malicious intentions toeasily game the system to give people the impression that they areindependent members of the public andpost fake opinions to promote or todiscredit target products, services, organizations, or individuals withoutdisclosing their true intentions, or th e person or organization that they aresecretly working for. Such individuals are called opinion spammers and theiractivities are called opinion spamming (Jindal and Liu, 2008; Jindal and Liu,2007).Opinion spamming has become a major issue. Apart from individuals whogive fake opinions in reviews and forum discussions, there are alsocommercial companies that are in the business of writing fake reviews andbogus blogs for their clients. Several high profile cases of fake reviews havebeen reported in the news. It is important to detect such spamming activitiesto ensure that the opinions on the Web are a trusted source of valuableinformation. Unlike extraction of positive and negative opinions, opinionspam detection is not just a NLP probl em as it involves the analysis ofpeople’s posting behaviors. It is thus alsoa data miningproblem. Chapter 10will discuss the current state-of-the-art detection techniques.

## 1.4

In this book, we explore this fascinating topic. Although the book deals with


---

<!-- Página 15 -->

the natural language text, which is often called unstructured data, I take astructured approachto writing this book. The next chapter will formallydefine the problem, which allows us to see a structure of the problem. Fromthe definition, we will see the key tasks of sentiment analysis. In thesubsequent chapters, existing techniques for performing the tasks aredescribed. Due to my research, consulting, and start-up experiences, thebook not only discusses key research concepts but also looks at thetechnology from an application point of view in order to help practitioners inthe field. However, I must apologize that when I talk about industrialsystems, I cannot reveal the names of companies or their systems, partiallybecause of my consulting/business agre ements and partially because of thefact thatthe sentiment analysis market moves rapidly and the companies thatI know of may have changed or improved their algorithms when you readthis book. I do not want to create problems for them and for me.Although I try to cover allmajor ideas and techniques in this book, it hasbecome an impossible task. In the past decade, a huge number of researchpapers (probably more than 1000) have been publishedonthe topic.Althoughmost papers appeared in NLP conferences and journals, manypapers have also been published in data mining, Web mining, machinelearning, information retrieval, e-commerce, management sciences, andmany other fields. It is thus almost impossible to write a book that covers theideas in every published paper. I am sorry if your good ideas or techniquesare overlooked. However, amajor advantage of publishing this bookin thesynthesis lecture series of Morgan & Claypool is that the authors can alwaysadd new or updated materials to the book because the printing is on demand.So if you find that some important ideas are not discussed, please do nothesitate to let me know and I will be very happy to include.Finally, background knowledge in the following areas will be very helpful inreading this book: natural language processing (Indurkhya and Damerau,2010; Manning and Schutze, 1999), machine learning(Bishop, 2006;Mitchell, 1997), datamining (Liu, 2006 and 2011), and information retrieval(Manning, Raghavan and Schutze, 2008).

Sentiment Analysis and Opinion Mining

15


---

<!-- Página 16 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 2

16

## The Problem of Sentiment Analysis

In this chapter, we define an abstraction of the sentiment analysis or opinionmining problem. From a research point of view, this abstraction gives us astatement of the problem and enables us to see a rich set of inter-related sub-problemswhich make up the sentiment analysis problem. It is often said thatif we cannot structure a problem, we probably do not understand theproblem. The objective of the definitions is thus to abstract astructure fromthe complex and intimidating unstructured natural language text. They alsoserve as a common framework tounify various existing researchdirections,and to enable researchers to design more robust and accurate solutiontechniques by expl oiting the inter-rela tionships of the sub-problems. From apracticalapplication point of view, thedefinitions let practitioners see whatsub-problemsneed to be solved in a practical system, how they are related,and what output should be produced.Unlike factual information, opinions and sentiments have an importantcharacteristic, namely, they are subjective. It is thus important to examine acollection of opinions frommany people rather than only a single opinionfrom one person because such anopinion represents only the subjective viewof that single person, which is usually not sufficient for application. Due to alarge collection of opinions on the Web, some form of summary of opinionsis needed (Hu and Liu, 2004). The problem definitions state whatkind ofsummarymay be desired. Along with the problem definitions, the chapterwill also discuss several related concepts such as subjectivity and emotion.Note that throughout this chapter and also the whole book, I mainly usereviews and sentences from reviews as examples to introduce ideas and todefinekey concepts, but the ideas and the resulting definitions are generaland applicable to all forms of formal and informal opinion text suchas newsarticles, tweets (Twitter postings), fo rum discussions, blogs, and Facebookpostings. Since product reviews are highly focused and opinion rich, theyallow us to see different issues mo re clearly than from other forms ofopinion text. Conceptually, there is no difference between them. Thedifferences are mainly superficial and in thedegreeof difficulty in dealingwith them. For example, Twitter postings (tweets) are short (at most 140characters) and informal, and use many Internet slangs and emoticons.Twitter postings are, in fact, easier to analyze due to the length limit because


---

<!-- Página 17 -->

the authors are usually straight to the point. Thus, it is often easier to achievehigh sentiment analysis accuracy. Revi ews are also easier because they arehighly focused with little irrelevant information. Forum discussions areperhaps thehardest to deal with becausethe users there can discuss anythingand alsointeract with one another. In terms of the degree of difficulty, thereis also the dimension of different application domains. Opinions aboutproducts and services are usuallyeasie r to analyze. Social andpoliticaldiscussions are much harder due to complex topic and sentimentexpressions, sarcasms and ironies.

## 2.1

As mentioned at the beginning of Chapter 1, sentiment analysis mainlystudies opinions which express or imply positive or negative sentiments.This section thus defines the problem in this context.

### 2.1.1 Opinion Defintion

We use the following review about a Canon camera to introduce the problem(an id number is associatedwith each sentence for easy reference):Posted by: John Smith“(1). (2) I simply love*it Thepicture quality is amazing . (4)*.(5).”From this review, we notice a few important points:1.Canon G12 camera. Sentence (2) expresses a positive opinion about theCanon camera as a whole. Sentence (3) expresses a positive opinionabout its picture equality. Sentence (4) expresses a positive opinionabout its battery life. Sentence (5) expresses a negative opinion aboutthe weight of the camera. From these opinions, we can make thefollowingimportant observation:**Observation : An opinionconsists of two key components: a targetg**and a sentiment s(where gopinion has been expressed, and ssentiment, or a numeric rating score expressing the strength/intensity

Sentiment Analysis and Opinion Mining

17


---

<!-- Página 18 -->

Sentiment Analysis and Opinion Mining

18

of the sentiment (e.g., 1 to 5 stars). Positive, negative and neutral arecalled sentiment (or)(or).For example, the target of the opinion in sentence (2) is Canon G12, andthe target of the opinion insentence (3) is the picture quality ofCanon*G12**topic in the literature.*2.*opinion**sources or*(Kim and Hovy, 2004; Wiebe, Wilson andCardie, 2005). The holder of the opinions in sentences (2), (3), and (4) isthe author of the review (“John Smith”), but for sentence (5), it is thewife of the author.3.practice because one often wants to know how opinions change withtime and opinion trends.We are now ready todefine opinion as a quadruple.**Definition (Opinion): An opinion is a quadruple,**(*g ,*where g*s*target, h*t*expressed.This definition, although quite concise, may not be easy to use in practiceespecially in the domain of online reviews of products, services, andbrandsbecause the full description of the targetcan be complex and may not evenappear in the same sentence. For exampl e, in sentence (3), the opinion targetis actually “picture qualityof Canon G12”, but the sentence mentioned only“picture quality”. In this case, the opinion target is not just

“picture quality”

picture quality because without knowing that the sentence is evaluating the ofthe Canon G12 camera, the opinion in sentence (3) alone is of little use. Inpractice, the target can often bedecomposed and described ina structuredmanner withmultiple levels, which greatly facilitate both mining of opinionsand later use of the mined opinion results. For example, “picture quality ofCanon G12” can be decomposed into an entityand anattribute of the entityand represented as a pair,(Cannon-G12, picture-quality)Let us use the term entity to denote the target object that has been evaluated.Entity can bedefined as follows (Hu and Liu, 2004; Liu, 2006 and 2011).**Definition ( ) entity**organization, or event. It is described with a pair, eW*T*hierarchy of parts ,, and so on, and W*attributes*


---

<!-- Página 19 -->

Sentiment Analysis and Opinion Mining

Each part or sub-part also has its own set of attributes.**Example 1: A particular model of camera is an entity, e.g., Canon G12. It**has a set of attributes, e.g., picture quality , , and weight, and a set ofparts, e.g., lens viewfinder , and battery .also has its own set ofattributes, e.g., battery life and battery weight . A topic can be an entitytoo, e.g., tax increase , with its parts,” “*increase for the middleclass ” and “ tax increase for therich.”*This definition essentially describes a hierarchicaldecompositionofentitybased on the part-of relation. The root node is the name of the entity, e.g.,Canon G12 in the above review. All the other nodes are parts and sub-parts,etc. An opinion can be expressed on any node and any attribute of the node.**Example 2: In our example review above, sentence (2) expresses a positive**opinion about the entity Canon G12 camera as a whole. Sentence (3)expresses a positive opinion on the attribute of picture quality of thecamera. Clearly, one can also express opinions about parts or componentsof the camera.This entity as a hierarchy of any number of levels needs a nested relation torepresent it, which is often too complex for applications. The main reason isthat since NLP is a very difficult task, recognizing parts and attributes of an19entity at different levels of details is extremely hard. Most applications alsodo not need such a complex analysis. Th us, we simplify the hierarchy to twolevels and use the term aspectssimplified tree, the root node is still the entity itself, but the second level(also the leaf level) nodes are different aspects of the entity. This simplifiedframework is what is typically used in practical sentiment analysis systems.Note thatin the research literature, entities are also called objects, andaspects are also called features (as inproduct features). However, featureshere can confuse with features used in machine learning, where a featuremeans a data attribute. To avoid confusion, aspects have becomemorepopular in recent years. Note that some researchers also use the terms facets,*attributes and , and in specific applications, entities and aspects may*also be called other names based onthe application domain conventions.After decomposing the opinion target, we can redefine an opinion (Hu andLiu, 2004; Liu, 2010).**Definition (opinion) : An opinion is a quintuple,**(

,,,,),*i**ij**ijkl**k**l*where*e*

is the name of an entity, a*i* of entity e*, h*isthe opinion holder, and t*ij**i**k* . The sentiment s*k*

is an aspectof e*ij*,is the sentimenton aspect a*i**ijkl* is the time whentheopinion is expressed by h*l* is positive, negative, or*ijkl*


---

<!-- Página 20 -->

Sentiment Analysis and Opinion Mining

neutral, or expressed withdifferent strength/intensity levels, e.g., 1 to 5stars as used bymost review sits on the Web. When an opinion is on theentity itself as a whole, the special as pect GENERAL is used to denoteit.Here, e

20 and*i*

of entity e*ij*

together represent the opinion target.*ij*Some important remarks about this definition are in order:1.pieces of information in the quintuplemust correspond to one another.That is, the opinion s

at time t*i*

must be given by opinion holder h*ijkl* . Any mismatch is an error.2.*l*in general. For example, if we do not have the time component, wewillnot beableto analyze opinions on anentity according to time, which isoften very important in practice because an opinion two years ago andan opinion yesterday is not the same. Without opinion holder is alsoproblematic. For example, in the sentence “ the mayor is loved by the*people in thecity, but he has been criticizedby the state government,”*the two opinion holders, “ people in the city ” and “ state government,” areclearlyimportant for applications.3.meaning of an opinion, which can be arbitrarily complex. For example,it does not cover the situation in “ The view finder and the lens are too*close ,” which expresses an opinion on the distance of two parts. It also*does not cover the context of the opinion, e g., “ This car is too small for*a tall person ,” which does not say the car is too small for everyone.*“Tall person” is the contexthere. Note also that inthe original definitionof entity, it is a hierarchy of parts, sub-parts, and so on. Every part canhave its set of attributes. Due tothe simplification, the quintuplerepresentation can result in informationloss. For example, “ink” is apart/component of a printer. In a printer review, one wrote “The ink of*this printer isexpensive .” This does not say thatthe printer is expensive*(which indicates the aspect price ). If one does not care about anyattribute of the ink, this sentence just gives a negative opinion to the ink,whichis anaspectof the printer entity. However, if one alsowants tostudy opinions about different aspects of the ink, e.g., price and quality,the ink needs to be treated as a separate entity. Then, the quintuplerepresentation still applies, but the part-of relationship needs to besaved. Of course, conceptually we can also expand the representation ofopinion target using a nested relation. Despite the limitations, thedefinition does cover the essentialinformationof an opinion which issufficient for most applications. As wementioned above, too complex adefinition can make the problem extremely difficult to solve.

*a*about aspect*k*


---

<!-- Página 21 -->

4.structured data. The quintuple above is basically a database schema,based on which the extracted opinions can be put into a database table.Then a rich set of qualitative, qu antitative, and trend analyses ofopinions can be performed using the whole suite of databasemanagement systems (DBMS) and OLAP tools.5.*opinion . Another type is comparative opinion (Jindal and Liu, 2006b;*Liu, 2006 and 2011), whichneeds a different definition. Section 2.3 willdiscuss different types of opinions. Chapter 8 defines and analyzescomparative opinions. For the rest of this section, we only focus onregular opinions. For simplicity, we just called them opinions.

### 2.1.2 Sentiment Analysis Tasks

With the definition, we can nowpresent the objectiveand the key tasks ofsentiment analysis (Liu, 2010; Liu, 2006 and 2011).**Objective of sentiment analysis: Given an opinion document d**opinion quintuples ( e

*regular*

Sentiment Analysis and Opinion Mining

21

,,,,) in .*i**ij**ijkl**k**l*The key tasks are derived from the 5 components of the quintuple. The firstcomponent is the entity. That is, we need to extract entities. The task issimilar to named entity recognition (NER) in information extraction (Hobbsand Riloff, 2010; Mooney and Bunescu, 2005; Sarawagi, 2008). Thus, theextraction itself is a problem. After extraction, we also need to categorize theextracted entities. In naturallanguage text, people often write the same entityin different ways. For example, Motorolamay be written as Mot, Moto, andMotorola. We needto recognize that theyall refer to the same entity.**Definition (****nd entity expression ) entity category**represents a unique entity, while an entityis an actual word orphrase that appears inthe text indicating an entity category.Each entity category (or simply entity) should havea unique name in aparticular application. The process of grouping entity expressions intoentitycategories is called entity categorization .Now we look at aspects of entities. The problem is basically the sameas forentities. For example, picture , , and photo are the same aspect forcameras. We thus need toextract aspe ct expressions and categorize them.**Definition (**) aspect category ofan entity represents a unique aspect of the entity, while anaspect


---

<!-- Página 22 -->

Sentiment Analysis and Opinion Mining

*expression isan actual word or phrase that appears inthe text indicating*an aspect category.Each aspect category (or simply aspect) should also have a uniquename in aparticular application. The process of grouping aspect expressions intoaspect categories (aspects) is called aspect categorization.Aspect expressions are usually nouns and noun phrases but can also beverbs, verb phrases, adje ctives, and adverbs. The following definitions areuseful (Hu and Liu, 2004).**Definition (**): Aspect expressions that are nounsand noun phrases are called explicit aspectexpressions.For example, “picture quality” in “ The picture quality of this camera is*great ” is an explicit aspect expression.***Definition (**): Aspect expressions that are notnouns or noun phrases are called implicit aspect expressions.For example, “expensive” is an implicit aspect expression in “This camera is*expensive .” It implies the aspect price . Many implicit aspect expressions are*adjectives and adverbs that are used todescribe or qualify some specificaspects, e.g., expensive (price), and reliably (reliability). They can also be22verb and verb phrases, e.g., “ I can install the software easily.” “Install”indicates the aspect installation . Implicit aspect expressions are not justadjectives, adverbs, verbs and verb phrases; they can also be very complex,e.g., “ This camera will not easily fit in a coat pocket.” Here, “fit in a coatpocket” indicates the aspect size*shape ).*The third component in the opinion definition is the sentiment. This taskclassifies whether the sentiment on the aspect is positive, negative or neutral.The fourth component and fifth components are opinion holder and timerespectively. They also need to be extracted and categorized as for entitiesand aspects. Note that anopinion holder (Bethard etal., 2004; Choi et al.,2005; Kim and Hovy, 2004) (also called opinion source in (Wiebe, Wilsonand Cardie, 2005)) can be a personor organization who expressed anopinion. For product reviews and blogs, opinion holders are usually theauthors of the postings. Opinion holders are more important for news articlesas theyoften explicitlystate the person or organizationthat holds an opinion.However, in some cases, identifying op inion holders can also be importantin social media, e.g., identifying opinions from advertisers or people whoquote advertisements of companies.Based on the above discussions, we can define a model of entity and amodelof opinion document (Liu, 2006 and 2011).


---

<!-- Página 23 -->

Sentiment Analysis and Opinion Mining

**Model of entity : An entity e**is represented by itself as a whole and a finiteset of aspects A = {,, …, a}.can be expressed with any one of a*i**i**i**in**i*finite set of its entity expressions { 23,, …, ee*i**i* can be expressed with anyone of its finite set of aspectexpressions {*i ae* ,, …,}.**Model of opinion document**: An opinion document d*ij**ij**ijm*a set of entities { e

*, e**,*} and a subset of their aspects from a set ofopinion holders { h r12 *, h**,*} at some particular time point.12*p*Finally, to summarize, given a set of opinion documents*D*analysis consists of the following 6 main tasks.**Task 1 (entity extraction and categorization): Extract all entity expressions**inclusters (or categories). Each entity expression cluster indicates a uniqueentity e

.**Task 2 i**of the entities, and categor ize these aspect expressions into clusters. Eachaspect expression cluster of entity e

represents a unique aspect a*i*

is positive, negative or neutral, or assign a numericsentiment rating to the aspect.**Task 6 (opinion quintuple generation): Produce all opinion quintuples (e**

,,,) expressed in document dtasks. This task is seemingly very simple but it is in fact very difficult in*ij**ijkl**k**l*many cases as Example 4 below shows.Sentiment analysis (or opinionmining) based on this framework is oftencalled aspect-based sentiment analysis (**)***sentiment analysis (*) as it was called in (Hu and Liu, 2004;Liu, Hu and Cheng, 2005).We now use an example blog to illustrate the tasks (a sentence id is againassociated with each sentence) and the analysis results.**Example 4:**(1)*camera yesterday . (2) In the past week, we both used the cameras a**lot The photos from my Samy are not that great, and the battery*

}. Each aspect*a**is*

**Task 3 (opinionholder extraction and categorization): Extractopinion**holders for opinions fromtext or structured data and categorize them.The task is analogous to the above two tasks.**Task 4 (time extractionand standardization): Extract the times when**opinions are given and standardize different time formats. The taskisalso analogous to the above tasks.**Task 5 (aspect sentiment classification): Determine whether an opinion on**an aspect a

of entity e*i*

.*ij*

,*a**i*


---

<!-- Página 24 -->

Sentiment Analysis and Opinion Mining

*life is short too . (4) My friend was very happy with his camera and**loves its picture quality . (5) I want a camera that can take good**photos . (6)*.Task 1 should extract the entity expressions, “Samsung,” “Samy,” and“Canon,” and group “Samsung” and “Samy” together as they represent thesame entity. Task 2 should extract aspect expressions “picture,” “photo,” and“battery life,” and group “picture” and “photo” together as for cameras theyare synonyms. Task 3 should find the holder of the opinions in sentence (3)to be bigJohn (the blog author) and the holder of the opinions in sentence (4)to be bigJohn’s friend .posted is Sept-15-2011. Task 5 should find that sentence (3) gives a negativeopinion to the picture quality of the Samsung camera and also a negativeopinion to its battery life. Sentence (4) gives a positiveopinion to the Canoncamera as a whole and also to its picture quality. Sentence (5) seeminglyexpresses a positive opinion, but it does not. To generate opinionquintuplesfor sentence (4) we need toknow what “his camera” and “its” refer to. Task6 should finally generate the following four opinion quintuples:(Samsung, picture_quality, negative, bigJohn, Sept-15-2011)(Samsung, battery_life, negative, bigJohn, Sept-15-2011)(Canon, GENERAL, positive, bigJohn’s_friend, Sept-15-2011)24(Canon, picture_quality, positive, bigJohn’s_friend, Sept-15-2011)

## 2.2

Unlike factual information, opinions ar e essentially subjective. One opinionfrom a single opinion holder is usually not sufficient for action. Inmostapplications, one needs to analyze opin ions from a large number of people.Thisindicates that some form of summary of opinionsis desired. Althoughan opinion summary can be in one of many forms, e.g., structured summary(see below) or short text summary, the key components of a summaryshouldinclude opinions about different entit ies and their aspects and should alsohave a quantitative perspective. The quantitative perspective is especiallyimportant because 20% of the people being positive about a product is verydifferent from 80% of the people being positive about the product. We willdiscuss this furthe r in Chapter 7.The opinion quintuple defined above actually provides a good source ofinformation and also a framework for generating both qualitative and*quantitative summaries. A common form of summaryis based on aspects*and is called aspect-based opinion summary (or feature-based opinion*summary ) (Hu and Liu, 2004; Liu, Hu and Cheng, 2005). In the past few*


---

<!-- Página 25 -->

years, a significant amount of research has been done on opinion summary.Most of themare related to this framework (see Chapter 7).Let us use an example to illustrate this form of summary, which wasproposed in (Hu and Liu, 2004; Liu, Hu and Cheng, 2005) . We summarize aset of reviews of a digital camera, called digital1. The summarylooks like that in Figure 2.1, which is called a structured summary incontrast to a traditional text summary of a short document generated fromone or multiple long documents. In the figure, GENERAL represents thecamera itself (the entity). 105 reviews expressed positive opinions aboutthecamera and 12 expressed negative opinions. Picture quality and battery lifeare two camera aspects. 95 reviews ex pressed positive opinions about thepicture quality, and 10 expressed negative opinions. <Individual review*sentences> is a link pointing to the senten ces and/or the whole reviews that*give the opinions. With such a summa ry, one can easily see how existingcustomers feel about the camera. If one is interestedin a particular aspectand additional details, he/she can drill down by following the <Individual*review sentences> link to see the actual opinion sentences or reviews.*

## 2.3

The type of opinions that we have discussed so far is called regular opinion(Liu, 2006 and 2011). Another type is called comparative opinionand Liu, 2006b). In fact, we canalso classify opinions based on how they areexpressed in text, explicit opinion and**(****)**.

*Digital Camera*1:Aspect:**GENERAL**105 <Individual review sentences>12 <Individual review sentences>Aspect:**Picture quality**95 <Individual review sentences>10 <Individual review sentences>Aspect:**Battery life**50 <Individual review sentences>9 <Individual review sentences>**…****Figure 2.1. An aspect-based opinion summary.**

### 2.3.1 Regular and Comparative Opinions

**Regular opinion : A regular opinion is often referred to simply as an**

Sentiment Analysis and Opinion Mining

25


---

<!-- Página 26 -->

Sentiment Analysis and Opinion Mining

*opinion in the literature and it has two main sub-types (Liu, 2006 and 2011):**Direct opinion : A*refers toan opinion expressed directlyon an entity or an entityaspect, e.g., “ The picture quality is great.”*Indirect opinion : An indirect opinion is an opinion that isexpressed*indirectly onan entity or aspect of anentity based on its effects onsome other entities. This sub-type often occurs in the medical domain.For example, the sentence “ After injection of the drug, my joints felt*worse ” describes anundesirable effect of the drugon “my joints”,*which indirectly gives a negative opinion or sentiment to the drug. Inthe case, the entity is the drug*effect on joints .*Much of the current research focuses on direct opinions. They are simplerto handle. Indirect opinions are often harder to deal with. For example, inthe drug domain, one needs to k now whether some desirable andundesirable state is before or after using the drug. For example, thesentence “ Since”does not express a sentiment or opinion on the drug because “painfuljoints” (which is negative) happenedbefore using the drug.**Comparative opinion : A comparative opinion expresses a relation of**similarities or differences between two or more entities and/or a26entities (Jindal and Liu, 2006a; Jinda l and Liu, 2006b). For example, thesentences, “ Coke tastes better than Pepsi ” and “ Coke tastes the best”express two comparative opinions. A comparative opinion is usuallyexpressed using the comparative orform of an adjective oradverb, althoughnot always (e.g., prefer ). Comparative opinions alsohave many types. We will discuss and define them in Chapter 8.

### 2.3.2 Explicit and Implicit Opinions

**Explicit opinion : An explicit opinion is a subjective statement thatgives a**regular or comparativeopinion, e.g.,“*Coke tastes great ,” and*“*Coke tastes better than Pepsi .”***Implicit (or implied) opinion : An implicit opinion is an objective statement**that implies a regular or comparative opinion. Such anobjectivestatement usually expressesa desirable or undesirable fact, e.g.,“*I bought the mattress a week ago, and a valley has formed,” and*“*The battery life of Nokia phones is longer than Samsung phones.”*Explicit opinions are easier to detect and to classify than implicit opinions.Much of the current research has focused on explicitopinions. Relatively


---

<!-- Página 27 -->

less work has been done on implicit opinions (Zhang and Liu, 2011b). In aslightlydifferent direction, (Greene andResnik, 2009) studied the influenceof syntactic choices on perceptions of implicit sentiment. For example, forthe same story, different headlines can imply different sentiments.

## 2.4

There are two important concepts that are closely related to sentiment andopinion, i.e., subjectivity and.**Definition (sentence subjectivity): An**presents somefactual information about the world, while a subjective sentenceexpresses some personal feelings, views, or beliefs.An example objective sentence is “ iPhone is an Apple product.” An examplesubjective sentence is “ I like iPhone .” Subjective expressions come in manyforms, e.g., opinions, allegations, desires, beliefs, suspicions, andspeculations (Riloff, Patwardhan and Wiebe, 2006; Wiebe, 2000). There issome confusion among researchers to equate subjectivity withopinionated.By, we mean that a document or sentence expresses or implies apositive or negative sentiment. The two concepts are not equivalent,although they have a large intersection. The task of determining whether asentence is subjective or objective is called subjectivity classification (Wiebeand Riloff, 2005) (see Chapter 4). Here, we shouldnote the following:*I**think that he wenthome ” is a subjective sentence, but does not express*any sentiment. Sentence (5) in Example 4 is also subjective but it doesnot give a positive or negative sentiment about anything.and undesirable facts (Zhang and Liu, 2011b). For example, thefollowing two sentences which state some facts clearly imply negativesentiments (which are implicit opinions ) about their respective productsbecause the facts are undesirable:“.”“”Apart from explicitopinion bearing subjective expressions, many othertypes of subjectivity have also been studied although not as extensive, e.g.,affect, judgment, appreciation, specul ation, hedge, perspective, arguing,agreement and disagreement, political stances (Alm, 2008; Ganter andStrube, 2009; Greene and Resnik, 2009; Hardisty, Boyd-Graber and Resnik,2010; Lin etal., 2006; Medlock and Briscoe, 2007; Mukherjee and Liu,

Sentiment Analysis and Opinion Mining

27


---

<!-- Página 28 -->

Sentiment Analysis and Opinion Mining

2012; Murakami and Raymond, 2010; Neviarouskaya, Prendinger andIshizuka, 2010; Somasundaran and Wiebe, 2009). Many of themmay alsoimply sentiments.**Definition (emotion): Emotions are our subjective feelings and thoughts.**Emotions have been studied in multiple fields, e.g., psychology, philosophy,and sociology. The studies are very broad, from emotional responses ofphysiological reactions (e.g., heart rate changes, blood pressure, sweatingand so on), facial expressions, gestures and postures to different types ofsubjective experiences of an individual’s state of mind. Scientists havecategorized people’s emotions into some categories. However, there is stillnot a set of agreed basic emotions among researchers. Based on (Parrott,2001), people have six primary emotions, i.e., lovejoy, ,*sadness , and fear*tertiary emotions. Each emotion can also have differentintensities.Emotions are closely related to sentiments. The strength of a sentiment oropinion is typically linked to the intensity of certain emotions, e.g., joy*anger . Opinions that we study in sentiment analysis are mostlyevaluations*(although not always). According to consumer behavior research,evaluations can be broadly categorized into two types: rational evaluations28and**Rational evaluation : Suchevaluations are from rational reasoning, tangible**beliefs, and utilitarian attitudes. For example, the following sentencesexpress rational evaluations: “ The voice of this phone is clear,” “*is worth the price ,” and “ I amhappy with this car .”***Emotional evaluation : Such evaluations are from non-tangible and**emotional responses to entities which go deep into people’s state of mind.For example, the following sentence s express emotional evaluations: “I*love iPhone ,” “*” and “ This is the*best car ever built. ”*To make use of these two types of evaluations in practice, we can design 5sentiment ratings, emotional negative (-2), rational negative (-1), neutral (0),*rational positive (+1), and emotional positive (+2). In practice, neutral often*means no opinion or sentiment expressed.Finally, we need to note that the concepts of emotion and opinion are clearlynot equivalent. Rational opinions express no emotions, e.g., “The voice of*this phone is clear ”, and many emotional sentences express no*opinion/sentiment on anything, e.g., “ I am so surprised to see you here”.More importantly, emotionsmay not have targets, but just people’s internalfeelings, e.g., “ I am so sad today .”


---

<!-- Página 29 -->

## 2.5

We can lookat an opinion from two perspectives, i.e., the author (opinionholder) who expresses the opinion, and the reader who reads the opinion.For example, one wrote “ The housing price has gone down,*the economy .” Clearly, this author talks about the negative impact of the*dropping housing price on the economy. However, this sentence can beperceived in both ways by readers. For sellers, this is indeed negative, butfor buyers, this could wellbe a piece of good news. As another example, onewrote “ I am so happy thatGoogle share price shot up today.” If a readersold his Google shares yesterday at a loss, he will not be very happy, but ifthe reader bought a lot of Google shares yesterday, he will almost certainlybe as happy as the author of the sentence.I am not aware of any reported studies about this issue. In current research orapplications, researchers ei ther ignore the issue or a ssume a standing point intheir analysis. Usually, the opinion holders are assumed to be the consumersor the general public unless otherwise stated (e.g., the President of theUnited States). Product manufacturers or service providers’ opinions areconsidered advertisements if they are ma rked explicitly or fake opinions ifthey are not marked explicitly (e.g., mixed with opinionsfrom consumers).

## 2.6 Summary

This chapter definedthe concept ofopinion inthe context of sentimentanalysis, the main tasks of sentiment analysis, and the framework of opinionsummarization. Along with them, two relevant and important concepts ofsubjectivity and emotion were also introduced, which are highly related tobut not equivalent to opinion. Existing studies about them have mostlyfocused on their intersections with opinion (although not always). However,we should realize that all these concepts and their definitions are ratherfuzzy and subjective. For example, there is still not a set of emotions that allresearchers agree. Opinion itself is a broad concept too. Sentiment analysismainly deals with the evaluation typeof opinions or opinions which implypositive or negative sentiments. I will not be surprised if youdo notcompletely agree with everything in this chapter. The goal of this chapter isto give a reasonablyprecise definition of sentiment analysis and its relatedissues. I hope I have succeeded to some extent.

Sentiment Analysis and Opinion Mining

29


---

<!-- Página 30 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 3

30

## Document Sentiment Classification

Starting fromthis chapter, we discuss the current major research directionsor topics and their core techniques. Sentiment classification is perhaps themost extensively studied topic (also see the survey (Pang and Lee, 2008)). Itaims to classify an opinion document as expressinga positive or negativeopinion or sentiment. The task is also commonly known as the document-*level sentiment classification because it considers the whole document as a*basic information unit. A large majority of researchpapers on this topicclassifies online reviews. We thus also define the problem in the reviewcontext, but the definition is also applicable to other similar contexts.**Problem definition : Given an opinion document d**determine the overall sentiment si.e., determine s(, _where the entity e*h**t*known or irrelevant (do not care).There are two formulations based onthe type of value thats*s*categorical values, e.g., positive and negative, thenit is a classificationproblem. If se.g., 1 to 5, the problem becomes regression.To ensure that the task is meaningful in practice, existing research makes thefollowing implicit assumption (Liu, 2010):**Assumption : Sentiment classification or regression assumes that the opinion**document d*e**h*In practice, if an opinion document evaluates more than one entity, then thesentiments on the entities can be different. For example, the opinion holdermay be positive about some entities and negative about others. Thus, it doesnot make practical sense to assign one sentiment orientation to the entiredocument in this case. It also does not make much sense if multiple opinionholders express opinions ina single document because their opinions can bedifferent too.This assumption holdsfor reviews of productsand servicesbecause each


---

<!-- Página 31 -->

review usually focuses on evaluating a single product or service and iswritten by a single reviewer. However, the assumption may not hold for aforum and blog post because in sucha post the author may express opinionson multiple entities and compare them using comparative sentences.Below, we first discuss theclassification problem to predict categorical classlabels and then the regression problem to predict ratingscores. Most existingtechniques for document-level classification use supervised learning,although there are also unsupervisedmethods. Sentiment regression hasbeen done mainly using supervised learning. Recently, several extensions tothis research have also appeared, most notably, cross-domain sentiment*classification (or domain adaptation ) and cross-language sentiment**classification , which will also be discussed atlength.*

## 3.1

## Supervised Learning

Sentiment classification is usually form ulated as a two-class classificationproblem, positive and negative . Training and testing data used are normallyproduct reviews. Since online reviews have rating scores assigned by theirreviewers, e.g., 1-5 stars, the positive and negative classes are determinedusing the ratings. For example, a review with 4 or 5 stars is consideredapositive review, and a review with 1 to 2 stars is considered a negativereview. Most research papers do not use the neutral class, which makes theclassification problem considerably eas ier, but it is possible to use theneutral class, e.g., assigning all 3-star reviews the neutral class.Sentiment classification is essentially a text classification problem.Traditional text classification mainly classifies documents of differenttopics, e.g., politics, sciences, and sports. In such classifications, topic-related words are the key features. However, in sentiment classification,sentiment or opinionwords that indicatepositiveor negative opinions aremore important, e.g., great ,,,, , , etc.Since it is a text classification problem, any existing supervised learningmethod can be applied, e.g., naïve Bayes classification, and support vectormachines (SVM) (Joachims, 1999; Shawe-Taylor and Cristianini, 2000).Pang, Lee and Vaithyanathan (2002) was the first paper to take this approachto classifymovie reviews into two classes, positive and negative. It wasshown that using unigrams (a bag of words) as features in classificationperformed quite well with either naïve Bayes or SVM, although the authorsalso tried a number of other feature options.

Sentiment Analysis and Opinion Mining

31


---

<!-- Página 32 -->

Sentiment Analysis and Opinion Mining

In subsequent research, manymore f eatures and learning algorithms weretried by a large number of researchers. Like other supervised machinelearning applications, the key for sentiment classification is the engineeringof a set of effective features. Some of the example features are:*Terms and their frequency . These features are individual words (unigram)*and their n-grams with associated frequency counts. They are also themost common features used in tradi tionaltopic-based text classification.In some cases, word positions may also be considered. The TF-IDFweighting scheme from information retrieval may be applied too. As intraditional text classification, these features have been shown highlyeffective for sentiment classification as well.*Part of speech . The part-of-speech (POS) of each word can be important too.*Words of different parts of speech (P OS) may be treated differently. Forexample, it was shown that adjectives are important indicators ofopinions. Thus, some researchers treate d adjectives as special features.However, one can also use all POS tags and their n-grams as features.Note that in this book, we use the standard Penn Treebank POS Tags asshown in Table 3.1 (Santorini, 1990). The Penn Treebank site is at[http://www.cis.upenn.edu/](http://www.cis.upenn.edu/) ~treebank/home.html..are words in a language that32are used to express positive or negative sentiments. For example, good,*wonderful , and amazing are positive sentiment words, and badpoor**terrible are negative sentiment words. Most sentiment words are*adjectives and adverbs, but nouns (e.g., rubbish , , and crapverbs (e.g., hate lovefrom individual words, there are also sentiment phrases and idioms, e.g.,*cost someone an armand a leg .**Rules of opinions . Apart from sentiment words and phrases, there are also*many other expressions or language compositions that can be used toexpress or imply sentiments and opinions. We will list and discuss someof such expressions in Section 5.2.*Sentiment shifters. These are expressions that are used to change the*sentiment orientations, e.g., from positive to negative or vice versa.Negation words are the most important class of sentiment shifters. Forexample, the sentence “ I don’t like this camera ” is negative. There arealso several other types of sentiment shifters. Wewill discuss theminSection 5.2 too. Such shifters also need to be handled with care becausenot all occurrences of such words mean sentiment changes. For example,“not” in “not only … but also” does not change sentiment orientation.*Syntactic dependency . Words dependency-based features generated from*parsing or dependency trees ar e also tried by researchers.


---

<!-- Página 33 -->

CCPRP$ Possessive pronoun CDRBAdverb DTRBRAdverb, comparative EX Existential thereAdverb, superlative FWRPParticle IN Preposition orSYM Symbolsubordinating conjunction

JJ Adjective TO to JJRUH Interjection JJSVB Verb, base form LSVBDVerb, past tense MDVBGVerb, gerund or present participle NNVBN Verb, past participle NNS Noun, pluralVerb, non-3rd personpresent

NNP Propernoun, singular VBZ Verb, 3rd person singularpresent NNPS Proper noun, plural WDT Wh-determiner PDT Predeterminer WPWh-pronoun POS Possessive ending WP$ **Table 3.1. Penn Treebank Part-Of-Speech (POS) tags**PRP Personal pronoun WRBWh-adverb**Tag Description****Description**  Instead of using a standardmachine learning method, researchers have alsoproposed several custom techniques specifically for sentiment classification,e.g., the score function in (Dave, Lawrence and Pennock, 2003) based onwords in positive and negative reviews, and the aggregation method in(Tong, 2001) using manually compiled domain-specific words and phrases.A large number of papers have been published in the literature. Here, weintroduce them briefly. In (Gamon, 2004), classification was performed oncustomer feedback data, which are usually short and noisy compared toreviews. In (Pang and Lee, 2004), the minimum cut algorithm working on agraph was employed to help sentiment classification. In (Mullen and Collier,2004; Xia and Zong, 2010), syntactic relations were used together withtraditional features. In (Kennedy and Inkpen, 2006; Li et al., 2010), thecontextual valence and sentiment shifte rs were employed for classification.In (Cui, Mittal and Datar, 2006), an evaluation was reported withseveralsentiment classification algorithms available at that time. In (Ng, Dasguptaand Arifin, 2006), the classification was done by using some linguisticknowledge sources. In (Abbasi, Chen and Salem, 2008), a genetic algorithmbased feature selection was proposed for sentiment classification in differentlanguages. In (Li, Zhang and Sindhwani, 2009), a non-negativematrixfactorization method was proposed. In (Dasgupta and Ng, 2009; Li et al.,2011; Zhou, Chen and Wang, 2010), semi-supervised learning and/or active

Sentiment Analysis and Opinion Mining

33


---

<!-- Página 34 -->

Sentiment Analysis and Opinion Mining

learning were experimented . In (Kim, Li and Lee, 2009) and (Paltoglou andThelwall, 2010), different IR term weighting schemes were studied andcompared for sentiment classification. In (Martineau and Finin, 2009), a newterm weighting scheme called Delta TFIDF was proposed. In (Qiu et al.,2009), a lexicon-based and self-supervision approach was used. In (He,2010), labeled features (rather than labeled documents) were exploited forclassification. In (Mejova and Srinivas an, 2011) the authors explored variousfeature definition and selection stra tegies. In (Nakagawa, Inui andKurohashi, 2010), a dependency tree-based classification method wasproposed, which used conditional randomfields (CRF) (Lafferty, McCallumand Pereira, 2001) with hidden variables. In (Bickerstaffe and Zukerman,2010), a hierarchical multi-classifier considering inter-class similarity wasreported. In (Li et al., 2010), persona l (I, we) and impersonal (they, it, thisproduct) sentences were exploited to help classification. In (Yessenalina,Choi and Cardie, 2010), automatically generated annotator rationales wasused to helpclassification. In (Yessenalina, Yue andCardie, 2010), multi-level structuredmodels were proposed. In (Wang et al., 2011), the authorsproposed agraph-based hashtag approach toclassifying Twitter postsentiments, and in (Kouloumpis, Wilson and Moore, 2011), linguisticfeatures and features that capture information about the informal and342011), the authors used word vectors which can capture some latent aspectsof the words to help classification. In (Bespalov et al., 2011), sentimentclassification was performed based on supervised latent n-gram analysis. In(Burfoot, Bird and Baldwin, 2011), congressionalfloor debates wereclassified. In (Becker and Aharonson, 2010), the authors showed thatsentiment classification should focus on the final portion of the text based ontheir psycholinguistic and psychophysical experiments. In (Liu et al., 2010),different linguistic features were compared for both blog and reviewsentiment classification. In (Tokuhisa, Inui and Matsumoto, 2008), emotionclassification of dialog utterances was investigated. It first performedsentiment classification of three classe s (positive, negative and neutral) andthen classified positive and negative utterances into 10 emotion categories.

## 3.2

## Unsupervised Learning

Since sentiment words are often the dominating factor for sentimentclassification, it is not hard to imagine that sentiment words and phrasesmaybe used for sentiment classification inan unsupervised manner. The method


---

<!-- Página 35 -->

Sentiment Analysis and Opinion Mining

in (Turney, 2002) is such a technique. It performs classification based onsome fixed syntactic patterns that are likely to be usedto express opinions.The syntactic patterns are composed based on part-of-speech (POS) tags.The algorithm given in (Turney, 2002) consists of three steps:Step 1: Two consecutive words are extracted if their POS tags conform toany of the patterns in Table 3.2. For example, pattern 2 means that twoconsecutive words are extracted if the first word is an adverb, the secondword is an adjective, and the third word (not extracted) is not a noun. Asan example, in the sentence “ This piano produces beautiful sounds”,“” is extracted as it satisfies the first pattern. The reasonthese patterns are used is that JJ, RB, RBR and RBS words often expressopinions. The nouns or verbs act as the contexts because in differentcontexts a JJ, RB, RBR and RBS word may express different sentiments.For example, the adjective (JJ) “unpredictable” may have a negativesentiment in a car review as in “unpredictable steering,” but it could havea positive sentiment in a movie review as in “unpredictable plot.”Step 2: It estimates the sentiment orientation ( SOusing the pointwise mutual information (PMI) measure:35

1 , and Pr( term2

1NN or NNSanything 2JJnot NN nor NNS 3JJnot NN nor NNS 4JJnot NN nor NNS 5VB, VBD, VBN, or VBG

) is the actual co-occurrence probability of term2 )Pr(1) is the co-occurrence probability of thetwo terms if they are statistically independent. The sentiment orientation2(reference word “excellent” and the negative referenceword “poor”:*SO*) (“excellent”)  (“poor”). (2)The probabilities are calculated by i ssuing queries to a search engine andcollecting the number of hitsusually gives the number of relevant documents to the query, which is thenumber of hits. Thus, by searching the two terms together and separately,**Table 3.2. Patterns of POS tags for extracting two-word phrases**First word**Second word****Third word**(not extracted)

(1)Pr()( , )Pr( ))PMI measures the degree of statisti cal dependence between two terms.*PMI term term   term  **term * 1212212

and1


---

<!-- Página 36 -->

Sentiment Analysis and Opinion Mining

the probabilities in Equation (1) can be estimated. In (Turney, 2002), theAltaVista search engine was usedbecause ithas a NEAR operator toconstrain the search to documents that contain the words within ten wordsof one another in either order. Let hits ) be the number of hitsreturned. Equation (2) can be rewritten as:

36

## 3.3

Apart from classification of positive and negative sentiments, researchersalso studied the problem of predicting the rating scores (e.g., 1–5 stars) ofreviews (Pang and Lee, 2005). In this case, the problemcan be formulated asa regression problem since the rating scores are ordinal, althoughnot allresearchers solved the problem using regression techniques. Pang and Lee(2005) experimented withSVM regression, SVM multiclass classificationusing the one-vs-all (OVA) strategy, and a meta-learningmethod calledmetric labeling. It was shown that OVA based classification is significantlypoorer than the other two approaches, which performed similarly. This isunderstandable as the numerical ratings are not categorical values. Goldbergand Zhu (2006) improved this approachbymodeling rating prediction as agraph-based semi-supervised learning problem, which used both labeled(with ratings) and unlabeled (without ratings) reviews. The unlabeledreviews were also the test reviews whose ratings need to be predicted. In thegraph, each node is a document (review) and the linkbetween two nodes isthe similarity value between the two documents. A large similarity weightimplies thatthe two documents tendto have the same sentiment rating. The

2(3)() " )( ).( " ()Step 3: Given a review, the algorithm computes the average SO*hits**NEAR**hits*phrases in the review and classifies*SO* *NEAR**hits**SO*Final classification accuracies on reviews from variousdomains range from84% for automobile reviews to 66% for movie reviews.Another unsupervised approachis the lexicon-based method, which uses adictionaryof sentiment words and phrases with their associatedorientationsand strength, and incorporates intensification and negation to compute asentiment score for each document (Taboada et al., 2011). This method wasoriginally used in sentence and aspect -levelsentiment classification (Ding,Liu and Yu, 2008; Hu and Liu, 2004; Kimand Hovy, 2004).


---

<!-- Página 37 -->

paper experimented with se veral differentsimilarity schemes. The algorithmalso assumes that initially a separate learner has already predicted thenumerical ratings of the unlabeled documents. The graph based method onlyimproves them by revising the ratings through solving an optimizationproblem to force ratings tobe smooth throughout the graph with regard toboth the ratings and the link weights.Qu, Ifrim and Weikum (2010) introduce d a bag-of-opinions representationof documents to capture the strength of n-grams with opinions, which isdifferent from the traditional bag-of-words representation. Each of theopinions is a triple, a sentiment word, a modifier, and a negator. Forexample, in “not very good”, “good” is the sentiment word, “very” is themodifier and “not” is the negator. Fo r sentiment classification of two classes(positive and negative), the opinion modifier is not crucial but for ratingprediction, it is very important and so is the impact of negation. Aconstrained ridge regression method was developed to learn the sentimentscore or strength of each opinion from domain-independent corpora (ofmultiple domains) of rated reviews. The key idea of learning was to exploitan available opinion lexicon and the review ratings. Totransfer theregressionmodel to a newly given domain-dependent application, thealgorithm derives a set of statistics over the opinion scores and then usesthem as additional features together with the standard unigrams for ratingprediction. Prior to this work, (Liu and Seneff, 2009) proposed an approachto extracting adverb-adjective-noun phr ases (e.g., “very nice car”) based onthe clause structure obtained by parsing sentences into a hierarchicalrepresentation. They assigned sentiment scores based on a heuristicmethodwhich computes the contribution of adjectives, adverbials and negations tothe sentiment degree based on the ratings of reviews where these wordsoccurred. Unlike the above work, there was no learning involved in thiswork.Instead of predicting the rating of each review, Snyder and Barzilay (2007)studied the problem of predicting the rating for each aspect. A simpleapproach tothis task wouldbe touse a standard regression or classificationtechnique. However, this approachdoes not exploit the dependenciesbetween users’ judgments across different aspects. Knowledge of thesedependencies is useful for accurate pr ediction. Thus, this paper proposedtwo models, aspectmodel (which works on individual aspects) andagreement model (which models the rating agreement among aspects). Bothmodels were combined in learning. The features used for training werelexical features such as unigra m and bigrams from each review.Long, Zhang and Zhu (2010) used a similar approach as that in (Pang andLee, 2005) but with a Baysian network classifier for rating prediction of

Sentiment Analysis and Opinion Mining

37


---

<!-- Página 38 -->

Sentiment Analysis and Opinion Mining

each aspect in a review. For good accuracy, instead of predicting for everyreview, they focused on predicting only aspect ratings for a selected subsetofreviews which comprehensively evaluates the aspects. Clearly, theestimations from these reviews should bemore accurate than for those ofother reviews because these other reviews do not have sufficientinformation. The review selection method used an information measurebased on Kolmogorov complexity. The aspect rating prediction for theselected reviews used machine learning. The features for training were onlyfrom those aspect related sentences. The aspect extraction was done in asimilar way to that in (Hu and Liu, 2004). 38

## 3.4 Cross-Domain Sentiment

## Classification

It has been shown that sentiment classification is highly sensitive to thedomain from which the training data is extracted. A classifier trained usingopinion documents from one domain often performs poorly on testdata fromanother domain. The reason is that word s and even language constructs usedin differentdomains for expressing opinions can be quite different. Tomakematters worse, the same word in one domain may mean positive but inanother domain maymean negative. Thus, domain adaptation or transferlearning is needed. Existing resear ches are mainly based on two settings.The first setting needs a small amountof labeled trainingdata for the newdomain (Aueand Gamon, 2005). The second needs nolabeleddata for thenew domain (Blitzer, Dredze and Pereira, 2007; Tan et al., 2007). Theoriginaldomain with labeled training data is often called the source domain,and the new domain which is used for testing is called the target domain.In (Aue and Gamon, 2005), the authors proposed to transfer sentimentclassifiers to new domains in the absence of large amounts of labeled data inthese domains. They experimented with four strategies: (1) training on amixture of labeled reviews from other domains where such data are availableand testing on the targetdomain; (2) training a classifier as above, butlimiting the set of features to those onlyobserved in the target domain; (3)using ensembles of classifiers from domains with available labeled data andtesting on the target domain; (4) combining small amounts of labeled datawith large amounts of unlabeled datain the target domain (this is thetraditional semi-supervised learning setting). SVM was used for the firstthree strategies, and EM for semi-supervised learning (Nigam et al., 2000)was used for the fourth st rategy. Their experiments showed that the strategy(4) performed the best because it was able to make use of both the labeledandunlabeled datainthe target domain.


---

<!-- Página 39 -->

In (Yang, Si and Callan, 2006), a simple strategy based on feature selectionwas proposed for transfer learning for sentence level classification. Theirmethod first used two fully labeled training set from two domains to selectfeatures thatwere highly ranked in both domains. These selected featureswere considered domain independent features. The classifier built usingthese features was then applied to any target/test domains. Another simplestrategy was proposed in (Tan et al., 2007), which first trains a baseclassifier using the labeled data from the source domain, and then uses theclassifier to label some informative examples in the target domain. Based onthe selected examples in the target domain, a new classifier is learned, whichis finally applied toclassify the testcasesin thetargetdomain.In (Blitzer, Dredze and Pereira, 2007) , the authors used a method calledstructural correspondencelearning (SCL) for domain adaptation, which wasproposed earlier in (Blitzer, McDonald and Pereira, 2006). Given labeledreviews froma source domain and unlabeled reviews from both the sourceand target domains, SCL first chooses a set of mfrequently in both domains and are also good predictors of the source label(the paper chose those features with highest mutual information to thesourcelabel). These features are called the pivot features which represent the sharedfeature space of the two domains. It th en computes the correlations of eachpivotfeature with other non-pivot features in both domains. This producesacorrelation matrix W*i*pivot features with the ithat those non-pivot features are positively correlated with the ifeature in the source domain or in th e new domain. This establishes a featurecorrespondence between the two domains. After that, singular valuedecomposition (SVD) is employed to compute a low-dimensional linearapproximation

Sentiment Analysis and Opinion Mining

39

(the top k***W***set of features for training and for testing is the original set of features xcombined with

**x***k*using the combined features and labeled data in the source domain shouldwork in both the source and the target domains.Pan et al. (Pan et al., 2010) proposed a method similar to SCL at the highlevel. The algorithm works in the setting where there are only labeledexamples in the source domain and unlabeled examples in the target domain.It bridges the gap between the domains by using a spectral feature alignment(SFA) algorithm to align domain-specific words fromdifferent domains intounified clusters, with the help of domain independent words as the bridge.Domain-independent words are like pivot words in (Blitzer, Dredze andPereira, 2007) and can be selected similarly. SFA works by first constructinga bipartite graph with the domain-independent words as one set of nodes andthe domain-specific words as the other set of nodes. A domain specific wordis linked to a domain-independent word if they co-occur. The co-occurrencecan be defined as co-occurring in the same document or within a window.


---

<!-- Página 40 -->

Sentiment Analysis and Opinion Mining

The link weight is the frequency of thei r co-occurrence. A spectral clusteringalgorithm is then applied on the bipartite graph to co-align domain-specificand domain-independent words into a set of feature clusters. The ideais thatif two domain-specific words have connections to more common domain-independent words in the graph, they tend to be aligned or clustered togetherwith a higher probability. Similarly, if two domain-independent words haveconnections tomore common domain-specific words in the graph, they tendto be aligned together with a higher probability. For the final cross-domaintraining and testing, all data examples are represented with the combinationof these clusters and the original set of features.Along the same line, He, Lin and Alani (2011) used joint topic modeling toidentify opinion topics (which are similar to clusters in the above work)from both domains to bridge them. The resulting topics which cover bothdomains are used as additional featur es to augment the original set offeatures for classification. In (Gao and Li, 2011), topicmodeling was usedtoo to find a common semantic space based on domain termcorrespondences and term co-occurrences in the two domains. This commonsemantic space was thenused to learn a classifier which was applied tothetarget domain. Bollegala, Weir and Carroll (2011) proposed a method toautomatically create a sentiment sensitive thesaurus using both labeled andunlabeled data frommultiple source domains to find the association between40thesaurus is then used to expand the orig inal feature vectors to train a binarysentiment classifier. In (Yoshida et al., 2011), the authors proposed a methodfor transfer frommultiple source domains to multiple target domains byidentifying domain dependent and independent word sentiments. In(Andreevskaia and Bergler, 2008), a method using an ensemble of twoclassifiers was proposed. The first classifier was built using a dictionary andthe second was built using a small amount of in-domain training data.In (Wu, Tan and Cheng, 2009), a graph-based methodwas proposed, whichuses the idea of label propagation on a similarity graph (Zhu andGhahramani, 2002) toperform the transfer . In the graph, each document is anode and each link between two nodes is a weight computed using thecosine similarity of the two documents. Initially, every document in the olddomain has a label score of +1 (positive) or -1 (negative) and each documentin the new domain is assigned a label score based a normal sentimentclassifier, which can be learned from the old domain. The algorithm theniteratively updates the label score of each new domain document i*k**k*domain. A linear combination of the neighbor label scores and link weightsare used to assign a new score to node ilabel scores converge. The sentiment orientations of the new domaindocuments are determined by their label scores.


---

<!-- Página 41 -->

Xia and Zong (2011) found that across different domains, features of sometypes of part-of-speech (POS) tags areusually domain-dependent, while ofsome others are domain-free. Based on this observation, they proposed aPOS-based ensemble model to integrate features with different types of POStags to improve the classification performance.

## 3.5 Cross-Language Sentiment

## Classification

Cross-language sentiment classification means to perform sentimentclassification of opinion documents in multiple languages. There are twomain motivations for cross-language cl assification. First, researchers fromdifferent countries want to build sentiment analysis systems in their ownlanguages. However, much of the res earch has been done in English. Thereare not manyresources or tools in other languages that can be used to buildgood sentiment classifiers quickly in these languages. The natural question iswhether it is possible to leverage the automated machine translationcapability and existing sentiment analysis resources and tools available inEnglish to help build sentiment analysis systems in other languages. Thesecond motivation is that in many applications, companies want to know andcompare consumer opinionsabout their products and services in differentcountries. If they have a sentiment analysis system in English, theywant toquickly build sentiment analysis systems in other languages throughtranslation.Several researchers have studied this problem. Much of the current workfocuses on sentiment classification at the document level, and subjectivityand sentiment classification at the sentence level. Limited work has beendone at the aspect level except that in (Guo et al., 2010). In this section, wefocus on cross-language document-level sentiment classification. Section 4.5inthe next chapter focuses onthe sentence level.In (Wan, 2008), the author exploited sentiment resources in English toperform classification of Chinese review s. The first step of the algorithmtranslates each Chinese review into En glish using multiple translators, whichproducedifferentEnglish versions. It thenuses a lexicon-based approachtoclassify each translated English version. The lexicon consists of a set ofpositive terms, a set of negative terms, a set of negation terms, and a set ofintensifiers. The algorithm then sums up the sentiment scores of the terms inthe review considering negations and intensifiers. If the final score is lessthan 0, the review is negative, otherw ise positive. For the final classificationof each review, it combines the scores of different translated versions usingvarious ensemble methods, e.g., average, max, weighted average, voting,

Sentiment Analysis and Opinion Mining

41


---

<!-- Página 42 -->

Sentiment Analysis and Opinion Mining

etc. If a Chinese lexicon is also available, the same technique can be appliedto the Chinese version. Its result may also be combined with the results ofthose English translations. The results show that the ensemble technique iseffective. Brooke, Tofiloski and Tabo ada (2009) also experimented withtranslation (using only one translator) from the source language (English) tothe target language (Spanish) and then used a lexicon-based approach ormachine learning for target language document sentiment classification.In (Wan, 2009), a co-training method was proposed which made use of anannotated English corpus for classification of Chinese reviews in asupervisedmanner. No Chinese resources were used. In training, the inputconsisted of a set of labeled English reviews and a set of unlabeled Chinesereviews. The labeled English reviews were translated into labeled Chinesereviews, and the unlabeled Chinese reviews were translated into unlabeledEnglish reviews. Each review was thus associated with an English versionand a Chinese version. English features and Chinese features for each reviewwere considered as two independent and redundant views of the review. Aco-training algorithm using SVM was then applied to learn two classifiers.Finally, the two classifiers were combin ed into a single classifier. In theclassification phase, each unlabeled Ch inese review for testing was firstthen the learned classifier was applied42to classify thereviewinto either positive or negative.Wei and Pal(2010) proposed to use a transfer learning method for cross-language sentiment classification. Due to the fact that machine translation isstill far fromperfect, to minimize the noise introduced in translation, theyproposed to use the structural correspondence learning (SCL) method(Blitzer, Dredze and Pereira, 2007) discussed inthe previous sectionto finda small set of core features shared by both languages (English and Chinese).To alleviate the problem of data and feature sparseness, they issuedqueriestoa search engine to find other highly correlated features to those in the corefeature set, and then used the newly discovered features to create extrapseudo-examples for training.Boyd-Graber and Resnik (2010) extended the topic modeling method*supervised latent Dirichlet allocation (SLDA) (Blei and McAuliffe, 2007) to*work on reviews frommulti-languages for review rating prediction. SLDA isable to consider the user-rating of each review in topic modeling. Theextendedmodel MLSLDA creates topics using documents frommultiplelanguages at the same time. The resultingmulti-language topics are globallyconsistent across languages. To bridge topic terms in different languages intopic modeling, themodel used the aligned WordNets of different languagesor dictionaries.


---

<!-- Página 43 -->

In (Guo et al., 2010), a topic model based method was proposedtogroup aset of given aspect expressions in different languages into aspect clusters(categories) for aspect-based sentiment comparison of opinions fromdifferent countries (see alsoSection 5.3.4).In (Duh, Fujino and Nagata, 2011), the authors presented their opinionsabout the research of cross-language se ntiment classification. Based on theiranalysis, they claimed that domain mi smatch was not caused by machinetranslation(MT) errors, and accuracy degradation would occur evenwithperfect MT. It also argued that the cross-language adaptation problemwasqualitatively different from other (monolingual) adaptation problems inNLP; thus new adaptation algorithms should to be considered.

## 3.6 Summary

Sentiment classification atthe document level provides an overall opinionon an entity, topic or event. It has been studied by a large number ofresearchers. However, this level of classification has some shortcomings forapplications:aspects of entities are liked and disliked by consumers. In typical opiniondocuments, such details are provided, but document sentimentclassification does not extract them for the user.such as forumdiscussions, blogs, an d news articles, because many suchpostings can evaluate multiple entities and compare them. In many cases,it is hard to determine whether a posting actually evaluates the entitiesthat the user is interested in, and whether the posting expresses anyopinion at all, let alone to determine the sentiment about them.Document-level sentiment classifi cation does not perform such fine-grained tasks, which require in-depth natural language processing. In fact,online reviews do not need sentiment classification because almost allreviews already have user-assigned star ratings. In practice, it is the forumdiscussions and blogs that need sentiment classification to determinepeople’s opinions about different entities (e.g., products and services) andtopics.

Sentiment Analysis and Opinion Mining

43


---

<!-- Página 44 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 4

44

## Sentence Subjectivity and

## Sentiment Classification

As discussed in the previous chapter, document-level sentimentclassification may be too crude for most applications. We now move to thesentence level, i.e., to classify sentiment expressed in each sentence.However, there is no fundamental difference between document andsentence level classifications because sentences are just short documents.One assumption that researchers often make about sentence-level analysis isthat a sentence usually contains a singleopinion (although not true inmanycases). A document typically contains multiple opinions. Let us start ourdiscussion with an example review:“*initially. The voice was clear and the battery life was long, although it**is abit bulky. Then, it stopped working yesterday .”*The first sentence expresses no opinion as it simply states a fact. All othersentences express either explicit or implicit sentiments. Note no opinion isusually regarded as neutral.**Problem definition : Given a sentence x**positive, negative, or neutral (or no) opinion.The quintuple ( e ,classification is an intermediate step. Inmost applications, one needs toknow the opinion targets. Knowing only that a sentence expresses a positiveor negative opinion, but not what entities/aspects the opinion is about, is oflimited use. However, sentence level classification is still useful because inmany cases, if we know what entities and entityaspects are talked about inasentence, this step can help determine whether the opinions about the entitiesand their aspects are positive or negative.Sentence sentiment classification can be solved either as a three-classclassification problem or as two separate classification problems. In thelatter case, the first problem(also called the first step) is to classify whethera sentence expresses an opinion or not. The secondproblem (also called thesecond step) then classifies those opinion sentences into positive andnegative classes. The first problem is usually called subjectivity*classification , which determines whether a sentence expresses a piece of*subjective information or factual (objective) information (Hatzivassiloglou

*x*


---

<!-- Página 45 -->

and Wiebe, 2000; Riloff, Patwardhan and Wiebe, 2006; Riloff and Wiebe,2003; Wiebe et al., 2004; Wilson, Wiebe and Hwa, 2004; Wilson, Wiebeand Hwa, 2006; YuandHatzivassilogl ou, 2003). Objective sentences areregarded as expressing no sentiment or opinion. This can be problematic aswe discussed earlier because objective sentences can also imply opinions.For example, “ Then, it stopped working yesterday ” in the above review is anobjective sentence, but itimplies a negative sentiment about thephonebecause of the undesirable fact. Thus, it ismore appropriate for the first stepto classify each sentence as opinionated or not opinionated, regardlesswhether it is subjective or objective. However, due to the common practice,we still use the term subjectivity classification in this chapter. Below, wefirst discuss existing work on sentence-level subjectivity classification andthen sentiment classification.

## 4.1

Subjectivity classification classifies sentences into two classes, subjectiveand objective (Wiebe, Bruce and O'Hara, 1999). An objective sentenceexpresses some factual information, while a subjective sentence usuallygives personal views and opinions. In fact, subjective sentences can expressmany types of information, e.g., opinions, evaluations, emotions, beliefs,speculations, judgments, allegations, stances, etc. (Quirk et al., 1985; Wiebe,Bruce and O'Hara, 1999). Some of them indicate positive or negativesentiments and some of them do not. Early research solved subjectivityclassification as a standalone problem, i.e., not for the purpose of sentimentclassification. In more recent research, some researchers treated it as the firststep of sentiment classification by using it to remove objective sentenceswhich are assumed to express or imply no opinion.Most existing approaches to subjectivity classification are based onsupervised learning. For example, the early work reported in (Wiebe, BruceandO'Hara, 1999) performed subjectivity classification using the naïveBayes classifier with a set of binary features, e.g., the presence in thesentence of a pronoun, an adjective, a cardinal number, a modal other than*will**not*learning algorithms and more sophisticated features.In (Wiebe, 2000), Wiebe proposed an unsupervised method for subjectivityclassification, which simply used the pr esence of subjective expressions in asentence to determine the subjectivity of a sentence. Since there was not acomplete set of such expressions, it provided some seeds and then useddistributional similarity (Lin, 1998) to find similar words, which were also

Sentiment Analysis and Opinion Mining

45


---

<!-- Página 46 -->

Sentiment Analysis and Opinion Mining

likely to be subjectivity indicators. However, words found this way had lowprecision and high recall. Then, themethod in (Hatzivassiloglou andMcKeown, 1997) and gradability in (Hatzivassiloglou and Wiebe, 2000)were applied to filter the wrong subjective expressions. We will discuss themethod in (Hatzivassiloglou and McKeown, 1997) in Section 6.2.*Gradability is a semantic property that enables a word to appear in a*comparative construct and to accept modifying expressions that act asintensifiers ordiminishers .degrees of strength, relative to a norm either explicitly mentioned orimplicitly supplied by the modified noun (for example, a small planet isusuallymuch larger than a large house ). Gradable adjectives were foundusing a seed list of manually compiled adverbs and noun phrases (such as a*little exceedingly ,*, and verymodifiers. Such gradable adjectives are good indicators of subjectivity.In (Yu and Hatzivassiloglou, 2003) Yu and Hatzivassiloglou performedsubjectivity classifications using sentence similarity and a naïve Bayesclassifier. The sentence similaritymethod is based on the assumption thatsubjective or opinion sentences are more similar to other opinion sentencesthan to factual sentences. They used the SIMFINDER system inmeasure sentence similarity based on46shared words, phrases, and WordNet syns ets. For naïve Bayes classification,they used features such as, words (u nigram), bigrams, trigrams, part ofspeech, the presence of sentiment words, the counts of the polarities (ororientations) of sequences of sentiment words (e.g., “++” for twoconsecutive positively oriented words), and the counts of parts of speechcombined with sentiment information (e.g., “JJ+” for positive adjective), aswell as features encoding the sentiment (if any) of the head verb, the mainsubject, and their immediate modifiers. This workalso does sentimentclassification to determine whether a subjective sentence is positive ornegative, which we will discuss in the next section.One of the bottlenecks in applying supervised learning is the manual effortinvolved in annotating a large number of training examples. To save themanual labeling effort, a bootstrapping approach to label training dataautomatically was proposed in (Riloff and Wiebe, 2003). The algorithmworks by first using two high precision classifiers (HP-Subj and HP-Obj) toautomatically identify some subjective and objective sentences. The high-precision classifiers use lists of lexical items (single words or nare good subjectivity clues. HP-Subj classifies a sentence as subjective if itcontains two ormore strong subjective clues. HP-Obj classifies a sentence asobjective if there are no strong subjective clues. These classifiers will givevery high precision but low recall. The extracted sentences are then added to


---

<!-- Página 47 -->

the training data to learn patterns. The patterns (which form the subjectivityclassifiers in the nextiteration) are then used toautomatically identifymoresubjective and objective sentences, which are then added tothe training set,and the next iteration of the algorithm begins.For pattern learning, a set of syntactic templates are provided to restrict thekinds of patterns to be learned. Someexample syntactic templates andexample patterns are shown below.Syntactic template<subj> passive-verb <subj> was satisfied<subj> active-verb <subj> complainedactive-verb <dobj> endorsed <dobj>noun aux <dobj> fact is <dobj>passive-verb prep <np> was worried about <np>Wiebe and Riloff (2005) used so discovered patterns to generate a rule-basedmethod to produce training data for subjectivity classification. The rule-based subjective classifier classifies a sentence as subjective if itcontainstwo or more strong subjective clues (otherwise, it does not label thesentence). In contrast, the rule-based objective classifier looks for theabsence of clues: it classifies a sentence as objective if thereare no strongsubjective clues in the sentence, and several other conditions. The systemalso learns new patterns about objective sentences using the informationextraction system AutoSlog-TS (Riloff, 1996), which finds patterns based onsome fixed syntactic templates. The data produced by the rule-basedclassifiers was used to train a naïve Bayes classifier. A related study wasalso reported in (Wiebe et al., 2004), which used a more comprehensive setof features or subjectivity clues for subjectivity classification.Riloff, Patwardhan and Wiebe (2006) studied relationships among differentfeatures. They defined subsumption relationships among unigrams, n-gramsand lexico-syntactic patterns. If a feature is subsumed by another, thesubsumed feature is not needed. This can remove many redundant features.In (Pang and Lee, 2004), a mincut-based algorithmwas proposed to classifyeach sentence as being subjective or objective. The algorithm works on asentence graph of an opinion document, e.g., a review. The graph is firstbuilt based on local labeling consistencies (which produces an associationscore of two sentences) and individual sentence subjectivity score computedbased on the probability produced bya traditional classification method(which produces a score for each sentence). Local labeling consistencymeans that sentences close to each other are more likely to have the sameclass label (subjective or objective). Th emincut approach is able to improveindividual sentence based subjectivity classification because of the local

Sentiment Analysis and Opinion Mining

47


---

<!-- Página 48 -->

Sentiment Analysis and Opinion Mining

labeling consistencies. The purpose of this work was actually to removeobjective sentences from reviews to improve document level sentimentclassification.

48

Barbosa andFeng (2010) classified the subjectivity of tweets (postings onTwitter) based on traditional features with the inclusion of someTwitterspecific clues such as retw eets, hashtags, links, upper case words, emoticons,and exclamation and question marks. For sentiment classification ofsubjective tweets, the same set of features was also used.Interestingly, in (Raaijmakers and Kraai j, 2008), itwas found thatcharactern-grams of subwords rather than words n-grams can also perform sentimentand subjectivity classification well. For example, for the sentence “This car*rocks ”, subword character bigrams are th, hi, is, ca, ar, ro, oc, ck, ks. In*(Raaijmakers, Truong and Wilson, 2 008) and (Wilson and Raaijmakers,2008), word n-grams, character n-gr am and phoneme n-grams were allexperimented and compared for subjec tivity classification. BoosTexter(Schapire and Singer, 2000) was used as the learning algorithm.Surprisingly, their experiments showed that character n-grams performed thebest, and phoneme n-grams performed similarly to word n-grams.Wilson, Wiebe and Hwa (2004) pointed out that a single sentencemaycontain both subjective and objective clauses. It is useful to pinpoint suchclauses. It is also useful to identify the strength of subjectivity. A study ofautomatic subjectivity classification was presented toclassify clauses of asentence bythe strengthdown to four levels deep ( neutral , medium , and highNeutral indicatestheabsence of subjectivity. Strength classification thus subsumes the task ofclassifying a sentence as subjective or objective. The authors usedsupervised learning. Their features included subjectivity indicating wordsand phrases, and syntactic clues generated from the dependency parse tree.Benamara et al. (2011) performed subjectivity classification with fourclasses, S ,*SN**S*sentiment can be positive or negative), OOopinion implied in an objective sentence or sentence segment, Oobjective with no opinion, and SNpositive or negative sentiment). This classification ismore complete andconforms to our discussion earlier and also in Section 2.4, which showedthat a subjective sentence may not be evaluative (with positive or negativesentiment) and an objective sentence can imply sentiment too.Additional works on subjectivity cla ssification of sentences has also beendone in Arabic (Abdul-Mageed, Diab and Korayem, 2011) and Urdulanguages (Mukund and Srihari, 2010) based on different machine learning


---

<!-- Página 49 -->

algorithms using general and language specific features.

## 4.2

If a sentence is classified as being subjective, we determine whether itexpresses a positive or negative opinion. Supervised learning again can beapplied just like that for document-level sentiment classification, and so canlexicon-basedmethods. Before discussing existing algorithms (somealgorithms do not use the subjectivity classification step), let us point out animplicit assumption made in much of the research on the subject.**Assumption of sentence-lev el sentiment classification: A sentence**expresses a single sentiment from a single opinion holder.This assumption is appropriate for simple sentences with one sentiment, e.g.,“.” However, for compoundand complex sentences, a single sentence may express more than onesentiment. For example, the sentence, “ The picture quality of this camera is*amazing and so is the battery life, but the viewfinder is too small for such a**great camera ,” expresses both positive and negative sentiments (or it has*mixed sentiments). For “picture quality” and “battery life,” the sentence ispositive, but for “viewfinder,” it is negative. It is also positive about thecamera as a whole (which is the GE NERAL aspect in Section 2.1).For sentiment classification of subjective sentences, Yu andHatzivassiloglou (2003) used a method similar to that in (Turney, 2002),which has been discussed in Section 3.2. Instead of using one seed word forpositive and one for negative as in (Turney, 2002), this work used a large setof seed adjectives. Furthermore, instead of using PMI, this work used amodified log-likelihood ratio to determine the positive or negativeorientation for each adjective, adve rb, noun and verb. To assign anorientation to each sentence, it usedth e average log-likelihood scores of itswords. Two thresholds were chosen using the training data and applied todetermine whether the sentence has a positive, negative, or neutralorientation. The same problemwas also studied in (Hatzivassiloglou andWiebe, 2000) considering gradable adjectives.In (Hu and Liu, 2004), Huand Liu proposed a lexicon-based algorithm foraspect level sentiment classification, but the method can determine thesentiment orientation of a sentence as well. It was based on a sentimentlexicon generated using a bootstrapping strategy with some given positiveand negativesentiment word seeds and the synonyms and antonymsrelations in WordNet. We will discuss various methods for generating

Sentiment Analysis and Opinion Mining

49


---

<!-- Página 50 -->

Sentiment Analysis and Opinion Mining

sentiment lexicons in Chapter 6. The sentiment orientation of a sentence wasdetermined by summing up the orientation scores of all sentiment words inthe sentence. A positive word was given the sentiment score of +1 and anegative word was given the sentiment score of -1. Negation words andcontrary words (e.g., but however ) were also considered. In (Kim andHovy, 2004), a similar approach was also used. Their method of compilingthe sentiment lexicon was also similar. However, they determined thesentiment orientation of a sentence bymultiplying the scores of thesentiment words in the sentence. Again, a positive word was given thesentiment score of +1 and a negative word was given the sentiment score of-1. The authors also experimented wi th two other methods of aggregatingsentiment scores but theywere inferior. In (Kim and Hovy, 2007; Kim andHovy, 2004; Kim et al., 2006), supervised learning was used to identifyseveral specific types of opinions. In (Nigam and Hurst, 2004), Nigam andHurst applied a domain specific lexicon and a shallow NLP approach toassessing the sentence sentiment orientation.In (Gamon et al., 2005), a semi-supervised learning algorithm was used tolearn from a small set of labeled sentences and a large set of unlabeledsentences. The learning algorithm was based on Expectation Maximization50work performed three-class classification, positive, negative, and “other" (noopinion or mixed opinion).In (McDonald et al., 2007), the author spresented a hierarchical sequencelearning model similar to conditional random fields (CRF) (Lafferty,McCallum and Pereira, 2001) to jointly learn and infer sentiment at both thesentence-level and the document-level. In the training data, each sentencewas labeled with a sentiment, and each whole review was also labeled with asentiment. They showed that learning both levels jointly improved accuracyfor both levels of classification. In (Täckström and McDonald, 2011), amethod was reported that learns from the document level labelingonly butperforms both sentence and document level sentiment classification. Themethod is thus partially supervised. In (Täckström and McDonald, 2011), afully supervised model and a partially supervised model were integrated toperformmulti-level sentiment classification.In (Hassan, Qazvinian and Radev, 2010), a method was proposedto identifyattitudes about participants in online discussions. Since the paper was onlyinterested in the discussion recipient, the algorithm only used sentencesegments with second person pronouns. Its first step finds sentences withattitudes using supervised learning. The features were generated usingMarkov models. Its second step determines the orientation (positive ornegative) of the attitudes, for which it used a lexicon-based method similar


---

<!-- Página 51 -->

to that in (Ding, Liu and Yu, 2008) except that the shortest path in thedependence tree was utilized to determ ine the orientation when there wereconflicting sentiment words in a sentence, while (Ding, Liu and Yu, 2008)used words distance (see Section 5.1).In (Davidov, Tsur and Rappoport, 20 10), sentiment classification of Twitterpostings (or tweets) was studied. Each tweet is basically a single sentence.The authors took a supervised learning approach. Apart from the traditionalfeatures, themethod alsoused hashtags, smileys, punctuations, and theirfrequent patterns. These features were shown to be quite effective.

## 4.3

Much of the existing research on senten ce-level subjectivity classification orsentiment classification focused on solving the general problem withoutconsidering that different types of sentencesmay needvery differenttreatments. Narayanan, Liu and Choudhary (2009) argued that it is unlikelyto have a one-technique-fit-all solution because different types of sentencesexpress sentiments in very different ways. A divide-and-conquer approachmay be needed, i.e., focused studies ondifferent types of sentences. Theirpaper focused on conditional sentences, which have some uniquecharacteristics that make ithard for a system to determine their sentimentorientations.Conditional sentences are sentences that describe implications orhypothetical situations and their consequences. Such a sentence typicallycontains two clauses: the condition cl ause and the consequent clause, thatare dependent on each other. Their relationship has significant impact onwhether the sentence expresses a positive or negative sentiment. A simpleobservation is that sentiment words (e.g., great ,, ) alone cannotdistinguishan opinion sentence from a non-opinion one, e.g., “If someone*makes a reliable car, I willbuy it ” and “ If your Nokia phone is not good, buy**this Samsung phone .”. The first sentence expr esses no sentiment towards*any particular car, although” is a positive sentiment word, but thesecond sentence is positive about the Samsung phone and it does not expressan opinion about the Nokia phone (although the owner of the Nokia phonemay be negative about it). Hence, a method for determining sentiments innon-conditional sentences will not work for conditional sentences.supervised learning approach was proposed to deal with the problem using aset of linguistic features, e.g., sentiment words/phrases and their locations,POS tags of sentiment words, tense patterns, conditional connectives, etc.Another typeof difficult sentences is the question sentences. For example,

Sentiment Analysis and Opinion Mining

51


---

<!-- Página 52 -->

Sentiment Analysis and Opinion Mining

“?” clearly has noopinion about anyparticular phone. However, “ Can anyone tell mehow to*fix this lousy Nokia phone ?” has a negative opinion about the Nokia phone.*To my knowledge, there is no study on this problem. I believe that for moreaccurate sentiment analysis, we need to handle different types of sentencesdifferently. Much furthe r research is neededinthis direction.

52

## 4.4

Sarcasm is a sophisticated form of sp eech act in which the speakers or thewriters say or writethe opposite of what they mean. Sarcasm has beenstudied in linguistics, psychology and cognitive science (Gibbs and Colston,2007; Gibbs, 1986; Kreuz and Caucci, 2007; Kreuz and Glucksberg, 1989;Utsumi, 2000)). In the context of sentim ent analysis, itmeans that when onesays something positive he/she actuallymeans negative, and vice versa.Sarcasm is very difficult to deal with. Some initial work has beendone in(González-Ibáñez, Muresan and Wacholder, 2011; Tsur, Davidov andRappoport, 2010). Based onmy own experiences, sarcastic sentences are notvery common in reviews of products and services, but they are very frequentin online discussions and commentaries about politics.In (Tsur, Davidov and Rappoport, 2010), a semi-supervised learningapproach was proposed to identify sarcasms. It used a small set of labeledsentences (seeds), but did not use unlabeled examples. Instead, it expandedthe seed setautomatically through We b search. The authors posited thatsarcastic sentences frequently co-occur in texts with other sarcasticsentences. An automated web search using each sentence in the seed trainingset as a query was performed. The system then collected up to 50 searchengine snippets for each seed example and added the collected sentences tothe training set. This enriched training set was then used for learning andclassification. For learning, it used two types of features, pattern-basedfeatures and punctuation-based featur es. A pattern is simply an orderedsequence of high frequency words. Two criteria were also designed toremove too general and too specific patterns. These patterns are similar tosequential patterns indatamining (Liu, 2006 and 2011). Punctuation-basedfeatures include the number of “!”, “?” and quotes, and the number ofcapitalized/all capital words in the sentence. For classification, a kmethod was employed. This work, however, did not perform sentimentclassification. It only separated sa rcastic and non-sarcastic sentences.The work of González-Ibáñez, Muresan and Wacholder (2011) studied theproblem in the context of sentiment analysis using Twitter data, i.e., to


---

<!-- Página 53 -->

distinguish sarcastic tweets and non-sa rcastic tweets that directly conveypositive or negative opinions (neutral utterances were not considered).Again, a supervised learning approach was taken using SVM and logisticregression. As features, they used unigrams and some dictionary-basedinformation. The dictionary-based fe atures include (i) word categories(Pennebaker et al., 2007); ii) Word Net Affect (WNA) (Strapparava andValitutti, 2004); and iii) a list of interjections (e.g., ah, oh, yeah), andpunctuations (e.g., !, ?). Features like emoticons, and ToUser (which marksif a tweet is a reply to another tweet, signaled by <@user>) were also used.Experimental results for three-way classification (sarcastic, positive andnegative) showed that the problem is very challenging. The best accuracywas only 57%. Again, this work did no t classify sarcastic sentences intopositive and negative classes.

## 4.5 Cross-language Subjectivity and

## Sentiment Classification

As in document-level cross-language sentiment classification, researchershave also studied cross-language subjectivity classification and sentimentclassification at the sentence level. Again, the research focused on usingextensive resources and tools available inEnglish and automated translationsto help build sentiment analysis systems in other languages which have fewresources or tools. Current research proposed threemain strategies:(1) Translate test senten ces in the target language into the source languageand classify them using a source language classifier.

(2). Translate a source language training corpus into the target language andbuild a corpus-based classifier in the target language.

(3). Translate a sentiment or subjectivity lexicon in the source language tothe target language and build a lexi con-based classifier in the targetlanguage.

Kim and Hovy (2006) experimented with (1) translating German emails toEnglish and applied English sentiment words to determine sentimentorientation, and (2) translating English sentiment words to German, andanalyzing German emails using German sentiment words. Mihalcea, Baneaand Wiebe (2007) also experimented with translating English subjectivitywords and phrases into the target language. In fact, they actually tried twotranslation strategies for cross-language subjectivityclassification. First,theyderiveda subjectivity lexicon for the newlanguage (in their case,Romanian) using an English subjectivitylexicon through translation. A rule-based subjectivity classifier similar to that in (Riloff and Wiebe, 2003) was

Sentiment Analysis and Opinion Mining

53


---

<!-- Página 54 -->

Sentiment Analysis and Opinion Mining

then applied to classify Romanian sentences intosubjective and objectiveclasses. The precision was not bad, but the recall was poor. Second, theyderived a subjectivity-annotated corpus in the new language using amanually translated parallel corpus. They first automatically classifiedEnglish sentences in the corpus into subjective and objective classes usingsome existing tools, and then projected the subjectivity class labels to theRomanian sentences in the parallel cor pus using the available sentence-levelalignment in the parallel corpus. A subjectivityclassifier based onsupervised learning was then built inRomanian to classify Romaniansentences. In this case, the result was better than the first approach.However, it should be noted that the translation of the parallel corpus wasdone manually.In (Banea et al., 2008), three sets of experiments were reported. First, alabeled corpus in the sourcelanguage (English) was automatically translatedinto the target language (Romanian). The subjectivity labels in the sourcelanguage were then mapped to the translated version in the target language.Second, the source language text was automatically labeled for subjectivityand then translatedinto the target la nguage. In both cases, the translatedversion with subjectivity labels in the target language was used to train asubjectivity classifier in the target language. Third, the target language wastranslated into the source language, and then a subjectivity classification tool54classification, the labels were mapped back into the target language. Theresulting labeled corpus was then used to train a subjectivity classifier in thetarget language. The final classificati on results were quite similar for thethree strategies.In (Banea, Mihalcea and Wiebe, 2010 ), extensive experiments for cross-language sentence level subjectivity classification were conducted bytranslating from a labeled English corpus to 5 other languages. First, it wasshown that using the translated corpus for training worked reasonably wellconsistently for all 5 languages. Combining the translated versions indifferent languages withthe original English version to form a singletraining corpus can also improve the original English subjectivityclassification itself. Second, the paper demonstrated that by combining thepredictions made by monolingual classifiers using majority vote, it was ableto generate a high precision sentence-level subjectivity classifier.The technique in (Bautin, Vijayarenu and Skiena, 2008) also translateddocuments in the target language to English and used a English lexicon-based method to determine the sentiment orientation for each sentencecontaining an entity. This paper actually worked atthe aspect level. Thesentiment classification method was similar to that in (Hu and Liu, 2004).In (Kim, Li and Lee, 2010), a concept called the multi-lingual comparability


---

<!-- Página 55 -->

was introduced toevaluatemulti-lingualsubjectivity analysis systems. Bymultilingual comparability, they meant the level of agreement in theclassification results of a pair of multilingual texts with an identicalsubjective meaning. Using a parallel corpus, they studied the agreementamong the classification results of the source language and the targetlanguage using Cohen’s Kappa. For the target language classification,several existing translation based cross-language subjectivityclassificationmethods were experimented. Their results showed that classifiers trained oncorpora translated from English to th e targetlanguages performed well forboth subjectivity classification and multi-lingual comparability.In (Lu et al., 2011), a slightly different problem was attempted. The paperassumed that there was a certain amount of sentiment labeled data availablefor both the source and target languages, and there was also an unlabeledparallel corpus. Their method can simultaneously improve sentimentclassification for both languages. The method is a maximum entropy-basedEM algorithm which jointly learns two monolingual sentiment classifiers bytreating the sentiment labels in the unlabeled parallel text as unobservedlatent variables, and maximizing the regularized joint likelihood of thelanguage-specific labeled data together with the inferred sentiment labels ofthe parallel text. In learning, it exploits the intuition that two sentences ordocuments that are parallel (i.e., translations of one another) should exhibitthe same sentiment.

## 4.6

## Sentiment Classification

Most existing works on both the docu ment-level and the sentence-levelsentiment classification do not use the discourse information either amongsentences or among clauses in the same sentence. Sentiment annotation atthe discourse level was studied in (Asher, Benamara and Mathieu, 2008;Somasundaran, Ruppenhofer and Wiebe, 2008). Asher, Benamara andMathieu (2008) used five types of rhetorical relations: Contrast,*Support , , and Continuation with attached sentiment information for*annotation. Somasundaran, Ruppenhofer and Wiebe (2008) proposed aconcept called opinion frame .opinions and the relationships between their targets.In (Somasundaran et al., 2009), Soma sundaran et al. performed sentimentclassification based on the opinion frame annotation. The classificationalgorithm used was collective classification (Bilgic, Namata and Getoor,

,

Sentiment Analysis and Opinion Mining

55


---

<!-- Página 56 -->

Sentiment Analysis and Opinion Mining

2007), which performs classification on a graph. The nodes are sentences (orother expressions) that need to be classified, and the links are relations. Inthe discourse context, they are sentim ents related discourse relations. Theserelations can be used to generate a set of relational features for learning.Each node itself also generates a set of local features. The relational featuresallow the classification of one node to affect the classification of other nodesin the collective classification scheme. In (Zhou et al., 2011), the discourseinformation within a single compound sentencewas used to performsentiment classification of the sentence. For example, the sentence“*loved by the domestic population because people hated the corruptedruling**class ” is a positive sentence although it has more negative opinion words*(see also Section 4.7). This paper used pattern mining to find discoursepatterns for classification.In (Zirn et al., 2011), the authors proposed a method to classify discoursesegments. Each segment expresses a single (positive or negative) opinion.Markov logic networks were used for classification which not only canutilize a sentiment lexicon but also the local/neighboring discourse context.56

## 4.7 Summary

Sentence level subjectivity classification and sentiment classification goesfurther than document level sentiment classification as it moves closer toopinion targets and sentiments on the targets. It can be regarded as an

intermediate

step in the overall sentiment analysis task. However, it still hasseveral shortcomings for many real-life applications:entities or aspects of entities are liked anddisliked. Asthe documentlevel, the sentence level analysis still does not dothat.and aspects, or topics), we can assign the sentiment orientation of asentence to the targets in the sentence. However, this is insufficient:(1) Many complex sentences have different sentiments on differenttargets, e.g., “ Trying out Chrome becauseFirefox keeps crashing” and“.” In this lattersentence, even theclauselevel classification is insufficient. We needto go to the opinion target or the aspect level.(2) Although a sentencemay have an overall positive or negative tone,some of its components may express opposite opinions. For example,some researchers regard the follow sentence as positive


---

<!-- Página 57 -->

(Neviarouskaya, Prendinger and Ishizuka, 2010; Zhou et al., 2011):“*Despite the high unemployment rate, the economy is doing well.”*is trying toemphasize the positive side, but it does contain a negativesentiment on the unemployment rate , which we must not ignore. If wego to the aspect-level sentiment anal ysis, the problem is solved. Thatis, the sentence is positive about the overall economy but negativeabout the unemployment rate.(3) Sentence level sentiment classification cannot deal with opinions incomparative sentences, e.g., “ Coke tastes better than Pepsi.” In thiscase, we need differentmethods toextract andto analyzecomparativeopinions as they have quitedifferent meanings from regular opinions.Although this sentence clearly expresses an opinion, we cannot simplyclassify the sentence as being positive, negative or neutral.We discuss aspect-level sentiment analysis in the next chapter andcomparative opinion analysis in Chapter 8.

Sentiment Analysis and Opinion Mining

57


---

<!-- Página 58 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 5

58

## Aspect-based Sentiment Analysis

Following the natural progression of chapters, this chapter should focus onphrase and word-level sentiment classifi cation as the last two chapters wereabout document and sentence-level classification. However, we leave thattopic to thenext chapter. In this chapter, we focus on aspect-basedsentimentanalysis as it is time to deal with the full problem defined in Chapter 2 andmany phrase and word sentiments dependon aspect contexts.As we discussed inthe two previous chapters, classifying opinion texts at thedocument level or the sentence level is often insufficient for applicationsbecause they do not identify opiniontargets or assign sentiments to suchtargets. Evenif we assume that each document evaluates a single entity, apositive opinion document about the entity does not mean that the author haspositive opinions about all aspects of the entity. Likewise, a negative opiniondocument does not mean that the author is negative about everything. Formore complete analysis, we need to discover the aspects and determinewhether the sentiment is positive or negative on each aspect.To extract such details, we go to the aspect level, which means that we needthe full model of Chapter 2, i.e., aspect-based sentiment analysis (or*mining ), which was also called the feature-based opinion mining in (Hu and*Liu, 2004). Note that as discussed in Chapter 2, the opinion target isdecomposed into entity and its aspect s. The aspect GENERAL is used torepresent theentity itself in the result. Thus aspect-based sentiment analysiscovers both entities and aspects. It al so introduces a suite of problems whichrequire deeper NLP capabilities and produce a richer set of results.Recall that, at the aspect level, the ob jective is to discover every quintuple(

,,,,) in a given document dto be performed. This chapter mainly focuses on the two core tasks listed*i**ij**ijkl**k**l*below. They have been studied extens ively by researchers. The other taskswill also be covered but relatively briefly.1.: This task extracts aspects that have been evaluated.For example, in the sentence, “ The voice quality of this phone is*amazing ,” the aspect is “voice quality” of the entity represented by “this*phone.” Note that “this phone” does not indicate the aspect GENERALhere because the evaluation is not about the phone as a whole, but onlyabout its voice quality. However, the sentence “I love thisphone”


---

<!-- Página 59 -->

evaluates the phoneas a whole, i.e., the GENERAL aspectof the entityrepresented by “this phone.” Bear in mind whenever we talkabout anaspect, wemust know which entity it belongs to. In our discussion below,we often omit the entityjustfor simplicity of presentation.2.: This task determines whether theopinions on different aspects are positive, negative, or neutral. In the firstexample above, the opinion on the “voice quality” aspect is positive. Inthe second, the opinion on the aspect GENERAL is also positive.Note that it is possible that in an application the opinion targets are givenbecause the user is only interested in these particular targets (e.g., the BMWand Ford brands). In that case, we do not need to perform entity or aspectextraction, but only to determine the sentiments on the targets.

## 5.1 Aspect Sentiment Classification

We study the second task first, i.e., determining the orientation of sentimentexpressed on each aspect in a sentence . There are two main approaches, i.e.,the supervised learning approach and the lexicon-based approach.For the supervised learning approach, the learning basedmethods used forsentence-level and clause-level sentiment classification discussed in Chapter4 are applicable. In (Weiand Gulla, 2010), a hierarchical classificationmodel was also proposed. However, the key issue is how to determine thescope of each sentiment expression, i.e., whether itcovers the aspect ofinterest in the sentence. The current main approachis to use parsing todetermine the dependencyand the other relevant information. For example,in (Jiang et al., 2011), a dependency parser was used to generate a set ofaspect dependent features for classification. A related approach was alsoused in (BoiyandMoens, 2009), which weights each feature based on theposition of the feature relative to the target aspect in the parse tree. Forcomparative sentences, “than” or other related words can be used to segmenta sentence (Ding, Liu and Zhang, 2009; Ganapathibhotla and Liu, 2008).Supervised learning is dependent on the training data. As we discussed inSection 3.4, amodel or classifier trained from labeled data in one domainoften performs poorly in another domain. Although domain adaptation (ortransfer learning) has been studie d by researchers (Section 3.4), thetechnology isstill far frommature, and the current methods are alsomainlyused for document level sentiment clas sification as documents are long andcontain more features for classification than individualsentences or clauses.Thus, supervised learninghas difficulty to scale up to a large number ofapplication domains.

Sentiment Analysis and Opinion Mining

59


---

<!-- Página 60 -->

Sentiment Analysis and Opinion Mining

The lexicon-based approach can avoid some of the issues (Ding, Liu and Yu,2008; Hu and Liu, 2004), and has been shown to perform quite well in alarge number of domains. Such methods are typically unsupervised. Theyuse a sentiment lexicon (which contains a list of sentiment words, phrases,and idioms), composite expressions, rules of opinions (Section 5.2), and(possibly) the sentence parse tree to determine the sentiment orientation oneach aspect in a sentence. They also consider sentiment shifters,(see below) and many other constructs whichmay affect sentiments. Ofcourse, the lexicon-based approach also has its own shortcomings, which wewill discuss later. An extension of thismethod tohandling comparativesentences will be discussed in Section 8.2. Below, weintroduce onesimplelexicon-basedmethod to give a flavor of this approach. The method is from(Ding, Liu and Yu, 2008) and it has four steps. Here, we assume that entitiesand aspects are known. Their extraction will be discussed in Section 5.3.1.: For each sentence that containsone or more aspects, this step mark s all sentiment words and phrases inthe sentence. Each positive word is assigned the sentiment score of +1and each negative word is assigned the sentiment score of example, we have the sentence, “ The voice quality of this phone is not” After this step, the sentence becomes60“The voice quality of this phone is not [+1], but the batterylifeislong” because “good” is a positive sentiment word (the aspects in thesentence are italicized). Note that “long” here is not a sentiment word asit does not indicate a positive or negative sentiment by itself in general,but we can infer its sentiment in this context shortly. In fact, “long” canbe regarded as a context-dependent sentiment word, which we willdiscuss in Chapter 6. Inthe next section, we will see some otherexpressions that can give or imply positive or negative sentiments.2.Sentiment shifters (also called valence*shifters in (Polanyi and Zaenen, 2004)) are words and phrases that can*change sentiment orientations. There are several types of such shifters.Negation words like not never , ,,,, and*cannot are themost common type. This step turns our sentence into “The**voice quality of this phone is not good [-1], but the battery life is long”*due to the negation word “not.” We will discuss several other types ofsentiment shifters in the next section. Note that not every appearance of asentiment shifter changes the sentiment orientation, e.g., “not only … butalso.” Such cases need tobe dealt withcare. That is, such special usesand patterns need to be identified beforehand.3.: Words or phrases that indicate contrary needspecial handling because they often change sentiment orientations too.


---

<!-- Página 61 -->

The most commonly usedcontrary word in English is “but”. A sentencecontaining a contrary word or phrase is handled by applying thefollowing rule: the sentiment orientations before the contrary word (e.g.,but)site to eachother if the opinionon one side cannot be determined. The if-condition in the rule is usedbecause contrary words and phrases do not always indicate an opinionchange, e.g., “ Car-x is great, but Car-yis better .” After this step, theabove sentence is turned into “The voice quality of this phone is not**good [-1], but the battery life is [+1]” due to “but” ([+1] is added at**the end of the but-clause). Notice here, we can infer that “long” ispositive for “battery life”. Apart from butexceptionof,” “except that,” and “except for” also have the meaning ofcontrary and are handled inthe same way. As in the case of negation, notevery butphrases containing need to be identified beforehand.4.: This step applies an opinion aggregation functionto the resulting sentiment scores to determine the final orientation of thesentiment on each aspect in the sentence. Let the sentence be scontains a set of aspects { a

Sentiment Analysis and Opinion Mining

61

, …, a} and a set of sentiment words orphrases { sw1*m* , …, sw} withtheir sentiment scores obtained from steps 1-3. The sentiment orientation for each aspect*a*1*n* infollowing aggregation function:*i*

(5).(,( )where sw

### 

*sw**score a**j**dist a**i* ow s*j**j*

is an sentiment word/phrase in s (,) is the distancebetween aspect a*j**i* and sentiment word swin sw.score of sw*i**j**j* .sentiment words that are far away from aspect*a**i* . If the final score ispositive, then the opinion onaspect a*i* innegative, then the sentiment onthe aspect is negative. It is neutral*i*otherwise.This simple algorithm performs quite well in many cases. It is able to handlethe sentence“ Apple is doing very well in this bad economy” with noproblem. Note that there are many other opinion aggregation methods. Forexample, (Hu and Liu, 2004) simply summed up the sentiment scores of allsentiment words in a sentence or sentence segment. Kim, and Hovy(2004)usedmultiplication of sentiment scores of words. Similar methods were alsoemployed by other researchers (W an, 2008; Zhu etal., 2009).To make thismethod evenmore effective, we can determine the scope ofeach individual sentiment word instead of using words distance as above. In


---

<!-- Página 62 -->

Sentiment Analysis and Opinion Mining

this case, parsing is needed to find the dependency as in the supervisedmethod discussed above. We can also automatically discover the sentimentorientation of context dependent words such as “long” above. More detailswill be given in Chapter 6. In fact, the above simple approach can beenhanced in many directions. For example, Blair-Goldensohn et al. (2008)integrated the lexicon-based method with supervised learning. Kessler andNicolov (2009) experimented with four different strategies of determiningthe sentiment on each aspect/target (includinga ranking method). They alsoshowed several interesting statistics on why it is so hard to link sentimentwords totheir targets based on a large amount of manuallyannotated data.Along with aspect sentiment classificati on research, researchers also studiedthe aspect sentiment rating prediction problem which has mostly been donetogether withaspect extraction in the context of topic modeling, which wediscuss in Section 5.3.4.As indicated above, apart from sentiment words and phrases, there aremanyother types of expressions that can convey or imply sentiments. Most ofthem are also harder to handle. Below, we list someof them, which arecalled the basic rules of opinions (Liu, 2010).62

## 5.2

## Compositional Semantics

An opinion rule expresses a concept that implies a positive or negativesentiment. Itcan be as simple as individual sentiment words with theirimplied sentiments or compound expressions thatmay need commonsenseor domain knowledge to determine their orientations. This section describessome of these rules. One way of representing these rules is to use the idea ofcompositional semantics (Dowty, Wall and Peters, 1981; Montague, 1974),which states that the meaning of a compound expression is a function of themeaning of its constituents and of the syntactic rules by which they arecombined. Below, we first describe the rules at the conceptual level withoutconsidering how they maybe expressed in actual sentences because many ofthese rules can beexpressed innumerous ways and can alsobe domain andcontext dependent. After that, we go to the expression level to discuss thecurrent research on compositional semantics in the context of sentimentanalysis, which aims to combine more than one input constituent expressionsto derive an overall sentiment orientation for thecomposite expression.The rules are presented using a formalism similar to the BNF form. Therules are from (Liu, 2010).


---

<!-- Página 63 -->

Sentiment Analysis and Opinion Mining

1.::= P2. | PO3.4|5.::= N6. | NE7.8.sentiment_shifter POThe non-terminals P and PO represent two types ofpositive sentiment*expressions . P indicates anatomic positive expression, a word or a phrase,*while PO represents a positive expre ssion composed of multiple expressions.Similarly, thenon-terminals N and NE also represent two types of negative*sentiment expressions . “sentiment_shifter N” and “sentiment_shifter NE”*represent the negation of N and NE, re spectively, and “sentiment_shifter P”and “sentiment_shifter PO” represent the negation of P and PO, respectively.We need to note that these are not expressed in the actual BNF form but apseudo language stating some abstract concepts. It is hard to specify themprecisely because in an actual sentence, the sentiment shifter may be inmany different forms and can appear before or after N, NE, P, or PO andthere may be words between the sentim ent shifter and positive (or negative)sentiment expressions. POSITIVE and NEGATIVE are the final sentimentsused to determine the opinions on the targets/aspects in a sentence.Sentiment_shifters (or valence shif ters (Polanyi and Zaenen, 2004)):*Negation words like not never , ,*,,, and*cannot are themost common type of sentiment shifters. Modal auxiliary**verbs (e.g., would , , , , , and ought) are another*type, e.g., “ The brake could be improved ,” which may change sentimentorientation, but not always. Some presuppositional items are yet anothertype. This case is typical for adverbs like barely and hardly as shown bycomparing “ It works ” with “ It hardly works .” “Works” indicates positive,but“hardly works” does not: it presupposes that better was expected.Words like fail , behave similarly, e.g., “This camera fails to*impress me .” Furthermore, sarcasm often changes orientations too, e.g.,*“.” Although itmay not behard to recognize such shifters manually, spotting them and handling

them correctly in actual sentences by an automated system is challenging(see Section 4.4). Also, the rules 11-14 below can be seen as sentimentshifters as well. We present them separatelybecause they also covercomparative opinions. Note that seve ral researchers also studied theapplication scope of negations (Ikeda et al., 2008; Jia, Yu and Meng,2009; Li et al., 2010; Morante, Schrauwen and Daelemans, 2011). We

63


---

<!-- Página 64 -->

Sentiment Analysis and Opinion Mining

will discuss more about sentiment shifters when we discuss sentimentcomposition.We now define N, NE, P, and PO, which contain no sentiment shifters. Wegroup these expressions into six conceptual categories based on theirspecific characteristics.1.: This is the simplest and also the mostcommonly used category, in which sentiment words or phrases alone canimply positive or negative opinions on aspects, e.g., “good” in “The voice*quality is good .” These words or phrasesare reduced to P and N.*9. P10. NAgain, the details of the right-hand sides are not specified (which alsoapply to all the subsequent rules). Much of the current research only useswords and phrases in this category.2.(N and P): Thisset of rules is similar to the negation (or sentiment shifter) rules 3, 4, 7,and 8 above. They express that decreasing or increasing the quantityassociated with an opinionated item (often nouns and noun phrases) canchange the orientation of the sentiment. For example, in the sentence64“,word, and the reduction of “pain” indicates a desirable effect of thedrug.Thus, decreased painimplies a positive opinion on the drug. The conceptofalso extends to removal and disappearance , e.g., “ My pain*disappeared after takingthedrug .” We then have the following rules:*11. ::= less_or_decreased N12.|13. ::= less_or_decreased P14.|Note that rules 12 and 14 do notchange of sentiment orientation, but theycan change the intensity of an opin ion. The actual words or phrasesrepresenting the concepts of less_or_decreased andmore_or_increased ina sentence may appear before or after N or P, e.g., “ My pain has subsided*after taking the drug ,” and “ This drug hasreduced my pain.”*3.*potential item : For some items, a small value/quantity of them is*negative, and a large value/quantity of them is positive, e.g., “The battery*life is short ” and “ The battery life is long .” We call such items positive**potential items*some other aspects, a small value/quantity of them is positive, and a largevalue/quantity of them is negative, e.g., “ This phone costs a lot” and


---

<!-- Página 65 -->

“.” Such items are called negative*potential items*Both positive and negative potential items themselves imply no opinions,i.e., “battery life” and “cost”, but wh en they are modified byquantityadjectives or quantity change words or phrases, positive or negativesentiments may be implied. The following rules cover these cases:15. ::= no_low_less_or_decreased_quantity_of NPI16.|17. ::= no_low_less_or_decreased_quantity_of PPI18.|19. ::=20. ::=In (Wen and Wu, 2011), a bootstrapping and classification methodwasproposed to discover PPI and NPI in Chinese.4.: The rules above all contain somesubjective expressions. But objective expressions can imply positive ornegative sentiments too as they can describe desirable and undesirablefacts. Such sentences often do not us e any sentiment words. For example,the sentence “ After my wifeand I slept on the mattress for two weeks, I*saw a mountain in the middle ” clearly implies a negative opinion about*the mattress. However, the word “mountain” itself does not carry anyopinion. Thus, we have the following two rules:21. ::= desirable_fact22. ::= undesirable_fact5.: In some applicationdomains, the value of an item has a desired range or norm. If the valuedeviates from the normal range, it is negative, e.g., “After takingthe*drug, my blood pressure went to 410 .” Such sentences are often objective*sentences as well. We thus have the following rules:23. ::= within the_desired_value_range24. ::= deviate_from the_desired_value_range6.: If an entity produces a largequantity of resources, it is desirabl e (or positive). If it consumes a largequantity of resources, it is undesirable (or negative). For example,*electricity is a resource. The sentence, “ This computer uses a lot of**electricity ” gives a negative opinion about power consumption of the*computer. Likewise, if an entity produc es a large quantity of wastes, it isnegative. If it consumes a large quantity of wastes, it is positive. Thesegive us the following rules:

Sentiment Analysis and Opinion Mining

65


---

<!-- Página 66 -->

Sentiment Analysis and Opinion Mining

25. ::= produce a_large_quantity_of_or_more resource26.|27.|28.|29. ::= produce no,_little_or_less resource30.|31.|32.|These conceptual rules can appear in many (seemly unlimited number of)forms using different wordsand phrases in actual sentences, and indifferentdomains theymay also manifest in different ways. Thus, they are very hardto recognize. Without recognizing them, the rules cannot be applied.This set of conceptual rules is by no means the complete set that governsopinions or sentiments. In fact, there are others, and with further research,more rules may be discovered. It is also important to note that like individualsentiment words an occurrence of any of the rules in a sentence does notalways imply opinions. For example, “ I want acar with high reliability”does not express a positive or negative opinion on any specific car, although“high reliability” satisfies rule 16. More complex rules or discourse level66analysismay beneeded to deal with suchsentences.We now discuss the existing work applying the principle of compositionalityto express some of the above rules at the expression level. The most studiedcomposition rules are those related to sentiment reversal, which arecombinations of sentiment shifters and positive or negative sentiment words,e.g., “ not*good ”) => NEG(“ not good ”). We have discussed them*at length above. Another maintypeis represented by rules 11 to 14 above,e.g., “ reduced ” & NEG(“ pain*reduced pain ”).*Such composition rules can express some of the opinion rules and alsocertainother expression level sentiment compositions. Apart from the abovetwo composition types, Moilanen and Pulman (2007) also introduced*sentiment conflict , which is used whenmultiple sentiment words occur*together, e.g., “ terribly good ”. Conflict resolution is achieved by ranking theconstituents on the basis of relative weights assigned tothem dictating whichconstituent is more important with respect to sentiment.In (Neviarouskaya, Prendinger and Ishizuka, 2010), six types of compositionrules were introduced, i.e., sentiment reversa l, aggregation,,*domination ,*, and intensification . Sentiment reversal is thesame as what we have discussed above. Aggregation is similar to sentiment*conflict above, but defined differently. If the sentiments of terms in*adjective-noun, noun-noun, adverb-adjective, adverb-verb phrases have


---

<!-- Página 67 -->

opposite directions, mixed polarity with dominant polarity of a pre-modifieris assigned to the phrase, e.g., POS(‘ beautiful ’) & NEG(‘fightPOSneg(‘ beautiful fight ’). The rule of propagation is applied when a verb of“propagation” or “transfer” type is used in a phrase/clause and the sentimentof an argument that has prior neutral polarity needs to be determined, e.g.,PROP-POS(“ to admire ”) & “ his behavior ” => POS(“*X**supports ”) & NEG(“ crime business ”) => NEG(‘ Mr. X’). The*rules of domination are: (1) if polarities of a verb and an object in a clausehaveopposite directions, the polarity ofverb is prevailing (e.g., NEG(“to*deceive ”) & POS(“ hopes ”) => NEG(“ to deceive hopes”)); (2) if a compound*sentence joints clauses using the coordinate connector “butfeatures of the clause following after the conne ctor are dominant (e.g.,‘NEG(“ It was hard to climb a mountain all night long”),POS(“a*magnificent view rewarded th e traveler at the morning”).’ => POS(whole*sentence)). The rule of neutralization is applied when apreposition-modifieror condition operator relates to a sentiment statement, e.g., “despite” &NEG(‘ worries ’) => NEUT(“ despite worries ”). The rule of intensificationstrengthensPos_score(“ happy ”) < Pos_score(“ extremely happy”)). Additional relatedworks can be found in (Choi and Cardie, 2008; Ganapathibhotla and Liu,2008; Min and Park, 2011; Nakagawa, Inui and Kurohashi, 2010; Nasukawaand Yi, 2003; Neviarouskaya, Prendinger and Ishizuka, 2009; Polanyi andZaenen, 2004; Socher et al., 2011; Yessenalina and Cardie, 2011).As we can see, some of the opinion rules have notbeen expressed withcompositions, e.g., those involved in resource usages (rules 25–32).However, it is possible to express them to some extent using triples in(Zhang and Liu, 2011a). The desirable and undesirable facts or value rangeshave not been included either (rules 21 –24). They are, in fact, not directlyrelated to composition because they are essentially context or domainimplicit sentiment terms, which need to be discovered in a domain corpus(Zhang and Liu, 2011b).

## 5.3 Aspect Extraction

We now turn to aspect extraction, whic h can also be seen as an informationextraction task. However, in the context of sentiment analysis, somespecificcharacteristics of the problem can facilitate the extraction. The keycharacteristicis that an opinion always has a target. The targetis often theaspector topic to be extracted from a sentence. Thus, it is important torecognize each opinion expression and its target froma sentence. However,

”); “

Sentiment Analysis and Opinion Mining

67


---

<!-- Página 68 -->

Sentiment Analysis and Opinion Mining

we should also note that some opinionexpressions can play two roles, i.e.,indicating a positive or negative sentiment and implying an (implicit) aspect(target). For example, in “ this car is expensive ,” “expensive” is a sentimentword and also indicates the aspect price . We will discuss implicit aspects inSection 5.3.5. Here, we will focus on explicit aspect extraction. There arefour main approaches:1.2.3.4.Since existing researchon aspect extraction (more precisely, aspect*expression extraction ) is mainly carried out inonline reviews, we also use*the review context todescribe these techniques, but there is nothing toprevent thembeing used onother forms of social media text.There are two common review formats on the Web.Format 1 The reviewer firstdescribes some brief pros and cons separately and then writes adetailed/full review. An example of such a review is given in Figure 5.1.Format 2 The reviewer writes freely, i.e., no brief pros andcons. An example of such a review is given in Figure 5.2.Extracting aspects fromPros and Cons in reviews of Format 1 (not thedetailed review, which is the same as that in Format 2) is a special case ofextracting aspects from the full review and also relatively easy. In (Liu, Huand Cheng, 2005), a specific method based ona sequential learningmethodwas proposedto extract aspects from Pros and Cons, which also exploited akey characteristic of Pros and Cons, i.e., they are usually very brief,consisting of short phrases or senten cesegments. Each segment typicallycontains only one aspect. Sentence se gments can be separated by commas,periods, semi-colons, hyphens, & ,extraction algorithm to performmore accurately.Since the same set of basic techniques can be applied to both Pros and Consand full text, from now on we will not distinguish them, but will focus ondifferent approaches.

### 5.3.1 Finding Frequent Nouns and Noun Phrases

This method finds explicit aspect expressions thatare nouns and nounphrases froma large number of reviews in a given domain. Hu and Liu(2004) used a data miningalgorithm. Nouns and noun phrases (or groups)


---

<!-- Página 69 -->

**Figure 5.1. An example of a review of format 1.****GREAT Camera. , Jun 3, 2004**Reviewer: jprice174 from Atlanta, Ga.I did a lot of research last year be fore I bought this camera... It kindahurt to leave behind my beloved nikon 35mmSLR, but I was going toItaly, and I needed something smaller, and digital.The pictures coming out of this cam era are amazing. The'auto' featuretakes great pictures most of the time. And with digital, you're notwasting film if the picture doesn't come out. …**Figure 5.2. An example of a review of format 2.**

were identified by a part-of-sp eech (POS) tagger. Their occurrencefrequencies are counted, and only the frequent ones are kept. A frequencythreshold can be decided experimentally. The reason that this approachworks is that when people comment on differentaspects of anentity, thevocabulary that they use usually conv erges. Thus, those nouns that arefrequently talked about ar e usually genuine and important aspects. Irrelevantcontents in reviews are often diverse, i. e., they are quite different in differentreviews. Hence, those infrequent nouns are likelyto be non-aspectsor lessimportant aspects. Although this method is very simple, it is actually quiteeffective. Some commercial companies are using thismethod with severalimprovements.The precisionof thisalgorithmwas improved in (Popescu and Etzioni,2005). Their algorithm tried to remove those noun phrases that may not beaspects of entities.pointwise mutual information (PMI) score between the phrase and some*meronymy discriminators associatedwiththe entity class, e.g., a camera*class. The meronymy discriminators for the camera class are, “of camera,”“camera has,” “camera comes with,” etc., which were used to findcomponents or parts of cameras by searching the Web. The PMI measurewas a simplified version of that in Section 3.2:

**Pros: Great photos, easyto use, verysmall****Cons: Battery usage; included memory is stingy.**I had never useda digital camera prior topurchasing this Canon A70.I have always useda SLR … Read the full review

Sentiment Analysis and Opinion Mining

69



**My SLR is on the shelf**by camerafun4. Aug 09 ‘04

 (4)*hits d**PMI a**hits ) d*where aidentified using the frequency approach and dis a discriminator. Web search was used to find the number of hits of


---

<!-- Página 70 -->

Sentiment Analysis and Opinion Mining

individual terms and alsotheir co-occurrences. The idea of this approach isclear. If the PMI value of a candidateaspect is too low, it may not be acomponent of the product because a dalgorithm also distinguishes components/parts from attributes usingWordNet’s is-aandmorphological cues (e.g., “-iness,” “-ity” suffixes).Blair-Goldensohn et al. (2008) refined the frequent noun and noun phraseapproach by considering mainlythose nounphrases thatare insentiment-bearing sentences or in some syntactic patterns which indicate sentiments.Several filters were applied to remove unlikely aspects, e.g., droppingaspects which do not havesufficient mentions along-side known sentimentwords. They also collapsedaspects at the word stem level, and ranked thediscovered aspects by a manually tuned weighted sum of their frequency insentiment-bearing sentences and the type of sentiment phrases/patterns, withappearances in phrases carrying a grea ter weight. Using sentiment sentencesis related to the approach inSection 5.3.2.A frequency-based approach was also taken in (Ku, Liang and Chen, 2006).The authors called the sodiscovered terms the major topics. Their methodalsomade use of the TF-IDF scheme considering terms at the document70the frequency-based approach with an additional pattern-based filter toremove some non-aspect terms. Their work also predicted aspect ratings.Scaffidi et al. (2007) compared the frequency of extracted frequent nounsand nounphrases in a review corpus with their occurrence rates in agenericEnglish corpus to identify true aspects.Zhu et al. (2009) proposed a method based on the Cvalue measure from(Frantzi, Ananiadou and Mima, 2000) for extracting multi-word aspects. TheCvalue method is also based on frequency, but it considers the frequency ofmulti-word term t*t**t*However, Cvalue onlyhelped find a set of candidates, which is then refinedusing a bootstrapping technique with a set of given seed aspects. The idea ofrefinement is based on each candidate’s co-occurrence with the seeds.Long, Zhang and Zhu (2010) extracted aspects (nouns) based on frequencyand information distance. Their method first finds the core aspect wordsusing the frequency-based method. It then uses the information distance in(Cilibrasi and Vitanyi, 2007) to find other related words to an aspect, e.g.,for aspect price , it may find “$” and “dollars”. All these words are then usedto select reviews which discuss a particular aspect most.


---

<!-- Página 71 -->

### 5.3.2 Using Opinion and Target Relations

Since opinions have targets, they are obviously related. Their relationshipscan be exploited to extract aspects which are opinion targets becausesentiment words are often known. This method was used in (Hu and Liu,2004) for extracting infrequent aspects. The ideais as follows: The samesentiment word can be used to describe or modify different aspects. If asentence does not have a frequent aspectbut has some sentiment words, thenearest nounor noun phrase to each sentiment word is extracted. Since noparser was used in (Hu and Liu, 2004), the “nearest” function approximatesthe dependency relation between sentiment word andnoun or noun phrasethat itmodifies, which usually works quite well. For example, in thefollowing sentence,“The software is amazing.”If we knowthat “amazing” is a sentiment word, then “software” is extractedas an aspect. This idea turns out to be qui te useful in practice even when it isapplied alone. The sentiment patterns method in (Blair-Goldensohn et al.,2008) uses a similar idea. Additionally, this relation-based method is also auseful method for discovering important or key aspects (or topics) in opiniondocuments because an aspect or topic is unlikely to be important if nobodyexpresses any opinion or sentiment about it.In (Zhuang, Jing and Zhu, 2006), a dependency parser was used to identifysuch dependency relationsfor aspect extraction. Somasundaran and Wiebe(2009) employed a similar approach, and so did Kobayashi et al. (Kobayashiet al., 2006). The dependency idea was further generalized intothedouble-propagation method for simultaneously extracting both sentiment words andaspects in (Qiu et al., 2011) (to be discussed in Section 5.5). In (Wuet al.,2009), a phrase dependency parser was used rather than a normaldependency parser for extracting noun phrases and verb phrases, which formcandidate aspects. The system then em ployed a language model to filter outthose unlikely aspects. Note that a normal dependency parser identifiesdependencyof individual words only, but a phrase dependency parseridentifies dependencyof phrases, which can be more suitable for aspectextraction. The idea of using dependency relations has been used bymanyresearchers for different purposes (Kessler and Nicolov, 2009).

### 5.3.3 Using Supervised Learning

Aspect extraction can be seen as a special case of the general information

Sentiment Analysis and Opinion Mining

71


---

<!-- Página 72 -->

Sentiment Analysis and Opinion Mining

extraction problem. Manyalgorithms based on supervised learning havebeenproposed in the past for information extraction (Hobbs and Riloff,2010; Mooney and Bunescu, 2005; Sarawagi, 2008). The most dominantmethods are based on sequential learning (or sequential labeling). Sincethese are supervised techniques, th ey need manually labeled data fortraining. Thatis, one needs to manually annotate aspects and non-aspects ina corpus. The current state-of-the-art sequential learning methods are Hidden*Markov*(HMM) (Rabiner, 1989) and Conditional RandomFields(CRF) (Lafferty, McCallum and Pereira, 2001). Jin and Ho (2009) applied alexicalized HMM model to learn patterns to extract aspects and opinionexpressions. Jakob and Gurevych (Jakob and Gurevych, 2010) used CRF.They trained CRF on review sentences from different domains for a moredomain independent extraction. A set of domain independent features werealso used, e.g. tokens, POS tags, syntactic dependency, word distance, andopinionsentences. Li et al (2010) integratedtwo CRF variations, i.e., Skip-CRF and Tree-CRF, to extract aspects and also opinions. Unlike the originalCRF, which can only use word sequencesin learning, Skip-CRF andTree-CRF enable CRF to exploit structure features. CRF was also used in(Choiand Cardie, 2010). Liu, Hu and Cheng (2005) and Jindal and Liu (2006b)used sequential pattern rules. These rules are mined based on sequential72One can also use other supervised methods. For example, the method in(Kobayashi, Inui and Matsumoto, 2007) first finds candidate aspect andopinion word pairs using a dependency tree, and then employs a tree-structured classification method to lear n and to classify the candidate pairsas being an aspect and evaluation rela tion or not. Aspects are extracted fromthe highest scored pairs. The features used in learning include contextualclues, statistical co-occurrence clues, among others. Yu et al. (2011) used apartially supervised learning method called one-class SVM (Manevitz andYousef, 2002) to extract aspects. Using one-class SVM, one onlyneeds tolabel some positive examples, which ar e aspects, but not non-aspects. Intheir case, they only extracted aspects from Pros and Cons of review format2 as in (Liu, Hu and Cheng, 2005). They also clustered those synonymaspects and ranked aspects based on their frequency and their contributionsto the overall review rating of reviews. Ghani et al. (2006) used bothtraditional supervised learning and semi-supervised learning for aspectextraction. Kovelamudi et al., (2011) used a supervised method but alsoexploited some relevant information fromWikipedia.


---

<!-- Página 73 -->

### 5.3.4

In recent years, statistical topic models have emerged as a principledmethodfor discovering topics from a large collection of text documents. Topicmodeling is an unsupervised learning method that assumes each documentconsists of a mixture of topics and each topic is a probability distributionover words. A topic model is basically a document generative model whichspecifies a probabilistic procedure by which documents can be generated.The outputoftopic modeling is a set of word clusters. Each cluster forms atopic and is a probability distribution over words in the document collection.There were two main basic models, pLSA (Probabilistic Latent SemanticAnalysis) (Hofmann, 1999) and LDA (Latent Dirichlet allocation) (Blei, Ngand Jordan, 2003; Griffiths and Steyvers, 2003; Steyvers and Griffiths,2007). Technically, topic models are a type of graphical models based onBayesian networks. Although they ar e mainly used to model and extracttopics from text collections, they can be extended tomodel many other typesof information simultaneously. For example, in the sentiment analysiscontext, one can design a joint model tomodel both sentiment words andtopics at the same time, due to the observation thatevery opinion has atarget. For readers who are not familiar with topic models, graphical modelsor Bayesiannetworks, apart from reading the topic modeling literature, the“pattern recognition and machine learning” book by Christopher M. Bishop(Bishop, 2006) is an excellent source of background knowledge.Intuitively topics from topic models are aspects in the sentiment analysiscontext. Topic modeling can thus be applied to extract aspects. However,there is also a difference. That is, to pics can cover both aspect words andsentiment words. For sentiment analysis, they need to be separated. Suchseparations can beachieved by extending the basic model (e.g., LDA) tojointlymodel both aspects and sentiments. Below, we give an overview ofthe current research in sentiment anal ysis that has used topic models toextract aspects and to perform other tasks. Note that topic models not onlydiscover aspects but also group synonymaspects.Mei et al (Mei et al., 2007) proposed a joint model for sentiment analysis.Specifically, they built an aspect-sentiment mixture model, which was basedon an aspect (topic) model, a positive sentiment model, and a negativesentiment model learned with the help of some external training data. Theirmodel was based onpLSA. Most other models proposed by researchers arebased on LDA.In (Titov andMcDonald, 2008), the authors showed that global topic modelssuch as LDA (Blei, Ng and Jordan, 2003 ) might not be suitable for detecting

Sentiment Analysis and Opinion Mining

73


---

<!-- Página 74 -->

Sentiment Analysis and Opinion Mining

aspects. The reason is that LDA depends on topic distribution differencesand word co-occurrences among documents to identify topics and wordprobabilitydistribution in each topic. However, opinion documents such asreviews about a particular type of products are quite homogenous, meaningthat every document talks about the same aspects, which makes global topicmodels ineffective and are only effective for discovering entities (e.g.,different brands or product names). The authors then proposed themultigraintopic models. The global model discovers entities while the localmodel discovers aspects using a few sentences (or a sliding text window) asa document. Here, each discovered aspect is a unigramlanguage model, i.e.,a multinomial distribution over words. Different words expressing the sameor related facets are automatically gr ouped together under the same aspect.However, this technique does not separateaspects and sentiment words.Branavan et al. (2008) proposed a method which made use of the aspectdescriptions as keyphrases in Pros andCons of review format 1 to helpfinding aspects in the detailed review text. Their model consists of two parts.The first part clusters the keyphrases in Pros and Cons into some aspectcategories based on distributional similarity. The second part builds a topicmodel modeling the topics or aspects in the reviewtext. Their final graphical74based ontheidea that the model biases the assignment of hidden topics inthe review text to be similar to the topics represented by the keyphrases inPros and Cons of the review, but it also permits some words in the documentto be drawn from other topics not represented by the keyphrases. Thisflexibility inthe coupling allows the model to learn effectively in thepresence of incomplete ke yphrases, while still encouraging the keyphraseclustering to cohere with the topics supported by the review text. However,this approach stilldoes not separate aspects andsentiments.Lin and He (2009) proposed a joint topic-sentimentmodel by extendingLDA, where aspect words and sentiment words were still not explicitlyseparated. Brody and Elhadad (2010) proposed to first identify aspects usingtopic models and then identify aspect-specific sentiment words byconsidering adjectives only. Li, Huang and Zhu (2010) proposed two jointmodels, Sentiment-LDA and Dependency-sentiment-LDA, to find aspectswith positive and negative sentiments. It does not find aspects independentlyand it does not separate aspect words and sentiment words. Zhao et al. (Zhaoet al., 2010) proposed the MaxEnt-LDA (a Maximum Entropy and LDAcombination) hybrid model to jointly discover both aspect words and aspect-specific opinion words, which can leverage syntactic features to helpseparate aspects and sentiment words. The joint modeling is achievedthrough an indicator variable (also called a switch variable) which is drawn


---

<!-- Página 75 -->

Sentiment Analysis and Opinion Mining

from a multinomial distribution governed by a set of parameters. Theindicator variable determines whether a word in sentence is an aspect word,an opinion word or a background word. Maximum Entropy was used tolearn the parameters of thevariable using labeled training data.A joint model was also proposed in (Sauper, Haghighi and Barzilay, 2011)which worked only on short snippets already extracted from reviews, e.g.,“” It combined topic modeling with ahidden Markovmodel (HMM), where the HMM models the sequence ofwords with types (aspect word, sentimen t word, or background word). Theirmodel is related to HMM-LDA proposed in (Griffiths et al., 2005), whichalso models the word sequence. Variations of the joint topic modelingapproach were also taken in (Liu et al., 2007), (Lu and Zhai, 2008) and (JoandOh, 2011).In (Mukherjee and Liu, 2012), a semi-supervised jointmodel was proposed,which allows the user to provide some seed aspect terms for sometopics/aspects in order to guide the in ference to produce aspect distributionsthat conform to the user’s need.Another lineof work using topic modeling aimed to associate aspects withopinion/sentiment ratings, i.e., to predict aspect ratings based on joint75modeling of aspects and ratings. Titov and McDonald (2008) proposed amodel to discover aspects fromreviews and also to extract textual evidencefromreviews supporting each aspect rating. Lu, Zhai and Sundaresan (2009)defined the problem of rated aspect summarization of short comments fromeBay.com. Their aspect extraction was based on a topic model calledstructured pLSA. This model can model the dependency structure of phrasesin short comments. To predict the rating for each aspect in a comment, itcombined the overall rating of the comment and the classification result of alearned classifier for the aspect based on all the comments. Wang et al.(2010) proposed a probabilistic rating regression model to assign ratings toaspects. Theirmethod firstuses some given seed aspects to find more aspectwords using a heuristic bootstrapping method. It then predicts aspect ratingsusing the proposed probabilistic rating regression model, which is also agraphical model. Themodel makes use of review ratings and assumes thatthe overall rating of a review is a line ar combination of its aspect ratings.The model parameters are estimated using the Maximum Likelihood (ML)estimator and an EM style algorithm.A series of joint models were also proposed in (Lakkaraju et al., 2011) basedon the composite topic model of HMM-LDA in (Griffiths et al., 2005),which considers both word sequence and word-bag. The models thus cancapture both syntactic structures and semantic dependencies similar to that


---

<!-- Página 76 -->

Sentiment Analysis and Opinion Mining

in (Sauper, Haghighi and Barzilay, 2011). Theyare able to discover latentaspects and their corresponding sentiment ratings. Moghaddam and Ester(2011) also proposed a joint topic model to find and group aspects and toderive their ratings.Althoughtopic modeling is a principled approach based on probabilisticinferencing and can be extended tomodel many types of information, it doeshave some weaknesses which limit its practical use in real-life sentimentanalysis applications. One main issue is that it needs a large volume of dataand a significant amount of tuning in order to achieve reasonable results. Tomake matters worse, most topicmodeling methods use Gibbs sampling,which produces slightly different results in different runs due to MCMC(Markov chain Monte Carlo) sampling, which makes parameter tuning timeconsuming. While it is not hard for topic modeling to find those very generaland frequent topics or aspects from a large document collection, itis noteasy to find those locally frequent but globally not so frequent aspects. Suchlocally frequent aspects are often the most useful ones for applicationsbecause theyare likely tobe most relevant to the specific entities that theuser is interested in. Those very general and frequent aspects can also beeasily found by the methods discussed earlier. These methods can find less76the results from current topic modeling methods are usually not granular orspecific enough for many practical sentim ent analysis applications. It ismore useful for the user to get some high level ideas about what a documentcollection is about.That being said, topic modeling is a powerful and flexible modeling tool. Itis also very nice conceptually and ma thematically. I expect that continuedresearch willmake it more practic ally useful. One promising researchdirection is to incorporatemore existing natural language and domainknowledge in the models. There are already some initial works in thisdirection (Andrzejewski and Zhu, 2009; Andrzejewski, Zhu and Craven,2009; Mukherjee and Liu, 2012; Zhai et al., 2011). We will discuss themSection 5.6. However, I think they are still too statistics centric and comewith their own limitations. It could be fruitful if we can shift more towardnatural language and knowledge centric for a more balanced approach.Another direction would be to integrate topic modeling with some othertechniques toovercome its shortcomings.Apart from the main methods discussed above and in the previous threesections, there are still other works on aspect extraction. For example, Yi etal. (2003) used a mixture languagemodel and likelihood ratio to extractproduct aspects.

Ma and Wan (2010) used the centering theory andsupervised learning. Meng and Wang (2009) extracted aspects from product


---

<!-- Página 77 -->

specifications, which arestructured data. Kim and Hovy (2006) usedsemantic role labeling. Stoyanov and Cardie (2008) exploited coreferenceresolution. Toprak, Jakob and Gurevych (2010) designed a comprehensiveannotation scheme for aspect-basedopinion annotation. Earlier annotationswere partial and mainly for the special needs of individual papers. Carvalhoet al. (2011) annotated a collection of political debates with aspects andother information.

### 5.3.5 Mapping Implicit Aspects

In (Hu and Liu, 2004), two kinds of aspects were identified, explicit aspectsand implicit aspects. However, it only dealt with explicit aspects. Recall inSection 2.1, we call aspects that are expressed as nouns and noun phrases the*explicit aspects , e.g., “picture quality” in “ The picture quality of this camera**is great .” All other expressions that indicate aspects are called implicit**aspects . There are many types of implicit aspect expressions. Adjectives and*adverbs are perhaps themost common types because most adjectivesdescribe some specific attributes or properties of entities, e.g., expensivedescribes “price,” and beautiful describes “appearance.” Implicit aspects canbe verbs too. In general, implicit aspect expressions can be very complex,e.g., “ This camera will not easily fit in a pocket .” “fit in a pocket” indicatesthe aspect sizeAlthough explicit aspect extraction has been studied extensively, limitedresearch has been done onmapping implicit aspects totheir explicit aspects.In (Su et al., 2008), a clustering method was proposed tomap implicit aspectexpressions, which were assumed to be sentiment words, to theircorresponding explicit aspects. Themethod exploits themutualreinforcement relationshipbetween an explicit aspectand a sentiment wordforming a co-occurring pair in a sentence. Such a pair may indicate that thesentiment word describes the aspect, or the aspect is associated with thesentiment word. The algorithm finds the mapping by iteratively clusteringthe set of explicit aspects and the set of sentiment words separately. In eachiteration, before clustering one set, the clustering results of the other set isused to update the pairwise similarity of the set. The pairwise similarity in aset is determined by a linear combination of intra-set similarity and inter-setsimilarity. The intra-set similarity of two items is the traditional similarity.The inter-set similarity of two items is computed based on the degree ofassociation between aspects and sentiment words. The association (ormutual reinforcement relationship) is modeled using a bipartite graph. Anaspect and an opinion word are linked if they have co-occurred in a

Sentiment Analysis and Opinion Mining

77


---

<!-- Página 78 -->

Sentiment Analysis and Opinion Mining

sentence. The links are also weighted based on the co-occurrence frequency.After the iterative clustering, the strongest nsentiment word groups form the mapping.

78

In (Hai, Chang and Kim, 2011), a two-phase co-occurrence association rulemining approach was proposed tomatch implicit aspects (which are alsoassumed to be sentiment words) with explicit aspects. In the first phase, theapproach generates association rules involving each sentiment word as thecondition and an explicitaspect as the consequence, which co-occurfrequentlyinsentences of a corpus. In the secondphase, itclusters the ruleconsequents (explicit aspects) to generate more robust rules for eachsentiment word mentioned above. For application or testing, given asentiment word withno explicit aspect, it finds the best rule cluster and thenassigns the representative word of the cl uster as the final identified aspect.

## 5.4

As discussed in Section 4.3, research ers often try to solve a problem in ageneral fashion and in many cases based on a simplistic view. In the contextof aspect extraction and aspect sentiment classification, it is not always thesentiment word and aspect word pairs that are important. As indicated inSection 5.2, the real world is much more complex and diverse than that.Here, we use resource usage as an example to show that a divide andconquer approach may be needed for aspect-based sentiment analysis.In many applications, resource usage is an important aspect, e.g., “This*washer uses a lot of water .” Here the water usage is anaspect of the washer,*and this sentence indicates a negative opinion as consuming toomuchresource is undesirable. There is no opinion word in this sentence.Discovering resource words and phrases, which are called resource terms,are thus important for sentiment analysis. In Section 5.2, we presented someopinion rules involving resources. We reproduce two of them below:1. ::= consume no,_little_or_less resource2. ::= consume a_large_quantity_of_or_more resourceIn (Zhang and Liu, 2011a), a method was proposed to extract resource terms.For example, in the above example, “water” should be extracted as aresource term. The paper formulated the problem based on a bipartite graphand proposedan iterative algorithm to solve the problem. The algorithm wasbased on the following observation:**Observation : The sentiment or opinion expressed in a sentence about**resource usage is often determined by the following triple,


---

<!-- Página 79 -->

## 5.5

## Expansion and Aspect Extraction

Asmentioned in Chapter 2, an opinion always has a target. This property hasbeen exploited in aspect extraction by several researchers (see Section5.3.2). In (Qiu et al., 2009; Qiu et al., 2011), it was used toextract bothsentiment words and aspects at the same time by exploiting certain syntacticrelations between sentiments and targets, and a small set of seed sentimentwords (no seed aspects are required) for extraction. Themethod is based onbootstrapping. Note that sentiment words generation is an important taskitself (see Chapter 6).Due to the relationships between sentiments/opinions and their targets (oraspects), sentiment words can be recognized by identified aspects, andaspects can be identified by known sentiment words. The extractedsentiment words and aspects are utilized to identifynew sentiment wordsand new aspects, which are used again to extract more sentiment words andaspects. This propagation process ends when no more sentiment words oraspects can be found. As the process involves propagation through bothsentiment words and aspects, the method is called double propagation.Extraction rules were based on certain special dependency relations amongsentiment words and aspects. The dependency grammar (Tesniere, 1959)

(verb, quantifier, noun_term),where noun_term is a noun or a noun phraseFor example, in “ This washer uses a lot of water ,” “uses” is the main verb,“a lot of” is a quantifier phrase, and “water” is the noun representing aresource. Themethod used suchtriples to helpidentify resources in adomain corpus. The model used a circul ar definition to reflect a specialreinforcement relationship between resource usage verbs (e.g., consume)and*water ) based onthe bipartite graph. The quantifier*was not used in computation but was employed toidentify candidate verbsand resource terms. The algorithm assumes that a list of quantifiers is given,which is not numerous and can be manually compiled. Based on thecirculardefinition, the problem is solved using an iterative algorithm similar to theHITS algorithm in (Kleinberg, 1999). To start the iterative computation,some global seed resources are employed to find and to score some strongresource usage verbs. These scores are then applied as the initialization forthe iterative computation for any application domain. When the algorithmconverges, a ranked list of candid ate resource terms is identified.

Sentiment Analysis and Opinion Mining

79


---

<!-- Página 80 -->

Sentiment Analysis and Opinion Mining

was adopted to describe the relations. The dependency parser used wasminipar (Lin, 2007).Some constraints were also imposed. Sentiment words were considered to beadjectives and aspects nouns or noun phrases. The dependency relationsbetween sentiment words and aspects include mod pnmod, , , ,and , while the relations for sentimen t words and aspects themselvescontain only the conjunction relation conjbetween sentiment words and aspects, OO-Rel between sentiment wordsthemselves, and AA-Rel between aspects. Each relation in OA-Rel, OO-Rel,or AA-Rel is a triple  w 80

and is one thedependency relations above.*i*The extraction process uses a rule-b ased approach. For example, in “Canon*G3 produces great pictures ,” the adjective “great”*the noun“pictures”*mod*If we know “great”which a sentiment word directlydepends through modwe can extract “pictures”aspect, we can extract “great”propagation performs four subtasks:1. extracting aspects using sentiment words2. extracting aspects using extractedaspects3. extracting sentiment words using extracted aspects4. extracting sentiment words using bothgiven and extractedopinionwordsOA-Rels are used for tasks (1) and (3), AA-Rels are used for task (2), andOO-Rels are used for task(4). Four types of rules are defined (shown inTable 5.1) respectively, for these four subtasks. In the table, o afor the output (or extracted) sentiment word (or aspect). {O Aset of known sentiment words (or aspe cts) either given or extracted. Hmeans any word. POS O A O A stand for the POS tag anddependency relation of the word O A*JJ**NN*sets of POS tags of potential sentiment words and aspects respectively. {JJcontains JJ and ; { } contains NN NNSMRdependency relations, which is the set { mod pnmod,

is employed to extract aspects ( awords ( O 2*i* *o**A 3**i*

),*w**i*)*w*) is the POS tagof word w*j**i*

*subj s , ,**desc CONJ } contains conj only. The arrowsmean dependency. For*example, O O-Dep *O**A**O-**Dep**R*

aspects ( a*A**i* ), and R(*O i**i* ).*i*


---

<!-- Página 81 -->

**Observations Output Examples**

R11 *O**a*(OA-Rel) s.t.  O-Dep  },*POS A NN*

R12 *O* A-Dep  a(OA-Rel) s.t.  O  },*POS A NN*

R21 *O**o*(OA-Rel) s.t.  O-Dep  },*POS O JJ*

R22 *O* A-Dep  o(OA-Rel) s.t.  O  },*POS O JJ*

R31 *A*(AA-Rel)

R32 *A*(AA-Rel)

R41 *O*(OO-Rel)

R42 *O*(OO-Rel)

**Table 5.1 . Rules for aspect and opinion word extraction.**

This method was originally designed for English, but it has also been usedfor Chinese online discussions (Zhai et al., 2011). Thismethod can also bereduced for finding aspects only using a large sentiment lexicon. Forpractical use, the set of relations can be significantly expanded. Also, insteadof using word-based dependency parsing, a phrase leveldependency parsingmay be better as many aspects are phras es (Wu et al., 2009). Zhang et al.(2010) improved this method by adding more relations and by ranking theextracted aspects using a graph method.

## 5.6

After aspect extraction, aspect ex pressions (actual words and phrasesindicating aspects) need tobe grouped into synonymous aspect categories.Each category represents a unique aspect. As i

### Sentiment Analysis and Opinion Mining

### 81

*-Dep ****s.t.****i**i**j* },*-Dep  },**POS A**j**i* *a*) }*i* *-Dep H**-Dep ****s.t.****i**i**j**j*  A*-Dep A**-Dep*(*i**i**j* *-Dep = AND A**-Dep = ),**POS A**i* *a*) }*j* *-Dep ****s.t. j****i**i*  O*-Dep  },**POS O**j**i* *o*) }*i* *-Dep  O**-Dep ****s.t.****i**i**j**j*  O*-Dep O**-Dep OR*(*i**i**j* /*-Dep*, }),*POS O**i**j* *o*) }*j*

*good  *

*best mod player  *

*Does the player play dvd with**audio and “video ”**i*

*video  *

*j* *len obj has subj G3*

*The camera is amazing and**i* *“easy” to use.**easy conj amazing*

*If you want to buy a sexy, “cool”,**j* *accessory-available mp3 player,* *y**ou can choose iPod.**sexy mod player  *

ID, column 2 is the observed relation (line 1) and the constraints that it must satisfy(lines 2 – 4), column 3 is the output, and column 4 is an example. In each example, theunderlined word is the known word and the word with double quotes is the extractedword. The corresponding instantiated relati on is given right below the example.

n any writing, people often

with screen as theknown word and good as theextracted word

with iPodknown word and best2extract word.

Column 1 is the rule


---

<!-- Página 82 -->

Sentiment Analysis and Opinion Mining

use different words and phrases to describe the same aspect. Forexample, “call quality” and “voice qual ity” refer to the same aspect forphones. Grouping such aspect expre ssions fromthe same aspect iscritical for opinion analysis. Although WorldNet and other thesaurusdictionaries can help to some extent , they are far fromsufficient becausemany synonyms are domain dependent (Liu, Hu and Cheng, 2005). Forexample, “movie” and “picture” are synonyms in movie reviews, butthey are not synonyms in camera reviews as “picture” is more likely tobe synonymous to “photo” while “movie” to “video”. 82

expressions are multi-word phrases, which cannotbe easily handled withdictionaries. Furthermore, it is also important to note that manyaspectexpressions describing the same aspect are notgeneral or domain specificsynonyms. For example, “expensive” and “cheap” can both indicate theaspect price but they are not synonyms of each other (but antonyms) orsynonyms of price .Carenini, Ng and Zwart (2005) proposed the first method to deal with thisproblem. Their method was based on several similarity metrics defined usingstring similarity, synonyms, and lexical distances measured using WordNet.The method requires a taxonomy of aspects to begiven for a particulardomain. It merges each discovered aspectexpression toan aspect node in thetaxonomybased on the similarities. Experiments based on digital cameraand DVD reviews showedpromising results. In (Yu et al., 2011), a moresophisticated methodwas presented to also use publicly available aspecthierarchies/taxonomies of products and the actual product reviews toproduce the final aspect hierarchies. A set of distancemeasures was alsoused but was combined with an optimization strategy.In (Zhai et al., 2010), a semi-supervised learning method was proposed togroup aspect expressions into some us er-specified aspect categories. Toreflect the user needs, he/she first labels a small number of seeds for eachcategory. The system then assigns the rest of the aspect expressions tosuitable categories using a semi-supervised learningmethod working withlabeled and unlabeled examples. Themethod uses the Expectation-Maximization (EM) algorithm in (Nigam et al., 2000). The method alsoemployed two pieces of prior knowledge to provide a better initialization forEM: (1) aspect expressions sharing some common words are likely to belongto the same group, e.g., “battery life” and “battery power,” and (2) aspectexpressions that are synonyms in a di ctionary are likely to belong to thesame group, e.g., “movie” and “picture.” These two pieces of knowledgehelp EM produce better classification results. In (Zhai et al., 2011), softconstraints were used to help label some examples, i.e., sharing words andlexical similarity (Jiang and Conrath, 1997). The learning method also used

Many aspect


---

<!-- Página 83 -->

Sentiment Analysis and Opinion Mining

EM, but it eliminated the need of asking the user to provide seeds. Note thatthe general NLP research on concept similarity and synonym discovery isalso relevanthere (Mohammad and Hirst, 2006; Wang and Hirst, 2011).

83

In (Guo et al., 2009), a method called multilevel latent semantic associationwas presented. At the first level, all the words in aspect expressions (eachaspectexpression can havemore than one word)concepts/topics using LDA. The results are used to build latent topicstructures for aspect expressions .expressions “day photos”, “day photo”, “daytime photos” and “daytimephoto”. If LDA groups the individual words “day” and “daytime” intotopic10, and“photo” and “photos” intotopic12, the system will group allfour aspect expressions into one group, call it “topic10-topic12”, which iscalled a latent topic structure. At the second level, aspect expressionsgrouped by LDA again but according to their latent topic structuresproducedat level 1 and their context snippets in reviews. Following theabove example, “day photos”, “day photo”, “daytime photos” and “daytimephoto” in “topic10-topic12” combined with their surrounding words form adocument. LDA runs on such documents to produce the final result. In (Guoet al., 2010), a similar idea was also used to group aspects from differentlanguages intoaspect categories, wh ich can be used to compare opinionsalong different aspects from differe nt languages (or countries).Topic modeling methods discussed in Section 5.3.4 actuallyperform bothaspect expression discovery and categorization at the same time in anunsupervisedmanner as topic modeling basically clusters terms in adocument collection. Recently, some algorithms have also been proposed touse domain knowledge or constraints to guide topic modeling to producebetter topic clusters (Andrzejewski, Zhu and Craven, 2009). The constraintsare in the form of must-links and cannot-links . A must-link constraint inclustering specifies that two data instances must be in the same cluster. Acannot-link constraint specifies that two data instances cannot be in the samecluster. However, the method can result in an exponential growth in theencoding of cannot-link constraints and thus have difficulty in processing alarge number of constraints.Constrained-LDA of Zhai et al. (2011) took a different but heuristicapproach. Instead of treating constraints as priors, the constraints were usedin Gibbs sampling to bias the conditional probability for topic assignment ofa word. This method can handle a large number of must-link and cannot-linkconstraints. The constraints can also be relaxed, i.e., they are treatedas soft(rather than hard) constraints and may not be satisfied. For aspectcategorization, Constrained-LDA used the following constraints:


---

<!-- Página 84 -->

Sentiment Analysis and Opinion Mining

*Must-link : If two aspect expressions a*

84

## 5.7

## Extraction

Entity, opinion holder and time extraction is the classic problem of namedentity recognition (NER). NER has been studied extensively in severalfields, e.g., information retrieval, text mining, data mining, machine learningand natural language processing under the name of information extraction(Hobbs andRiloff, 2010; Mooney and Bunescu, 2005; Sarawagi, 2008).There are two main approaches to in formation extraction: rule-based andstatistical. Early extraction systems were mainly based on rules (e.g., (Riloff,1993)). Statistical methods were typically based on Hidden Markov Models(HMM) (Rabiner, 1989) (Jin and Ho, 2009) and Conditional Random Fields(CRF) (Lafferty, McCallum and Pereira, 2001). BothHMM and CRF aresupervisedmethods. Due tothe prior work in the area, specific works in thecontext of sentiment analysis and opinion mining is notextensive. Thus, wewill not discuss it further. See a comprehensive survey of informationextraction tasks and algorithms in (Sarawagi, 2008). Here we only discusssomespecific issues in sentiment analysis applications.In most applications that use socialmedia, we do not need to extract opinionholders and the times of postings from th e text as opinion holders are usuallythe authors of the reviews, blogs, or discussion postings, whose login ids areknown although their true identities in the real world are unknown. The dateand time when a posting was submitted are alsoknown and displayed on theWeb page. They can bescraped from the page using structured dataextraction techniques (Liu, 2006 and 2011). In some cases, opinion holderscan be in the actual text and need tobe extracted. We discuss it below.

and ashare one or more words, theyform a must-link, i.e., they are likely j*i*e.g., “battery power” and “battery life.”*Cannot-link : If two aspect expressions a*

and ain the same sentence, theyform a cannot-link. The reason for this constraint is that people usually*i**j*do not repeat the same aspect in the same sentence, e.g., “I like the*picture quality, battery life, and zoom of this camera.”*In (Mukherjee and Liu, 2012), the domain knowledge came in the form ofsome user-provided seedaspect words to some topics (or aspects). Theresulting model is thus semi-supervised. The model also separates aspectwords and sentiment words. The model in (Andrzejewski, Zhu and Craven,2009) or the Constrained-LDA method does not do that.


---

<!-- Página 85 -->

Here we first discuss a specific problem of named entity extraction in thesentiment analysis context. In a typical sentiment analysis application, theuser usuallywants to find opinions about some competing entities, e.g.,competing products or brands. However, he/she often can only provide a fewnames because there are somany different brands and models. Evenfor thesame entity, Web users may write the entity in many different ways. Forexample, “Motorola” may be written as “Moto” or “Mot.” It is thusimportant for a system to automatically discover them from the corpus (e.g.,reviews, blogs and forum discussions). Themain requirement of thisextraction is that the extracted entities must be of the same type as theentities provided by the user (e.g., phone brands and models).In (Li et al., 2010), Li etal. formulated the problem as a set expansion*problem (Ghahramani and Heller, 2006; Pantel et al., 2009). The problem is*stated as follows: Given a set Q*C*set of candidate entities, we wish to determine which of the entities in Dbelong to C*C*examples Qproblem is often solved as a ranking problem, i.e., to rank the entities in Dbased on their likelihoods of belonging to CThe classic methods for solving this problem in NLP are based ondistributional similarity (Lee, 1999; Pantel et al., 2009). The approach worksby comparing the similarity of the surround words of each candidate entitywith those of the seed entities and then ranking the candidate entities basedon the similarity values. In (Li et al., 2010), it was shown that this approachwas inaccurate. Learning from positive and unlabeled examples (PUlearning) using the S-EM algorithm(L iu et al., 2002) was considerablybetter. To apply PU learning, the given seeds were used to automaticallyextract sentences that contain one or more of the seeds. The surroundingwords of each seed in these sentences served as the context of the seed. Therest of the sentences were treated as unlabeled examples. Experimentalresults indicated that S-EM outperformed the machine learning technique*Bayesian Sets (Ghahramani and Heller, 2006), which also outperformed the*distributional similaritymeasure significantly.About opinion holder extraction in the context of sentiment analysis, severalresearchers have investigated it. Th e extraction was mainly done in newsarticles. Kimand Hovy (2004) consid ered person and organization as theonly possibleopinionthem. Choi, Breck and Cardie (2006) used conditional randomfields (CRF)for extraction. To train CRF, they used features such as surroundingwords,part-of-speech of surrounding words, grammatical roles, sentiment words,etc. In (Kim and Hovy, 2006), the method first generates all possible holder

Sentiment Analysis and Opinion Mining

85


---

<!-- Página 86 -->

Sentiment Analysis and Opinion Mining

candidates in a sentence, i.e., all nounphrases, including common nounphrases, named entities, and pronouns . It then parses the sentence andextracts a set of features from the parse tree. A learned MaximumEntropy(ME) model then ranks all holder candidates according toobtained by the ME model. The system picks the candidate with the highestscore as the holder of the opinion in the sentence. Johansson and Moschitti(2010) used SVM with a set of features. Wiegand and Klakow (2010) usedconvolution kernels, and Lu (2010) applied a dependency parser.

86

## 5.8

## Sense Disambiguation

Although we discuss only coreference resolution and word sense*disambiguation in this section, we reallywant to highlight NLP issues and*problems in the sentiment analysis context. Most of such issues have notbeen studied in sentiment analysis.Coreference resolution has been studiedextensively in the NLP communityin general. It refers to the problem of determining multiple expressions in asentenceor document referring to the same thing, i.e., they have the same"referent."

For example, in“ I bought aniPhone two days ago. It looks very*nice I made many calls in the past two days. They were great,” “It” in the*second sentence refers to iPhone, which is an entity, and “they” in the fourthsentence refers to “calls”, which is an aspect. Recognizing these coreferencerelationships is clearly very important for aspect-based sentiment analysis. Ifwe do not resolve them, but only consider opinion in each sentence inisolation, welose recall. That is, although weknowthat the second andfourth sentences express opinions, we donot knowabout what. Then, fromthis piece of text we will get no useful opinion, but in fact, it has a positiveopinion on iPhone itself and also a positive opinion onthe call quality.Ding and Liu (2010) proposed the problem of entity and aspect coreference*resolution . The task aimsto determine which mentions of entities and/or*aspects that pronouns refer to. The paper took a supervised learningapproach. The key interesting points were the design and testing of twoopinion-related features, which showed that sentiment analysis was used for

In (Ruppenhofer, Somasundaran and Wiebe, 2008), the authors discussedthe issue of using automatic semantic role labeling (ASRL) to identifyopinion holders. They argued that ASRL is insufficient and other linguisticphenomena such as the discourse structure may need to be considered. Kimand Hovy (2006) earlier also used semantic role labeling for the purpose.


---

<!-- Página 87 -->

the purpose of coreference resolution. The first feature is based on sentimentanalysis of regular sentences and co mparative sentences, and the idea of*sentiment consistency . Consider these sentences, “ The Nokia phone is better**than this Motorola phone. It is cheap too .” Our commonsense tells us that*“It” means “Nokia phone” because in th e first sentence, the sentiment about“Nokia phone” is positive (comparative positive), but it is negative(comparative negative) for “Motorola phone,” and thesecondsentence ispositive. Thus, we conclude that “It” refers to “Nokia phone” because peopleusually express sentiments in a consistent way. It is unlikely that “It” refersto “Motorola phone.” However, if we change “ It is cheap too” to “It is also*expensive ”, then “it” should now refer to“Motorola phone.” To obtain this*feature, the system needs to have the ability to determine positive andnegative opinions expressed in both regular and comparative sentences.The second feature considers what entities and aspects are modified by whatopinion words. Consider these sentences, “ I bought a Nokia phone*yesterday. The sound quality is good. It is cheaptoo.” The question iswhat*“It” refers to, “sound quality” or the “Nokia phone.” Clearly, we know that“It” refers to “Nokia phone” because “sound quality” cannot be cheap. Toobtain this feature, the system needs to identify what sentiment words areusually associated with what entities or aspects. Such relationships have tobe mined from the corpus. These two f eatures are semantic features thatcurrent general coreference resolutionmethods do not consider. These twofeatures can help improve the coreference resolution accuracy.In (Stoyanov and Cardie, 2006), Stoyanov and Cardie proposed the problemofwhich ismentions of opinion holders (sources) refer to the same entity. The authorsused existing coreference resolution features in (Ng and Cardie, 2002).However, instead of simply employing supervisedlearning, they usedpartially supervised clustering.Akkaya, Wiebe and Mihalcea (2009) studied subjectivity wordsense*disambiguation (SWSD). The task is to automatically determine which*instances in a corpus are being usedbeing used with objective senses. Currently, most subjectivity or sentimentlexicons are compiled as lists of words, rather than word meanings (senses).However, many words have both subjective and objective senses. False hits– subjectivity clues used with objective senses – are a significant source oferror in subjectivity and sentiment analysis. The authors built a supervisedSWSD model to disambiguate members of a subjectivity lexicon as having asubjective sense or anobjective sense in a corpus context. The algorithmrelied on common machine learning features for word sense disambiguation(WSD). However, the performance wa s substantially better than the

Sentiment Analysis and Opinion Mining

87


---

<!-- Página 88 -->

Sentiment Analysis and Opinion Mining

performance of full WSD on the same data, suggesting that the SWSD taskwas feasible, and that subjectivity provided a natural coarse grainedgrouping of senses. They also showed that SWSD can subsequently helpsubjectivity and sentiment analysis.

88

## 5.9 Summary

Aspect-level sentiment analysis is usually the level of details required forpractical applications. Most industrial systems are so based. Although agreat deal of work has been done in the researchcommunity and manysystems have also been built, the problem is still far from being solved.Every sub-problem remains to be highly challenging. As one CEO put it,“our sentiment analysis is as bad as everyone else’s,” which is a niceportrayal of the current situation and the difficultyof the problem.Two most outstanding problems are aspect extraction and aspect sentimentclassifications. The accuracies for bo th problems are not high becauseexisting algorithms are still unable to deal with complex sentences thatrequires more than sentiment words and simple parsing, or to handle factualsentences that imply opinions. We discussed some of these problems inbasic rules of opinions in Section 5.2.On the whole, we seem to havemet a long tail problem. While sentimentwords can handle about 60% of the cases (more in somedomains and less inothers), the rest are highly diverse, numerous and infrequent, which make ithard for statisticallearning algorithms to learn patterns because there aresimply not enough training data for them. In fact, there seem to be anunlimited number of waysthat people can use to express positive or negativeopinions. Every domain appears to have something special. In (Wu et al.,2011), a more complex graph-based representation of opinions wasproposed, which requires even more sophisticated solution methods.So far, the research community has mainly focused on opinions aboutelectronics products, hotels, and restaurants. Thesedomains are easier(although not easy) and reasonably good accuracies can be achieved if onecan focus on each domain and take care of its special cases. When onemoves to other domains, e.g., mattress and paint, the situations getconsiderably harder because in these domains many factual statements implyopinions. Politics is another can of warms. Here, the current aspectextraction algorithms only had limited success because few political issues(aspects) can be described with one or two words. Politicalsentiments arealso harder to determine due to complexmixture of factual reporting andsubjective opinions, and heavy use of sarcastic sentences.


---

<!-- Página 89 -->

In term of the type of social media, researchers working on aspect-basedsentiment analysis have focused mainly on product/service reviews andtweets from Twitter. These forms of data are also easier (again, not easy) tohandle because reviews are opinion rich and have little irrelevantinformation while tweets are very short and often straight to the point.However, other forms of opinion text such as forum discussions andcommentaries are much harder to deal with because they are mixed with allkinds of non-opinion contents and often talk about multiple entities andinvolve user interactions. This leads us to another major issue thatwe havenot discussed so far as there is limited research on it. It is the data noise.Almost all forms of socialmedia are very noisy (except reviews) and full ofall kinds of spelling, grammatical, and punctuation errors. Most NLP toolssuch as POS taggers and parsers need clean data to perform accurately. Thusa significant amount of pre-processing is needed before any analysis. See(Dey and Haque, 2008) for some pre-processing tasks and methods.To make a significant progress, we still need novel ideas and to study a widerange of domains. Successful algorithms are likely tobe a goodintegrationof machine learningand domain and natural language knowledge.

Sentiment Analysis and Opinion Mining

89


---

<!-- Página 90 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 6

90

## Sentiment Lexicon Generation

By now, it should be quite clear that words and phrases that convey positiveor negative sentiments are instrumental for sentiment analysis. This chapterdiscusses how to compile such words lists. In the researchliterature,*sentiment words are also called opinion words ,*, or*bearing words . Positive sentiment words are used toexpress somedesired*states or qualities while negative sen timent words are used to express someundesired states or qualities. Examples of positive sentiment words are*beautiful ,*, and amazing . Examples of negative sentiment wordsare , , and poorsentiment phrases and idioms, e.g., cost someone an arm and a leg.Collectively, they are called sentiment lexicon). For easypresentation, from now on when we sa y sentiment words, we mean bothindividual words and phrases.Sentiment words can be divided into two types, base type and comparative*type*the comparative type (which include the superlative type) are used toexpresscomparative and superlative opinio ns. Examples of such words are better,*worse , , , etc., which are comparative and superlative forms of their*base adjectives or adverbs, e.g., good and badthe base type, sentiment words of th e comparative type do not express aregular opinion on an entity but a comparative opinion on more than oneentity, e.g., “ Pepsi tastes betterthanCoke .” This sentence does not expressan opinion saying that any of the two drinks is good or bad. It just says thatcompared to Coke , tastes better. We will discuss comparative andsuperlative sentiment words further in Chapter 8. This chapter focuses onlyon sentiment words of the base type.Researchers have proposed many approaches to compile sentiment words.Three main approaches are: manual approach ,,and. The manual approach is labor intensive andtime consuming, and is thus not usually used alone but combined withautomated approaches as the final check, because automated methods makemistakes. Below, we discuss the tw o automated approaches. Along withthem, we will also discuss the issue of factual statements implying opinions,which has largely been overlooked by the research community.


---

<!-- Página 91 -->

## 6.1 Dictionary-based Approach

Using a dictionary to compile sentiment words is an obvious approachbecause most dictionaries (e.g., Word Net (Miller et al., 1990)) list synonymsand antonyms for each word. Thus, a simple technique in this approach is touse a few seed sentiment words to bootstrap based on the synonym andantonym structure of a dictionary. Sp ecifically, this method works asfollows: A small set of sentiment words (seeds) with known positive ornegative orientations is first collected manually, which is very easy. Thealgorithm then grows this set by searching in the WordNet or another onlinedictionary for their synonyms and antonyms. The newly found words areadded to the seed list. Thenext iteration begins. The iterative process endswhen no more new words can be found. This approach was used in (Hu andLiu, 2004). After the process complete s, a manual inspection step was usedto clean up the list. A similar method was also used by Valitutti, Strapparavaand Stock (2004). Kim and Hovy (2004) tried to clean up the resultingwords (to remove errors) and toassign a sentiment strength to each wordusing a probabilistic method. Mohammad, Dunne and Dorr (2009)additionally exploited many antonym-generating affix patterns likeXdisA more sophisticated approach was propos ed in (Kamps et al., 2004), whichused a WordNet distance based method to determine the sentimentorientation of a given adjective. The distance d

Sentiment Analysis and Opinion Mining

91

,) between terms t12 and tin WordNet. Theorientation of an adjective term t12two reference (or seed) terms good and bad SOd− ,good))/ d*t**SO*The absolute value of SOsimilar line, Williams and Anand (2009) studied the problem of assigningsentiment strength to each word.In (Blair-Goldensohn et al., 2008), a different bootstrappingmethod wasproposed, which used a positive seed set, a negative seed set, and also aneutral seed set. The approach works ba sed ona directed, weighted semanticgraph where neighboring nodes are synonyms or antonyms of words inWordNet andare not part of the seed neutral set. The neutral set is used tostop the propagation of sentiments through neutral words. The edge weightsare pre-assigned based on a scaling parameter for different types of edges,i.e., synonym or antonym edges. Each word is then scored (giving asentiment value) using a modified version of the label propagation algorithmin (Zhu andGhahramani, 2002). At thebeginning, each positive seed wordis given the score of +1, each negative seed is given the score of -1, and all

andis the lengthof the shortest path that connects t2


---

<!-- Página 92 -->

Sentiment Analysis and Opinion Mining

other words are given the score of 0. The scores are revised during thepropagation process. When the propagation stops after a number ofiterations, the final scores after a logarithmic scaling are assigned towordsas their degrees of being positive or negative.In (Rao and Ravichandran, 2009), three graph-based semi-supervisedlearning methods were tried to separate positive and negative words given apositive seed set, a negative seed set, and a synonymgraph extracted fromtheWordNet. The three algorithmswe re Mincut (Blum and Chawla, 2001),Randomized Mincut (Blum et al., 2004), and label propagation (Zhu andGhahramani, 2002). It was shown that Mincut and Randomized Mincutproduced better F scores, but label propagation gave significantly higherprecisions with low recalls.Hassan and Radev (2010) presented a Markov random walk model over aword relatedness graph to produce a sentiment estimate for a given word. Itfirst uses WordNet synonyms and hypernyms to build a word relatednessgraph. A measure, called the mean hitting time ), was then defined andused to gauge the distance from a node i*S*the average number of steps thata randomwalker, starting in state itake to enter a state k for the first time. Given a set of positive seed92 S

*+*and a set of negative seed words S

−). If (

Esuli and Sebastiani (2005) used superv ised learning to classify words intopositive and negative classes. Given a set P*N*synonym and antonym relations in an online dictionary (e.g., WordNet) to

*+*) is greater than h

−, to estimate the sentimentorientation of a given word w*h*

−), the word is classified as negative,otherwise positive. In (Hassan et al., 2011), this method was applied to findsentiment orientations of foreign words. For this purpose, amultilingualword graph was created with both English words and foreign words. Wordsin different languages are connected based on their meanings indictionaries.Other methods based on graphs include those in(Takamura, Inui andOkumura, 2005) and (Takamura, Inui and Okumura, 2007; Takamura, Inuiand Okumura, 2006).In (Turney and Littman, 2003), the same PMI based method as in (Turney,2002) was used to compute the sentiment orientation of a given word.Specifically, it computes the orientation of the word from the strength of itsassociation with a set of positive words ( good , ,,,*fortunate , , and superior ), minus the strength of its association with a*set of negative words ( bad nasty , ,,, , and*inferior ). Theassociation strength is measured using PMI.*

*h* +) and


---

<!-- Página 93 -->

generate the expanded sets P’ N’algorithm then uses all the glosses in the dictionary for each term in P’N’to generate a feature vector. A binary classifier is then built using differentlearning algorithms. The process can also be run iteratively. Thatis, thenewly identified positiveand negative terms and their synonyms andantonyms are added to the training set, an updated classifier can beconstructed and so on. In (Esuli and Sebastiani, 2006), the authors alsoincluded the category objective . To expand the objective seedset,

Sentiment Analysis and Opinion Mining

93

synonyms and antonyms. They then tried differentstrategies to do the three-class classification. In (Esuli and Sebastiani, 2006),a committee of classifiers based on the above method was utilized to buildthe SentiWordNet, a lexical resource inwhich each synset of WordNet isassociated with three numerical scores Obj(s), Pos(s) and Neg(s), describinghow Objective, Positive, and Negative the terms contained in the synset are.The method of Kim and Hovy (2006) also started with three seed sets ofpositive, negative, and neutral words. It then finds their synonyms inWordNet. The expanded sets, however, have many errors. The method thenuses a Bayesian formula to compute the closeness of each word to eachcategory (positive, negative, and neutral) to determine the most probableclass for the word.Andreevskaia and Bergler (2006) proposed amore sophisticatedbootstrapping method withseveral techniques to expand the initial positiveand negativeseed sets and to clean up the expanded sets (removing non-adjectives and words in both positive and negative sets). In addition, theiralgorithm also performs multiple runs of the bootstrapping process usingnon-overlapping seed sub-sets. Each run typically finds a slightly differentset of sentiment words. A net overlapping score for each word is thencomputed based on howmany times the wo rd is discovered in the runs as apositive wordand as a negative word. The score is thennormalized to [0, 1]based on the fuzzy set theory.In (Kaji and Kitsuregawa, 2006; Kaji and Kitsuregawa, 2007), manyheuristics were used to build a sentiment lexicon from HTML documentsbased on Web page layout structures. For example, a table in a Web pagemay have a column clearly indicate positive or negative orientations (e.g.,Pros and Cons) of the surround text. These clues can be exploited to extracta large number of candidate positive and negative opinion sentences from alarge set of Web pages. Adjective phr ases are then extracted from thesesentences and assigned sentiment orientations based on different statistics oftheir occurrences in the positive and negative sentence sets respectively.Velikovich et al. (2010) also proposeda method toconstruct a sentient

hyponymswere used in addition to


---

<!-- Página 94 -->

Sentiment Analysis and Opinion Mining

lexicon usingWeb pages. It was based on a graph propagation algorithmover a phrase similarity graph. It again assumed as input a set of positiveseed phrases and a set of negative seed phrases. The nodes in the phrasegraph were the candidate phrases selected from all n-grams up to length 10extracted from 4 billion Web pages. Only 20 million candidate phrases wereselected using several heuristics, e.g., frequency and mutual information ofword boundaries. A context vector for each candidate phrase was thenconstructed based on a word window of size six aggregated over allmentions of the phrase in the 4 billion documents. The edge set wasconstructed through cosinesimilarity computation of the context vectors ofthe candidatephrases. All edges ( v 94

,) were discarded if they were notoneof the 25 highest weighted ed ges adjacent to either nodev orweight was set to the corresponding cosine similarity value. A graph-propagation method was used to calculate the sentiment of each phrase asthe aggregateof all the bestpaths to the seed words.In (Dragut et al., 2010), yet another but very different bootstrapping methodwas proposed using WordNet. Given a set of seed words, instead ofsimplyfollowing the dictionary, the author s proposed a set of sophisticatedinference rules to determine other words’ sentiment orientations through adeductive process. That is, the algorithm takes words with known sentimentorientations (the seeds) as input an d produces synsets (sets of synonyms)with orientations. The synsets with the deduced orientations can then beused to further deduce the polarities of other words.Peng and Park (2011) presented a sentiment lexicon generation methodusing constrained symmetric nonnegativematrix factorization (CSNMF).The method first uses bootstrapping to find a set of candidate sentimentwords in a dictionary and then uses a large corpus to assign polarity scoresto each word. This method thus uses both dictionary and corpus. Xu, Mengand Wang (2010) presented several integrated methods as wellusingdictionaries and corpora to find emotion words. Theirmethod is based onlabel propagation in a similarity graph (Zhu and Ghahramani, 2002).In summary, we note that the advantage of using a dictionary-basedapproach is that one can easily and quickly find a large number of sentimentwords with their orientations. Althoughthe resulting list can havemanyerrors, a manual checking can be performed to clean it up, which is timeconsuming (not as bad as people thought, only a few days for a nativespeaker) but it is only a one-time effort. The main disadvantage is that thesentiment orientations of words collectedthis way are general or domain andcontext independent. In other words, it is hard to use the dictionary-basedapproach to find domain or context dependent orientations of sentimentwords. As discussed befo re, many sentiment words have context dependent

. The edge*j*


---

<!-- Página 95 -->

orientations. For example, for a speaker phone, if it is quiet, it is usuallynegative. However, for a car, if it is quiet, it is positive. The sentimentorientation of quiet is domain or context dependent. The corpus-basedapproach below can help deal with this problem.

## 6.2 Corpus-based Approach

The corpus-based approach has been applied to twomain scenarios: (1)given a seedlist of known (often general-purpose) sentiment words, discoverother sentiment words andtheir orientations from a domain corpus, and (2)adapt a general-purpose sentiment lexicon to a new one using a domaincorpus for sentiment analysis applications in the domain. However, the issueis more complicated than just building a domain specific sentiment lexiconbecause in the same domain the same word can bepositive in onecontextbut negative in another. Below, we discuss some of the existing works thattried to deal with these problems. Note that although the corpus-basedapproach may also be used to build a general-purpose sentiment lexicon if avery large and very dive rse corpus is available, the dictionary-basedapproach is usually more effective for that because a dictionary has allwords.One of the key and also early ideas was proposed by Hazivassiloglou andMcKeown (1997). The authors used a corpus and some seed adjectivesentiment words to find additional sentiment adjectives in the corpus. Theirtechnique exploited a set of linguistic rules or conventions on connectives toidentifymore adjective sentiment words and their orientations from thecorpus. One of the rules is about the conjunction AND, which says thatconjoined adjectives usually have the same orientation. For example, in thesentence, “ This car is beautiful and spacious ,” if “beautiful” is known to bepositive, it can be inferred that “spacious” is also positive. This is so becausepeople usually express the same sentiment on both sides of a conjunction.The following sentence is not likely, “ This car is beautiful and difficult to*drive. ” It is more acceptable if it is changed to “ This car is beautiful but**difficult to drive. ” Rules were also designed fo r other connectives, i.e., OR,*BUT, EITHER–OR, and NEITHE R–NOR. This idea is called sentiment*consistency . In practice, it is not always consistent. Thus, a learning step was*also applied to determine if two conjoined adjectives have the same ordifferent orientations. First, a graph was formed with same- and different-orientation links between adjectives. Clustering was then performed on thegraph to produce two sets of words: positive and negative.Kanayama and Nasukawa (2006) extended the approach by introducing the

Sentiment Analysis and Opinion Mining

95


---

<!-- Página 96 -->

Sentiment Analysis and Opinion Mining

concepts of intra-sentential (within a sentence) and inter-sentential (betweenneighboring sentences) sentiment consistency, which they call coherency.The intra-sentential consistency is similar to the idea above. Inter-sententialconsistency simply appliesthe idea toneighboring sentences. Thatis, thesame sentiment orientation is usually expressed in consecutive sentences.Sentiment changes are indicated by adversative expressions such as but*however . Some criteria were also proposed to determine whether to add a*word to the positive or negative lexicon. This study was based on Japanesetext and was used to find domain dependent sentiment words and theirorientations. Other related work includes those in (Kaji and Kitsuregawa,2006; Kaji and Kitsuregawa, 2007).Although finding domain specific sentiment words and their orientations areuseful, it is insufficient in practice. Ding, Liu and Yu (2008) showed thatmany words in the same domain can have different orientations in differentcontexts. In fact, this phenomenon has been depicted by the basic rules ofopinions in Section 5.2. For example, in the camera domain, the word “long”clearly expresses opposite opinions in the following two sentences: “The*battery life is ” (positive) and “ It takes a longtimeto focus” (negative).*Such situationsoften occur with quantifiers, e.g., longshort, , ,96“” is positive, but the sentence“ The audio system in the*car is very quiet ” is negative. Thus, finding domain-dependent sentiment*words and their orientations is insufficient. The authors found that both theaspect and the sentiment expressing words were both important. They thenproposed to use the pair ( aspect ,) as an opinion context , e.g.,(“battery life”, “long”). Their method thus determines sentiment words andtheir orientations togetherwith the aspects that they modify. Indeterminingwhether a pair is positive or negative, the above intra-sentential and inter-sentential sentiment consistency rules about connectives are still applied.The work in(Ganapathibhotla and Liu, 2008) adopted the samecontextdefinition but usedit for analyzing comparative sentences. Wu and Wen(2010) dealt with a similar problem in Chinese. However, they only focusedon pairs in which the adjectives are quantifiers such asbig , and*high*also use the Web search hit counts to solve the problem. Lu et al. (2011)used the same context definition as well. Like that in (Ding, Liu and Yu,2008), they assumed that the set of aspects was given. They formulated theproblem of assigning each pair the positive or negative sentiment as anoptimizationproblem with a number of constraints. The objective functionand constraints were designed based on clues such as a general-purposesentiment lexicon, the overall sentiment rating of each review, synonyms


---

<!-- Página 97 -->

and antonyms, as well as conjunction “and” rules, “but” rules, and“negation” rules. To some extent, the methods in (Takamura, Inui andOkumura, 2007; Turney, 2002) can also be considered as an implicit methodfor finding context-specificopinions, but they did not use the sentimentconsistency idea. Instead, they used the Web to find their orientations.However, we should note that all these context definitions are still notsufficient for all cases as the basic rules of opinions discussed in Section 5.2showed, i.e., many contexts can be more complex, e.g., consuming a largeamount of resources.Along a similar line, Wilson, Wiebe, and Hoffmann (2005) studiedcontextual subjectivities and sentiments at the phrase or expression level.Contextual sentiment means that although a word or phrase in a lexicon ismarked positive or negative, but in the context of the sentence expression itmay have no sentiment or have the opposite sentiment. In this work, thesubjective expressions were first labeled in the corpus, i.e., those expressionsthat contain subjective words or phrases in a given subjectivity lexicon. Notethat a subjectivity lexicon is slightlydifferent from a sentiment lexicon assubjectivity lexicon may contains words that indicate only subjectivity butno sentiment, e.g., feel think . The goal of the work was to classify thecontextual sentiment of the given ex pressions that contain instances ofsubjectivity clues in the subjectivity lexicon. The paper took a supervisedlearning approach with two steps. In the first step, itdetermines whether theexpression is subjective or objective. In the second step, it determineswhether the subjective expression is positive, negative, both, or neutral. Bothmeans there are both positive and negative sentiments. Neutral is stillincluded because the first step can make mistakes and left some neutralexpressions unidentified. For subjectivity classification, a large and rich setof features was used, which included word features,(dependency features), structure features (dependency tree based patterns),*sentence features , and document features . For the second step of sentiment*classification, it used features such as word tokens ,,*negations ,*,, etc. For both steps, themachine learning algorithm BoosTexter AdaBoost.HM (Schapire andSinger, 2000) was employed to build classifiers.A related work on expression level sentiment classification was also done in(Choi and Cardie, 2008), where the authors classified the expressionsannotated in Multi-Perspective Qu estion Answering (MPQA) corpus(Wiebe, Wilson and Cardie, 2005). Both lexicon–based classification andsupervised learning were experimented. In (Breck, Choi and Cardie, 2007),the authors studied the problem of extracting sentiment expressions with anynumber of words using Conditional Random Fields (CRF) (Lafferty,

Sentiment Analysis and Opinion Mining

97


---

<!-- Página 98 -->

Sentiment Analysis and Opinion Mining

McCallum and Pereira, 2001).The problem of adapting a general lexicon toa new one for domain specificexpression level sentiment classification was studiedin (Choi and Cardie,2009). Their technique adapted the word-level polarities of ageneral-purpose sentiment lexicon for a particular domain by utilizing theexpression-level polarities in the domai n, and in return, the adapted word-level polarities were used to improve the expression-level polarities. Theword-level and the expression-level polarity relationships were modeled as aset of constraints and the problemwas solved using integer linearprogramming. This work assumed that there was a given general-purposepolarity lexicon L*f* 98

based on the words in el determine the polarity of the opinion expression e,*l* and . Jijkoun, Rijke and Weerkamp (2010) proposed a related method toadapt a general sentiment lexicon to a topic specific one as well.Du et al. (2010) studied the problem of adapting the sentiment lexicon fromone domain (not a general-purpose lexicon) to another domain. As input, thealgorithm assumes the availability of a set of in-domain sentiment-labeleddocuments, a set of sentiment words from these in-domain documents, and aset of out-of-domain documents. The task was to make the in-domainsentiment lexicon adapted for the out-of-domain documents. Two ideas wereused in the study. First, a document should be positive (or negative) if itcontains many positive (or negative) words, and a word should be positive(or negative) if it appears inmany positive (or negative) documents. Theseare mutual reinforcement relationships. Second, even though the twodomains may be under different distributions, it is possible toidentify acommon part between them (e.g. the same word has the same orientation).The sentiment lexicon adaption was solved using the information bottleneckframework. The same problem was also solved in (Du and Tan, 2009).On a slightly different topic, Wiebe and Mihalcea (2006) investigated thepossibilityof assigning subjectivity labels to word senses based on a corpus.Two studies were conducted. The first study investigated the agreementbetween annotators who manually assigned labels subjective,*both to WordNet senses. The second study evaluated amethod for automatic*assignment of subjectivity labels/scores to word senses. The method wasbased on distributional similarity (Lin, 1998). Their work showed thatsubjectivity is a property that can be a ssociated with word senses, and wordsense disambiguation can directly benefit fromsubjectivity annotations. Asubsequent work was reported in (Akkaya, Wiebe and Mihalcea, 2009). Suand Markert (2008) also studied the problem and performed a case study forsubjectivity recognition. In (Su and Mark ert, 2010), they further investigatedthis problemand applied it ina cross-lingual environment.

*l*

, or


---

<!-- Página 99 -->

Brody and Diakopoulos (2011) studied the lengthening of words (e.g.,*slooooow ) inmicroblogs. They showed that lengthening is strongly*associated with subjectivity and sentiment, and presented an automatic wayto leverage this association to detect domain sentiment and emotion words.Finally, Feng, Bose and Choi (2011) studied the problem of producing aconnotation lexicon. A connotation lexicon differs from a sentiment lexiconin that the latter concerns words that express sentiment either explicitly orimplicitly, while the former concerns wo rds that are often associatedwith aspecific polarity of sentiment, e.g., award and promotion have positiveconnotation and cancer and warmethod based on mutual reinforcement was proposed tosolve the problem.

## 6.3

Sentiment words and expressions that we have discussed so far are mainlysubjective words and expressions that indicate positive or negative opinions.However, as mentioned earlier, many objective words and expressions canimply opinions too in certain domains or contexts because they can representdesirable or undesirable facts in these domains or contexts.In (Zhang and Liu, 2011b), a method was proposed to identify nouns andnoun phrases that are aspects and also imply sentiments in a particulardomain. These nouns and noun phrases alone indicate no sentiments, but inthe domain context theymay represent desirable or undesirable facts. Forexample, “valley” and “mountain” do not have any sentiment connotation ingeneral, i.e., they are objective. However, in the domain of mattress reviews,theyoften imply negative opinions as in “ Withina month, a valley has*formed in the middle of the mattress .” Here, “valley” implies a negative*sentiment on the aspect of mattress quality. Identifying the sentimentorientations of such aspects is very challenging but critical for effectivesentiment analysis in these domains.The algorithm in (Zhang and Liu, 2011b) was based on the following idea:Although such sentences are usually objective with noexplicit sentiments, insome cases the authors/reviewers may al so give explicit sentiments, e.g.,“*terrible .” The context of this sentence indicates that “valley” maynot be*desirable. Note that this work assumed that the setof aspects whicharenouns and noun phrases are given. However, the problemwith this approachis that those aspects (nouns and noun phrases) with no implied sentimentmay also be in some positive or negative sentiment contexts, e.g., “voicequality” in “ The voice quality is poor .” To distinguish these two cases, the

Sentiment Analysis and Opinion Mining

99


---

<!-- Página 100 -->

Sentiment Analysis and Opinion Mining

following observation was used.**Observation : For normal aspects which themselves don’t have positive or**negative connotations, people can express different opinions, i.e., bothpositive and negative. For example, for aspect “voice quality”, peoplecan say “good voice quality” and “bad voice quality”. However, foraspects which represent desirable or undesirable facts, they often haveonlya single sentiment, either positiveor negative, but not both. Forexample, it is unlikely thatboth the following two sentences appear: “A*bad valley has formed ” and “ a good valley has formed”.*With this observation in mind, the approach consists of two steps:1.: This step determines the surrounding sentimentcontext of each noun aspect. If an aspect occurs in negative (respectivelypositive) sentiment contexts significantly more frequently than in positive(or negative) sentiment contexts, it is inferred that its polarity is negative(or positive). This step thus produces a list of candidate aspects withpositive opinions and a listof candidate aspects with negative opinions.2.: This step prunes the two lists based on the observation above.The idea is that when a noun aspect is directly modified by both positiveand negativesentiment words, it is unlikely to be an opinionated aspect.100Type 1: O  It means O*F**O-Dep , e.g., “ This TV**has a good picturequality. ”*

Type 2: O    It means both O F*H**O-Dep and F-**Dep**The springs of the mattress are bad .”*

where O*O-Dep / F-Dep is a dependencyrelation. F*is the noun aspect. H“picture quality”, we can identify itsmodification sentiment word“good.” For the second example, given aspect “springs”, we can get itsmodification sentiment word “bad”. Here HThis work is just the first attempt to tackle the problem. Its accuracyis stillnot high. Much further researchis needed.

## 6.4 Summary

Due tocontributions ofmany researchers, several general-purposesubjectivity, sentiment, and emotion lexicons have been constructed, andsome of them are alsopubl ically available, e.g.,


---

<!-- Página 101 -->

([http://www.wjh.harvard.edu/~inqui](http://www.wjh.harvard.edu/~inqui) rer/ spreadsheet_guide.htm)([http://www.cs.uic.edu/~liub/FBS/](http://www.cs.uic.edu/~liub/FBS/) sentiment-analysis.html)([http://www.cs.pitt.edu/mpqa/subj](http://www.cs.pitt.edu/mpqa/subj) _lexicon.html)([http://sentiwordnet.isti.cnr.it/)](http://sentiwordnet.isti.cnr.it/))([http://www.purl.org/net/emolex)](http://www.purl.org/net/emolex))However, domain and context dependent sentiments remain to be highlychallenging even with so much research. Recent work also used word vectorand matrix to capture the contextual information of sentiment words (Maaset al., 2011; Yessenalina and Cardie, 2011). Factual words and expressionsimplying opinions have barely been studied (see Section 6.3), but they arevery important for many domains.Finally, we note that having a sentiment lexicon (even with domain specificorientations) does not mean that a word in the lexicon always expresses anopinion/sentiment in a specific sentence. For example, in “I am looking for a*good car to buy ,” “good” here does not express either a positive or negative*opinion on any particular car.

Sentiment Analysis and Opinion Mining

101


---

<!-- Página 102 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 7

102

## Opinion Summarization

As discussed in Chapter 2, inmost sentiment analysis applications, oneneeds to study opinions frommany people because due tothe subjectivenature of opinions, looking at only the opinion from a single person isusually insufficient. Some form of summary is needed. Chapter 2 indicatedthat the opinion quintuple provides the basic information for an opinionsummary. Such a summary is called an aspect-based summary*based summary )*Cheng, 2005). Much of the opinion summarization research usesrelatedideas. This framework is also widely applied in industry. For example, thesentiment analysis systems of Micros oftBing and Google Product Searchuse this formof summary. The output su mmary can be either in a structuredform (see Section 7.1) or in an unstructu red form as a short text document.In general, opinion summarization can be seen as a form of multi-document*text summarization . Text summarization has been studied extensivelyin*NLP (Das, 2007). However, an opinion summary is quite different from atraditional single document or multi-document summary (of factualinformation) as an opinion summary is of ten centered on entities and aspectsand sentiments about them, and also ha sa quantitative side, which are theessence of aspect-based opinion su mmary. Traditional single documentsummarization produces a short text from a long text by extracting some“important” sentences. Traditional multi-document summarization findsdifferences among documents and discards repeated information. Neither ofthem explicitly captures different topics/entities and their aspects discussedin the document, nor do they have a quantitative side. The “importance” of asentence in traditional text summarization is often defined operationallybased on the summarization algorithmsand measures used in each system.Opinion summarization, on the other hand, can be conceptually defined. Thesummaries are thus structured. Even for output summaries that are short textdocuments, there are still some e xplicit structures in them.

## 7.1 Aspect-based Opinion

## Summarization


---

<!-- Página 103 -->

Aspect-based opinion summarization has two main characteristics. First, itcaptures the essence of opinions: opinio n targets (entities and their aspects)and sentiments about them. Second, it is quantitative, which means that itgives the number or percent of people who hold positive or negativeopinions about the entities and aspect s. The quantitative side is crucialbecause of the subjective nature of opinions. The resulting opinion summaryis a form of structured summary produced from the opinion quintuple inSection 2.1. We have described the summary in Section 2.2. It is reproducedhere for completeness. Figure 7.1 shows an aspect-based summary ofopinions about a digital camera (Hu and Liu, 2004). The aspect GENERALrepresents opinions on the camera as a whole, i.e., the entity. For each aspect(e.g., picture quality), it shows how many people have positive and negativeopinions respectively. <individual review sentences> links to the actualsentences (or full reviews or blogs). This structured summary can also bevisualized (Liu, Hu and Cheng, 2005). Figure 7.2(A) uses a bar chart tovisualize the summary in Figure 7.1. In the figure, each bar above the Xshows the number of positive opinions about the aspect given at the top. Thecorresponding bar below the Xon the same aspect. Clicking on each bar, we can see the individualsentences and full reviews. Obviously, other visualizations are also possible.For example, the bar charts of both Microsoft Bing search andGoogleProduct Search use the percent of positiveopinions on eachaspect.Comparing opinion summaries of a few entities is evenmore interesting(Liu, Hu and Cheng, 2005). Figure 7.2(B) shows the visual opinioncomparison of two cameras. We can see how consumers view each of themalong different aspect dimensions including the entities themselves.The opinion quintuples in fact allows one to providemanymore forms ofstructured summaries. For example, if time is extracted, one can show thetrend of opinions on different aspects. Even without using sentiments, onecan see the buzz (frequency) of each asp ect mentions, which gives the useran idea what aspects people are most concerned about. In fact, with thequintuple, a full range of database and OLAP tools can be used to slice anddice the data for all kinds of qualitative and quantitative analysis. Forexample, in one practical sentiment an alysis application in the automobiledomain, opinion quintuples of individual cars were mined first. The userthen compared sentiments about small cars, medium sized cars, German carsand Japanese cars, etc. In addition, the sentiment analysis results were alsoused as raw data for datamining. Theuser ran a clustering algorithm andfound some interesting segments of the market. For example, it was foundthatone segment of the customers always talkedabout how beautiful andslick the car looked and how fun it was to drive, etc, while another segmentof the customers talked a lot about b ack seats and trunk space, etc. Clearly,

Sentiment Analysis and Opinion Mining

103


---

<!-- Página 104 -->

Sentiment Analysis and Opinion Mining

104

*Digital Camera*1:Aspect:**GENERAL**105 <individual review sentences>12 <individual review sentences>Aspect:**Picture quality**95 <individual review sentences>10 <individual review sentences>Aspect:**Battery life**50 <individual review sentences>9 <individual review sentences>**…****Figure 7.1. An aspect-based opinion summary.**the first segment consisted of mainly young people, while the secondsegment consisted mainly of peoplewith families and children. Suchinsights were extremely important. They enabled the user to see the opinionsof different segments of customers.

**Figure 7.2. Visualization of aspect-based summaries of opinions**This form of structured summary has also been adopted by other researchersto summarize movie reviews (Zhuang, Jing and Zhu, 2006), to summarizeChinese opinion text (Ku, Liang and Chen, 2006), and to summarize service

**Negative**

(A) Visualization of aspect-based su mmary of opinions on a digital camera

(B) Visual opinion comparison of two digital cameras **Positive**

**Negative**

**Positive GENERAL Picture Batter**

**GENERAL Picture Battery Lens Weight Size**

Digital camera 1

DiDigital camera 1

**y****Lens Wei**

gital camera

**g****ht Size**


---

<!-- Página 105 -->

reviews (Blair-Goldensohn et al., 2008). However, we should note thataspect-based summary does not have to be in this structured form. It can alsobe inthe form of a textdocument based on the same idea. In the nextsection, we discuss othe r related researches.

## 7.2 Improvements to Aspect-based

## Opinion Summarization

Several improvements and refinements have been proposed by researchersfor the basic aspect-based summary. Carenini, Ng and Pauls (2006)proposed to integrate aspect-basedsu mmarization with two traditional textsummarization approaches of factual documents, i.e., sentence selection (orextraction) and sentence generation. We discuss the integration with thesentence selection approach first. Their system first identifies aspectexpressions from reviews of a particular entity (e.g., a product) using themethod in (Hu and Liu, 2004). It thenmaps the aspect expressions to somegiven aspect categories organized as anontology treefor the entity. Theseaspects in the tree are then scored based on their sentiment strength. Thosesentences containing aspect expressions are alsoextracted. Each suchsentence is then rated based on scores of aspects inthesentence. If multiplesentences have the same sentence rating, a traditional centroid basedsentence selection method is used to break the tie (Radev et al., 2003). Allrelevant sentences are attached to their corresponding aspects in theontology. The sentences for each aspect are then selected for the finalsummary based on sentencescores and aspect positions in the ontology tree.The integration with the sentence generation approachworks similarly. First,a measure is used to score the aspe cts in the ontology based on theiroccurrence frequencies, sentiment strengths, and their positions in theontology. Analgorithm is also applied toselect aspects in the ontology tree.Positive and negative sentiments are then computed for the aspects. Basedon the selected aspects andtheir sentiments, a language generator generatesthe summarysentences which can be qualitative and quantitative. A userevaluation was carried out to assess the effectiveness of the two integrationapproaches. The results showed that they performed equally well, but fordifferent reasons. The sentence selection method gave more variedlanguages andmore details, while the sentence generation approach gives abetter sentiment overview of the reviews.In (Tata and Di Eugenio, 2010), Tata and Eugenio produced an opinionsummary of song reviews similar tothatin (Hu and Liu, 2004), but for eachaspect and each sentiment (postive or ngative) they first selected a

Sentiment Analysis and Opinion Mining

105


---

<!-- Página 106 -->

Sentiment Analysis and Opinion Mining

representative sentence for the group. The sentence shouldmention thefewest aspects (thus the representative sentence is focused). They thenordered the sentences using a given domain ontology bymapping sentencesto the ontology nodes. The ontology basically encodes the key domainconcepts and their relations. The sent ences were ordered and organizedintoparagraphs following the tree suchthat they appear in a conceptuallycoherent fashion.Lu et al. (2010) also used online ontologies of entities and aspects toorganize and summarize opinions. Their method is related to the above two,but is also different. Their system fi rst selects aspects that capturemajoropinions. The selection is done by frequency, opinion coverage (noredundancy), or conditional entropy. It then orders aspects and theircorresponding sentences based on a co herence measure, which tries tooptimize the ordering so that they best follow the sequences of aspectappearances intheir originalpostings.Ku, Liang, and Chen (2006) performed blog opinion summarization, andproduced two types of summaries: brief and detailed summaries, based onextracted topics (aspects) and sentiments on the topics. For the briefsummary, their method picks upthe document/article with the largest106the overall summary of positive-topical or negative-topical sentences. Fordetailed summary, it lists positive-topical and negative-topical sentenceswith high sentiment degrees.Lerman, Blair-Goldensohn and McDonald (2009) defined opinionsummarization in a slightly different way. Given a set of documents Dreviews) that contains opinions about some entity of interest, the goal of anopinion summarization system is to generate a summarySis representative of the average opinion and speaks to its important aspects.This paper proposed three differentmodels to performsummarization ofreviews of a product. All these models choose some set of sentences from areview. The first model is called sentiment match (SM), which extractssentences so that the average sentim ent of the summary is as close aspossible to the average sentiment rating of reviews of the entity. The secondmodel, called sentiment match + aspect coverage (SMAC), builds asummary that trades-off between maximally covering important aspects andmatchingthe overall sentiment of the entity. The third model, called*sentiment-aspect match (SAM), not only attempts to cover important*aspects, butcover themwith appropriate sentiment. A comprehensiveevaluation of human users was conducted to compare the three types ofsummaries. It was found that although theSAM model was the best, it is notsignificantlybetter than others.


---

<!-- Página 107 -->

In (Nishikawa et al., 2010b), a more sophisticated summarization techniquewas proposed, which generates a traditional text summary by selecting andordering sentences taken frommultip le reviews, considering bothinformativeness and readability of the final summary. The informativenesswas defined as the sum of frequency of each aspect-sentiment pair.Readability was defined as the natural sequence of sentences, which wasmeasured as the sum of the connectiv ity of all adjacent sentences in thesequence. The problem was then solved through optimization. In (Nishikawaet al., 2010a), the authors further studied this problem using an integer linearprogramming formulation. In (Ganesan, Zhai and Han, 2010), a graphicalmodel basedmethod was used to generate an abstractive summary ofopinions. In (Yatani et al., 2011), adjective-noun pairs were extracted as asummary.

## 7.3 Contrastive View Summarization

Several researchers also studied the problem of summarizing opinions byfinding contrastive viewpoints. For example, a reviewermay give a positiveopinion about the voice qualityof iPhone by saying “The voice quality of*iPhone is really good ,” but another reviewer may say the opposite, “The**voice quality of myiPhone is lousy .” Such pairs can give the reader a direct*comparative viewof different opinions.Kim and Zhai (2009) proposed and studied this problem. Given a positivesentence set and a negative sentence set, this work performed contrastiveopinion summarization by extracting a set of kfrom the sets. A pair of opinionated sentences ( x*contrastive**sentence pair if sentence x**y*but have opposite sentiment orientations. The kalso represent both the positive and negative sentence sets well. The authorsformulated the summarization as an optimization problem and solved itbased on several similarity functions.Paul, Zhai and Girju (2010) worked on this problem as well. Their algorithmgenerates a macro multi-view summary and a micro multi-view summary. Amacro multi-view summary contains multiple sets of sentences, eachrepresenting a differentopinion. A micro multi-view summary contains a setof pairs of contrastive sentences ( each pair consists of two sentencesrepresenting two different opinions). The algorithm works intwo steps. Inthe first step, it uses a topic modeling approach to modeling and mining bothtopics (aspects) and sentiments. In the second step, a random walkformulation (similar to PageRank (Page et al., 1999)) was proposed to score

Sentiment Analysis and Opinion Mining

107


---

<!-- Página 108 -->

Sentiment Analysis and Opinion Mining

sentences and pairs of sentences from opposite viewpoints based on boththeir representativeness and their contrastiveness witheach other. Along asimilar line, Park, Lee and Song (2 011) reported another method forgenerating contrasting opposing views innews articles.In (Lerman and McDonald, 2009), Lerman and McDonald formulated adifferent contrastive summarization problem. They wanted to producecontrastive summaries of opinions abouttwo differentproducts to highlightthe differences of opinionsabout them. Their approach is to jointlymodelthe two summarization tasks and in optimization toexplicitly consider thefact that it wants the two summaries to contrast. 108

## 7.4 Traditional Summarization

Several researchers havealso studied opinion summarization in thetraditional fashion, e.g., producing a short text summary with limited orwithout consideration of aspects (or topics) and sentiments about them. Asupervisedlearningmethod was proposed in (Beineke etal., 2003) to selectimportant sentences in reviews. A paragraph-clustering algorithm wasproposed in (Seki et al., 2006) to also select a set of important sentences.In (Wang and Liu, 2011), the authors studied extractive summarization(selection of important sentences) of opinions in conversations. Theyexperimented with both the traditional sentence ranking and graph-basedapproaches, but also considered addition al features such as topic relevance,sentiments, and the dialogue structure.A weakness of such traditional summaries is that theyonly have limited orno consideration of target entities and aspects, and sentiments about them.Thus, they may select sentences which are not related to sentiments or anyaspects. Another issue is that there is no quantitative perspective, which isoften important in practice because one out of ten people hating something isvery different from 5 out of ten people hating something.

## 7.5 Summary

Opinion summarization is still an active research area. Most opinionsummarization methods which produce a short text summary have notfocused on the quantitative side (proportions of positive and negativeopinions). Future research can deal with this problemwhile also producinghuman readable texts. We should no te that the opinion summarization


---

<!-- Página 109 -->

research cannot progress alone because it critically depends on results andtechniques from other areas of research in sentiment analysis, e.g., aspect ortopic extraction and sentiment classification. All these research directionswill need to go hand-in-hand. Finally, we should also note that based on thestructured summary in Section 7.1 one can generate natural languagesentences as well based on what are s hown in the bar charts using somepredefined sentence templates. For instance, the first bar in Figure 7.2(B)can be summarized as “70% of the peopleare positive about digital camera 1in general.” However, this may not be the best sentence for people’s readingpleasure.

Sentiment Analysis and Opinion Mining

109


---

<!-- Página 110 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 8

110

## Analysis of Comparative Opinions

Apart from directly expressing positive or negative opinions about an entityand its aspects, one can also express op inions by comparing similar entities.Such opinions are called comparative opinions (Jindal and Liu, 2006a;Jindal and Liu, 2006b). Comparative opinions are related to but are alsodifferent fromregular opinions. They not only have different semanticmeanings but also have different syntactic forms. For example, a typicalregular opinion sentence is “ The voice quality of this phone is amazing,” anda typical comparative opinion sentence is “ The voice quality of Nokia phones*is better than that of iPhones .” This comparative sentence does not say that*any phone’s voice quality is good or bad, but simply compares them. Due tothis difference, comparative opinions require different analysis techniques.Like regular sentences, comparative sentences can be opinionated or not-opinionated. The comparative sentence above is opinionated because itexplicitly expresses a comparative sentiment of its author, while the sentence“1” expresses no sentiment.In this chapter, we first define the problem and thenpresent some existingmethods for solving it. We should also note that there are in fact two maintypes of opinions thatare based on comparisons: comparative opinions and*superlative opinions . In English, they are usually expressed using the**comparative or*forms of adjectives or adverbs, but not always.However, in this chapter, we study them together and just call themcomparativeopinions ingeneral because their semantic meanings andhandling methods are similar.

## 8.1

A comparative sentence expresses a relation based on similarities ordifferences ofmore than one entity. There are several types of comparisons.They can begrouped intotwo main categories: gradable comparison and*non-gradable comparison (Jindaland Liu, 2006a; Kennedy, 2005).***Gradable comparison: Such a comparison expresses anordering**relationshipof entitiesbeing compared. Ithas three sub-types:1.: It expresses a relation of the type


---

<!-- Página 111 -->

Sentiment Analysis and Opinion Mining

*greater or*that ranks a set of entities over another set of entitiesbased on some of their shared aspects, e.g., “ Coke tastes better than*Pepsi .” This type also includes preference, e.g., “I prefer Coke to**Pepsi .”*2.: It expresses a relation of the type equal to thatstates two ormore entities are equal based on some of their sharedaspects, e.g., “ Coke and Pepsi taste the same .”3.: It expresses a relationof the type greater or*less than all others that ranks one entity over all**Coke**tastes the best among all soft drinks .”***Non-gradable comparison: Such a comparison expresses a relation of two**or more entities but does not grade them . There are three main sub-types:

1.Entity A*B*shared aspects, e.g., “ Coke tastes differently fromPepsi.”

2.Entity A*a*

3.Entity A*a**B**Nokia phones**come with earphones, but iPhones donot. ”*We only focus on gradable comparisons in this chapter. Non-gradablecomparisons may also express opinions but they are often more subtle anddifficult to recognize.In English, comparisons are usually expressed usingcomparative words(also called comparatives ) and superlative words (also called superlatives).Comparatives are formed by adding the suffix -formed by adding the suffix -est*base adjectives and adverbs . For*example, in “ The battery life of Nokia phones is longer than Motorola*phones ,” “longer” is the comparative form of the adjective “long.” “longer”*(and “than”) here also indicates that this is a comparative sentence. In “The*battery life of Nokia phones is the longest ,” “longest”*of the adjective “long”, an d it indicates thatthis is a superlative sentence.We call this type of comparatives and superlatives Type 1 comparatives and*superlatives . Note that for simplicity, we often usecomparative to mean*bothandif superlative is not explicitly stated.However, adjectives and adverbs with two syllables or more and not endingin*er est**more , , , and least**more beautiful .*We call this type of comparatives and superlatives Type 2 comparatives*superlatives . Both Type 1 and Type 2 are called regular comparatives and**superlatives .*

111

, and entity B*a*1(and asubstitutable), e.g., “ Desktop PCs use external speakers but laptops use21*internal speakers .”*are usually


---

<!-- Página 112 -->

Sentiment Analysis and Opinion Mining

English also has irregular comparatives superlatives, i.e., more, ,*less least better , , , ,*and furthest/farthest ,which do not follow the above rules. However, they behave similarly toType 1 comparatives and are thus groupedunder Type 1.These standard comparatives and superl atives are only some of the wordsthat indicate comparisons. In fact, there are many other words and phrasesthat can be used to express comparisons, e.g., prefer and superior. Forexample, the sentence “ iPhone’s voice quality is superior to that of*Blackberry ” says that iPhone has a better voice quality and is preferred. In*(Jindal and Liu, 2006a), a list of suchwords and phrases were compiled(which bynomeans is complete).behave1. All these words and phrases plus the above standard comparatives andsuperlatives are collectively called comparative keywords.Comparative keywords usedin non-equal gradable comparisonscan befurther grouped into two categories according to whether they expressincreasedor decreased quantities, whic h are useful in sentiment analysis.: Such a comparative expresses an increasedquantity, e.g., more and .112Such a comparative expresses a decreasedquantity, e.g., less fewer .**Objective of mining comparative opinions (Jindal and Liu, 2006b; Liu,**2010): Given an opinion document d*d*opinion sextuples of the form:(*E*

,,),1where 2

and Eare the entity sets being compared based on their sharedaspects 2*E*1 appear before entities in E1 ,}) is thepreferred entity set of the opinionholder h ttime when the comparative opinion is expressed. For a superlative1comparison, if one entity set is implicit (not given in the text), we can usea special set Uspecial symbol EQUAL as the value for PEFor example, consider the comparative sentence “ Canon’s picture quality is*better than those of LG and Sony ,” written by Jim on 9-25-2011. The*extracted comparative opinion is:The entity set E

is {Canon}, the entity set E1

in the sentence), PE2(

is {LG, Sony }, their sharedaspect set A2


---

<!-- Página 113 -->

{Canon}, the opinion holder h*t*opinion was written is 9-25-2011.Note that the above representation may not be easily put in a database due tothe use of sets, but it can be easilyconverted tomultiple tuples withno sets,e.g., the above sets based sextuples can be expanded into two tuples:(Canon, LG, picture_quality, Canon, Jim, Dec-25-2010)(Canon, Sony, picture_quality, Canon, Jim, Dec-25-2010)Like mining regular opinions, mining comparative opinions needs to extractentities, aspects, opinion holders, and times. The techniques used are similartoo. In fact, these tasks are often easier for comparative sentences becauseentities are usually on the two sides of the comparative keyword, and aspectsare also near. However, for sentiment anal ysis to identify the preferred entityset, a differentmethod is needed which we will discuss in Section 8.3. Wealso need to identify comparative se ntences themselves because not allsentences containing comparative keywords express comparisons and manycomparativekeywords and phrases arehard to identify (Jindal and Liu,2006b). Below, we only focus on studying two comparative opinionsentiment analysis specific problems, i.e., identifying comparative sentencesand determining the preferred entity set.

## 8.2

Although most comparative sentences contain comparative and superlativekeywords, e.g., better ,, and bestwords are not comparative sentences, e.g., “ I cannot agree with you more.”In (Jindal and Liu, 2006a), it was sh own that almost every comparativesentence has a keyword (a word or phrase) indicating comparison. Using aset of keywords, 98% of comparative sentences (recall = 98%) wereidentified with a precision of 32% based on their data set. The keywords are:1.*more ,**less better , and words ending with -er*keywords.2.superlative adverbs (RBS), e.g., most*least best**-est*two keywords.3.*favor , ,**exceed ,*, ,,,*up against , etc. These are counted indi vidually in the number of*keywords.

Sentiment Analysis and Opinion Mining

113


---

<!-- Página 114 -->

Sentiment Analysis and Opinion Mining

Since keywords alone are able to achiev e a high recall, they can be used tofilter out those sentences that are unlikely to be comparative sentences. Wejust need to improve the precision on the remaining sentences.It was also observed in (Jindal and Liu, 2006a) that comparative sentenceshave strong patterns involving comparative keywords, which is notsurprising. These patterns can be used as features in learning. To discoverthese patterns, class sequential rule (CSR) mining was employed in (Jindaland Liu, 2006a). Class sequential rule mining is a special kind of sequentialpattern mining (Liu, 2006 and 2011). Each training example is a pair (s 114

is a sequenceand y*i*

For classification model building, the left-hand side sequence patterns of theCSR rules with high conditional probabilities were used as features. NaïveBayes was employed for model building. In (Yang and Ko, 2011), the sameproblem was studied but in the context of Korean language. The learningalgorithm used was the transformation-based learning, which produces rules.**Classifying comparative sent ences into four types: After comparative**sentences are identified, the algorithm also classifies them into four types,*non-equal gradable ,*,, non-gradable . For this task,(Jindal and Liu, 2006a) showed that keywords and keyphrases as featureswere already suffi cient. SVM gave the best results.

Li et al. (2010) studied the problem of identifying comparative questionsand the entities (which they call comp arators) that are compared. Unlikethe works above, this paper did not decide the types of comparison. Forcomparative sentences identification, they also used sequentialpatterns/rules. However, their pa tterns are different. They decidedwhether a question is a comparative question and the entities beingcompared at the same time. For example, the question sentence “Which*city is better, New York or Chicago ?” satisfies the sequential pattern*<which NN is better, $C or $C ?>, where $C is an entity. A weaklysupervised learning method based on the idea in (Ravichandran andHovy, 2002) was used to learn such patterns. The algorithm is based onbootstrapping, which starts with a user -given pattern. From this pattern,the algorithm extracts a set of initial se ed entity (comparators) pairs. Foreach entity pair, all questions containing the pair are retrieved from thequestion collection and regarded as comparative questions. From thecomparative questions and entity pair s, all possible sequential patternsare learned and evaluated. The learning process is the traditional

is a class label, i.e., y*i*

,*comparison }. The sequenceis generated from a sentence. Using the training**i*data, CSRs can be generated.

,),*i**i*where s


---

<!-- Página 115 -->

generalization and specialization pro cess. Any words or phrases whichmatch $C in a sentence are entities. Both (Jindal and Liu, 2006b) and(Yang and Ko, 2011) also extract compared entities. We will discussthem in Section 8.4. Other information extraction algorithms areapplicable here as well.

## 8.3

Unlike regular opinions, itdoes not make much sense to perform sentimentclassification to a comparative opinion sentence as a whole because such asentence does not express a direct positive or negative opinion. Instead, itcompares multiple entities by ranking the entities based on their sharedaspects to give a comparative opinion . That is, it expresses a preferenceorder of theentities using comparison. Since most comparative sentencescompare two sets of entities, the anal ysis of an opinionated comparativesentencemeans to identify the preferred entity set. However, for applicationpurposes, onemay assign positive opinions to the aspects of the entities inthe preferred set, and negative opinions to the aspects of the entities in thenot preferred set. Note that like regular sentences, it is still meaningful toclassify whether a comparative sentence expresses an opinion or not, butlittle research has been done on such classification. Below we only describea method for identifying the preferred entity set.The method, proposedin (Ding, Liu and Zhang, 2009) and in(Ganapathibhotla and Liu, 2008), ba sically extends the lexicon-basedapproach to aspect based sentiment classification of regular opinions tocomparative opinions. It thus needs a sentiment lexicon for comparativeopinions. Similar to opinion words of the base type, we can dividecomparative opinion wordsintotwo categories:1.: For Type 1comparatives, this categoryincludes words like better, , etc., whichoften have domain independent positive or negative sentiments. Insentences involving such words, it is often easy to determine which entityset is preferred. In the case of Type 2 comparatives, formed by adding*more , , , or before adjectives/adverbs, the preferred entity*sets are determined byboth words. The following rulesare applied:Comparative Negative|Comparative Positive ::= increasing_comparativeP| decreasing_comparative N

Sentiment Analysis and Opinion Mining

115


---

<!-- Página 116 -->

Sentiment Analysis and Opinion Mining

tive (negative) sentiment word orphrase of the base type. The first rule above says that the combination ofan increasing comparative (e.g., more ) and a negative sentiment word(e.g., awful ) implies a negative comparative opinion (on the left). Theother rules have similar meanings. Note that the above four rules havealready been discussed as basic rules of opinions in Section 5.2.2.: In the case of Type 1comparatives, such words include higher , , etc. For example,“” carries acomparative positive sentiment about “Nokia phones” and a comparativenegative sentiment about “Motorola phones,” i.e., “Nokia phones” arepreferred with respect to the battery life aspect. However, withoutdomain knowledge it is hard to know whether “longer” is positive ornegative for battery life. This issue is the same as for regular opinions,and this case has alsobeen included in the basic rules of opinions inSection 5.2. Here, “battery life” is a positive potential item(PPI).In the case of Type 2 comparatives, the situation is similar. However, inthis case the comparative word ( more , , or leastadjective/adverb, and the aspect are all important in determining thepreference. If we know whether the comparative word is an increasing or116decreasing comparative (which is easy since there are only four of them),then the opinion can be determined by applying the four rules in (1).As discussed in Section 6.2, the pair ( aspect ,)forms an opinion context. To determine whether a pair is positive ornegative, the algorithm in (Ganapathibhotla and Liu, 2008) uses a largeamount of external data. It employed a large corpus of Pros and Consfrom product reviews. The idea is to determine whether the aspect and*context_sentiment_word are more associated with each other in Pros or in*Cons. If they are more associated in Pros,ismost likely tobe positive. Otherwise, it islikely tobe negative. However,since Pros and Cons seldom use comparative opinions, the contextopinion words in a comparative sentence have tobe converted to its baseform, which can be done using WordNet with the help of Englishcomparative formation rules. This conversion is useful because of thefollowing observation.*Observation: If an adjective or adverb of the base form is positive (or*negative), then its comparative or superlative form is also positive (ornegative), e.g., good , , and bestAfter the conversion, these word s are manually categorized intoincreasing and decreasin g comparatives. For context dependent opinion


---

<!-- Página 117 -->

words, comparative words can alsobe converted totheir base forms.After the sentiment words and their orientations are identified,determiningwhich entity set is preferred is fairly simple. Withoutnegation, if the comparative is positive (or negative), then the entitiesbefore (or after) thanthe entities after (or before)*than*Zhang, 2009; Ganapathibhotla and Liu, 2008).

## 8.4 Summary

Although there have been some existing works, comparative sentences havenot been studied as extensively as many other topics of sentiment analysis.Further research is still needed. One of the difficult problems is how toidentifymany types of non-standard or implicit comparative sentences, e.g.,“.”Without identifying them, further sentiment analysis is hard to perform.Apart from identifyingcomparative sentences andtheir types, severalresearchers have also studied the extr action of compared entities, comparedaspects, and comparative words. Jindal and Liu (2006b) used labelsequential rule mining, which is a supervised learning method based onsequential patterns. Yang and Ko (2011) applied the Maximum Entropy andSVM learning algorithms to extract compared entities and comparativepredicates, which are aspects that are compared. As noted in Section 8.2,sequential patterns in (Li et al., 20 10) for identifying comparative questionscan already identify compared entities. However, their work is limited in thesense that it only works with simple comparative questions. In (Fiszman etal., 2007), the authors studied the problem of identifying which entity hasmore of certain aspects in comparative sentences in biomedical texts, butthey did notanalyze opinions in comparisons.

Sentiment Analysis and Opinion Mining

117


---

<!-- Página 118 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 9

118

## Opinion Search and Retrieval

As Web search has proven to be a valuab le service on the Web, it is not hardto imagine that opinion search will also be of great use. Two typical kinds ofopinion search queries are:1.e.g., find customer opinions about a digital camera or the picture qualityof the camera, and find public opinions about a political issue orcandidate.2.particular entity or an aspect of the entity (or topic), e.g., find BarackObama’s opinionabout abortion. This type of search is particularlyrelevant to news articles, where individuals or organizations whoexpress opinions are explicitly stated.For the first type of queries, the user may simply give the name of the entityor the name of the aspect together with the name of the entity. For thesecond type of queries, the user may gi ve the name of the opinion holder andthe name of the entity or topic.

## 9.1

Similar to traditional Web search, opinion search also has two major tasks:1) retrieve relevant documents/sentences to the user query and 2) rank theretrieved documents or sentences. Howeve r, there are alsomajor differences.On retrieval, opinion search needs to perform two sub-tasks:1.onlytask performed in the traditional Web searchor retrieval.2.query topic (entity and/or aspect) and whether the opinions are positiveor negative. This is the task of sentiment analysis. Traditional searchdoes not performthis sub-task.As for ranking, traditional Web searchengines rankWeb pages based onauthority andrelevance scores (Liu, 2006 and 2011). The basic premise isthat the top ranked pages (ideally the first page) contain sufficientinformation to satisfy the user’s information need. This paradigm is adequate


---

<!-- Página 119 -->

for factual information search because one fact equals to any number of the*same fact . That is, if the first page contains the required information, there is*no need to see the rest of the relevant pages. For opinion search, thisparadigm is fine only for the second type of queries because the opinionholder usually has only one opinion about a particular entity or topic, and theopinion is contained in a single document or page. However, for the firsttype of opinion queries, this paradigm needs to be modified because rankingin opinion search has two objectives. First, it needs to rank those opinionateddocuments or sentences with high utilities or information contents at the top(see Chapter 11). Second, it needs toreflectthe natural distribution ofpositive and negative opinions. This se cond objective isimportant becausein most applications the actual proportions of positive and negative opinionsare critical pieces of information. Only reading the top ranked result as in thetraditional search is problematic because the top result only represents theopinion of a single opinion holder. Thus, ranking in opinion search needs tocapture the natural distribution of positive and negative sentiments of thewhole population. One simple solution for this is to produce two rankings,one for positive opinions and one for negative opinions, and also to displaythe numbers of positive andnegative opinions.Providing anaspect-based summary for each opinion search will be evenbetter. However, it is anextremely challenging problem because aspectextraction, aspect categorization, and asso ciating entities to its aspects are allvery challenging problems. Without effective solutions for them, suchasummary will not be possible.

## 9.2

## Techniques

Current research in opinion retrieval typically treats the task as a two-stageprocess. In the first stage, documents are ranked by topical relevance only.In the second stage, candidate relevant documents are re-ranked by theiropinion scores. The opinion scores canbe acquired by either a machinelearning based sentiment classifier, such as SVM, or a lexicon-basedsentiment classifier using a sentiment lexicon anda combination ofsentiment word scores and query term–sentiment word proximityscores.More advanced research models topic relevance and opinion at the sametime, and produces rankings based on their integrated score.To give a flavor of opinion search, we present an example system (Zhangand Yu, 2007), which was the winner of the blog track in the 2007 TREC

Sentiment Analysis and Opinion Mining

119


---

<!-- Página 120 -->

Sentiment Analysis and Opinion Mining

evaluation ([http://trec.nist.gov/)](http://trec.nist.gov/)). The task was exactly opinion search (orretrieval). This system has two components. The first componentis forretrieving relevant documents for each query. The second component is forclassifying the retrieved documents as being opinionated or not-opinionated.The opinionated documents are further classified into positive, negative, ormixed (containing both positive and negative opinions).**Retrieval component : This componentperforms the traditional information**retrieval (IR) task. It considers both keywords and concepts. Concepts arenamed entities (e.g., names of people or organizations) or various types ofphrases fromdictionaries and other sources (e.g., Wikipedia entries). Thestrategy for processing a user query is as follows (Zhang et al., 2008; Zhangand Yu, 2007): It first recognizes and disambiguates the concepts within theuser query. It then broadens the search query with its synonyms. After that,it recognizes concepts in the retrieved documents and also performs pseudo-feedback toautomatically extract relevant words from the top-rankeddocuments to expand the query. Finally, it computes a similarity (orrelevance score) of each document w ith the expanded query using bothconcepts and keywords.**Opinion classification component : Thiscomponent performs two tasks: (1)**120the two categories, opinionated andnot-opinionated, and (2) classifyi ng each opinionated document asexpressing a positive, negative, or mixed opinion. For both tasks, the systemuses supervised learning. For the first task, it obtains a large amount ofopinionated (subjective) trainingdata from review sites such as rateitall.comand epinions.com. The data are also collected from different domainsinvolving consumer goodsand services as well as government policies andpolitical viewpoints. The not-opinionated training data are obtained fromsites that give objective information such as Wikipedia. From these trainingdata, a SVM classifieris constructed.This classifier is then applied to each retrieved document as follows. Thedocument is first partitioned into sentences. The SVM classifier thenclassifies each sentence as opinionated or not-opinionated. If a sentence isclassified to be opinionated, its strength, as determined bySVM, is alsonoted. A document is regarded opinionate d if there is at least one sentencethat is classified as opinionated. To ensure that the opinion of the sentence isdirected at the query topic, the systemrequires that enough queryconcepts/words are found in its vicinity. The totality of the opinionatedsentences and their strengths ina document together with thedocument’ssimilarity with the query is used to rank the document.


---

<!-- Página 121 -->

To determine whether an opinionated document expresses a positive,negative or mixed opinion, a second classifier is constructed. The trainingdata are reviews from review sites containing review ratings (e.g.,rateitall.com). A low rating indicates a negative opinion while a high ratingindicates a positive opinion. Using positive and negative reviews as trainingdata, a sentiment classifier is built to classify each document as expressing apositive, negative, or mixed opinion.There are also other approaches to opinion retrieval in TREC evaluations.The readers are encouraged to read the papers at the TREC Web site([http://trec.nist.gov/)](http://trec.nist.gov/)). For asummaryof TREC evaluations, please refer tothe overview paper of 2006 TREC bl og track (Ounis et al., 2006), theoverview paper of 2007 TREC blog track (Macdonald, Ounis and Soboroff,2007), and the overview paper of 2008 TREC blog track (Ounis, Macdonaldand Soboroff, 2008). Below, we discuss research published inother forums.In (Eguchi and Lavrenko, 2006), Eguchi and Lavrenko proposed a sentimentretrieval technique based on generative languagemodeling. In theirapproach, the user needs to provide a set of query terms representing aparticular topic of interest, and also sentiment polarity(orientation) interest,which is represented eitheras a set of seed sentiment words or a particularsentiment orientation (positive or negative). One main advance of their workis that they combined sentiment relevance models and topic relevancemodels withmodel parameters estimated from the trainingdata, consideringthe topic dependence of the sentimen t. They showed that the explicitmodeling of dependency between topic and sentiment produced betterretrieval results than treating them independently. A similar approach wasalso proposed by Huang and Croft (2009), which scored the relevance of adocument using a topic reliance model and an opinion relevance model.Both these works took a linear combination of topic relevance and sentimentrelevance for final ranking. In (Zhang and Ye, 2008), the authors used theproduct of the two relevance scores. The relevance formulation is also basedon language modeling.In (Na et al., 2009), a lexicon-based approach was proposed for opinionretrieval. They also attempted to deal with the domain dependent lexiconconstruction issue. A relevant feedback style learning for generating query-specific sentiment lexicon was proposed, which made use of a set of top-ranked documents in response to a query.Liu, Li and Liu (2009) explored various lexical and sentiment features anddifferent learningalgorithms for identifying opinionated blogs. They alsopresented results for the strategy that combines both the opinion analysis andthe retrieval components for retrieving relevant and opinionated blogs.

Sentiment Analysis and Opinion Mining

121


---

<!-- Página 122 -->

Sentiment Analysis and Opinion Mining

Li et al. (2010) took a different approach. Their algorithm first finds topicand sentiment word pairs from each sent ence of a document, and then buildsa bipartite graph to link such pairs with the documents that contain the pairs.The graph based ranking algorithmHITS (Kleinberg, 1999) was applied torank the documents, where documents we re considered as authorities andpairs were considered as hubs. Each link connecting a pair and a documentis weighted based onthe contribution of the pair to the document.In (Pang and Lee, 2008), a simple meth od was proposed for review search. Itonly re-ranksthe top k 122

unsupervised and does notuse anypre-existing lexicon.

## 9.3 Summary

It will be really useful if a Web search engine such as Google or MicrosoftBing can provide a general opinion sear ch service. Although bothGoogleand Microsoft Bing already provide opinion summarization services forreviews of some products, their coverage is still very limited. For those notcovered entities and topics, it is not easy to find opinions about thembecause their opinions are scattered all over the Internet. There are also somelarge and well known review hosting sites such as Amazon.com andYelp.com. However, they do not cover all entities and topics either. Forthose not covered entities or topics, finding opinions about them remains tobe a formidable task because of the proliferation of diverse sites and thedifficultyof identifying relevant opinions. A lot of research is still neededbefore a breakthrough can be achieved.

the search engine has alre ady found good results andonly re-ranking is needed to put reviews at the top. The method is

measure defined on the rarity of te rms appeared in the initial searchresults .assumption was that

*idiosyncrasy*


---

<!-- Página 123 -->

### CHAPTER 10

## Opinion Spam Detection

Opinions from social media are increasingly used by individuals andorganizations for making purchase decisions and makingchoices at electionsand for marketing and product design. Positive opinions often mean profitsand fames for businesses and individuals, which, unfortunately, give strongincentives for people to game the system by post

Sentiment Analysis and Opinion Mining

123

*reviews to promote or to discredit some target products, services,*organizations, individuals, and even ideas without disclosing their trueintentions, or the person or organization that they are secretly workingfor. Such individuals are called opinion spammers and their activities arecalled opinion spamming (Jindal and Liu, 2008; Jindal and Liu, 2007). ingor

Opinion spamming about social and political issues can even be frighteningas they can warp opinions and mobilize masses into positions counter tolegal or ethical mores. It is safe to say that as opinions in social media areincreasingly used in practice, opinion spamming will becomemore and morerampant and also sophisticated, which presents a major challenge for theirdetection. However, they must be detected in order toensure that the socialmedia continues to be a trusted source of public opinions, rather than beingfull of fake opinions, lies, and deceptions.Spam detection in general has been studied in many fields. Web spam andemail spam are the two most widely studied types of spam. Opinion spam is,however, very different. There are two main types of Web spam, i.e., link*spam and content spam (Castillo and Davison, 2010; Liu, 2006 and 2011).*Link spam is spam on hyperlinks, whichhardlyexist in reviews. Althoughadvertising links are common in other forms of social media, they arerelatively easy to detect. Content spam adds popular (but irrelevant) wordsin target Web pages inorder to fool search engines to make them relevant tomany search queries, but this hardly occurs in opinion postings. Email spamrefers to unsolicited advertisements, whic h are also rare in online opinions.**Challenge : The key challenge of opinion spam detection is that unlike other**forms of spam, it is very hard, if not impossible, to recognize fakeopinions by manually reading them, which makes it difficult to findopinionspamdatato help design and evaluate detection algorithms. Forother forms of spam, one can re cognize them fairly easily.In fact, in the extreme case, it is logi cally impossible to recognize spam bysimply reading it. For example, one can write a truthful review for a good


---

<!-- Página 124 -->

Sentiment Analysis and Opinion Mining

restaurant and post it as a fake review for a bad restaurant in order topromote it. There is no way to detect this fake review without consideringinformation beyond the review text its elf simply because the same reviewcannot be both truthful and fake at the same time.This chapter uses consumer reviews as an example to study the problem.Little research has beendone in the context of other forms of socialmedia.

124

## 10.1

Three types of spam reviews were identified in (Jindal and Liu, 2008):**Type 1 (fake reviews) : These are untruthful revi ews that are written not**based on the reviewers’ genuine experiences of using the products orservices, but are written with hiddenmotives. They often containundeserving positive opinions about some target entities (products orservices) in order to promote the entities and/or unjust or false negativeopinions about some other entities in order to damage their reputations.**Type 2 (reviews about brands only) : These reviews do not comment on the**specific products or services that th ey are supposed to review, but onlycomment on the brands or the manufact urers of the products. Althoughthey may be genuine, they are considered as spam as they are not targetedat the specific products and are ofte n biased. For example, a review for aspecific HP printer says “ I hate HP. I never buy any of their products”.**Type 3 (non-reviews) : These are not reviews. There are two main sub-**types: (1) advertisements and (2) other irrelevant texts containing noopinions (e.g., questions, answers, and random texts). Strictly speaking,they are not opinion spam as theydo not give user opinions.It has been shown in (Jindal and Liu, 2008) that types 2 and 3 spam reviewsare rare and relatively easy to detect us ing supervised learning. Even if theyare not detected, it is not a major problem because human readers can easilyspot them during reading. This chapter thus focuses on type 1, fake reviews.Fake reviews can be seen as a special form of deception (Hancock et al.,2007; Mihalcea and Strapparava, 2009; Newman et al., 2003; Pennebaker etal., 2007; Vrij, 2008; Zhou, Shi and Zhang, 2008). However, traditionaldeceptions usually refer to lies about some facts or a person’s true feeling.Researchers have identified many deception signals in text. For example,studies have shown that when people lie they tend todetach themselves andlike to use words such as you

*she ,*, rather than*I*, , etc.Liars also usewords related to certaintymore frequently to hide “fake” or toemphasize “truth”. Fake reviews are different from lies in many aspects.


---

<!-- Página 125 -->

Average quality product*4****3*** Bad qualityproduct***5*****6**  First, fake reviewers actually like to use

### 10.1.1 Harmful Fake Reviews

Not all fake reviews are equally harmful. Table 10.1 gives a conceptual viewof different kinds of fake reviews. Here we assumewe know the true qualityof a product. The objective of fake reviews in regions 1, 3 and 5 is topromote the product. Although opinions expressed in region 1 maybe true,the reviewers do not disclose their conflict of interests or hiddenmotives.The goal of fake reviews in regions 2, 4, and 6 istodamage the reputation ofthe product. Although opinions in the reviews of region 6 may be true, thereviewers havemalicious intensions. Clearly, fake reviews in regions 1 and6 are not very damaging, but fake reviews in regions 2, 3, 4, and 5 are veryharmful. Thus, fake review detection algorithms should focus on identifyingreviews in these regions. Some of the existing detection algorithms arealready using this idea by employing different types of rating deviationfeatures. Note that the good, bad, and average qualitymay be defined basedon the average ratingof the reviews given tothe product. However, this canbe invalid if there are many spamme rs or there are too few reviews.

**Table 10.1. Fake reviews vs. product quality**Positive fake reviewGood quality product***2***

### 10.1.2 Individual and Group Spamming

Fake reviews may be written bymanytypes of people, e.g., friends andfamily, company employees, competitors, businesses that provide fakereview writing services, and even genuine customers (some businesses givediscounts and even full refunds to some of their customers on the conditionthat the customers write positive reviews for them). In other forms of social

Sentiment Analysis and Opinion Mining

125

*I*, , etc.,to give readersthe impression that their reviews express their true experiences . Second, fakereviews are not necessarily the tradit ional lies. For example, one wrote abook and pretended to be a reader and wrote a review to promote the book.The review might be the true feeling of the author. Furthermore, many fakereviewers might have never used the reviewed products/services, but simplytried togive positive or negative opinions about something that theydo notknow. They are not lying about any facts they know or their true feelings.


---

<!-- Página 126 -->

Sentiment Analysis and Opinion Mining

media, public or private agencies and politicalorganizations may employpeople to post messages to secretly in fluence social media conversations andto spread lies and disinformation.In general, a spammermay work individually, or knowingly or unknowinglywork as a member of a group (these ac tivitiesare often highlysecretive).*Individual spammers : In this case, a spammer does not work with anyone.*He/she just writes fake reviews him/herself using a single user-id, e.g., theauthor of a book.*Group spammers : Thereare two main sub-cases (Mukherjee, Liu and*Glance, 2012; Mukherjeeet al., 2011).entity and/or to damage the reputation of another. The individualspammers in the group mayor may not know each other.ids. These multiple user-ids behave just like a group in collusion. Thiscase is often called sock puppetting .Group spamming is highlydamaging because due to the sheer number ofmembers in a group, it can take total control of the sentiment on a productand completelymislead potential customers, especially at the beginning of126mmers can also be seen as manyindividual spammers, group spamming has some special characteristicswhich can give them away as we will see in Section 10.4.We should also note that a spammer maywork individually sometimes andas a member of a group some other times. A spammer may also be a genuinereviewer sometimes because he/she also purchases products as a consumerand may write reviews aboutthem based onhis/her true experiences. Allthese complicated situationsmake opinion spamming very difficult todetect.

### 10.1.3 Types of Data, Features and Detection

Three main types of data have beenused for review spam detection:*Review content : The actual text content of each review. From the content,*we can extract linguistic features such as word and POS n-grams andother syntactic and semantic clues for deceptions and lies. However,linguistic features may not be enough because one can fairly easily craft afake review that is just like a genuine one. For example, one can write afake positive review for a bad restaurant based on his true experience in agood restaurant.*Meta-data about the review : The data such as the star rating given to each*


---

<!-- Página 127 -->

review,time taken towrite the review, the host IP address and MAC address ofthe reviewer’s computer, the geo-location of the reviewer, and thesequence of clicks at the review site . From such data, we can mine manytypes of abnormal behavioral patterns of reviewers and their reviews.For example, from review ratings, we may find that a reviewer wroteonly positive reviews for a brand and only negative reviews for acompeting brand. Along a similar line, if multiple user-ids from the samecomputer posted a number of positive reviews about a product, thesereviews are suspicious. Also, if the positive reviews for a hotel are allfrom the nearby area of the hotel, th ey are clearly not trustworthy.*Product information : Information about the entity being reviewed, e.g., the*product description and sales volume/rank. For example, a product is notselling well but has many positive reviews, which is hard to believe.These types of data have been used to produce many spamfeatures. One canalso classify the data into public data and site private data. By public data,wemean the data displayed on the review pages of the hosting site, e.g., thereview content, the reviewer’s user-id and the time when the review wasposted. By private data, we mean the data that the site collects but is notdisplayed ontheir review pages for public viewing, e.g., the IP address andMAC address from the reviewer’s com puter, and the cookie information.**Opinion Spam Detection : The ultimate goal of opinion spam detection in**the review context is to identify every fake review, fake reviewer, and fakereviewer group. The three concepts are clearly related as fake reviews arewritten by fake reviewers and fake reviewers can form fake reviewergroups. The detection of one type can help the detection of others.However, each of them also has its own special characteristics, which canbe exploited for detection.In the next two sections, we focus on detecting individual fake reviews andreviewers, and in section 10.4 we discuss the detection of spammer groups.

## 10.2 Supervised Spam Detection

In general, opinion spamdetection can be formulated as a classificationproblemwith two classes, fake non-fake . Supervised learning isnaturally applicable. However, as we described above,

Sentiment Analysis and Opinion Mining

, if not impossible, to recognize fakereviews reliably bymanually reading them because a spamme r can carefully craft a fake reviewthat is just like any innocent review (Jindal and Liu, 2008). Due to thisdifficulty, there is no reliable fake review and non-fake review data available

127

it is very harda key difficulty is that


---

<!-- Página 128 -->

Sentiment Analysis and Opinion Mining

to train a machine learning algorithm to recognize fake reviews. Despitethese difficulties, several detection algorithms have been proposed andevaluated invarious ways. This section discusses three supervised learningmethods. Thenext section describes some unsupervised methods.Due to the fact that there is no labeled training data for learning, Jindal andLiu (2008) exploited duplicate reviews. In their studyof 5.8 million reviewsand 2.14 million reviewers from amazon.com, a large number of duplicateand near-duplicate reviews were found, which indicated that review spamwas widespread. Since writing new reviews can be taxing, many spammersuse the same reviews or slightly revised reviews for different products.These duplicates and near-duplicates can be divided intofour categories:1.2.3.4.The first type of duplicates can be the results of reviewers mistakenlyclicking the review submit buttonmultiple times (which can be easilychecked based on the submission dates). However, the last three types ofduplicates are very likely to be fake. Thus the last three types of duplicates128were used as fake reviews and the rest of the reviews as non-fake reviews inthe training data for machine learning. Th ree sets of features were employed:*Review centric features : These are features about each review. Example*features include the actual words and n-grams of the review, the numberof times that brand names are mentioned, the percent of opinion words,the review length, and the number of helpful feedbacks. In many reviewsites (e.g., amazon.com), the readers ca n provide feedback to each reviewby answering a question like “ Do you findthis review helpful?”*Reviewer centric features : These are features about each reviewer. Example*features include the aver age rating given by the reviewer, themean andthe standard deviation in rating, the ratio of the number of reviews thatthis reviewer wrote whichwere the firstreviews of products to the totalnumber of reviews that he/she has written, and the ratio of the number ofcases in which he/she was the only reviewer.*Product centric features : These features are abou t each product. Example*features include the price of the pr oduct, the sales rank of the product(amazon.comassigns a sales rank to each product according to its salesvolume), the mean and the standarddeviation of review ratings of theproduct.Logistic regression was used for model building. Experimental resultsshowed sometentative but interesting results.


---

<!-- Página 129 -->

from the average rating of a product) tendto be heavilyspammed.Positive outlier reviews arenot badly spammed.This can be explained by the tendency of a seller promoting an unpopularproduct by writing a fake review.gives a rank to each reviewer based on its proprietary method. Analysisshowed that top-ranked reviewers generally wrote a large number ofreviews. People who wrote a large number of reviews are naturalsuspects. Some top reviewers wrote thousands or even tens of thousandsof reviews, which is unlikely for an ordinary consumer.feedbacks. This shows thatif the qualityof a review is defined based onhelpfulness feedbacks, people can be fooled by fake reviews becausespammers can easily craft a sophistic ated review that can getmanypositive feedbacks.indicates that spam activities seem to be limited to low selling products,which is intuitive as it is difficult todamage the reputation of a popularproduct, and an unpopular product needs some promotion.It shouldbe stressed again that these results are tentative because (1) it is notconfirmed that the three types of duplic ates are definitely fake reviews, and(2) many fake reviews are not duplicat es and they are considered as non-fake reviews in model building in (Jindal and Liu, 2008).In (Li et al., 2011), another supervised learning approach was attempted toidentify fake reviews. Intheir case, a manually labeled fake review corpuswas built from Epinions reviews. In Epinions, after a review is posted, userscan evaluate the review by giving it a helpfulness score. They can also writecomments about the reviews. The authors manually labeled a set of fake ornon-fake reviews by reading the reviews and the comments. For learning,several types of features were proposed , which are similar to those in (Jindaland Liu, 2008) with some additions, e.g., subjective and objectivity features,positive and negative features, reviewer’s profile, authority score computedusing PageRank (Page et al., 1999), etc. For learning, they used naïveBayesian classification which gavepr omising results. The authors alsoexperimented with a semi-supervised learning method exploiting the ideathat a spammer tends to write many fake reviews.In (Ott et al., 2011), supervised learning was also employed. In this case, theauthors used Amazon Mechanical Turk to crowdsource fake hotel reviews of

Sentiment Analysis and Opinion Mining

129


---

<!-- Página 130 -->

Sentiment Analysis and Opinion Mining

20 hotels. Several provisions were made to ensure the quality of the fakereviews. For example, they only allowed each Turker to make a singlesubmission,

130

## 10.3 Unsupervised Spam Detection

Due to the difficulty of manually labeling of trainingdata, using supervisedlearning alone for fake review detectio n is difficult. In this section, wediscuss two unsupervised approaches. Techniques similar to these arealready in use in many review hosting sites.

### 10.3.1 Spam Detection based on Atypical Behaviors

This sub-section describes some techni ques that try to discover atypicalbehaviors of reviewers for spammer detection. For example, if a reviewerwrote all negative reviews for a brand but other reviewers were all positiveabout the brand, and wrote all positive reviews for a competing brand, thenthis reviewer is naturally suspicious.The first technique is from (Lim et al., 2010), which identified severalunusual reviewer behavior models based on different review patterns thatsuggest spamming. Each model assigns a numeric spamming behavior score

Turkers must be in the United States, etc. The Turkers werealso given the scenario that they wo rked in the hotels and their bossesasked them to write fake reviews to promote the hotels.

were obtained from the TripAdvisor Web site. Theauthors triedseveralclassification approaches which have been used in related tasks such asgenreidentification, psycholinguistic deception detection, andtextclassification. All these tasks have some existing features proposed byresearchers. Their experiments showed that text classification performed thebest using only unigram and bigrams based on the 50/50 fake and non-fakeclass distribution. Traditional features for deceptions (Hancock et al., 2007;Mihalcea and Strapparava, 2009; Newman et al., 2003; Pennebaker et al.,2007; Vrij, 2008; Zhou, Shi and Zhang, 2008) did not do well. However,like the previous studies, the evaluation data used here is also not perfect.The fake reviews fromAmazon Mechanical Turk may not be true “fakereviews” as the Turkers do not know the hotels being reviewedalthoughthey were asked to pretend that they worked for thehotels. Furthermore,using 50/50 fake and non-fake data for testing may not reflect the truedistribution of the real-life situation. The class distribution can have asignificant impact on the precision of thedetected fake reviews.

Truthful reviews


---

<!-- Página 131 -->

to a reviewer by measuring the exte nt to which the reviewer practicesspamming behavior of the type. All the scores are thencombined toproducethe final spam score. Thus, this method focuses on finding spammers or fakereviewers rather than fake reviews. The spamming behavior models are:(a): To game a review system, it is hypothesized that aspammer will directmost of his efforts on promoting or victimizing afew target products. He is expected tomonitor the products closely andmitigate the ratings by writing fake reviews when time is appropriate.(b): This spam behavior model defines the pattern ofspammers manipulating ratings of a set of products sharing someattribute(s) within a short span of time. For example, a spammer maytarget several products of aratings saves the spammers’ time as they do not need to log onto thereview systemmany times. To achievemaximum impact, the ratingsgiven to these target groups of products are either very high or very low.(c): A genuine reviewer is expected togiveratings similar to other raters of the sameproduct. As spammers attemptto promote or demote some products, their ratings typically deviate agreat deal from those of other reviewers.(d): Early deviation captures the behavior of aspammer contributing a fake review soon after product launch. Suchreviews are likely to attract attention from other reviewers, allowingspammers to affect the view s of subsequent reviewers.The second technique also focused on finding fake reviewers or spammers(Jindal, Liu and Lim, 2010). Here the problem was formulated as a datamining taskof discovering unexpect ed class association rules. Unlikeconventionalspam detection approaches such as the above supervised andunsupervised methods, which first manually identify some heuristic spamfeatures and then use themfor spamde tection. This technique is generic andcan be applied to solve a class of prob lems due to its domain independence.Class association rules are a special type of association rules (Liu, Hsu andMa, 1998) with a fixed class attribute. The data for mining class associationrules (CARs) consists of a set of data records, which are described by a setof normal attributes A A

Sentiment Analysis and Opinion Mining

131

,1}, and a class attribute C c*n*

) (called support ).*i*For the spammer detection application, the data for CAR mining is producedas follows: Each review forms a data record with a set of attributes, e.g.,

*,*} of1 m*m X c**class labels . A CAR rule is of the form:* ,where X*A c**i* is a class labelin*i c* |*confidence ) and the joint probability Pr( X**i*


---

<!-- Página 132 -->

Sentiment Analysis and Opinion Mining

*reviewer-id ,*,, and a class. The class represents thesentiment of the reviewer on the product, positive ,, or basedon the review rating. In most review sites (e.g., amazon.com), each reviewhas a rating between 1 (lowest) and 5 (highest) assigned by its reviewer. Therating of 4 or 5 is assigned positive, 3 neutral, and 1 or 2 negative. Adiscovered CAR rule could be that a reviewer gives all positive ratings to aparticular brand of products. The method in (Jindal, Liu and Lim, 2010)finds four types of unexpected rules based on four unexpectednessdefinitions. The unexpected rules represent atypical behaviors of reviewers.Below, an example behavior is given for each type of unexpectednessdefinition. The unexpectedness definiti ons are quite involved and can befound in (Jindal, Liu and Lim, 2010).: Using this measure, one can find reviewerswho give all high ratings to products of a brand, but most other reviewersare generallynegative about the brand.: Using this measure, one can find reviewerswho write multiple reviews for a single product, while other reviewersonly write one review.: Using this measure, one can132only one reviewer although there are a large number of reviewers whohave reviewed the products of the brand.: Using this measure, one can find reviewerswho write only positive reviews to one brand and only negative reviewsto another brand.The advantage of this approach is th at all the unexpectedness measures aredefined on CARs rules, and are thus domain independent. The technique canthus be used in other domains to find unexpected patterns. The weakness isthat some atypical behaviors cannot be detected, e.g., time-related behaviors,because class association rules do not consider time.It is importanttonotethat the behaviors studied in published papers are allbased on public data displayed on review pages of their respective reviewhosting sites. Asmentioned earlier, review hosting sites also collectmanyother pieces of data about each reviewer and his/her activities at the sites.These data are not visible to the general public, but can be very useful,perhaps evenmore useful than the public data, for spam detection. Forexample, if multiple user-ids from th e same IP address posted a number ofpositive reviews about a product, then these user-ids are suspicious. If thepositive reviews for a hotel are all from th e nearby area of the hotel, they arealso doubtful. Some review hosting sitesare alreadyusing these and other


---

<!-- Página 133 -->

pieces of their internaldata to de tect fake reviewers and reviews.Finally, Wu et al. (2010) also proposed an unsupervised method todetectfake reviews based on a distortion criterion (not on reviewers’ behaviors asthe above methods). The idea is that fake reviews will distort the overallpopularity ranking for a collection of entities. That is, deleting aset ofreviews chosen at random should not overly disrupt the ranked list ofentities, while deleting fake reviews should significantly alter or distort theranking of entities to reveal the “true" ranking. This distortion can bemeasured bycomparing popularity rankings before and after deletion usingrank correlation.

### 10.3.2 Spam Detection Using Review Graph

In (Wang et al., 2011), a graph-based method was proposedfor detectingspam in store or merchant reviews. Such reviews describe purchaseexperiences and evaluations of stores. This study was based on a snapshot ofall reviews from resellerratings.com, which were crawled on Oct. 6th, 2010.After removing stores withno reviews, there were 343603 reviewers whowrote 408470 reviews about14561 stores.Although one can borrow some ideas from product review spammerdetection, their clues areinsufficient for the store review context. Forexample, it is suspicious for a person to post multiple reviews to the sameproduct, but it can be normal for a person topost more than one reviewtothe same store due tomultiple purchasing experiences. Also, it can benormal to have near-duplicate reviews from one reviewer for multiple storesbecause unlike different products, different stores basically provide the sametype of services. Therefore, featur es or clues proposedin existingapproaches to detecting fake product reviews and reviewers are not allappropriate for detecting spammers of store reviews. Thus, there is a need tolook for a more sophisticated and complementary framework.This paper used a heterogeneous review graph with three types of nodes, i.e.,reviewers, reviews and stores, to capture their relationships and to modelspamming clues. A reviewer node has a link to each review that he/shewrote. A review node has an edge to a store node if the review is about thatstore. A store is connected to a reviewer via this reviewer’s review about thestore. Each node is also attached with a set of features. For example, a storenode has features about its average rating, its number of reviews, etc. Basedon the review graph, three concepts are defined and computed, i.e. the*trustiness of reviewers, the honesty of reviews, and the reliability of stores.*A reviewer is more trustworthy if he /she has written more honesty reviews;

Sentiment Analysis and Opinion Mining

133


---

<!-- Página 134 -->

Sentiment Analysis and Opinion Mining

a store is more reliable if it has more positive reviews from trustworthyreviewers; and a review ismore honest if it is supported by many otherhonest reviews. Furthermore, if the honesty of a review goes down, it affectsthe reviewer’s trustiness, which has animpact on thestore he/she reviewed.These intertwined relations are revealed in the review graph and definedmathematically. An iterative computationmethod was proposed to computethe three values, which are then used to rank reviewers, stores and reviews.Those top ranked reviewers, stores and reviews are likely to be involved inreview spamming. The evaluation was done using human judges bycomparing with scores of stores from Better Business Bureaus (BBB), whichisthat gathers reports on businessreliabilityand alerts the public tobusiness or consumer scams. 134

## 10.4 Group Spam Detection

An initial group spam detection algorithm was proposed in (Mukherjee etal., 2011), which was improved in (M ukherjee, Liu and Glance, 2012). Thealgorithmfinds groups of spammers who might have worked in collusion inpromoting or demoting sometarget entities. It works in two steps:1.: First, it pre-processes the review data toproduce a set of transactions. Each transaction represents a uniqueproduct and consists of all reviewers (their ids) who have reviewedthatproduct. Using all the transactions, it performs frequent pattern mining tofind a set of frequent patterns. Each pattern is basicallya group ofreviewers who have all reviewed a set of products. Such a group isregarded as a candidate spam group. The reason for using frequentpattern mining is as follows: If a group of reviewers who only workedtogether once to promote or to demote a single product, it can be hard todetect based on their collective behavior. However, these fake reviewers(especially those who get paid to write) cannot be justwriting one reviewfor a single product because they would not make enough money thatway. Instead, they work onmany products, i.e., write many reviewsabout manyproducts, which also gives them away. Frequent patternmining can find them working together onmultipleproducts.2.**of group spam indicators : The groups**discovered in step 1 may not all be truespammer groups. Many of thereviewers are grouped together in patternmining simply due to chance.Then, this step first uses a set of indicators to catch different types ofunusual group and individual member behaviors. These indicatorsinclude writing reviews together in a short time window, writing reviews


---

<!-- Página 135 -->

right after the product launch, group reviewcontentsimilarity, grouprating deviation, etc (Mukherjee, Liu and Glance, 2012). A relationalmodel, called GSRank (Group Spam Rank), was then proposed to exploitthe relationships of groups, individual group members, and products thatthey reviewed to rank candidate groups based on their likelihoods forbeing spammer groups. An iterative algorithm was then used to solve theproblem. A set of spammer groups was also manually labeled and used toevaluate the proposedmodel, which showed promising results. Oneweakness of this method is that due to the frequency threshold used inpatternmining, if a group has not worked together many times (three ormore times), it will not be detected by thismethod.This method is unsupervised as it does not use anymanually labeled data fortraining. Clearly, with the labeled data supervised learning can be applied aswell. Indeed, (Mukherjee, Liu and Glance, 2012) described experiments withseveral state-of-the-art supervised classification, regression and learning torank algorithms but they were shown tobe less effective.

## 10.5 Summary

As social media is increasinglyused for critical decision making byorganizations and individuals, opinion spamming is also becoming moreand more widespread. For many businesses, posting fake opinionsthemselves or employing others to do it for them has become a cheapway of marketing and brand promotion.

Sentiment Analysis and Opinion Mining

135

an arms race between detection algorithms andspammers. However, I am optimistic that more sophisticated detectionalgorithmswill be designed to make it very difficult for spammers topost fake opinions. Such algorithms ar e likely to be holistic approachesthat integrate all possible features or clues in the detection process.

Althoughcurrent researchon opinion spam detection is still in its earlystage, several effective algorithms have already been proposed and used inpractice. Spammers, however, are also getting more sophisticated andcareful in writing and posting fake opinions to avoid detection. In fact, wehave already seen

Finally, we should note that opinion spamming occurs not only in reviews,but also in other forms of social media such as blogs, forum discussions,commentaries, and Twitter postings. However, so far little research has beendone in these contexts.


---

<!-- Página 136 -->

Sentiment Analysis and Opinion Mining

### CHAPTER 11

136

## Quality of Reviews

In this chapter, we discuss the qualit y of reviews. The topic is related toopinion spam detection, but is also different because low quality reviewsmay not be spam or fake reviews, and fake reviews may not be perceived aslow quality reviews by read ers because as we discussed in the last chapter,by reading reviews it is very hard to spot fake reviews. For this reason, fakereviews may also be seen as helpful or high quality reviews if the imposterswrite their reviews early and craft them well.The objective of this task is to determine the quality, helpfulness, usefulness,or utility of each review (Ghose and Ipeirotis, 2007; Kim et al., 2006; Liu etal., 2007; Zhang and Varadarajan, 2006). This is a meaningful task becauseit is desirable to rank reviews based on quality or helpfulness when showingreviews to the user, with the most helpfu l reviews first. In fact, many reviewaggregation or hosting sites have been practicing this for years. They obtainthe helpfulness or quality score of each review by asking readers to providehelpfulness feedbacks to each review. For example, in amazon.com, thereader can indicate whether he/she finds a reviewhelpful by responding tothe question “ Was the review helpful to you? ” just below each review. Thefeedback results from all those responded are then aggregated and displayedright before each review, e.g., “ 15 of 16 people found the following review*helpful .” Although most review hosting sites alreadyprovide the service,*automatically determining the quality of each review is still useful because agood number of user feedbacks may take a long time to accumulate. That iswhymany reviews have few or no feedbacks. This is especially true for newreviews.

## 11.1

Determining the quality of reviews is usually formulated as a regressionproblem. The learned model assigns a quality score to each review, whichcan be used in review ranking or re view recommendation. In this area ofresearch, the ground truth data used fo r both training and testing are usuallythe user-helpfulness feedback given to each review, which as we discussedabove is provided for each review at many reviewhosting sites. So, unlikefake review detection, thetraining andtesting data here is not anissue.


---

<!-- Página 137 -->

Researchers have used many types of features for model building.In (Kim et al., 2006), SVM regression was used to solve the problem. Thefeaturesets included,*Structure features : review length, number of sentences, percentages of*question sentences and exclamations, andthe number of HTML bold tags<b> and line breaks <br>.*Lexical features : unigrams and bigrams with tf-idf weights.**Syntactic features :*that are of open-class (i.e.,nouns,nouns, percentage of tokensverbs conjugated in the first person, and percentage of tokens that areadjectives or adverbs.*Semantic features : product aspects, and sentiment words.**Meta-data features :*In (Zhang and Varadarajan, 2006), the authors also treated the problem as aregressions problem. They used similar features, e.g., review length, reviewrating, counts of some specific POS tags, sentiment words, tf-idf weightingscores, wh-words, product aspect mentions, comparison with productspecifications, comparison with editorial reviews, etc.Unlike the above approaches, (Liu et al., 2008) considered three mainfactors, i.e., reviewers’ expertise, the timeliness of reviews, and reviewstyles basedon POS tags. A nonlinear regression model was proposed tointegrate the factors. This work focused on movie reviews.In (Ghose and Ipeirotis, 2007; Ghose and Ipeirotis, 2010), three additionalsets of features were used, namely, reviewer profile features which areavailable from the review site, reviewer history features which capture thehelpfulness of his/her reviews in the past, and a set of readability features,i.e., spelling errors and readability indices from the readability research. Forlearning, theauthors tried both regression and binaryclassification.Lu et al. (2010) looked at the problem from an additional angle. Theyinvestigated how the social context of reviewers can help enhance theaccuracy of a text-based review quality predictor. They argued that thesocial context can reveal a great deal of information about the quality ofreviewers, which in turn affects the qu ality of their reviews. Specifically,their approach was based on the following hypotheses:*Author consistency hypothesis :*quality.*Trust consistency hypothesis : A link from a reviewer r*

Sentiment Analysis and Opinion Mining

137

to a reviewer r1 trusts reviewer r1 explicit or implicit statement of trust. Reviewer ris an2 only2


---

<!-- Página 138 -->

Sentiment Analysis and Opinion Mining

if the qualityof reviewer r

138

## 11.2

In (O'Mahony and Smyth, 2009), a clas sification approach was proposed toclassify helpful and non-helpful reviews. Many features were used:*Reputation features : the mean (R1) andstandard deviation (R2) of review*helpfulness over all reviews authored by the reviewer, the percentage ofreviews authored by the reviewer which have received a minimumof Tfeedbacks (R3), etc.*Content features : review length (C1), the rati o of uppercase to lowercase*characters in the review text(C3), etc.*Social features :*by the reviewer (SL1), themean (SL2) and standard deviation (SL3) of the number of reviewsauthoredby all reviewers, etc.*Sentiment features : the rating score of the review (ST1), and the mean (ST5)*and standarddeviation (ST6) of the sc ores assignedby the reviewer overall reviews authored by the reviewer, etc.In (Liu et al., 2007), the problem wa s also formulated as a two-classclassification problem. However, theyargued that using the helpfulnessvotes as the ground truth may not be a ppropriate because of three biases: (1)vote imbalance (a very large percentageof votes are helpful votes); (2) earlybird bias (early reviews tend to get more votes); (3)

when some reviews get many votes they are rankedhigh at the review sites

, then their quality should be similar.*Link consistency hypothesis : If two people are connected in the social*3network ( r

trusts r1, or*r*2

is at least as high as that of reviewer r2

and rare trusted by the same thirdreviewer*r*12

*r*, or both), then their review qualityshould be similar.21These hypotheses were enforced as re gularizing constraints and added intothe text-based linear regression model to solve the review quality predictionproblem. For experiments, the authors used the data from Ciao(www.ciao.co.uk), which is a community review Website. In Ciao, peoplenot only write reviews for products and services, but also rate the reviewswritten by others. Furthermore, people can add members to their network oftrusted members or “Circle of Trust”, if theyfind these members’ reviewsconsistentlyinteresting and helpful. Clearly, this technique will not beapplicable to Web sites which do not ha ve a trust social network inplace.

(winner circle bias

*Co-citation consistency hypothesis : People are consistent in how they trust*other people. So if two reviewers r.1


---

<!-- Página 139 -->

which help them get even more votes). Those lowly ranked reviews get fewvotes, but theymay not be of low quality. The authors then divided reviewsinto 4 categories, “best review”, “good review”, “fair review”, and “badreview,” based on whether reviews

Tsur and Rappoport (2009) studied the helpfulness of book reviews using anunsupervised approach which is quite different from the above supervisedmethods. Themethod works in three steps. Given a collection of reviews, itfirst identifies a set of important terms in the reviews. These terms togetherform a vector representing a virtual optimal or core review. Then, eachactual review is mapped or converted to this vector representation based onoccurrences of the discovered important terms in the review. After that, eachreview is assigned a rank score based on the distance of the review to thevirtual review(both are represented as vectors).In (Moghaddam, Jamali and Ester, 2012), a new problem of personalizedreview quality prediction for recommendation of helpful reviews wasproposed. Allof the above methods assume that the helpfulness of areviewis the same for all users/readers, wh ich the authors argued is not true. Tosolve the new problem, they proposed several factorization models. Thesemodels are based on the assumption that the observed review ratings dependon some latent features of the reviews, reviewers, raters/users, and products.In essence, the paper treated the problem as a personalized recommendationproblem. The proposed technique to solve the problem is quite involved.Some background knowledge about this form of recommendation can befound in Chapter 12 of the book (Liu, 2006 and 2011).All the above approaches rank reviews based on the computed helpfulness orquality scores. However, Tsaparas, Ntoulas and Terzi (2011) argued thatthese approaches do not consider an important fact that the top fewhigh-quality reviews may be highly redundant and repeating the sameinformation. In their work, they proposed the problem of selecting a*comprehensive and yet a small set of high-quality reviews that cover many*different aspects of the reviewed entity and also different viewpoints of thereviews. They formulated the problem as a maximum coverage problem, andpresented an algorithm to solve the problem. An earlier work in (Lappas and

informativeness, subjectiveness, and

Sentiment Analysis and Opinion Mining

139 discuss many aspects of the productand provide convincing opinions. Manual labeling was carried out toproduce the gold-standard training and te sting data. In classification, theyused SVM toperform binary classificat ion. Only the “bad review” categorywas regarded as the low quality class and all the other three categories wereregarded as belonging to the high qua lity class. The features for learningwere

readability. Each of themcontained a set of individual features.


---

<!-- Página 140 -->

Sentiment Analysis and Opinion Mining

Gunopulos, 2010) also studied the problem of finding a small set of reviewsthat cover all

140

## 11.3 Summary

In summary, determining review helpfulness is an important research topic.It is especially useful for products and services that have a large of numberreviews. To help the reader get quality opinions quickly, review sites shouldprovide good review rankings. However, I would also like to add somecautionary notes. First, as we discussed in the chapter about opinion searchand retrieval, we argued that the revi ew ranking (rankings) must reflect thenatural distribution of positive and negative opinions. It is not a good idea torank all positive (or all negative) reviews at the top simply because theyhave high quality scores. The redundancyissue raised in (Tsaparas, Ntoulasand Terzi, 2011) is also a valid concern. In my opinion, both quality anddistribution (in terms of positive and negative viewpoints) are important.Second, readers tend to determine whether a review is helpful or not basedon whether the review expresses opinions on many aspects of the productand appear to be genuine. A spammer can satisfy this requirement bycarefully crafting a review that is just like a normal helpful review. So, usingthe number of helpfulness feedbacks to define review quality or as theground truth alone can be problematic. Furthermore, user feedbacks can bespammed too. Feedback spam is a s ub-problem of click fraud in searchadvertising, where a person or robot c licks on some online advertisements togive the impression of real customer clicks. Here, a robot or a humanspammer can click on the helpfulnes s feedback button to increase thehelpfulness of a review.


---

<!-- Página 141 -->

### CHAPTER 12

## Concluding Remarks

This book introduced the field of sentiment analysis and opinion mining andsurveyed the current stat e-of-the-art. Due to manychallenging researchproblems and a wide variety of practic al applications, the research in thefield has been very active in recent years. It has spread from computerscience to management science (Archak, Ghose and Ipeirotis, 2007; Chenand Xie, 2008; Das and Chen, 2007; Dellarocas, Zhang and Awad, 2007;Ghose, Ipeirotis and Sundararajan, 2007; Hu, Pavlou and Zhang, 2006; Park,Lee and Han, 2007) as opinions about pr oducts are closely related toprofits.The book first defined the sentiment analysis problem, which provided acommon framework to unify di fferent research directions in the field. It thendiscussed the widely studied topic of document-level sentimentclassification, which aims to determine whether an opinion document (e.g., areview) expresses a positive or negative sentiment. This was followed by thesentence-level subjectivity and sentiment classification, which determineswhether a sentence is opinionated, and if so, whether it carries a positive ornegative opinion. The book then described aspect-based sentiment analysiswhich explored the full power of the problem definition and showed thatsentiment analysis is a multi-faceted problem with many challenging sub-problems. The existing techniques for dealing with them were discussed.After that, the book discussed the problem of sentiment lexicon generation.Two dominant approaches were covered. This was followed by the chapteron opinion summarization, which is a special form of multi-documentsummarization. However, it is also very different from the traditional multi-document summarization because opinion summarization can be done in astructured manner, which facilitates both qualitative and quantitativeanalysis, and visualization of opinions. Chapter 8 discussedthe problemofanalyzing comparative and superlative sentences. Suchsentences representadifferent typeof evaluationfrom regular opinions which have been the focusof the current research. The topic of opinion search or retrieval wasintroduced in Chapter 9. Last but not least, we discussed opinion spamdetection inChapter 10 and assessing the quality of reviews in Chapter 11.Opinion spamming by writing fake reviews and posting bogus comments areincreasinglybecoming an important issue as more and more people arerelying on the opinions on the Web for decision making. To ensure thetrustworthiness of such opinions, co mbating opinion spamming is anurgent

Sentiment Analysis and Opinion Mining

141


---

<!-- Página 142 -->

Sentiment Analysis and Opinion Mining

and critical task.By reading this book thus far, it is not hard to see that sentiment analysis isvery challenging technically. Although the research community hasattempted so many sub-problems frommany different angles and a largenumber of research papers have also been published, none of the sub-problems has been solved satisfactorily. Our understanding and knowledgeabout the whole problem and its solution are still very limited. The mainreason is that this is a natural language processing task, and natural languageprocessing has no easy problems. Another reason may be due to our popularways of doing research. We probably relied too much on machine learning.Some of the most effectivemachine learning algorithms, e.g., support vectormachines, naïve Bayes and conditional randomfields, produce no humanunderstandable results such that although they may helpus achieveimproved accuracy, we know little about how and why apart from somesuperficial knowledge gained in the manual feature engineering process.That being said, we have indeed made significant progresses over the pastdecade. This is evident from the larg e number of start-up and establishedcompanies that offer sentiment analysis services. There is a real and hugeneed in the industry for such services because every business wants to know142competitors. The same can alsobe saidabout consumers because wheneverone wants tobuy something, one wants to know the opinions of existingusers. These practical needs and the technical challenges will keep the fieldvibrant and lively for years to come.Buildingonwhat has been doneso far, I believe that we just need to conductmore in-depth investigations and to build integrated systems that tryto dealwith all the sub-problems together because their interactions can help solveeach individual sub-problem. I am optimistic that thewhole problem will besolved satisfactorily in the near future for widespread applications.For applications, a completely automate d and accurate solution is nowherein sight. However, it is possible to devise effective semi-automatedsolutions. The key is to fully understand the whole range of issues andpitfalls, cleverlymanage them, and determine what portions can be doneautomatically and what portions need human assistance. In the continuumbetween the fully manual solution and the fully automated solution, as timegoes by we can push more and more towards automation. I do not see asilver bullet solution soon. A good bet would be to work hard on a largenumber of diverse application domains, understand each of them, and designa general solution gradually.


---

<!-- Página 143 -->

## Bibliography

1.*Sentiment analysis in**multiple languages: Feature selection for opinion classification in web**forums. ACM Transactions onInformation Systems (TOIS), 2008. 26*2.*Subjectivity and sentiment analysisof modern standard Arabic. in**Proceedings of the 49th Annual Meeting of the Association for**Computational Linguistics:shortpapers . 2011.*3.*Subjectivity word sense**disambiguation . in Proceedings of the 2009 Conference on Empirical**Methods in Natural Language Processing (EMNLP-2009). 2009.*4.*Affect in text and speech, 2008: ProQuest.*5.*Mining WordNet for fuzzy**sentiment: Sentiment tag extra ction from WordNet glosses. in**of Conference of the European Chapter of the Association for**Computational Linguistics (EACL-06) . 2006.*6.*When specialists andgeneralists**work together: Overcomingdomain dependence in sentiment tagging. in**Proceedings of the Annual Meeting of the Association for Computational**Linguistics (ACL-2008) . 2008.*7.*Latent Dirichlet Allocation with**topic-in-set knowledge . in*. 2009.8.*Incorporating**domain knowledge into topic modeling via Dirichlet forest priors. in**Proceedings ofICML . 2009.*9.*Show me the**money!: deriving the pricingpower ofproductfeatures by mining**consumer reviews . in**Knowledge Discovery and Data Mining (KDD-2007). 2007.*10.*Distilling**opinion indiscourse: A preliminary study . inProceedings of the**International Conference on Comput ational Linguistics (COLING-2008):**Companion volume: Posters and Demonstrations . 2008.*11.*Predicting the future with**social media. Arxiv preprint arXiv:1003.5699, 2010.*12.*Customizing sentiment classifiers to**new domains: a casestudy . in**Language Processing (RANLP-2005) . 2005.*13. Banea, Carmen, Rada Mihalcea, and Janyce Wiebe. Multilingual*subjectivity: are more languages better? inProceedings of the**International Conference on Computational Linguistics (COLING-2010).*2010.14.*Multilingual subjectivity analysis using machine translation. in**Proceedings of the Conference on Empirical Methods in Natural Language**Processing (EMNLP-2008) . 2008.*15.Goldstein. Identifying and Following Expert Investors inStock Microblogs.in*Language Processing (EMNLP-2011) . 2011.*

Sentiment Analysis and Opinion Mining

143


---

<!-- Página 144 -->

Sentiment Analysis and Opinion Mining

144

*Linguistics (ACL-2007) . 2007.*30.*Domain adaptation**with structural correspondence learning . in**on Empirical Methods in Natural Language Processing (EMNLP-2006).*2006.31.*Learning from labeled and unlabeled**data using graphmincuts . in**Machine Learning(ICML-2001) . 2001.*32.Reddy. Semi-supervised learningusing randomized mincuts. in

16.*Robust sentiment detection on twitter**frombiased and noisy data . in Proceedings ofthe International**Conference on ComputationalLinguistics (COLING-2010). 2010.*17.*International**sentiment analysis for news and blogs . in**AAAI Conference on Weblogs an d Social Media (ICWSM-2008). 2008.*18.*Lastbut definitely not least: on the**role of the last sentence in automatic polarity-classification. in**Proceedings of the ACL 2010 Conference Short Papers. 2010.*19.Vaithyanathan. An explorationof sentiment summarization. in*of AAAI Spring Symposium on Exploring Attitude and Affect in Text:**Theories and Applications . 2003.*20.Popescu. Towards Context-BasedSubjectivity Analysis. in*the 5thInternational Joint Conference on Natural Language Processing**(IJCNLP-2011) . 2011.*21.*Sentiment**classificationbased on supervised latent n-gramanalysis. in**the ACM conference on Information and knowledge management (CIKM-**2011) . 2011.*22.and Dan Jurafsky. Automaticextraction of opinion propositions andtheir*holders . in Proceedings of the AAAI Spring Symposium on Exploring**Attitude and Affect in Text . 2004.*23.*A hierarchical classifier applied to**multi-way sentiment detection . in**Conference onComputational Linguistics (Coling 2010). 2010.*24.*Combining**collective classification andlink prediction. in**on Mining Graphs and Complex Structures . 2007.*25.*Pattern recognitionand machine learning . Vol. 4. 2006:*springer New York.26.George A. Reis, and Jeff Reynar. Buildinga sentiment summarizer for*local service reviews . in**the Information Explosion Era . 2008.*27.*Supervised topic models . in**Proceedings ofNIPS . 2007.*28.Ng, and Michael I. Jordan. Latent dirichlet*allocation. The Journal of Machine Learning Research, 2003. 3*1022.29.ze, and Fernando Pereira. Biographies, bollywood,*boom-boxes and blenders: Domain adaptation for sentiment classification.*in


---

<!-- Página 145 -->

*Proceedings of International Conf erence on Machine Learning (ICML-**2004) . 2004.*33.rie-Francine Moens. A machine learning approach to*sentiment analysis inmultilingual Web texts. Information retrieval, 2009.***12**34.*Using multiple**sources to construct a sentiment sensitive thesaurus for cross-domain**sentiment classification . in**Association for Computational Linguistics (ACL-2011). 2011.*35.*Twitter moodpredicts the**stock market. Journal of Computational Science, 2011.*36.*Holistic sentiment analysis across**languages: multilingual supervised latent Dirichlet allocation. in**Proceedings of the Conference on Empirical Methods in Natural Language**Processing (EMNLP-2010) . 2010.*37.*Learning document-level semantic pr operties from free-text annotations. in**Proceedings of the Annual Meeting of the Association for Computational**Linguistics (ACL-2008) . 2008.*38.*Identifying expressions of**opinion in context . in**national Joint Conference on**Artificial Intelligence (IJCAI-2007) . 2007.*39. Brody, Samuel and Nicholas Diakopoulos.*Cooooooooooooooollllllllllllll!! !!!!!!!!!!!! Us ing Word Lengthening to**Detect Sentiment in Microblogs . in Proceedings of the Conference on**Empirical Methods in Natural Language Processing (EMNLP-2011).*2011.40.*An UnsupervisedAspect-Sentiment**Model for Online Reviews . in**of the North American Chapter of the ACL . 2010.*41.*Cross-linguistic**sentiment analysis: From english to spanish . in*.2009.42. Burfoot, Clinton, StevenBird, and Timothy Baldwin. Collective*classificationof congressional floor-debate transcripts. in**the 49th Annual Meetingof the Association for Computational Linguistics**(ACL-2011) . 2011.*43.*Multi-document**summarization of evaluative text . in**of the Association for Computational Linguistics (EACL-2006). 2006.*44.*Extracting knowledge**from evaluative text . in**Capture (K-CAP-05) . 2005.*45.*Liars**andsaviors ina sentiment annotated corpus of comments to political**debates . in**Meeting of the Association for**Computational Linguistics:shortpapers . 2011.*46.Mohamed Dekhil, Yue Lu, Lei Zhang, and Mark Schreiman.

Sentiment Analysis and Opinion Mining

145

*channel analysis platform for live customer intelligence. in**the 2011 international conference on Management ofdata (SIGMOD-**2011) . 2011.*47. Castillo, Carlos and Brian D. Davison. Adversarial web search.Foundations and Trends inInformation Retrieval, 2010. 4 *LCI: a social*


---

<!-- Página 146 -->

Sentiment Analysis and Opinion Mining

146

*gallery: Opinion extractionand semantic classificationof product reviews.*in*2003) . 2003.*63.*Enhanced sentiment**learning using twitter hashtags and smileys . in**2010 . 2010.*64.*Exploring the value of online**product reviews in forecasting sale s: The case ofmotion pictures. Journal*ofInteractive Marketing, 2007. 21

48. Chaudhuri, Arjun. Emotion and reason in consumer behavior2006:Elsevier Butterworth-Heinemann.49.*What is an opinion**about? exploringpolitical standpoints using opinion scoring model. in**Proceeedings of AAAI Conference on Artificial Intelligence (AAAI-2010).*2010.50.*Online consumer review: Word-of-mouth as**a new element of marketing communication mix. Management Science,*2008. 5451.*Joint extraction of entities and**relations for opinion recognition . in**Empirical Methods in Natural Language Processing (EMNLP-2006).*2006.52.*Adapting a polarity lexicon using integer**linear programming for domain-specific sentiment classification. in**Proceedings of the 2009 Conference on Empirical Methods in Natural**Language Processing (EMNLP-2009) . 2009.*53.*Hierarchical sequential learning for**extracting opinions and their attributes . in**of the Association for Computational Linguistics (ACL-2010). 2010.*54.*Learning with compositional semantics as**structural inference for subsentential sentiment analysis. in**Conference on Empirical Methods inNatural Language Processing**(EMNLP-2008) . 2008.*55.*Identifying sources of opinions with conditional random fields and**extraction patterns . in**Conference and the Conference on Empirical Methods in Natural**Language Processing (HLT/EMNLP-2005) . 2005.*56.*The google similarity distance.*IEEE Transactions on Knowledge and Data Engineering, 2007. 19370-383.57.*Comparative experiments on**sentiment classification for online product reviews. in Proceedings of**AAAI-2006 . 2006.*58. Das, Dipanjan. A Survey on Automatic Text Summarization Single-*Document Summarization. Language, 2007. 4*59.*Yahoo! for Amazon: Extracting market**sentiment from stock message boards . in*. 2001.60.*Yahoo! for Amazon: Sentiment extraction from**small talk on the web. Management Science, 2007. 53*61.*Mine the easy, classify the hard: a semi-**supervisedapproach to automatic sentiment classification. in**of the 47th Annual Meeting of the ACL and the 4th IJCNLP of the AFNLP**(ACL-2009) . 2009.*62.*Mining the peanut*


---

<!-- Página 147 -->

65.*Opinion mining from noisy text data .*in*shop on Analytics for Noisy**Unstructured Text Data (AND-2008) . 2008.*66.*ResolvingObject and Attribute Coreference**in OpinionMining . in Proceedings of International Conference on**Computational Linguistics (COLING-2010) . 2010.*67.*A holistic lexicon-based**approach to opinion mining . in**Search and Web Data Mining(WSDM-2008) . 2008.*68.*Entity discovery andassignment**for opinionmining applications . in Proceedings of ACM SIGKDD**International Conference on Knowledge Discovery and Data Mining**(KDD-2009) . 2009.*69.*Introduction to**Montague semantics . Vol. 11. 1981: Springer.*70.*Construction of a sentimental word dictionary . in**InternationalConference on Information and Knowledge Management**(CIKM-2010) . 2010.*71.*Buildingdomain-oriented sentiment lexiconby**improved informationbottleneck . in**Information and Knowledge Management(CIKM-2009). 2009. ACM.*72.*Adapting**information bottleneck me thod for automatic construction of domain-**oriented sentiment lexicon . in Proceedingsof ACM International**Confernece on Web search and data mining (WSDM-2010). 2010.*73.*Is machine translation**ripe for cross-lingual sentiment classification? in**Annual Meeting of the Association for Computational**Linguistics:shortpapers (ACL-2011) . 2011.*74.*Sentiment retrieval using generative**models . in**Empirical Methods in Natural**Language Processing (EMNLP-2006) . 2006.*75.*Determining term subjectivity and**term orientation for opinion mining . in Proceedings of Conf. of the**European Chapter of the Association for Computational Linguistics**(EACL-2006) . 2006.*76. Esuli, Andrea and Fabrizio Sebastiani. Determining the semantic*orientation ofterms through gloss classification . in**InternationalConference on Information and Knowledge Management**(CIKM-2005) . 2005.*77.*SentiWordNet: A publicly available**lexical resource for opinion mining . in Proceedings of Language**Resources and Evaluation (LREC-2006) . 2006.*78.Fresko. The Stock Sonar - SentimentAnalysisof StocksBased on a Hybrid*Approach . in*

Sentiment Analysis and Opinion Mining

147

*Proceedings of23rd IAAI Conference on Artificial**Intelligence (IAAI-2011) . 2011.*79.*Learning general connotation of**wordsusing graph-based algorithms . in**Empirical Methods in Natural Language Processing (EMNLP-2011).*2011.80.Goetz, and Thomas C. Rindflesch. Interpreting comparative constructions*in biomedical text . in*. 2007.


---

<!-- Página 148 -->

Sentiment Analysis and Opinion Mining

148

81.*Automatic**recognition of multi-word terms:. the C-value/NC-value method.*International Journal onDigital Libraries, 2000. 382. Gamon, Michael.*Sentiment classification on customer feedback data:**noisy data, large feature vectors, and the role of linguistic analysis. in**Proceedings of International Conference on Computational Linguistics**(COLING-2004) . 2004.*83.*Pulse: Mining customer opinions from free text. Advances in Intelligent*Data Analysis VI, 2005: p. 121-132.84.*Mining opinions in comparative**sentences . in**Linguistics (COLING-2008) . 2008.*85.*Opinosis: a graph-**based approachto abstractive summarization of highly redundant**opinions . in Proceedings of the 23rd International Conference on**Computational Linguistics (COLING-2010) . 2010.*86.*Finding hedges by chasing weasels:**Hedge detection using Wikipedia tags and shallow linguistic features. in**Proceedings of the ACL-IJCNLP 2009 Conference, Short Papers. 2009.*87.*A cross-domainadaptation method for**sentiment classification using probabilistic latent analysis. in**of the ACM conference on Information and knowledge management**(CIKM-2011) . 2011.*88.*Bayesian sets. Advances in*Neural Information Pro cessing Systems, 2006. 1889.Fano. Text mining for product attributeextraction. ACM SIGKDDExplorations Newsletter, 2006. 890.*Designing novel review**ranking systems: predicting the usefulness and impact of reviews. in**Proceedings of the Internationa l Conference on Electronic Commerce.*2007.91.*Estimatingthe helpfulness and**economicimpact of productreview s: Mining text and reviewer**characteristics. IEEE Transactions on Knowledge and DataEngineering,*2010.92.*Opinion**miningusing econometrics: A case study on reputation systems. in**Proceedings of the Association for Computational Linguistics (ACL-2007).*2007.93.*Irony in language and**thought: A cognitive science reader, 2007: Lawrence Erlbaum.*94. Gibbs, RaymondW. On the psycholinguistics of sarcasm. Journal ofExperimental Psychology: General, 1986. 11595.*Seeing stars when there aren't**many stars: graph-based semi-sup ervised learning for sentiment**categorization . in Proceedingsof HLT-NAACL 2006 Workshopon**Textgraphs: Graph-based Algorithms for Natural Language Processing*

2006.96.*Identifying sarcasm in Twitter: a closer look . in**Annual Meeting of the Association for Computational**Linguistics:shortpapers (ACL-2011) . 2011.* .


---

<!-- Página 149 -->

97.*More than words: Syntactic packaging**and implicit sentiment . in**The 2009 Annual Conference of the North American Chapter of the ACL**(NAACL-2009) . 2009.*98.*Prediction andsemantic**association . in*. 2003.99.Tenenbaum. Integrating topics and syntax. Advances in NeuralInformation ProcessingSystems, 2005. 17100. Groh, Georg and Jan Hauffa. Characterizing Social Relations Via NLP-*based Sentiment Analysis . in**Conference on Weblogs and Social Media (ICWSM-2011). 2011.*101. Guo, Honglei , Huijia Zhu, Zhili Guo, Xiaoxun Zhang, and Zhong Su.*OpinionIt: a text mining system for cross-lingual opinion analysis. in**Proceeding of the ACM conference on Information and knowledge**management (CIKM-2010) . 2010.*102. Guo, Honglei , Huijia Zhu, Zhili Guo, Xiaoxun Zhang, and Zhong Su.*Product feature categorization with mu ltilevel latent semantic association.*in*Knowledge Management(CIKM-2009) . 2009.*103. Hai, Zhen, Kuiyu Chang, and Jung-jae Kim. Implicit feature identification*via co-occurrence association rule mining. ComputationalLinguistics and*Intelligent Text Processing, 2011: p. 393-404.104. Hancock, Jeffrey T., Lauren E. Curry, Saurabh Goorha, and MichaelWoodworth. On lying and being lied to: A lin guistic analysis of deception*in computer-mediated communication. Discourse Processes, 2007. 45*1-23.105. Hardisty, Eric A., JordanBoyd-Graber, and Philip Resnik. Modeling*perspective using adaptor grammars . in Proceedings of the 2010**Conference on Empirical Methods inNatural Language Processing**(EMNLP-2010) . 2010.*106. Hassan, Ahmed, Amjad Abu-Jbara, Rahul Jha, and Dragomir Radev.*Identifying the semantic orientation of foreign words. in**49th Annual Meeting of the Association for Computational**Linguistics:shortpapers (ACL-2011) . 2011.*107. Hassan, Ahmed, Vahed Qazvinian, and Dragomir Radev. What's with the*attitude?: identifying sentences with attitude inonline discussions. in**Proceedings of the 2010 Conference on Empirical Methods in Natural**Language Processing (EMNLP-2010) . 2010.*108. Hassan, Ahmed and DragomirRadev. Identifying text polarity using*random walks . in**ng of the Association for**Computational Linguistics (ACL-2010) . 2010.*109. Hatzivassiloglou, Vasileios, Judith L. Klavans, Melissa L. Holcombe,Regina Barzilay, Min-Yen Kan, and Kathleen R. McKeown. Simfinder: A*flexible clustering tool for summarization . in In Proceedings of the**Workshop on SummarizationinNAACL-01 . 2001.*110. Hatzivassiloglou, Vasileios and Kathleen R. McKeown. Predicting the*semantic orientation of adjectives . in**Association for Computational Linguistics (ACL-1997)*

Sentiment Analysis and Opinion Mining

149

111. Hatzivassiloglou, Vasileios and Janyce Wiebe.*orientation andgradability on sentence subjectivity. in Proceedings of**Interntional Conference onComputational Linguistics (COLING-2000).*2000.. 1997.*Effects of adjective*


---

<!-- Página 150 -->

Sentiment Analysis and Opinion Mining

150

126. Jiang, Long, Mo Yu, MingZhou, Xiaohua Liu, and Tiejun Zhao. Target-*dependent twitter sentiment classification . in Proceedings of the 49th**Annual Meeting of the Association for Computational Linguistics (ACL-**2011) . 2011.*127. Jijkoun, Valentin , Maarten de Rijke, andWouterWeerkamp. Generating*Focused Topic-Speci Þ*. in Proceedings of Annual*Meeting of the Association for Computational Linguistics (ACL-2010).*2010.

112. He, Yulan. Learning sentiment classificatio n model from labeled features.in*management (CIKM-2011) . 2010.*113. He, Yulan, ChenghuaLin, and HarithAlani. Automatically extracting*polarity-bearing topics for cros s-domain sentiment classification. in**Proceedings of the 49th Annual Meeting of the Association for**Computational Linguistics (ACL-2011) . 2011.*114. Hearst, Marti. Direction-based text interpretation asan informationaccess*refinement , in Text-Based Intelligent Systems , P. Jacobs, Editor1992,*Lawrence ErlbaumAsso ciates. p. 257-274.115. Hobbs, JerryR. and Ellen Riloff. Information Extraction, in*of Natural Language Processing, 2nd Edition , N. Indurkhya and F.J.*Damerau, Editors. 2010, Chapman & Hall/CRC Press.116. Hofmann, Thomas. Probabilistic latent semantic indexing. in*of Conference on Uncertainty in Artificial Intelligence (UAI-1999). 1999.*117. Hong, Yancheng and Steven Skiena. The Wisdom of Bookies? Sentiment*Analysis vs. the NFL Point Spread . in**Conference on Weblogs and Social Media (ICWSM-2010). 2010.*118. Hu, Minqing and Bing Liu. Mining and summarizing customer reviews. in*Proceedings of ACM SIGKDD International Conference on Knowledge**Discovery andData Mining (KDD-2004) . 2004.*119. Hu, Nan, Paul A Pavlou, and Jennifer Zhang. Can online reviews reveal a*product's true quality?: empirical findings and analytical modeling of**Online word-of-mouth communication . in Proceedings of Electronic**Commerce (EC-2006) . 2006.*120. Huang, Xuanjing and W. Bruce Croft. A unified relevance model for*opinion retrieval . in**ACM Confernece on Information and**Knowledge Management(CIKM-2009) . 2009.*121. Ikeda, Daisuke, Hiroya Takamura, Lev-Arie Ratinov, and ManabuOkumura. Learning to shift the polarity of words for sentiment*classification . in**Natural Language Processing (IJCNLP-2008) . 2008.*122. Indurkhya, Nitin and Fred J. Damerau. Handbook of Natural Language*Processing, 2010: Second Edition, Chapman & Hall.*123. Jakob, Niklas and Iryna Gurevych. Extracting Opinion Targets in a Single-*and Cross-DomainSetting with Conditional Random Fields. in**Proceedings of Conference on EmpiricalMethods in Natural Language**Processing (EMNLP-2010) . 2010.*124. Jia, Lifeng, Clement Yu, and Weiyi Meng. The effect of negation on*sentiment analysis and retrieval effectiveness . in**ACM Conference on Information and Knowledge Management (CIKM-**2009) . 2009.*125. Jiang, Jay J. and David W. Conrath. Semantic similarity based on corpus*statistics and lexical taxonomy . in Proceedings of Research in**Computational Linguistics . 1997.*


---

<!-- Página 151 -->

128. Jin, Weiand HungHay Ho. A novel lexicalized HMM-based learning*framework for web opinion mining . in Proceedings of International**Conference on Machine Learning (ICML-2009) . 2009.*129. Jindal, Nitin and Bing Liu. Identifyingcomparative sentences in text*documents . in Proceedings of ACM SIGIR Conf. on Researchand**Development inInformatio n Retrieval (SIGIR-2006). 2006a.*130. Jindal, Nitin and Bing Liu. Mining comparative sentences and relations. in*Proceedings of National Conf. on Artificial Intelligence (AAAI-2006).*2006b.131. Jindal, Nitin and Bing Liu. Opinion spam and analysis. in*the Conference on Web Search and Web Data Mining (WSDM-2008).*2008.132. Jindal, Nitin and Bing Liu. Review spam detection. inProceedings of*WWW (Posterpaper) . 2007.*133. Jindal, Nitin, Bing Liu, and Ee-PengLim. Finding Unusual Review*PatternsUsing Unexpected Rules . in**Conference on Information and Knowledge Management (CIKM-2010).*2010.134. Jo, Yohan and Alice Oh. Aspect and sentiment unificationmodel for online*review analysis . in**Data Mining (WSDM-2011) . 2011.*135. Joachims, Thorsten. Making large-Scale SVM Learning Practical, in*Advances in Kernel Methods - Support Vector Learning, B. Schölkopf, C.*Burges, andA. Smola, Editors. 1999, MIT press.136. Johansson, Richard and Alessandro Moschitti. Reranking models in fine-*grained opinion analysis . in**on ComputationalLinguistics (COLING-2010) . 2010.*137. Joshi, Mahesh, Dipanjan Das, Kevin Gimpel, and Noah A. Smith. Movie*reviews and revenues: An experiment in text regression. in**the North American Chapter of the Association for Computational**Linguistics Human Language Technologies Conference (NAACL 2010).*2010.138. Kaji, Nobuhiro and MasaruKitsuregawa. Automatic construction of*polarity-tagged corpus from HTML documents. in Proceedings of**COLING/ACL 2006 Main Conference Poster Sessions(COLING-ACL-**2006) . 2006.*139. Kaji, Nobuhiro and Masaru Kitsuregawa. Building lexicon for sentiment*analysis from massive colle ction of HTML documents. in**the Joint Conference onEmpirical Methods in Natural Language**Processing andComputationalNatural Language Learning(EMNLP-**2007) . 2007.*140. Kamps, Jaap, Maarten Marx, Robert J. Mokken, and Maarten De Rijke.*Using WordNet to measure semantic orientation of adjectives. in**LREC-2004 . 2004.*141. Kanayama, Hiroshi and Tetsuya Nasukawa. Fully automatic lexicon*expansion for domain-oriented sentiment analysis. in*

*rnational Conference*

Sentiment Analysis and Opinion Mining

151

*Conference on Empirical Methods inNatural Language Processing**(EMNLP-2006) . 2006.*142. Kennedy, Alistair and Diana Inkpen. Sentiment classificationof movie*reviews using contextual valence shifters. Computational Intelligence,*2006. 22143. Kennedy, Christopher. Comparatives, Semantics of, inEncyclopedia of*Languageand Linguistics, Second Edition, 2005, Elsevier.*144. Kessler, Jason S. and Nicolas Nicolov. Targeting sentiment expressions*through supervised ranking of linguistic configurations. in* *Proceedings of*


---

<!-- Página 152 -->

Sentiment Analysis and Opinion Mining

152

*the Third International AAAI Conference on Weblogs and Social Media**(ICWSM-2009) . 2009.*145. Kim, Hyun Duk and ChengXiang Zhai.*Generating comparative**summaries of contradictory opinions intext . in Proceedings ofACM**Conference on Information and Knowledge Management (CIKM-2009).*2009.146. Kim, Jungi Kim, Jin-Ji Li, and Jong-Hyeok Lee.*Evaluating**multilanguage-comparab ility of subjectivity analysis systems. in**Proceedings of the 48th Annual Meeting of the Association for**Computational Linguistics (ACL-2010) . 2010.*147. Kim, Jungi, Jin-Ji Li, and Jong-Hyeok Lee. Discovering the discriminative*views: Measuring term weights for sentiment analysis. in**the 47th Annual Meetingofthe ACL and the 4thIJCNLP of the AFNLP**(ACL-2009) . 2009.*148. Kim, Soo-Min and EduardHovy. Automatic identification of proand con*reasons in online reviews . in**NG/ACL 2006 Main**Conference Poster Sessions (ACL-2006) . 2006.*149. Kim, Soo-Min and EduardHovy. Crystal: Analyzing predictive opinions*on the web . in**onference on Empirical Methods**in Natural Language Processingand Computational Natural Language**Learning (EMNLP/CoNLL-2007) . 2007.*150. Kim, Soo-Min and EduardHovy. Determining the sentiment ofopinions. in*Proceedings of Interntional Conference on Computational Linguistics**(COLING-2004) . 2004.*151. Kim, Soo-Min and Eduard Hovy. Extracting opinions, opinion holders,*and topics expressed inonline newsmedia text. in**Conference on Empirical Methods inNatural Language Processing**(EMNLP-2006) . 2006.*152. Kim, Soo-Min and Eduard Hovy. Identifying and analyzing judgment*opinions . in**the North American Chapterof the ACL . 2006.*153. Kim, Soo-Min, Patrick Pantel, Tim Chklovski, and Marco Pennacchiotti.*Automatically assessing review helpfulness . in Proceedings of the**Conference on Empirical Methods inNatural Language Processing**(EMNLP-2006) . 2006.*154. Kleinberg, Jon M. Authoritative sources in a hyperlinked environment.Journal of the ACM (JACM), 1999. 46155. Kobayashi, Nozomi, Ryu Iida, Kentaro Inui, and Yuji Matsumoto. Opinion*miningon the Webbyextracting subject-attribute-value relations. in**Proceedings ofAAAI-CAAW'06 . 2006.*156. Kobayashi, Nozomi, Kentaro Inui, and YujiMatsumoto. Extracting aspect-*evaluation and aspect-of relations inopinion mining. in**2007 Joint Conference on Empirical Methods inNatural Language**Processing and Computational Natural Language Learning. 2007.*157. Kouloumpis, Efthymios, Theresa Wilson, and Johanna Moore. Twitter*Sentiment Analysis: The Good the Badand the OMG! in**the FifthInternational AAAI Confer ence on Weblogs andSocial Media**(ICWSM-2011)*

. 2011.158. Kovelamudi, Sudheer, Sethu Ramalingam, Arpit Sood, and VasudevaVarma. Domain Independent Model for Product Attribute Extraction from*User Reviews using Wikipedia . in**Joint Conference on Natural Lan guage Processing (IJCNLP-2010). 2011.*159. Kreuz, Roger J and Gina M Caucci. Lexical influences on the perception*of sarcasm . in**to Figurative Language . 2007.*


---

<!-- Página 153 -->

160. Kreuz, Roger J. and Sam Glucksberg. How to be sarcastic: The echoic*reminder theory of verbal irony. Journalof Experimental Psychology:*General, 1989. 118161. Ku, Lun-Wei, Yu-Ting Liang, and Hsin-Hsi Chen. Opinion extraction,*summarization and trackingin news and blog corpora. in**AAAI-CAAW'06 . 2006.*162. Lafferty, John, Andrew McCallum, and Fernando Pereira. Conditional*random fields: Probabilistic models for segmenting and labeling sequence**data Proceedings of International Conference on Machine Learning**(ICML-2001) . 2001.*163. Lakkaraju, Himabindu, Chiranjib Bhattacharyya, Indrajit Bhattacharya, andSrujana Merugu. Exploiting Coherence for the Simultaneous Discovery of*Latent Facets and associated Sentiments . in Proceedings ofSIAM**Conference on DataMining (SDM-2011) . 2011.*164. Lappas, Theodoros and Dimitrios Gunopulos. Efficient confident search in*large review corpora . in*165. Lee, Lillian. Measures of distributional similarity. in Proceedings of*Annual Meeting of the Association for Computational Linguistics (ACL-**1999) . 1999.*166. Lerman, Kevin, Sasha Blair-Goldensohn, and Ryan McDonald. Sentiment*summarization: Evaluatingand learning user preferences. in**of the 12th Conference of the EuropeanChapter of the Association for**Computational Linguistics (EACL-2009) . 2009.*167. Lerman, Kevin and Ryan McDonald. Contrastive summarization: an*experiment with consumer reviews . in**Short Papers . 2009.*168. Li, Binyang, Lanjun Zhou, Shi Feng, andKam-Fai Wong. A UniÞ*Graph Modelfor Sentence-Based Opinion Retrieval. in**Annual Meeting of the Association for Computational Linguistics (ACL-**2010) . 2010.*169. Li, Fangtao, Chao Han, Minlie Huang, Xiaoyan Zhu, Ying-Ju Xia, ShuZhang, and Hao Yu. Structure-aware review mining and summarization. in*Proceedings ofthe 23rd International Conference onComputational**Linguistics (COLING-2010) . 2010.*170. Li, Fangtao, Minlie Huang, YiYang, and Xiaoyan Zhu. Learning to*Identify Review Spam . in Proceedings of the International Joint**Conference on Artificial Intelligence (IJCAI-2011). 2011.*171. Li, Fangtao, Minlie Huang, and Xiaoyan Zhu. Sentiment analysis with*global topics and localdependency . in**AAAI Conference on Artificia l Intelligence (AAAI-2010). 2010.*172. Li, Junhui, Guodong Zhou, Hongling Wang, and Qiaoming Zhu. Learning*the scope of negation via shallow semantic parsing. in**23rd International Conference on Computational Linguistics (COLING-**2010) . 2010.*173. Li, Shasha, Chin-Yew Lin, Young-In Song, and ZhoujunLi.

. 2010.

Sentiment Analysis and Opinion Mining

153

*entity mining from comparative questions . inProceedings ofAnnual**Meeting of the Association for Computational Linguistics (ACL-2010).*2010.174. Li, Shoushan, Chu-Ren Huang, GuodongZhou, and Sophia Yat Mei Lee.*Employing Personal/Impersonal Views inSupervised and Semi-Supervised**Sentiment Classi Þ . in Proceedings of AnnualMeeting of the**Association for Computational Linguistics (ACL-2010). 2010.*175. Li, Shoushan, Sophia YatMei Lee, Ying Chen, Chu-Ren Huang, andGuodong Zhou. Sentimentclassification and polarity shifting. in *Comparable*


---

<!-- Página 154 -->

Sentiment Analysis and Opinion Mining

154

. 2009.190. Liu, Feifan, DongWang, Bin Li, and Yang Liu. Improving blogpolarity*classificationvia topic analysis and adaptive methods. in**Human Language Technologies: The 2010 Annual Conference of the North**American Chapter of the ACL (HLT-NAACL-2010). 2010.*191. Liu, Jingjing, Yunbo Cao, Chin-Yew Lin, Yalou Huang, and Ming Zhou.*Low-quality product review detection in opinion summarization. in*

*Proceedings ofthe 23rd International Conference onComputational**Linguistics (COLING-2010) . 2010.*176. Li, Shoushan, Zhongqing Wang, Guodong Zhou, and Sophia Yat Mei Lee.*Semi-SupervisedLearningfor Imbalanced Sentiment Classification. in**Proceedings of International Joint Conference on Artificial Intelligence**(IJCAI-2011) . 2011.*177. Li, Tao, Yi Zhang, and Vikas Sindhwani. A non-negative matrix tri-*factorizationapproach tosentiment classification with lexical prior**knowledge . in**Computational Linguistics (ACL-2009) . 2009.*178. Li, Xiao-Li, Lei Zhang, Bing Liu, and See-Kiong Ng. Distributional*similarity vs. PU learning for entity set expansion. in Proceedings of**Annual Meeting of the Association for Computational Linguistics (ACL-**2010) . 2010.*179. Lim, Ee-Peng, Viet-AnNguyen, NitinJindal, Bing Liu, and HadyW.Lauw. Detecting Product Review Spammers using Rating Behaviors. in*Proceedings of ACM International Conference onInformation and**Knowledge Management(CIKM-2010) . 2010.*180. Lin, Chenghua and Yulan He. Joint sentiment/topic model for sentiment*analysis . in**Conference on Information**and Knowledge Management (CIKM-2009) . 2009.*181. Lin, Dekang. Automatic retrieval and clusteringof similar words. in*Proccedings of 36th AnnualMeeting of the Association for Computational**Linguistics and 17th International Conference on Computational**Linguistics (COLING-ACL-1998) . 1998.*182. Lin, Dekang. Minipar . [http://webdocs.cs.ualberta.ca/lindek/minipar.htm](http://webdocs.cs.ualberta.ca/lindek/minipar.htm).2007.183. Lin, Wei-Hao, Theresa Wilson, Janyce Wiebe, and Alexander Hauptmann.*Which sideare youon?: identifyingperspectives at the document and**sentence levels . in**ence on Natural Language**Learning (CoNLL-2006) . 2006.*184. Liu, Bing. Sentiment Analysis andSubjectivity, in*Language Processing, Second Edition , N. Indurkhya and F.J. Damerau,*Editors. 2010.185. Liu, Bing. Web DataMining: Exploring Hyperlinks, Contents, and Usage*Data, 2006 and2011: Springer.*186. Liu, Bing, Wynne Hsu, and Yiming Ma. Integrating classification and*association rule mining . in**ational Conference on**Knowledge Discovery and Data Mining (KDD-1998). 1998.*187. Liu, Bing, Minqing Hu, and Junsheng Cheng. Opinion observer: Analyzing*and comparing opinions on the web . in Proceedings ofInternational**Conference onWorld Wide Web (WWW-2005) . 2005.*188. Liu, Bing, Wee Sun Lee, Philip S. Yu, andXiao-Li Li. Partially supervised*classification of text documents . in Proceedings ofInternational**Conference on Machine Learning (ICML-2002) . 2002.*189. Liu, Feifan, Bin Li, and Yang Liu. Finding Opinionated Blogs Using*Statistical Classifiers and Lexical Features . in**International AAAI Conference on We blogs and Social Media (ICWSM-**2009)*


---

<!-- Página 155 -->

*Computational Linguistics (ACL-2011) . 2011.*205. Macdonald, Craig, Iadh Ounis, and Ian Soboroff. Overview of the TREC*2007 blogtrack . 2007.*206. Manevitz, Larry M. and Malik Yousef. One-class SVMs for document*classification. The Journal of Machine Learning Research, 2002. 2*154.

*Proceedings of the Joint Conference on Empirical Methods in Natural**Language Processing and Computational Natural Language Learning**(EMNLP-CoNLL-2007) . 2007.*192. Liu, Jingjing and Stephanie Seneff. Review sentiment scoring via a parse-*and-paraphrase paradigm . in Proceedings of the 2009 Conference on**Empirical Methods in Natural Language Processing (EMNLP-2009).*2009.193. Liu, Yang, Xiangji Huang, Aijun An, and Xiaohui Yu. ARSA: a sentiment-*aware model for predicting sales performance using blogs. in**of ACM SIGIR Conf. on Research and Developmentin Information**Retrieval (SIGIR-2007) . 2007.*194. Liu, Yang, Xiangji Huang, Aijun An, and Xiaohui Yu. Modeling and*predicting the helpfulness of online reviews . in Proceedings of ICDM-**2008 . 2008.*195. Long, Chong, Jie Zhang, and Xiaoyan Zhu. A review selection approach*for accurate feature rating estimation . in**Poster Volume . 2010.*196. Lu, Bin. Identifying opinion holders andtargets with dependency parser in*Chinese news texts . in**2010 Annual Conference of the North American Chapter of the ACL (HLT-**NAACL-2010) . 2010.*197. Lu, Bin, Chenhao Tan, Claire Cardie, and Benjamin K. Tsou. Joint*bilingualsentiment classification withunlabeled parallel corpora. in**Proceedings of the 49th Annual Meeting of the Association for**Computational Linguistics (ACL-2011) . 2011.*198. Lu, Yue, Malu Castellanos, Um eshwar Dayal, and ChengXiang Zhai.*Automatic constructionof a context-aware sentiment lexicon: an**optimization approach . in**international conference**on World wide web (WWW-2011) . 2011.*199. Lu, Yue, Huizhong Duan, HongningWang, and ChengXiang Zhai.*Exploiting StructuredOntology to Organize Scattered Online Opinions. in**Proceedings of Interntional Conference on Computational Linguistics**(COLING-2010) . 2010.*200. Lu, Yue, Panayiotis Tsaparas, Al exandros Ntoulas, and Livia Polanyi.*Exploiting social context for review quality prediction. in**International World Wide Web Confernece (WWW-2010). 2010.*201. Lu, Yue and ChengXiang Zhai. Opinion integration through semi-*supervised topic modeling . in**World Wide Web (WWW-2008) . 2008.*202. Lu, Yue, ChengXiang Zhai, and Neel Sundaresan.*Rated aspect**summarization of short comments . in Proceedings ofInternational**Conference onWorld Wide Web (WWW-2009) . 2009.*203. Ma, Tengfei and Xiaojun Wan. Opinion target extraction in Chinese news*comments . in*.2010.204. Maas, Andrew L., Raymond E. Daly, Peter T. Pham, Dan Huang, AndrewY. Ng, and Christopher Potts. Learning word vectors for sentiment*analysis . in**Meeting of the Association for*

Sentiment Analysis and Opinion Mining

155


---

<!-- Página 156 -->

Sentiment Analysis and Opinion Mining

156

222. Moghaddam, Samaneh and Martin Ester. ILDA: interdependent LDA*model for learning latentaspects and their ratings from online product**reviews . in Proceedings of the Annual ACM SIGIR International**conference on Research and Development in Information Retrieval (SIGIR-**2011) . 2011.*223. Moghaddam, Samaneh and Martin Ester. Opinion digger: an unsupervised*opinion miner from unstructured productreviews. in*

207. Manning, Christopher D., Prabhakar Raghavan, and Hinrich Schutze.*Introduction to information retrieval . Vol. 1. 2008: Cambridge University*Press.208. Manning, Christopher D. and Hinrich Schutze. Foundations ofstatistical*natural language processing . Vol. 999. 1999: MIT Press.*209. Martineau, Justin and Tim Finin. Delta tfidf: An improved feature space for*sentiment analysis . in Proceedings of the Third International AAAI**Conference on Weblogs and Social Media (ICWSM-2009). 2009.*210. McDonald, Ryan, Kerry Hannan, Tyler Neylon, Mike Wells, and JeffReynar. Structured models for fine-to-coarse sentiment analysis. in*Proceedings of Annual Meeting of the Association for Computational**Linguistics (ACL-2007) . 2007.*211. McGlohon, Mary, Natalie Glance, and Zach Reiter. Star quality:*Aggregating reviews to rank productsand merchants. in**the International Conference on Weblogs and SocialMedia (ICWSM-**2010) . 2010.*212. Medlock, Ben and Ted Briscoe. Weakly supervised learning for hedge*classification in scientific literature . in**Meeting ofthe Associationof ComputationalLinguistics. 2007.*213. Mei, Qiaozhu, Xu Ling, MatthewWondra, Hang Su, and ChengXiangZhai. Topic sentimentmixture: modeling facets and opinions in weblogs. in*Proceedings of International Conference on World Wide Web (WWW-**2007) . 2007.*214. Mejova, Yelena and Padmini Srinivasan. ExploringFeature Definition and*Selection for Sentiment Classifiers . in Proceedings of the Fifth**International AAAI Conference on We blogs and Social Media (ICWSM-**2011) . 2011.*215. Meng, Xinfanand HoufengWang. Mininguser reviews: from specification*to summarization . in**Short Papers . 2009.*216. Mihalcea, Rada, Carmen Banea, and JanyceWiebe. Learning multilingual*subjective language via cross-lingual projections. in**Annual Meeting of the Association for Computational Linguistics (ACL-**2007) . 2007.*217. Mihalcea, Rada a nd Carlo Strapparava. The lie detector: Explorations in*the automatic recogniti on of deceptive language. in**ACL-IJCNLP 2009 Conference Short Papers . 2009.*218. Miller, George A., RichardBeckwith, Christiane Fellbaum, Derek Gross,and Katherine Miller. WordNet: An on-line lexical database1990: OxfordUniv. Press.219. Miller, Mahalia, Conal Sathi, Daniel Wiesenthal, Jure Leskovec, andChristopher Potts. Sentiment Flow Through Hyperlink Networks. in*Proceedings of the Fifth International AAAI Conference on Weblogs and**Social Media (ICWSM-2011) . 2011.*220. Min, Hye-Jin and Jong C. Park. Detecting and Blocking False Sentiment*Propagation . in**Natural Language Processing (IJCNLP-2010) . 2011.*221. Mitchell, Tom. Machine learning 1997: McGraw Hill.


---

<!-- Página 157 -->

*ACM conference on Information and knowledge management (CIKM-**2010) . 2010.*224. Moghaddam, Samaneh, Mohsen Jamali, and MartinEster. ETF: extended*tensor factorization model for personalizing prediction of review**helpfulness . in Proceedings of ACM International Conference on Web**Search andData Mining (WSDM-2012) . 2012.*225. Mohammad, Saif. From Once Upon aTime to Happily Ever After:*Tracking Emotions in Novels and Fairy Tales . in**2011 Workshop on Language Technologyfor Cultural Heritage, Social**Sciences, and Humanities (LaTeCH) . 2011.*226. Mohammad, Saif and Tony Yang. Tracking Sentiment in Mail: How*Genders Differ on Emotional Axes . in**onACL 2011 Workshop on ComputationalApproaches to Subjectivityand**Sentiment Analysis (WASSA-2011) . 2011.*227. Mohammad, Saif, Cody Dunne, and Bonnie Dorr. Generating high-*coverage semantic orientation lexicons from overtly marked words and a**thesaurus . in**erence on Empirical Methods in**Natural Language Processing (EMNLP-2009) . 2009.*228. Mohammad, Saif and Graeme Hirst. Distributional measures of concept-*distance: A task-oriented evaluation . in**Empirical Methods in Natural Language Processing (EMNLP-2006).*2006.229. Mohammad, Saif M. and Peter D. Turney. Emotions evoked by common*words andphrases: Using mechanical tu rk to create an emotion lexicon. in**Proceedings of the NAACL HLT 2010 Workshop on Computational**Approaches toAnalysis andGeneration ofEmotion in Text. 2010.*230. Moilanen, Karo and Stephen Pulman.*Sentiment composition . in**Proceedings of Recent Advances in Na tural Language Processing (RANLP**2007) . 2007.*231. Montague, Richard. Formal philosophy; selected papers of Richard*Montague, 1974: Yale University Press.*232. Mooney, Raymond J. and Razvan Bunescu. Mining knowledge fromtext*using information extraction. ACM SIGKDD Explorations Newsletter,*2005. 7233. Morante, Roser, Sarah Schrauwen, and Walter Daelemans. Corpus-based*approaches toprocessing the scope of negation cues: an evaluation of the**state of the art . in**Computational Semantics (IWCS-2011) . 2011.*234. Morinaga, Satoshi, KenjiYamanishi, KenjiTateishi, and ToshikazuFukushima. Mining product reputationson the web. in Proceedings of*ACM SIGKDD International Conference on Knowledge Discovery and**Data Mining (KDD-2002) . 2002.*235. Mukherjee, Arjun and Bing Liu. Aspect Extraction through Semi-*Supervised Modeling . in**for Computational Linguistics (ACL -2012) (Accepted for publication).*2012.236. Mukherjee, Arjun and Bing Liu.*Modeling Review Comments . in**Proceedings of 50th Anunal Meeting ofAssociation for Computational**Linguistics (ACL-2012) (A ccepted for publication).*

Sentiment Analysis and Opinion Mining

157

237. Mukherjee, Arjun, Bing Liu, and Natalie Glance. Spotting Fake Reviewer*Groups in Consumer Reviews . in**Conference (WWW-2012) . 2012.*238. Mukherjee, Arjun, Bing Liu, JunhuiWang, Natalie Glance, and NitinJindal. Detecting Group Review Spam . in Proceedings of International*Conference on World WideWeb(WWW-2011, poster paper). 2011.* 2012.


---

<!-- Página 158 -->

Sentiment Analysis and Opinion Mining

158

*formulation for sentence extraction and ordering . in**2010: Poster Volume . 2010a.*254. Nishikawa, Hitoshi, TakaakiHasegawa, Yoshihiro Matsuo, and GenichiroKikui. Optimizing informativeness and readability for sentiment

239. Mukund, Smruthi and Rohini K. Srihari. A vector spacemodel for*subjectivity classification inUrdu aided by co-training. in**Coling 2010: Poster Volume . 2010.*240. Mullen, Tony and NigelCollier. Sentiment analysis using support vector*machines with diverse information sources . in**2004 . 2004.*241. Murakami, Akiko and Rudy Raymond. Support oroppose?: classifying*positions inonline debates from reply activities andopinion expressions. in**Proceedings ofColing 2010: Poster Volume . 2010.*242. Na, Seung-Hoon, Yeha Lee, Sang-Hyob Nam, and Jong-Hyeok Lee.*Improving opinion retrieval based on query-specific sentiment lexicon.*Advances in Information Retrieval, 2009: p. 734-738.243. Nakagawa, Tetsuji, Kentaro Inui, and Sadao Kurohashi. Dependency tree-*based sentiment classification using CRFs withhidden variables. in**Proceedings of Human Language Technologies: The 2010 Annual**Conference of the NorthAmerican Chapter of the ACL (HAACL-2010).*2010.244. Narayanan, Ramanathan, Bing Liu, and Alok Choudhary. Sentiment*analysis of conditional sentences . in Proceedings of Conference on**Empirical Methods in Natural Language Processing (EMNLP-2009).*2009.245. Nasukawa, Tetsuya and Jeonghee Yi. Sentiment analysis: Capturing*favorability usingnatural language processing . in**CAP-03, 2ndIntl. Conf. on Knowledge Capture . 2003.*246. Neviarouskaya, Alena, Helmut Prendinger, and Mitsuru Ishizuka.*Compositionality principle in recognitionof fine-grained emotions from**text Proceedings of Third International Conference on Weblogsand**Social Media (ICWSM-2009) . 2009.*247. Neviarouskaya, Alena, Helmut Prendinger, and Mitsuru Ishizuka.*Recognitionofaffect, judgment, and appreciation in text. in**the 23rdInternational Conference on Computational Linguistics**(COLING-2010) . 2010.*248. Newman, Matthew L., James W. Pennebaker, Diane S. Berry, and Jane M.Richards. Lying words: Predicting deception from linguisticstyles.Personality and Social Psychology Bulletin, 2003. 29249. Ng, Vincent and Claire Cardie. Improving machine learning approaches to*coreference resolution . in Proceedings of the Annual Meeting of the**Association for Computational Linguistics (ACL-2002). 2002.*250. Ng, Vincent, Sajib Dasgupta, and S. M. Niaz Arifin. Examining the role of*linguistic knowledge sources in the automatic identification and**classification ofreviews . in Proceedings of COLING/ACL 2006 Main**Conference Poster Sessions (COLING/ACL-2006). 2006.*251. Nigam, Kamal and MatthewHurst. Towards a robust metric of opinion. in*Proceedings of AAAI Spring Symp. on Exploring Attitude and Affect in**Text*252. Nigam, Kamal, AndrewK. McCallum, Sebastian Thrun, and TomMitchell. Text classification from labeled andunlabeleddocuments using*EM.***39**253. Nishikawa, Hitoshi, TakaakiHasegawa, Yoshihiro Matsuo, and GenichiroKikui. Opinion summarization with integer linear programming


---

<!-- Página 159 -->

*of Conference on Empirical Methods inNatural Language Processing**(EMNLP-2002) . 2002.*268. Pantel, Patrick, Eric Crestan, Arkady Borkovsky, Ana-Maria Popescu, andVishnu Vyas. Web-scale distributional similarity and entity set expansion.in*Processing (EMNLP-2009) . 2009.*269. Park, Do-Hyung, Jumin Lee, andIngoo Han. The effect of on-line*consumer reviews on consumer purchasing intention: The moderating role**of involvement. International Journal of Electronic Commerce, 2007. 11*p. 125-148.

*summarization . in**Computational Linguistics (ACL-2010) . 2010b.*255. O'Connor, Brendan, Ramnath Balasubramanyan, Bryan R. Routledge, andNoahA. Smith. From Tweets to Polls: Linking Text Sentiment to Public*Opinion Time Series. in**on Weblogs and Social Media (ICWSM 2010) . 2010.*256. O'Mahony, Michael P. and Barry Smyth. Learning to recommend helpful*hotel reviews . in Proceedings of the third ACM conference on**Recommender systems . 2009.*257. Ott, Myle, Yejin Choi, Claire Cardie, and Jeffrey T. Hancock. Finding*deceptive opinion spam by any stretch of the imagination. in**of the 49th Annual Meeting of the Association for Computational**Linguistics (ACL-2011) . 2011.*258. Ounis, Iadh, Craig Macdonald, Maarten de Rijke, Gilad Mishne, and IanSoboroff. Overview of the TREC-2006 blog track. in*Fifteenth Text REtrieva l Conference (TREC-2006). 2006.*259. Ounis, Iadh, Craig Macdonald, and Ian Soboroff. Overview of the TREC-*2008 blogtrack . in**Text REtrieval Conference**(TREC-2008) . 2008.*260. Page, Lawrence, Sergey Brin, Rajeev Motwani, and TerryWinograd. The*PageRank citation ranking: Bringing order to the web. 1999.*261. Paltoglou, Georgios and Mike Thelwall. A study of information retrieval*weighting schemes for sentiment analysis . in Proceedingsof the 48th**Annual Meeting of the Association for Computational Linguistics (ACL-**2010) . 2010.*262. Pan, Sinno Jialin, Xiaochuan Ni, Jian-TaoSun, Qiang Yang, and ZhengChen. Cross-domain sentiment classificationvia spectral feature*alignment . in**(WWW-2010) . 2010.*263. Pang, Bo and Lillian Lee. Opinion mining and sentiment analysis.Foundations and Trends inInformation Retrieval, 2008. 2264. Pang, Bo and Lillian Lee. Seeing stars: Exploiting class relationships for*sentiment categorization with respect to rating scales. in**Meeting of the Association for Computational Linguistics (ACL-2005).*2005.265. Pang, Bo and Lillian Lee. A sentimental education: Sentiment analysis*using subjectivity summarization based onminimum cuts. in**of Meeting of the Association for Computational Linguistics (ACL-2004).*2004.266. Pang, Bo andLillian Lee. Using Very Simple Statistics for Review Search:*An Exploration . in Proceedings ofInternational Conference on**Computational Linguistics, poster paper (COLING-2008). 2008.*267. Pang, Bo, Lillian Lee, and Shivakumar Vaithyanathan. Thumbs up?:*sentiment classification usingmachine learning techniques. in*

Sentiment Analysis and Opinion Mining

159


---

<!-- Página 160 -->

Sentiment Analysis and Opinion Mining

160

270. Park, Souneil, KyungSoon Lee, and Junehwa Song. Contrasting opposing*views of news articles on contentious issues . in**Annual Meeting of the Association for Computational Linguistics (ACL-**2011) . 2011.*271. Parrott, W. Gerrod. Emotions insocial psychology: Essential*readings 2001: Psychology Pr.*272. Paul, Michael J., ChengXiang Zhai, and Roxana Girju. Summarizing*Contrastive Viewpoints in Opinionated Text . in**on Empirical Methods in Natural Language Processing (EMNLP-2010).*2010.273. Peng, Wei and Dae Hoon Park. Generate Adjective Sentiment Dictionary*for SocialMedia Sentiment AnalysisUsing Constrained Nonnegative**Matrix Factorization . in Proceedings of the Fifth International AAAI**Conference on Weblogs and Social Media (ICWSM-2011). 2011.*274. Pennebaker, James W., Cindy K. Chung, Molly Ireland, Amy Gonzales,and Roger J. Booth. The development and psychometric properties of*LIWC2007. www.LIWC.Net, 2007.*275. Polanyi, Livia and Annie Zaenen.*Contextual valence shifters . in**Proceedings of the AAAI Spring Symposium on Exploring Attitudeand**Affect in Text . 2004.*276. Popescu, Ana-Maria and Oren Etzioni. Extracting product features and*opinions from reviews . in Proceedings of Conference onEmpirical**Methods in Natural Language Processing (EMNLP-2005). 2005.*277. Qiu, Guang, Bing Liu, Jiajun Bu, and Chun Chen. Expanding domain*sentiment lexicon through double propagation. in Proceedings of**International Joint Conference on Artificial Intelligence (IJCAI-2009).*2009.278. Qiu, Guang, Bing Liu, Jiajun Bu, and Chun Chen. Opinion Word*Expansion and Target Extraction through Double Propagation.*ComputationalLinguistics, Vol. 37, No. 1: 9.27, 2011.279. Qiu, Likun, Weish Zhang, Changjian Hu, and Kai Zhao. Selc: aself-*supervisedmodel for sentiment classification . in**ACM conference on Information and knowledge management (CIKM-**2009) . 2009.*280. Qu, Lizhen, Georgiana Ifrim, and Gerhard Weikum. The Bag-of-Opinions*Method for Review Rating Prediction fromSparse Text Patterns. in**Proceedings of the International Conference on Computational Linguistics**(COLING-2010) . 2010.*281. Quirk, Randolph, Si dney Greenbaum, Geoffrey Leech, and Jan Svartvik. A*comprehensive grammar of the English language. Vol. 397. 1985:*Cambridge Univ Press.282. Raaijmakers, Stephan and Wessel Kraaij.*A shallow approach to**subjectivity classification , in*2008. p. 216-217.283. Raaijmakers, Stephan, Kh*Multimodal**subjectivity analysis ofmultiparty conversation. in Proceedings of**Conference on Empirical Methods inNatural Language Processing**(EMNLP-2008) . 2008.*284. Rabiner, Lawrence R. A tutorial on hidden Markov models and selected*applications in speech recognition.*

Proceedings of the IEEE, 1989. 77p. 257-286.285. Radev, Dragomir R., Simone Teufel, Horacio Saggion, Wai Lam, JohnBlitzer, Hong Qi, ArdaCelebi, Danyu Liu, and Elliott Drabek. Evaluation*challenges in large-scale document summarization. in*


---

<!-- Página 161 -->

*Annual Meeting of the Association for Computational Linguistics (ACL-**2003) . 2003.*286. Rao, Delipand DeepakRavichandran. Semi-supervised polaritylexicon*induction . in**ence of the European Chapter**of the ACL (EACL-2009) . 2009.*287. Ravichandran, Deepak and Eduard Hovy. Learning surface text patterns*for a question answeringsystem . in**the Association for Computational Linguistics (ACL-2002). 2002.*288. Riloff, Ellen. Automatically constructing adictionary for information*extraction tasks . in*. 1993.289. Riloff, Ellen. Automatically generatingextraction patterns from untagged*text Proceedings ofAAAI-1996 . 1996.*290. Riloff, Ellen, Siddharth Patwardhan, andJanyce Wiebe. Feature*subsumption for opinionanalysis . in**Empirical Methods in Natural Language Processing (EMNLP-2006).*2006.291. Riloff, Ellen and Janyce Wiebe. Learning extraction patterns for subjective*expressions . in Proceedings of Conference on Empirical Methods in**Natural Language Processing (EMNLP-2003) . 2003.*292. Ruppenhofer, Josef, Swapna Somasundaran, and JanyceWiebe. Finding*the sources and targets of subjective expressions . in*.2008.293. Sadikov, Eldar, Aditya Parameswaran, and Petros Venetis. Blogs as*predictors of movie success . in Proceedings of the Third International**Conference on Weblogs and Social Media (ICWSM-2009). 2009.*294. Sakunkoo, Patty andNathan Sakunkoo. Analysis of Social Influence in*Online Book Reviews . in Proceedings of third International AAAI**Conference on Weblogs and Social Media (ICWSM-2009). 2009.*295. Santorini, Beatrice. Part-of-speech taggingguidelines for the Penn*Treebank Project, 1990: University ofPennsylvania, School of*Engineering and Applied Science, Dept. of Computer and InformationScience.296. Sarawagi, Sunita. Information extraction. Foundations and Trends inDatabases, 2008. 1297. Sauper, Christina, Aria Haghighi, and Regina Barzilay. Content models*with attitude . in**for ComputationalLinguistics (ACL-2011) . 2011.*298. Scaffidi, Christopher, Kevin Bierhoff, Eric Chang, Mikhael Felker,Herman Ng, and Chun Jin. Red Opal: product-feature scoring from*reviews . in Proceedings of Twelfth ACM Conference on Electronic**Commerce (EC-2007) . 2007.*299. Schapire, Robert E. and Yoram Singer. BoosTexter: A boosting-based*system for text categorization. Machine learning, 2000.*

Sentiment Analysis and Opinion Mining

161

300. Seki, Yohei, Koji Eguchi, Noriko Kando, and Masaki Aono. Opinion-*focused summarization andits analysis at DUC 2006. in**the DocumentUnderstanding Conference (DUC) . 2006.*301. Shanahan, James G., Yan Qu, and JanyceWiebe. Computing attitude and*affect in text: theory and applications . Vol. 20. 2006: Springer-Verlag New*York Inc.302. Shawe-Taylor, John and Nello Cristianini. Support Vector Machines, 2000,Cambridge University Press.303. Snyder, Benjamin and Regina Barzilay. Multiple aspect rankingusing the*good griefalgorithm . in Proceedings of the Conference of the North**American Chapter of the Association for Computational Linguistics:**Human Language Technologies (NAACL/HLT-2007). 2007.* **39**


---

<!-- Página 162 -->

Sentiment Analysis and Opinion Mining

162

304. Socher, R., J. Pennington, E. H. Huang, A.Y. Ng, and C.D. Manning. Semi-*Supervised Recursive Autoencoders for PredictingSentiment Distributions.*in*Language Processing (EMNLP-2011) . 2011.*305. Somasundaran, S., J. Ruppenhofer, and J. Wiebe. Discourse level opinion*relations: An annotation study . in Proceedings of the 9th SIGdial**Workshop on Discourse and Dialogue . 2008.*306. Somasundaran, Swapna, GalileoNamata, Lise Getoor, and Janyce Wiebe.*Opinion graphs for polarity anddiscourse classification. in**the 2009 Workshop onGraph-based Methods for Natural Language**Processing . 2009.*307. Somasundaran, Swapna and Janyce Wiebe. Recognizing stances in online*debates . in**Meeting of the ACL and the 4th**IJCNLP ofthe AFNLP (ACL-IJCNLP-2009) . 2009.*308. Steyvers, Mark and Thomas L. Griffiths. Probabilistic topic models.Handbookof latent semantic analysis, 2007. 427309. Stone, Philip. The general inquirer: A computer approach to content*analysis. Journal ofRegional Science, 1968. 8*310. Stoyanov, Veselin and Claire Cardie. Partially supervised coreference*resolution for opinion summarization through structured rule learning. in**Proceedings of Conference on EmpiricalMethods in Natural Language**Processing (EMNLP-2006) . 2006.*311. Stoyanov, Veselin and Claire Cardie. Topic identificationfor fine-grained*opinion analysis . in Proceedings of the International Conference on**Computational Linguistics (COLING-2008) . 2008.*312. Strapparava, Carlo and Alessandro Valitutti. WordNet-Affect: an affective*extension of WordNet . in**rnational Conference on**LanguageResources and Evaluation . 2004.*313. Su, Fangzhong andKatja Markert. From words to senses: a case study of*subjectivity recognition . in Proceedings of the 22nd International**Conference on ComputationalLinguistics (COLING-2008). 2008.*314. Su, Fangzhongand Katja Markert. Word sense subjectivity for cross-*lingual lexical substitution . in Proceedingsof Human Language**Technologies: The 2010 Annual Conference of the North American**Chapter ofthe ACL (HLT-NAACL-2010) . 2010.*315. Su, Qi, Xinying Xu, Honglei Guo, Zhili Guo, Xian Wu, Xiaoxun Zhang,Bin Swen, and Zhong Su. Hidden sentiment association in chinese web*opinion mining . in Proceedings of International Conference on World**Wide Web (WWW-2008) . 2008.*316. Taboada, Maite, Julian Brooke, M ilanTofiloski, Kimberly Voll, andManfred Stede. Lexicon-based methods for sentiment analysis.Computational Linguistics, 2011. 37317. Täckström, Oscar and Ryan McDonald.*Discovering fine-grained**sentiment with latent variable structuredprediction models. Advancesin*Information Retrieval, 2011: p. 368-374.318. Täckström, Oscar and Ryan McDonald.

*Semi-supervised latent variable**models for sentence-level sentiment analysis . in**Annual Meeting of the Association for Computational**Linguistics:shortpapers (ACL-2011) . 2011.*319. Takamura, Hiroya, Takashi Inui, and Manabu Okumura. Extracting*semantic orientationsof phrases from dictionary. in**Joint Human Language Technology/North American Chapter of the ACL**Conference (HLT-NAACL-2007) . 2007.*320. Takamura, Hiroya, Takashi Inui, and Manabu Okumura. Extracting*semantic orientations of words using spinmodel. in*


---

<!-- Página 163 -->

*applied tounsupervised classification of reviews . in**Meeting of the Association for Computational Linguistics (ACL-2002).*2002.335. Turney, Peter D. and Micharel L. Littman. Measuringpraise and criticism:*Inference ofsemantic orientation from association. ACM Transactions on*Information Systems, 2003.

*Annual Meeting of the Association for Computational Linguistics (ACL-**2005) . 2005.*321. Takamura, Hiroya, Takashi Inui, and Manabu Okumura. Latent variable*models for semantic orientations of phrases . inProceedings of the**Conference ofthe European Chapter of the Association for Computational**Linguistics (EACL-2006) . 2006.*322. Tan, Songbo, GaoweiWu, Huifeng Tang, and Xueqi Cheng. A novel*scheme for domain-transfer problem in the context ofsentiment analysis. in**Proceeding of the ACM conference on Information and knowledge**management (CIKM-2007) . 2007.*323. Tata, Swati and Barbara DiEugenio. Generating fine-grained reviews of*songs from album reviews . in Proceedings of Annual Meeting of the**Association for Computational Linguistics (ACL-2010). 2010.*324. Tesniere, L. Élements de syntaxe structurale: Préf. de Jean Fourquet1959:C. Klincksieck.325. Titov, Ivan and Ryan McDonald. A jointmodel of textand aspect ratings*for sentiment summarization . in Proceedings of Annual Meeting of the**Association for Computational Linguistics (ACL-2008). 2008.*326. Titov, Ivan and Ryan McDonald. Modeling online reviews with multi-grain*topic models . in**Web (WWW-2008) . 2008.*327. Tokuhisa, Ryoko, Kentaro Inui, and Yuji Matsumoto.*Emotion**classificationusing massive examples extracted from the web. in**Proceedings of the 22nd InternationalConference on Computational**Linguistics (COLING-2008) . 2008.*328. Tong, Richard M. An operational system for detecting and tracking*opinions in on-line discussion . in Proceedings of SIGIR Workshopon**Operational Text Classification . 2001.*329. Toprak, Cigdem, Niklas Jakob, and Iryna Gurevych. Sentence and*expression level annotation of opinions in user-generated discourse. in**Proceedings of the 48th Annual Meeting of the Association for**Computational Linguistics (ACL-2010) . 2010.*330. Tsaparas, Panayiotis, Alexandros Ntoulas, andEvimariaTerzi. Selecting a*Comprehensive Set of Reviews . in Proceedings of the ACM SIGKDD**Conference on Knowledge Discover y and Data Mining (KDD-2011). 2011.*331. Tsur, Oren, Dmitry Davidov, and Ari Rappoport. A Great Catchy Name:*Semi-Supervised Recognitionof Sarcastic Sentences in Online Product**Reviews . in**rnational AAAI Conference on**Weblogsand Social Media (ICWSM-2010) . 2010.*332. Tsur, Oren and Ari Rappoport. Revrank: A fully unsupervised algorithm for*selectingthe most helpful book reviews . in**AAAI Conference on Weblogs an d Social Media (ICWSM-2009). 2009.*333. Tumasjan, Andranik, TimmO. Sprenger, Philipp G. Sandner, and IsabellM. Welpe. Predicting elections with twitter: What 140 characters reveal*about political sentiment . in**ational Conference on**Weblogsand Social Media (ICWSM-2010) . 2010.*334. Turney, Peter D. Thumbs up or thumbs down?: semantic orientation

Sentiment Analysis and Opinion Mining

163


---

<!-- Página 164 -->

Sentiment Analysis and Opinion Mining

164

*International Joint Conference on Natural Language Processing (IJCNLP-**2010) . 2011.*350. Wiebe, Janyce. Identifying subjective characters in narrative. in*Proceedings of the International Conference on Computational Linguistics**(COLING-1990) . 1990.*351. Wiebe, Janyce. Learning subjective adjectives from corpora. in*Proceedings of National Conf. on Artificial Intelligence (AAAI-2000).*2000.352. Wiebe, Janyce. Tracking point of view in narrative. ComputationalLinguistics, 1994. 20

336. Utsumi, Akira. Verbal irony as implicit display of ironic environment:*Distinguishing ironic utterances fromnonirony. Journal of Pragmatics,*2000. 32337. Valitutti, Alessandro, CarloSt rapparava, and OlivieroStock. Developing*affective lexical resources. PsychNology Journal, 2004. 2*338. Velikovich, Leonid, Sasha Blair-Goldensohn, Kerry Hannan, and RyanMcDonald. The viability ofweb-derived polarity lexicons. in*of Annual Conference of the North Am erican Chapter of the Association**for ComputationalLinguistics (HAACL-2010) . 2010.*339. Vrij, Aldert. Detecting lies anddeceit: Pitfalls and opportunities, 2008:Wiley-Interscience.340. Wan, Xiaojun. Co-training for cross-lingual sentiment classification. in*Proceedings of the 47th Annual Meeting of the ACL and the 4th IJCNLP of**the AFNLP (ACL-IJCNLP-2009) . 2009.*341. Wan, Xiaojun. Using bilingual knowledge and ensemble techniques for*unsupervised Chinese sentiment analysis . in**Empirical Methods in Natural Language Processing (EMNLP-2008).*2008.342. Wang, Dong and Yang Liu. A pilot study of opinion summarizationin*conversations . in Proceedings of the 49th Annual Meeting of the**Association for Computational Linguistics (ACL-2011). 2011.*343. Wang, Guan, Sihong Xie, Bing Liu, and Philip S. Yu. Identify Online Store*Review Spammers via So cial Review Graph. ACM Transactions on*Intelligent Systems and Technology, Accepted for publication, 2011.344. Wang, Hongning, Yue Lu, andChengxiangZhai. Latent aspect rating*analysis on review text data: a rating regression approach. in**of ACM SIGKDD International Conference on Knowledge Discovery and**Data Mining (KDD-2010) . 2010.*345. Wang, Tong and Graeme Hirst. Refining the Notions of Depth and Density*in WordNet-based Semantic Similarity Measures. in**Conference on Empirical Methods inNatural Language Processing**(EMNLP-2011) . 2011.*346. Wang, Xiaolong, FuruWei, Xiaohua Liu, Ming Zhou, and Ming Zhang.*Topic sentiment analysis in twitter: agraph-basedhashtag sentiment**classification approach . in Proceeding of the ACM conference on**Information and knowledge management (CIKM-2011). 2011.*347. Wei, Bin and Christopher Pal. Cross lingual adaptation: an experiment on*sentiment classifications . in Proceedings of the ACL 2010 Conference**Short Papers (ACL-2010) . 2010.*348. Wei, Wei and Jon Atle Gulla. Sentiment learning on product reviews via*sentiment ontology tree . in Proceedings of Annual Meeting of the**Association for Computational Linguistics (ACL-2010). 2010.*349. Wen, Miaomiao and Yunfang Wu. Mining the Sentiment Expectation of*Nouns Using Bootstrapping Method . in Proceedings of the 5th*


---

<!-- Página 165 -->

*Empirical Methods in Natural Language Processing (EMNLP-2009).*2009.367. Wu, Yuanbin, QiZhang, Xuanjing Huang, and Lide Wu. Structural*opinionmining for graph-based sentimentrepresentation. in**of the 2011 Conference on Empiri cal Methods in Natural Language**Processing (EMNLP-2011) . 2011.*368. Wu, Yunfang and Miaomiao Wen. Disambiguating dynamic sentiment*ambiguous adjectives . in**International Conference**on ComputationalLinguistics (Coling 2010) . 2010.*

353. Wiebe, Janyce and Rada Mihalcea. Word sense and subjectivity. in*Proceedings of Intl. Conf. on Computational Linguistics and 44th Annual**Meeting ofthe ACL (COLING/ACL-2006) . 2006.*354. Wiebe, Janyce, Rebecca F. Bruce, and Thomas P. O'Hara. Development*anduse ofa gold-standard data set for subjectivity classifications. in**Proceedings of the Association for Computational Linguistics (ACL-1999).*1999.355. Wiebe, Janyce and Ellen Riloff. Creating subjective and objective sentence*classifiers from unannotated texts. Computational Linguistics and*Intelligent Text Processing, 2005: p. 486-497.356. Wiebe, Janyce, Theresa Wilson, Rebecca F. Bruce, Matthew Bell, andMelanie Martin. Learning subjective language. Computational Linguistics,2004. 30357. Wiebe, Janyce, Theresa Wilson, and Claire Cardie. Annotating expressions*of opinions and emotions in language. Language Resources and*Evaluation, 2005. 39358. Wiegand, M. and D. Klakow. Convolution kernels for opinion holder*extraction . in**Annual Conference of the North AmericanChapter of the ACL (HAACL-**2010) . 2010.*359. Williams, Gbolahan K. and Sarabjot Singh Anand. Predicting the polarity*strength of adjectives using wordnet . in Proceedings of the Third**International AAAI Conference on We blogs and Social Media (ICWSM-**2009) . 2009.*360. Wilson, Theresa a nd Stephan Raaijmakers. Comparing word, character,*and phoneme n-grams for subjective utterance recognition. in**of Interspeech . 2008.*361. Wilson, Theresa, Janyce Wiebe, and Paul Hoffmann.*Recognizing**contextual polarity in phras e-level sentiment analysis. in**the Human Language Technology Conference and the Conference on**Empirical Methods in Natural Language Processing (HLT/EMNLP-2005).*2005.362. Wilson, Theresa, Janyce Wiebe, and Rebecca Hwa. Just how mad are you?*Finding strong and weak opinion clauses . in Proceedings ofNational**Conference on Artificial Intelligence (AAAI-2004). 2004.*363. Wilson, Theresa, Janyce Wiebe, and Rebecca Hwa. Recognizing strong*and weak opinion clauses. Computational Intelligence, 2006. 22*99.364. Wu, Guangyu, Derek Greene, Barry Smyth, andPádraig Cunningham.*Distortion as a validation criterion in the identification of suspicious**reviews . in*. 2010.365. Wu, Qion, Songbo Tan, and Xueqi Cheng. Graph ranking for sentiment*transfer . in Proceedings of the ACL-IJCNLP 2009 Conference Short**Papers (ACL-IJCNLP-2009) . 2009.*366. Wu, Yuanbin, Qi Zhang, Xuanjing Huang, and Lide Wu. Phrase*dependencyparsing for opinion mining . in*

Sentiment Analysis and Opinion Mining

165


---

<!-- Página 166 -->

Sentiment Analysis and Opinion Mining

166

369. Xia, Rui and Chengqing Zong. Exploring the use of word relation features*for sentiment classification . in Proceedings of Coling 2010: Poster**Volume . 2010.*370. Xia, Rui and Chengqing Zong. A POS-based ensemble model for cross-*domain sentiment classification . in**Joint Conference on Natural Lan guage Processing (IJCNLP-2010). 2011.*371. Xu, G., X. Meng, and H. Wang. Build Chinese emotion lexicons usinga*graph-based algorithm and multiple resources . in**International Conference on Computational Linguistics (Coling 2010).*2010.372. Yang, Hui, Luo Si, and Jamie Callan. Knowledge transfer and opinion*detection in the TREC2006 blog track . in*. 2006.373. Yang, Seon and Youngjoong Ko. Extracting comparative entities and*predicates from texts using comparative type classification. in**of the 49th Annual Meeting of the Association for Computational**Linguistics (ACL-2011) . 2011.*374. Yano, Tae and Noah A. Smith. What's Worthy of Comment? Content and*Comment Volume in Political Blogs . in**AAAI Conference on Weblogs and Social Media (ICWSM 2010). 2010.*375. Yatani, Koji, Michael Novati, Andrew Trusty, and Khai N. Truong.*Analysis of Adjective-Noun Word Pair Extraction Methods for Online**Review Summarization . in**on Artificial Intelligence (IJCAI-2011) . 2011.*376. Yessenalina, Ainur and Claire Cardie. Compositional Matrix-Space Models*for Sentiment Analysis . in**Methods in Natural Language Processing (EMNLP-2011). 2011.*377. Yessenalina, Ainur, Yejin Choi, and Claire Cardie.*Automatically**generatingannotator rationales to improve sentiment classification. in**Proceedings of the ACL 2010 Conference Short Papers. 2010.*378. Yessenalina, Ainur, Yison Yue, and Claire Cardie. Multi-level Structured*Models for Document-level Sentiment Classification. inProceedings of**Conference on Empirical Methods inNatural Language Processing**(EMNLP-2010) . 2010.*379. Yi, Jeonghee, Tetsuya Nasukawa, Razvan Bunescu, and Wayne Niblack.*Sentiment analyzer: Extracting sentiments about agiven topic using**natural language processing techniques . in Proceedings of IEEE**International Conference on DataMining(ICDM-2003). 2003.*380. Yoshida, Yasuhisa, Tsutomu Hirao, Tomoharu Iwata, Masaaki Nagata, andYuji Matsumoto. Transfer Learning for Multiple-Domain Sentiment*Analysis—Identifying DomainDependent/Independent Word Polarity. in**Proceedings of the Twenty-Fifth AAAI Conference on Artificial Intelligence**(AAAI-2011) . 2011.*381. Yu, Hong and Vasileios Hatzivassiloglou. Towards answering opinion*questions: Separating facts fromopinions and identifying the polarity of**opinion sentences . in**on Empirical Methods in**Natural Language Processing (EMNLP-2003) . 2003.*382. Yu, Jianxing, Zheng-Jun Zha, Meng Wang, and Tat-Seng Chua. Aspect*ranking: identifying important product aspects from online consumer**reviews . in*

*Proceedings of the 49th Annual Meeting of the Association for**Computational Linguistics . 2011.*383. Yu, Jianxing, Zheng-Jun Zha, Meng Wang, KaiWang, and Tat-Seng Chua.*Domain-Assisted Product Aspect Hierarchy Generation: Towards**HierarchicalOrganization of Unstructured Consumer Reviews. in**Proceedings of the Conference on Empirical Methods in Natural Language**Processing (EMNLP-2011) . 2011.*


---

<!-- Página 167 -->

384. Zhai, Zhongwu, Bing Li u, Hua Xu, and Peifa Jia. Clustering Product*Features forOpinion Mining . in Proceedings of ACM International**Conference on Web Searchand DataMining (WSDM-2011). 2011.*385. Zhai, Zhongwu, Bing Li u, Hua Xu, and Peifa Jia. Constrained LDA for*Grouping ProductFeatures inOpinion Mining. inProceedings of**PAKDD-2011 . 2011.*386. Zhai, Zhongwu, Bing Liu, Hua Xu, and Peifa Jia. Grouping Product*Features Using Semi-Supervised Learning withSoft-Constraints. in**Proceedings of International Conference on Computational Linguistics**(COLING-2010) . 2010.*387. Zhai, Zhongwu, Bing Liu, Lei Zhang, Hua Xu, and Peifa Jia. Identifying*evaluative opinions inonline discussions . in*. 2011.388. Zhang, Lei and Bing Liu. Extracting Resource Terms for Sentiment*Analysis . in*. 2011a.389. Zhang, Lei and Bing Liu. Identifying noun product features that imply*opinions . in**Computational Linguistics (shortpaper) (ACL-2011). 2011b.*390. Zhang, Lei, Bing Liu, Suk Hwan Lim, and Eamonn O’Brien-Strain.*Extracting and Ranking Product Features inOpinion Documents. in**Proceedings of International Conference on Computational Linguistics**(COLING-2010) . 2010.*391. Zhang, Min and Xingyao Ye. A generation model to unify topic relevance*and lexicon-based sentiment for opinionretrieval. in**Annual ACM SIGIR International conference on Researchand**Development inInformatio n Retrieval (SIGIR-2008). 2008.*392. Zhang, Wei, Lifeng Jia, Clement Yu, and Weiyi Meng. Improve the*effectiveness of the opinion retrieval and opinion polarity classification. in**Proceedings of ACM International Conference onInformation and**Knowledge Management(CIKM-2008) . 2008.*393. Zhang, Wei and Clement Yu. UIC at TREC 2007 Blog Report, 2007.394. Zhang, Wenbin and Steven Skiena. Trading strategies to exploit blogand*news sentiment . in Proceedings of the International Conference on**Weblogsand Social Media (ICWSM-2010) . 2010.*395. Zhang, Zhu and Balaji Varadarajan. Utility scoring ofproduct reviews. in*Proceedings of ACM International Conference onInformation and**Knowledge Management(CIKM-2006) . 2006.*396. Zhao, Wayne Xin, Jing Jiang, Hongfei Yan, and Xiaoming Li. Jointly*modeling aspects and opinions with a MaxEnt-LDA hybrid. in**of Conference on Empirical Methods inNatural Language Processing**(EMNLP-2010) . 2010.*397. Zhou, Lanjun, Binyang Li, Wei Gao, Zhongyu Wei, and Kam-FaiWong.*Unsupervised discovery of discourse relations for eliminating intra-**sentence polarity ambiguities . in Proceedings of the Conference on**Empirical Methods in Natural Language Processing (EMNLP-2011).*2011.398. Zhou, Lina, Yongmei Shi, and DongsongZhang. A Statistical Language*Modeling Approach to Online Deception Detection. IEEE Transactions on*Knowledge and DataEngineering, 2008: p. 1077-1081.399. Zhou, Shusen, Qingcai Chen, and XiaolongWang.

Sentiment Analysis and Opinion Mining

167

*for semi-supervised sentiment classification . in Proceedings of Coling**2010: Poster Volume . 2010.*400. Zhu, Jingbo, Huizhen Wang, Benjamin K. Tsou, and Muhua Zhu. Multi-*aspect opinionpolling from textual reviews . in Proceedings ofACM**InternationalConference on Information and Knowledge Management**(CIKM-2009) . 2009.* *Active deep networks*


---

<!-- Página 168 -->

Sentiment Analysis and Opinion Mining

168

401. Zhu, Xiaojin and Zoubin Ghahramani. Learning from labeled and*unlabeled data with labelpropagation. School Comput. Sci., Carnegie*Mellon Univ., Pittsburgh, PA, Tech. Rep. CMU-CALD-02-107, 2002.402. Zhuang, Li, Feng Jing, andXiaoyan Zhu. Movie review mining and*summarization . in Proceedings of ACM International Conference on**Information and Knowledge Management(CIKM-2006). 2006.*403. Zirn, Cäcilia, Mathias Niepert, Heiner Stuckenschmidt, and MichaelStrube. Fine-Grained Sentiment Analysis with Structural Features. in*Proceedings ofthe5th International JointConference onNatural**Language Processing (IJCNLP-2011) . 2011.*


---

