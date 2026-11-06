## 3.1 Preliminaries

We begin with a known subroutine on output-sensitive computation of sumsets. This subproblem was first solved by Cole and Hariharan \[CH02\] with randomization, which was later derandomized/improved in a series of subsequent papers \[CL15, BFN21, BFN22, JX24\]:

**Lemma 3.1.** _Given two sets A and B of integers in_ \[_t_\]_, we can compute the sunset A+B in_ \(\widetilde{O}(|A+B|)\) _deterministic time._

Output-sensitive computation of clipped sumsets is more expensive. Bringmann and Nakos \[BN20\] described a simple approach yielding the following (using the subroutine in Lemma 3.1):

**Lemma 3.2.** _Given two sets A and B of integers in_ \[_t_\]_, we can compute the clipped sunset_ \(C=(A+B)\cap[t]\) _in_ \(\widetilde{O}(\sqrt{|A||B||C|})\le\widetilde{O}((|A|+|C|)\sqrt{|B|})\) _deterministic time._

The next lemma below, observed by Bringmann, Fischer, and Nakos \[BFN25, Lemma 3.1\] (but stated in a different form), derandomizes the small _k_ case using Bringmann’s color-coding approach \[Bri17\]. For completeness, we include a quick proof sketch:

**Lemma 3.3.** _Given a set X of n integers in_ \[_t_\]_, a set A of integers in_ \[_t_\]_, and a number k, we can compute a set_ \(\mathrm{OUT}\) _such that_ \((A+\Sigma_{\le k}(X))\cap[t]\subseteq\mathrm{OUT}\subseteq(A+\Sigma(X))\cap[t]\)_, in_ \(\widetilde{O}(k^{O(1)}|(A+\Sigma(X))\cap[t]|\sqrt{n})\) _deterministic time._

_Afterwards, for any given_ \(y\in\mathrm{OUT}\)_, we can report one number_ \(a\in A\) _and one subset_ \(S\subseteq X\) _with_ \(a+\sigma(S)=y\)_, in_ \(\widetilde{O}(|S|)\) _time._

_Proof._ There exists a family H of _O(k_<sup>_O_(1)</sup>log_n_) "perfect" hash functions from _X_ to {1_,...,k_<sup>2</sup>} satisfying the following property: for every subset \(S\subseteq X\) with \(|S|\le k\), there exists \(h\in\mathcal{H}\) such that \(\{h(x):x\in S\}\) are all distinct. The family can be constructed in _O(k_<sup>_O_(1)</sup>log<sup>_O_(1)</sup>_n_) time. E.g., see \[AYZ95, Section 4\].

Fix \(h\in\mathcal{H}\). For each \(j\in\{1,\dots,k^2\}\), let \(X_{h,j}=\{x\in X:h(x)=j\}\). Compute the clipped sumset

\(\mathrm{OUT}_h=(A+(X_{h,1}\cup\{0\})+\cdots+(X_{h,k^2}\cup\{0\}))\cap[t]\)

by applying Lemma 3.2 _O(k_<sup>2</sup>) times in \(\widetilde{O}(k^{O(1)}|(A+\Sigma(X))\cap[t]|\sqrt{n})\) time. Then \(\mathrm{OUT}=\bigcup_{h\in\mathcal{H}}\mathrm{OUT}_h\) fulfills the output requirement. For any given \(y\in\mathrm{OUT}\), we can report a corresponding number \(a\in A\) and subset \(S\subseteq X\) again using the deterministic witness-finding technique by Alon and Naor \[AN96\].

## 3.2 Halver

As before, the key idea is the construction of a halver. We now need a "weighted" variant that halves the sum of a subset rather than its cardinality:

**Definition 3.4.** _Given a set X of positive integers, and numbers t and_ \(\Delta\)_, a_ weighted \((t,\Delta)\)-halver _of X is a partition of X into two disjoint subsets_ \(X'\) _and_ \(X''\) _with the following property:_

_For every subset_ \(S\subseteq X\) _with_ \(\sigma(S)\le t\)_, there exists a subset_ \(\hat{S}\subseteq X\) _with_ \(\sigma(\hat{S})=\sigma(S)\)_, and_ \(\sigma(\hat{S}\cap X'),\sigma(\hat{S}\cap X'')\le\sigma(\hat{S})/2+\Delta\).

As before, we will generate a collection of small canonical subsets, to which we will then apply Lemma 2.3 to construct a halver. Unfortunately, Koiliaris and Xu’s algorithm is no longer applicable, since it is not output-sensitive. Instead, we will use the algorithm from Lemma 3.3 for small _k_ for this purpose.<tbc>

