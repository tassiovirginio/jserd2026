<!-- Página 1 -->

EmpirDOI

### Sentiment

###

### Software

1Fabio&Filippo 2Federico&Nicole

#

Abstract Theopers ’However,andproblempresentsentiment’validatedusingcommentstated forkeyword-basedwellshelf tool,positiveincluding classifier, wordgoldguidelines....Keywords Sentiment.

Communicated Yasutaka

*[nicole.novielli@uniba.it](mailto:nicole.novielli@uniba.it)Fabio[fabio.calefato@uniba.it](mailto:fabio.calefato@uniba.it)Filippo[filippo.lanubile@uniba.it](mailto:filippo.lanubile@uniba.it)Federico[f.maiorano2@studenti.uniba.it](mailto:f.maiorano2@studenti.uniba.it)

1DipartimentoB^ 2DipartimentoB^70125Italy

2 & 2


---

<!-- Página 2 -->

1

Sentimentpolarity(positiveLee ).large collectionsprior polarity).istheRecentevolution),reviews2016(Guzman 2016’role ofincollaborative,Bruegge 2013 201620162015Overflow20152015With a,2015softwarebeen trained2013(Thelwall 20122015tool conclusionstudycommentsissuetrackers.predictionsthey only’communicationthey also disagreeAnotheristhecase,Noviellietal.2015Novielli )or amI^ erroneouslybecause ‘ ’ ‘ ’evidenceassumption thefully determined1965In address problemengineeringproposeexploitssemanticNovielli2015domain-dependent ofimplementedproblemsentencesobserveandby

1The packageDSM golddownload[https://github.com/collab-uniba/Senti4SD](https://github.com/collab-uniba/Senti4SD)

Empir

1andcontributiontestminedarelease goldstandard


---

<!-- Página 3 -->

Empir

awarenessassumption,assume contextualbeordersemanticrepresentsemantics.tics,2014usedword2vec2013a )wordsovercommentsresource softwareuse ofembeddingofprovidenegativedomain.firmedprovideevidenceThe2methods34study5 6used classifier, then,evaluation.threatsvalidity7 89with10present

2

Ourcodingbuildingdevelopment,featureOverflowemotionsummarizescompletefourIntheoreticalemotion).emotions itsto).In 4builtsampled(see4.1 Overall, annotationingimprovebesentiment, URLs,trainingfinal(see4.2 4.3In 4.3 wegoldstandardinterratercomputedusingschema.were assigned


---

<!-- Página 4 -->

Fig. Overview

In 5 6andrepresenting

3Background

Inaddressedproposedconcepts needed.presentedfollowing

3.1

Psychologiststivefar,emerged: considersthea2009Asfirst viewpointtypically

Empir


---

<!-- Página 5 -->

Empir

and levelcase‘’representationemotion(activationbeB afor defined^1980Onasetthethese basic1999universal1991negativedisgust) sevenpositivegratitude)appraisaltriggeredwithShaver )hierarchygranularityincludes,anger,surprise.TheConsistently goal oftheneutralthismappingannotationAppendix ).

3.2

