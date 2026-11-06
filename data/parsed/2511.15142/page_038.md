where the graph at this point is a contraction of the original, so the current vertex set _V_ may consist of disjoint subsets of the original vertices (which poses no issue). The algorithm then outputs the best cut among a small collection of candidate cuts, which can be selected using cut comparisons.<br>
Notably, the identity

\(argmin_{u\in V\backslash S}\big(w(\partial(S+u))-w(\partial u)\big)=argmin_{u\in V\backslash S}w(\partial(S,u))\)

implies that the Nagamochi-Ibaraki algorithm can also be implemented under the second, arbitrary- set comparison model. Finally, the Nagamochi-Ibaraki algorithm has a natural extension to general non-negative symmetric submodular functions, as shown by \[Que98\].

## D.4 Illustrative Examples

### D.4.1 Separations between Comparison and Value Queries

In the weighted setting, consider taking two disjoint cycles _C_<sub>1</sub> and _C_<sub>2</sub> of _k=n/_2 vertices and with unit-weight edges, and adding in a perfect matching of size _k_ between them, with edges of cost \(\varepsilon\). This is the _circular ladder graph_, with cross-edge weight \(\varepsilon\).

**Claim D.7.** _There exist non-adaptive algorithms making O(n_<sup>2</sup>) _value queries to sets of size one and two that can reconstruct any graph, but for any non-adaptive algorithm in the comparison-query model making queries to sets of constant size (or even_ \(\checkmark n/2\) _size), there exist weighted n-vertex graphs G_<sup>+</sup>_,G_<sup>-</sup> _which cannot find the minimum cut._

_Proof._ Take the circular ladder graph with \(\varepsilon=\frac{2}{k-1}\pm\gamma\) for some tiny \(\gamma>0\); the sign in front of the \(\gamma\) will determine whether the min-cut is a single-vertex cut with cost \(2+\varepsilon\), or the bisection (_C_<sub>1</sub>_,C_<sub>2</sub>) with cost \(k\varepsilon\). However, we cannot distinguish these two cases if we compare sets _S,T_ of size \(\checkmark n/2\). (This is true even if we know the edges of the graph and the entire construction, except the sign in front of \(\gamma\). This is in contrast to the value query setting, where asking the value of _f(S_) for sets of size 1 and 2 allows us to completely reconstruct the graph.

**Claim D.8.** _There exist non-adaptive algorithms making O(n_<sup>2</sup>) _value queries to reconstruct the graph, but for any non-adaptive algorithm in the comparison-query model, there exist weighted n- vertex graphs G_<sup>+</sup>_,G_<sup>-</sup> _which require_ exp(_n_) _comparison queries to have high success probability._

_Proof._ Again, take the circular ladder graph, and rename the vertices uniformly at random. Assume that the cross-edge weight is \(\varepsilon=\frac{2}{k-1}\pm\gamma\) for some tiny \(\gamma>0\); the sign in front of the \(\gamma\) will determine whether the degree cut or the partition (_C_<sub>1</sub>_,C_<sub>2</sub>) is optimal. Again, for value queries we can non- adaptively reconstruct the graph using _O(n_<sup>2</sup>) queries. But for comparison queries, the only way to learn the sign in front of \(\gamma\) would be to query the correct partition with a degree cut. Now if the queries are non-adaptive, and the vertices of the graph have been uniformly and randomly renumbered, the number of non-adaptive queries would have to be exponential in _n_ in order to have a high probability of success.

### D.4.2 Non-Reconstructable Graphs

The unweighted graph pairs \((K_2,\bar{K}_2)\) and \((K_3,\bar{K}_3)\) are not distinguishable, since essentially the only feasible sets _S_ are singleton sets (recall that by symmetry, \(f(S)=f(\bar{S})\)), and all of them have the same cut value. However, as we showed in Theorem 1.7, we can recover all unweighted simple graphs other than \(K_2,\bar{K}_2,K_3,\bar{K}_3\) using comparison queries.

