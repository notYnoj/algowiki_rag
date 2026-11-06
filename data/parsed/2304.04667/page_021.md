## Queries

To answer a query for a pair of nodes _u_ and _v_, we first check if Max-Flow(_u,v_) was computed directly for them. If so, we output the corresponding separator. Otherwise, we do the following for each recursion tree _T_ and pick the answer with minimal value: we go to the recursion depth that separated _u_ and _v_, which corresponds to some node \(t_{V^\prime}\) in _T_, and output a pointer to one of the two corresponding cuts (_S<sub>p,f(u)</sub>,C<sub>p,f(u)</sub>,S<sub>f(u),p</sub>_) or (_S<sub>p,f(v)</sub>,C<sub>p,f(v)</sub>,S<sub>f(v),p</sub>_) - the one with smaller capacity among the (at most) two that separate _u_ and _v_. We prove that at least one of the two cuts separates them. To find out which recursive node separates _u_ and _v_, we start from the root and continue down, guided by the array _B_, to the nodes that contain both _u_ and _v_ until we reach a node that separates them. The query time depends on the depth of the recursion, which we will show later to be logarithmic for all trees.

## Correctness

The claim below proves that the cut returned for each pair _u,v_ is optimal with high probability. The main idea is that either both \(\alpha(u)\) and \(\alpha(v)\) are high with respect to \(n':=|V'|\) in the instance \(V'\) that separates them, in which case the algorithm computes Max-Flow(_u,v_) directly, or at least one of \(\alpha(u)\) and \(\alpha(v)\) is small, in which case their separator is small, and _p_ is unlikely to be in it. Then, assume without loss of generality that \(\text{Max-Flow}(p,u)\le\text{Max-Flow}(p,v)\). Consequently, either _C<sub>p,u</sub>_ is optimal for Max-Flow(_u,v_), or \(v\in C_{p,u}\), and we computed Max-Flow(_u,v_) directly. More formally,

**Lemma 3.2.** _With high probability, the separator returned for any pair of nodes u,v is a minimum uv-separator._

_Proof._ Let _T_ be a recursion tree, and let \(V'\subseteq V\) be the instance where _u_ and _v_ belong to \(V'\) but were sent to different sets during the expansion operation. We will use the following claim to make the assumption that the pivot _p_ in \(V'\) satisfies \(p\notin C_{u,v}\).

**Claim 3.3.** _With high probability, for at least one recursion tree T either Max-Flow(u,v_) _is computed in step 1, or_ \(p\notin C_{u,v}\) _for the instance separating u and v._

_Proof._ For a node \(r\in V\) , let \(V'_r\) be an instance in _T_ that contains _r_, and is the first instance satisfying \(\alpha(r)\ge|V'_r|/(20log_{4/3}n)\). Let \(V'_{u,v}\) be \(V'_w\) for \(w=arg_{u,v}min\{\alpha(u),\alpha(v)\}\), and let X_<sub>u,v</sub>_ be the event that \(p\notin C_{u,v}\) for all instances \(V'\) along the path from the root to the parent of \(V'_{u,v}\) in _T_. Note that X_<sub>u,v</sub>_ trivially occurs for \(V'_{u,v}=V\) . The probability of X_<sub>u,v</sub>_ is at least \((1-1/(10log_{4/3}n))^{log_{4/3}n}\ge 1/2\), as follows. A uniformly random node in one such \(V'\) does not belong to _C<sub>u,v</sub>_ with probability \(\frac{|V'|-|C_{u,v}|}{|V'|}\ge(1-1/20log_{4/3}n)\), then recall that only successful pivots could be chosen, and by Corollary 3.5 below, their number is at least \(|V'|/2\). Lastly, we raise to the power of log<sub>4/3</sub>_n_, as we will show later that the depth of _T_ is at most this value. Now, if X_<sub>u,v</sub>_ occurs in _T_ then either _u_ and _v_ both survived the expansions and belong to \(V'_{u,v}\) and then they are queried directly in step 1, or \(z=arg_{u,v}max\{\alpha(u),\alpha(v)\}\) was partitioned away in a higher instance \(V'\) in _T_, in which case \(p\notin C_{u,v}\) for \(V'\).

The probability that X_<sub>u,v</sub>_ does not occur in any tree is at most \((1/2)^{4logn}\le 1/n^4\). By applying a union bound over all \(\le n^2\) node pairs, we can conclude that with high probability, X_<sub>u,v</sub>_ occurs in at least one of the recursion trees for every pair of nodes _u,v_. This completes the proof of Claim 3.3.

Thus, henceforth we assume that

\(p\notin C_{u,v}.\) (3.1)

An additional assumption we make is that for any pair _u,v_ considered,

\(u\notin C_{p,v}\wedge v\notin C_{p,u}.\) (3.2)

