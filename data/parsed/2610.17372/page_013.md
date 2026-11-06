## 7.4 Effect of Optical Range _R_ on Temporal Contact Density

We next quantify how the physical feasibility threshold _R_ shapes temporal adjacency. Figure 7 plots snapshot- wise average degree \(\bar{k}_t(R)\) over one orbit for \(R\in\{659,1319,1500,1700\}\) km.

(1) Periodicity: Connectivity exhibits repeated peaks and troughs over the orbit, validating the one-orbit observation window and confirming that temporal connectivity is structured rather than random.

(2) Densification with _R_: Increasing _R_ increases baseline degree and reduces trough depth. In terms of the methodology, larger _R_ increases the likelihood that when a packet arrives at a node, at least one outgoing edge will soon have a contiguous run of ones of length \(\ge t_{uv}\), reducing waiting.

7 reports compact statistics derived from Fig. 7, including intermittency (CV<sub>_k_</sub>) that correlates with waiting- dominated operation.

## 7.5 Baseline Comparison: Correctness Agreement

We validate correctness by comparing Algorithm 1 to two known-correct baselines on configurations where they are feasible: (i) a time-expanded graph shortest-path method and (ii) a temporal Dijkstra-like method that uses the same run-length admissibility rule (contiguous ones of length \(\ge t_{uv}\) after arrival). Time-expanded constructions and temporal shortest-path formulations are standard baselines for temporal routing validation \[31\], \[30\], \[32\]. For a test set of ordered pairs S, we measure reachability agreement and latency agreement (Section 6.5). Baselines were evaluated on the same temporal-graph instances and admissibility rules (contiguous runs of ones of length \(\ge t_{uv}\)). Unless stated otherwise, agreement is computed over _N_pairs randomly sampled ordered pairs (distinct \(p\neq q\)) using a fixed seed; for the smallest configuration (_n_=2048) we additionally verified agreement over all ordered pairs. When multiple optimal solutions exist (ties in T_<sub>pq</sub>_), we break ties by selecting the smallest finishing interval _I<sub>f</sub>_, and then the smallest starting interval _I<sub>s</sub>_.

\begin{tabular}{cc}
**Parameter** & **Value(s)** \\
Orbit window & One orbital period, \(T=M\tau\approx 96\) min (LEO-like); sensitivity: \(P_\mathrm{orb}\in[90,128]\) min \\
Snapshot duration \(\tau\) & {5, 10, 20} s \\
Number of snapshots _M_ & For _T_=96 min: _M_={1152, 576, 288} for \(\tau=\{5,10,20\}\) s \\
Constellation size _n_ & Mega-constellation: _n_≈20,000; scalability sweeps: \(n\in\{2048,4096,8192,16384,20000\}\) \\
Source-destination sampling & Uniform random distinct pairs; _N_pairs=50,000 per _R_ (reachability/latency); 10,000 per _R_ (hop/wait decomposition) \\
FSO feasibility threshold _R_ & {659, 1319, 1500, 1700} km \\
Connectivity primitive & Connectivity strings \(CS_{pq}^{(R)}[t]=\unknown\{d_{pq}(t)\le R\}\) over _t_=1_,...,M_ \\
Edge traversal requirement _t<sub>pq</sub>_ & Constant per hop: baseline _t<sub>pq</sub>_=2 snapshots; sensitivity: \(t_{pq}\in\{1,2\}\) \\
Temporal-path admissibility & Time-respecting paths requiring a contiguous run of ones of length \(\ge t_{pq}\) on each traversed edge \\
Reported metrics & Reachability, T_<sub>pq</sub>_, hop count, waiting fraction _f<sub>w</sub>_, temporal degree series \(\bar{k}_t(R)\) \\
\end{tabular}

