## V. EVALUATION

#### a) Setup.:

Prototype on a FreshDiskANN fork, `io\_uring`; SIFT at 10K (robust local scale) and 100K (mid-scale), plus a filtered YFCC slice; Yamana _R_=32, build/search _L_=75, beam 4, _k_=10. Every filtered/multi- tenant recall uses _per-label_ ground truth, built as the true top-_k_ among same-label points by brute force. Unfiltered ground truth would floor label-filtered recall at ≈1_/L_<sub>pred</sub>; on one label at 2,500 queries the same run reads 24.4 against unfiltered ground truth versus 86.6 against per-label ground truth, a +62 pp gap that brackets the 1/6 floor. Every reference used here is brute-force _K_=100 in the two-block format the loader expects. Disk-graph numbers are cache-empty; we state the engine and full config on each. Determinism (insert-order invariance) means exponent uncertainty is the log-log fit CI, not run replication.

#### A. Merge-order re-ordering has negligible effect on terminal recall

The general theorem’s additivity rests on the scheduler not degrading the terminal graph (Assumption 5). We replay the enforce-ordered and FIFO-ordered multi-partition merge groupings to the _identical_ 18,000-point terminal and read cache-empty recall@10 under an identical search over the full 10,000-query set: \(\Delta=\text{recall(enforce)}-\text{recall(FIFO)}=54.58-54.60=-0.02\) pp, i.e. \(|\Delta|=0.02\) pp \(\le 0.67\) pp ( I; also Fig. S1). Re-ordering therefore leaves terminal recall unchanged to within 0.02 pp, the order-invariance the label-blind design predicts (Assumption 5). The instrument measures recall, so the claim is functional equivalence at the recall level.

The instrument’s absolute value (54.6) sits far below every other recall we report (≈99.7) for a benign reason. To obtain a single-method \(\Delta\) we searched both terminals with one standalone tool that scores all 18,000 live points against ground truth built for the first 8,000, so about half of each query’s true neighbours lie outside the scored reference. This depresses both legs _equally_, cancelling in \(\Delta\) though not in the level (the aligned in-process path reads 99.911 on the enforce leg but hangs on the other leg on this box, so the aligned-absolute \(\Delta\) is deferred). The 0.02 pp is a real graph difference rather than noise, since both indexes are deterministic and insert- order replication is byte-identical across seeds (\(\sigma=0.000\) pp). The 0.67 pp acceptance band is a pre-registered prior threshold, not a power calculation; it comes from a separate single-partition deferred-vs-FIFO experiment (97.0 vs. 97.67 at 80K) that over-estimates the compositional effect because its terminal drain was one large merge (carrying the merge- size effect of Theorem 3); we claim only that the measured \(\Delta\) is two orders of magnitude inside it, with no calibrated power to exclude differences between 0.02 and 0.67 pp.

#### B. Anti-amortization: the per-merge law, and how it assembles over a horizon

This subsection carries the empirical weight of Theorem 3, whose two factors are measured separately: the _per-merge_ law<tbc>

<tbc>_g(c,N_)<tbc>

<tbc>(measured directly and cleanly), and its _assembly_ over _M_ merges (measured at a single _c_, and sub-additive).

#### a) (a) Per-merge law (single-merge isolation, N_<sub>0</sub>=100_K, L_=75).:

We restore a pristine base graph, insert exactly _c_ fresh points, force one merge, reload with an empty memory index, and read cache-empty recall@10 over 10K SIFT queries against ground truth for the identical live set; the reference _R_<sub>scratch</sub> is a from-scratch Yamana on the same points with identical parameters.  SI (supplementary material) gives _g=R_<sub>scratch</sub>-_R_<sub>merge</sub>. The fitted exponent is _a_=1.28 (95% CI \[1.03,1.52\], _R_<sup>2</sup>=0.99) after excluding the two cells below the 0.02 pp floor, confirming a super-linear trend; the local slopes across successive doublings (1.17,0.88,1.64,1.44) straddle 1, so the trend holds over the range without monotone super-linearity at every _c_. The batch-fraction cap acts as a structural ceiling rather than a predictive law, with _g_<sub>frac</sub> sitting 10-300\(\times\) under _c/(N+c_) throughout. Because _R_<sub>scratch</sub> varies only 0.18 pp across the sweep (99.71 \(\rightarrow\) 99.53), the _c_- comparison is not an artifact of a moving reference.

#### b) (b) Assembly over a horizon (twelve sequential merges, c_=5000, N<sub>0</sub>=100_K).:_

The theorem multiplies _g_ by _M_. We test that directly: a streaming inserts-only run with _M_=12 forced merges of _c_=5000 each, reading cache-empty recall at every merge boundary against ground truth matched to the live set. The first merge reproduces the isolation harness to 0.006 pp (99.627 vs. 99.633), validating the two measurements against each other. Cumulative loss then grows to 0.384 pp by _m_=12 (relative to _m_=1; ≈0.46 pp against a from-scratch 160K reference), against _M\(\cdot g=1.04\) pp predicted by additive assembly ( SII, supplementary material). The per-merge increment settles to ≈0.024 pp after a four-merge transient, with no downward trend, so the loss is linear in _M_ in _steady state_, but at a per-merge rate \(3.6\times\) below the isolated single- merge _g_. The mechanism is visible in a per-epoch decomposition of the missed top-_k_: the _V_<sub>0</sub> (pre-existing point) component decays with _m_ while the newly-inserted-frontier component grows: later merges damage the recent frontier rather than red- damaging the base. This carries one favourable implication and one cost. Favourably, the _c_-independent _V_<sub>0</sub> floor saturates instead of accumulating, removing the \(Mg_0\propto 1/c\) term and with it any interior recall-optimum in _c_ (§III-A). The cost is that _M\(\cdot g\) over-states the horizon loss by 2.3-2.7\(\times\) at this _c_, so the additive bound is conservative in this regime, and whether \(\eta\) is _c_-dependent (which could in principle flatten _L_<sup>∗</sup>(_c_)) is settled by part (c). The decomposition is scratch-free and not tie-aware, so its absolute magnitudes are confounded, and the conclusions above use only its sign and the decomposition-free comparison \(L_\mathrm{cum}\checkmark Mg_0\).

\begin{tabular}{ccc}
leg & terminal pts & recall@10 (same tool) \\
enforce-ordered & 18,000 & 54.58 \\
FIFO-ordered & 18,000 & 54.60 \\
\multicolumn{3}{c}{\(|\Delta|=0.02\) pp, inside the \(\le 0.67\) pp band.} \\
\end{tabular}

TABLE I

TERMINAL-RECALL \(\Delta\) UNDER MERGE RE-ORDERING (IDENTICAL 18K TERMINALS, SAME-METHOD RELATIVE).

