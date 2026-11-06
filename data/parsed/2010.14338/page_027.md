Another demand we are interested in is the following:

**Definition 34.** Let (_P,D_) be an input to MinGMConn. The input demand _D_ is called _complete bipartite demand_ if _P_ is partitioned into two subsets \(A\cup B\) such that \((p,q)\in D\) if and only if \(p\in A\) and \(q\in B\).

**Lemma 35.** _If there is an_ \(\alpha\)_-approximation for the complete bipartite case, then there is an_ \(O(\alpha)\)_- approximation for two-disk demands. This implies an O_(loglog_n)-approximation for two-disk demand._

_Proof._ Let (_P,D_) be an input such that _D_ is a two-disk demand without isolated vertices, i.e., every point in _P_ is part of at least one demand. Define \(D_A=D\cap(A\times A)\) and \(D_B=D\cap(B\times B)\). Using the algorithm for unit-disk demands, we have an algorithm satisfying _D<sub>A</sub>_ and _D<sub>B</sub>_ using at most _O_(OPT(_A,D<sub>A</sub>_)) and _O_(OPT(_B,D<sub>B</sub>_)) points respectively, which is together _O_(OPT(_P,D_)).

Consider the grid G of size _r<sub>B</sub>/_2 used to satisfy _D<sub>B</sub>_. For each point _p_ in _A_ consider the cell \(C\in\mathcal{C}\) that contains that point. As before, \((p,q)\in D\) only for those points \(q\in C'\) such that _C_ and \(C'\) are in close proximity (that is, constant grid cells away from each other.) By projecting _p_ in each direction to the two closest grid lines, we use _O_(OPT(_P,D_)) points and satisfy all demand pairs between _A_ and _B_ for which both points lie in different grid cells. Within a cell, the remaining demands are complete bipartite. Hence, if we have an \(O(\alpha)\)-approximation for the complete bipartite case we will have a \(O(\alpha)\)-approximation for this case.

