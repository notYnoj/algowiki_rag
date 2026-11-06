Thus, \(X'\) is indeed a valid solution for I. \(\lrcorner\)

Next, we analyze the structure of _S_ inside a single path from P. We show that at most one unprofitable edge per path is needed.

**Claim 9.** _If two edges e<sub>i</sub> and e<sub>j</sub> from S with i\<j lie on the same path P in_ P _and_ \(\mathbf{rp}(S_{j-1},e_j)\le 0\)_, then_ \(X':=X+e_j-(\mathrm{Inv}(e_j)\backslash\mathrm{Inv}(S_{j-1}))\) _is also a solution for_ I.

_Proof of Claim 9._ Consider an edge \(e_j\in S\) for which there exists an edge \(e_i\in S\) with _i\<j_ from the same path _P_. Choose _e<sub>i</sub>_ with the maximum possible index. Note that in this case _S_<sub>_j_-1</sub>=_S<sub>i</sub>_: since _e_<sub>1</sub>_,...,e_<sub>_n_-1</sub> is a P-respecting ordering, the edges of the path _P_ form a contiguous subsegment. Hence, for every index \(i'\) with \(i<i'<j\), the edge \(e_{i^\prime}\) also lies on the path _P_ and it cannot belong to _S_; otherwise, this would contradict the maximality of _i_.

Suppose that _e<sub>j</sub>_ goes from _x_ to _y_, and let _L_ be the set of vertices reachable from _y_ via _tree_ edges in \(X'\). Denote the starting vertex of _e<sub>i</sub>_ by _z_. Observe that _L_ is a subpath of _P_ between _y_ and _z_ (inclusive): since _e_<sub>1</sub>_,...,e_<sub>_n_-1</sub> is a P-respecting ordering, all edges on the tree path from _y_ to _z_ have indices between _i_+1 and _j_-1, and are therefore present in \(X'\), because _S_<sub>_j_-1</sub>=_S<sub>i</sub>_. Consequently, every vertex on this path belongs _L_. On the other hand, all these vertices are internal vertices of _P_ and hence each of them has exactly one outgoing edge in _T_. Combining with the fact that \(e_i\notin E(X')\), this implies that _L_ contains no other vertices.

We aim to show that \(N_{X^\prime}[L]=L\):

• For every _tree_ edge \(\ell\rightarrow v\) with \(\ell\in L\), the ending vertex _v_ must also belong to _L_ by the definition of _L_.<tbc>

• Since _L_ consists only of internal vertices of _P_, no vertex in _L_ is incident to any _allowed_ edge; this follows directly from the definition of a proper path cover.<tbc>

• Consider a _blocked_ edge \(e=\ell\rightarrow v\) in \(X'\) such that \(\ell\in L\). By Observation 1, _T_ contains a directed path \(P'\) from _v_ to \(\ell\). First, we claim that \(e\notin\mathrm{Inv}(S_{j-1})\). Assume the contrary. Then there exists an edge \(e_t\in S_{j-1}\) such that \(e\in\mathrm{Inv}(e_t)\). Since _S_<sub>_j_-1</sub>=_S<sub>i</sub>_, we have \(t\le i\). By Observation 1, _e<sub>t</sub>_ lies on \(P'\). Thus there is also a directed path in _T_ that starts at _e<sub>t</sub>_ and ends in \(\ell\). Observe that there is only one tree edge _e<sub>s</sub>_ that leads to \(\ell\) and it lies between _e<sub>j</sub>_ and _e<sub>i</sub>_ (including _e<sub>j</sub>_, but not _e<sub>i</sub>_) on the path _P_. Hence, we have that \(i<s\le j\). Consequently, there must be a path in _T_ that starts at _e<sub>t</sub>_ and ends at _e<sub>s</sub>_, which contradicts the definition of P-respecting ordering, because \(t\le i<s\).<tbc>

<tbc>Next, suppose that \(v\notin L\). Recall that every vertex in _L_ has exactly one incoming tree edge (as they are internal vertices of _P_). Moreover, _e<sub>j</sub>_ is the only tree edge that goes from _V_\\_L_ to _L_. Since \(v\in(V\backslash L)\) and \(\ell\in L\), \(P'\) must contain _e<sub>j</sub>_. By Observation 1, it follows that \(e\in\mathrm{Inv}(e_j)\). But this is impossible, because together with \(e\notin\mathrm{Inv}(S_{j-1})\), we would have \(e\in(\mathrm{Inv}(e_j)\backslash S_{j-1})\). But \(E(X')\cap(\mathrm{Inv}(e_j)\backslash\mathrm{Inv}(S_{j-1}))=\emptyset\), and hence the edge _e_ cannot be in \(X'\).

Using this fact, it is easy to see that \(X'\) is acyclic. If \(X'\) contained a cycle, this cycle would have to include the edge \(e_j=x\rightarrow y\), since it is the only edge in \(X'\) that is not present in _X_. It would then follow that _x_ is reachable from _y_ in \(X'\). But note that \(x\notin L\) and \(y\in L\). This leads us to the contradiction, because \(N_{X^\prime}[L]=L\).

