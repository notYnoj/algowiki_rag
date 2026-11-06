<tbc>we try to find windows \(w_a,w_b\in S\) such that \(\langle w_i,w_a,w_b,w_j\rangle\) is constructive. If such a constructive tuple is found for a pair of windows, then we conclude that their normalized LCS is at least \((1-\epsilon)\lambda^3\).

All that remains is to argue that this method discovers almost all the edges of the lcs-graph \(\mathsf{G}_\lambda\) and the number of undiscovered edges is \(k^{2-\Omega(1)}\). This is the most difficult part of the analysis. We note that even proving the existence of **only one** constructive tuple is already non-trivial **even when** \(\mathsf{G}_\lambda\) **is complete**. However, our goal is to show that almost all the edges are discovered via constructive tuples when \(\mathsf{G}_\lambda\) is dense (and of course not necessarily complete).

Define a pair of windows _w<sub>i</sub>_ and _w<sub>j</sub>_ to be _well-connected_, if there are at least \(k^{2-\gamma}\) different (_w<sub>a</sub>,w<sub>b</sub>_) pairs such that \(\langle w_i,w_a,w_b,w_j\rangle\) is \((\epsilon,\lambda)\)-constructive. Since each window appears in _S_ with probability \(k^{\gamma-1}logk\), for each well-connected pair we find one constructive tuple via our algorithm with high probability. Therefore, we need to prove that the total number of pairs (_w<sub>i</sub>,w<sub>j</sub>_) such that (_w<sub>i</sub>,w<sub>j</sub>_) is not well-connected but \(||\mathsf{lcs}(w_i,w_j)||\ge\lambda\) is subquadratic. Let us put these edges in a new graph \(\mathsf{NG}_\lambda\) whose vertices are all the windows.

We first leverage the Blakley-Roy inequality and a double counting technique to prove that if \(\mathsf{NG}_\lambda\) has a large complete bipartite subgraph, then there is one constructive tuple which includes only the vertices of this subgraph (Lemma 3.12). Next, we apply the Turan’s theorem to show that if \(\mathsf{NG}_\lambda\) is dense, then it has a lot of large complete bipartite subgraphs. Finally, we use a probabilistic method to conclude that \(\mathsf{NG}_\lambda\) cannot be too dense otherwise there are a lot of constructive tuples in the graph which implies that at least one edge (_w<sub>i</sub>,w<sub>j</sub>_) in \(\mathsf{NG}_\lambda\) is well-connected. This is not possible since all the well-connected pairs are detected in our sparsification algorithm with high probability.

The above argument proves that if we sparsify our graph using our sparsification algorithm, the remainder graph would have a subquadratic number of edges. Therefore after plugging Step 2 into the algorithm, the running time remains subquadratic. However, since Turan theorem gives us a weak bound, the running time of the algorithm using this sparsification is \(O(n^{2-\Omega(\lambda)})\) and is only truly subquadratic when \(1/\lambda\) is constant.

## Sparsification 2, \(\Omega(\lambda^3)\)-approximation

In Section 3.1, we present another sparsification method that although gives us a slightly worse approximation factor \(\Omega(\lambda^3)\) it always leaves a truly subquadratic number of edges behind and therefore the running time of the algorithm would be truly subquadratic regardless of the parameter \(\lambda\). This sparsification is based on a novel data structure.<tbc>

wa
wj
Wi
wb

Figure 2: Let _w<sub>i</sub>,w<sub>a</sub>,w<sub>b</sub>_ and _w<sub>j</sub>_ denote four windows and each of them has length _d_=8. This figure shows how the intersection of the edges of three windows are taken in order to construct a solution for the LCS of _w<sub>i</sub>_ and _w<sub>j</sub>_. If the size of the intersection is large, then such a tuple is called constructive. The solid lines represent LCS between two strings, and the dashed line represents the intersection of the three LCSs.

