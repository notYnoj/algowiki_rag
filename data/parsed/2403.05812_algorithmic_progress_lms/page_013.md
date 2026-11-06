obtained under the Kaplan scaling law. The Compute-Equivalent Gain (CEG) was subsequently determined as the ratio of the original compute budget to the compute required by the Chinchilla scaling to match the Kaplan loss.

We find that the compute equivalent multiplier from the Chinchilla scaling laws for dense autoregressive transformer models is between 1.75-fold (for GPT-2 scale models) and 4-fold (for PaLM-scale models Chowdhery et al. 2023).<sup>10</sup>

## C Core model parameter estimates

The core model that we use was chosen based on leave-one-out cross validation, and is defined similarly to equation 3 but with a few modifications. The most important change is that _A_ and _B_ are estimated separately for each benchmark, whereas all other parameters are benchmark-agnostic. In order to help with model fitting, we normalize _N_ and _D_ to some minimum _N_<sub>0</sub> and _D_<sub>0</sub> values in our dataset, and reparameterize _A_ and _B_ as exponentials. In full, our model is

\(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}\mathrm{log}(N/N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}\mathrm{log}(D/D_0)],\) (8)

To estimate these in benchmark-specific fashion, we introduce dummy variables _x_<sub>WT2</sub> and _x_<sub>PTB</sub> for WT2 and PTB respectively. We then complete the model definition as follows:

\(\alpha'_\mathrm{const}=\alpha_\mathrm{const}+\alpha_\mathrm{const,PTB}x_\mathrm{PTB}+\alpha_\mathrm{const,WT2}x_\mathrm{WT2},\)<br>
\(\beta'_\mathrm{const}=\beta_\mathrm{const}+\beta_\mathrm{const,PTB}x_\mathrm{PTB}+\beta_\mathrm{const,WT2}x_\mathrm{WT2}.\)

Our parameter estimates are summarized in  2.

One observation about the parameter estimates in  2 is that the confidence intervals for \(\alpha_\mathrm{year}\) and \(\beta_\mathrm{year}\) are not statistically significant at the 5% significance level, while \(\alpha_\mathrm{param}\) and \(\beta_\mathrm{data}\) are. As mentioned in section 3.2, the result is that the model fails to obtain statistically significant estimates of effective parameter and effective data doubling times. However, when we use these estimates to determine effective compute doubling times, we obtain statistically significant estimates. The reason for this is illustrated in Figure 9--the estimates for \(\alpha_\mathrm{year}\) and \(\beta_\mathrm{year}\) are clearly negatively correlated. In particular, when \(\alpha_\mathrm{year}\) is positive, \(\beta_\mathrm{year}\) is negative and vice versa, such that the overall estimated effective compute doubling time is always positive.

<sup>10</sup>We use PaLM as a reference rather than larger more recent models such as GPT-4 because it was unlikely that GPT-4 would have been trained without an improvement in our understanding of scaling laws, whereas PaLM was likely trained prior to the development of updated scaling laws.

Compute multiple equivalent
5x
4x
PaLM (540B) scale
3x
GPT-3 scale
2x
GPT-2 scale
1x
1019
1020
1021
1022
1023
1024
1025
Compute

Figure 8: Compute equivalent multiplier from optimal scaling from switching from Kaplan et al. 2020 to Chinchilla (Hoffmann et al. 2022) scaling laws as a function of training compute for dense autoregressive transformer models. Note that GPT-3 and PaLM (540B) use around 1.7 and 1.44 tokens/parameter respectively, close to what the Kaplan scaling laws recommend, suggesting that Kaplan-scaling was close to what was practiced at the time.

