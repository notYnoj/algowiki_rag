• if no edge on \(\pi_{b,v_i(h)}\) had its weight decreased since the data structure was initialized: then we use the trees \(\overleftarrow{T}'_{v_i(h)}\) and \(\overleftarrow{T}'_{u^t}\), starting at vertex _b_, we use binary search on the parameter _d_ in the level ancestor data structures to detect which boundary vertex \(b'\) in \(\partial_childP\) is the last on the shortest paths \(\pi_{b,v_i(h)}\) and \(\pi_{b,u^t}\) (from _b_ we use a reasonable _d_ for the paths to _v<sub>i</sub>(h_) and _u<sup>t</sup>_ respectively and if the edges agree we search the interval containing values larger than _d_ and otherwise, we search the interval containing values smaller than _d_; we repeat this step iteratively to find the last edge that is shared on the paths by recursing on the relevant subintervals; this takes at most _O_(log_n_) time).<tbc>

<tbc>Given \(b'\), let \(b''\) be the next vertex on \(\overleftarrow{T}'_{v_i(h)}[b]\) and \(b'''\) the next vertex on \(\overleftarrow{T}'_{u^t}[b]\). If \(b''\) and \(b'''\) are in different child pieces of _P_, then we can conclude that \(b'\) is equal _x_.<tbc>

<tbc>Otherwise, we know that all three vertices are incident to the child piece \(P''\). The final problem becomes to find the last common vertex of the shortest paths \(\pi_{b^\prime,b^{\prime\prime}}\) from \(b'\) to \(b''\) and \(\pi_{b^\prime,b^{\prime\prime}}\) from \(b'\) to \(b'''\).<tbc>

<tbc>It is not hard to see that this problem can now be solved by recursing on the piece \(P''\). Each binary search for the last child boundary vertex takes _O_(log_n_) time and the recursion depth is bounded by _O_(log_n_) giving a total query time of _O_(log<sup>2</sup>_n_).<tbc>

• if some edge \(e^\ell\) is the edge on \(\pi_{b,v_i(h)}\) that had last its edge weight decreased: we can then use the same strategy as suggested above on the trees \(T'_{v^\ell}\) and \(\overleftarrow{T}'_{u^\ell}\) and the edge \(e^\ell\) separately. While this increases the time to find the last child boundary vertex shared by the paths slightly, we still only require a single recursive call and therefore the query time is again _O_(log<sup>2</sup>_n_).

This completes the description of our data structure and establishes Theorem 5.1.

## Making the Data Structure Fully-Persistent.

Lastly, to turn our data structure into a fully- persistent data structure, we use the following result by \[13\].

**Definition 5.10** (Emphemeral Linked Data Structure)**.** _An_ emphemeral linked data structure _is a data structure that consists of a finite number of_ nodes _where each node has a constant number of_ words _containing either information or a pointer to another node._

**Theorem 5.11** (\[13\])**.** _Any emphemeral linked data structure, where each node has its pointer stored at a constant number of nodes at most, can be made fully-persistent at the cost of an additional_ factor _of O_(log_n_) _to the amortized/ worst-case update/ query cost._

While our described data structure is not an emphemeral linked data structure yet, we can convert multiple pointers pointing to the same node by binary trees over them which increases update times, query times and space by at most a logarithmic factor.

## Acknowledgements.

The authors would like the anonymous reviewers of this article for their useful feedback and suggestions.

