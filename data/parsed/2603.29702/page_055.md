The full recursion is as follows:<tbc>

\(\widehat{\text{ans}}[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\text{ew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{max}_{\widehat{Y}\in\text{\unknown}}\sum_{i=1}^M\widehat{\text{ans}}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{if}s\notin\widetilde{S} \\
\sum_{i=1}^M\widehat{\text{ans}}[m_{i-1},\overline{y_i},m_i,\overline{y_i}], & \text{if}s\in\widetilde{S}
\end{array}\right..\)

<tbc>Unfortunately, this scheme still queries too many edge weights. The key to efficiency is to use a _sub- sampling_ technique for active scales. We first show a native attempt that can guarantee a small additive error (we later improve it to also obtain a bound on the multiplicative error). Notice that if \(s\in\widetilde{S}\), since no overfitting can happen when the path is fixed, we can just sample half of these values and double our sum from the sample. Thus, for every scale-_s_ interval (_l,r_\], we first uniformly randomly sample _M_0-1 variables \(\eta_{l,r,1\dots M}\) containing exactly _M/_21’s. We use the following scheme:

\(\text{est}^*[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\text{ew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{max}_{\widehat{Y}\in\text{\unknown}}\sum_{i=1}^M\text{est}^*[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{if}s\notin\widetilde{S} \\
2\sum_{i=1}^M\eta_{l,r,i}\text{est}^*[m_{i-1},\overline{y_i},m_i,\overline{y_i}], & \text{if}s\in\widetilde{S}
\end{array}\right..\) (31)

Note that for every active scale, half of the sub-intervals (_m_<sub>_i_-1</sub>_,m<sub>i</sub>_\] for which \(\eta_{l,r,i}=0\) get discarded. Over \(\left|\widetilde{S}\right|\) active scales, only \(2^{-\left|\widetilde{S}\right|}\) fraction of the intervals remain, which is a significant speed-up.

Unfortunately, the scheme with (31) is not enough for a small multiplicative error, as \(\text{est}^*[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\) may be imbalanced over \(1\le i\le M\). In the most extreme example, if \(\text{est}^*[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\neq 0\) for only a single _outlier i_, then (31) either gets us an estimate that is 0 or an estimate that is twice the actual value, depending on the value of \(\eta_{l,r,i}\).

Due to the bound on tree total deviation, the weight distribution on the longest path should intuitively not be imbalanced everywhere and there are not too many outliers in total. Thus we can afford to have some large error when there are outliers.

However, if our estimator consistently overestimates the answer (by a large factor) when there is an outlier, a path can overfit our estimator by specifically aiming for the regions that contain a large number of outliers. This means that our estimator has to remain sound (i.e., does not overestimate) even at the presence of outliers. To do this, we clip down the values of the outliers before obtainin our estimate. Given a non- negative sequence _A_=(_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>M</sub>_), we design a way to approximate \(\sum_ia_i\) when no _a<sub>i</sub>_ is too large compared to the mean of _A_ using the clipping idea above:

**Claim 7.8.** _Let A_=(_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>M</sub>_) _be a sequence of non-negative numbers. Suppose that we only know A<sub>I</sub>, that is, the sub-sequence_ \((a_i)_{i\in I}\) _for a uniformly randomly chosen subset_ \(I\subset[M]\) _of M/_2 _indices._

_We obtain a non-negative estimate EstSum(A<sub>I</sub>_) _for the sum_ \(\sum_{i=1}^Ma_i\) _in the following way:_

1. _Estimate the mean of A using_ \(\widetilde{A}:=\sum_{i\in I}a_i/\left(\frac{M}{2}\right)\);<tbc>

_2._ _Estimate the sum of A by clipping outliers down:_ \(\text{\textit{EstSum}}(A_I):=2\sum_{i\in I}\mathrm{min}\left(a_i,2\mathrm{log}^{0.02}\left(n\right)\widetilde{A}\right)\).

_The pseudocode for computing EstSum(A<sub>I</sub>_) _is shown in Algorithm 2._

_Then with probability_ \(1-\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\)_, the estimate we obtain satisfies_

