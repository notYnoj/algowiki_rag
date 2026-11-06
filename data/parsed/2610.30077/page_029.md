### Proof of Theorem 5.1.

After spatial discretisation, (S1)-(S4) form a square linear system for the unknowns \((\phi^{n+1},\mu^{n+1},q^{n+1},r^{n+1})\), whose right-hand side depends on the data from the two previous time levels. A square linear system _A_**x**=**b** has exactly one solution for every **b** if and only if the homogeneous system _A_**x**=**0** has only the trivial solution **x**=**0**, that is, if the kernel of _A_ is trivial. The matrix _A_ is built from the frozen coefficients \(b_\star,c_\star,A_\star,\kappa_\star,G_\star\) and does not depend on the previous-level data. It therefore suffices to consider the homogeneous problem: we show that the scheme with zero previous-level data, \(\phi^n=\phi^{n-1}=q^n=q^{n-1}=r^n=r^{n-1}=0\), has only the trivial solution. This is a property of the linear map defining the scheme, and it implies unique solvability for arbitrary (non-zero) data in an actual simulation.

To distinguish this homogeneous problem from an actual trajectory, we denote its solution by \((\psi,\nu,\chi,\rho)\) instead of \((\phi^{n+1},\mu^{n+1},q^{n+1},r^{n+1})\). For zero previous-level data, the BDF2 operators (7) reduce to \(D_2\psi=3\psi/(2\Delta t)\) and \(D^2\psi=\psi\), and similarly for \(\chi\) and \(\rho\).

_Step 1:_ \(\nabla\psi=0\), \(\chi=0\), \(\rho=0\) _and_ \(\widetilde{\mathcal{D}}=0\). For zero previous-level data, E_<sup>n</sup>_=-_C_<sub>0</sub>, and, using \(\Phi(u,0)=5\|u\|^2\),<tbc>

\(\mathcal{E}^{n+1}+C_0=\frac{5}{4}\big[\gamma\|\nabla\psi\|^2+\|\chi\|^2+2\rho^2\big].\)

<tbc>The identity (12) holds for arbitrary previous-level data, so it holds here as well. Inserting the expressions above (the remainder term in (12) contributes \(\frac{1}{4}[\gamma\|\nabla\psi\|^2+\|\chi\|^2+2\rho^2]\)) gives<tbc>

\(\frac{3}{2}\big[\gamma\|\nabla\psi\|^2+\|\chi\|^2+2\rho^2\big]+\Delta t\widetilde{\mathcal{D}}=0,\)

<tbc>where \(\widetilde{\mathcal{D}}\) is (11) evaluated at \((\nu,\chi)\). Since \(\gamma>0\), and \(\widetilde{\mathcal{D}}\ge 0\) by Assumption 1 (as in Step 5 of the proof of Theorem 4.1), all terms are non-negative. Hence each of them vanishes:

\(\nabla\psi=0,\chi=0,\rho=0,\widetilde{\mathcal{D}}=0.\)

### Step 2: \(\psi=0\).

Since \(\nabla\psi=0\), the function \(\psi\) is constant in space. To determine the constant, we test (S1) with 1. By (6a) with _g_=1, the right-hand side integrates to zero, so \(\int_\Omega D_2\psi=\frac{3}{2\Delta t}\int_\Omega\psi=0\). Thus \(\psi\) has zero mean. A constant function with zero mean on \(\Omega\) vanishes, so \(\psi=0\).

_Step 3:_ \(\nu=0\). With \(\chi=0\), the integrand of \(\widetilde{\mathcal{D}}\) simplifies, because \(\big(b_\star-\frac{c_\star^2}{d_0}\big)+\frac{c_\star^2}{d_0}=b_\star\):

\(\widetilde{\mathcal{D}}=\int_\Omega\big(b_\star-\frac{c_\star^2}{d_0}\big)|\nabla\nu|^2+\frac{1}{d_0}\int_\Omega|c_\star\nabla\nu|^2=\int_\Omega b_\star|\nabla\nu|^2.\)

Since \(\widetilde{\mathcal{D}}=0\) and \(b_\star\ge b_1>0\), we obtain \(\nabla\nu=0\), so \(\nu\) is constant in space. (This is the only place where the additional assumption \(b_\star\ge b_1>0\) is used.) The constant is fixed by (S2): with \(\psi=0\) and \(\rho=0\), it reads \(\nu=-\gamma\Delta\psi+\rho G_\star=0\).

We have shown \(\psi=\nu=\chi=\rho=0\). Thus the homogeneous system has only the trivial solution, and (S1)-(S4) has a unique solution for every \(\Delta t>0\) and for arbitrary data \((\phi^n,q^n,r^n)\) and \((\phi^{n-1},q^{n-1},r^{n-1})\).

## B The manufactured solution used in Section 7.2

The temporal MMS check of Section 7.2 uses the explicit, smooth functions<tbc>

\(\phi_\mathrm{ex}(x,y,t):=0.5+0.15\mathrm{cos}(2\pi x)\mathrm{cos}(2\pi y)e^{-3t},q_\mathrm{ex}(x,y,t):=0.10\mathrm{sin}(2\pi x)\mathrm{sin}(2\pi y)e^{-2t},\)

<tbc>on \(\Omega=(0,1)^2\) at \(\gamma=0.30\), chosen large enough that \(\phi=0.5\) is not spimodally unstable for this low wavenumber, so the forced problem below is not numerically stiff. Neither function solves (1). With \(\mu_\mathrm{ex}:=-\gamma\Delta\phi_\mathrm{ex}+f'(\phi_\mathrm{ex})\), define the forcing pair

\(S_\phi(t):=\partial_t\phi_\mathrm{ex}(t)-\nabla\cdot\big(b(\phi_\mathrm{ex})\nabla\mu_\mathrm{ex}-c(\phi_\mathrm{ex})\nabla(A(\phi_\mathrm{ex})q_\mathrm{ex})\big),\)<br>
\(S_q(t):=\partial_tq_\mathrm{ex}(t)-\big[-\kappa(\phi_\mathrm{ex})q_\mathrm{ex}-A(\phi_\mathrm{ex})\nabla\cdot\big(c(\phi_\mathrm{ex})\nabla\mu_\mathrm{ex}-d_0\nabla(A(\phi_\mathrm{ex})q_\mathrm{ex})\big)+\varepsilon_q\Delta q_\mathrm{ex}\big],\)

