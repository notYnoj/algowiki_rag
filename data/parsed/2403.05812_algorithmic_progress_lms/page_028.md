the numerator _increases_, whereas the opposite is true in the compute-only case (equation 37). As a result, fits of the compute-only model tend to have very small values of \(\alpha\), since the difference in scaling behaviour between the two expressions tends to be more pronounced for larger values of \(\alpha\). Indeed, estimates using the compute-only model yield very small values of \(\alpha\), at 0.004 with a 95% CI of [0.002, 0.012]. We illustrate the difference between the scaling behavior of equations 36 and 37 in Figure 13.

We nevertheless test the compute-only model in cross validation and find that it performs very poorly on out-of-sample prediction, far worse than any of the other models that we consider. The results of this exercise are elaborated upon in section J.3.

## J.2 Algorithmic progress through changes in the scale exponents \(\alpha_\text{\textbf{param}}\) and \(\beta_\text{\textbf{data}}\)

As mentioned in Section 2.1, the final model that we use for our core results does not explicitly account for efficiency improvements through changes in scaling exponents (i.e. \(\alpha_\text{param}\) and \(\beta_\text{data}\)). The primary reason for our decision is that while this form of algorithmic progress is theoretically plausible, our model fits to the available data suggest that this effect has not been very large. For example, if we consider the estimates from model 15, which includes both the form of algorithmic progress described in Section 2.1 and improvements through changes in scaling exponents, we find that the overall contribution to algorithmic progress is dominated by the former.

Another piece of supporting evidence is that in cross validation, model 14 appears to perform roughly as well as models without any algorithmic progress at all (models 16 and 17). Furthermore, the parameters which determine the rate of changing scale exponents (\(\alpha_\text{rate}\) and \(\beta_\text{rate}\)) are generally very small (around 0.001 to 0.01). As such, the model appears to simply be approximating the equivalent models without algorithmic progress. This suggests that this form of algorithmic progress is negligible, and is also why we have excluded model 14 from Figure 3.

## J.3 Performance metrics

In this section we list the resulting goodness-of-fit metrics from our cross validation analysis. In this case we report the average out-of-sample MSE loss.

Normalized value
Chinchilla
Compute-only
1.0
0.8
0.6
0.4
0.2
α =0.01
α =0.05
α =0.3
0.0
106
107
108
109
1010
1011
1012
106
107
108
109
1010
1011
1012
106
107
108
109
1010
1011
1012
Parameters

Figure 13: Comparing the scaling behavior of equations 36 and 37, for \(\alpha=0.01\), 0.05 and 0.3. For illustration, we choose _N=D_, and normalize both expressions to equal 1 when the number of parameters _N_=10<sup>6</sup>. The difference between the scaling laws is smallest when \(\alpha\) is set to a smaller value--this is illustrated by the double-headed arrow in each plot, showing the largest gap between the two curves.

