(Appendix C.2). Writing _J_ for \(J_{\bar{X},\bar{S}}\), the residual derivative is \(\delta'_\sigma(\bar{Z};H)=-\mathsf{P}J(H)-\mathsf{P}^\perp(H-J(H))\), with orthogonal components. Two cones organize everything that follows:

\(\mathcal{C}(\bar{Z}):=\{H\in\mathbb{S}^p:\delta'_\sigma(\bar{Z};H)=0\},T_{\mathcal{Z}_\star}(\bar{Z}):=\text{the tangent cone of}\mathcal{Z}_\star\text{at}\bar{Z}.\) (3.6)

The first is the _stall cone_: the directions along which the residual vanishes to first order, so the first-order dynamics of the splitting method stalls \[KY26b\]; the second collects the directions along the optimal set. Always \(T_{\mathcal{Z}_\star}(\bar{Z})\subseteq\mathcal{C}(\bar{Z})\), since \(\delta_\sigma\) vanishes on Z_<sub>⋆</sub>_; the question is whether the stall cone is _larger_ (Appendix D.7 relates this to the second-order limit dynamics of \[KY26b\]).

## 3.3 The rigidity theorem

Define the relative-interior and full-normal derivative moduli

\(\mu_\mathrm{ri}:=\mathrm{inf}_{\bar{Z}\in\mathrm{ri}\mathcal{Z}_\star H\in\mathcal{D}^\perp,\|H\|_F=1}\|\delta'_\sigma(\bar{Z};H)\|_F,\mu_\mathrm{nor}:=\mathrm{inf}_{\bar{Z}\in\mathcal{Z}_\star H\in N_{\mathcal{Z}_\star}(\bar{Z}),\|H\|_F=1}\|\delta'_\sigma(\bar{Z};H)\|_F.\) (3.7)

**Theorem 3.2** (Two-sided rigidity and exact linearization)**.** _Under Theorem 3.1, the following are equivalent:_

(i) Uniform interior modulus: \(\mu_\mathrm{ri}>0\).<tbc>

(ii) Complementarity rigidity: _the_ primal identity _(left) holds for every_ \(\bar{S}\in\mathrm{rb}\mathcal{S}_\star\) _and the_ dual identity _(right) for every_ \(\bar{X}\in\mathrm{rb}\mathcal{X}_\star\)_, both named after the direction space they test:_<tbc>

\(\{E\in\mathcal{N}:P_VEP_V=0,E\bar{S}=0\}=\mathcal{M},\{F\in\mathcal{R}:P_UFP_U=0,\bar{X}F=0\}=\mathcal{L}.\) \(\text{(3.8)}\)

(iii) Setwise error bound: _there are_ \(c_\sigma,t_\sigma>0\) _with_<tbc>

\(\|\delta_\sigma(Z)\|_F\ge c_\sigma\mathrm{dist}_F(Z,\mathcal{Z}_\star)\text{\textit{whenever}}\mathrm{dist}_F(Z,\mathcal{Z}_\star)\le t_\sigma.\) \(\text{(3.9)}\)

(iv) Uniform normal modulus: \(\mu_\mathrm{nor}>0\).<tbc>

(v) Exact linearization: \(\mathcal{C}(\bar{Z})=T_{\mathcal{Z}_\star}(\bar{Z})\) _for every_ \(\bar{Z}\in\mathrm{rb}\mathcal{Z}_\star\).

_Conditions (ii) and (v) hold automatically at relative-interior factors and endpoints, so requiring them everywhere is equivalent. Whether the conditions hold does not depend on_ \(\sigma\)_; the constants do. No positive lower bound on the nonzero eigenvalues of the varying optimal pair_ \((\bar{X},\bar{S})\) _is imposed._

### What each condition says.

_(i) Stiffness across the flat interior._ Transverse to the optimal set, the residual responds at first order, with a lower bound \(\mu_\mathrm{ri}\) that is uniform over the interior endpoints, however close they sit to the singular boundary. This is the verifiable condition. Interior endpoints are nonsingular matrices, where the residual is real-analytic with the explicit linear derivative (3.5), so checking (i) is linear algebra plus compactness; §4 does this. _(ii) Complementarity rigidity._ At an endpoint where one factor has lost rank, a direction can couple its vanished eigenspace with the support of the other factor, and the linearized residual does not see it. The two identities say that every such direction already runs along the optimal set. _(iii) The residual measures the distance._ In a tube around the optimal set, the KKT residual is at least a constant times the distance to it, which averaged splitting methods convert into linear rates (§5). _(iv) Stiffness along every normal._ At a singular endpoint the normal cone is larger than \(\mathcal{D}^\perp\), since directions leaving the PSD cone through a vanished eigenspace are normal there too; (iv) asks for the response of (i) along all these normals, with a bound uniform over all endpoints. _(v) Stall cone equals tangent cone._ The directions along which the residual vanishes to first order are exactly those along the optimal set; equivalently, no direction leaves Z_<sub>⋆</sub>_ while the first-order dynamics stalls--the geometric content of "benign".

