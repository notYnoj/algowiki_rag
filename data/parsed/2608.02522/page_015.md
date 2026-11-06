it contains no monochromatic member of O_<sub>r</sub>_. In particular, there is no monochromatic closed odd walk of length at most 2_r_+1 in \((K_{[H+1]},\tau)\), since every closed odd walk yields an odd cycle of length at most the length of the walk. This implies that \(\ell=2r+3\) and that _z_<sub>1</sub>_,...,z_<sub>2_r_+3</sub> must be pairwise distinct, as otherwise \(z_1z_2\dots z_\ell\) or a suitable cyclic subsequence of it would form a monochromatic closed odd walk of length at most 2_r_+1 in \((K_{[H+1]},\tau)\), a contradiction.

Moving on, we distinguish two cases.

First, suppose that \(j+1\notin\{z_1,\dots,z_{2r+3}\}\). By definition of the vertex-coloring \(L_{j,c}(\cdot)\), this implies that every vertex of _C_ lies in a block on which _c_ is active. By invariant (iii) for counter _j_, no edge whose primary color under \(\kappa_j\) equals _c_ can join two distinct such blocks. Hence we find that the cycle _C_ must lie entirely within one block _V<sub>P</sub>_ on which _c_ is active. But then invariant (ii) for counter _j_ shows that the cycle _C_ corresponds to a monochromatic odd cycle of length 2_r_+3 under the coloring \(\kappa_{j-1}\) of the complete graph _K_<sub>_V<sub>j</sub>_-1</sub> identified with _K<sub>V<sub>P</sub></sub>_, contradicting our inductive assumption that invariant (iv) holds for counter _j_-1.

Hence we must have \(j+1\in\{z_1,\dots,z_{2r+3}\}\). Since we have shown that _z_<sub>1</sub>_,...,z_<sub>2_r_+3</sub> are pairwise distinct, _j_+1 equals exactly one of the _z<sub>i</sub>_. Without loss of generality (possibly after relabeling), we may assume that _z_<sub>1</sub>=_j_+1. Again by our definition of \(L_{j,c}(\cdot)\), we then must have that _v_<sub>1</sub> lies in a block _V<sub>Q</sub>_ on which _c_ is missing, while all the other vertices _v_<sub>2</sub>_,...,v_<sub>2_r_+3</sub> must lie in blocks on which _c_ is active. Again by invariant (iii) for counter _j_, the path \(v_2v_3\cdots v_{2r+3}\) must then lie in a single block \(V_P\neq V_Q\) on which _c_ is active. Both of the edges _v_<sub>1</sub>_v_<sub>2</sub> and _v_<sub>1</sub>_v_<sub>2_r_+3</sub> are assigned primary color _c_ by \(\kappa_j\). Hence, invariant (iii) for counter _j_ implies that

\(z_2=L_{j,c}(v_2)=L_{j,c}(v_{2r+3})=z_{2r+3},\)

contrary to the fact that we earlier proved that _z_<sub>1</sub>_,...,z_<sub>2_r_+3</sub> are pairwise distinct. This yields the desired contradiction and proves the invariant (iv) for counter _j_. All in all, this concludes the inductive proof that all invariants (i)-(iv) are satisfied for _j_=0,1_,...,H_.

Now consider the coloring \(\kappa_H:E(K_{V_H})\rightarrow[M_H]\times[q]\) of the complete graph _K<sub>V<sub>H</sub></sub>_ on _n<sub>H</sub>_ vertices at stage _H_ of the process. It uses a total of at most _M<sub>H</sub>q_ colors and by invariant (iv) there is no monochromatic member of O<sub>_r_+1</sub> in any color. By Lemma 3.2, we furthermore have

\(n_H=\prod_{j=1}^HB_j\ge\prod_{j=1}^H\frac{j^t}{s\left(e^2j\lceil logH\rceil 2\right)^s}=\frac{(H!)^{t-s}}{s^H\left(e^2\lceil logH\rceil 2\right)^{sH}}\)

and hence \(n_H\ge N_H\).

Altogether this shows that \(a_{r+1}(N_H)\le a_{r+1}(n_H)\le M_Hq=Htq=Hta_r(H+1)\), which is the statement of the lemma that we set out to prove. This concludes the proof. \(\square\)

_Proof of Theorem 1.7._ In the following, let _H_ be a sufficiently large integer, and let _m_, _s_, _t_ and _N<sub>H</sub>_ be defined as in the statement of Lemma 3.3 and let _M<sub>H</sub>_:=_Ht_. From the<tbc>

