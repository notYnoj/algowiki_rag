// Input/Output: See Theorem 3.5<br>
if \(\Delta\le 2\) then<br>
Let<br>
\(\phi_2=0\)<br>
and<br>
jump<br>
to<br>
Phase<br>
3<br>
(<br>
Line<br>
10<br>
)<br>
Let<br>
\(d=\Delta/2\)<br>
.<br>
Let<br>
\(G_{\ge 0}^B:=(V,E,w_{\ge 0}^B)\)<br>
where<br>
\(w_{\ge 0}^B(e):=max\{0,w^B(e)\}\)<br>
for<br>
all<br>
\(e\in E\)<br>
// Phase 0: Decompose V to SCCs V<sub>1</sub>,V<sub>2</sub>,... with weak diameter dB in G<br>
\(E^{rem}\leftarrow\) LowDiamDecomposition\((G_{\ge 0}^B,dB)\) (Lemma 1.2)<br>
Compute Strongly Connected Components (SCCs) of G<sup>B</sup>\\E<sup>rem</sup>, denoted by V<sub>1</sub>,V<sub>2</sub>,...<br>
// Properties: (Lemma 4.3) For each \(u,v\in V_i\), dist<sub>G</sub>(u,v)\le dB\).<br>
// (Lemma 4.4) If \(\eta(G^B)\le\Delta\), then for every \(v\in V_i\), \(E[P_{G^B}(v)\cap E^{rem}]=O(log^2n)\)<br>
// Phase 1: Make edges inside the SCCs G<sup>B</sup>\[V<sub>i</sub>\] non-negative<br>
Let \(H=\bigcup_iG[V_i]\), i.e. H only contains edges inside the SCCs.<br>
// (Lemma 4.5) If G has no negative-weight cycle, then \(\eta(H^B)\le d=\Delta/2\).<br>
\(\phi_1\leftarrow\) Scale\(Down(H,\Delta/2,B)\) // (Corollary 4.6) \(w_{H_{\phi_1}^B}(e)\ge 0\) for all \(e\in H\)<br>
// Phase 2: Make all edges in G<sup>B</sup>\\E<sup>rem</sup> non-negative<br>
\(\psi\leftarrow\) FixDAGEdges\((G_{\phi_1}^B\backslash E^{rem},\{V_1,V_2,\dots\})\) (Lemma 3.2)<br>
\(\phi_2\leftarrow\phi_1+\psi\) // (Lemma 4.7) All edges in \((G^B\backslash E^{rem})_{\phi_2}\) are non-negative<br>
// Phase 3: Make all edges in G<sup>B</sup> non-negative<br>
\(\psi'\leftarrow\) Elim\(Neg((G_s^B)_{\phi_2},s)\) (Lemma 3.3) // (Theorem 4.2) expected time O(mlog<sup>3</sup>m).<br>
(To define \((G_s^B)_{\phi_2}\) here, we define \(\phi_2(s)=0\).)<br>
\(\phi_3=\phi_2+\psi'\) // (Theorem 4.1) All edges in \(G_{\phi_3}^B\) are non-negative.<br>
return \(\phi_3\) ; // Since \(w_{\phi_3}^B(e)\ge 0\), we have \(w_{\phi_3}(e)\ge-B\)

## 4 Algorithm ScaleDown (Theorem 3.5)

We start by describing the algorithm ScaleDown, as this contains our main conceptual contributions; the much simpler algorithm SPmain is described in the following section. Full pseudocode of ScaleDown is given in Algorithm 1. The algorithm mostly works with graph _G<sup>B</sup>_=(_V,E,w<sup>B</sup>_). For the analysis, the readers may want to familiarize themselves with, e.g., \(G_s^B\), \(w_s^B\), _P<sub>G<sup>B</sup></sub>(v_) and \(\eta(G^B)\) from Definitions 2.3 and 2.4. In particular, throughout this section, source _s always_ refers to a dummy source that has outgoing edges to every vertex in _V_ and has no incoming edges.

Note that \(m=\Theta(n)\) since the input condition requires constant out-degree for every vertex. So, we use _m_ and _n_ interchangeably in this section. We briefly describe the ScaleDown algorithm and sketch the main ideas of the analysis in Section 4.1, before showing the full analysis in Section 4.2.

### 4.1 Overview

The algorithm runs in phases, where in the last phase it calls \(\mathrm{ElimNeg}((G_s^B)_{\phi_2},s)\) for some price function \(\phi_2\) (Line 10). Recall (Lemma 3.3) that if ElimNeg terminates, it returns price function \(\psi'\) such that all edge weights in \((G_s^B)_{\phi_2+\psi^\prime}\) are non-negative. Consequently, all edge weights in \(G_{\phi_3}^B\) are non-negative for \(\phi_3=\phi_2+\psi'\) (since \(G_{\phi_2}^B\) is a subgraph of \((G_s^B)_{\phi_2}\)). We thus have \(w_{\phi_3}(e)\ge-B\) for all \(e\in E\) as desired (because \(w^B(e)\le w(e)+B\)). This already proves the output correctness of ScaleDown (Item 2 of Theorem 3.5). (See Theorem 4.1 for the detailed proof.) Thus it remains to<tbc>

**Algorithm 1:** Algorithm for Scale\(\Downtext{own}(G=(V,E,w),\Delta,B)\)

