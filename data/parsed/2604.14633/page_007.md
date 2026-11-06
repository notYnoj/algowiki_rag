calls ToggleCut(\(\eta\)) with \(\eta=\frac{1}{16\alpha u}\). Otherwise, if \(g/u>-1/(3\alpha)\), then since the data structure is \(\alpha\)-approximate, the minimum ratio cut is at least -1/3. By Lemma 6, we have \(w(\partial^+S)\ge\frac{1}{2}w(\partial^-S)\) for all \(S\subseteq V\) . The actual weights maintained by the data structure are approximations of _w(u,v_), but we show that they are also balanced up to constant factors.

The algorithm calls Sparsifier(\(\beta\)) with \(\beta=9\), obtaining a subgraph on _n_<sup>1+_o_(1)</sup> arcs. By the previous balance guarantee, there is an augmenting path from _s_ to _t_ in the sampled graph. The algorithm finds such a path in _n_<sup>1+_o_(1)</sup> time and updates both data structures as follows. For each arc _e_=(_v,u_) along the path, the algorithm calls DeleteEdge(_e_)/DeleteArc(_e_) for the corresponding arc/edge (_v,u_), and then InsertEdge(_e_)/InsertArc(_u,v_) with the new weight \(\frac{1}{max\{\mathbf{y}(v)-\mathbf{y}(u),0\}+1}\) of the flipped arc (_u,v_). The algorithm also calls UpdateGradient accordingly.

## 3.1 Stability

Since edge weights only get updated when they are returned in \(E'\), the data structures only maintain approximations of the true weights. In more detail, for each arc (_u,v_), define the real weight \(w(u,v)=\frac{1}{max\{\mathbf{y}(v)-\mathbf{y}(u),0\}+1}\) based on the current potential function **y**, and define the approximate weight \(\tilde{w}(u,v)=\mathbf{u}(u,v)\) as the current weight maintained by the data structure, which is the real weight at the last time the corresponding edge (_u,v_) was inserted or returned in \(E'\).

Our algorithm requires that the approximate weights \(\tilde{w}(u,v)\) indeed approximate the real weights. We begin with a stability guarantee on the weight function that is used throughout the analysis.

**Lemma 11** (Stability)**.** _Consider two values_ \(x_1,x_2\in\mathbb{R}\)_, and define the weights_ \(w_i=\frac{1}{max\{x_i,0\}+1}\) _for_ \(i\in\{1,2\}\)_. For any parameter_ \(0\le\delta<1\)_, if_ \(|x_1-x_2|\le\delta/w_1\)_, then_ \(\frac{1}{1+\delta}w_1\le w_2\le\frac{1}{1-\delta}w_1\).

_Proof._ We bound

\(w_2=\frac{1}{max\{x_2,0\}+1}\ge\frac{1}{max\{x_1+\delta/w_1,0\}+1}\ge\frac{1}{max\{x_1,0\}+1+\delta/w_1}=\frac{1}{1/w_1+\delta/w_1}=\frac{w_1}{1+\delta}\)

and

\(w_2=\frac{1}{max\{x_2,0\}+1}\le\frac{1}{max\{x_1-\delta/w_1,0\}+1}\le\frac{1}{max\{x_1,0\}+1-\delta/w_1}=\frac{1}{1/w_1-\delta/w_1}=\frac{w_1}{1-\delta}\)

as desired.

**Lemma 12** (Approximation of weights)**.** _For any arc_ (_u,v), we have_ \(\frac{1}{1+\epsilon}\tilde{w}(u,v)\le w(u,v)\le\frac{1}{1-\epsilon}\tilde{w}(u,v)\).

_Proof._ Let \(\tilde{\mathbf{y}}\) be the potential function when the edge (_u,v_) was last inserted or returned in \(E'\). In particular, \(\tilde{w}(u,v)=\frac{1}{max\{\tilde{\mathbf{y}}(v)-\tilde{\mathbf{y}}(u),0\}+1}\). By the guarantee of the data structure, we have

\(\tilde{w}(u,v)\cdot|(\tilde{\mathbf{y}}(u)-\tilde{\mathbf{y}}(v))-(\mathbf{y}(u)-\mathbf{y}(v))|<\epsilon\Longleftrightarrow|(\tilde{\mathbf{y}}(u)-\tilde{\mathbf{y}}(v))-(\mathbf{y}(u)-\mathbf{y}(v))|<\epsilon/\tilde{w}(u,v).\)

Applying Lemma 11 with \(x_1=\tilde{\mathbf{y}}(u)-\tilde{\mathbf{y}}(v)\) and _x_<sub>2</sub>=**y**(_u_)-**y**(_v_) and \(\delta=\epsilon\) finishes the proof.

Finally, we show that if the algorithm stops calling ToggleCut(\(\eta\)), at which point \(g/u>-1/(3\alpha)\), then the (approximate) edge weights maintained by the data structure are balanced. In particular, Sparsifier(\(\beta\)) with \(\beta=9\) returns a subgraph containing an augmenting path from _s_ to _t_ with high probability.

