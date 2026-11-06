the criterion is the squared-error loss of the whole covariance matrix for a single sample, the projection-based estimator can be preferable, as it was in all nine settings considered here.

The relative RMSE values are large for all three estimators, especially in the GEV-copula design, where they range from 2.0 to 2.9; values above one also occur in the independent design for \(n\le 30\). This reflects the intrinsic difficulty of estimating a covariance matrix of L-comoments from one small sample: each entry of \(\widetilde{C}_n\) is a second moment of the moment vector, so its sampling variability depends on fourth moments of the data. For GEV margins with shape \(\xi\), the fourth moment is finite only when \(\xi<1/4\), so \(\xi=0.2\) lies close to this boundary, and the estimators have heavy-tailed sampling distributions whose occasional large values dominate the mean squared error. The RMSE decreases with _n_ in every design, and the ranking of the estimators is the same as under lighter tails. In heavy-tailed applications, covariance estimates from samples of this size should therefore be interpreted with caution.

## 6.4 Scaling of the fast algorithm

1 is limited to \(n\le 50\) because the direct method becomes impractical for larger samples. To examine the growth of the fast algorithm alone,  4 reports elapsed times of a vectorized NumPy implementation of Proposition 5.1 for _n_ up to 4000; each time is the median of five measurements (\(n\le 1000\)) or three measurements (\(n\ge 2000\)).

The least-squares slope of log time on log _n_ is 2.18 for \(100\le n\le 1000\) and 2.26 over all sizes, close to the quadratic arithmetic complexity established in Proposition 5.1. The slight excess at the largest sizes reflects memory traffic in the large prefix tables. The six prefix tables require 48(_n_+1)<sup>2</sup> bytes, about 46MB at _n_=1000 and 0.73GB at _n_=4000. The vectorized implementation also stores pair-level quantities, and its peak memory use was about 4.9GB at _n_=4000; a loop over pairs, as in the R implementation, avoids this pair-level storage. The algorithm is therefore practical well beyond the record lengths typical of L-moment applications, whereas direct enumeration is already slow at _n_=50.

\begin{tabular}{ccccccc}
_n_ & 100 & 200 & 500 & 1000 & 2000 & 4000 \\
Time (s) & 0.010 & 0.047 & 0.336 & 1.543 & 8.489 & 44.02 \\
Prefix tables (MB) & 0.5 & 1.8 & 11.5 & 45.9 & 183.3 & 732.8 \\
\end{tabular}

4: Elapsed time of the fast algorithm for the full \(8\times 8\) unbiased covariance matrix (vectorized NumPy implementation).

