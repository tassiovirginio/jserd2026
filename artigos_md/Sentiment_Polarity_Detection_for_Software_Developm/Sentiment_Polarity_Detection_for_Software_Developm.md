<!-- Página 1 -->

#

# Sentiment

# Polarity

# Detection

# forSoftware

# Development

# DipartimentoJonico, UniversityofBari“A. Moro”, via

# Duomo, 259

# 74123 Taranto, Italy.

# DipartimentodiInfomatica, UniversityofBari“A. Moro”, viaE. Orabona, 4

# 70125, Bari, Italy

# Email: {fabio.calefato, filippo.lanubile,

# nicole.novielli}@uniba.it,

# f.maiorano2@studenti.uniba.it

# Abstract

# Theroleofsentimentanalysisisincreasinglyemerging

# tostudy

# software

# developers’ emotions

# mining

# crowd

# generated contentwithin

# socialsoftwareengineeringtools

# . However,

# off

# the

# shelf

# sentimentanalysis

# tools

# havebeen trained

# technical

# domains

# and

# general

# purpose

# thus

# resulting

# misclassification

# of

# and

# problem

# Here,

# e

# Senti4SD,

# a

# developers’

# communicationchannels

# Senti4

# SD istrainedandvalidatedusinga

# gold standard

# ofStack Overflowquestions, answers, and

# commentsmanuallyannotatedforsentimentpolarity.

# Itexploits

# a suite ofboth

# lexicon

# andkeyword

# based features, aswell

# assemantic f

# eaturesbasedonwordembe

# dding.

# ithrespect toa

# mainstream

# off

# the

# shelf

# tool

# , whichweuseasabaseline

# Senti4SD

# reduc

# themisclassificationsofneutral

# andpositive posts

# asemotionallynegative.

# Toencourage

# replications

# , w

# release

# a labpackage including

# the classifier,

# the

# wordembeddingspace, and

# the gold standard

# withannotationguidelines

# Keywords

# Sentiment

# nalysis

# ommunication

# hannels

# Stack

# ;

# Social

# Software

# Engineering

# Introduction

# Sentimentanalysisisthestudyofthe

# subjectivity(neutralvs. emotionallyloaded) andpolarity(positivevs. negative) ofa

# text

# (PangandLee2008).

# It

# rel

# ies

# on sentimentlexicons,

# that is,

# largecollectionsofwords

# , each

# annotatedwith

# itsown

# positive

# ornegativeorientation

# (i.e., prio

# r polarity)

# . Theoverall sentiment ofatext isthereforecomputed

# the

# prior

# polarity ofthe

# containedwords.

# Recentstudies

# suggestapproaches forenhancingsoftwaredevelopment, maintenance

# andevolutionby

# applying

# sentiment

# analysisonStack

# Overflow

# Rahman

# etal. 2015)

# , appreviews

# Maalej

# etal. 2016)

# , andtweets

# containingcommentson

# software

# application

# Guzman

# etal. 2016)

# Furtherresearch

# on developers’ emotions

# addressesthe role ofaffectinsocial

# software

# engineering

# applyingsentimentanalysistothe contentavailable in

# collaborative developmentenvironments

# suchas GitHub

# Guzman

# etal. 2014, GuzmanandBruegge 2013,

# Sinha

# etal.2016)

# Jira

# Mäntylä

# etal. 2016,

# Ortu

# etal. 2015)

# , andStack

# Overflow

# (Calefatoetal

# . 2015,

# Novielli

# etal. 2015

# Withanotablefewexceptions

# (BlazandB

# ecker2016,

# Panichellaetal. 2015)

# empiricalsoftware engineering

# studies

# have

# exploited

# off

# the

# shelf

# sentimentanalysis

# tools

# that

# havebeen trained on non

# softwareengineeringdocuments, suchas movie

# reviews

# Socher

# etal. 2013)

# orpostscrawled fromgeneral

# purposesocialmedia, such asTwitterand

# YouTube

# Thelwall

# et

# al. 2012)

# Jongelingetal.

# (2017)

# show

# howthechoiceofthesentimentanalysistoolmay impacttheconclusion validity of

# empiricalstudiesbyperforminga benchmarkingstudyonsevendatasets, including

# discussionsand commentsfrom

# Stack

# Overflow

# and

# issuetrackers.

# By

# compar

# ing

# thepredicti

# onsof

# widelyused

# off

# the

# shelf

# sentimentanalysis tools

# they

# show

# that not onlythe

# toolsdonot agreewithhumanannotationof

# developers’ communication channels

# , but theyalsodisagree

# among

# themselves.


---

<!-- Página 2 -->

# bug

# Anotherchallengetoaddressisthenegativebiasof

# existing

# sentimentanalysis tools, thatis themisclassificationofneutral

# technical textsasemotionallynegative. It is

# particularly

# thecaseof

# reportsor problemdescriptions

# Blazand

# Becke

# r 20

# 16,

# Noviellietal. 2015

# .

# Noviellietal.

# (2015)

# showhow

# sentences like

# Whatisthebestwaytokillacriticalprocess

# or

# I am

# missingaparenthesisbutI don’tknowwhere

# are erroneouslyclassifiedasnegative because both

# tokill

# and

# miss

# ing

# hold

# a negative polarityinthe SentiStrengthlexicon. Thisevidence isconsistentwith

# the

# meaning

# use

# assumptionthatthe sense

# ofan expression isfully dete

# rminedbyitscontextof use

# Wittgenstein

# Inthispaper

# weaddressthe

# problemofapplying

# sentimentanalysis

# to

# the

# software

# engineering

# discipline

# Weproposea

# entimentanalysisclassifier

# , named Senti4SD,

# which

# exploitsa suite oflexicon

# based, keyword

# based, and semanticfeatures

# (BasileandNovielli2015)

# for appropri

# atelydealingwith

# the

# domain

# dependentuseof

# lexicon

# Theapproachimplemented

# by

# successfully

# the

# ying

# neutral

#

# observe

# improvement

# precision

# for

# % improvement

# recall

# baseline,

# by

# and first

# contributionofthispaper.

# trainandtest

# Senti4SD

# , webuilt ago

# ldstandardof4

# post

# min

# edfrom

# StackOverflow. As

# a secondcontributionofthisstudy, we release ourgoldstandard

# aswellasthe emotionannotationguidelines

# tobeusedin

# further studiesonemotionawarenessinsoftwareengineering.

# Consistently

# withthe

# meaning

# use

# assumption, we assume

# that thecontextual polarityofawordcanbecorrectlyinferredbyitsuse. Thus,

# orderto derive

# semanticfeature

# , we

# represent

#

# .

# we

# explo

# neural

# network

# based

# distributionalsemantics

# , alsoknownaswordembedding

# Levyand

# Goldberg

# Specifically, w

# e used

# word2vec

# Mikolov

# etal. 2013)

# tobuildaDistributional SemanticModel (DSM)

# wherewordsarerepresentedas

# high

# dimensional

# vectors

# . The

# DSM

# , which

# buil

# on acollection ofover20 million questions, answers, and commentsfromStack Overflow

# represent

# valuable

# for

# software

#

# who

# intend

# of

# word

# text

# categorizationtasks. Therefore, we release the DSM asa thirdcontributionofthisstudy

# Finally, asafourth

# contribution

# we

# provide

# a

# the

# the

# shelf tools

# when

# engineeringdomain.

# Thecontributionof

# lexicon

# based, keyword

# based, and semantic

# features

# is

# confirmedby

# ourempirical

# evaluation

# leveraging

# feature

# e evidence

# of

# lso

# minimal

# setoftrainingdocuments

# Thepaperisstructuredasfollows.

# InSection

# wepresentanoverview oftheresearchmethods

# followedby

# thetheoretical

# background

# in

# Section

# escribesthe annotationstudyforbuildingthe goldstandard. In

# Sections

# and

# we

# describe

# respectively

# thefeatures

# used by ourclassifier,

# andthe

# n, theexperimental

# setupan

# d evaluation.

# Discussionandthreat

# tovalidityare

# presented

# Sections

# and

# respectively.

# InSection

# wepositionourcontributionwithrespecttorelated

# ork

# . Finally,

# in Section

# we

# raw

# onclusion

# and

# present

# futurework.

# Resea

# rchMethods

# Our

# researchleveragesamixof

# qualitativeand quantitative

# methods

# includingmanual codingoftextual data

# for building

# a goldstandardonemotionpolarityinsoftware development

# naturallanguageprocessing techniques

# for featureextraction

# fromStackOverflowtexts

# , and

# machinelea

# rning

# for training

# ouremotion polarity classifier

# Fig. 1 summ

# arizesthe process

# wefollowed

# in the current study

# hecompleteprocess

# is

# organized in

# four

# sequentialphases.

# Thefulllabpackag

# e includingSenti4SD, the DSM andthe goldstandardis available fordownloadat:

# https://github.com/collab

# uniba/Senti4SD


---

<!-- Página 3 -->

#

# In

# annotation(see Section

# wedefine

# InPhase2

# answers, andcommentsextractedfromStackOverflow

# documents

# questions,

# and

# readability

# Theannotationphase

# (seeSections

# InPhase3

# software

# The

# procedureand

# criterion.

# InPhase4

# performance

# identified

# the

# 3.1

# . The

# first

# output

# the

# taxonomyof

# emotionsand

# the c

# oding guidelines

# to adopt in the

# annotationstudy

# (seeAppendixA)

# (seeSection

# thea

# otation study

# was

# carriedout. W

# built

# (seeSection

# 4.1

# Overall, theannotationsampleiscomposedof4,800

# User

# contributed

# by discard

# ing

# text

# elementsthatshouldnotbe annotatedforsentiment, i.e. URLs, code snippets, andHTML tags.

# included

# the

# training

# ofcoders

# anda pilotannotationstudybefore the finalannotation

# 4.2

# and

# 4.3

# (seeSection

# 4.3

# weusedthe

# resultsof theannotationphasetobuildour

# was

# computed

# using

# schema

# Thegoldlabels

# were

# assignedtodocumentsinthe annotationsample builtu

# (seeSections

# and

# , we

# used

# thegoldstandardforemotionpolaritytotra

# was

# comparedwithoff

# the

# shelftools representingthestateoftheartforsenti

# Fig.

# Overviewoftheresearchprocess

# chose

# the to

# mappingwithpolarity. Asasecondoutput,

# theannotation

# sample

# were

# preprocessed

#

# gold standard

# assess

# inandevaluateourclassifier, whose

# mentanalysisonsocialmedia.

# by leveraging questions,

# for emotionpolarityin

# lity

# singamajorityvoting

# was

# performed


---

<!-- Página 4 -->

# 3.

# Background

# Inorder tofullycomprehendtheaddressedproblemandtheproposedsolution, some

# pointsofsuch supporting conceptsarepresented in thefollowing sections.

# 3.1.

# Emotion

# Modeling

# Psychologistsworkedatdecodingemotionsfordecades,

# developing theoriesbased on cognitivepsychology and natural

# language

# mmunication

# Sofar, t

# wopointsofview

# have

# emerged

# considersemotionsasa continuousfunctionofone or

# moredimensions

# , while the

# other

# assumesthata limitedsetofbasic emotionsexists

# Asregardsthefirstviewpoint(c

# ontinuousfunction),

# miningaffectivestatesfrom text

# acrosstwodimensions:

# (1)

# theaffect polarity

# orvalence

# and

# (2) the

# level ofactivation

# thecaseofthe‘circumplex

# model’ ofaffect, whichrepresentsemotionsaccordingtoabi

# capturingthe emotionvalence (pleasantvs. unpleasant) andarousal(activationvs. deactivation).

# emo

# tion can be considered a

# belforafuzzy set, defined asa

# classwithoutsharpboundaries

# Ontheotherhand, theoriesfollowingthediscrete

# viewpoint

# agree onthe idea thata limitedsetofbasic emotionsexists,

# although

# thereisno

# consensusaboutthe nature an

# d thenumberofthesebasicemotions.

# emotions

# specific

# signals

# and

# negative

# (anger, fright, anxiety, guilt, shame, sadness, envy,

# jealousy, anddisgust) andsevenpositive(happiness, pride, relief,

# love, hope, compassion, andgratitude) emotions, withtheirappraisal patterns: positiveemotionsaretriggeredifthesituat

# experiencediscongruentwith

# individual goal

# otherwi

# senegativeemotions areprompted

# Shaveretal.

# defin

# a tree

# structuredhierarchicalclassificationofemotions. Thehierarchyorganizes emotionlabels

# inthreelevelsofhierarchical clusters.

# Eachlevel

# refines

# thegranularityofthepreviousone, thusprovidingmoreindicationon

# itsnature. Theframeworkincludes, at thetoplevel, sixbasicemotions, namelylove, joy, anger, sadness, fear, andsurpris

# framework

# is

# easytounderstand

# , thankstotheintui

# tivenatureoftheemotionlabels

# classifierforemotionpolarity, we

# maptheemotionsinthe

# modelbyShaveretal.

# Section

# . We use this mapping

# asa theoretical

# frameworktoinformour annotationguidelines(see

# 3.2.

# PolarityDetectionwithSentiStrength

# SentiStrength

# Thelwall

# etal. 2012)

