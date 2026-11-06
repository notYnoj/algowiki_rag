Applying \(\mathrm{Red}_{\eta_\ell}\) multiplies the lower and upper bounds by \(1-\eta_\ell\) and \(1+\eta_\ell\), respectively, thereby yielding the induction.

The schedule satisfies<tbc>

\(s:=\sum_{\ell\ge 1}\eta_\ell<\frac{\varepsilon}{20}\le\frac{1}{40}.\)

<tbc>Therefore<tbc>

\(\prod_{\ell\ge 1}(1-\eta_\ell)\ge 1-s\ge 1-\varepsilon\)

<tbc>and, using \(e^x\le 1+2x\) for \(0\le x\le 1/2\),

\(\prod_{\ell\ge 1}(1+\eta_\ell)\le e^s\le 1+2s\le 1+\varepsilon.\)

This then finishes the claim.

**Claim 6.13.** _Let d_=NRD_<sub>n</sub>(R). A level-_\(\ell\) _sparsifier has support size at most_

\(O_R\big(\frac{d}{\varepsilon^2}(\ell+1)^{10}\big),\) (6.14)

_and each of its positive weights is an integer smaller than_ \(2^{\ell+1}\)_. On a stream of length m, the total space used is bounded by_

\(O_R\big(\frac{d}{\varepsilon^2}\mathrm{log}^{11}(m+2)\big(\mathrm{log}(n+2)+\mathrm{log}(m+2)+\mathrm{log}(1/\varepsilon+2)\big)\big)\) (6.15)

_bits._

_Proof._ Let<tbc>

\(b_\ell=\prod_{j=1}^\ell(1+\eta_j).\)

<tbc>The proof of Claim 6.11 gives \(b_\ell<2\). If a constraint _C_ has positive weight in a level-\(\ell\) sparsifier _H<sub>B</sub>_, then _C_ is not vacuously true (otherwise, we simply ignore the constraint), so some assignment \(\alpha_C\) violates it. Hence

\(w_{H_B}(C)\le\mathrm{unsatval}_{H_B}(\alpha_C)\le b_\ell\mathrm{unsatval}_{I_B}(\alpha_C)\le b_\ell|I_B|<2^{\ell+1}.\) (6.16)

Integrality follows from Lemma 6.5.

Put _q_=|_D_|. A uniformly random assignment violates every occurrence in the support of _H<sub>B</sub>_ with probability at least _q_<sup>-_k_</sup>. Therefore Claim 6.11 also gives the total-mass bound<tbc>

\(q^{-k}W(H_B)\le\mathbb{E}_\unknown[\mathrm{unsatval}_{H_B}(\unknown)]\le b_\ell\mathbb{E}_\unknown[\mathrm{unsatval}_{I_B}(\unknown)]<2^{\ell+1}.\)

<tbc>Now, we consider a merge that creates a level-\(\ell\) sparsifier, where \(\ell\ge 1\). Its input _J_ is the union of two level-\((\ell-1)\) sparsifiers. Adding the preceding bound for the two children gives<tbc>

\(W(J)<2q^k2^\ell=O_R(2^\ell).\) (6.17)

