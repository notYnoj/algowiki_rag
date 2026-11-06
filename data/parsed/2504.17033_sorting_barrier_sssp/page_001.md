# Breaking the Sorting Barrier for Directed Single-Source Shortest Paths

**Abstract**

We give a deterministic _O(m_log<sup>2/3</sup>_n_)-time algorithm for single-source shortest paths (SSSP) on directed graphs with real non-negative edge weights in the comparison-addition model. This is the first result to break the _O(m+n_log_n_) time bound of Dijkstra’s algorithm on sparse graphs, showing that Dijkstra’s algorithm is not optimal for SSSP.

### 1 Introduction

In an _m_-edge _n_-vertex directed graph _G_=(_V,E_) with a non-negative weight function \(w:E\rightarrow\mathbb{R}_{\ge 0}\), single-source shortest path (SSSP) considers the lengths of the shortest paths from a source vertex _s_ to all \(v\in V\) . Designing faster algorithms for SSSP is one of the most fundamental problems in graph theory, with exciting improvements since the 50s.

The textbook Dijkstra’s algorithm [Dij59], combined with advanced data structures such as the Fibonacci heap [FT87] or the relaxed heap [DGST88], solves SSSP in _O(m+n_log_n_) time. It works in the _comparison- addition_ model, natural for real-number inputs, where only comparison and addition operations on edge weights are allowed, and each operation consumes unit time. For undirected graphs, Pettie and Ramachandran [PR05] proposed a hierarchy-based algorithm which runs in \(O(m\alpha(m,n)+min\{nlogn,nloglogr\})\) time in the comparison-addition model, where \(\alpha\) is the inverse-Ackermann function and _r_ bounds the ratio between any two edge weights.

Dijkstra’s algorithm also produces an ordering of vertices by distances from the source as a byproduct. A recent contribution by Haeupler, Hladík, Rozhoň, Tarjan and Tětek [HHR<sup>+</sup>24] showed that Dijkstra’s algorithm is optimal if we require the algorithm to output the order of vertices by distances. If only the distances and not the ordering are required, a recent result by Duan, Mao, Shu and Yin [DMSY23] provided an \(O(m\sqrt{lognloglogn})\)-time randomized SSSP algorithm for undirected graphs, better than _O(n_log_n_) in sparse graphs. However it remains to break such a sorting barrier in directed graphs.

#### 1.1 Our results

In this paper, we present the first SSSP algorithm for directed real-weighted graphs that breaks the sorting bottleneck on sparse graphs.

**Theorem 1.1.** _There exists a deterministic algorithm that takes O(m_log<sup>2/3</sup>(_n_)) _time to solve the single- source shortest path problem on directed graphs with real non-negative edge weights._

<sup>∗</sup>Tsinghua University. Email: duanran@mail.tsinghua.edu.cn, mjy22@mails.tsinghua.edu.cn, ylh21@mails.tsinghua.edu.cn. <sup>†</sup>Stanford University. Email: matthew99a@gmail.com. <sup>‡</sup>Max Planck Institute for Informatics. Email: xshu@mpi-inf.mpg.de.

arXiv:2504.17033v2 [cs.DS] 30 Jul 2025

Ran Duan <sup>∗</sup> Jiayi Mao <sup>∗</sup> Xiao Mao <sup>†</sup> Xinkai Shu <sup>‡</sup> Longhui Yin <sup>∗</sup>

July 31, 2025

