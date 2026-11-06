\(\mathcal{T}_d:=\mathrm{span}\{A_\Gamma:\emptyset\neq\Gamma\in\mathcal{I}_{2d}\}\) (every matrix in it has zero diagonal), and its row space is \(\mathcal{R}_d:=\mathcal{T}_d^\perp\). Compactness of S_<sub>⋆</sub>_ is the trace identity (Theorem B.2), and X_<sub>⋆</sub>_={_X<sub>⋆</sub>_} is a point, so Theorem 3.1 holds with M={0} and D=L, and the dual identity in (3.8) is automatic.

## 4.1 Two decisive subspace identities

**Lemma 4.1** (Boolean subspace geometry)**.** _With_ \(V=q^\perp\):

\(\mathbb{S}(V)^\perp=\{qv^\top+vq^\top:v\in\mathbb{R}^N\},\) (4.1)

\(\mathcal{T}_d\cap\mathbb{S}(V)^\perp=\{0\},\) (4.2)

\(\mathcal{L}=\mathbb{S}(V)\cap\mathcal{R}_d=\mathbb{S}(V)\cap\mathcal{H}_d^\perp,\mathcal{H}_d:=\mathrm{span}\{I_N\}\oplus\mathcal{T}_d.\) (4.3)

The first identity is elementary. The second is the _constant-diagonal identity_: a matrix \(qv^\top+vq^\top\in\mathcal{T}_d\) has zero diagonal 2_q<sub>A</sub>v<sub>A</sub>_ with every \(q_A=\pm N^{-1/2}\) nonzero, so _v_=0. The third is the _XOR-class identity_, built on \(uu^\top=\sum_{\Gamma\in\mathcal{I}_{2d}}x_\star^\Gamma A_\Gamma\); the full proofs are in Appendix E.1. In words: no consistency direction can lie in \(\mathbb{S}(V)^\perp\), and inside S(_V_) the equality row space and the Gram-map kernel agree.

## 4.2 A continuous extension of the interior derivative

For every \(S\in\mathcal{S}_\star\)--including boundary certificates--define the linear maps

\(\mathscr{J}_S(H):=h_{00}qq^\top+qw^\top+wq^\top,h_{00}:=q^\top Hq,w:=N(NI_N+\sigma S)^{-1}P_VHq,\Psi_S:=\mathsf{P}\mathscr{J}_S+\mathsf{P}^\perp(\mathrm{Id}-\mathscr{J}_S).\text{(4.4)}\)

The inverse exists because \(NI_N+\sigma S\unknown NI_N\), and \(S\mapsto\Psi_S\) is operator-norm continuous on all of S_<sub>⋆</sub>_. For \(S\in\mathrm{ri}\mathcal{S}_\star\) the projection is differentiable at \(X_\star-\sigma S\) and \(\Pi'_+(X_\star-\sigma S;\cdot)=\mathscr{J}_S\), so \(\delta'_\sigma(X_\star-\sigma S;\cdot)=-\Psi_S\). At a boundary certificate the true directional derivative acquires exactly one extra nonlinear term, \(Q_K\Pi_+(Q_K^\top HQ_K)Q_K^\top\) with _Q<sub>K</sub>_ an orthonormal basis of \(K:=\mathrm{ker}(S)\cap V\) (Appendix E.2). So \(\Psi_S\) is a continuous _algebraic extension_ of the interior derivative.

**Proposition 4.2** (Uniform relative-interior modulus)**.** _For every_ \(S\in\mathcal{S}_\star\), \(\mathrm{ker}(\Psi_S)=\mathcal{L}\)_; consequently_

\(\mu_\mathrm{ri}\ge\mu_\star:=\mathrm{min}_{S\in\mathcal{S}_\star}\sigma_\mathrm{min}\big(\Psi_S\big|_{\mathcal{L}^\perp}\big)>0.\) (4.5)

The proof (Appendix E.3) is a kernel chain through the two identities. If \(\Psi_S(H)=0\), the two residual components vanish separately. The constant-diagonal identity (4.2) then forces \(\mathscr{J}_S(H)\in\mathcal{T}_d\cap\mathbb{S}(V)^\perp=\{0\}\), and unwinding (4.4) places _H_ in \(\mathbb{S}(V)\cap\mathcal{R}_d=\mathcal{L}\). Continuity of \(S\mapsto\Psi_S\) and compactness of S_<sub>⋆</sub>_ turn the pointwise kernel statement into the uniform bound (4.5).

## 4.3 The deterministic theorem

**Theorem 4.3** (Deterministic Boolean benign degeneracy)**.** _Suppose the order-d Boolean moment relaxation has a unique rank-one optimum and one strictly complementary optimal SOS certificate. Then, for every fixed_ \(\sigma>0\)_, the canonical DR residual satisfies the setwise error bound_ (3.9) _around its entire fixed-point set_ Z_<sub>⋆</sub>, and its stall cone equals the tangent cone of_ Z_<sub>⋆</sub> at every endpoint. The algorithmic conclusions of Theorems 5.1 and 5.2 hold for the independent encoding_ (B.3)_, at every endpoint, regardless of the rank of the certificate selected by the iteration._

_Proof._ Theorem B.1 gives surjectivity of A_<sub>d</sub>_ and Theorem B.2 compactness of S_<sub>⋆</sub>_; the instantiation above places us under Theorem 3.1; Theorem 4.2 verifies condition (i) of Theorem 3.2, whose condition (iii) is the error bound and condition (v) the exact linearization. Then apply §5.

