_Then we have an sub-routine BMSSP(l,B,S_) _(Algorithm 3) in O_((_kl+tl/k+t_)|_U_|) _time that outputs a new boundary_ \(B'\le B\) _and a vertex set U that contains every vertex v with_ \(d(v)<B'\) _and the shortest path to v visits some vertex of S. At the end of the sub-routine, U is complete. Moreover, one of the following is true:_

## Successful execution \(B'=B\).

## Partial execution due to large workload \(B'<B\), and \(|U|=\Theta\left(k2^{lt}\right)\).

On the top level of divide and conquer, the main algorithm calls BMSSP with parameters \(l=\lceil(logn)/t\rceil\), \(S=\{s\},B=\infty\). Because \(|U|\le|V|=o(kn)\), it must be a successful execution, and the shortest paths to all vertices are found. With chosen _k_ and _t_, the total running time is _O(m_log<sup>2/3</sup>_n_).

BMSSP procedure on level _l_ works by recursion, it first tries to "shrink" _S_ to size |_U|/k_ by a simple Bellman-Ford-like method (Lemma 3.2), then it makes several recursive calls on level (_l_-1) until the bound reaches _B_ or the size of _U_ reaches \(\Theta\left(k2^{lt}\right)\). We always make sure that a recursive call solves a problem that is smaller by a factor of roughly 1/2_<sup>t</sup>_, so the number of levels of the recursion is bounded by _O_((log_n)/t_). The main ideas are:

• Every time we only select about 2<sup>(_l_-1)_t_</sup> vertices for our next recursive call, so we use a partial sorting heap-like data structure as described in Lemma 3.3 to improve the running time.<tbc>

• If we used all of _S_ in the recursive calls, then after all remaining levels _S_ could be fully sorted and nothing is improved. Thus FinDPIVOTS (Algorithm 1) procedure is crucial here, as it shows that only at most |_U|/k_ vertices of _S_ are useful in the recursive calls.<tbc>

• Partial executions may be more complicated to analyze, so we introduce some techniques like Batch- PrepEND operation in Lemma 3.3.

## Finding Pivots.

Recall that in the current stage, every _u_ such that _d(u)\<b_ is complete, and we have relaxed all the edges from such _u_’s, and the set _S_ includes every vertex _v_ with current \(b\le\widehat{d}[v]<B\). Thus, the shortest path of every incomplete vertex _v_ such that _d(v)\<B_ visits some complete vertex in _S_. (This is because the first vertex _w_ in the shortest path to _v_ with \(d(w)\ge b\) is complete and included in _S_.)

The idea of finding pivots is as follows: we perform relaxation for _k_ steps (with a bound _B_). After this, if the shortest _s-v_ path with \(b\le d(v)<B\) goes through at most _k_ vertices _w_ with \(b\le d(w)<B\), then _v_ is already complete. Observe that the number of large shortest path trees from _S_, consisting of at least _k_ vertices and rooted at vertices in _S_, is at most \(|\widetilde{U}|/k\) here, where \(\widetilde{U}\) is the set of all vertices _v_ such that _d(v)\<B_ and the shortest path of _v_ visits some complete vertex in _S_. So only the roots of such shortest-path trees are needed to be considered in the recursive calls, and they are called "pivots".

**Lemma 3.2** (Finding Pivots)**.** _Suppose we are given a bound B and a set of vertices S. Suppose that for every incomplete vertex v such that d(v)\<B, the shortest path to v visits some complete vertex_ \(u\in S\).

_Denote by_ \(\widetilde{U}\) _the set that contains every vertex v such that d(v)\<B and the shortest path to v passes through some vertex in S. The sub-routine FinDPIVOTS(B,S_) _(Algorithm 1) finds a set_ \(W\subseteq\widetilde{U}\) _of size O(k|S_|) _and a set of pivots_ \(P\subseteq S\) _of size at most_ |_W|/k such that for every vertex_ \(x\in\widetilde{U}\)_, at least one of the following two conditions holds:_

• _At the end of the sub-routine,_ \(x\in W\) _and x is complete;_<tbc>

• _The shortest path to x visits some complete vertex_ \(y\in P\).

_Moreover, the sub-routine runs in time O(k|W_|)=_O_(min{_k_<sup>2</sup>|_S|,k_|\(\widetilde{U}|\})).

