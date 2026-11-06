# Independent Set Hardness in Graphs of Bounded Twin-Width and Low-Radius Merge-Width

**Édouard Bonnet** \(\unknown\) **Univers Lyon, CNRS, ENS de Lyon, Université Claude Bernard Lyon 1, LIP UMR5668, France**

**Maël Dumas** \(\unknown\) **Institute of Informatics, University of Warsaw, Poland**

**Julien Duron** \(\unknown\) **Institute of Informatics, University of Warsaw, Poland**

**Abstract**

For every \(\varepsilon>0\), Max Independent Set admits a polynomial-time \(n^\varepsilon\)-approximation algorithm on _n_-vertex graphs of effectively bounded twin-width [Bergé et al., STACS ’23]. The approximation factor actually obtained is more precisely _n_<sup>O(1/loglog_n_)</sup>. Prior to the current paper, no approximation hardness was known for this problem, and the existence of a polynomial-time approximation scheme (PTAS) was repeatedly raised as an open question. We answer this question in a strong sense: We show that there is a constant \(\gamma>0\) such that a polynomial-time \(n^{\gamma/(loglogn)^2}\)-approximation algorithm for Max Independent Set on graphs of twin-width at most 4 would refute the Exponential-Time Hypothesis (ETH). This lower bound further holds if a 4-sequence is provided as part of the input. We show the same hardness of approximation for Min Coloring, which also has a nearly matching _n_<sup>O(1/loglog_n_)</sup>-approximation algorithm on graphs of effectively bounded twin-width.

We also clarify the parameterized complexity of _k_-Independent Set on graphs of bounded radius-_r_ merge-width when the range of _r_ is limited. There is a fixed-parameter tractable algorithm for _k_-Independent Set on graphs given with radius-2<sup>O(_k_<sup>2</sup>)</sup> merge sequences of bounded width [Dreier and Toruńczyk, S ’25]. We complement this result by showing that _k_-Independent Set is W[1]-hard on graphs given with radius-_o(k_) merge sequences of bounded width. We further show that this result also holds for _k_-Dominating Set.

Funding JD received funding from ERC grant BUKA (No. 101126229). MD and JD were supported by the project BOBR that has received funding from ERC under the European Union’s Horizon 2020 research and innovation programme, grant agreement No. 948057.

Acknowledgements We want to thank Karolina Drabik, Jakub Nowakowski, Nikolas Mählmann, and Szymon Toruńczyk for fruitful discussions at an early stage of this project.

### 1 Introduction

The problem of finding in a graph a largest subset of pairwise non-adjacent vertices, Max Independent Set (MIS for short), is NP-complete [20], and very hard to approximate: For any \(\varepsilon>0\), an \(n^{1-\varepsilon}\)-approximation algorithm would imply that P=NP [22, 26]. The best known polynomial-time approximation factor is \(\frac{n(loglogn)^2}{log^3n}\) [18]. In contrast, this central problem enjoys much better approximation algorithms on structured graph classes. A historical example is that of planar graphs where, due to Baker’s shifting technique, a polynomial-time approximation scheme (PTAS) exists [2]. MIS also has a PTAS on minor-free classes [21] and on disk graphs [12]. If a geometric representation is provided, there is, for every \(\varepsilon>0\), an \(n^\varepsilon\)-approximation algorithm for the independence number of the intersection graph of _n_ curves every two of which have at most a constant number of intersections [19], and a quasipolynomial-time approximation scheme (QPTAS) for general string graphs [1].





