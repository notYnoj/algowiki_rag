The procedure BUILDCLOSE takes O(n<sup>2</sup>) time. Consider the running time of Algorithm 3. The algorithm processes a vertex x only when \(|\text{ESTIMATEDCLOSE}(x)|\le n^{0.875}\) and pairs x only with vertices in ESTIMATEDCLOSE(x). Hence, x pairs with at most n<sup>0.875</sup> vertices. Using Theorem 3.5, since \(cluster_\alpha(\cdot)=\tilde{O}(2^{2^\alpha})\), the algorithm spends \(\tilde{O}(2^{2^{\alpha+1}})\) time to process each pair. This is the only place in our algorithm where we need a bounded size of cluster. Thus, the running time of Algorithm 3 equals:

\(\sum_x\sum_{y\in\text{ESTIMATEDCLOSE}(x)}\tilde{O}(2^{2^{\alpha+1}})\)<br>
\(=\sum_x\tilde{O}(n^{0.875}2^{2^{\alpha+1}})\)<br>
\(=\tilde{O}(n^{1.875}2^{2^{\alpha+1}})\)

In Theorem 4.1, \(\alpha\) is set to loglogn-4. Thus, we get:

\(=\tilde{O}(n^{1.875}2^{\mathrm{loglog}n-3})\)<br>
\(=\tilde{O}(n^{1.875}2^\frac{\mathrm{log}n}{8})\)<br>
\(=\tilde{O}(n^{1.875}\times n^{0.125})\)<br>
\(=\tilde{O}(n^2)\)

Thus, the total running time of our algorithm is \(\tilde{O}(n^2)\). We now describe how the algorithm processes x when |ESTIMATEDCLOSE(x)| is large.

## 4.2 Dense Case: |ESTIMATEDCLOSE(x)|_\>_n<sup>0.875</sup>

In this section, we use FMM to estimate the distance between s and t. In Algorithm 4, we compute a random set \(L_\gamma\) of vertices where each vertex of G is sampled with probability \(\tilde{O}(\frac{1}{\gamma})\), where \(\gamma\in\{n^{0.875},2n^{0.875},2^2n^{0.875},\dots\}\). For each \(z\in L_\gamma\), we call \(\text{UPDATEFROM}(z,\gamma)\). This function constructs a graph \(G(\gamma)\) that contains all edges whose degree is at most \(\tilde{O}(\gamma)\). One can verify that \(G(\gamma)\) contains at most \(\tilde{O}(n\gamma)\) edges. We then compute the shortest path from z to every other vertex in \(G(\gamma)\) and update the estimates, if required.

\(\text{\textbf{Algorithm 4: Compute estimates using FMM
1}}\gamma\leftarrow n^{0.875}\text{\textbf{while}}\gamma\le n\text{\textbf{do
3}}L_\gamma\leftarrow\text{a random sample of size}\tilde{O}(\frac{n}{\gamma})\text{\textbf{4 foreach}}z\in L_\gamma\text{\textbf{do
5}}\text{UPDATEFROM}(z,\gamma)\text{\textbf{6 Construct a matrix B of size}}n\times\tilde{O}(\frac{n}{\gamma})\text{that stores the estimates of distances from vertices in}L_\gamma\text{to vertices in G
7 Using Theorem 3.11, compute}C=B\star B^\text{T
8 Update the estimates for all vertex pairs in G using C, if required
9}}\gamma\leftarrow 2\gamma\)

