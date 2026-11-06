## B Asymptotic Subrank and the Minimum Cut

We give a tensor-language proof of the minimum-cut formula of Vrana and Christandl \[VC17, Theorem 1\]. Their theorem concerns hypergraphs and is stated in terms of entanglement conversion. For graphs, we retain their orthogonal-representation construction, give the local maps explicitly, and verify the passage from degeneration to ordinary asymptotic subrank. The aim is to select many edge labelings such that the labels at any one vertex determine the entire labeling. The following definition and lemma give the required linear equations.

**Definition B.1** (general-position orthogonal representation)**.** Let _H_ be a finite simple graph with vertex set _W_, and let _d_ be a positive integer with \(d\le|W|\). A _general-position orthogonal representation_ of _H_ in R_<sup>d</sup>_ is a family \((c_w)_{w\in W}\) of vectors in R_<sup>d</sup>_ such that \(\langle c_u,c_v\rangle=0\) for every two distinct nonadjacent vertices \(u,v\in W\), and every subfamily of at most _d_ vectors is linearly independent. Here \(\langle x,y\rangle=\sum_{j=1}^dx_jy_j\).

The _line graph L(G_) of a graph _G_ has vertex set _E(G_); two distinct vertices of _L(G_) are adjacent exactly when the corresponding edges of _G_ share an endpoint.

The next lemma is the graph case of \[VC17, Theorem 3\]. Its real-vector input is the theorem of Lovász, Saks, and Schrijver \[LSS89, Theorem 1.1\], with the corrected proof in \[LSS00, Theorem 1\]. We include the rational approximation argument to obtain the integer weights used below.

**Lemma B.2** (integral orthogonal representations)**.** _Let G be a finite connected simple graph with at least three vertices. Put m_=|_E(G_)|, \(\ell=\mathrm{MinCut}(G)\)_, and_ \(d=m-\ell\)_. Then_ \(d\ge 1\)_, and L(G_) _has a general-position orthogonal representation_ \((c_e)_{e\in E(G)}\) _with_ \(c_e\in\mathbb{Z}^d\) _for every_ \(e\in E(G)\).

_Proof._ If _G_ has \(k\ge 3\) vertices, then \(\ell\le\mathrm{min}_{v\in V(G)}\mathrm{deg}(v)\le 2m/k<m\). Also \(\ell\ge 1\) because _G_ is connected. Consequently \(1\le d\le m-1\).

Deleting fewer than \(\ell\) edges leaves _G_ connected: otherwise a component of the remaining graph would give a cut of _G_ with fewer than \(\ell\) edges. It follows that deleting fewer than \(\ell\) vertices leaves _L(G_) connected. Indeed, the remaining vertices are the edges of the connected remaining graph, and a path in that graph connects any two of its edges by a sequence of incident edges. Thus _L(G_) is \(\ell\)-vertex-connected: it has more than \(\ell\) vertices and remains connected after deleting any set of fewer than \(\ell\) vertices.

The theorem of Lovász, Saks, and Schrijver \[LSS89, LSS00\] states that an (_m-d_)-vertex- connected graph on _m_ vertices admits a general-position orthogonal representation in R_<sup>d</sup>_. Apply it to _L(G_) and fix such a representation _a_<sub>1</sub>_,...,a<sub>m</sub>_, after ordering its vertices by the edges of _G_.

We now obtain rational vectors while preserving all orthogonality constraints. For each \(1\le i\le m\), let _A<sub>i</sub>_ be the set of indices _j\<i_ whose vertices are not adjacent to vertex _i_ in _L(G_). Every vertex of an \(\ell\)-vertex-connected graph has degree at least \(\ell\): otherwise deleting its fewer than \(\ell\) neighbors would isolate it while leaving another vertex. Hence \(|A_i|\le m-1-\ell=d-1\). Given vectors _f_<sub>1</sub>_,...,f<sub>m</sub>_ sufficiently close to _a_<sub>1</sub>_,...,a<sub>m</sub>_, define vectors _z_<sub>1</sub>_,...,z<sub>m</sub>_ in order. Let _B<sub>i</sub>_ be the matrix whose columns are _z<sub>j</sub>_ for \(j\in A_i\), ordered increasingly, and set

\(z_i=f_i-B_i(B_i^\mathsf{T}B_i)^{-1}B_i^\mathsf{T}f_i.\)

If _A<sub>i</sub>_ is empty, the subtracted term is defined to be zero. At _f<sub>i</sub>=a<sub>i</sub>_ for every _i_, induction gives _z<sub>i</sub>=a<sub>i</sub>_: the columns of _B<sub>i</sub>_ are independent by general position, and _a<sub>i</sub>_ is orthogonal to all of them. Thus every nonempty Gram matrix \(B_i^\mathsf{T}B_i\) is invertible at this choice.

