with variance 1. In all cases we set

\(\mu=1,\sigma=1,c=0,\)

so that the centered variable is _W=X-c_. We evaluate both estimators over 100 logarithmically spaced sample sizes between 10 and 10<sup>7</sup>, and estimate the MAE

\(\mathbb{E}\big[|\hat{\mu}_n-\mu|\big]\)

by averaging over 1000 Monte Carlo repetitions.

## Bias-target calibration.

We use a common deterministic bias target<tbc>

\(b=0.1\)

<tbc>for both estimators. For our estimator, Theorem 5 contains the clipping-bias term \(\sigma^2/(2L)\), so we choose<tbc>

\(L=\frac{\sigma^2}{2b}.\)

<tbc>In the implementation of the baseline experiment, the \[21\] truncation parameter _t_ is calibrated to the same target _b_. With \(\sigma=1\) and _b_=0.1, this gives<tbc>

\(L=t=5.\)

## True bias computation.

Beyond the common nominal bias budget _b_, we also compute the exact deterministic bias induced by the chosen clipping/truncation level for each distribution. For our estimator, the true bias is<tbc>

\(B_\text{ours}:=\left|\mathbb{E}\big[[W]_L-W\big]\right|,\)

<tbc>where \[_W_\]_<sub>L</sub>_=max{-_L,_min{_W,L_}}. For the \[21\] estimator, the true bias is

\(B_\text{LS}:=\left|\mathbb{E}\big[W\mathbf{1}\{|W|<t\}\big]-\mathbb{E}[W]\right|=\left|\mathbb{E}\big[W\mathbf{1}\{|W|\ge t\}\big]\right|.\)

These quantities are evaluated from the known distribution in each environment and are plotted as horizontal reference lines in Figure 1 whenever they exceed 10<sup>-3</sup>.

## Discussion of the ratio plot.

Figure 3 highlights the MAE comparison more directly. In the pre-asymptotic regime, where neither estimator has yet reached its bias floor, the ratio is close to 2 across all three distributions. In other words, before bias dominates, the \[21\] estimator has roughly double the MAE of our estimator. As _n_ grows, the ratio increases further in the heavy-tailed and asymmetric cases because the larger true bias of the baseline causes its MAE to plateau earlier and at a higher level.

\begin{tabular}{ccc}
Distribution & _B_ours & _B_LS \\
Normal & \(7.15\times 10^{-6}\) & \(1.66\times 10^{-4}\) \\
Student-_t_(5) & \(1.56\times 10^{-3}\) & \(9.06\times 10^{-3}\) \\
Exponential & \(6.74\times 10^{-3}\) & \(4.04\times 10^{-2}\) \\
\end{tabular}

Normal
Student-t (df=5)
Exponential
6
4
MAE ratio
2
102
104
106
102
104
106
102
104
106
Samples n
Samples n
Samples n
MAE ratio (Lau-Scarlett / Ours)
Parity (ratio = 1)

1: True bias under the common theoretic bias target _b_=0.1.

Figure 3: Ratio MAE<sub>LS</sub>(_n)/_MAE<sub>ours</sub>(_n_) as a function of _n_. Values above 1 indicate that the \[21\] estimator has larger error.

