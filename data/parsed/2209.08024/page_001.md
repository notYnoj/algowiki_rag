# Fast approximation of search trees on trees with centroid trees

**Abstract**

Search trees on trees (STTs) generalize the fundamental binary search tree (BST) data structure: in STTs the underlying search space is an arbitrary tree, whereas in BSTs it is _a path_. An optimal BST of size _n_ can be computed for a given distribution of queries in O(_n_<sup>2</sup>) time [Knuth, Acta Inf. 1971] and _centroid_ BSTs provide a nearly-optimal alternative, computable in O(_n_) time [Mehlhorn, SICOMP 1977].

By contrast, optimal STTs are not known to be computable in polynomial time, and the fastest constant-approximation algorithm runs in O(_n_<sup>3</sup>) time [Berendsohn, Kozma, SODA 2022]. Centroid trees can be defined for STTs analogously to BSTs, and they have been used in a wide range of algorithmic applications. In the unweighted case (i.e., for a uniform distribution of queries), the centroid tree can be computed in O(_n_) time [Brodal, Fagerberg, Pedersen, Östlin, ICALP 2001; Della Giustina, Prezza, Venturini, SPIRE 2019]. These algorithms, however, do not readily extend to the weighted case. Moreover, no approximation guarantees were previously known for centroid trees in either the unweighted or weighted cases.

In this paper we revisit centroid trees in a general, weighted setting, and we settle both the algorithmic complexity of constructing them, and the quality of their approximation. For constructing a weighted centroid tree, we give an _output-sensitive_ \(\mathcal{O}(nlogn)\subseteq\mathcal{O}(nlogn)\) time algorithm, where _h_ is the height of the resulting centroid tree. If the weights are of polynomial complexity, the running time is O(_n_loglog_n_). We show these bounds to be optimal, in a general decision tree model of computation. For approximation, we prove that the cost of a centroid tree is at most _twice_ the optimum, and this guarantee is best possible, both in the weighted and unweighted cases. We also give tight, fine-grained bounds on the approximation-ratio for bounded-degree trees and on the approximation-ratio of more general \(\alpha\)-centroid trees.

### 1 Introduction

Search trees on trees (STTs) are a far-reaching generalization of binary search trees (BSTs), modeling the exploration of tree-shaped search spaces. Given an undirected tree T , an STT on T is a tree rooted at an arbitrary vertex _r_ of T , with subtrees built recursively on the components resulting after removing _r_ from T , see Figure 1 for an example. BSTs correspond to the special case where the underlying tree T is a _path_.

STTs and, more generally, search trees on graphs arise in several different contexts and have been studied under different names: _tubings_ [CD06], _vertex rankings_ [DKKM94, BDJ<sup>+</sup>98, ES14], _ordered color- ings_ [KMS95], _elimination trees_ [Liu90, PSL90, AH94, BGHK95]. STTs have been crucial in many algorithmic applications, e.g., in pattern matching and counting [Fer13, KPR<sup>+</sup>14, GHLW15], cache-oblivious data struc- tures [BFCK06, FV16], tree clustering [FJ83], geometric visibility [GHL<sup>+</sup>87], planar point location [GT98], distance oracles [CGMW21]. They arise in matrix factorization (e.g., see [DER17, § 12]), and have also been related to the competitive ratio in certain online hitting set problems [ES14].

<sup>∗</sup>Institut für Informatik, Freie Universität Berlin, Germany. Email: `beab@zedat.fu-berlin.de`. Supported by DFG grant KO 6140/1-1. <sup>†</sup>Blavatnik School of Computer Science, Tel Aviv University, Israel. Email: `ishayg@mail.tau.ac.il`. Supported by ISF grant no. 1595-19 and the Blavatnik Family Foundation. <sup>‡</sup>Blavatnik School of Computer Science, Tel Aviv University, Israel. Email: `haimk@tau.ac.il`. Supported by ISF grant no. 1595-19 and the Blavatnik Family Foundation. <sup>§</sup>Institut für Informatik, Freie Universität Berlin, Germany. Email: `laszlo.kozma@fu-berlin.de`. Supported by DFG grant KO 6140/1-1.

Benjamin Aram Berendsohn<sup>∗</sup><br>
Ishay Golinsky<sup>†</sup><br>
Haim Kaplan<sup>‡</sup><br>
László Kozma<sup>§</sup>

