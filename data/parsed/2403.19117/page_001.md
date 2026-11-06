# A Faster Algorithm for Pigeonhole Equal Sums

**Ce Jin** \(\boxtimes\) MIT **Hongxun Wu** \(\boxtimes\) UC Berkeley

**Abstract**

An important area of research in exact algorithms is to solve Subset-Sum-type problems faster than meet-in-middle. In this paper we study _Pigeonhole Equal Sums_, a total search problem proposed by Papadimitriou (1994): given _n_ positive integers _w_<sub>1</sub>_,...,w<sub>n</sub>_ of total sum \(\sum_{i=1}^nw_i<2^n-1\), the task is to find two distinct subsets \(A,B\subseteq[n]\) such that \(\sum_{i\in A}w_i=\sum_{i\in B}w_i\).

Similar to the status of the Subset Sum problem, the best known algorithm for Pigeonhole Equal Sums runs in _O_<sup>∗</sup>(2<sup>_n/_2</sup>) time, via either meet-in-middle or dynamic programming (Allcock, Hamoudi, Joux, Klingelhöfer, and Santha, 2022).

Our main result is an improved algorithm for Pigeonhole Equal Sums in _O_<sup>∗</sup>(2<sup>0.4_n_</sup>) time. We also give a polynomial-space algorithm in _O_<sup>∗</sup>(2<sup>0.75_n_</sup>) time. Unlike many previous works in this area, our approach does not use the representation method, but rather exploits a simple structural characterization of input instances with few solutions.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Design and analysis of algorithms

**Keywords and phrases** Subset Sum, Pigeonhole, PPP

**Funding** _Ce Jin_: Supported by NSF grants CCF-2129139 and CCF-2127597. Work done while visiting the Simons Institute for the Theory of Computing.

_Hongxun Wu_: Supported by Avishay Tal’s Sloan Research Fellowship, NSF CAREER Award CCF- 2145474, and Jelani Nelson’s ONR grant N00014-18-1-2562.

**Acknowledgements** We thank Ryan Williams for useful discussions.

### 1 Introduction

The Subset Sum problem is an important NP-hard problem in computer science: given positive integers _w_<sub>1</sub>_,w_<sub>2</sub>_,...,w<sub>n</sub>_ and a target integer _t_, find a subset \(A\subseteq[n]\) such that \(\sum_{i\in A}w_i=t\). Subset Sum can be solved in _O_(2<sup>_n/_2</sup>) time by a simple meet-in-middle algorithm [14], and an important open problem is to improve it to \(O(2^{(1/2-\varepsilon)n})\). A long line of research attempts to solve Subset Sum faster using the representation method [15] and connections to uniquely decodable code pairs [3, 4, 22], but these techniques have so far only succeeded on average-case inputs [15, 8, 9] or restricted classes of inputs [2, 3]. Nevertheless, significant progress has been made for other variants of Subset Sum, including Equal Sums [17], 2-Subset Sum and Shifted Sums [1] and more general subset balancing problems [12], as well as Subset Sum in other computational settings such as Merlin–Arthur protocols [18], low-space algorithms [6, 19], quantum algorithms [1], and algorithms with lower-order run time improvements [13]. The general hope is that the tools developed for solving these variant problems might one day help solve the original Subset Sum problem.

In this paper we study an interesting variant of Subset Sum called _Pigeonhole Equal Sums_:

Pigeonhole Equal Sums [20]

**Input:** positive integers _w_<sub>1</sub>_,w_<sub>2</sub>_,...,w<sub>n</sub>_, with promise \(\sum_{i=1}^nw_i<2^n-1\).

**Output:** two different subsets \(A,B\subseteq[n]\) such that \(\sum_{i\in A}w_i=\sum_{i\in B}w_i\).

Since there are 2_<sup>n</sup>_ subsets \(S\subseteq[n]\) with only 2_<sup>n</sup>_-1 possible subset sums \(\sum_{i\in S}w_i\in\)

