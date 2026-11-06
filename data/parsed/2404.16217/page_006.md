## 6 Fault-Tolerant Bounded Flow Preservers

Thus even after _k_ faults atleast one path from _r<sub>i</sub>_ to _v<sub>j</sub>_ will exist in H\\_F_. This contradicts the assumption that there is no _s_ to _v<sub>j</sub>_ path in G\\_F_ passing through _r<sub>i</sub>_. Hence, max-flow(_s,v<sub>j</sub>,_G\\_F_) must be identical to max-flow(_s,v<sub>j</sub>,_H\\_F_). \(\blacktriangleleft\)

The proof of Theorem 7 now directly follows from Lemma 9, Lemma 10, and Lemma 11, along with the fact that for every integer \(n\ge 1\), there exist hard instances of the SET- COVER problem (_U,_F) satisfying |_U_|=_n_, where the size of the optimal solution is significantly larger than log|_U_|.

## 4 Upper bound of \(\lambda 2^kn\) Edges

In this section we will provide construction of a sparse \((\lambda,k)\)-FT-BFP.

### 4.1 Locality Property for Flow Preservers

\(\blacktriangleright\) **Lemma 12.** _Let_ G=(_V,E_) _be a graph with a source_ \(s\in V\), \(\lambda\ge 1\) _be an integer, and v be a vertex in V. Let_ \(\alpha=min\left(\lambda,max-flow(s,v,\mathcal{G})\right)\)_. Let_ E_<sub>v</sub> be the set of in-edges of v corresponding to any arbitrary set of_ \(\alpha\)_-edge-disjoint paths from s to v in_ G_. Further, let_ H _be a subgraph of_ G _obtained by restricting the in-edges of v to those present in_ E_<sub>v</sub>. Then, for any vertex_ \(t\in V\),

\(max-flow(s,t,\mathcal{H})\ge min\left(\lambda,max-flow(s,t,\mathcal{G})\right).\)

**Proof.** By construction of _H_, \(\alpha=max-flow(s,v,H)\). Denote \(\beta=max-flow(s,t,H)\). Let (_A,B_) be an (_s,t_)-min-cut in _H_. If \(v\in A\) then, by construction of _H_, the (_s,t_)-cut (_A,B_) has value \(\beta\) also in _G_, so \(\beta\ge max-flow(s,t,G)\) and we are done. Assume next \(v\in B\). Then (_A,B_) is an (_s,v_)-cut of value \(\beta\) in _H_. By construction of _H_, \(\alpha=max-flow(s,v,H)\), so \(\beta\ge\alpha\). If \(\alpha=\lambda\) we are done, so assume \(\alpha=max-flow(s,v,G)\).

We now show that \(\beta\ge max-flow(s,t,G)\), which ends the proof. Suppose not, and let _f_ be an (_s,t_)-max-flow in _H_. Then the residual graph _G<sub>f</sub>_ must have an augmenting path _P_, containing some edges present in _G_ but not in _H_. Such edges are all incoming to _v_. Thus, \(P=P[s,w]\circ(w,v)\circ P[w,t]\) where \((w,v)\in E(G)\backslash E(H)\), and _P[s,w],P[v,t_] are present in the residual graph _H<sub>f</sub>_. Adding _P_ to _f_ gives an (_s,t_)-flow of in _H_+(_w,v_), implying that

**1.** max-flow(_s,t,H_+(_w,v_))=\(\beta+1\)

**2.** \((w,v)\in A\times B\)

**3.** (_A,B_) is an (_s,t_)-min-cut in _H_+(_w,v_)

Let \(\{Q_i\circ e_i\circ Q'_i\}_{i=1}^\alpha\) be \(\alpha\) edge-disjoint _s_-to-_v_ paths in _H_, where the edge _e<sub>i</sub>_ of each such path is its last edge crossing the (_s,v_)-cut (_A,B_), so \(V(Q'_i)\subseteq B\). Such exist as \(\alpha=max-flow(s,v,H)\). Let \(e_{\alpha+1},\dots,e_\beta\) be the other edges crossing (_A,B_) in _H_. Let _e_<sub>0</sub>=(_w,v_), crossing (_A,B_) by (ii). Let \(\{P_j\circ e_j\circ P'_j\}_{j=0}^\beta\) be \(\beta+1\) edge-disjoint _s_-to-_t_ paths in _H_+(_w,v_), each crossing the cut (_A,B_) exactly once, at _e<sub>j</sub>_, so \(V(P_j)\subseteq A\). Such exist by (i) and (iii). Then, \(\{P_0\circ e_0\}\cup\{P_i\circ e_i\circ Q'_i\}_{i=1}^\alpha\) are \(\alpha+1\) edge-disjoint _s_-to-_v_ paths in _G_, contradicting \(\alpha=max-flow(s,v,G)\). \(\blacktriangleleft\)

In the next lemma we show that in order to compute a sparse \((\lambda,k)\)-FT-BFP it suffices to focus on a single destination node.

