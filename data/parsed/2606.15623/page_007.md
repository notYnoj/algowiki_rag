### 3.5 Composite Surprise Score

The surprise score estimates the risk of resolving a pair without a human label. For each candidate pair (_i,j_), SGS computes three normalized uncertainty signals. First, forward and reverse VLM queries yield a position-bias-cancelled preference estimate,<tbc>

\(p_\text{fwd}=\frac{\mu_i^\rightarrow}{\mu_i^\rightarrow+\mu_j^\rightarrow+\varepsilon},p_\text{rev}=\frac{\mu_i^\leftarrow}{\mu_i^\leftarrow+\mu_j^\leftarrow+\varepsilon},\hat{p}_{ij}=\frac{p_\text{fwd}+p_\text{rev}}{2},\) (6)

<tbc>which is converted to VLM uncertainty \(S_\text{vlm}(i,j)=1-2|\hat{p}_{ij}-0.5|\). Second, the Elo gap \(\Delta_{ij}=|R_i-R_j|\) is mapped to<tbc>

\(S_\text{elo}(i,j)=1-2\left(\frac{1}{1+10^{-\Delta_{ij}/400}}-0.5\right).\) (7)

<tbc>Third, vote entropy _S_ent is computed from the _K_ simulated VLM votes. The final score is

\(S(i,j)=w_\text{vlm}S_\text{vlm}(i,j)+w_\text{elo}S_\text{elo}(i,j)+w_\text{ent}S_\text{ent}(i,j),\) (8)

with default weights (0.4,0.3,0.3).

### 3.6 Budget Allocation and Capped Automatic Resolution

At round _t_, the scheduler returns cross-run candidates whose outcomes are not already implied by transitivity. If more than 3_B_ unknown candidates are visible, SGS subsamples at most 3_B_ for surprise scoring, keeping VLM query cost linear in the round budget. The scored candidates are sorted by decreasing surprise. Pairs with \(S(i,j)\ge\theta_S\) are routed to the human oracle up to budget _B_; if fewer than _B_ pairs clear the threshold, the remaining budget is filled by the next most surprising pairs.

Low-surprise pairs are not automatically trusted wholesale. They are merely eligible for capped automatic resolution, with the cap reduced in later merge passes and under lower observed agreement:

\(C_t=max\left(20\cdot\mathbf{1}[\gamma_t>0],\text{round}(C_\text{max}\gamma_t)\right),\gamma_t=(1-0.7p_t)\big((1-\omega)+\omega\tilde{a}_t\big),\) (9)

where _p<sub>t</sub>_ is normalized merge-pass progress and \(\tilde{a}_t\) combines Round-0 agreement with the previous round’s human agreement. For an admitted pair, SGS uses Elo only when the rating gap is sufficiently informative (default \(|R_i-R_j|\ge 50\)). If VLM reliability is low, scheduler-order fallback is disabled and only high- confidence Elo decisions can support automatic resolution. In the reported experiments, inferred edges use _k_inf=0: they constrain pass completion and the transitive closure, but never update Elo, which is updated exclusively from human labels.

