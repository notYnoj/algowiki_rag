of Four Russians, we start by preparing a look-up table containing answers for all Edge Coloring instances of certain small size \(n'\). Because of the truly exponential time complexity of Edge Coloring, the running time of this step is only polynomially slower than solving a single Edge Coloring instance of size \(n'\). Then, using efficient self-reducibility of SAT, we reduce a given CNF formula to a bunch of sufficiently small formulas. Finally, using the assumed fine-grained reduction and the prepared look-up table, we solve SAT for each of the resulting formulas faster than the brute force search.

**Theorem 1.** _If there exists a fine-grained reduction showing that, assuming SETH, Edge Coloring cannot be solved in time_ \(\alpha^{n^2}\)_, for some_ \(\alpha>1\)_, then SETH is false._

_Proof._ Assume that there exists a reduction<tbc>

\((\mathsf{SAT},2^n)\le(\mathsf{Edge Coloring},\alpha^{n^2}).\)

<tbc>This is an algorithm A that checks whether an input formula with _n_ variables is satisfiable by making oracle calls to an algorithm for Edge Coloring. The main property of A is that it solves SAT in time \(2^{(1-\delta)n}\), for a \(\delta>0\), if the oracle solves Edge Coloring in time \(\alpha^{n^2/2}\) for some \(\delta>0\). This implies that if A makes an oracle call to a graph with _t_ nodes, then \(\alpha^{t^2/2}\le 2^{(1-\delta)n}\), hence

\(t\le\left(\frac{2(1-\delta)n}{log_2\alpha}\right)^\frac{1}{2}.\) (2)

Using this observation, we can design a faster than 2_<sup>n</sup>_ algorithm for SAT by designing an efficient oracle for Edge Coloring. To do this, we solve Edge Coloring for every graph with at most _k_=(_n/_2)<sup>1/2</sup> nodes and save the result in a table. Each graph on at most _k_ nodes can be specified by a characteristic 0/1-vector of \(\genfrac(){pt}{2}{k}{2}\) potential edges. Solving Edge Coloring on such a graph takes time \(O^*(2^\genfrac(){pt}{2}{k}{2})\) \[5\]. Hence, the total running time of this stage is<tbc>

\(O^*(2^\genfrac(){pt}{2}{k}{2})=O^*(2^{k^2})=O^*(2^{n/2}).\)

<tbc>To check satisfiability of a given formula _F_ with _n_ variables, branch on all but \(\beta n\) variables, for a parameter \(\beta\) to be chosen later. It suffices to solve SAT for the resulting \(2^{(1-\beta)n}\) formulas. Due to (2), on every such formula, A calls the oracle for Edge Coloring on graphs with at most

\(\left(\frac{2(1-\delta)\beta n}{log_2\alpha}\right)^{1/2}\)

nodes. By choosing \(\beta=\frac{log_2\alpha}{4(1-\delta)}>0\), we ensure that the answers for all such graphs are already in the table (computed at the preprocessing stage). This way, we can answer all oracle calls quickly meaning that A solves SAT for every formula with \(\beta n\) variables in time \(2^{(1-\delta)\beta n}\).

The resulting algorithm for checking satisfiability of a formula with _n_ variables prepares an oracle, branches on all but \(\beta n\) variables, and solves SAT of the resulting \(2^{(1-\beta)n}\) formulas using the algorithm A with the constructed oracle. Its running time is

\(O^*\left(max\left\{2^{n/2},2^{(1-\beta)n}\cdot 2^{(1-\delta)\beta n}\right\}\right)=O^*\left(2^{(1-\sigma)n}\right),\)

where \(\sigma=min\{1/2,\delta\beta\}>0\).

