<!-- Página 1 -->

### A Survey

### on

### Large

### Language

### Model

### (LLM)

### Security

### and

### Privacy:

### The Good,

### the

### Bad,

### and

### the

### Ugly

## Yifan

## Yao, Jinhao

## Duan, Kaidi

## Xu , Yuanfang

## Cai , Zhibo

## Sun and

## Yue

## Zhang

*a**Drexel*

A R T I C L E IN F OA B S T R A C T

*Keywords*:Large Largeunderstanding Security,tion Attacks,various also potential vacy. threats literature “The We vulnerability methods. to For hindered requires and

LLMs aregainingpopularitywithinthesecuritycom-

## 1. Introduction

munity.As of February 2023, a research study reported that A large language model is thewith massive GPT-3 uncovered 213 security vulnerabilities (only 4 turned parameters thatundergoespretrainingtasks(e.g.,maskedout to be false positives) [141] in a code repository. In con- language modelingandautoregressiveprediction)toun-trast, one of the leading commercial tools in the market de- derstand andprocesshumanlanguage,bymodelingthetected only 99 vulnerabilities. More recently, several LLM- contextualized textsemanticsandprobabilitiesfromlargepowered security papers have emerged in prestigious confer- amounts oftextdata.AcapableLLMshouldhavefour ences. For instance, in IEEE S&P 2023, Hammond Pearce et key features[323 ]: (i)profoundcomprehensionofnatural al. [ 211] conducted a comprehensive investigation employ- language context;(ii)abilitytogeneratehuman-liketext;ing various commercially available LLMs, evaluating them (iii) contextual awareness, especially in knowledge-intensiveacross synthetic,hand-crafted,andreal-world securitybug domains; (iv)stronginstruction-followingabilitywhichisscenarios. The results are promising, as LLMs successfully useful for problem-solving and decision-making.addressed all synthetic and hand-crafted scenarios. In NDSS There areanumberofLLMsthatweredeveloped and 2024, atoolnamedFuzz4All[313 ] showcasedtheuseof released in2023,gainingsignificantpopularity.NotableLLMs forinputgenerationandmutation,accompaniedby examples includeOpenAI’s*ChatGPT*[ 203 ], MetaAI’san innovative autoprompting technique and fuzzing loop. *LLaMA*[ 4 ], andDatabricks’Dolly2.0[50 ]. Forinstance, arXiv:2312.02003v3 [cs.CR] 20 Mar 2024These remarkable initial attempts prompt us to delve into ChatGPT alone boasts a user base of over 180 million [69].three crucial security-related research questions: LLMs now offer a wide range of versatile applications across various domains. Specifically, they not only provide techni-•***RQ1 . How****do**LLMs**make**a**positive**impact**on**se-* cal support to domains directly related to language process-*curity and privacy across diverse domains, and what* ing (e.g., search engines [352, 13], customer support [259],*advantages do they offer to the security community?* translation [327 , 138]) butalsofindutilityinmoregeneral •***RQ2 . What potential risks and threats emerge from the***scenarios suchascodegeneration[118 ], healthcare[274 ], *utilization of LLMs within the realm of cybersecurity?*finance [310 ], andeducation[186 ]. Thisshowcasestheir adaptability andpotentialtostreamlinelanguage-related •***RQ3 . What****vulnerabilities**and**weaknesses**within* tasks across diverse industries and contexts.*LLMs, and how to defend against those threats?* [yy566@drexel.edu](mailto:yy566@drexel.edu)(Y.[jd3734@drexel.edu](mailto:jd3734@drexel.edu)(J. [kx46@drexel.edu](mailto:kx46@drexel.edu)(K.[yfcai@cs.drexel.edu](mailto:yfcai@cs.drexel.edu)(Y.[zs384@drexel.edu](mailto:zs384@drexel.edu) **Findings.To comprehensively address these**questions, we(Z.[yz899@drexel.edu](mailto:yz899@drexel.edu)(Y. ORCID(s):conducted ameticulousliteraturereviewandassembled a collectionof281paperspertainingtotheintersection

Yifan Yao etal.: Preprint submitted to ElsevierPage 1 of 24


---

![Image 1 from page 1](data:image/jpeg;base64,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)



---

<!-- Página 2 -->

A SurveyonLarge LanguageModel(LLM)Security and

of LLMswithsecurityandprivacy. We categorizedthese papers into three distinct groups: those highlighting security- beneficial applications(i.e.,thegood),thoseexploringap- plications thatcouldpotentiallyexertadverseimpactson security (i.e.,thebad),andthosefocusingonthediscus- sion of securityvulnerabilities (alongside potential defense mechanisms) withinLLMs(i.e.,theugly).Tobemore specific:

•**The Good (§4):**LLMs have a predominantly positive impact on the security community, as indicated by the most significantnumberofpapersdedicatedtoen- hancing security. Specifically, LLMs have made con- tributions to both code security and dataand privacy.Inthecontextofcodesecurity,LLMshave **Contributions.Our work makes a dual contribution.**been usedforthewholelifecycleofthecode(e.g., we aresecure coding,testcasegeneration,vulnerablecode and privacy. We delvedetection, malicious codeand code fixing). LLMs onIn datasecurityandprivacy,LLMshavebeenap- abilities inplied to ensure data integrity, data confidentiality, data nisms. Otherreliability,anddatatraceability.Meanwhile,Com- pects, such as beneficial applications, offensivepared tostate-of-the-artmethods,mostresearchers vulnerabilities, orfound LLM-basedmethodstooutperformtraditional our survey isapproaches. to security •**The Bad (§5):**LLMs also have offensive applicationsmade several against securityandprivacy. We categorizedtheat-search reveals tacks intofivegroups:hardware-levelattacks(e.g.,negatively side-channel attacks),OS-level attacks(e.g.,analyz-that most ing informationfromoperatingsystems),software-of-the-art methods level attacks(e.g.,creatingmalware),network-leveldata. Concurrently, it becomes evident that user-level attacks (e.g., network phishing), and user-levelare the (e.g., misinformation,socialengineering,scientificreasoning abilities exhibited by LLMs. misconduct). User-level attacks, with32papers,are **Roadmap.The rest of the paper is organized as follows. We**the mostprevalentduetoLLMs’human-likerea- begin withsoning abilities.Thoseattacks threatenbothsecurity the overview of(e.g., malware attacks) and privacysocial engi- impacts of employing LLMs. §5 discusses the negative im-neering). Nowadays, LLMslackdirectaccesstoOS pacts on security and privacy. In §6, we discuss the prevalentand hardware-level functions. The potential threats of threats, vulnerabilities associated with LLMs as well as theLLMs could escalate if they gain such access. countermeasures to •**The Ugly**(§**6 ):**Weexplorethevulnerabilitiesandin other defenses inLLMs,categorizingvulnerabilitiesintoconclude the paper in §9. two maingroups:AIModelInherentVulnerabili- ties (e.g.,datapoisoning,backdoorattacks,training **2. Background**data extraction)andNon-AIModelInherentVul- nerabilities (e.g.,remotecodeexecution,promptin-**2.1. Large** jection, sidechannels).TheseattacksposeadualLarge Language Models (LLMs) [347] represents an evolu- threat, encompassingbothsecurityconcerns(e.g.,tion from language models. Initially, remote codeexecutionattacks)andprivacyissuesstatistical in (e.g., data extraction). Defenses for LLMs are dividedtational linguistics. into strategies placed in the architecture, and appliedicantly increased during thetrainingandinferencephases.Trainingthe use phase defensesinvolvecorporacleaning,andopti-training techniques is pivotal in areas such as AI for science, mization methods,whileinferencephasedefenseslogical reasoning, and embodied AI. These models undergo include instructionpre-processing,maliciousdetec-extensive training on tion, andgeneration post-processing. Thesedefensesduce text collectively aimtoenhancethesecurity,robustness,LLMs are endowed with hundreds of billions, or even more,

Yifan Yao etal.: Preprint submitted to Elsevier

Privacy:TheGood,theBad,andUgly

and ethical alignment of LLMs. We found that model extraction, parameterandsimilarattacks havereceivedlimitedresearchattention,remaining primarily theoreticalwithminimalpracticalexplo- ration. The vast scale of LLM parameters makes tradi- tional approaches less effective, and the confidential- ity of powerful LLMs further shields them from con- ventional attacks.StrictcensorshipofLLMoutputs challenges evenblack-boxMLattacks.Meanwhile, research on the impact of model architecture on LLM safety isscarce,partlyduetohighcomputational costs. Safe instructiontuning,arecentdevelopment, requires further investigation.

First, pioneerssummarizingtherole ofLLMsinsecurity deeplyintothepositiveimpactsof security, theirpotential risksandthreats,vulner- LLMs,andthecorrespondingdefensemecha- surveys may focus ononeortwo specificas-

defenses.Tothebestofourknowledge, thefirsttocover allthreekey aspectsrelated andprivacyfor thefirsttime.Second,wehave interestingdiscoveries.Forinstance,ourre- thatLLMscontributemorepositivelythan tosecurityandprivacy.Moreover,weobserve researchersconcurthatLLMsoutperformstate- whenemployedforsecuringcodeor

mostprevalent,largelyowingtothehuman-like

abriefintroductiontoLLMin§2 . §3 presents ourwork. In§4 , we explore thebeneficial

mitigatetheserisks.§7 discussLLMs securityrelatedtopicsandpossibledirections.We

Language Models (LLMs)

models were natureandlaidthegroundworkforcompu- Theadventoftransformershassignif- theirscale.Thisexpansion,alongwith ofextensivetrainingcorporaandadvancedpre-

vast datasetsto comprehend andpro- thatcloselymimicshumanlanguage.Typically,

Page 2of24


---

<!-- Página 3 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

parameters, honedthroughtheprocessingofmassivetex-Table1 tual data. They have spearheaded substantial advancementsComparison ofPopular LLMs in therealmofNaturalLanguageProcessing(NLP)[82 ]Model gpt-464 ]✗1.7T✗and findapplicationsinamultitudeoffields(e.g.,risk gpt-3.5-turbo✗175B✗ assessment [202 ], programming[26 ], vulnerabilitydetec-gpt-324 ]✗175B✗ cohere-medium170 ]✗6B✓tion [118 ], medicaltextanalysis[274 ], andsearchengine cohere-large170 ]✗13B✓ optimization [13]).cohere-xlarge170 ]✗52B✓ BERT61 ]✓340M✓Based onYang’sstudy[323 ], anLLMshouldhave T5225 ]✓11B✓ at leastfourkeyfeatures.First,anLLMshoulddemon-PaLM198 ]✓540B✓ LLaMA4 ]✓65B✓strate adeepunderstandingandinterpretationofnatural CTRL229 ]✓1.6B✓ language text, enabling it to extract information and performDolly50 ]✓12B✓ various language-relatedtasks(e.g.,translation).Second, it shouldhavethecapacitytogeneratehuman-liketext pinpointing gapsinourcollectiveknowledge.Whileitis(e.g., completingsentences,composingparagraphs,and true thatLLMswieldmultifacetedapplicationsextendingeven writing articles)when prompted. Third, LLMs should beyond securityconsiderations(e.g.,socialandfinancialexhibit contextualawarenessbyconsideringfactorssuch impacts), ourprimaryfocus remainssteadfastly onmattersas domainexpertise,aqualityreferredtoas“Knowledge- of securityandprivacy.Moreover,itisnoteworthythatintensive”. Fourth,thesemodelsshouldexcelinproblem- GPT modelshaveattainedsignificantprominencewithinsolving and decision-making, leveraging information this landscape.Consequently,whendelvingintospecifictext passagestomaketheminvaluablefortaskssuchas content andexamples,weaimtoemployGPTmodelsasinformation retrieval and question-answering systems. illustrative benchmarks. **2.2. Comparison**of Popular LLMs **3.2. The**Research QuestionsAs showninTable1[276 , 235], thereisadiversityof LLMs havecarriedprofoundimplicationsacrossdiverseproviders forlanguagemodels,includingindustryleaders domains. However, it is essential to recognize that,as withsuch asOpenAI,Google,MetaAI,andemergingplayers any powerfultechnology, LLMsbearasignificantrespon-such as Anthropic and Cohere. The release dates span from Ourpaperdelves deeplyintothemultifaceted role2018 to 2023, showcasing the rapid development and evolu-sibility. of LLMsinthecontext ofsecurityandprivacy. We intendtion of language models in recent years. Newersuch theirpositivecontributionstothesedomains,as “gpt-4” have emerged in 2023, highlighting the ongoingto scrutinize explore the potential threats they may engender, and uncoverinnovation inthisfield.Whilemostofthemodelsarenot the vulnerabilities that could compromise their integrity. Toopen-source, it is interesting to note that models like BERT, T5, PaLM, LLaMA, and CTRL are open-source, which canaccomplish this, our study will conduct a thorough literature review centered around three pivotal research questions:facilitate community-driven development andapplications. Larger modelstendtohavemoreparameters,potentially •**The Good (§4):**How do LLMs positively contributeindicating increasedcapabilitiesbutalsogreatercomputa- to security and privacy in various domains, and whattional demands.Forexample,“PaLM”standsoutwitha are thepotentialbenefitstheybringtothesecuritymassive 540billionparameters.Itcanalsobeobserved community?that LLMstendtohave moreparameters,potentiallyindi- cating increased capabilities but also greater computational •**The Bad (§5):**What are the potential risks and threats demands. The“*Tunability*” columnsuggests whetherthese associated with the use of LLMs in the context of cy- models can be fine-tuned for specific tasks. In other words, bersecurity? Specifically, how can LLMs be used for it ispossibletotakealarge,pre-trainedlanguagemodel malicious purposes,andwhattypesofcyberattacks and adjust its parameters and training on a smaller, domain- can be facilitated or amplified using LLMs? specific datasettomakeitperformbetteronaparticular task. For instance, with tunability, one can fine-tune BERT•**The Ugly (§6):**What vulnerabilities and weaknesses on a dataset of movie reviews to make it highly effective atexist withinLLMs,andhow dothesevulnerabilities sentiment analysis.pose a threat to security and privacy?

