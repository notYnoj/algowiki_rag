<tbc>most four with five distinct roots \(e^{i\theta_j}\). All five coefficients in the displayed equation must therefore vanish. Since _a,s\>_0, this gives _M_<sub>12</sub>=_M_<sub>13</sub>=_M_<sub>23</sub>=0 and _M_<sub>11</sub>=_M_<sub>22</sub>=1. Hence _M=I_, proving uniqueness. □

**Remark 4.2.** The wheel illustrates why it is useful to allow a general dual slack matrix. Its largest Laplacian eigenvalue is 6 and is simple: an eigenvector has entry -5 at the hub and entry 1 at every cycle vertex. No Gram matrix with unit diagonal can have its range in this eigenspace. The matrix _S_ in the proof instead uses a diagonal shift of the adjacency matrix tailored to the hub and the cycle vertices.

## 5. Realizing every rank

Each rank now has a connected unweighted example on the smallest possible number of vertices. Attaching leaves increases the order one vertex at a time while preserving the unique optimum and its rank.

_Proof of Theorem 1.2._ Let \(1\le r\le r_\mathrm{BP}(n)\), so \(\genfrac(){pt}{2}{r+1}{2}\le n\). For _r_=1 start with _K_<sub>1</sub>, and for _r_=2 start with _K_<sub>3</sub>; as observed in Section 2, their optima are unique and have ranks one and two, respectively. For _r_=3 use the six-vertex wheel of Theorem 4.1. For \(r\ge 4\) use _K(r_+1,2), whose unique optimum has rank _r_ by Theorem 1.1.

These starting graphs are connected. For the Kneser graph, disjoint pairs are adjacent, while two distinct intersecting pairs have a common neighbour: since \(r+1\ge 5\), a two-element set can be chosen outside their union. Each starting graph has \(\genfrac(){pt}{2}{r+1}{2}\) vertices. Attach \(n-\genfrac(){pt}{2}{r+1}{2}\) pendant vertices and apply Lemma 2.4 repeatedly. The resulting graph is connected and unweighted, and its optimum is unique and still has rank _r_. □

_Proof of Corollary 1.3._ The upper bound (1) applies to every graph under consideration. Theorem 1.2 with _r=r_<sub>BP</sub>(_n_) attains it in the smallest of the three classes, the connected unweighted graphs. □

Can the bound \(\rho(G)=r_\mathrm{BP}(n)\) be attained with a unique optimum by a 2-connected graph at every order \(n\ge 3\), or by a connected regular graph at every sufficiently large order?

## 6. Random graphs

The constructions above attain the largest possible optimal rank. We now ask what happens when the edges are chosen independently. The next result shows that a dense random graph forces every optimal representation to use a polynomially growing number of dimensions.

**Theorem 6.1.** _There is an absolute constant c\>_0 _such that, for_ \(G\sim G(n,\frac{1}{2})\),

\(\mathbb{P}\big\{\rho(G)\ge c\left(\frac{n}{(\mathrm{log}n)^3}\right)^{1/7}\big\}\longrightarrow 1.\)

The idea is to separate objective values: if every representation in at most _r_ dimensions performs worse than one feasible matrix, then every optimum has rank greater than _r_. After centering and scaling the adjacency matrix, we compare both values with the spectral edge 2. A Gaussian comparison produces a loss of order 1_/r_ at bounded rank, and a spectral construction comes closer to 2. The main work is to keep the errors small enough as _r_ grows.

_Proof of Theorem 6.1._ Let _A_ be the adjacency matrix and put

\(W=\frac{J-I-2A}{\sqrt{n}},F_n(X)=\langle W,X\rangle-\frac{\mathbf{1}^\top X\mathbf{1}}{\sqrt{n}}.\)

