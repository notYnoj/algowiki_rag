# Fast Approximation Algorithms for Balanced Edge and Vertex Separators

**Abstract**

We present a family of fast pseudo-approximation algorithms for the minimum balanced element cut problem in a graph, which includes vertex and edge separators. Given a graph _G_=(_V,E_) with polynomially-bounded finite integer element weights with _n_ vertices and _m_ edges, and a (constant) balance parameter \(c\in(0,1/2)\), where _G_ has some (unknown) _c_- balanced element cut of size OPT_<sub>c</sub>_, we give a (Monte-Carlo randomized) algorithm running in \(O(n^\varepsilon m^{1+o(1)})\) time that produces a \(\Theta(1)\)-balanced element cut of size \(O(OPT_c\cdot\sqrt{(logn)/\varepsilon})\) for any value \(\varepsilon\in[\Theta(1/log(n)),\Theta(1)]\). In particular, for any function \(f(n)=\omega(1)\) (including _f(n_)=loglog_n_, for instance), we can produce an element cut of size \(O(OPT_c\cdot\sqrt{logn}\cdot f(n))\) in time _O(m_<sup>1+_o_(1)</sup>). Moreover, for an arbitrarily small constant \(\varepsilon=\Theta(1)\), our algorithm also achieves the best-known approximation ratio for the vertex-separator specialization in \(O(m^{1+\varepsilon})\) time.

Our algorithms are based on a semidefinite programming (SDP) relaxation of the problem. A standard approach to solving an SDP relaxation for this kind of problem would use the primal- dual Matrix Multiplicative Weights Update framework of Arora and Kale, but this framework does not seem to apply, since we cannot express all of our SDPs primal variables explicitly. Instead, we present a new MMWU framework for our problem that allows us to represent some of our variables implicitly. We also extend our framework to a general **Partial-variable MMWU framework**, which we expect will be useful for future work. Our oracle for the balanced element cut problem within our framework uses \(O(n^\varepsilon\text{polylog}(n))\) almost-linear time maximum-flow computations, and would be sped up if the time complexity of maximum-flow improves.

For graphs with _padding bound_ \(\beta\), another oracle gives an \(O(\sqrt{\beta}/\varepsilon)\) approximation in \(m^{1+o(1)}n^\varepsilon\text{polylog}(n)\) time. It is known that \(\beta\le O(logh)\) for _K<sub>h</sub>_-minor-free graphs (and in particular \(\beta\le O(logn)\)).

### 1 Introduction

Partitioning a graph into smaller pieces is a fundamental problem that arises in many fields. One kind of graph partition with widespread applications in algorithms is the **vertex separator**: A small set of vertices whose removal disconnects the graph into small components.

More generally, let _G_=(_V,E_) be a graph with _n_=|_V_| vertices, let \(w:V\cup E\rightarrow\mathbb{Z}_{\ge 0}\) assign a polynomially-bounded weight to each vertex and edge, and let \(c\in(0,1/2)\) be a constant. For \(Z\subseteq V\cup E\), write \(w(Z)=\sum_{z\in Z}w(z)\). We treat vertex and edge separators in a common framework. A _c_-balanced **element cut** is a partition \(V=A\sqcup B\sqcup C\) with \(max\{|A|,|B|\}\le(1-c)n\), of cost

\(cost(A,B,C)=w(C)+w(E(A,B)).\)

It deletes the vertices in _C_ and the edges between _A_ and _B_. We also use \(w(z)=\infty\) as notation for forbidding deletion of an element _z_. Vertex separators are the specialization \(w(e)=\infty\) for all \(e\in E\), and edge cuts are the specialization \(w(x)=\infty\) for all \(x\in V\) . Write OPT_<sub>c</sub>_ for the minimum finite cost of a _c_-balanced element cut, _w_max for the maximum finite element cost, and _W_ for the sum of all finite element costs. Balance always counts original vertices. For fixed sets to separate,

Vladimir Kolmogorov Institute of Science and Technology Austria (ISTA) `vnk@ist.ac.at`

Jack Spalding-Jamieson Independent `jacksj@uwaterloo.ca`

arXiv:2603.15782v2 [cs.DS] 22 Oct 2026

