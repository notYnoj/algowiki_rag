## Computing Distances for Updates Efficiently.

It remains to give the precise algorithm to update the data structure when processing the _t<sup>th</sup>_ update to _H_. Here, we focus on updating a single affected piece _P_ (i.e. \(e^t\in P\)) in \(\tilde{O}(\sqrt{|P|})\) time. It then follows immediately that we can update all affected pieces in time \(\tilde{O}(\sqrt{r})\).

We start by describing the first step of our update procedure, that is to compute for each vertex \(x\in\partial P\), the distances _d<sub>P<sup>t</sup></sub>(x,u<sup>t</sup>_) and _d<sub>P<sup>t</sup></sub>(v<sup>t</sup>,x_). Note however, that we can find these distances in the graph _P_<sup>_t_-1</sup>, since shortest paths to _u<sup>t</sup>_ do not need to use an out-going edge of _u<sup>t</sup>_. More precisely, these distances can be found in _P<sup>t</sup>_\\{_e<sup>t</sup>_}=_P_<sup>_t_-1</sup>\\{_e<sup>t</sup>_}. An analogous observation also holds for the distances _d<sub>P<sup>t</sup></sub>(v<sup>t</sup>,x_), i.e. _d<sub>P<sup>t</sup></sub>(v<sup>t</sup>,x_)=_d_<sub>_P_<sup>_t_-1</sup></sub>(_v<sup>t</sup>,x_).

It thus remains to compute these distances in the graph _P_<sup>_t_-1</sup>. To this end, let _P_<sub>1</sub>_,P_<sub>2</sub>_,...,P<sub>k</sub>_ be the unique path in R from piece _P=P_<sub>1</sub> to the leaf piece _P<sub>k</sub>_ containing _e<sup>t</sup>_. Further, for each such _P<sub>i</sub>_, let _P_<sub>_i,_1</sub>_,P_<sub>_i,_2</sub>_,...P_<sub>_i,k<sub>i</sub>_</sub> be the siblings of _P<sub>i</sub>_ in R (this set does not contain _P<sub>i</sub>_ itself). Let <o>_P_</o><sub>_i,_1</sub>_,P_<sub>_i,_2</sub>_,...,P_<sub>_i,k<sub>i</sub>_</sub> be the dense distance graphs of all siblings of _P<sub>i</sub>_.

Next, note that \(\bigcup_{\ell,j}P_{\ell,j}^{t-1}\) forms exactly the graph _P<sup>t</sup>_\\{_e<sup>t</sup>_} by our discussion above and the fact that each leaf of R contains exactly one edge (see Definition 1.2). Further note that our data structure already holds the DDGs \(\overline{P_{i,1}^{t-1}},\overline{P_{i,2}^{t-1}},\dots,\overline{P_{i,k_i}^{t-1}}\).

Then, to find the distances _d<sub>P<sup>t</sup></sub>(v<sup>t</sup>,x_) for \(x\in\partial P\), we can invoke the following version of FR- Dijkstra which is a stronger version of Theorem 1.3.

**Theorem 5.3** (Extended FR-Dijkstra, see \[16, 21\])**.** _Given a graph G, an r-capped recursive decomposition_ R _a set of edge-disjoint pieces X_<sub>1</sub>_,X_<sub>2</sub>_,...,X<sub>k</sub> in_ R_, along with a data structure that answers queries for edge weights in their corresponding dense distance graphs_ <o>X</o><sub>1</sub>_,<o>X</o>_<sub>2</sub>_,...<o>X</o><sub>k</sub> in_ \(\tilde{O}(1)\) _time._

_Then, there exists an algorithm that given some_ \(v\in\bigcup_j\partial X_j\)_, computes a shortest path tree T<sub>v</sub> in_ \(\bigcup_j\overline{X_j}\) _in time_ \(\tilde{O}(\sum_j\sqrt{|X_j|})\).

It is not hard to see that this not only gives all distance _d<sub>P<sup>t</sup></sub>(v<sup>t</sup>,x_) when invoked for vertex _v<sup>t</sup>_, but also with a single invocation of this algorithm, we can find all distances _d<sub>P<sup>t</sup></sub>(x,u<sup>t</sup>_) by reversing all edges in the dense distance graphs and invoking the theorem again for _u<sup>t</sup>_. Thus, the total time to find all such distances for our fixed piece _P_ is \(\tilde{O}(\sqrt{|P|})\).

## Updating D_<sub>b,h</sub>_ Efficiently.

Let us now describe how to update the data structures D_<sub>b,h</sub>_ for each \(b\in\partial P\) and \(h\in h(P)\). We first point out that we only need to update the data structures for affected pieces.

Let us fix _P,b_ and _h_ for the rest of this section and let \(h'\) be the hole in _h(P_) with _b_ on \(h'\). Note that for every \(b'\in h\), we could query the distances \(d_{P^{t-1}}(b,b')\) in the current version of the data structure. We could then verify using the information computed in the last paragraph whether \(d_{P^{t-1}}(b,b')<d_{P^t}(b,u^t)+\omega^t+d_{P^t}(v^t,b')\) for each \(b'\). However, we aim to identify the entire set _S<sub>b,h</sub>_ of all such vertices \(b'\in h\) in \(\tilde{O}(1)\) time. To this end, we first need to prove that _S<sub>b,h</sub>_ consists of at most two subintervals of _Q(h_) so that we can represent this set by the _O_(1) endpoints of such intervals. This will allow us to update each affected data structure D_<sub>b,h</sub>_ in \(\tilde{O}(1)\) time and thus update all such affected data structures in time \(\tilde{O}(\sqrt{r})\) since we only have to perform this operation once for each affected _P_ and every vertex _b_ on _h(P_).

Here, we prove an even more powerful statement that we further build upon in the next section when we show how to compute _S<sub>b,h</sub>_ efficiently. We need some additional notation and we start with<tbc>

