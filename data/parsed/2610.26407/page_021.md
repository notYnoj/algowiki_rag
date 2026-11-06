et al. (2013) designed specifically for fixed-budget top-_k_ identification with batched sampling. We consider the Gaussian and Bernoulli families with \(I\in\{20,50,100\}\), _k=_5, and the middle column of  1. Since BatchSAR’s schedule depends on the total budget, we cannot run it with a large budget and read off its performance at every point along the way, so we fix a budget of 50\(\cdot I\) and consider batch sizes of 1%, 2%, 5%, and 10% of the budget. Figure 7 plots PCS, the objective BatchSAR is designed to maximize. Not only does TEAk have a higher PCS at the smallest batch size, but it also decreases less as the batch size grows: from batches of 1% to 10% of the budget, its PCS falls by up to 12%, and BatchSAR’s by up to 29%.

## 6. Discussion

We give a simple and interpretable algorithm for top-_k_ selection that accommodates batching in a principled way and can be applied to a wide range of sampling distribution families. We prove that it is consistent and that with the threshold _q_<sup>†</sup>(_t_), its posterior convergence rate is at least half of the best rate achievable by any sampling rule. In simulation, it is competitive with the state-of-the-art methods across likelihood families, problem sizes, values of _k_, and batch sizes.

## References

Audibert JY, Bubeck S, Munos R (2010) Best arm identification in multi-armed bandits. _Proceedings of the 23rd Conference on Learning Theory (COLT)_.

Bubeck S, Wang T, Viswanathan N (2013) Multiple identifications in multi-armed bandits. _Proceedings of the 30th International Conference on Machine Learning (ICML)_, 258-265.

TEAk TEAk-q (t) BatchSAR Gaussian, = = = = = = = = = = 0.63 0.38 0.19 0.62 0.36 0.18 0.17 0.61 0.34 0.16 PCS 0.60 0.15 0.59 0.32 0.14 0.58 0.30 0.13 1% 2% 5% 10% 1% 2% 5% 10% 0.12 1% 2% 5% 10% Bernoulli, = = = Bernoulli, = = = 0.41 0.19 0.065 0.40 0.18 0.060 0.39 0.17 0.38 0.16 0.055 PCS 0.37 0.15 0.050 0.36 0.14 0.35 0.14 0.045 0.34 0.13 1% 2% 5% 10% 1% 2% 5% 10% 1% 2% 5% batch size as % of budget batch size as % of budget batch size as % of budget

**Figure 7** PCS at the final budget of 50\(\cdot I\) against the batch size for the Gaussian (top) and Bernoulli (bottom) families with _k=_5.

