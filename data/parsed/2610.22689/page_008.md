1. The projective subgroup \(\pi(G)\subseteq\mathrm{PU}(W)\) is closed. This holds, in particular, under the periodicity conditions of (11).<tbc>

2. The vector \(|s\rangle\) is an eigenvector of some _H<sub>r</sub>_, \(1\le r\le k\), and its corresponding eigenspace is one- dimensional.

Then there exist an integer \(L\ge 0\), indices<tbc>

\(j_1,\dots,j_L\in\{1,\dots,k\},\)

<tbc>and collection of parameters \(\theta=(\theta_1,\dots,\theta_L)\in\mathbb{R}^L\) such that

\(U_L(\theta)\cdot[s]=[t]\) (13)

with \(U_L(\theta)\) as in (5).

**Remark IV.5.** Every product ansatz of the form (5) in Theorem IV.4 can also be expressed using the fixed-order layered ansatz

\(U_L(\theta)=\prod_{\ell=1}^L\left(e^{-i\theta_{\ell,k}H_k}\cdots e^{-i\theta_{\ell,1}H_1}\right),\) (14)

where the product is time-ordered from right to left. Indeed, one may use a single nonzero parameter in each layer \(\ell\) corresponding to generator \(H_{j_\ell}\), setting all remaining parameters within that layer equal to zero.

For _k_=2, with _H_<sub>1</sub>=_H<sub>P</sub>_ and _H_<sub>2</sub>=_H<sub>M</sub>_, equation (14) reduces to the standard QAOA circuit

\(U_p(\beta,\gamma)=\prod_{k=1}^pe^{-i\beta_kH_M}e^{-i\gamma_kH_P}=e^{-i\beta_pH_M}e^{-i\gamma_pH_P}\cdots e^{-i\beta_1H_M}e^{-i\gamma_1H_P},\) (15)

where \(\beta=(\beta_1,\dots,\beta_p)\in\mathbb{R}^p\) and \(\gamma=(\gamma_1,\dots,\gamma_p)\in\mathbb{R}^p\) are variational parameters.

**Corollary IV.6.** Suppose that the DLA g admits a decomposition

\(\mathfrak{g}=[\mathfrak{g},\mathfrak{g}]\oplus\mathfrak{c},\mathfrak{c}\subseteq i\mathbb{R}I_W.\) (16)

Then every projective _G_-orbit is closed. Consequently, for any non-zero states \(|s\rangle,|t\rangle\in W\),

\([t]\in\overline{G\cdot[s]}\)

implies that \(|t\rangle\) is exactly (up to a global phase) reachable from \(|s\rangle\) by a finite parameterized circuit.

In particular, the conclusion holds whenever g is semisimple.

