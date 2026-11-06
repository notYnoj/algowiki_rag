**- **Evaluator accuracy.** The true rating and comparison accuracies are 65% and 75%, or 85% and 90%.<tbc>

**- **Rating threshold.** The true threshold is \(\theta_0=-1.58\) or \(\theta_0=1.58\).<tbc>

<tbc> 1 reports the percent increase in terminal EOC of SE relative to unbiased SE. In 16 of the 18 cases it is between -9% and 27%. While this decrease in performance (on average) is not negligible, it is small relative to SE’s advantage even over KG(SA) in the corresponding configurations (20%, 111%, and 217%). The setting we consider where misspecification has a substantial impact is when the true accuracies are<tbc>

<tbc>85% and 90%. There, the terminal EOC of SE is 41% and 74% higher than unbiased SE at _I_=80 and 160. We note that this misspecification is extreme: \(\beta_0\) is twice what SE assumes (0.621 instead of 0.316), and \(\beta_1\) is 1.6 times (0.688 instead of 0.439). To understand what drives the difference in performance,  2 shows for the _I_=80 configuration how SE and unbiased SE split spending between ratings and comparisons over the course of the budget. Unbiased SE shows the rating-then-comparison pattern of Figure 2 even more sharply than in the base configurations: it spends the first half of the budget on ratings, and then turns almost entirely to comparisons, making good use of the more accurate evaluations (ratings in particular). In contrast, SE mixes in comparisons early, and its shift to more comparisons comes later and is less pronounced. The mechanism driving this is the following. Consider a good item, one prior standard deviation above the mean. With the more accurate evaluators, a rating results in a thumbs-up 97.5% of the time, while SE assumes it is 84%. SE sees multiple good items receive several thumbs-up, quickly becomes overconfident that they are good, and starts comparing them early. As a result, it does not rate enough of the other items in the first half of the budget, and later goes back to rating them. Overall, misspecification generally has a negative impact<tbc>

<tbc>on SE’s performance, which can be substantial when the misspecification is extreme, but the loss is small relative to SE’s advantage over the benchmarks.

\begin{tabular}{ccccccc}
misspecification & _I_=20, _k_=2 & \multicolumn{2}{c}{_I_=80, _k_=3} & \multicolumn{3}{c}{_I_=160, _k_=4} \\
heterogeneous accuracies & +3.7% & (5.0) & +16.7% & (4.3) & +14.8% & (3.8) \\
heterogeneous \(\theta_0\) & +2.5% & (4.6) & -6.6% & (3.4) & +1.7% & (3.4) \\
true accuracies 65/75 & -3.1% & (2.6) & -8.9% & (2.2) & -4.6% & (1.8) \\
true accuracies 85/90 & +5.3% & (6.6) & +41.2% & (6.1) & +73.7% & (6.5) \\
true \(\theta_0=+1.58\) & +3.2% & (3.7) & -0.4% & (3.6) & +1.5% & (3.2) \\
true \(\theta_0=-1.58\) & -1.2% & (4.0) & +26.9% & (4.3) & +21.5% & (3.5) \\
\end{tabular}

\begin{tabular}{ccccccccc}
eighth of the budget & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
SE & 22% & 31% & 32% & 31% & 30% & 34% & 47% & 73% \\
unbiased SE & 0% & 0% & 0% & 1% & 52% & 99% & 98% & 94% \\
\end{tabular}

** 1 % increase in the EOC of SE relative to unbiased SE (standard error),** _r_<sub>1</sub>=3.

** 2 % of each eighth of the budget spent on comparisons. Accuracies:** 85% and 90% **(**_I_=80**,** _k_=3**,** _r_<sub>1</sub>=3).**

