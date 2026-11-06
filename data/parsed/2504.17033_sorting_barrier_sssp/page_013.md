<tbc>on level _l_-1, the _i_-th recursive call is correct and we have \(U_i=T_{<B_i^\prime}(S_i)\) and is complete. Note that _S<sub>i</sub>_ includes all the vertices _v_ in D_<sub>i</sub>_ such that \(\widehat{d}[v]<B'_i\) and that \(B'_i\le B\). Thus by Lemma 3.6 and proposition (b) on case _i_, \(U_i=T_{<B_i^\prime}(S_i)=T_{<B_i^\prime}(\mathcal{D}_i)=T_{[B_{i-1}^\prime,B_i^\prime]}(P)\) and is complete (thus proving Remark 3.8). Then, every incomplete vertex _v_ with _d(v)\<B_ is in \(T_{[B_{i-1}^\prime,B)}(P)\backslash T_{[B_{i-1}^\prime,B_i^\prime]}(P)=T_{[B_i^\prime,B)}(P)\). Thus, we proved proposition (a) for the (_i_+1)-th iteration.

Now we prove proposition (b) for the (_i_+1)-th iteration. Since \(B'_i\ge B'_{i-1}\), from proposition (b) of the _i_-th iteration, we have \(T_{[B_i^\prime,B)}(P)=T_{[B_i^\prime,B)}(\mathcal{D}_i)=T_{[B_i^\prime,B)}(\mathcal{D}_i^*)\). Suppose we can show that \(T_{[B_i^\prime,B)}(\mathcal{D}_i^*)\subseteq T_{<B}(\mathcal{D}_{i+1}^*)\) and \(T_{<B}(\mathcal{D}_{i+1})\subseteq T_{[B_i^\prime,B)}(\mathcal{D}_i)\). By definition \(T_{<B}(\mathcal{D}_{i+1}^*)\subseteq T_{<B}(\mathcal{D}_{i+1})\), then

\(T_{[B_i^\prime,B)}(P)=T_{[B_i^\prime,B)}(\mathcal{D}_i^*)\subseteq T_{<B}(\mathcal{D}_{i+1}^*)\subseteq T_{<B}(\mathcal{D}_{i+1})\subseteq T_{[B_i^\prime,B)}(\mathcal{D}_i)=T_{[B_i^\prime,B)}(\mathcal{D}_i^*),\)

and by sandwiching, proposition (b) holds for (_i_+1). Thus it suffices to prove \(T_{[B_i^\prime,B)}(\mathcal{D}_i^*)\subseteq T_{<B}(\mathcal{D}_{i+1}^*)\) and \(T_{<B}(\mathcal{D}_{i+1})\subseteq T_{[B_i^\prime,B)}(\mathcal{D}_i)\).

For any vertex \(y\in\mathcal{D}_i^*\backslash\mathcal{D}_{i+1}^*\), we have \(y\in S_i\). Note that vertices _v_ of _S<sub>i</sub>_ with \(\widehat{d}[v]\ge B'_i\) are batch prepended back to D<sub>_i_+1</sub> on Line 21, so we have \(\widehat{d}[y]<B'_i\). Thus \(y\in U_i\) and is complete. For any vertex \(x\in T_{[B_i^\prime,B)}(y)\), as \(x\unknown\in U_i\), along the shortest path from _y_ to _x_, there is an edge (_u,v_) with \(u\in U_i\) and \(v\unknown\in U_i\). During relaxation, _v_ is then complete and is added to D<sub>_i_+1</sub>, so \(x\in T_{[B_i^\prime,B)}(v)\subseteq T_{<B}(\mathcal{D}_{i+1}^*)\).

