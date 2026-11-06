<tbc>Van Dam and Sotirov \[20\] show that the spectral bound is attained for all walk-regular graphs, a class containing the Kneser graphs. Attaining the value alone does not determine the minimum optimal rank. We prove that the diagonal equations are independent on the relevant space of symmetric matrices, so the entire optimal face consists of one point. This is an application of the classical extremality criterion for correlation matrices \[10, 13\].

The centred-incidence representation is also central to the work of Godsil, Roberson, Rooney, Šámal and Varvitsiotis \[8\], who prove universal completability and unique vector colorability of Kneser graphs. Those problems prescribe or bound individual edge correlations; Max-Cut optimizes their sum. The difference is substantive: _K_<sub>4</sub> has a unique optimal vector coloring, represented by a regular tetrahedron, while its Max-Cut relaxation has both this rank-three optimum and rank- one optima coming from balanced cuts. For _K(m,_2), we establish uniqueness using the diagonal equations alone within the least adjacency eigenspace.

The wheel uses the same principle with the kernel of a dual slack matrix in place of the top Laplacian eigenspace. Finally, attaching a leaf preserves the optimal rank and uniqueness. This extension is a special case of the vertex-sum constructions in \[12\]. We collect the necessary facts in Section 2, prove the Kneser and wheel results in Sections 3 and 4, and assemble the construction proving Theorem 1.2 in Section 5. The final section gives a polynomial lower bound for random graphs and proposes a conjecture on the growth of their optimal rank.

## 2. The optimal face

We begin with the geometry shared by the two constructions. The dual of the relaxation is \(min\{\sum_iy_i:Diag(y)-\frac{1}{4}L\unknown 0\}\). The identity matrix is strictly feasible for the primal problem, so strong duality holds and the dual optimum is attained. If _S_ is an optimal dual slack, complementary slackness confines every optimum _X_ to \(rangeX\subseteq kerS\). A scalar diagonal choice gives the familiar eigenvalue bound.

**Lemma 2.1** (Eigenvalue bound \[16, 6\])**.** _Let_ \(\lambda=\lambda_{max}(L)\) _and let E be its eigenspace. For every_ \(X\in\mathcal{E}_n\) _we have_ \(\langle L,X\rangle\le n\lambda\)_, with equality if and only if_ \(rangeX\subseteq E\)_. If some_ \(X\in\mathcal{E}_n\) _satisfies_ \(rangeX\subseteq E\)_, then_ \(sdp(G)=\frac{n}{4}\lambda\) _and_

\(F(G)=\{X\in\mathcal{E}_n:rangeX\subseteq E\}.\)

_Proof._ \(\lambda I-L\unknown 0\) and \(X\unknown 0\) give \(\langle\lambda I-L,X\rangle\ge 0\), that is \(\langle L,X\rangle\le\lambda trX=n\lambda\). Equality holds if and only if \(\langle\lambda I-L,X\rangle=0\), which for two positive semidefinite matrices means \((\lambda I-L)X=0\), that is \(rangeX\subseteq E\). □

**Lemma 2.2** (Parametrising the face)**.** _Let_ \(E\subseteq\mathbb{R}^n\) _be a subspace of dimension g, let_ \(U\in\mathbb{R}^{n\times g}\) _have columns forming a basis of E, and let_ \(u_i^\top\) _be the i-th row of U. Then the map_ \(M\mapsto UMU^\top\) _is a rank-preserving bijection from_

\(\mathcal{M}=\{M\in Sym(\mathbb{R}^g):M\unknown 0,u_i^\top Mu_i=1(i\in[n])\}\)

_onto_ \(\{X\in\mathcal{E}_n:rangeX\subseteq E\}\).

_Proof._ A symmetric _X_ has \(rangeX\subseteq rangeU\) if and only if \(X=UMU^\top\) for a symmetric _M_, which is unique because _U_ has full column rank; for the same reason \(X\unknown 0\) if and only if \(M\unknown 0\), and rank_X_=rank_M_. The condition _X<sub>ii</sub>_=1 reads \(u_i^\top Mu_i=1\). □

In these coordinates, uniqueness becomes a question about linear equations: do the conditions \(u_i^\top Mu_i=1\) determine _M_? The following form of the correlation-matrix extremality criterion \[10, 13\] will be useful.

**Lemma 2.3** (Spanning forces a single point)**.** _In the setting of Lemma 2.2, suppose that the rank- one matrices_ \(u_iu_i^\top\), \(i\in[n]\)_, span_ Sym(R_<sup>g</sup>), and that_ M _contains a positive definite matrix M_<sub>0</sub>_. Then_ M={_M_<sub>0</sub>}_. If moreover E is the top eigenspace of L, then_ \(F(G)=\{UM_0U^\top\}\) _and_ \(\rho(G)=g\).