# isa

# state

# the

# art,

# lexicon

# based classifierthatexploitsasentimentlexicon builtby

# combiningentriesfromdifferentlinguistic resources. Inthe SentiStrengthlexicon, eachnegative wordreceivesa senti

# rangingfrom

# 2 to

# , whichrepresentsitspriorpolari

# ty(i.e., thepolarityofthetermout ofitscontextual use). Similarly, positive

# wordsareassociated

# with

# a score between

# 2 and

# , whileneutral wordsreceivescoresequal to

# emoticons

# are

# Based

# SentiStrengthoutputsbothpositiveandnegativesentimentscoresforanyinputtextwritteninEnglish. Itdeterminestheov

# positiveand negative scores to a text byconsidering the

# maximum among all the sentencescores, based on the prior polarity of

# theirterms.

# Intensifiers,

# i.e.

# exclamat

# ionmarks

# orverbssuch as‘really’

# , aretreatedasboosterwordsandincreasetheword

# sentimentscores. Negations

# are alsotreatedanddetermi

# theinversionofthepolarityscoreforagivenword

# overallpositive

# andnegative

# sentimentscores issuedbythetoolrangefrom

# key conceptsareneeded. Themain

# CaroÞglio

# etal. 2009)

# typically

# involves

# alsoknownasarousalor

# dimensionalrepresentation schema

# Accordingtothismodel, each

# Russell

# Accordingto

# Ekman

# (1991)

# Con

# istentlywithourgoal oftraininga

# topositive,

# negative, and neutralpolarity

# AppendixA

# 1.

# Positiveandnegative

# 1 (absenceof

# positive/negative

# ing

# them

# intensity. It is

# (1999)

# basic

# describes

# ion

# e.

# he

# (see

# ).

# mentscore

# erall

# The

# refore, the

# sentiment) to


---

<!-- Página 5 -->

# ±

# 5 (extremely positive/negative).

# Basedontheiralgebra

# icsum, SentiStrengthcanalsoreport theoverall trinaryscore, i.e. the

# overallpositive(score= 1), negative(score=

# 1) and neutral(score= 0).

# xamplesareprovided in

# TABLE 1.

# classificationreportedinthe secondcolumnofthe table

# obtained by enabling the‘explain’

# option in SentiStrength.

# TABLE 1.

# XAMPLES OF

# ENTIMENT

# ETECTION IN

# TACK

# VERFLOW US

# ING

# ENTI

# TRENGTH

# Final

# SentimentS

# core (maximum)

# InputText

# ClassificationRationalebasedonWordand

# SentenceScores

# Negative

# Score

# PositiveScore

# I haveverysimpleandstupid

# 3] trouble

# 2]

# (absenceof

# I haveverysimpleand

# [sentence: 1,

# positive

# stupidtrouble

# [result: max+ and

# ofany sentence]

# sentiment)

# [overallresult=

# 1 aspos<

# neg]

# Thank

# [2] you,

# that was really helpful

# [2] [+1

# (absenceof

# Thankyou, thatwas

# booster

# word] [sentence: 3,

# 1]

# negative

# really helpful

# [result: max+ and

# ofany sentence]

# sentiment)

# [overallresult= 1 aspos>

# neg]

# I wantthemtoresize

# I wantthemto

# resizebasedonthelen

# gth ofthe

# (absenceof

# based on thelength of

# datathey'reshowing

# [sentence: 1,

# 1]

# negative

# positive

# the data they're

# [result: max+ and

# ofany sentence]

# sentiment)

# showing.

# overall

# result= 0 aspos=1 neg=

# Validated

#

# SentiStrength

# can

# with abbreviations,

# and

# emoticons

# that typicallyoccurinonlineinteractions

# Assuch, ithasbeenwidelyadoptedinsocialcomputing

# 2012,

# Thelwall

# etal. 2012)

# andsocialsoftware engineering(

# GuzmanandBruegge2013, Guzmanetal. 201

# Noviellietal2015

# Toovercomethelimitationsandthreatstovalidityderivedfromtheuseofoff

# the

# shelfsentiment

# analysistoolsinempirical

# softwareengineering

# studies

# (BlazandBecker 2016, Jongelingetal. 2017, Noviellietal2015), wetrainanemotionpolarity

# classifierina supervisedmachine learningsettingbyleveraginga goldstandardoftechnicaltextsc

# ontributed by developersin

# StackOverflow.

# customizedversionofSentiStrengthhasbeendevelopedtosupportsentimentanalysisinsoftware engineering

# Zibran

# . Thetool iscalledSentiStrength

# SE andi

# s builtupontheSentiStrengthAPI

# Itleveragesamanuallyadjusted

# version oftheSentiStrength lexicon and implements

# ad hoc

# heuristicsto correctthemisclassificationsobserved when running

# SentiStrengthonthe

# Ortu

# dataset(Ortu etal. 2016).

# Inour

# evaluation,

# wealsoincludetheper

# formance

# ofSentiStrength

# benchmarking

# (seeSection

# 3.3.

# Distributional

# SemanticModel

# State

# the

# artsentimentanalysistoolsandlexiconsrelyon

# a dictionary

# based

# wordrepresentation

# (seeNoviellietal. 2015

# for anoverview).

# Wordsare

# reatedasatomicunitsand

# are associatedtoa priorpolarity

# expressedas

# sentimentscore, ranging

# fromextremelynegativetoextremelypositivewiththeabsen

# ce ofsentimentinthe middle. Since the

# notion of

# nottaken into account

# thepolarity

# ofatext

# is

# only

# based on thepriorpo

# larityofthewordsit containsandcannot beadjusted

# based

# on their

# contextualmeaning.

# DistributionalSema

# nticModels(DSMs) representwordsasmathematicalpointsin high

# dimensionalvectorspaces.

# rel

# ies

# on theso

# called

# distributionalhypothesis

# claimingthatlinguistic itemswithsimilarmeaningsoccurinthe same context

# Therationalefor

# OverallScore

# Negative(

# overall

# result=

# Positive(

# overall

# result=

# Neutral(overall

# result= 0)

# Kucuktunc

# etal.

# Maalejetal. 2016,

# Islam

# and

# SE for

# word

# similarity

# DSM


---

<!-- Página 6 -->

# (

# Millerand

# Charles

# Based

# on theassumption thatthemeaning ofadocumentisdetermined by themeaning ofthewords

# that appearinit

# , a

# text unit (e.g., adocument, asentence, atext fragment, etc.)

# canbe representedasthe vectorsumofallthe

# word

# vectorsoccurring in

# it. Thus, in

# a DSM, b

# oth wordsand documents

# are homogeneouslyrepresented

# asvectors

# and

# canbe

# comparedusingsimilaritymetrics

# that measure

# theirclosenessinthespace

# , traditionallyt

# hrough cosinesimilarity

# Mikolov

# et

# al. 2013

# Traditionalappro

# achestodistributionalsemanticscreate wordvectors

# countingthe occurrencesoftermsina corpusand

# then

# operating adimensionality reduction ofword

# documentmatrices. Itisthecase, forexample, ofLatentSemanticAnalysis

# (Landauer and

# Dutnai

# , which

# operate

# a singularvalue decompositiononthe originalterm

# documentmatrix to alow

# dimension latentvectorspace. Such methodsareusually referred in

# the

# literature

# as

# context

# counting

# approaches

# Baroni

# etal.

# Recently,

# neural

# network

# based approaches

# havebeen proposed

# Bengio

# etal. 2003,

# Collobert

# and

# Weston

# 2008,

# Mikolov

# et

# for

# These

# approaches

# ,

# word

# embedding

# Levyand

# Goldbe

# learnthevector

# that maximizetheprobabilityofthecontextsinwhichthetarget word

# appears. Forthisreason, theyare usuallyreferredtoas

# context

# predicting

# approaches

# Baroni

# etal.

# Inour study, we

# leveragetheapproachdefinedby

# Milokov

# etal.

# (2013)

# . Theyd

# evelopedtwomodel

# for

# implementing

# context

# predicting approaches:

# (1) t

# heContinuousBag

# Words(CBOW) modelpredict

# thetarget wordbyconsideringthe

# previousand following

# wordsina

# symmetricalcontextwindow

# ; (2)

# theSkip

# grammodelpredictsthesurrounding words

# based on thetargetword.

# Botharchitectu

# resareimplementedinword2vec

# a publiclyavailable toolforbuildinga

# DSM

# from

# a large collectionofdocuments.

# oth CBOW and Skip

# gram

# models

# are capable ofscalinguptolarge data sets

# withbillions

# of

# words

# andare

# computationally

# moreefficientfortraininghigh

# dimensionalspaces

# than

# context

# countingapproaches

# Mikolov

# etal. 2013

# Furthermore

# , theyoutperf

# ormtraditionalcontext

# countingapproachesonstandardlexicalsemanticsbenchmarks

# Baroni

# etal. 2014)

# Dataset

# GoldStandardforEmotionP

# olarity

# in

# SoftwareD

# evelopment

# To

# a

# 423

# Overflow.

#

# balanced:

#

# positive

# emotions

# present

# negative

# emotions.

# No

# emotionsare observedf

# ortheremaining 38% ofposts, thusthey receivethe

# neutral

# larity label.

# Inthefollowing, wedescribethesamplingandcoding

# processes

# adoptedforbuildingthe goldstandard.

# 4.1.

# CreatingtheAnnotationSample

# heannotation sample

# was

# extract

# fromtheofficial

# StackOverflow

# dump

# ofuser

# contributedcontent

# m July2008 to

# September2015. Toimprovethe

# readability, wepre

# processed allthepost

# , usingregularexpressions,

# todiscardall those

# elementsthatare outofthe scope ofthe sentimentannotationtask

# , e.g. code snippets, URLs

# andHTML tags

# In

# previous

# study

# Novielli

# etal. 2015)

# wefoundthat

# trongerexpression

# ofemotionsareusually detected in comments

# rather thanin

# question oranswers. Therefore, weconsider

# asa unitofanalysisthe StackOverflow

# post

# whichincludesnotonly

# question

# and

# answer

# butalso

# comment

# provided

# communitymember

# Hence, conceptuallyweareaddressing3x

# groups

# https://github.com/dav/word2vec


---

<!-- Página 7 -->

# ,

# positive, negative, neutral}

# ofposts, thatis

# four

# typesofStackOverflowpostsin

# {question,

# ,

# withthreepossibleemotionstylesin

# A desirablepropertyofatrainingsetisthat

# its

# itemsareequallydistributedacrossthe

# existing

# classesof

# values

# (Heand

# Garcia, 2009)

# Therefore, webuil

# thedataset fortheann

# otation by performing opportunisticsampling ofpostsbased on

# both

# thepresenceof

# affectively

# loadedlexiconandtheirtype.

# Todoso,

# use

# SentiStrengthto

# assessthe presence/absence of

# affective lexiconina post. We

# compute

# thepositiveandnegativesentiment scoresfor

# thetext of

# allthe

# four typesof posts

# extractedfromthe StackOverflowdump

# . Then, werandomlyselectedthesame

# number

# ofitemsbased on the

# type

# of

# post

# and

# sentimentscores. Oursampleforannotation

# contains4

# 800 itemsoverall

# , equallydistributedwithrespect tothetypesofposts

# andp

# arity

# , i.e.

# third

# ofpostssco

# redaspositivebySentiS

# trength,

# asnegative, and

# asneutral.

# 4.2.

# PilotAnnotationStudy

# Twelvecoders

# participated in theemotion polarity annotation task. The

# coders

# wererecruitedamong

# graduateCS

# students

# the

# University

# ofBari

# and

# trainedina

# joint

# hour

# session

# the

# last

# author. She

# first

# explainedthe codingguidelinesand

# then

# provided asam

# pleof25 Stack Overflowpoststo beannotated indi

# vidually in 30

# minutes.

# Then

# , a

# follow

# up discussion

# aimedatclarifyingpossible ambiguitiesinthe interpretationofthe codingguidelines.

# raining

# wascompleted

# withapilotsubsetof100 itemstobeannotatedindividuallyathome. Thetwelveparticipantswere

# organized

# four group

# ofthreecoderseach. Therefore, thepilotstudy wasperformed on 400 postsoveralland each itemin

# the dataset was assigned to

# three coders.

# Thecoderswererequestedtoindicatetheemotionpolarity, with

# possiblevaluein

# {positive, negative, neutral,

# (seeAppendixA for guidelines)

# Analogouslyto

# Murgiaetal.

# (2014)

# werefertothe

# Shaveretal.

# tree

# structured

# mework

# for

# detecting emotionsin thetext

# (see

# TableA in

# AppendixA

# Themaindifferencewiththe

# annotationstudy

# is

# that

# ourcodersto providea

# polarity label

# accordingtothe

# specific

# emotiondetected.

# In

# ositive

# polarity

# was

# indicatedwhen

# the

# coders

# cted

# eitherjoyorlove. Conversely,

# negative

# polarity should beindicated

# when

# thecodersidentified

# anger, sadness, orfear.

# Regarding

# surpris

# weask

# thecoderstodeterminethepolaritybasedon

# contextualinformation. The

# neutral

# label

# indicates

# theabsenceofemotion. Post

# conveyingmultiple emotionswithopposite

