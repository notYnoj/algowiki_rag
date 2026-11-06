For any level-1 _X_-block, if the portion of it in the _r_-th region of the _t_-th term is not \(\varepsilon\)-approximate consistent with \(\beta_{X,t}^{(r)}\), we zero it out. We similarly handle level-1 _Y_ -blocks and _Z_-blocks. It is not hard to see the following.

**Claim 6.4.** _After the previous zeroing-out, we obtain a tensor that is isomorphic to_<tbc>

\(\otimes_{r=1}^3\otimes_{t=1}^{s^\prime} T_{i_t,j_t,k_t}^{\otimes A_t,r}n_t[\beta_{X,t}^{(r)},\beta_{Y,t}^{(r)},\beta_{Z,t}^{(r)},\varepsilon].\)

<tbc>_Proof._ We only need to show that for a fixed _t_,

\(T_{i_t,j_t,k_t}^{\otimes n_t}[\beta_{X,t},\beta_{Y,t},\beta_{Z,t},\varepsilon]\unknown\otimes_{r=1}^3T_{i_t,j_t,k_t}^{\otimes A_t,r}n_t[\beta_{X,t}^{(r)},\beta_{Y,t}^{(r)},\beta_{Z,t}^{(r)},\varepsilon]\) (15)

by performing the above zeroing-out rule, i.e., zeroing out every level-1 _X_-block whose portion in the _r_-th region is not \(\varepsilon\)-approximate consistent with \(\beta_{X,t}^{(r)}\), and doing similarly for _Y_ - and _Z_-blocks. Suppose some level-1 _X_-block belongs to the right-hand side and has complete split distributions \(\xi_{X,t}^{(1)},\xi_{X,t}^{(2)},\xi_{X,t}^{(3)}\) in three regions respectively, each of which is at most \(\varepsilon\) away from \(\beta_{X,t}^{(1)},\beta_{X,t}^{(2)},\beta_{X,t}^{(3)}\) in \(L_\infty\) distance. Then, its average complete split distribution \(\xi_{X,t}:=A_1\xi_{X,t}^{(1)}+A_2\xi_{X,t}^{(2)}+A_3\xi_{X,t}^{(3)}\) has at most \(\varepsilon\) distance from \(\beta_{X,t}\), which means that the considered level-1 _X_-block also belong to the left-hand side. It is the same for _Y_ - and _Z_-blocks, so the right-hand side of (15) is a subtensor of the left-hand side, i.e., Eq. (15) holds, which further implies the claim.

In the following, we will focus on the first region _r_=1, in which we will apply asymmetric hashing that allows the sharing of _Z_-blocks. Let

\(\mathcal{T}^{(1)}:=\otimes_{t=1}^{s^\prime} T_{i_t,j_t,k_t}^{\otimes A_{t,1}n_t}[\beta_{X,t}^{(1)},\beta_{Y,t}^{(1)},\beta_{Z,t}^{(1)},\varepsilon].\)

We will omit the superscript (1) on all variables for conciseness.

## 6.2 Asymmetric Hashing

Next, we apply hashing similarly to the global stage. For every \(t\in[s']\), recall that \(\alpha_t\) is a distribution on \(\{(i',j',k')\in\mathbb{Z}_{\ge 0}^3:i'+j'+k'=2^{\ell-1}\}\). Additionally, the marginal distributions of \(\alpha_t(i',j',k')\) on the three dimensions are the same as \(\gamma_{X,t}(i',i_t-i')\), \(\gamma_{Y,t}(j',j_t-j')\), \(\gamma_{Z,t}(k',k_t-k')\), respectively.

Each level-\((\ell-1)\) index sequence is partitioned into \(s'\) parts, where each part corresponds to one term in T . The _t_-th part is a length-\((2n_t)\{0,\dots,2^{\ell-1}\}\)-sequence, which can also be viewed as a length-\((n_t)\{0,\dots,2^{\ell-1}\}^2\)-sequence by combining pairs of adjacent numbers. If the _t_-th part of a level-\((\ell-1)X\)-index sequence is not consistent with the distribution \(\gamma_{X,t}\) for any _t_, we zero out the corresponding level-\((\ell-1)X\)-block. We similarly handle the _Y_ - and _Z_-blocks.

Let _N_<sub>BX</sub> be the number of remaining level-\((\ell-1)X\)-blocks, and it is not difficult to see that

\(N_\mathrm{BX}=2^{\sum_tH(\gamma_{X,t})\cdot A_{t,1}n_t\pm o(n)}.\) (16)

Similarly, let _N_<sub>BY</sub> and _N_<sub>BZ</sub> be the number of remaining _Y_ - and _Z_-blocks, and we have

\(N_\mathrm{BY}=2^{\sum_tH(\gamma_{Y,t})\cdot A_{t,1}n_t\pm o(n)},N_\mathrm{BZ}=2^{\sum_tH(\gamma_{Z,t})\cdot A_{t,1}n_t\pm o(n)}.\) (17)

