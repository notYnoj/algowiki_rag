Almost Optimal Multiple Source Shortest Paths and Reachability

**Abstract**

Given a graph, computing distances and reachabilities from a small set of vertices to the whole graph is an important primitive both in theory and in practice. In this paper, we study this problem in various important settings.

In undirected unweighted graphs, while computing single-source shortest path (SSSP) requires _O(n_<sup>2</sup>) time in dense graphs, all-pairs shortest paths (APSP) can be computed in \(\hat{O}(n^\omega)=O(n^{2.372})\) time [Seidel ’95] providing significant savings over running _n_ SSSP instances separately. However, if one needs to compute multiple-source shortest paths (MSSP) from a set of \(n^\sigma\) vertices, the previously best known running time was \(\hat{O}(min\{n^\omega,n^{2+\sigma}\})\): either by running APSP or running SSSP from each of the \(n^\sigma\) sources. On the other hand, a standard reduction shows that computing MSSP from \(n^\sigma\) sources is at least as hard as computing the Boolean matrix product between an \(n^\sigma\times n\) matrix and an \(n\times n\) matrix. This lower bound has a gap from the state-of-the-art algorithm and therefore, MSSP can potentially be solved much faster. The first main result of our paper is an algorithm for MSSP on undirected unweighted graphs that matches this lower bound. In particular, using fast rectangular matrix multiplication, our algorithm runs in \(\hat{O}(n^{\omega(\sigma,1,1)})\) time, which gives a smooth interpolation between the SSSP algorithm and the APSP algorithm. We also extend our algorithm to the case where the graph has small integer weights. The main technical tool behind our first main result is a novel graph decomposition, which may be of independent interest. As applications, we improve the state-of-the-art running times for hop-sets construction and computing +4-distance emulators.

Next, we study the multiple-source reachability problem, where we need to determine whether a given set of \(n^\sigma\) vertices can reach each of the vertices in a given directed graph. Multiple-source reachability can also be solved in \(\hat{O}(min\{n^\omega,n^{2+\sigma}\})\) time, and similarly is as hard as computing Boolean matrix product between an \(n^\sigma\times n\) matrix and an \(n\times n\) matrix. [Elkin and Trehan ’24, ’25] gave the first nontrivial algorithm for multiple-source reachability that runs in \(\hat{O}(n^{1+2\omega(\sigma,1,1)/3})\) time. This only beats the trivial \(\hat{O}(min\{n^\omega,n^{2+\sigma}\})\) time for a restricted range of \(\sigma\). We significantly improve their results, by giving an algorithm that runs in \(\hat{O}(n^{\omega(\sigma,1,1)})\) time, again matching the running time for Boolean matrix product. Our algorithm for multiple-source reachability can be generalized to MSSP on DAGs with small integer weights. As an application, we provide an _O(n_<sup>2.084</sup>) time algorithm for computing an \(\widetilde{O}(n)\)-size shortcut set that reduces diameter to _O(n_<sup>1/3</sup>), improving the previous \(\widetilde{O}(n^{7/3})\) time algorithm [Kogan and Parter ’22, ’23].

<sup>∗</sup>Supported by NSF HDR TRIPODS Phase II grant 2217058 (EnCORE Institute).

Barna Saha<sup>∗</sup><br> University of California San Diego<br> `bsaha@ucsd.edu`

Yinzhan Xu<sup>∗</sup><br> University of California San Diego<br> `xyzhan@ucsd.edu`

Christopher Ye<sup>∗</sup><br> University of California San Diego<br> `czye@ucsd.edu`

