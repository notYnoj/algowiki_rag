## a. Lifting orbit descent to circuit parameters

Let _m_=dim<sub>R</sub>(g) denote the dimension of the dynamical Lie algebra. The construction from Section VI provides a smooth local family of parameterized unitaries

\(V(\mathbf{x})=\prod_{\ell=1}^Le^{\vartheta_\ell(\mathbf{x})a_{j_\ell}},L\le\mathcal{T}_\mathfrak{g},\) (E10)

defined on a neighborhood of \(\mathbf{0}\in\mathbb{R}^m\), where the \(a_{j_\ell}\) are skew-Hermitian control generators and

\(V(\mathbf{0})=I,(dV)_\mathbf{0}(\mathbb{R}^m)=\mathfrak{g}.\) (E11)

Fix a circuit \(U(\unknown_p)\) of depth _p_, and set

\(\rho_p:=U(\unknown_p)\rho U^\dagger(\unknown_p).\)

For the augmented circuit

\(U(\mathbf{x},\unknown_p)=V(\mathbf{x})U(\unknown_p),\) (E12)

the loss function becomes

\(\ell_{(\mathbf{x},\unknown_p)}(\rho,H_P)=\mathrm{Tr}\big[V(\mathbf{x})\rho_pV^\dagger(\mathbf{x})H_P\big].\) (E13)

In particular,

\(\ell_{(\mathbf{0},\unknown_p)}(\rho,H_P)=\ell_{\unknown_p}(\rho,H_P),\) (E14)

demonstrating that appending the identity block initially preserves the state and energy.

_Proof of Theorem IX.1._ Consider the state endpoint map \(\Psi_p:\mathbb{R}^m\rightarrow\mathcal{O}_\rho\) given by

\(\Psi_p(\mathbf{x})=V(\mathbf{x})\rho_pV^\dagger(\mathbf{x}).\)

By virtue of (E11), its differential at the origin satisfies

\((d\Psi_p)_\mathbf{0}(\mathbb{R}^m)=[\mathfrak{g},\rho_p]=T_{\rho_p}\mathcal{O}_\rho.\) (E15)

Thus, \(\Psi_p\) is a local submersion onto the unitary orbit \(\mathcal{O}_\rho\) at **_x_=0**. By \[7, Proposition 9.6\], first- and second-order criticality of the parameterized loss \(\ell_{(\mathbf{x},\unknown_p)}\) at **_x_=0** is strictly equivalent to that of the orbit loss at \(\rho_p\).

Since Proposition E.1 asserts that all non global minima orbit critical points are saddle points or local maxima (excluding suboptimal second-order local minima), \(\rho_p\) cannot be second-order optimal unless \(\ell_{\unknown_p}(\rho,H_P)=\lambda_\mathrm{min}(H_P)\). Thus either the parameter gradient is nonzero or the parameter Hessian has a negative direction. In either case, arbitrarily small parameter changes strictly decrease the loss.

