**Theorem 3.4.** _Let Assumption 2.1 and_ (3) _hold and let_ \(\tau>0\)_. Then problem_ (23) _has a unique solution_ \(\Phi_\tau\in H_0^1(\Omega)\)_, which is the unique minimizer of_ \(J_\tau\) _over_ \(H_0^1(\Omega)\)_, and_<tbc>

\(|||\Phi_\tau|||\le\epsilon_p^{-1/2}C_P\left\|\rho_\tau(U)\right\|_{0,2,D_s}\le\epsilon_p^{-1/2}C_PC_0|D_s|^{1/2}(1+M_U)^2.\) (25)

<tbc>_Proof._ The functional \(J_\tau\) is strictly convex on \(H_0^1(\Omega)\), since \(v\mapsto a(v,v)\) is strictly convex and \(P_\tau\) is convex. It is coercive, since \(P_\tau\ge 0\) gives \(J_\tau(v)\ge\frac{1}{2}|||v|||^2\). It is continuous: if \(v_k\rightarrow v\) in \(H_0^1(\Omega)\) then \(v_k\rightarrow v\) in \(L^3(\Omega)\), and since<tbc>

\(0\le P_\tau(U+v)\le C_0\big(1+M_U+|v|\big)^3\text{a.e. in}D_s,\)

<tbc>the Nemytskii operator \(v\mapsto P_\tau(U+v)\) is continuous from _L_<sup>3</sup>(_D<sub>s</sub>_) to _L_<sup>1</sup>(_D<sub>s</sub>_) \[1\]. A continuous convex functional is weakly lower semicontinuous, so \(J_\tau\) has a unique minimizer \(\Phi_\tau\in H_0^1(\Omega)\) \[13, Proposition II.1.2\]. Moreover, \(J_\tau\) is Gâteaux differentiable with

\(J'_\tau(v)w=a(v,w)+\big(\rho_\tau(U+v),w\big)_{D_s},v,w\in H_0^1(\Omega),\)

by dominated convergence, using (21) and \(v,w\in L^6(\Omega)\). Hence the minimizer satisfies (23). Conversely, every solution of (23) is a critical point of the strictly convex functional \(J_\tau\) and therefore its unique minimizer; this proves uniqueness.

For (25), take \(v=\Phi_\tau\) in (23) and subtract \((\rho_\tau(U),\Phi_\tau)_{D_s}\) from both sides:<tbc>

\(|||\Phi_\tau|||^2+\big(\rho_\tau(U+\Phi_\tau)-\rho_\tau(U),\Phi_\tau\big)_{D_s}=-\big(\rho_\tau(U),\Phi_\tau\big)_{D_s}.\)

<tbc>The second term on the left is nonnegative because \(\rho_\tau\) is increasing, so by the Cauchy–Schwarz inequality, (10) and (13),

\(|||\Phi_\tau|||^2\le\left\|\rho_\tau(U)\right\|_{0,2,D_s}\left\|\Phi_\tau\right\|_{0,2}\le\left\|\rho_\tau(U)\right\|_{0,2,D_s}C_P\epsilon_p^{-1/2}|||\Phi_\tau|||,\)

which gives the first inequality in (25); the second follows from (21), since \(|\rho_\tau(U)|\le C_0(1+M_U)^2\) a.e. in _D<sub>s</sub>_.

## 3.3 A priori \(L^\infty\) bounds and equivalence with the original problem

The following bound is the analogue of \[19, Theorem 2.3\] and \[9, Lemma 3.1\] for the problem (23); its proof uses only the monotonicity of \(\rho_\tau\) and the fact that \(\rho_\tau(0)=0\). No smoothness of \(\Gamma\) beyond the Lipschitz property is required.

**Theorem 3.5.** _Let Assumption 2.1 and_ (3) _hold, let_ \(\tau>0\) _and let_ \(\Phi_\tau\) _be the solution of_ (23)_. Then_

\(-M_U\le\Phi_\tau\le M_U\text{\textit{a.e. in}}\Omega.\) (26)

_The same bound holds for every solution_ \(\widehat{\Phi}\in\mathcal{H}\) _of the original problem_ (15).

_Proof._ Let \(\Phi\) denote either \(\Phi_\tau\) or a solution \(\widehat{\Phi}\in\mathcal{H}\) of (15), and let _r_ denote \(\rho_\tau\) or \(\rho\) accordingly; in both cases _r_ is increasing with _r_(0)=0, and \(r(U+\Phi)\in L^2(D_s)\) (for \(\rho_\tau\) this was shown above; for \(\rho\) it follows from \(U\in L^\infty(D_s)\) and the definition of H). Consider<tbc>

\(\phi:=(\Phi-M_U)^+=max\{\Phi-M_U,0\}.\)

<tbc>Since \(\Phi\in H_0^1(\Omega)\) and \(M_U\ge 0\), we have \(\phi\in H_0^1(\Omega)\), \(\phi\ge 0\), and, by \[22, Theorem A.1\] and \[17, Lemma 7.6\],<tbc>

\(\nabla\phi=\nabla\Phi\text{a.e. on}\{\Phi>M_U\},\nabla\phi=0\text{a.e. on}\{\Phi\le M_U\}\)

