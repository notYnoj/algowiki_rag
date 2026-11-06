The analogous edge-deletion problems are also of interest, and have already been studied in the literature. The minimization version is equivalent to finding a matching that has the smallest possible number of blocking pairs. This problem was shown to be NP-hard by Abraham et al. \[1\], even for complete preference lists. The subset version is equivalent to the following: given an edge subset \(F\subseteq E\), is there a matching in _G_ for which every blocking edge is in _F_? This problem is called _stable roommates with free edges_, and was shown to be NP-complete by Cechlárová and Fleiner \[6\].

Among the vertex deletion problems, vertex-del-sr was considered by Tan \[27\] who gave an algorithm based on Irving’s algorithm \[18\]. In the following, we give a significantly simpler algorithm for vertex-del-sr. We also show that vertex-subset-del-sr is NP-complete. The latter implies that finding a minimum weight removable set is NP-complete even for vertex weights in {0,1}, and it is inapproximable, since it is hard to decide if there is a removable set of weight 0.

We show that it is very easy to determine a minimum cardinality removable vertex set using a stable partition. The algorithm is presented as Algorithm 1; it chooses an arbitrary vertex from each odd cycle in the stable partition. Note, however, that a removable set does not necessarily contain a vertex from each odd cycle, so optimality is not obvious. We show the correctness of the algorithm in the proof of the theorem below.

**Theorem 4.** _Algorithm 1 runs in in polynomial time and finds a smallest removable set._

_Proof._ By Theorem 2, the algorithm has polynomial running time. We prove the correctness in two steps. First, we show that Algorithm 1 outputs a removable set.

**Claim 5.** _Algorithm 1 outputs a set_ \(S\subseteq V\) _and a matching M that is stable in G-S._

_Proof._ Let _uv_ be an edge of _G-S_ not in _M_; we show that _uv_ is not a blocking edge. Recall that \(\pi\) denotes the stable partition of (_G,\>_) obtained by applying Tan’s algorithm.

Assume first that at least one of _u_ and _v_ is a singleton in \(\pi\), say, \(\pi(u)=u\). Then for any of its neighbors \(w\in N(u)\), we have \(\pi(w)\neq w\), \(\pi(w)>_wu\), and \(\pi^{-1}(w)>_wu\) since \(\pi\) is a stable partition. In particular, this holds for _v_. Since _v_ is matched to either \(\pi(v)\) or \(\pi^{-1}(v)\) in _M_, _uv_ is not a blocking edge.

Consider the case when \(\pi(u)\neq u\) and \(\pi(v)\neq v\). Since every vertex in _V_\\_S_ that is not a singleton in \(\pi\) gets a partner in _M_, both _u_ and _v_ are matched by the algorithm. If \(u\neq\pi(v)\) and<tbc>

\begin{tabular}{cc}
\multicolumn{2}{c}{VERTEX-DEL-SR} \\
**Input:** & A graph _G_=(_V,E_) with strict preferences _\><sub>v</sub>_ on the vertices and an integer \(k\in\mathbb{Z}_+\). \\
**Question:** & Does there exist a removable set \(S\subseteq V\) such that \(|S|\le k\)? \\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{VERTEX-SUBSET-DEL-SR} \\
**Input:** & A graph _G_=(_V,E_) with strict preferences _\><sub>v</sub>_ on the vertices and a vertex subset \(T\subseteq V\) . \\
**Question:** & Does there exist a removable set \(S\subseteq T\)? \\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{VERTEX-DEL-SQM} \\
**Input:** & A graph _G_=(_V,E_) with strict preferences _\><sub>v</sub>_ and capacities _q(v_) on the vertices, and an integer \(k\in\mathbb{Z}_+\). \\
**Question:** & Does there exist a removable set \(S\subseteq V\) such that \(|S|\le k\)? \\
\end{tabular}

