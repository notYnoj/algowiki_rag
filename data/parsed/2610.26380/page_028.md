everything SE depends on, the outcome probabilities, the expected posterior covariance, the threshold, and the expected mismatch loss, is computed as a Monte Carlo average over those draws, so that the Gaussian approximation does not enter anywhere. Figure 9 plots the percent change in the terminal EOC of SE when the Gaussian approximation is replaced by the exact posterior, in all configurations. It shows that the approximation negatively affects the terminal EOC by 4% on average across all configurations and by at most 13%, which is quite mild compared to SE’s advantage over the baselines.

SE assumes perfect knowledge of the parameters and that evaluators are homogeneous (in the base configurations, accuracies of 75% and 85% and \(\theta_0=0\)). We next test the method under misspecification when the assumed parameter values are wrong and when evaluators are heterogeneous. We compare the resulting performance with unbiased SE, which runs with the correct assumptions. We consider the following misspecifications:

**–** **Evaluator heterogeneity.** Each evaluation comes from a different evaluator. We consider heterogeneity in accuracy and in rating threshold separately, and in each, an evaluator is one of two types with equal probability.

1. **Accuracies.** The rating accuracy is 70% or 80% and the comparison accuracy is 80% or 90%.

2. **Threshold.** The threshold is \(\theta_0=-1.58\) or \(\theta_0=1.58\), half a prior standard deviation below or above the assumed threshold.

1 = 20, k = 2, r1 = 3
1 = 80, k = 3, r1 = 3
1 = 160, k = 4, r1 = 3
10000%
KG(SA)
10000%
10000%
KG
1000%
RateRank
1000%
1000%
% difference in terminal EOC
from SA
100%
100%
100%
10%
10%
0%
0%
0%
-10%
-10%
-10%
-100%
-100%
-100%
1
21
41
81
161
1
21
41
81
161
1
21
41
81
161
budget
budget
budget

10%
% change in terminal EOC
0%
-10%
-20%
1,2
1,3
1,2
1,3
2,2
2,3
1,2
1,3
2,2
2,3
4,2
4,3
1,2
1,3
3,2
3,3
8,2
8,3
1,2
1,3
4,2
4,3
16,2
16,3
1 = 10
1 = 20
1 = 40
1 = 80
1 = 160
configuration (k, r1), grouped by I

**Figure 8 Percent difference in terminal EOC from SA against the total budget.**

**Figure 9 % difference in terminal EOC between the Gaussian and exact posterior.**

