its well-posedness is established in Lemma 4.5 below. We write

\(\delta:=\left\|\Psi-\Psi^*\right\|_{0,2,D_s}=\left\|U-U^*\right\|_{0,2,D_s}\) (42)

for the size of the data perturbation. The nonlinearity in (41) is the truncated one, in accordance with Remark 3.7, and that \(U^*+\Phi_h\) need not be bounded pointwise.

**Lemma 4.5.** _Let Assumption 2.1 and_ (3) _hold,_ \(\tau>0\)_, and let U_<sup>∗</sup> _be as in_ (40)_. Then_ (41) _has a unique solution_ \(\Phi_h\in V_h^0\)_, and_

\(\left\|\Phi_h\right\|\le\epsilon_p^{-1/2}C_P\left\|\rho_\tau(U^*)\right\|_{0,2,D_s}\le C_\Lambda,\) (43)

_where_ \(C_\Lambda\) _depends only on_ \(\tau,\beta,Z_i,\bar{c}_i,\epsilon_p,\Omega\), \(\left\|G\right\|_{H^1(D_s)}\) _and_ \(\Lambda\)_, but not on h._

_Proof._ The functional<tbc>

\(J_\tau^*(v):=\frac{1}{2}a(v,v)+\int_{D_s}P_\tau(U^*+v)\mathrm{d}\mathbf{r},v\in V_h^0,\)

<tbc>is well defined on \(V_h^0\) because \(U^*\in L^6(D_s)\) (recall that \(G\in C^\infty(\overline{D_s})\) and \(\Psi^*\in H^1(\Omega)\unknown\rightarrow L^6(\Omega)\)) and \(v\in L^6(\Omega)\), and the argument of Theorem 3.4 carries over to the finite-dimensional space \(V_h^0\): \(J_\tau^*\) is strictly convex, continuous and coercive, so it has a unique minimizer, which is the unique solution of (41). The first inequality in (43) is proved exactly as (25). For the second, (21) gives<tbc>

\(\left\|\rho_\tau(U^*)\right\|_{0,2,D_s}\le C_0\left\|(1+|U^*|)^2\right\|_{0,2,D_s}=C_0\left\|1+|U^*|\right\|_{0,4,D_s}^2\le C_0\big(|D_s|^{1/4}+\left\|U^*\right\|_{0,4,D_s}\big)^2,\)

<tbc>and

\(\left\|U^*\right\|_{0,4,D_s}\le C\left\|U^*\right\|_{H^1(D_s)}\le C\big(\left\|G\right\|_{H^1(D_s)}+\Lambda\big)\)

by the Sobolev embedding on the Lipschitz domain _D<sub>s</sub>_.

We shall repeatedly use the following elementary consequence of the mean value theorem and Lemma 3.2(ii): for all \(\xi_1,\xi_2\in\mathbb{R}\),

\(|\rho_\tau(\xi_1)-\rho_\tau(\xi_2)|\le C_1\big(1+|\xi_1|+|\xi_1-\xi_2|\big)|\xi_1-\xi_2|,\) (44)

which follows from \(\rho_\tau(\xi_1)-\rho_\tau(\xi_2)=\rho'_\tau(\zeta)(\xi_1-\xi_2)\) with \(\zeta\) between \(\xi_1\) and \(\xi_2\), so that \(|\zeta|\le|\xi_1|+|\xi_1-\xi_2|\).

## 4.4 Energy-norm error estimate

**Theorem 4.6.** _Let Assumptions 2.1 and 4.1(i) hold, let_ (3) _and_ (27) _hold, and let U_<sup>∗</sup> _be as in_ (40)_. There exist h_<sub>0</sub>_\>_0 _and C\>_0_, depending only on_ \(\tau,\beta,Z_i,\bar{c}_i,\epsilon_p,\epsilon_s,\Omega,M_U,\Lambda\), \(\left\|G\right\|_{H^1(D_s)}\), \(\left\|\Psi\right\|_{H^1(\Omega)}\) _and_ \(\left\|\widehat{\Phi}\right\|_{H^s(D_p\cup D_s)}\)_, such that for all_ \(h\le h_0\) _the solution_ \(\Phi_h\) _of_ (41) _satisfies_

\(\left\|\widehat{\Phi}-\Phi_h\right\|\le C\big(h^{s-1}+\delta\big),\) (45)

_where_ \(\delta\) _is defined in_ (42).

