<tbc>TAPAS \[39\]) target the smooth-cost traffic program. Each is specialized to one problem class. NLF’s contribution is orthogonal: a _single_ solver, parametrized by one edge law, that spans all of them and inherits graph-class robustness from its multi- grid core. We benchmark against representatives of each family where a runnable one exists (Ipopt \[14\] for congestion, Boykov-Kolmogorov for max flow) and position the rest honestly where it does not (Frank-Wolfe, bush methods; §4.2).

**2. A unified resistor-network formulation.** Let _B_ be the \(n\times m\) signed node- edge incidence matrix of a connected graph (_B<sub>ie</sub>_=+1 if node _i_ is the head of edge _e_, -1 if the tail). Write \(\phi\in\mathbb{R}^n\) for the node potentials, \(d\in\mathbb{R}^n\) for a balanced demand (\(\mathbf{1}^\top d=0\)), and \(\alpha\ge 0\) for a scalar load. Each edge _e_ carries a flow _f<sub>e</sub>_ driven by its potential difference \(g_e=(B^\top\phi)_e=\phi_i-\phi_j\) where _i,j_ are the head and tail of _e_. The physics of the medium is encoded in a smooth, strictly monotone edge law \(\rho_e:\mathbb{R}\rightarrow\mathbb{R}\):

(2.1) \(f_e=\rho_e(g_e).\)

Different choices of \(\rho_e\) give different physical problems ( 2.1): an Ohmic resistor has \(\rho_e(g)=g/R_e\); a saturating capacity has \(\rho_e(g)=c_etanh(g/c_e)\); a BPR congestion link has \(\rho_e\) equal to the inverse of the BPR travel-time function.

_The equilibrium equation._ Flow conservation at every node, \(Bf=\alpha d\), together with the constitutive relation (2.1), gives the _NLF master equation_ (1.1), a nonlinear system in the potentials \(\phi\) alone. This is the equation NLF solves.

**2.1. Primal-dual structure and the co-energy.** Because each \(\rho_e\) is monotone, it is the derivative of a strictly convex _co-energy_ \(\Psi_e\): \(\rho_e=\Psi'_e\). Equation (1.1) is then the stationarity condition \(\nabla_\phi E=0\) of the unconstrained, convex _dual energy_

(2.2) \(E(\phi)=\sum_e\Psi_e\big((B^\top\phi)_e\big)-\alpha d^\top\phi,\)

Solving (1.1) is therefore equivalent to minimizing _E_.

The dual energy _E_ arises naturally from a _primal_ convex program in the flow variables _f_. Each edge has a _primal energy_ (cost) \(\Phi_e(f_e)\), and the primal problem minimizes total cost subject to flow conservation:

(2.3) \(min_f\sum_e\Phi_e(f_e)\text{s.t.}Bf=\alpha d.\)

The Lagrangian of (2.3) introduces node potentials \(\phi\) as multipliers on the conservation constraint; the KKT stationarity condition \(\Phi'_e(f_e)=(B^\top\phi)_e\) says the marginal cost equals the potential difference, i.e. _t<sub>e</sub>(f<sub>e</sub>_)=_g<sub>e</sub>_, or \(f_e=\rho_e(g_e)\). The _marginal cost_ \(t_e=\Phi'_e=\rho_e^{-1}\) is thus the inverse edge law. Substituting into \(Bf=\alpha d\) recovers (1.1).

The relationship between \(\Phi_e\) and \(\Psi_e\) is the _Legendre-Fenchel duality_ \[44\]: \(\Psi_e=\Phi_e^*\), i.e. \(\Psi_e(g)=sup_f\big[g\cdot f-\Phi_e(f)\big]\), and \(\Psi'_e=(\Phi_e^*)'=(\Phi'_e)^{-1}=\rho_e\). In words: the co- energy \(\Psi_e\) is the convex conjugate of the primal cost \(\Phi_e\), and its derivative is the edge law \(\rho_e\). The potentials \(\phi\) are sometimes called _co-potentials_ in the resistor-network literature \[26\] because they live in the dual (potential) space, conjugate to the primal (flow) space. Appendix A derives \(\Phi_e\) and \(\Psi_e\) for each application in  2.1.

_The Newton linearization._ Differentiating (1.1) with respect to \(\phi\) gives the Newton (Jacobian) matrix

(2.4) \(J=Bdiag\big(\rho'(B^\top\phi)\big)B^\top,w_e=\rho'_e(g_e)=\Psi''_e(g_e)=1/t'_e(f_e)\ge 0,\)

a weighted graph Laplacian with _solution-dependent conductances w<sub>e</sub>_. Everything problem-specific lives in \(\rho_e\); the solver never sees anything but \(\rho_e\), \(\rho'_e\), and _J_.

