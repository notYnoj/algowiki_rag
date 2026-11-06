By the defining properties of the sets involved (see Figure 9), we know that \(\mathrm{DInv}_\rho(A_<,B_>)=-a_<b_>\) and \(\mathrm{DInv}_\rho(A_>,B_<)=a_>b_<\), where \(a_<\doteq|A_<|\), \(a_>\doteq|A_>|\), \(b_<\doteq|B_<|\), and \(b_>\doteq|B_>|\). Thus, we can rewrite criterion (9) as:

\(\mathrm{DInv}_\rho(A_<,B_<)+\mathrm{DInv}_\rho(A_>,B_>)=a_<b_>-a_>b_<+a_<-a_>+b_>-b_<.\) (11)

A critical observation that helps us to bound the probability of (11) is that, conditioned on all four values _a_. and _b_., the right-hand side of (11) is fixed, but the left-hand side still contains a lot of randomness. In fact, under the conditioning stated, the ranking that \(\rho\) induces on \(A_<\sqcup B_<\) is still distributed uniformly at random, the same holds for the ranking that \(\rho\) induces on \(A_>\sqcup B_>\), and both distributions are independent. This means that, under the same conditioning, the left-hand side of (11) has the same distribution as the sum _X_<sub>_a<sub></sub>,b<sub></sub>_</sub>+_X_<sub>_a<sub></sub>,b<sub></sub>_</sub> of two independent random variables of the following type:

**Definition 33 (cross inversion distribution,** \(X_{\cdot,\cdot}\)**).** _For nonnegative integers a and b, X<sub>a,b</sub> denotes the random variable_ XInv(_A,B_) _that counts the number of cross inversions from A to B, where A is an array of length a, B an array of length b, and the concatenation AB is a uniformly random permutation of_ \[_a+b_\].

In Section 9 we establish the following upper bound on the probability that the number of cross inversions takes on any specific value.

**Lemma 34.** _There exists a constant C such that for all integers_ \(a,b\ge 1\) _and_ \(0\le k\le ab\),

\(\mathbb{P}[X_{a,b}=k]\le\frac{C}{\sqrt{ab(a+b)}}.\) (12)

Using Lemma 34 we can establish an upper bound of the same form as the right-hand side of (12) for the probability that (11) holds: For some constant \(C'\)

\(\mathbb{P}[X_{a_<,b_<}+X_{a_>,b_>}=a_<b_>-a_>b_<+a_<-a_>+b_>-b_<]\le\frac{C'}{\sqrt{ab(a+b)}},\) (13)

where \(a\doteq a_<+a_>\ge 1\) and \(b\doteq b_<+b_>\ge 1\). We consider several cases based on the relative sizes of _a<sub></sub>_ vs _a<sub></sub>_, and _b<sub></sub>_ vs _b<sub></sub>_.

(i) In case both \(a_<\ge\eta a\) and \(b_<\ge\eta b\), the bound (13) follows from (12) as long as \(C'\ge C/\eta^{3/2}\).<tbc>

(ii) By switching the order in (i), the same holds true in case both \(a_>\ge\eta a\) and \(b_>\ge\eta b\).<tbc>

(iii) In case \(a_>\le\eta a\) and \(b_<\le\eta b\), the left-hand side of (11) is at most \(2\eta ab\), whereas the right-hand side is at least<tbc>

<tbc>\((1-\eta)^2ab-\eta^2ab+(1-\eta)a-\eta a+(1-\eta)b-\eta b=(1-2\eta)(ab+a+b).\)<tbc>

<tbc>As long as \(2\eta\le 1-2\eta\), or equivalently, \(\eta\le 1/4\), this case cannot occur.<tbc>

(iv) By switching the roles of _A_ and _B_ in (iii), the same holds true in case \(b_>\le\eta b\) and \(a_<\le\eta a\).<tbc>

