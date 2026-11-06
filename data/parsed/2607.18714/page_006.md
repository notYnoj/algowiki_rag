\(\sum_x\sum_{y\in\text{ESTIMATEDCLOSE}(x)}\sum_{s\in\text{cluster}_A(x),t\in\text{cluster}_A(y)}\text{O}(1)\)<br>
\(=\sum_x\sum_{y\in\text{ESTIMATEDCLOSE}(x)}\tilde{\text{O}}(n^{0.05}\times n^{0.05})\)<br>
\(=\sum_x\tilde{\text{O}}(n^{0.875}\times n^{0.1})\)<br>
\(=\tilde{\text{O}}(n^{1.975})\)

Thus, the running time of our algorithm is less than \(\tilde{\text{O}}(n^2)\). We now move to the second case.<tbc>

2. **Dense Case:** |ESTIMATEDCLOSE(x)|_\>_n<sup>0.875</sup><tbc>

<tbc>In this case, we exploit the fact that ESTIMATEDCLOSE(x) is large. Let L be a set of vertices sampled from V with probability \(\tilde{\text{O}}\left(\frac{1}{n^{0.875}}\right)\). With high probability, \(|\text{L}|=\tilde{\text{O}}(n^{0.125})\), meaning L is a very small set. Moreover, with high probability, L contains at least one vertex \(z\in\text{ESTIMATEDCLOSE}(x)\). We therefore estimate the distance using the vertices of L as intermediaries:<tbc>

\(est(s,t)=min_{z\in\text{L}}\{est(s,z)+est(z,t)\}\)

<tbc>Later, we show that est(s,t) is a constant additive approximation of |st| and that we can compute these estimates concurrently for all dense vertices using Fast Matrix Multiplication (FMM). Because \(|\text{L}|=\tilde{\text{O}}(n^{0.125})\), this computation involves multiplying small rectangular matrices of size \(n\times n^{0.125}\) and \(n^{0.125}\times n\). Following \[Cop82, Wil14\], we can multiply these matrices in \(\tilde{\text{O}}(n^2)\) time. Thus, the running time of our algorithm remains \(\tilde{\text{O}}(n^2)\) despite the use of FMM.

Because the algorithm correctly handles every candidate x, it successfully approximates the st path when it processes x=p<sub>s</sub>. If ESTIMATEDCLOSE(p<sub>s</sub>) is sparse, the modified algorithm checks the pair (p<sub>s</sub>,p<sub>t</sub>) and computes an additive approximation of the st path. If ESTIMATEDCLOSE(p<sub>s</sub>) is dense, one of the vertices in the random set L lies near the st path, and the FMM step guarantees we find a good approximation.

To summarise, the key takeaway from this overview is the following. The st path naturally decomposes into three segments: the low-degree prefix sp<sub>s</sub>, the short middle segment p<sub>s</sub>p<sub>t</sub>, and the low- degree suffix p<sub>t</sub>t. The prefix and suffix are handled cheaply because their low-degree structure allows efficient exact distance computation inside balls. The middle segment is handled by the sparse/dense case split: if few vertices are close to p<sub>s</sub>, we enumerate them directly; if many are, a small random sample is guaranteed to hit one, and FMM does the rest. The entire approach hinges on Theorem 2.6, which ensures the middle segment is short. Justifying this assumption is the main technical contribution of the subsequent sections, and we use the recent work of Gupta \[Gup25\] to establish it.

## 3 Preliminaries

Let G be an undirected unweighted graph with n vertices and m edges. Let V and E denote the vertex and edge sets of G. For any pair s,t, let st denote a shortest path between s and t. If multiple shortest paths exist, pick one arbitrarily. Let |st| denote the length of st. Let deg(s) denote the degree of a vertex \(s\in V\). We denote an edge between two adjacent vertices s and t by (s,t). For brevity, we will assume that log log n is an integer.

