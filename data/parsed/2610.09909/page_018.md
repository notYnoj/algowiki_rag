## 4. _A posteriori_ error analysis

### 4.1. Reliability and efficiency of the error indicator.

A fundamental advantage of the PHT-spline space is its global _C_<sup>1</sup>-continuity. This higher-order smoothness circumvents the need for interface jump residuals--which typically complicate the analysis of standard _C_<sup>0</sup> finite element methods--and enables the formulation of an _a posteriori_ error indicator based exclusively on the interior _L_<sup>2</sup>-residual.

**Proposition 4.1** (Reliability and efficiency of the _a posteriori_ indicator)**.** _Let_ \(u_h\in S_h\) _denote the discrete solution, and let_ \(\tilde{u}\in H^{k+1}(\widetilde{\Omega}_h)\) _be the exact extension of the true solution u, satisfying_ \(-\Delta\tilde{u}=f+r\) _in_ \(\Omega_h\) _with the perturbation_ \(r\equiv 0\) _in the physical domain_ \(\Omega\)_. We define the local and global_ a posteriori _error indicators by_<tbc>

\(\eta_T:=\|\Delta u_h+f\|_{L^2(T)}\forall T\in\mathcal{T}_h,\eta:=\left(\sum_{T\in\mathcal{T}_h}\eta_T^2\right)^{1/2},\) (4.1)

<tbc>_respectively. Then, the error_ \(e_h:=\tilde{u}-u_h\) _satisfies the reliability bound_<tbc>

\(\|\Delta e_h\|_{L^2(\Omega_h)}\le\eta+\|r\|_{L^2(\Omega_h)},\) (4.2)

<tbc>_and the efficiency bound_<tbc>

\(\eta\le\|\Delta e_h\|_{L^2(\Omega_h)}+\|r\|_{L^2(\Omega_h)}.\) (4.3)

<tbc>_Proof._ Recalling the strong form \(f=-\Delta\tilde{u}-r\) in \(\Omega_h\) and substituting this relation into the definition of the global indicator \(\eta\), we obtain

\(\eta=\|\Delta u_h+f\|_{L^2(\Omega_h)}\)<br>
\(=\|\Delta u_h-\Delta\tilde{u}-r\|_{L^2(\Omega_h)}\)<br>
\(=\|-\Delta e_h-r\|_{L^2(\Omega_h)}=\|\Delta e_h+r\|_{L^2(\Omega_h)}.\)

Applying the triangle inequality directly yields the reliability upper bound (4.2):<tbc>

\(\|\Delta e_h\|_{L^2(\Omega_h)}=\|(\Delta e_h+r)-r\|_{L^2(\Omega_h)}\le\|\Delta e_h+r\|_{L^2(\Omega_h)}+\|r\|_{L^2(\Omega_h)}=\eta+\|r\|_{L^2(\Omega_h)}.\)

<tbc>A completely analogous application of the triangle inequality to \(\eta=\|\Delta e_h+r\|_{L^2(\Omega_h)}\) establishes the efficiency lower bound (4.3):

\(\eta\le\|\Delta e_h\|_{L^2(\Omega_h)}+\|r\|_{L^2(\Omega_h)},\)

which completes the proof. □

**Remark 4.2.** _Proposition 4.1 shows that the indicator_ \(\eta\) _provides two-sided bounds for the Laplacian error up to the perturbation term_ \(\|r\|_{L^2(\Omega_h)}\)_. Indeed,_<tbc>

\(\big|\eta-\|\Delta e_h\|_{L^2(\Omega_h)}\big|\le\|r\|_{L^2(\Omega_h)}.\)

<tbc>_Using_ \(\|\Delta e_h\|_{L^2(\Omega_h)}\le\sqrt{d}|e_h|_{H^2(\Omega_h)}\) _together with_ (3.36) _and_ (3.24)_, we obtain_

\(\eta\le\|\Delta e_h\|_{L^2(\Omega_h)}+\|r\|_{L^2(\Omega_h)}\le Ch^{k-1}.\)

_Thus, the indicator_ \(\eta\) _decays with the optimal-order upper bound_ O(_h_<sup>_k_-1</sup>).

### 4.2. Adaptive algorithm.

Based on the _a posteriori_ error indicator defined above, we implement a standard adaptive iteration loop of the form \(\text{\textbf{SOLVE}}\rightarrow\text{\textbf{ESTIMATE}}\rightarrow\text{\textbf{MARK}}\rightarrow\text{\textbf{REFINE}}[1,12,16]\) to efficiently capture local features of the solution on the hierarchical T-mesh. The detailed procedure is outlined in Algorithm 1.

Starting from an initial uniform background mesh \(\hat{\mathcal{T}}_h^{(0)}\), the algorithm iterates until the error tolerance TOL is met. In the **MARK** step, we employ the standard Dörfler marking strategy with a parameter \(\theta\in(0,1)\) to select a minimal subset of elements \(\mathcal{M}^{(\ell)}\) that contribute significantly to the global error \(\eta^{(\ell)}\). In the **REFINE** step, the marked elements undergo a one-to-four (or one-to-eight in 3D) spatial subdivision. Furthermore, recursive refinement is triggered on adjacent cells to strictly enforce the 1-regularity constraint. Finally,

