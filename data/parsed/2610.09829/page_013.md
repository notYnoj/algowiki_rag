<tbc>over a finite alphabet \(\Sigma\). An instance of _L_ is a pair (_x,k_), where \(x\in\Sigma^*\) is the input and \(k\in\mathbb{N}\) is the _parameter_. A parameterized problem is _fixed-parameter tractable_ (FPT, for short) if it can be solved in time \(f(k)\cdot|x|^{\mathcal{O}(1)}\) for some computable function _f_. The class FPT consists of all fixed-parameter tractable parameterized problems.

For two parameterized problems \(A,B\subseteq\Sigma^*\times\mathbb{N}\), a _parameterized reduction_ from _A_ to _B_ is an algorithm which given an instance (_x,k_) of _A_ produces an equivalent instance \((x',k')\) of _B_ in time \(f(k)\cdot|x|^{\mathcal{O}(1)}\) and the parameter \(k'\le g(k)\) for some computable functions _f_ and _g_.

The standard approach to ruling out the existence of an FPT-algorithm for a parameterized problem, under the standard assumptions in parameterized complexity that \(\mathsf{FPT}\neq W[1]\), is to prove that the problem is _W_\[1\]_-hard_. In particular, if there exists a _parameterized reduction_ from a _W_\[1\]-hard parameterized problem _A_ to a parameterized problem _B_, then _B_ is also _W_\[1\]-hard.

## 4 Hardness of Edge-Disjoint Shortest Cycle Packing

In this section, we prove Theorem 1.1. We restate it here for the reader’s convenience.

**Theorem 1.1.** Edge-Disjoint Shortest Cycle Packing _is W\[1\]-hard parameterized by k on unweighted subcubic graphs._

We reduce from a well-known W\[1\]-hard problem called Multicolored Clique \[14, 22\], which is formally defined below.

Let (_G,V_<sub>1</sub>_,V_<sub>2</sub>_,...,V<sub>h</sub>_) be an instance of Multicolored Clique. We assume that \(h\ge 3\), as otherwise the instance can be resolved in polynomial time. Furthermore, we assume that for all distinct \(i,j\in[h]\), the number of edges in _G_ with one endpoint in _V<sub>i</sub>_ and the other in _V<sub>j</sub>_ is exactly the same integer \(m\ge 1\). If this is not the case, then we can add edges with their endpoints in _V<sub>i</sub>_ and _V<sub>j</sub>_ forming connected components of the graph. Since \(h\ge 3\), this does not change the answer. Finally, we assume that for all \(i\in[h]\), the size of _V<sub>i</sub>_ is the same integer \(n\ge 1\) (otherwise, we can add isolated vertices without changing the answer).

We set \(\ell=(hm+1)(2m+1)n\) and define \(L=2\ell\). We construct the graph \(G'\) with \(g(G')=L\). In the construction, we use two blocks, called _edge_ and _vertex selection gadget_, respectively. Copies of the edge selection gadgets are constructed for all pairs of indices \(i,j\in[h]\) such that _i\<j_. The crucial property of the gadget is that it allows us to choose exactly _m_ sets of four edge-disjoint shortest cycles corresponding to the selection of one edge in _G_ with its endpoints in _V<sub>i</sub>_ and _V<sub>j</sub>_. We construct a copy of the vertex selection gadget for each \(i\in[h]\). This gadget has _n_ possibilities to choose sets of pairs of edge-disjoint shortest cycles, and each choice corresponds to the selection of a vertex of _V<sub>i</sub>_. In the final stage of our reduction, we construct \(G'\) using edge and vertex selection gadgets to ensure that \(G'\) has \(k=2h+4\genfrac(){pt}{2}{h}{2}\) edge-disjoint shortest cycles if and only if _G_ has a multicolored clique of size _h_.

Multicolored Clique parameterized by h
Input:
A graph G with a partition V1,V2,...,Vh of V(G).
Task:
Decide whether there is a clique X V(G) such that for each i [h],
|X Vi
= 1.