# polarity (i.e.

# and

# ) wereannotatedas

# mixed

# Thed

# eadline

# wassetaweek

# afterthe assignment

# andthe resultsofthe annotationwere discussedina

# hour

# plenary meeting

# withtheexperimenter. Duringthisdiscussion, thecoders

# had to

# resolv

# thedisagreementsonthepilot sample. Thissessionwas

# also

# used to disambiguateunclearpartsoftheguidelinesaswellasto enrich themwith borderlineexampleswhoseannotation

# wasagreed

# during themeeting. Afterthedisagreementsweresolved, thepilotannotation

# becamethefirstbuilding block

# ofthe

# ld standard.

# 4.3.

# EmotionPolarityCoding: ExtendedStudy

# Oncethetrainingwascomplete, weassignedanew setof500 poststoeachcoder. Onceagain, eachitemwasannotatedby

# threecoders. Overall, 2,000 newitemswereannotatedinthissecondstep.

# Again,

# oderswererequired to performthisnew

# annotationtaskindividually

# . The

# deadline for returning the annotation was set in three weeks. We then assigned the final set of

# 600 poststo thecoders. Overall, 2,400 additionalnewitemswereannotated in thisf

# inal step.


---

<!-- Página 8 -->

#

# Asanevidenceofthe

# reliabilityof thecodingschema

# andprocedure, we computedthe weightedCohen’s

# Kappa

# amongthe

# pairsofraters

# Cohen

# Weareinterestedin

# distinguishing

# between

# mild

# disagreement, thatisthedisagreementbetween

# negative/positive

# neutral

# and

# strong

# disagreement,

# positive

# judgments. Weassignedaweight = 2 tostrongdisagreement andaweight = 1 tomilddisagreement.

# Wecomputethe

# inter

# coder

# reliabi

# lity

# for theentireset, includingthepilot

# set

# annotation.

# Theagreementiscomputedforallthefourgroupsofparticipants

# (A,

# and

# for allpair of

# coders

# (C1, C2, andC3)

# ineachgroup

# (see

# TABLE 2)

# e note

# a substantialagreementwith

# Kappa

# valuesranging in [.66, .80] (average.74). Thisevidenceisconfirmed also by thevaluesofthe

# observed agreement

# , which

# is the percentage of cases on which the raters agree, ranging in [.73, .85] (average .79

# Consistentlywithpreviousresearchon

# emotionannotation

# (BlazandBecker 2016, Murgiaetal. 2014),

# weresolvedthe

# disagreementsby applying amajority voting

# criterion

# . Weexcludedfromthegoldstandardall thepostsforwhichopposite

# polarity labelswereprovided, including mixed cases

# (3%)

# , eveninpresenceofmajorityagreement. Thefinal goldstandard

# resultedin4,423 posts, representing92% of 4,800 annotateditems.

# TABLE 2.

# EIGHTED

# OHEN

# APPA

# GREEMENT

# FOR ALL THE COUPLE O

# F CODERS IN THE

# OLARITY ANNOTATION

# TUDY

# Weighted

# Cohen’s

# Kappaforp

# airsofcoders

# ObservedAgreementforp

# Group

# C1 andC2

# and C

# .66

# .74

# .74

# .77

# .77

# .77

# .76

# .76

# .76

# AverageWeightedCohen’sKappa.74

# AverageObservedAgreement.

# EmotionPolarityClassifier

# : FeatureDescription

# andSystemSetup

# Previous

#

# specific

# the

# performance

# analysis

# Bollegala

# etal. 2013)

# Therefore

# weexploitthreedifferentkindsoffeaturesbased

# (1)

# genericsentimentlexicons,

# (2)

# keywords

# (i.e.,

# gram

# extracted

#

# (3)

# word

# specificallytrainedonsoftwareengineeringdata

# 5.1.

# Lexicon

# based features

# Thefirstsetoffeaturesexploit

# existing

# sentimentlexicons.

# Theapproachistotally

# independent

# thelexiconchosenand

# simplyrequires that

# a sentimentscore isprovided

# for eachentryof theinput

# (NovielliandBasile, 2015)

# Forexample,

# inthe

# lexiconusedby

# SentiS

# trength

# , eachnegativewordisassociated

# with

# an

# a priori

# sentimentscorein

# . Similarly, positive

# wordsreceiveascorein

# . A list of objective words is also provided, with scores equal to

# oragiven post

# wecompute

# thelexicon

# based featuresreported in

# TABLE 3.

# Inparticular, wecompute

# thenumberof

# tokenswithpositive

# and

# negativepriorpolarity

# and

# theoverall numberoftokenswitheitherpositive

# or (

# ),

# the

# emoticon

# ,

# for

# ),

# negative

# ), andsubjective

# tokens, andthemaximumpositiveandnegativescore

# observed

# in

# and

# We

# presence with


---

<!-- Página 9 -->

# Pos_Emph

# exclamationmarks, indicatingemphasis(

# and combined

# lexicon

# based featureshavebeen already

# Our

# based

# representedbySentiStrength, f

# supportedbyits abilitytodeal

# used

# in

# Furthermore,

# validated in thescopeofempiricalresearch in sentimentanalysis

# Francis, 2001)

# Feature

# Pos_words

# Thenumberoftokenswithpositive

# Neg_words

# Thenumberoftokenswithnegative

# Subj_words

# Thenumber

# Last_pos

# Thescoreofthelastpositivetokeninthepost

# Last_neg

# Thescoreofthelastnegativetokeninthepost

# Last_emo

# Thescoreofthelastemoticoninthepost

# Sum_pos

# Thesumofthescoreforthetokenswithpositive

# Sum_neg

# Thesumofthescoreforthetokenswithnegative

# Sum_subj

# Thesumofthescoreforthetokenswitheitherpositiveornegativeprior

# Max_pos

# Themaximumscoreforthetokenswithpositive

# Max_neg

# Themaximumscoreforthetokenswithnegative

# Pos_emo

# Thenumberof

# Neg_emo

# Thenumberofemoticonswith

# Boolean, istrue

# Pos_Emph

# emphasis.

# Boolean, istrue

# Neg_Emph

# emphasis.

# End_Pos_Emph

# Boolean, istrue

# End_Pos_Emph

# Boolean, istrue

# End_

# Pos

# Boolean, istrueifthedocumentendswithapositivetokenoremoticon.

# End_

# Neg

# Boolean, istrueifthedocumentendswitha

# 5.2.

# Keyword

# based features

# Keyword

# based

# featuresincludeword

# ourfeature

# set

# weconsideruni

# achn

# gramin ourcorpuscorrespondsto afeature, with thenumberofoccurrences

# we

# intensifiers, t

# hepresenceofpositiveand negative

# Novielli2015)

# Thetotalnumberofkeyword

# and

# Finally, wecapturethesentimentofthelasttoken/emotion

# exclamation

# mark

# used forthe

# sentimentanalysis

# ofcrowd

# generated content

# independent

# the

# To

# fair

# orthisstudy, weuse

# theSentiStrength

# lexicon

# Thechoiceof

# theSentiStrengthlexicon

# shortinformaltext,

# asitincludesalso

# abbreviations,

# ntensifiers

# andemoticons

# incorporates

# scores linguistic

#

# (Stoneetal., 1966)

# andpsycholinguistics(Pennebakerand

# TABLE 3.

# ENTIMENT

# EXICON

# EATURES

# Description

# prior

# polarity

# prior

# polarity

# oftokenswith eithernegativeorpositivepriorpolarity

# prior

# polarity

# prior

# polarity

# polarity

# prior

# polarity

# in the post

# prior

# polarity

# in the post

# emoticons

# withpositiveprior

# polarity

# negative

# prior

# polarity

# if the document

# hasatleastonepositivetoken and endswith

# exclamation

# if the document

# hasatleastonenegativetoken and endswith

# exclamation

# if the document

# ends witha positive tokenandanexclamationmark

# if the document

# ends witha negative tokenandanexclamationmark

# negative

# token or emoticon.

# countsfor

# grams

# appearingina document, inourcase a StackOverflowpost.

# andbi

# grams

# Consistent

# y with traditionalapproachesto textclassification

# itsvalue. Otherthanincluding

# blogging,

# elongated

# as

# emoticons

# , andtheoccurrenceofslangexpressionof

# based featuresis

# 76,34

# . We report a summary in

# TABLE 4.

# All

# Mohammad

# etal. 2013)

# isfurther

# that are

# typically

# mark, indicating

# mark, indicating

# In

# Joachims

# grams,

# laughter

# (Basileand


---

<!-- Página 10 -->

#

# TABLE 4.

# EYWORD

# ASED

# EATURES

# Feature

# Description

# Uni

# grams

# Totaloccur

# ences ofuni

# grams. Overall, ourunigramdictionary counts

# entries.

# ams

# Totaloccurrencesofbi

# grams. Overall, ourbi

# gramdictionary counts

# 65,844

# entries.

# Totaloccurrencesofuppercasewords

# Uppercase_words

# (e.g. ‘GOOD’, ‘BAD’)

# Totaloccurrencesof

# slangexpressions forlaughter

# , such as ‘

# hah

# aha

# ’ or

# abbreviations

# as ‘LOL’ occurringin

# Laughter

# Senti

# trength list of abbreviations.

# Totalcountoftokenswithrepeatedcharacters

# Elongated_words

# (e.g. 'scaaaaary', 'gooooood')

# Thetotaloccurrencesofstringswithrepeated

# question orexclamation marks.

# M_repetitions

# (e.g., '????', '!!!!', '?!?!?!?!?')

# Totaloccurrencesofusermentions

# User_mentions

# (intheform@username)

# EndWith_EXMark

# Boolean, trueifthedocumentendswithanexclamationmark.

# 5.3.

# Semanticfeatures

# The

# the

# Stack

# prototypevectors

# representingthepolarityclassesin

# DSM

# . Analogouslyto

# (BasileandNovielli2015, NovielliandStrapparava

# 2013),

# werepresentaStackOverflow document(i.e., aquestion, answer, orcomment) intheDSM asthevectorsumofallthe

# vectorsofwordsoccurring in thedocument, using thesuperposition operator

# Smolensky

# The

# prototypevectors

# are vectorrepresen

# tationofthepositive, negative, andneutral classes

# intheDSM

# and

# . A prototypevectorisavectorrepresentationofthelexical profileforagivenpolarityclass, basedona

# sentimentlexiconthatprovides priorpolaritysco

# resfor words. Tocomputetheprototypevector

# for thepositiveclass

# sumallthevectors forwords withpositivepolarityscoreinthechosensentimentlexicon.

# Inasimilar fashion, we

# and

# by summing up, respectively, allthe

# negativeand neutralwordsin the

# chosen

# sentimentlexicon. In

# we

# list and included

# SentiStrength

# We

# subjectiveprototype

# vectorby summing up thepositiveand negative

# word

# vectors, to bettercapturethedifferencesin

# the lexical choice of neutral sentences and

# affectively

# loaded ones.

# Weusedthefourprototypevectorstocomputethesemanticfeatures, thatisthesimila

# rityscoresbetweenthedocument

# vector

# i.e., aStackOverflowpost

# andeachprototype vector,

# namely

# ThesemanticfeaturesarecomputedonaDSM builtonStackOverflowdata, usingtheCBOW architecture

# word2vec

# Mikolov

# etal. 2013)

# as

# depicted in Fig.

# Wechooseaconfigurationwith600 vectordimensions, afterhaving

# repeatedthe10

# foldcross

# validation forparametertuning (seeSection

# 5.4

# Weranword2veconacorpusextractedfromthe

# StackOverflowofficialdumpupdatedtoSeptember2015.

# Weextracted3.8 millionquestionsfromthedumpwiththeassociated

# 5.9

# swers    codes,

# snippets, obtainingacollectionofmorethan20 millionposts with912,201,785 tokens overall.

# TABLE 5.

# EMANTIC

# EATURES

# Feature

# Description

# Sim_pos

# Thecosinesimilaritybetweenthe

# post

# vectorand theobjectiveprototypevectorp_pos.

# Sim_neg

# Thecosinesimilaritybetweenthe

# post

# vectorand theobjectiveprototypevectorp_neg.

# Sim_neu

# Thecosinesimilaritybetweenthe

# post

# vectorand theobjectiveprototypevectorp_neu.

# Sim_subj

# Thecosinesimilaritybetweenthe

# post

# vectorand thesubjectiveprototypevectorp_subj.

# the

# , namely

# we

# compute

# thisstudy,

# (see

# TABLE

# implementedby


---

<!-- Página 11 -->

#

# 5.4.

# Before

# tokenization, wereplacedtheusermentionswiththemeta

# sinceaninflectedfo

# holds lexicon.

# not consistently

# researchinsentimentc

# We using SVM

# dimensionalfeaturespace, which isatypicalscenario in textclassification taskslikeours

# SVM isastate

# numberoffeatures

# Onewaytoavoiddealingwithsuchhighdimensionalinputspaceswouldbetoperformsubstantialfeatureselection. However,

# insupervisedlearningfortext classificationtasks, veryfewfeaturesareactuallyirrelevant, andfeature

# significantloss ofinformation

# valueofourfeatures, weanalyzeand rank themaccording to theirinformation gain

