<tbc>we prove a more general result: given any interval _I_, all distances in \(S\cap I\) can be enumerated in \(O(n^{4/3}+|S\cap I|)\) time. The result follows from an _implicit biclique partition theorem_ (Theorem 4), which computes a compact representation of all distances in \(S\cap I\) in an implicit manner within _O(n_<sup>4/3</sup>) time. We believe this theorem may be of independent interest. For comparison, the algorithms of Katz and Sharir \[20\] and Wang and Zhao \[28\] both rely on explicit representations of the relevant distances. Their techniques require _O(n_<sup>4/3</sup>log_n_) and _n_<sup>4/3</sup>2<sup>_O_(log<sup>∗</sup>_n_)</sup> time, respectively, to construct these representations. In contrast, our representation is maintained implicitly, which is crucial for acheiving the _O(n_<sup>4/3</sup>) running time.

### The asymmetric case.

To solve the asymmetric case \(m\neq n\), we seek to reduce the problem to the symmetric case. For several related geometric problems, such as Hopcroft’s problem \[10\], the problem of computing \(K_\delta\) \[24\], and computing many faces in line arrangements \[26\], such a reduction is relatively straightforward, and the symmetric case algorithm can be used essentially as a black box. For the distance selection problem, however, the situation appears to be more subtle. In particular, we cannot simply invoke the symmetric case algorithm as a black box and obtain the desired running time. Instead, additional ideas are needed to combine the symmetric subproblems efficiently.

One possible reason is that distance selection lacks the type of decomposability enjoyed by the above problems. Solving a subproblem on two subsets \(A'\subseteq A\) and \(B'\subseteq B\) does not immediately provide useful information for solving the original problem on _A_ and _B_. Consequently, extra care is needed in order to exploit the symmetric case machinery while acheiving the desired time complexity.

Besides distance selection, the techniques developed in this paper may also be useful for other geometric optimization problems involving interpoint distances.

### Outline.

The remainder of the paper is organized as follows. Section 2 introduces notation and reviews the partial biclique partition technique from \[28\]. The next three sections focus on the symmetric case _m=n_. Section 3 develops the approximate counting theorem (Theorem 1) and the resulting quasi-decision algorithm (Theorem 2). Section 4 proves the distance representation theorem (Theorem 3). Section 5 combines these ingredients to obtain a deterministic _O(n_<sup>4/3</sup>)-time distance selection algorithm. Section 6 extends the framework to the asymmetric case \(m\neq n\) and presents the _O(m_log<sup>2</sup>_n+n_log<sup>2</sup>_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>)-time algorithm.

## 2 Preliminaries

For any two points _a,b_ in the plane, we use \(\|ab\|\) to denote their Euclidean distance. Let _A_ and _B_ be two sets of points in the plane. Define \(S(A,B)=\{\|ab\||a\in A,b\in B\}\) to be the set of pairwise distances between points of _A_ and points of _B_. We write _S_ for _S(A,B_) when the point sets are clear from the context. We assume that no point of _A_ is co-located with a point of _B_. Consequently, \(0\notin S\).

For an interval _I_, we use \(S\cap I\) to denote the subset of distances in _S_ whose values lie in _I_. Unless stated otherwise, all intervals considered in this paper are of the form \((\alpha,\beta]\), that is, they are open on the left endpoint and closed on the right endpoint.

For any region \(\sigma\) in the plane, we use \(A(\sigma)\) to denote the subset of points of _A_ in \(\sigma\), i.e., \(A(\sigma)=A\cap\sigma\). We define \(B(\sigma)\) similarly.

**Definition 1** (Biclique)**.** _Let_ \(A_t\subseteq A\) _and_ \(B_t\subseteq B\)_. A_ biclique _is a complete bipartite graph with bipartition_ (_A<sub>t</sub>,B<sub>t</sub>), i.e., the graph containing all edges between every point of A<sub>t</sub> and every point of B<sub>t</sub>. We denote the biclique by_ \(A_t\times B_t\)_. The_ size _of the biclique is defined as_ |_A<sub>t</sub>_|+|_B<sub>t</sub>|._

A biclique \(A_t\times B_t\) compactly represents all distance pairs between points of _A<sub>t</sub>_ and points of _B<sub>t</sub>_. We therefore often say that the biclique _records_ these pairs or their corresponding distances. For a<tbc>

