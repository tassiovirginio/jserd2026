<!-- Página 1 -->

1

# An Empirical

# Evaluation

# of

# Using

# Large

# Language Models

# for

# Automated

# Unit

# Test

# Generation

Max Schafer,Sarah Nadi,AryazEghbali,Frank Tip

**Abstract—Unit tests play a key role in ensuring the correctness of software. However, manually creating unit**is a laborious task, motivating the need for automation. Large Language Models (LLMs) have recently been applied to various aspects of software development, including their suggested use for automated generation of unit tests, but while requiring additional training or few-shot learning on examples of existing tests. This paper presents a large-scale empirical evaluation on the effectiveness of LLMs for automated unit test generation without requiring additional training or manual effort. Concretely, we consider an approach where the LLM is provided with prompts that include the signature and implementation of a function under test, along with usage examples extracted from documentation. Furthermore, if a generated test fails, our approach attempts to generate a new test that fixes the problem by re-prompting the model with the failing test and error message. We implement our approachESTPinILOTT, an adaptive LLM-based test generation tool for JavaScript that automatically generates unit tests for the methods in a given project’s API. We evaluate TESTPILOTusing OpenAI’sgpt3.5-turbo LLM on 25 npm packages with a total of 1,684 API functions. The generated tests achieve a median statement coverage of 70.2% and branchof 52.8%. In contrast, the state-of-the feedback-directed JavaScript test generation technique, Nessie, achieves only 51.3% statement coverage and 25.6% branch coverage. Furthermore, experiments with excluding parts of the information included in the prompts show that all components contribute towards the generation of effective test suites. We also find that 92.8%ESTof T ILOT’s generated tests have≤ 50% similarity with existing(as measured by normalized edit distance), with none of them being exact copies. Finally, weESTrunP ILOTTwith two additional LLMs, OpenAI’s older code-cushman-002 LLM and StarCoder, an LLM for which the training process is publicly documented. Overall, we observed similar results with the former (68.2% median statement coverage), and somewhat worsewith the latter (54.0% median statement coverage), suggesting that the effectiveness of the approach is influenced by the size and trainingof the LLM, but does not fundamentally depend on the specific model.

**Index Terms—test generation, JavaScript, language models**

✦

**1 I****NTRODUCTION**due totheuseofunintuitivevariablenames[20].Second, the generated tests often lack assertions [21], or only containUnit testscheckthecorrectnessofindividualfunctionsor very genericassertions(e.g.,thatadereferencedvariableother unitsofsourcecode,andplayakeyroleinmodern must notbe**null), or**toomanyspuriousassertions[22].software development[1]–[3].However, creatingunittests While such tests can provide inspiration for manually craft-by hand is labor-intensive and tedious, causing some devel- ing high-coveragetestsuites,theydonotlooknaturalandopers to skip writing tests altogether [4]. generally cannot be used verbatim.This facthasinspiredextensiveresearchontechniques Given thesedisadvantages,therehasrecentlybeenin-for automatedtestgenerationincludingfuzzing[5],[6], creasing interestinutilizingmachinelearning-basedcode-feedback-directed random test generation [7]–[11], dynamic generation techniquestoproducebetterunittests[23]– arXiv:2302.06527v4 [cs.SE] 11 Dec 2023symbolic execution[12]–[15],andsearch-basedandevolu- [29]. Specifically, theseresearcheffortsleverageLLMsthattionary techniques[16],[17].Atahighlevel,mostofthese have been trained on large corpora of natural-language texttechniques usestaticordynamicanalysistoex- and source code.We are specificallyinterested inplore control and data flow paths in the program, and then transformer modelsthat, whengivenasnippetoftextorattempt togenerateteststhatmaximizecoverage.While source code(referredtoastheprompt), willpredicttextthey areoftensuccessfulingeneratingteststhatexpose that islikelytofollowit(henceforthreferredtoasthefaults, these techniques have two major shortcomings. First, completion). ItturnsoutthatLLMsaregoodatproducingthe generatedtestsaretypicallylessreadableandunder- natural-looking completionsforbothnaturallanguageandstandable thanmanuallywrittentests[18],[19],especially source code,andtosomeextent“understand”theseman- tics ofnaturallanguageandcode,basedonthestatistical•M. Sch¨afer is withUK E-mail: [max-schaefer@github.com](mailto:max-schaefer@github.com)relationships onthelikelihoodofseeingaparticularword •S. Nadi is with the University of Alberta, Canadain agivencontext.SomeLLMssuchasBERT[30]orGPT- E-mail: [nadi@ualberta.ca](mailto:nadi@ualberta.ca) 3 [31]aretrainedpurelyontextextractedfrombooksand•A. Eghbali is with the University of Stuttgart, Germany other publicsources,whileotherslikeOpenAICodex[32]E-mail: [aryaz.egh@gmail.com](mailto:aryaz.egh@gmail.com) •F.Tip is with Northeastern University, USAand AlphaCode [33] are put through additional training on E-mail: [f.tip@northeastern.edu](mailto:f.tip@northeastern.edu)publicly availablesourcecodetomakethembettersuited


---

<!-- Página 2 -->

2

and whetherornottheycontainassertionsthatactuallyfor software development tasks [34]–[43]. exercise functionalityfromthetargetpackagenon-trivial(Given theproperties ofLLMs,itisreasonable toexpect assertions). Wealsoempiricallyevaluatetheeffectofthethat they may be able to generate natural-looking tests. Not various components of our prompt-crafting strategy as wellonly aretheylikelytoproducecodethatresembleswhat EST PILOTis generating previously memorizeda humandeveloperwouldwrite(including,forexample,as whether T tests from the LLM’s training data.sensible variablenames),butLLMsarealsolikelytopro- duce testscontainingassertions,simplybecausemostUsing OpenAI’scurrent mostcapableandcost-effective 1in theirtrainingsetdo.Thus,byleveragingLLMs,onemodelgpt3.5-turbo,T ESTPILOT’s generatedtestsachievea might hopetosimultaneouslyaddressthetwoshortcom-median statementcoverageof70.2%,andbranch ings oftraditionaltest-generationtechniques.Ontheotherof 52.8%.Wefindthatamedian61.4%ofthegenerated hand, one would perhaps not expect LLMs to produce testscontain non-trivial assertions, and that these that cover complex edge cases or exercise unusual functiontests aloneachieveamedian61.6%coverage,indicating inputs, asthesewillberareinthetrainingdata,makingthat thegeneratedtestscontainmeaningfuloraclesthat LLMs more suitable for generating regression tests than forexercise functionality from the target package. Upon deeper bug finding.examination, wefindthatthemostcommonreason forthe There hasbeensomeexploratoryworkonusingLLMsgenerated teststofailisexceedingthetwo-secondtimeout for testgeneration.Forexample,Bareißet al.[25] evaluatewe enforce,usuallybecauseofafailuretocommunicate the performanceofCodexfortestgeneration.Theyfollowtest completiontothetestingframework.Wefindthat, a few-shotlearningparadigmwhere theirprompt includeson average,theadaptiveapproachisabletofix15.6% the functiontobetestedalongwithanexampleofanotherof failingtests.Ourempiricalevaluationalsoshowsthat function andanaccompanyingtesttogivethemodelanall fivecomponentsincludedinthepromptsareessential idea of what a test should look like. In a limited evaluationfor generatingmeaningfultestsuiteswithhighcoverage. on 18Javamethods,theyfindthatthisapproach comparesExcluding any of these components results in either a higher favorably to feedback-directed test generation [8]. Similarly,proportion offailingtestsorinreducedcoverage.Onthe Tufanoetal.’sATHENATEST[26] generatestestsusingaother hand, while excluding usage examples from prompts BART transformermodel[44]fine-tunedonatrainingsetreduces effectivenessoftheapproach,itdoesnotrenderit of functionsandtheircorrespondingtests.Theyevaluateobsolete, suggestingthattheLLMisabletolearnfromthe on fiveJavaprojects,achievingcomparablecoveragetopresence of similar test code in its training set. EvoSuite [17]. While these are promising early results,Finally,fromexperimentsconductedwiththegpt3.5- approaches, aswellasothers[29],[45],[46],relyonaturboLLM, wenotethathighcoverageisstillachievedon training corpusoffunctionsandtheircorrespondingtests,packages whose source code is hosted on GitLab (and thus which is expensive to curate and maintain.has notbeenpartoftheLLM’strainingdata).Moreover, In this paper, we explore the feasibility of automaticallywe findthat60.0%ofthetestsgeneratedusingthe generating unittestsusingoff-the-shelfLLMs,withnoturbo LLM have ≤ 40% similarity to existing tests and 92.8% additional trainingandaslittlepre-processingaspossible.have≤50% similarity, withnoneofthetestsbeingexact Following ReynoldsandMcDonell[47],wepositthatpro-copies. This suggests that the generated tests are not copied viding the model with input-output examples or performingverbatim from the LLM’s training set. additional training is not necessary and that careful promptIn principle, the test generation approach under consid- crafting is sufficient. Specifically, apart from test scaffoldingeration canbeusedwithanyLLM.However, theeffective- code, ourprompts contain(1)thesignature ofthefunctionness oftheapproachislikelytodependontheLLM’ssize under test;(2)itsdocumentationcomment,ifany;(3)us-and training set. To explore this factor, we further conducted age examplesforthefunctionminedfromdocumentation,experiments withtwoadditionalLLMs:thepreviouspro- if available;(4)itssourcecode.Finally,weconsideranprietary code-cushman-002 [48] model developed by OpenAI adaptive componenttoourtechnique:eachgeneratedtestandStarCoder[49], anLLMforwhichthetrainingprocess is executed, and if it fails, the LLM is prompted again withis publiclydocumented.We observedqualitativelysimilar a specialprompt including(5)thefailingtestandtheerrorresults usingcode-cushman-002(median coverageof68.2% message itproduced,whichoftenallowsthemodeltofixfor statements,51.2%forbranches),andsomewhatworse the test and make it pass.results using StarCoder (54.0% and 37.5%). Toconductexperiments,wehaveimplementedthese In summary, thispapermakesthefollowingcontribu- techniques inasystemcalledTP ILOT, anLLM-based tions: test generatorforJavaScript.WechoseJavaScriptasan •A simpletestgenerationtechniquewhereunittestsareexample ofapopularlanguageforwhichtest generated by iteratively querying an LLM with a promptusing traditional methods is challenging due to the absence containing signaturesofAPIfunctionsundertestand,of static type information and its permissive runtime seman- optionally,thebodies,documentation,andusageexam-tics [11].Weevaluateourapproachon25npmpackages ples associatedwithsuchfunctions.Thetechniquealsofrom variousdomainshostedonbothGitHubandGitLab, features an adaptive component that includes in a promptwith varyinglevels ofpopularity andamounts ofavailable error messages observed when executing previously gen-documentation. Thesepackageshaveatotalof1,684API erated tests.functions thatweattempttogeneratetestsfor.Weinves- tigate thecoverageachievedbythegeneratedtestsand their qualityintermsofsuccessrate,reasonsforfailure, 1. [https://platform.openai.com/docs/models/gpt-3-5](https://platform.openai.com/docs/models/gpt-3-5)


---

<!-- Página 3 -->

3

to completeagivencodefragment,onemighttherefore 1**let**mocha'' ); expect ittogeneratetherestofthetestforus.Comments 2**let**assert'' ); can beincludedinthetestskeletontoprovideadditional3**let**pkg' package-under-test'); 4information about the function that may be useful to guide 5//the LLM towards generating better tests. 6

7describe('test' ,**function()** **2.1 T****ESTPILOT****Architecture**8it( 'test' ,**function(done)** 9//Figure 2presentsthehigh-levelarchitecture ofESTT P ILOT, 10})which consistsoffivemaincomponents:GivenaPUT 11}) as input,theAPI exploreridentifies functionstotest;the documentation minerextracts metadataaboutthem;andtheFig. 1: Illustration of the structure of prompts and tests. prompt generator, test validator, andrefinercollaborate to construct prompts for test generation, assemble complete tests fromtheLLM’sresponse,runthemtodetermine•An implementationofthistechniqueforJavaScriptina whether theypass,andconstructfurtherpromptstogen-tool calledTEST PILOT, whichisavailableasopen-source erate more tests. We now discuss each of these componentssoftware at [https://github.com/githubnext/testpilot](https://github.com/githubnext/testpilot). in more detail.•An extensiveempiricalevaluationofTP ILOTon 25 **API Explorer:**This componentanalyzesthePUTtonpm packages,demonstratingitseffectivenessingen- determine itsAPI,i.e.,thesetoffunctions,methods,con-erating testsuiteswithhighcoverage.Ourevaluation stants, etc. that the package exposes to clients. In JavaScript,explores the following aspects: it is very difficult to determine the API statically due to the**–**Quality of the generated tests in terms of the assertions highly dynamic nature of the language. Therefore, similar tothey contain,andcoverageofteststhatincludenon- other JavaScripttest-generationwork[10],[11],wepursuetrivial assertions. an approachbasedondynamicanalysis.Inparticular,we**–**Effect of excluding various prompt components. load the application’s main package and apply introspection**–**Similarity of generated tests to existing tests. to traverse the resulting object graph and identify properties**–**Comparison againstNessie[11],astate-of-the-art that are bound to functions. For each function, we record itsfeedback-directed random test generation technique for access path (that is, the sequence of properties that must beJavaScript. traversed toreachitfromthemainmodule),itssignature**–**Comparison oftheeffectoftheunderlyingLLMon (which in the absence of static type information is simply aT ESTPILOT’s generated tests. list of parameter names), and its definition (that is, its source The raw data and analysis for all our experiments can be code). TheoutputoftheAPIExplorerisalistoffunctions found at [https://doi.org/10.6084/m9.figshare.23653371](https://doi.org/10.6084/m9.figshare.23653371). described by their access paths, signatures, and definitions; other API elements are ignored. **Documentation Miner:**This componentextracts**2 A****PPROACH** code snippets and comments from documentation included T ESTPILOTgenerates testsusingthepopularJavaScript with thePUT, andassociatesthemwiththeAPIfunctions testing framework Mocha [50] with its BDD-style syntax in they pertainto.Theaimistocollect,foreachAPIfunc- which testsareimplementedascallbackfunctionsthatare tion, commentsandexamplesdescribingitspurposeand passed to theit function. Test suites consist of one or more intended usage.InJavaScript codebases,documentationis calls toitthat occurinacallbackfunctionthatispassed typically providedintheformofMarkdown. md() files,in to thedescribefunction. Assertionsarecheckedusingthe which codesnippetsareembeddedasfencedcodeblocks built-in Node.js assert module. (i.e., blocks surrounded by triple backticks). We find all such Figure 1illustratesthestructure ofgeneratedtestsfora blocks in all Markdown files in the code base, and associate functionf. Here, lines 1–3 are boilerplate code for importing with each function the set of all code snippets that textually the testing libraries and the Package under Test (PUT). These contain the function’s name. While this is a simple heuristic, are followedbyoneormore commented-outlinescontain- code examples may not be complete or syntactically correct, ing function metadata included in the prompt, as we explain so amoresophisticatedapproachrelyingonparsingor shortly.Lines7–8beginthedefinitionofatestsuiteusing static analysisisnotlikelytoworkwell.We alsoassociate describewith asingletestdefinedasacallbackfunction each APIfunctionwiththedoccomment/**.(. . */) that accepting aparameterdonepassed totheitfunction. The immediately precedes it, if any. test codeusesassertto checkitsassertions,andfinally invokesdone()to signalcompletion.ThisisnecessaryforThe remainingthreecomponentsaretheprompt gener- asynchronous teststhatmaytakemultipleiterationsoftheator , thetest validator, andtheprompt refiner, whichwork JavaScript event loop to finish. Callingdone()more than oncetogether togenerateandvalidatetestsforallAPIfunc- results inaruntimeerror, whilenotcallingitatallcausestions identifiedbytheAPIExplorer, usingtheinformation the test to fail with a timeout error.provided bytheDocumentationMiner. Functionsarepro- cessed oneatatime,andforeachfunctiononlyonetestThe basic idea of our approach is to send the initial part is generatedatatime(asopposedtogeneratinganentireof theabovetestskeletonupto(butnotincluding)the test suiteatonce).Thisistoenableustovalidateeachteststart oftheactualtestcodeonLine9(highlightedabove individually without interference from other tests.in blue)asaprompttotheLLM.SinceLLMsaretrained


---

<!-- Página 4 -->

4

### prompt

readFile(f, cb)

readFileSync(f)

### explorer

Fig. 2: Overview of the adaptive test generation technique we useESTin PT. 1**let**mocha'' );1**let**'' ); 2**let**assert'' );2**let**'' ); 3**let**countries_and_timezones' countries-and-timezones');3**let**'' ); 4//4// 5describe('test' ,**function()**5//' countries-and-timezones'); 6it( 'test' ,**function(done)**6// 7**let**country' US ');7//' DE '); 8assert.equal(country.name,' United' );8// 9assert.equal(country.timezones.length,);9// 10assert.equal(country.timezones[0],' America/New_York');10// this function ..11assert.equal(country.timezones[1],' America/Chicago');11// 12done();12// 13})13//

