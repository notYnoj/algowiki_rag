**Algorithm 1** Sort(directed acyclic graph _G_ over a ground set _X_, Oracle _O<sub>L</sub>_) time

1: \(\pi\leftarrow\) a longest directed path in _G_ \(\triangleright O(n+m)\)

2: \(T_\pi\leftarrow\) a level-linked (2-4)-tree over \(\pi\) \[6\] \(\triangleright O(n)\)

3: \(H\leftarrow G-\pi\) \(\triangleright O(n+m)\)

4: Compute for each vertex in _H_ its in-degree in _H_ \(\triangleright O(n+m)\)

5: \(S\leftarrow\) sources in _H_ \(\triangleright O(n)\)

6: **while** \(S\neq\emptyset\) **do**

7: Remove an arbitrary vertex _x<sub>i</sub>_ from _S_ \(\triangleright O(1)\)

8: \(p_i\leftarrow\) a dummy vertex, which is prepended before the head of \(\pi\) \(\triangleright O(1)\)

9: **for all** in-neighbors _u_ of _x<sub>i</sub>_ in _G_ **do** \(\triangleright O(d^*(x_i))\)

10: \(p_i\leftarrow\) Compare(_p<sub>i</sub>,u_) \(\triangleright O(1)\)

11: Remove _x<sub>i</sub>_ from _H_ and add any new sources in _H_ to _S_ \(\triangleright O(d^*(x_i))\)

12: \(q_i\leftarrow\) Search(_x<sub>i</sub>,p<sub>i</sub>,O<sub>L</sub>_) \(\triangleright O(1+logd_i)\)

13: FingerInsert(_q<sub>i</sub>,x<sub>i</sub>_) \(\triangleright O(1)\) amortised

14: **return** the leaves of \(T_\pi\) in order \(\triangleright O(n)\)

so, we return _q<sub>i</sub>=p<sub>i</sub>_. Otherwise, we set _p<sub>i</sub>=h_ and invoke Search. This returns _q<sub>i</sub>_ in _O_(1+log_d<sub>i</sub>_) time and queries, where _d<sub>i</sub>_ is the length of the subpath from _p<sub>i</sub>_ to _q<sub>i</sub>_ in \(\pi\) (_d<sub>i</sub>_=1 if _p<sub>i</sub>=q<sub>i</sub>_).

Finally, we insert _x<sub>i</sub>_ into \(T_\pi\) succeeding _q<sub>i</sub>_ in constant time. Updating the dynamic list order data structure and rebalancing \(T_\pi\) takes amortised _O_(1) time. Thus, these operations take _O(n_) total time over all insertions. Therefore, our algorithm uses \(O\big(n+m+\sum_{x_i\in H}(1+logd_i)\big)\) time and \(O\big(\sum_{x_i\in H}(1+logd_i)\big)\) queries.

## 2.1 Proof of optimality

Recall that _e(P<sub>G</sub>_) denotes the number of linear extensions of _P<sub>G</sub>_ and let _H_ start out with _k_ vertices. For ease of analysis, we re-index the vertices _X_ so that the path \(\pi\) are vertices (_x_<sub>_k_+1</sub>_,...,x<sub>n</sub>_), in order, and _x<sub>i</sub>_ for \(i\in[k]\) is the _i_’th vertex our algorithm inserts into \(T_\pi\). We prove that our algorithm is tight by showing that \(\sum_{i=1}^k(1+logd_i)=k+\sum_{i=1}^klogd_i\in O(loge(P_G))\).

**Lemma 1.** _Let G be a directed acyclic graph, P<sub>G</sub> be its induced partial order and_ \(\pi\) _be a longest directed path in G. If_ \(\pi\) _has n-k vertices then_ \(loge(P_G)\ge k\).

_Proof._ Denote \(\ell(x)\) the length of the longest directed path in _G_ from a vertex _x_. Denote for \(i\in[n]\) by \(L_i:=|\{x\in X|\ell(x)=i\}|\). For each \(i\in[n-k]\), there is one \(u\in\pi\) with \(\ell(u)=i\) so:

\(k=\sum_{i=1}^{n-k}(L_i-1).\) (1)

Consider a linear order \(L'\) that is obtained by first sorting all \(x\in X\) by \(\ell(x)\) from high to low, and ordering (_u,v_) with \(\ell(u)=\ell(v)\) arbitrarily. The order \(L'\) must extend _P<sub>G</sub>_, since any vertex _w_ that has a directed path towards a vertex _u_ must have that \(\ell(w)>\ell(u)\). We count the number of distinct \(L'\) that we obtain in this way to lower bound _e(P<sub>G</sub>_):

