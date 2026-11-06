<tbc>which will be later added to _E<sup>rem</sup>_. We recurse the algorithm on this ball (Line 16) which may add more edges to _E<sup>rem</sup>_ (via _E<sup>recurse</sup>_). Finally, we remove this ball from the graph and repeat the process. Note that the algorithm may also terminate prematurely with _E<sup>rem</sup>=E(G_) in Lines 15 and 20. We will show that this happens with very low probability (Section 6.3).

**Analysis.** The remainder of this section is devoted to analyze the above algorithm. In Section 6.1, we make a few simple observations. Then, in Section 6.2, we analyze the runtime of the algorithm. The next two subsections are to bound the probability that an edge is in _E<sup>rem</sup>_: in Section 6.3 we prove that the probability that the algorithm terminates prematurely on Lines 15 or 20 is very small, and complete the bound of \(Pr[e\in E^{rem}]\) in Section 6.4. Finally, in Section 6.5, we prove the diameter bound, completing the proof of Lemma 1.2.

## 6.1 Observations

**Observation 6.4.** _Consider the execution of an initial call_ LDD(_G,D_) _and let_ LDD(_G<sub>i</sub>,D_) _denote all the lower-level recursive calls that follow from it. The following always holds:_

1. _For each vertex v, there are at most O_(log(_n_)) _calls_ LDD(_G<sub>i</sub>,D_) _such that G<sub>i</sub> contains v._<tbc>

_2._ _The total number of recursive calls_ LDD(_G<sub>i</sub>,D_) _is O(n_log(_n_)).

_Proof._ The second property follows from the first because _G_ has at most _n_ vertices, and each call LDD(_G<sub>i</sub>_) contains at least one of those vertices. For the first property, note that **(i)** recursion only occurs in Line 16, **(ii)** if a vertex participates in the recursion in Line 16, it will be removed from _G_ on Line 18, **(iii)** each time the algorithm recurses, the number of vertices in the child-graph is at most 7/10 the number of vertices in the parent-graph because otherwise the algorithm terminates in Line 15 without recursing, and **(iv)** the algorithm always terminates when |_V(G_)|=1 because every vertex is heavy in this case, so the while loop is never executed and no recursion occurs. Thus, a single vertex can participate in only log<sub>10/7</sub>(_n_)=_O_(log(_n_)) recursive calls.

**Observation 6.5.** _Consider any call_ LDD(_G,D_) _and say that the algorithm makes some recursive call_ \(\text{LDD}(G[\text{Ball}_G^*(v,R_v)],D)\) _in Line 16. Then, once the call_ LDD(_G,D_) _terminates, if vertex_ \(x\in\text{Ball}_G^*(v,R_v)\) _and vertex_ \(y\notin\text{Ball}_G^*(v,R_v)\)_, then x and y are not in the same SCC in G_\\_E<sup>rem</sup>._

_Proof._ Say that the recursive call is on an out-ball \(\text{Ball}_\text{G}^\text{out}(v,R_v)\); the argument for in-balls is the same. Note that all the edges of \(\text{Ball}_\text{G}^\text{out}(v,R_v)\) are added to _E<sup>boundary</sup>_ (Line 14) and later to _E<sup>rem</sup>_ (in Lines 15 or 17). Thus, in _G_\\_E<sup>rem</sup>_ there are no edges leaving \(\text{Ball}_\text{G}^\text{out}(v,R_v)\), so clearly vertices _x_ and _y_ cannot be in the same SCC.

## 6.2 Running Time Analysis

**Lemma 6.6.** _The total running time of_ LDD(_G,D_) _is O_(|_V(G_)|log<sup>3</sup>(_n_)+|_E(G_)|log<sup>2</sup>(_n_)).

_Proof._ Let us first consider the non-recursive work, i.e. everything except Line 16. The balls in Line 5 are computed via _k=O_(log(_n_)) executions of Dijkstra’s algorithm in total time _O_(|_V(G_)|log<sup>2</sup>(_n_)+|_E(G_)|log(_n_)). The sets in Line 6 are computed from the information in Line 5.

Every time the algorithm executes the While loop in Line 11 it first samples _R<sub>v</sub>_∼Geo(_p_) from the geometric distribution; this can be done in _O_(log(_n_)) time using e.g. \[BF13\].<sup>19</sup> It then computes some ball \(\text{Ball}_\text{G}^*(v,R_v)\) (Line 13). All vertices in this ball are then removed from _G_ (Line 18), so<tbc>

<sup>19</sup>By Theorem 5 in \[BF13\] with _p_=log(_n)/D_ and word size \(w=\Omega(loglogD)\), the expected time is _O_(log(min{_D/_log_n,n_})/log_w_)=_O_(log_n_). Note that there might be other simpler methods since we do not need an exact algorithm.

