<tbc>where \(\beta_j:=\frac{1}{\sqrt{1+\sigma_j^2}}\in(0,1]\), for \(j\in\{0,1\}\), captures the evaluator precision when providing a rating or a pairwise comparison. As shown in Pérez-Ortiz et al. (2020), a single latent-utility model for ratings and pairwise comparisons can fit human data well as long as the two evaluation types are allowed to differ in signal quality, which we capture through \(\beta_0\) and \(\beta_1\). In addition to variation in signal quality, there may also be heterogeneity in evaluator accuracy and bias. If these differences were known, our model would capture this by using different values of \(\theta_0\), \(\beta_0\), and \(\beta_1\) for each evaluator. Because they are generally unknown, we instead use common parameters across evaluators, effectively absorbing evaluator-level variation into the noise terms rather than learning evaluator-specific accuracy or bias from past evaluations. This is a standard simplification in the literature, and models using it have been shown to still fit human data well (Pérez-Ortiz et al. 2020). Learning evaluator-specific parameters could further inform the allocation, but would introduce an additional inference problem that we leave for future work. In the numerical experiments of §7, we stress-test this assumption by using synthetic data where accuracy and bias differ across evaluators.

One may question the feasibility of calibrating these parameters in practice. Remark 1 shows that after fixing one for identification, the rest can be calibrated from three simple, interpretable quantities.

REMARK 1. _The binary data alone cannot identify the latent utility scale and the observation accuracy parameters simultaneously: for any c\>_0_, replacing_ \((\theta,\theta_0,\beta_0,\beta_1)\) _with_ \((c\theta,c\theta_0,\beta_0/c,\beta_1/c)\) _leaves every outcome probability_ \(\Phi\big(\beta_j(\theta_i-\theta_j)\big)\) _unchanged. Thus, one parameter can (and must) be fixed, and we fix the scale of_ \(\theta\) _by choosing the prior variance s. The remaining parameters_ \(\beta_1,\beta_0,\theta_0\) _can then be found given the following more interpretable quantities, which we formally derive in the Appendix:_

(_i)_ _The probability that a comparison of two randomly chosen items agrees with the true ordering,_<tbc>

<tbc>\(\frac{1}{2}+\frac{1}{\pi}arcsin\left(\frac{\beta_1\sqrt{2s}}{\sqrt{1+2s\beta_1^2}}\right),\)<tbc>

<tbc>_which determines_ \(\beta_1\).<tbc>

(_ii)_ _The probability that a rating of a randomly chosen item is correct,_<tbc>

<tbc>\(1-\Phi\big(\frac{\theta_0}{\sqrt{s}}\big)-\Phi\big(\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}}\big)+2\Phi_2\big(\frac{\theta_0}{\sqrt{s}},\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}};\frac{\beta_0\sqrt{s}}{\sqrt{1+s\beta_0^2}}\big),\)<tbc>

<tbc>_where_ \(\Phi_2(\cdot,\cdot;\rho)\) _is the standard bivariate normal CDF with correlation_ \(\rho\).<tbc>

(_iii)_ _The expected proportion of items that receive a ‘thumbs-up’ rating,_<tbc>

<tbc>\(\Phi\big(-\frac{\beta_0\theta_0}{\sqrt{1+s\beta_0^2}}\big),\)<tbc>

<tbc>_which together with (ii) jointly determines_ \(\beta_0\) _and_ \(\theta_0\).<tbc>