Motivated by these questions, we conducted a search on **3. Overview**Google Scholar and compiled papers related to security and privacy involving LLMs.AsshowninFigure1, wegath-**3.1. Scope** ered atotalof83“good”papersthathighlightthepositiveOur paper endeavors to conduct a thorough literature review, contributions of LLMs to security and privacy. Additionally,with theobjectiveofcollatingandscrutinizingexisting we identified 54 “bad” papers, in which attackers exploitedresearch and studies about the realms of security and privacy LLMs totargetusers,and144“ugly”papers,inwhichin thecontextofLLMs.Theeffortisgearedtowards both authors discovered vulnerabilities within LLMs. Most of theestablishing thecurrentstateoftheartinthisdomainand

Yifan Yao etal.: Preprint submitted to ElsevierPage 3of24


---

<!-- Página 4 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

**4.1. LLMs**for Code Security

As shown in Table 2, LLMs have access to a vast repository of codesnippetsandexamplesspanningvariousprogram- ming languages and domains. They leverage their advanced language understanding and contextual analysis capabilities to thoroughlyexaminecodeandcode-relatedtext.More specifically,LLMscanplayapivotalrolethroughoutthe entire code security lifecycle, including coding (C), test case generation (TCG), execution, and monitoring (RE).

**Secure Coding (C).We**first discuss the use of LLMs in the context of secure code programming [75] (or generation [63, 285 , 199 , 90]). Sandoval et al. [234] conducted a user study (58 users) to assess the security implications of LLMs, par- ticularly OpenAICodex,ascodeassistantsfor developers. They evaluated code written by student programmers whenGood: 83 assisted byLLMsandfoundthatparticipantsby LLMs did not introduce new securityrisks:the AI-assisted group producedcriticalsecuritybugsataratenogreater FebFigure 1:An overviewofourcollectedpapers.than 10% higher than the control group (non-assisted). He et Ugly: 144al. [ 98, 99] focused on enhancing the security of code gener-Jan ated by LLMs. They proposed a novel method calledSVEN, which leveragescontinuouspromptstocontrolLLMsinpapers were published in 2023, with only 82 of them released generating securecode.Withthismethod,thesuccessratein between2007and2022.Notably,thereisaconsistent Aprimprovedfrom59.1%to92.3%whenusingtheCodeGenupward trend in the number of papers released each month, MarLM. Mohammed et al. introduceSALLM[254], a frameworkwith Octoberreachingitspeak,boastingthehighestnum- Bad: 54consisting ofanew security-focused dataset,anevaluationber ofpaperspublished(38intotal,accountingfor Mayenvironment, and novel metrics for systematically assessing15.97% ofallthecollectedpapers).Itisconceivablethat LLMs’ ability to generate secure code. Madhav et al. [197]more security-relatedLLMpaperswillbepublishedinthe evaluate the security aspects of code generation processes onnear future. the ChatGPT platform, specifically in the hardware domain. **Finding I.**In termsofsecurity-relatedapplicationsThey explore the strategies that a designer can employ to en- (i.e., the“good”andthe“bad”parts),itisevidentthatable ChatGPT to provide secure hardware code generation. Junthe majorityofresearchersareinclinedtowardsusing Jul**Test**CaseGenerating(TCG).Several papers[33 , 6, 238,LLMs tobolsterthesecuritycommunity,suchasin 316 , 156, 253, 335] discusstheutilizationofLLMsforvulnerability detectionandsecuritytestgeneration, Auggenerating test cases, with our particular emphasis on thosedespite thepresenceofsomevulnerabilitiesinLLMs Decaddressing security implications. Zhang et al. [343] demon-at thisstage.TherearerelativelyfewresearchersNov strated the use of ChatGPT-4.0 for generating security testswho employLLMsastoolsforconductingattacks. to assesstheimpactofvulnerablelibrarydependenciesonIn summary,LLMscontributemorepositivelythanOct software applications. They found that LLMs could success-negativelyto the security community. Sepfully generate teststhatdemonstratedvarioussupply chain attacks, outperforming existing security test generators. This Sepapproach resultedin24successfulattacksacross55appli-**4. Positive**Impacts on Securityand PrivacyOctcations. Similarly,Libro[136], a framework that uses LLMs In this section, we explore the beneficial impacts of employ-Decto automaticallygeneratetestcasestoreproducesoftware ing LLMs.Inthecontext ofcodeordataprivacy, we havesecurity bugs. opted tousetheterm“privacy”tocharacterizescenariosIn therealmofsecurity,fuzzingstands[325 , 109, in which LLMs are utilized to ensure theconfidentiality of337 , 345, 272] outasawidelyemployedtechniqueforNovAug either codeordata.However, giventhatwedidnotcomegenerating test cases. Deng et al. introducedTitanFuzz[56], Novacross any papers specifically addressing code privacy, ourJulan approachthatharnessesLLMstogenerateinputpro- discussion focusesoncodesecurity(§4.1 ) aswellasbothgrams for fuzzing Deep Learning (DL) libraries. TitanFuzzDec data security and privacy (§4.2).demonstrates impressivecodecoverage(30.38%/50.84%) and detectspreviouslyunknownbugs(41outof Jun65)in popular DLlibraries.Morerecently,Dengetal.[58 , 57]OctSeprefined LLM-basedfuzzing(namedFuzzGPT),aimingto May generate unusualprogramsforDLlibraryfuzzing.While Apr AugJanMar JulFebJanYifan Yao etal.: Preprint submitted to ElsevierPage 4of24Jun FebMayMar Apr


---

<!-- Página 5 -->

### A Survey

### on

### Large Language

### Model

### (LLM)

### Security and

### Privacy:

### The

### Good,

### the

### Bad,

### and

### Ugly

### Table

### 2

### LLMs for Code

### Security and

### Privacy

Life

WhenRunningTestWorkLLM(s)CodingSOTAGenerating BugMaliciousVulnerability(TCG)Fixing DetectingCode

Sandoval234 ]○Codex$ Negligible SVEN98 ]○CodeGen$ More SALLM254 ]○ChatGPT Madhav197 ]○ChatGPT Zhang343 ]○␣ChatGPT$ More Libro136 ]○␣LLaMA! Higher TitanFuzz56 ]○␣Codex$ Higher FuzzGPT57 ]○␣ChatGPT$ Higher Fuzz4All313 ]○␣ChatGPT$ Higher WhiteFox321 ]○␣GPT4$ High-quality Zhang337 ]○␣ChatGPT CHATAFL190 ]○␣ChatGPT$ Higher Henrik105 ]○␣ChatGPT! Higer Apiiro74 ]○␣N/A Noever201 ]○␣ChatGPT$ 4X Bakhshandeh15 ]○␣ChatGPT$ Low Moumita218 ]○␣ChatGPT! Higher Cheshkov41 ]○␣ChatGPT! No LATTE174 ]○␣GPT$ Cost DefectHunter296 ]○␣Codex Chen37 ]○␣ChatGPT Hu110 ]○␣ChatGPT KARTAL233 ]○␣ChatGPT$ Less VulLibGen38 ]○␣LLaMa$ Higher Ahmad3 ]○␣Codex$ Fix InferFix125 ]○␣Codex$ CI Pearce211 ]○␣Codex$ Zero-shot Fu83 ]○␣ChatGPT$ Higher Sobania257 ]○␣ChatGPT$ Higher Jiang123 ]○␣ChatGPT$ Higher

### exposing a

### noticeable

### performance

### gap

### when

### compared

### to

### TitanFuzz leverages

### LLMs’

### ability

### to

### generate

### ordinary

### conventional

### static

### analysis

### tools.

### This

### disparity

### primarily

### code, FuzzGPT

### addresses

### the

### need

### for

### edge-case

### testing

### arises from

### the

### relatively higher

### occurrence

### of

### false

### alerts

### by priming

### LLMs

### with

### historical

### bug-triggering

### program.

### LLMs.

### Similarly, Cheshkov

### et

### al.

### [

### 41 ] point

### Fuzz4All [313] leverages LLMs as input generators and mu-generated by

### tation engines, creating diverse and realistic inputs for vari-out that

### the

### ChatGPT

### model

### performed

### no

### better

### than

### a

### for

### both

### binary

### and

### multi-label

### classifi-

### ous languages (e.g., C, C++), improving the previous state-dummy classifier

### cation tasks

### in

### code

### vulnerability

### detection.

### Wang

### et

### al.

### of-the-art coverage by

### 36.8%

### on

### average.

### WhiteFox[321],

### [ 296 ], a

### model that employs

### a novel

### white-box

### compiler

### fuzzer

### that

### utilizes

### LLMs

### to introduceDefectHunter

### LLM-driven techniques

### for

### code

### vulnerability

### detection.

### test compiler optimizations, outperforms existing fuzzers (it

### They demonstrate

### the

### potential

### of

### combining

### LLMs

### with

### generates high-quality tests for intricate

### optimizations, sur-

### passing state-of-the-art

### fuzzers

### by up

### to

### 80

### optimizations).

### advanced mechanisms (e.g., Conformer) to identify software

### vulnerabilities more effectively. This combination shows an

### Zhang et al. [337] explore the generation of fuzz drivers for

### in

### effectiveness,

### approximately from

### 14.64%

### library API

### fuzzing

### using

### LLMs.

### Results

### show

### that

### LLM-improvement

### compared

### with

### Pongo-70B.

### LATTE[174] is

### a

### based generation is practical, with 64% of questions solvedto 20.62%,

### entirely automatically and up to 91% with manual validation.novel static binary taint analysis method powered by LLMs.

### techniques (e.g.,

### CHATAFL[190] is an LLM-guided protocol fuzzer that con-LATTEsurpasses existing state-of-the-art

### structs grammars

### for message

### types

### and

### mutates

### messages

### Emtaint, Arbiter,

### and

### Karonte),

### demonstrating

### remarkable

### or predicts

### the

### next

### messages

### based

### on

### LLM

### interactions,effectiveness in vulnerability detection (37 new bugs in real-

### achieving better state and code coverage compared to state-world firmware) with lower cost.

### Efforts in

### leveraging

### LLMs

### for

### vulnerability

### detection

### of-the-art fuzzers (e.g., AFLNET [217], NSFUZZ [222]).

### extend to

### specialized

### domains

### (e.g.,blockchain

### [

### 110 , 37

### ],

### Vulnerable

### Code

### Detecting

### (RE).Noever

### [

### 201 ] explores

### kernel [

### 104 ] mobile

### [

### 303 ]). For

### instance,

### Chen

### et

### al.

### [

### 37 ]

### the capability

### of

### LLMs,

### particularly

### OpenAI’s

### GPT-4,

### in

### and Hu

### et

### al.

### [

### 110 ] focus

### on

### the

### application

### of

### LLMs

### detecting software

### vulnerabilities.

### This

### paper

### shows

### that

### in identifying

### vulnerabilities

### within

### blockchain smart

### con-

### GPT-4 identified

### approximately

### four

### times

### the

### number

### of

### tracts. Sakaoglu’s study

### introduces

### KARTAL [

### 233 ], a

### pio-

### vulnerabilities compared to traditional static code analyzers

### neering approach that

### harnesses

### LLMs for web application

### (e.g., Snyk and Fortify). Parallel conclusions have also been

### vulnerability detection.

