Query Complexity of Densest Sub(hyper)graph Problems

**Abstract**

Rubinstein et al. [ITCS ’18] introduce the study of connectivity and minimum cut problems in the cut query model, where an algorithm can only access the edges of a graph through cut queries. In this work, we examine the query complexity of densest subgraph problems. Our first contribution is to generalize the uniform sparsification approach for Densest Subgraph and other heavy subgraph problems to weighted graphs, achieving the following results.

\(\bullet\) A \((1+\varepsilon)\)-approximation for weighted Densest Subgraph in \(O(nlog^2n/\varepsilon^2)\) queries, roughly matching the \(\Omega(n/logn)\) lower bound we prove for randomized algorithms.

\(\bullet\) A \((1+\varepsilon)\)-approximation for weighted Max Cut in \(O(nlog^2n/\varepsilon^2)\) queries. This improves upon the bound of \(O(nlog^3n(logn+1/\varepsilon^2))\) queries achieved by Plevrakis et al. [ICALP ’18], making significant progress towards their lower bound of \(\Omega(n/logn)\) queries.

In contrast, we rule out approximation schemes with truly subquadratic query complexity for Densest _k_-Subgraph and settle its exact query complexity in both the unweighted and deterministic settings.

For hypergraphs, we show cut queries alone cannot achieve \(o(\sqrt{n})\)-approximation for Densest Subhypergraph or _o(n_)-approximation for Densest _k_-Subhypergraph, regardless of the number of queries. Augmenting cut queries with the edge oracle of Chen et al. [ICALP ’21], we overcome this barrier for Densest Subhypergraph and obtain a \((1+\varepsilon)\)-approximation on rank-_r_ hypergraphs using \(O(nrlogn/\varepsilon^2)\) queries. We also extend our Densest _k_-Subgraph hardness results to hypergraphs and prove exponential query lower bounds for exact Densest _k_-Subhypergraph. Lastly, confirming a conjecture of Chakrabarty and Liao [ESA ’26], we show that simulating an add query using cut and is-edge<sup>7</sup> queries requires exponentially-many queries.

### 1 Introduction

In the _cut query model_, the edges of a graph _G_=(_V,E_) are unknown, but we have access to a cut oracle; upon query cut(_S_), the oracle returns the number of edges crossing from _S_ to _V_\\_S_. It is known that a graph can be reconstructed using \(\widetilde{O}(n^2)\) cut queries<sup>1</sup> [19], which is tight by a simple information theoretic argument. Recently, Rubinstein et al. [35] introduced this setting as a computational model for algorithms, circumventing the quadratic barrier for graph reconstruction and solving the global and _s-t_ Min Cut problems in \(\widetilde{O}(n)\) and \(\widetilde{O}(n^{5/3})\) cut

Authors listed in alphabetical order. PNNL Information Release PNNL-SA-228134. <sup>∗</sup>This work was done while the author was an intern at the Pacific Northwest National Laboratory. <sup>1</sup>Throughout, we let \(\widetilde{O}(\cdot)\) hide polylog(_n_) factors. Similarly, we use \(O_\varepsilon(\cdot)\) hide poly\((\varepsilon^{-1})\) factors.

Sinan G. Aksoy<sup>1</sup>, Eli Friedman<sup>∗</sup><sup>2</sup>, Nate Veldt<sup>3</sup>, and Stephen J. Young<sup>1</sup>

<sup>1</sup>Pacific Northwest National Laboratory <sup>2</sup>School of Computing, University of Utah <sup>3</sup>Department of Computer Science and Engineering, Texas A&M University

October 9, 2026

arXiv:2610.17581v1 [cs.DS] 13 Oct 2026

