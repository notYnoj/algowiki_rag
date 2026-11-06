## 1 Introduction

Cycle packing is a fundamental optimization problem in which one seeks to find the maximum number of edge- (or vertex-) disjoint cycles in a graph. The authors in \[4, 3\] initiated the study of Edge-Disjoint Shortest Cycle Packing and Vertex-Disjoint Shortest Cycle Packing, the problems where one seeks a packing of _k_ shortest (minimum-weight) edge- (or vertex-) disjoint cycles, respectively. They showed that both packing problems are solvable in time _n_<sup>O(_k_<sup>6</sup>)</sup>, while ruling out a kernel of size polynomial in _k_ under standard complexity assumptions. Our first theorem resolves the FPT vs. W\[1\]-hard question left open in \[3\].

**Theorem 1.1.** Edge-Disjoint Shortest Cycle Packing _is W\[1\]-hard parameterized by k on unweighted subcubic graphs._

Since two cycles in a subcubic graph are edge-disjoint if and only if they are vertex-disjoint, we immediately obtain the hardness for the vertex-disjoint variant of the problem.

**Corollary 1.1.** Vertex-Disjoint Shortest Cycle Packing _is W\[1\]-hard parameterized by k on unweighted subcubic graphs._

Theorem 1.1 rules out fixed-parameter tractability under standard assumptions for general graphs. For planar graphs, the authors in \[4, 3\] showed that Edge-Disjoint Shortest Cycle Packing admits a kernel with O(_k_<sup>2</sup>) vertices and an algorithm running in time \(k^{\mathcal{O}(k)}\cdot n^{\mathcal{O}(1)}\), and asked explicitly whether a _single-exponential_ algorithm with running time \(2^{\mathcal{O}(k)}\cdot n^{\mathcal{O}(1)}\) exists.

Our next theorem resolves a more general question than what was asked in \[3\]. It works for a natural relaxation of edge-disjointness: for an integer \(d\ge 0\), two cycles _C_<sub>1</sub> and _C_<sub>2</sub> are _d-diverse_ if \(w(E(C_1)\cap E(C_2))\le d\), that is, the total weight of shared edges is at most _d_. Edge-disjointness is the special case _d_=0. Building on this, we introduce the following problem, which simultaneously captures edge-disjoint shortest cycle packing, the search for diverse shortest cycles, and the problem of maximizing edge coverage by shortest cycles.

The framework of Diverse Shortest Cycle Coverage captures several problems of independent interest.

• **Edge-disjoint Packing.** Taking _d_=0 (or equivalently \(\ell=k\cdot g(G)\)) forces the _k_ cycles to be pairwise edge-disjoint, recovering Edge-Disjoint Shortest Cycle Packing exactly.<tbc>

• **Diverse Shortest Cycles.** Taking \(\ell=0\) removes the coverage requirement, leaving the problem of finding _k_ shortest cycles that are pairwise _d_-diverse. This fits within the growing literature on _diversity_ in combinatorial optimization \[2, 15, 17\]: rather than a single optimal solution, one seeks a collection of near-optimal solutions that are spread out in a meaningful<tbc>

\begin{tabular}{cc}
\multicolumn{2}{c}{Diverse Shortest Cycle Coverage (DSCC)} \\
_Input:_ & A weighted graph _G_ with weight function \(w:E(G)\rightarrow\mathbb{Z}_{>0}\), and integers \\
 & _k,d_, and \(\ell\). \\
_Task:_ & Decide whether there exists a set C={_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>k</sub>_} of exactly _k_ many pairwise _d_-diverse shortest cycles of _G_ such that the weight of the set of edges covered by these cycles is at least \(\ell\), that is, \(w\left(\bigcup_{i=1}^kE(C_i)\right)\ge\ell\). \\
\end{tabular}

