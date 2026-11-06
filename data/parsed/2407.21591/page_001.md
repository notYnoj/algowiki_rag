Simpler Optimal Sorting from a Directed Acyclic Graph

**Abstract**

Fredman proposed in 1976 the following algorithmic problem: Given are a ground set _X_, some partial order _P_ over _X_, and some comparison oracle _O<sub>L</sub>_ that specifies a linear order _L_ over _X_ that extends _P_. A _query_ to _O<sub>L</sub>_ has as input distinct \(x,x'\in X\) and outputs whether \(x<Lx'\) or vice versa. If we denote by _e(P_) the number of linear orders that extend _P_, then it follows from basic information theory that log_e(P_) is a worst-case lower bound on the number of queries needed to output the sorted order of _X_.

Fredman did not specify in what form the partial order is given. Haeupler, Hladík, Iacono, Rozhon, Tarjan, and Tˇtek (’24) propose to assume as input a directed acyclic graph, _G_, with _m_ edges and _n_=|_X_| vertices. Denote by _P<sub>G</sub>_ the partial order induced by _G_. Their algorithmic performance is measured in running time and the number of queries used, where they use \(\Theta(m+n+loge(P_G))\) time and \(\Theta(loge(P_G))\) queries to output _X_ in its sorted order. Their algorithm is worst-case optimal in terms of running time and queries, both. Their algorithm combines topological sorting with heapsort. Their analysis relies upon sophisticated counting arguments using entropy, recursively defined sets defined over the run of their algorithm, and vertices in the graph that they identify as bottlenecks for sorting.

In this paper, we do away with sophistication. We show that when the input is a directed acyclic graph then the problem admits a simple solution using \(\Theta(m+n+loge(P_G))\) time and \(\Theta(loge(P_G))\) queries. Especially our proofs are much simpler as we avoid the usage of advanced charging arguments and data structures, and instead rely upon two brief observations.

Funding. Ivor van der Hoog received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 899987. Daniel Rutschmann and Eva Rotenberg received funding from Carlsberg Foundation Young Researcher Fellowship CF21-0302 “Graph Algorithms with Geometric Applications”. Eva Rotenberg additionally receives funding from DFF Grant 2020-2023 (9131-00044B) “Dynamic Network Analysis”, and VILLUM Foundation grant VIL37507 “Efficient Recomputations for Changeful Problems”.

## 1 Introduction

Sorting is a fundamental problem in computer science. In 1976, Fredman introduced a natural generalisation of sorting, namely sorting under partial information [4]:

Given a ground set _X_ of size _n_, and some partial order _P_ on _X_, and an oracle _O<sub>L</sub>_ with access to a ground-truth linear order _L_ of _X_, the task is to minimise the number of oracle queries to recover the linear order of _X_. A query takes two input elements from _X_, and outputs their relation in the linear order. Algorithmic efficiency is measured in time, and the number of queries used. Let _e(P_) denote the number of linear orders that extend the partial order _P_. Then, for any binary (e.g. yes/no) query, \(\lceil log_2(e(P))\rceil\) is a worst-case lower bound for the number of queries needed, simply because the sequence of answers should be able to lead to any possible extension of the order.

Ivor van der Hoog, Eva Rotenberg, Daniel Rutschmann. Technical University of Denmark, DTU

arXiv:2407.21591v6 [cs.DS] 7 Feb 2026