### prompt

### prompt

14})14//' DE ', 15//' Germany', 16//' Europe/Berlin',' Europe/Zurich'] 17// 18// 19// 20// 21describe('test' ,**function()** let x = 22it( 'test' ,**function(done)** 23**let**country' DE '); readFile(f, cb)24assert.equal(country.id,' DE '); 25assert.equal(country.name,' Germany'); 26assert.equal(country.timezones[0],' Europe/Berlin'); 27assert.equal(country.timezones[1],' Europe/Zurich'); 28done(); 29}) 30}) **(a) (b)**

Fig. 3: Examples of prompts (highlighted) and the completions provided by the LLM, comprising complete tests. Prompt (a) contains no snippets and the test generated from it fails. Prompt (b)one snippet and thetest passes.

**Test**Validator: Next, we send the generated prompts**Prompt Generator:**This componentconstructsthe to LLM and wait for completions. We only consume as manyinitial prompttosendtotheLLMforgeneratingatest tokens as are needed to form a syntactically valid test. Sincefor agivenfunctionf. Asmentionedabove,weinitially there is no guarantee that the completions suggested by thehave (atmost)fourpiecesofinformationaboutfat our model aresyntacticallyvalid,thetestvalidatortriestofixdisposal: itssignature,itsdefinition,itsdoccomment,and simple syntacticerrorssuchasmissingbrackets,andthenits usagesnippetsextractedfromdocumentation.Whileit parses the resulting code to check whether it is syntacticallymight seemnaturaltoconstructaprompt containingallof valid. Ifnot,thetestisimmediatelymarkedasfailed.this information,inpracticeitcansometimeshappenthat Otherwise it is run using the Mocha test runner to determinemore complexpromptsleadtoworsecompletionsasthe whether it passes or fails (either due to an assertion error orLLM getsconfusedbytheadditionalinformation.There- some other runtime error).fore, wefollowadifferentstrategy:westartwithavery simple initialpromptthatincludesnometadataexceptthe Each returned completioncanbeconcatenatedwiththefunction signature, and then let the prompt refiner extend it prompt toyieldacandidatetest.However,toallowustostep by step with additional information. eliminate duplicatetestsgeneratedfrom different prompts, we post-processthecandidatetestsasfollows:westrip

### candidate

### fi

### ner


---

<!-- Página 5 -->

5

**Algorithm 1**Pseudo-code for API exploration.uniquely represents an API method, andsig is the signature of a function. Our notion of an access path takes a somewhat1:**function exploreAPI(pkgName)** 2:modObj ← object created by importingpkgNamesimplified form compared to the original concept proposed 3:seen ←by Mezzettietal.[51],andconsistsofapackagename 4:**return explore(pkgName,modObj,seen)** followed by a sequence of property names. 5:**function explore(accessPath,obj,seen)** WerelyonadynamicapproachtoexploretheAPI6:apis ← 7:**if obj ̸∈ seen then**of apackagepkgName, bycreatingasmallprogramthat 8:seen ← seen ∪obj }imports thepackage(line2),andrelyingonJavaScript’s 9:**if obj is a function with signature**sig then introspective capabilities to determine which properties are10:apis ← apis ∪accessPath,sig⟩ present inthe package rootobjectmodObjthat iscreatedby11:**else if obj is an****then** 12:props ←prop | obj has a propertyprop }importingpkgNameand whattypesthesepropertieshave. 13:**for prop in props do**Exploration ofmodObj’s properties is handled by a recursive 14:apis ← apis ∪ functionexplorethat beginsattheaccesspathrepresenting15:explore(extend(accessPath,prop),obj[prop],seen) the packagerootandthattraversesthisobjectrecursively,16:**else if obj is an array****then** 17:**for each index i in the arraydo**calling another auxiliary functionextendtothe access 18:apis ← apis ∪path as the traversal descends into the object’s structure. 19:explore(extend(accessPath,prop),obj[i],seen) During exploration, if an object is encountered at access 20:**return apis** pathawhose typeisafunctionwithsignaturesig , thena 21:**function extend(accessPath,component)** pair ⟨a,sig⟩ is recorded (line 10). If the typepofis an object,22:**if component is numeric then** then theobjectsreferenced byitsproperties are recursively23:**return accessPath[component ]** 24:**else**explored (lines15–15),andifthetypeofis anarray, then 25:**return accessPath.component**p ’s properties are explored recursively as well (lines 17–19). **Test**Generation:Algorithm 2showspseudo-code for thetestgenerationstep.Thealgorithmbeginsbyini- out thecommentcontainingthefunctionmetadatainthetializing theset promptsof generatedprompts,thesettests prompt andreplacethedescriptionsinthedescribeanditof generatedpassingtests,andthesetseencontaining all calls withthegenericstrings'test'and' test' ,generated teststotheemptysetandbyusingAlgorithm1 respectively.to obtaintheset apisof (accesspath,signature)pairsthat **Prompt Refiner:**TheRefiner applies a num-constitute the package’s API (lines 2–5). Then, on lines 6–7, ber ofstrategiestogenerateadditionalpromptstousefor each such pair, a base prompt is constructed and added for queryingthemodel.Overall,weemployfourprompttoprompts, containingonlytheaccesspathandsignature, refiners as follows:using thetemplateillustratedinFigure1.Next,lines9– 1)FnBodyIncluder: Ifp did not contain the definition off , a27 createadditionalpromptsbyaddingthefunctionbody, prompt is created that includes it.example usagesnippets,anddocumentationcommentsex- 2)DocCommentIncluder: Iffhas adoccommentbutpdidtracted fromthecodetopreviouslygeneratedprompts. not include it, a prompt with the doc comment is created.Here, therefinefunction extendsapreviouslygenerated 3)SnippetIncluder: If usage snippets forfare available butpprompt byaddingthefunctionbody, examplesnippets,or did not include them, a prompt with snippets is created.doc comment. The order in which each type of information, 4)RetryWithError: If t failed with error messagee , a promptif included, appears in prompts is fixed as follows: example is constructedthatconsistsof:thetextofthefailingtestsnippets, error message from previously generated test, doc tfollowed byacomment// thetestabovefailswithcomments, function body, signature. the followingerror:e , followedbyacomment// fixedThe while loop on lines 29–44 describes an iterative pro- test. This strategy is only applied once per prompt, socessitforgeneratingteststhatcontinuesaslongasprompts is not attempted ifp itself was already generated by thisremain thathavenotbeenprocessed.Ineachiteration,a strategy.prompt is selected and removed fromprompts, and the LLM is queried for completions (line 31). For eachcompletion thatThe refinedpromptisthenusedtoconstructatestin was received,atestisconstructedbyconcatenatingthethe samewayastheoriginalprompt.Allstrategiesare prompt andthecompletion(line33)andminorsyntacticapplied independently and in all possible combinations, but problems are fixed such as adding missing} ’ characters atnote thatthefirstthreewillonlyapplyatmostonceand the end of the test (line 34). Moreover, we remove commentsthe fourthwillneverapplytwiceinarow, thusensuring from the test to enable deduplication of tests that only differtermination. in their comments (line 35). If theresultingtestissyntacticallyvalidandthesame **2.2 Algorithm**Detailstest was not encountered previously, it is executed (line 38). Wenowprovideadditionaldetailonthetwokeystepsofwe do not re-execute it but still link the prompt our approach: API exploration and test generation.to the previously seen test. If the test executed successfully, we additto tests(line 40).Ifitfailed(duetoanassertion**API Exploration:**Algorithm 1showspseudocode failure, nontermination,orbecauseofanuncaughtexcep-that illustrateshowthesetoffunctionsthatconstitutethe andifthetestwasnotderivedfromapromptthatAPI forapackageisidentified.Thealgorithmtakesa fromapreviousfailingtest(line42),thenpackage undertest, pkgName, andproducesalistofpairswas constructed we createanewpromptcontainingthefailedtestandthe⟨ a, sig⟩representing itsAPI.Here,ais anaccess paththat


---

<!-- Página 6 -->

6

**Algorithm 2**Pseudo-code for test generation.

1:**function generateTests**( pkgName, LLM) 2:prompts ← 3:tests ← 4:seen ← 5:apis ← exploreAPI(pkgName)▷ See Algorithm 1 6:**for api ∈ apis do** 7:prompts ←∪createBasePrompt(api)}▷ create basecontaining only the signature, see Figure 1 8: 9:promptsWithFnBody←▷ refine prompts by adding function body 10:**for prompt ∈ prompts do** 11:body ∈ findFnBody(prompt.api.accessPath,. api . sig) 12:promptsWithFnBody←∪ refine(prompt,body) 13:prompts ←∪ promptsWithFnBody 14: 15:promptsWithExamples←▷ refine prompts in cases where example snippets are available 16:**for prompt ∈ prompts do** 17:snippets ← findExamples(prompt.api.accessPath,. api . sig) 18:**if snippets ̸**∅ then 19:promptsWithExamples←∪ refine(prompt,snippets) 20:prompts ←∪ promptsWithExamples 21: 22:promptsWithDocComments←▷ refine prompts in cases where doc comments are available 23:**for prompt ∈ prompts do** 24:docComment ← findDocComments(prompt.api.accessPath,. api . sig) 25:**if docComment ̸**∅ then 26:promptsWithDocComments←∪ refine(prompt,docComment) 27:prompts ←∪ promptsWithDocComments 28: 29:**while prompts ̸**∅ do 30: selectand removeprompt from prompts 31:completions ← getCompletions(LLM,prompt.text)▷ requestfrom the LLM 32:**for completion ∈ completions do** 33:test ← concatenate(prompt, completion) 34:test ← fixMinorSyntaxIssues(test)▷ e.g., add missing close parentheses 35:test ← removeComments(test) 36:**if test is syntactically validand test ̸∈ seen then** 37:seen ← seen ∪test} 38:result ← executeTest( test )▷ execute the test 39:**if result.status = ok then**▷ add successful test totests 40:tests ←∪test} 41:**else**▷ result.status=assertionFailureor.= crash or.= nonTermination 42:**if prompt was not constructed from a previous failed test****then**▷ apply error retry refiner ′43:prompt← refineFromError(test,result.errorMessage) ′44:prompts ←∪prompt} 45:**return tests**

Next, we refine this prompt to include the usage snippeterror message and add it to. as shown in the highlighted part of Figure 3(b). This enablesWhen theiterativeprocessconcludes,thesettestsis the LLMtogenerateatestincorporatingtheinformationreturned (line 45). provided in this snippet, which passes when executed. 3Weshow another example in Figure 4 fromquill-delta, **2.3 Examples** a packageforrepresentingandmanipulatingchangesto Tomakethediscussionmoreconcrete,wewillnowshowdocuments. Asbefore, Figure 4(a)showstheinitialprompt two examples of how ESTPILOTgenerates tests.forquill-delta’sconcatmethod, whichconcatenatestwo As thefirstexample,weconsiderthenpmpackagechange sets, and a test that was generated from this prompt. 2countries-and-timezones.API explorationrevealsthatthisIt isnoteworthythattheLLMwasabletogeneratea package exportsafunctiongetCountrywith asinglepa-syntactically correcttestfor quill-delta, wherearguments rameteridand theproject’sREADME.mdfile providesausagesuch as example.1[{: ' Hello'}, 2{: ',::}Figure 3(a) shows a test for this function generated from 3{: ' World!'}] the initialhighlightedpromptthatonlyincludesthefunc- are passed to the constructoreven in the absence of any usagetion signature,butnoothermetadata.Thistestfailswhen examples. Most likely, this is becausequill-deltais a popularexecution reachestheassertiononline8becausetheex- package withmorethan1.2millionweeklydownloads,pression country.name evaluates to"United StatesofAmerica", which meansthattheLLMislikelytohaveseenexampleswhich differs from the value"United States"expected by the of its use in its training set.assertion.

3. See [https://github.com/quilljs/delta](https://github.com/quilljs/delta).2. See [https://www.npmjs.com/package/countries-and-timezones](https://www.npmjs.com/package/countries-and-timezones).


---

<!-- Página 7 -->

7

1**let**mocha'' );1**let**'' ); 2**let**assert'' );2**let**'' ); 3**let**quill_delta' quill-delta');3**let**'' ); 4//4// 5describe('test' ,**function()**5' test' ,() 6it( 'test' ,**function(done)**6it( 'test' , 7**let**delta1**new**quill_delta([{: ' Hello'},7**let****new**: ''}, 8{: ',8{: ', 9attributes:: true}9:: true} 10{: ' World!'}]);10{: ''}]); 11**let**delta2**new**quill_delta([{: ' Hello'},11**let****new**: ''}, 12{: ',12{: ', 13attributes:: true}13:: true} 14{: ' World!'}]);14{: ''}]); 15**let**delta315**let** 16assert.equal(delta3.ops.length,);16); 17done();17

18})18}) 19})19

20// 21// 22// 23it( 'test' ,**function(done)** 24**let**delta1**new**quill_delta([{: ' Hello'}, 25{: ', 26attributes:: true} 27{: ' World!'}]); 28**let**delta2**new**quill_delta([{: ' Hello'}, 29{: ', 30attributes:: true} 31{: ' World!'}]); 32**let**delta3 33assert.equal(delta3.ops.length,); 34done(); 35}) 36}

### (a) (b)

### Fig. 4:

### Example

### illustrating

### how

### a

### prompt

### is

### refined

### in

### response

### to

### the

### failure

### of

### a

### previously

### generated

### test.

### Prompt

### contains no

### information

### except

### the

### method

### signature,

### and

### the

### test

### generated

### from

### it

### fails.

### Prompt

### (b)

### adds

###

### about the test failure, and the generated test passes.

### Nevertheless, the

### test

### in

### Figure

### 4(a)

### fails

### because

### when

### RQ1

### How much statement coverage and branch

### do tests

### reaching the

### assertion

### on

### line

### 16

delta3.ops.length

### has the

### generated by

### T ESTPILOT

### achieve? Ideally,

### the

### value

5 , whereas

### the

