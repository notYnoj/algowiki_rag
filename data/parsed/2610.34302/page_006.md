The two approximation guarantees use two closely related but different choices of global representatives. For the constant-factor guarantee, we use separated covers: at each scale, the selected centers are pairwise farther than the ball radius. This separation is a coarse, scale-by-scale analogue of the ordered-greedy packing condition above. For each fixed source _s_, this separation allows us to map the selected centers at each scale to outgoing edges of _s_ in a sparsest \((2\alpha+O(1))\)-navigable graph. The map is injective at each scale, and each edge is used by these maps at only constantly many scales.

For the logarithmic guarantee, we instead use the standard greedy Set Cover algorithm over all radius-\(\Theta(r_i/\alpha)\) balls, allowing the chosen center to be a point that has already been covered. This variant does not have the separation property used in the constant-factor analysis. For each source and scale, the clusters whose centers lie in the annulus define a local set-cover instance. We show that the number of selected centers is at most _O_(log_n_) times the optimum of this local instance. We then bound each local optimum by the number of outgoing edges of the source in a sparsest \((\alpha+O(1))\)-navigable graph that navigate to points in the local instance. Each such edge is counted at only constantly many scales.

Finally, to obtain the simultaneous statement of Theorem 1.4, we run both constructions and return the graph with fewer edges. Since both candidate graphs are \(\alpha\)-navigable, the returned graph is \(\alpha\)-navigable; because its size is no larger than either candidate, it inherits both bicriteria bounds.

## 2 Bicriteria Approximation in Near-Quadratic Time.

### 2.1 Algorithm Description.

Let (_P,_d) be a finite metric space on _n_ points and let \(\alpha\ge 1\) be a fixed parameter. By rescaling all distances by a common positive factor, we assume that the minimum nonzero pairwise distance is \(1+1/\alpha\). Consequently, all nonzero pairwise distances lie in the range \(\left[1+\frac{1}{\alpha}\right]\), \(\left(1+\frac{1}{\alpha}\right)\Delta\right]\), where \(\Delta\) is the aspect ratio of the metric. For any \(s\in P\) and radius parameter _r\>_0, define<tbc>

\(B(s,r)=\{u\in P|\mathsf{d}(s,u)\le r\}.\)

<tbc>Let \(\delta=1/\alpha\), let \(L=\left\lceil\mathrm{log}_{1+\delta}\Delta\right\rceil\), and define \(r_i=(1+\delta)^i\) for every \(0\le i\le L+1\). Notice that _r_<sub>0</sub>=1 and \(r_{L+1}\ge(1+\delta)\Delta\). Hence, for every pair of distinct points \(s,t\in P\), there exists an index \(0\le i\le L\) such that \(r_i<\mathsf{d}(s,t)\le r_{i+1}\). We use the following annulus around a source point _s_ at level _i_:

\(A_i(s)=\left\{v\in P:r_i-\frac{r_i}{\alpha+2}<\mathsf{d}(s,v)\le r_{i+1}+\frac{r_i}{\alpha+2}\right\}.\)

We use two different ball-cover routines. The first one is a separated cover and is used for the constant-factor bicriteria approximation. The second one is the usual greedy Set Cover algorithm over metric balls and is used for the logarithmic bicriteria approximation.

#### Separated ball cover.

Given a radius _r\>_0, the following procedure partitions _P_ into clusters _C_ with centers _p_ satisfying \(C\subseteq B(p,r)\). The centers are pairwise separated by distance strictly larger than _r_.

For every pair (_C,p_) returned by Algorithm 2.1, we have \(C\subseteq B(p,r)\). Moreover, if _p_ is chosen before another center \(p'\), then \(p'\) is not covered by _B(p,r_), and hence \(\mathsf{d}(p,p')>r\). Thus all centers are pairwise separated by distance more than _r_.

