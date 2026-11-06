subject to the constraint _C_=6_ND_ described in Hoffmann et al. 2022, which is solved with values \(N_1^*\) and \(D_1^*\). We then perform the same optimization problem but with a budget constraint of 2_C_=6_ND_, yielding a corresponding cross entropy loss of _L_<sub>2</sub>. The reduction in cross entropy loss is given by \(\Delta L=L_2-L_1\le 0\).<tbc>

2. We then estimate the years of algorithmic progress that would be needed to achieve this same reduction \(\Delta L\). In particular, the optimization problem is<tbc>

\(min_{\delta\in\mathbb{R}^+}f(\delta),\) \(\text{(10)}\)

where we have<tbc>

\(f=\big|exp[\alpha'_\text{const}-\alpha_\text{year}(Y+\delta-Y_0)-\alpha_\text{param}log(N/N_0)]\)<br>
\(+exp[\beta'_\text{const}-\beta_\text{year}(Y+\delta-Y_0)-\beta_\text{data}log(D/D_0)]-L_2\big|\) \(\text{(11)}\)

. Here \(\delta\) can be interpreted as a doubling time for effective compute due to algorithmic progress in pre-training. \(\alpha'_\text{const}=\alpha_\text{const}+\alpha_\text{const,PTB}x_\text{PTB}+\alpha_\text{const,WT2}x_\text{WT2}\) and \(\beta'_\text{const}=\beta_\text{const}+\beta_\text{const,PTB}x_\text{PTB}+\beta_\text{const,WT2}x_\text{WT2}\), where _x_PTB and _x_WT2 are dummy variables for PTB and WT2 respectively.

We apply this approach over 100 bootstraps of our dataset, yielding a median doubling time of 8.6 months, and a 95% confidence interval of 4.5 to 14.5 months. This is very similar to the doubling times estimated using the closed-form approach discussed in section 3.1.

## H Irreducible loss

Our main model for estimating doubling times does not estimate the irreducible loss. This is in part due to empirical difficulties encountered in estimating plausible values for this term, and in part because the inclusion of this term does not have a bearing on our estimates of the rate of algorithmic improvements. Since the latter is the focus of our paper, we decided to move forward with the outlined model without irreducible loss estimates. However, we caution against overinterpretation of these results--for instance, our parameter estimates are not reliable enough to strongly inform how to scale models compute-optimally (although they can be somewhat illustrative).

The focus of this section is to justify the robustness of our core doubling time results to this omitted variable in our model. In particular, we fit a model which incorporates estimates of the irreducible loss and show that the doubling times remain in line with our previous findings. The model we consider is

\(\hat{L}=\gamma'+exp(\alpha'_\text{const}-\alpha_\text{year}(Y-Y_0)-\alpha_\text{param}logN/N_0)+exp(\beta'_\text{const}-\beta_\text{year}(Y-Y_0)-\beta_\text{data}logD/D_0),\) (12)

where \(\gamma'=\gamma+\gamma_{PTB}x_{PTB}+\gamma_{WT2}x_{WT2}\), and the rest of the model is defined in the same way as in Section 3.1. When we fit this model, we obtain a compute efficiency doubling time of 8.8 months, with a 95% confidence interval of 4.2 to 18.7 months, consistent with the estimates from our primary model. Our core parameter estimates are shown in  8.

\begin{tabular}{ccc}
 & Estimate & 95% CI \\
\(\alpha_\text{const}\) & 0.317

(0.336) & -0.000,1.395 \\
\(\alpha_\text{const,PTB}\) & 0.098

(0.079) & -0.033,0.220 \\
\(\alpha_\text{const,WT2}\) & 0.077

(0.158) & -0.071,0.569 \\
\(\alpha_\text{year}\) & -0.069

(0.033) & -0.107,0.022 \\
\(\alpha_\text{param}\) & 0.135<sup>∗</sup>

(0.026) & 0.073,0.186 \\
\(\beta_\text{const}\) & 1.373<sup>∗</sup>

(0.319) & 0.000,1.542 \\
\(\beta_\text{const,PTB}\) & 0.049

(0.105) & -0.034,0.339 \\
\(\beta_\text{const,WT2}\) & 0.100

(0.185) & -0.649,0.190 \\
\(\beta_\text{year}\) & 0.075

(0.026) & -0.003,0.103 \\
\(\beta_\text{data}\) & 0.024<sup>∗</sup>

(0.010) & 0.015,0.063 \\
\end{tabular}

\begin{tabular}{ccc}
 & Estimate & 95% CI \\
\(\alpha_\text{const}\) & 0.930

(0.340) & -0.000,1.357 \\
\(\alpha_\text{const,PTB}\) & 0.000

(0.074) & -0.088,0.137 \\
\(\alpha_\text{const,WT2}\) & 0.143

(0.130) & -0.001,0.589 \\
\(\alpha_\text{year}\) & -0.012

(0.031) & -0.097,0.027 \\
\(\alpha_\text{param}\) & 0.081<sup>∗</sup>

(0.027) & 0.060,0.165 \\
\(\beta_\text{const}\) & 0.826<sup>∗</sup>

(0.331) & 0.000,1.432 \\
\(\beta_\text{const,PTB}\) & 0.176

(0.129) & -0.003,0.401 \\
\(\beta_\text{const,WT2}\) & -0.001

(0.211) & -0.756,0.281 \\
\(\beta_\text{year}\) & 0.062<sup>∗</sup>

(0.028) & -0.006,0.111 \\
\(\beta_\text{data}\) & 0.036

(0.013) & 0.016,0.060 \\
\end{tabular}

6: _D_= tokens seen.

7: _D_= tokens seen with diminishing returns.

Parameter estimates from the model described in equation 8, to 3 decimal places. We report 95% confidence intervals for all of the parameter estimates by bootstrapping 100 iterations. \* corresponds to a p value below 5%.

