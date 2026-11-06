_given in Algorithm 5 satisfies_ \(\frac{1}{4}k_e\le k'_e\le k_e\)_. Furthermore, the algorithm requires_ \(\widetilde{O}(n/\varepsilon^2)\) _oracle queries to produce a sparsifier H with the following properties:_

• _H has_ \(O(nlogn/\varepsilon^2)\) _edges._<tbc>

• _The maximum weight of any edge e in H is_ \(O(\varepsilon^2k_e/logn)\).<tbc>

• _Every cut in H approximates the corresponding cut in G within a_ \((1\pm\varepsilon)\) _factor._

**6.1 Input:** Oracle access to the cut values of an unweighted simple graph _G_.

1. Compute all of the single-vertex cuts.<tbc>

2. Compute a sparsifier _H_ of _G_ using Algorithm 5 with small constant \(\varepsilon\).<tbc>

3. Find all non-singleton cuts of size at most \((1+3\varepsilon)\) times the size of the minimum cut in _H_, and contract any edge which is not in such a cut. Call the resulting graph \(G'\).<tbc>

4. If the number of edges between the super-vertices of \(G'\) is _O(n_), learn all of the edges between the super-vertices of \(G'\) and compute the minimum cut.

**Output:** Return the best cut seen over the course of the algorithm.

**Theorem D.6** (Theorem 4.2 from \[RSW18\])**.** _Algorithm 6 uses_ \(\widetilde{O}(n)\) _queries and finds the exact minimum cut in G with high probability._

_Proof of Theorem 1.6._ For each \(0\le j\le logn\), step 2(a) of Algorithm 5 can be implemented using Lemma 5.4 with \(O(|E_j|\cdot q_j\cdot logn)+\widetilde{O}(n)\) comparison queries in expectation; which is shown to be \(\widetilde{O}(n)\) in the proof of Theorem D.5. The runtime bound of the same step is \(\widetilde{O}(n^2)\). Step 2(b)(ii) of Algorithm 5 also takes \(\widetilde{O}(n/\varepsilon^2)\) queries and \(\widetilde{O}(n^2)\) time because the number of edges sampled and added to _H_ is shown to be \(\widetilde{O}(n/\varepsilon^2)\) (see proof of Theorem 4.2, \[RSW18\]) and this sub-sampling can be done again using Lemma 5.4. In Algorithm 6, since step (1) is only used to compare the singleton cuts to output the minimum cut seen by the algorithm, we can implement this using comparison in _O(n_) queries and time. In step (3), all the approximate cuts can be computed in \(\widetilde{O}(n^2)\) time using \[HHS24\]. In step (4), all the edges of \(G'\) can be learned using Lemma 5.4 with _p_=1. The proof of theorem D.6 shows that the number of edges in \(G'\) is at most _O(n_) with high probability. This implies that all the steps in the algorithms take \(\widetilde{O}(n/\varepsilon^2)\) queries and \(\widetilde{O}(n^2)\) time. There are at most log_n_ steps in any algorithm which proves the desired bounds.

## D.3 Weighted Min-Cut: Special Cases and Stronger Oracles

In the weighted setting, where the edges of the graph _G_=(_V,E_) have unknown non-negative weights, the techniques developed for the unweighted case (where weights are 0 or 1; see Section 5) no longer apply. Even when the weights are restricted to integers in \[0_,B_\], little is known.

### D.3.1 Weighted regular graphs

We consider the case when the graph satisfies the _weighted regularity_ condition, i.e., \(|w^*(\partial u)|\) is identical for all \(u\in V\) . Under this assumption,

\(w^*(\{u,v\})=\frac{1}{2}\big(w^*(\partial u)+w^*(\partial v)-w^*(\partial\{u,v\})\big),\) (33)

**Algorithm 6:** Simpler global Min Cut with \(\widetilde{O}(n)\) oracle queries

