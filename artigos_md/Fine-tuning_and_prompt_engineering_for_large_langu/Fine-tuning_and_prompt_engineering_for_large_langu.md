<!-- Página 1 -->

InformationandSoftwareTechnology175(2024)107523

**Contents**

## Information and Software Technology

journal

## Fine-tuning and prompt engineering for large language models-based code

## review automation

∗

### Chanathip Pornprasit,

### Chakkrit Tantithamthavorn

***Monash***

### A B

### S

### T

### R

### A

### C

### T

### A R

### T

### I

### C

### L

### E

### I

### N

### F

### O

***Keywords:*****Context: The** **Modern****their** **Code****review** **Large****and** **GPT-3.5** **for** **Few-shot** **Objective: We** **Persona** **contexts,** **on** **generation** **Methods: We** **and** **code** **three** **Results: The** **EM** **achieves** **Conclusions: Based** **tuned** **cold-start** **Our** **deploying**

**1.****based****7****[** **textual** **Code****approaches****],** **opers****on**8 ]**5****[** **the** **CodeReviewer** **integrated** **approaches****1 – 3 ].** **quality,** **requires****machine** **with****were**1 – 3] **are****cess.**, 5 ] **not****Since** **automation****pensive,** **To****proaches** **review****fine-tuning** **model****5 ,** **on****9****al.****]** **6 ].**

∗**Corresponding** ***E-mail*****[chanathip.pornprasit@monash.edu](mailto:chanathip.pornprasit@monash.edu)**

**[https://doi.org/10.1016/j.infsof.2024.107523](https://doi.org/10.1016/j.infsof.2024.107523)** **Received** Availableonline11July2024 0950-5849/©).Published


---

<!-- Página 2 -->

***C.***

**LLaMa-Reviewer,** **approach****10 ].** **other****11 – 13]** **to** **code****14 ]** **pirical** **automation** **While****14 ]** **3.5** **limitations.****14 ]** **shot** **(i.e.,** **study.** **Fig.****An** **is** **although****15 – 17]** **prove****14 ]** **•****We****evaluate** **automation****difficult** **automation** **Open****Our****Third,****14 ]** **available****23 ].****learning,** **Paper****Section****learning****18 – 20].** **mulates****which** **study.****and** **experiment****In** **Section****code** **leveraged** **2.****LLMs****21 ])** **code****4 – 6 ]** **In****evaluation****1 , 4 ]****22 ].** **view****Through** **datasets****[ 5 ],****[ 6 ],****[ 4 ]),****review****data****data****data** **we** **(RQ1)*****2.1.*** **code** **Result.****The****Code** **73.17%–74.23%****14 ]****opers** **3-5****code** **fine-tuned****has** **(RQ2)****ensure** **code****expensive.** **Result.****The****feedback****24 , 25].** **63.91%–1100%****approaches****1 , 4 – 6,26]** **The****code** **revised****Code** **(RQ3)****eration** **for****between** **Result.****GPT-3.5** **inference** **higher** **code** **other** **review****1 – 3 ].** **achieves** **based** **is** **code****4 , 5 ]** **prompting** **based** **few-shot** **not** **Recommendation.****Based** **knowledge** **LLMs** **are** **highest** **tuning** ***2.2.*** **should** **Contributions.In** **Large****as** **to** **automation****•****We** **written****code** **Since****ence** **syntactical****persona).**


---

<!-- Página 3 -->

***C.***

**Table****review****5 , 6 , 9].****5 ]** **The****14 ].****posed** **Guo****14 ]****model****8 ].** **LLMs/approaches****GPT-3.5,****tion****4 – 6 ].** **CodeReviewer****[ 21 ],****ple,****5 ]** **[ 5 ]****[ 5 ],****6 ],** **transformer-based****D-ACT****4 ]** **the** **Include****No** **presented****.****LLMs?** **Model****refers** **Prompting****Zero-shot** **language****techniques****learning,****Few-shot** **unlabeled****Persona** **aims** **can** **have** **tasks****35 – 38].** **specifically** **LLMs** **example,** **On****18 , 30,31]** **such****27 ],****28 ],****21 ];** **ing***𝑁***demonstration** **commercial** {( 𝑥*, 𝑦 ) ,(𝑥**, 𝑦 ) ,…,(𝑥**, 𝑦*)} and1122*𝑁**𝑁* **However,***𝑥***and***𝑦***are***𝑖**𝑖* **quires****respectively.****13 ]** **1****quires****LLaMa2****29 ]****role** **requires****to** **duction** **GPUs*****2.3.*** **resources** **Recently,****14 ]****models.** **gate****approaches** **their****).****when** **First,**[ 14]are**large** **3.5.****In****14 ]****desirable** **best****Model****is** **there****learning** **few-shot****domain,** **systematic****different** **GPT-3.5** **Recently,** **is** **LLMs** **this** **proaches.****9 ]** **is****RQ1:** **tuned****10 ]****review** **tasks,** **Second,****a** **still****In****14 ]****comments** **performance****generate****9 ]** **ies****15 – 17]****that** **of****of** **makes****Inference****refers** **review** **model** **results.** **prompt** **question.** **tant** **LLMs****RQ2:** **2****have****For****review** **ing****18 , 30,31],****32 , 33],****32 , 33],** **Third,****consistency****34 ],****13 ].** **when****In****strategies** **et****14 ]****of-thought,** **for****18 – 20]****applicable** **that****for** **zero-shot** **from** **LLMs** **In** **conclude** **ing** **learning,** **suitable** **tion.** **question.**

