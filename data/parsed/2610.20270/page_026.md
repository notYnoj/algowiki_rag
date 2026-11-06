Dually, fix \(\bar{X}\in\mathrm{rb}\mathcal{X}_\star\) and \(F\in\mathcal{R}\) with _F<sub>UU</sub>_=0 and \(\bar{X}F=0\), and consider \(\bar{Z}:=\bar{X}-\sigma S_\mathrm{sc}\in\mathrm{rb}\mathcal{Z}_\star\). In case (c) of (C.7), the _UU_ block of \(\Pi'_+(\bar{Z};F)\) is the positive part of the \(K_\bar{X}K_\bar{X}\) block of _F<sub>UU</sub>_=0, hence zero, and the _VV_ block is zero. The cross block solves \(\bar{X}Y+\sigmaYS_\mathrm{sc}|_V=\bar{X}F_{UV}=0\), so _Y_=0 by Theorem C.3(b). Thus \(\Pi'_+(\bar{Z};F)=0\) and \(\delta'_\sigma(\bar{Z};F)=-\mathsf{P}^\perp F=0\), so \(F\in\mathcal{C}(\bar{Z})=T_{\mathcal{Z}_\star}(\bar{Z})\subseteq\mathcal{D}\), and _F<sub>UU</sub>_=0 gives \(F\in\mathcal{L}\).

## D.6 Examples

_Example_ D.3 (A firmly nonexpansive map with a flat boundary normal). Let \(\psi(s)=s^2/(1+s)\) for \(s\ge 0\) and

\(q(t)=\left\{\begin{array}{ c c }
t+\psi(-t), & t<0, \\
t, & 0\le t\le 1, \\
t-\psi(t-1), & t>1,
\end{array}\right.\)

a nondecreasing 1-Lipschitz function, so _G(t,s_):=(_q(t),_0) is firmly nonexpansive on R<sup>2</sup> with \(\mathrm{Fix}G=[0,1]\times\{0\}\). Along relative-interior normals (0_,h_) the residual has derivative (0,-_h_), so the relative-interior modulus equals one. Yet at the boundary point (1,0) with outward normal (1,0), \((G-\mathrm{Id})(1+t,0)=\left(-t^2/(1+t),0\right)\), so the residual vanishes to first order. Rigidity fails for this map: the implication (i)\(\Rightarrow\)(iv) is a statement about PSD geometry, not about averaged maps.

_Example_ D.4 (Two disks: both identities are needed). Let _p_=4, _U_=span{_e_<sub>1</sub>_,e_<sub>2</sub>}, _V_=span{_e_<sub>3</sub>_,e_<sub>4</sub>}, and

\(\mathrm{min}_{X\unknown 0}\frac{1}{2}(X_{33}+X_{44})\text{s.t.}\mathrm{tr}X=1,X_{33}-X_{44}=0,X_{34}=0,X_{13}-X_{24}=0,X_{14}+X_{23}=0.\)

The constraints are independent, and _I_<sub>4</sub>/4 is strictly feasible. The optimal value is 0. On the primal side, the optimal value forces _X_<sub>33</sub>=_X_<sub>44</sub>=0, so rows 3,4 of a PSD optimal _X_ vanish and \(\mathcal{X}_\star=\left\{\left[\begin{array}{ c }
A \\
0
\end{array}\right]:A\unknown 0,\mathrm{tr}A=1\right\}\). On the dual side, the trace multiplier equals the dual objective, which is zero at optimality. Hence the _UU_ slack block vanishes, and PSD-ness kills the cross block. The two constraints on the _VV_ block allow every traceless change to \(\frac{1}{2}I_2\), so \(\mathcal{S}_\star=\left\{\left[\begin{array}{ c }
0 \\
0
\end{array}\right]:B\unknown 0,\mathrm{tr}B=1\right\}\). Both optimal sets are two-dimensional disks with rank-one boundaries. The anchors are \(X_\mathrm{sc}=\frac{1}{2}P_U\) and \(S_\mathrm{sc}=\frac{1}{2}P_V\), and M, L are the traceless parts of S(_U_) and S(_V_). The cross block of a matrix in N has the form \(\left[\begin{array}{ c }
a \\
-b
\end{array}\right]\) and that of a matrix in R the form \(\left[\begin{array}{ c }
a \\
b
\end{array}\right]\); both are invertible unless zero. If \(E\in\mathcal{N}\) has _E<sub>VV</sub>_=0 and \(E\bar{S}=0\), then \(E_{UV}\bar{S}_{VV}=0\) with \(\bar{S}_{VV}\neq 0\) (trace one), so _E<sub>UV</sub>_=0 and \(E\in\mathcal{M}\); symmetrically \(\bar{X}_{UU}F_{UV}=0\) forces \(F\in\mathcal{L}\). Thus (3.8) holds at every endpoint, including those at which _both_ factors have rank one, and Theorem 3.2 applies for every \(\sigma>0\) although neither optimum is unique.

_Remark_ D.5 (What rigidity does and does not assert). The proof gives positive constants \(\mu_\mathrm{nor},c_\sigma,t_\sigma\) for the fixed instance, but does not identify them with \(\mu_\mathrm{ri}\) or furnish a uniform rate over objectives. The proof of (ii)\(\Rightarrow\)(iii) is not a uniform Taylor expansion across singular endpoints. It exploits exact PSD complementarity of the projection secants. The uniform spectral estimates use the fixed anchor gaps, and no estimate divides by eigenvalues of the moving optima; the remaining constants depend on the fixed problem data and the compact optimal sets. Likewise, by Theorem D.1 every relative-interior derivative \(\delta'_\sigma(\bar{Z};\cdot)\) has kernel exactly D, that is, it is injective on \(\mathcal{D}^\perp\). This pointwise statement is weaker than the uniform bound \(\mu_\mathrm{ri}>0\): the tied-objective instance of Appendix E.5 satisfies Theorem 3.1 and yet has \(\mu_\mathrm{ri}=0\).

