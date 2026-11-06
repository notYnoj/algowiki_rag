### Input.

The input consists of an instance (_P,D_) of MinGMConn and a parameter _s_ specifying the number of sub-problems (strips) in which the algorithm should divide the instance. As in the previous section, we allow that distinct points in _P_ have the same _x_-coordinate but require distinct _y_- coordinates. Again, we may assume monotone demands.

### Subdivision into Strips.

Let (_P,D_) be an instance of MinGMConn. Let \(s\ge 2\) be a positive integer and let _B_ be a set of _s_-1 distinct vertical lines in the plane. The lines in _B_ partition the plane into a set S of _s_ many vertical strips. We call the lines in _B strip boundaries_ of S, where each strip has one or two strip boundaries (left and right). We call S a _strip subdivision of_ (_P,D_) if each boundary of S is disjoint from _P_.

Let _g_ be the number of _x_-groups in _P_. In line 2, we compute a strip division S such that each strip contains at most \(\lceil g/s\rceil\) many _x_-groups. We call such a strip subdivision _balanced_.

### Intra-Strip Instances.

We first satisfy intra-strip demand pairs (Algorithm 3, Line 4). To this end, we invoke the algorithm recursively for each strip _S_ and solve the sub-instance of (_P,D_), which satisfies all demands in _D_ lying completely in _S_ (intra-strip instance). The result is added to our solution _Q_.

### Inter-Strip Instances.

Consider an instance (_P,D_) of MinGMConn and a strip subdivision S with strips _S_<sub>1</sub>_,...,S<sub>s</sub>_ ordered left-to-right. For each input point \(p\in P\), there is a unique strip \(S\in\mathcal{S}\) containing _p_. If \(S\neq S_1\), then we denote by \(\pi_\mathcal{S}^1(p)\) the horizontal projection of _p_ to the left boundary of _S_. Analogously, if \(S\neq S_s\), then we denote by \(\pi_\mathcal{S}^\mathrm{r}(p)\) the horizontal projection of _p_ to the right boundary of _S_. For any subset \(P'\subseteq P\), we define \(\pi_\mathcal{S}^1(P')=\{\pi_\mathcal{S}^1(p)|p\in P'\backslash S_1\}\), \(\pi_\mathcal{S}^\mathrm{r}(P')=\{\pi_\mathcal{S}^\mathrm{r}(p)|p\in P'\backslash S_s\}\), and \(\pi_\mathcal{S}(P')=\pi_\mathcal{S}^1(P')\cup\pi_\mathcal{S}^\mathrm{r}(P')\) as the set of horizontal projections of the points in \(P'\) to left, right, and both strip boundaries of their respective strips in S, respectively.

Define a new instance on the projection \(\pi_\mathcal{S}(P)\) of _P_ to the adjacent strip boundaries by

\(\pi_\mathcal{S}(D)=\{(\pi_\mathcal{S}^\mathrm{r}(p),\pi_\mathcal{S}^1(q))|(p,q)\in D\text{and}p,q\text{lie in different and non-adjacent strips}\},\)

the "projected" demands. (Recall that we assumed that _x(p)\<x(q)._) We drop demands within the same strip as they are handled in the respective intra-strip instance and demands from adjacent strips because are projected to the same boundary and thus automatically satisfied. Call \(\pi_\mathcal{S}(P,D):=(\pi_\mathcal{S}(P),\pi_\mathcal{S}(D))\) the _inter-strip instance_ corresponding to (_P,D_). Note that the input points of this resulting instance share _s_-1 many distinct _x_-coordinates.

Intuitively, the following lemma states that a feasible solution to the inter-strip distance along with the projected points satisfies all the demand-pairs for which not both points are in the same strip. This fact is used in algorithm and analysis.

**Lemma 19.** _Let_ (_P,D_) _be an instance with strip subdivision_ S_. If Q is a feasible solution to the inter-strip instance_ \(\pi_\mathcal{S}(P,D)\)_, then_ \(Q\cup\pi_\mathcal{S}(P)\) _satisfies all demands_ \((p,q)\in D\) _for which p and q lie in different strips._

_Proof._ To see the feasibility of \(Q\cup\pi_\mathcal{S}(P)\) consider a demand \((p,q)\in D\) where _p_ and _q_ lie in different strips. Observe that we can connect _p_ to \(\pi_\mathcal{S}^\mathrm{r}(p)\) directly, then \(\pi_\mathcal{S}^\mathrm{r}(p)\) to \(\pi_\mathcal{S}^1(q)\) via _Q_, and finally connect \(\pi_\mathcal{S}^1(q)\) to _q_ to obtain a Manhattan path from _p_ to _q_. Recall that \(\pi_\mathcal{S}^\mathrm{r}(p)\) and \(\pi_\mathcal{S}^1(q)\) are automatically connected if _p_ and _q_ lie in adjacent strips.

Algorithm 3 provides an overview of our algorithm.

