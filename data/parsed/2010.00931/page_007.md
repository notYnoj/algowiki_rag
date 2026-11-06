<tbc>up to some constant factor. As mentioned, this (conjectured) property of Splay trees is called _dynamic optimality_. Since the generalization of Splay to SplayTT appears quite natural, we propose the following open question that subsumes classical dynamic optimality.

**Open question.** _Is SplayTT dynamically optimal in the STT model?_

A further natural question is whether Greedy BST can be similarly extended to the STT setting. The linear-time transformation between Steiner-closed trees (Theorem 2) suggests a possible generalization, but its analysis appears to require the development of further tools, which we leave to future work.

**Further related work.** As mentioned, concepts related to STTs and more broadly to search trees on graphs have been studied in various contexts by different communities. Apart from the work of Bose et al. \[BCI<sup>+</sup>20\], that is closest in spirit to ours, earlier work has largely focused on _minimum height_, i.e. the problem of computing the treedepth, or considered different models where queries are for _edges_, see e.g. \[BFN99, LN01, MOW08, OP16\], or relatedly, searching in posets \[LS85b, LS85a, CDKL04, HIT11\].

In the edge-query model, search distributions (in the sense of Theorem 1) have also been considered, and constant-approximations are known, with the existence of a PTAS remaining open \[LM11, CJLM11, CJLM14\]. We remark that results do not directly transfer between the vertex-query and edge-query models.

Other related, but not directly comparable work includes searching with weighted queries \[DKUZ17\], searching with an oracle that identifies a shortest-path edge towards the target \[EKS16\], or searching with errors (stochastic or adversarial) \[BK93, FRPU94, KK07, FGI07, BKR18\]. Search trees on graphs and trees have also been motivated with practical applications including file system synchronisation \[BFN99, MOW08\], software testing \[BFN99, MOW08\], asymmetric communication protocols \[LM11\], VLSI layout \[Lei80\], and assembly planning \[IRV88\]. Even and Smorodinsky \[ES14\] relate STTs with the competitive ratio of certain online hitting set problems.

**2. Preliminaries**

We use standard terminology on trees and graphs. A _subtree_ of an undirected tree is a connected subgraph. The set of nodes of a tree _S_ is denoted _V(S_). The subgraph of _S_ induced by node set _A_ is denoted _S_\[_A_\]. By _S_\\_x_ we denote the forest obtained by deleting node _x_ in tree _S_. We say that _z separates x and y_, if _x_ and _y_ fall into different connected components of _S_\\_z_, or equivalently if _z_ is on the path between _x_ and _y_ in _S_. The _convex hull_ of a set of nodes \(A\subseteq V(S)\), denoted `ch`(_A_) is the subtree of _S_ induced by the union of all paths between nodes in _A_.

For a rooted tree _T_ and a node \(x\in V(T)\) we denote by _T<sub>x</sub>_ the subtree of _T_ rooted at _x_. The _search path_ of \(x\in V(T)\) in _T_ is the unique path from the root to _x_. The number of nodes on the search path of _x_ in _T_ is `depth`_<sub>T</sub>(x_). Denoting the root of _T_ as `root`(_T_), we have `depth`_<sub>T</sub>_(`root`(_T_))=1.