\begin{tabular}{cccccccc}
_R_ (km) & Mean %Found & Mean %Missing & \(\bar{k}\) (deg) & Reach. (%) & Med\[T \] (s) & Med\[_H_\] & Med\[_f<sub>w</sub>_\] \\
659 & \(19.0\pm 0.6\) & \(19.5\pm 0.7\) & \(5.2\pm 0.3\) & \(71.4\pm 1.2\) & \(184\pm 9\) & \(8.1\pm 0.4\) & \(0.68\pm 0.03\) \\
1319 & \(11.2\pm 0.4\) & \(10.9\pm 0.4\) & \(9.8\pm 0.5\) & \(92.6\pm 0.6\) & \(97\pm 5\) & \(6.3\pm 0.3\) & \(0.41\pm 0.02\) \\
1500 & \(8.7\pm 0.3\) & \(8.5\pm 0.3\) & \(11.4\pm 0.6\) & \(96.1\pm 0.4\) & \(79\pm 4\) & \(5.7\pm 0.3\) & \(0.31\pm 0.02\) \\
1700 & \(6.2\pm 0.2\) & \(6.0\pm 0.2\) & \(13.6\pm 0.7\) & \(98.3\pm 0.2\) & \(64\pm 3\) & \(5.1\pm 0.2\) & \(0.22\pm 0.01\) \\
\end{tabular}

\begin{tabular}{ccccccc}
**Method** & **Reach. (%)** & **Med\[T \] (s)** & **P95\[T \] (s)** & **Med\[_f<sub>w</sub>_\]** & **Runtime (s)** & **Reference** \\
**Ours (Alg. 1)** & **96.7**\(\pm\)**0.3** & **59**\(\pm\)**4** & **168**\(\pm\)**8** & **0.31**\(\pm\)**0.02** & **118**\(\pm\)**6** & **Our work** \\
TEG & 91.1\(\pm\)0.6 & 66\(\pm\)5 & 1177\(\pm\)6 & 0.37\(\pm\)0.01 & 1620\(\pm\)55 & \[30\], \[31\] \\
Temporal Dijkstra & 92.6\(\pm\)0.4 & 80\(\pm\)4 & 171\(\pm\)9 & 0.32\(\pm\)0.02 & 790\(\pm\)30 & \[32\], \[30\] \\
Time graph routing & 87.4\(\pm\)0.2 & 92\(\pm\)5 & 196\(\pm\)11 & 0.38\(\pm\)0.03 & 245\(\pm\)12 & \[33\], \[34\] \\
Dynamic time routing & 85.9\(\pm\)0.4 & 84\(\pm\)5 & 179\(\pm\)10 & 0.34\(\pm\)0.02 & 410\(\pm\)18 & \[35\] \\
Spl. shortest paths & 94.8\(\pm\)0.6 & 81\(\pm\)4 & 173\(\pm\)9 & 0.33\(\pm\)0.02 & 305\(\pm\)15 & \[36\], \[37\] \\
\end{tabular}

TABLE 1

Experimental parameters used in orbit-scale temporal-graph evaluation.

TABLE 2

End-to-end temporal-routing performance over one orbital window as a function of optical range _R_. Larger _R_ increases temporal connectivity (higher \(\bar{k}\), lower churn) and improves routing outcomes (higher reachability, lower Med\[T \] and Med\[_f<sub>w</sub>_\]). Values are mean\(\pm\)std over _K_=5 trials.

TABLE 3

Comparison with representative baseline methods under the same temporal-graph instance and hop-admissibility rule (a hop (_p,q_) is traversable at time _t_ only if _CS<sub>pq</sub>_\[_t:t+t<sub>pq</sub>_-1\] is all ones). TEG (restricted) is evaluated with a restricted departure-time set T_<sub>s</sub>_ (uniformly sampled start times) and a finite horizon _H_ snapshots due to time-expanded memory limits; therefore its reported reachability is a conservative lower bound relative to full \(\mathrm{min}_{t_s\in\{0,\dots,M-1\}}\) evaluation. Reported values are mean\(\pm\)std over _K_=5 trials using identical \((n,M,\tau,R,t_{pq})\) settings and identical sampled (_s,d_) pairs per trial.

