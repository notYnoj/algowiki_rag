## 1 Introduction

Computing shortest paths is among the most fundamental problems in computer science. Many of its variants have been studied in the literature, and the All-Pairs Shortest Paths (APSP) problem is one of the most fundamental variants and has been extensively studied.

In APSP, one needs to compute the distance between every pair of nodes in a given _n_-vertex graph.<sup>1</sup> One could run Dijkstra’s algorithm _n_ times to obtain an _O(n_<sup>3</sup>) running time. An alternative classical algorithm, the Floyd-Warshall algorithm, also achieves an _O(n_<sup>3</sup>) running time. A long series of works (e.g. \[Fre76, Dob90, Tak92, Tak98, Han04, Pet04, Zwi04, Cha05, Han06, Cha10, HT12\]) improved poly-logarithmic factors over the classic _O(n_<sup>3</sup>) running time, culminating in the current fastest algorithm by Williams \[Wil18\] with \(n^3/2^{\Theta(\sqrt{\mathrm{log}n})}\) running time for general weighted graphs, a super poly-logarithmic improvement over the classic _O(n_<sup>3</sup>) running time. Due to the lack of polynomial improvements, the APSP hypothesis, stating that there is no \(O(n^{3-\varepsilon})\) time algorithm for any \(\varepsilon>0\) that computes APSP for _n_-node graphs, is among the most popular hypotheses in Fine-Grained Complexity.

Faster algorithms are known in unweighted graphs. If the graph is undirected, Seidel \[Sei95\] gave an algorithm computing APSP in \(\widehat{O}(n^\omega)\) time.<sup>2</sup> More generally, on undirected graphs with positive integer weights bounded by _B_, APSP can be computed in \(\widehat{O}(Bn^\omega)\) time \[SZ99, AGM97\]. For directed unweighted graphs, the current fastest algorithm was designed by Zwick \[Zwi02\], which runs in _O(n_<sup>2.528</sup>) time.

A simpler version of distance problems is reachability problems, where one needs to decide whether a vertex can reach another vertex. All-Pairs Reachability, also popularly known as transitive closure, is another fundamental problem in graph algorithms. It is known to be equivalent to the Boolean Matrix Multiplication problem, and can be solved in \(\widehat{O}(n^\omega)\) time \[FM71, Mun71\].

Computing all the pairwise distances (resp. reachability) gives full distance (resp. reachability) information of the graph, but it also comes with a cost: it is computationally expensive. In contrast, computing the distance between a fixed pair of vertices only takes near-linear time in all the variants mentioned above, though it gives much less information than APSP. A natural question is to study the intermediate cases:

**Question 1.** _Can we compute some distances faster than all distances?_

Graphs arising in theory and practice applications often contain a small set of hot spots, where distances between these hot spots and other vertices are more likely to be queried. For instance, in the network connecting all locations in a city, distances from places like grocery stores, shopping malls and parks are more likely to be queried than distances between two residential buildings. In theory, many applications using distance computations only need distances from a fixed small set of vertices to other vertices (e.g. approximate APSP \[DHZ96, DKR<sup>+</sup>22, SY24, DFK<sup>+</sup>24, JKSV26\], approximate diameter \[RV13, CLR<sup>+</sup>14, CGR16\] and shortcut sets and hopsets \[UY91\]).

Motivated by these applications, we study the multiple source version of distance and reachability problems. More formally, we study:

**Definition 1.1** (Multiple Source Shortest Paths / Reachability)**.** _Given graph G_=(_V,E_) _and a set of sources_ \(S_\mathrm{in}\subseteq V\) _, compute_ dist(_s,v_) _for all_ \(s\in S_\mathrm{in}\) _and_ \(v\in V\) _. In the reachability version of the problem, we only need to determine if the distance is_ \(\infty\) _or not._

### 1.1 Shortest Paths in Undirected Unweighted Graphs

Our first result is for Multiple-Source Shortest Paths in undirected unweighted graphs. There are two straightforward algorithms to solve MSSP: we can either solve SSSP for every \(s\in S_\mathrm{in}\), or solve APSP. For undirected graphs, there were no other known algorithms besides these two approaches, to the best of our knowledge. This leads to the following question that motivated our work, instantiating a specific instance of Question 1.

<sup>1</sup>Throughout this paper, we consider dense graphs with _m=O(n_<sup>2</sup>). <sup>2</sup>\(\omega\le 2.372\) \[ADV<sup>+</sup>25\] is the fast matrix multiplication exponent, or the smallest constant _c_ such that an \(n\times n\times n\) matrix product can be computed in _n_<sup>_c+o_(1)</sup> time. \(\widehat{O}\) hides sub-polynomial factors.