### assertion

### expects

### the

###

6 . The

### tests would achieve high coverage to ensure that most

### reason for

### the

### assertion’s

### failure

### is

### the

### fact

### that

### the

### of the

### API’s

### functionality

### is

### exercised. Given

### that

### our

### method merges

### adjacent

### elements

### if

### they

### have

### the

### same

### goal is

### to

### generate

### complete

### unit

### test

### suites

### (as

### op-

### attributes. Therefore,

### when

### execution

### reaches

### line

### 16,

### the

### posed to bug finding), we measure statement coverage

### array delta3.ops will hold the following value:

### for passing testsonly. We report coverage on both the

1[

### package level and function level.

2{: ' Hello'},

### RQ2

### How does

### T ESTPILOT’s

### coverage

### compare

### to

### Nessie

### [11]?

3{: ',::}

### We

### compare

### T ESTPILOT’s coverage

### to

### the

### state-of-

4{: ' World!Hello'},

### the-art JavaScript

### test

### generator,

### Nessie,

### which

### uses

5{: ',::} 6{: ' World!'}

### a feedback-directed approach.

7]

### RQ3

### How many

### of

### T ESTPILOT’s

### generated

### tests

### contain

### non-

### and therefore delta3.ops.length will have the value

5 .

### trivial assertions?

### A test

### with

### no

### assertions

### or

### with

### In response to this failure, the Prompt Refiner will create

### trivial

### assertions such

### as

assert.equal(true,) may

### the prompt shown in Figure 4(b) from which a passing test

### still achieve high coverage. However, such tests do not

### is generated. In this test, the expected value in the assertion

### provide useful oracles. We examine the generated tests

### has been updated to

5 , as per the assertion error message.

### and measure the prevalence of non-trivial assertions.

### Note that

### all

### these

### tests

### look

### quite

### natural

### and

### similar

### RQ4

### What are the characteristics of

### T ESTPILOT’s

### failing tests?

### to tests

### that

### a

### human

### developer

### might

### write,

### and

### they

### We

### investigate

### the

### reasons

### behind

### any

### failing

### gener-

### exercise typical

### usage

### scenarios

### (rather

### than

### edge

### cases)

### of

### ated test.

### the functions under test.

### RQ5

### How does each of the different types of information included

### in prompts contribute

### to

### the

### effectiveness

### of ESTPILOT’s

## 3 R

### ESEARCH

## Q UESTIONS

## & E VALUATION

## S ETUP

### generated tests?

### To

### investigate

### if

### all

### the

### information

### included in prompts through the refiners is necessary

### 3.1 Research

### Questions

### to generate effective tests, we disable each refiner and

### Our evaluation aims to answer the following research ques-

### report how it affects the results.

### tions.

### (a)


---

<!-- Página 8 -->

8

TABLE1: Overview of npm packages used for evaluation, ordered by descending popularity in terms of downloads/wk. The top 10 packages correspond to the Nessie benchmark, the next 10 are additional GitHub-hostedwe include, while the last 5 are GitLab-hosted packages.

**RQ6**AreT ESTPILOT’sgeneratedtestscopiedfromexistingan additional5packageswhosesourcecodeishostedon 4tests?Sincegpt3.5-turbois trainedonGitHubcode,itGitLab. is likelythattheLLMhasalreadyseenthetestsofTable1showsthatthe25packagesvaryintermsof our evaluationpackagesbeforeandmaysimplybe popularity (downloads/week)andsize(LOC),aswellas producing copiesoftestsit“memorized”.We inves-in termsofthenumberofAPIfunctionstheyoffer andthe tigate thesimilaritybetweenthegeneratedtestsandextent of the available documentation. The “API functions” any existing tests in our evaluation packages.columns showthenumberofavailableAPIfunctions;the **RQ7**How muchdoesthecoverageofT ESTPILOT’sgeneratednumber andproportionofAPIfunctionsthathaveatleast tests relyontheunderlyingLLM?Tounderstandtheone examplecodesnippetinthedocumentation(“w/ex- generalizability ofanLLM-basedtestgenerationap-amples”); and the number and proportion of API functions proach and the effect of the underlying LLMESTTP I -that haveadocumentationcomment(“w/comment”).We **API**relies on,wecomparecoveragewe Weeklyobtainusing**Package**LOTalso show the total numberTotalof example snippets available in**Existing** **#****Tests****Downloads****Examples**gpt3.5-turbowith twootherLLMs:(1)OpenAI’scode-the documentation of each package. glob cushman-002model [48],oneof gpt3.5-turbo’s prede-Toanswer**RQ1–RQ6**, werunTEST PILOTusing thefs-extra graceful-fscessors whichispartoftheCodexsuiteofLLMs[52]gpt3.5-turbo LLM (versiongpt-3.5-turbo-0301), sampling fivejsonfile 5bluebirdand whichservedasthemainmodelbehindthefirstcompletions ofupto100tokensattemperature zero,withq rsvprelease of GitHub Copilot [38], and (2)[49], aall otheroptionsattheirdefaultvalues.In, weuse memfs publicly available LLM for which the training processnode-dirsamesettingsforcode-cushman-002and StarCoder, except zip-a-folderis fully documented.that thesamplingtemperatureforthelatteris0.01sinceit js-sdsl not supporta temperatureof zero.quill-delta complex.js Note thatLLM-basedtestgenerationdoesnothaveapull-stream countries-and-timezonestest-generation budgetpersesinceitisnotaninfinitesimple-statistics **3.2 Evaluation**Setuppluralprocess. Instead,weasktheLLMforatmostfivecomple- dirty geo-pointtions for every prompt (but the model may return less). We uneval1answertheaboveresearchquestions,weuseabench- deduplicate the returned tests to avoid inflating the number image-downloadermark of25npmpackages.Table1showsthesizeand crawler-url-parser0generatedtests.For example,iftwopromptsreturnthe gitlab-js14 each ofofdownloads(popularity)ofthesepack- same test (modulo comments), we only record this test oncecore ages. The first 10 packages shown in the table are the sameomnitoolbut keep track of which prompt(s) resulted in its generation. GitHub-hosted packagesusedforevaluatingNessie[11], While wesetthesamplingtemperatureaslowaspos- a recentfeedback-directedtest-generationtechniquefor sible, thereisstillsomenondeterminisminthereceived JavaScript. However,wenoticethatthese10packages responses. Accordingly,werunallexperiments10times. primarily focusonpopularI/O-relatedlibrarieswitha All theper-packagedatapointsreportedinSection4are callback-heavy style,soweadd10newpackagesfrom dif- ferent domains(e.g.,documentprocessinganddatastruc- 4. We checkedsimilarly-namedrepostoensurethattheyarenot tures), programmingstyles(primarilyobject-oriented),asmirrored on GitHub. well as less popular packages. Sincegpt3.5-turbo (as well as5. Intuitively speaking,thesamplingtemperaturecontrolstheran- domness of the generated completions, with lower temperatures mean-the otherLLMsweexperimentwithin) wastrained ing lessnon-determinism.Languagemodelsencodetheirinputandon GitHubrepositories,wehavetoassumethatallour output usingavocabularyoftokens,withcommonlyoccurringse- subject packages(andinparticulartheirtests)were partofquences ofcharacters(suchas**require, but**alsocontiguousrunsof the model’strainingset.Forthisreason,wealsoincludespace characters) represented by a single token.


---

<!-- Página 9 -->

9

TABLE2: Statement and branch coverage forESTT P ILOT’s passing tests, generated usinggpt3.5-turbo. We also show tests that uniquely cover a statement. The last two columns show Nessie’s statement and branch coverage for each package. Note that Nessie generates 1000 tests per package and the reported coverage is for all generated tests.

7median valuesoverthese10runs,exceptforinteger-typedrepository.Including theextractedexamplesnippetsfrom data suchasnumberoftestswhereweusetheceilingofexternalrepositoryincreasestheachievedcoverageto **EST****P****ILOT which****Nessie****Tests**the medianvalue.LoadingFor RQ6, withoutlossofgenerality, we43.6%,suggeststheimportanceofincludingusage**Project** **Stmt**present the similarity numbers based on the first run only.examples in the prompts. We examine the effect of the infor- glob**71.3%**4(Section 4.5).WeuseIstanbul/nyc[53]tomeasurestatementandmation included in prompts in detail in fs-extra**58.8%**17 It isworthnotingthatTP ILOT’s coverageforthebranchanduseMocha’sdefaulttimelimitof2sgraceful-fs**49.8%** jsonfile**91.5%**GitLab projects listed in the bottom 5 rows of Table 2 rangesper test.bluebird**68.0%**26 from 51.4%to78.3%.ThisdemonstratesthatESTT P ILOTisq**70.4%**53.7%**54.4%** rsvp**70.1%**6effective at generating high-coverage unit tests for packagesmemfs**81.1%**40

### 4 E

**VALUATION**

### R ESULTS

node-dir**65.4%**it has not seen in its training set. zip-a-folder**88.0%** **Branch Coverage: We also show the branch coverage****4.1 RQ1:**T**ESTPILOT’s**Coveragejs-sdsl**33.9%**18 achievedbythepassingtestsinTable2.We findthatthequill-delta**73.0%**8 Table2showsthenumberoftestsESTTP ILOTgeneratescomplex.js**70.2%**10branch coverageperpackageisbetween16.5%and71.3%,pull-stream**69.1%**11for eachpackage,thenumber(andproportion)ofpassingcountries-and-timezones**96.0%**with amedianof52.8%.Similartostatementcoverage,the simple-statistics**87.8%**14tests, and the corresponding coverage achieved by the pass- achieved branchcoverageisalsomuchhigherthantheplural**73.8%**1 ing tests.ThefirsttwocolumnsofTable2alsoshowthedirty**74.5%**2loading coveragewithadifferenceof15.9%–71.3%andageo-point**87.8%**1coverage obtainedbysimplyloadingthepackage( unevalmediandifferenceof 50.0%. coverage). Thisistheweget“forfree”withoutimage-downloader**63.6%**0Since achieving branch coverage is generally harder than crawler-url-parser**73.9%**having anytestsuite,whichweprovideasapointofachieving statement coverage, it is expected that the branchgitlab-js**55.3%** reference forinterpretingourresults.Overall,9.9%–80.0%core**78.3%**5coverage for the generated tests is lower than the statement omnitool**74.2%**90of the tests generated by TP ILOTare passing tests, withcoverage. However, we note an interesting casegitlab-jsin **Median**16.1%**70.2%**10.5%a median of 48.0% across all packages. We now discuss thewhere thisdifferenceseemsmorepronounced(51.7%vs. different coverage measurements of these passing tests.16.5%). Uponfurtherinvestigationofitssourcecodeand **Statement Coverage**: Thestatementcoverageperdocumentation, we find thatgitlab-jsoffers various config- package achieved by the passing tests ranges between 33.9%uration options and parameters to specify the GitLab reposi- and 93.1%,withamedianof70.2%.We notethatacross alltory to connect to and use/query (e.g., its url, authentication packages, theachievedstatementcoverageismuchhighertoken, search parameters to use for a query). The processing than the loading coverage with a difference of 19.1%– 88.2%of theseoptionsisreflectedinthemainbranchinglogic 6and a median difference of 53.7%.in thecode.WhileTEST PILOTdoes attempttogenerate The lowest statement coverage TP ILOTachieves is onreasonable teststhatcalldifferentendpointswith js-sdsl, at 33.9%. Upon further investigation of this package,options, itsometimesstrugglestofindthecorrectfunction we findthatitmaintainsthedocumentationexamplesthatcall touse,resultingintypeerrors.Ingeneral,alarge appear onitswebsiteasmarkdownfilesinaseparateproportion of the tests TP ILOTgenerates for this package fail, and thus do not contribute to our coverage numbers. It 6. For someoftheprojects weshare withNessie,ourloadingcov- is alsoworthnotingthatproperlytestingsuchapackageerage differsfromtheonereportedintheirpaper. We contactedthe would requiremocking,butwedidnotobserveanyofauthors, who confirmed that with recent versions of Istanbul/nyc they obtained the same numbers as we did, except for a very small difference on memfs (29.1% vs 29.3%), which may be due to platform differences.7. [https://github.com/js-sdsl/js-sdsl.github.io/tree/main/start](https://github.com/js-sdsl/js-sdsl.github.io/tree/main/start)


---

<!-- Página 10 -->

### 1.0

### 0.8

### 0.6 contributing, meaning that they cover at least one statement

### 0.4

### 0.2

### 0.0

Statement Coverage per Function

10

the generatedteststousemocking.Inthefuture,itwould be interestingtoinvestigateifincludingmockinglibraries in theprompt,orothermockingrelatedinformation,may result in the model using mocking when needed. **Coverage per function**: Figure5 shows the distribu- tion ofstatementcoverageperfunctionforeachpackage. Each boxcorrespondstooneofourbenchmarkpackages and eachdatapointinaboxrepresents thestatementcov- erage for a function in that package. The median statement coverage per function for each package is shown in red. Overall, the median statement coverage per function for a givenprojectrangesfrom0.0%–100.0%,withamedian Fig. 5:Distributionofstatementcoverageperfunctionforof 77.1%.To ensurethatTP ILOTis notgeneratinghigh T ESTPILOT’s generated tests usinggpt3.5-turbo.coverage tests only for smaller functions, we run a Pearson’s correlation test between the statement coverage per function and the corresponding function size (in statements). We find9ditional feedback-directedapproach.For eachpackage, no statistically significant correlation between coverage and Nessie generates 1000 tests, for which we measure statement size, indicatingthatTEST PILOTis notonlydoingwellfor and branchcoverageinthesamewayasforESTTP ILOT.8smaller functions. Wethenrepeatthesemeasurements10timesandtakethe As expected,Figure5showsthatformostpackages, median coverage across the 10 runs to follow a similar setup T ESTPILOTdoes wellforsomefunctionswhileachieving to T ESTPILOT’s evaluation. We use a Wilcoxon paired rank- low coverage for others. Let us takejsonfileas an example. sum testtodetermineiftherearestatisticallysignificant In Table 2, we saw that its statement coverage at the package differences between the coverage achieved by both tools. level is 38.3%. From Figure 5, we see that statement coverage The lasttwocolumnsofTable2showstatementand per functionrangesfrom0%to100%,withamedianof branch coverageforNessie.WenotethatNessiecould almost 50%.Divingintothedata,wefindthatthereare not runonuneval, becausethemodule’sonlyexportisa two functionsthatTEST PILOTcannot cover,becausetheir function, which Nessie does not support. For the remaining corresponding generated tests fail either due to references to 24 packages,Nessieachieved4.7%–96.0%statementcov- non-existent files TEST PILOTincludes in the tests or because erage, withamedianof51.3%.Incontrast,asshownin they timeout.However,thefunctionsthatESTTP ILOTis Table2,T ESTPILOT’s medianstatementcoverageismuch able tocoverhavestatementcoveragerangingfrom58%- higher at70.2%.Thedifferenceinbranchcoverageiseven 100%. We canobservesimilarbehaviorwithotherfilesys- higher,with 52.8% for ESTPILOTvs 25.6% for Nessie. Both tem dependent packages, such asgraceful-fsorfs-extra. At these differences arestatisticallysignificant(p-values0.002 the otherendofthespectrum,weseezip-a-folderwhere and 0.027respectively)withalargeeffectsize,measured T ESTPILOTachieves bothhighstatementcoverageatthe by Cliff’sdelta[55],of0.493forstatementcoverageand package level(84%)aswellashighstatementcoverage10a mediumone(0.431)forbranchcoverage.Note that at thefunctionlevelinFigure5wheretheminimumper Nessie always generates 1000 tests per package, whileESTT- function coverage is 75%. P ILOTusually generatesfarfewertests,exceptonmemfs **Uniquely Contributing Tests**: To further understand andomnitool. ItisalsoworthemphasizingthatNessie(and the diversityofthegeneratedtests,Table2alsoshows other test-generation techniques such as LambdaTester [56]) how manyofthetestsTP ILOTgenerates areuniquely report coverage ofall generated tests, regardless of whether they passorfailwhileourreportedcoveragenumbersare that noothertestscover.Amedianof10.5%ofthepass- for passing tests only. ing testsareofthiskind,withsomepackagesashighas Wenowdiveintotheresultsatthepackagelevel. 100.0%. These results are promising because they show that For eachpackage,Table2highlightsthehighercoverage T ESTPILOTcan generateteststhatcoveredgecases,but from thetwotechniquesinbold. ESTTP ILOToutperforms there is clearly some redundancy among the generated tests. Nessie on17ofthe24packages(glob,fs-extra,blue- Of course,wecannotsimplyexcludeall89.5%remaining bird, q,rsvp,memfs,js-sdsl,quill-delta,complex.js,pull- tests withoutlosingcoverage,sincesomestatementsmay stream, simple-statistics,plural,dirty,geo-point,image- be coveredbymultipletestsnon-uniquely.Exploringtest downloader,core,omnitool),increasingcoverageby3.6%– suite minimization techniques [54] to reduce the size of the 74.5%, withamedian30.0%increase.For7ofthere- qgenerated test suite is an interesting avenue for future work. maining packages(graceful-fs,jsonfile,node-dir,zip-a- rsvp dirty

globfolder,countries-and-timezones,crawler-url-parser,gitlab- plural

js-sdsl

uneval

memfs

jsonfile

fs-extra**4.2 RQ2**T**ESTPILOT****vs. Nessie**9. Note thatNessie’simplementationhasbeenrefactoredandim- bluebird

node-dir proved afterthepublicationoftheoriginalpaper,whichiswhy geo-point

quill-delta

graceful-fs

complex.jsWecompareT ESTPILOT’s coveragetothestate-of-the-artsome ofthevaluesinthistabledifferslightlyfromthepub- pull-stream

zip-a-folder lished numbers.Nessie’sfirstauthorhaskindlyhelpedusruntheJavaScript testgeneratorNessie[11],whichusesatra- improved version(specifically, [https://github.com/emarteca/nessie/](https://github.com/emarteca/nessie/) tree/86e48f1d038d98dcd2663d6d36a58a70c4666b1b) on all 25 packages. simple-statisticsWeinclude the Nessie results in our artifact8. Exact correlationcoefficientsandp-valuesareprovidedinour artifact.10. All effect sizes for all statistical tests are available in our image-downloader

countries-and-timezones

crawler-url-parser

gitlab-js

core

omnitool


---

<!-- Página 11 -->

11

1**let**manuelmhtr_countries_and_timezones"../../TEST_REPO_manuelmhtr_countries_and_timezones"); 2module.exports**function()** 3**let**ret_val_manuelmhtr_countries_and_timezones_1; 4**try**{ 5ret_val_manuelmhtr_countries_and_timezones_1 6Promise.resolve(ret_val_manuelmhtr_countries_and_timezones_1).catch(e"error_1":}); 7}**catch(e)** 8console.log({"error_1":**true});** 9} 10**let**ret_val_manuelmhtr_countries_and_timezones_2; 11**try**{ 12ret_val_manuelmhtr_countries_and_timezones_2 13manuelmhtr_countries_and_timezones.getCountry({"k":293.76984807333383, 14"rHMR":17.71151399309167, 15"vSF6":, 16"l" :, 17"EnL":611.9090030925536}); 18Promise.resolve(ret_val_manuelmhtr_countries_and_timezones_2).catch(e"error_2":}); 19}**catch(e)** 20console.log({"error_2":**true});** 21} 22}

