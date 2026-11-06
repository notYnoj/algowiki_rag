<tbc>The distinction between arbitrary objectives and graph objectives is essential here. Extreme points of E_<sub>n</sub>_ exist at every rank permitted by (1) \[10, 13\]. Since every face of a spectrahedron is exposed \[19\], each is the unique optimum of a suitable linear functional. The same sharp rank bound appears in the extreme Gram dimension of Eisenberg-Nagy, Laurent and Varvitsiotis \[7\], where the objective coefficients on a fixed graph may be arbitrary real numbers. For an unweighted graph, the off-diagonal entries of its Laplacian belong to {0,-1}. Since diagonal terms contribute a constant on E_<sub>n</sub>_, it is this restriction on the off-diagonal coefficients that distinguishes our objectives. Our result realizes every admissible rank under this restriction, while also requiring connectivity and uniqueness.

The main construction uses Kneser graphs, familiar from graph coloring and Lovász’s work \[14\]. The graph _K(m,_2) has the two-element subsets of \[_m_\] as vertices, with two vertices adjacent exactly when the corresponding subsets are disjoint.

**Theorem 1.1.** _Let_ \(m\ge 5\) _and_ \(n=\genfrac(){pt}{2}{m}{2}\)_. Then the relaxation_ SDP(_K(m,_2)) _has a unique optimal solution X_<sup>∗</sup>_, given by_

\(X_{ef}^*=\frac{m|e\cap f|-4}{2(m-2)}(e,f\in\genfrac(){pt}{2}{[m]}{2})),\)

_and_ rank_X_<sup>∗</sup>=_m_-1=_r_<sub>BP</sub>(_n). In particular_ \(\rho(K(m,2))=r_\mathrm{BP}(n)\).

Explicitly, _X_<sup>∗</sup> is the Gram matrix obtained by assigning to the pair {_a,b_} the unit vector proportional to the centred indicator vector \(e_a+e_b-\frac{2}{m}\mathbf{1}\), where _e<sub>a</sub>_ is the _a_-th standard basis vector. Disjoint pairs have inner product \(-\frac{2}{m-2}\) and distinct overlapping pairs have inner product \(\frac{m-4}{2(m-2)}\). For _m_=5 this is the Petersen graph, whose unique optimal solution has rank 4=_r_<sub>BP</sub>(10).

The Kneser family skips rank three, because _K_(4,2) is a perfect matching. The wheel formed by joining a hub to all five vertices of a cycle supplies the missing rank, already on six vertices (Theorem 4.1). To reach any larger order, we attach pendant vertices: each new leaf receives the negative of its neighbour’s vector, preserving both the rank and the uniqueness of the optimum. These observations give a complete realization result.

**Theorem 1.2.** _For every_ \(n\ge 1\) _and every integer_ \(1\le r\le r_\mathrm{BP}(n)\)_, there is a connected unweighted graph on n vertices whose Max-Cut semidefinite relaxation has a unique optimal solution of rank r._

**Corollary 1.3.** _For every_ \(n\ge 1\)_, the maximum of_ \(\rho(G)\) _over connected unweighted graphs on n vertices equals r_<sub>BP</sub>(_n). The same maximum is obtained over all unweighted graphs, or over graphs with nonnegative real edge weights._

Thus every rank permitted by the general theory occurs as the rank of a unique optimum, even when the graph is required to be connected and all its edge weights are one.

The constructions also suggest a question about random graphs: must the dimension grow when the edges are chosen independently? For \(G\sim G(n,\frac{1}{2})\), where each pair is an edge independently with probability 1/2, we prove

\(\rho(G)\ge c\left(\frac{n}{(\mathrm{log}n)^3}\right)^{1/7}\)

with probability tending to one, for an absolute constant _c\>_0 (Theorem 6.1). Thus, with probability tending to one, every optimal representation of an Erdős-Rényi graph with edge probability 1/2 requires polynomially many dimensions. The proof compares the best objective value at bounded rank with a feasible matrix concentrated near the upper spectral edge. We also formulate a conjecture on the growth rate, motivated by the Gaussian spin-glass literature.

The proofs of the realization results follow a common pattern: first locate the range of every optimum, then use the diagonal equations to determine the Gram matrix. For the Kneser graphs, the classical Laplacian eigenvalue bound \[16, 6\] confines this range to the top Laplacian eigenspace.

