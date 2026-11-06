This formulation immediately yields _O_(log_n_)-approximation algorithms via greedy Set Cover, and it also explains why the problem inherits the classical Set Cover hardness barrier. Previous algorithms [KPW26, CDFC<sup>+</sup>26] for sparse navigable graphs in general metrics are based on this viewpoint. However, if one wants to beat the _O_(log_n_) approximation factor, the Set Cover formulation by itself does not reveal enough additional structure.

## Warm-up: source-wise ordered greedy.

Fix a source _s_ and consider the following simple greedy procedure. Process all targets \(t\in P\backslash\{s\}\) in nondecreasing order of d(_s,t_). Whenever no previously added outgoing edge of _s_ is an \(\alpha\)-navigation from _s_ to the current target _t_, add the edge (_s,t_). This procedure clearly produces an \(\alpha\)-navigable graph, since any uncovered target can always be covered by selecting itself. Let _p_<sub>1</sub>_,p_<sub>2</sub>_,...,p<sub>k</sub>_ be the out-neighbors selected for source _s_, in nondecreasing order of their distance from _s_. When _p<sub>j</sub>_ is selected, none of the previously added edges (_s,p<sub>i</sub>),i\<j_, is an \(\alpha\)-navigation from _s_ to _p<sub>j</sub>_. Therefore,

\(\mathsf{d}(p_i,p_j)\ge\frac{\mathsf{d}(s,p_j)}{\alpha}\text{for every}i<j.\) (1.1)

Now compare this ordered-greedy solution with any \(2\alpha\)-navigable graph _H_. For every selected point _p<sub>j</sub>_, the graph _H_ contains an out-neighbor _u<sub>j</sub>_ of _s_ such that<tbc>

\(\mathsf{d}(u_j,p_j)<\frac{\mathsf{d}(s,p_j)}{2\alpha}.\)

<tbc>Choose one such out-neighbor _u<sub>j</sub>_ for each selected point _p<sub>j</sub>_. We show that the map \(p_j\mapsto u_j\) is injective, which bounds the number of selected points by the out-degree of _s_ in _H_. Indeed, suppose two selected points _p<sub>i</sub>,p<sub>j</sub>_ with _i\<j_ were mapped to the same out-neighbor _u_. Then by triangle inequality,

\(\mathsf{d}(p_i,p_j)\le\mathsf{d}(p_i,u)+\mathsf{d}(u,p_j)<\frac{\mathsf{d}(s,p_i)}{2\alpha}+\frac{\mathsf{d}(s,p_j)}{2\alpha}\le\frac{\mathsf{d}(s,p_j)}{\alpha},\)

where the last inequality uses \(\mathsf{d}(s,p_i)\le\mathsf{d}(s,p_j)\). This contradicts (1.1). Hence, for this fixed source _s_, the ordered-greedy procedure selects no more out-neighbors than the out-degree of _s_ in any \(2\alpha\)-navigable graph.

However, this ordered-greedy procedure is too slow for our purposes. Running it independently for all sources requires repeatedly testing whether each target is already navigated by one of the previously selected out-neighbors. A direct implementation takes _O(n_<sup>3</sup>) time in the worst case.

## Global acceleration via hierarchical covers.

Our starting point is the classical use of nets and hierarchical covers, which has been widely adopted in low-dimensional Euclidean and doubling metrics [KL04, LT25]. Instead of running greedy independently for every source, we precompute globally shared representatives at multiple distance scales. More concretely, let \(r_i=\left(1+\frac{1}{\alpha}\right)^i\) range over the relevant distance scales. At each scale _r<sub>i</sub>_, we use balls of radius \(\Theta(r_i/\alpha)\) and, for each source _s_, add edges to selected centers lying in an appropriate annulus around _s_. The annulus is chosen so that if a target _t_ satisfies d(_s,t_)≈_r<sub>i</sub>_, and _p_ is the center covering _t_ at scale _i_, then _p_ is included as an out-neighbor of _s_ and

\(\mathsf{d}(p,t)<\frac{\mathsf{d}(s,t)}{\alpha}.\)

Hence (_s,p_) is an \(\alpha\)-navigation from _s_ to _t_, and taking all sources and scales gives an \(\alpha\)-navigable graph.

