## C Missing Proofs

**Lemma C.1.** _Let G be an unweighted, undirected graph on n vertices. Let_ \(\hat{\delta}\) _be the estimate output by Algorithm 2. Then,_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all_ \(u,v\in V\) .

_Proof._ Consider some _t_=2_<sup>j</sup>_. Then,

\(\hat{\delta}(u,v)=min_{w\in W}\hat{\delta}(u,w)+\hat{\delta}(w,v)\delta(u,v)\)

so that Algorithm 2 outputs \(\delta(u,v)\le\hat{\delta}(u,v)\) for all _u,v_.

**Lemma C.2.** _Let G be an unweighted, undirected graph on n vertices. Let_ \(\hat{\delta}\) _be the estimate output by Algorithm 3. Then,_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all_ \(u,v\in V\) .

_Proof._ We will show for all vertex pairs (_u,v_) that \(\delta(u,v)\le\hat{\delta}(u,v)\). To do so, it suffices to observe that every estimated distance is witnessed by some path in the graph _G_.

Initially, the only finite entries of \(\hat{\delta}\) are edges (_u,v_) in the graph _G_. Phase 1 calls **DominatingSetAPASP**(_G<sub>t</sub>,V,V,C<sub>t</sub>,C_+1) so that \(\hat{\delta}(u,v)\ge\delta(G_t,u,v)\ge\delta(u,v)\) for all _u,v_ since \(G_t\subset G\) is a sub-graph and Lemma C.1.

Similarly, Phase 2.1 calls **DominatingSetAPASP**(_G_<sub>_s_<sub>1</sub></sub>_,V,D_<sub>_k_-1</sub>_,D_<sub>1</sub>_,C_+2) so that after Phase 2.1, \(\hat{\delta}(u,v)\ge\delta(G_{s_1},u,v)\ge\delta(u,v)\) as \(G_{s_1}\subset G\).

In Phase 2.2, any path found by **BFS** in subgraphs \(G_x,G_2\subset G\) is naturally also a path in _G_.

In Phase 2.3, since for any \(u\in q(w,D_i)\), \((u,w)\in E\), by the triangle inequality,

\(1+\hat{\delta}(u,v)\ge 1+\delta(u,v)\ge\delta(w,v)\)

Thus, any distance in _G<sub>i,w</sub>_ is witnessed by some path in _G_. Therefore, executing **Dijkstra** on _G<sub>i,w</sub>_ with weight function \(\hat{\delta}\) will not return any distance \(\hat{\delta}\) smaller than the shortest distance between _u,v_.

Finally, we conclude by noting the correctness of **BoundedAdaptiveAPASP** and **DenseAPASP** implies \(\delta(u,v)\le\hat{\delta}(u,v)\).

**Proposition C.3.** _For any_ \(x\in[0,1]\) _and any integer_ \(k\ge 1\),

\(\omega\left(1,1-\frac{(k-1)}{k}x,1-\frac{x}{k}\right)\le\omega(1,1-x,1)\)

_Proof._ Recall that by symmetry of \(\omega\), \(\omega(1,1-x,1)=\omega(1,1,1-x)\). The claim follows from applying Lemma B.4 with \(t=\frac{1}{k}\).

**Proposition C.4.** _We obtain the running times in  1 for_ (2,0) _approximation on paths of length_ \(\delta(u,v)\ge k\) _from Theorem 4.2._

_Proof._ Recall from Theorem 4.2 we wish to minimize the following,

\(max\left(\omega\left(1-\frac{k-2}{2(l-k+2)}x,1-x,1-\frac{k-4}{2(l-k+2)}x\right),2+\frac{x}{l-k+2},1.5+x\right)\)

In all cases, we can set _M_ to be some arbitrary constant without affecting the asymptotic running time.

