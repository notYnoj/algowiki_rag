<tbc>Hence \(a(\Phi,\phi)=a(\phi,\phi)\). On the set \(\{\phi>0\}\cap D_s\) we have \(U+\Phi\ge-M_U+M_U=0\), so \(r(U+\Phi)\ge r(0)=0\) there, and therefore \((r(U+\Phi),\phi)_{D_s}\ge 0\). Taking \(v=\phi\) in the weak formulation gives<tbc>

\(a(\phi,\phi)=a(\Phi,\phi)=-\big(r(U+\Phi),\phi\big)_{D_s}\le 0,\)

<tbc>so that \(|||\phi|||=0\) and \(\phi=0\), i.e., \(\Phi\le M_U\) a.e. For the lower bound, let

\(\psi:=(\Phi+M_U)^-=\mathrm{min}\{\Phi+M_U,0\}\in H_0^1(\Omega),\psi\le 0.\)

As before \(a(\Phi,\psi)=a(\psi,\psi)\), and on \(\{\psi<0\}\cap D_s\) we have \(U+\Phi\le M_U-M_U=0\), so \(r(U+\Phi)\le 0\) and \((r(U+\Phi),\psi)_{D_s}\ge 0\). Taking \(v=\psi\) gives \(a(\psi,\psi)\le 0\), hence \(\psi=0\) and \(\Phi\ge-M_U\) a.e.

We can now state the main result of this section: for a truncation level above an explicit threshold, the truncated problem and the original problem have the same solution.

**Theorem 3.6.** _Let Assumption 2.1 and_ (3) _hold, and let_

\(\tau\ge\tau_0:=2Z_\mathrm{max}M_U.\) (27)

_Then the solution_ \(\Phi_\tau\) _of the truncated problem_ (23) _belongs to_ H _and is the unique solution of the original problem_ (15)_. In particular, the solution_ \(\widehat{\Phi}\) _of_ (15) _does not depend on_ \(\tau\ge\tau_0\)_, satisfies_ \(\left\|\widehat{\Phi}\right\|_{0,\infty}\le M_U\)_, and_<tbc>

\(\left\|U+\widehat{\Phi}\right\|_{0,\infty,D_s}\le 2M_U.\) (28)

<tbc>_Proof._ By Theorem 3.5, \(|\Phi_\tau|\le M_U\) a.e. in \(\Omega\), so that

\(|U+\Phi_\tau|\le 2M_U\text{and}Z_\mathrm{max}|U+\Phi_\tau|\le\tau_0\le\tau\text{a.e. in}D_s.\)

By Lemma 3.2(iii), \(\rho_\tau(U+\Phi_\tau)=\rho(U+\Phi_\tau)\) a.e. in _D<sub>s</sub>_, so \(\Phi_\tau\) satisfies (15); and \(\Phi_\tau\in\mathcal{H}\) because it is bounded. Conversely, let \(\widehat{\Phi}\in\mathcal{H}\) be any solution of (15). By the second part of Theorem 3.5, \(|\widehat{\Phi}|\le M_U\), hence \(\rho(U+\widehat{\Phi})=\rho_\tau(U+\widehat{\Phi})\) and \(\widehat{\Phi}\) solves (23). By the uniqueness in Theorem 3.4, \(\widehat{\Phi}=\Phi_\tau\).

_Remark_ 3.7. Theorem 3.6 gives a second proof of the existence and uniqueness result \[34, Theorem 4.2\] for \(\widehat{\Phi}\). It also explains why the truncation used in practice is harmless. In \[34\] the exponentials are truncated at \(\tau=85\) to avoid overflow in the first Newton iterations, with the argument that the truncation is inactive near the minimizer; by Theorem 3.6, for every \(\tau\ge 2Z_\mathrm{max}\left\|U\right\|_{0,\infty,D_s}\) the truncated problem coincides with the original one. In the discrete problems below we always use the truncated nonlinearity. A code that uses \(\rho_\tau\) as its overflow safeguard computes exactly this discrete solution, and with the truncation the constants in the error estimates depend on \(\tau\) (through \(e^\tau\)) but not on pointwise bounds of discrete solutions. The smallest constants are obtained for \(\tau\) close to \(\tau_0\), which only requires a bound on the potential of the solute in water in the solvent region; this bound is available once \(\Psi\) has been computed. Since \(|Z_i(U+\widehat{\Phi})|\le\tau_0\) by (28), the factor \(e^{\tau_0}\) reflects the actual size of the ionic densities _e_<sup>-_Z<sub>i</sub>u_</sup> and is not caused by the truncation.

Henceforth we fix \(\tau\ge\tau_0\) and denote by \(\widehat{\Phi}=\Phi_\tau\) the unique solution of (15) and (23). For later use we record the consequences of Theorem 3.6 and Lemma 3.2 that

\(0<c(\mathbf{r}):=\rho'_\tau\big(U(\mathbf{r})+\widehat{\Phi}(\mathbf{r})\big)\le C_1(1+2M_U)=:c_\mathrm{max}\text{for a.e.}\mathbf{r}\in D_s.\) (29)

