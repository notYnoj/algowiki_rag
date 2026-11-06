## 5 The two-grid algorithm and its analysis

### 5.1 The algorithm

Let T_<sub>H</sub>_ be a coarse mesh with mesh size _H_ from the family introduced in Section 4, and let T_<sub>h</sub>_, _h\<H_, be obtained from T_<sub>H</sub>_ by (possibly repeated) uniform refinement that keeps it in the family (e.g., red refinement of tetrahedra), so that T_<sub>h</sub>_ is fitted to \(\Gamma\) and the finite element spaces are nested, \(V_H^0\subset V_h^0\). The two-grid solution decomposition scheme is described in Algorithm 1. In Step 3 the datum \(\Psi^\sharp\) used to assemble the coarse nonlinear problem may be either the fine-mesh approximation \(\Psi_h\) or a coarse-mesh approximation \(\Psi_H\in V_H\) defined by (34) on T_<sub>H</sub>_; both choices are covered by the analysis below (see Remark 5.5 for a discussion).

**Algorithm 1** Two-grid PBE solution decomposition scheme

**Require:** atomic positions **r**_<sub>j</sub>_ and charges _z<sub>j</sub>_; ionic species \((Z_i,\bar{c}_i)\); permittivities \(\epsilon_p,\epsilon_s\); boundary value \(\hat{g}\); truncation level \(\tau\); meshes T_<sub>H</sub>_, T_<sub>h</sub>_.

1: Compute _G_ and \(\nabla G\) from (6).

2: **(Fine linear solve.)** Find \(\Psi_h\in V_h\) with \(\Psi_h=I_h^\partial(\hat{g}-G)\) on \(\partial\Omega\) satisfying (34); set \(U_h:=G+\Psi_h\). Choose \(\Psi^\sharp\in\{\Psi_h,\Psi_H\}\), where \(\Psi_H\in V_H\) is computed by (34) on T_<sub>H</sub>_ if this variant is chosen, and set \(U^\sharp:=G+\Psi^\sharp\).

3: **(Coarse nonlinear solve.)** Find \(\Phi_H\in V_H^0\) such that

\(a(\Phi_H,v)+\left(\rho_\tau(U^\sharp+\Phi_H),v\right)_{D_s}=0\forall v\in V_H^0.\) (57)

4: **(Fine linear solve: one Newton correction.)** Find \(\Phi_h^\mathrm{tg}\in V_h^0\) such that for all \(v\in V_h^0\)

\(a(\Phi_h^\mathrm{tg},v)+\left(\rho'_\tau(U_h+\Phi_H)\Phi_h^\mathrm{tg},v\right)_{D_s}=\left(\rho'_\tau(U_h+\Phi_H)\Phi_H-\rho_\tau(U_h+\Phi_H),v\right)_{D_s}.\) (58)

**Ensure:** \(u_h^\mathrm{tg}:=G+\Psi_h+\Phi_h^\mathrm{tg}\).

The coarse problem (57) is problem (41) on T_<sub>H</sub>_ with datum \(\Psi^*=\Psi^\sharp\). It has a unique solution by Lemma 4.5 and can be solved, for example, by the modified Newton minimization scheme of \[34, Algorithm 2\]; for the truncated nonlinearity this is a descent method for the strictly convex functional \(J_\tau^*\) of Lemma 4.5 with \(U^*=U^\sharp\) and, with a suitable line search, converges from any initial guess. Writing \(\Phi_h^\mathrm{tg}=\Phi_H+d_h\), the fine problem (58) is equivalent to the Newton correction equation

\(a(d_h,v)+\left(\rho'_\tau(U_h+\Phi_H)d_h,v\right)_{D_s}=-\left[a(\Phi_H,v)+\left(\rho_\tau(U_h+\Phi_H),v\right)_{D_s}\right]\forall v\in V_h^0,\) (59)

whose right-hand side is the residual of the coarse solution in the fine problem (41) with _U_<sup>∗</sup>=_U<sub>h</sub>_. The bilinear form \(B_h(v,w):=a(v,w)+(\rho'_\tau(U_h+\Phi_H)v,w)_{D_s}\) on the left of (59) is symmetric and, since \(\rho'_\tau>0\), it satisfies

\(|||v|||^2\le B_h(v,v)\le\left(1+C_1\epsilon_p^{-1}C_P^2\big(1+\|U_h+\Phi_H\|_{0,\infty,D_s}\big)\right)|||v|||^2\forall v\in V_h^0,\) (60)

where the upper bound uses (21) and the fact that \(U_h+\Phi_H\) is bounded on _D<sub>s</sub>_ (_G_ is smooth on <o>_D<sub>s</sub>_</o> and \(\Psi_h+\Phi_H\) is piecewise linear). Thus only two symmetric positive definite systems are solved on the fine mesh, one for \(\Psi_h\) and one for _d<sub>h</sub>_, and both can be solved by preconditioned conjugate gradients with multilevel preconditioners that are robust with respect to the jump of \(\epsilon\) \[40\]. The coefficient \(\rho'_\tau(U_h+\Phi_H)\) in (58) is bounded on each element but may be large where the truncation<tbc>

