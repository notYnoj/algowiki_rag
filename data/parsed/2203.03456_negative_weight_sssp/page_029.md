## A.1 Correctness

Throughout the execution of the algorithm, We define an edge (_v,x_) of _G_ to be _active_ if _d(v_)+_w(v,x)\<d(x_) and _inactive_ otherwise. We define an edge (_v,x_) for which \(d(v)=d(x)=\infty\) to be inactive.

**Invariant A.1.** _At any point during the execution of Algorithm 4, if an edge_ (_v,x_) _is active, then v is in Q or marked. If_ (_v,x_) _is active and_ \((v,x)\in E\backslash E^{neg}(G)\)_, then v is in Q._

_Proof._ The statements hold initially: For all \(v\in V\backslash\{s\}\), any edge (_v,x_) is inactive since \(d(v)=\infty\) and _s_ is in _Q_. The statements are affected when we (i) extract a vertex _v_ from _Q_ (Line 11), (ii) unmark a vertex _v_ (Line 17), or (iii) decrease _d(x_) for some vertex _x_ (Lines 10 and 16), potentially making some inactive edges (_x,y_) active.

For (i), when a vertex _v_ is extracted from _Q_ on Line 11, it was already marked on Line 6, so the first statement still holds. Also, all edges \((v,x)\in E\backslash E^{neg}(G)\) were made inactive using the for-loop (Lines 7-10, by setting \(d(x)\leftarrow min\{d(x),d(v)+w(v,x)\}\)); thus, the second statement still holds. For (ii), before we unmark _v_ on Line 17, we make all edges (_v,x_) inactive using the previous for-loop (by setting \(d(x)\leftarrow min\{d(x),d(v)+w(v,x)\}\)); thus, the statements still hold right after we unmark _v_. For (iii), we add _x_ to _Q_ before decreasing _d(x_) on Lines 10 and 16; thus the statements still hold after Lines 10 and 16 are executed.

Observe that the algorithm terminates only when _Q_ is empty and every vertex is unmarked (every vertex is unmarked after the Bellman-Ford Phase). So, we have:

**Corollary A.2.** _When the algorithm terminates, all edges are inactive._

For every inactive edge (_v,x_), \(d(v)+w(v,x)-d(x)\ge 0\). Thus, _d_ is the desired price function when the algorithm terminates.

## A.2 Running time

The correctness analysis already implies that if there is a negative cycle then the algorithm never terminates (in particular, it is easy to check that if a graph has a negative-weight cycle, then for any labels _d_ on the vertices there is always contains at least one inactive edge.) So, we assume that there is no negative cycle in this section. We analyze each iteration of the Dijkstra and Bellman-Ford phases. The initial iteration is referred to as iteration 0, the next iteration is iteration 1, and so on. To simplify notation, we let dist(_v_) and \(\eta(v)\) refer to dist_<sub>G</sub>(v_) and \(\eta_G(v;s)\) for every vertex _v_. The key to the runtime analysis is the following lemma.

**Lemma A.3.** _After iteration i of the Dijkstra phase, d(v_)=dist(_s,v_) _for every v where_ \(\eta(v)\le i\).

_Proof._ Iteration 0 of the Dijkstra phase is simply the standard Dijkstra’s algorithm on the subgraphs induced by _E_\\_E<sup>neg</sup>(G_); thus, the statement holds for _i_=0 by the standard analysis. We complete the proof by induction.

Fix any \(i\ge 1\). Let _v_ be any vertex such that \(\eta(v)=i\). Let _P_=(_u_<sub>0</sub>=_s,u_<sub>1</sub>_,u_<sub>2</sub>_,...,u<sub>k</sub>=v_) be the shortest _sv_-path with _i_ negative-weight edges. Let _u<sub>j</sub>_ is the first vertex in _P_ with \(\eta(u)=i\); i.e., we define _u<sub>j</sub>_ to be the vertex in _P_ such that \((u_{j-1},u_j)\in E^{neg}(G)\) and the subpath \(P'\) of _P_ between _u<sub>j</sub>_ and _v_ contains no edge in _E<sup>neg</sup>(G_).

Consider when we just finished iteration _i_-1 of the Dijkstra phase. By induction hypothesis, we can assume that _d(u_<sub>_j_-1</sub>)=dist(_s,u_<sub>_j_-1</sub>) (since \(\eta(u_{j-1})\le i-1\)). Observe that after the next execution of the Bellman-Ford phase (i.e. iteration _i_-1),

\(d(u_j)\le d(u_{j-1})+w(u_{j-1},u_j)\) (11)