SentiStrength2012exploitssentimentSentiStrength−whichpolarityofSimilarly,whilereceivenegativeBasedaconveybothnegativewrittenthenegative bysentenceexclamationor’increaseNegationsdetermineTherefore,pnrange±1algebraicalso report(scoreneutralTheclassificationenabling explain ’Validateddeal withabbreviations,emoticons typicallyhas,Thelwalletal.2012socialBruegge2013201420162015


---

<!-- Página 6 -->

^

Table Examples tack

Input Classification FinalSentimentScore(m aximum)  1  of  Sentiment  Detection  in  S  Scores

Negative

Negative

−

B I − −

result −

positive

trouble^ [sentence: −

sentiment)

[result: –

[overall − −

− +3

B ^

sentiment)

word]

[sentence: −

[result: –

[overall −

Neutral

− 1(absenceof

I

B

sentiment) positive

they −

length ’

[result:

showing.

[overall − Overflow  using  SentiStrength  Text  Rationale  based  on  Word  and  Sentence  Overall  Score  Score  Positive  Score  have  very  simple  and  stupid  [  trouble  [  1,  max  +  and  any  sentence]  result  =  1  (absence  of  (overall  =  you,  that  was  really  helpful  [2]  you,  that  was  really  helpful  [2]  [+1  booster  3,  max  +  and  any  sentence]  result  =  1  as  pos  >  (absence  of  negative  Positive  (overall  result  =  1)  want  them  to  resize  based  on  the  of  the  data  they  want  them  to  resize  based  on  the  length  of  the  data  showing.  [sentence:  1,  max  +  and  -  of  any  sentence]  result  =  0  as  pos  =  1  neg  =  (absence  of  negative  (overall  result  =  0)

# Empir

#


---

<!-- Página 7 -->

Empir

Tolimitationsusesentiment,Jongeling 20152015 trainsupervisedutedAanalysis2017 ).SentiStrength-SE istrengthversionad heuristicsmisclassifications2016 ).alsoperformancebenchmarking6

3.3

State-of-the-artrepresentationforandextremelyabsenceSince notionpolaritybasedcontextualDistributionalhigh-dimensionaldistributionalclaimingCharles 1991 ).meaningthefragment, beThus,homogeneouslyandtraditionally).Traditionaloccurrencesthen operatingdocumentcase,Dutnais 1997documentinapproaches2014Recently,,Collobert Weston 20082013a )wordsword embedding (LevyGoldberg 2014maximizetargetusuallyapproaches2014IntwoimplementingtheWordsfollowingwordssurrounding


---

<!-- Página 8 -->

words

4Emotion

To evaluate classifier4423 postsemotions negative emotions.38% ofpolarityIncodinggold

4.1Annotation

Theofficialcontributedpre-processedareofcodeHTMLIn), strongerusuallyunitpost whichonlyanswers,also4groupscomment,with.Aequallyexisting2009built dataset theannotationpresenceaffectively-loadedwepresence/absencecomputed positivesentimentfour typesdump.itssentimentwithone-thirdSentiStrength,one-third

4.2

Twelveamongtrained sessionlastthen provided

2[https://github.com/dav/word2vec](https://github.com/dav/word2vec)

Empir

2apubliclyavailableSkip-gramarecomputationallytrainingapproaches2013a ).approaches).


---

<!-- Página 9 -->

Empir

OverflowclarifyingTraininghome. twelvefour groupsthe performedeach item in assignedthree coders.Theemotion{positive,(seeforet ),the 12 Appendix).explicitlycodersdetected. positive polarityorlove. Conversely, negative polaritycoderssadness,coderscontextuallabel indicates absencemultipleand).Theassignment resultsdiscussed plenarydiscussion, codershaddisagreementsbiguatewhosethe

4.3

Oncecomplete,postseach itemsecondnew annotationdeadlinethen assigned600Ascomputedweighted ’among pairs1968 aredistinguishingmild disagreement,positivedisagreement,positiveassignedweightcompute inter-coderthe

Table’allannotationWeighted ’GroupC3C2C3A.76.68.73.82.76B.72.74.79.76.79C.77.77.83.80.85D.76.76.80.78.81Average’


---

<!-- Página 10 -->

including pilot annotation.allparticipants B,allTable 2values.74). This,percentageConsistentlyBecker ,et 2014 resolved disagreementsexcludedincludingresulted

5

Previousdomain-specificperformance).kinds(1)keywordsextracted dataset),specifically

5.1

ThedentsimplyaofNovielli,2015 example,each negativesentiment 2,

TableFeaturePos_words TheNeg_words TheSubj_words TheLast_posThe positiveLast_negThe negativeLast_emoThe emoticonSum_posTheSum_negTheSum_subjTheMax_posTheMax_negThePos_emoTheNeg_emoThePos_Emph Boolean,at positive endsmark,Neg_Emph Boolean,at negative endsmark,End_Pos_Emph Boolean,anEnd_Pos_Emph Boolean,anEnd_PosBoolean,End_NegBoolean,

Empir


---

<!-- Página 11 -->

Empir

positivescoresFor.Inparticular,wenumbernegativeandNeg_words ),(), emoticonLast_emo ),(),),)theandand).presenceemphasisand).capture sentiment token/emotion,),(,). lexicon-basedfor).basedcomparisontheuseThetext,emoticons aresocialwere previously1966 psycholinguisticsFrancis,2001

5.2

Keywordsatraditional1998correspondsnumbern-gramsofuppercasepresenceemoticons theNovielli ).totalreport

