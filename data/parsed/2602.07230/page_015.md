[DGG99] Yefim Dinitz, Naveen Garg, and Michel X. Goemans. "On the single-source unsplittable flow problem". In: _Combinatorica_ 19.1 (1999), pp. 17–41.

[FF62] Lester R. Ford and Delbert R. Fulkerson. _Flows in Networks_. Princeton University Press, 1962.

[GMW22] Fabrizio Grandoni, Tobias Mömke, and Andreas Wiese. "A PTAS for unsplittable flow on a path". In: _Proceedings of the Annual ACM Symposium on Theory of Computing_. 2022.

[Kle96a] Jon M. Kleinberg. "Approximation algorithms for disjoint paths problems". PhD thesis. Massachusetts Institute of Technology, 1996.

[Kle96b] Jon M. Kleinberg. "Single-source unsplittable flow". In: _Proceedings of 37th Conference on Foundations of Computer Science_. IEEE. 1996, pp. 68–77.

[Knu74] Donald E. Knuth. "Wheels within wheels". In: _Journal of Combinatorial Theory, Series B_ 16.1 (1974), pp. 42– 46.

[Kol05] Stavros G. Kolliopoulos. "Minimum-cost single-source 2-splittable flow". In: _Information Processing Letters_ 94.1 (2005), pp. 15–18.

[Kol07] Stavros G. Kolliopoulos. "Edge-Disjoint Paths and Unsplittable Flow". In: _Handbook of Approximation Algorithms and Metaheuristics_ (2007).

[KS01] Stavros G. Kolliopoulos and Clifford Stein. "Approximation algorithms for single-source unsplittable flow". In: _SIAM Journal on Computing_ 31.3 (2001), pp. 919–946.

[MS22] Sarah Morell and Martin Skutella. "Single source unsplittable flows with arc-wise lower and upper bounds". In: _Mathematical Programming_ 192.1 (2022), pp. 477–496.

[MSW25] Mohammed Majthoub Almoghrabi, Martin Skutella, and Philipp Warode. "Integer and Unsplittable Multiflows in Series-Parallel Digraphs". In: _International Conference on Integer Programming and Combinatorial Optimization_. Springer. 2025, pp. 427–441.

[RT87] Prabhakar Raghavan and Clark D. Tompson. "Randomized rounding: a technique for provably good algorithms and algorithmic proofs". In: _Combinatorica_ 7.4 (1987), pp. 365–374.

[Sku02] Martin Skutella. "Approximating the single source unsplittable min-cost flow problem". In: _Mathematical Programming_ 91.3 (2002), pp. 493–514.

[SS09] Fernanda Salazar and Martin Skutella. "Single-source k-splittable min-cost flows". In: _Operations research letters_ 37.2 (2009), pp. 71–74.

[Swa+26] Chaitanya Swamy, Vera Traub, Laura Vargas Koch, and Rico Zenklusen. "Unsplittable Cost Flows from Unweighted Error-Bounded Variants". In: _2026 SIAM Symposium on Simplicity in Algorithms (SOSA)_. SIAM. 2026, pp. 512–523.

[TVZ24] Vera Traub, Laura Vargas Koch, and Rico Zenklusen. "Single-source unsplittable flows in planar graphs". In: _Proceedings of the 2024 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA)_. SIAM. 2024, pp. 639– 668.

[Wil19] David P. Williamson. _Network flow algorithms_. Cambridge University Press, 2019.

## Appendix A Hardness result

**Lemma 9.** _Given an unsplittable transshipment instance with integral supplies and demand values and unit arc capacities, it is NP-complete to decide whether there exists a feasible unsplittable transshipment._

_Proof._ The problem clearly belongs to `NP`. To establish `NP`-hardness, we reduce the `NP`-complete _arc- disjoint paths problem_ [Knu74] which is defined as follows: Given a directed graph _D_=(_V,A_) and a set \(\{(s^i,t^i)\}_{i=1}^k\subseteq V\times V\) of vertex pairs, the task is to determine whether there exist pairwise arc-disjoint paths _P_<sub>1</sub>_,...,P<sub>k</sub>_ such that _P<sub>i</sub>_ is an _s<sup>i</sup>_-_t<sup>i</sup>_ path for each _i_=1_,...,k_.

A given arc-disjoint paths instance can be turned into an unsplittable transshipment instance with unit arc capacities as follows: add direct arcs (_s<sup>i</sup>,t<sup>i</sup>_) for all \(i\neq j\) and assign supply _b(s<sup>i</sup>_)=_k_ and demand _b(t<sup>i</sup>_)=-_k_, for _i_=1_,...,k_. It is then easy to check that there exists a feasible unsplittable transshipment if and only if there exist arc-disjoint _s<sup>i</sup>_-_t<sup>i</sup>_ paths for _i_=1_,...,k_.