### This

### method

### achieves an

### accuracy

### drawn in

### other

### efforts

### [

### 141 , 15

### ]. However,

### Moumita

### et

### al. [ 218] applied LLMs for software vulnerability detection,

### Yifan Yao et

### al.: Preprint submitted to Elsevier

### Page 5

### of

### 24


---

<!-- Página 6 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

observed thatLLMs canrepair insecure codeina range ofTable3 contexts even without being explicitly trained on vulnerabil-LLMs for DataSecurity andPrivacy ity repair tasks. Prop.ComparedChatGPT is noted for its ability in code bug detection andWorkModel SOTA correction. Fu et al. [83] assessed ChatGPT in vulnerability-I related taskslike predicting and classifying vulnerabilities, Fang294 ]○ChatGPT Liu187 ]○ChatGPTseverity estimation,andanalyzingover190,000C/C++ Amine73 ]○ChatGPT$ Alignedfunctions. TheyfoundthatChatGPT’sperformancewas HuntGPT8 ]○ChatGPT$ More Chris71 ]○ChatGPT$ Lessbehind otherLLMsspecializedinvulnerabilitydetection. AnomalyGPT91 ]○ChatGPT$ LessHowever,Sobaniaetal.[257 ] foundChatGPT’sbugfix- LogGPT221 ]○ChatGPT$ Less Arpita286 ]○␣BERTing performancecompetitive withstandardprogramrepair Takashi142 ○␣ChatGPT$ Highmethods, asdemonstratedbyitsabilitytofix31outof Fredrik102 ]ChatGPT$ Effective IPSDM119 ]○␣BERT40 bugs.Xiaet al.[315 ] presentedChatRepair, leveraging Kwon149 ]○␣ChatGPT$ Non-exppre-trained language models (PLMs) for generating patches Scanlon237○␣ChatGPT$ More Sladić255 ]○␣ChatGPT$ Morewithout dependencyonbug-fixingdatasets,aimingtoen- WASA297 ]○␣-$ Morehance performancetogeneratepatcheswithoutrelyingon REMARK340 ]○␣-$ More SWEET154 ]○␣-$ Morebug-fixing datasets,aimingtoimproveChatGPT’scode- fixing abilitiesusingamixofsuccessfulandfailuretests. As a result, they fixed 162 out of 337 bugs at a cost of $0.42 of upto87.19%andiscapableofconducting539pre-each. dictions persecond.Additionally,Chenetal.[38 ] make **Finding II.As shown in Table 2, a comparison with state-**a noteworthycontributionwithVulLibGen,agenerative of-the-art methods reveals that the majority of researchersmethodology utilizing LLMs to identify vulnerable libraries. (17 outof25)have concludedthatLLM-basedmethodsAhmad et al. [3 ] shiftthefocus to hardware security. They outperform traditionalapproaches(advantagesincludeinvestigatetheuseofLLMs,specifically OpenAI’s Codex, higher code coverage,detecting accuracy, less costin automaticallyidentifyingandrepairingsecurity-related etc.). OnlyfourpapersarguethatLLM-basedmethodsbugs inhardwaredesigns.PentestGPT[55 ], anautomated do not surpassthestate-of-the-artappoarches. Themostpenetration testing tool, uses the domain knowledge inherent frequently discussedissuewithLLM-basedmethodsisin LLMstoaddressindividualsub-tasksofpenetration their tendencytoproducebothhighfalsenegativesandtesting, improving task completion rates significantly. false positives when detecting vulnerabilities or bugs. **Malicious Code**Detecting(RE).Using LLMtodetect malware isapromisingapplication.Thisapproachlever-**4.2. LLMs**for Data Security and Privacy ages thenaturallanguageprocessingcapabilitiesandcon- As demonstratedinTable3, LLMsmakevaluablecontri- textual understandingofLLMstoidentifymalicioussoft- butions totherealmofdatasecurity, offeringmultifaceted ware. InexperimentswithGPT-3.5conductedbyHenrik approaches tosafeguarding sensitive information. We have Plate [105], it was found that LLM-based malware detection organized the research papers into distinct categories based can complementhumanreviews butnotreplacethem.Out on the specific facets of data protection that LLMs enhance. of 1800binaryclassificationsperformed,therewereboth These facetsencompasscriticalaspectssuchasdatain- false-positives and false-negatives. The use of simple tricks tegrity (I),whichensuresthatdataremainsuncorrupted could alsodeceivetheLLM’s assessments.Morerecently, throughout its life cycle; data reliability (R), which ensures there are a few attempts have been made in this direction. For the accuracy of data; data confidentiality (C), which focuses example, Apiiro [74] is a malicious code analysis tool using on guardingagainstunauthorizedaccessanddisclosure LLMs. Apiiro’s strategy involves the creation of LLM Code of sensitiveinformation;anddatatraceability(T),which Patterns (LCPs) to represent code in vector format, making it involvestracking and monitoring data access and usage. easier to identify similarities and cluster packages efficiently. Its LCP detector incorporates LLMs, proprietary code anal-**Data Integrity (I).Data**ensures that data remains ysis, probabilistic sampling, LCP indexing, and dimension-unchanged and uncorruptedthroughout its life cycle. As of ality reduction to identify potentially malicious code.now,there are a few works that discuss how to use LLMs to protect data integrity. For example, ransomware usually en- **Vulnerable/Buggy**Code Fixing (RE).Several papers [123, crypts a victim’s data, making the data inaccessible without 211 , 314] hasfocusedonevaluatetheperformanceof a decryption key that is held by the attacker, which breaks the LLMs trainedoncodeinthetaskofprogramrepair.Jin data integrity. Wang Fang’s research [294 ] examines using et al. [125] proposedInferFix, a transformer-based program LLMs for ransomware cybersecurity strategies, mostly theo- repair framework that works in tandem with the combination retically proposing real-time analysis, automated policy gen- of cutting-edge static analyzer with transformer-based model eration, predictive analytics, andknowledge transfer. How- to addressandfixcriticalsecurityandperformanceissues ever,thesestrategieslackempiricalvalidation.Similarly, with accuracybetween65%to75%.Pearceetal.[211 ]

Yifan Yao etal.: Preprint submitted to ElsevierPage 6of24


---

<!-- Página 7 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