TableFeatureUni-gramsTotal occurrencesunigramBi-gramsTotal occurrencesbi-gramUppercase_words Total occurrences(e.g. GOOD’ , ’LaughterTotal occurrenceshahaha ’‘ ’Elongated_words Total count(e.g. scaaaaary ’’M_repetitions The(e.g., ‘ ’ ’’User_mentions Total occurrencesEndWith_EXMark Boolean,


---

<!-- Página 12 -->

5.3

ThesimilarityvectorOverflowprototyperepresenting polarityAnalogously20152013 representStackof vectorssuperposition(Smolensky 1990Theareneutralin p_pos , ,and p_neu .theprovidespolarityforallsimilarp_neg andbyrespectively,andnegative, neutralfurthersubjectivep_subj vectornegativebetteraffectively-loadedones.Weisscoreseachnamely Sim_pos ,,,(see5computedby2013a ), depicted 2600(seeranStackdumpextractedassociated millionpreprocessed postsremove URLs,codemillion

5.4

BeforeperformedStanford(Manning 2014tokenization, replaced usermeta-token @USER . notstemming lemmatizationform may convey‘‘ ’did

TableFeatureSim_posThethe.Sim_negThethe.Sim_neuThethe.Sim_subjThethe.

Empir


---

<!-- Página 13 -->

Empir

Fig. Building

removeet 2014Wegeneralizeclassification1998learningaNonly non-null2006inputlearning text classificationactuallyselectionof1998setrankthem according19976features

TableRank1Sum_pos0.56081Lexicon-based2Max_pos0.546423Pos_words0.524974Last_pos0.512735Sum_neg0.393556Max_neg0.393307Neg_words0.387608Last_neg0.382919Sum_subj0.3376510Subj_words0.3161411Sim_pos0.26473Semantic12Sim_neg0.1650713Sim_subj0.1559614Sim_obj0.1129715Last_emo0.10775Lexicon-based16Pos_emo0.0729917‘ ’0.06496Keyword-based18‘’0.0605519‘0.0564920‘ ’0.0385621Neg_emo0.03525Lexicon-based22‘0.03445Keyword-based23‘’0.0282024Uppercase_words0.0281925‘0.02800


---

<!-- Página 14 -->

TableParameterDSMDSMSVM

We experiment R20152008large-scaleclassification,ofalgorithmtrainingpotentiallyrisk ofSVMpreventingLiblinear10-foldchoseingrepeatedcombining two availableSkip-gram,space.parametersfrequentthanmin-count timeswhileinputthevector).Consistently2015 maintained defaultvalue sample parameterthan 10obtainingfinal classifieris7

6Evaluation

6.1

WetestTeam 2008caret (Kuhn 2016used trainingseektrainedthen evaluated

TablecomparisonOverallRPFRPFRPBaseline.92 .89.96 .67.95 .76SentiStrength-SESenti4SD.87 .89 .80.87 .83Improvement+6% +6%–− +19%− +9%SentiStrength

Empir


---

<!-- Página 15 -->

Empir

set,trainedclassificationset.

6.2

Afterset.Table 8F-measuresingle overall.aggregated2002 highlightIn 8

3The[http://sentistrength.wlv](http://sentistrength.wlv).ac.uk / December

3onset,which considerchooseSentiStrengthmostsoftware20152016Bruegge 2013Ortu et 2015 ,2016 ).also performanceSentiStrength-SE. mappedSentiStrength-SEsentimentforConsistently approach)andalready),(p)p+n>0 ,negative when p+n<0 ,andneutral if ) ).p considereddataset.foundperformanceandthebaseline,In 9 reportSenti4D,agreementtheconsideronlycomplement evidenceprovidedpostsclassified3Lookingobserve 24SentiStrength )Fig. ),only oneisSentiStrength3cWeallimprovementperformance,techniqueoffeatures, lexicon-basedstart byauni-includeconsiderationrepresentscategorization1998


---

<!-- Página 16 -->

TablePredictionPredictionSentiStrengthNegativeManual NegativePositiveNeutral

what extent additionalrelatedincrementalcontributionclassifier10by) role ofcolumn10)improvement previousdifferencewithByperformanceobserveyieldacceptabletheperformpoorlyhisunsatisfyingfour semantic(F .81).withrecall.67 and ofprecision toimprovementstatisticallyrecallis .73).includeconsiderationnegative up.89upSearchingwegolddifferentreported 11SentiStrengthperformance seteachofonandthree

Fig. PostsPositive andSentiStrength

Empir


---

<!-- Página 17 -->

Empir

TableExperimentalvalueRPFRPFRPFRPFN-gramsKeyword-basedKeywordKeyword.87Based* 0.05