Fig. 6: Example of a test generated by Nessie. Highlighted lines are for debugging purposes only and do not contribute to the testing of the package under test.

js), T ESTPILOTachieves lowercoveragethanNessie.ForTable3showsthenumberoftestswithnon-trivialas- these packages,itreducescoverageby0.5%–53.2%,withsertions (non-trivial testfor short)andtheirproportion w.r.t a median3.6%decrease.WealsonotethatNessiefailsto generatedtestsfromTable 2.Thetablealsoshowsthe achieve any branch coverage on 3 projects (dirty, geo-point,number andproportion oftheseteststhatpass,alongwith core), while the statement coverage for these projects is non-thethey achieve. zero. Uponfurtherexamination,andafterconsultingtheWeobservethatthereisonlyonepackage, Nessie authors,wefoundthatcannotgeneratetestsimage-downloaderwhere TEST PILOTgenerates onlytrivial that instantiateclasses,meaningthatstatementcoverageistests. Whilethegeneratedtestsforimage-downloaderdid barely aboveloadingcoverageforpackageswithaclass-include callstoitsAPI,theywereallmissingassert based API, while the branch coverage is zero.statements. Acrosstheremainingpackages,amedianof 94.6%ofTP ILOT’s generatedtestsperpackageAside fromthedifferenceincoverageachievedby 9.1% – are non-trivial.Amedianof61.4%ofthegeneratedtestsNessie andT ESTPILOT,bytend for agivenpackagearenon-trivial.Whencomparedtoto lookquitedifferentfromtheonesgeneratedbyESTT- tests,wecanalsoseethatonlyaslightlyP ILOT, whichstemsfromNessie’srandomapproachto all generated lower proportion of non-trivial tests pass (median 48.0% fortest generation.Toillustratethis,Figure6showsanex- overall passingtestsfromTable 2vs.43.7%fornon-trivialample ofatestgeneratedbyNessiethatexercisesthe passing testsfromTable3).BoththeseresultsshowthatgetCountryfunction ofcountries-and-timezones. As can be seen T ESTPILOTtypically generatestestswithassertionsthatin thefigure,thetestuseslongvariablenamessuchas exercise functionality from the target package.ret_val_manuelmhtr_countries_and_timezones_1that hamper read- ability.Moreover, thetestinvokesgetCountryon lines13–17The coverageachievedbythenon-trivialtestsalsosup- with an object literal that binds random values to some ran-ports thisfinding.Specifically, whencomparingthestate- domly namedproperties,whichdoesnotreflectintendedment coverageforallthegeneratedtestsinTable2to use oftheAPI.Moreover,testsgeneratedbyNessiedothat fornon-trivialinTable3,wefindthatthedif- not containanyassertions.Bycontrast,testsgeneratedbyference rangesfrom0.0%–84.0%,withamediandifference T ESTPILOTfor thesamepackage(seeFigure3)typicallyof only7.5%.Thismeansthattheachievedcoveragefor use variablenamesthataresimilartothosechosenbymost packagesmainlycomesfromexercisingAPIfunc- programmers, invokeAPIswithsensiblevalues,andoftentionality thatistestedbythegeneratedoracles.Wenote contain assertions.however thatthereare4packages(jsonfile,node-dir,zip- a-folder,image-downloader) where non-trivial tests achieve 0% statement coverage, causing the larger differences. Apart **4.3 RQ3:**Non-trivial Assertionsfromimage-downloaderdiscussed above,thethreeremaining packages do not have any passing non-trivial tests. Since weWedefine aassertion as anthat depends calculate coverageforpassingtestsonly, thisresultsintheon atleastonefunctionfromthepackageundertest.To 0% statement coverage for the non-trivial tests.identifyassertions,wefirstuseCodeQL[57]to compute abackwardsprogramslicefromeachassertion in thegeneratedtests.We considerassertionswhoseback- **4.4 RQ4:**Characteristics of Failing Tests wards slice contains an import of the package under test as non-trivial assertions.WethenreportgeneratedteststhatFigure 7 shows the number of failingfor each package, contain at least one non-trivial assertion.along with the breakdown of the reasons behind the failure.


---

<!-- Página 12 -->

12

TABLE3: Number (%) of**non-trivialTESTPILOT**tests gener- ated using gpt3.5-turbo and the resulting statement coverage from the passing non-trivial tests.

Fig. 8:EffectofdisablingpromptrefinersinESTT P ILOT, usinggpt3.5-turbo.Fullconsiders allrefinerswhileBase includes only the function signature and Mocha scaffolding.

11simply adding a call todone. Wefindthatamedian19.2%offailuresareassertion errors, indicatingthatinsomecasesgpt3.5-turbois notable to figureoutthecorrectexpectedvalueforthetestoracle. This isespeciallytruewhenthepackageundertestisnot**Passing****Project****Non-trivial**widely usedandnoneoftheinformationweprovidethe **Tests**(%) model canhelpitinfiguringoutthecorrectvalues.For glob example, inoneofthetestsforgeo-point, TESTPILOTwasfs-extra graceful-fsable tousecoordinates intheprovided examplesnippetto jsonfile correctly constructtwogeographicalcoordinatesasinputbluebird qfor thecalculateDistancefunction, whichcomputesthedis-rsvp memfstance betweenthetwocoordinates.However, ESTTP ILOT node-dirincorrectly generated131.4158102876726astheexpectedzip-a-folder value forthedistancebetweenthesetwopoints,whilethe js-sdsl correct expectedvalueis130584.05017990958;thiscausedquill-delta complex.jsthe testtofailwithanassertionerror.Wenotethatinpull-stream countries-and-timezonesthis specificcase,whenTP ILOTre-prompted themodel simple-statisticswith thefailingtestanderrormessage,itwasthenabletoplural dirtyproduce a passing test with the corrected oracle. On average geo-pointacross the packages, we find that theRetryWithError refineruneval was able to fix 11.1% of assertion errors.image-downloaderWithout Error MsgsWithout Doc Comments crawler-url-parserFinally,wenotethatfile-systemerrorsaredomainspe- gitlab-jsWithout Function BodyBase PromptWithout Example Snippetscific. ThegeneratedtestsforpackagesinthefilesystemAssertion ErrorsFile System ErrorsCorrectness ErrorsTimeout ErrorsOthercore omnitooldomain, such asfs-extra or memfs, have a high proportion of100% glob7:Typesoferrors61.4%in thefailedtestsgeneratedby**Median**failingdue to such errors. This is not surprising given fs-extraT ESTPILOT, using gpt3.5-turbo.that thesetestsmayrelyonfilesthatmaybenon-existent graceful-fs or require containing specific content. Packages in the otherjsonfile domains do not face this problem.80%bluebird Assertion errorsoccurwhentheexpectedvalueinanas-Overall, wefindthatre-promptingthemodelwiththeq sertion doesnotmatchtheactualvaluefrom executingtheerror messageoffailingtests(regardlessofthefailurerea-rsvp code. File-system errors includesuch as files or direc-son) allows TEST PILOTto produce a consequent passing testmemfs beingfound,whichweidentifybycheckingfor60% tories notin 15.6% of the cases.node-dir zip-a-folderfile-systemrelatederrorcodes[58]inthestacktrace. js-sdslCorrectness errorsincludealltypeerrors,syntax**4.5 RQ5:**Effect of Prompt Refiners quill-deltareference errors,incorrectinvocationsofdone, andinfinite ValueOur resultssofarincludetestsgeneratedwithallfourcomplex.js40% recursion/call stack errors. Timeout errors occur when tests prompt refinersdiscussedinSection2.InthisRQ,wepull-streamexceed the maximum running time we allow them (2s/test). countries-and-timezonesinvestigate the effect of each of these refiners on the qualityFinally,wegroupallotherapplication-specificerrorswe simple-statisticsof thegeneratedtests.Specifically, weconductanablationobserve under Other. pluralstudy wherewedisableonerefineratatime.Disabling20%Wefind that the most common failure reason is timeoutsdirty with a median 22.7% of failing tests, followed by correctnessgeo-point11. While theinsertionofmissingcallstomay seemstraight- errors (particularlytypeerrors)withamedianof20.0%offorward andthereforebeamenabletoautomatedrepair,itcanbeuneval surprisingly trickytofindthecorrectlocationswheretoinsertsuchfailing tests.Themajorityoftimeoutsareduetomissingimage-downloader calls, and handling this correctly would require applying static analysis0%crawler-url-parsercalls todone , causingMochatokeepwaitingforthecall. to thegeneratedtest.We therefore optedforanautomatedapproach gitlab-jsWenote that on average, theRetryWithErrorrefiner was able

### coverage

### non

### % passing

that relies solely on the LLM but will consider the use of static analysis coreto fix15.4%ofsuchtimeouterrors,withthemodeloftento repair generated tests as future work.

### trivial

### tests

omnitool

### coverage

0100200300400500600700

### Metric

Number of failing tests


---

<!-- Página 13 -->

13

1**let**mocha'' );1**let**'' ); 2**let**assert'' );2**let**'' ); 3**let**complex_js' complex.js');3**let**'' ); 4//4// 5describe('test' ,**function()**5// 6it( 'test' ,**function(done)**6//' im '] 7assert.equal(complex_js.ZERO.valueOf(),);7//' re ']; 8done();8// 9})9// 10})10// 11describe('test' ,**function()** 12it( 'test' ,**function(done)** 13assert.equal(complex_js.ZERO.valueOf(),**null);** 14done(); 15}) 16}) **(a) (b)**

Fig. 9:Exampleofarefinementnegativelyinfluencingtestgeneration.Prompt(a)containsnoinformationexceptthe method signature, and the generated test passes. Prompt (b) adds the body of the method, but thetest fails.

