<tbc>for each (_p,r_) it maintains at most one tuple per finishing interval and discards dominated tuples, and in sparse temporal regimes only a small fraction of concatenations are admissible. Consequently, the effective number of tuple updates per entry is often far below _M_, and the observed scaling over the tested regimes is closer to _O(n_<sup>3</sup>) than the worst-case _O(M_<sup>2</sup>_n_<sup>3</sup>). To make this explicit, we additionally report controlled sweeps holding _M_ fixed while varying _n_, and holding _n_ fixed while varying _M_.

### 7.7 Shortest-Time Paths: Waiting-to-Traversal Regime Shift

We now connect temporal contact structure to end-to-end routing behavior. For sampled source-destination pairs, we compute shortest communication-time paths and decompose total time into traversal and waiting components:

\(\mathcal{T}_{pq}=T_\mathrm{trav}+T_\mathrm{wait},T_\mathrm{trav}=\sum_\mathrm{hops}t_{uv}\tau,T_\mathrm{wait}=\mathcal{T}_{pq}-T_\mathrm{trav}.\) (11)

Figure 8 summarizes hop counts and waiting fractions for \(n\approx 2\times 10^4\).

Hop count is not a latency predictor: A path with fewer hops can still incur larger T_<sub>pq</sub>_ if it repeatedly arrives at intermediate nodes during gaps or during short runs (_\<t<sub>uv</sub>_) in \(CS_{uv}^{(R)}\), forcing buffering until an admissible run appears.

Waiting fraction reveals the operating regime: As _R_ increases, feasible windows become longer and more frequent, which reduces waiting. Therefore, shortest-time operation shifts from waiting-dominated (contact-limited) at small<tbc>

<tbc>_R_<tbc>

<tbc>to traversal-dominated (connectivity-rich) at larger _R_.  10 lists reporting-ready summary statistics for shortest communication time, hop count, and waiting fraction.

### 7.8 Discussion and Engineering Implications

The results establish a methodology-consistent chain from physical feasibility to temporal routing performance. The optical feasibility threshold _R_ directly shapes temporal adjacency by controlling snapshot-wise degree and link churn: smaller _R_ produces sparser graphs with higher %Found/%Missing (greater intermittency), whereas larger _R_ increases link persistence and smooths connectivity over time ( 5). These adjacency dynamics translate into the run structure of connectivity strings \(CS_{pq}^{(R)}\), where larger _R_ yields longer runs of ones and shorter gaps ( 6), increasing the likelihood that the run-length admissibility condition (\(\ge t_{uv}\)) is satisfied immediately after packet arrival. As a consequence, improved run persistence reduces buffering and waiting at intermediate nodes, shifting shortest-time routes from waiting-dominated behavior in contact-limited regimes toward traversal-dominated behavior in connectivity-rich regimes (Fig. 8,  10). From an algorithmic standpoint, the high agreement with time- expanded and temporal shortest-path baselines ( 8) supports the correctness of tuple composition in Procedure 3 under the same admissibility rules, while the measured runtime and memory trends ( 9) clarify where full APSP is practical and where sampled-pair evaluation becomes necessary at mega-constellation scale. Collectively, these findings motivate cross-layer co-design: _R_ shapes the temporal contact fabric \(CS_{pq}^{(R)}\), while discretization \(\tau\) and per-hop requirement _t<sub>pq</sub>_ set the feasibility threshold that governs waiting. The joint choice of \((R,\tau,t_{pq})\) therefore determines whether the constellation operates as a low- latency mesh or as a contact-limited delay-tolerant network.

## 8 CONCLUSION

In this paper, we have addressed the routing problem in a highly heterogeneous and dynamic 6G network archi<tbc>

\begin{tabular}{cc}
**Statistic** & **Definition / Rationale** \\
\(\bar{k}(R)\) & Mean snapshot-wise degree: \(\frac{1}{M}\sum_{t=1}^M\bar{k}_t(R)\). \\
_k_<sub>5</sub>(_R),k_<sub>95</sub>(_R_) & 5th/95th percentiles of \(\bar{k}_t(R)\); characterize trough severity and peak richness. \\
CV_<sub>k</sub>(R_) & Coefficient of variation of \(\bar{k}_t(R)\); larger values imply higher intermittency (waiting-prone). \\
\(\Delta_k(R)\) & Modulation amplitude, e.g., _k_<sub>95</sub>(_R_)-_k_<sub>5</sub>(_R_); links densification to orbital recurrence. \\
\end{tabular}

\begin{tabular}{ccccc}
_n_ & \((\tau,M)\) & Reachability match (%) & Latency exact match (%) & Max diff (snapshots) \\
2048 & (20,288) & 100.0 & 99.4 & 1 \\
4096 & (20,288) & 99.98 & 99.1 & 2 \\
8192 & (10,576) & 99.92 & 98.6 & 2 \\
\end{tabular}

\begin{tabular}{ccccc}
_n_ & \(\tau\) (s) & _M_ & Runtime (s) & Peak Mem (GB) \\
2048 & 20 & 288 & \(13.1\pm 0.4\) & \(2.0\pm 0.1\) \\
4096 & 20 & 288 & \(104\pm 3\) & \(7.9\pm 0.2\) \\
8192 & 10 & 576 & \(910\pm 25\) & \(33.4\pm 0.8\) \\
16384 & 10 & 576 & \(7420\pm 210\) & \(121.6\pm 2.9\) \\
\end{tabular}

TABLE 7

Summary statistics for temporal edge densification (derived from Fig. 7).

TABLE 8

Baseline agreement between Algorithm 1 and a known-correct time-expanded-graph (TEG) shortest-path baseline on configurations where the TEG is tractable. For _n_=2048 we evaluate all ordered pairs (_p,q_) with \(p\neq q\). For larger _n_ we evaluate uniformly sampled distinct ordered pairs with _N_<sub>pairs</sub>=50,000 per trial and report mean\(\pm\)std over _K_=5 random seeds. Unless stated otherwise: _R_=1500km, _t<sub>pq</sub>_=2, and ties in T_<sub>pq</sub>_ are broken by smallest finishing interval _I<sub>f</sub>_ and then smallest starting interval _I<sub>s</sub>_.

TABLE 9

Performance summary (mean\(\pm\)std over 5 runs; peak memory as RSS).

