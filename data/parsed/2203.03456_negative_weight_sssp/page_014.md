where (b) and (c) are because the edges from _s_ to _u_ and _v_ in \(H_s^B\) have weight zero. Then,<sup>13</sup>

\(\mathrm{dist}_G(u,v)\le w_H(P)\le^{(a)}w_{H^B}(P)-|E^{neg}(H^B)\cap P|\cdot B\)<br>
\(=^{(b)}w_{H^B}(P)-\eta_{H^B}(v)\cdot B\le^{(c)}-\eta_{H^B}(v)\cdot B.\) (3)

Note that _u_ and _v_ are in the same SCC _V<sub>i</sub>_;<sup>14</sup> thus, by Lemma 4.3:

\(\mathrm{dist}_G(v,u)\le dB.\) (4)

If _G_ contains no negative-weight cycle, then \(\mathrm{dist}_G(u,v)+\mathrm{dist}_G(v,u)\ge 0\) and thus \(\eta_{H^B}(v)\le dB\cdot(1/B)=d\) by Equations (3) and (4). Since this holds for every \(v\in V\) , Lemma 4.5 follows.

Consequently, ScaleDown (Theorem 3.5) is guaranteed to output \(\phi_1\) as follows.

**Corollary 4.6.** _If G has no negative-weight cycle, then all edges in_ \(G_{\phi_1}^B[V_i]\) _are non-negative for every i._

**Phase 2: Make all edges in** _G<sup>B</sup>_\\_E<sup>rem</sup>_ **non-negative.** Now that all edges in \(G_{\phi_1}^B[V_i]\) are non- negative, we turn to the remaining edges in _G<sup>B</sup>_\\_E<sup>rem</sup>_. Intuitively, since these remaining edges (i.e. those not in the SCCs) form a directed acyclic graph (DAG), calling FixDAGEdges(\(G_{\phi_1}^B\backslash E^{rem},\{V_1,V_2,\dots\}\)) (Lemma 3.2) in Phase 2 produces the following result.

**Lemma 4.7.** _If G has no negative-weight cycle, all weights in_ \(G_{\phi_2}^B\backslash E^{rem}\) _are non-negative._

_Proof._ Clearly, \(G_{\phi_1}^B\backslash E^{rem}\) and {_V_<sub>1</sub>_,V_<sub>2</sub>_,..._} satisfy the input conditions of Lemma 3.2, i.e. (1) \((G^B\backslash E^{rem})_{\phi_1}[V_i]\) contains no negative-weight edges for every _i_ (this is due to Corollary 4.6), and (2) when we contract every _V<sub>i</sub>_ into a node, the resulting graph is a DAG (since the _V<sub>i</sub>_ are precisely the (maximal) SCCs of \(G_{\phi_1}^B\backslash E^{rem}\)).<sup>15</sup> Thus, FixDAGEdges(\((G^B\backslash E^{rem})_{\phi_1},\{V_1,V_2,\dots\}\)) returns \(\psi\) such that \((G_{\phi_1}^B\backslash E^{rem})_\psi=G_{\phi_2}^B\backslash E^{rem}\) contains no negative-weight edges.

**Phase 3 runtime.** Now we are ready to prove Theorem 4.2, i.e. the runtime bound of \(\mathrm{ElimNeg}((G_s^B)_{\phi_2},s)\) in Phase 3 when _G_ contains no negative-weight cycle. We start by clarifying the nature of the graph \((G_s^B)_{\phi_2}\). We start with the graph _G<sup>B</sup>_; we then get \(G_s^B\) by adding a dummy source with outgoing edges of weight 0 to every \(v\in V\) ; finally we get \((G_s^B)_{\phi_2}\) by applying price function \(\phi_2\) to \(G_s^B\), where we define \(\phi_2(s)=0\). The reason we apply \(\phi_2\) at the end is to ensure that \(G_s^B\) and \((G_s^B)_{\phi_2}\) are equivalent. Note that after we apply \(\phi_2\), the edges incident to _s_ can have non-zero weight (positive or negative); but _s_ can still reach every vertex, so we can still call ElimNeg with _s_ as the source.

Recall (Lemma 3.3 and definition 2.4) that the runtime of \(\mathrm{ElimNeg}((G_s^B)_{\phi_2},s)\) is<tbc>

\(O\left(\left(m+\sum_{v\in V}\eta_{(G_s^B)_{\phi_2}}(v;s)\right)\mathrm{log}m\right)\)

<tbc>Fix any \(v\in V\) , observe that

\(\eta_{(G_s^B)_{\phi_2}}(v;s)=\mathrm{min}\{|P\cap E^{neg}((G_s^B)_{\phi_2})|:P\text{is a shortest}sv\text{-path in}(G_s^B)_{\phi_2}\}(\text{Definition 2.4})\)<br>
\(\le|P_{G^B}(v)\cap E^{neg}((G_s^B)_{\phi_2})|\)

<sup>13</sup>The "\(\le^{(a)}\)" part in (3) is not equality because there can be an edge in \(E^{neg}(H)\cap P\) that is not in \(E^{neg}(H^B)\cap P\). <sup>14</sup>in fact all vertices in _P_ are in the same SCC _V<sub>i</sub>_, because we define \(H=\bigcup_iG[V_i]\). <sup>15</sup>See, e.g., Lemma 22.13 in \[CLRS09\].

