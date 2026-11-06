<tbc>and studied in two directions: In \[8\], the authors generalize the Manhattan problem to higher dimension R_<sup>d</sup>_ for \(d\ge 2\). The arbitrary-demand case was suggested in \[4\]. An _O_(log_n_)-approximation algorithm was presented in \[7\], which remains the best known ratio. Our MinGMConn problem can be seen as an analogue of \[7\] in the node-cost setting. We present an improved approximation ratio of \(O(\sqrt{logn})\), therefore, raising the possibility of similar improvements in the edge-cost variants.

**Directed Steiner Forests (DSF).** MinGMConn is a special case of _node-cost directed Steiner forest (DSF):_ Given a directed graph _G_=(_V,E_) and pairs of terminals \(\mathcal{D}\subseteq V\times V\) , find a minimum cardinality subset \(S\subseteq V\) such that _G_\[_S_\] contains a path from _s_ to _t_ for all \((s,t)\in\mathcal{D}\). DSF is known to be highly intractable, with hardness \(2^{log^{1-\epsilon}|V|}\) unless \(\mathsf{NP}\subseteq\mathsf{DTIME}(n^{polylogn})\) \[11\]. The best known approximation ratios are slightly sub-linear \[3, 12\]. Manhattan problems can be thought of as natural, tractable special cases of DSF, with approximability between constant and logarithmic regimes. For more details, see \[8\].

## 1.1 Our Contributions

In this paper, we present both hardness and algorithmic results for MinGMConn.

**Theorem 1.** _The_ MinGMConn _problem is NP-hard, even for an input that contains at most one point per row and column._

This result can be thought of as a first step towards developing structural understanding of Manhattan connectivity with respect to lower bounds. We believe that such an understanding would come in handy in future study of binary search trees in the geometric view.

Next, we present algorithmic results. Due to the BST structures, an _O_(log_n_)-approximation is trivial. The main ingredient in obtaining a sub-logarithmic approximation is an approximation algorithm for the case of "few" _x_-coordinates. More formally, we say that an input instance is _s-thin_ if the points in _P_ lie on at most _s_ different _x_-coordinates.

**Theorem 2.** _There exists an efficient O_(log_s)-approximation algorithm for an s-thin instance_ (_P,D_) _of_ MinGMConn.

In fact, our algorithm produces solutions with \(O(logs\cdot\mathsf{IS}(P,D))\) many points, where \(\mathsf{IS}(P,D)\le\mathsf{OPT}(P,D)\) is the cardinality of a _boundary independent set_ (a notion introduced below). This theorem is tight up to a constant factor, since there exists an input instance (_P,D_) on _s_ different columns such that the \(\mathsf{OPT}(P,D)=\Omega(\mathsf{IS}(P,D)logs)\); see Appendix C.

This theorem, along with the boundary independent set analysis, turns out to be an important building block for our approximation result, which achieves an approximation ratio that is sublogarithmic in _n_.

**Theorem 3.** _There is an efficient_ \(O(\sqrt{logn})\)_-approximation algorithm for_ MinGMConn.

This gives an improvement over the trivial _O_(log_n_)-approximation and may grant some new hope with regards to improving the _O_(log_n_)-approximation for the edge-cost variants.

We provide improved approximation ratios for settings when the graph formed by the demands has a special structure.

**Theorem 4.** _There is an O_(loglog_n)-approximation algorithm for_ MinGMConn _when the demands form a complete k-partite graph._