**1****[https://gaming.lenovo.com/emea/threads/17314-The-hardware-behind-](https://gaming.lenovo.com/emea/threads/17314-The-hardware-behind-)****RQ3:** **ChatGPT****code** **2****[https://www.promptingguide.ai/](https://www.promptingguide.ai/)**


---

<!-- Página 4 -->

***C.***

**Fig.****An**

**Table****other** **Experimental****and** **#4** **randomly** **review)** **using** **Experimental** **the** **Prompting** **other** **#1**✗**few-shot****Zero-shot** **#2**✓ **3 , 4**✓**for** **#3**✗ **However,****Few-shot** **#4**✓ **select** **#5**✗ **Zero-shot****training** **#6**✓ ✗**templates.** **#7**✗ **Few-shot****from** **#8**✓ **model** **hyper-parameter**

**3.*****3.2.***

**Recently,**, 2 ]**In** **that****mental** **that** **not*****3.1.*** **new** **this****5**6 ],**]****The** **datasets,****when** **instead.****learning,**18 , 30,31],13 ]). **of**in**).****this** **Magicoder****21 ])** **•****CodeReviewer****:****]****data****code****, 9 , 14,39]:****[ 5 ],****data****GitHub** **Tufano****[ 6 ]****[ 4 ].****21****[****]****data****data****C#,** **iment** **contains** **and** **granularity),** **In** **code** **sented****.** **•****Tufano****:****]****data****we** **projects** **few-shot** **record** **learn** **view** **and** **being****6 ]****[ created** **are** **two****(with****data****where** **Tufano****(without****data****Finally,**×**6**×**3** **datasets).** **Fig.****3****[https://help.openai.com/en/articles/6654000-best-practices-for-prompt-](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-)** **the****engineering-with-openai-api** **4****sets.****[https://platform.openai.com/docs/guides/prompt-engineering/strategy-](https://platform.openai.com/docs/guides/prompt-engineering/strategy-)** **reviewers’****write-clear-instructions**


---

<!-- Página 5 -->

***C.***

**Table** **A****dataset****4 ]).****data** **Dataset**

**CodeReviewer****[ 5 ]**✓**data** **Tufano****[ 6 ]**✓ / ✗**data** **Android****4 ]**✗ **Google****4 ]**✗ **Ovirt****4 ]**✗

**•****D-ACT****:****4 ]****data** **three** **Ovirt).** **(function** **tion** **(function**

***3.3.***

**To** **select** **mance** **whole**randomfunction **bias** **to** **training** **the** **approximately** **fine-tune** **training** **approaches****4 – 6 ].** **training** **After** **Fig.****Prompt** **studied****simple**<lang>**refers** **5****vided****On****21 ],****omitted** **leverage** **called****40 ].**

**BM25****41 ]** ***3.4.*****engineering****41 ]** **6**gensim**package.** **In****testing****11 ]** **techniques:****demonstration** **explain****the** **For*****zero-shot*****,****highest** **3 , 4****sented****to****Then,****;** **that****the** **template****set;** **input****Finally,** **Then,****For persona [13],** **and****Fig.** **testing****ensure** **created****code** **For few-shot****[ 18 , 30,31],** **as****.*****3.5.*** **guidelines** **prompt****We** **examples,****the****21 ])** **and****automation****5 ],****6 ],** **In****D-ACT****4 ]).** **a** **1.****Exact****[ 4 – 6]****example** **code****a** **dataset.****BM25****41 ].****41 ]****12 , 42]** **ating****1 , 4 , 6].**

