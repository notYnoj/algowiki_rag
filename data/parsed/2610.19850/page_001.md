Output-linear time enumeration of potential maximal cliques<sup>∗</sup>

**Abstract**

First defined by Bouchitté and Todinca, Potential Maximal Cliques (PMC) are a well studied notion in graph theory due to its numerous applications. The PMCs of an undirected graph _G_ are defined as the maximal cliques of the minimal triangulations of _G_. Their number can be exponential in the size of the graph. PMCs were crucial in the design of a polynomial-time algorithm which solves Maximum Weight Independent Set on _P_<sub>6</sub>-free graphs (Grzesik, Klimošová, Pilipczuk, Pilipczuk, 2020). They also play a central role in the proposal of a polynomial-time algorithm to solve Largest Induced Subgraph of treewidth \(\le t\) (Fomin, Todinca, Villanger, 2013).

Last but not least, certainly one of the main application of PMCs is the existence of an exact dynamic-programming algorithm to determine the treewidth of a graph (Fomin, Kratsch, Todinca, Villanger, 2008) which uses its list of PMCs as an input. In fact, the enumeration of PMCs stands as the bottleneck for the computation of treewidth with this method: the PMC-enumeration step takes output-quadratic time (Bouchitté, Todinca, 2002) while the dynamic-programming one takes a time linear in the number of PMCs. This two-step procedure was proven to be among the most performing approaches in practice to determine treewidth.

Answering a longstanding open question, we propose an algorithm to enumerate PMCs in output-linear time, _i.e._ a running time linear in the number of PMCs. This offers nice perspectives not only from the theoretical viewpoint - better running time for the PMC- based methods determining treewidth, for Minimum Fill-In and Largest Induced Subgraph of treewidth \(\le t\) - but also from the practical side, with the possibility to propose top-performance implementation.

<sup>∗</sup>This work was supported by the French "Agence Nationale de la Recherche" project SPAWN (ANR-25CE48-1750) and project MIAI (ANR-23-IACL-0006). <sup>†</sup>Corresponding author

arXiv:2610.19850v3 [cs.DS] 20 Oct 2026

Pierre Bergé<sup>1</sup>, Vincent Limouzy<sup>2</sup>, and Nicolas Schivre<sup>†</sup><sup>2</sup>

<sup>1</sup>Université Grenoble Alpes, CNRS, Grenoble INP, LIG, 38000 Grenoble, France

<sup>2</sup>Université Clermont-Auvergne, CNRS, Mines de Saint-Etienne, Clermont-Auvergne-INP, LIMOS, 63000 Clermont-Ferrand, France

