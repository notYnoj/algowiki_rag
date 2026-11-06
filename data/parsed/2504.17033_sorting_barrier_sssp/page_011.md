## Correctness.

In a call of BMSSP, let \(\widetilde{U}\) denote the set that contains all vertices _v_ with _d(v)\<B_ and the shortest path to _v_ visits some vertex in _S_. Then BMSSP should return \(U=\widetilde{U}\) in a successful execution, or \(U=\{u\in\widetilde{U}:d(u)<B'\}\) in a partial execution, with all vertices in _U_ complete.

In the base case where _l_=0, _S_ contains only one vertex _x_, a Dijkstra-like algorithm starting from _x_ completes the task.

Otherwise we first shrink _S_ to a smaller set of pivots _P_ to insert into D, with some vertices complete and added into _W_. Lemma 3.2 ensures that the shortest path of any remaining incomplete vertex _v_ visits some complete vertex in D. For any bound \(B_i\le B\), if _d(v)\<B<sub>i</sub>_, the shortest path to _v_ must also visit some complete vertex \(u\in\mathcal{D}\) with _d(u)\<B<sub>i</sub>_. Therefore we can call subprocedure BMSSP on _B<sub>i</sub>_ and _S<sub>i</sub>_.

By inductive hypothesis, each time a recursive call on Line 11 of Algorithm 3 returns, vertices in _U<sub>i</sub>_ are complete. After the algorithm relaxes edges from \(u\in U_i\) and inserts all the updated out-neighbors _x_ with \(\widehat{d}[x]\in[B'_i,B)\) into D, once again any remaining incomplete vertex _v_ now visits some complete vertex in D.

Finally, with the complete vertices in _W_ added, _U_ contains all vertices required and all these vertices are complete.

## Running time.

The running time is dominated by calls of Findpivots and the overheads inside the data structures D. By (4) and (5), the running time of Findpivots procedure at node _x_ is bounded by _O_(|_U<sub>x</sub>|k_), so the total running time over all nodes on one depth of T is _O(nk_). Summing over all depths we get \(O(nk\cdot(logn)/t)=O(nlog^{2/3}n)\).

For the data structure D in a call of BMSSP, the total running time is dominated by Insert and BATCH Prepend operations. We analyze the running time as follows.

• Vertices in _P_ can be added to D on Line 6. Since |_P<sub>x</sub>_|=_O_(|_U<sub>x</sub>|/k_), the total time for nodes of one depth of T is \(O(n/k\cdot(t+logk))=O(nt/k)\). Summing over all depths we get _O_((_nlogn)/k_)=_O(n_log<sup>2/3</sup>_n_).<tbc>

• Some vertices already pulled to _S<sub>i</sub>_ can be added back to D through BATCHPrepend on Line 21. Here we know in every iteration _i_, \(|S_i|\le|U_i|\), so the total time for adding back is bounded by \(\sum_{x\in\mathcal{T}}|U_x|\cdot logk=O(nlogk\cdot(logn)/t)=O(n\cdot log^{1/3}n\cdot loglogn)\).<tbc>

• A vertex _v_ can be inserted to D through edge (_u,v_) **directly** on Line 18 if \(B_i\le d(u)+w_{uv}<B\), or **through** _K_ as on Line 20 if \(B'_i\le d(u)+w_{uv}<B_i\). (Note that \(u\in U_i\) is already complete.) Every edge (_u,v_) can only be relaxed once in each level by (6), but it can be relaxed in multiple levels in an ancestor-descendant path of the recursion tree T . (Note that the condition on Line 15 is \(\widehat{d}[u]+w_{uv}\le\widehat{d}[v]\).) However, we can show every edge (_u,v_) can only lead _v_ to be directly inserted to D by the Insert operation on one level.<tbc>

– It can be easily seen that if _y_ is a descendant of _x_ in the recursion tree T , \(B_y\le B_x\).<tbc>

**–** If (_u,v_) leads _v_ to be directly inserted to D on Line 18, then \(d(u)+w_{uv}\ge B_i\). Since \(u\in U_i\), for every descendant _y_ of the current call in the recursion tree T satisfying \(u\in U_y\), we have \(B_y\le B_i\le d(u)+w_{uv}\), so _v_ will not be added to D through (_u,v_) in any way in lower levels.<tbc>

• Since every edge (_u,v_) can only lead _v_ to be directly inserted to D by the Insert operation once in the algorithm, the total time is _O(m_(log_k+t_))=_O(m_log<sup>2/3</sup>_n_). The time for all edges (_u,v_) leading _v_ to be inserted to D through _K_ in one level is _O(m_log_k_), and in total is \(O(mlogk\cdot(logn)/t)=O(m\cdot log^{1/3}n\cdot loglogn)\).<tbc>

