## 2 Overview

In the following section, we give an overview of the proofs of Main Theorem 1, Main Theorem 2, and Main Theorem 3: the first because its proof is simple and can be explained briefly, and the second and third because they let us highlight the additional structural properties we establish for these problems.

### 2.1 Induced Subgraph Connected Components in Matrix Multiplication Time

Given a graph **G**=(_V,E_) and a family of subsets \(\mathcal{S}\subseteq 2^V\), our goal is to compute, for each \(S\in\mathcal{S}\), the connected components of **G**[_S_]. The core idea of the algorithm is to gradually grow the connected components of **G**[_S_] for every \(S\in\mathcal{S}\). We proceed in rounds, maintaining a partition of each **G**[_S_] that refines its connected components. Let _C<sub>S</sub>(u_) denote a unique identifier associated with the part containing node _u_ in **G**[_S_].

We initialize the process with singleton parts for the nodes in every **G**[_S_]. In each round, for every \(S\in\mathcal{S}\) and node \(u\in\mathbf{G}[S]\), we check whether there exists an edge \(\{u,w\}\in\mathbf{G}[S]\) such that \(C_S(u)\neq C_S(w)\). Discovering such an edge allows us to merge the respective parts and update \(C_S(\cdot)\) accordingly for each _S_. We claim that O(log_n_) rounds suffice for these partitions to grow into the connected components. Indeed, any part that does not yet form a complete connected component will, by induction, contain at least 2_<sup>i</sup>_ nodes after the _i_-th round.

It remains to briefly outline how to find the edges across which we merge parts. We accomplish this in parallel for each **G**[_S_] via matrix multiplication. To this end, in each round we assign every part in each **G**[_S_] a value of zero or one, chosen uniformly and independently at random. Let \(C'_S(u)\) denote the bit assigned to the part _C<sub>S</sub>(u_).

Note that if, for some \(S\in\mathcal{S}\) and \(u\in\mathbf{G}[S]\), there exists an edge \(\{u,w\}\in\mathbf{G}[S]\) with \(C_S(u)\neq C_S(w)\), then with probability 1/4 we have \(C'_S(u)=0\) and \(C'_S(w)=1\). Furthermore, edges contained entirely within a single part of **G**[_S_] always have their endpoints assigned the same bit. Thus, it suffices to search for an edge spanning parts with differing assigned bits, repeating the procedure a logarithmic number of times to guarantee success with high probability.

The product we perform is between an \(|\mathcal{S}|\times n\) Boolean matrix _M_ (indexed by the sets in S and the vertices in _V_ ) and the adjacency matrix _A_ of **G** (indexed by the vertices in _V_ ). For the matrix _M_, we set _MS<sub>S,w</sub>=_1 if and only if \(w\in\mathbf{G}[S]\) and \(C'_S(w)=1\). It is easy to see that for every \(S\in\mathcal{S}\) and \(u\in\mathbf{G}[S]\) with \(C'_S(u)=0\), there exists an inter-part edge {_u,w_} if and only if (_MA)<sub>S,u</sub>=_1. The Boolean matrix multiplication witness for this product directly provides the desired edge.

It is also not difficult to derandomize the above procedure. In the full proof, we provide such a derandomized version with a slightly more formal presentation.

### 2.2 Recognizing AT-free Graphs in Matrix Multiplication Time

We proceed to outline the main idea behind our \(\tilde{\mathcal{O}}(n^{\omega_0})\)-time algorithm to verify whether a graph **G**=(_V,E_) contains an AT. We recall that such a triple consists of an independent set \(\{x,y,z\}\subseteq V\) such that there exists a path between every pair of nodes in {_x,y,z_} that does not pass through the neighborhood of the third node.

Before presenting the main idea of the algorithm, we note that the triangle-detection hardness of finding such a triple can be shown to rely solely on the condition that \(\{x,y,z\}\subseteq V\) forms an independent set. To clarify our point, we consider the following elementary reduction demonstrating how, given a tripartite graph \(\mathbf{G}=(X\cup Y\cup Z,E)\), we can build a graph \(\mathbf{G}'=(V',E')\) such that **G** contains a triangle