outperformsof ),theAgain, highlightbest valuemetric.

7

Comparison SentiStrength

TablecomparisonExperimentalClassifierRPFRPFRPFRPFSentiStrength .96 .67.95 .76TrainSenti4SD.89 .80.87 .83Test(same8TrainSentiStrength .93 .89 .91.68.94 .77TestSenti4SD.91 .89 .90.80.84 .81TrainSentiStrength .93 .90.94 .67.93 .76TestSenti4SD.91 .91.83 .78.82 .80

Thetest 8 9engineering2015 ). caseSentiStrengthneutralexplicitlyasin’does notaffectiveSenti4SDproblemnumbertoF-measuretonegative to theclassifier 8recallfrom .64thetoexample,sentences arehelp youpreviousapplication


---

<!-- Página 18 -->

want toaboveHowever,thisclass recall,Fornegative‘the screen?&body field in‘torun?ofFLoggerinitializationcontrary,negative‘ ’ ‘ ).probablyprevalencenot sentimentthirdpossiblelimitationannotationMisclassificationclassificationdisagreement shouldcases. example,worry!datastoredtype islexicon ’et 2012Surprisingly,Stack(Islam 2017adheuristicsspecificallyobserved’).AsSE study.

ImplicationsSenti4SDemotions,2017specifically,betweenanalyzingtranslatingactionableinsights2017because’2012Parnin, 20152017whetherapplicationcould(i.e.,Parnin, 2015Fritzscenario,interventionfurtherdeveloper.tool low

Empir


---

<!-- Página 19 -->

Empir

severaldetrimentaldevelopers ’numberpositives negativeSentiStrength, toSimilarly,hostility(Gachechiladze 2017detecting(Tromp Pechenizkiy 2015example,sentimentand

Contribution

4[https://help.github.com/articles/locking-conversations](https://help.github.com/articles/locking-conversations)

4Ininvolveguide contributors ’optimizesensitivityconversationtoFinally,miningsoftwarerole ofet 2014).classifiertrollinget ).

Consistentlylearning1998 didincludingfull suitesemantic5groupperformedassessedtop-tensince they basedsentimentpolarityimmediatelythattheAmong topnegative(and,’tion ‘ ’’topevidencetheenthusiasmprogrammer201520152015versely,’’toppredictorsperformanceas10supervisedastraining11


---

<!-- Página 20 -->

Gold

8

OurHowever,about7

5Source: [http://stackexchange.com/sites#questionsLast](http://stackexchange.com/sites#questionsLast)‘

Ourresourcebuilt upondatasetthe2016 ).networkingquestions,andnon-technicalinfluencedoes affect).commentsquestions been),addressed).larly, detectinginterlocutorators toStackcontributors 2017et 2013The)released4000byCodeHaus.basicShaver )

5)thedevelopers ’replicationstoWeannotationbebypersonal).threat,provided)identificationassignedpresenceoppositeKappaintendimprovenumbercontroversial lead toTheemotionbuilt ournegative,Becker 201620152015

Empir


---

<!-- Página 21 -->

Empir

analysisdomain.Tables 8 9neutralcorrectlyonproportionbecausenegativebutionshowshowthepositive posts, negative posts, 38%SentiStrengthsample sentenceswordsthemakingforFinally,were provided,3%intentionCurrently,acknowledgenegativeourand

9RelatedWork

9.1Software

TryinglimitationssoftwarePanichella )Playusingmetricscomparisonthewefound itMäntylä )potential’trackingburnout.issue commentstheaffectpolarity),sensationcontrolimplementedpsychologytoevaluationOrtu et )fixingemotioncommentsfor


---

<!-- Página 22 -->

classifierpresence( ),sadness, love.featurespolitenesset 2013 theVa tu ).F-measureforclassifierBlaz and Becker )ITissemiautomaticexpandingoffeaturespolaritytheTheythey obtainSenti4SDmisclassificationative.ance onclass (F =.74,Pproblem obtainingboth negativeRPPhasIslam),SentiStrength softwareincorporates ad heuristicsmisclassificationsobservedOrtu2016sentimentsemanticsneutral’ ’ ‘ ’formedOrtushowing SentiStrength-SEPR P(F .78, =.78,PP(F .87, RStackgold6

9.2

Tobeentothevectorslexicalofinunsuper-vised2013 )and2015 ).However,research.readylettopicOverflow2014 )recoveringlinks in). 2014 )

Empir


---

<!-- Página 23 -->

Empir

