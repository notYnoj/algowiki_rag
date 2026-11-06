been completed. For example, if some set _S<sub>i</sub>_ did not pay for any element during the whole execution, then _T_ is equal to the value of _b<sub>i</sub>_ at the end of the execution of Algorithm 1.

Let _Q_ be the set of queries that Algorithm 1 makes in the current round. We claim that every wasted query in _Q_ is charged only to sets that are solved in this round. Consider a wasted query _e_ that is in some set _S<sub>j</sub>_ not solved in this round. At the time _e_ was selected, _j_ cannot have been in _F<sub>e</sub>_ because otherwise _e_ would be a useful query. Therefore, we do not charge _e_ to _S<sub>j</sub>_.

The total number of wasted queries is therefore bounded by _Ts_, as these queries are paid for by the _s_ sets solved in this round. As the number of wasted queries in a bad round is larger than _k/_2, we therefore have _Ts\>k/_2. As _s\<a/r_, we get _k/_2_\<Ta/r_, so \(T>(r/2)\cdot(k/a)\).

Call a surviving set _S<sub>i</sub>_ **rich** if _b<sub>i</sub>\>k/a_ when the computation of _Q_ is completed. A set that is not rich is called **poor**. Note that a poor set must have spent at least an amount of \((r/2-1)\cdot(k/a)>0\), as its total budget would be at least \(T>(r/2)\cdot(k/a)\) if it had not paid for any queries. As the poor sets have paid for fewer than _k/_2 elements in total (as there are fewer than _k/_2 useful queries in the current round), the number of poor sets is bounded by \(\frac{k/2}{(r/2-1)\cdot(k/a)}=a/(r-2)>0\). As there are more than \((1-1/r)\cdot a\) surviving sets and at most _a/(r_-2) of them are poor, there are at least \((1-1/r)\cdot a-a/(r-2)=((r-2)(r-1)-r)/(r(r-2))\cdot a=2a/(2+\varepsilon)>0\) surviving sets that are rich.

Let _e_ be any element that is the leftmost unqueried element (at the end of the current round) of a rich surviving set. If _e_ was the leftmost unqueried element of more than _a/k_ rich surviving sets, those sets would have been able to pay for _e_ (because their total remaining budget would be greater than \(k/a\cdot a/k=1\)) before the end of the execution of Algorithm 1, a contradiction to _e_ not being included in _Q_. Hence, the number of distinct leftmost unqueried elements of the at least \(2a/(2+\varepsilon)\) rich surviving sets is at least \((2a/(2+\varepsilon))/(a/k)=2k/(2+\varepsilon)\). So the following round will query at least \(2k/(2+\varepsilon)\) elements that are the leftmost unqueried element of an active set, and all those are useful queries that are made in the next round. \(\blacktriangleleft\)

\(\blacktriangleright\) **Theorem 4.3.** _Let_ opt_<sub>k</sub> denote the optimal number of rounds and A<sub>k</sub> the number of rounds made if the queries are determined using Algorithm 1. Then, for every_ \(0<\varepsilon<1\), \(A_k\le(2+\varepsilon)\cdot\mathrm{opt}_k+\mathrm{O}\left(\frac{1}{\varepsilon}\cdot\mathrm{lg}m\right)\).

**Proof.** In every round, one of the following must hold:

The algorithm makes at least _k/_2 useful queries.

The algorithm solves at least a fraction of 1_/r_ of the active sets.

If none of the above hold, the algorithm makes at least \(2k/(2+\varepsilon)\) useful queries in the following round (by Lemma 4.2).

The number of rounds in which the algorithm solves at least a fraction of 1_/r_ of the active sets is bounded by \(\lceil log_{r/(r-1)}m\rceil=\mathrm{O}\left(\frac{1}{\varepsilon}\cdot\mathrm{lg}m\right)\), since \(1/\left(\mathrm{lg}\frac{r}{r-1}\right)<5/\varepsilon\) for \(0<\varepsilon<1\). In every round where the algorithm does not solve at least a fraction of 1_/r_ of the active sets, the algorithm makes at least \(k/(2+\varepsilon)\) useful queries on average (if in any such round it makes fewer than _k/_2 useful queries, it makes \(2k/(2+\varepsilon)\) useful queries in the following round). The number of such rounds is therefore bounded by \((2+\varepsilon)\cdot\mathrm{opt}_k\). \(\blacktriangleleft\)

We do not know if this analysis is tight, so it would be worth investigating this question.

## 4.2 The Minimum Problem with Disjoint Sets

We now consider the case where \(k\ge 2\) and the _m_ sets in the given family S are pairwise disjoint. For this case, it turns out that the balanced algorithm achieves good upper bounds.

