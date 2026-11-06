<tbc>**Theorem 6.** _For each of flipping, swapping, and sliding,_ Coloring Discovery _is_ NP_-complete on connected graphs of diameter exactly two, even with exactly four available colors. Consequently, on connected input graphs, each variant is_ para-NP_-complete parameterized by q_+diam(_G), and also by q together with either radius or domination number._

_Proof._ We reduce from 3-Coloring \[16\]. Let _G_ have \(n\ge 2\) vertices. Add three independent reservoirs _R_<sub>1</sub>_,R_<sub>2</sub>_,R_<sub>3</sub>, each of size _n_, and a vertex _z_ adjacent to every vertex of \(G\cup R_1\cup R_2\cup R_3\). There are no other edges incident with reservoir vertices. Initially, _z_ has color 4, every vertex of _G_ has color 1, and every vertex of _R<sub>i</sub>_ has color _i_. Put _N_=4_n_+1. Set the budget to _n_ for flips, _N_-1 for swaps, and 3(_N_-1) for slides. The constructed graph is connected and has a dominating vertex. Two reservoir vertices are nonadjacent, so its diameter is exactly two.

Suppose first that _G_ has a proper 3-coloring \(\psi\). In the flip model, recolor the vertices of _G_, using at most _n_ flips. For the other models, write \(g_i=|\psi^{-1}(i)|\). Color the 3_n_ reservoir vertices so that 2_n-g_<sub>1</sub> of them have color 1, _n-g_<sub>2</sub> have color 2, and _n-g_<sub>3</sub> have color 3. These numbers are nonnegative and sum to 3_n_. The resulting coloring is proper and has the same histogram (2_n,n,n,_1) as the initial coloring. Lemma 1 gives at most _N_-1 swaps. For slides, choose the matching of tokens so that _z_ remains the unique vertex colored 4 and replace every transposition of two other vertices _u,v_ by the three slides (_u,z),(z,v),(u,z_). Thus 3(_N_-1) slides suffice.

Conversely, consider a reachable proper target. Under flips, the color on the universal vertex cannot occur on _G_, so the restriction to _G_ uses at most three colors. Under swaps or slides, the histogram remains (2_n,n,n,_1). We can assume \(n\ge 2\) as otherwise we could add isolated vertices, thus color 4 is the only color with multiplicity one. The color on a universal vertex is globally unique in every proper coloring, so _z_ must still have color 4. Hence _G_ is properly colored with colors 1,2,3.

Membership in NP has been established in all three models \[17,11,13\]. The construction also has radius one and domination number one, proving the stated consequences.

C1
C2
C3
C4
C5
G

**Fig.2.** The connectivity gadget for the sliding reduction, shown for _q_=3. Rainbow (_q_+1)-cliques form a chain, and a connector of each component of _G_ is attached to a distinct clique in the chain.

