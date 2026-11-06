<tbc>delimits the predicate class on which the filtered term is a _loss_ bound rather than a one-sided necessity statement.

**Assumption 4** (Local predicate density; the frontier is the post-filtered list)**.** \(\beta\) _is a property of the engine’s result contract, not a free constant:_ the post-filter can only see candidates the search returns, so \(\beta=1\) whenever the engine surfaces its full width-_L_ list to the filter (our disk post-filter path, and the measurement of §V-C, which post-filters a dump of exactly _L_ candidates), and \(\beta<1\) for an engine that truncates to _k_ before filtering. We take \(\beta=1\) throughout and carry \(\beta\) symbolically only so the law transfers to engines with a different contract. Filtered recall is governed by the local density \(\sigma_\mathrm{loc}(p,v)\), not the global \(\sigma(p)\): on the shared graph a width-_L_ greedy search returns a candidate frontier of effective size \(L_\mathrm{eff}=\beta L\) whose expected in-predicate mass is \(\beta L\sigma_\mathrm{loc}\).

**Assumption 5** (Per-merge degradation is filter and tenant-independent)**.** Because the disk graph is a single label-blind Yamana (§II), M_<sub>c</sub>_ and hence _g(c,N_) (Assumption 2) depend only on the label-agnostic vector set, not on the predicate or tenant partition.

**Assumption 6** (Per-query frontier model)**.** For a _single_ query _q_ with local density \(\sigma_\mathrm{loc}(q)\), the in-predicate count of its frontier is \(X_q\sim\mathrm{Binom}(\beta L,\sigma_\mathrm{loc}(q))\). This constrains one query’s neighborhood, not the query population: \(\sigma_\mathrm{loc}(\cdot)\) may vary arbitrarily across queries and tenants, and the tenant-level law is the _average of the per-query law over the query population_ (Lemma 7(iii)). Substituting a tenant’s _mean_ local density into the per-query law is a separate and strictly optimistic step, and spatially-clustered predicates break it (§V-C).

Assumption 5 makes the degradation term _transferable_ across the filter and tenant partition (the same _g(c,N_) applies regardless of predicate or tenant, i.e. modularity), rather than making the overall bound additive; the additivity of the two loss components is the separate union-bound argument of Theorem 8. It is measured: replaying the scheduler’s re-ordered multi-partition merge groupings to the identical terminal point set changes disk-graph recall by \(|\Delta|=0.02\) pp \(\le 0.67\) pp (§V), so merge re-ordering has negligible measured effect on terminal recall.

**Lemma 7** (Post-filter recall is a frontier-mass event)**.** _Fix a converged label-blind graph and a query q with local density_ \(\sigma_\mathrm{loc}(q)\)_, and let X<sub>q</sub> be the in-predicate count of its frontier (Assumption 4). If the frontier is the true metric top-_\(\beta L\)_, then post-filter recall@k is_ exactly min(_X<sub>q</sub>,k)/k: the in- predicate members of a true top-_\(\beta L\) _list are precisely the nearest in-predicate points, so the first_ min(_X<sub>q</sub>,k_) _of them are ground-truth items (proof in the supplementary material). An approximate search can only_ omit _in-predicate ground- truth points that a true top-_\(\beta L\) _list would have contained, so the identity degrades in one direction: writing_ \(\delta_\mathrm{ann}(L)\) _for the expected fraction of a query’s in-predicate ground-truth points that lie in the true top-_\(\beta L\) _but are missed by the graph search,_ \(\mathbb{E}[\mathrm{recall}]\ge\mathbb{E}[\mathrm{min}(X_q,k)]/k-\delta_\mathrm{ann}(L)\)_. This is the_<tbc>

<tbc>_only direction Theorem 8 needs, since it bounds a recall_ loss _from above; the reverse inequality is not claimed. Then:_

(_i)_ (Assumption-free envelope; necessity.) _Without any distributional assumption on X,_<tbc>

\(\mathbb{E}[\mathrm{min}(X,k)]/k\le\mathrm{min}\big(1,\frac{\beta L\sigma_\mathrm{loc}}{k}\big),\) \(\text{(4)}\)