# top 25 features ranked by information gain.

# WeranourexperimentusingtheR interface

# scalelinearclassificationwithSVM. Forlinearclassification, theonlyparameteris thecostparameterC. ToolargeC valu

# makesthecostofmisclassificationhigh, thusforcingthealgorithm tobetterexplainthetra

# theriskofoverfitting. Tofine

# utility on ourtraining setin a10

# the We

# architectures

# CBOW

# Furthermore, word2vechastwoinputparametersforrare

# than

# defi

# ned

# prediction

# SystemSetup and ParameterTuning

# extractingallfeatures, we

# Mikolov

# rmmayconveyimportantinformationaboutpolarity. Itisthecase, for exampleof ‘

# lassification tasks

# the

# artlearningtechnique forsuchhigh

# , whereeachitemhasonly

# timesarediscardedfromthedocument collectionbeforestartingtheDSM training, whilefrequent words(as

# input

# etal. 2013)

# Fig.

# BuildingtheDSM onStackOverflowdata

# performed tokenization using theStanford NLP suite

# token

# Saif

# etal. 2014)

# dimensionalsparsedatasetswith alargenumberofitemsand alarge

# s << N

# nullfeatures

# Joachims

# 1998).

# Thus, weexploitthefullsetoffeatures. Still, inordertoassessthepredictive

# Helleputte

# toLiblinear

# tunetheSVM parameterwhilestill preventingoverfitting, werantheLiblinearparametertuning

# fold

# cross

# validation

# setting. Wechosetheoptimalva

# gram,

# wordpruningandfrequentwordsub

# sampled

#

# Consistentlywithpreviousresearch

# Manning

# etal. 2014)

# . Wedidnot performanystemmingnorlemmatization

# ail

# ’ and‘ailing’, which

# Joachims

# . Inparticular, linear

# Joachims

# , astypical i

# n presenceofn

# selectionresults ina

# (Mitchell1997)

# . In

# TABLE 6

# Fan

# etal. 2008),

# anopensource libraryforlarge

# iningdatabut potentiallyinducing

# luefortheC parameterbymaximizing

# {200,

# 800,

# sampling: words appearingless

# (BasileandNovielli2015)

# , wemaintainedthedefault

# . Duringthe

# , wereport the

# grams.

# es


---

<!-- Página 12 -->

# sam

# valueforthe

# 346,236 terms.

# Theoptimalconfiguration, usedtotrainourfinalclassifieroverthetrainingset, isreportedin

# parameterwhilediscarding thetermswith lessthan

# occurrences, thusobtaining afinalvocabulary of

# TABLE 6.

# OP

# FEATURES RANKED BY I

# NFORMATION GAIN

# Rank

# Feature

# InformationGain

# FeatureGroup

# Sum_pos

# 0.56081

# Max_pos

# 0.54642

# Pos_words

# 0.52497

# Last_pos

# 0.51273

# Sum_neg

# 0.39355

# Lexicon

# Max_neg

# 0.3933

# Neg_words

# 0.3876

# Last_neg

# 0.38291

# Sum_subj

# 0.33765

# Subj_words

# 0.31614

# Sim_pos

# 0.26473

# Sim_neg

# 0.16507

# Semantic

# Sim_subj

# 0.15596

# Sim_obj

# 0.11297

# Last_emo

# 0.10775

# Lexicon

# Pos_emo

# 0.07299

# ‘great’

# 0.06496

# ‘excellent’

# 0.06055

# Keyword

# ‘:)’

# 0.05649

# ‘thanks’

# 0.03856

# Neg_emo

# 0.03525

# Lexicon

# ‘hate’

# 0.03445

# ‘annoying’

# 0.0282

# Keyword

# Uppercase_words

# 0.02819

# ‘:(‘

# 0.028

# TABLE 7.

# YSTEM

# ETUP AFTER

# ARAMETER

# PTIMIZATION

# Parameter

# Value

# word2vecarchitecture

# ContinuousBag

# Words(CBOW)

# DSM

# DSM dimensions

# SVM

# 0.05

# based

# based

# based

# based

# based

# TABLE 7.


---

<!-- Página 13 -->

#

# Evaluation

# 6.1.

# CreationofTrainandTestSets

# We

# splitthegoldset

# intotrain

# ing

# (70%) andtest

# (30%)

# set

# , using

# theR

# R DevelopmentCoreTeam

# package

# caret

# Kuhn

# 2016)

# for stratifiedsampling.

# Weuse

# thetrain

# ing

# setto

# seek

# theoptimal parametersettingforourclassifier

# seeSection

# 5.4

# Thefinalmodel

# s trainedonthewholetrain

# ing

# setusing

# theoptimal configuration

# and

# then

# evaluatedonthe testset, to

# assesstowhatdegree the trainedmodelisable togeneralize

# ntimentpolarity classification

# on unseen newdata

# fromtheheld

# outtestset.

# 6.2.

# Results

# After

# learned

# model

# TABLE

# eports

# performanceobtained in termsof

# ecall,

# recision,

# andF

# measureforthesingleclassesandoverall. Theoverallperformanceis

# computedadoptingmicro

# averagingasaggregatedmetric

# Sebastiani

# highlight

# inbold

# thebest valueforeachmetric

# In

# TABLE

# wealsoreporttheperformanceofSentiStrength

# on the

# StackOverflow

# test set, whichweconsidera

# s a

# baseline

# for

# the

# performance

# assessment

# ofSenti4

# WechooseSentiStrengthbecauseitisthemostwidelyemployedtoolinsentiment

# anal

# ysisstudiesin softwareengineering

# Calefato

# etal. 2015,

# Guzman

# etal. 2016,

# GuzmanandBruegge2013, Ortuetal. 2015,

# Sinha

# et

# In

# SE.

# e

# ped

# both

# SentiStrength

# and

# SentiStrength

# SE

# scores toacategoricalsentimentlabelin

# {positive,

# negative}

# for

# entire question,

# answerorcomment

# . Consistentlywiththe

# approachdefinedbySentiStrengthauthors

# Thelwall

# etal. 2012)

# andalreadyadopted

# TABLE

# ERFORMANCE OF

# ENTI

# 4SD

# AND COMPARISON

# WITH

# ENTI

# TRENGTH

# BASELINE

# Overall

# Positive

# Negative

# Neutral

# Baseline(SentiStrength)

# .82

# .82

# .82

# .92

# .89

# .90

# .96

# .67

# .79

# .64

# .95

# .76

# SentiStrength

# .79

# .73

# .73

# Senti4SD

# .87

# .87

# .87

# .92

# .92

# .92

# .89

# .80

# .84

# .80

# .87

# .83

# Improvementoverthe

# +6%

# +6%

# +6%

# +3%

# +2%

# +19%

# +6%

# +25%

# +9%

# SentiStrength

# baseline

# TABLE

# GREEMENT

# ETWEEN

# ANUAL

# ABELING AND

# REDICTION ON THE

# TACK

# VERFLOW

# EST

# Prediction

# SentiStrength

# Senti4SD

# Negative

# Positive

# Neutral

# Negative

# 345 (9

# 5.8

# (1.9

# 8 (

# 2.2

# 321 (89

# 3 (0.8

# 36 (10

# Positive

# 30 (

# 6.6

# 20 (91.7

# 8 (

# 1.8

# 11 (2

# 423 (9

# 2.4

# 24 (

# 5.2

# Manual

# Neutral

# 140 (

# 27.6

# 44 (

# 8.7

# 324 (6

# 3.8

# 0 (13.8

# 32 (6

# 406 (79.9

# TheevaluationshavebeenperformedusingtheSentiStrengthJavaAPI obtainedfrom

# http://sentistrength.wlv.ac.uk/

# on December2016.


---

<!-- Página 14 -->

# in

# previou

# benchmarking studies

# onsider

# a textas

# Textswithascoreof

# p

# dataset. However, no such controversialcasesarefound in ourdataset.

# % improvementinprecisionforthenegative

# SentiStrengthbaseline

# , which in turn outperforms SentiStrength

# n TABLE

# wereporttheconfusionmatrixforbothSentiStrengthandSenti4D, showingtheagreementbetween

# labelingandthepolaritypredictedbyeachtool.

# complementthe

# evidence provided

# negative,

# positive, and neutral

# negativecasesrecognized only by SentiStrength

# Fig.

# .b)

# ,

# Conversely, the13 recognizedonlybySenti4SD aremisclassifiedbySentiStrength

# recogn

# ize

# d only by Senti4SD (see

# We

# Senti4SD. Ourgoalistoassesswhethertheimprovementofpe

# machinelearningtechniqueoris

# based features) wepropose. Westartby computing the

# Suchamodeldoesnotincludeconsiderationofanysentiment

# categorizationbasedonmachine learning

# contribute

# by

# Senti4SD byconsideringincrementalfeaturesettings, inordertoas

# performance.

# Resultsarereportedin

# TABLE 6

# ) abouttheroleof eachfeaturegroup. Thelastcolumnof

# statistically

#

# between settingsiscomputed by performing the

# Bycomparing

# the

# performance

# classifierbasedonn

# gramsdoesnotyield an acceptable

# Fig.

# PostsCorrectlyClassifiedasNegative(a), Positive(b), andNeutral(c) bySenti4SD andSentiStrength

# Jongeling

# etal. 2017)

# give

# thepositive(

# nd negative(

# when

# p + n > 0

# when

# p + n <0

# , and

# and

#

# are consideredhavinganundeterminedsentimentandshouldbe removedfromthe

# Looking

# at

# theperformanceofSenti4SD, weobserve

# classanda 25% improvementinrecallforthe neutralclasswithrespecttothe

# SE.

# WeconsideronlySentiStrengthbecauseitoutperformsSentiStregth

# by the

# confusionmatrix

# withVenndiagramsrepresentingthepostscorrectlyclassified

# by SentiStren

# gth and Senti4SD (seeFig. 3

# ).

# Lookingatthepredictions, weobservethatthe24

# (see

# Fig.

# .a)

# are classifiedasneutralbySenti4SD. Asforpositive posts

# aspositive

# Fig.

# .c)

# are

# classif

# ied mainly as negative (69

# /84

# ).

# ious

# rformance

# withrespecttoSentiStrength

# rather

# dueto theadditionalfeatures(fullsetofkeyword

# based, semanticfeatures, and lexicon

# performancewith asimplemodelincluding only theuni

# specificfeatureandrepresents thetraditionalapproachtotext

# Joachims

# . By

# doing so, wewantto assessto whatextenttheadditional

# related Then,

# sess thecontributionofeachfeaturegrouptotheclassifier

# TABLE

# andcomplementthe evidence providedbythe informat

# TABLE

# value <0.05

# a

# Statistical

# Chi

# squared

# test with

# = 0.05.

# ofSenti4SD leveraging differentsetsoffeatures, weobservethatsimply training asupervised

# overall

# performance

# (F = .

# Byleveragingthefullsetofkey

# ) scoresissuedbythetool,

# if

# (p = n) and (p < 4)

# Asforneutral, the84 cases

# isaresult oftheadopted

# evaluate

# the

# iongainanalysis(see

# ) indicateswhether

# significance

# we

# themanual

# SE.

# We

# as

# andbi

# grams.

# features

# weobservea

# difference

# board


---

<!-- Página 15 -->

# t

# TABLE

# ERFORMANCE OF

# ENTI

# 4SD

# WITH INCREMENTAL FEA

# TURE SETTINGS

# ExperimentalSetting

# Overall

# Positive

# Negative

# Neutral

# value <0.05

# gramsonly

# .69

# .69

# .69

# .84

# .75

# .79

# .88

# .57

# .69

# .42

# .85

# .56

# Keyword

# based features

# .79

# .79

# .79

# .84

# .84

# .84

# .67

# .80

# .73

# .83

# .74

# .79

# Keyword+ Semantics

# .81

# .81

# .81

# .86

# .86

# .86

# .73

# .80

# .76

# .83

# .78

# .81

# Keyword+ Semantics+ LexiconBased

# .87

# .87

# .87

# .92

# .92

# .92

# .89

# .80

# .84

# .80

# .87

# .83

# (fullfeatureset)

# * p < 0.05

# based features

# heoverallperfo

# rmanceimprove

# toF = .79. However, suchaclassifierwouldstill performpoorlyifcompared

# to

# In

# negative

# is .67)

# Adding

# four

# semantic

# performance

# further improved

# (F=.81).

# Inparticular,

# addingonlyfourfeatures(i.e., the cosine similarityofthe documentwith

# thesentiment prototypevectors)

# weobservea

# improvement ofthe

# negative

# recallfrom.67 to.73 andof the

# neutral

# precision

# from.74 to.78.

# However,

# whi

# letheimprovement isstatisticallysignificant,

# the

# recallfor

# negative

# isstill low

# (R=.73).

# Finally,

# weincludeconsiderationoflexicon

# based features, which furtherincreasetherecallof

# negative

# up to .89

# andthe precisionof

# neutral

# up to .87.

# Searching

# for further evidenceof therobustnessof theapproachimplementedbySenti4SD, we

# also

# assessitsperformance

# by splitting ourgold standard into train and testsetwith differentpercentages. Resultsarereported in

# TABLE

# andcompared

