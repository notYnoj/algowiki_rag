## 7.6. Impact of batching

Finally, we test the batched version of the method with the batch endgame parameter _w=_3 and the switching round chosen by the procedure of §5.2 applied to rounds. We run it on three configurations with the total budget of 4_I_ split into round budgets of _B=I/_8, _I/_4, _I/_2, and _I_ (rounded up), that is, from 32 rounds down to 4. Figure 10 shows how EOC improves as the budget is spent. The impact of batching is small at _B=I/_8 with a 5% to 8% increase in terminal EOC relative to SE, and grows with the round budget, with 31% to 145% at _B=I_. Even then, with only four total rounds, batched SE has a lower terminal EOC than sequential KG(SA) on the _I=_80 and _I=_160 configurations.

## 8. Concluding remarks

For adaptive top-_k_ selection, we consider a unifying generative model for ratings (thumbs-up/down) and pairwise comparisons and allow the two input types to differ in both accuracy and cost. We replace the resulting intractable dynamic program with a novel surrogate-based allocation method. Despite consisting of a sequence of state-based static optimization problems, it is effectively forward-looking by rewarding decision-relevant uncertainty reduction. Based on the surrogate, we construct an allocation policy whose decision rule decomposes into interpretable parts that give insight into exactly why a particular evaluation was chosen. For the endgame regime, we switch to the knowledge gradient policy, with a criterion for when to do so, and extend the procedure to the batched evaluation setting. Finally, we show that our method performs well in simulations, stress-test the approximation made in the analysis, and test the method under model misspecification.

There are a number of exciting possible extensions for future work. One can consider heterogeneous evaluators whose \(\beta\)’s and \(\theta_0\) are unknown and learned from the evaluations. Additionally, one may consider richer evaluation types. Our model and analysis extend to ratings with any number of categories using an ordered probit model. However, considering partial rankings of a subset larger than two items would require additional work. We also hope that our surrogate method can be further improved upon and applied to additional Bayesian sequential learning settings. For example, in Goldberger and Rudi (2026b) we develop a

1 = 20, k = 2, r1 = 3
1 = 80, k = 3, r1 = 3
1 = 160, k = 4, r1 = 3
Sequential SE 17.5
25
8
batched SE, B = I/8
15.0
batched SE, B = I/4
20
6
batched SE, B = I/2
12.5
10.0
15
4
7.5
10
EOC
5.0
2
2.5
5
0
0.0
0
20
40
60
80
50
100
150
200
250
300
100
200
300
400
500
600
budget spent
budget spent
budget spent

**Figure 10 EOC against the budget spent.**

