**Lemma 25** (The best arm is never eliminated)**.** _On_ E<sub>ph</sub>, RESTARTPHASEDCLIP-1BITBAI _never eliminates k<sup>⋆</sup>._

_Proof._ Fix a phase _j_ and suppose _k<sup>⋆</sup>_ is active when the elimination rule is applied. Let _A_ be the active set at that moment and let<tbc>

\(m:=max_{i\in A}\mathrm{LCB}_{i,j}.\)

<tbc>On E<sub>ph</sub>, for every active arm _i_,<tbc>

\(\mathrm{LCB}_{i,j}\le\mu_i\le\mu^\star.\)

<tbc>Therefore<tbc>

\(m=max_{i\in A}\mathrm{LCB}_{i,j}\le\mu^\star.\)

<tbc>Also, since _k<sup>⋆</sup>_ is active and its interval is valid,<tbc>

\(\mathrm{UCB}_{k^\star,j}\ge\mu^\star.\)

<tbc>Combining the two displays gives

\(\mathrm{UCB}_{k^\star,j}\ge\mu^\star\ge m>m-\varepsilon.\)

Thus _k<sup>⋆</sup>_ cannot satisfy the elimination condition \(\mathrm{UCB}_{k,j}<m-\varepsilon\).

**Lemma 26** (Phased stopping and final-output correctness)**.** _On_ E<sub>ph</sub>_, every arm returned by_ RESTARTPHASEDCLIP-1BITBAI _is_ \(\varepsilon\)_-optimal._

_Proof._ There are three possible ways the algorithm returns.

_Singleton return._ If the active set has size one, Lemma 25 implies that the unique active arm must be _k<sup>⋆</sup>_, hence the output is correct.

_Interval stopping._ Suppose the algorithm returns an arm _h_ in phase _j_ because, with \(\ell\in argmax_{a\in A\backslash\{h\}}\mathrm{UCB}_{a,j}\),<tbc>

\(\mathrm{UCB}_{\ell,j}-\mathrm{LCB}_{h,j}\le\varepsilon.\)

<tbc>If _h=k<sup>⋆</sup>_, the claim is immediate. Otherwise, Lemma 25 implies that _k<sup>⋆</sup>_ is still active, and since \(k^\star\neq h\),<tbc>

\(\mathrm{UCB}_{\ell,j}=max_{a\in A\backslash\{h\}}\mathrm{UCB}_{a,j}\ge\mathrm{UCB}_{k^\star,j}\ge\mu^\star.\)

<tbc>Also \(\mathrm{LCB}_{h,j}\le\mu_h\), so

\(\mu^\star-\mu_h\le\mathrm{UCB}_{\ell,j}-\mathrm{LCB}_{h,j}\le\varepsilon.\)

Thus _h_ is \(\varepsilon\)-optimal.

_Final-phase return._ Finally, suppose the algorithm reaches the final phase _J_ and returns \(h\in argmax_{k\in A}\mathrm{LCB}_{k,J}\) after all active arms satisfy \(\beta_{k,J}\le r_J\). By Lemma 25, _k<sup>⋆</sup>_ is active. Hence<tbc>

\(\mathrm{LCB}_{h,J}\ge\mathrm{LCB}_{k^\star,J}.\)

<tbc>On E<sub>ph</sub> and because \(\beta_{k^\star,J}\le r_J\),<tbc>

\(\mathrm{LCB}_{k^\star,J}=\widehat{\mu}_{k^\star,J}-\beta_{k^\star,J}\ge\mu^\star-2\beta_{k^\star,J}\ge\mu^\star-2r_J.\)

<tbc>Similarly, \(\mu_h\ge\mathrm{LCB}_{h,J}\). Therefore

\(\mu_h\ge\mathrm{LCB}_{h,J}\ge\mathrm{LCB}_{k^\star,J}\ge\mu^\star-2r_J.\)

Since \(r_J=\rho_J/16\) and \(\rho_J\le\varepsilon\), we have \(2r_J\le\varepsilon/8\le\varepsilon\). Thus \(\mu_h\ge\mu^\star-\varepsilon\).

**Lemma 27** (Per-phase sample requirement)**.** _For each phase j, define_<tbc>

\(\Gamma_j:=log\frac{K(J+1)}{\delta}+loglog\left(e^e\frac{\sigma}{\rho_j}\right)+loglog\left(e^e\frac{K(J+1)}{\delta}\right).\)

<tbc>_There exists a universal constant C\>_0 _such that_<tbc>

\(n_j^\circ:=\left[C\frac{\alpha_j\sigma^2}{\rho_j^2}\Gamma_j\right]\)

<tbc>_satisfies_

\(\beta_j(n_j^\circ)\le r_j=\frac{\rho_j}{16}.\)

_Consequently, in phase j, an active arm is queried at most_ \(n_j^\circ\) _times before its phase-j radius is at most r<sub>j</sub>._

