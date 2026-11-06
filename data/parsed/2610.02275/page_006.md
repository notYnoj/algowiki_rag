partial star with at least one edge. Label _L_ means that _x_ is a leaf of a star whose centre lies outside the bag and has at least two selected neighbours. In particular, a _K_<sub>2</sub> meeting the bag only at _x_ always has label _C_, irrespective of any earlier orientation.<tbc>

• A pair state \((\{x,y\},\lambda)\) has distinct \(x,y\in B_t\) and \(\lambda\in\{E,S_x,S_y\}\). Since _B<sub>t</sub>_ is a clique, \(xy\in E(G)\). In every pair state, _xy_ is selected but has not yet been counted. Label _E_ means that _xy_ currently forms a _K_<sub>2</sub>-component with no counted attachment at either endpoint. Label _S<sub>x</sub>_ means that the partial star is centred at _x_ with _y_ as a leaf and at least one counted edge from _x_ to a leaf outside the bag. Label _S<sub>y</sub>_ is defined symmetrically.

A partial solution at _t_ is a set \(U\subseteq V(G_t)\) such that _H=G<sub>t</sub>_\[_U_\] is a disjoint union of stars with at least one edge, with the possible addition of one isolated vertex in _B<sub>t</sub>_. The active vertices are exactly \(U\cap B_t\), and every edge of _H_ is selected. The component meeting the bag, if any, has the canonical label defined above; an isolated active vertex has label _P_. There is at most one such component because the bag is a clique. All components disjoint from the bag are complete.

For a state \(\sigma\), the table entry \(\mathrm{DP}[t,\sigma]\) is the maximum number of edges of _H_ with at least one endpoint outside _B<sub>t</sub>_ over partial solutions with state \(\sigma\), or \(-\infty\) if none exists. Thus, the counting invariant is that every selected edge outside the bag has been counted, while no edge entirely inside the bag has been counted. The latter case occurs only for the edge _xy_ in a pair state; it is counted when the first of _x,y_ is forgotten. Canonical labels depend on the current partial star, so the two endpoints of a _K_<sub>2</sub> need not be assigned permanent roles.

## 4.2 Transitions

All updates are maximum updates. Entries not produced by a listed transition remain equal to \(-\infty\).

**Leaf node.** For a leaf _t_ with empty bag, set \(\mathrm{DP}[t,\varnothing]=0\).

**Introduce node.** Let _t_ be an introduce node with child \(t'\) and \(B_t=B_{t^\prime}\cup\{v\}\). The vertex _v_ may be left inactive, so every child state is copied to the same state at _t_ with the same value. If _v_ becomes active, the possible updates are

\(\mathrm{DP}[t,(v,P)]\leftarrow\mathrm{max}\{\mathrm{DP}[t,(v,P)],\mathrm{DP}[t',\varnothing]\},\)<br>
\(\mathrm{DP}[t,(\{x,v\},E)]\leftarrow\mathrm{max}\{\mathrm{DP}[t,(\{x,v\},E)],\mathrm{DP}[t',(x,P)]\},\)<br>
\(\mathrm{DP}[t,(\{x,v\},S_x)]\leftarrow\mathrm{max}\{\mathrm{DP}[t,(\{x,v\},S_x)],\mathrm{DP}[t',(x,C)]\},\)

for every \(x\in B_{t^\prime}\) for which the child entry is finite. No other transition that makes _v_ active is allowed. Activating _v_ from (_x,L_) would give the leaf _x_ a second selected neighbour, while activating it from a pair state would create three active vertices in a clique. No selected edge is counted at an introduce node.

**Forget node.** Let _t_ be a forget node with child \(t'\) and \(B_t=B_{t^\prime}\backslash\{v\}\). If _v_ does not occur in a child state \(\sigma\), copy the state unchanged. The state (_v,P_) is rejected because _v_ would be forgotten before becoming incident with a selected edge. For \(\lambda\in\{C,L\}\), the state \((v,\lambda)\) produces the empty state at _t_ with the same value.

Now suppose that the child state is a pair state involving _v_ and another vertex \(x\in B_t\). The selected edge _vx_ is counted at this forget step. The updates are

\(\mathrm{DP}[t,(x,C)]\leftarrow\mathrm{max}\{\mathrm{DP}[t,(x,C)],\mathrm{DP}[t',(\{v,x\},E)]+1\},\)<br>
\(\mathrm{DP}[t,(x,L)]\leftarrow\mathrm{max}\{\mathrm{DP}[t,(x,L)],\mathrm{DP}[t',(\{v,x\},S_v)]+1\},\)<br>
\(\mathrm{DP}[t,(x,C)]\leftarrow\mathrm{max}\{\mathrm{DP}[t,(x,C)],\mathrm{DP}[t',(\{v,x\},S_x)]+1\}.\)

The first update views the counted _K_<sub>2</sub> as a star centred at its remaining endpoint. In the second update, _v_ is the forgotten centre and _x_ remains a leaf; the positive attachment in _S<sub>v</sub>_ ensures that _v_ has at least two selected neighbours. In the third, _x_ remains the centre.

**Join node.** Let _t_ be a join node with children _t_<sub>1</sub>_,t_<sub>2</sub>, where _B<sub>t</sub>=B_<sub>_t_<sub>1</sub></sub>=_B_<sub>_t_<sub>2</sub></sub>. Two child states are combined only when they activate the same subset of _B<sub>t</sub>_.

Define a partial merge operation ⋆ on labels. For the empty state, \(\varnothing\star\varnothing=\varnothing\). For singleton states on the same vertex, the valid merges are<tbc>

\(P\star P=P,P\star C=C,C\star P=C,\)<br>
\(P\star L=L,L\star P=L,C\star C=C.\)

