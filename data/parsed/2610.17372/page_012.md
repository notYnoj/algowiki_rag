<tbc>_R_, _t<sub>pq</sub>_) are logged to enable exact reproduction.

All sampled-pair experiments use fixed seeds per trial. We report mean and standard deviation over _K_=5 trials to capture sampling variance and runtime variability.

## 7 RESULTS

This section reports results in the same order as the validations defined in Section 6, and in direct correspondence with the methodology in Section 4. Recall that (i) the temporal graph is represented by snapshot-wise edge sets encoded as connectivity strings \(CS_{pq}^{(R)}\), (ii) a hop (_q,r_) is admissible only if there exists a _future_ contiguous run of ones of length \(\ge t_{qr}\) in \(CS_{qr}^{(R)}\) (Procedure 1), and (iii) the algorithm returns for each ordered pair (_p,q_) a shortest communication-time tuple \((I_s^{pq},I_f^{pq},pred^{pq})\) (Algorithm 1) from which the end-to-end time is \(\mathcal{T}_{pq}=(I_f^{pq}-I_s^{pq}+1)\tau\). We first validate the temporal connectivity primitives (including % links found/missing), then validate correctness via baseline comparison, then report performance (run- time/memory/scaling), and finally connect temporal contact structure to waiting-vs-traversal behavior in shortest- time paths.

### 7.1 Methodology-to-Metrics Mapping

For a given range threshold _R_, let \(E_t^{(R)}\) denote the set of feasible inter-satellite links at snapshot _t_:

\(E_t^{(R)}=\{(p,q)|CS_{pq}^{(R)}[t]=1\},t\in\{1,\dots,M\}.\) (6)

This snapshot-based temporal representation is standard in temporal-network modeling \[30\], \[31\]. Algorithm 1 produces a path matrix _P_ whose entry _P(p,q_) stores the selected shortest communication-time contact tuple \((I_s^{pq},I_f^{pq},pred^{pq})\) after Procedure 4. We compute:

\(\bullet\) Shortest communication time: \(\mathcal{T}_{pq}=(I_f^{pq}-I_s^{pq}+1)\tau\).<tbc>

\(\bullet\) Hop count _H_: recovered by following predecessor pointers _pred<sup>pq</sup>_ backward.<tbc>

\(\bullet\) Traversal time: \(T_\mathrm{trav}=\sum_\mathrm{hops}t_{uv}\tau\).<tbc>

\(\bullet\) Waiting time: _T_<sub>wait</sub>=T_<sub>pq</sub>-T_<sub>trav</sub> and waiting fraction _f<sub>w</sub>=T_<sub>wait</sub>/T_<sub>pq</sub>_.

These metrics align exactly with the admissibility and tuple- composition rules in Section 4.

### 7.2 Validation 1: Temporal Connectivity Dynamics and Link Churn (Percentage Found / Percentage Missing)

We first validate that the temporal adjacency varies substantially over time, and quantify _how much_ connectivity changes between consecutive snapshots. Figures 4 and 5 show a focus satellite (S7) and its neighborhood across four consecutive snapshots, visually demonstrating link appearance/disappearance at short timescales. Space-time / snapshot modeling is widely used in satellite-network topology analysis \[33\], \[34\].

4 quantifies neighborhood churn for the focus node via persistent/new/dropped neighbors and Jaccard similarity. High turnover indicates that a packet arriving at an intermediate satellite often encounters a different set of outgoing options than existed one snapshot earlier, increasing the probability of waiting for a future admissible run.

To quantify link volatility at the constellation scale, we define the _found_ (new) and _missing_ (dropped) link sets between consecutive snapshots:

\(E_\mathrm{found}^{(R)}(t)=E_t^{(R)}\backslash E_{t-1}^{(R)},\) (7)

\(E_\mathrm{missing}^{(R)}(t)=E_{t-1}^{(R)}\backslash E_t^{(R)}.\) (8)

We then report the corresponding percentages:

\(\%\mathrm{Found}(t)=100\cdot\frac{|E_\mathrm{found}^{(R)}(t)|}{|E_{t-1}^{(R)}|+\epsilon},\) (9)

\(\%\mathrm{Missing}(t)=100\cdot\frac{|E_\mathrm{missing}^{(R)}(t)|}{|E_{t-1}^{(R)}|+\epsilon},\) (10)

where \(\epsilon\) is a small constant used only to avoid division- by-zero in extremely sparse snapshots. These churn and similarity summaries are commonly used to characterize temporal adjacency dynamics \[30\], \[31\].  5 summarizes these churn percentages over one orbit; as expected, smaller _R_ yields higher churn and therefore more waiting- dominated routing.

### 7.3 Validation 2: Connectivity Strings Capture Contact Runs (Run-Length View)

The algorithm’s admissibility check (Procedure 1) is based on contiguous runs of ones in \(CS_{pq}^{(R)}\). Temporal-path feasibility under time-respecting constraints is a core concept in temporal graphs \[32\], \[30\]. Consequently, if connectivity is fragmented, a packet may arrive during a "0" period or within a run shorter than _tpq_ and must wait until a sufficiently long run appears.

6 summarizes run and gap statistics that directly determine how far forward Procedure 1 must search to find an admissible hop.

Connectivity strings CSfocus,neighbor(t) (1=contact feasible) 0
1.0 19 0.8 38 0.6 Time into orbit (minutes) Contact feasibility 57 0.4 76 0.2 96 0.0 1
6 11 16 22 Neighbor index (22 nearest satellites)

Fig. 6. Connectivity-string heatmap for a focus satellite and neighbors. The heatmap shows _CS_<sub>focus_,u_</sub>(_t_) over one orbital period for the same 23-satellite neighborhood used in Fig. 5. Long runs of ones correspond to sustained feasibility windows; fragmented patterns indicate contact- limited regimes that incur waiting to satisfy the run-length constraint _t<sub>qr</sub>_.

