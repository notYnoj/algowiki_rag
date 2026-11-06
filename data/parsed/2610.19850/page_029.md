## 4.1 Presentation of the algorithm: an extension of Bouchitté-Todinca method

Our algorithm PMC-Traversal can be seen as an extension of BT-Enum. We will keep its outline while improving the bottleneck step. Indeed, the fourth step of BT-Enum determines completely its worst-case time complexity. For the three first steps, we still do the same as BT-Enum, since these steps already cost output-linear time. Then, for the fourth step, we will search for the _a_-nice PMCs of _G_ in a BFS manner, starting from the PMCs enumerated in the three first steps. In fact, we will navigate in a "supergraph of solutions" which admits PMCs as vertices and is directed. Its arcs will be defined through a neighborhood function N. We will then show that all _a_-nice PMCs of _G_ can be found by exploring this (partially unknown) supergraph, starting from PMCs which are not _a_-nice.

We define the notion of _neighborhood_ between PMCs.

**Definition 20** (PMC neighborhood)**.** _We define the_ PMC neighborhood N _as a set of ordered pairs of PMCs. Given two PMCs_ \(\Omega'\) _and_ \(\Omega\) _of G, the ordered pair_ \((\Omega',\Omega)\in\mathcal{N}\) _if_ \(\Omega\) _can be obtained from_ \(\Omega'\) _via the following process:_

1. _Guess some vertex_ \(u^*\in\Omega'\) _and fix_ \(X^*=\Omega'\cup N_G(u^*)\).<tbc>

2. _Guess a second vertex_ \(b^*\in\Omega'\) _and compute the X_<sup>∗</sup>_-close_ (_b_<sup>∗</sup>_,u_<sup>∗</sup>)_-separator S_<sup>∗</sup>.<tbc>

_3._ _Keep only the vertices of X_<sup>∗</sup> _which belong to_ \(C_G[b^*,S^*]=S^*\cup C_G(b^*,S^*)\)_, then_ \(\Omega=X^*\cap C_G[b^*,S^*]\).

_We can also write_ \(\Omega\in\mathcal{N}(\Omega')\) _instead of_ \((\Omega',\Omega)\in\mathcal{N}\).

\(\text{\textbf{Algorithm 2:} PMC-BFS
1: \textbf{Input:} A graph}G\text{and a set}\widehat{\Pi}\text{containing some PMCs of}G\text{.
2: \textbf{Output:} A set}\Pi\text{containing PMCs of}G\text{, with}\widehat{\Pi}\cap\Pi=\emptyset\text{.
3:}\Pi\leftarrow\emptyset\text{\# Result of PMC-BFS, initially fixed as empty \#
4:}L\leftarrow\widehat{\Pi}\text{\# Queue of the BFS \#
5: \textbf{while}}L\text{\textit{is not empty do}
6:}\Omega'\leftarrow\text{First PMC of}L\text{7:}L\leftarrow L\backslash\Omega'\text{8: \textbf{for}}\Omega\in\mathcal{N}(\Omega')\text{\textbf{do
9: \textbf{if}}}\Omega\notin(\Pi\cup\widehat{\Pi})\text{\textbf{then
10:}}\Pi\leftarrow\Pi\cup\{\Omega\}\text{11:}L\leftarrow L\cup\{\Omega\}\text{12: \textbf{return}}\Pi\)

This neighborhood function size is polynomial in the graph size: concretely, every PMC admits at most _n_<sup>2</sup> PMC out-neighbors. Computing the out-neighbors of some given PMC consists in guessing two vertices of the input graph and then applying several deterministic rules. Observe that given an arbitrary PMC \(\Omega'\) and two of its vertices _u_<sup>∗</sup>_,b_<sup>∗</sup>, it is possible that the process of Definition 20 does not produce a PMC (Figure 9). Therefore, we only keep in collection N the pairs \((\Omega',\Omega)\) for which the result returned by the process is indeed a<tbc>

