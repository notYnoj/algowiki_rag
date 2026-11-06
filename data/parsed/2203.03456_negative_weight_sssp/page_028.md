## Appendix A Proof of Lemma 3.3 (ElimNeg)

**Lemma 3.3.** (ElimNeg) _There exists an algorithm_ ElimNeg(_G,s_) _that takes as input a graph G_=(_V,E,w_) _in which all vertices_ \(v\neq s\) _have constant out-degree and a source_ \(s\in V\) _that can reach all vertices in V . The algorithm outputs a price function_ \(\phi\) _such that_ \(w_\phi(e)\ge 0\) _for all_ \(e\in E\) _and has running time_ \(O(log(n)\cdot(n+\sum_{v\in V}\eta_G(v;s)))\) _(Definition 2.4); note that if G contains a negative-weight cycle then_ \(\sum_{v\in V}\eta_G(v;s)=\infty\) _so the algorithm will never terminate and hence not produce any output._

Set \(d(s)\leftarrow 0\) and \(d(v)\leftarrow\infty\) for \(v\neq s\)<br>
Initialize priority queue Q and add s to Q.<br>
Initially, every vertex is unmarked<br>
// Dijkstra Phase<br>
while Q is non-empty do<br>
   Let v be the vertex in Q with minimum d(v)<br>
   Mark v<br>
   foreach edge \((v,x)\in E\backslash E^{neg}(G)\) do<br>
   if d(v)+w(v,x)\<d(x) then<br>
   if \(x\notin Q\), add x to Q<br>
  \(d(x)\leftarrow d(v)+w(v,x)\) and decrease-key(Q,x,d(x))<br>
   Extract v from Q<br>
// Bellman-Ford Phase<br>
foreach marked vertex v do<br>
   foreach edge \((v,x)\in E(G)\) do<br>
   if d(v)+w(v,x)\<d(x) then<br>
   if \(x\notin Q\), add x to Q<br>
  \(d(x)\leftarrow d(v)+w(v,x)\) and decrease-key(Q,x,d(x))<br>
   Unmark v<br>
If Q is empty: return d(v) for each \(v\in V\)<br>
// labels do not change so we have<br>
correct distances.<br>
Go to Line 4<br>
// Q is non-empty.

At a high level, we implement ElimNeg(_G,s_) to compute distance estimates _d(v_) so that at termination, _d(v_)=dist<sub>G</sub>(s,v_) for each \(v\in V\) ; we will then return \(\phi(v)=dist_G(s,v)\). The pseudocode is given in Algorithm 4. We use priority queue _Q_ that supports finding an element with a minimum key, extracting an element, and decreasing the key of some element _x_ to _k_ (decrease- key(_Q,x,k_)). It can be implemented as a binary heap to support each queue in _O_(log_n_) time. (This suffices for our needs, although there exist better implementations, such as the Fibonacci heap.) Note that, instead of extracting _v_ on Line 11, one can do so at the same time when _v_ is marked on Line 6. Also, on Line 13, it suffices to only consider edges \((v,x)\in E^{neg}(G)\). We instead consider all edges in _E(G_) because this implementation simplifies some of the proofs.

**Algorithm 4:** Algorithm for ElimNeg(_G_)

