# If Edge Coloring is Hard under SETH, then SETH is False

Alexander S. Kulikov <sup>∗</sup><br>
Ivan Mihajlin <sup>†</sup>

**Abstract**

The Edge Coloring problem is notoriously hard: it is still unknown whether it can be solved in time 2<sup>_o(n_<sup>2</sup>)</sup> (let alone 2<sup>_O(n_)</sup>), where _n_ is the number of nodes of the input graph. Can one explain the lack of such upper bounds by deriving a lower bound \(2^{\Omega(n^2)}\) from a lower bound for SAT, 3-SUM, or APSP? In this note, we provide a negative answer for this question: if there is a reduction showing that Edge Coloring cannot be solved faster than in \(\alpha^{n^2}\) (where \(\alpha>1\) is an explicit constant) under a hypothesis that known algorithms for one of the problems mentioned above are optimal, then the corresponding hypothesis is false.

## 1 Overview of New Results

The field of fine-grained complexity aims to establish tight connections between complexity of computational problems. A fine-grained reduction, denoted \((P,p(n))\le(Q,q(n))\), implies that a faster than _q(n_)-time algorithm for _Q_ leads to a faster than _p(n_)-time algorithm for _P_. Equivalently, it says that if _P_ cannot be solved faster than in _p(n_) time, then _Q_ cannot be solved faster than in _q(n_) time. The standard assumptions in this field are hardness of Satisfiability (SAT) [13, 14], 3-SUM [10, 9], Orthogonal Vectors (OV) [18], All Pairs Shortest Paths (APSP) [19], Online Matrix- Vector Multiplication [12], and Set Cover [8]. For example, assuming the Strong Exponential Time Hypothesis (stating that for every \(\varepsilon>0\) there exists _k_ such that _k_-SAT cannot be solved in time \(2^{(1-\varepsilon)n}\)), the following upper bounds are essentially optimal: 2_<sup>n</sup>_ for Hitting Set (where _n_ is the size of the universe), 2_<sup>n</sup>_ for NAE-SAT (where _n_ is the number of the variables) [8], _nk_ for _k_-Dominating Set [17] (where _n_ is the number of nodes in the input graph and \(k\ge 7\)), 2tw for Independent Set [16] (where tw is the treewidth of the input graph).

In the Edge Coloring problem (also known as Chromatic Index), one is given an undirected graph and is asked to color the edges using the minimum number of colors such that any two edges sharing a node receive different colors. The best known algorithm for Edge Coloring transforms an input graph with _n_ nodes and _m_ edges into a line graph with _m_ nodes and finds its chromatic index in time _O_∗(2_<sup>m</sup>_) [5]. (The \(O^*(\cdot)\) notation suppresses polynomial factors.) As _m_ can be as large as \(\genfrac(){pt}{2}{n}{2}\), the running time can be as bad as \(2^{\Omega(n^2)}\). It is not known whether Edge Coloring can be solved in time 2<sup>_o(n_<sup>2</sup>)</sup>. It is natural to ask whether one can prove a lower bound \(2^{\Omega(n^2)}\) for Edge Coloring under an assumption that SAT, 3-SUM, or APSP is hard. We give a negative answer to this question.

**Theorem 1.** _If there exists a fine-grained reduction showing that, assuming SETH, Edge Coloring cannot be solved in time_ \(\alpha^{n^2}\)_, for some_ \(\alpha>1\)_, then SETH is false._

<sup>∗</sup>JetBrains Research. Email: `alexander.s.kulikov@gmail.com`. <sup>†</sup>JetBrains Research. Email: `ivmihajlin@gmail.com`.

