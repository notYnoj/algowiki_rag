Proof. This lemma follows from Lemma 4.1 and the facts that, (i) at each level, the total number of the (next-level) items is at most _n_, and (ii) there are only three levels. □

**The Overall Query Algorithm.** To perform a PSS query with parameters \((\alpha,\beta)\) on _S_, the overall query algorithm is as simple as invoking Algorithm 1, Query(BG-Str(_S_), \((\alpha,\beta)\), \(\ell_\mathrm{cur}=1\)).

Lemma 4.10 (Correctness). _Every PSS query with parameters_ \((\alpha,\beta)\) _on S can be correctly answered with the three-level sampling hierarchy._

Proof. Follows immediately by applying Theorem 4.7 inductively. □

Lemma 4.11 (Query Complexity). _If there exists an algorithm that can solve every final-level instance on Z<sub>k</sub> optimally in_ \(O(1+\mu_{Z_k})\) _expected time, then the PSS query with parameters_ \((\alpha,\beta)\) _on S can be answered optimally in_ \(O(1+\mu_S(\alpha,\beta))\) _expected time._

Proof. First, by Lemma 4.2, there are at most 3 next-level instances on _Y<sub>j</sub>_’s at level-1. By the same lemma, each of these instances on _Y<sub>j</sub>_ can produce at most 3 next-level instances on _Z<sub>k</sub>_’s at level-2. And each instance on _Z<sub>k</sub>_ corresponds to a final-level instance _V<sub>k</sub>_. Therefore, there are in total at most 9 final-level instances.

Second, by mathematical induction from the final level, with Theorem 4.8, the query complexity of the one-level algorithm, and by the fact that there are at most 9 final-level instances, the overall expected query time complexity follows. □

Thus, the problem reduces to solving the final-level PSS instances optimally. Our approach is to use a lookup table. However, the basic idea of a lookup table is to _hard code_ all the possible sampling results for all possible _input configurations_ for a special family of _static subset sampling_ problems. Therefore, three main challenges must be addressed. The first challenge is to _efficiently_

S = {x1, x2, , xn} 2i 2i+1 2i+2 2i+3 2i+logn -1 2i+log n Level-1 BX(i) BX(i + 1) BX(i + 2) BX(i + log - 1) GX(j - 1) GX(j) (i = log n - )) GX(j + 1) Yj 2i' yi 2i'+1 yi+1 yi+2 2i'+2 2i' Level-2 BYj (i') BYj (i' + 1) BYj (i") (i' = log log n k) GYk (k') Zk Zk Zk Zi' Zi'+1 2i'+1 2i'+1 2i'+1 Level-3 Zk (l) (l) (l) (l') (l') (l') + 1) Vk Vk vl vl vl+1

Fig. 1. Visualization of the three-level sampling hierarchy. Here, circles represent items and ovals represent buckets. The diagram illustrates the structure of a level-1 group _G<sub>X</sub>(j_), where each bucket in _B<sub>X</sub>(i_) corresponds to an item \(y_i\in Y_j\). The BG-Str(_Y<sub>j</sub>_) contains multiple buckets in multiple groups. Each group, e.g. _G<sub>Y<sub>j</sub></sub>(k_) corresponds to a next-level item set, e.g. _Z<sub>k</sub>_. In level-3, each item set _Z<sub>k</sub>_ generates one final-level instance _V<sub>k</sub>_, in which each item corresponds to a bucket in level-3.

