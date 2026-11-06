_r_<sub>1</sub>, \(\beta_0\), \(\beta_1\), and \(\theta_0\), such that a fixed heuristic would do much worse, but SE will still do well by adapting to the configuration.

## 7.4. Comparison to external benchmarks

We next compare the performance of our method to RATERANK and the two KG variants. Figure 6 plots the EOC against the budget spent on three configurations. In addition to the terminal EOCs, this figure highlights two interesting differences in how the alternative approaches get there. First, we can see the "forward-looking" property of SE. During a large part of the early budget spend, its EOC is higher than that of KG(SA): SE chooses evaluations that do not maximize immediate EOC improvement, but enable it to surpass the KG policies later in the horizon. Towards the middle of the horizon, this early investment starts to pay off, and SE pulls ahead. The second takeaway from the figure is the separation between KG and KG(SA), which allows us to clearly see where, on average, in the budget KG gets stuck and how much it suffers from it.

Figure 7 shows the terminal EOC of the competing policies across all configurations, as the percent difference from SE. Remarkably, SE tends to substantially outperform KG(SA): KG(SA) has a higher terminal EOC in 23 of the 24 configurations, by more than 30% in 16 of them, and up to 281% at _I_=160, _k_=4, _r_<sub>1</sub>=2. We say this is remarkable since KG(SA) is a strong benchmark for our problem: the budgets are small, a regime where KG performs well, and we equip it with the best available fallback rule. Furthermore, the fallback is

40% 30% % change in terminal EOC of SE(rc = 1/2) relative to SE 20% 10% 0% -10% 1.2 1.3 1.2 1.3 2.2 2.3 1.2 1.3 2.2 2.3 4.2 4.3 1.2 1.3 3.2 3.3 8.2 8.3 1.2 1.3 4.2 4.3 16.2 16.3 1= 10 1= 20 1= 40 1= 80 1= 160 configuration (k, r1), grouped by I

1 = 40, k = 2, r1 = 3 1 = 80, k = 3, r1 = 3 1 = 160, k = 4, r1 = 3 KG 10 6
KG(SA) 12 RateRank 8
5 SE switch to KG 10 4
6 8
6 EOC 3
4 4
2 2
1 2
0 0
0 25 50 75 100 125 150 50 100 150 200 250 300 100 200 300 400 500 600 budget spent budget spent budget spent

**Figure 5 Percent difference in terminal EOC of SE(rc**=1/2)** relative to SE, all configurations. Above zero SE is better, below zero SE(rc**=1/2)** is. Error bars are one standard error.**

**Figure 6 EOC against budget spent.**