**5****[https://platform.openai.com/docs/guides/fine-tuning/create-a-fine-](https://platform.openai.com/docs/guides/fine-tuning/create-a-fine-)** **6****tuned-model****[https://github.com/piskvorky/gensim](https://github.com/piskvorky/gensim)**


---

<!-- Página 6 -->

***C.***

**Table** **The** **Approach****Inference** **Tuning** **Prompting**

✗**37.93%** ✓ ✓**37.70%** **Zero-shot** ✗**17.72%** **GPT-3.5** ✓**17.07%** ✗ ✗**26.55%** **Few-shot** ✓**26.28%**

✗**27.43%** ✓ ✓**27.98%** **Zero-shot** ✗**9.75%** **Magicoder** ✓**9.93%** ✗ ✗**15.89%** **Few-shot** ✓**17.80%**

**Guo****14 ]**✗**Zero-shot**✓**21.77%**

**CodeReviewer****5 ]****33.23%** **–** **TufanoT5****6 ] 11.90%**

**D-ACT****4 ] –**

**Table****4.** **The** **and** **In** **approaches.** **questions.** **Model** **(RQ1)****GPT-3.5** **code****Magicoder****21 ]** **TufanoT5****6 ]** **Approach.****To** **CodeReviewer****5 ]** **techniques** **D-ACT****4 ]** **GPT-3.5** **presented****)** **from****14 ].** **the** **Result.** **tokenize** **GPT-3.5** **compared** **[ 14 ] ’s****Table** **with****3.5,****14 ].** **value****when** **that****73.17%–74.23%** **2.****CodeBLEU[22]****approach****14 ],** **overlap****The** **Magicoder****model****43 ]** **approach****14 ].****evaluation** **GPT-3.5****in****5 , 6 ]****22 ]** **between****ignores** **ment)****In** **a****14 ]****match,** **the** **AST)** **never** **when** **(RQ2)** **code** **review** **cates****Approach.****To** **and****Section****.** **dataset.****from** **zero-shot** **Result.** ***3.6.*****GPT-3.5** **not****Table** **of****In** **1100%****using** **the** **gested****14 ]),** **achieve** **length** **The** **number** **CodeBLEU** **OpenAI** **tuning** **For****21 ],****directly** **to****for** **hyper-parameters****40 ]:***𝑟 ) (***of****from** **tuned****( 𝛼 )**


---

<!-- Página 7 -->

***C.***

**Fig.****(RQ3)**

**Fig.****Example**

**presented****in** **better****the** **fine-tuned.****Result.** **(RQ3)****higher** **for****in** **to****Approach.****To** **of****learning*****non*****GPT-3.5,** **used****respectively.**

**.**

**Table**


---

<!-- Página 8 -->

***C.***

**GPT-3.5****automation** **the****higher** **Recommendations****LLMs****and** **tomation****The** **reason****higher** **tuned****few-shot** **when****3.5** **problem),****prompt** **for****mitted** **the****demonstration** **forms****vised** **outperforms****comment.** **When** ***5.2.*****1.02%–54.17%** ***GPT-3.5*****input****Table** **in** **The****3.67%–54.17%** **fine-tuning****persona** **tomation****persona** **understand****learning** **that****compared** **qualitatively****The** **generate.****GPT-3.5** **correctly****CodeBLEU.** **revised****example** **others****learning** **interval****revised** **revised****without****.** **code****1 ]****Fig.** **changes****):****learning** **gests**logArg. **•*****fixing*****:****Fig.** **in****(use** **gory:****changing**Booleantobooleanand **method****the**sample_name**to**sampleName**in** **•*****refactoring:*****to**logArg. **changes** **Fig.** **changed** **3.5** **category:** **figure,**if condition. **ability;** **presents** **•*****other:******fixing*** **persona)** ***bug*****nor refactoring****will** **additional if statement**elseblock. **The****Fig.*****Fixing*** **prompts,*****Bug ,Refactoring*****and Other)** **the****generates.****(with****data** **prompts.****CodeReviewer****and****dataset,****data****data** **The****with** **using****code*****Refactoring*****and*****Other.*****data** **sona.****(without** **learning** **5.****According****,** **and** **In****used**other**across** **additional****all** **3.5.****the*****fixing*****and refactoring)** **in** ***5.1.*****not*****fixing*****or*****refactoring.*** **code*****other*****.** **GPT-3.5** **tuning****since*****5.3.*** **shows** **outperforms****4 – 6 ].****The** **results****the** **task****tuned** **with****20k**


---

<!-- Página 9 -->

***C.***

**Fig.****The****, GPT-3.5****and****categorized****and****refer****Zero-shot****Few-shot****Fine-tuned** **fine-tuned****refers****Fine-tuned**

**Table** **The**

**Size****CodeReviewer** **training** **EM**

**6%****6.02%****79.81%****3.05%****74.67%** **10%****80.68%****75.10%** **20%****38.80%****5.65%****76.04%****2.83%****75.46%**

**Table** **The****Fig.****).** **instructions****Fig.****).****Fig.****).**

