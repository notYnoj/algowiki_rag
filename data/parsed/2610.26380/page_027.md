<tbc>invoked precisely in states where SA’s exploratory nature is most valuable to KG, where no single evaluation can directly change the current top-_k_ set. This shows that while the most obvious drawback of KG being myopic is that it can get stuck, that alone is not the entire problem. The eagerness to directly improve the selected _k_ throughout the budget results in evaluation choices with limited information contribution to the ultimate selection. We also note that KG(SA) outperforms KG in every configuration, by 4% to 701%, and for the configurations where it is computationally practical, RATERANK does considerably worse than our method (and KG), with 1.7 to 12 times higher terminal EOC. While a large motivating factor in this work is

small budgets, there are settings of crowdsourcing from human evaluators where budgets far beyond 4_I_ are realistic. Thus we compare the benchmarks to our method in this regime, with no switching (SA throughout), since as the budget grows the impact of the endgame and the value of switching decrease. Figure 8 shows the percent difference between the benchmarks and SA as a function of the budget spent, with the budget extended to 16_I_. As expected, at the extremely small budget _R = I_, KG is as good as SA or better, but as the budget grows the advantage of SA grows substantially with it, which is to be expected, as this is the regime where the myopia of KG hurts more.

## 7.5. Robustness to the Gaussian approximation and to misspecification

We next stress-test the effect of Approximation 1 on SE. In the absence of a conjugate prior for the probit likelihood that is amenable to analysis, this approximation replaces the posterior with a multivariate Gaussian fitted by variational inference, and the expected mismatch loss is computed with respect to it. To check whether this significantly alters the performance of the method, we run SE with the exact posterior in place of the Gaussian one. The posterior is represented by 2,000 draws of a Gibbs sampler in each round, and

KG(SA) KG RateRank SE 1,2 1,3 1,2 1,3 2,2 2,3 1,2 1,3 2,2 2,3 4,2 4,3 1,2 1,3 3,2 3,3 8,2 8,3 1,2 1,3 4,2 4,3 16,2 16,3 -10% 0% 10% 100% 1000% % difference in terminal EOC from SE

**Figure 7 Percent difference in terminal EOC from SE. Rows are labeled** _k,r_<sub>1</sub> **and grouped by** _I_**.**

