\(\mu_G(s):=min_{v\in V\backslash\{s\}}\lambda_G(s,v)\), and the _global min-cut_ value is \(\mu_G:=min_{s\in V}\mu_G(s)\). Given an (_s,t_)-flow _h_ in _G_, the _residual graph G<sub>h</sub>_ is obtained from _G_ by reversing every edge that carries flow under _h_, i.e., replacing each edge _e_=(_u,v_) with _h(e_)=1 by its reverse _e_<sup>rev</sup>=(_v,u_), where **_c_**(_e_<sup>rev</sup>)=-**_c_**(_e_). We use val(_h_) to denote the value of the flow _h_.

An (_s,t_)-min-cut _C_<sup>∗</sup> is said to be the _nearest min-cut_ if for each (_s,t_)-min-cut _C_ we have \(A_{C^*}\subseteq A_C\). We denote such a _C_<sup>∗</sup> with NMC_<sub>G</sub>(s,t_). Ford and Fulkerson \[FF62\] gave an algorithm for constructing the (unique) nearest (_s,t_)-min-cut. For the sake of completeness we state the following characterization of NMCs from \[FF62\].

**Lemma 2.1.** _Let C=NMC<sub>G</sub>(s,t_) _with partition_ (_A,B). Then A consists precisely of those_ \(w\in V\backslash\{t\}\) _for which G<sub>w</sub>_:=_G_+(_w,t_) _satisfies_ \(\lambda_{G_w}(s,t)=\lambda_G(s,t)+1\).

## Algebraic Primitives

We now state the algebraic tools that we use to compute determinants of low-degree polynomial matrices in (near) matrix-multiplication time. We shall use F to denote a field. Recall that F\[_Y_\] is used to denote the ring of polynomials in _Y_ with coefficients from F. Given a non-negative integer _d_, let F_<sub>d</sub>_\[_Y_\] be the subset of polynomials in F\[_Y_\] of degree at most _d_. Finally, we shall use \(\mathbb{F}_d[Y]^{N\times N}\) to denote the set of \(N\times N\) matrices whose entries belong to F_<sub>d</sub>_\[_Y_\].

**Lemma 2.2.** _For any matrix_ \(M\in\mathbb{F}_d[Y]^{N\times N}\)_, one can compute_ det(_M_) _in_ \(\widetilde{O}(dN^\omega)\) _field operations._

**Lemma 2.3** (Matrix Determinant Lemma)**.** _Let_ \(M\in\mathbb{F}_d^{N\times N}\) _be an invertible matrix and let_ \(U,V\in\mathbb{F}_d^{N\times k}\)_. Then_

\(det(M+UV^T)=det(M)\cdot det(I_k+V^TM^{-1}U).\)

Our results also employ the oracle by Brand and Saranurak \[vdBS19\] that preprocesses a matrix _H_ to efficiently answer determinant queries following a limited number of updates to _H_.

**Lemma 2.4** (\[vdBS19, Corollary of Theorem 4.1\])**.** _Let_ \(M\in\mathbb{F}_d[Y]^{N\times N}\) _be a matrix such that_ \(det(M)\neq 0\)_. Then, there is an algorithm that preprocesses M using_ \(\widetilde{O}(dN^3)\) _operations and creates a data structure occupying O(dN_<sup>3</sup>log_N_) _space with the following guarantee: given_ \(C\in\mathbb{F}_d[Y]^{N\times N}\) _with at most_ \(\delta\) _nonzero entries and satisfying_ \(det(M+C)\neq 0\)_, one can query_ det(_M+C_) _in_ \(\widetilde{O}(dN\delta^\omega)\) _operations._

_Moreover, if d_=0_, then the preprocessing, space and query time are_ \(O(N^\omega)\)_, O(N_<sup>2</sup>log_N_) _and_ \(O(\delta^\omega)\) _respectively._

While the above lemma assumes a non-singular base matrix, we show in Appendix that this result can be naturally extended to general, possibly singular matrices with same asymptotic complexity bounds.

We next state two determinant identities that will be used to expand determinants of products of rectangular matrices and to decompose determinants of block-structured representation matrices.

**Lemma 2.5** (Cauchy-Binet)**.** _Let A and B be two_ \(r\times m\) _matrices with_ \(m\ge r\)_. Then_

\(det(AB^T)=\sum_{S\subseteq[m]|S|=r}det(A_S)det(B_S),\)

_where the sum ranges over all_ \(\genfrac(){pt}{2}{m}{r}\) _subsets S of size r, and A<sub>S</sub>, B<sub>S</sub> denote the corresponding_ \(r\times r\) _submatrices._

