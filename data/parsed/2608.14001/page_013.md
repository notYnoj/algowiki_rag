<tbc>in the same way, meaning \(\kappa_1\neq\kappa_2\). We generate the \(\mathcal{A}_\unknown\)- eigenvectors in the same manner as in Case 1, but now for the observation function, we generate \(\mathbf{c}\in\mathbb{R}^n\) by letting \(\mathbf{c}=\sum_{j=1}^d((1+w_{2j-1})\Re(\mathbf{v}_j)+(1+w_{2j})\unknown(\mathbf{v}_j))\), with the \(\{w_j\}_{j=1}^{2d}\) being i.i.d. Gaussian random variables of mean 0 and variance 0.1. For each value \(\ell\), we generate \(\mathbf{h}=\sqrt{\frac{2d}{\ell}}\frac{\mathbf{c}}{\|\mathbf{c}\|_2}\) . Since each \(\{w_j\}_{j=1}^{2d}\) is of low variance, \(\frac{|\mathbf{v}_j^H\mathbf{h}|}{\|\mathbf{h}\|_2^2}\) is close to 1, in which case \(\kappa_1\) and \(\kappa_2\) are close to but typically not equal to 1. With _A_<sub>1</sub>=_A_<sub>2</sub> and \(\kappa_1\) and \(\kappa_2\) close to 1, \(\delta_0\) is small.

Figures 8, 9, 10 depict the results, and  II contains the parameters. Again, max{_Q_} and min{_Q_} do begin to converge to \(C(1\pm\delta_0)\) for each of the non-uniformly-sampled delay-coordinate maps, but because \(\kappa_1\neq\kappa_2\), there is a fundamental limit to the quality achievable to the time-delay embedding and it cannot achieve isometry. This confirms that increasing the lags \(\ell\) in the delay-coordinate map does improve the embedding quality, but up to a limit, an observation in agreement with Theorem 8. Again, the normal delay-coordinate map (8) outperforms maps with non-uniform delays, and there is no theoretical enveloping bound for a \(\delta_1(\ell)\) that could provide convergence guarantees.

## 6) Case 3 (Non-Ideal Dynamics and Non-Ideal Measurement):

Finally, we simulate the case when \(\delta_0\) may be larger, which is when \(A_1\neq A_2\) and \(\kappa_1\neq\kappa_2\). We use the same \(\mathcal{A}_\unknown\)- eigenvalues and the same **h** as in Case 1. For the attractor dynamics, we let \(\{\mathbf{v}_j\}=\frac{(\mathbf{a}_j+i\mathbf{b}_j)}{\sqrt{\|\mathbf{a}\|_2^2+\|\mathbf{b}\|_2^2}}\), where \(\{\mathbf{a}_j,\mathbf{b}_j\}\in\mathbb{R}^n\) are randomly-constructed vectors the entries of which are<tbc>

<tbc>normally-distributed with mean 0 and variance 1.

In this "non-ideal" setting, the results for which are shown in Figures 11, 12, 13, and the parameters for which are in  III, again the embedding is not isometric in the asymptotic case, although it could be improved by absorbing _C_ into \(\unknown\). Again, the unevenly-spaced delay-coordinate map quality converges to that of the evenly-spaced delay-coordinate map, and the variance of the empirical quality is low.

Given that the deterministic delay-coordinate map with<tbc>

\begin{tabular}{ccccc}
M-Dimension Index: _j_ & 1 & 2 & 3 & 4 \\
\(\theta_j\) & 2.5480 & 1.5158 & 1.6468 & 0.1489 \\
\(|\mathbf{v}_j^H\mathbf{h}|^2/\|\mathbf{h}\|_2^2\) & 1.0409 & 1.0547 & 0.9539 & 0.9654 \\
\(\lambda_j(\mathbf{V}^H\mathbf{V})\) & 1 & 1 & 1 & 1 \\
\end{tabular}

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
Number of Lags [t]
Min Max Q(x, y) (Standard)
Min Max Q(x, y) (Uniform Dist.)
C
Var Q(x, y) (Standard)
Var Q(x, y)
C(1 + 80)
Isometry
Minimal Embedding Dimension: 2d
C(1 - 80)

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
Number of Lags [t]
Min Max Q(x, y) (Standard)
Min Max Q(x, y) (Exponential Dist.)
C
Var Q(x, y) (Standard)
Var Q(x, y)
C(1 + 80)
Isometry
Minimal Embedding Dimension: 2d
C(1 - 80)

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
Number of Lags [t]
Min Max Q(x, y) (Standard)
Min Max Q(x, y) (Normal Dist.)
C
Var Q(x, y) (Standard)
Var Q(x, y)
C(1 + 80)
Isometry
Minimal Embedding Dimension: 2d
C(1 - 80)

TABLE II CASE 2

_A_<sub>1</sub>=1, _A_<sub>2</sub>=1, \(\kappa_1=0.9339\), \(\kappa_2=1.0547\), _C_=0.7886, \(\delta_0=0.1210\), and \(\nu=15.4879\).

Fig. 8. Numerical simulation of the conditioning of delay-coordinate maps with delays drawn uniformly from \([0,\ell]\) in the case when _A_<sub>1</sub>=_A_<sub>2</sub> and \(\kappa_1\neq\kappa_2\) (and thus \(\delta_0>0\)), with the deterministic delay-coordinate map with evenly-spaced delays as a reference and the bounds from Theorem 8. As \(\ell\) grows large, the random and deterministic maps approach isometry, and, although max{_Q_} and min{_Q_} can be large, var{_Q_} is still relatively small.

Fig. 9. The stability of non-uniform linear Takens’ embedding in the case where _A_<sub>1</sub>=_A_<sub>2</sub> but where \(\kappa_1\neq\kappa_2\) where the time delays adhere to an exponential distribution. Again, the non-deterministically-generated map performs poorer than its deterministic, evenly-spaced counterpart, but as \(\ell\rightarrow\infty\) they do begin to converge to the same asymptotic bounds. Again Var{_Q_} is comparably small to max{_Q_} and min{_Q_}, so most of the embedded attractor is isometric to the original attractor.

Fig. 10. Stability of non-uniform Linear Takens’ Embedding where time lags adhere to a normal distribution. Low variance

TABLE III CASE 3

_A_<sub>1</sub>=0.2790, _A_<sub>2</sub>=1.4294, \(\kappa_1=0.1888\), \(\kappa_2=0.6581\), _C_=0.7886, \(\delta_0=0.9684\), and \(\nu=15.4879\).

