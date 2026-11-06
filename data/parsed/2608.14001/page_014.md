<tbc>uniformly-spaced delays seems to empirically lower and upper bound the maximal and minimal values of the embedding quality _Q_ for the maps of non-uniformly-spaced delays, a few natural questions are: whether uniform-sampling tends to outperform non-uniform sampling schemes and in what kinds of applications and settings; or whether a better basis of forming delay-coordinate maps with non-uniform delays is needed to have a more suitable comparison to the uniform counterparts. Another important question would be whether it is possible to establish estimates for an enveloping bound for the conditioning \(\delta_1(\ell)\) so as to be able to offer guarantees of convergence and estimates of the rate of convergence.

## IV. CONCLUSIONS

We considered delay-coordinate maps constructed using unevenly-spaced time delays for linear systems evolving on their attractors and established that they can form stable embeddings. To analyze the temporal component of the embeddings, we considered generalized Vandermonde matrices with distinct but unevenly-spaced powers (14). Just as having a distinct set of points and a distinct set of evenly-spaced integer powers are sufficient conditions for typical Vandermonde matrices (10) to be full column rank when the number of lags exceeds the number of points, so too should having a distinct set of points and a distinct set of powers be sufficient for Vandermonde matrices with unevenly-spaced powers to be full column rank, but perhaps with the caveat that the statement would be one of high probability rather than a deterministic one. As an initial step to confirm this, we proved theoretical results for when the number of time-delays \(\ell\) is small and for the asymptotic regime as \(\ell\rightarrow\infty\); we also provided empirical support for when such matrices are full rank. Rigorously proving the conjecture that generalized Vandermonde matrices are full rank does remain an open problem, yet the results for the base cases, for the asymptotic case, and from the numerical simulations all support the proposition.

If generalized Fourier Vandermonde matrices with unevenly-spaced powers are full column rank with probability one if the system frequencies and time samples are distinct, then the theorems we proposed for the existence of stable embeddings using delay-coordinate maps of unevenly-spaced lags and for the explicit asymptotic bounds of the embedding stability hold true. In the asymptotic regime where \(\ell\rightarrow\infty\), the embedding quality of the delay-coordinate map generated for each of the chosen random time-sampling schemes converged to the same limiting asymptotic bound as that of the deterministic, uniformly-sampled delay-coordinate map. This is to be expected in the linear setting, since, as shown in the deterministic case, the limiting behavior is dependent not on the number of time lags, but exclusively on the coordinates<tbc>

2.00
1.75
1.50
Empirical Embedding Quality
1.25
1.00
0.75
0.50
0.25
0.00
0
100
200
300
400
500
Number of Lags [f]
Min Max Q(x, y) (Standard)
Min Max Q(x, y) (Uniform Dist.)
C
Var Q(x, y) (Standard)
Var Q(x, y)
C(1 + 60)
Isometry
Minimal Embedding Dimension: 2d
C(1 - 60)

2.5
2.0
Empirical Embedding Quality
1.5
1.0
0.5
0.0
0
100
200
300
400
500
Number of Lags [f]
Min Max Q(x, y) (Standard)
Min Max Q(x, y) (Exponential Dist.)
Var Q(x, y) (Standard)
Var Q(x, y)
C(1 + 60)
Isometry
Minimal Embedding Dimension: 2d
C(1 - 60)

2.00
1.75
1.50
Empirical Embedding Quality
1.25
1.00
0.75
0.50
0.25
0.00
0
100
200
300
400
500
Number of Lags [f]
Min Max Q(x, y) (Standard)
Min Max Q(x, y) (Normal Dist.)
C
Var Q(x, y) (Standard)
Var Q(x, y)
C(1 + 60)
Isometry
Minimal Embedding Dimension: 2d
C(1 - 60)

Fig. 11. Simulation of the conditioning of delay-coordinate maps with delays drawn uniformly from \([0,\ell]\) when \(A_1\neq A_2\) and \(\kappa_1\neq\kappa_2\) (\(\delta_0>0\)). The deterministic map with evenly-spaced delays acts as a reference, and the theoretical bounds of Theorem 8 are plotted. The unevenly-sampled delay- coordinate map conditioning converges to the evenly-spaced case, with the normal mapping consistently outperforming it. The empirical lower bound converges to \(1-\delta_0\), but the upper bound is not tight. Without scaling by absorbing _C_ into \(\unknown\), the delay-coordinate map cannot be an isometric embedding. While the maximum and minimum quality range widely, the variance is small.

Fig. 12. A numerical simulation similar to that of Figure 11, with \(A_1\neq A_2\) and \(\kappa_1\neq\kappa_2\), except that the time lags used for the non-uniform delay- coordinate map are drawn from an exponential distribution. The embedding quality performs similarly to the map with deterministic, uniformly-spaced delays, as well as with the map with unevenly-spaced delays drawn uniformly.

Fig. 13. A numerical simulation like that of Figure 11, but now with delays drawn from a normal distribution. Again, because the eigenvectors of the underlying system are of differing magnitudes, and the difference of the magnitudes in the observed states varies greatly, the quality of the embedding is poor, yet it does not become singular.

