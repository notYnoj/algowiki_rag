# Maximum Stable Matching with Matroids and Partial Orders <sup>∗</sup>

**Abstract**

The Stable Marriage problem (SM), solved by the famous deferred acceptance algorithm of Gale and Shapley (GS), has many natural generalizations. If we allow ties in preferences, then the problem of finding a maximum stable matching becomes NP-hard, and the best known approximation ratio is 1.5 (McDermid 2009, Paluch 2011, Z. Király 2012), achievable by running GS on a cleverly constructed modified instance. Another elegant generalization of SM is the matroid kernel problem introduced by Fleiner (2001), which is solvable in polynomial time using an abstract matroidal version of GS. Our main result is a simple 1.5-approximation algorithm for the matroid kernel problem when preferences are given as interval orders -- a broad subclass of partial orders that covers many applications beyond preferences with ties. In addition, for the bipartite matching case, we show that the output of our algorithm also 1.5-approximates the LP-optimum of the relaxation of the corresponding Integer Program, which shows that the integrality gap is at most 1.5 for the interval order case. To contrast this with hardness results, we show that if arbitrary partial orders are allowed in the preferences, then even in the bipartite matching case, the problem becomes hard to approximate within a factor better than 2 assuming the Unique Games Conjecture, and the integrality gap becomes 2.

### 1 Introduction

The deferred acceptance algorithm of Gale and Shapley [18] is a quintessential example of a simple combinatorial algorithm that has wide-ranging applications, in such diverse areas as healthcare labor markets, kidney exchange planning, project allocations, and school choice mechanisms. The original stable marriage problem solved by the Gale–Shapley algorithm has been generalized in many directions, and the mathematical research in the area is still thriving, 60 years after the original paper.

The aim of this paper is to bring together two directions in which the problem has been extended. One is the design of approximation algorithms for finding a maximum stable matching when ties are allowed in the preference lists. The other is the generalization of the stable marriage problem to matroid intersection, in particular, the matroid kernel problem introduced and solved by Fleiner [14] using an abstract version of the Gale–Shapley algorithm.

<sup>∗</sup>Some of the results in this paper have appeared in the 6th SIAM Symposium on Simplicity of Algorithms (SOSA 2023) [12] <sup>†</sup>Department of Operations Research, Eötvös Loránd University, Budapest, Hungary, and Mechanism Design Research Group, Institute of Economics and Regional Studies, Budapest, Hungary. Email: `csaji.gergely@krtk.hu`, `csajigergely@student.elte.hu` <sup>‡</sup>ELKH-ELTE Egerváry Research Group, Department of Operations Research, Eötvös Loránd University, Budapest, Hungary. Email: `tamas.kiraly@ttk.elte.hu` <sup>§</sup>Department of Mathematical and Computing Science, School of Computing, Tokyo Institute of Technology, Tokyo, Japan. Email: `yokoi@c.titech.ac.jp`

Gergely Csáji<sup>†</sup>

Tamás Király<sup>‡</sup>

Yu Yokoi<sup>§</sup>

September 11, 2024

arXiv:2208.09583v3 [cs.GT] 9 Sep 2024

