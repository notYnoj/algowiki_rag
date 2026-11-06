<tbc>where the inequality is because, for any price function \(\phi_2\), _P<sub>G<sup>B</sup></sub>(v_) is a shortest _sv_-path in \((G_s^B)_{\phi_2}\) (because \((G_s^B)_{\phi_2}\) and \(G_s^B\) are equivalent and _P<sub>G<sup>B</sup></sub>(v_) is a shortest _sv_-path in \(G_s^B\) by definition). By Lemma 4.7, all negative-weight edges in \(G_{\phi_2}^B\) are in _E<sup>rem</sup>_, i.e. \(E^{neg}(G_{\phi_2}^B)\subseteq E^{rem}\); so,<tbc>

\(\eta_{(G_s^B)_{\phi_2}}(v;s)\le|P_{G^B}(v)\cap E^{rem}|+1\)

<tbc>where the "+1" term is because the edge incident to _s_ in _P<sub>G<sup>B</sup></sub>(v_) can also be negative. By Lemma 4.4 and the fact that \(\eta(G^B)\le\Delta\) (input requirement Item 1b in Theorem 3.5),<sup>16</sup><tbc>

\(E\left[\eta_{(G_s^B)_{\phi_2}}(v;s)\right]\le E\left[|P_{G^B}(v)\cap E^{rem}|\right]+1=O(log^2m).\) (5)

<tbc>(The last equality is by Lemma 4.4.) Thus, the expected runtime of \(\mathrm{ElimNeg}((G_s^B)_{\phi_2},s)\) is

\(O\left(\left(m+E\left[\sum_{v\in V}\eta_{(G_s^B)_{\phi_2}}(v;s)\right]\right)logm\right)=O\left(mlog^3m\right).\)

## 5 Algorithm SPmain (Theorem 3.4)

In this section we present algorithm SPmain(_G<sub>in</sub>,s<sub>in</sub>_) (Theorem 3.4), which always runs on the main input graph _G<sub>in</sub>_ and source _s<sub>in</sub>_.

**Description of Algorithm** SPmain(_G<sub>in</sub>,s<sub>in</sub>_)**.** See Algorithm 2 for pseudocode. Recall that if _G<sub>in</sub>_ contains a negative-weight cycle, then the algorithm is not supposed to terminate; for intuition, we recommend the reader focus on the case where _G<sub>in</sub>_ contains no negative-weight cycle.

The algorithm first creates an equivalent graph \(\bar{G}\) by scaling up edge weights by 2_n_ (Line 1), and also rounds _B_ (Line 2), all to ensure that everything remains integral. It then repeatedly calls ScaleDown until we have a price function \(\phi_t\) such that \(w_{\phi_t}(e)\ge-1\) (See for loop in Line 4). The algorithm then defines a graph _G_<sup>∗</sup>=(_V,E,w_<sup>∗</sup>) with \(w^*(e)=w_{\phi_t}(e)+1\) (Line 7). In the analysis, we will argue that because we are dealing with the scaled graph \(\bar{G}\), the additive +1 is insignificant and does not affect the shortest path structure (Claim 5.3), so running Dijkstra on _G_<sup>∗</sup> will return correct shortest paths in _G_ (Lines 8 and 9).

**Correctness** We focus on the case where the algorithm terminates, and hence every line is executed. First we argue that weights in _G_<sup>∗</sup> (Line 7) are non-negative.

**Claim 5.1.** _If the algorithm terminates, then for all_ \(e\in E\) _and_ \(i\in[0,t:=log_2(B)]\) _we have that_ \(\bar{w}_i\) _is integral and that_ \(\bar{w}_i(e)\ge-B/2^i\) _for all_ \(e\in E\)_. Note that this implies that_ \(\bar{w}_t(e)\ge-1\) _for all_ \(e\in E\)_, and so the graph G_<sup>∗</sup> _has non-negative weights._

_Proof._ We prove the claim by induction on _i_. For base case _i_=0, the claim holds for \(\bar{G}_{\phi_0}=\bar{G}\) because \(w_{in}(e)\ge-1\) (see Assumption 2.1), so \(\bar{w}(e)\ge-2n\ge-B\) (see Lines 1 and 2).

Now assume by induction that the claim holds for \(\bar{G}_{\phi_{i-1}}\). The call to Scale\(\mathrm{Down}(\bar{G}_{\phi_{i-1}},\Delta:=n,B/2^i)\) in Line 5 satisfies the necessary input properties (See Theorem 3.5): property 1a holds by the induction hypotheses; property 1b holds because we have \(\eta_G(v)\le n\) for any graph _G_ with no negative-weight cycle; property 1c holds because _G<sub>in</sub>_ has constant out-degree, and the algorithm never changes the graph topology. Thus, by the output guarantee of ScaleDown we have that \((\bar{w}_{\phi_{i-1}})_{\psi_i}(e)\ge(B/2^{i-1})/2=B/2^i\). The claim follows because as noted in Definition 2.5, \((\bar{w}_{\phi_{i-1}})_{\psi_i}=\bar{w}_{\phi_{i-1}+\psi_i}=\bar{w}_{\phi_i}\).

<sup>16</sup>The expectation in (5) is over the random outcomes of the low-diameter decomposition in Phase 0 and the recursion in Phase 1. Note that both \(\eta_{(G_s^B)_{\phi_2}}(v;s)\) and \(|P_{G^B}(v)\cap E^{rem}|\) are random variables. Since we always have \(\eta_{(G_s^B)_{\phi_2}}(v;s)\le|P_{G^B}(v)\cap E^{rem}|+1\), we also have \(E\left[\eta_{(G_s^B)_{\phi_2}}(v;s)\right]\le E\left[|P_{G^B}(v)\cap E^{rem}|\right]+1\).