a refinermeansthatwenolongergeneratepromptsthatin alargedropinthepercentageofpassingtests.This include the informationit provides. Forexample, disablingsuggests that the refiners are effective in guiding the model DocCommentIncludermeans thatnoneofthepromptswe towards generatingmorepassingtests,evenifthisdoes generate would contain documentation comments. We thennot necessarilyresultinadditionalcoverage.We findthat compare thepercentageofpassingtests,theachievedcov-acrossallpackages, afullconfigurationalwaysleadstoa erage, as well as the coverage by non-trivial tests (higher percentageofpassingforagivenAPI,while coverage).maintaining high coverage. Figure 8 shows our results. The x-axisthe metricsTounderstandifthedifferencesbetweenthedistribu- we compareacrossthedifferentconfigurationsshownin tions weobserveinFigure 8are statisticallysignificant,we the legend.They-axisshowsthevaluesforeachmetriccompare theresultsofeachpairofconfigurationsforall (all percentages).Eachdatapointinaboxplotrepresentsthree metricsusingaWilcoxon matchedpairssignedrank the results ofthespecificmetricforagivenpackage,usingtests. NotethatwhencomparingagainstDocCommentIn- the correspondingrefinerconfiguration.Theblacklineincluder, wecomparedistributionsforonlythe8packages the middleofeachboxrepresentsthemedianvalueforthat contain doc comments. Wefindastatisticallysignificantdifference betweentheeach metric across all packages. The full configuration is the fullandeachthatdisablesanyconfiguration we presented so far (i.e., all refiners enabled). wellasbetweenthebaseconfigurationandeachThe otherconfigurationsshowtheresultsofexcludingrefiner as of theotherconfigurations.Comparedtothefullconfigu-only oneoftherefiners.Forexample,theredboxplot ration, thelargesteffectsizeweobservedforashows theresultswhendisablingtheSnippetIncluder(i.e., refiner wasonpassingtestswheneitherFnBodyIncluderorWithout ExampleSnippets). Thebasepromptconfiguration were disabled(Cliff’sdelta0.582andcontains onlythefunctionsignatureandtestscaffoldingDocCommentIncluder 0.531 respectively).(i.e., disablingallrefiners).Note,however,thatonly8 Apart from differences with the full and base configura-of thepackagesinourevaluationcontaindocumentation tion, we find no statistically significant differences betweencomments. Itdoesnotmakesensetocomparetheeffectof the pairsofotherconfigurationsexceptforthefollowingdisabling theDocCommentIncluderon packagesthatdonot cases: Wefindthatforbothpassingtestsandcoverage,contain doc comments in the first place. Therefore, while the there isastatisticallysignificantdifferencebetweenthedistributions showninallboxplotsrepresent25packages, configuration thatdisablesFnBodyIncluderand thatwhichtheWithout DocCommentscontainsdatafor disables RetryWithError(medium and negligible effect sizes,only 8 packages. respectively). Forpassingtests,wealsofindastatisticallyOverall, wecanseethatthefullconfigurationout- significant difference between disablingFnBodyIncluder andperforms allotherconfigurations,acrossallthreemetrics, disabling eachofSnippetIncluderandDocCommentIncluderimplying thatallthepromptinformationweincludecon- (small and medium effect sizes, respectively). However, wetributes togeneratingmoreeffectivetests.Wefindthat note thatasamplesizeof8istoosmalltodrawanythere wasnotasinglepackagewheredisablingarefiner conclusionsfor DocCommentIncluder. Itisparticularlyled tobetterresultsonanymetric.With theexceptionof valid4 interesting toseethattherewasnostatisticallysignificantpackages wheredisablingoneoftherefinersdidnotaffect difference betweendisabling SnippetIncluderandthe results(oncrawler-url-parseranddirty; any oftheotherrefiners.Thissuggeststhattheabsenceofand RetryWithErroron gitlab-js and zip-a-folder), disabling a refineralwaysresulted inlowervaluesinatleastone example snippets does not necessarily affect the metrics any more than the absence of any of the information provided bymetric. The contributionsoftherefinersareespeciallynotablethe other refiners. Since Figure 8 shows that we still obtain a for thepercentageofpassingtestswheredisablinganyofhigh median coverage even whenSnippetIncluder, the refiners(e.g., FnBodyIncluderorSnippetIncluder) resultsthis suggeststhatthepresenceofexamplessnippetsis


---

<!-- Página 14 -->

14

it( 'test' ,**function(done)** bluebird.resolve().then(function() **throw**( ' test'); }).catchThrow().catch(function(err) assert.equal(err.message,' test'); }). finally(done); }); **(a)**

it( "1, function() **return**Promise.resolve().then(function() **throw**(); }).then(assert.fail,**function(e)** assertLongTrace(e,,1 ]); }); }); **(b)**

Fig. 10:CumulativepercentofTP Igenerated testFig. 11:ExampleofaTP Itestcasefor cases, using gpt3.5-turbo, with maximum similarity less thanbluebird(a), and an existing test case (b) with0.62. the similarity value shown on the x-axis.

∗not essentialforgeneratingeffectivetestsuiteswithhightis agivengeneratedtest,anddistis theeditdistance coverage, andthatTEP Iis applicableevenincasesbetween a generated test and an existing test. We follow the where no documentation examples are present.same methodforcalculatingmaximumsimilarityforeach Finally,wenotethatwhiletheoverallresultsacrossagenerated test,usingthenpmLevensteinpackage[61]to given packageshowthattherefinersalwaysimprove,orcalculate dist. at least maintain, coverage and percentage of passing tests, Figure 10 shows the cumulative percentage of generatedthis does not mean that a refiner always improves the results tests cases for each project where the maximum similarity isfor an individual API function. We have observed situations less than the value on the x-axis. We also show this cumula-where addinginformationsuchasthefunctionimplemen- tive percentage forallgenerated test cases across all projects.tation toapromptthatdoesnotincludeitconfusesthe find that 6.2% of ETP Igenerated test cases havemodel, resulting in the generation ofa failing test. FigureWe9 less than≤0 . 3%maximum similaritytoanexistingtest,shows an example for thecomplex.jspackage: given the base 60.0% have≤0 . 4similarity,92.8%have≤0 . 5 , 99.6%haveprompt ontheleft, gpt3.5-turbois abletoproducea(very ≤0 . 6 while 100.0% of the generated tests cases have≤0 . 7 .simple) passingtestforthevalueOfmethod oftheconstant EP Inever generates exact copies ofZEROexported bythepackage;addingthefunctionbodyThis means that T existing tests. In contrast, while 90% of Lemieux et al. [27]’syields the prompt on the right, which seems to confuse the Pythontestshave≤0 . 4similarity,2%oftheirmodel, resulting in the generation of a failing test. Across all 100%test casesareexactcopies.Thatsaid,giventhedifferencespackages, 5,367 prompts were generated by applying one of between testing frameworks in Python and JavaScript (e.g.,the refiners, and in only 394 cases (7.3%) the refined prompt Mocha requires more boilerplate code than pytest), similar-was less effective than the original prompt in the sense that ity numberscannotbedirectlycomparedbetweenthetwoa passingtestwasgeneratedfrom theoriginalprompt, but languages.not from the refined prompt. 80% Tofurtherillustratetheresultingsimilaritynumbers,**4.6 RQ6:**Memorization Figure 11showsanexampleofatestcasefrombluebird Since gpt3.5-turbo was trained on GitHub code, some of thewith 0.62similaritytoanexistingtestcase.Whiletheedit existing testsincludedinourbenchmarksmayhavebeendistance here is low, resulting in the high similarity, we can part ofitstrainingset.ThisraisestheconcernthatET I -see that the tests have semantic differences. For example, the60% Lmay be memorizing existing tests, rather than generat-generated test simply checks that the thrown exception is a ing new ones, limiting its usefulness for packages it was notglobpull-streamtype error, whiletheexistingtestchecksforcertainvalues trained on. To investigate potential effects of memorization,fs-extracountries-and-timezonesin thetrace.Thus,the7.2%oftestcaseswegeneratewith we measure the similarity between each generated test andgraceful-fssimple-statistics>0 . 5similarity donotposeaconcernthat ETP Iis the existingtestsinthebenchmarks(numberofjsonfilepluralgenerating memorizedtestcases.Finally, wewouldexpect40% tests shown in Table 1). Recently, Lemieux et al. [27] reportedbluebirddirtythe generatedtestsforGitLab-hostedprojectstohavea that codeplagiarismorclonedetection[59]techniquesqgeo-pointlower similarity to existing tests since, as far as we know, the are noteffectiveatidentifyingLLMcodememorization.rsvpunevaltraining set for OpenAI’s models only includes projects from Instead, theyfindthatmeasuringsimilaritythroughedit Cumulative Percent of Test CasesGitHub, so the model is less likely to have seen the existing distance [60] produces more meaningful results. They definenode-dircrawler-url-parsertests during training. Our results do indeed show that three20% maximum similarityas a metric that measures the normalizedzip-a-foldergitlab-jsout of the five projects have a maximum similarity≤of0 . 4 , highest similarity between a given generated test and all ex-js-sdslcorewith theremainingtwohavingmaximumsimilarityof0.5.∗dist (t,t)p,isting testsasfollows:max1 −∗tp ∈ TPThis givesusconfidencethatomnitoolthesimilaritymetricweusemax(len(t) , len(tp)) where TPis thesetofexistingtestfunctionsinapackage,provides meaningfulcomplex.js results.all 0% 0.00.20.40.60.81.0

Mitx ima x im S umm iS rmty la S ity 1Sn o rma liz e de d itd is ta n c e)ee


---

<!-- Página 15 -->

15

TABLE4: A comparison of statement coverage ofESTTP ILOT’s generated tests using three LLMs. For each project, we show the number of generated tests, the(%) of passingand the statement coverage achieved by thesetests.

12**4.7 RQ7:**Effect of Different LLMsfor agivenpackageis6m55s.The bulkofthistimeis spent queryingthemodel,sothechoiceofLLMmakesa big difference. For example, the median time forESTTP ILOT to generatetestsforagivenfunctionusingStarCoderandTable4showsthenumberofgeneratedtests,percentof code-cushman-002is 24sand11s,respectively, and10m48sgenerated teststhatpass,aswellasstatementandbranch and 4m53s,respectively,foracompletetestsuite.Allcoverage ofTEST PILOT’s generatedtestswhenusingthree these performancenumberssuggestthatitisfeasibletodifferent LLMs. While the individual coverage per package either inanonlinesetting(e.g.,inanIDE)varies, we can see that the coverage of tests generated by the TESTPILOT to generatetestsforindividualfunctions,orinanofflinecode-cushman-002model iscomparabletothosegenerated setting (e.g.,duringcodereview)togeneratecompletetestbygpt3.5-turbo, withthelatterhavingaslightlyhigher suites for an API.median statementandbranchcoverageacrossthepack- ages. AWilcoxonmatched-pairssigned-ranktestshows no statisticallysignificantdifferencesbetweengpt3.5-turbo**5 T****HREATS TO****V ALIDITY** andcode-cushman-002for eithertypeofcoverage.Onthe **Internal Validity**: Theextraction of example snippetsother hand,wedofindastatisticallysignificantdifference from documentationreliesontextuallymatchingafunc-between StarCoder and each of the OpenAI models (p-value tion’s name.Giventwofunctionswiththesamenamebut<0 . 05 ) forbothtypesofcoverage.AsshowninTable4, different access paths, we cannot disambiguate which func-StarCoderachieves lowermedianstatement(54.0%)and tion isbeingusedintheexamplesnippet.Accordingly, webranch coverage(37.5%)thanbothothermodels.Cliff’s match this snippet to both functions. While this may lead todelta [55]showsalargeandmediumeffectsizeforstate- **gpt3.5-turbo****Project**inaccuracies, there is unfortunately no precise alternative forment andbranchcoverage,respectively,betweengpt3.5-**Tests** this matching. Any heuristics may cause us to miss snippetsturboandStarCoderand amediumandsmalleffect sizeforglob**71.3%**76 fs-extra**58.8%**394altogether,which may be worse since example snippets helpstatement andbranchcoverage,respectivelybetweencode-graceful-fs**49.3%**301 jsonfile**59.6%**with increasingthepercentageofpassingtestsasshowncushman-002 and StarCoder.bluebird**68.2%**395 q**70.4%**356highin Figure8.Theoverallcoverageandpercentageof rsvp**73.3%**141However,wenotethatStarCoder’s medianstatementpassingtestssuggestourmatchingtechniqueisnotamemfs**81.1%**1058that node-dir**64.3%**22coverage andbrancharebothhigherthanNessielimiting factor in practice.zip-a-folder**88.0%**11 js-sdsl**36.5%**235(statement: 54.0%vs.51.3%andbranch:37.5%vs25.6%).**Construct Validity**: Weuse the concept of non-trivialquill-delta**74.0%**135 complex.js**70.2%**221While thishighercoveragewasnotstatisticallysignificant,assertions asaproxyfororaclequalityinthegeneratedpull-stream**70.8%**69 countries-and-timezones**93.1%**69.1%33the resultsshowthatevenLLMstrainedwithpotentiallytests. Whendeterminingnon-trivialassertions,wesearchsimple-statistics**87.8%**350 plural**59.1%**17**75.4%**13smaller datasetsand/oradifferenttrainingprocessthanforanyusage ofthepackageundertestinthebackwardsdirty**81.1%**57 geo-point**87.8%**87**70.6%**62OpenAI’s modelsareonpar(orevensometimeshigher)slice of the assertion. Such usage may be different from theuneval**68.8%**5 image-downloader63.6%**50.0%**5**75.8%**5than state-of-the-arttraditionaltest-generationtechniques,intended functionundertest.However, giventhedynamiccrawler-url-parser**51.4%**17 such asNessie[11].Furthermore,in RQ2showedgitlab-js, we**61.8%**117nature ofJavaScript,preciselydeterminingtheusageofacore**78.3%**102 that usinggpt3.5-turbowith TESTPILOTresulted inhigheromnitool**74.2%**1029given function,asextractedbytheAPIexplorer,andits **Median**47.1%coverage test suites, with statistically significant differencesoccurrence inthebackwardssliceisdifficult.Whileour to Nessie.Overall,theseresultsemphasizethepromiseofapproach doesnotallowustopreciselydeterminenon- LLM-based testgenerationtechniquesingeneratinghightrivial coverage for a given function, this does not affect the coverage test suites.non-trivial coverage we report for each package’s complete

Finally,wenotethatthemediantimeforESTT P ILOT 12. These timingsweremeasuredonastandardGitHubActions to generatetestsforagivenfunctionusinggpt3.5-turboisLinux VMwitha2-coreCPU,7GBofRAM,and14GBofSSDdisk 15s, andthemediantimetogenerateacompletetestsuitespace.


---

<!-- Página 16 -->

16

