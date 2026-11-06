So _T=T_<sub>1,1</sub>+_T_<sub>1,2</sub>+_T_<sub>2,1</sub>+_T_<sub>2,2</sub> for some tensors

\(T_{1,1}\in\mathcal{V}_{a-1}\otimes\mathcal{V}_b\otimes\mathcal{V}_{a+b-1}^*,T_{1,2}\in\mathcal{V}_{a-1}\otimes\mathcal{V}_b\otimes\mathcal{V}_{a+b-3}^*,\)<br>
\(T_{2,1}\in\mathcal{V}_{a-1}\otimes\mathcal{V}_{b-2}\otimes\mathcal{V}_{a+b-1}^*,T_{2,2}\in\mathcal{V}_{a-1}\otimes\mathcal{V}_{b-2}\otimes\mathcal{V}_{a+b-3}^*.\)

(Here V_<sub>b</sub>_ is considered as the subspace \(\mathcal{V}_b\oplus 0\subseteq\mathcal{V}_b\oplus\mathcal{V}_{b-2}\), similarly for the other factors.) Because we can obtain _T<sub>i,j</sub>_ from _T_ using SL<sub>2</sub>(C) equivariant projections along the direct sums, each _T<sub>i,j</sub>_ is SL<sub>2</sub>(C) invariant. By Lemma 3.7, \(T_{1,1}=\alpha_1\mathsf{P}_{a,b+1}\) and \(T_{2,2}=\alpha_2\mathsf{P}_{a,b-1}\) for some \(\alpha_1,\alpha_2\in\mathbb{C}\), and _T_<sub>2,1</sub>=0. Since _B_ and _C_ are isomorphisms, _T_, like \(\mathsf{P}_{a,b}\otimes\mathsf{P}_{1,2}\), is _concise_: no leg can be replaced by a proper subspace containing it. So \(\alpha_1\neq 0\) and \(\alpha_2\neq 0\), since otherwise _T_ would lie in \(\mathcal{V}_{a-1}\otimes(\mathcal{V}_b\oplus\mathcal{V}_{b-2})\otimes\mathcal{V}_{a+b-3}^*\) or in \(\mathcal{V}_{a-1}\otimes\mathcal{V}_b\otimes(\mathcal{V}_{a+b-1}^*\oplus\mathcal{V}_{a+b-3}^*)\). Composing _B_ with \(\alpha_1^{-1}I_{\mathcal{V}_b}\oplus\alpha_2^{-1}I_{\mathcal{V}_{b-2}}\) makes both diagonal coefficients equal to 1. Then the result follows from Lemma 2.3.

**Remark 3.8.** Over a field of positive characteristic, the Clebsch-Gordan decomposition can fail. For example, one checks that over a field F of characteristic 2, the representation \(\mathbb{F}^2\otimes\mathbb{F}^2\) of SL<sub>2</sub>(F) is not isomorphic to \(\mathrm{Sym}^2\mathbb{F}^2\oplus\mathbb{F}\). This is why the proof over every field uses a subspace and a quotient instead of this direct sum decomposition.

**Remark 3.9.** After homogenisation, \(\sigma_d\) is the multiplication map \(\mathbb{F}[x,y]_{d-1}\otimes\mathbb{F}[x,y]_1\rightarrow\mathbb{F}[x,y]_d\) of binary forms, which is equivariant for the action of SL<sub>2</sub>(F) by linear substitutions in _x_ and _y_. Over C, where \(\mathbb{C}[x,y]_d\cong\mathcal{V}_d\), it is, up to a nonzero scalar, the component \(\mathcal{V}_{d-1}\otimes\mathcal{V}_1\rightarrow\mathcal{V}_d\) of the SL<sub>2</sub>(C)-equivariant isomorphism \(\mathcal{V}_{d-1}\otimes\mathcal{V}_1\cong\mathcal{V}_d\oplus\mathcal{V}_{d-2}\) that the proof over C uses for _d=b_.

**Remark 3.10.** Lemma 3.6 generalises as follows. Let \(a,b,c\ge 1\) and \(d\ge 0\) be integers with \(b\ge c\) and _d\<c_. Then \(\mathsf{P}_{a,b+d}\oplus_1\mathsf{P}_{a,c-d}\unknown_1\mathsf{P}_{a,b}\oplus_1\mathsf{P}_{a,c}\); Lemma 3.6 is the case _b=c_ and _d_=1. The proof of Lemma 3.6 over every field gives this, with _t_<sup>_b-c+d_</sup> in place of _t_ in \(\iota_d\) and \(\sigma_d\). For an integer \(r\ge 1\) and a tuple \(\lambda=(\lambda_1,\dots,\lambda_r)\) of positive integers, let \(T_\lambda=\mathsf{P}_{a,\lambda_1}\oplus_1\cdots\oplus_1\mathsf{P}_{a,\lambda_r}\). Let \(\lambda\) and \(\nu\) be tuples of _r_ positive integers with the same sum. If \(\lambda\) majorises \(\nu\), that is, if for every \(k\in[r]\) the sum of the _k_ largest entries of \(\lambda\) is at least that of \(\nu\), then \(T_\lambda\unknown_1T_\nu\), by repeated use of the case _d_=1 on two of the summands.

## 3.4 Tripling degeneration for P_<sub>a,b</sub>_

We will construct a degeneration of a polynomial multiplication tensor to a partial direct sum of three smaller ones, the middle one with its second and third legs exchanged. The trivial starting point is this: for all integers \(a,b\ge 1\),

\(\mathsf{P}_{a,b}\oplus_1\mathsf{P}_{a,b}\le\mathsf{P}_{a,2b+a-1}.\) (3.5)

In terms of polynomials, the idea is as follows. The left-hand side describes the simultaneous multiplication \((f,(g_1,g_2))\mapsto(fg_1,fg_2)\) of polynomials \(f\in\mathbb{F}[t]_{\le a-1}\) and \(g_1,g_2\in\mathbb{F}[t]_{\le b-1}\). The restriction then follows the embedding of \((g_1,g_2)\mapsto g:=g_1+t^{a+b-1}g_2\in\mathbb{F}[t]_{\le 2b+a-2}\), and the subsequent observation that the coefficients of _fg_<sub>1</sub> and _fg_<sub>2</sub> appear as the coefficients of _fg_.

However, the coefficients of _g_ at _t<sup>b</sup>,...,t_<sup>_a+b_-2</sup> are not used. The tripling degeneration uses these coefficients, and _b_ further coefficients, for a third summand in the middle.

**Lemma 3.11** (Tripling degeneration)**.** _Let_ \(a,b\ge 1\) _be integers. Then_<tbc>

\(\mathsf{P}_{a,b}\oplus_1\left((23)\cdot\mathsf{P}_{a,b}\right)\oplus_1\mathsf{P}_{a,b}\unknown_1\mathsf{P}_{a,3b+a-1}.\)

