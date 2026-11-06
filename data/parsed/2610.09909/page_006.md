<tbc>_where_ \(D_h^2\) _denotes the elementwise second derivative._<tbc>

(P3) _The cut-to-interior proximity condition holds: there exists c<sub>b</sub>\>_0 _such that for every_ \(T\in\mathcal{T}_h^\Gamma\)_, there exists an interior element_ \(K\in\mathcal{T}_h^\mathrm{in}\) _satisfying_ \(\mathrm{dist}(T,K)\le c_bh_T\).<tbc>

(P4) _The hierarchical mesh is 1-regular, meaning that the refinement levels of adjacent cells differ by at most one, ensuring that the mesh sizes of neighboring cells are comparable._

**Remark 2.2.** Property (P2) is a standard requirement in the context of unfitted finite element methods, which is naturally satisfied when the _k_-th degree PHT-spline function \(\phi_h\in V_h\) is defined as the global spline interpolation of a sufficiently smooth level-set function \(\phi\). Furthermore, for polynomial degrees \(k\ge 3\), the \(L^\infty\)-norm of \(\nabla\phi_h\) is uniformly bounded as a consequence of (P2) and the standard inverse inequalities for splines.

**Remark 2.3.** Properties (P1)-(P2) ensure that the discrete interface \(\Gamma_h\) provides a high- order approximation of \(\Gamma\) while maintaining its non-degeneracy. Property (P3) serves as a standard geometric assumption, ensuring that every cut cell is sufficiently close to the interior to facilitate the stable extension of the solution. Furthermore, (P4) is critical for guaranteeing that the number of elements _N_ in a face-adjacent path from a cut cell to an interior cell remains uniformly bounded, independent of the local refinement level. This property is essential for establishing the uniform stability of the ghost penalty terms across non-conforming mesh interfaces.

## 2.2. A simple least-squares UnCut FEM using PHT-splines.

In this subsection, we present the proposed numerical scheme and state the main theoretical results. Throughout this paper, the notation \(A\lesssim B\) denotes \(A\le CB\) with a positive constant _C_ independent of the mesh size, while _A≈B_ indicates that \(A\lesssim B\) and \(B\lesssim A\) simultaneously. We utilize \((\cdot,\cdot)_{L^2(D)}\) and \((\cdot,\cdot)_{H^1(D)}\) to denote the standard _L_<sup>2</sup> and _H_<sup>1</sup> inner products over a domain _D_.

Based on the spline space _V<sub>h</sub>_ and the approximate level-set function \(\phi_h\), we define the finite element space as \(S_h:=\{\phi_hv_h:v_h\in V_h\}\). Since the functions in _S<sub>h</sub>_ are globally _C_<sup>1</sup>-continuous, their zero-th and first-order normal jumps across any internal face are intrinsically zero. Thus, the jump penalty term only involves higher-order derivatives from _j_=2 to 2_k_, defined as

\(j_h(u_h,v_h):=\sum_{j=2}^{2k}\sum_{F\in\mathcal{F}_h^\Gamma} h_F^{2j-3}\int_F\left[\left[\partial_n^ju_h\right]\right]\left[\left[\partial_n^jv_h\right]\right],\forall(u_h,v_h)\in S_h\times S_h,\) (2.6)

where _h<sub>F</sub>_:=min(_h_<sub>_T_<sup>+</sup></sub>_,h_<sub>_T_<sup>-</sup></sub>) denotes the characteristic mesh size associated with the interior face \(F=T^+\cap T^-\).

It is important to emphasize that all computations in the proposed scheme (1.3) are carried out directly on the background mesh T_<sub>h</sub>_. This approach circumvents the need for complex numerical integration over geometrically curved cut elements induced by the intersection of the physical boundary with the Cartesian grid. Consequently, the scheme relies solely on standard element-wise quadrature rules, significantly simplifying the implementation and the computational pipeline.

**Theorem 2.4** (_H_<sup>1</sup>-error estimate)**.** _Under Assumption 2.1, assuming_ \(\Omega\subset\Omega_h\)_, let_ \(f\in H^{k-1}(\Omega_h)\) _and let_ \(\tilde{u}\in H^{k+1}(\widetilde{\Omega}_h)\) _be the extension of the exact solution u, satisfying_ \(\tilde{u}|_\Omega=u\) _and_ \(\left\|\tilde{u}\right\|_{H^{k+1}(\widetilde{\Omega}_h)}\le C\left\|u\right\|_{H^{k+1}(\Omega)}\)_. Then the numerical scheme in_ (1.3) _admits a unique solution_ \(u_h\in S_h\)_, and the following error estimate holds:_

\(\left\|\tilde{u}-u_h\right\|_{H^1(\Omega_h)}\le Ch^k\left\|f\right\|_{H^{k-1}(\Omega_h)}.\) (2.7)

Although the hierarchical T-mesh framework permits local refinement, the _a_ priori analysis in Section 3 is carried out under the additional assumption that the active meshes are globally comparable, namely, \(h_M/h_m\le C\) with a constant independent of _h_. Accordingly, we use the

