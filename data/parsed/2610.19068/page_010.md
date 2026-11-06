Appendix

## A Full Retrieval Metrics

3 reports pass rate, retrieval precision, and retrieval recall for both architectures across all three subsets. Pass rate (fraction of queries where the planner’s intended plan selects at least one API) is reported here as a supplementary indicator; the main text focuses on precision and recall as the primary retrieval metrics. RtP leads on all G1 metrics; PtR leads on all G2 and G3 metrics.

## B Stub Generation Statistics

4 reports stub generation statistics per subset. The high uniqueness rate (79-99%) confirms stubs are hallucinated from scratch. The cosine similarity between stubs that correctly match a relevant API (0.874) and those that do not (0.872) is virtually identical, meaning the embedding space provides no signal to distinguish good routing from bad.

5 reports the effective search width for each architecture and subset at _k_=5. At equal nominal _k_, PtR explores ∼2-2.5\(\times\) more candidates than RtP before returning the top-_k_ to the planner.

\begin{tabular}{ccccccc}
 & & \multicolumn{2}{c}{**RtP**} & \multicolumn{2}{c}{**PtR**} & \\
**Subset** & **Metric** & **Mean** & \(\pm\)**Std** & **Mean** & \(\pm\)**Std** & _p_ \\
\multirow{3}{*}{G1 (_n_=200)} & Pass Rate & **0.884** & 0.015 & 0.840 & 0.024 & 0.022<sup>∗</sup> \\
 & Precision & **0.274** & - & 0.209 & 0.008 & _\<_0.001<sup>∗∗∗</sup> \\
 & Recall & **0.372** & - & 0.289 & 0.010 & 0.002<sup>∗∗</sup> \\
\multirow{3}{*}{G2 (_n_=200)} & Pass Rate & 0.747 & 0.015 & **0.855** & 0.020 & _\<_0.001<sup>∗∗∗</sup> \\
 & Precision & 0.167 & - & **0.204** & 0.007 & 0.039<sup>∗</sup> \\
 & Recall & 0.143 & - & **0.188** & 0.007 & _\<_0.001<sup>∗∗∗</sup> \\
\multirow{3}{*}{G3 (_n_=100)} & Pass Rate & 0.732 & 0.010 & **0.820** & 0.014 & _\<_0.001<sup>∗∗∗</sup> \\
 & Precision & 0.135 & - & **0.144** & 0.007 & 0.052 n.s. \\
 & Recall & 0.160 & - & **0.172** & 0.008 & 0.080 n.s. \\
\end{tabular}

\begin{tabular}{cccccc}
**Subset** & **Gen.%** & **Stubs/q** & **Unique%** & **Match%** & **Cos** \\
G1 & 98.5% & 2.1 & 98.6% & 40.6% & 0.874 (correct) / 0.872 (incorrect) \\
G2 & 99.5% & 2.4 & 93.6% & 38.3% & 0.843 / 0.840 \\
G3 & 100% & 2.5 & 79.1% & 24.8% & 0.858 / 0.854 \\
\end{tabular}

\begin{tabular}{ccccccc}
**Subset** & **Stubs/q** & **PtR eff. width** & **RtP eff. width** & **Budget-equiv.** _k_ & **RtP recall** \\
G1 & 2.1 & ≈10 & 5 & 10 & 0.453 \\
G2 & 2.4 & ≈12 & 5 & 10 & 0.186 \\
G3 & 2.5 & ≈13 & 5 & 10 & 0.217 \\
\end{tabular}

** 3** Retrieval metrics by subset (4 independent runs each). RtP precision and recall are deterministic (no run-to-run variance; reported without std). _p_-values: one-sample _t_-test for precision/recall (PtR’s 4-run mean vs. deterministic RtP); two-sample _t_-test for pass rate. **Bold**: best mean per metric. <sup>∗∗</sup>_p\<_0.01, <sup>∗∗∗</sup>_p\<_0.001, n.s. = not significant.

** 4** Stub generation statistics by subset. _Gen.%_: fraction of queries generating stubs. _Stubs/q_: mean stubs per query. _Unique%_: fraction of stub names unique across queries. _Match%_: fraction of stubs whose top-1 matched API is in Ground-Truth. _Cos_: mean cosine similarity of stub to its top-1 match (virtually identical for correct vs. incorrect matches).

** 5** Effective search width at _k_=5. RtP searches exactly _k_ candidates; PtR searches \(k\times\)Stubs/q (union, deduped) then returns top-_k_. Budget-equivalent RtP recall from  1.

