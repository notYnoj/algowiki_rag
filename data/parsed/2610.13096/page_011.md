and hence _M(S_)=_N(S_). Thus, under any perfect matching, _S_ corresponds to a nonempty proper vertex subset of _D<sub>M</sub>_ with no arcs leaving it. The choice of perfect matching cannot change the outcome of the strong-connectivity test. Combining this equivalence with the projection theorem gives

\(G\text{contains a small blocking set}\Longleftrightarrow D_M\text{is not strongly connected.}\)

When _D<sub>M</sub>_ is not strongly connected, its condensation digraph is a directed acyclic graph (DAG) with at least two vertices, and hence has a sink SCC _C_. As _C_ has no arcs to vertices outside it, consider \(T_C=\{x_i:i\in C\}\). Since \(T_C\subseteq I\) and _I_ is independent, every neighbor of _T<sub>C</sub>_ lies in _J_. The matching edges guarantee

\(\{y_i:i\in C\}\subseteq N(T_C),\)

while the absence of arcs leaving _C_ guarantees that _T<sub>C</sub>_ is not adjacent to any _y<sub>j</sub>_ with \(j\notin C\). Therefore,

\(N(T_C)=\{y_i:i\in C\},\)

so |_T<sub>C</sub>_|=|_N(T<sub>C</sub>_)|. Moreover,

\(0<|T_C|<|I|=\frac{n}{2}.\)

Since \(T_C\subseteq I\) is independent, it is a small blocking set.

If _D<sub>M</sub>_ is strongly connected, its only SCC corresponds to the entire set _I_, whose cardinality is _n/_2, so it cannot be output as a small blocking set. The equivalence above requires the algorithm to return `NO` in this case.

## 5.2. Algorithmic framework

**Algorithm 1: Small blocking set detection and construction.**

**Input:** A connected simple graph _G_=(_V,E)._

**Output:** A small blocking set, or `NO`.

1. If \(n\le 1\), return `NO`.<tbc>

2. Compute a maximum-cardinality CIS _I_ using Larson’s algorithm, and set \(\delta=|I|-|N(I)|\).<tbc>

3. If \(\delta>0\), apply the vertex-deletion construction of Lemma 1 and return the resulting small blocking set _S_.<tbc>

4. If \(\delta=0\) and \(I=\varnothing\), return `NO`.<tbc>

