<tbc>pipelined-SSD search targets and the beam-4 `io\_uring` path does not. On the filtered axis the design is competitive at high \(\sigma_\mathrm{loc}\) with Filtered-DiskANN (86.56 vs. 85.9-87.8) while additionally supporting streaming and multi-tenancy, and the low-\(\sigma_\mathrm{loc}\) collapse is a shared graph-substrate property.

## IV. SUPPLEMENTARY FIGURES

\begin{tabular}{ccccc}
_m_ & live _N_ & cum. loss (pp) & \(M\cdot g\) (pp) & ratio \(\eta\) \\
1 & 105,000 & 0.000 & 0.087 & -- \\
4 & 120,000 & 0.188 & 0.348 & 0.54 \\
8 & 140,000 & 0.292 & 0.696 & 0.42 \\
12 & 160,000 & 0.384 & 1.044 & 0.37 \\
\end{tabular}

\begin{tabular}{ccccccc}
\((\hat{\sigma}_\mathrm{loc},L)\) & \(\mu\) & _x_ & meas. & _h_ & resid & _h_<sub>tail</sub> \\
\multicolumn{7}{c}{_diffuse_ (ladder; \(\hat{\sigma}_\mathrm{loc}\) measured, ≈1_/T_)} \\
(0.01033,75) & 0.775 & 0.078 & 7.75 & 7.75 & -0.00 & _\<_0.01 \\
(0.02077,75) & 1.558 & 0.156 & 15.63 & 15.58 & -0.05 & _\<_0.05 \\
(0.01033,300) & 3.099 & 0.310 & 30.98 & 30.99 & +0.01 & 2.6 \\
(0.04168,75) & 3.126 & 0.313 & 31.36 & 31.25 & -0.11 & 3.8 \\
(0.01033,600) & 6.198 & 0.620 & 61.41 & 61.31 & -0.10 & 55.8 \\
(0.02077,300) & 6.231 & 0.623 & 61.03 & 61.63 & +0.60 & 58.9 \\
(0.08383,75) & 6.287 & 0.629 & 61.87 & 62.24 & +0.38 & 62.2 \\
(0.01033,1000) & 10.330 & 1.033 & 89.99 & 88.83 & -1.16 & 96.0 \\
(0.04168,300) & 12.504 & 1.250 & 95.29 & 95.25 & -0.04 & 99.7 \\
(0.16750,75) & 12.563 & 1.256 & 95.42 & 96.07 & +0.66 & 99.7 \\
(0.02077,1000) & 20.770 & 2.077 & 99.94 & 99.87 & -0.07 & 100.0 \\
\multicolumn{7}{c}{_clustered_ (_h_ at the mean \(\hat{\sigma}_\mathrm{loc}\); all residuals one-signed)} \\
(0.04702,75) & 3.527 & 0.353 & 29.18 & 35.26 & +6.1 & 5.6 \\
(0.04702,150) & 7.053 & 0.705 & 47.17 & 68.88 & +21.7 & 71.4 \\
(0.04702,300) & 14.106 & 1.411 & 71.61 & 97.58 & +26.0 & 100.0 \\
(0.04702,600) & 28.212 & 2.821 & 92.80 & 100.0 & +7.2 & 100.0 \\
(0.16779,75) & 12.584 & 1.258 & 73.55 & 96.09 & +22.5 & 99.7 \\
(0.16779,150) & 25.169 & 2.517 & 92.30 & 100.0 & +7.7 & 100.0 \\
(0.51053,75) & 38.290 & 3.829 & 97.78 & 100.0 & +2.2 & 100.0 \\
\end{tabular}

F8: topology = -0.02 pp 0.67
55.0
54.8
54.60
recall@10 (same-method)
54.6
54.4
54.2
54.0
enforce
FIFO

F13b: feasibility (Oloc > 1.25k/L max)
latency @ p = 0.95
mean latency at 95% recall (ms)
102
t = 50 ms
101
t = 10 ms
10-2
10-1
Oloc

Serving vs merge-peak RSS (matched T=6)
1.75
serving: baseline + configured serving: PQ+tags ( = N)
1.50
merge: serving portion merge: released transient
peak RSS (GB)
1.25
1.00
0.75
0.50
0.25
slopes 18K-100K: serving bar 2.6 kB/pt (PQ+tags sub-seg. 0.115 kB/pt, only = N) merge-peak bar 8.3 kB/pt (transient, released)
0.00
18000 (T=6)
1000000 (T=6)

TABLE SII

HORIZON ASSEMBLY AT _c_=5000, _N_<sub>0</sub>=100K. MEASURED CUMULATIVE TIER-0B LOSS VS. THE ADDITIVE PREDICTION \(M\cdot g\).

TABLE SIII

MODEL COMPARISON ON THE COLLAPSED CURVE. \(\mu=\sigma_\mathrm{loc}L\), \(x=\mu/k\), _k_=10; ALL COLUMNS IN RECALL-%. _h_ IS LEMMA 7(II) WITH \(\beta\)=1 (NO FITTED CONSTANT); _h_<sub>tail</sub> IS THE SINGLE-TERM TAIL WITH THE PREVIOUSLY-CALIBRATED \(\beta\)=1.66; ENVELOPE IS LEMMA 7(1). THE _h_ COLUMN IS COMPUTED FROM THE 5-DECIMAL \(\hat{\sigma}_\mathrm{loc}\) USING A NORMAL APPROXIMATION TO E\[(_k-X_)<sup>+</sup>\] RATHER THAN THE EXACT BINOMIAL; THE APPROXIMATION IS GOOD TO \(\approx\pm 0.2\) PP, SO PER-CELL RESIDUALS BELOW THAT MAGNITUDE ARE WITHIN NUMERICAL PRECISION AND THE \(\le 1.2\) PP HEADLINE IS QUOTED AT THAT PRECISION.

Fig. S1. Terminal recall under enforce- and FIFO-ordered merges on the identical 18K terminal; \(|\Delta|=0.02\) pp inside the \(\le 0.67\) pp band.

Fig. S2. Feasibility boundary: the mean latency required to reach \(\rho\)=0.95 (at \(L_{95}=1.25k/\sigma_\mathrm{loc}\)) vs. local density, with candidate SLO lines \(\ell\in\{10,50,200\}\) ms; a tenant is feasible where its curve sits below its \(\ell\). Low- \(\sigma_\mathrm{loc}\) tenants (many-tenant, diffuse) are infeasible at an interactive SLO; this is the priced infeasibility boundary. The linear-in-_L_ cost model underlying the required-latency axis is Fig. 2 of the main text.

Fig. S3. RSS decomposition on the matched _T_=6 pair (18K, 100K), on the conventions of  IV. The _serving_ bar is whole-process first stable RSS, rising at 2.6 kB/point across the pair; its only \(\propto N\) component is the PQ-codes-and-tags residency (graph on disk), the sub-segment rising at 0.115 kB/point that is the bounded quantity restoring the serving-memory claim, the remainder being a fixed baseline plus configured, high-water- bounded allocations. The _merge-peak_ bar adds a released transient (the StreamingMerger’s in-RAM _O(N_) rewrite plus build-thread arenas), giving an 8.3 kB/point peak that is reclaimed after the merge and is reducible by thread and batch configuration.

