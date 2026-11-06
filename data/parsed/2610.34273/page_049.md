operation, invertible row and column operations put a matrix of rank _r_ into a rectangular matrix with an \(r\times r\) identity block and zeros elsewhere. Applying the Kronecker products of these operations to two matrices of ranks _r_ and _s_ produces a matrix with exactly _rs_ independent nonzero rows and columns. Its rank is _rs_, proving the remaining identity.

The following calculation identifies the flattenings used in the cut bounds of \[CVZ19, Example 1.1.21\].

**Lemma A.3** (flattening across a graph cut)**.** _Let G_=(_V,E_) _be a finite simple undirected graph with V_={1_,...,k_} _and_ \(k\ge 2\)_. For every integer_ \(q\ge 2\) _and every nonempty proper subset_ \(S\subset V\)_, we have_ \(\mathrm{FR}_S(\mathsf{GT}_q(G))=q^{|\delta_G(S)|}\).

_Proof._ For each edge \((u,v)\in E\), the edge tensor \(E_{u,v}^{(q)}\) has nontrivial coordinates only at _u_ and _v_. If exactly one endpoint belongs to _S_, its flattening is a \(q\times q\) identity matrix, up to coordinates of dimension 1, and has rank _q_.

Suppose instead that both endpoints belong to _S_. The flattening is the nonzero column vector \(\sum_{a=0}^{q-1}e_{aq+a}^{(q^2)}\), with additional coordinates of dimension 1, and has rank 1. If neither endpoint belongs to _S_, it is the transpose of this vector and again has rank 1. Thus<tbc>

\(\mathrm{FR}_S(E_{u,v}^{(q)})=\left\{\begin{array}{ c c }
q, & (u,v)\in\delta_G(S), \\
1, & (u,v)\notin\delta_G(S).
\end{array}\right.\)

<tbc>Definition 2.20 expresses GT_<sub>q</sub>(G_) as the Kronecker product of these edge tensors. Repeatedly applying Lemma A.2 yields

\(\mathrm{FR}_S(\mathsf{GT}_q(G))=\prod_{(u,v)\in E}\mathrm{FR}_S(E_{u,v}^{(q)})=q^{|\delta_G(S)|}.\)

The same formula holds when _E_ is empty, since both sides are 1.

The lower bound below and its equality for bipartite graphs are recalled in \[CVZ19, Example 1.1.21 and the discussion after Question 1.3.2\].

**Proposition A.4** (maximum-cut lower bound)**.** _For every finite simple undirected graph G with at least two vertices and every integer_ \(q\ge 2\),

\(\mathrm{log}_2\widetilde{\mathsf{R}}(\mathsf{GT}_q(G))\ge\mathrm{MaxCut}(G)\mathrm{log}_2q.\)

_If G is bipartite, then_ \(\mathrm{log}_2\widetilde{\mathsf{R}}(\mathsf{GT}_q(G))=|E(G)|\mathrm{log}_2q=\mathrm{MaxCut}(G)\mathrm{log}_2q\)_. In particular, the lower bound gives_ \(\mathrm{log}_2\widetilde{\mathsf{R}}(\mathsf{GT}_2(K_n))\ge|n^2/4|\) _for every integer_ \(n\ge 2\).

_Proof._ Fix a nonempty proper subset \(S\subset V(G)\). Lemmas A.2 and A.3 give, for every positive integer _N_,

\(\mathrm{R}(\mathsf{GT}_q(G)^{\otimes K}N)\ge\mathrm{FR}_S(\mathsf{GT}_q(G)^{\otimes K}N)=\mathrm{FR}_S(\mathsf{GT}_q(G))^N=q^{N|\delta_G(S)|}.\)

Taking _N_-th roots, letting \(N\rightarrow\infty\), and taking base-two logarithms gives \(\mathrm{log}_2\widetilde{\mathsf{R}}(\mathsf{GT}_q(G))\ge|\delta_G(S)|\mathrm{log}_2q\). Since \(q\ge 2\), we have log<sub>2</sub>_q\>_0, so maximizing over _S_ gives the first assertion.

Suppose that _G_ is bipartite and has at least one edge. Its bipartition is a cut crossed by every edge, so MaxCut(_G_)=|_E(G_)|. The defining expansion of GT_<sub>q</sub>(G_) has one simple tensor for each of the _q_<sup>|_E(G_)|</sup> edge labelings. Hence \(\mathrm{R}(\mathsf{GT}_q(G))\le q^{|E(G)|}\), and taking Kronecker powers<tbc>

