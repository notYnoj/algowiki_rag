<tbc>_can be computed deterministically in time_

\(O\underbrace{\big(L|W|\sum_{d=0}^t\alpha_d}_\text{queries}+\underbrace{Lm\frac{\rho^t}{1-\rho}N^2}_\text{boxes}+\underbrace{\frac{N\cdot 10^L}{\sqrt{K}N_0}}_\text{encodings}\big).\) (9)

_The constants hidden in the_ \(O(\cdot)\) _depend only on the exponent in N_<sup>_O_(1)</sup>.

_Proof. Preprocessing._ We tile the product as in Section 2.3.4, padding _N_ to a multiple of _K_<sub>0</sub>_N_<sub>0</sub>, which at most doubles it since \(N\ge\sqrt{K}N_0\ge K_0N_0\), and we store the \(K_0^2\) subsets, in \(O(KL)\le O(10^L)\) operations. We then form and encode the input arrays of all row bands and column bands, at most \(4N/(\sqrt{K}N_0)\) of them since \(K_0\ge\sqrt{K}/2\). Each has at most \(KN_0D\le 7^L\) nonzero entries, so we form it in \(O(L\cdot 7^L)\) operations, and its encoding takes _O_(10_<sup>L</sup>_) operations (Section 2.4.1). This is the last term of (8). Finally, we compute the values of all the boxes of each of the at most 4_N_<sup>2</sup>_/M_ tiles, where \(M=KN_0^2\) is the number of output entries of a tile. By Lemma 29, this takes \(O(L(m+1)\sum_{d\ge t}\beta_d)\) time and space per tile, and \(\sum_{d\ge t}\beta_d\le M\rho^t/(1-\rho)\) by (7), which gives the first term.

_Query._ Given (_I,J_), we find its tile from the bands of row _I_ and column _J_, the subset _Q_ of its block product, and its output string _w_ (whose variables at the levels outside _Q_ we read off the row and column of (_I,J_) within the block product), all in _O(L_) operations (Section 2.4.4). We then compute (_X<sub>Q</sub>Y<sub>Q</sub>_)\[_w_\] as the sum in Lemma 28, which has two parts.

The first part is the sum of the products at the leaves of order below _t_ contributing to _w_. Each of these leaves is obtained from the private leaf of _w_, which has _P_<sub>0</sub> at every level of _Q_, by picking fewer than _t_ of those levels and replacing _P_<sub>0</sub> with one of the nine other terms at each of them. We enumerate them, and for each such leaf \(\tau\) we look up its two numbers \(\Phi_\tau(a)\) and \(\Psi_\tau(b)\) in the encodings of the tile and multiply them. The second part is the sum of the values of the boxes of _w_: for every \(V\subseteq Q\) with |_V_|=_m-t_ and every box of B_<sub>V</sub>_, we look up its value in the trie of the tile. In all, these are \(\sum_{d=0}^{t-1}\alpha_d+\alpha_t\) numbers, and we find each of them in _O(L_) operations, including forming its leaf or its box from the private leaf. Enumerating them also takes _O(L_) operations per number. By Section 2.4.4, the sum is (_XY_)\[_I,J_\]. For a set _W_, we ask |_W_| queries, which gives (9).

_Word size._ As in Section 2.4.4, every number in an encoding is a sum of entries of the input array with coefficients \(0,\pm 1\), and every value we compute is a sum of at most 10_<sup>m</sup>_ products of two such numbers. Since \(N\ge N_0=3^{L-m}\) and \(L\ge 10m\), we have \(10^L\le N^{5/2}\), so, as in Section 2.4.4, all the values are _N_<sup>_O_(1)</sup> in absolute value, and every integer we use has _O_(log_N_) bits.

## 4.4 Choosing the parameters

We now choose the parameters in Theorem 30 and prove the results of Section 4.1. In other words, we do the arithmetic and bookkeeping to derive the explicit exponents from Theorem 30. We first do the calculation in full for a single choice of the parameters, _L_=21_m_ and \(t=\lceil m/9\rceil\), which proves Corollary 26. We then say what changes for other choices, which gives Theorems 24 and 25 and the entries of  2.

_Proof of Corollary 26. Setting up._ Let \(m:=\lceil log_4D\rceil\), and pad the inner dimension to 4_<sup>m</sup>\<_4_D_ with zero columns of _X_ and zero rows of _Y_ . This changes no entry of _XY_ , and it changes _D_ by a factor less than 4, which only affects the constants. So from now on _D_=4_<sup>m</sup>_, and since<tbc>

