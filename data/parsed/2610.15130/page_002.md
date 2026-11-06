<tbc>displace them.

We make one theoretical and two engineering contributions. Our theorem (C1, §III) establishes the anti-amortization bound and generalizes it to the filtered, multi-tenant, deletes/migration setting. Its filtered term is a _parameter- free_ frontier-mass law in the _local_ predicate density \(\sigma_\mathrm{loc}\) that predicts the recovery scale \(L_{95}=1.25k/\sigma_\mathrm{loc}\) and yields a per-tenant admission test \(1.25k/\sigma_\mathrm{loc}\le L_\mathrm{max}(\ell_\tau)\); evaluated as a query average, it is a conservative per-tenant recall lower bound. The staleness half is measured at horizon scale rather than extrapolated, with terminal recall decreasing monotonically as the merge size grows across a \(20\times\) range of _c_.

Two engineering designs instantiate the bound. A filter and tenant-aware staging cache (C2, §IV) absorbs in-flight inserts, deletes, and tenancy changes on the query path and collapses to the baseline on a single partition. An SLA- aware, select-not-resize scheduler (C3) honors a per-tenant max-staleness ceiling, re-prioritizing which pending work each fixed-size merge drains rather than re-sizing the merge that anti-amortization forbids.

On a FreshDiskANN substrate we measure that anti- amortization holds end to end (at a fixed 60K-insert horizon, terminal recall@10 falls \(99.44\rightarrow 99.01\) as merges grow \(1\text{K}\rightarrow 20\text{K}\)), that re-ordering merges leaves terminal recall unchanged (\(|\Delta\text{recall@10}|=0.02\) pp), that the per-tenant staleness ceiling eliminates tight-tier SLA violations under churn where a ceiling-less baseline fails, and that the design remains memory-bounded and recall-correct at 100K.

## II. SYSTEM MODEL AND NOTATION

### _Vectors, queries, predicates_

Let \(\mathcal{X}\subseteq\mathbb{R}^d\) be the ambient space with metric \(\rho\). A point \(x\in\mathcal{X}\) carries metadata \(m(x)\in\mathcal{M}\); a _predicate_ \(p:\mathcal{M}\rightarrow\{0,1\}\) selects the filtered subset X_<sub>p</sub>_={_x:p(m(x_))=1}, of _global selectivity_ \(\sigma(p)=|\mathcal{X}_p|/|\mathcal{X}|\). A _query_ is _q_=(_v,k,p_) with query vector _v_, neighbor count _k_, and predicate _p_; its ground truth is the _k_ closest points of X_<sub>p</sub>_ to _v_ under \(\rho\). Because filtered-graph recall is governed by predicate density _near the query_ rather than globally (§III), we also define the query- joint _local density_ \(\sigma_\mathrm{loc}(p,v)=\mathrm{Pr}_{x\sim\mathrm{nbhd}(v)}[p(m(x))=1]\), the fraction of _v_’s metric neighborhood that satisfies _p_.

### _Tenants and SLOs_

The point set is marked by tenant: T is the tenant set and \(t(x)\in\mathcal{T}\) each point’s tenant. A query has tenant scope \(T(q)\subseteq\mathcal{T}\) (single-tenant when |_T(q_)|=1); its effective candidate set is \(\mathcal{X}_p\cap\{x:t(x)\in T(q)\}\). Each tenant \(\tau\) carries a service-level objective \(\text{SLO}(\tau)=(\rho_\tau,\ell_\tau)\) (minimum recall \(\rho_\tau\), maximum latency \(\ell_\tau\)) and a _max-staleness ceiling_ \(S_\tau\) that the scheduler (§IV) honors.

### _Graph index_

_G_=(_V,E_) is a directed graph over \(V\subseteq\mathcal{X}\) built by Yamana (out-degree cap _R_, candidate width _L_, prune slack \(\alpha>1\), pool cap `maxc`); Search(_G,q,ef_) returns an approximate top-_k_ using exploration budget _ef_. **The disk graph is a**<tbc>

<tbc>**single _label-blind_ Yamana:** predicates and tenant labels are query-time post-filter tags and are never used in construction. This fact is central to both the theorem’s additivity and topology preservation (§III,§IV).

### _Mutation streams_

Updates arrive as a marked point process _M_={(_s<sub>i</sub>,u<sub>i</sub>_)} with \(u_i\in\{\mathrm{ins}(x),\mathrm{del}(x),\mathrm{mig}(x,\tau\rightarrow\tau')\}\) and per-class rates \(\lambda_\mathrm{ins},\lambda_\mathrm{del},\lambda_\mathrm{mig}\). The toy setting (§III) is Poisson inserts-only (\(\lambda_\mathrm{del}=\lambda_\mathrm{mig}=0\)); the general theorem admits all three (migration = a delete in \(\tau\) plus an insert in \(\tau'\)).

### _Cache, scheduler, compaction_

A filter-aware, tenant-aware _staging cache C_ of capacity _c_ holds pending mutations and is consulted on the query path, keyed by (_p,T(q_)). A priority-queue _scheduler_ orders background graph-repair work by a composite key \(\kappa=\alpha_1\mathrm{stale}+\alpha_2\widehat{\Delta R}+\alpha_3\mathrm{SLA}+\alpha_4\mathrm{mig}\). Compaction fires a merge when cache occupancy reaches _c_ (the theorem’s referent for _c_); the merge integrates the pending batch into _G_ and resets the cache.

### _Recall as a random variable_

For query _q_ at time _t_, \(R_q(t)=|(\text{Search}(G_t,q,ef)\cup\text{Cache}_t(q))\cap\mathrm{GT}(q,t)|/k\). The _per-tenant recall_ is \(\bar{R}_\tau(t)=\mathbb{E}_q[R_q(t)|T(q)\unknown\tau]\), and the _recall@k loss_ is \(L_\tau(t)=\rho_\tau-\bar{R}_\tau(t)\). The object the theorem bounds is the worst-case _over time_ of the query-averaged per-tenant loss on the horizon \[0_,T_\], \(L_\tau^*=\mathrm{sup}_{t\in[0,T]}L_\tau(t)\): worst-case in _t_, in expectation over _q_, so the guarantee is on the query average rather than on any individual query.

## III. THE RECALL-BOUNDED STALENESS THEOREM (C1)

We first prove the central kernel in the toy setting (single tenant, no filter, inserts only), then lift it to the filtered, multi- tenant, deletes/migration setting. The staleness half of the bound is _semi-empirical / loose-but-correct-form_: its mechanism and functional shape are derived and validated on two independent axes, while the exponents are calibrated. The filtered half is derived and parameter-free. We state this status precisely throughout.

### A. The toy bound: anti-amortization

**Definition 1** (Batch-merge operator M_<sub>c</sub>_)**.** Let _G_<sub>0</sub> be the disk graph over _N_ points and _B_ a batch of _c_ pending inserts. M_<sub>c</sub>(G_<sub>0</sub>_,B_) acts in two phases. _Forward_: each \(x\in B\) obtains out-neighbors by greedy search against the _frozen_ snapshot _G_<sub>0</sub> then ROBUSTPRUNE/\(\alpha\)-RNG to degree _R_; _G_<sub>0</sub> is not mutated during the batch. _Reconcile_: each existing node unions its buffered reverse edges and re-prunes (on PQ distances) only if it exceeds _R_. Two structural consequences follow: (M1) the _c_ batch points are _mutually invisible_ during selection (no \(x\in B\) takes another batch point as a neighbor, unlike a from-scratch build); (M2) hubs flooded by batch reverse edges are re-pruned tossily on approximate distances.

