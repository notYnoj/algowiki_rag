**Remark.** Our sequence of phases 0-3 is reminiscent of the sequencing used by Bernstein, Probst- Gutenberg, and Saranurak in their result on dynamic reachability \[BGS20\], although the actual work within each phase is entirely different, and the decompositions have different guarantees. The authors of \[BGS20\] decompose the graph into a DAG of _expanders_ plus some separator edges (analogous to our phase 0); they then handle reachability inside expanders (phase 1), followed by reachability using the DAG edges (phase 2), and finally incorporate the separator edges (phase 3).

## 4.2 Full Analysis

Theorem 3.5 follows from Theorems 4.1 and 4.2 below. We start with Theorem 4.1 which is quite trivial to prove.

**Theorem 4.1.** Scale\(\mathrm{Down}(G=(V,E,w),\Delta,B)\) _either does not terminate or returns_ \(\phi=\phi_3\) _such that_ \(w_\phi(e)\ge-B\) _for all_ \(e\in E\).

_Proof._ Consider when we call \(\mathrm{ElimNeg}((G_s^B)_{\phi_2},s)\)(Lemma 3.3) in Phase 3 for some integral price function \(\phi_2\). Either this step does not terminate or returns an integral price function \(\psi'\) such that \((G_{\phi_2}^B)_{\psi^\prime}=G_{\phi_2+\psi^\prime}^B=G_{\phi_3}^B\) contains no negative-weight edges; i.e. \(w_{\phi_3}^B(e)\ge 0\) for all \(e\in E\). Since \(w^B(e)\le w(e)+B\), we have \(w_{\phi_3}(e)\ge w_{\phi_3}^B(e)-B\ge-B\) for all \(e\in E\).

Theorem 4.1 implies that the output condition of ScaleDown (item 2 in Theorem 3.5) is always satisfied, regardless of whether _G_ contains a negative-weight cycle or not. It remains to show that if _G_ does not contain a negative-weight cycle, then Scale\(\mathrm{Down}(G=(V,E,w),\Delta,B)\) has expected runtime of \(O(m\mathrm{log}^3(m)\mathrm{log}(\Delta))\). It suffices to show the following.

**Theorem 4.2.** _If G does not contain a negative-weight cycle, then the expected time complexity of Phase 3 is O(m_log<sup>3</sup>_m)._

This suffices because, first of all, it is easy to see that Phase 0 requires _O(m_log<sup>3</sup>(_m_)) time (by Lemma 1.2) and other phases (except the recursion on Line 7) requires _O(m+n_) time. Moreover, observe that if _G_ contains no negative-weight cycle, then the same holds for _H_ in the recursion call Scale\(\mathrm{Down}(H,\Delta/2,B)\) (Line 7 of Algorithm 1); thus, if _G_ contains no negative-weight cycle, then all recursive calls also get an input with no negative-weight cycle. So, by Theorem 4.2 the time to execute a single call in the recursion tree is _O(m_log<sup>3</sup>_m_) in expectation. Since there are \(O(\mathrm{log}\Delta)\) recursive calls, the total running time is \(O(m\mathrm{log}^3(m)\mathrm{log}(\Delta))\) by linearity of expectation.

**Proof of Theorem 4.2.** The rest of this subsection is devoted to proving Theorem 4.2. From now on, we consider any graph _G_ that does not contain a negative-weight cycle. (We often continue to state this assumption in lemma statements so that they are self-contained.)

**Base case:** \(\Delta\le 2\). This means that for every vertex _v_, \(\eta_{G^B}(v)\le\eta(G^B)\le\Delta\le 2\) (see the input requirement of ScaleDown in Item 1b of Theorem 3.5). So, the runtime of Phase 3 is

\(O\left(\left(m+\sum_{v\in V}\eta_{G^B}(v)\right)\mathrm{log}m\right)=O\left(m\Delta\mathrm{log}m\right)=O\left(m\mathrm{log}m\right).\)

We now consider when \(\Delta>2\) and show properties achieved in each phase. We will use these properties from earlier phases in analyzing the runtime of Phase 3.

**Phase 0: Low-diameter Decomposition.** It is straightforward that the SCCs _G_\[_V<sub>i</sub>_\] have weak diameter at most _dB_ (this property will be used in Phase 1):

