# Detection and Construction of Small Blocking Sets via Critical Independent Sets and Matching Decomposition

Quanlong Niu<sup>a</sup>, Riheng Jia<sup>b,∗</sup>

<sup>_a_</sup>_School of Big Data and Artificial Intelligence, Fuyang University of Technology, Fuyang, 236000, Anhui, China_

<sup>_b_</sup>_School of Computer Science and Technology, Zhejiang Normal University, Jinhua, 321004, Zhejiang, China_

**Abstract**

The small blocking set detection and construction problem asks whether a given connected simple graph contains a nonempty independent set whose cardinality equals the size of its neighborhood and is strictly less than half the number of vertices, and, if so, how to construct such a set. Previous work characterized restless explorability in vertex-permuted temporal graphs using small blocking sets, but left the computational complexity of detecting their existence as an open problem. We give a polynomial-time algorithm for detection and construction. Specifically, we first compute a maximum-cardinality critical independent set and use its difference and cardinality to handle the cases that admit an immediate solution. In the remaining boundary case, where the critical difference is zero and the selected independent set contains exactly half the vertices, we establish a projection theorem using a perfect matching and neighborhood counting: the graph contains a small blocking set if and only if the selected independent set contains a nonempty proper tight subset. We then use matching contraction to translate the tight-subset condition into the absence of arcs leaving a vertex subset in an auxiliary digraph. This yields a strong-connectivity test for the existence of a small blocking set and, when one exists, a construction based on a sink strongly connected component. The result resolves the open complexity question for small blocking set detection and provides an explicit construction algorithm.

<sup>∗</sup>Corresponding author _Email address:_ `rihengjia@zjnu.edu.cn` (Riheng Jia)

