<tbc>time for directed graphs \[Tho04\], where _C_ is the maximum edge weight. For graphs with negative weights, recent breakthrough results include near-linear time _O(m_<sup>1+_o_(1)</sup>log_C_) algorithms for SSSP with negative integer weights \[CKL<sup>+</sup>22, BNWN22, BCF23\], and strongly subcubic time algorithm for SSSP with negative real weights \[Fin24, HJQ24\].

Based on the lower bound of \(\Omega(nlogn)\) for comparison-based sorting algorithms, it was generally believed that such _sorting barrier_ exists for SSSP and many similar problems. Researchers have broken such a sorting barrier for many graph problems. For example, Yao \[Yao75\] gave a minimum spanning tree (MST) algorithm with running time _O(m_loglog_n_), which is further improved to randomized linear time \[KKT95\]. Gabow and Tarjan \[GT88\] solves _s-t_ bottleneck path problem in _O(m_log<sup>∗</sup>_n_)-time, later im proved to randomized \(O(m\beta(m,n))\) time \[CKT<sup>+</sup>16\], where \(\beta(m,n)=min\{k\ge 1:log^{(k)}n\le\frac{m}{n}\}\). For the single-source all-destination bottleneck path problem, there is a randomized \(O(m\sqrt{logn})\)-time algorithm by Duan, Lyu, Wu and Xie \[DLWX18\]. For the single-source nondecreasing path problem, Virginia V.Williams \[Wil10\] proposed an algorithm with a time bound of _O(m_loglog_n_).

## 2 Preliminaries

We consider a directed graph _G_=(_V,E_) with a non-negative weight function \(w:E\rightarrow\mathbb{R}_{\ge 0}\), also denoted by _w<sub>uv</sub>_ for each edge \((u,v)\in E\). Let _n_=|_V_|, _m_=|_E_| be the number of vertices and edges in the graph. In the single-source shortest path problem, we assume there is a source vertex in the graph denoted by _s_. The goal of our algorithm is to find the length of shortest path from _s_ to every vertex \(v\in V\) , denoted by _d(v_). Without loss of generality, we assume that every vertex in _G_ is reachable from _s_, so \(m\ge n-1\).

### Constant-Degree Graph.

In this paper we assume that the algorithm works on a graph with constant in- degrees and out-degrees. For any given graph _G_ we may construct \(G'\) by a classical transformation (similar to \[Fre83\]) to accomplish this:

• Substitute each vertex _v_ with a cycle of vertices strongly connected with zero-weight edges. For every incoming or outgoing neighbor _w_ of _v_, there is a vertex _x<sub>vw</sub>_ on this cycle.<tbc>

• For every edge (_u,v_) in _G_, add a directed edge from vertex _x<sub>uv</sub>_ to _x<sub>vu</sub>_ with weight _w<sub>uv</sub>_.

It’s clear that the shortest path is preserved by the transformation. Each vertex in \(G'\) has in-degree and out-degree at most 2, while \(G'\) being a graph with _O(m_) vertices and _O(m_) edges.

### Comparison-Addition Model.

Our algorithm works under the _comparison-addition_ model, where all edge weights are subject to only comparison and addition operations. In this model, each addition and comparison takes unit time, and no other computations on edge weights are allowed.

### Labels Used in the Algorithm.

For a vertex \(v\in V\) , denote _d(u_) as the length of shortest path from _s_ to _u_ in the graph. Similar to the Dijkstra’s algorithm, our algorithm maintains a global variable \(\widehat{d}[u]\) as a sound estimation of _d(u_) (that is, \(\widehat{d}[u]\ge d(u)\)). Initially \(\widehat{d}[s]=0\) and \(\widehat{d}[v]=\infty\) for any other \(v\in V\) . Throughout the algorithm we only update \(\widehat{d}[v]\) in a non-increasing manner by relaxing an edge \((u,v)\in E\), that is, assign \(\widehat{d}[v]\leftarrow\widehat{d}[u]+w_{uv}\) when \(\widehat{d}[u]+w_{uv}\) is no greater than the old value of \(\widehat{d}[v]\). Therefore each possible value of \(\widehat{d}[v]\) corresponds to a path from _s_ to _v_. If \(\widehat{d}[x]=d(x)\), we say _x_ is _complete_; otherwise, we say _x_ is _incomplete_. If all vertices in a set _S_ are complete, we say _S_ is complete. Note that completeness is sensitive to the progress of the algorithm. The algorithm also maintains a shortest path tree according to current \(\widehat{d}[\cdot]\) by recording the predecessor Pred\[_v_\] of each vertex _v_. When relaxing an edge (_u,v_), we set \(\mathsf{Pred}[v]\leftarrow u\).