_so_ \(L\ge k/(\beta\sigma_\mathrm{loc})\) _is_ necessary _for recall_ \(\rightarrow 1\)_: recovery scale_ \(L=\Theta(k/\sigma_\mathrm{loc})\).<tbc>

(_ii)_ (Exact form under Assumption 6.) _With_ \(X\sim\mathrm{Binom}(\beta L,\sigma_\mathrm{loc})\)_, expected post-filter recall equals_<tbc>

\(h(\sigma_\mathrm{loc},L,k)=\frac{1}{k}\sum_{i=1}^k\mathrm{Pr}\big[\mathrm{Binom}(\beta L,\sigma_\mathrm{loc})\ge i\big],\) \(\text{(5)}\)

_which_ \(\rightarrow 1\) _when_ \(\beta L\sigma_\mathrm{loc}\gg k\) _and_ \(\rightarrow\beta L\sigma_\mathrm{loc}/k\) _when_ \(\beta L\sigma_\mathrm{loc}\checkmark k\)_. The single-term tail_ \(h_\mathrm{tail}=\mathrm{Pr}[\mathrm{Binom}(\beta L,\sigma_\mathrm{loc})\ge k]\) _is the i=k summand alone, so_ \(h_\mathrm{tail}\le h\le\mathrm{min}(1,\beta L\sigma_\mathrm{loc}/k)\)_: a tail-probability model is a valid but order-of-magnitude-loose lower bound on recall (§V-C)._<tbc>

(_iii)_ (Tenant law = query average; substituting the mean is optimistic.) _A tenant’s expected filtered recall is the_ average of the per-query law over its query population,<tbc>

\(\bar{h}_\tau(L,k)=\mathbb{E}_{q|\tau}\big[h(\sigma_\mathrm{loc}(q),L,k)\big],\) \(\text{(6)}\)

_and_ \(p\mapsto\mathbb{E}[\mathrm{min}(\mathrm{Binom}(n,p),k)]\) _is concave in p, so by Jensen_<tbc>

\(\bar{h}_\tau(L,k)\le h\big(\mathbb{E}_{q|\tau}[\sigma_\mathrm{loc}(q)],L,k\big):\) \(\text{(7)}\)

_plugging a tenant’s_ mean _local density into the per-query law over-predicts its recall, with a gap that grows with the dispersion of_ \(\sigma_\mathrm{loc}\) _across queries and vanishes where h is linear (small x) or saturated (large x). Diffuse predicates have near-zero dispersion and are unaffected; spatially-clustered predicates are not, and §V-C exhibits the predicted curvature signature._<tbc>

_(iv)_ (Ordering.) _Collecting (i)-(iii),_ \(h_\mathrm{tail}\le\bar{h}_\tau\le h(\bar{\sigma}_\mathrm{loc}^{(\tau)},L,k)\le\mathrm{min}(1,\beta L\bar{\sigma}_\mathrm{loc}^{(\tau)}/k)\)_, so only the leftmost quantity is a lower bound on recall without further assumptions, and only the rightmost is an upper bound on recall without any._

_Status (§V-C):_ with \(\beta=1\) fixed by the engine contract (Assumption 4) and _no fitted constant of any kind_, part (ii) matches all 35 diffuse cells to a mean absolute residual of 0.2 pp (max 1.2 pp, two-sided), and predicts the separately-measured recovery constant \(L_{95}\approx 1.25k/\sigma_\mathrm{loc}\) because _h_ crosses 0.95 at \(L\sigma_\mathrm{loc}\approx 1.25k\). On the clustered controls the residual is _uniformly one-signed_ (all 15 cells over-predict, up to +26 pp) and peaks in the knee _x_≈1-1.5, decaying to ≈1 pp at both ends. Two distinct clustering effects are at work. One is _density variation across queries_, where the dispersion of \(\sigma_\mathrm{loc}(q)\) within a tenant makes the mean-substituted \(h(\bar{\sigma}_\mathrm{loc},L,k)\) optimistic by Jensen (Lemma 7(iii)); this is the curvature signature the +26 pp deficit exhibits, not a failure of the frontier- mass form. The other is _within-frontier correlation_, where spatially-clustered in-predicate points are not the independent<tbc>

