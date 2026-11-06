manufactured solution. The test isolates the nonlinear component \(\widehat{\Phi}\); the linear component \(\Psi\) is not computed, and _U_ is prescribed analytically. Since the nonlinear term is integrated with the vertex quadrature rule (see below), only the nodal values of _U_ enter the discrete problems, i.e., the discrete problem on each mesh automatically uses the interpolated datum _I<sub>h</sub>U_ (resp. _I<sub>H</sub>U_); the data perturbation \(\delta=\|U-I_hU\|_{0,2,D_s}=O(h^2)\) of (42) is therefore present implicitly, and the two variants of Step 3 of Algorithm 1 coincide. All experiments were run on an Apple Mac Studio (Apple M4 Max, 16 cores, 64 GB), the code is available from the authors.

## 6.1 Setting

Let \(\Omega=(-1,1)^3\), \(D_p=(-\frac{1}{2},\frac{1}{2})^3\), \(\epsilon_p=2\), \(\epsilon_s=80\), and consider a symmetric 1:1 electrolyte with \(\kappa^2=40\) in _D<sub>s</sub>_. We solve<tbc>

\(-\nabla\cdot(\epsilon\nabla\Phi)+\kappa^2\chi_{D_s}sinh(U+\Phi)=f\text{in}\Omega,\Phi=0\text{on}\partial\Omega,\) (69)

<tbc>with the homogeneous interface conditions of (8), where the source _f_ is chosen so that the exact solution (denoted by \(\Phi\) in this section) is

\(\Phi(x,y,z)=\frac{1}{4}q(x)q(y)q(z),q(x)=cos(2\pi x)-1,\)

and the datum is \(U(x,y,z)=2cos(\pi x)cos(\pi y)cos(\pi z)\), so that _M<sub>U</sub>_=2. Since \(q'(\pm\frac{1}{2})=0\), the normal derivative of \(\Phi\) vanishes on \(\Gamma\) and both interface conditions hold; \(f=-\epsilon\Delta\Phi+\kappa^2\chi_{D_s}sinh(U+\Phi)\) is piecewise smooth and discontinuous across \(\Gamma\). The presence of _f_ does not affect the error analysis except for an additional linear term on the right-hand sides; it does, however, invalidate the a priori bound of Theorem 3.5, see Section 6.5. The manufactured solution is smooth, so _s_=2. For the dual problem (30) on the cubic interface with \(\epsilon_s/\epsilon_p=40\) we cannot expect \(\sigma=2\) (cf. Remark 4.2), so Corollary 5.3 guarantees full accuracy only for \(H\le Ch^\gamma\) with some \(\gamma\in(2/5,1/2)\); the observed _L_<sup>2</sup> rates below are nevertheless consistent with _t_=1.

The domain is partitioned into _N_<sup>3</sup> cubes of side _h_=2_/N_, each split into six Kuhn tetrahedra (we identify _h_ with the cube side, which is proportional to the element diameter); for _N_ divisible by 4 the mesh is fitted to \(\Gamma\), and the meshes for _N_ and 2_N_ are nested, so that \(V_H^0\subset V_h^0\) and the prolongation of \(\Phi_H\) to the fine mesh in Step 4 of Algorithm 1 is exact. The nonlinear term and the load are integrated with the vertex quadrature rule (mass lumping), which makes the Newton Jacobian equal to the stiffness matrix plus a diagonal matrix. The truncated functions \(sinh_\tau,cosh_\tau\) of (22) are used with \(\tau=85\) unless stated otherwise; by Theorem 3.6 this does not alter the solution (see also Section 6.5). All linear systems on meshes with more than \(2\cdot 10^4\) unknowns are solved by the conjugate gradient method with a smoothed-aggregation algebraic multigrid preconditioner to a relative residual of 10<sup>-12</sup>; smaller systems are solved directly. Newton’s method (undamped) on a given mesh is started from zero and stopped when the Euclidean norm of the residual is below 10<sup>-12</sup> relative to that of the load; this applies to the fine-mesh reference solutions, to the coarse solves in Algorithm 1, and to the runs of Section 6.5. Errors are computed with the four-point degree-two quadrature rule and are reported relative to the exact solution: for a function _v_ we write

\(e_E(v):=\frac{|||v|||}{|||\Phi|||},e_2(v):=\frac{\|v\|_{0,2}}{\|\Phi\|_{0,2}},e_4(v):=\frac{\|v\|_{0,4}}{\|\Phi\|_{0,4}},\)

with |||\(\Phi|||=68.41\), |||\(\Phi|||_{0,2}=1.299\) and |||\(\Phi|||_{0,4}=1.272\). Differences of discrete solutions, such as \(\Phi_h-\Phi_h^\text{tg}\), are scaled by the same norms of \(\Phi\).

