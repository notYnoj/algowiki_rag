<tbc>and its incident edges in a local neighborhood over four successive snapshots. We quantify the churn using neighbor- set persistence, Jaccard similarity, and turnover ( 4). This validates that the topology evolves substantially within one orbit and that static aggregation would be misleading, motivating the temporal model.

## 6.4 Traversal-Time Requirement and Run-Length Feasibility

As assumed in the methodology, traversing an edge is not instantaneous and requires _t<sub>pq</sub>_ snapshot units; therefore, a hop (_p,q_) is admissible only if a contiguous run of ones of length at least _t<sub>pq</sub>_ exists in _CS<sub>pq</sub>_ starting after the packet arrives at _p_. This is exactly the rule enforced by Procedure 1.

In the main results we use a conservative baseline _t<sub>pq</sub>_=2 snapshots for all feasible links, capturing non-propagation effects such as pointing/acquisition, scheduling, buffering, and framing overhead. We also perform sensitivity checks with \(t_{pq}\in\{1,2\}\) to quantify how stricter run requirements affect reachability and waiting.

To validate that run structure is the mechanism that drives waiting, we visualize feasibility timelines using a connectivity-string heatmap for a focus satellite and its neighbors (Fig. 6). We then compute standard run-length features ( 6), including duty cycle, run-length percentiles, and gap-length percentiles. These metrics link directly to Procedure 1: shorter runs and longer gaps increase the frequency with which the algorithm must search forward in time to find the next feasible transmission window.

## 6.5 Algorithmic Evaluation: Correctness, Necessity of Two Passes, and Baselines

For each range threshold _R_, we build the temporal adjacency matrix _A_<sup>(_R_)</sup> whose entries follow the tuple structure in Section 3, and compute the path matrix _P_<sup>(_R_)</sup> using Algorithm 1. Each \(P^{(\tilde{R})}(p,q)\) returns the selected shortest communication-time tuple \((I_s^{pq},I_f^{pq},pred^{pq})\) after Procedure 4.

We validate correctness against two known-correct baselines that optimize the same objective as our method: minimum end-to-end communication time (minimum duration). First, we construct a directed _time-expanded graph_ _G_<sub>TE</sub>=(_V_<sub>TE</sub>_,E_<sub>TE</sub>) whose node set is \(V_\mathrm{TE}=\{(v,t)|v\in V,t\in\{0,1,\dots,M-1\}\}\). To represent waiting and transmission under our run-feasibility constraint, we add (i) _wait edges_ \((v,t)\rightarrow(v,t+1)\) of weight 1 for all \(v\in V\) and _t\<M_-1, and (ii) _traverse edges_ \((p,t)\rightarrow(q,t+t_{pq})\) of weight _t<sub>pq</sub>_ if and only if the hop (_p,q_) is admissible at time _t_, i.e., \(CS_{pq}[t]=CS_{pq}[t+1]=\cdots=CS_{pq}[t+t_{pq}-1]=1\). For each ordered pair (_s,d_), we compute the shortest-path distance in _G_<sub>TE</sub> from (_s,t<sub>s</sub>_) to (_d,t<sub>f</sub>_) and then minimize over all possible departure times _t<sub>s</sub>_, namely \(\mathrm{min}_{t_s\in\{0,\dots,M-1\}}\mathrm{dist}_{G_\mathrm{TE}}\big((s,t_s),(d,\cdot)\big)\). This value equals the minimum number of snapshot intervals spent waiting plus traversing, and therefore equals \(\mathcal{T}_{sd}/\tau\) under the same run-length feasibility rule enforced by Procedure 1; as a result, _G_<sub>TE</sub> provides a known-correct baseline for the exact objective optimized by Algorithm 1.

As a second, independent correctness check, we implement a _temporal Dijkstra-like_ shortest-duration algorithm<tbc>

<tbc>(run for a subset of sources) over the same state space (_v,t_) with the same two transition types: unit-weight waiting transitions and admissible traverse transitions that require a contiguous run of ones of length at least _t<sub>pq</sub>_ beginning at the transmission time. This single-source baseline optimizes the same end-to-end duration objective T_<sub>sd</sub>_ and serves to validate our path-matrix update rules through an algorithmic approach that is structurally different from the time- expanded shortest-path computation.

For each tested pair (_p,q_) we compare: (i) whether a path exists (reachability agreement), (ii) the returned communication time \((I_f-I_s+1)\tau\) (latency agreement), and (iii) the reconstructed hop sequence (path agreement, when computed). We report the fraction of pairs with exact latency match and the maximum absolute latency deviation (in snapshots and seconds).

The methodology motivates performing two ordered sweeps--first forward and then backward--to ensure that optimal paths with different structural vertex-order patterns are discovered. We validate the necessity of this design experimentally by running three algorithm variants: a _forward-only_ version that executes only the forward loops in Algorithm 1, a _backward-only_ version that executes only the backward loops, and the _full_ version that performs both passes (forward+backward) as proposed.

We measure the fraction of pairs for which forward- only (or backward-only) matches the full solution in communication time and reachability. Any mismatch indicates that the omitted pass is necessary for discovering certain optimal path structures, consistent with the proof intuition in Lemmas 1-3.

## 6.6 Scalability Design: Full APSP vs. Pair Sampling at Mega-Constellation Scale

At mega-constellation scale (\(n\approx 2\times 10^4\)), the number of ordered pairs is _n(n_-1), which is too large for exhaustive path extraction and storage in experimental evaluation. Therefore, while we still construct temporal connectivity primitives over all satellites, we evaluate routing statistics using randomized sampling of ordered pairs.

Unless stated otherwise, we sample:

\(\bullet\) _N_<sub>pairs</sub>=50,000 distinct ordered pairs per _R_ for reachability and latency distributions, and<tbc>

\(\bullet\) _N_<sub>pairs</sub>=10,000 per _R_ for hop-count and waiting/traversal decomposition (requires path reconstruction).

We repeat each configuration _K_=5 times with different random seeds and report mean \(\pm\) standard deviation.

## 6.7 Metrics Reported (Directly Tied to Methodology)

We report the following metrics, each of which corresponds directly to quantities defined in Section 4:

\(\bullet\) Reachability ratio: fraction of pairs for which _P(p,q_) contains a valid tuple (not \((0,0,\infty)\)).<tbc>

\(\bullet\) Shortest communication time: \(\mathcal{T}_{pq}=(I_f^{pq}-I_s^{pq}+1)\tau\).<tbc>

\(\bullet\) Hop count: obtained by following predecessor pointers _pred<sup>pq</sup>_ backward to reconstruct the selected path.

