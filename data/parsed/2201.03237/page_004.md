<tbc>_O(n_<sup>2</sup>_m_) where _n_ is the size of nodes and _m_ is the size of neighbors, which is unacceptable. Therefore, in order to approximate a (_r,p_)-MSNET and reduce the complexity, we propose TBSG (Tree-based Search Graph). The index complexity of TBSG is close to _O(n_) and it is applicable for many datasets. The detail of TBSG can be seen in Section 3.

The main contribution can be summarized as follows:

1. We propose the (_r,p_)-MSNET to match the query scenarios better.<tbc>

2. We propose a new graph-based algorithm, called TBSG, which is an approximation of (_r,p_)-MSNET with low index complexity.<tbc>

3. We conduct experiment on four million-scaled datasets. The result shows that TBSG yields better or comparable search performance than all recent state-of-the-art algorithms.

First we introduce the definition of ANNS, and then introduce the related work. For convenience, some frequently used notations are listed in  1.

Q
Q
E
E
C
C
F
A
B
F
A
B
D
D
G
G

Figure 1: The left graph adopts NSSG ’s strategy and point _A_ will connect all other points. While in the right graph point _A_ only connects points _B_, _C_, _D_. For the search with _Q_ as query and starting from point _A_, in left graph it needs to calculate the distance between 6 neighbors and _Q_, while in right graph it will visit points _B_, _C_, _D_ and find point _C_ is closer to _Q_ and _E_, _F_ are visited later. So in right graph it only need to evaluate 5 points-_B_, _C_, _D_, _E_, _F_.

