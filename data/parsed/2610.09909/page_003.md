<tbc>while entirely circumventing the need for dual variables or mixed systems. To illustrate this approach, we consider the Poisson problem on a domain \(\overline{\Omega}\subset(0,1)^d\) defined by a _C_<sup>_k_+1</sup> level-set function \(\phi:[0,1]^d\rightarrow\mathbb{R}\), with \(d\in\{2,3\}\), i.e.,

\(\left\{\begin{array}{ c c }
-\Delta u=f & \text{in}\Omega=\{\mathbf{x}\in(0,1)^d:\phi(\mathbf{x})<0\}, \\
u=0 & \text{on}\partial\Omega=\{\mathbf{x}\in(0,1)^d:\phi(\mathbf{x})=0\}.
\end{array}\right.\) (1.1)

Specifically, we consider a background hierarchical T-mesh T_<sub>h</sub>_ defined over a computational domain \(\Omega_h\) such that<tbc>

\(\Omega\subset\Omega_h\subset[0,1]^d,\text{dist}(\partial\Omega_h,\partial\Omega)=O(h),\)

<tbc>where _h_ denotes the mesh size. The approximation space is then constructed as<tbc>

\(S_h=\{w_h=\phi_hv_h:v_h\in V_h\},\)

<tbc>where _V<sub>h</sub>_ is the discrete spline space defined in (2.2), and \(\phi_h\in V_h\) is a _k_-th degree PHT-spline approximation of \(\phi\) such that

\(\|\phi-\phi_h\|_{L^2(\Omega_h)}\le Ch^{k+1},\|\phi-\phi_h\|_{H^1(\Omega_h)}\le Ch^k,\)

for a constant _C\>_0 (e.g., \(\phi_h\) may be chosen as the global spline interpolant or the _L_<sup>2</sup>- projection of \(\phi\)). By construction, every function in _S<sub>h</sub>_ vanishes on the discrete interface \(\Gamma_h=\{\phi_h=0\}\). Thus, the homogeneous Dirichlet condition is imposed exactly on \(\Gamma_h\) and only approximately on the physical boundary \(\Gamma=\partial\Omega\).

We define the numerical solution _u<sub>h</sub>_ to problem (1.1) as the minimizer of the following functional:

\(u_h=argmin_{w_h\in S_h}\left(\|\Delta w_h+f\|_{L^2(\Omega_h)}^2+j_h(w_h,w_h)\right),\) (1.2)

where \(j_h(\cdot,\cdot)\) is a jump-type stabilization term defined in (2.6). For simplicity, _f_ is understood as a fixed bounded extension to \(\widehat{\Omega}\), still denoted by _f_. This quadratic minimization problem is equivalent to the following weak formulation: find \(u_h\in S_h\) such that

\((\Delta u_h,\Delta v_h)_{L^2(\Omega_h)}+j_h(u_h,v_h)=-(f,\Delta v_h)_{L^2(\Omega_h)}\forall v_h\in S_h.\) (1.3)

This formulation is used for practical implementation. However, the optimal-order _H_<sup>1</sup> convergence of this scheme--based on minimizing an _L_<sup>2</sup>-residual over a _C_<sup>1</sup> finite element space-- is not immediate and requires careful analysis.

The main contributions of this paper are threefold:

\(\bullet\) _tion:_ We introduce a novel unfitted finite element method in which no numerical integration over curved boundaries or cut subregions of boundary elements is required. All computations are performed on the _entire_ background mesh using standard element-wise quadrature. This is achieved without introducing dual formulations or auxiliary unknowns; instead, we exploit _C_<sup>1</sup> trial spaces constructed via PHT-splines, leading to a method that is both simple to implement and computationally efficient.<tbc>

\(\bullet\) _Theory:_ We establish a rigorous error analysis for the proposed method. In particular, we prove existence and uniqueness of the discrete solution and derive optimal- order error estimates in the _H_<sup>1</sup> norm. This is nontrivial since the formulation is based on minimizing the _L_<sup>2</sup> residual rather than directly enforcing an _H_<sup>1</sup>-coercive variational structure.<tbc>

\(\bullet\) _Adaptivity:_ PHT-splines are defined on hierarchical T-meshes that admit T-junctions, enabling efficient local _h_-refinement via a simple _cross-insertion_ strategy. Leveraging this flexibility, we introduce a residual-based _a posteriori_ error indicator for each cell \(T\in\mathcal{T}_h\),<tbc>

<tbc>\(\eta_T:=\|\Delta u_h+f\|_{L^2(T)},\)<tbc>

