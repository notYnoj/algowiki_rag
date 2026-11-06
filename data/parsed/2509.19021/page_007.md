- **Stage 3 (Termination):** Incurs a variable cost but offers no further savings, as there is no subsequent round to benefit from a partition.<tbc>

- **Stage 2 (The Core):** This is the exclusive window for optimization. The cost of partitioning in round _r_ is amortized only if it reduces the sorting workload in round _r_+1.

Consequently, if the total number of rounds \(R\le 2\), the "Optimization Window" (Stage 2) is effectively empty. In such cases, SP-LSD incurs the overhead of Stage 1 and Stage 3 without any intermediate rounds to realize the gain from partitioning. Therefore, a structural prerequisite for SP-LSD viability is the existence of at least one intermediate round, implying _R\>_2, from this we arrive to our crossover, namely **Round-feasibility Crossover** (_k\>n_<sup>2</sup>). Accordingly, our analytical results and viability tables presented in the subsequent sections begin evaluation at _R_=3.

### 5.4 Case 1: Conservative Skew Model

We first derive the condition for datasets exhibiting heavy tail skew. We adopt a conservative assumption where effective pruning occurs in the first partition (Round 2), reducing the active set to (1-_p)n_. For the remainder of Stage 2 and Stage 3, we conservatively assume the active region does not shrink further.

**Cost Derivation:**

- **Stage 1 (Round 1):** Perform sorting on the mod values of the entire array, no partitioning required. \(\mathrm{Cost}_{\mathrm{Stage}1}=\alpha\cdot n\)<tbc>

**-** **Stage 2 (Rounds** 2_...R_-1**):** Perform partitioning and sort the active region iteratively. Note that the partition in Round 2 acts on the full array size _n_ to identify zeros, while subsequent operations act on the reduced active set (1-_p)n_.<tbc>

\(\bullet\) Round 2 Cost: \(\beta\cdot n\) (full partition) + \(\alpha(1-p)n\) (partial sort).<tbc>

\(\bullet\) Rounds 3_...R_-1 Cost: Total of _R_-3 rounds (excluding the first two rounds and the last round _R_) involving both partitioning and sorting on the active set. Cost: \((R-3)(\alpha+\beta)(1-p)n\).<tbc>

<tbc>\(\mathrm{Cost}_{\mathrm{Stage}2}=\beta n+\alpha(1-p)n+(R-3)(\alpha+\beta)(1-p)n\).<tbc>

**-** **Stage 3 (Round _R_):** Perform sorting on the final active region, no partitioning required. \(\mathrm{Cost}_{\mathrm{Stage}3}=\alpha(1-p)n\).

**Total Cost Equation:** Summing Stage 1 with the combined costs of Stage 2 and 3: \(T_\mathrm{SP-LSD}^\mathrm{skewed}=n[(\alpha+\beta)+[(R-1)\alpha+(R-3)\beta](1-p)]\).

**Break-Even Analysis:** We compare this against standard BNRS (\(T_\mathrm{BNRS}=R\cdot\alpha\cdot n\)). Substituting \(\alpha=c\beta\), and cancelling the common terms _n_ and \(\beta\):

\((c+1)+[c(R-1)+(R-3)](1-p)<Rc\)<br>
\([c(R-1)+(R-3)](1-p)<Rc-c-1\)<br>
\(1-p<\frac{c(R-1)-1}{c(R-1)+(R-3)}\)

