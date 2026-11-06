## 1. The loss landscape on the reachable orbit

**Proposition E.1** (Absence of suboptimal orbit minima)**.** Assume that the adjoint orbit \(\mathcal{O}_\rho\) of a pure-state projector \(\rho\) (see (E1)) contains a projector \(|\phi\rangle\langle\phi|\) onto a normalized ground state of _H<sub>P</sub>_:

\(\mathrm{min}_{A\in\mathcal{O}_\rho} h(A)=\langle\phi|H_P|\phi\rangle=\lambda_\mathrm{min}(H_P).\) (E4)

Then _h_ has no suboptimal local minima on \(\mathcal{O}_\rho\). Specifically:

(i) Every local minimum \(A\in\mathcal{O}_\rho\) is a global minimum, corresponding to a rank-one projector onto a ground state of _H<sub>P</sub>_ with \(h(A)=\lambda_\mathrm{min}(H_P)\).<tbc>

(ii) Every critical point \(A\in\mathcal{O}_\rho\) with \(h(A)>\lambda_\mathrm{min}(H_P)\) possesses a tangent direction \(Y\in T_A\mathcal{O}_\rho\) of strictly negative second variation:<tbc>

\(\mathrm{Hess}(h|_{\mathcal{O}_\rho})_A(Y,Y)<0.\) (E5)

<tbc>_Proof of Proposition E.1._ Let h=_i_g denote the Hermitian form of the dynamical Lie algebra, and let proj<sub>h</sub> be the Hilbert-Schmidt orthogonal projection onto h. Define the compact connected adjoint orbit<tbc>

\(\mathcal{A}:=\mathrm{Ad}_G\big(\mathrm{proj}_\mathfrak{h}\rho\big)\subset\mathfrak{h}.\)

<tbc>By _G_-equivariance of proj<sub>h</sub> and inclusion of stabilizers \(G_\rho\subseteq G_{\mathrm{proj}_\mathfrak{h}}_\rho\), the map<tbc>

\(q:\mathcal{O}_\rho\longrightarrow\mathcal{A},q(A)=\mathrm{proj}_\mathfrak{h}A,\) (E6)

<tbc>is a well-defined surjective submersion. Because \(H_P\in\mathfrak{h}\), the energy functional factors through _q_ as _h(A_)=_f(q(A_)), where

\(f:\mathcal{A}\longrightarrow\mathbb{R},f(M)=\mathrm{Tr}(MH_P).\) (E7)

The function _f_ is the component of the moment map for the Hamiltonian _G_-action on the orbit A along the line spanned by \(H_P\in\mathfrak{h}\). By \[3, Lemma 2.2\], any such moment-map component is a Morse-Bott function whose critical manifolds all have even Morse indices. Since critical manifolds of index zero correspond to local minima and distinct sublevel set components can merge only at critical manifolds of index one (which are absent here), _f_ possesses a unique local-minimum connected component on A, which is necessarily the global minimum set \[3, Lemma 2.1\]. Because all Morse-Bott indices of _f_ are even, any critical point lying outside this global minimum set cannot have index zero and must instead have index \(\lambda\ge 2\), meaning the Hessian has at least two negative eigenvalues. Consequently, every non-global critical point \(M\in\mathcal{A}\) admits a tangent direction \(Z\in T_M\mathcal{A}\) such that Hess(_f)<sub>M</sub>(Z,Z)\<_0.

As _q_ is a smooth submersion, its differential \(dq_A:T_A\mathcal{O}_\rho\rightarrow T_{q(A)}\mathcal{A}\) is surjective at every point \(A\in\mathcal{O}_\rho\). Pullback by a submersion preserves local minima and critical points \[7, Proposition 9.6\]. If \(A\in\mathcal{O}_\rho\) is a critical point of _h_ with \(h(A)>\lambda_\mathrm{min}(H_P)\), then _q(A_) is a non-global critical point of _f_. Choosing \(Y\in T_A\mathcal{O}_\rho\) such that \(dq_A(Y)=Z\in T_{q(A)}\mathcal{A}\), the second-order chain rule at a critical point (_df_<sub>_q(A_)</sub>=0) yields

\(\mathrm{Hess}(h|_{\mathcal{O}_\rho})_A(Y,Y)=\mathrm{Hess}(f)_{q(A)}(Z,Z)<0.\)

Finally, assumption (E4) identifies the global minimum value on \(\mathcal{O}_\rho\) with \(\lambda_\mathrm{min}(H_P)\), completing the proof.

At a noncritical orbit point \(\sigma\), an explicit loss function descent generator direction is

\(X_\sigma:=\mathrm{proj}_\mathfrak{g}\big([\sigma,H_P]\big),\) (E8)

where the projection uses the Hilbert-Schmidt inner product \(\langle X,Y\rangle_\mathrm{HS}=-\mathrm{Tr}(XY)\) on skew-Hermitian matrices. For the one-parameter unitary flow \(\sigma(t)=e^{tX_\sigma}\sigma e^{-tX_\sigma}\), the corresponding loss function \(\ell_t(\sigma,H_P)=\mathrm{Tr}(H_P\sigma(t))\) satisfies

\(\left.\frac{d}{dt}\right|_{t=0}\ell_t(\sigma,H_P)=-\|X_\sigma\|_\mathrm{HS}^2<0.\) (E9)

Moreover, \(X_\sigma=0\) if and only if \(\sigma\) is a critical point of the orbit loss under _G_.