andtheseefforts:(i)thegoalandtypesoftestsAPI. Notethatwhencalculatingnon-trivialcoverage,we our work generated and (ii) the need for some form of fine-tuning ormeasure thefullcoverageofteststhatcontainat leastone additional data. We discuss the details below.non-trivial assertion. There may be other calls in those non- **Differing goals**: TI C ODER[24] andC ODET [23]trivial tests that contribute to coverage but do not togenerateimplementationsandtestcasesto theassertion.Measuringassertion/checkedcoverageas use Codex from problemdescriptionsexpressedinnaturallanguage.defined bySchulerandZeller[62]isapossiblealternative, T I C ODERrelies onatest-drivenuser-intentformalizationbut thisispracticallydifficulttoimplementpreciselyfor (TDUIF) loopinwhichtheuserandmodelinteracttoJavaScript. Our definition of non-trivial assertions is simple, settinggenerate both an implementation matching the user’sintent a low bar for non-triviality. Any assertion classified as trivialand a set of test cases to validate its correctness.ODECT, on by our criterion is, indeed, not meaningful, but the conversethe other hand, generates both a set of candidate implemen- is notnecessarilytrue.Accordingly,ourmeasureofnon-tations and some test cases based on the same prompt, runs trivial coverageisalowerboundonthetruenon-trivialthe generatedtestsonthecandidateimplementations,and coverage.chooses thebestsolutionbasedonthetestresults.Unlike While theexamplesweshowinthepapersuggestthatT ESTPILOT, neitheroftheseeffortssolvestheproblemof T ESTPILOT’s generatedtestsusevariablenamesthatare automatically generating unitforexisting code. similar to those chosen by programmers, we do not formallyGiven thecharacteristicsofLLMsingeneratingnatural assess the readability of these tests. In the future, it would becode,therehavebeenseveraleffortsexploringthe interesting toconductuserstudiestoassessthereadabilityuse ofLLMstohelp[27]orcomplement[28]traditional of tests generated by different techniques.test generationMost recently, Lemieux et al. [27] **External Validity: Despite**ourevaluationscalesig-explore using tests generated by Codex as a way to unblock nificantly exceeding evaluations of previous test generationthe searchprocessoftestusingsearch-based approaches [11],[25],ourresultsarestillbasedon25techniques [64], which often fails when the initial randomly npm packagesandmaynotgeneralizetootherJavaScriptgenerated testhasmeaninglessinputthatcannotbemu- code bases. In particular, TP ILOT’s performance may nottated effectively. Theirresultsshowthat,onmostoftheir generalize toproprietarycodethatwasneverseeninthetarget 27Pythonprojects,theirproposedtechnique, OC LLM’s trainingset.We trytomitigatethiseffectinseveralDA MOSA, outperforms the baseline search-based technique, ways: (1)weevaluateonlesspopularpackagesthatarePynguin’s implementationofMOSA[64], aswellasusing likely tohavehadlessimpactonthemodel’straining,(2)only Codex.However,theirCodexpromptincludesonly we evaluateon5GitLabrepositoriesthathavenotbeenthe function implementation and an instruction to generate included inthemodels’training,and(3)wemeasurethetests. Sincetheirmaingoalistoexplorewhetheratest similarity ofthegeneratedteststotheexistingtests.OurbyCodexcanimprovethesearchprocess,they results show that TP ILOTperforms well for both populardo notsystematicallyexplore theeffect ofdifferent prompt and unpopularpackagesandthat92.8%ofthetestcasescomponents. Infact,theyconjecturethatfurtherprompt have≤50% similaritywithexistingtests,withnoexactengineering might improve results, motivating the need for copies. Overall,thisreassuresusthatESTTP ILOTis notour workwhichsystematicallyexploresdifferentprompt producing “memorized” code.components. Additionally, theirgeneratedtestsareinthe Finally,we note that while our technique is conceptuallyMOSA format[64],whichtheauthorsacknowledgecould language-agnostic, ourcurrentimplementationofTP I -lose readability, anddonotcontainassertions.Mostofour LOTtargets JavaScript,andthuswecannotgeneralizeourtests contain assertions, and we further study the quality of results to other languages.assertions we generate as well as reasons for test failures. Similarly,given that it is often difficult for traditional test generation techniquestogenerate(useful)assertions[21],**6 R****ELATED WORK** [22], ATLAS[28] uses LLMs to generate an assert statement T ESTPILOTprovides an alternative to (and potentially com- for a given (assertion-less) Java test. They position their tech- plements) traditionaltechniquesforautomatedtestgener- nique asacomplementtotraditionaltechniques[8],[17]. ation, includingfeedback-directedrandomtestgeneration Withthe same goal, Mastrapaolo et al. [29], [45] and Tufano [7]–[11], search-based and evolutionary techniques [16], [17], et al.[46]performfollowupworkusingtransferlearning, [63], [64],anddynamicsymbolicexecution[12]–[15].This while Yu etal.[66]useinformationretrievaltechniquesto section reviewsneuraltechniquesfortestgeneration,and further improvetheassertstatementsgeneratedbyAtlas. previous test generation techniques for JavaScript. TOGA [67]usessimilartechniquesbutadditionallyincor- porates anexceptionaloracleclassifiertodecideifagiven **6.1 Neural**Techniquesmethod requires an assertion to test exceptional behavior. It Neural techniquesarerapidlybeingadoptedforsolvingthen basesthegenerationoftheassertiononapre-defined various SoftwareEngineeringproblems,withpromisingoracle taxonomycreatedbymanuallyanalyzingexisting results inseveraldomainsincludingcodecompletion[34]–Java testsandusinganeural-basedrankingmechanismto [38], programrepair[39]–[41],andbug-finding[42],[43].rank candidateswithoracleshigher. Incontrastwiththese Pradel andChandra[65]surveythecurrentstateoftheefforts, our goal is to generatecompleteatest method without art inthisemergingresearch area.We areawareofseveralgiving themodelanycontentofthetestmethod(aside recent research efforts in which LLMs are used for test gen-from boilerplatecoderequiredbyMocha),means eration [23]–[29].Therearetwomaindifferencesbetweenthat themodelneedstogeneratebothany testsetupcode


---

<!-- Página 17 -->

17

gram elementssuchasvariablesandexpressions.Then,a(e.g., initializing objects and populating them) as well as the probabilistic type inference is applied to these relationshipsassertion. While TOGA can be integrated with EvoSuite [16] to constructamodel.Finally, theyshowhowsearch-basedto create an end-to-end test-generation tool, recent work [68] techniques can take advantage of the information containedpoints out several shortcomings of the evaluation methods, in suchmodelsbyproposingtwostrategiesforconsultingcasting doubt on the validity of the reported results. these models in the main loop of DynaMOSA [64].**Differing Input/Training: Bareiß**etal.[25]evaluate the performanceofCodexonthreecode-generationtasks,Recently,ElHaji[71]presentedanempiricalstudythat including testgeneration.Likeus,theyrelyonembeddingexplores theeffectivenessofGitHubCopilotatgenerating contextual informationintotheprompttoguidetheLLM,tests. Inthisstudy,testsareselectedfromexistingtest though thespecificdatatheyembedisdifferent:whilesuites associatedwith7open-source Pythonprojects. After T ESTPILOTonly includesthesignature,definition,docu-removing thebodyofeachtestfunction,Copilotisasked mentation, andusageexamplesintheprompt,Bareißetto completetheimplementationsothattheresultingtest al. pursueafew-shotlearningapproach where, inadditioncan beexecutedandcomparedagainsttheoriginaltest. to thedefinitionofafunctionundertest,theyincludeanTwovariationsofthisapproachareexplored,viz.,“with example ofadifferentfunctionfromthesamecodebasecontext” where the other tests in the suite are preserved and and itsassociatedtesttogivethemodelahintastowhat“without context”whereothertestsareremoved.ElHaji it isexpectedtodo,aswellasalistofrelatedhelperalso explorestheimpactof(manually)addingcomments function signatures that could be useful for test generation.that includedescriptionsofintendedbehaviorandusage For alimitedlistof18Javamethods,theyshowthatthisexamples. Theresultsfromthestudyshowthat45.28%of approach yieldsslightlybettercoveragethanRandoop[8],generated testarepassinginthe“withcontext”scenario [9], apopulartechniqueforfeedback-directedrandomtest(the restarefailing,syntacticallyinvalid,orempty)vs generation. Thisisapromisingresult,butfindingsuitableonly 7.55%passinggeneratedtestsinthe“withoutcon- example teststouseinfew-shotlearningcanbedifficult,text” scenario,andthattheadditionofusageexamples especially sincetheirevaluationshowsthatgoodcoverageand commentsisgenerallyhelpful.Thereareseveralsig- crucially dependsontheexamplesbeingcloselyrelatedtonificant differencesbetweenourapproachandElHaji’s the function under test.work: we explore a fully automated technique without any Tufanoetal.[26]presentAthenaTest,anapproachformanual steps,wereportonasignificantlymoreextensive automated testgenerationbasedonaBARTtransformerempirical evaluation,wepresentanadaptivetechniquein model [44].Foragiventestcase,theyrelyonheuristicswhich promptsarerefinedinresponsetotheexecution to identifythe“focal”classandmethodundertest.Thesebehavior ofpreviouslyexecutedtests,wetargetadifferent mapped testcasesarethenusedtofine-tunethemodelprogramming language(JavaScriptinsteadofPython),and for thetaskofproducingunittestsbyrepresentingthisTestPilotinteracts directly with an LLM rather than relying task asatranslationtaskthatmapsafocalmethod(alongon Copilot, an LLM-based programming assistant. with the focal class, constructors, and other public methods and fieldsinthatclass)toatestcase.Inexperimentson **6.2 Test**Generation Techniques for JavaScript5 projectsfromDefects4J[69],AthenaTest generated158K T ESTPILOT’s mechanismforrefining prompts basedonex-test cases,achievingsimilartestcoverageasEvoSuite[16], ecution feedback was inspired by the mechanism employeda popularsearch-basedtestgenerationtool,andcovering by feedback-directed random test generation techniques [7]–43% ofallfocalmethods.Asignificantdifferencebetween [11], wherenewtestsaregeneratedbyextendingprevi-their work and ours is thatapproach requires training ously generatedpassingtests.AsreportedinSection4.2,the modelonalargesetoftestcaseswhereasESTT ILOT T ESTPILOTachieves significantly higher statement coverageuses anoff-the-shelfLLM.Infact,inadditiontothegoal and branch coverage than Nessie [11], which represents thedifferences withATLAS [28]andMastrapaoloetal.’s[29], in feedback-directed random test generation[45] work above, both these efforts also require a data setstate-of-the-artof for JavaScript.test methods (with assertions) and their corresponding focal projectshaveconsideredtestgenera-methods, whether to use in the main training [28] or in fine Several previous tion forJavaScript(see[72]forasurvey).Saxenaetal.[73]tuning during transfer learning [29], [45], [46]. present Kudzu,atoolthataimstofindinjectionvulnera-Unfortunately,theabovedifferencesingoalsorinthe bilities in client-side JavaScript applications by exploring anrequired dataformodeltrainingmakeitmeaninglessor impossible todoadirectexperimentalcomparisonwithapplication’s input space. They differentiate an input spaceintoan event, whichconcernstheorderT ESTPILOT. Additionally,noneoftheseeffortssupport in which event handlers execute (e.g., as a result of buttonsJavaScript orprovidedatasetsthatcanbeused being clicked), and aspacewhich concerns the choice offor comparison.Infact,oneofourmainmotivationsfor exploring promptengineeringforanoff-the-shelfLLMis values passed to functions or entered into text fields. Kudzu uses dynamic symbolic execution to explore the value spaceto avoidtheneedtocollecttestexamplesforfew-shot systematically,but it relies on a random exploration strategylearning [25]ortestmethod/focalmethodpairsrequired to explore theeventspace.Artemis[74]isaframeworkforfor training [28] or additional fine tuning [29], [45], [46]. **Other techniques: Stallenberg**etal.[70]presenta automated test generation that iteratively generates tests for client-sideapplications consisting of sequences oftest generationtechniqueforJavaScriptbasedonunsuper- events, usingaheuristics-basedstrategythatconsidersthevised type inference consisting of three phases. First, a static locations readandwrittenbyeacheventhandlertofocusanalysis is performed to deduce relationships between pro-


---

<!-- Página 18 -->

18

tuning nor a parallel corpus of functions and tests. Instead,on thegenerationoftestsinvolvingeventhandlersthat we embed contextual information about the function underinteract witheachother. Lietal.[75]extendsArtemiswith test intotheprompt,specificallyitssignature,itsattacheddynamic symbolic execution to improve its ability to explore documentation comment (if any), any usage examples fromthe valuespace,andTanida etal.[76]furtherimproveon the project documentation, and the source code of the func-this workbyaugmentinggeneratedtestinputswithuser- tion. Furthermore,ifageneratedtestfails,weadaptivelysupplied invariants.Fardetal.[77]presentConFix,atool create anewpromptembeddingthistestandthefailurethat usesacombinationofdynamicanalysisandsymbolic message to guide the model towards fixing the problematicexecution toautomaticallygenerateinstancesoftheDocu- test. WehaveimplementedourapproachforJavaScriptment ObjectModel(DOM)thatcanserveastestfixtures on topofoff-the-shelfLLMs,andshownthatitachievesin unittestsforclient-sideJavaScriptcode.Marchettoand state-of-the artstatementcoverageon25npmpackages.Tonella[78] present a search-based test generation technique Further evaluation shows that the majority of the generatedthat constructstestsconsistingofsequencesofeventsthat tests containnon-trivialassertions,andthatallpartsofrelies ontheautomaticextractionofafinitestatemachine the informationincludedinthepromptcontributestothethat represents thatapplication’sstate.Noneofthesetools quality of the generated tests. Experiments with three LLMsgenerate tests that contain assertions. Several test generation tools for JavaScript are capable of( gpt3.5-turbo,code-cushman-002, andStarCoder) demonstrate generating testscontainingassertions.JSART[79]isatoolthat LLM-basedtestgenerationalreadyoutperformsstate- that generates regression tests that contain assertions reflect-of-the-art previoustestgenerationmethodssuchasNessie ing likelyinvariantsthatare generatedusingavariationofkey metrics. We conjecture that the use of more advanced the Daikondynamicinvariantgenerator[80].SinceLLMs will further improve results, though we are reluctant generates assertionsthatare likelyto hold,anadditionalto speculate by how much. step isneededinwhichinvalidassertionsareremovedIn future work, we plan to further investigate the quality from the generated tests. Mirshokraie et al. [81], [82] presentof thetestsbyTP ILOT. Whileinthispaper an approachinwhichtestsaregeneratedforclient-sidewe havefocusedonpassingandexcludedfailing JavaScript applicationsconsistingofsequencesofevents.tests from consideration entirely, we have seen examples of Then, inanadditionalstep,function-levelunittestsarefailingthat are “almost right” and might be interesting derived by instrumenting program execution to monitor theto adeveloperasastartingpointforfurtherrefinement. state ofparameters,globalvariables,andtheDOMuponHowever,doing this depends on having a good strategy for entry and exit to functions to obtain values with which func-telling apartusefulfailingtestsfromuselessones.Ourex- tions are to be invoked. Assertions are added automaticallyperiments have demonstrated that timeout errors, assertion to thegeneratedtestsby:(i)mutatingtheDOMandtheerrors, and correctness errors are key factors that cause code oftheapplicationundertest,(ii)executinggeneratedto fail. In future work, we plan to apply static and dynamic tests todeterminehowapplicationstateisimpactedbyprogram analysis to failingin order towhy mutations, and (iii) adding assertions to the tests that reflecttimeout errorsandassertionoccurandhowfailing the behaviorpriortothemutation.Testilizer [83]isatesttests could be modified to make them pass. generation toolthataimstoenhanceanexistinghuman-Further researchisneededtodeterminewhatfactors written test suite. To this end, Testilizer instruments code tothegenerationofnon-trivialassertions.Anecdo- observe howexistingtestsaccesstheDOM,andexecutestally,wehaveobservedthattheavailabilityofusageex- them toobtainaState-FlowGraphinwhichthenodesamples isgenerallyhelpful.Weenvisionthatthenumber reflect dynamicDOMstatesandedgestheevent-of usefulassertionscouldbeimprovedbyobtainingusage driven transitionsbetweenthesestates.Alternativepathsexamples inotherways,e.g.,byinteractingwithauser, or are exploredbyexploringpreviouslyunexploredevents by extracting usage examples from clients of the application in eachstate.Testilizeraddsassertionstothegeneratedunder test. tests thatareeithercopiedverbatimfromexistingtests,byAnother fruitfularea ofexperimentationcouldbevary- adapting thestructureofanexistingassertiontoanewlying the sampling temperature of the LLM. In this work, we explored state,orbyinferringasimilarassertionusingalways sampleattemperaturezero,whichhastheadvan- machine learning techniques.tage ofprovidingstableresults,butalsomeansthatthe These techniquessharethelimitationthattheyrequiremodel islesslikelytoofferlower-probabilitycompletions the entireapplicationunderthetesttobeexecutable,lim-that might result in more interesting tests. iting their applicability. Moreover, several of the techniquesAnother areaoffutureworkisthedevelopmentof discussed aboverequirere-executionoftests(toinferas-hybrid techniquesthatcombineexistingfeedback-directed sertions usingmutationtesting[81],[82],ortofilterouttest generationtechniqueswithanLLM-basedtechnique assertions thatareinvalid[79]),whichaddstotheircost.such asT ESTPILOT. Forexample,onecoulduseanLLM- By contrast,TEST PILOTonly requiresthefunctionsofAPIbased techniquetogenerateaninitialsetoftestsanduse functions undertesttobeavailableandexecutable,andittests that it generates as a starting point for extension by executes each test that it generates only once.a feedback-directed technique such as Nessie, thus enabling it to uncover edges cases that would be difficult to **7 C****ONCLUSIONS**AND**F UTURE****W ORK**using only random values. In principle,ourcanbeadaptedtoanypro-WehavepresentedTEST PILOT, anapproachforadaptive gramming language.Practicallyspeaking,thiswouldin-unit-test generationusingalargelanguagemodel.Unlike volve adaptingpromptstousethesyntaxofthelanguageprevious work in this area, ESTTP ILOTrequires neither fine


---