# withtheSentiStrengthperformanceonthesametestsetforeachiteration. Foreach

# setting

# , wecompare

# thebehaviorofthetwo

# classifier

# by performing a

# Chi

# square

# test onthepredictionsissue

# d by Senti4SD and SentiStrength

# , observing

# valuelower

# than

# 0.05

# In

# all

# thethree

# settings, Senti4S

# outperformsSentiStrength,

# evenwitha reducedtrainings

# et(lastrowof

# TABLE

# , with 30% of the gold standard

# used

# as

# training

# set.

# Again, wehighlightinboldthebestvalueforeachmetric.

# Discussion

# ComparisonwiththeSentiStrengthbaseline.

# The

# performanceofSentiStrength on ourtestset(

# see

# TABLE

# and

# confirm

# previous

# findingsabout

# negativebias

# inthesoftwareengineeringdomain

# Noviellietal.

# Inthecaseof

# TABLE

# ERFORMANCE OF

# ENTI

# 4SD

# AND COMPARISON WITH

# ENTI

# TRENGTH WITH DIFFERE

# NT TRAIN

# TEST PROPORTIONS

# ExperimentalSetting

# Overall

# Positive

# Negative

# Neutral

# Classifier

# Train= 70%

# SentiStrength

# .82

# .82

# .82

# .92

# .89

# .90

# .96

# .67

# .79

# .64

# .95

# .76

# Test= 30%

# Senti4SD

# .87

# .87

# .87

# .92

# .92

# .92

# .89

# .80

# .84

# .80

# .87

# .83

# (sameasTABLE 8

# SentiStrength

# .82

# .82

# .82

# .93

# .89

# .91

# .95

# .68

# .79

# .64

# .94

# .77

# Train= 50%

# Test= 50%

# Senti4SD

# .85

# .85

# .85

# .91

# .89

# .90

# .87

# .80

# .83

# .78

# .84

# .81

# SentiStrength

# .82

# .82

# .82

# .93

# .90

# .91

# .94

# .67

# .78

# .64

# .93

# .76

# Train= 30%

# Test= 70%

# Senti4SD

# .84

# .84

# .84

# .91

# .91

# .91

# .83

# .78

# .80

# .79

# .82

# .80


---

<!-- Página 16 -->

#

# StackOverflow

# dataset

# SentiStrength

# erroneously

# classifies2

# 8% ofneutralpostsasnegative

# with

# recallfor neutral

# class

# .64

# ) and

# low

# precision forthenegativeone(

# .67

# Since

# StackOverflowisexplicitlydesignedtosupportdeveloperslooking

# for

# discussions

# misclassified

# negative

# in

# the

# ‘problem’

# lexicon, which do

# esnotnecessarilyindicate the intentiontoshowanyaffective state.

# Senti4SD

# able problem

# such

# negative

# TABLE

# shows

# misclassifie

# d from

# Senti

# trength

# Senti4SD

# As

# the

# easure

# increasesfrom.79 to.84

# for

# the

# negative

# class

# andfrom

# .76 to.83

# for

# the

# neutral

# , thusdepictingamorebalancedclassifier

# (seeTABLE

# Inparticular,

# ur

# classifierimprove

# therecall ofneutral

# documents

# from.64

# up to .80 (25

# % of improvement)

# andthe precisionofnegative

# documents

# from.67

# up to .80 (19

# % ofimprovement)

# Forexample,

# SentiStrengtherroneously

# classifiesasnegative sentencesthatare insteadneutral, ast

# hefollowing

# s: ‘

# Thiswillhelpyoutocomebacktotheprevious

# activity. Asperyourcode, theapplication wascompletelykilled.

# ’, ‘

# Orifyoudon'twanttoworryaboutheightcalculationdo

# this

# Onthecontrary, Senti4SD

# correctlylabel

# s theabove

# sentences

# asneutral.

# However

# , we

# observethatthis

# gain in precision isobtained atthe

# expense of

# thenegative

# class

# recall

# , whichdecreasesfrom

# .96 to.89

# Forexample, SentiStrengthcorrectlyclassifiesas

# negativethefollowing

# posts

# : ‘

# Isit

# possibleto preventa userfrom

# editingthe title ofanode onthe node editscreen? One ofthe thingsI really detestaboutDrupalisthe rigidity ofthe ti

# tle& body

# field

# and

# Ew, bit

# class

# initializationsectionhasrun? Inother

# words,

# couldaninstance ofTMyObjecttry touse

# FLogger

# beforeit'sbeen setin the

# initializationsection?

# . Onthecontrary, thetwo

# posts

# are

# erroneouslylabeledasneutral

# by Senti4SD

# eveninpresence of

# the

# negative

# lexicon(i.e.,

# detest

# and‘

# ugly

# ).

# Such

# misclassificatio

# nsare

# probably dueto the

# prevalenceofneutrallexicon

# inthe

# posts

# . Specifically,

# inthefirst

# post

# thefirst sentencedoesnot carryanysentiment

# whileinthesecond

# post

# thesecondandthird

# sentence

# are

# neutral.

# A possiblew

# aytoovercome thislimitation

# occurring with long posts

# istoperform

# finer

# grained

# annotatio

# ata sentence level

# in order

# train a sentence

# based version ofSenti4SD

# Misclassification

#

# ve

# %

# the

# cases

# when

# the

# classification

#

# SentiStrength

# (see

# TABLE

# ).

# Thisiswhatweconsiderastrongdisagreementthatshouldbeavoided.

# Senti4SD

# reduce

# such

# misclassificatio

# n to

# % of

# the

# cases.

# Forexample, sentenceslike‘

# s insouneed

# not

# worry! Internallythedataisalwaysstored

# as

# o

# ,  data

# erroneously

#

# SentiStrengthas

# negativedueto

# thepresenceof

# negativelexicon (‘worry’)

# evenifSentiStrengthissupposedtocorrectlydeal

# withnegations

# (Thelwalletal. 2012

# which

# should

# determinepolarity inversion

# Surprisingly

# , SentiStrength

# SE producesalower

# performance

# than

# SentiStrength

# on ourStack Overflowgold

# standardalbeit

# it

# SentiStrength

#

# This

# SE

# incorporates

# ad hoc

# heuristicsand word polarity scores

# that

# are

# specif

# ically

# designed to solvemisclassificationsobserved on a

# small

# unbalanced datasetof400 developers’

# commentsinJira (Ortuetal. 2016)

# . Assuch,

# overfitting

# isaplausible

# explana

# tion

# for

# the decay in

# performance

# ofSentiStrength

# SE

# in our study

# Implic

# ations.

# Senti4SD

#

# the

# engineering(

# Noviellietal. 2014

# Mäntyläetal. 2017)

# Morespecifically, weenvision

# the

# emergence

# ofsentimentanalysistools

# monitoring

#

# ntributed

#

# reviews

# analyzing

# the

# affect

# expressedinthiscommunicationandtranslatingthe resultsintoactionable insight

# Gachechiladze

# etal

# Amongothers, negativeaffectivestates

# deserve

# attention

# becauseof

# theirdetrimental impact on

# developers’

# productivity


---

<!-- Página 17 -->

#

# (Denning2012,

# FordandParnin, 2015, Graziotinetal. 2017

# When

# implementinga

# sentiment

# classifier

# deciding whetherto

# optimizeby precision orby

# recall

# isnot atrivial decision

# , which

# depend

# on theapplication scenario.

# Earlydetectionofnegative

# sentimenttowards self, suchas frustration

# couldbe usefultodesigntoolsforsupportingdevelopers

# experiencing

# cognitive

# difficulties

# i.e.

# , learninganewlanguageor

# solvingtasks

# withhighreasoningcomplexity) (FordandParnin, 2015),

# aswellas

# intheirdailyprogrammingtasks

# (Müller andFritz2015).

# Insuchascenario, amonitoringtoolmightsu

# ggest

# theintervention

# ofan expertor

# provide

# link

# tofurthermaterial anddocumentation

# tosupport thedeveloper

# . However, asentiment analysistool

# with

# for

# would

# produce

# positive

# ,

# undesired

# erroneou

# s interruptions

# that are

# detrimental

# developers'

# productivity and focus.

# Insuchcases

# , beingabletoreduce

# thenumberoffalsepositive

# for negativesentimentbecomescrucialandSenti4SD shouldbepreferredtoS

# entiStrength, due to

# its higher precision.

# Similarly,

# timely

# detection of

# negativesentiment

# towards

# peers

# , suchasangerandhostility

# Gachechiladzeetal2017

# might

# be

# detecting

# code

# of

# Tromp

# and

# Pechenizkiy

# enhancing

# effective

# management.

# Forexample, sentimentanalysismaysupportGitHubuserswhowanttobenotifiedofheatedconversationand

# lockthembeforeflamewarsbreakout.

# Inscenariosthatinvolve

# human intervention

# toguidethecontri

# butors’ behaviortowards

# a

# ,

# recall

# , leverage

# SentiStrength higher

# sensitivitytonegative

# emotions

# . Conversely, ifautomaticfilteringofoffensivecomm

# entsorconversation

# is envisaged, it becomes important to

# optimizeby precision by using Senti4SD, to avoid ban

# ning

# neutralconversations

# Finally,

# sentiment

# analysis

# is

# technique

# also

# useful

# for

# g e

# to

# understand theroleofsentimentin security discussions(Pleteaetal. 2014)

# and

# commitsinGitHub(Guzmanetal. 2014)

# In

# suchscenarios,

# sentiment

# classifier

# specifically

# trainedandvalidatedinthesoftwareengineeringdomain

# allows

# controllin

# for

# threats to validity

# dueto

# inappropriate instrumentation

# , as

# argued

# Jongelingetal(2017)

# Contribution

# of

# Consistently

#

# Joachims

# , wed

# notperformfeatureselection, thusincluding in ourevaluation setting thefullsuiteoflexicon

# based,

# keyword

# based

# andsemantic features

# described in Section

# Asafurtherevidenceoftheimportanceofeachgroupoffeatures,

# weperform

# ananalysisbasedoninformationgain

# (see

# TABLE

# andassess

# Senti4SD performancebyleveragingdifferen

# featuresettings(see

# TABLE

# ).

# The

# top

# tenp

# redictive

# featuresbelongtothegroupof lexicon

# based

# , whichis

# an

# expected

# result

# sincethey

# are basedonsentimentlexic

# onsspecifically

# designed to represent

# thesentiment polarityassociationtowords

# Theyare

# immediately followed by the four semantic features that measure the similarity between a document and the linguistic

# profile class.

# Among

# keyword

# based

# we

# positive

# and

# emoticons

# and

# ,

# Expressions

# gratitude

# i.e.,

# )

# appreciation

# )

# gram  that

# paying

# gratitude

# for thehelpreceived

# aswellas

# enthusiasm

# for thesolutionprovided

# are

# the

# maincausesforpositivesentimentinthe

# socialprogrammerecosystem

# Calefato

# etal. 2015,

# Novielli

# Ortu

# etal. 2015)

# Conversely, expressionof

# angerand

# frustration(

# i.e.,

# are amongthe

# top

# predictorsfornegativesentiment

# The

# contributionofeachfeature

# group performance

# confirmed

#

# ging

# ,

# reported

# 1

# Furthermore,

# e that

# producesimilarperformancealso in presenceofa

# minimal

# setoftrai

# ning documents(seeTABLE 1

# ).

# https://help.github.com

# /articles/locking

# conversations


---

<!-- Página 18 -->

#

# Goldstandard.

# Our

# manuallyannotateddataset

# isthefirst

# resource

# on emotion pol

# arity

# tobe

# builtupon thecorpusof

# Stack

# Overflow

# As

# dataset

# represents

#

# in

# empirical

#

# software

# (SEmotion

# Stack

# an online programmers

# networking

# and questions,

# in diffusion

# documentation.

# mongthenon

# technical factors

# that

# caninfluence the membersof

# onlinecommunities, theemotionalstyleof

# a

# ect

# Calefato

# et

# eing

# towards

# ons

# not

# answered

# Novielli

# etal. 2015)

# , whichisagoal addressedbycurrent researchoneffectiveknowledge

# shari

# Anderson

# etal.

# Similarly

# ,

# allow

# the

# ity

# towards

# appropriate

# interaction

# pattern

# . This

# is

# anopenprobleminthe Stack

# Overflow

# community

# asusers

# complainabout

# harsh commentscoming fromexpert

# contributors

# Meta201

# , which

# may

# impair

# successful

# question

# answering

# Asaduzzaman

# etal. 2013)

# Thereleaseofourgoldstandardcomplem

# entsthe effortofOrtuetal.

# (2016)

# who

# recentlyreleaseda

# dataset

# of2,000 issue

# comments

# sentences

#

# the

# reposito

# ries

# ecosystems

# namely Apache, Spring, JBoss, and CodeHaus

# heirdatasetisannotated using thebasicemotion labelsin

# theframeworkby

# Shaveretal.

# (1987)

# that we also adopt in the present study.

# Threat

# toValidity

# ur produce

# results

# f

# outside

# However,

# Stack

# so

# popularamong softwaredevelopers(currently

# used by

# about

# millionsoftwaredevelopers

# reasonably

# confident

# that the

# data

# set

# is

