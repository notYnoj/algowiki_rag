## C Trajectory Analysis Detail

6 reports quantitative trajectory divergence metrics across subsets. All metrics are computed over paired queries where both architectures produced a scorable response.

## D Tool Selection Divergence

7 shows tool selection divergence between RtP and PtR across all subsets. Divergence increases monotonically with query complexity, reaching 100% on G3, where the two architectures retrieve from entirely non-overlapping API sets for every query.

When tools diverge, the recall-win pattern flips: RtP wins on 63 G1 queries vs. PtR’s 33 (mean recall 0.369 vs. 0.294), but PtR wins on 69 G2 queries vs. RtP’s 30 (mean recall 0.184 vs. 0.142).

## E Inference Cost Analysis

8 quantifies PtR’s token overhead against its recall benefit. PtR’s discovery call adds ∼175-200 output tokens per query. On G1 this overhead hurts (higher cost, lower recall). On G2 it is well justified (+0.042 recall for +80% tokens).

\begin{tabular}{ccccc}
**Metric** & **Arch.** & **G1** & **G2** & **G3** \\
\multirow{2}{*}{Selection rate} & PtR & 28.6% & 28.2% & 26.8% \\
 & RtP & 26.7% & 21.2% & 22.4% \\
Jaccard (selected) & both & 0.40 & 0.29 & 0.28 \\
\multirow{2}{*}{Plan steps} & PtR & 3.8 & 3.9 & 4.1 \\
 & RtP & 3.5 & 3.7 & 3.6 \\
\multirow{2}{*}{Fidelity} & PtR & 98.8% & 97.8% & 98.5% \\
 & RtP & 96.6% & 97.3% & 100% \\
\multirow{2}{*}{Refusal on miss} & PtR & 26% & 27% & 33% \\
 & RtP & 28% & 47% & 40% \\
\end{tabular}

\begin{tabular}{cccc}
**Subset** & _n_ & **Identical** & **Divergent** \\
G1 & 200 & 2.5% & 97.5% \\
G2 & 200 & 1.0% & 99.0% \\
G3 & 100 & 0.0% & 100.0% \\
\end{tabular}

\begin{tabular}{ccccc}
 & **RtP** & **PtR** & **Overhead** & \(\Delta\)R \\
G1 & ∼226 & ∼396 & +75% & -0.072 \\
G2 & ∼238 & ∼429 & +80% & +0.042 \\
G3 & ∼221 & ∼450 & +104% & +0.017 \\
\end{tabular}

** 6** Trajectory divergence metrics. Selection rate = fraction of retrieved APIs the planner uses. Jaccard = similarity of planner-selected API sets. Fidelity = fraction of planner selections drawn from the retrieved set.

** 7** Tool selection divergence: fraction of queries where the two architectures retrieve different top-_k_ API sets.

** 8** Inference cost and recall benefit of PtR over RtP. The sign of \(\Delta\)R matches the crossover in  3, where the G1 and G2 recall differences are statistically significant (_p\<_0.01) and G3 is not.