Liu et al. [187] explored the potential of LLMs for creatingdepended upon to be accurate, and free from errors or bias. cybersecurity policiesaimedatmitigatingransomwareat-Takashi etal.[142 ] proposedtouseChatGPTforthede- tacks with data exfiltration. They compared GPT-generatedtection of sites that contain phishing content. Experimental Governance, Risk and Compliance (GRC) policies to thoseresults using GPT-4 show promising performance, with high from established security vendors and government cyberse-precision andrecallrates.Fredriketal.[102 ] assessedthe curity agencies. They recommended that companies shouldability of four large language models (GPT, Claude, PaLM, incorporate GPT into their GRC policy development.and LLaMA) to detect malicious intent in phishing emails, Anomaly detectionisakeydefensemechanismthatand found that they were generally effective, even surpassing identifies unusual behavior. While it does not directly protecthuman detection,althoughoccasionallyslightlylessaccu- data integrity, it identifies abnormalor suspicious behaviorrate.IPSDM[ 119 ] isamodelfine-tunedfromtheBERT that canpotentiallycompromisedataintegrity(aswellas family toidentifyphishingandspamemailseffectively. data confidentiality and data reliability). Amine et al. [73] in-IPSDMdemonstrates superiorperformanceinclassifying troduced an LLM-based monitoring framework for detectingemails, both in unbalanced and balanced datasets. semantic anomaliesinvision-basedpoliciesandappliedit **Data Traceability**(T).Data traceabilityisthecapabilityto both finite state machine policies for autonomous driving to trackanddocumenttheorigin,movement,andhistoryand learnedpolicies for object manipulation. Experimental of datawithinasinglesystemoracrossmultiplesystems.results demonstrate that it can effectively identify semantic This conceptisparticularlyvitalinfieldssuchasincidentanomalies, aligningwithhumanreasoning.HuntGPT[ 8 ] management and forensic investigations, where understand-is anLLM-basedintrusiondetectionsystemfornetwork ing thejourneyandtransformationsofevents toresolvinganomaly detection. The results demonstrate its effectiveness issues and conducting thorough analyses. LLMs have gainedin improvinguserunderstandingandinteraction.Chriset traction in forensic investigations, offering novel approachesal. [ 71] andLogGPT[221] explore ChatGPT’s potential for for analyzing digital evidence. Scanlon et al. [237] exploredlog-based anomaly detection in parallel file systems. Results how ChatGPTassistsinanalyzingOSartifactslikelogs,show thatitaddressestheissuesintraditionalmanual files, cloud interactions, executable binaries, and in examin-labeling and interpretability.AnomalyGPT[91] uses Large ing memorydumps to detect suspicious activities or attackVision-Language Modelstodetectindustrialanomalies.It patterns. Additionally, Sladić et al. [255] proposed that gen-eliminates manual threshold setting and supports multi-turn erative models like ChatGPT can be used to create realisticdialogues. honeypots to deceive human attackers. Watermarking involvesembeddingadistinctive,typ-**Data Confidentiality (C).Data confidentiality refers to the** ically imperceptibleorhard-to-identifysignalwithinthepractice ofprotectingsensitiveinformationfromunautho- rized accessordisclosure,atopicextensively discussedin outputs ofamodel.Wangetal.[297 ] discussesconcerns LLM privacy discussions [214, 242, 286, 1]. However, mostregarding the intellectual property of training data for LLMs and proposedWASAframeworktolearnthemappingbe-of thesestudiesconcentrateonenhancingLLMsthrough tween the texts of different data providers. Zhang et al. [340]state-of-the-art PrivacyEnhancingTechniques(e.g.,zero- knowledgeproofs [224], differential privacy (e.g., [242, 184,developedREMARK-LLMthat focused on monitor the uti- lization oftheircontentandvalidatewatermarkre-166 ], and federated learning [145, 122 , 78]). There are only a few attemptsthatutilizeLLMstoenhanceuserprivacy.trieval. Thishelpsprotectagainstmalicioususessuchas plagiarism.Furthermore,identifyingcodeFor example,Arpitaetal.[286 ] useLLMstopreservespamming and produced by LLMsisvitalfor addressing legal andethicalprivacy by replacing identifying information in textual data codelicensing,plagiarism,andmalwarewith genericmarkers.Insteadofstoringsensitiveuserin-issues concerning formation, suchasnames,addresses,orcreditcardnum-creation. Similarly, Li et al. [169] propose the first watermark bers, theLLMssuggestsubstitutesforthemaskedtokens.technique to protect large language model-based code gen- This obfuscationtechnique helpstoprotectuserdatafromeration APIs from remote imitation attacks. Lee et al. [154] SWEET, atoolthatimplementswatermarkingbeing exposedtoadversaries.ByusingLLMstogeneratedeveloped specifically on tokens within programming languages.substitutes for masked tokens, the models can be trained on obfuscated data without compromising the privacy and secu- **Finding III.**Likewise, itisnoticeablethatLLMsrity of the original information. Similar ideas have also been excel in data protection, surpassing current solutions andexplored inotherstudies[1 , 262]. Hyeokdongetal.[149 ] requiring fewer manual interventions. Table 2 and3explore implementingcryptographywithChatGPT,which reveal that ChatGPT is the predominant LLM extensivelyultimately protectsdataconfidentiality.Despitethelack employed indiversesecurityapplications.Itsversatilityof extensive codingskillsorprogrammingknowledge, the and effectivenessmakeitapreferredchoiceforvariousauthors were able to successfully implement cryptographic security-related tasks,furtherreinforcingitspositionasalgorithms throughChatGPT. Thishighlightsthepotential a go-tosolutioninthefieldofartificialintelligenceandfor individuals to utilize ChatGPT for cryptography tasks. cybersecurity. **Data Reliability (R).**In our context, data reliability refers to the accuracy of data. It is a measure of how well data can be

Yifan Yao etal.: Preprint submitted to ElsevierPage 7of24


---

<!-- Página 8 -->

Hardware Attacks OS Attacks Software Attacks

Network Attacks User-

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

information associated withthehardware. Side-channel at- tack [260, 107, 189] is one attack that can be powered by the LLMs. Side-channel attacks typically entailtheanalysis of unintentional information leakage from a physical system or implementation, such as a cryptographic device or software, with the aim of inferring secret information (e.g., keys). Yaman[ 319] has explored the application of LLM tech- niques todevelopside-channelanalysismethods.There- search evaluates the effectiveness of LLM-based approaches in analyzingside-channelinformationintwohardware- related scenarios:AESside-channelanalysisanddeep- learning accelerator side-channel analysis. Experiments are conducted todeterminethesuccessratesofthesemethods in both situations.

**OS-Level Attacks.LLMs operate at a high level of abstrac-** tion and primarily engage with text-based input and output. They lackthenecessarylow-level systemaccessessential for executing OS-level attacks [114, 288, 128]. Nonetheless, they canbeutilizedfortheanalysisofinformationgath- ered fromoperatingsystems, thuspotentially aidinginthe execution ofsuchattacks.Andreasetal.[94 ] establisha feedbackloop connecting LLM to a vulnerable virtualma- chine through SSH, allowing LLM to analyze the machine’s state, identifyvulnerabilities,andproposeconcreteattack strategies, whicharethenexecutedautomaticallywithin the virtual machine. More recently, they [95] introduced an automated Linux privilege-escalation benchmark using localFigure 2:TaxonomyofCyberattacks.Thecoloredboxesrep- virtual machinesandanLLM-guidedprivilege-escalationresent attacksthathavebeendemonstratedtobeexecutable tool toassessvariousLLMsandpromptstrategiesagainstusing LLMs,whereasthegrayboxesindicateattacksthat the benchmark.cannot beexecutedwithLLMs.

**Software-Level**Attacks.Similar to how they employ LLM to targethardwareandoperatingsystems,therearealso instances whereLLMhasbeenutilizedtoattacksoftware (e.g., [343 , 209, 212, 32]). However,themostprevalent software-levelusecaseinvolves maliciousdevelopersuti- lizing LLMstocreatemalware.Mikaetal.[17 ] present a proof-of-conceptinwhichChatGPTisutilizedtodis- tribute malicioussoftware whileavoiding detection. Yin et al. [ 207] investigate the potential misuse of LLM by creating a numberofmalwareprograms(e.g.,ransomware,worm, keylogger,brute-forcemalware,Filelessmalware).Anto- Figure 3:Prevalence oftheexistingattacks nio Monjeetal.[194 ] demonstratehowtotrickChatGPT into quicklygeneratingransomware.MarcusBotacin[22 ] explores differentcodingstrategies(e.g.,generatingentire **5. Negative**Impacts on Securityand Privacymalware, creatingmalwarefunctions)andinvestigates the LLM’s capacities to rewrite malware code. The findings re-HardwareOSSoftwareNetworkUserAs shown in Figure 2 , we have categorizedthe attacks into veal that LLM excels in constructing malware using buildingfive groupsbasedontheirrespectivepositionswithinthe block descriptions. Meanwhile, LLM can generate multiplesystem infrastructure. These categories encompass hardware- versions ofthesamesemanticcontent(malwarevariants),level attacks, OS-levelsoftware-levelnetwork- with varying detection rates by Virustotal AV (ranging fromlevel attacks,anduser-level attacks.Additionally, wehave 4% to 55%).quantified thenumberofassociatedresearchpaperspub- lished for each group, as illustrated in Figure 3.**Network-Level**Attacks.LLMs canalsobeemployedfor initiating network attacks. A prevalent example of a network-**Hardware-Level**Attacks.Hardware attackstypicallyin- level attackutilizingLLMisphishingattacks[18 , 43].volvephysical access to devices. However, LLMs cannot di- Fredrik et al. [102 ] compared AI-generated phishing emailsrectly access physical devices. Instead, they can only

Yifan Yao etal.: Preprint submitted to ElsevierPage 8of24

FilelessCAPTCHA Breaking RansomwarePhishing AttacksKeyloggerFingerprinting AttacksScientificWormmisconductWeb Side- ChannelImpersonationBrute- Attacks Spear PhishingMalwarePrivilegeWeb DoSAttacksEscalationMisinformation SoftwareCSRF AttacksOS RCEExploitationFraudOSSoftwareHardwareXSS AttacksSide-DoSSide-SocialAttacksAttacksEngineeringSoftwareSQL InjectionSide-OS DoSFaultAttacksCredentialInjectionDirectoryStuffingMemoryTraversalRaceEvil MaidAttacksConditionsAttacksCookie TheftTailgating RootkitMaliciousBOF Attacks Firmware NetworkUserOSSoftwareHardwareAttacksAttacks

Cyber Attacks


---

<!-- Página 9 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

using GPT-4 withmanuallydesignedphishingemailscre-social engineersinvolves tacticssuchaspsychologi- ated usingtheV-Triad, alongsideacontrolgroupexposedcal manipulation, targeted phishing,and thecrisisof to genericphishingemails.Theresultsshowedthatper-authenticity. sonalized phishingemails,whethergenerated by AIorde- •**Scientific Misconduct.**Irresponsible useofLLMssigned manually, had higher click-through rates compared to can resultinissuesrelatedtoscientificmisconduct,generic ones. Tyson et al. [151] investigated how modifying stemming fromtheircapacitytogenerateoriginal,ChatGPT’s inputcanaffectthecontentofthegenerated coherent text. The academic community [45, 265, 215,emails, makingthemmoreconvincing.JulianHazell[97 ] 46 , 179, 72, 200, 223, 87, 139, 226], encompass-demonstrated the scalability of spear phishing campaigns by ing diversedisciplinesfromvariouscountries,hasgenerating realistic and cost-effective phishing messages for raised concernsabouttheincreasingdifficultiesinover 600 British Members of Parliament using ChatGPT. In detecting scientificmisconductintheeraofLLMs.another study, Wang et al. [295] discuss how the traditional Concerns arisefromLLMs’abilitytogenerateco-defenses may fail in the era of LLMs. CAPTCHA challenges, herent andoriginalcontent,includingcompletepa-involvingdistorted letters and digits, struggle to detect chat- pers fromunreliablesources[283 , 287, 232]. Re-bots relying ontext andvoice. However, LLMsmay break searchers arealsoactivelyengagedintheefforttothe challenges, as they can produce high-quality human-like detect suchmisconduct.Forexample,KavitaKu-text andmimichumanbehavioreffectively.Thereisone mari etal.[146 , 147] proposedDEMASQ, aprecisestudy thatutilizesLLMfordeployingfingerprintattacks. ChatGPT-generatedcontent detector.DEMASQcon-Armin etal.[236 ] employeddensity-basedclusteringto siders biasesintextcompositionandevasiontech-cluster HTTPbannersandcreatetext-basedfingerprints niques, achievinghighaccuracyacrossdiversedo-for annotatingscanningdata.Whenthesefingerprintsare mains in identifying ChatGPT-generated content.compared toanexistingdatabase,itbecomespossibleto identify new IoT devices and server products.•**Fraud.Cybercriminals have devised a new tool called** FraudGPT [76, 10], which operates like ChatGPT but **User-Level**Attacks.Recent discussions have primarily fo- facilitates cyberattacks. It lacks the safety controls of cused onuser-levelattacks,asLLMdemonstratesitsca- ChatGPT andissoldonthedarkwebandTelegram pability to create remarkably convincing but ultimately de- for $200permonthor$1,700annually.FraudGPT ceptive content,aswellasestablishconnectionsbetween can createfraudemailsrelatedtobanks,suggesting seemingly unrelatedpiecesofinformation.Thispresents malicious links’placementinthecontent.Itcan opportunities formaliciousactorstoengageinarangeof also listfrequentlytargetedsitesorservices,aiding nefarious activities. Here are a few examples: hackers inplanningfutureattacks.WormGPT[52 ], a cybercrimetool,offersfeaturessuchasunlimited•**Misinformation.**Overreliance oncontentgenerated character supportandchatmemoryretention.Theby LLMs without oversight is raising serious concerns tool was trained on confidential datasets, with a focusregarding thesafety ofonlinecontent[206 ]. Numer- on malware-relatedandfraud-relateddata.Itcanous studies have focused on detecting misinformation guide cybercriminalsinexecutingBusinessEmailproduced byLLMs.Severalstudy[35 , 308, 324] Compromise (BEC) attacks.reveal contentgeneratedbyLLMsarehardertode- tect andmayusemoredeceptivestyles,potentially **Finding IV.As illustrated in Figure 3, when compared to**causing greaterharm.CanyuChenetal.[35 ] pro- other attacks, it becomes apparent thatuser-level attackspose a taxonomy for LLM-generated misinformation are the most prevalent, boasting a significant count of 33and validate methods. Countermeasures and detection papers. This dominance can be attributedto the fact thatmethods [308 , 280, 40, 267, 36, 341, 19, 155, 263] LLMs have increasinglyhuman-likereasoningabilities,havealsobeendeveloped toaddresstheseemerging enabling themto generate human-like conversations andissues. content (e.g.,scientificmisconduct,socialengineering). •**Social Engineering.LLMs not only have the potential**Presently,LLMs do not possess the same level of access to to generatecontentfromtrainingdata,buttheyalsoOS-level or hardware-level functionalities. This observa- offer attackers a new perspective for social engineer-tion remains consistent with the attack observed in other ing. Work from Stabb et al. [261] highlights the capa-levels aswell.Forinstance,atthenetwork level, LLMs bility of well-trained LLMs to infer personal attributescan beabusedtocreatephishingwebsitesandbypass from text, such as location, income, and gender. TheyCAPTCHA mechanisms. also revealshowthesemodelscanextractpersonal information fromseemingly benignqueries.Tong et **6. Vulnerabilities**and Defenses in LLMsal. [ 275] investigated the content generated by LLMs may include user information. Moreover, Polra VictorIn thefollowingsection,weembarkonanin-depthex- Falade [76 ] statedtheexploitationbyLLM-drivenploration oftheprevalentthreatsandvulnerabilitiesasso- ciated withLLMs(§6.1 ). Wewillexaminethespecific

Yifan Yao etal.: Preprint submitted to ElsevierPage 9of24


---

<!-- Página 10 -->

Adversarial Attacks Data Poisoning Backdoor Attacks

I Attribute Membership Inferences

Extraction Attacks Inherent Vulnerabilities and Threats

-Bias and Unfairness AIExploitation

I Jailbreaking Prompt Injection

Remote Code Execution

Side Channel

Inherent Vulnerabilities and Threats

-

AISupply Chain -Vulnerabilities Non

### Vulnerabilities and Threats

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

risks andchallengesthatariseinthecontextofLLMs.In addition todiscussingthesechallenges,wewillalsodelve into the countermeasures and strategies that researchers and practitioners have developed tomitigatetheserisks(§6.2 ). Figure 4 illustrates the relationship between the attacks and defenses.

**6.1. Vulnerabilities**and Threats in LLMs In thissection,weaimtodelveintothepotentialvulner- abilities andattacksthatmaybedirectedtowardsLLMs. Our examination seekstocategorizethesethreatsintotwo distinct groups: AI Model Inherent Vulnerabilities and Non- AI Model Inherent Vulnerabilities.

***6.1.1. AI****Inherent Vulnerabilities and Threats* These are vulnerabilities and threats that stem from the very nature and architecture of LLMs, considering that LLMs are fundamentally AImodelsthemselves. For example, attack- ers maymanipulatetheinputdatatogenerateincorrector undesirable outputs from the LLM.

**(A1) Adversarial Attacks.**attacksinmachine learning refer to a set of techniques and strategies used to in- tentionally manipulate or deceive machine learning models. These attacks are typically carried out with malicious intent and aimtoexploitvulnerabilitiesinthemodel’s behavior. Weonlyfocusonthemostextensivelydiscussedattacks, namely,data poisoning and backdoor attacks.

•**Data Poisoning.**Data poisoningstandsfor attackers influencing thetrainingprocessbyinjectingmali- cious data into the training dataset. This can introduce vulnerabilities orbiases,compromisingthesecurity, effectiveness, or ethical behavior of the resulting mod- els [ 206]. Various study [148, 290 , 289 , 2 , 291 , 239] havedemonstratedthatpre-trainedmodelsarevul- Figure 4:TaxonomyofThreatsandtheDefenses.Thelinenerable tocompromiseviamethodssuchasusing represents adefensetechniquethatcandefendagainsteitheruntrusted weightsorcontent,includingtheinsertion a specificattackor agroupofattacks.of poisonedexamplesintotheirdatasets.By inherent nature as pre-trained models, LLMs are sus- ceptible to data poisoning attacks [227, 251, 245]. For introducing hiddentriggersintothemodeltoma-example, Alexander et al. [290] showed that even with nipulate specificbehaviorsorresponseswhenthejust 100 poison examples, LLMs can produce consis- trigger is encountered. LLMs are subject to backdoortently negative results or flawed outputs across various attacks [161, 331, 167]. For example, Yao et al. [329] atasks. Larger language models are more susceptible to bidirectional backdoor, which combines trigger mech-poisoning, and existing defenses like data filtering or anisms with prompt tuning.model capacity reduction offer only moderate protec-Fileless tion while hurting test accuracy. Ransomware **(A2) Inference**Attacks.attacksinthecontext •**Backdoor Attacks.**attacks involve the ma-Keyloggerof machinelearningrefertoaclassofattackswherean licious manipulationoftrainingdataandmodelpro- adversary triestogainsensitiveinformationorinsightsWormcessing, creatingavulnerabilitywhereattackerscan about amachinelearningmodeloritstrainingdataby embed a hidden backdoor into the model [322]. BothBrute- making specific queries or observations to the model. These backdoor attacksanddatapoisoninginvolve attacks oftenexploitunintendedinformationleakagefromPrivilegeMalware manipulating machinelearningmodels,whichcanAttacksEscalationthe responses.Softwareinclude manipulation of inputs. However, the key dis-OS RCEExploitation tinction is that backdoor attacks specifically focus on•**Attribute Inference Attacks.**inference At-OSSoftwareHardwareSide-DoStack [208, 181 , 133 , 258 , 183 , 160] is a typeof threat-AttacksAttacksSoftware Side-OS DoSFaultAttacksYifan Yao etal.: Preprint submitted to ElsevierPage 10of24InjectionMemoryRaceEvil MaidAttacksConditionsAttacks RootkitMaliciousBOF Attacks Firmware OSSoftwareHardwareAttacksAttacks

Cyber Attacks

Model Architecture LLM capacity ArchitectureLLM Sparsity in

Cognitive Architectures Knowledge Graph Defense Corpora Cleaning Language Identification Detoxicification Debiasing De- Deduplication Optimization Methods Adversarial Training Adversarial Fine- Defense Strategies in LLM TrainingSafe Instruction- Differential Privacy

Instruction Processing (Pre- Instruction Manipulation Instruction Purification Defensive Demonstrations Malicious Detection (In- Confidence- Entropy- Consistency Check Gradient- Outlier Detection Defense Strategies in LLM InferenceGeneration Processing (Post- Majority Vote (Self-

Defenses for Non-- ()

### Defenses

CAPTCHA Breaking Phishing Attacks Fingerprinting Attacks Web Side- ChannelI Attacks Web DoS CSRF Attacks XSS Attacks SQL Injection Directory Traversal Cookie Theft

Network

Scientific misconduct mpersonation Spear Phishing Misinformation Fraud Social Engineering Credential Stuffing Tailgating

User


---

<!-- Página 11 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

where anattackerattemptstodeducesensitiveorhas prompteddiscussionsabouttheethicalresponsibilities researchers developing anddeployingpersonal information of individuals or entities by ana-of organizations and lyzing the behavior or responses of a machine learningthese models. This has led to increased scrutiny and research models. ItworksagainsttheLLMsaswell.Robinon bias and fairness. Concerns of bias were raised from var- ious fields,encompassinggender andminoritygroups[65 ,et al.[261 ] presentedthefirstcomprehensiveexam- ination ofpretrainedLLMs’ abilitytoinfer personal144 , 81, 244], the identification of misinformation, political information from text. Using a dataset of real Redditaspects. Multiplestudies[269 , 281] revealed biasesinthe language usedwhilequeryingLLMs.Moreover, Urmanetprofiles, thestudydemonstratedthatcurrentLLMs al. [ 282] discovered that biases may arise from adherence tocan accurately infer a variety of personal information government censorship guidelines. Bias in professional writ-(e.g., location, income, sex) with high accuracy. ing [292, 263 , 79] involving LLMs is also a concern within •**Membership Inferences.**inference At- the community,asitcansignificantlydamagecredibility. tack isaspecifictypeofinference attack inthefield The biasesofLLMsmay alsoleadtonegative sideeffects of data security and privacy that determining whether in areas beyond text-based applications. Dai et al. [47] noted a datarecordwas partofamodel’s trainingdataset, that contentgeneratedbyLLMsmightintroducebiasesin given white-/black-box accesstothemodelandthe neural retrieval systems, and Huang et al. [111] discovered specific data record [250, 68, 143, 85, 84, 191, 112]. A that biases could also be present in LLM generated code. number of research studies have explored the concept of membershipinference,eachadoptingaunique**(A5) Instruction**Tuning Attacks.tuning,also perspective andmethodology.Thesestudieshaveknown as instruction-based fine-tuning, is a machine-learning explored various membership inference attacks by an-technique usedtotrainandadaptlanguagemodelsfor alyzing the label [42], determining the threshold [120,specific tasks by providing explicit instructions or examples 28 , 96], developing ageneralizedformulation[278 ],during the fine-tuning process. In LLMs, instruction-tuning among othermethods.Mireshghallahetal.[192 ]attacks refertoaclassoformanipulationsthat found that fine-tuning the head of the model exhibitstarget instruction-tunedLLMs.Theseattacksareaimedat greater susceptibilitytoattackswhencomparedtoexploiting vulnerabilitiesorlimitationsinLLMsthathave fine-tuning smaller adapters.been fine-tunedwithspecificinstructionsorexamplesfor particular tasks. **(A3) Extraction Attacks.**attacks typically refer •**Jailbreaking.Jailbreaking in LLMs involves bypass-** to attemptsbyadversariestoextractsensitiveinformation ing securityfeaturestoenableresponsestoother- or insightsfrommachinelearningmodelsortheirasso- wise restrictedorunsafequestions,unlockingcapa- ciated data.Extractionattacksandinferenceshare bilities usually limited by safety protocols. Numerous similarities but differ in theirspecific focus and objectives. studies havedemonstratedvariousmethodsforsuc- Extraction attacksaimtoacquirespecificresources(e.g., cessfully jailbreakingLLMs[159 , 271, 248]. Wei et model gradient,trainingdata)orconfidentialinformation al. [301 ] emphasizedthatthealignmentcapabilities directly.Inference attacks seek to gain knowledge or insights of LLMscanbeinfluencedormanipulatedthrough about the model or data’s characteristics, often by observing in-context demonstrations. In addition to this, several the model’sresponsesorbehavior.Varioustypesofdata researches [300 , 132] alsodemonstratedsimilarma- extraction attacks exist, including model theft[ 130, nipulation using various approaches, highlighting the 137 ], gradientleakage[158 ], andtrainingdataextraction versatility ofmethodsthatcanjailbreakingLLMs. attacks [29]. As of the current writing, it has been observed More recently,MASTERKEY[54] employed a time- that training data extraction attacks may be effective against based methodfordissectingdefenses,anddemon- LLMs. Trainingdataextraction[29 ] referstoamethod strated proof-of-concept attacks. It automatically gen- where an attacker attempts to retrieve specific individual ex- erates jailbreakpromptswitha21.58Moreover,di- amples from a model’s training data by strategically query- verse methodshavebeenemployedinjailbreaking ing the machine learningmodels. Numerous research [344, LLMs, such as conducting fuzzing [328], implement- 210 , 326] studieshave shownthatitispossibletoextract ing optimized search strategies [353], and even train- training datafrom LLMs,which may includepersonaland ing LLMsspecificallytojailbreakotherLLMs[53 , private information [113, 339]. Notably, the work by Truong 353 ]. Meanwhile, Cao et al. [27] developed RA-LLM, et al.[279 ] standsoutfor itsabilitytoreplicatethemodel a method to lowers the success rate of adversarial and without accessing the original model data. jailbreaking prompts without needing of retraining or access to model parameters.**(A4) Bias**andUnfairnessExploitation.Bias andunfair- ness in LLMs pertain to the phenomenon where these mod- •**Prompt Injection.**injection attack describes els demonstrate prejudiced outcomes or discriminatorybe- a methodofmanipulatingthebehaviorofLLMsto haviors. Whilebiasandfairnessissuesarenotuniqueto elicit unexpectedandpotentiallyharmfulresponses. LLMs, they have received more attention due to the ethical This techniqueinvolves craftinginputpromptsina and societal concerns. That is, theimpact of LLMs

Yifan Yao etal.: Preprint submitted to ElsevierPage 11of24


---

<!-- Página 12 -->

A SurveyonLarge LanguageModel(LLM)Security and

waythatbypassesthemodel’ssafeguardsortrig-**(A6) Remote** gers undesirableoutputs.Asubstantialamountofically target research [177, 332, 135, 299, 173, 124] has already au-services, or servers to execute arbitrary code remotely. While tomated theprocess ofidentifyingsemanticpreserv-RCE attacks ing payload inpromptinjectionswithvariousfocus.if an Facilitated by the capability for fine-tuning, backdoors//chat.openai.com/) and may beintroducedthroughpromptattacks[12 , 133, in the 346 , 243]. Moreover, Greshakeetal.[89 ] expressedcould potentially concerns aboutthepotentialfornewvulnerabilitiesenvironment. Tong et al. arising from LLMs invoking external resources. Otherin six studies havealsodemonstratedtheabilitytotakearbitrary file advantage ofpromptinjectionattacks,suchasun-of 51 veiling guideprompts[342 ], virtualizingpromptin-16 being vulnerable to RCE and 1 to SQL injection. These jection [320 ], andintegratingapplications[178 ]. Hevulnerabilities allow attackers to et al.[100 , 101] exploredashifttowards leveragingapp servers through prompt injections. LLMs, trainedonextensivedatasets,formitigating **(A7) Side**such attacks. cally leak information through traditional side channels such •**Denial of**Service.AofService(DoS)at-as power consumption or electromagnetic radiation, they can tack isatypeofcyberattackthataimstoexhaustbe vulnerable computational resources, causing latency or renderingdeployment scenarios. resources unavailable.DuetothenatureofLLMsintroduce privacy require significant amount of resources, attackers usethat exploit deliberately construct prompts to reduce the availabil-output monitoring) to extract private information at a much ity of models [59]. Shumailov et al. [252] proved thehigher rate than possibility ofconductingspongeattacksinthefieldcategories of side channels covering the entire ML lifecycle of LLMs,specificallydesignedtomaximizeenergyare proposed, enabling enhanced membership inference at- consumption andlatency(byafactorof10to200).tacks and novel threats (e.g., extracting users’ test queries). This strategy aims to draw the community’s attentionFor instance, to theirpotentialimpactonautonomousvehicles, astraining data well as scenarios requiring making decisions in timelycreates a side channel that compromises privacy guarantees. manner. **(A8) Supply Chain Vulnerabilities.** **Finding V.Currently, there is limited research on model**abilities refer extraction attacks[68 ], parameterattacks,orcations that the extractionofotherintermediateesults[279 ]. Whileor services. there are a few mentions of these topics, they tend to re-models, and main primarily theoretical (e.g., [172]), with limited prac-application’s tical implementation or empirical exploration. We believefocused on that thesheerscaleofparametersinLLMscomplicatesextension or these traditional approaches, rendering them less effectiveof an or even infeasible. Additionally, the most powerful LLMsexpand its are privately owned, withtheirweights, parameters, andtasks, including other detailskeptconfidential,furthershieldingthemcution. However, some from conventional attackstrategies.Strictcensorshipofexperts [ outputs generated by these LLMs challenges even black-used to steal chat histories, box traditionalMLattacks,asitlimitstheattackers’execute code ability to exploit or analyze the model’s responses.associated with the use of OAuth in plug-ins, a web standard for data ***6.1.2. Non-AI****Inherent Vulnerabilities and Threats*attempted to work. The framework formulates an extensive taxonomy ofWealsoneedtoconsidernon-AIInherentAttacks,which attacks specificencompass externalthreatsandnewvulnerabilities(which capabilities ofhavenotbeenobservedorinvestigatedintraditionalAI By considering the relationships between these stakeholders,models) thatLLMsmightencounter.Theseattacksmay the framework helps identify potential security, privacy, andnot beintricatelylinkedtotheinternalmechanismsofthe safety risks.AI model, yet they can present significant risks. Illustrative instances ofnon-AIInherentAttacksinvolve system-level vulnerabilities (e.g., remote code execution).

Yifan Yao etal.: Preprint submitted to Elsevier

Privacy:TheGood,theBad,andUgly

CodeExecution(RCE).RCE attackstyp- vulnerabilitiesinsoftwareapplications,web

arenottypically applicabledirectly toLLMs, LLMisintegratedintoawebservice(e.g.,https: ifthereareRCEvulnerabilities underlyinginfrastructureorcodeofthatservice,it leadtothecompromiseoftheLLM’s [175 ] identified13 frameworks, including12RCE vulnerabilitiesand1 read/writevulnerability. Additionally, 17out testedappswerefoundtohavevulnerabilities,with

execute arbitrarycodeon

Channel.While LLMsthemselvesdonottypi-

tocertainside-channelattacksinpractical Forexample,Edoardoetal.[51 ] sidechannelattacks,whichareattacks system-levelcomponents(e.g.,datafiltering,

what standalonemodelscanachieve. Four

theresearchdemonstrateshowdeduplicating beforeapplyingdifferentially-private

Vulner- totherisksinthelifecycleofLLMappli- mayarisefromusingvulnerablecomponents Theseincludethird-partydatasets,pre-trained plugins,anyofwhichcancompromisethe integrity[206 ]. Mostresearchinthisfieldis thesecurityofplugins.AnLLMpluginisan add-onmodulethatenhancesthecapabilities LLM.Third-partyplug-inshavebeendevelopedto functionality, enablinguserstoperformvarious websearches,textanalysis, andcodeexe- oftheconcernsraisedbysecurity 206 , 25] includethepossibilityofplug-insbeing access personal information, or onusers’ machines.Thesevulnerabilitiesare

sharingacrossonlineaccounts.Umaretal.[115 ] addressthisproblembydesigningaframe-

toLLMplatforms,takingintoaccountthe plugins,users,andtheLLMplatform itself.

Page 12of24


---

<!-- Página 13 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

**6.2. Defenses**for LLMsde-identification (personallyidentifiableinformation (PII)) [264 , 284], anddeduplication[153 , 134, 106,In thissection,weexaminetherangeofexistingdefense 157 ]. Debiasinganddetoxificationaimedtoremovemethods againstvariousattacksandvulnerabilitiesassoci- 1undesirable content from training corpora.ated with LLMs.

***6.2.1. Defense****in Model Architecture*•**Optimization Methods.**objectives are crucial indirectinghowLLMslearnfromtrainingModel architecturesdeterminehowknowledgeandcon- data, influencingwhichbehaviors areencouragedorcepts are stored, organized, and contextually interacted with, penalized. Theseobjectivesaffecttheprioritizationwhich iscrucialinthesafetyofLargeLanguageModels. of knowledge and concepts within corpora, ultimatelyThere have been a lot of works [165, 351 , 168 , 333] delved impacting theoverall safety and ethical alignment ofinto howmodelcapacitiesaffecttheprivacypreservation LLMs. Inthiscontext,robusttrainingmethodslikeand robustnessofLLMs.Lietal.[165 ] revealed thatlan- adversarial training[176 , 293, 350, 330, 163] andguage modelswithlargerparametersizescanbetrained robust fine-tuning[66 , 121] haveshownresiliencemore effectivelyinthedifferentialprivacymannerusing against perturbation-basedtextattacks.Drawingin-appropriate non-standardhyper-parameters, incomparison spiration fromtraditionaladversarialtrainingintheto smallermodels.Zhuetal.[351 ] andLietal.[168 ] image field [182], Ivgi et al. [116] and Yoo et al. [330]found thatLLMs withlarger capacities, such as thosewith applied adversarialtrainingtoLLMsbygeneratingmore extensiveparametersizes,generallyshowincreased perturbations concerningdiscretetokens.Wangetrobustness against adversarial attacks. This was also verified al. [293 ] extendedthisapproachtothecontinuousin theOut-of-distribution(OOD)robustnessscenariosby embedding space,facilitatingmorepracticalconver-Yuanetal.[333 ]. Beyond thearchitectureofLLMsthem- gence, as followed by subsequent research [176, 350 ,selves, studieshavefocusedonimprovingLLMsafetyby 163 ]. Safety alignments[205 ], anemerginglearningcombining them with external modules including knowledge paradigm, guideLLMbehaviorusingwell-alignedgraphs [39 ] andcognitivearchitectures(CAs)[150 , 11]. additional modelsorhumanannotations,proving ef-Romero etal.[231 ] proposedimprovingAIrobustnessby fectiveforethicalalignment.EffortstoalignLLMsincorporating variouscognitivearchitecturesintoLLMs. with other LLMs [334] and LLMs themselves [268].Zafar etal.[336 ] aimedtobuildtrustinAIbyenhancing In terms of human annotations, Zhou et al. [349] andthe reasoning abilities of LLMs through knowledge graphs. Shi etal.[249 ] emphasizedtheimportanceofhigh- quality training corpora with carefully curated instruc-***6.2.2. Defenses****in LLM Training and Inference* tions and outputs for enhancing instruction-following **Defense Strategies**inLLMTraining.The corecompo-capabilities inLLMs.Bianchietal.[20 ] highlighted nents of LLM training include model architectures,that the safety of LLMs can be substantially improved data, and optimization methods. Regarding model architec-by incorporatingalimitedpercentage(e.g.,3%)of tures, we examine trustworthy designs that exhibit increasedsafe examples during fine-tuning. robustness against malicioususe.Fortrainingcorpora,our investigationfocusesonmethodsaimedatmitigatingun- desired propertiesduringthegeneration,collection,and**Defense Strategies in LLM Inference.**When LLMs are de- cleaning oftrainingdata.Inthecontextofoptimizationployed as cloud services, they operate by receiving prompts methods, we review existing works that developed safe andor instructionsfromusersandgeneratingcompletedsen- secure optimization frameworks.tences inresponse.Giventhisinteractionmodel,theim- plementation oftest-timeLLMdefensebecomesaneces- sary andcriticalaspectofensuringsafeandappropriate•**Corpora Cleaning.**LLMs are shaped by theirtrain- outputs. Generally, test-timedefenseencompassesarangeing corpora, from which they learn behavior, concepts, of strategies,includingthepre-processingofpromptsandand datadistributions[302 ]. Therefore,thesafety instructions to filter or modify inputs, the detection of abnor-of LLMsiscruciallyinfluencedbythequalityof mal events that might signal misuse or problematic queries,the trainingcorpora[86 , 204]. However, ithasbeen and thepost-processingofgeneratedresponsestoensurewidely acknowledged that raw corpora collected from they adhere to safety and ethical guidelines. Test-time LLMthe web are full of issues of fairness [14], toxicity [88], defenses are essential to maintain the integrity and trustwor-privacy [208], truthfulness[ 171], etc. A lot of efforts thiness of LLMs in real-time applications.havebeen made to clean raw corpora and create high- quality training corpora for LLMs [129, 306, 152, 307, 213 , 277]. In general, these pipelines consist of the fol-•**Instruction Processing**(Pre-Processing).Instruc- lowing steps: language identification [129, 9], detox-tion pre-processingappliestransformationsoverin- ification [88 , 48, 180, 195], debiasing[188 , 21, 16],structions sentby users,inordertodestroy potential 1adversarial contextsormaliciousintents.ItplaysaPlease inherentvital roleasitblocksoutmostmalicioususageand

Yifan Yao etal.: Preprint submitted to ElsevierPage 13of24


---

<!-- Página 14 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

prevents LLMsfromreceivingsuspiciousinstruc-**7. Discussion** tions. Ingeneral, instructionpre-processingmethods **7.1. LLM**in Other Security Related Topicscan becategorizedasinstructionmanipulation[246 , 230 , 140, 117, 318], purification [164], and defensive**LLMs in Cybersecurity Education.**LLMs can be used in demonstrations [172 , 193, 301]. Jainetal.[117 ]security practicesandeducation[80 , 162, 270]. Forexam- and Kirchenbaueretal.[140 ] evaluatedmultipleple, inasoftware securitycourse,studentsaretaskedwith baseline preprocessingmethodsagainstjailbreakingidentifying and resolving vulnerabilities in a web application attacks, includingretokenizationandparaphrase.Liusing LLMs. Jingyue et al. [162] investigated how ChatGPT et al.[164 ] proposedtopurifyinstructionsbyfirstcan be used by students for these exercises. Wesley Tann et masking theinputtokensandthenpredictingtheal. [ 270] focused on theevaluation of LLMs in thecontext masked tokens with other LLMs. The predictedof cybersecurity Capture-The-Flag (CTF) exercises (partici- will serve as the purified instructions. Wei et al. [301]pants find “flags” by exploiting system vulnerabilities). The and Moetal.[193 ] demonstratedthatinsertingpre-study first assessed thequestion-answering performanceof defined defensivedemonstrationsintoinstructionsthese LLMsonCiscocertificationswithvaryingdifficulty effectively defends jailbreaking attacks of LLMs.levels, thenexaminedtheirabilitiesinsolvingCTFchal- lenges. Jin et al. [126] conducted a comprehensive study on LLMs’ understanding of binary code semantics [127] across •**Malicious Detection (In-Processing).**de- different architectures and optimization levels, providing key tection provides in-depth examinations of LLM inter- insights for future research in this area. mediate results,such asneuronactivation, regarding the given instructions, which are more sensitive, accu-**LLMs in Cybersecurity Laws, Policies and Compliance.** rate, and specified for malicious usage. Sun et al. [266]LLMs canassistindraftingsecuritypolicies,guidelines, proposed to detect backdoored instructions with back-and compliance documentation, ensuring that organizations ward probabilities of generations. Xi et al. [312] dif-meet regulatory requirements and industry standards. How- ferentiated normal and poisoned instructions from theever,it’s important to recognize that the utilization of LLMs perspective ofmasksensitivities.Shaoetal.[246 ]can potentially necessitate changes to current cybersecurity- identified suspiciouswordsaccordingtotheirtex-related lawsandpolicies.TheintroductionofLLMsmay tual relevance.Wangetal.[298 ] detectedadversar-raise new legal and regulatory considerations, as these mod- ial examplesaccordingtothesemanticconsistencyels can impact various aspects of cybersecurity, data protec- among multiple generations, which has been exploredtion, andprivacy. Ekenobietal.[273 ] examinedthelegal in the uncertainty quantification of LLMs by Duan etimplications arisingfromtheintroductionofLLMs,with al. [ 67]. Apart from the intrinsic properties of LLMs,a particularfocus on dataprotection and privacy concerns. there have been works leveraging the linguistic statis-It acknowledgesthatChatGPT’sprivacypolicycontains tic properties, such as detecting outlier words [220],commendable provisions for safeguarding user data against potential threats. The paper also advocated for emphasizing the relevance of the new law. •**Generation Processing**(Post-Processing).Genera- tion postprocessingreferstoexaminingtheproper-**7.2. Future**Directions ties (e.g., harmfulness)of thegenerated answers andWehave gleaned valuable lessons that we believe can shape applying modifications if necessary, which is the finalfuture directions. step beforedeliveringresponsestousers.Chenet •**Using LLMs**forML-SpecificTasks. Wenoticedal. [34 ] proposedtomitigatethetoxicityofgenera- that LLMs can effectively replace traditional machinetions bycomparingwithmultiplemodelcandidates. learning methods and in this context, if traditional ma-Helbling etal.[103 ] incorporatedindividualLLMs chine learning methods can be employed in a specificto identify the harmfulness of the generated answers, security application (whether offensive or defensive inwhich sharedsimilarideasasXiongetal.[317 ] and nature), it is highly probable that LLMs can also be ap-Kadavath et al. [131] where they revealed that LLMs plied to address that particular challenge. For instance,can be prompted to answer the confidences regarding traditional machine learning methods have found util-the generated responses. ity in malware detection, and LLMs can similarly be harnessed for this purpose.Therefore, one promising**Finding VI.**For defenseinLLMtraining,there’s ano- avenueistoharnessthepotentialofLLMsinsecu-table scarcity of research examining the impact of model rity applicationswheremachine learningservesasaarchitecture onLLMsafety,whichislikelyduetothe foundational or widely adopted technique. As securityhigh computational costs associated with training or fine- researchers, we are capable of designing LLM-basedtuning largelanguagemodels.Weobservedthat*safe* approaches to tackle security issues. Subsequently, we*instruction tuning*is arelativelynewdevelopmentthat can comparetheseapproacheswithstate-of-the-artwarrants further investigation and attention. methods to push the boundaries.

Yifan Yao etal.: Preprint submitted to ElsevierPage 14of24


---

<!-- Página 15 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

•**Replacing Human**Efforts.It isevidentthatLLMsChatGPT) couldpotentially alterthecurrentcybersecurity blendingtechnicalandsocialaspects.Theirhavethepotentialtoreplacehumaneffortsinbothlandscape by emphasis leansmoretowardsthesocialaspects.Munaetoffensive and defensive securityapplications. For in- al. [5 ] andMarshalletal.[185 ] discussedtheimpactofstance, tasksinvolving socialengineering,tradition- cybersecurity,highlightingitspracticalappli-ally reliant on human intervention, can now be effec-ChatGPT in tively executed using LLM techniques. Therefore, onecations (e.g.,codesecurity,malwaredetection).Dhoniet promising avenue for securityresearchers istoiden-al. [ 62] demonstrated how LLMs can assistanalysts in developingsolutions against cyber threats. How-tify areaswithintraditionalsecuritytaskswherehu- theirworkdoesnotextensively addressthepotentialman involvement has been pivotal and explore oppor-ever, cybersecurity threatsthatLLMmayintroduce.Anumbertunities tosubstitutethesehumaneffortswithLLM of surveys(e.g.,[92 , 59, 247, 49, 60, 228, 240, 241, 7])capabilities. highlight thethreatsandattacksagainstLLMs.Incom- •**Modifying Traditional ML**Attacks for LLMs.weparison toourwork,theydonotdedicateasmuchtextto haveobservedthatmanysecurityvulnerabilitiesinthe vulnerabilities that the LLM may possess. Instead, their LLMs areextensionsofvulnerabilitiesfoundintra-primary focus liesintherealmofsecurityapplications,as ditional machine-learningscenarios.Thatis,LLMsthey delve intoutilizingLLMsfor launchingcyberattacks. remain a specialized instance of deep neural networks,Attia Qammaretal.[219 ] andMaximilianetal.[196 ] inheriting common vulnerabilities such as adversarialdiscussed vulnerabilitiesexploited by cybercriminals,with attacks and instructiontuning attacks. With therighta specificfocusontherisksassociatedwithLLMs.Their adjustments (e.g., the threat model), traditional ML at-works emphasizedtheneedforstrategiesandmeasures tacks can still be effective against LLMs. For instance,to mitigatethesethreatsandvulnerabilities.HaoranLiet the jailbreaking attack is a specific form of instructional. [ 166] analyzed current privacy concerns on LLMs, cate- tuning attack aimed at producing restricted texts.gorizing them based on adversary capabilities, and explored existing defense strategies. Glorin Sebastian [242] explored•**Adapting Traditional ML Defenses for LLMs.**The the application of established Privacy-Enhancing Technolo-countermeasures traditionallyemployed forvulnera- gies (e.g., differential privacy [70], federated learning [338],bility mitigation can also be leveraged to address these and dataminimization[216 ]) forsafeguardingtheprivacysecurity issues.Forexample,thereareexistingef- of LLMs.Smithetal.[256 ] alsodiscussedtheprivacyforts that utilize traditional Privacy-Enhancing Tech- risks ofLLMs.Ourstudycomprehensively examined bothnologies (e.g., zero-knowledge proofs, differential pri- the securityandprivacyaspectsofLLMs.Insummary,vacy,andfederatedlearning[304 , 305] )totackle our research conducted an extensive review of the literatureprivacy challengesposedbyLLMs.Exploringaddi- on LLMsfrom athree-fold perspective: beneficialsecuritytional PETs techniques, whetherthey areestablished applications (e.g., vulnerability detection, secure code gen-methods orinnovativeapproaches,toaddressthese eration), adverse implications (e.g., phishing attacks, socialchallenges representsanotherpromisingresearchdi- engineering), andvulnerabilities(e.g.,jailbreaking attacks,rection. prompt attacks),alongwiththeircorrespondingdefensive measures.•**Solving Challenges**inLLM-SpecificAttacks.As previously discussed, there are several challenges as- sociated withimplementingmodelextractionorpa-**9. Conclusion** rameter extractionattacks(e.g.,vastscaleofLLM Our workrepresentsapioneeringeffortinsystematicallyparameters, privateownershipandconfidentialityof examining themultifacetedroleofLLMsinsecurityandpowerful LLMs).Thesenovelcharacteristicsintro- privacy.On the positive side, LLMs have significantly con-duced byLLMsrepresentasignificantshiftinthe tributed toenhancingcodeanddatasecurity,whiletheirlandscape, potentially leadingtonew challenges and versatile naturealsoopensthedoortomaliciousapplica-necessitating theevolutionoftraditionalMLattack tions. We also delved into the inherent vulnerabilities withinmethodologies. these models, and discussed defense mechanisms. We have illuminated thepathforwardforharnessingthepositive **8. Related**Workaspects ofLLMswhilemitigatingtheirpotentialrisks.As LLMs continuetoevolve andfindtheirplaceinanever- There have already been a number of LLM surveys released expanding arrayofapplications,itisimperativethatwe with avarietyoffocuses(e.g.,LLMevolutionandtaxon- remain vigilant in addressing security and privacy concerns, omy [31 , 347, 309, 93, 311, 23, 348], softwareengineer- ensuring that these powerful models contribute positively to ing [77 , 108], andmedicine[274 , 44]). Inthispaper,our the digital landscape. primary emphasisisonthesecurityandprivacyaspects of LLMs.Wenowdelveintoanexaminationoftheex- isting literaturepertainingtothisparticulartopic.PeterJ. Caven[30 ] specificallyexploreshowLLMs(particularly,

Yifan Yao etal.: Preprint submitted to ElsevierPage 15of24


---

<!-- Página 16 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

[20]

## Acknowledgement

T. Wethanktheanonymousreviewers andXinJinfromTheproving *arXiv*, 2023.Ohio StateUniversityfortheirinvaluablefeedback.This [21]research wassupportedpartlybytheNSFawardFMitF- in*arXiv*,2319242. Anyopinions,findings,conclusions,orrecom- 2019. mendations expressed are those of the authors and not nec-[22] essarily of the NSF.threat?”*2023*. IEEE, [23] *arXiv*, 2023.

## References

[24] [1] wal, health A. [2] D. C. M. puzzle:*arXiv* A. *arXiv:2301.02344,2023.* few-shot [3] [25] “Fixing com/story/chatgpt-plugins-security-privacy-risk/ , *arXiv*, 2023. [26] [https://doi.org/10.48550/arXiv.2302.01215](https://doi.org/10.48550/arXiv.2302.01215) T.*et*, “Low-code [4] llms,”arXiv, 2023. parameter [27] large-language-model-llama-meta-ai/ , breaking 2023-11-13. [28] [5] “Membership security: *Symposium*. IEEE, *Cluster*, vol. 1914. [6] [29] Assertion-augmented*arXiv* K.*et*, “Ex- *preprint*, 2023. tracting*30th*in [7] *Security*, 2021, Omolara*et*, “Unveiling [30] cyberattacks security,”ChatGPT’s, [8] 2023. based [31] models*arXiv*, 2023. X.*et*, “A [9] language*arXiv*, 2023. identification:*IEEE*, [32] vol. “From [10] language what-is-fraudgpt, [33] [11]*The*. W.*arXiv* Psychology *preprint*, 2022. [12] [34] models: ing*arXiv* in*Submitted* *arXiv:2310.02417,2023.* *Learning*, 2023, [35] [https://openreview.net/forum?id=E6Ix4ahpzd](https://openreview.net/forum?id=E6Ix4ahpzd) tected?” [13] [36] european*J.* and*arXiv*, 2023. *L. , vol.* [37] [14] and words*Science*, vol. detection:*arXiv*, 2023. no. [Online]. [15] [38] Chekidehkhoun, Q. testing*arXiv*, 2023. third-party*arXiv* [16] *preprint*, 2023. world //doi.org/10.48550/arXiv.2308.04662 language*arXiv*, 2021. [39] [17] knowledge*Expert*, vol. llms 112948, [18] [40] the models [19] llms models,

Yifan Yao etal.: Preprint submitted to ElsevierPage 16of24


---

<!-- Página 17 -->

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

[41][61] of*arXiv*training *arXiv:2304.07232,2023.*ing,” 48550/arXiv.2304.07232[62] [42]curity: “Label-onlyInternationalgovernment *ence*. PMLR,[63] [43]M.*et*, “A R.evaluation*arXiv* management*2023**preprint*, 2023. *on*, 2023,[64] [44]Z. N.languageProceedings Veldhuizenet, “The*of* medicine,”Communications, vol.*High*, [45]ser. ing:*Innovations*[http://dx.doi.org/10.1145/3624062.3624172](http://dx.doi.org/10.1145/3624062.3624172) *in*, pp.[65] [46]implicit*arXiv* chatgptSeminars.*preprint*, 2023. Elsevier,[66] [47]trained “Llmsness?”Advances, vol. ased*arXiv*,pp. 2023.[67] [48]B. N.the*arXiv* trained*arXiv*, 2021.*arXiv:2307.01379,2023.* [49][68] endangering*International*vulnerable*Proceedings* *Journal*, vol.*the*, 2023, [50]8717–8730. first[69] llm,”explodingtopics.com/blog/chatgpt-users,2023, dolly-first-open-commercially-viable-instruction-tuned-llm ,13. 2023,[70]International [51]*automata,*. Springer, M.[71] side*arXiv*chatgpt *arXiv:2309.05610,2023.*logs,” [52][72] usingintegrity?”Journal, vol. at/iwFL7,2023. [53][73] andM. language*arXiv*, 2023.els,” Autonomous, pp. [54][74] chatbots,”*Proceedings*Our *tributed*, 2024.//apiiro.com/blog/llm-code-pattern-malicious-package-detection/ , [55]2023, Y.[75] tomatic*arXiv*,Albuquerque, 2023.On [56]*Computer*. deep-learning*arXiv*Schloss-Dagstuhl-Leibniz *arXiv:2212.14834,2022.*[76] [57]and*International* “Large*of* ing*arXiv*, 2023.*Information*, p. [58][http://dx.doi.org/10.32628/CSEIT2390533](http://dx.doi.org/10.32628/CSEIT2390533) unusual2024[77] *IEEE/ACM*S. *(ICSE),2024,*engineering: [59][78] rity*arXiv*“Fate-llm: *arXiv:2311.11415,2023.*language*arXiv*, [60][79] securityof

Yifan Yao etal.: Preprint submitted to ElsevierPage 17of24


---

<!-- Página 18 -->

A SurveyonLarge LanguageModel(LLM)Security and

language*arXiv*, 2023.[101] [80] S. exercise*2022*[102] *Global*. IEEE, 2022, [81][103] A language*arXiv*, 2023. [82][104] and *arXiv*, 2021. [83] vulnerability 2023. [84][105] bership via [85][106] tack [86] of*Proceedings*in *of*[107] *Transparency*, 2023, [87] Y.[108] ated output *BioRxiv,pp.* [88][109] altoxicityprompts: models,”arXiv, 2020.[110] [89] M. of language*arXiv*, 2023.[111] [90] testing,” [91][112] lygpt: models,”arXiv, 2023. [92] chatgpt[113] privacy,”IEEE, 2023. [93] N.[114] models: *TechRxiv*, 2023. [94][115] large*arXiv*, 2023. [95] escalation[116] [96] Membership*arXiv*[117] *preprint*, 2017. [97] spear [98][118] hardening*ICML* *ableGenerativeAI,2023,* generation, [99][119] adversarial*Proceedings* *Conference*, 2023, 1865–1879.[120] [100] On tackle*arXiv*, 2023.

Yifan Yao etal.: Preprint submitted to Elsevier

Privacy:TheGood,theBad,andUgly

on*2024*in *Symposium*, 2024.  and models,”  By*arXiv* *preprint*,  reliable firmware*Detection* *Vulnerability* *2023,*, vol. 13959.  to, 2023, 11-13.  Showk,*et*, “Scaling *arXiv*, 2022.  learning*Journal* *Cryptographic*, vol.  D. ware*arXiv* *arXiv:2308.10620,2023.*  generative*arXiv*, 2023.  model-powered perspectives,”arXiv, 2023, [Online].  assessment*arXiv* *preprint*, 2023.  “Damia: bership*IEEE* *Secure*, vol.  language*arXiv* *arXiv:2205.12628,2022.*  nerabilities*IEEE* *&*, vol.  ing 2023.  adversarial*arXiv*, 2021.  P.-y. “Baseline models,”arXiv, 2023.  evaluation vulnerability*Proceedings* *novations*, 2023,  for approach,”  visiting*arXiv* *preprint*, 2020.

Page 18of24


---

<!-- Página 19 -->

[121]

[122]

[123]

[124]

[125]

[126]

[127]

[128]

[129]

[130]

[131]

[132]

[133]

[134]

[135]

[136]

[137]

[138]

[139]

[140]

[141]

Yifan Yao et

A SurveyonLarge LanguageModel(LLM)Security and

[142] Robust models*arXiv*[143] *arXiv:1911.03437,2019.*  large*arXiv*, 2023.[144]  models [145] llms*arXiv* *preprint*, 2023.  A.[146] 2023.  tion:[147] 2023.  tion[148] aware*Proceedings* *Conference*, 2022,[149] 1631–1645.  attacks*Interna-* *tional*, vol.[150]  T. *arXiv*, 2016. [151] against2019 *posium*. IEEE, 527.[152]  N.*et*, “Language*arXiv* *arXiv:2207.05221,2022.* [153] attacks*arXiv* *arXiv:2307.14692,2023.* [154] and [155] data*International*in *Conference*. PMLR, 10[156]  “Exploiting dard*arXiv*, 2023. [157] bugs,*2023*in *International*. IEEE,[158] 2023.  model[159] *Proceedings* *Pattern*, 2021,[160]  leverage errors*arXiv*, 2023.  plagiarism*arXiv*, 2023.  K. reliability*arXiv*[161] *arXiv:2306.04634,2023.*  codebase,”, 2023.[162]

al.: Preprint submitted to Elsevier

Privacy:TheGood,theBad,andUgly

sites*arXiv*, 2023.  “An by*arXiv*, 2023.  in*Proceedings* *Intelligence*, 2023,  Y. package *arXiv*, 2023.  “Demasq:*arXiv* *arXiv:2311.05019,2023.* *Proceedings* *of* *sium*, 2024.  pre-trained*arXiv*, 2020.  to Archive,. [Online].  of artificial *Ai*, vol.  into*Proceedings* *Conference.Springer,*  Moral, H.*et*, “The multilingual*Advances* *Systems,vol.*  Burch, models*arXiv*, 2021.  “Who  “Detecting weak*arXiv*, 2023.  Escaping language*International* *ing*, *Mining* *sets . Cambridge*  into*arXiv* *preprint*, 2023.  privacy*arXiv*, 2023.  Preventing personas,”*Proceedings* *American* *Human*, M. and for Available:  attack model*arXiv*, 2023.  “Evaluating

Page 19of24


---

<!-- Página 20 -->

[163]

[164]

[165]

[166]

[167]

[168]

[169]

[170]

[171]

[172]

[173]

[174]

[175]

[176]

[177]

[178]

[179]

[180]

[181]

Yifan Yao et

A SurveyonLarge LanguageModel(LLM)Security and

course,”[182]  language*Proceedings* *Artificial*, vol.[183]  against*arXiv*, 2022.  models*arXiv*[184] *arXiv:2110.05679,2021.*  large*arXiv*,[185] 2023. [186] backdoor  following[187] injection,” org/CorpusID:261048972  property[188] watermarks,”*Proceedings* *on*, 2023, [189] Y. B. Navas,[190] H. sekgonul, P. T.[191] Y. models,” [192] mimic*arXiv*, 2021. *et*, “Adver- sarial strategies:*Security* *Networks,vol.*  “A*arXiv* *preprint*, 2023.[193]  “Harnessing [194] vulnerabilities  “Adversarial*arXiv*[195] *preprint*, 2020.  jailbreak*arXiv* *arXiv:2310.04451,2023.* [196] Y. applications,”arXiv, 2023. [197] of*Education*, vol.  D. DetoxificationProceedings[198] *Meeting* *1:*, 2022,  for privacy*Findings*[199] *Computational*, T. and Linguistics, [https://aclanthology.org/2020.findings-emnlp.213](https://aclanthology.org/2020.findings-emnlp.213)

al.: Preprint submitted to Elsevier

Privacy:TheGood,theBad,andUgly

“Towards *arXiv*, 2017.  M. beyond,”ArXiv,vol. [https://api.semanticscholar.org/CorpusID:235593386](https://api.semanticscholar.org/CorpusID:235593386)  “Differentially*arXiv* *preprint*, 2022.  security,”  A. of  and grc*Computers* *&*, vol.  the models,”arXiv, 2021.  embedded*Applied*, vol. no.  language*Proceedings* *31th* *(NDSS’24),2024.*  R. using  Kirkpatrick, tuned*Proceedings* *2022* *Processing,Y.* Dhabi, Linguistics, [https://aclanthology.org/2022.emnlp-main.119](https://aclanthology.org/2022.emnlp-main.119)  time defensive*arXiv*, 2023.  influence using  cross-lingual models.”*Proceedings* *ciation*, 2022,  illicit

hardware Archive,. [Online].  model breakthrough 04/pathways-language-model-palm-scaling-to.html,apr accessed:  X. with*International*. PMLR,

Page 20of24


---

<!-- Página 21 -->

[200]

[201]

[202]

[203]

[204]

[205]

[206]

[207]

[208]

[209]

[210]

[211]

[212]

[213]

[214]

[215]

[216]

[217]

Yifan Yao et

A SurveyonLarge LanguageModel(LLM)Security and

S.[218] engineering institutional intelligence*European* *nal*, pp.[219]  software?”*arXiv*, 2023. Available: [220] “Taking *AI*, pp. ,[221] 2023.  “Probing[222] *Proceedings* *putational* *on*, 2021,[223] pp.  C.*et*, “Training[224] models*Advances* *Neural*, vol.[225] 2022.  LLM.[226] www-project-top-10-for-large-language-model-applications/ assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf [227] T. chatgptProceedings[228] *Security*, 2023,  purpose*2020*[229] *and*. IEEE,  to-end[230] tion,”arXiv, 2023.  language*arXiv*,[231] 2022.  amining in 2023*, 2023,*[232] 2339–2356.  B. reverse [233] H. finedweb web*arXiv*, 2023.[234]  R.*Proceedings* *of* *Data*, 2023,  models*Journal* *University*, vol.[235] [236] privacy tectability, ment,”[237]  fuzzer*2020* *Conference*.

al.: Preprint submitted to Elsevier

Privacy:TheGood,theBad,andUgly

IEEE,  vulnerability *34th* *Workshops*, 2023,  H. vulnerabilities, 2023.  simple*arXiv* *preprint*, 2020.  Exploring*arXiv* *arXiv:2309.01189,2023.*  Towards*ACM* *Transactions*, 2023.  plagiarism*arXiv* *preprint*, 2023.  *Available*, 2023.  Y. learning  research:*Applied*, vol.  soned*arXiv*, 2023. *From* *HackGPT:*. Sloan  model, apr 2023,  fending *preprint*, 2023.  ergistic tectures*arXiv* *arXiv:2308.09830,2023.*  raini, conduct negeri*Jurnal* *Pendidikan*, vol.  large Security Available:  B. implications *USENIX*, 2023, URL]([https://arxiv.org/abs/2208.09727)](https://arxiv.org/abs/2208.09727)). Sandoval Available: , 2023.  gerprinting*Proceedings* *ACM*, 2023,  J. the*Forensic* *Investigation*, vol.

Page 21of24


---

<!-- Página 22 -->

[238]

[239]

[240]

[241]

[242]

[243]

[244]

[245]

[246]

[247]

[248]

[249]

[250]

[251]

[252]

[253]

[254]

[255]

[256]

[257]

[258]

[259]

Yifan Yao et

A SurveyonLarge LanguageModel(LLM)Security and

//www.sciencedirect.com/science/article/pii/S266628172300121X  using*arXiv*,[260] 2023.  plete *30th**, 2021,*[261] 1559–1575.  attacks[262] 2023. [263] risk?:*International* *Privacy*, vol. 2023.[264]  bots:*Available* *4454761,2023.* [265] harthi, *et*, “Loft: of*arXiv*[266] *arXiv:2310.04445,2023.*  second shot*arXiv*, 2022.[267]  specific *arXiv*, 2023.[268]  defense*Computers*, vol. [269] N. els  now": on*arXiv*, 2023. [270] guage*arXiv* *arXiv:2311.08685,2023.* [271] inference *symposium*. IEEE,  stein,*arXiv* *arXiv:2306.17194,2023.*[272] [273] R. networks,” [274] V. in*arXiv*, 2023. [275] to [Online]. [276] Generative [277] and survey,”  automatic[278]  models,”*Proceedings* *computer*, 2020,[279]  J.

al.: Preprint submitted to Elsevier

Privacy:TheGood,theBad,andUgly

for*arXiv* *arXiv:2307.03744,2023.*  classification vices,”IEEE, vol. 465–488,  rization: els,”  patient*AXIS*,  news models,”arXiv, 2023.  personal*Proceed-*in *ings* *ing*, 2023,  cation: 2023.  fending in*Proceedings*, vol.  modal tion*arXiv*, 2023.  and from*arXiv* *arXiv:2305.03047,2023.*  S.*et*, “You what gual*Proceedings* *on*, 2022,  large and  S. Unraveling story*International* *Storytelling.Springer,*   data*The* *Protection*, 2023.  T. *Nature*, vol.  Privacy-preserving 2023.  leading, 2023.  N.*et*, “Llama 2:*arXiv* *arXiv:2307.09288,2023.*  wards*arXiv* *arXiv:1807.09173,2018.*  model*Proceedings* *computer*, 2021,

Page 22of24


---

<!-- Página 23 -->

[280]

[281]

[282]

[283]

[284]

[285]

[286]

[287]

[288]

[289]

[290]

[291]

[292]

[293]

[294]

[295]

[296]

[297]

[298]

Yifan Yao et

A SurveyonLarge LanguageModel(LLM)Security andPrivacy:TheGood,theBad,andUgly

[299] D.deception: identifying*Proceedings*guage*arXiv*, 2023. *AAAI*,[300] vol.safety*arXiv*, 2023. [https://ojs.aaai.org/index.php/HCOMP/article/view/27557](https://ojs.aaai.org/index.php/HCOMP/article/view/27557)[301] language*arXiv* S.*preprint*, 2023. exploring*arXiv*[302] *arXiv:2310.03031,2023.*M.*et*, “Ethical and*arXiv* lingual*arXiv:2112.04359,2021.* chatgpt,[303] Y. tificial*Language*ligent*arXiv*, 2023. *Technology*, vol.[304] “Auditable art*Journal*method *Informatics*, vol.uS [305] perience:“Deepchain: by*Chi*blockchain-based*IEEE* *computing*, 2022,*Secure*, vol. [306] O.A. languagedatasets*arXiv*, 2019. index*Available*[307] *4332664,2023.*D.*et*, “Bloom: A*arXiv* us:*5th*in*preprint*, 2022. *on*, 2011.[308] detection poisoning*arXiv*,[309] 2020.“A future*arXiv*, 2023. language*arXiv*[310] *arXiv:2305.00944,2023.*P. large*arXiv*, L.2023. in*Proceedings*[311] *European*concerns *Foundations*, 2022,[312] “Defending “"kellybackdoor*arXiv*, 2023. llm-generated*arXiv*,[313] 2023.“Universal*arXiv* *arXiv:2308.04748,2023.* elingInternational[314] *chine*. PMLR,of [315] threats,”*Preprints,November*out //doi.org/10.20944/preprints202311.0676.v1[316] chatgpt-based*arXiv* chatgpt*arXiv:2305.04764,2023.* [317] Aexpress detection*arXiv*, 2023.elicitation*ArXiv,vol.* [Online].Available: [318] Low,“In model-generatedtext*International* *Processing.Springer,* defense[319]*et*, “Agentsca: attacks,”*Proceedings*agent *tion*, 2023,[320] pp.X. large*arXiv*, 2023.

al.: Preprint submitted to ElsevierPage 23of24


---

<!-- Página 24 -->

[321]

[322]

[323]

[324]

[325]

[326]

[327]

[328]

[329]

[330]

[331]

[332]

[333]

[334]

[335]

[336]

[337]

[338]

[339]

[340]

[341]

[342]

Yifan Yao et

A SurveyonLarge LanguageModel(LLM)Security and

“White-box[343] els,”  of[344] networks,”arXiv, 2023.  X.[345] chatgpt*arXiv*, 2023.  M.[346] language*bioRxiv,pp.*  libraries,”[347] Champaign,  do[348] models*arXiv*, 2023.  based*arXiv*[349] *arXiv:2305.14328,2023.*  novel[350] jailbreak*arXiv* *arXiv:2309.05274,2023.* [351] tack*arXiv* *arXiv:2310.12439,2023.*  models,”arXiv, 2021.[352]  are attacks*arXiv*,[353] 2023.  models*arXiv* *arXiv:2309.10253,2023.*  Z. nlp:*arXiv* *arXiv:2306.04618,2023.*  Rank without*arXiv*, 2023.  “No test*arXiv*, 2023. et, “Building solution llms*arXiv*, 2023.  and generation,”arXiv, 2023.  federated*Knowledge-Based*, vol. 2021.  reconstruction *arXiv*, 2022.  llm: large  claims*arXiv* *preprint*, 2023.  Systematically*arXiv*

al.: Preprint submitted to Elsevier

Privacy:TheGood,theBad,andUgly

*preprint*, 2023.  does*arXiv*, 2023.  extraction confidence*arXiv*, 2023.  ing *arXiv:2305.13592,2023.*  triggers models,”arXiv, 2023.  B.*et*, “A models,”arXiv, 2023.  Y. generalization  P.*et*, “Lima:*arXiv* *arXiv:2305.11206,2023.*  Enhanced *arXiv*, 2019.  W.*et*, “Promptbench: ing *arXiv*, 2023.  models*arXiv* *arXiv:2305.09612,2023.*  and *communication,* *in* *Cipher*,

Page 24of24


---