# resent

# ative

# developers’

# style

# Nevertheless,

#

# are

# further

# increase the external validity

# to the

# entire

# software

# developerecosystem

# Webuil

# gold standard on emotion polarity

# throughmanual annotation

# Emotion

# annotation

# isasubjectiveprocess

# since

# affect

# influenced

# by

# personal

# Scherer

# To

# mitigate

# we

# provided

# clear

# ee

# grounded

# theoretical

# for

# identification

# based on the

# model

# by Shaveretal. (1987)

# Furthermore

# , polaritylabel

# were

# assignedusingmajorityagreement

# amongthree coders

# To

# bemoreconservative, even in presenceofm

# ajorityagreement,

# weexcludedfromthegoldstandardall

# thepostsforwhichoppositepolaritylabelswereprovided.

# Theinterrateragreement(

# average

# weightedCohen’sKappa

# = 0.7

# confirm

# a good

# reliabilityof thegoldstandard.

# Nevertheless

# , weintendtoimprovecodingguidelinesbyenrichingthenumber

# ofexamples, especially

# for

# those more controversial that lead to coding conflicts.

# Thesamplesetfortheemotionannotationexperiment

# wasbuiltusingSentiStrength.

# builtoursamples

# et

# have

# third

# postsscored by SentiStrength aspositive,

# asnegative, and

# asneutral.

# However, ashighlightedby

# previousresearch (Blazand Becker2016, Jongeling etal. 2017, Noviellietal. 2015)

# off

# the

# shelftools forse

# ntimentanalysis

# report

# limitedperformance

# when

# detecting sentimentin

# thesoftwareengineering

# domain.

# Inparticular, SentiStrengthtendsto

# misclassifyneutralsentencesasnegative(see

# TABLES

# and

# ).

# Asaresult, weendedupincludinginoursample

# setahigher

# proportion ofneutralsentencesthatwereoriginally misclassified asnegative

# by SentiStregth

# andlatercorrectlyclassifiedas

# neutralby ourcoders

# AnothercauseoferrorwhenusingSentiStrengthonourdatais

# the

# misclassificationofpos

# itivepostsas

# Source: http://stackexchange.com/sites#questionsLastacc

# essed:


---

<!-- Página 19 -->

#

# negative(see

# TABLE

# ). Assuch, asmallproportionof thepostsoriginallyincludedinthesampleannotationsetbecauserated

# asnegative bySentiStrengthwere subsequentlyclassifiedaspositive bythe coders.

# throughtheannotationstudyconfirms

# these

# issue

# andshowshowthe negative classisunderrepresentedinour

# gold

# 35%

# positive

# posts,

# 27%

# negative

# and

# SentiStrengthtocreatethesamplesetisthat

# the

# sentences inourdataset

# lexicon. Hence,

# weobserveaverygoodperformanceofthetoolonourgoldstandard(F = .82,

# challenging

# baselineforourclassification task.

# Finally, we

# excludedfromthe goldstandardallthe postsforwhichopposite polaritylabelswere provided,

# the3% ofall annotateddata. Ourchoiceisjustifiedbytheintentiontonot introducenoiseinthe

# training Currently,

# would

# acknowledge thata minorityofpostsmightpresentbothpositive andnegative emotions. Inourfuture

# Senti4SD bytrainingseparatebinaryclassifiersforpositiveandnegative

# RelatedWork

# 9.1.

# SentimentAnalysisResourcesfor

# SoftwareEngineering

# Tryingtoovercomethelimitationsposed

# using

# off

# the

# shelfsentimentanalysis tools,

# recently

# startedto

# develop

# their own tool

# Panichella

# etal.

# (2015)

# appl

# ied

# sentimentanalysis forclassifyinguserreviews inGooglePlayandAppleStore. They

# theirownclassif

# er

# on 2,000 manually

# annotated

# reviews

# using NaïveBayes

# not

# reportevaluationmetricsfor their

# classifiersowe are notable tomake anycomparisonwiththeir

# completeness, we alsoexperimentedwithNaïve Bayes, astheysuggest,

# Mäntylä

# etal.

# investigate

# thepotential ofmining

# developers’

# productivity and burnout. They measure

# theemotionsinissuecommentsintermsof

# (i.e., theaffectpo

# larity),

# rousal(i.e., theaffectintensity), and

# ominance(i.e., thesensation of

# ToestimateVAD scores

# theyadopt

# thesamelexicon

# based approach implemented by SentiStrength, using aVAD lexicon

# of over

# 13K

# Englis

# h words developed

# psychology research

# However,

# notableto provideany evaluation oftheirapproach to emotion mining.

# Ortuetal.

# (2015)

# presented an empiricalstudy on theco

# rrelationof emotions

# rackingsystem.

# TheymeasuretheemotionpolarityinissuecommentsusingSentiStrength. Asfor

# developed theirown classifierfordetecting thepresenceoffour

# basicemotions

# anger, joy, sadness, andlove. TheirapproachexploitsSVM usinga suite

# politeness

# Danescu

# Niculescu

# Mizil

# et

# and

# (StrapparavaandValitutti2004)

# Theclassifierisevaluatedon

# gold standard of4

# rangingfrom.

# for anger to.

# for sadness

# . At the time of writing, the classifier

# BlazandBecker

# (2016)

# developed apolarity classifierforIT tickets.

# using

# semiautomatic

# boots

# rapping

# approachto

# expand

# ing

# aninitialsetof

# exploitfeature

# base

# d on thedocumentstructure, i.e.

# by distinguishing between thepolarity oftheopening section fromthe

# polarity oftheactualproblemreportsection in theticket. They

# compare differentapproaches

# Thedistributionofthegold

# standardbuilt

# dataset

# , i.e.

# the

# 38%

# neutral

# posts.

# Another

#

# f

# contain

# emotionwords

# included

# theSentiStrength

# TABLE

# , makingSentiStre

# ngth

# whichrepresent

# dataduring thesupervised

# ver,

# work,

# we

# will

# fine

# tune

# sentimenttobeabletorecognizealsomixedse

# ntiment

# softwareengineering

# researchers

# trained

# anda bag

# wordapproach

# . However, theydo

# method

# Forthesakeof

# butwe

# foundthatitisoutperformedbySVM

# emotionsin

# issue

# trackingsystemstoprevent lossof

# VAD metrics, thatis

# scores fortheV

# alence

# being in

# controlofa situation)

# iventhelackofagoldstandardforVAD, they

# were

# andissue

# fixingtimein

# theApache

# ssue

# discrete

# emotionlabels, they

# framew

# ork by

# theShaveret al.

# (1987)

# , namely

# of

# featuresbasedontheSentiS

# rengthoutput, the

# affective

# words

# derived

# 000 sentences, obtaining a

# measure

# score

# is not

# yet

# available forresearchpurposes

# Theirapproachisbasedonadomaindictionary

# created

# affectively

# loadedw

# ordsused asseeds.

# They

# also

# with

# differentfeaturesettings.

# In


---

<!-- Página 20 -->

# (F

# thebest setting, theyobtainanoverall performanceofF = .85, that iscomparabletotheoneachievedby

# Senti4SD

# =.86

# However,

# their report

# negative

# bias

# the

# misclassification

# neutral

# document

# as

# performanceon thenegative

# class

# (F =

# .70

# , R =

# , P =

# reflects

# such

# bias.

# Senti4SD

# successfullyaddresses this

# problem

# by obtaining amorebalanced performanceforboth th

# e negative

# (F =

# .84

# , R =

# .87

# , P =

# .80

# andneut

# ral

# .83

# .80

# , P =

# .85

# classes.

# Furthermore,

# Senti4SD

# hasbeen trained and evaluated on a

# balanced

# and

# larger

# dataset

# IslamandZibran(2017) developed

# SentiStrength

# SE,

# a customizedversionofSentiStrengthforsoftware engineering.

# The

# tool

# upon API

# and

# ad

# heuristics

# to

# solve of

# SentiStrengthobservedonasubsetof

# about400 commentsfrom

# theOrtudataset (Ortuet al. 2016).

# hesentimentscoresofthe

# lexic

# on havebeen manually adjusted

# toreflect thesemanticsandneutral polarityofdomainwords

# suchas

# support

# ’, ‘

# error

# ’, or

# default

# ’.

# Theauthorsperformed

# anevaluationofthe toolonthe remaining5,600

# commentsfromthe Ortudataset, showingthat

# Senti

# Strength

# SE

# F =

# .78

# , R =

# .85

# , P =

# .74

# outperformsSentiStrength

# (F =

# .62

# .79

# .62

# on technicaltexts.

# However,

# SentiStrength

# SE producesalowerperformance

# (F =

# , R = .7

# , P = .7

# than

# both

# .82

# , R =

# .82

# , P =

# .82

# and

# Senti4SD

# (F =

# .87

# , R = .87, P =

# .87

# whenusedtoclassifypolarityofposts

# from

# ourStack Overflowgold standard

# (see

# Section

# 9.2.

# DistributionalS

# emantics

# in

# oftware

# ngineering

# Tothebestofourknowledge, wordembeddingtechniqueshavenotbeenappliedbeforetosentimentanalysistasksinthe

# softwaredevelopmentdomain.

# Inparticular, we

# exploit

# theideaof

# using featuresbased on

# the

# documentsimilarity w

# ithrespect

# toprototypevectors

# modeling

# thelexical profileofthe

# polarity classes

# heuseofprototypevectors

# intext classifications

# was

# successfullyexploited

# indifferent domains, e.

# for

# unsupervised speech

# actrecognition

# intelephone

# conversations

# (Novielli

# andStrapparava 2013)

# and

# for

# sent

# iment analysis

# micro

# blogging

# (BasileandNovielli2015)

# However,

# distributional

#

# entirely

# new

# software

# research.

# Traditional,

# context

# countingapproac

# hesto distributionalsemanticshave

# already

# been used

# , including

# LatentDirichletAllocationfortopic

# modeling

# inStackOverflow

# Barua

# etal. 2014)

# andLatentSemantic Analysisforrecoveringtraceabil

# itylinksinsoftwareartifact

# (De

# Luciaetal. 2007

# . Tianet al.

# (2014)

# recentlyproposedtheuseof pointwisemutualinformationtorepresentswordsimilarityin

# a high

# dimensionalspace. They

# built

# SEWord

# Sim, awordsimilaritydatabase

# trainedonStackOverflowquestionsandanswers.

# However, asalreadydiscussedinSection

# count

# based approachessuffer

# from

# themaindrawback

# ofpoorscalability. In the

# specific the

# dimensional

# whose

# elements

#

# pointwisemutualinformation between thewords

# and

# , thusdescribingtheirsemanticassociation. Thef

# actthatvectorspace

# dimensionsequalthevocabulary sizesignificantly limitsthescalability ofapproachesbased on such word models.

# Instead, w

# ord

# embedding

# overcome

# thelimitations

# ofcontext

# countingapproaches

# dueto theirpoorscalability to lar

# gedocumentcollecti

# Mikolov

# etal. 2013a)

# andprovide

# moreeffective

# vector

# representation

# ofwords

# Baroni

# etal. 2014,

# etal. 2013b)

# Thus, inour

# study

# weadoptwordembeddingforbuildingourdistributionalsemanticmodel.

# Yeetal.

# (2016)

# alreadyexploited

# wordembeddingforenhancinginformationretrievalinsoftwareengineering.

# hey run

# word2vec

# a collectionofover12K Java SE 7 documentstorepresentbothnaturallanguage wordsandsource code tokensin

# distributional

# ntic

# heir bridge

# gap

# description thatcan befound in tutorials, API documentations, and bug reports. They empirically demonstratehowexploiting


---

<!-- Página 21 -->

#

# wordembedding

# improvesover

# state

# the

# artapproachestobuglocalization. Furthermore, theydemonstrate the benefitof

# exploitingwordembeddingforlinkingAPI documentstoJava que

# stions postedinStackOverflow.

# Conclusions

# We

# present

# Senti4SD

# , asentiment polarity

# classifierfor

# softwaredevelopers

# art

# facts.

# Theclassifier

# istrainedandtested

# a

# over

# posts

# mined

# and

# manually

#

# The

# gold

# standard

# publicly availablefor

# further studiesone

# motionawarenessinsoftwareengineering.

# also

# releasetheguidelines

# for

# annotation

# toencouragethecommunitytoextendandfurthervalidateour

# dataset

# by replicating theannotation experiment.

# ThesemanticfeaturesofSenti4SD arecomputed

# based on adistributionalsemanticmodelbuiltexploiting word embedding.

# WebuilttheDSM byrunningword2veconacollectionofover20 milliondocumentsfromStackOverflow, thusobtainingword

# vectorsthatare

# representativeof developers’ communicatio

# n style. TheDSM

# released, withthereplicationkit,

# for future

# researchonwordembeddingfor textcategorizationandinformationretrievalinsoftwareengineering.

# Bycombining

# lexicon

# based,

# keyword

# based

# andsemantic

# features,

# Senti4SD

# successfully

# addressesthe problemof

# the

# negativebias

# in

# off

# the

# shelf

# sentimentanalysis tool

# n particular, weobservea

# % improvement

# precision forthenegative

# classanda 2

# % improvementin

