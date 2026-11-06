For each \(1<i\le q\), let _T<sub>i</sub>_ be the sub-tree of _T_ rooted at the vertex \(v'_i\). We prove the following claim:

**Claim 4.14** _For all_ \(1<i\le q\)_, the total cost of all vertices in T<sub>i</sub> is at most_ \(O(N(v'_i)logloglogN)\).

Assume first that the above claim is correct. Notice that every vertex of _T_ that does not lie on the path _P_ must belong to one of the trees _T<sub>i</sub>_. The total cost of all vertices lying in all trees _T<sub>i</sub>_ is then bounded by \(\sum_{i=2}^qO(N(v'_i)logloglogN)\le O(logNlogloglogN)\). Since the total cost of all vertices on the path _P_ is bounded by 2log_N_, overall, the total cost of all vertices in _T_ is bounded by _O_(log_N_logloglog_N_).

In order to complete the proof of Lemma 4.13, it now remains to prove Claim 4.14.

**Proof of Claim 4.14.** We fix some index \(1<i\le q\), and consider the vertex \(v'_i\). If the parent _v_<sub>_i_-1</sub> of \(v'_i\) belongs to a different class than \(v'_i\), then \(v'_i\) must be an important vertex in its class. In this case, since we have assumed that Event E does not happen, \(N(v'_i)\le O(loglogN)\). From Claim 4.1, the total cost of all vertices in _T<sub>i</sub>_ is bounded by

\(\sum_{v\in V(T_i)}\mathsf{cost}(v)\le O(N(v'_i)log(N(v'_i)))\le O(N(v'_i)logloglogN)\)

Therefore, we can assume from now on that _v_<sub>_i_-1</sub> and \(v'_i\) both belong to the same class, that we denote by _Q<sub>j</sub>_. Notice that, if a vertex _v_ belongs to class _Q<sub>j</sub>_, then at most one of its children may belong to class _Q<sub>j</sub>_; the other child must belong to some class \(Q_{j^\prime}\) for \(j'<j\), and it must be an important vertex in its class.

We now construct a path _P<sub>i</sub>_ in tree _T<sub>i</sub>_ iteratively, as follows. The first vertex on the path is \(v'_i\). We then iteratively add vertices at to the end of path _P<sub>i</sub>_ one-by-one, so that every added vertex belongs to class _Q<sub>j</sub>_. In order to do so, let _v_ be the last vertex on the current path _P<sub>i</sub>_. If some child _u_ of _v_ also lies in class _Q<sub>i</sub>_, then we add _u_ to the end of _P<sub>i</sub>_ and continue to the next iteration. Otherwise, we terminate the construction of the path _P<sub>i</sub>_.

Denote the sequence of vertices on the final path _P<sub>i</sub>_ by \((v'_i=u_1,u_2,\dots,u_z)\); recall that every vertex on _P<sub>i</sub>_ belongs to class _Q<sub>j</sub>_, and that path _P<sub>i</sub>_ is a sub-path of some path connecting \(v'_i\) to a leaf of _T<sub>i</sub>_. Let _Z_ be a set of vertices containing, for all \(1<z'\le z\) a sibling of the vertex \(u_{z^\prime}\), and additionally the two children of _u<sub>z</sub>_ (if they exist). Note that every vertex \(x\in Z\) is an important vertex in its class, and, since we have assumed that Event E did not happen, \(N(x)\le O(loglogN)\). For every vertex \(x\in Z\), we denote by \(T'_x\) the sub-tree of _T_ rooted at _x_. From Claim 4.1, \(\mathsf{cost}(T'_x)\le O(N(x)log(N(x)))=O(N(x)logloglogN)\).

Notice that all strips in \(\{S(x)|x\in Z\}\) are disjoint from each other, except for possibly sharing a boundary. It is then easy to see that \(\sum_{x\in Z}N(x)\le N(v'_i)\). Therefore, altogether \(\sum_{x\in Z}\mathsf{cost}(T'_x)\le O(N(v'_i)logloglogN)\)).

Lastly, notice that every vertex of _V(T<sub>i</sub>_) either lies on _P<sub>i</sub>_, or belongs to one of the trees \(T'_x\) for \(x\in Z\). Since, from Claim 4.1, the total cost of all vertices on _P<sub>i</sub>_ is bounded by \(N(v'_i)\), altogether, the total cost of all vertices in _T<sub>i</sub>_ is bounded by \(O(N(v'_i)logloglogN)\).

\(\square\)

To summarize, if the shift _s_ is chosen such that Event E does not happen, then \(WB_\sigma(X_s)\le O(logNloglogN)\). Assume now that the shift _s_ is chosen such that Event E happens. From<tbc>

