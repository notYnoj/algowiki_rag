By running Claim 6.10 immediately after step 3, we have the additional property that each chain has length \(\unknown 2n/\ell=D/8\). Note that we maintain the required properties of C, so that correctness is maintained. As a corollary of Claim 6.9 and Claim 6.10, we have that with high probability

\(V(\mathcal{C}')=O(nlogn/D).\) (6)

We now present our algorithm for computing \(\hat{H}\). Consider the graph <o>_G_</o> constructed as follows:

1. Add a vertex for every \(v\in V(G)\) and edge \(e\in E(G)\) with weight wt(_e_)=0.<tbc>

2. For every \(C\in\mathcal{C}'\), add a vertex _t<sub>C</sub>_.<tbc>

3. For every \(C\in\mathcal{C}'\), denote _C_={_c_<sub>1</sub>_,...,c<sub>p</sub>_}. Add a path \(\pi_{C,i}\) of _i_ edges with weight 1 from _c<sub>i</sub>_ to _t<sub>C</sub>_ for all \(1\unknown i\unknown p\). Note that distinct \(\pi_{C,i}\) are vertex disjoint except for _t<sub>C</sub>_.

We claim that distances from \(v\in V'\) to _t<sub>C</sub>_ for \(C\in\mathcal{C}'\) allow us to compute _w(v,C_).

**Claim 6.11.** _Let_ \(v\in V'\) _and_ \(C\in\mathcal{C}'\)_. Let C_={_c_<sub>1</sub>_,...,c<sub>p</sub>}. Then, w(v,C_)=_c<sub>i</sub> if and only if_ dist<o>_G_</o>(_v,t<sub>C</sub>_)=_i._

_Proof._ Fix \(v\in V',C\in\mathcal{C}'\) and let _w_:=_w(v,C_). If _w=c<sub>i</sub>_, there is a path from _v_ to _w_ using only edges in _E(G_), and thus a path _P_<sub>0</sub> of weight 0 from _v_ to _w_ in <o>_G_</o>. Then, \(P_0\circ\pi_{C,i}\) is a path of length _i_ from _v_ to _t<sub>C</sub>_, establishing \(\mathrm{dist}_\overline{G}(v,t_C)\unknown i\).

Suppose dist<o>_G_</o>(_v,t<sub>C</sub>)\<i_. We claim there is a vertex _c<sub>j</sub>_ with _j\<i_ such that \((v,c_j)\in\mathrm{TC}(G)\), contradicting the minimality of _c<sub>i</sub>_. Let _c<sub>j</sub>_ be the final vertex in _C_ on the shortest path from _v_ to _t<sub>C</sub>_. Note that _j\<i_ since the \(\pi_{C,j}\) has length _j_. However, this implies that \((v,c_j)\in\mathrm{TC}(G)\) since there is no path from vertices in \(\pi_{C^\prime,i^\prime}\backslash c'_{i^\prime}\) for any \(C',i'\) to vertices in _G_, so any path from _v_ to _c<sub>j</sub>_ must be contained in _E(G_). In particular, \((v,c_j)\in\mathrm{TC}(G)\), contradicting the minimality of _i_.

Thus, it suffices to compute dist<o>_G_</o>(_v,t<sub>C</sub>_) for all \(v\in V'\) and \(C\in\mathcal{C}'\). Equivalently, we can compute dist<o>_G_</o><sub>rev</sub>(_t<sub>C</sub>,v_), which requires one invocation of MSSP on <o>_G_</o><sub>rev</sub>. To bound the running time, it remains to show that <o>_G_</o> is a DAG with \(\widetilde{O}\left(n\right)\) vertices and diameter _O(D_). The number of vertices in <o>_G_</o> is

\(O\left(n+|\mathcal{C}'|D^2\right)=O\left(nlogn\right).\)

Next, we claim <o>_G_</o> is a DAG. First, observe that there is no path from any vertex not in _V(G_) to a vertex in _V(G_), so no SCC can contain both a vertex in _V(G_) and one not in _V(G_). In particular, the additional vertices and edges introduce no paths between vertices in _V(G_), so no SCC can contain multiple vertices in _V(G_). To conclude, observe that no SCC can contain multiple vertices not in _V(G_). Finally, we claim <o>_G_</o> has diameter _O(D_). This follows as any \((u,v)\in\mathrm{TC}(G)\) has a path of length 0 in <o>_G_</o> (by following edges in _G_) and any of the additional paths \(\pi_{C,i}\) has length _O(D_) by Claim 6.10.

Thus, we invoke Proposition 6.4 on <o>_G_</o><sub>rev</sub> with sources {_t<sub>C</sub>_} to compute the required distances and \(\hat{H}\) in \(\widetilde{O}\left(\mathsf{T}_\mathrm{MPP}(n/D^2,n,n|D,1)\right)\) time, completing the proof of Theorem 6.6.

## References

