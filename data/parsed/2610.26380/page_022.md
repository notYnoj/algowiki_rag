<tbc>Using these scores, the batch-building procedure is given in Algorithm 4. We consider elastic round budgets, meaning that as long as some budget remains in the current round, the algorithm may choose any evaluation provided it satisfies the total budget constraint. If its cost exceeds the remaining round budget, the excess is deducted from the next round’s budget. This ensures that the knapsack nature of the round budget does not bias the choice of evaluation type.

**Algorithm 4** Surrogate batch allocation

**Input:** \(\mu_{t-1}\), \(\Sigma_{t-1}\), round budget _B<sub>t</sub>_, remaining total budget _R_<sub>rem</sub> (initially _R_), and excess from the previous round (initially zero)<br>
\(B_\mathrm{rem}\leftarrow B_t-\mathrm{excess}\)<br>
\(n\leftarrow 0,\Sigma'_t(0)\leftarrow\Sigma_{t-1}\)<br>
Compute (_q<sub>t</sub>,b<sub>t</sub>_)<br>
while B<sub>rem</sub>\>0 and \(R_\mathrm{rem}\ge\mathrm{min}(r_0,r_1)\)<br>
   Compute \(\psi_{t,ij}(n)\) by (13) for all \((i,j)\in\mathcal{I}\) with \(r_j\le R_\mathrm{rem}\)<br>
   Choose \((i,j)\in\mathrm{argmax}_{(i,j)\in\mathcal{I}:r_j\le R_\mathrm{rem}}\psi_{t,ij}(n)\)<br>
   Update the covariance from \(\Sigma'_t(n)\) to \(\Sigma'_t(n+F^{ij})\) by (12)<br>
   \(n\leftarrow n+F^{ij}\)<br>
   \(B_\mathrm{rem}\leftarrow B_\mathrm{rem}-r_j,R_\mathrm{rem}\leftarrow R_\mathrm{rem}-r_j\)<br>
   excess \(\leftarrow\mathrm{max}\{0,-B_\mathrm{rem}\}\)<br>
return n(t)=n, R<sub>rem</sub>, and excess

## 6.2. The batched endgame

Extending the KG algorithm to batches introduces two computational difficulties. First, it optimizes over possible batch allocations, which we address through sequential batch construction, as in §6.1. Second, computing the myopic value of a given batch requires the outcome probabilities and posterior means for every possible combination of batch outcomes. We derive explicit expressions for these quantities given a batch outcome (analogous to Lemma 3), but they involve multivariate normal CDFs whose dimension grows with the batch size, making them expensive to evaluate numerically (Genz and Bretz 2009). Moreover, a batch of _U_ evaluations has 2_<sup>U</sup>_ possible outcomes, each requiring these calculations.

The computational difficulty comes from considering all the ways the evaluations in a batch can jointly move the posterior means. We instead approximate the myopic value of a batch by decomposing it into the myopic values of sub-batches of at most _w_ evaluations. This retains interaction effects among up to _w_ evaluations while keeping the computation tractable: the value of each sub-batch requires normal CDFs of dimension at most _w_ and a sum over at most 2_<sup>w</sup>_ outcomes. Because the details are technical and not the focus of this paper, we leave the full decomposition and batch construction procedure, along with additional details on surrogate batch allocation, to the Appendix.

## 7. Numerical experiments

The numerical experiments serve two purposes: to illustrate what the algorithm does, which supplements the insights from the analysis, and to investigate how well it performs. §7.2 serves the first, showing how evaluations are allocated as we learn more, how the mix of ratings and comparisons shifts over the budget,<tbc>

