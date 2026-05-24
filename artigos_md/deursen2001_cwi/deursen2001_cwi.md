<!-- Página 1 -->

Refactoring test codeA. van Deursen, L.M.F. Moonen, A. van den Bergh, G. Kok

Software Engineering (SEN)

**SEN-R0119 July 31, 2001**

Centrum voor Wiskunde en Informatica

## REPORT

## RAPPORT


---

<!-- Página 2 -->

Report SEN-R0119ISSN 1386-369XCWIP.O. Box 940791090 GB AmsterdamThe Netherlands

CWI is the National Research Institute for Mathematicsand Computer Science. CWI is part of the StichtingMathematisch Centrum (SMC), the Dutch foundationfor promotion of mathematics and computer scienceand their applications.SMC is sponsored by the Netherlands Organization forScientific Research (NWO). CWI is a member ofERCIM, the European Research Consortium forInformatics and Mathematics. Copyright © Stichting Mathematisch CentrumP.O. Box 94079, 1090 GB Amsterdam (NL)Kruislaan 413, 1098 SJ Amsterdam (NL)Telephone +31 20 592 9333Telefax +31 20 592 4199


---

<!-- Página 3 -->

Note:W

Note:

Keyw

2000

trouble

refacto

(1)

refacto

that

Tw

ABSTRA

Published

ords

CM

rings.

red.

okey

CT

orkrried

W

o

e

of

re

Refacto

rojects

P

ro

Kruislaan

.O.

p

ring,

rogramming

falex,gerard

[http://www.software-improvers](http://www.software-improvers).

.

# 1.

# NTRODUCTION

# “If

#

# extreme

# (XP),

#

#

# programming

#

#

#

#

#

#

#

#

#

# automated,

#

#

#

#

#

#

#

#

#

# the

#

#

#

# The

#

#

#

#

#

#

#

#

#

#

# are

#

#

#

#

#

#

# code

#

#

#

#

#

#

#

#

#

# least,

#

#

#

#

#

#

#

# test

#

#

#

#

#

#

#

# method,

#

#

#

#

#

#

#

# Writing

#

#

# JUnit [3].

ring

x

[http://www.cwi.nl/](http://www.cwi.nl/)

Refacto

# Proceedings

#

#

#

#

#

# Processes

#

#

,

# Software

test

Soft

and

# guages

1098

Alex

f

# Domain-Specific

D.2.3,

wa

arie,leon

Arie

re

g@software-impro

Gera

Leon

ring

y

a

A

rings

ractitioners,

roaches

reunit

rovement

rd

CWI

g@cwi.nl



T

rogramming

testing

f

est

arie,leon

roving

from

ri,

Co

and

e

.

merciless

g

ring

/

rising

p

ro

refactoring.

co

Given

wow

re

a

fact

ys:


---

<!-- Página 4 -->

2

Theaour project

ESTCODESMELLS This**Smell**WhenConsequently,thatchangesresource..resourcesto**Smell**.Test(suchsituationyourselfto**Smell n**Suchrunas*Apply***Smell***.*IntoThingsSuch

1Thisoffive

1Oneofchange:ofastheTheitrangeavailable,codeWheniswhichimprovingassoThethatindicatingexplainingassumesreferName andin(#).2.


---

<!-- Página 5 -->

2.

dointerferingThe*Extract**Method*andexample,that.**Smell**WhenthereforeharderThe*Extract*smaller**Smell**Thisusingtheso**Smell***.*“Guessexplanation.Addto**Smell**Amethodsclass-to-be-tested).*Extract**(F:110)*followed*on*thatNoteagainstharderindirect**Smell**Whenneededthose*Extract*subclasstheyFearreasonspecificallyseparate**Smell***.*Itresult,howevermethodequality*.*

Test3


---

<!-- Página 6 -->

4

**Smell**.TestparticulartoTheusing Extract*.*hierarchycodeAtest:Arefactoring,anymore3.

EFACTORINGS BadproductionOneprogrammersinvaluable.We*test*ascases,Theasucceedscodeby

assert(true)isproductionWhile**Refactoring :***.*TotheThistheIfsmell.Extract*or***Refactoring :***.*Iftest(take**Refactoring :***.*AbySuchallocated,allocatingtheir**Refactoring :**Minimizethem**Refactoring :**.Assertionswhen


---

<!-- Página 7 -->

4.

Testingoccur**Refactoring :**Iffortestthe4.

ELATEDWORK FowlerbetweenbookrefactoringInsteadpreventThe

ONCLUSIONS Inproject,notteststartedweThe

We

Wetest

ForrefactoringTheotherforin

2[http://c2.com/cgi/wiki?TwoYearItch](http://c2.com/cgi/wiki?TwoYearItch) 3[http://c2.com/cgi/wiki?RefactorBrokenUnitTests](http://c2.com/cgi/wiki?RefactorBrokenUnitTests) 4[http://c2.com/cgi/wiki?RefactoringTestCode](http://c2.com/cgi/wiki?RefactoringTestCode)

Related

3Opinionscompletely,to Indirect (8)5.

4.AnpresencetestrevealproductionIn

ork

2,and

5


---

<!-- Página 8 -->

jw-1-it.html

6

1.,2. Extreme3.Java ,4.*Processes*.5. Refactoring:*.*6.,

. [http://www.javaw](http://www.javaw)orld.com/javaw

References

orld/


---

