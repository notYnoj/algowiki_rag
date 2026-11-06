### VLM annotator.

We use Ollama-hosted Qwen-3.5 with _K_=5 simulated annotators per item providing pointwise quality scores via JSON-formatted prompts.

### Human oracle.

Following standard practice \[17,10\], we simulate the human oracle as \(h(i,j)=\mathbf{1}[s_i+\epsilon_i>s_j+\epsilon_j]\) where \(\epsilon\sim\mathcal{N}(0,25)\).

### Baselines.

We compare against five methods under identical total budget (\(n_\mathrm{cal}+T\times B=600\)): (1) **Random Elo**: random pair selection with Elo updates; (2) **Active Elo** \[8\]: Elo-gap-based active pair selection; (3) **Active Elo (same budget)**: Active Elo restricted to the same human budget as SGS; (4) **RAIR- Laplacian** \[12\]: Laplacian effective resistance pair selection; (5) **PairS-like MergeSort** \[10\]: PairS-style merge sort with VLM-gap-based uncertainty.

### Default hyperparameters.

All hyperparameters and their rationale are listed in  1; they are held fixed across all six datasets (no per-dataset tuning). The surprise weights (0.4,0.3,0.3) slightly favor the VLM-confidence term as the only signal available before any human label is collected; the sensitivity of the results to \(\theta_S\) and \(\alpha\) is examined in Section 4.5.

### 4.2 Main Results

### 4.3 Budget and Domain Analysis

s 2-3 show that SGS achieves the best average \(\tau\times 100\) (71.1), with the largest gains over Active Elo on LIVE-C (+12.5) and STS-B (+12.1). The improvement is not uniform: RAIR-Laplacian remains strongest on BIOSSES and SICKR-STS,<tbc>

\begin{tabular}{ccc}
Symbol & Value & Rationale \\
_n_<sub>cal</sub> & 100 & calibration pairs to estimate \(\alpha\) and seed Elo \\
\(T\times B\) & \(5\times 100\) & rounds \(\times\) per-round human budget \\
_K_ & 5 & VLM votes per item (pointwise) \\
(_w_<sub>vlm</sub>_,w_<sub>elo</sub>_,w_<sub>ent</sub>) & (0.4,0.3,0.3) & favor VLM term pre-labels; Elo/entropy equal \\
\(\theta_S\) & 0.55 & surprise cutoff for human routing (results are insensitive over \[0.4,0.75\], Sec. 4.5) \\
_k_<sub>inf</sub> & 0.0 & inferred pairs constrain order only, never update Elo \\
_C_<sub>max</sub> & 200 & cap on inferred comparisons per round \\
\(\alpha\)-gate & 0.70 & below this, disable backbone \(\rightarrow\) Active Elo \\
warm-start & 250, 0.5 & rating scale and calibration-blend weight \\
trust gaps & 50, 60 & min. Elo gap to infer / to order an unknown merge pair \\
\end{tabular}

** 1.** SGS hyperparameters, default values, and rationale. Values are fixed across all datasets; the Elo/merge trust gaps and warm-start constants follow the conventional Elo scale (400 points = 10\(\times\) odds).