**Prompt****Prompting** **design** **EM**

**P1****17.72%** **P2****Zero-shot** **P3**

**P1****26.55%** **P2****Few-shot** **P3**

**persona****10%** **3.5****persona** **use****Table** **7****steps,****as****.****3.5** **8****contains****as****.****GPT-3.5** **Table****12.07%** **achieves****that** **shot****is** **instruction****EM** **prompted****tuned** **smaller****fine-tuned** **with****with** **GPT-3.5** **The** ***5.4.*** **prompted** **290.00%** **In** **ple****44 , 45]** **found****7****[https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/)** **of****advanced-prompt-engineering?pivots=programming-language-chat-** **GPT-3.5****completions#break-the-task-down** **8****[https://www.promptingguide.ai/introduction/tips](https://www.promptingguide.ai/introduction/tips)****by**


---

<!-- Página 10 -->

***C.***

**a** **automation.**

***5.5.***

**Cost** **for** **9****cost****In** **cost** **is** **output** **1k** **tuning** **examples** **3.5** **output** **Assume** **review** **and** **1000×25×12=300,000** **for**×**0.002)** **with**× 0.0035) **learning**× 0.009)) **when** **Fig.****Prompt****10****erage****the** **instructions*****<lang>*****refers** **usage****The** **99.46%** **and** **respectively.** **3.5** **the** **3.5** **GPT-3.5** **leveraging** **considered**

**6.**

**We**

***6.1.***

**Threats** **niques** **design** **In****41 ]** **demonstration** **demonstration** **examples** **Thus,** **demonstration** **Since** **Fig.****Prompt** **patches*****an*****are*****<lang>*****refers** ***expert*****)****blue** **GPT-3.5** **However,** **neer,****with** **future****GPT-3.5** **find****achieves** **the** **The** **9****with****[https://openai.com/pricing](https://openai.com/pricing)** **10****other****[https://codesubmit.io/blog/s](https://codesubmit.io/blog/s)**


---

<!-- Página 11 -->

***C.***

**References*****6.2.***

**[1]****Threats** **Poshyvanyk,** **Magicoder,****translation,** **GPT-3.5****[2]** **Bavota,****Magicoder** **2021,****However,** **[3]** **sive** **AutoTransform:** **combinations****process,** **[4]****learning** **Chunyang****so** **under** **can** **[5]** **the****Majumder,** **code****investigate** **2022,****automation** **[6]** **Poshyvanyk,** ***6.3.*****automation,** **[7]** **Aidan** **Threats** **Proceedings** **ings****[8]** **aware****with****4 – 6 ].** **generation,****of** **[9]** **Thus,** **automation** **Another****in:** **[10]****in** **Lachaux,****from** **Azhar,** **preprint****.** **[11]****7.** **Michael** **tasks** **In****[12]** **3.5****Constructing** **empirical****fine-tuning** **[13]****learning,** **Gilbert,** **with****4 – 6 ].** **pattern** **sults****arXiv:2302.11382.** **[14]****automation** **Xin****without** **empirical****.** **the** **[15]** **should****Mishra,** **Sebastian****data** **J.****a** **[16]** **Lester,** **CRediT****zero-shot****.** **[17]** **Oliveira** **Chanathip****Writing** **Brockman,** **inal****Chakkrit****preprint****.** **[18]****Tantithamthavorn: Writing** **Prafulla** **Askell,** **Declaration****1877–1901.** **[19]** **testers:****The** **2023,** **cial****[20]** **influence****Xiaoguang** **Multi-intent** **[21]** **Data** **Source****.** **[22]** **Sundaresan,****Data** **automatic****.** **[23]** **Acknowledgment****review-automatiton.** **[24]** **Czerwonka,** **Chakkrit** **Softw.** **search****[25]** **Practices,****funding**


---

<!-- Página 12 -->

***C.***

**[36]****[26]** **code****Bavota,** **2024,****.****2021,** **[37]****[27]** **AI-assisted****qing** **2402.00247.****llama:****.** **[38]****[28]** **Huo,****Chenghao** **framework,****.****Starcoder:****.** **[39]****[29]** **Generation-based****Yasmine** **arXiv:2303.07221.****Bhosale,** **[40]****arXiv****.** **Wang,****[30]** **adaptation,****.****Chen,**3 ? **[41]****arXiv:2101.06804.** **BM25****[31]** **[42]****Chen,** **Evaluating****in-context****.** **generation,****.****[32]** **[43]****Shin,** **automatic****of** **311–318.****2305.14045.** **[44]****[33]** **Emad****Quoc** **friends****large** **pp.****[34]** **[45]****Aakanksha** **Yingjun****reasoning****.** **models****[35]** **2404.11595.****ing** **09950.**


---