usesentsspace.questions3.3proaches mainSEWordSim, words represented

10

We’classifiertestedandfurtheralso releaseforcommunitydatasetreplicatingThebuilt exploitingover 20representative’kit,informationsoftwareBy,cessfullyproblemtools.observetheandtherepresentedAscontributionfurtherrhetoricalstructurealsomixedur

elementscorrespondij and,thusdescribingjvocabularyscalabilitymodels.limitationsproaches –2013a )Mikolov 2013b ).adoptbuildingdistributionalYe)in7documentsbutionallexicalfragmentsbetations,improvesstrate benefitlinkingquestions


---

<!-- Página 24 -->

performancetools and repositoriesfurtherlexicons.workingthat will includelove,buildingemotions.

Acknowledgements This work‘Roleofthe ItalianUniversityprogramB^(SIR).beenReCaSMIUR B – ^Pierpaoloinsightfulannotatorsgold standard

Appendix:

IntheinvolvedTask Description AnnotationYoustudyarepresenceinteractions.The‘andYou.pleaseany)columnand .Emotion allowed you should tosecondchoosing primaryasshowninAppendixTable13Once emotionchoosingpositive,and .containemotion,matchdetermineareannotatedonly hasapositivefound,

Empir


---

<!-- Página 25 -->

Empir

indicaterequiredcorrespondingabsenceofcombinationallowedTable 14.

TableEmotionBasic SecondThirdPolarityEmotions EmotionsPositiveLove,LustDesire,Longing–JoyJolliness,Jubilation,ZestEnthusiasm,ContentmentOptimismPrideEnthrallmentNegativeExasperationRage Anger,Hostility,VengefulnessDisgustEnvyTorment–SadnessSadnessGlumness,DisappointmentShameNeglectIsolation,HumiliationSympathyFearNervousnessDreadEitherSurpriseor


---

<!-- Página 26 -->

