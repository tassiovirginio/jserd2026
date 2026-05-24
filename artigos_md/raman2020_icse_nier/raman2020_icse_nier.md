<!-- Página 1 -->

2020 IEEE/ACM 42nd International Conference on Software Engineering: New Ideas and Emerging Results (ICSE-NIER)

### Stress and

### Burnout

### in

### Open

### Source:

### Finding, Understanding,

### and

### Mitigating

### Unhealthy

♥♣♣

### Naveen Raman,

### Minxuan Cao,

### Yulia Tsvetkov,

### Christian Kästner,

♥♣University of Maryland, College Park, USACarnegie Mellon University, USA

**ABSTRACT** Developers fromopen-sourcecommunitieshavereportedhigh stress levelsfromfrequentdemandsforfeaturesandbugfixes and from the sometimes aggressive tone of these demands. Toxic conversations may demotivate and burn out developers, creating challenges for sustainingopen source. We outline a path toward **Figure 1: Excerpt from an issue discussion on GitHub.** finding, understanding,andpossiblymitigatingsuchunhealthy interactions.We take a first step toward finding them, by developing high stakes, many maintainers complain about and demonstrating a measurement instrument (an SVM classifier teractions, sometimes formulated aggressively or from a position of tailored forsoftwareengineering)to detecttoxicdiscussionsin entitlement,as in Figure 1. For developers, this can be draining, GitHubissues. We used our classifier to analyze trends over time “ GitHubnotifications are a constant stream of negativity [...] Reading and in differentGitHubcommunities, finding that toxicity varies through these [...] can be mentally and emotionally exhausting by community and that toxicity decreased between 2012 and 2018. Heightened levels of stress brought on by unhealthy interactions may makeit harderfor projects diverse talent pool.We argue that studying,**1 INTRODUCTION** mitigatingstress and burnout among open-source developers is anSustainingopen-source software is an important and difficult chal- important and understudied research field. There are many impor-lenge. On the one hand, open source has a critical role in our soft- tant research questions, including: How prevalent is self-reportedware infrastructure,affectingdirectlyor indirectlyalmostevery stress and burnout among open-source contributors? What are thesoftware product and facet of modern life. Some argue that open causes of stress in open-source? How do they compare to other worksourceprovides just as important infrastructure as roads and bridges environments?When is stress most damaging to open-source con-do for the economy, yet its importance,and our dependenceon tributorsand who is most at risk? What interventions are effective?it, are often not recognized9[ On the other hand, open-source Our vision is to answer such questions empirically using mixedsoftware,as allneeds to be maintained. Continuous effort methods, relying heavily on public trace data. The advantages ofis needed to fix bugs and vulnerabilities and to evolve the software such a computational approach are manifold. First, analyzing traceto accommodate new requirements to stay relevant. How to sustain data avoids the recall errors and response biases typical of surveyssuch effort, be it from volunteers or through explicit support from and interviews. Second, it makes the ethical choice of avoiding tocorporations, is an open, controversially discussed problem. burden already potentially stressed individuals by asking them toOpen-sourcepractitioners have been raising awareness of recall or envision stressful interactions. Third, analyzing large, mul-and burnout.Community members are openly worried about men- tidimensional samples offers statistical opportunities for modelingtal and physical well-being of contributors and about exploitation and hypothesis testing that are typically not present in smaller andof volunteers, including self-exploitation with the vague promise simplerdata sets from experiments, surveys, or interviews. Last butof building a profile that could help them find a better job, as evi- not least, operationalizingdenced by many recent blog posts, talks, podcasts, even entire con- data paves the way to develop automated, non-invasive measuresferences[e.g.,5,17,25,27,37]. A common theme is that open-source and models to help identify contributors that show signs of stressmaintainers feel overwhelmed by the number of requests they re- and projects at risk, as well as to design automated interventions.ceive ( e.g., bug reports,supportrequests).In addition,the trans- In this paper, we take a first step towards realizing this vision,parency on social coding websites likeGitHubraises stakes [] in by developing and demonstrating a critical research instrument (athat mistakes are visible and can affect a contributor’s reputation. classifier)to detect toxic language in open-source issue discussions.Even more important,more than just volume of requestsand Toxiclanguage in open source can manifest in multiple ways, includ- ing hate speech and microaggressions found also elsewhere online Permission ( e.g. ,Youtube), but also through open-source-specific displays of en-classroom titlementand urgency related to timing expectations as in Figure 1.for onOur work builds on prior research on detecting toxic language— author(s) from hate speechto microaggressions—inrepublish, and/orProcessing (NLP)community ICSE-NIER’20,tributions. First, we show that toxic © 2020 English)can be identified using a combination ofACM [https://doi.org/10.1145/3377816.3381732](https://doi.org/10.1145/3377816.3381732)tors of negative sentiment, anger, impoliteness, and toxicity. Second,

57

### Toward

♣

### Bogdan Vasilescu

to attract,

open-source

[ , 12, 32], making GitHubissue discussions (in

### Interactions

♣

the tone of these in-

e.g. ,

” 25 ].

include,and retaina understanding,and

stress factors using trace

the Natural Language twomaincon-

detec-


---

<!-- Página 2 -->

ICSE-NIER’20,

**Table 1: Features used by our classifier.**we show that classificationaccuracy can be further improved by domainadaptation, tailoring our detector to the context of software- **Feature**engineering discussions. We demonstrate the potential of our clas- sifier withthreepreliminaryempiricalstudies.OurreplicationLength Frequencypackage is at [https://github.com/CMUSTRUDEL/toxicity-detector](https://github.com/CMUSTRUDEL/toxicity-detector). Politeness Toxicity Subjectivity,As**2 RELATED**WORKTextBlob SentimentAsWebuild on prior work that (a) has studied motivations of develop- library ers and users to see why conflict might arise and (b) has developedAnger NLP tools to detect different forms of toxicity incontexts.

**Volunteering,**motivations, and conflicts in open source.Re- **Data. With a few exceptions from blog posts, online discussions,** searchers have extensively studied motivations of developers con- and interviews [e.g.,5], no labeled data for toxic language in open tributing toopensource[e.g.,18 ,24 ], revealingamultitudeof source exists.We curateda datasetmanuallyand incrementally. intrinsic and extrinsic reasons, such as working on projects they Toxicinteractions seem to be rare but very stressful; given the low enjoy or find useful. Despite increasing commercialization and pro- rate, randomsamplingseemedineffective,soweidentifiedtwo fessionalization, manycontributorsarevolunteers19[ ,38 ]. Yet, different strategies. First, we queried theGitHubAPI to identify among the manyreasonsto contributeto opensource, building issue threadsthathadbeenlockedas“tooheated”.Amongthe one’sprofessional reputation and signalingskills to potential 118,629 GitHub projects with any issues (accordingto our copy employers are common ones [28]. ofGHTorrent[14]), wefound294805 lockedissuesofwhich At the same time, open source is broadlyused in commercial 654 whereexplicitlylockedas “tooheated”(providinga reason projects, even for mission-critical components. Only a small num- for lockingisaveryrecentGitHubfeature). Issuediscussions ber of users of an open-source project contribute to that19 ].[ locked as too heated often contain toxic behavior that was called Given this asymmetry, high stakes, and the lack of a contractual out, e.g.,“I’m locking the conversation. Inappropriate/unprofessional relationship,users that demand changes from the project, be it addi- conduct will not be tolerated. ” We manually reviewed all the ones tional features, specific changes (e.g.,perceived bugs or limitations), written in English, labeling their comments as either toxic or not or betterdocumentation,maybeperceivedentitledas[25 ,26 ]. (by extrapolating,wealsolabeledtheissueasa wholeastoxic, Within developer communities, there have been reports of insults if at least one commentwas toxic). Second,inspiredby patterns and attacks [,21]. Beyond concerns for the maintainer’s well being, found earlier, we searched throughGHTorrentissue comments toxic interactions are concerning for recuiting contributors [34]. for reactions, by maintainers,containingthe word ‘attitude’ ( e.g., **Detecting Toxicity. The NLP community has achieved significant**Figure 1) andmanuallylabeledthem.In theend,usingthetwo advances at detecting different forms of negativity and toxicity instrategieswe compiled a data set of 386 issue threads, 167 of which text,e.g., in movie reviews or social-media interactions, on whichcontain at least one toxic comment each, manually labelled. we build for our own toxicity detection instrument.After labelling, we split our data in two, half for training and half In the software-engineering community,sentiment analysis[]for testing. To increase the representativeness (our previous sam- is a popular such technique, used to analyze, among others, issuepling was non-random) and the realism (toxic issues are relatively discussions, pull requests, email messages, and forum posts [e.g.,rare) of our training data, we further manually labelled 300 random 4 , 16 ]. Similar approaches have been used to detect anger in issueissue threads, none of which were toxic, adding 225 of them (written reports[ 13 ]. Software engineering research has shown though thatin English, having at least one comment each) to the training set. a sentiment-analysis classifier for software engineering tasks needs **Classifier Features. The domain-specificity**of toxicityin open- to betrainedspecificallyonsoftwareengineeringcontent22 ],[ source suggests that a custom approach to classification is needed. because traditionalclassifiersassignnegativeweightstomany Since we are limited by the relatively small amount of labelled data technical phrases such as “kill a process.” available for training,based on our review of the NLP literature There is also related work on detecting toxicity in language, in- we attempt to capture open-sourcetoxicity using a combination cluding hate speech, abuse, microagressions, and harassment11 [ of general pre-trained sentiment analysis, politeness, and abusive 36 ]. For example,hate-speechdetectionspecificallylooks for strong, language detectors; for example, we use Google’s pre-trained Per- toxic interactions [], trained on comments in online forums8 , 31[ ]. spectiveAPI for detecting “rude, disrespectful, or unreasonable com- As for sentiment analysis, we expect that we will have to adjust exist- ments”in non-software-specific online discussions (e.g.,Wikipedia). ing classifiers for the software engineering context, where toxic in- Our full set of features is described in Table 1. teractionsmay be less direct, related to technical issues, or to timing. task is to assigntoxicaor non-toxic**Training. Our classification** label toagivenissuecomment(andbyextensiontotheissue). **3 DATA**AND METHODSTo this end, we trained an SVM classifier. SVMs are often used to At a highlevel,we manuallylabeleda sampleGitHubofissueclassify text [], they tend to perform on par with other statisti- commentsand trained a classifier to identify toxic comments, usingcal classifiers and they outperform state-of-the-art neural network features inspired by prior research on detecting toxic language inclassifiers in low-resource training data scenarios like ours. online communities. This section details the individual steps.Weused 10-fold nested cross validation to learn hyperparameters

58


---

<!-- Página 3 -->

### 1%

### 0%

Toward

and evaluate the model10[ ]. Because of the imbalance in the train- ing data, for each split, we adjusted the class weights, with a ratio 𝑟between non-toxic and toxic examples, where𝑟is a hyperparam- eter.We grid searched over SVM hyperparameters𝛾= { 1 ,2,2.5,3}, Toxic␣iss./all␣iss. 𝐶= { 0 .01,0.05,0.1,0.5,1,10}; and𝑟= { 1 ,1.5,1.75,2,2.25}.

### 2012

**Tuning. A commonly recognized risk with NLP models is poor per-** formanceoutside of the context where they have been trained22 ]. [**Figure 2: Rate of toxic issues over time decreases gradually** For example, ‘abort’ and ‘kill’ have negative connotations in general English, but are mostly neutral in software engineering,e.g. , when referring to processes, leading to inaccurate predictions. Toalleviate this risk, we identified, using log odds with Dirichlet

### Noncorporate

### Corporate

### Rate␣of␣toxic␣issues

prior [29], words that are significantly overrepresented in software engineering language compared to general English, and replaced those words with a neutral filler word, so that the sentence struc- ture would not be modified.Specifically, log odds with Dirichlet prior assumes words follow a Dirichlet distribution, and uses the distribution of software-engineeringwords along with the distri-

### Ruby

### Javascript

### Haskell

### Rate␣of␣toxic␣issues

bution of regular English words to estimate a confidence level for whethera word is software-engineering-specific; we use the typical **Figure 3:**Corporateprojectsarelesstoxicthannon-𝛼<0 . 05 cutoff. Our softwareengineeringcorpuscomesfrom a **corporate projects; there are differences between languages.**random sampleof10KGitHubissues, andourgenericEnglish corpus comes from the Python librarywordfreq[33], which uses sevencorpora, including Wikipedia. For computational reasons, we apply this correction as a post-processing step, both at training and**Toxicity**Over Time.Weperceive the public conversations about inference time, and only for commentsinitially predictedby ourtoxicity,stress, and burnout in open source as a recent phenomena. classifier as toxic, after which we re-compute all the features andWeare interested to see whether this public attention corresponds re-classify the now-modified comment.with a measurable increase in toxic interactions. To that end, we use our instrument to automatically classify issue discussions in a lon-**Evaluation.**Toquantify model accuracy during cross-validation, gitudinal study. We classify all the 1 732 124 issuesGHTorrentinwe use the𝑓score,because of the imbalance of our dataset and to0 . from the second Monday of each month between 2012–2018 (thisvalue precision above recall. Of the different feature combinations sampling strategy accounts for confoundssuch as the day of thewe experimented with, our model performed best when using Po- week or time of the month). As expected, toxic issues are rare, withliteness,Perspective, and after the tuning and post-processing steps about 6 for every 1 000 issues. The rate of toxic issues decreasesdescribed above. Our best classifier had a precision0ofand a over time, as plotted in Figure 2. While we leave a deeper analysisrecall of 042 . Featureablationexperimentsshow that removing of reasons for future work, we suspect that increased awareness offeaturesfrom our model decreasesperformance, and adding the issue may both cause a lower frequency of toxic interactionsfeatures to our model does not improve performance. and more public discussions about the remaining cases.On a held-out test set (half the labelled data), our model achieves 75 % precision and 35 % recall. We additionally tested our classifier**Corporate vs.**Non-Corporate. Suspecting thattoxicityistar- on 100,000 randomly sampledGitHubissues. We manually labeledgeted more at volunteers, we explore whether corporate-run projects 100 randomly selected issues that were predicted as toxic to estimateare lessexposedtotoxicissuediscussionsthannon-corporate the precision of the classifier. We found that the classifier achievedprojects. Specifically, we selected the 50 projects with the largest 50 % precision on the random issues. This indicates that the classifiernumber of employees from corporations actively contributing (us- performsreasonably well outside of the training and validation sets.ing email accounts to detect corporate affiliations) and selected the Some noise is acceptablefor studying toxicity trends in the wild,top 50 projects by number of stars not associated with a corpora- assuming that wrong classifications are randomly distributed.tion. We then labeled 949 739 issues from these projects using our classifier.As shown in Figure 3, our results indicate that the rate of toxic issue discussions is substantially lower for corporate projects**4 PRELIMINARY**EMPIRICAL STUDIES (statistically significant,Wilcoxon𝑝< . 001). We suspect that theWhile our long-term agenda is much broader, we conducted three increasingnumber of less toxic corporate projects onmaypreliminary studies of toxicity in open-source projects to demon- lead to the overall reduced rate of toxic interactions, but again, westrate possibleusesofourmeasurementinstrument.We study leave deeper explorations to future work.(1) whethertoxic interactionsin issue discussionshave changed over time, (2) whethercorporateand non-corporateprojectsarebetween commu-**Toxicity**by Community.Cultural differences affected differently, and (3) whether communities around differentnities [2] may also affect the degree of toxic interactions.We use programming languages are affected differently. We report initialas a proxyforcommunitiesandclassi- llobservations,but leave a deeperexplorationof these issues ( e.g., fied all 872 565from the 30 most popular projects in each oflllll lll ll lll ll lll l l l l ll lll l l l l lll ll llll l lll the influence of a community’s culture) for future work.7 languages. Our findings (Figure 3) suggest differences in toxicity

59

### Python

### Lua

### R

### 0%

### 1%


---

<!-- Página 4 -->

ICSE-NIER’20,

### among communities, with R having the lowest rate of toxic discus-

GitHub:Proc.In CSCW, pages

### sions, Ruby the highest, and Lua the widest variance. Differences

[7]Cristian

### among communities and projects suggests that future research can

and toProc., pages

### study the role of community values, and the effectiveness of existing

[8]Nemanja

### practices

### and interventions in natural experiments, where possible.

and Proc., pages

### Threats to Validity.

### Our study is limited to issue discussions on

[9]Nadia

### GitHubtracked inGHTorrent. It does not include other forms

ture.

### of communication,

### such

### as forums,

### mailing

### lists,

### or face-to-face

[10]NIR, 21(5):14–15, [11]Darja

### interactions at conferences.

### While we evaluated

### our classifier

### in

Waseem,Proc.

### Section 3, due to the large number of issues analyzed in our study,

Online, 2018. [12]Paula

### we did not verify all classification results. Although we have little

inACM, 51(4):85,

### reason to expect systematic bias, there is a risk that our classifier

[13]Daviti

### may perform differently in different subpopulations.

Anger, pages

### Additionally, our classifier has relatively low precision on ran-

[14]GeorgiosProc., pages

### dom issues, and low recall on the held-out test set. This might be a

233–236,

### result of overfitting to the training set. A larger

### and vali-[15]

Joshua verbalProc., pages

### dation set should be used to reduce these issues. Larger validation

[16]Emitza

### sets allow for more fine tuning of parameters, which could make

commentsProc., pages 2014.

### the classifier more accurate. Data with more varied sources could

[17]Eran

### also improve the classifier.

hueniverse.com/86d1fcf3e353. [18]Guido developers

## 5 CONCLUSION

theResearch, 32(7):1159–1177,

### We

### argue that developer stress and burnout are important threats to

Eric[19] collective”Organization, 14(2):209–223,

### open-source sustainability, and suggest a larger research program

[20]Clayton

### to find, understand, and mitigate unhealthy interactions. As a key

sentiment, 2014.

### component

### of such a research program, we report on initial steps to[21]

Carlos communities:

### detect toxic interactions in

### GitHubissue discussions, which seem

In Proc., pages

### particularly stressful

### to

### maintainers.

### We design

### a

### classifier

### and

[22] On

### demonstrate its utility with three preliminary studies. Our results

research. Empirical, 22(5):2543–2584,

### show promise, and could be used to inform the design of automated,

[23]Speech. Pearson,

### non-invasive measures and models to both help identify contrib-

[24]Sandeep developers. Knowledge,, 18(4):17–39,

### utors and projects exposed to higher levels of toxicity (and likely

[25]NolanWhat, March

### also stress), as well as to intervene to avoid such toxic comments in

Blog

### the first place ( e.g., by flagging them for moderation before being

[26]Jan learned

### posted). We are excited to see such systems developed, evaluated,

[27]Pia

### and deployed in the near future.

sustainers [28]Career, pages

### Acknowledgements. Raman was supported

### through CMU’s Re-

[29]Burt

### search Experiences

### for Undergraduates

### in Software Engineering.

feature Political, 16(4):372–403,

### The researchers

### were supported

### in part by awards

### from the Na-

[30]BoFoundations

### tional Science Foundation and the Alfred P. Sloan Foundation. Many

and, 2(1–2):1–135,

### thanks to collaborators

### for useful suggestions:

### Carolyn Rose and

[31]Haji webFirst

### Jim Herbsleb at CMU; Julia Ferraioli, Erin McKean, and Emerson

Text, 2016.

### Murphy-Hill at Google.

[32]Anna naturalProc. for, pages

## REFERENCES

[33]Robert Anonymous.[1]v1. com/pieces/leaving-toxic-open-source-communities.Igor[34] [2]ChristopherDavid tocomersInformation, tems.Proc., pages59:67–85, [3]Luke[35]Yla gressionsLiwcJournal posts.Proc., 2019.Psychology, 29(1):24–54, [4]FabioZeerak[36] mentEmpirical,Proc.. ACL, 23(3):1352–1382,[37]Tim [5]Bretttimrwood/moment-endof-term-522d8965689. call[38]Frances [6]Lauraodo.806811.

60


---

