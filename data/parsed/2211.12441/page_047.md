**Lemma 67 (interval matching).** _Let a,b be positive integers. For any real t, there exists a bijection_ \(\beta_t\) _between_ {1_,...,a_} _and_ {_b_+1_,...,b+a_} _such that for all k_=1_,...,a, k encloses_ \(\ell=\beta_t(k)\) _at t._

Note that the bijection can be different depending on _t_. In fact, this is necessary as otherwise \(\ell\) would need to be a multiple of _k_, which is not possible with a bijection between the sets {1_,...,a_} and {_b_+1_,...,b+a_}.

We can interpret Lemma 67 as a matching on a bipartite graph by using Hall’s marriage lemma.

**Lemma 68 (Hall’s marriage lemma).** _Let G be a bipartite graph with partitions L,R. For any_ \(A\subseteq L\)_, let N(A_) _be the set of all vertices in R with at least one neighbor in A. The graph G admits a perfect matching if and only if for all such A,_ \(|N(A)|\ge|A|\).

For \(A\subseteq\{1,\dots,a\}\), let _N<sub>t</sub>(A_) be the set of all \(\ell\in\{b+1,\dots,b+a\}\) such that there exists \(k\in A\) where _k_ encloses \(\ell\) at _t_. To produce the desired bijection \(\beta_t\) in Lemma 67, it is sufficient to prove that \(|N_t(A)|\ge|A|\) for all _t_ and _A_.

There are some values of \(\ell\) that are always contained in _N<sub>t</sub>(A_) regardless of the value of _t_. Let _N(A_) be the set of all \(\ell\in\mathbb{N}\) such that for all _t_, there exists \(k\in A\) where _k_ encloses \(\ell\) (this _k_ can vary depending on _t_). As \(N(A)\cap\{b+1,\dots,b+a\}\subseteq N_t(A)\), it is sufficient to prove that \(|N(A)\cap\{b+1,\dots,b+a\}|\ge|A|\) for all _A_ and apply Lemma 68 to prove Lemma 67.

**Example 69.** \(5\in N(\{2,3\})\).

_Proof._ We only consider \(t\in[0,1)\) for clarity. When \(t\in[0,0.4)\), the 2-interval for _t_ is \[0,0.5), while the 5-interval for _t_ is either \[0,0.2) or \[0.2,0.4), which means 2 encloses 5. When \(t\in[0.4,0.6)\), the 3-interval for _t_ is \[1/3,2/3), which encloses the 5-interval \[0.4,0.6). When \(t\in[0.6,1)\), the 2-interval is \[0.5,1) while the 5-interval is either \[0.6,0.8) or \[0.8,1), so 2 encloses 5. These enclosures are shown in Fig. 15, where the marked 5-intervals are contained within the respectively marked 2 or 3-intervals.

For all _t_, either 2 encloses 5, or 3 encloses 5. In other words, \(5\in N(\{2,3\})\).

We first consider a different characterization of _N(A_).

**Claim 70.** _Let_ \(\ell\) _be a positive integer. Then_ \(\ell\in N(A)\) _if and only if every open interval_ \(I\subset\mathbb{R}\) _that contains a fraction of denominator k for every_ \(k\in A\) _must also contain a fraction of denominator_ \(\ell\)_. (These fractions do not have to be distinct or reduced.)_

t
l
k
(a) Bad case: no interval enclosure
(b) Good case: interval enclosure

Figure 14: Enclosing intervals are needed for Lemma 65.