<!-- Página 19 -->

19

[13] K.Sen,D.Marinov,andG.Agha,“CUTE:aconcolicunitunder consideration, and to use a testing framework for that testing engine for C,” inProceedings of the 10th European Softwarelanguage. Inaddition,theminingofdocumentationand Engineering Conferenceheldjointlywith13thACMSIGSOFT usage exampleswouldneedtobeadaptedtomatchtheInternational SymposiumonFoundationsofSoftwareEngineering, documentation formatusedforthatlanguage.TheLLMs2005, Lisbon,Portugal,September5-9,2005, M.Wermelinger and H. C.Gall,Eds.ACM,2005,pp.263–272.[Online].Available:that weuseddidnotlanguage-specifictrainingandcould [https://doi.org/10.1145/1081706.1081750](https://doi.org/10.1145/1081706.1081750)be usedtogeneratetestsforotherlanguages,thoughthe [14] C.Cadar,V.Ganesh,P.M.Pawlowski,D.L.Dill,and effectiveness oftheapproachwilldependontheamountD. R.Engler,“EXE:automaticallygeneratinginputsofdeath,” of codewritteninthatlanguagethatwasincludedintheinProceedings ofthe13thACMConferenceonComputerand Communications Security, CCS2006,Alexandria,VA, USA,OctoberLLM’s trainingset.Onespecificquestionthatwouldbein- 30 -November3,2006, A.Juels,R.N.Wright,andS.D.C.teresting to explore is how well an approach likeESTTP ILOT di Vimercati, Eds. ACM,2006, pp. 322–335. [Online]. Available: would perform on a statically-typed language.[https://doi.org/10.1145/1180405.1180445](https://doi.org/10.1145/1180405.1180445) [15] N.Tillmann,J.deHalleux,andT.Xie,“Transferringan automated testgenerationtooltopractice:frompexto fakes andcodedigger,”in ACM/IEEE InternationalConference

### A CKNOWLEDGMENT

on AutomatedSoftwareEngineering,ASE’14,Vasteras,Sweden - September15-19,2014, I.Crnkovic,M.Chechik,andThe research reported on in this paper was conducted while P.Gr unbacher,Eds. ACM,2014, pp. 385–396. [Online]. Available:S. NadiandF. TipweresabbaticalvisitorsandA.Eghbali [https://doi.org/10.1145/2642937.2642941](https://doi.org/10.1145/2642937.2642941) an intern at GitHub. The authors are grateful to the GitHub [16] G.FraserandA.Arcuri,“Evolutionarygenerationofwhole Next teamformanyinsightfulandhelpfuldiscussionstest suites,”inProceedings ofthe11thInternationalConference on QualitySoftware,QSIC2011,Madrid,Spain,July13-14,about TestPilot.F.TipwassupportedinpartbyNational 2011, M.N u nez, R.M.Hierons,andM.G.Merayo,Eds.Science FoundationgrantsCCF-1907727andCCF-2307742. IEEE ComputerSociety,2011,pp.31–40.[Online].Available: S. Nadi’sresearchissupportedbytheCanadaResearch[https://doi.org/10.1109/QSIC.2011.19](https://doi.org/10.1109/QSIC.2011.19) Chairs ProgramandtheNaturalSciencesandEngineering[17] ——,“EvoSuite:automatictestsuitegenerationforobject- oriented software,”inSIGSOFT/FSE’11 19thACMSIGSOFTResearch Council of Canada (NSERC), RGPIN-2017-04289. Symposium ontheFoundationsofSoftwareEngineering(FSE-19) and ESEC’11:13thEuropeanSoftwareEngineeringConference (ESEC-13), Szeged, Hungary, September 5-9, 2011, T. Gyimothy and

### R EFERENCES

A. Zeller,Eds.ACM,2011,pp.416–419.[Online].Available: [https://doi.org/10.1145/2025113.2025179](https://doi.org/10.1145/2025113.2025179) [1] K.Beck,Extreme ProgrammingExplained:EmbraceChange. [18] M.M. Almasi, H. Hemmati, G. Fraser, A. Arcuri, and J. Benefelds,Addison-Wesley,2000. “An industrialevaluationofunittestgeneration:Findingreal[2] J.ShoreandS.Warden,The ArtofAgileDevelopment, 2nded. faults inafinancialapplication,”in2017 IEEE/ACM39thInter-O’Reilly,2021. national Conference on Software Engineering:Engineering in[3] S.Siddiqui,Learning Test-Driven Development. O’Reilly,2021. Practice Track (ICSE-SEIP). IEEE,2017, pp. 263–272. [4] E.DakaandG.Fraser, “Asurveyonunittestingpracticesand [19] G.Grano, S. Scalabrino, H. C. Gall, and R. Oliveto, “An empiricalproblems,” in2014 IEEE 25th International Symposium on Software investigation onthereadabilityofmanualandgeneratedtestReliability Engineering, 2014, pp. 201–211. cases,” in 2018 IEEE/ACM 26th International Conference on Program[5] B.P.Miller,L.Fredriksen,andB.So,“Anempirical Comprehension (ICPC). IEEE,2018, pp. 348–3483.study ofthereliabilityofUNIXutilities,”Commun. ACM, [20] E.Daka, J. Campos, G. Fraser, J. Dorn, and W. Weimer, “Modelingvol. 33,no.12,pp.32–44,1990.[Online].Available:https: readability toimprove unittests,”inProceedings ofthe201510th//doi.org/10.1145/96267.96279 Joint MeetingonFoundationsofSoftwareEngineering,ESEC/FSE[6] M.Zalewski,“Americanfuzzylop,”[https://lcamtuf.coredump](https://lcamtuf.coredump). 2015, Bergamo,Italy,August30-September4,2015, E.D.Nitto,cx/afl/, 2022. M. Harman,andP. Heymans,Eds.ACM,2015,pp.107–118.[7] C.Csallner and Y. Smaragdakis, “JCrasher: an automatic robust- [Online]. Available: [https://doi.org/10.1145/2786805.2786838](https://doi.org/10.1145/2786805.2786838)ness tester for Java,”Software Practice and Experience, vol. 34, no. 11, [21] A.Panichella,S.G.Fraser,A.A.Sawant,andpp. 1025–1050, 2004. V.J.Hellendoorn,“Revisitingtestsmellsinautomatically[8] C.PachecoandM.D.Ernst,“Randoop:Feedback-directed generated tests:Limitations,pitfalls,andopportunities,”inrandom testingforjava,”inCompanion tothe22NdACM IEEE InternationalConferenceonSoftwareMaintenanceandSIGPLAN ConferenceonObject-orientedProgrammingSystems Evolution, ICSME2020,Adelaide,Australia,September28-and ApplicationsCompanion , ser.OOPSLA’07.NewYork, October 2,2020. IEEE,2020,pp.523–533.[Online].Available:NY,USA:ACM,2007,pp.815–816.[Online].Available: [https://doi.org/10.1109/ICSME46990.2020.00056](https://doi.org/10.1109/ICSME46990.2020.00056)[http://doi.acm.org/10.1145/1297846.1297902](http://doi.acm.org/10.1145/1297846.1297902) [22] F.Palomba,D.D.Nucci,A.Panichella,R.Oliveto,andA.D.[9] C.Pacheco,S.K.Lahiri,andT.Ball,“Findingerrorsin.net Lucia, “On the diffusion of test smells in automatically generatedwith feedback-directed random testing,” inProceedings of the 2008 test code: an empirical study,” inof theInternationalInternational Symposium on Software Testing and Analysis, ser. ISSTA Workshop onSearch-BasedSoftwareTesting,SBST@ICSE2016,’08. NewYork,NY,USA:ACM,2008,pp.87–96.[Online]. Austin, Texas,USA,May14-22,2016. ACM,2016,pp.5–14.Available:[http://doi.acm.org/10.1145/1390630.1390643](http://doi.acm.org/10.1145/1390630.1390643) [Online]. Available: [https://doi.org/10.1145/2897010.2897016](https://doi.org/10.1145/2897010.2897016)[10] M.Selakovic,M.Pradel,R.Karim,andF. Tip, “Test generation [23] B.Chen,F.Zhang,A.Nguyen,D.Zan,Z.Lin,J.-G.Lou,andfor higher-orderfunctionsindynamiclanguages,”Proc. ACM W.Chen, “CodeT: Code Generation with Generated Tests,” 2022.Program. Lang., vol.2,no.OOPSLA,pp.161:1–161:27,2018. [Online]. Available: [https://arxiv.org/abs/2207.10397](https://arxiv.org/abs/2207.10397)[https://doi.org/10.1145/3276531](https://doi.org/10.1145/3276531) [24] S.K.Lahiri,A.Naik,G.Sakkas,P.Choudhury,C.vonVeh,[11] E.Arteca, S. Harner, M. Pradel, and F. Tip, “Nessie: Automatically M. Musuvathi, J. P. Inala, C. Wang, and J. Gao, “Interactive Codetesting javascriptapiswithasynchronouscallbacks,”in44th Generation viaTest-DrivenUser-IntentFormalization,”2022.IEEE/ACM 44thInternationalConferenceonSoftwareEngineering, [Online]. Available: [https://arxiv.org/abs/2208.05950](https://arxiv.org/abs/2208.05950)ICSE 2022, Pittsburgh, PA, USA, May 25-27, 2022. ACM,pp. [25] P.Bareiß,B.Souza,M.d’Amorim,andM.Pradel,“Code1494–1505. [Online]. Available: [https://doi.org/10.1145/3510003](https://doi.org/10.1145/3510003). Generation Tools (Almost)forFree?AStudyofFew-Shot,Pre-3510106 TrainedLanguage Models on Code,”CoRR, vol. abs/2206.01335,[12] P.Godefroid,N.Klarlund,andK.Sen,“DART:directed 2022. [Online].Available:[https://doi.org/10.48550/arXiv.2206](https://doi.org/10.48550/arXiv.2206).automated randomtesting,”inProceedings oftheACM 01335SIGPLAN 2005ConferenceonProgrammingLanguageDesignand [26] M.Tufano,D.Drain,A.Svyatkovskiy,S.K.Deng,andImplementation, Chicago,IL,USA,June12-15,2005, V. Sarkarand N. Sundaresan,“UnittestcasegenerationwithtransformersM. W. Hall,Eds.ACM,2005,pp.213–223.[Online].Available: and focalcontext,”arXiv,May2021.[Online].Avail-[https://doi.org/10.1145/1065010.1065036](https://doi.org/10.1145/1065010.1065036)


---

<!-- Página 20 -->

20

able: [https://www.microsoft.com/en-us/research/publication/](https://www.microsoft.com/en-us/research/publication/)Eds. AAAIPress, 2017, pp. 1345–1351. [Online]. Available: http: unit-test-case-generation-with-transformers-and-focal-context///aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/14603 [40] V.J. Hellendoorn, C. Sutton, R. Singh, P. Maniatis, and D. Bieber,[27] C.Lemieux,J.P. Inala,S.K.Lahiri,andS.Sen,“CodaMOSA: “Global relationalmodelsofsourcecode,”in8th InternationalEscaping coverageplateausintestgenerationwithpre-trained onLearningRepresentations,ICLR2020,AddisAbaba,large language models,” in45th International Conference on Software Ethiopia, April26-30,2020. OpenReview.net,2020.[Online].Engineering, ser. ICSE, 2023. Available:[https://openreview.net/forum?id=B1lnbRNtwr](https://openreview.net/forum?id=B1lnbRNtwr)[28] C.Watson, M. Tufano, K. Moran, G. Bavota, and D. Poshyvanyk, [41] M.Allamanis,H.Jackson-Flux,andM.Brockschmidt,“Self-“On Learning Meaningful Assert Statements for Unit Test Cases,” supervised bugdetectionandrepair,”in Advances inNeuralinProceedings oftheACM/IEEE42ndInternationalConference Information ProcessingSystems34:AnnualConferenceonNeuralon SoftwareEngineering. ACM,jun2020.[Online].Available: Information Processing Systems 2021, NeurIPSDecember 6-14,[https://doi.org/10.1145%2F3377811.3380429](https://doi.org/10.1145%2F3377811.3380429) 2021, virtual, M.Ranzato,A.Beygelzimer,Y.N.Dauphin,[29] A.Mastropaolo,S.Scalabrino,N.Cooper,D.NaderPalacio, P.Liang,andJ.W.Vaughan,Eds.,2021,pp.27865–27 876.D. Poshyvanyk,R.Oliveto,andG.Bavota,“Studyingtheusage [Online]. Available: [https://proceedings.neurips.cc/paper/2021/](https://proceedings.neurips.cc/paper/2021/)of text-to-text transfer transformer to support code-related tasks,” hash/ea96efc03b9a050d895110db8c4af057-Abstract.htmlin 43rd IEEE/ACM International Conference on Software Engineering [42] M.PradelandK.Sen,“Deepbugs:alearningapproach(ICSE), 2021, pp. 336–347. to name-basedbugdetection,”Proc. ACMProgram.Lang.,[30] J.Devlin,M.-W.Chang,K.Lee,andK.Toutanova,“Bert:Pre- vol. 2,no.OOPSLA,pp.147:1–147:25,2018.[Online].Available:training ofdeepbidirectionaltransformersforlanguageunder- [https://doi.org/10.1145/3276517](https://doi.org/10.1145/3276517)standing,” arXiv preprint arXiv:1810.04805, 2018. [43] M.Allamanis,M.Brockschmidt, andM.Khademi,“Learningto[31] T.B.Brown,B.Mann,N.Ryder,M.Subbiah,J.Kaplan, represent programs with graphs,” in6th International Conference onP.Dhariwal,A.Neelakantan,P.Shyam,G.Sastry,A.Askell, Learning Representations,ICLR2018,Vancouver, BC,Canada,AprilS. Agarwal,A.Herbert-Voss, G.Krueger, T. Henighan,R.Child, 30 -May3,2018,Conference Track Proceedings. OpenReview.net,A. Ramesh,D.M.Ziegler, J.Wu, C.Winter, C.Hesse,M.Chen, 2018. [Online].Available:[https://openreview.net/forum?id=](https://openreview.net/forum?id=)E. Sigler,M.Litwin,S.Gray,B.Chess,J.Clark,C.Berner, BJOFETxR-S. McCandlish,A.Radford,I.Sutskever,andD.Amodei, [44] M.Lewis,Y.Liu,N.Goyal,M.Ghazvininejad,A.Mo-“Language modelsarefew-shotlearners,”2020.[Online]. hamed, O.Levy,V.Stoyanov,andL.Zettlemoyer,“Bart:Available:[https://arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165) Denoising sequence-to-sequencepre-trainingfornaturallan-[32] M.Chen,J.Tworek,H.Jun,Q.Yuan,H.P. deOliveiraPinto, guage generation, translation, and comprehension,”arXiv preprintJ. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, arXiv:1910.13461, 2019.R. Puri,G.Krueger, M.Petrov, H.Khlaaf,G.Sastry, P. Mishkin, [45] A.Mastropaolo, N. Cooper, D. N. Palacio, S. Scalabrino, D. Poshy-B. Chan,S.Gray,N.Ryder,M.Pavlov,A.Power,L.Kaiser, vanyk, R.Oliveto,andG.Bavota,“UsingtransferlearningforM. Bavarian,C.Winter,P.Tillet,F.P.Such,D.Cummings, code-related tasks,”IEEE TransactionsonSoftwareEngineering,M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, 2022.A. Nichol,A.Paino,N.Tezak, J.Tang, I.Babuschkin,S.Balaji, [46] M.Tufano,D.Drain,A.Svyatkovskiy,andN.Sundaresan,S. Jain,W. Saunders,C.Hesse,A.N.Carr, J.Leike,J.Achiam, “Generating accurateassertstatementsforunittestcasesV.Misra,E.Morikawa,A.Radford,M.Knight,M.Brundage, using pretrainedtransformers,”inProceedings ofthe3rdM. Murati,K.Mayer,P.Welinder,B.McGrew,D.Amodei, ACM/IEEE InternationalConferenceonAutomationofSoftwareS. McCandlish, I. Sutskever, and W. Zaremba, “Evaluating Large Test, ser.AST’22.NewYork,NY,USA:AssociationforLanguage Models Trained on Code,”CoRR, vol. abs/2107.03374, Computing Machinery,2022,p.54–64.[Online].Available:2021.[https://arxiv.org/abs/2107.03374](https://arxiv.org/abs/2107.03374) [https://doi.org/10.1145/3524481.3527220](https://doi.org/10.1145/3524481.3527220)[33] Y.Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond, [47] L.ReynoldsandK.McDonell,“PromptprogrammingforlargeT.Eccles,J.Keeling,F. Gimeno,A.D.Lago,T.P. Choy, language models: Beyond the few-shot paradigm,” 2021. [Online].C. d.M.d’Autume,I.Babuschkin,X.Chen,P.-S.Huang, Available:[https://arxiv.org/abs/2102.07350](https://arxiv.org/abs/2102.07350)J. Welbl, S.Gowal,A.Cherepanov, J.Molloy, D.J.Mankowitz, [48] OpenAI,“OpenAILLMs:Deprecations,”E. S.Robson,P.Kohli,N.deFreitas,K.Kavukcuoglu,and [https://platform.openai.com/docs/deprecations](https://platform.openai.com/docs/deprecations), 2023.O. Vinyals, “Competition-level code generation with alphacode,” [49] HuggingFace,“Starcoder:Astate-of-the-artLLMforcode,”2022. [Online]. Available: [https://arxiv.org/abs/2203.07814](https://arxiv.org/abs/2203.07814) [https://huggingface.co/blog/starcoder](https://huggingface.co/blog/starcoder),2023.[34] J.Li,Y.Wang,M.R.Lyu,andI.King,“Codecompletion [50] “Mocha,”[https://mochajs.org/](https://mochajs.org/), 2022.with neuralattentionandpointernetworks,”inProceedings Mezzetti, A. Møller, and M. T. Torp, “Type Regression Testingof theTwenty-SeventhInternationalJointConferenceonArtificial [51] G. to Detect Breaking Changes in Node.js Libraries,”32ndinEuropeanIntelligence, IJCAI2018,July13-19,Stockholm,Sweden, Conference on Object-Oriented Programming, ECOOPJuly 16-J. Lang,Ed.ijcai.org,2018,pp.4159–4165.[Online].Available: 21, 2018,Amsterdam,TheNetherlands, ser. LIPIcs,D.Millstein,[https://doi.org/10.24963/ijcai.2018/578](https://doi.org/10.24963/ijcai.2018/578) Ed., vol. 109. SchlossDagstuhl - Leibniz-Zentrum fuer Informatik,[35] A.Svyatkovskiy, S. K. Deng, S. Fu, and N. Sundaresan, “Intellicode 2018, pp. 7:1–7:24.compose: codegenerationusingtransformer,” inESEC/FSE ’20: [52] OpenAI,“OpenAICodex,”[https://openai.com/blog/openai-](https://openai.com/blog/openai-)28th ACMJointEuropeanSoftwareEngineeringConferenceand codex, 2023.Symposium ontheFoundationsofSoftwareEngineering,Virtual Event, USA,November8-13,2020, P.Devanbu,M.B.Cohen,[53] “Istanbulcoverage tool,” [https://istanbul.js.org/](https://istanbul.js.org/), 2022. and T. Zimmermann, Eds. ACM,2020, pp. 1433–1443. [Online].[54] S.Yoo and M. Harman, “Regression testing minimization, selec- Available:[https://doi.org/10.1145/3368089.3417058](https://doi.org/10.1145/3368089.3417058)tion and prioritization: a survey,”Software testing, verification and reliability, vol. 22, no. 2, pp. 67–120, 2012.[36] R.Karampatsis, H. Babii, R. Robbes, C. Sutton, and A. Janes, “Big code != big vocabulary: open-vocabulary models for source code,”[55] N.Cliff, “Dominance statistics: Ordinal analyses to answer ordinal inICSE ’20:42ndInternationalConference onSoftware Engineering,questions.” Psychological bulletin, vol. 114, no. 3, p. 494, 1993. Seoul, SouthKorea,27June-19July,2020, G.Rothermeland[56] M.Selakovic,M.Pradel,R.Karim,andF. Tip, “Test generation D. Bae,Eds.ACM,2020,pp.1073–1085.[Online].Available:for higher-order functionsindynamiclanguages,”Proceedings of [https://doi.org/10.1145/3377811.3380342](https://doi.org/10.1145/3377811.3380342)the ACM on Programming Languages, vol. 2, no. OOPSLA, pp. 1–27, [37] S.Kim,J.Zhao,Y. Tian,andS.Chandra,“Codepredictionby2018. feeding treestotransformers,”in 43rd IEEE/ACMInternational[57] GitHub,“CodeQL,” [https://codeql.github.com/](https://codeql.github.com/), Conference onSoftwareEngineering,ICSE2021,Madrid,Spain,[58] O.Foundation,“Node.jserrorcodes,”[https://nodejs.org/dist/](https://nodejs.org/dist/) 22-30 May2021. IEEE,2021,pp.150–162.[Online].Available:latest-v18.x/docs/api/errors.html#nodejs-error-codes, 2022. [https://doi.org/10.1109/ICSE43902.2021.00026](https://doi.org/10.1109/ICSE43902.2021.00026)[59] S.Schleimer,D.S.Wilkerson,andA.Aiken,“Winnowing: [38] GitHub,“GitHub Copilot,” [https://copilot.github.com/](https://copilot.github.com/), 2022.Local algorithmsfordocumentfingerprinting,”inProceedings of [39] R.Gupta, S. Pal, A. Kanade, and S. K. Shevade, “Deepfix: Fixingthe 2003ACMSIGMODInternationalConferenceonManagement common C language errors by deep learning,”Proceedingsinof theof Data , ser.SIGMOD’03.NewYork,NY,USA:Association Thirty-First AAAI Conference on Artificial Intelligence, February 4-9,for ComputingMachinery,2003,p.76–85.[Online].Available: 2017, SanFrancisco,California,USA, S.SinghandS.Markovitch,[https://doi.org/10.1145/872757.872770](https://doi.org/10.1145/872757.872770)


---

<!-- Página 21 -->

21

[60] G.Myers,“Afastbit-vectoralgorithmforapproximateEds. ACM,2014,pp.449–459.[Online].Available:https: string matchingbasedondynamicprogramming,”J. ACM,//doi.org/10.1145/2635868.2635913 vol. 46,no.3,p.395–415,may1999.[Online].Available:[76] H.Tanida, T. Uehara, G. Li, and I. Ghosh, “Automatic Unit Test [https://doi.org/10.1145/316542.316550](https://doi.org/10.1145/316542.316550)Generation andExecutionforJavaScriptProgram through Sym- bolic Execution,” inProceedings of the Ninth International Conference[61] “npmlevenshteindistancepackage.”[Online].Available: https: on Software Engineering Advances, 2014, pp. 259–265.//www.npmjs.com/package/levenshtein [77] A.M. Fard, A. Mesbah, and E. Wohlstadter, “Generating fixtures[62] D.Schuler and A. Zeller, “Assessing oracle quality with checked for JavaScriptunittesting,”in30th IEEE/ACMInternationalcoverage,” in Fourth IEEE International Conference on Software Test- Conference onAutomatedSoftwareEngineering,ASE2015,Lincoln,ing, Verification and Validation, 2011, pp. 90–99. NE, USA,November9-13,2015, M.B.Cohen,L.Grunske,and[63] P.McMinn,“Search-basedsoftwaretesting:Past,presentand M. Whalen,Eds.IEEEComputerSociety,2015,pp.190–200.future,” in Fourth IEEE International Conference on Software Testing, [Online]. Available: [https://doi.org/10.1109/ASE.2015.26](https://doi.org/10.1109/ASE.2015.26)Verificationand Validation, ICST 2012, Berlin, Germany, 21-25 March, [78] A.Marchetto and P. Tonella, “Using search-based algorithms for2011, Workshop Proceedings. IEEEComputer Society,pp. 153– Ajax eventsequencegenerationduringtesting,”Empir.Softw.163. [Online]. Available: [https://doi.org/10.1109/ICSTW.2011.100](https://doi.org/10.1109/ICSTW.2011.100) Eng. , vol.16,no.1,pp.103–140,2011.[Online].Available: [64] A.Panichella,F.M.Kifetew,andP.Tonella,“Automatedtest [https://doi.org/10.1007/s10664-010-9149-1](https://doi.org/10.1007/s10664-010-9149-1) case generationasamany-objectiveoptimisationproblemwith [79] S.MirshokraieandA.Mesbah,“JSART:JavaScriptassertion- dynamic selectionofthetargets,”IEEE Transactions onSoftware based regression testing,”in Web Engineering-12thInternational Engineering, vol. 44, no. 2, pp. 122–158, 2018. Conference, ICWE2012,Berlin,Germany,July23-27,2012. [65] M.Pradel and S. Chandra, “Neural software analysis,”Commun.Proceedings, ser. Lecture Notes in Computer Science, M. Brambilla, ACM, vol.65,no.1,pp.86–96,2022.[Online].Available:T.Tokuda,andR.Tolksdorf,Eds.,vol.7387.Springer, [https://doi.org/10.1145/3460348](https://doi.org/10.1145/3460348)2012, pp.238–252.[Online].Available: [https://doi.org/10.1007/](https://doi.org/10.1007/) [66] H.Yu,Y.Lou,K.Sun,D.Ran,T.Xie,D.Hao,Y.Li,978-3-642-31753-818 G. Li,andQ.“AutomatedAssertionGenerationvia[80] “TheDaikon invariant detector,” [http://plse.cs.washington.edu/](http://plse.cs.washington.edu/) Information RetrievalandItsIntegrationwithDeepLearning,”daikon/, 2023. inProceedings ofthe44thInternationalConferenceonSoftware[81] S.Mirshokraie,A.Mesbah,andK.Pattabiraman,“PYTHIA: Engineering, ser.ICSE’22.NewYork,NY,USA:Associationgenerating testcaseswithoraclesforJavaScriptapplications,” for ComputingMachinery, 2022,p.163–174.[Online].Available:in2013 28thIEEE/ACMInternationalConferenceonAutomated [https://doi.org/10.1145/3510003.3510149](https://doi.org/10.1145/3510003.3510149)Software Engineering,ASE2013,SiliconValley,CA,USA, [67] E.Dinella,G.Ryan,T.Mytkowicz,andS.K.Lahiri,November 11-15,2013, E.Denney,T.Bultan,andA.Zeller, “Toga:Aneuralmethodfortestoraclegeneration,”inEds. IEEE,2013,pp.610–615.[Online].Available:https: Proceedings ofthe44thInternationalConferenceonSoftware//doi.org/10.1109/ASE.2013.6693121 Engineering, ser. ICSE ’22. NewYork, NY, USA: Association for[82] ——,“JSEFT:automatedJavascriptunittestgeneration,”in Computing Machinery,2022,p.2130–2141.[Online].Available:8th IEEEInternationalConferenceonSoftwareTesting,Verification [https://doi.org/10.1145/3510003.3510141](https://doi.org/10.1145/3510003.3510141)and Validation,ICST2015,Graz,Austria,April13-17,2015. IEEE ComputerSociety,2015,pp.1–10.[Online].Available:[68] Z.Liu,K.Liu,X.Xia,andX.Yang,“Towardsmorerealistic [https://doi.org/10.1109/ICST.2015.7102595](https://doi.org/10.1109/ICST.2015.7102595)evaluation forneuraltestoraclegeneration,”inProceedings of [83] A.M.Fard,M.MirzaAghaei,andA.Mesbah,“Leveragingthe ACM SIGSOFT International Symposium on Software Testing and existing tests in automated test generation for web applications,”Analysis, ser. ISSTA ’23, 2023. inACM/IEEE InternationalConferenceonAutomatedSoftware[69] R.Just, D. Jalali, and M. D. Ernst, “Defects4j: a database of existing Engineering, ASE’14,Vasteras,Sweden-September15-faults toenablecontrolled testingstudiesforjavaprograms,” in 19, 2014, I.Crnkovic,M.Chechik,andP.Grunbacher,International SymposiumonSoftwareTestingandAnalysis,ISSTA Eds. ACM,2014,pp.67–78.[Online].Available:https:’14, SanJose,CA,USA-July21-26,2014C.S.Pasareanuand //doi.org/10.1145/2642937.2642991D. Marinov, Eds.ACM,2014,pp.437–440.[Online].Available: [https://doi.org/10.1145/2610384.2628055](https://doi.org/10.1145/2610384.2628055) [70] D.M.Stallenberg,M.Olsthoorn,andA.Panichella,“Guess what: TestcasegenerationforJavascriptwithunsupervised probabilistic typeinference,” inSearch-Based Software Engineering - 14thInternationalSymposium,SSBSE2022,Singapore,November 17-18, 2022,Proceedings, ser. Lecture NotesinComputerScience, M. PapadakisandS.R.Vergilio,Eds.,vol.13711.Springer, 2022, pp.67–82.[Online].Available:[https://doi.org/10.1007/](https://doi.org/10.1007/) 978-3-031-21251-25 [71] K.ElHaji,“EmpiricalstudyontestgenerationusingGitHub Copilot,” Master’s thesis, Delft University of Technology, 2023. [72] E.Andreasen, L. Gong, A. Møller, M. Pradel, M. Selakovic, K. Sen, and C. Staicu, “A survey of dynamic analysis and test generation for JavaScript,”ACM Comput. Surv., vol. 50, no. 5, pp. 66:1–66:36, 2017. [Online]. Available: [https://doi.org/10.1145/3106739](https://doi.org/10.1145/3106739) [73] P.Saxena,D.Akhawe,S.Hanna,F.Mao,S.McCamant,and D. Song,“AsymbolicexecutionframeworkforJavaScript,”in 31st IEEE Symposium on Security and Privacy, S&P 2010, 16-19 May 2010, Berleley/Oakland,California,USA. IEEEComputerSociety, 2010, pp.513–528.[Online].Available: [https://doi.org/10.1109/](https://doi.org/10.1109/) SP.2010.38 [74] S.Artzi,J.Dolby,S.H.Jensen,A.Møller,andF.Tip, “A frameworkforautomatedtestingofJavaScriptweb applications,” inProceedings ofthe33rdInternationalConference on SoftwareEngineering,ICSE2011,Waikiki,Honolulu,HI, USA, May21-28,2011, R.N.Taylor,H.C.Gall,and N. Medvidovic,Eds.ACM,2011,pp.571–580.[Online]. Available:[https://doi.org/10.1145/1985793.1985871](https://doi.org/10.1145/1985793.1985871) [75] G.Li,E.Andreasen,andI.Ghosh,“Symjs:automaticsymbolic testing ofJavaScriptwebapplications,”in Proceedings ofthe 22nd ACMSIGSOFTInternationalSymposiumonFoundations of SoftwareEngineering,(FSE-22),HongKong,China,November 16 -22,2014, S.Cheung,A.Orso,andM.D.Storey,


---

