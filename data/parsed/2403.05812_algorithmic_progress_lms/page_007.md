An alternative approach relies on a numerical procedure rather than a closed-form solution for doubling times. We first calculate the reduction in loss \(\Delta L\) that is achieved by doubling the compute budget, assuming that _N_ and _D_ are scaled optimally under the estimated model. We then determine the time needed for algorithmic improvements to yield the equivalent reduction in loss, \(\Delta L\). It turns out that these methods yield nearly identical results, with a median doubling time of 8.6 months, and a 95% confidence interval of 4.5 to 14.5 months. This procedure is spelled out in more detail in Appendix G.

This estimate falls within the range of confidence intervals of the estimated rates of algorithmic progress in computer vision (Erdil and Besiroglu 2022), sample efficiency improvements in reinforcement learning (Dorner 2021), and the rates observed for common algorithm families (Sherry and Thompson 2021) for certain input sizes. Overall, our results suggest that algorithmic progress for language models is comparable to, and perhaps on the faster end of estimates of rates of progress in algorithms and software in domains studied previously (see Figure 1).

While the structure of our model is not amenable to analyzing fine-grained speedups or slowdowns in the rate of algorithmic improvements, we can nevertheless test the possibility of a one-time increase or decrease in growth rates over the full time period. To this end, we consider a variant of our preferred model (model 7) where a dummy variable is introduced--this is equal to 0 for any model that is published before the start of a certain year, and 1 otherwise. This allows us to consider doubling times before and after a certain year cutoff (e.g. 2017), and we perform this analysis for several such cutoffs.

The result is shown in Figure 4. Here we see that the difference in estimated doubling time before and after the start of 2017 is very pronounced, however this is not the case for other choices of the cutoff year. In each year the median doubling time is faster after the start of the cutoff year, but usually only marginally so. Overall, this does not provide strong evidence of a drastic speedup in algorithmic progress. This does not rule out the possibility of weaker effect sizes, since our approach is statistically under-powered.

## 3.2 Most recent performance gains in next-token prediction have been from compute-scaling

Naively extrapolating our estimated doubling times suggests that, between 2014 and 2023, pre-training algorithmic progress has enabled performance to improve as much as it would have with around 22,000\(\times\) more compute.<sup>5</sup> At the same time, Sevilla et al. 2022 find that physical compute budgets have doubled roughly every 6 months since the start of deep learning, including in language models. This suggests that physical compute has instead grown by a factor of around one-million-fold. This paints a stylized picture where "effective compute" expanded by about 22-billion-fold since 2014, with slightly under two-thirds of the scaling being due to increased use of actual, physical computing resources.

<sup>5</sup>We consider 2014 since this is publication year of the earliest model in our dataset for which the training compute is known.

Doubling Time
Pre
Post
3.0
2.5
2.0
1.5
1.0
0.5
0.0
2016
2017
2018
2019
2020
Year

Figure 4: Comparison of estimated doubling times for effective compute from algorithmic progress, before and after set cutoff years from 2016-2020. Shorter doubling times in the "post" period relative to "pre" indicate an acceleration in the rate of algorithmic progress after that cutoff year. Longer doubling times indicate a deceleration.

