**Definition 4.6** (Popular Sums)**.** _For two integer sets_ \(X,Y\subseteq\mathbb{Z}\)_, we define their set of s_-popular sums _as_

\(P_s(X,Y)=\{z\in X+Y:r_{X+Y}(z)\ge s\}.\)

**Observation 4.7.** \(|P_s(X,Y)|\le|X||Y|/s\).

It is easy to compute (a superset of) the set of _s_-popular sums in randomized time \(\tilde{O}(|X||Y|/s)\). The idea is to subsample \(X'\subseteq X\) with rate roughly 1_/s_; with good probability the popular sums are preserved in \(X'+Y\) . Fischer, Jin, and Xu \[53\] showed that with more effort this task can be derandomized in essentially the same running time.

**Lemma 4.8** (Approximating Popular Sums \[53, Theorem 1.9\])**.** _Given sets_ \(X,Y\subseteq[u]\) _and_ \(s\ge 1\)_, we can compute_ \(P_{2s}(X,Y)\subseteq P\subseteq P_s(X,Y)\) _in randomized time_ \(\tilde{O}(|X||Y|/s)\) _or deterministic time_ \(|X||Y|/s\cdot u^{o(1)}\).

The following lemma--the so-called "popular sum decomposition"--is the key insight behind this reduction step from \[4\]. Intuitively, it states that sets _X_<sub>1</sub>_,...,X<sub>n</sub>_ and _Y_<sub>1</sub>_,...,Y<sub>m</sub>_ can be decomposed into few structured parts that look exactly alike (up to shifts), plus some remainders \(X_1^*,\dots,X_n^*\) and \(Y_1^*,\dots,Y_n^*\). Almost all remainder pairs \(X_i^*,Y_j^*\), however, have _no_ popular sum.

**Lemma 4.9** (Popular Sum Decomposition \[4\])**.** _Let_ \(X_1,\dots,X_n,Y_1,\dots,Y_m\subseteq[u]\) _be sets of size at most d, and let_ \(p\ge 1\)_. Then there exist partitions_

\(X_i=X_i^*\sqcup\sqcup_{g=1}^{p^2}X_{i,g},\)<br>
\(Y_j=Y_j^*\sqcup\sqcup_{h=1}^{p^2}Y_{j,h}\)

_satisfying the following two properties:_

1. _There are sets S<sub>g</sub> of size_ \(|S_g|\le d\) _and shifts s<sub>i,g</sub> so that_ \(X_{i,g}\subseteq S_g+s_{i,g}\) _(for all_ \(i\in[n],g\in[p^2]\)_), and there are sets T<sub>h</sub> of size_ \(|T_h|\le d\) _and shifts t<sub>j,h</sub> so that_ \(Y_{j,h}\subseteq T_h+t_{j,h}\) _(for all_ \(j\in[m],h\in[p^2]\)_)._<tbc>

_2._ \(|\{(i,j)\in[n]\times[m]:P_{2d/p}(X_i^*,Y_j)\neq\emptyset\}|\le nm/p\)_, and_<br>
\(|\{(i,j)\in[n]\times[m]:P_{2d/p}(X_i,Y_j^*)\neq\emptyset\}|\le nm/p\).

_Moreover, there is an algorithm that, given the sets X<sub>i</sub>,Y<sub>j</sub>, computes the partitions along with the sets S<sub>g</sub>,T<sub>h</sub> and the shifts_ \(s_{i,\ell},t_{j,\ell}\) _in randomized time_ \(\tilde{O}(nmdp^3)\) _or deterministic time_ \(nmdp^3\cdot u^{o(1)}\).

**Proof.** We only show how to construct the partition of _X_ and the accompanying sets _S<sub>g</sub>_ and shifts _s<sub>i,g</sub>_. The partition of _Y_ is obtained symmetrically by exchanging _X_<sub>1</sub>_,...,X<sub>n</sub>_ and _Y_<sub>1</sub>_,...,Y<sub>m</sub>_. Consider the following algorithm. For each \(g\leftarrow 1,2,\dots\) we run the following steps:

1. Apply Lemma 4.8 to compute sets \(P_{2d/p}(X_i,Y_j)\subseteq P_{i,j}\subseteq P_{d/p}(X_i,Y_j)\) for all \((i,j)\in[n]\times[m]\).<tbc>

2. If \(|\{(i,j)\in[n]\times[m]:P_{i,j}\neq\emptyset\}|\le nm/p\): Pick \(X_i^*\leftarrow X_i\) for all \(i\in[n]\) and stop the algorithm.<tbc>

3. Otherwise: Pick some \(j\in[m]\) with \(|\{i\in[n]:P_{i,j}\neq\emptyset\}|\ge n/p\). We choose _S<sub>g</sub>_=-_Y<sub>j</sub>_. Let us call an index _i good_ if \(P_{i,j}\neq\emptyset\) and _bad_ otherwise. For each bad _i_ we choose \(X_{i,g}=\emptyset\) and _s<sub>i,g</sub>_ arbitrarily. For each good _i_ we instead choose an arbitrary shift \(s_{i,g}\in P_{i,j}\). Then we pick \(X_{i,g}=X_i\cap(S_g+s_{i,g})\). This forms the next part in the partition of _X<sub>i</sub>_, so we can safely remove it, \(X_i\leftarrow X_i\backslash X_{i,g}\).<tbc>

