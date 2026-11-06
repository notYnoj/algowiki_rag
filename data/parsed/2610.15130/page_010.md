<tbc>convex tail) and the query average corrects both. The bound is _safe but loose_ at low \(\sigma_\mathrm{loc}\)/small _L_, where \(\bar{h}_\tau\) under-predicts measured recall by up to 14 pp. No retreat to the assumption- free envelope is needed; the only cost is that the guarantee is stated on \(\bar{h}_\tau\) (a query average) rather than on the mean density, and is conservative for spatially-correlated predicates (binomial independence under-counts correlated in-predicate mass).

### i) Bound-check at scale.:

At 100K, for the _c_=1000 merge the measured loss is 0.30 pp, within the batch-fraction cap _c/(N+c_)=0.99 pp (\(3.3\times\) slack; at 18K, 0.09 pp within 5.26 pp). The cap holds at mid-scale, though the batch-fraction cap is weak (it is satisfied by any merge that does not corrupt a constant fraction of the graph), so this is a sanity check, not a discriminating test ofS Assumption 2. (The single-merge isolation at _c_=10K, _N_=100K independently reads 0.30 pp, a coincidence of value from a different experiment.)

## D. Recall-latency feasibility

The admission test of Contribution C1 (\(1.25k/\sigma_\mathrm{loc}\le L_\mathrm{max}(\ell_\tau)\)) assumes search cost is linear in _L_; we measure it. Mean search latency is linear in _L_ (\(\mathrm{mean}(L)\approx 0.22\mathrm{ms}\cdot L+1.6\mathrm{ms}\), with mean disk IOs ≈_L_ exactly, since the search is IO-bound, one candidate ≈ one IO; Fig. 2), so the cost<tbc>

<tbc>model **holds** and \(L_\mathrm{max}(\ell_\tau)\approx\ell_\tau/0.22\mathrm{ms}\), giving the concrete feasibility condition

\(\sigma_\mathrm{loc}\ge 1.25k/L_\mathrm{max}(\ell_\tau)\approx 1.25k\cdot 0.22\mathrm{ms}/\ell_\tau\) (e.g. \(\ell_\tau=50\mathrm{ms}\Rightarrow\sigma_\mathrm{loc}\unknown 0.055).\) (12)

This prices the boundary of §V-F/§VII quantitatively: a \(\sigma_\mathrm{loc}=0.01\) tenant needs _L_<sub>95</sub>≈1250, i.e. ≈275 ms mean, so it cannot hold a 95% recall floor and an interactive latency SLO on this substrate, and the test reports this _before_ deployment (Fig. S2, supplementary material). We report the test on **mean** latency, with a \(\rho\)=0.95 floor and a candidate latency ladder (\(\ell\in\{10,50,200\}\) ms). Since an interactive SLO is ultimately a _tail_ guarantee, a low-contention _p_<sub>99</sub> capture would extend the test to the tail; the linear-cost and infeasibility conclusions here rest on the mean.

## E. Multi-tenant SLA under churn (the payoff axis)

On an identical, genuinely-contended churn stream (_T_=6, tiers tight/medium/lax, ceilings 1000/3000/10<sup>9</sup>), the C3 ceiling drives tight-tier SLA violations to _zero_ at equal staleness and equal drained recall (82.34 vs. 82.22, i.e. enforcement costs nothing on terminal recall), where an otherwise-identical scheduler-less baseline violates every tight query ( III). The medium tier is uneventful in this regime (zero violations on _both_ legs), so the ceiling protects the tight tier only. Two qualifications bound the reading. The violation counted here is a per-tenant staleness-ceiling breach, staleness exceeding \(S_\tau\), a freshness bound distinct from the recall/latency SLO (\(\rho_\tau,\ell_\tau\)). The baseline comparison is close to definitional (C3 force-drains at \(S_\tau\)), so it establishes that the mechanism is implemented and effective; and the 100%-vs-0% split is a _saturated_ margin (tight queries arrive in a burst inside the post-ceiling stale window), demonstrating the mechanism while the magnitude is specific to this 10K, three-checkpoint regime. The mechanism is not free in every regime; in an earlier configuration whose high-volume tier was the _lax_ one, honoring tight ceilings deferred it and cost ≈10 pp of aggregate unfiltered recall at intermediate checkpoints (final topology unaffected by merge-order invariance). The substantive comparator is a per-tenant shard, against which ours is a rebuild-outage advantage: a shard is unqueryable for each cold rebuild, growing with per-tenant size (0.26 s at 1.8K/tenant to ≈28 s at 100K/tenant), while ours never rebuilds (no rebuild- induced serving outage; the index stays queryable through the background merge, which does inflate the tail for ≈_c/d_ s but

\begin{tabular}{cccccccc}
control (_T_) & \(\sigma\)=1_/T_ & \(\hat{\sigma}_\mathrm{loc}\) & _L_=75 & 150 & 300 & 600 & 1000 \\ diffuse (6) & 0.167 & 0.168 & 95.42 & 99.97 & 99.99 & 100.0 & 100.0 \\ diffuse (12) & 0.083 & 0.084 & 61.87 & 95.27 & 99.98 & 100.0 & 100.0 \\ diffuse (24) & 0.042 & 0.042 & 31.36 & 61.54 & 95.29 & 99.99 & 100.0 \\ diffuse (48) & 0.021 & 0.021 & 15.63 & 31.06 & 61.03 & 95.40 & 99.94 \\ diffuse (96) & 0.010 & 0.010 & 7.75 & 15.51 & 30.98 & 61.41 & 89.99 \\ clustered (6) & 0.167 & 0.511 & 97.78 & 99.47 & 99.84 & 99.94 & 99.97 \\ clustered (24) & 0.042 & 0.168 & 73.55 & 92.30 & 98.71 & 99.83 & 99.96 \\ clustered (96) & 0.010 & 0.047 & 29.18 & 47.17 & 71.61 & 92.80 & 98.87 \\ \end{tabular}

F13a: mean latency linear in L
mean, 10k mean, 100k 200 0.22 ms L + 1.6 mean latency (ms) 150 100 50 200 400 600 800 1000 search width L

TABLE II

POST-FILTER RECALL@10 vs. (\(\hat{\sigma}_\mathrm{loc},L\)), SIFT-10K, PER-LABEL GT. GLOBAL SELECTIVITY \(\sigma\)=1_/T_ SHOWN FOR CONTRAST: FOR SPATIALLY-COHERENT (CLUSTERED) TENANTS \(\hat{\sigma}_\mathrm{loc}\) EXCEEDS \(\sigma\) SEVERAL-FOLD AT EVERY TENANT COUNT, AND IT IS \(\hat{\sigma}_\mathrm{loc}\) THAT GOVERNS RECALL.

Fig. 2. Mean search latency is linear in the search width _L_ at both scales (\(\mathrm{mean}(L)\approx 0.22\mathrm{ms}\cdot L+1.6\mathrm{ms}\); mean disk IOs ≈_L_, one candidate ≈ one IO), the IO-bound cost model on which the C1 admission test rests. Latencies are cache-empty disk-index means; the figure establishes the linearity of the cost model, not absolute speed.

