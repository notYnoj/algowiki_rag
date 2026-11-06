<tbc>lower bound for \(f\ge 2\). For all-pairs single-failure min-cut, Baswana and Pandey \[BP22\] obtained an _O(n_<sup>2</sup>)-space, _O_(1)-query oracle. These combinatorial approaches exploit the structure of near- minimum cuts and flow decompositions, and appear inherently limited to one or two failures. Our framework resolves the open problem of \[BBP22\], providing the first (_s,t_)-min-cut sensitivity ora cle for any _f_, with _O_((_fn_)<sup>2</sup>log_n_) space, \(\widetilde{O}(f^{3\omega})\) query time for the value, and \(\widetilde{O}(f^{3\omega} n)\) time for reporting the nearest min-cut.

#### Fault-Tolerant Reachability and Distances.

Algebraic matrix tools have become a powerhouse for dynamic and fault-tolerant reachability and distances. Sankowski \[San04\] introduced dynamic reachability algorithms based on maintaining the inverse of a symbolic adjacency matrix. For weighted graphs, Weimann and Yuster \[WY13\] employed matrix adjoint computation for distance sensitivity, constructing an _f_-DSO with \(\widetilde{O}(n^{3-\alpha})\) space and \(\widetilde{O}(n^{2-2(1-\alpha)/f})\) query time. Brand and Saranurak \[vdBS19\] substantially improved the preprocessing and query time for multiple failures, obtaining \(\widetilde{O}(Wn^3)\) preprocessing and \(\widetilde{O}(Wnf^\omega)\) query time. Karczmarz and Sankowski \[KS23a\] recently improved multiple-failure DSOs via generic matrices and the Frobenius normal form. On the combinatorial side, \[DTCR08, BK09, DP10, CLPR12, BGLP16, Cho16, BCR17, CCFK17, DP17, GIP17, GDHI<sup>+</sup>17, GS18, BCFS21, IKP21, DR22, BCC<sup>+</sup>23, DG24\] studied the problem of designing fault-tolerant oracles for reachability, distances, and strong connectivity.

#### Dynamic Algorithms.

In the fully dynamic regime, min-cut algorithms range from Thorup’s tree-packing approach \[Tho07\] to recent expander-decomposition methods \[GHN<sup>+</sup>23, JST24\], sub- polynomial update times for all-pairs min-cuts \[JS22\], and dynamic flow advances \[VDBCK<sup>+</sup>24, vdBCK<sup>+</sup>, CKL<sup>+</sup>24, Kar24\]. Several recent works study dynamic graph algorithms with predictions \[PR23, HKP24, HSSY24, vdBFNP24, LS24, MMNS24, MMN<sup>+</sup>25\], a model related in spirit to our subset sensitivity setting.

### 1.4 Organization

The remainder of this paper is organized as follows. We establish notation and algebraic primitives in Section 2. We next present our packing and covering oracles in Section 3. These primitives are applied to flows and cuts in Section 4, and to spanning structures in Section 5. We extend the framework to linear matroid parity and \(\alpha\)-factors in Sections 6 and 7 respectively. Our subset sensitivity results are presented in Section 8, and matching space lower bounds are presented in Section 9.

## 2 Preliminaries

Let _G_=(_V,E_) be an uncapacitated directed graph with a cost function \(c:E\rightarrow\{-W,\dots,W\}\). A _trail P_ from edge _e_<sub>0</sub> to edge \(e_\ell\) in _G_ is a sequence of distinct edges \((e_0,e_1,\dots,e_\ell)\) with head(_e<sub>i</sub>_)=tail(_e_<sub>_i_+1</sub>) for each \(0\le i<\ell\) (vertices may repeat). The cost of a trail is the sum of its edge costs. A trail is a _path_ if no vertex repeats.

For a subset of _U_=(_I,F_) of edge updates consisting of a set _I_ of edge insertions and a set \(F\subseteq E\) of edge deletions, with \(|U|=|I|+|F|\le f\), we denote by \(G+U:=(V,(E\backslash F)\cup I)\) the graph obtained by applying the updates in _U_ to _G_.

For a pair \(s,t\in V\) , we use \(\lambda_G(s,t)\) to denote the maximum value of an (_s,t_)-flow in _G_. An (_s,t_)_-cut C_ partitions the vertex set into (_A<sub>C</sub>,B<sub>C</sub>_) with \(s\in A_C\) and \(t\in B_C\); its capacity is the number of edges directed from _A<sub>C</sub>_ to _B<sub>C</sub>_, and an (_s,t_)-min-cut is one with minimum capacity, of value \(\lambda_G(s,t)\) by the max-flow min-cut theorem. For a fixed source \(s\in V\) , the _s-min-cut_ value is<tbc>

