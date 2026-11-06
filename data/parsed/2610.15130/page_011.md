<tbc>never takes the tenant offline). The shard’s violation figures are _modelled, not measured head-to-head_: no query stream was run against a shard during rebuild. What is measured is the rebuild wall-clock; the violation rate is the duty cycle min(1_,r_<sub>churn</sub>.build(_n_)), an _upper_ bound (it assumes uniform arrival and a query path that cannot dodge a rebuild, a churn- aware path would give 0; we lead with the upper bound because production paths do not know rebuild timing). At the measured 10K scale the shard’s count is small (∼3/2000, 0.15-0.5%), so the direction is established but the margin is thin and mid-scale sharding remains viable. And the magnitude at larger per-tenant sizes is governed by the assumed churn rate. At the anchor’s calibrated _r_<sub>churn</sub>≈10<sup>-2</sup>/s/tenant the model reproduces the measured near-null, but sweeping _r_<sub>churn</sub> from \(1.7\times 10^{-3}\) to \(1.7\times 10^{-2}\) moves the projected 100K/tenant violation rate from 4.8% to 48%, an order-of- magnitude spread set by the assumed rate, not the build cost (measured to 100K/tenant, and _flattening_ above ≈60K as the parallel build saturates, so linear extrapolation would overstate the outage). The per-op wall-clock the shard wins at small _n_ is _unamortized_, since C3 folds ≈6 tenant-ops into one merge (narrowing the gap \(\approx 6\times\)), and the shard’s cost is a serving _outage_ while ours is background.

### F. Baselines and Curator: the tradeoff on static data

On static low-per-tenant data (_T_=6\(\rightarrow\)96, fixed total _N_), per-tenant sharding is _not_ navigability-limited (shards recall ≈100) but is _memory_-limited, its summed footprint growing linearly in tenant count and OOMing a 3 GB box at _T_=96 (FreshDiskANN-shard \(393\rightarrow\)6144 MB, PipeANN- shard \(757\rightarrow\)11776 MB), whereas our shared graph is flat. Under matched search cost our post-filter recall degrades with tenant count (the \(\sigma_\mathrm{loc}\) effect, §V-C). Our Curator comparison uses the authors’ published artifact at a pinned commit, so it measures genuine per-tenant navigability rather than a post- filter over a label-blind graph. It recalls ≈100 flat at ∼100 MB in-memory and thus beats us on _static_ recall; our contribution is instead on streaming, per-tenant SLA scheduling, the bound and disk-resident scale, axes the evaluated static, in-memory Curator artifact does not target. The outcome on static data is a _tradeoff_, not a clean win for either side; the payoff axis is churn (§V-E) and scale (§V-G).

### G. Scale: bounded and correct at mid-scale; the inversion beyond

At 100K our prototype runs _bounded_ (steady RSS ≈1.06 GB single-tenant, ≈1.67 GB six-tenant) and _correct_ (recall@10 99.70, on-curve), with the SLA win intact, closing<tbc>

<tbc>the one at-scale assumption the projection could not vouch for ( IV). Because in-memory footprints are \(\propto N\) while a disk-resident index keeps the graph and full-precision vectors on disk, the memory picture should _invert_ at scale, since an in-memory Curator at its measured 5.6 KB/vector exceeds 16 GB by ≈2.9M points and needs ≈56 GB at 10M, whereas only the PQ-compressed vectors and tags (32-128 B/vector) grow with _N_ on our side, putting us at ≈1-2 GB even at 10M.

_The scaling claim rests on a decomposition, not on the two headline RSS points, which conflate several quantities._ An RSS breakdown at fixed tenant and thread count (_T_=6, 32 threads) on the matched 18K/100K pair separates three marginals. The _serving_ graph-residency marginal is **0.115 kB/point** (PQ codes and tags resident in RAM, the graph on disk), matching the PQ-code size architecturally (≈102 B/point at 100K); serving memory is therefore _N_-independent up to that marginal and the bounded-memory claim holds _for serving_. The _merge-peak transient_ is **8.3 kB/point**, incurred while the StreamingMerger rewrites the _O(N_) graph in RAM under 32 build threads and released afterwards (proportional to _N_, reducible by thread and batch configuration). Between the two sits the _whole- process first stable RSS_, which grows at ≈2.6 kB/point on the matched pair, above the serving marginal because it includes configured allocations (per-thread search buffers, staging sized as #partitions \(\times 2\)Merge\_Size) that the supplementary RSS decomposition (Fig. S3) does not fully attribute to _N_; isolating that residual is left open. This decomposition supersedes an earlier reading that took the raw two-point 18K\(\rightarrow\)100K RSS slope (≈10 kB/point) at face value and extrapolated it to ≈11 GB at 1M. That slope is the mixed whole-process quantity, not a serving cost, which is why the 1M-10M rows in  IV are quoted as residency-model _projections_ on the 0.115 kB/point serving term rather than as extrapolations of the raw curve. The 0.115 kB/point marginal is a two-point measurement whose agreement with the PQ-code size makes it credible.

### H. External comparisons

Preliminary cross-system comparisons (single-tenant streaming vs. PipeANN, filtered recall vs. Filtered-DiskANN, and tail latency) are reported in the supplementary material. They are preliminary (the PipeANN gap is on unmatched parameters, a param-matched head-to-head ongoing) and are not central to our claims.

## VI. RELATED WORK

#### a) Filtered-static graph ANN.:

Filtered-DiskANN \[5\] and ACORN \[6\] encode predicates into graph construction;

\begin{tabular}{cccc}
system & tight viol & medium viol & note \\
ours (C3 ceiling) & **0/2000** & 0/3000 & force-drain, no rebuild \\
scheduler-less baseline & 2000/2000 & 0/3000 & no ceiling (medium not exercised) \\
per-tenant shard (UB) & ∼3/2000 & ∼8/3000 & rebuild-outage duty cycle @10K \\
\end{tabular}

TABLE III

TIGHT-TIER SLA VIOLATIONS UNDER CHURN (PER-TENANT GT). OUR ROWS AND THE BASELINE ARE MEASURED; THE SHARD ROW IS A DUTY-CYCLE _upper bound_ COMPUTED FROM MEASURED REBUILD WALL-CLOCKS, NOT A MEASURED HEAD-TO-HEAD.

