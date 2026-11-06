Now consider each \(i\in[f-k]\). The edges in \(P_i\cap C\) split _P<sub>i</sub>_ into \(\eta_i+1\) contiguous segments. We claim that for a segment consisting of _l_ edges, we can label its vertices in at most \(l\le n\) ways. To see this, suppose that this segment is S=(_v_<sub>0</sub>_,...,v<sub>l</sub>_). Then, _v_<sub>0</sub> must have already been labeled with ‘t’ (either _v_<sub>0</sub>=_t_ or it is the tail of some _s-t_ edge in _C_). Similarly, _v<sub>l</sub>_ must have already been labeled with ‘s’. As there can be no other _s-t_ edges in S, the only valid labelings are monotonic -- that is, to label {_v_<sub>0</sub>_,...,v<sub>j</sub>_} with ‘t’ and {_v_<sub>_j_+1</sub>_,...,v<sub>d</sub>_} with ‘s’ for some \(0\le j\le l-1\); giving _l_ possible labeling of _V_(S). See Figure 3 for an illustration.

Thus, the number of consistent labels for _V(E_<sub>2</sub>) is upper-bounded by:

\(\prod_{i=1}^{f-k}n^{\eta_i+1}\le n^{f-k+\sum_{i=1}^{f-k}\eta_i}\le n^{f-k^\prime-1}<n^f.\)

Going forward, we fix the labels of the vertices in _V(E_<sub>2</sub>)\\_V(C_) accordingly.

**Step 3: Counting the number of labels for** _V_ **given a labeling of** \(V(E_2)\cup V(C)\)**.** Fix a labeling of \(V(E_2)\cup V(C)\) from Steps 1 and 2. In this final steps, we will label the remaining vertices. For any vertex \(u\in V\) , let _d(u_) denote the length of the shortest path from _s_ to _u_ in _H_ (such path must exist due to Assumption C.3). We will prove the following claim by induction on _d_: For any vertex \(u\in V\) such that _d(u_)=_d_, given a fixed labeling \(\phi\) of \(V(E_2)\cup V(C)\), there is at most one consistent label for _u_ with respect to _C_. We may assume \(u\notin V(E_2)\cup V(C)\), as those vertices have already been assigned labels from the previous steps.

The base case _d_=1 means \((s,u)\in E(H)\). Since \(u\notin V(E_2)\), the undirected unit-capacitated edge (_s,u_) belongs to _H<sub>F</sub>_, which then can be replaced with two directed edges (_s,u,_1) and (_u,s,_1). Furthermore, because \(u\notin V(C)\), neither (_s,u,_1) nor (_u,s,_1) can be an _s-t_ edge. As a result, _s_ and _u_ must be assigned the same label. Since _s_ is labeled with ‘s’, _u_ can only be labeled with ‘s’.

't'
's'
't'
s
t
't'
's'
's'
's'
's'

Figure 2: Shown above is a graph _H<sub>F</sub>_ with its partial labels given a fixed _C_. The shaded vertices (_s_ and _t_) are already given a label. The red and blue edges represent _E_<sub>2</sub> which is the reversal of a flow graph _F_ of size 2. The black edges represent undirected unit-capacitated edges, each of which viewed as two directed edges of weight 1. The _wavy_ edges represent the fixing of _C_. Step 1 _uniquely_ labels vertices in _V(C_) according to _C_. Such unique label is indicated by the label within each node itself.

