On E<sub>fix</sub>, all intervals are valid, so<tbc>

\(\mathrm{LCB}_j\le\mu_j\le\mathrm{UCB}_j\text{for every}j\in\mathcal{A}.\)

<tbc>Therefore, for every \(\ell\neq h\),<tbc>

\(\mu_\ell-\mu_h\le\mathrm{UCB}_\ell-\mathrm{LCB}_h\le\varepsilon.\)

<tbc>If _h=k<sup>⋆</sup>_, the claim is immediate. Otherwise, choosing \(\ell=k^\star\) gives

\(\mu^\star-\mu_h\le\varepsilon,\)

and hence \(\mu_h\ge\mu^\star-\varepsilon\).

The next lemma is the key interval comparison: an arm can be pulled only while its own confidence radius is still large enough to explain the current ambiguity.

**Lemma 21** (Fixed-clipping structural comparison)**.** _Assume_ E<sub>fix</sub> _holds. Consider a non-stopping round, and write_<tbc>

\(B_k=\mathrm{max}_{a\neq k}\mathrm{UCB}_a-\mathrm{LCB}_k,h\in\mathrm{argmin}_{k\in\mathcal{A}}B_k,\ell\in\mathrm{argmax}_{a\neq h}\mathrm{UCB}_a.\)

<tbc>_If the algorithm samples_ \(k\in\{h,\ell\}\)_, then_<tbc>

\(B_h\le\mathrm{min}\{0,-\Delta_k+2\beta_k\}+2\beta_k,\)

<tbc>_where_ \(\beta_k:=\beta_\varepsilon(N_k,\delta/K)\).

<tbc>_Proof._ For brevity, write<tbc>

\(U_i:=\mathrm{UCB}_i,L_i:=\mathrm{LCB}_i,\beta_i:=\beta_\varepsilon(N_i,\delta/K).\)

<tbc>Since \(U_i-L_i=2\beta_i\) and the intervals are valid on E<sub>fix</sub>, we have<tbc>

\(L_i\le\mu_i\le U_i,U_i\le\mu_i+2\beta_i,L_i\ge\mu_i-2\beta_i\text{for all}i\in\mathcal{A}.\) (3)

<tbc>By definition of \(\ell\),<tbc>

\(B_h=\mathrm{max}_{a\neq h}U_a-L_h=U_\ell-L_h.\)

<tbc>_Case 1: the sampled arm is_ \(k=\ell\). The sampling rule gives \(\beta_\ell\ge\beta_h\). We first show that \(L_\ell\le L_h\). Suppose, for contradiction, that \(L_\ell>L_h\). Then<tbc>

\(U_\ell=L_\ell+2\beta_\ell>L_h+2\beta_h=U_h.\)

<tbc>Since \(U_\ell=\mathrm{max}_{a\neq h}U_a\), and since \(U_\ell>U_h\), we have<tbc>

\(\mathrm{max}_{a\neq\ell} U_a\le U_\ell.\)

<tbc>Hence<tbc>

\(B_\ell=\mathrm{max}_{a\neq\ell} U_a-L_\ell<U_\ell-L_h=B_h,\)

<tbc>contradicting the definition of _h_ as a minimizer of _B<sub>k</sub>_. Thus \(L_\ell\le L_h\), and therefore

\(B_h=U_\ell-L_h\le U_\ell-L_\ell=2\beta_\ell.\) (4)

We next prove<tbc>

\(B_h\le-\Delta_\ell+4\beta_\ell.\)

<tbc>If _h=k<sup>⋆</sup>_, then \(\ell\neq k^\star\). Using (3) and \(\beta_h\le\beta_\ell\),<tbc>

\(B_h=U_\ell-L_h\le(\mu_\ell+2\beta_\ell)-(\mu^\star-2\beta_h)\le-\Delta_\ell+4\beta_\ell.\)

<tbc>Now suppose \(h\neq k^\star\). Since \(k^\star\neq h\), the definition of \(\ell\) gives<tbc>

\(U_\ell=\mathrm{max}_{a\neq h}U_a\ge U_{k^\star}\ge\mu^\star.\)

<tbc>If \(\ell\neq k^\star\), then \(U_\ell\le\mu_\ell+2\beta_\ell\), and hence<tbc>

\(2\beta_\ell\ge\mu^\star-\mu_\ell=\Delta_\ell.\)