# recallfor theneutralclasswithrespecttothebaselinerepres

# entedbySentiStrength.

# Asfuturework,

# weintend

# explore the contributionof

# additionalfeaturestocapture

# further

# meaningfulaspect

# of

# language

# use

# , such

# aspart

# speechandtherhetoricalstructureofsentences.

# We also intend to fine

# tuneSenti4SD torecognizecontent

# withmixedsentiment.

# Asa

# further assess

# mentof

# pproach

# intend

# to

# evaluate

# Senti4SD performanceo

# further

# crowd

# generated content

# from

# othersocialsoftwareengineering

# toolsandreposit

# ories

# (e.g.,

# GitHub

# issuetrackingsystems).

# Besides

# plan to providefurther

# benchmarking

# withothersentimentanalysistool

# and

# lexicons

# Finally

# e are

# also

# working

# an

# extendedversionofourgoldstandard

# that

# willinclude

# emotionlabels

# (e.g., love, anger, sadness, joy)

# asa firststepto

# wards

# building

# classifier

# to detect

# specific

# emotion

# Acknowledgment

# Thisworkispartiallysupportedbytheproject‘

# EmoQuest

# InvestigatingtheRoleof EmotionsinOnlineQuestion&

# Answer

# Sites’,

# Education,

# under

# Independenceof

# Researchers” (SIR). ThecomputationalworkhasbeenexecutedontheIT resourcesmadeavailableby

# twoprojects,

# ReCaS andPRISMA, fundedbyMIUR undertheprogram“PON R&C 2007

# 2013”.

# Wethank

# PierpaoloBasile

# for insightfuldiscussionsandhelpfulcom

# mentsandthe

# annotators

# involved in the gold standard

# building

# References

# AndersonA, Hut

# tenlocherD, Kleinberg

# J, LeskovecJ (2012) Discoveringva

# luefromcommunityac

# tivityonfocusedquestion

# answeringsites: A case st

# udy ofstack overflow. In: Pro

# ceedingsofthe 18thACM SIGKDD International

# Conferenceon

# Knowledge

# ery

# ng, NY,

# SA,

# ’12,

# 858,

# 10.1145/2339530.2339665

# AsaduzzamanM, MashiyatAS, RoyCK, SchneiderKA (2013) Answeringquestionsaboutunansweredquestionsofstack

# overflow. In: Proceedingsofthe10th Working Conferenceon Mining SoftwareRepositories, I

# EEE Press, Piscataway, NJ,

# USA, MSR ’13, pp97

# Baroni

# Kruszewski

# Don’t a

# counting

# predicting semanticvectors. In: Proceedingsofthe52nd AnnualMeeting oftheAssociati

# on forComputationalLinguistics

# (Volume1: LongPapers), Associationfor ComputationalLinguistics, Baltimore, Maryland, pp238


---

<!-- Página 22 -->

#

# BaruaA, ThomasSW, HassanAE (2014) Whataredeveloperstalkingabout? ananalysisoftopicsandtrendsin

# flow. Empirical

# Softw

# Engg19(3):619

# DOI 10.1007/s10664

# BasileP, NovielliN (2015)

# Uniba

# :

# features. In: Proceedingsof the9thInternationalWorksho

# BengioY, DucharmeR, Vin

# centP, JanvinC (2003) A neuralprobabilistic language model. J MachLearnRes3:1137

# Blaz

# CCA,

# Becker

# (2016)

# Sentiment

# analysis

# tickets

# on Mining SoftwareReposito

# ries, ACM, NewYork, NY, USA, MSR ’16, pp235

# alefatoF, Lanubile F, MarasciuloMC, NovielliN (2015) Miningsuccessfulansw

# the12thWorkingConferenceonMiningSoftwareRepositories, IEEE Press, Piscataway, NJ, USA, MSR ’15, pp430

# Carofiglio

# de

# Rosis

# F, Cognitive

# Springer

# London, London, pp23

# CohenJ (1968) Weightedkappa: Nominalscaleagreementprovisionforscaleddisagreementorpartialcredit. Psychological

# Bulletin

# Collo

# bertR, Weston J (2008) A unified architecturefornaturallanguageprocessing: Deep neuralnetworkswith multitask

# learning. In: Proceedingsofthe25thInternational ConferenceonMachineLearning, ACM, NewYork, NY, USA, ICML

# ’08, pp160

# 167, DOI 10.114

# 5/1390156.1390177

# Danescu

# Niculescu

# Mizil

# C, SudhofM, JurafskyD, LeskovecJ, PottsC (2013) A computationalapproachtopolitenesswith

# applicationtosocialfactors. In: ACL (1),

# TheAssociationforComputerLinguistics, pp250

# EkmanP (1999) Hand

# book ofCognition and Emotion. John Wiley & SonsLtd

# DeLuciaA, FasanoF, OlivetoR, TortoraG (2007) Recovering

# using information retrievalmethods. ACM TransSoftwEng Methodol16(4), DOI 10.1

# Denning

# . Moods.

# (2012) Commun.

# ACM, 55(12):33

# FanRE, ChangKW, HsiehCJ, WangXR, LinCJ (2008) Liblinear: A libraryforlargelinearclassification. J MachLearnRes

# 9:1871

# 1874, URL

# http://dl.acm.org/citation.cfm?id=1390681.1

# Ford

# D and

# Parnin

# C (2015)

# Exploringcausesoffrustrationforsoftwaredevelopers. InC

# Gachechiladze

#

# development.

# Ideas

# Results

# NIER Piscataway,

# 11

# NIER.2017.18

# GraziotinD,

# Fagerholm

# , Wang

# Abrahamsson

# P (2017

# BadforSoftwareProduct

# ToappearasaposterpaperintheProceedingsofthe39thInternationalConferenceon

# Engineering(ICSE '17).

# GuzmanE, BrueggeB (2013) Towardsemotionalawarenessinsoftwaredevelopmentteams. In: Proceedingsofthe

# JointMeetingonFoun

# dationsofSoftwareEngineering, ACM, NewYork, NY, USA, ESEC/FSE 2013, pp 671

# 10.1145/2491411.2494578

# GuzmanE, Az

# carD, LiY (2014) Sen

# timent analysisofcommit commentsin

# the11thWorkingConfer

# ence onMiningSoftware Repositories, ACM, NewYork, NY, USA, MSR 2014, pp352

# DOI 10.1145/2597073.2

# Guzman

#

# Seyff

# N

# ) What

# International

#

# ngineering

# EngineeringConference(RE),

# pp. 96

# 105,

# doi: 10.1109/RE.2016.67

# Garcia

# , Learningf

# romImbalancedData. IEEE TransasctiononKnowledgeandDataEngineering

# (2009). doi:10.1109/TKDE.2008.239.

# Helleputte T (2015) LiblineaR: Linear Predictive Models Based on the LIBLINEAR C/C++ Library. R package version 1.94

# HogenboomA, FrasincarF, deJongF, KaymakU (2015) Usingrhetoricalstructurein

# 58(7):69

# 77, DOI 10.1145/2699418

# Islam

# MDR

# andZibran

# MF (

# Leveragingautomatedsentimentanalysisinsoftwareengineering. InProceedingsofthe

# 14th InternationalConferenceon Mining SoftwareRepositories(MSR '17). I

# DOI: https://doi.org/10.1109/MSR.2017.9

# Joachims T (1998) Textcategorizationwith

# suport

# vectormachines: Learning with many relevantfeatures. In: Proceedingsof

# the 10th European Conference on Machine Learning,

# Joachims T (2006) Traininglinear

# SVM

# s inlineartime. In: Proceed

# on

# ery ACM,

# NY, ’06,

# 10.1145/1150402.1150429

# Jongeling

# Choosing

# On tools

# research. In: SoftwareMaintenanceandEvolution(ICSME), 2015 IEEE InternationalConferenceon, pp531

# English

# tweets

# blogging,

# semantic

# p on SemanticEvaluation (SemEval2015), ACL, pp 595

# for

# IT

# support. In: Proc

# eedingsofthe 13thInternationalConferen

# 246, DOI 10.1145/2901739.2901781

# ersin

# stack

# overflow. In

# traceability

# linksinsoftwareartifact management sys

# 145/1276933.1276934

# HASE, pages115

# .

# 14.

# https://doi.org

# UnhappyDevelopers: BadforThemselves, BadforProcess, and

# ithub:

# Anempiricalstudy. In: Proceed

# twitter

# users In:

# In: the

# sentimentanalysis. CommunACM

# EEE Press, Piscataway, NJ, USA, 203

# Springer

# Verlag, London, UK, UK, ECML ’98, pp137

# ingsofthe12thACM SIGKDD International

# stack

# over

# : Pro

# ceedingsof

# tems

# 116. IEEE Press.

# /10.1109/ICSE

# Software

# 2013 9th

# 674, DOI

# ingsof

# 355,

# 21(9), 1263

# 214.

# Conference

# 26,

# 35, DOI


---

<!-- Página 23 -->

#

# 10.1109/ICSM.2015.7332508

# KucuktuncO, CambazogluBB, WeberI, FerhatosmanogluH (2012) A large

# scalesentimentanalysis forY

# ahoo! answers. In:

# ProceedingsoftheFifthACM InternationalConferenceonWebSearchandDataMining, ACM, NewYork, N

# WSDM ’12, pp633

# 2, DOI 10.1145/2124295.2124371

# KuhnM (2016)  ContributionsfromJedWing, S. Weston, A. Williams, C. Keefer, A. Engelhardt, T. Cooper, Z. Mayer, B.

# Kenkel, theR CoreTeam, M. Benesty, R. Lescarbeau, A.

# Ziem

# , L. Scrucca

# , Y. Tang, andC. Candan., caret: Classification

# andRegressionTraining, 2016, rpackage version6.0

# 70. Available: https://CRAN.R

# project.org/package=caret

# LandauerTK, D

# utnaisST (1997) A solution to Platosprob

# lem: Thelatent semanticanalysistheo

# ryof acquisition, induction,

# andrepresentationofknowledge. PSYCHOLOGICAL REVIEW 104(2):211

# LazarusR (1991) Emotionandadaptation. NewYork: OxfordUniversityPress.

# LevyO, GoldbergY (2014) Neuralwordembeddingasimplicitmatrixfactorizatio

# n. In: GhahramaniZ, Welling M, Cortes

# LawrenceND, WeinbergerKQ (E

# ds) Advancesin NeuralInformation Processing Systems27, Curran Associates, Inc., pp

# 2185, URL http://papers.nips.cc/paper/5477

# neural

# word

# embedding

# implicit

# matrix

# factoriza

# tion.pdf

# MaalejW, KurtanovicZ, NabilH, StanikC (2016) Ontheautomaticclassificationof

# appreviews. RequirementsEngi

# 21(3):311

# 331, DOI 10.1007/s00766

# Manning

#

# tanford language

# processing

# Proceedings

# Annual

# System

# Demonstrations, pp55

# ntyl

# M, AdamsB, DestefanisG, GraziotinD,

# Ortu

# M (2016) Miningvalence, arou

# sal, anddominance: Possibilities for

# detecting burnoutand productivity? In: Proceedingsofthe13th InternationalConferenceon Mining SoftwareRepositories,

# ACM, New York, NY, USA, MSR ’16, pp247

# 258, DOI 10.1145/2901739.2901752

# Mäntylä

# , Novielli

# , Lanubile

# , Claes

# , andKuutila

# M (2017)

# Bootstrappingalexiconforemotionalarousalinsoftware

# engineering. InProceedingsofthe 14thInternationalConference onMiningSoftware Repositories(MSR '17). IEEE Press,

# Piscataway, NJ, USA, 198

# 202. DOI:

# https://doi.org/10.1109/MSR.2017.47

# Meta

# (2017)

# .  new

# exchange

# too

# harsh

# new

# users

# please

# help

# them

# improve

# low

# quality

# po, Lastaccessed:

# February201

# Mikolov

# Corrado

# J

# abs/1301.3781

# MikolovT, SutskeverI, ChenK, CorradoGS, DeanJ (2013b) Distributedrepresentationsofwordsandphrasesandtheir

# composit

# ionality.

#

# ,

# ds)

# InformationProcessingSystems26, Cur

# ran

# Associates, Inc., pp3111

# MillerGA, CharlesWG (1991) ContextualCorrelatesofSemanticSimilarity. Langua

# geand CognitiveProcesses6(1):1

# DOI 10.1080/01690969108406936

# Mitchell

# TM (

# MachineLearning(1 ed.). McGraw

# Hill, Inc., New York, NY, USA.

# MohammadSM (2016) Sentimentan

# alysis: Detectingvalence, emo

# tions, andother

# affectual

# stat

# esfromtext. In: Meiselman

# H (E

# d) Emotion Measurement, Elsevier

# Mohammad

#

# NRC

# anada:

# state

# the

# art

# CoRR abs/1308.6242, URL http://arxiv.org/abs/1308.6242

# ller

# Fritz

# T

# Stuck sensing

# emotions

# In

# Proceedings

#

# Volume

# Vol.

# Piscataway, NJ, USA, 688

# Murg

# iaA, Tourani P, AdamsB, OrtuM (2014

# ) Dodevelopersfeelemotions? A

# n exploratory analysisofemotionsin software

