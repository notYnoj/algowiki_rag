### D.7 Relation to second-order limit dynamics

The stall cone \(\mathcal{C}(\bar{Z})\) of (3.6) is the central object of the companion analysis \[KY26b\], which studies ADMM near an arbitrary KKT point under the same strict-complementarity assumption. There, \(\mathcal{C}(\bar{Z})\) is the fixed-point set of the local first-order dynamics. Every direction \(H\in\mathcal{C}(\bar{Z})\backslash T_{\mathcal{Z}_\star}(\bar{Z})\) drives a second-order limit drift \(\phi(\bar{Z};H)\neq 0\) (its Proposition 6). Along such a direction the residual decays like _t_<sup>2</sup> while the distance to the optimal set stays of order _t_; these are the slow regions seen in practice. That paper proves that a local linear growth condition at \(\bar{Z}\) forces \(\mathcal{C}(\bar{Z})=T_{\mathcal{Z}_\star}(\bar{Z})\) (its Corollary 1(3)) and conjectures that the equality is necessary for local linear convergence. Theorem 3.2 supplies the converse in the setwise form: the equality at every endpoint of a compact fixed-point set is _equivalent_ to the uniform error bound (iii). In words, benign degeneracy means that no endpoint carries a direction of \(\mathcal{C}(\bar{Z})\backslash T_{\mathcal{Z}_\star}(\bar{Z})\), along which the residual is of second order while the distance is of first order. §4 shows that exact Boolean relaxations have none, and Theorem 4.4 exhibits one for nonconstant full-order Boolean objectives with tied minimizers.

## E The Boolean Modulus

### E.1 Proof of the subspace identities

_Proof of Theorem 4.1._ In coordinates whose first vector is _q_, matrices of S(_V_) have zero first row and column, so \(\mathbb{S}(V)^\perp\) consists of the matrices with zero _VV_ block, which are \(\{qv^\top+vq^\top\}\); this is (4.1). If such a matrix lies in T_<sub>d</sub>_, its diagonal vanishes; the diagonal entries are 2_q<sub>A</sub>v<sub>A</sub>_ and every \(q_A=\pm N^{-1/2}\neq 0\), so _v_=0, proving (4.2). For (4.3), the Boolean moment identity is

\(uu^\top=\sum_{\Gamma\in\mathcal{I}_{2d}}x_\star^\Gamma A_\Gamma=I_N+\sum_{\Gamma\neq\emptyset} x_\star^\Gamma A_\Gamma,\) (E.1)

since \((uu^\top)_{A,B}=x_\star^Ax_\star^B=x_\star^{A\triangle B}\). If \(H\in\mathbb{S}(V)\cap\mathcal{R}_d\), then _Hu_=0 and \(H\perp\mathcal{T}_d\), so \(0=\langle uu^\top,H\rangle=\text{tr}H\) by (E.1); hence \(H\perp I_N\) as well and \(H\in\mathcal{H}_d^\perp\). The reverse inclusion is immediate because \(\mathcal{T}_d\subseteq\mathcal{H}_d\). By (3.3), \(\mathbb{S}(V)\cap\mathcal{R}_d=\mathcal{L}\); that L also equals span(S<sub>⋆</sub>-S<sub>⋆</sub>) is Theorem C.2 under the instantiation of §4. Taking orthogonal complements gives \(\mathcal{L}^\perp=\mathbb{S}(V)^\perp+\mathcal{H}_d=\mathbb{S}(V)^\perp+\mathcal{T}_d\) (subspace sums, not orthogonal sums), the last equality because \(I_N=uu^\top-\sum_{\Gamma\neq\emptyset} x_\star^\Gamma A_\Gamma\) and \(uu^\top=Nqq^\top\in\mathbb{S}(V)^\perp\).

This resolves a distinction worth recording: the primal equality row space is \(\mathcal{T}_d^\perp\), while the kernel of the Gram-to-polynomial map is \(\mathcal{H}_d^\perp\). They differ, but their intersections with \(\mathbb{S}(q^\perp)\) agree.

### E.2 Derivative identifications for the extension

Fix \(\sigma>0\) and \(S\in\mathcal{S}_\star\), and let \(P_K:=Q_KQ_K^\top\) be the orthogonal projector onto \(K:=\text{ker}(S)\cap V\) , with _Q<sub>K</sub>_ from (C.3). Recall J_<sub>S</sub>_ and \(\Psi_S\) from (4.4). We prove the two identifications used in §4:<tbc>

\(S\in\text{ri}\mathcal{S}_\star:\Pi'_+(X_\star-\sigma S;\cdot)=\mathscr{J}_S,\delta'_\sigma(X_\star-\sigma S;\cdot)=-\Psi_S,\) (E.2)

\(S\in\mathcal{S}_\star\text{arbitrary},K=\text{ker}(S)\cap V:\Pi'_+(X_\star-\sigma S;H)=\mathscr{J}_S(H)+Q_K\Pi_+(Q_K^\top HQ_K)Q_K^\top.\) (E.3)

<tbc>_Proof._ Apply (C.4) at \(\bar{Z}=X_\star-\sigma S\) with the Boolean instantiation of §4: _U_=span{_q_} is one- dimensional, so \(\Lambda_+=(N)\) in (C.3) and \(\Omega_{1j}=N/(N+\sigma s_j)\). The _UU_ block contributes \(h_{00}qq^\top\) with \(h_{00}=q^\top Hq\). The cross blocks from _U_ to _K_ and to ran_S_ assemble into \(qw^\top+wq^\top\) with<tbc>

\(w=\sum_j\frac{N}{N+\sigma s_j}\theta_j\theta_j^\top Hq+P_KHq=N(NI_N+\sigma S)^{-1}P_VHq,\)

