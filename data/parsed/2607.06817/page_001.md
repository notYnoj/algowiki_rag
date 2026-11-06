# Computation of small reflective and dihedral Ramsey numbers

**Abstract**

Throughout, all graphs are simple, finite and have vertex sets of the form {0,1,2_,...,n_-1} for some \(n\in\mathbb{N}\). For graphs _G_ and _H_, and a permutation group \(\Gamma\) on the vertex set of _H_, we say that _H_ is \(\Gamma\)_-embeddable_ in _G_ if there exists a graph homomorphism from _H_ to _G_ of the form \(\psi\circ\varphi\), where \(\varphi\in\Gamma\) and \(\psi\) is an increasing injection. Recently, standard and ordered Ramsey numbers of graphs were unified through the introduction of permutational Ramsey numbers, defined as follows. For graphs _H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_ and permutation groups \(\Gamma_1,\Gamma_2,\dots,\Gamma_k\) on their respective vertex sets, the _permutational Ramsey number_ \(R(H_1^{\Gamma_1},H_2^{\Gamma_2},\dots,H_k^{\Gamma_k})\) is the minimum \(n\in\mathbb{N}\) such that for every _k_-edge-coloring of a complete graph on _n_ vertices, there exists some \(j\in\{1,2,\dots,k\}\) for which _H<sub>j</sub>_ is \(\Gamma_j\)-embeddable in the spanning subgraph of the complete graph comprising the edges of color _j_.

Here, we consider reflective (resp. dihedral) Ramsey numbers, which are a specific class of permutational Ramsey numbers in which each group \(\Gamma_j\) is the reflection group (resp. dihedral group) on the naturally ordered vertex set of _H<sub>j</sub>_. Focusing on the two-color case, we apply the SAT-based approach originally proposed by Poljak for ordered Ramsey numbers and recently extended to cyclic Ramsey numbers. We utilize the Kissat SAT solver to obtain exact values and lower bounds for small reflective and dihedral Ramsey numbers whose two arguments belong to the following graph classes: monotone and alternating paths, monotone cycles, start-central stars, complete graphs and nested matchings. We also derive several general results and formulate conjectures based on the computational findings.

**Keywords:** Ramsey numbers, reflective Ramsey numbers, dihedral Ramsey numbers, permutational Ramsey numbers, SAT.

**Mathematics Subject Classification (2020):** 05D10, 05C55.

### 1 Introduction

We consider all graphs to be undirected, simple and finite, with vertex sets of the form {0,1,2_,...,n_-1} for some \(n\in\mathbb{N}\). For a graph _G_, we denote its vertex and edge sets by _V(G_) and _E(G_), respectively, and write |_G_| for its order. We write _K<sub>n</sub>_ for the complete graph on _n_ vertices. A _k_-edge-coloring of a graph _G_ is a mapping from _E(G_) to {1,2_,...,k_}.

Ramsey theory originates from a theorem of Ramsey [25], which asserts that for any graphs _H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_, every _k_-edge-coloring of _K<sub>n</sub>_ contains a monochromatic copy of _H<sub>j</sub>_ in color _j_, for some \(j\in\{1,2,\dots,k\}\), provided that \(n\in\mathbb{N}\) is sufficiently large. The minimum such _n_ is called the _Ramsey number R(H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_). Although the definition of Ramsey numbers is straightforward, determining their exact values is often remarkably difficult. Indeed, even the diagonal Ramsey number _R(K_<sub>5</sub>_,K_<sub>5</sub>) remains unknown [24]. Ramsey-type phenomena have been investigated in numerous settings over the past century, leading to a rich literature on a variety of combinatorial structures, including hypergraphs, ordered graphs, geometric configurations, and sequences; see [11,13-15,17,20-22,24] and the references therein.

Among the many directions in modern Ramsey theory, ordered Ramsey numbers have received considerable attention in recent years. Given graphs _H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_, the _ordered Ramsey number_ Rord(_H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_) is defined as the minimum \(n\in\mathbb{N}\) such that for every _k_-edge-coloring of _K<sub>n</sub>_, there exists an increasing injective homomorphism from _H<sub>j</sub>_ to the spanning subgraph of _K<sub>n</sub>_ comprising the edges of color _j_, for some \(j\in\{1,2,\dots,k\}\). The systematic study of ordered Ramsey numbers was initiated independently by Balko, Cibulka, Král and Kynčl [2,3], and Conlon, Fox, Lee and Sudakov [10]. For a selection of recent results on the asymptotic properties of ordered Ramsey numbers, see the survey [1] by Balko and the references therein.

<sup>∗</sup>Corresponding author. Email: `ivan.damnjanovic@elfak.ni.ac.rs` (I. Damnjanović).

Ivan Damnjanović<sup>∗</sup><sup>1,2</sup> and Irena Dđević<sup>1</sup>

<sup>1</sup>_Faculty of Electronic Engineering, University of Niš, Aleksandra Medvedeva 4, Niš, 18104, Serbia_

<sup>2</sup>_Faculty of Mathematics, Natural Sciences and Information Technologies, University of Primorska, Glagoljaška 8, Koper, 6000, Slovenia_

arXiv:2607.06817v2 [math.CO] 12 Jul 2026

