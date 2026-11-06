\(\blacktriangleright\) **Lemma 4.9.** BAL _is_ O(lg_k/_lglg_k)-round-competitive._

**Proof.** If \(k\ge m\), the lemma follows from Corollary 4.8.

If _k\<m_, let _L_ be the given instance and let _R_<sub>0</sub> be the number of rounds the algorithm needs until the number of active sets falls below _k_+1 for the first time. As the algorithm makes at most one query in each active set in the first _R_<sub>0</sub> rounds, all queries made in the first _R_<sub>0</sub> rounds are useful. Let \(L'\) be the instance at the end of round _R_<sub>0</sub>. As \(L'\) has at most _k_ active sets, BAL is O(lg_k/_lglg_k_)-round-competitive on \(L'\) by Corollary 4.8, and it needs at most \(\mathrm{O}(\mathrm{lg}k/\mathrm{lglg}k)\cdot\mathrm{opt}_k(L')=\mathrm{O}(\mathrm{lg}k/\mathrm{lglg}k)\cdot\lceil\mathrm{opt}_1(L')/k\rceil\) rounds to solve \(L'\).

We have that \(\mathrm{opt}_1(L)=k\cdot R_0+\mathrm{opt}_1(L')\), and hence \(\mathrm{opt}_k(L)=R_0+\lceil\mathrm{opt}_1(L')/k\rceil\). Thus,

\(\mathrm{BAL}_k(L)\le R_0+\mathrm{O}(\mathrm{lg}k/\mathrm{lglg}k)\cdot\lceil\mathrm{opt}_1(L')/k\rceil\)<br> \(\le\mathrm{O}(\mathrm{lg}k/\mathrm{lglg}k)\cdot(R_0+\lceil\mathrm{opt}_1(L')/k\rceil)\)<br> \(=\mathrm{O}(\mathrm{lg}k/\mathrm{lglg}k)\cdot\mathrm{opt}_k(L),\)

and the claim follows.

The following theorem then follows from Corollary 4.8 and Lemma 4.9.

\(\blacktriangleright\) **Theorem 4.10.** BAL _is_ O(lgmin{_k,m}/_lglgmin{_k,m})-round-competitive._

## 4.3 Lower Bounds

In this section we present lower bounds for Minimum that hold even for the more restricted case where the family S consists of disjoint sets.

\(\blacktriangleright\) **Theorem 4.11.** _For arbitrarily large m and any deterministic algorithm ALG, there exists an instance with m sets and k\>m queries per round, such that_ opt_<sub>k</sub>_=1, \(\mathrm{ALG}_k\ge W^{-1}(\mathrm{lg}m)\) _and_ \(\mathrm{ALG}_k=\Omega(W^{-1}(\mathrm{lg}k))\)_. Hence, there is no_ o(lgmin{_k,m}/_lglgmin{_k,m})-round- competitive deterministic algorithm._

**Proof.** Fix an arbitrarily large positive integer _M_. Consider an instance with _m=M<sup>M</sup>_ sets, and let _k=M_<sup>_M_+1</sup>. Each set contains _Mk_ elements, with the _i_-th element having uncertainty interval \((1+i\varepsilon,100+i\varepsilon)\) for \(\varepsilon=1/m\). The adversary will pick for each set an index _j_ and set the _j_-th element to be the minimum, by letting it have value \(1+(j+0.5)\varepsilon\), while the _i_-th element for \(i\neq j\) is given value \(100+(i-0.5)\varepsilon\). The optimal query set for the set is thus its first _j_ elements. We assume that an algorithm queries the elements of each set in order of increasing lower interval endpoints. (Otherwise, the lower bound only becomes larger.)

Consider the start of a round when \(a\le m\) sets are still active; initially _a=m_. The adversary observes how the algorithm distributes its _k_ queries among the active sets and repeatedly adds the active set with largest number of queries (from the current round) to a set L, until the total number of queries from the current round in sets of L is at least (_M_-1)_k/M_. Let \(\mathcal{S}'\) denote the remaining active sets. Note that \(|\mathcal{S}'|\ge a/M\). For the sets in L, the adversary chooses the minimum in such a way that a single query in the current round would have been sufficient to find it, while the sets in \(\mathcal{S}'\) remain active (and so the optimum must make the same queries in them that the algorithm has made in the current round, and these are at most _k/M_ queries). We continue for _M_ rounds. In the _M_-th round, the adversary picks the minimum in all remaining sets in such way that a single query in that round would have been sufficient to solve the set. The optimal number of queries is then at most (_M_-1)_k/M+M<sup>M</sup>_=(_M_-1)_k/M+k/M=k_, and hence opt_<sub>k</sub>_=1. On the other hand, we have ALG_<sub>k</sub>=M_.

