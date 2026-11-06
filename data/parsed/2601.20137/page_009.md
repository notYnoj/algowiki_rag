_2. For any_ \(u'\in S\) _and_ \(v'\in T\)_, adding the undirected edge_ \(\{u',v'\}\) _to_ \(G'\) _increases the maximum u-v flow by one._

_Proof._<tbc>

1. If \(w\in S\cap T\), then _G<sub>f</sub>_ contains a path from _u_ to _w_ (since \(w\in S\)) and a path from _w_ to _v_ (since \(w\in T\)). Concatenating these paths yields an augmenting _u-v_ path, contradicting maximality of _f_.<tbc>

2. Adding edge \(\{u',v'\}\) to \(G'\) introduces the arc \((u',v')\) in the residual graph. Since \(u'\in S\), there is a path from _u_ to \(u'\) in _G<sub>f</sub>_; since \(v'\in T\), there is a path from \(v'\) to _v_ in _G<sub>f</sub>_. Concatenating these with the new arc gives an augmenting path from _u_ to _v_, increasing the flow by one.

**Theorem 7.** _Let_ \(G'=G\backslash\{e\}\) _where e_={_u,v_} _and_ \(\lambda(G')<k\)_. Let_ \(G''\) _be the augmented graph produced by Algorithm 4. Then_ \(\lambda(G'')\ge k\)_, and_ \(|E(G'')\backslash E(G')|\le 2\).

_Proof._ By Lemma 1, \(\lambda(u,v;G')=k-1\), and every cut of size less than _k_ in \(G'\) separates _u_ and _v_. The max _u-v_ flow in \(G'\) therefore equals _k_-1.

1. Case 1: \(|S|\ge 2\) or \(|T|\ge 2\). There exist \(u'\in S\) and \(v'\in T\) with \(\{u',v'\}\neq\{u,v\}\). The algorithm adds \(\{u',v'\}\). By Lemma 6, this increases the maximum _u-v_ flow to _k_. Since every cut of size less than _k_ separates _u_ and _v_ (Lemma 1), and the minimum _u-v_ cut now has size _k_, we have \(\lambda(G'')\ge k\). One edge is added.<tbc>

2. Case 2: _S_={_u_} and _T_={_v_}. The algorithm selects \(w\in V\backslash\{u,v\}\) and adds {_u,w_} and {_w,v_}. This creates the augmenting path \(u\rightarrow w\rightarrow v\), increasing the maximum _u-v_ flow to _k_. The same argument as Case 1 gives \(\lambda(G'')\ge k\). Two edges are added.

In both cases \(|E(G'')\backslash E(G')|\le 2\) holds.

The cost of Algorithm 4 is dominated by one execution of Dinic’s algorithm on the sparsified graph \(G'\). After applying the Nagamochi–Ibaraki sparsification \[12\], the graph has _m=O(kn_) edges while preserving all cuts of size at most _k_. By the Even–Tarjan bound \[5\], Dinic’s algorithm on a unit-capacity network runs in \(O(min(n^{2/3},m^{1/2})\cdot m)\) time. Substituting _m=O(kn_), this yields \(O(n^{2/3}\cdot kn)=O(kn^{5/3})\) and \(O((kn)^{1/2}\cdot kn)=O(k^{3/2}\cdot n^{3/2})\), respectively. Since _k_ is a fixed constant, \(k^{1/2}\cdot n^{1/2}<n^{2/3}\) for sufficiently large _n_, so the second branch dominates and the total cost is \(O(k^{3/2}\cdot n^{3/2})\). The subsequent BFS/DFS algorithm to compute _S_ and _T_ runs in _O(kn_) time and does not affect the asymptotic bound.

## References

