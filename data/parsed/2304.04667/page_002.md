## 1 Introduction

The maximum _st_-flow problem, denoted Max-Flow, has been extensively studied in theoretical computer science for almost 70 years. This problem has become a key tool in algorithm design, with numerous applications of the problem and its techniques \[AMO93, FF56, AHK12, WL93\]. In a recent breakthrough, \[CKL<sup>+</sup>22, vdBCP<sup>+</sup>23\] gave an almost linear \(\hat{O}(m)\) time algorithm for the problem <sup>1,2,3</sup>. But what if we desire to find the Max-Flow value for all pairs? This problem is named All-Pairs Max-Flow, and the naive approach for it always works: simply apply a Max-Flow routine for every pair of nodes, thus resulting in an \(n^2\cdot m^{1+o(1)}\) time algorithm. Then the following question arises:

**_Q1_**_: Can All-Pairs Max-Flow be solved faster than the naive approach?_

_Alternatively, can we show conditional lower bounds?_

In the main variants of All-Pairs Max-Flow considered in the literature, the input graphs may be:

• directed or undirected,<tbc>

• edge-capacitated or node-capacitated, and<tbc>

• with unit-capacities, also called _connectivities_, or with arbitrary (usually polynomially-bounded) capacities.

It turns out that undirected graphs with edge capacities are particularly easy to solve, as a recent exciting line of work \[LP20, LP21, AKT21b, AKT21a, LPS21\] on Gomory-Hu tree<sup>4</sup> construction culminated with an almost linear \(\hat{O}(m)\) time algorithm \[AKL<sup>+</sup>22, ALPS23\]. However, the remaining variants are unlikely to be solved in almost linear time since hardness results are known for them (see  1), and so henceforth we call them _the hard variants_. In this context, the Strong Exponential Time Hypothesis (SETH)<sup>5</sup> \[IPZ01\] has been particularly useful, proving _n_<sup>3-_o_(1)</sup> time conditional lower bounds for hard variants in sparse \(m=\tilde{O}(n)\) graphs with (node or edge) capacities \[KT18, AKT20a\], and an _n_<sup>3-_o_(1)</sup> conditional lower bound for dense _m=O(n_<sup>2</sup>) graphs with unit edge- capacities.

Despite the lower bounds mentioned, the answer to **_Q1_** is positive in some restricted cases. For unit capacities in hard variants where either the input graph is sparse or the desired flow value is bounded, nontrivial algorithms are known. These include a network-coding based \(\tilde{O}(m^\omega)\) time algorithm for directed graphs with unit edge-capacities \[CLL13\], an \((nk)^\omega\) time adaptation of the latter to the _k_-bounded version of unit node-capacities (i.e., where the flow value is bounded by _k_), and an \(\hat{O}(mk^3)\) time algorithm for the _k_-bounded version of undirected graphs with unit node-capacities. The latter was obtained through an adaptation of an approximate Gomory-Hu tree algorithm \[LP21\] and employing an isolating cut lemma \[LP20, AKT21b, LNP<sup>+</sup>21\]. Very recently, via a high-degree low-degree method previously used in the context of Gomory-Hu trees \[AKT20a\], the \(\hat{O}(mk^3)\) algorithm above was adapted to an \(\hat{O}(m^{11/5})\) time algorithm for the unbounded version \[HLSW23\]. Still, in spite of extensive research, the naive approach remains the fastest algorithm for general dense graphs in all hard variants, while no matching conditional lower bounds are known. A relaxed phrasing of **_Q1_** restricts attention to combinatorial algorithms.<sup>6</sup>

<sup>1</sup>Henceforth, _n_ denotes the number of nodes, and _m_ the number of edges in an input graph. <sup>2</sup>\(\hat{O}(\cdot)\) hides _n_<sup>_o_(1)</sup> factors and \(\tilde{O}(\cdot)\) hides polylog(_n_) factors. <sup>3</sup>We say that a time bound _T(m_) is almost linear if it is bounded by _m_<sup>1+_o_(1)</sup> <sup>4</sup>This is a data structure that succinctly represents all min _st_-cuts in an input undirected graph with edge capacities. <sup>5</sup>SETH postulates that for every \(\varepsilon>0\) there exists an integer _k\>_0 such that _k_-SAT requires \(\Omega(2^{(1-\varepsilon)n})\) time. <sup>6</sup>_combinatorial algorithms_ commonly refers to algorithms avoiding fast matrix multiplication as a subroutine.

