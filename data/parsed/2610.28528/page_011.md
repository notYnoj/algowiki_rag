<tbc>cation in the dataset: its 1967339 recovered solutions, a 11923\(\times\) expansion of the quantum pool, represent 0.26% of a ground-state manifold of \(D_\mathrm{MIS}=7.7\times 10^8\). Manifold size is not the only factor, however, and the two must be separated before the trend can be interpreted. Coverage also depends on how many seeds the hardware supplied, and across these 35 instances the seed pool spans 2 to 493 solutions. Writing _f=N_<sub>total</sub>_/D_<sub>MIS</sub> for the recovered fraction of the manifold, a joint fit of both predictors gives

\(f\propto D_\mathrm{MIS}^{-0.58\pm 0.04}n_\mathrm{seed}^{1.40\pm 0.12}\) (2)

with _R_<sup>2</sup>=0.89, and the two effects are close to independent in this dataset (Spearman \(\rho=+0.17\) between _n_<sub>seed</sub> and _D_<sub>MIS</sub>, _p_=0.3). Controlling for seed count therefore _strengthens_ the degeneracy trend rather than explaining it away: the partial rank correlation between coverage and _D_<sub>MIS</sub> at fixed _n_<sub>seed</sub> is -0.94, against -0.79 for the raw pairwise value, while the partial correlation with seed count at fixed degeneracy is +0.85. The marker shapes in Figure 5 show both factors acting together: binning by seed pool as in the seed statistics above, median coverage rises from 0.3% for the thirteen instances with fewer than 10 seeds, to 26.6% for the fourteen with 10 to 99, to 70.2% for the eight with 100 or more. This is the expected behaviour of a method working from a bounded seed budget, and it sets the trade-off. The absolute number of solutions recovered grows with manifold size (Spearman \(\rho=+0.66\) between _D_<sub>MIS</sub> and final count), while the _fraction_ recovered falls. Applications needing a fixed number of diverse solutions are therefore well served across the whole range, whereas applications needing a guaranteed-complete manifold are served only when the manifold is small enough to enumerate from the seeds available. Of the two factors, only the seed count is under experimental control, since _D_<sub>MIS</sub> is a property of the instance.

### F. Computational Efficiency

Figure 6 shows cluster-update time versus final solution count for the 40 instances whose size did not improve. All runs completed on a standard laptop [15], and the entire dataset, 2451 quantum seeds expanded to 2749146 validated configurations, required 1073 seconds of computation end to end, i.e., 18 minutes on a single laptop core. Almost all of it is the cluster-update loop: 870 seconds across the 43 first-level passes and 200 seconds for the higher-level passes of the three multilevel runs. The one-off repair of every post-selected hardware sample to a maximal independent set (Section IID) takes 2 seconds for all 18759 samples. Both stages are recovery costs. The post-hoc validation of Section IIF and the coverage certification of Section IIIE are analysis costs and are excluded. Of those configurations, 2485881 are certified optimal against the reference values. The remaining 263265, or 9.6%, belong to the 8 instances whose<tbc>

<tbc>seed pool sat below the certified optimum (Section IIF) and are validated at their best-found size rather than at the true optimum. The post-processing cost is small compared with the hardware time already expended: at a cycle time of about 0.1s [7], a 1000-shot run takes about 100s of device time per instance. Per family:

• **Benchmark instances**: from under 1 second (`HP125`, `HP1412`, with only 3 and 15 pairs) up to 580 seconds for instance `HP1478` (13530 pairs), spanning nearly four orders of magnitude in runtime.<tbc>

• **Hard instances**: from under 1 second up to 20 seconds (`L16\_seed4392`, 190 pairs), all reaching exhaustive pairwise exploration of their first- level seed pools. The two higher-level passes of `L17\_seed46` halted on saturation instead and took 200 seconds together.<tbc>

• **Standard instances**: from under 1 second to approximately 90 seconds, depending on manifold size.

Figure 6 plots cluster-update time rather than end-to- end time, because it is the exploration loop whose cost scales with the manifold being recovered. On that axis the log-log plot reveals a near-linear scaling of solution count with runtime, \(N_\mathrm{total}\propto t^{0.89}\) (_R_<sup>2</sup>=0.93), the exponent slightly below unity indicating modestly diminishing returns on additional computation. Substantial scatter remains about this trend: instances with comparable run times can differ by more than an order of magnitude in final count, because the per-pair cost (set by cluster count and repair complexity) varies by more than three orders of magnitude across the dataset, while the number of pairs required depends on seed-pool size.

The hard cutoff of 10<sup>5</sup> pair comparisons was never invoked, since the pass with the most pairs processed required only 16539. Combined with the modest hardware requirements, these results suggest Houdayer post- processing is a practical and lightweight component of any quantum optimization pipeline, as can also be seen in Fig. 6 where the scaling is close to linear.

## IV. DISCUSSION

### A. Why Houdayer Cluster Updates Work for the MIS Problem

The effectiveness of Houdayer cluster updates for MIS manifold exploration rests on a combination of structural and algorithmic properties that make it well-matched to the geometry of degenerate combinatorial optimization problems, especially for unit-disk quasi-two-dimensional graphs.

The key mechanism is nonlocal, rejection-free recombination. Local search moves such as single-vertex swaps [20] change one site at a time. Houdayer updates<tbc>

