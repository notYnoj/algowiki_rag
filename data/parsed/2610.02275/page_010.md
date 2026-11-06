_Proof._ Process _S_<sub>1</sub>_,...,S<sub>k</sub>_ in their defined order, possibly adding leaves. We maintain the exact barriers of the corresponding original prefix and keep the enlarged prefix compatible with the unprocessed components. Initially both barriers are zero. Suppose the current barriers are \(\alpha,\beta\), and _S_ is the next component. Lemma 10 gives index greater than \(\beta\) for every _X_-vertex of _S_, and left endpoint greater than \(\alpha\) for every _Y_ -vertex of _S_.

If _S_ is centred at \(x_i\in X\), let \(q=max\{r(y):y\in V(S)\cap Y\}\). Every original leaf is counted by \(w_X(i,\alpha,q)\), so the corresponding transition selects at least |_E(S_)| edges. An added leaf has left endpoint greater than \(\alpha\) and right endpoint at most _q_, excluding edges to all earlier selected _X_-vertices. Applying Lemma 10 to the original prefix including _S_ shows that every later selected _X_-vertex has index greater than _q_, excluding edges to these vertices as well. An added leaf cannot already belong to a later component, since its edge to _x<sub>i</sub>_ would join that component to _S_. Since an original leaf attains _q_ and \(q\ge i>\beta\), the enlarged prefix has exact barriers (_i,q_), the same as the original prefix including _S_.

If _S_ is centred at \(y\in Y\) , put \(q=max\{h:x_h\in V(S)\cap X\}\) and \(s=max\{\ell(y),\beta+1\}\). All original leaves lie in _x<sub>s</sub>,...,x<sub>q</sub>_, so the transition again selects at least |_E(S_)| edges. Any added leaf has index greater than \(\beta\), excluding edges to previously selected _Y_ -vertices. Applying Lemma 10 to the original prefix including _S_ shows that every later selected _Y_ -vertex _z_ satisfies \(\ell(z)>q\). Thus none of the added leaves has an edge to a later selected _Y_ -vertex. Claim 9 also ensures that none is a selected _X_-vertex of a later component. The exact barriers are (_q,r(y_)), unchanged from those of the original prefix including _S_, since _x<sub>q</sub>_ is an original leaf and \(r(y)\ge q>\beta\).

Both transitions therefore preserve the induction invariant. Their sequence gives a reachable value at least |_D_|.

### 5.5 Running time and reconstruction

Deleting isolated vertices and extracting interval endpoints from a given convex ordering takes _O(n+m_) time. If an ordering is not supplied, it can be found in _O(n+m_) time by consecutive-ones testing \[2\].

The table has (_p_+1)<sup>2</sup>=_O(p_<sup>2</sup>) entries. Compute \(C[a,b]=|\{y\in Y:\ell(y)=a,r(y)=b\}|\) for \(1\le a\le b\le p\), with zero entries elsewhere. A two-dimensional prefix-sum table gives \(w_X(i,\alpha,q)=\sum_{a=\alpha+1}^i\sum_{b=i}^QC[a,b]\) in _O_(1) time. This preprocessing takes _O(p_<sup>2</sup>+|_Y_|) time and space. From one state there are _O(p_<sup>2</sup>) _X_-centred transitions and _O_(|_Y|p_) _Y_ -centred transitions. The total time is therefore _O(p_<sup>4</sup>+_p_<sup>3</sup>|_Y_|)=_O(n_<sup>4</sup>).

For each improving update, store its predecessor state, transition type, centre, and endpoint _q_. Backtracking identifies at most _p_ transitions, since \(\beta\) strictly increases. Recover the leaves of each _X_-centred star by scanning _Y_ , and those of each _Y_ -centred star by listing its selected interval. Reconstruction takes _O(p|Y_|+_p_<sup>2</sup>) time. The tables, interval endpoints, and predecessor records use _O(p_<sup>2</sup>+|_Y_|) auxiliary space once the ordering is available; including the input and ordering preprocessing, _O(n_<sup>2</sup>) space suffices.

**Theorem 13.** _The_ Maximum Edge Open Packing _problem can be solved in O(n_<sup>4</sup>) _time and O(n_<sup>2</sup>) _space on convex bipartite graphs._

_Proof._ Lemma 11 bounds the returned value from above by \(\rho_\mathrm{e}^\mathrm{o}(G)\), and Lemma 12 gives the reverse inequality. The preceding analysis establishes the time and space bounds and the reconstruction of an optimum packing.

## 6 Conclusion

We proved that the oriented star-conflict graph of Das and Santra \[13\] preserves AT-freeness and used this property to obtain an _O(n_<sup>2</sup>+_m_<sup>4</sup>)-time algorithm for Maximum Edge Open Packing on AT-free graphs. We also gave _O(n_<sup>4</sup>)-time dynamic programs for chordal and convex bipartite graphs. The former handles unbounded clique number, while the latter extends the earlier biconvex algorithm.

Natural next questions are whether these running times can be improved and whether Maximum Edge Open Packing admits a polynomial-time algorithm on chordal bipartite graphs. Distance- hereditary graphs are already covered by Bhyravarapu et al. \[1\]. It is also useful to study further classes for which the construction \(G\mapsto A_G\) preserves a structure that makes maximum independent set tractable.

For general graphs, fixed-parameter tractability by treewidth follows from monadic second-order optimisation \[10\]: feasibility of a chosen edge set is expressed by excluding two selected edges together with a third edge joining their endpoints, and the objective is its cardinality. Thus, the questions concern explicit algorithms, their dependence on treewidth, and kernelisation bounds. An independent set _S_ is asteroidal if _S_\\{_v_} lies in one component of _G-N<sub>G</sub>_\[_v_\] for every \(v\in S\); its maximum size is the asteroidal<tbc>

