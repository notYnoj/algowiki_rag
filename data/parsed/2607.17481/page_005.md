<tbc>anchor draws its own projection vectors, so the anchors that a region intersects provide multiple, nearly independent opportunities for its discovery (Figure 3).

Proposition 3 (Cross-length redundancy). _Call a pair matchable at anchor a if it is valid and would lower at least one profile cell at length a, and let M<sub>A</sub> be the set of anchors at which it is matchable. Let p<sub>a</sub> be the probability that signatures and probes collide at anchor a, and c<sub>a</sub> the probability that the budgeted scan retains the pair after collision. Since the per-anchor projections are drawn independently (§3.4), the probability that no anchor discovers the pair is at most_ \(\prod_{a\in M_A}(1-p_ac_a)\) _(proof in Appendix C)._

The proposition quantifies the redundancy that anchors provide. The probabilities _p<sub>a</sub>_ and _c<sub>a</sub>_ are data dependent, so recall is evaluated empirically (§4), while soundness (Prop. 1) and determinism (Prop. 5) hold unconditionally. Anchoring skips lengths on purpose, and the skipped lengths carry no online state. They<tbc>

<tbc>are still searched. Every motif emitted at an anchor length starts a local completion (§3.6), which evaluates exact distances at the neighboring lengths and positions around the emitted pair, and the contiguity of low regions is exactly what makes these neighborhoods the right place to look. A low region that spans fewer than _s_ consecutive lengths can still escape every anchor. A smaller stride or a wider completion neighborhood moves the method toward dense coverage at higher cost.

## 3.4 Streaming Candidate Generation

For every anchor length, an individual hash directory is maintained, so a window is only ever compared against earlier windows of the same length. Earlier start positions are stored under a SimHash signature of their feature vectors. Bit \(\ell\) of the signature of a start _i_ at anchor _a_ is \(b_a(i)_\ell=\mathbf{1}\{\langle g_{a,\ell},F_{i,a}\rangle\ge 0\}\) for \(\ell=1,\dots,B\), where \(g_{a,\ell}\) are seeded Gaussian projections drawn independently per anchor. The per-anchor draw is what makes the anchors’ discovery attempts nearly independent (Prop. 3).

Fact 1 ([6]). _For a standard Gaussian projection g and vectors u,v at angle_ \(\theta\), \(Pr[sign\langle g,u\rangle\neq sign\langle g,v\rangle]=\theta/\pi\).

Windows whose normalized shapes are close therefore agree on each signature bit with high probability (Figure 2B). A hash table with a fixed number of buckets, however, degrades as the stream grows. Bucket populations increase linearly with _n_ while the per- query budget is constant, so either the budget is exceeded or queries compare only against recent arrivals. Panache controls bucket size with a _global-depth_ prefix directory, a variant of extendible hashing [10] in which every bucket shares one directory-wide depth _d_ rather than carrying a per-bucket local depth. The bucket address<tbc>

