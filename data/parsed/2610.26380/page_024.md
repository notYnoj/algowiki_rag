## 7.2. What the policy does

To get insight into the SA allocations, Figure 2 shows the average allocation of SA at each stage of the horizon. The rating-then-comparison pattern emerges. In the first half of the budget, mostly ratings are allocated, nearly uniformly across the items and then concentrating towards the top items. In the second half, comparisons gradually take over, concentrating on items near the top-_k_ boundary. To see how the endgame

of SE differs from SA, we consider the allocation difference between SE and SA _after_ SE switches, which on this instance is at 95% of the budget. Figure 3a shows the difference in where the budget is spent. Both focus on the top-_k_ boundary, but KG concentrates much more on comparing items 2 and 3, while SA spreads more across nearby items as it is still looking for long-term uncertainty reduction around the top-_k_ threshold. This is the value of switching to KG: at the end of the horizon we want to narrow in on evaluations with potential for immediate improvement.

Figure 3b shows the terminal EOC of \(\mathrm{SE}(\mathrm{sw}=\nu)\) which, for illustrative purposes, we compute for all \(\nu\). The marginal analysis stops at \(\nu=0.95\), while the minimum is at \(\nu=0.8\), showing that it need not give the optimal switching point. However, the two differ by less than 1% of the EOC, well within one standard error of the estimated EOC. In general, as \(\nu\) moves back the EOC first dives to the optimal point and then increases, and the same pattern appears in the other configurations. In the majority of the configurations, the switching procedure identifies the minimum.

## 7.3. The value of combining the two evaluation types

We next focus on the value of combining the two evaluation types and test how well SE balances between them by comparing SE to the restricted versions of itself defined in §7.1. We find that rating only (SE(rc=1))

budget 0-20 budget 20-40 budget 40-60 budget 60-80 1
0.8 5
0.6 mean ratings 10 0.4 0.2 8% on comparisons 19% on comparisons 19% on comparisons 28% on comparisons 15 0.0 budget 80-100 budget 100-120 budget 120-140 budget 140-160 1
0.5 5
0.4 0.3 true rank mean comparisons 10 0.2 0.1 15 49% on comparisons 70% on comparisons 81% on comparisons 73% on comparisons 0.0 1
5 10 15 1
5 10 15 1
5 10 15 1
5 10 15 true rank true rank true rank

**Figure 2 Mean SA allocation by true rank in each eighth of the budget (**_I_=40**,** _k_=2**,** _r_<sub>1</sub>=3**), with ratings on diagonal and comparisons off diagonal. The lower triangle reports the percent of budget spent on comparisons.**

