_interval_ \[_v<sub>i</sub>(h),v<sub>j</sub>(h_)\] for the hole _h_, where if \(1\le i\le j\le s_h\) the interval is defined as above and if \(1\le j<i\le s_h\), is defined to be the interval {_v<sub>i</sub>(h),v_<sub>_i_+1</sub>(_h),...,v<sub>s<sub>h</sub></sub>(h),v_<sub>1</sub>(_h),v_<sub>2</sub>(_h),...,v<sub>j</sub>(h_)}. We define (_v<sub>i</sub>,v<sub>j</sub>_) to be \[_v<sub>i</sub>,v<sub>j</sub>_\]\\{_v<sub>i</sub>,v<sub>j</sub>_}. We use the above indexing trick for _v<sub>i</sub>_’s where _i_ is potentially larger than _s<sub>h</sub>_ in conjunction with intervals, and wrapped intervals.

Finally, we require a simple data structure.

**Theorem 5.2.** _\[Last Interval Detection Data Structure\] Given a universe of size U, we can maintain a data structure that allows adding at time_ \(i\ge 1\)_, a sub-interval_ \([l_i,r_i]\subseteq[1,U]\)_, and for queries at time i where on input_ \(x\in[1,U]\)_, the data structure outputs the largest integer_ \(j\le i\)_, such that_ \(x\in[l_j,r_j]\) _where we assume that_ \[_l_<sub>0</sub>_,r_<sub>0</sub>\]=\[1_,U_\] _(so j is well-defined). If the length of the update sequence is polynomially bounded in n, then the data structure can be implemented with pre-processing time_ \(\tilde{O}(1)\) _and_ \(\tilde{O}(1)\) _worst-case update and query time._

## Initialization.

We start by computing initially, for each piece _P_ in the tree of R rooted at _H_, the DDG using the FR-Dijkstra algorithm \[16\] (we later show that we need to store slightly more information to make updates efficient). We further initialize for each piece _P_, boundary vertex \(b\in\partial P\) and for each hole \(h\in h(P)\) a Last Interval Detection data structure D_<sub>b,h</sub>_ on the universe _Q(h_)={_v_<sub>1</sub>(_h),v_<sub>2</sub>(_h),...,v<sub>s<sub>h</sub></sub>(h_)} as described in Theorem 5.2.

## Updates.

After the _t<sup>th</sup>_ update, we compute and store for each piece _P_, with \(e^t=(u^t,v^t)\in P\), the distances _d<sub>Pt</sub>(b,u<sup>t</sup>_) and _d<sub>Pt</sub>(v<sup>t</sup>,b_) for each \(b\in\partial P\). Further, for each such piece _P_, \(b\in\partial P\), and hole \(h\in h(P)\), we find the set of vertices \(S_{b,h}\subseteq Q(h)\) such that for each \(b'\in S_{b,h}\),

\(d_{P^{t-1}}(b,b')>d_{Pt}(b,u^t)+\omega^t+d_{Pt}(v^t,b').\)

We say that a vertex \(b'\in S_{b,h}\) _profits_ from _e<sup>t</sup>_.

We will later see that _S<sub>b,h</sub>_ consists of at most two subintervals of _Q(h_). We add these two subintervals to the data structure D_<sub>b,h</sub>_. Before we show how to implement updates efficiently, let us illustrate a query of the data structure.

## Queries.

Consider a query for the weight of an edge in the DDG of some piece _P_ from a boundary vertex _b_ to a boundary vertex \(b'\).

We can now simply query the data structure D_<sub>b,h</sub>_ for vertex \(b'\). This allows us to locate the last time _t_ that the shortest path from _b_ to \(b'\) (in _P_) was decreased in weight (note that technically the times of D_<sub>b,h</sub>_ and versions of the pieces _P_ do not align however it is straight-forward to pair them). Since the decrease must have resulted from decreasing the weight of edge _e<sup>t</sup>_, we can now simply output

\(d_{Pt}(b,b')=d_{Pt}(b,u^t)+\omega^t+d_{Pt}(v^t,b').\)

Since we stored _d<sub>Pt</sub>(b,u<sup>t</sup>),d<sub>Pt</sub>(v<sup>t</sup>,b_) and \(\omega^t\) at time step _t_, a look-up suffices to recover them once _t_ is known. Since \(b'\) has not profited from any edge thereafter, we conclude that the returned distances is the current distance.

