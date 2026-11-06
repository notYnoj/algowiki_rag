edge from each \(x\in X\) to each \(y\in Y\) . In other words, \(V(G)=\{s\}\cup V(B_1)\cup\cdots\cup V(B_\lambda)\cup Y\) and \(E(G)=\{(s,r_i)|1\le i\le\lambda\}\cup E(B_1)\cup\cdots\cup(B_\lambda)\cup(X\times Y)\).

We prove in the following lemma that any \((\lambda,k)\)-FT-BFP of the above constructed graph contains at least \(\Omega(2^k\lambda n)\) edges.

**Proof.** It is easy to see that the out-edges of _s_, and the edges of each of the binary tree _B<sub>i</sub>_’s must be present in a \((\lambda,k)\)-FT-BFP of G. Thus, let us consider an edge \((x,y)\in X\times Y\) , where _x_ is the leaf node of some binary tree _B<sub>i</sub>_.

Let _P_ be the unique path from _r<sub>i</sub>_ to _x_ in _B<sub>i</sub>_, and let _F_ be the set of all those edges \((u,v)\in B_i\) such that \(u\in P\) and _v_ is the child of _u_ not lying on _P_. On failure of set _F_, there remains a unique path from _s_ to _y_ that passes through edge (_s,r<sub>i</sub>_). Moreover, max-flow\((s,y,\mathcal{G}\backslash F)=\lambda\). So, any subgraph H of G not containing (_x,y_) edge would not be a \((\lambda,k)\)-FT-BFP as on failure set _F_, H would not preserve (_s,y_)-max-flow.

Hence, any \((\lambda,k)\)-FT-BFP of G contains at least \(|X\times Y|=2^k\lambda|Y|\ge 2^k\lambda n/3\) edges.

In this section we present applications of FT-BFP structure.

Georgiadis et al. [16] showed that for any _n_ vertex directed graph G=(_V,E_) we can compute 2-reachability information for all pairs of vertices in \(O(n^\omega logn)\) time, where \(\omega\) is the matrix multiplication exponent. Abboud et at. [1] extended this result to all-pairs \(\lambda\)-reachability by presenting an algorithm that takes \(O((\lambda logn)4^{\lambda+o(\lambda)}\cdot n^\omega)\) time. One of the interesting open questions is if for any constants \(\lambda,k\ge 1\), we can compute an oracle that given any query vertex-pair \(x,y\in V\) and any set _F_ of _k_ edge failures, reports (_x,y_)-\(\lambda\)-reachability in G\\_F_ efficiently.

For any vertex \(x\in V\) , let H_<sub>x</sub>_ denote a \((\lambda,k)\)-FT-BFP of G with _x_ as the source. Our data structure simply stores the graph family \(\{\mathcal{H}_x|x\in V\}\). Given any query vertex-pair (_x,y_) and any set _F_ of _k_ edges, we compute the (_x,y_)-max-flow in H_<sub>x</sub>_ by employing the max-flow algorithm of Chen et al. [10]. The time to compute the max-flow is _O_(|_E_(H_<sub>x</sub>_)|<sup>1+_o_(1)</sup>), which

### 6.1 Fault-tolerant All-Pairs \(\lambda\)-reachability oracle

## 6 Applications

S
r1
r2
r3
X
Y
y

\(\blacktriangleright\) **Lemma 22.** _Any_ \((\lambda,k)\)_-FT-BFP of_ G _must contain_ \(\Omega(2^k\lambda n)\) _edges._

**Figure 2** Depiction of lower bound on the size of \((\lambda,k)\)-FT-BFP when _k_=3.