TableInputannotation(secondfound)PolarityBasicEmotion(s)foundBLove Positiveawesome ^(secondBJoylooks ^CheerfulnessBlead Surprisetosurprisinglypectedcode.Bslap youB^SadnessBFearbetween Character^

TableNotLoveAnnotationxNegative NegativexPositive PositivexNegative SurprisexPositive values allowedxNexxPositiveMultiplexxMultiplexxMixed MultipleNeutral AbsenceAnnotationNegative NoPositive NoMixed NoxNeEmotionxNepolarity

### References

AndersonfocusedProceedingsSIGKDDUSA, ’[https://doi.org/10.1145/2339530.2339665](https://doi.org/10.1145/2339530.2339665)Asaduzzaman MashiyatquestionsProceedingsRepositories,USA, –Baronicontext-predicting

Empir


---

<!-- Página 27 -->

Empir

ComputationalMaryland, –Barua(2014)trendsstack over- – [https://doi.org/10.1007/s10664-012-9231-y](https://doi.org/10.1007/s10664-012-9231-y)BasilesemanticInternational2015), –Bengio3:1137 1155Blaz CCA,Conference–[https://doi.org/10.1145/2901739.2901781](https://doi.org/10.1145/2901739.2901781)Bollegalathesaurus.– [https://doi.org/10.1109/TKDE.2012.103](https://doi.org/10.1109/TKDE.2012.103)CalefatoProceedingsUSA, ‘ –CarofiglioSpringer–CohenPsychologicalCollobertmultitaskYor A, – [https://doi.org/10.1145/1390156.1390177](https://doi.org/10.1145/1390156.1390177)Danescu-Niculescu-Mizilpoliteness(1),puter Linguistics, –EkmanEmotion.Desys-org/10.1145/1276933.1276934Denning–Fan Wang CJMach 9:1871– [http://dl.acm.org/citation.cfm?id=1390681.1442794](http://dl.acm.org/citation.cfm?id=1390681.1442794)Ford DIEEEGachechiladzesoftwareIdeas EmergingUSA,org/10.1109/ICSE-NIER.2017.18GraziotinProcess, SoftwareInternationalGuzmanthe JointFSE – [https://doi.org/10.1145/2491411.2494578](https://doi.org/10.1145/2491411.2494578)GuzmanProceedingsUSA,MSR – [https://doi.org/10.1145/2597073.2597118](https://doi.org/10.1145/2597073.2597118)GuzmanaboutIEEERequirements96 [https://doi.org/10.1109/RE.2016.67](https://doi.org/10.1109/RE.2016.67)He (2009)

4.[https://doi.org/10.1109/TKDE.2008.239](https://doi.org/10.1109/TKDE.2008.239)HelleputteversionHogenboomCommun–IslamProceedingsPress,USA,[https://doi.org/10.1109/MSR.2017.9](https://doi.org/10.1109/MSR.2017.9)


---

<!-- Página 28 -->

JoachimsProceedingsECML ‘JoachimsConferenceData226,JongelingsentimentengineeringEvolutionInternationalon,[https://doi.org/10.1109/ICSM.2015.7332508](https://doi.org/10.1109/ICSM.2015.7332508)Kucuktuncanswers.DataNew York, ‘[https://doi.org/10.1145/2124295.2124371](https://doi.org/10.1145/2124295.2124371)KuhnWing,Mayer,RCandan.,Regression–CRAN.R-project.org/package=caretLandauer(1997)acquisition,representation–Lazarusadaptation.LevyM,(Eds)Curran– [http://papers.nips.cc/paper/5477-neural-word-embedding-as-](http://papers.nips.cc/paper/5477-neural-word-embedding-as-)implicit-matrix-factorization.pdfMaalej21(3):311 – [https://doi.org/10.1007/s00766-016-0251-9](https://doi.org/10.1007/s00766-016-0251-9)ManninglanguageLinguistics:–Mäntylä AdamsPossibilitiesproductivity?Mining– [https://doi.org/10.1145](https://doi.org/10.1145)/2901739.2901752MäntyläarousalRepositoriesUSA, [https://doi.org/10.1109/MSR.2017.47](https://doi.org/10.1109/MSR.2017.47)Meta (2017).exchange-is-too-harsh-to-MikolovCoRRMikolovphrasesandAdvancesCur- Associates,Miller–[https://doi.org/10.1080/01690969108406936](https://doi.org/10.1080/01690969108406936)MitchellMohammad (2016)otherMeiselmanMohammadofMüller and Fritzprogress.'15),MurgiadevelopersexploratoryemotionsProceedingsRepositories, 271,NovielliComput–

.

Empir


---

<!-- Página 29 -->

Empir

Noviellirole ofProceedings InternationalYork, [https://doi.org/10.1145/2661685.2661689](https://doi.org/10.1145/2661685.2661689)Novielliecosystem.InternationalYork, –Ortu M,TonelliEmpiricalMiningUSA, –Ortu M,softwareProceedingsRepositories, USA, – [https://doi.org/10.1145/2901739.2903505](https://doi.org/10.1145/2901739.2903505)Pang B,sentiment 2):1 135.org/10.1561/1500000011Panichellaapp?classifyingSoftwareEvolutionPennebakerWordPleteaemotion:onACM, [https://doi.org/10.1145/2597073.2597117](https://doi.org/10.1145/2597073.2597117)REnvironmentStatistical[http://www.R-project.org](http://www.R-project.org) ,RahmansourcecrowdsourcedManipulation,––/SCAM.2015.7335404Russell1178Saifdata sparsitytwitter.PiperidisEvaluation ’ EuropeanSchererProbabilityriskreactionSci –Sebastiani[https://doi.org/10.1145/505282.505283](https://doi.org/10.1145/505282.505283)SEmotionInternationalEmotionEngineering.Shaverapproach.– [https://doi.org/10.1037//0022-3514.52.6.1061](https://doi.org/10.1037//0022-3514.52.6.1061)SinhaInternational523,Smolenskythetionist– [https://doi.org/10.1016/0004-3702(90)90007-M](https://doi.org/10.1016/0004-3702(90)90007-M)SochercompositionalityNaturalpp –Strapparavavol–Stoneanalysis.Th

elwallInfTechnol– [https://doi.org/10.1002/asi.21662](https://doi.org/10.1002/asi.21662)Tian Y,CompanionProceedingsICSE– [https://doi.org/10.1145/2591062.2591071](https://doi.org/10.1145/2591062.2591071)


---

<!-- Página 30 -->

TrompWiratunga602.WittgensteinYeCinformationSoftware– 2016, – [https://doi](https://doi).org/10.1145/2884781.2884862

Fabioisinintersectionsoftwaremining

Filippois FullCollaborativeresearching(2008), theandGeneral ProgramConference

Empir


---

<!-- Página 31 -->

Empir

Federicoisresearchincludemachine

NicoleisreceivedScienceintersectionaffectivewith adevelopers ’started ICSESoftware


---

