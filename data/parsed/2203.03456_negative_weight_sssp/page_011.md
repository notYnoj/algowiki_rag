bound the runtime when _G_ contains no negative-weight cycle (Item 3). _In the rest of this subsection we assume that G contains no negative-weight cycle._

Bounding the runtime when \(\Delta\le 2\) is easy: The algorithm simply jumps to Phase 3 with \(\phi_2=0\) (Line 1 in Algorithm 1). Since \(\eta(G^B)\le\Delta\le 2\) (the input requirement; Item 1b), the runtime of \(\mathrm{ElimNeg}((G_s^B)_{\phi_2},s)\) is \(O((m+\sum_{v\in V}\eta_{G^B}(v))\mathrm{log}m)=O(m\Delta\mathrm{log}m)=O(m\mathrm{log}m)\).

For \(\Delta>2\), we require some properties from Phases 0-2 in order to bound the runtime of Phase 3. In Phase 0, we partition vertices into strongly-connected components (SCCs)<sup>11</sup> _V_<sub>1</sub>_,V_<sub>2</sub>_,..._ such that each _V<sub>i</sub>_ has weak diameter \(dB=B\Delta/2\) in _G_. We do this by calling \(E^{rem}\leftarrow\mathrm{LowDiamDecomposition}(G_{\ge 0}^B,dB)\), where \(G_{\ge 0}^B\) is obtained by rounding all negative weights in _G<sup>B</sup>_ up to 0; we then let _V_<sub>1</sub>_,V_<sub>2</sub>_,..._ be the SCCs of _G<sup>B</sup>_\\_E<sup>rem</sup>_. (We need \(G_{\ge 0}^B\) since LowDiamDecomposition can not handle negative weights.<sup>12</sup>) See Lemma 4.3 for the formal statement and proof.

The algorithm now proceeds in three phases. In Phase 1 it computes a price function \(\phi_1\) that makes the edges inside each SCC _V<sub>i</sub>_ non-negative; in Phase 2 it computes \(\phi_2\) such that the edges between SCCs in _G<sup>B</sup>_\\_E<sup>rem</sup>_ are also non-negative; finally, in Phase 3 it makes non-negative the edges in _E<sup>rem</sup>_ by calling ElimNeg.

**(Phase 1)** Our goal in Phase 1 is to compute \(\phi_1\) such that \(w_{\phi_1}^B(e)\ge 0\) for every edge _e_ in _G<sup>B</sup>_\[_V<sub>i</sub>_\] for all _i_. To do this, we recursively call Scale\(\mathrm{Down}(H,\Delta/2,B)\), where _H_ is a union of all the SCCs _G_\[_V<sub>i</sub>_\]. The main reason that we can recursively call ScaleDown with parameter \(\Delta/2\) is because we can argue that, when _G_ does not contain a negative-weight cycle,

\(\eta(H^B)\le d=\Delta/2.\)

As a rough sketch, the above bound holds because if any shortest path _P_ from dummy source _s_ in some (_G<sup>B</sup>_\[_V<sub>i</sub>_\])_<sub>s</sub>_ contains more than _d_ negative-weight edges, then it can be shown that _w(P)\<-dB_; this is the step where we crucially rely on the difference between _w<sup>B</sup>(P_) and _w(P_). Combining _w(P)\<-dB_ with the fact that _G<sup>B</sup>_\[_V<sub>i</sub>_\] has weak diameter at most _dB_ implies that _G_ contains a negative-weight cycle. See Lemma 4.5 for the detailed proof.

**(Phase 2)** Now that all edges in \(G_{\phi_1}^B[V_i]\) are non-negative, we turn to the remaining edges in _G<sup>B</sup>_\\_E<sup>rem</sup>_. Since these remaining edges (i.e. those not in the SCCs) form a directed acyclic graph (DAG), we can simply call FixDAGEdges(\(G_{\phi_1}^B\backslash E^{rem},\{V_1,V_2,\dots\}\)) (Lemma 3.2) to get a price function \(\psi\) such that all edges in \((G_{\phi_1}^B\backslash E^{rem})_\psi=G_{\phi_2}^B\backslash E^{rem}\) are non-negative. (See Lemma 4.7.)

**(Phase 3)** By the time we reach this phase, the only negative edges remaining in \(G_{\phi_2}^B\) are the ones in _E<sup>rem</sup>_; that is, \(E^{neg}(G_{\phi_2}^B)\subseteq E^{rem}\). We call \(\mathrm{ElimNeg}((G_s^B)_{\phi_2},s)\) to eliminate these negative edges. We are now ready to show that the runtime of Phase 3, which is \(O((m+\sum_{v\in V}\eta_{(G_s^B)_{\phi_2}}(v;s))\mathrm{log}m)\) (Lemma 3.3), is _O(m_log<sup>3</sup>_m_) in expectation. We do so by proving that for any \(v\in V\) ,

\(E\left[\eta_{(G_s^B)_{\phi_2}}(v;s)\right]=O(\mathrm{log}^2m).\)

(See Equation (5) near the end of the next subsection.) A competitive reader might want to try to prove the above via a series of inequalities: \(\eta_{(G_s^B)_{\phi_2}}(v)\le|P_{G^B}(v)\cap E^{neg}(G_{\phi_2}^B)|+1\le|P_{G^B}(v)\cap E^{rem}|+1\), and also, the guarantees of LowDiamDecomposition (Lemma 1.2) imply that after Phase 0, \(E\left[|P_{G^B}(v)\cap E^{rem}|\right]=O(\mathrm{log}^2m)\). (Proved in Lemma 4.4.)

Finally, observe that there are \(O(\mathrm{log}\Delta)\) recursive calls, and the runtime of each call is dominated by the _O(m_log<sup>3</sup>_m_) time of Phase 3. So, the total expected runtime is \(O(m\mathrm{log}^3(m)\mathrm{log}\Delta)\)<tbc>

<sup>11</sup>Recall that a SCC is a _maximal_ set \(C\subseteq V\) such that for every \(u,v\in V\) , there are paths from _u_ to _v_ and from _v_ to _u_. See, e.g., Chapter 22.5 in \[CLRS09\]. <sup>12</sup>One can also use \(G_{\ge 0}\) instead of \(G_{\ge 0}^B\). We choose \(G_{\ge 0}^B\) since some proofs become slightly simpler.