For any vertex \(v\in\mathcal{D}_{i+1}\backslash\mathcal{D}_i\), since _v_ is added to D<sub>_i_+1</sub>, there is an edge (_u,v_) with \(u\in U_i=T_{<B_i^\prime}(\mathcal{D}_i)\) and the relaxation of (_u,v_) is valid (\(\widehat{d}[u]+w_{uv}\le\widehat{d}[v]\)). Pick the last valid relaxation edge (_u,v_) for _v_. If \(v\in T(u)\), then _v_ is complete, \(d(v)=\widehat{d}[v]\ge B'_i\), and \(v\in T_{[B_i^\prime,B)}(\mathcal{D}_i)\); if _v_ is incomplete, then by proposition (a), \(v\in T_{[B_i^\prime,B)}(P)=T_{[B_i^\prime,B)}(\mathcal{D}_i)\); or if _v_ is complete but \(v\notin T(u)\), we have a contradiction because it implies that relaxation of (_u,v_) is invalid.

Now that we have proven the propositions, we proceed to prove that the returned \(U=T_{<B^\prime}(S)\) and that _U_ is complete. Suppose there are _q_ iterations. We have shown that every \(U_i=T_{[B_{i-1}^\prime,B_i^\prime]}(P)\) and is complete, so _U<sub>i</sub>_’s are also disjoint. By Lemma 3.2, _W_ contains every vertex in _T<sub>\<B</sub>(S_\\_P_) (as they are not in _T(P_)) and they are complete; besides, all vertices _v_ in _W_ but not in _T<sub>\<B</sub>(S_\\_P_) with \(d(v)<B'_q\) are complete (because they are in \(T_{<B_q^\prime}(P)\)). Therefore, \(\{x\in W:\widehat{d}[x]<B'_q\}\) contains every vertex in \(T_{<B_q^\prime}(S\backslash P)\) and is complete. Thus finally \(U:=(\bigcup_{i=1}^qU_i)\cup\{x\in W:\widehat{d}[x]<B'_q\}\) equals \(T_{<B_q^\prime}(S)\) and is complete.

**Remark 3.8.** From the proof of Lemma 3.7, \(U_i=T_{[B_{i-1}^\prime,B_i^\prime]}(P)\) and they are disjoint and complete. As a reminder, Lemma 3.6 and proposition (b) of Lemma 3.7 prove this.

## 3.4 Time Complexity Analysis

**Lemma 3.9.** _Under the same conditions as in Lemma 3.7, where every incomplete vertex v with d(v)\<B is in T<sub>\<B</sub>(S_<sup>∗</sup>)_. After running Algorithm 3, we have_ \(|U|\le 4k2^{lt}\)_. If_ \(B'<B\)_, then_ \(|U|\ge k2^{lt}\).

_Proof._ We can prove this by induction on the number of levels. The base case _l_=0 clearly holds.

Suppose there are _q_ iterations. Before the _q_-th iteration, |_U|\<k_2<sup>_lt_</sup>. After the _q_-th iteration, the number of newly added vertices \(|U_q|\le 4k2^{(l-1)t}\) (by Lemma 3.7, the assumptions for recursive calls are satisfied), and because \(|W|\le k|S|\le k2^{lt}\), we have \(|U|\le 4k2^{lt}\). If D is empty, the algorithm succeeds and quits with \(B'=B\). Otherwise, the algorithm ends partially because \(|U|\ge k2^{lt}\).

**Lemma 3.10.** _Immediately before the i-th iteration of Algorithm 3,_ \(min_{x\in\mathcal{D}}d(x)\ge B'_{i-1}\).

_Proof._ From the construction of D, immediately before the _i_-th iteration of Algorithm 3, \(min_{v\in\mathcal{D}}\widehat{d}[v]\ge B'_{i-1}\). For \(v\in\mathcal{D}\), if _v_ is complete, then \(d(v)=\widehat{d}[v]\ge B'_{i-1}\). If _v_ is incomplete, by proposition (a) of Lemma 3.7, because \(v\in T_{[B_{i-1}^\prime,B)}(P)\), \(d(v)\ge B'_{i-1}\).

