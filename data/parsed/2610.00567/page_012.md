<tbc>**Theorem 3.** _Given an n-vertex, m-edge host graph H as input, there are_ \(\widetilde{O}(m^2)\)_- time algorithms to detect induced subgraphs for the sixty-five_ 6_-vertex graphs in  4._

_Proof._ For each six-vertex graph _G_, we enumerate all super-graphs that contain _G_ an odd number of times. A table containing these subgraph counts <sup>3</sup> is given in a spreadsheet at `https://github.com/lekhakanjaani/Review/blob/ main/Graphs%20on%206%20vertices%20-%206vertices.csv` provides the corresponding computations for graphs on six vertices, analogous to those for graphs on five vertices available at B. Finally, we give (0,2)-width tree decompositions for these graphs along with automorphism avoiding conditions. The complete table is given in Appendix E.

**Theorem 4.** _Given an m-edge host graph H as input, we can detect whether H has an induced P_<sub>7</sub> _(C_<sub>7</sub>_) in_ \(\widetilde{O}(nm^2)\)_-time._

_Proof._ We enumerate all 7-vertex supergraphs of _P_<sub>7</sub> and _C_<sub>7</sub> that contain them an odd number of times and show that all of them have (1,2)-width tree decompositions and checks that can be implemented in those tree decompositions that would make the number of remaining automorphisms odd. These can be found in Appendix F.

<sup>3</sup> The program generating this table is also given in the same appendix.

