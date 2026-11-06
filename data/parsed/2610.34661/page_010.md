## 4 Finite element discretization and error estimates

### 4.1 Meshes, spaces and assumptions

From now on, we assume that \(\Omega\) and _D<sub>p</sub>_ are polyhedral, so that the interface \(\Gamma\) is a closed polyhedral surface, and we let {T_<sub>h</sub>_}<sub>_h\>_0</sub> be a family of conforming, shape-regular and quasi-uniform tetrahedral meshes of \(\Omega\) that are fitted to the interface, i.e., every \(T\in\mathcal{T}_h\) satisfies \(T\subset\overline{D_p}\) or \(T\subset\overline{D_s}\). Quasi-uniformity is used only in Section 5, to relate mesh sizes to numbers of unknowns. Here \(h=\mathrm{max}_{T\in\mathcal{T}_h}\mathrm{diam}(T)\), and without loss of generality \(h\le 1\). All constants _C_ below are independent of the mesh, unless stated otherwise. (If \(\Gamma\) is a curved surface, the results below remain valid for meshes that resolve \(\Gamma\) up to _O(h_<sup>2</sup>), cf. \[10, 24, 19\]; we do not pursue this generalization.) Let

\(V_h:=\{v\in C(\overline{\Omega}):v|_T\in\mathbb{P}_1(T)\forall T\in\mathcal{T}_h\}\subset H^1(\Omega),V_h^0:=V_h\cap H_0^1(\Omega),\)

be the spaces of continuous piecewise linear functions. The restriction to piecewise linear elements is for ease of exposition; see Remark 4.11.

**Assumption 4.1** (regularity)**.** There exist \(s,\sigma\in(1,2]\) such that:

(i) the solutions \(\Psi\) of (14) and \(\widehat{\Phi}\) of (15) satisfy \(\Psi,\widehat{\Phi}\in H^s(D_p\cup D_s)\);<tbc>

(ii) for every measurable _c_ with \(0\le c\le c_\mathrm{max}\) a.e. in _D<sub>s</sub>_, where _c_<sub>max</sub> is the constant in (29), and every \(f\in L^2(\Omega)\), the solution \(w\in H_0^1(\Omega)\) of the linear dual problem<tbc>

\(a(v,w)+(cv,w)_{D_s}=(f,v)\forall v\in H_0^1(\Omega),\) \(\text{(30)}\)

satisfies \(w\in H^\sigma(D_p\cup D_s)\) and<tbc>

\(\left\|w\right\|_{H^\sigma(D_p\cup D_s)}\le C_R\left\|f\right\|_{0,2},\) \(\text{(31)}\)

with _C<sub>R</sub>_ independent of _c_ and _f_ (it may depend on _c_<sub>max</sub>). (The two cases used below are _c_=0, for the linear component \(\Psi\), and \(c=\rho'_\tau(U+\widehat{\Phi})\), for the nonlinear component \(\widehat{\Phi}\).)

We set

\(t:=\mathrm{min}\{s,\sigma\}-1\in(0,1].\) \(\text{(32)}\)

Both parts of Assumption 4.1 are regularity statements for linear elliptic interface problems with piecewise constant diffusion coefficient: \(\widehat{\Phi}\) solves (8) with the bounded right-hand side \(-\rho(U+\widehat{\Phi})\chi_{D_s}\in L^\infty(\Omega)\) (see (28)), \(\Psi\) solves (7) with data determined by _G_ and \(\hat{g}\), and (30) is an interface problem with a bounded nonnegative reaction coefficient, which can be moved to the right-hand side since \(\left\|cw\right\|_{0,2,D_s}\le c_\mathrm{max}C_P\epsilon_p^{-1/2}\left\|w\right\|\le C\left\|f\right\|_{0,2}\) (test (30) with _v=w_ and use \(c\ge 0\)). Assumptions of this type are common in the analysis of interface problems, see \[24, Assumption 4.3\] and \[19, Eq. (3.11)\].

_Remark_ 4.2. The exponents _s_ and \(\sigma\) are determined by the regularity of the linear interface problems (7) and (30), hence by the geometry of \(\Gamma\) and \(\partial\Omega\) and by the ratio \(\epsilon_s/\epsilon_p\). For the polyhedral interfaces of this section one can in general only expect \(s,\sigma\in(1,2)\), with values depending on the edge and vertex angles of \(\Gamma\) and on \(\epsilon_s/\epsilon_p\) \[21, 28\]. If \(\Gamma\) is of class _C_<sup>2</sup>, \(\Omega\) is convex and \(\hat{g}\) is smooth, then \(s=\sigma=2\) \[28, 10, 34\], because \(G\in C^\infty(\overline{D_s})\) and the right-hand side of (8) is bounded. This case lies outside the polyhedral setting assumed here, but it is the relevant one when \(\Gamma\) is smooth and the mesh approximates it with sufficient accuracy \[24\]. Since \(\Psi\) and \(\widehat{\Phi}\) solve interface problems of the same type with smooth or bounded data, their regularity is limited by the same edge and vertex singularities, and one can usually take \(s=\sigma\). The case \(\sigma<s\) occurs when the solution is smoother than in the worst case, for example for the manufactured solution of Section 6.

