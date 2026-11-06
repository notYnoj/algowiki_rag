variation. In contrast, Algorithm ENUM takes around 8s for an instance of size _n_=1000 with a far larger variation.

_Sex-equal score:_ A wide variation in sex-equal score over the six optimal matchings can be seen in Figure 2b (and  4). Sex-equal and balanced stable matchings are extremely closely aligned giving a mean sex-equal score of 265.0 and 284.0 respectively for the instance type with _n_=1000. Min-sum regret stable matchings, on the other hand, performed the least well with a mean sex-equal score of 12400.0 for the same instance type.

_Regret-equality score:_ Similar to the previous point we see a wide variation in regret- equality score over the six optimal stable matchings in Figure 2e (and  7). For the instance type with _n_=1000, this ranges from a mean regret-equality score of 14.2 for the regret-equal stable matching to 84.6 for the minimum regret stable matching. It is interesting to note that the type of optimal stable matching (out of the six optimal stable matchings tested) whose regret-equality score tends to be furthest away from that of a regret-equal stable matching is the min-regret sum stable matching. This may be due to the fact that minimising the sum of two measures does not necessarily force the two measures to be close together.

_Output from Algorithm REDI:_ Due to the wide variation of regret-equality scores among different types of optimal stable matchings (as described above) it is clear that no other optimal stable matching is able to closely approximate a regret-equal stable matching, which highlights the importance of Algorithm REDI that is designed specifically for optimising this measure. Interestingly, Algorithm REDI is also competitive in terms of balanced score, cost and degree. Indeed, we can see from s 3, 5 and 6, that Algorithm REDI approximates these types of optimal stable matchings at an average of 9.0%, 1.1% and 3.0% over their respective optimal values, for instances with _n_=1000. Over all instance sizes, these values are within ranges [4.0%,10.9%], [1.1%,3.4%] and [1.3%,3.7%], respectively. This gives a good indication of the high-quality of output from this algorithm even on seemingly unrelated measures.

Algorithm REDI Algorithm ENUM 104 Duration (ms) 103 0
200 400 600 800 1000 n

**Figure 1** A log plot of the time taken to execute Algorithms REDI and ENUM. A second order polynomial model has been assumed for best-fit lines.

