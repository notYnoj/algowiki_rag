<tbc>**Definition 4.2** (Transfer surplus)**.** For an integral vector \(\unknown\) whose coordinates sum to zero, define the _transfer surplus_

\(\Delta_{J,k}(\unknown)=\mathrm{max}_{\mathbf{p}\in\mathcal{M}_k(J)\mathbf{p}+\unknown\ge\mathbf{0}}\rho_{J,k}(\mathbf{p}+\unknown)-\beta_k(J).\) (4.2)

An empty maximum has value \(-\infty\). The vector \(\unknown\) records a change in the local color counts relative to a proper coloring. Its coordinates can have both signs, although their sum is zero because the order of the summand is unchanged. For a union, this change must be offset by \(-\unknown\) on the other summand.

**Theorem 4.3.** _Let_ \(k\ge\mathrm{max}\{\chi(G),\chi(H)\}\)_, and put_<tbc>

\(T_k(G,H)=\mathrm{max}_\unknown\big(\Delta_{G,k}(\unknown)+\Delta_{H,k}(-\unknown)\big).\)

<tbc>_Then_<tbc>

\(\beta_k(G\sqcup H)=\beta_k(G)+\beta_k(H)+T_k(G,H),\) (4.3)

<tbc>_where_<tbc>

\(0\le T_k(G,H)\le\varepsilon_k(G)+\varepsilon_k(H).\) (4.4)

<tbc>_Proof._ A proper coloring of \(G\sqcup H\) is exactly a pair of local proper colorings, and hence<tbc>

\(\mathcal{M}_k(G\sqcup H)=\mathcal{M}_k(G)+\mathcal{M}_k(H).\)

<tbc>For fixed local source words, the two weak repairs are independent and their costs add. Maximizing over sources of prescribed local profiles therefore gives<tbc>

\(\beta_k(G\sqcup H)=\mathrm{max}_{\mathbf{a}\in\mathcal{A}_k(G),\mathbf{c}\in\mathcal{A}_k(H)\mathbf{a}+\mathbf{c}\in\mathcal{M}_k(G)+\mathcal{M}_k(H)}\big(\rho_{G,k}(\mathbf{a})+\rho_{H,k}(\mathbf{c})\big).\) (4.5)

<tbc>For every admitted pair **a**,**c**, choose proper profiles **p**,**q** with **p**+**q**+**c**. Then

\(\unknown=\mathbf{a}-\mathbf{p}=\mathbf{q}-\mathbf{c}\)

has coordinate sum zero. Conversely, proper profiles **p**,**q** and a vector \(\unknown\) for which \(\mathbf{p}+\unknown\) and \(\mathbf{q}-\unknown\) are nonnegative determine an admitted source pair. For fixed \(\unknown\), the choices of **p** and **q** are independent. Substitution into (4.5) and separate maximization over these two profiles prove (4.3).

The zero transfer satisfies \(\Delta_{J,k}(\mathbf{0})=0\), so \(T_k(G,H)\ge 0\). Also \(\rho_{J,k}(\mathbf{p}+\unknown)\le F_k(J)\), which bounds each surplus by \(\varepsilon_k(J)\) and proves the upper bound in (4.4). □

The theorem identifies two distinct effects in the original superadditivity question. A common palette changes the individual weak-villainy values to \(\beta_k(G)\) and \(\beta_k(H)\). Relative to these common-palette values, transferring color counts can only increase the worst repair cost, and its entire contribution is _T<sub>k</sub>(G,H_).

**Corollary 4.4.** _If_ \(\chi(G)=\chi(H)=k\)_, then_<tbc>

\(B_\mathrm{w}(G\sqcup H)=B_\mathrm{w}(G)+B_\mathrm{w}(H)\)

<tbc>_if and only if_

\(\Delta_{G,k}(\unknown)+\Delta_{H,k}(-\unknown)\le 0\text{\textit{for every}}\unknown.\) (4.6)

_In particular, equality holds if F<sub>k</sub>(G_)=_B_<sub>w</sub>(_G_) _and F<sub>k</sub>(H_)=_B_<sub>w</sub>(_H)._

_For arbitrary G,H, set_ \(k=\mathrm{max}\{\chi(G),\chi(H)\}\) _and_<tbc>

\(\Gamma_k(G,H)=B_\mathrm{w}(G)+B_\mathrm{w}(H)-\beta_k(G)-\beta_k(H).\)

<tbc>_Then_

\(B_\mathrm{w}(G\sqcup H)-B_\mathrm{w}(G)-B_\mathrm{w}(H)=T_k(G,H)-\Gamma_k(G,H).\) (4.7)

_Consequently superadditivity holds if and only if_ \(T_k(G,H)\ge\Gamma_k(G,H)\)_, and equality holds if and only if_ \(T_k(G,H)=\Gamma_k(G,H)\).