# artifacts. In: Proceedings of the 11th Working Conference on Mining Software Repositories, ACM, New York, NY, USA,

# MSR 2014, pp262

# 271, DO

# I 10.1145/2597073.2597086

# NovielliN, StrapparavaC (

# 2013) Theroleofaffectanaly

# sis indialogueactidentification. IEEE Transactions onAffective

# Computing4(4):439

# 451, DOI 10.1109/T

# AFFC.2013.20

# Novielli

# N, CalefatoF, LanubileF (2014

# TowardsdiscoveringtheroleofemotionsinStackOverflow.

# InProceedingsof the

# 6th on  2014).

# 33

# DOI=http://dx.doi.org/10.1145/2661685.2661689

# Novielli

#

# ubile   In:

# Proceedingsofthe7thInternationalWorkshoponSocialSoftwareEngineering, ACM, NewYork, NY, USA, SSE 2015,

# pp 33

# 40, DOI 10.1145/2804381.2804387

# Ortu

# M, Adam

# s B, Destefanis G, TouraniP, MarchesiM, TonelliR (2015) Arebullies moreproductive?: Empiricalstudyof

# affectivenessvs. issue fixingtime. In: Proceedingsofthe 12thWorkingConference onMiningSoftware Repositories, IEEE

# Press, Piscataway, NJ, USA

# , MSR ’15, pp 303

# Ortu Destefanis

# The

# side

# developers

# ira.  Conference

# ACM,

# Y, USA,

# C,

# neering

# 28,

# 36.


---

<!-- Página 24 -->

# –

# York,

# NY, USA, MSR ’16, pp480

# 483, DOI 10.1145/2901739.2903505

# PangB, LeeL (2008) Opinionminingandsentimentanal

# ysis

# . FoundTrendsInfRetr2(1

# Panichella

#

# reviews

# 31st

# Evolution

# Pennebaker

# J and

# Francis

# , Linguistic Inquiry and Word Count: LIWC. Erlbaum Publishers, 2001.

# Pletea

# , Vasilescu

# , andSerebrenik

# A (

# Securityandemotion: sentimentanalysisofsecuritydiscussionsonGitHub.

# InProceedingsof the11thWorkingConferenceonMiningSoftwareRepositories(MSR 2014). ACM, NewYork, NY,

# USA, 348

# 351. DOI: http:

# //dx.doi.org/10.1145/2597073.2597117

# R DevelopmentCoreTeam(2008) R: A LanguageandEnvironmentforStatisticalComputing. R Foundation

# Computing, Vi

# enna, Austria, URL http://www.R

# project.org, ISBN 3

# Rahman

#

# nloo insightful

#

# knowl

# edge. In: 15thIEEE InternationalWorkingConference onSource Code AnalysisandManipulation, SCAM 2015,

# Bremen, Germany, September27

# 28, 2015, pp 81

# 90, DOI 10.1109/S

# CAM.2015.7335404

# RussellJ (1980) A circumplexmodelofaffect. Journalofpersonalityandsocialpsychology39(6):1161

# SaifH, FernandezM, HeY, AlaniH (2014) Onstopwords, filteringanddatasparsityforsentimentanalysisof

# Chair)

# NCC, ChoukriK, DeclerckT, LoftssonH, MaegaardB, MarianiJ, MorenoA, OdijkJ, PiperidisS (eds) Proceedings

# oftheNinth InternationalConferenceon LanguageRe

# sources andEvaluation(LREC’14), EuropeanLanguageResources

# Association(ELRA), Reykjav

# ik, Iceland

# SchererK, WranikT, SangsueJ, TranV, SchererU (2004) Emotionsineverydaylife: Probabilityofoc

# appraisalandreactionpatterns. SocialScience Information43(4):499

# Sebastiani

# Machine

# g

# utomated

# gorization.

#

# 10.1145/505282.505283

# SEmotion

# (2016)

# Proceedingsofthe1stInternationalWorkshoponEmotionAwarenessinSoftwareEngineering, ACM, New

# York, NY, USA

# ShaverP, SchwartzJ, Kirson

# D, O’ConnorC (1987) Emotionknowledge: Furtherexplorationofaprototypeapproach. Journal

# of Social 52(6):1061

# 1086,

# http://dx.doi.org/10.1037//0022

# 3514.52.6.1061

# inhaV, LazarA, Sha

# rif B (2016) Analyzingdeveloper sentimentincommitlogs. In: Proceedingsof the13thInternational

# Conference

# ACM,

# NY, ’16,

# 10.1145/2901739.2903501

# Smolensky

# (1990)

# Tensor

# product

# var

# iable

# binding

# and

# the

# representationof symbolicstructuresinconnectionistsystems.

# Artif

# icial Intelligence

# 46(1

# 2):159

# 216, DOI 10.1016/0004

# 3702(90)90007

# Socher

# Recursive

# compositionality

# In: the on

# LanguageProcessing, AssociationforComputationalLinguistics, Stroudsburg, PA, pp1631

# StrapparavaC, ValituttiA (2004) WordNet

# Affect: an

# affective

# extensionofWordNet. In: ProceedingsofLREC, vol4, pp

# StonePJ, DunphyDC

# , Sm

# ithMS, andOgilvieDM

# (1966). Thegeneralinquirer: A computer approachtocontentanalysis.

# Cambridg

# e, MA: The MIT Press.

# Thelwall

# Sentiment

# social Soc

# 63(1):163

# 173, DOI 10.1002/asi.21662

# TianY, LoD, LawallJ (2014) Sewordsim

# : Software

# specificwordsimilaritydatabase. In: CompanionProceedings ofthe36th

# InternationalConferenceonSoftwareEngineering, ACM, NewYork, NY, USA, ICSE Companion2014, pp568

# 10.1145/2591062.2591071

# Tromp

# E

# Pechenizkiy

# M

# Pat

# tern

# based on M.

# Wiratunga, andA. Goker, editors,

# AdvancesinSocialMediaAnalysis

# , pages 1

# WittgensteinL (1965) PhilosophicalInvestigations. TheMacmillanCompany, NewYork,

# YeX, ShenH, MaX, BunescuRC, LiuC (2016) Fromwordembeddingstodocumentsimilaritiesforimprovedinformation

# retrieval

#

# 2016, Austin

# , TX, USA, May 14

# 22, 2016, pp 404

# 415, DOI 10.1145/2884781.2884862

# 2):1

# 135, DOI 10.1561/1500000011

# can

# improve

# code

# currence, riskfactors,

# 3514.52.6.1061,

# 20.

# Springer

# NY, USA

# for Statistical

# twitter

# 47,

# 523,

# for

# 571, DOI

# Cocea

# . In:

# ,


---

<!-- Página 25 -->

# A:

# Appendix

# CodingGuidelines

# In

# the

# we

# task

# annotationstudy

# TaskD

# escription

# and Annotation Guidelines

# Youareinvitedtotakepartinthe

# inStackO

# verflow.  Weareinterested in

# annotatingthe

# presenceof

# during the

# ir online interactions.

# The Overflow

# ump Exchange

# You to

# annotate r

# andomlyselected

# posts, including questions,

# answers

# Youwilluse

# the

# coding

# schem

# reportedin

# TABLE A.

# Foreachpost,

# the

# basic

# emotion

# s (firstcolumninthetable)

# that

# are

# love, joy, surprise, anger, sadness,

# allowed

# butyou should try to avoid ifpossible.

# Youcanusethe

# the primary emotion, as

# shown

# in TABLE B

# Once

# ,

# ify

# neutral

# and

# mixed

# If thepostdoesnotcontain

# anyemotion, itshouldbe annotatedasneutral. The surprise isthe onlyemotion

# that  please,

# negative, or

# neutral

# polarity.

# If multipleemotionlabelsareindicated

# A text

# annotate

# with

# oneormore

# positiveemotion

# only hasapositivepolarity. Conversely, apostannotated with

# negativeemotions

# holdsanegativepolarity. Ifboth positiveand negativeemotions

# ishtoindicateapolaritylabel

# you arerequired

# tospecifythecorrespondingemotion.

# exclusivelyasneutral.

# Thelistofallpossiblecombinationallowed

# used  the

# emotions

# andc

# omments.

# pleaseindicatewhat

# secondandthirdlevel

# a giventext, youshoulddefine the polarityaccordingly.

# andnotallowed

# annotation

# study

# ofdeveloperscontributed texts

# intechnical documentsauthoredbydevelopers

# Theunitofannotationistheentirep

# ost.

# emotionitconveys

# (if any)

# among

# and

# fear

# MultipleEmotion

# labelsare

# intheschema

# asa reference forchoosing

# ccordingly

# ,

# positive,

# t

# are

# found, youshouldindicatebot

# If you

# Thea

# bsence

# ofemotion can beannotated

# by ou

# coding

# schema

# isreportedinTABLE


---

<!-- Página 26 -->

# T

# Emotion

# Polarity

# Positive

# Negative

# EitherPositive

# orNegative

# Basic

# Emotions

# Love

# Joy

# Anger

# Sadness

# Fear

# Surprise

# ABLE

# Secondlevel

# Affection

# Lust

# Longing

# Cheerfulness

# Zest

# Contentment

# Optimism

# Pride

# Enthrallment

# Irritation

# Exasperation

# Rage

# Disgust

# Envy

# Torment

# Suffering

# Sadness

# Disappointment

# Shame

# Neglect

# Sympathy

# Horror

# Nervousness

# APPING

# THE

# HAVER ET AL

# EMOTION

# Liking, Caring, Compassion, Fondness, Affection, Love, Attraction, Tenderness,

# Sentimentality

# Desire, Passion, Infatuation,

# Happiness, Amusement, Satisfaction, Bliss, Gaiety, Glee, Jolliness, Joviality, Joy,

# Delight, Enjoyment, Gladness, Jubilation, Elation, Ecstasy, Euphoria

# Enthusiasm,

# Excitement, Thrill, Zeal, Exhilaration

# Pleasure

# Hope, Eagerness

# Triumph

# Rapture

# Annoyance, Agitation, Grumpiness, Aggravation, Grouchiness

# Frustration

# Anger, Fury, Hate, Dislike, Resentment, Outrage, Wrath, Hostility, Bitterness, Ferocity,

# Loathing, Scorn, Spite, Vengefulness

# Revulsion

# , Contempt

# Jealousy

# Hurt, Anguish, Agony

# Depression,

# Sorrow, Despair, Gloom, Hopelessness, Glumness, Unhappiness, Grief,

# Woe, Misery, Melancholy

# Displeasure, Dismay

# Guilt, Regret, Remorse

# Emb

# arrassment, Insecurity, Insult, Rejection, Alienation, Isolation, Loneliness,

# Homesickness, Defeat, Dejection, Humiliation

# Pity

# Alarm, Fright, Panic, Terror, Fear, Hysteria, Shock, Mortification

# Anxiety, Distress,

# Worry, Uneasiness, Tenseness, Apprehension, Dread

# Amazement, Astonishment

# AMEWORK TO SENTIMENT

# ThirdlevelEmotions

# Arousal

# POLARITY


---

<!-- Página 27 -->

# T

# Thanksforyourinput! You're, like, awesome

# I'mhappywiththeapproachandthecodelooks

# I stillquestionthedefault, whichcanlead

# surprisingly huge memory use

# I willcomeovertoyourworkandslapyou

# SorryforthedelayStephen

# I'mworriedaboutsomesubtlediffere

# between charand Character”

# Love

# Surprise

# InputText

# ABLE

# Anger

# ABLE

# XAMPLES OF

# NNOTATED

# OSTS

# Annotation

# Rationaleforannotation

# Basic

# (secondandthirdlevelemotionfound)

# Emotion(s)

# Polarity

# found

# Liking(thirdlevel), Affection(second

# Love

# Pos

# tive

# level)

# indicating gratitude.

# Happiness, Satisfaction(third),

# Joy

# Positive

# Cheerfulness(second)

# to

# Surprise(s

# econd) due to

# Surprise

# Negative

# undesirablebehaviorof

# Hostility(third), Rage(second)

# Anger

# Negative

# Guilt(third), Shame(second)

# Sadness

# Negative

# nces

# Worry(third)

# Fear

# Negative

# OMBINATIONS OF

# ALUES

# LLOWED

# OT

# ALLOWED

# NNOTATION

# Sadness

# Fear

# Polarity

# Explanation

# Annotationallowedbyourschema

# Negative

# Negativeemotionandnegativepolarity

# Positive

# Positiveemotionandpositivepolarity

# Negative

# Positive

# Surpriseis

# intrinsically

# ambiguous,

# allpolarityvaluesareallowed

# Neutral

# Positive

# Multipleemotionlab

# els

# , positive polarity

# Negative

# Multipleemotionlabels

# , negative polarity

# Mixed

# Multiple

# emotion

# labels

# , mixed polarity

# Neutral

# Absenceofemotion

# AnnotationNOT allowedbyourschema

# Negative

# No

# emotion

# and negative

# polarity

# Positive

# Noemotionandpositivepolarity

# Mixed

# Noemotionandmixedpolarity

# Neutral

# Emotionlabeldifferentfrom

# surprise andneutralpolarity

# Neutral

# the

# unexpected

# the

# code


---

