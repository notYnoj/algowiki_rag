1. A conceptual difference between Theorem 1.1 and Theorem 4.2 is that the former uses _conic spans_ while the second result uses only _linear spans_ for inference. The use of linear spans makes it easier to reason about, and as we will see, to obtain efficient algorithms.<tbc>

2. The GSL algorithm can be implemented even when restricted to only performing equality queries--i.e., queries that only tell us whether _w_<sup>∗</sup>(_S_)=_w_<sup>∗</sup>(_T_) or \(w^*(S)\neq w^*(T)\). In this setting, the buckets would be unordered, and identifying whether _w_<sup>∗</sup>(_y_<sub>_t_+1</sub>)=_w_<sup>∗</sup>(_r<sub>i</sub>_) would require _O(nB_) equality queries, increasing the query complexity to _O(n_<sup>2</sup>_B_<sup>2</sup>). More generally, \(O((n+C)\cdot C)\) equality queries if _C_ is the number of distinct weight values realized by the feasible set.

## 4.2 Efficient Implementation of Global Subspace Learning

The main computational bottleneck in the GSL algorithm is in finding a point \(y\in\mathcal{P}\) such that \(y\notin\bigcup_{i\in[\ell]}\mathcal{A}_i\)--i.e., the separation problem over the union of the affine subspaces A_<sub>i</sub>_. We show that we can solve this separation problem when F is the family of all _k_-subsets \(\genfrac(){pt}{2}{U}{k}\), or more generally, when F is the set of bases of a linear matroid representable over R.

Recall that the subspace A is the span of directions orthogonal to _w_<sup>∗</sup>; since _w_<sup>∗</sup> has integer coordinates, it must lie in the orthogonal lattice \(\mathcal{W}:=\mathcal{A}^\perp\cap\mathbb{Z}^n\). Let \(A\in\mathbb{Z}^{m\times n}\), where \(m=\mathrm{dim}(\mathcal{A})\le n-1\), be the matrix whose rows form a basis for A. By definition, the orthogonal complement \(\mathcal{A}^\perp\) is the nullspace of _A_. Therefore, W is precisely the _integer nullspace_ of _A_.

An integer basis for W can be computed using the _Smith Normal Form_ (SNF) of the \(m\times n\) matrix _A_, which returns a decomposition _D=UAV_, where \(U\in\mathbb{Z}^{m\times m}\) and \(V\in\mathbb{Z}^{n\times n}\) are unimodular matrices, and _D_ is an \(m\times n\) diagonal matrix with _m_ non-zero entries. The last _s_:=_n-m_ columns of _V_ , which correspond to the zero columns of _D_, form the required integer basis for W. Moreover, the decomposition _U,D,V_ can be found in polynomial time.

**Lemma 4.3** (Integer Nullspace via SNF, \[KB79, Sch86\])**.** _Let_ \(A\in\{-1,0,1\}^{m\times n}\)_. An integer basis for the integer nullspace_

\(\mathrm{ker}_\mathbb{Z}(A)=\{x\in\mathbb{Z}^n:Ax=0\}\)

_can be computed in polynomial time in n and m. The entries of the resulting basis vectors are bounded in bit-length by_ poly(_n,m)._

Note that our matrix entries are of the form \(\unknown_S-\unknown_T\) where \(S,T\in\mathcal{F}\), and hence they lie in {-1,0,1}. Since \(m\le n\), Lemma 4.3 implies that the resulting integer basis vectors have entries bounded by 2<sup>poly(_n_)</sup>. Let \(W\in\mathbb{Z}^{s\times n}\) denote the matrix whose rows form this basis spanning the orthogonal lattice W. The next implication is immediate:

**Observation 4.4.** Point _x_ belongs to A_<sub>i</sub>_ for some \(i\in[\ell]\) if and only if _W(x-r<sub>i</sub>_)=0. This implies that \(y\notin\bigcup_{i\in[\ell]}\mathcal{A}_i\) is equivalent to \(Wy\notin\{Wr_1,\dots,Wr_\ell\}\), where the _r<sub>i</sub>_ vectors are the bucket representatives.

Let _W_=\[_w_<sub>1</sub>_,...,w<sub>n</sub>_\] where \(w_i\in\mathbb{Z}^s\) is the _i_th column of _W_ and \(Z=\{z_1,\dots,z_\ell\}\) with _z<sub>i</sub>=Wr<sub>i</sub>_. We will use \(w(S):=\sum_{i\in S}w_i\). Henceforth, the following problem is the one we focus on.

**Definition 4.5** (Separation Problem)**.** Given vectors \(w_1,w_2,\dots,w_n\in\mathbb{Z}^s\), and a collection \(Z\subseteq\mathbb{Z}^s\) with some \(\ell\) vectors, identify a subset \(S\in\mathcal{F}\) such that \(w(S)\notin Z\).

