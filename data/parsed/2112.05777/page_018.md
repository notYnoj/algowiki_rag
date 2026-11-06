## 6.2.2 Influence of the Structure of Preferences

Now, we analyze whether our observations from Figure 2a are still applicable beyond the case where agents have random preferences.

### Research Question.

How does the structure of the preferences influence our study of the relationship between \(|\mathcal{P}_1\oplus\mathcal{P}_2|\) and \(|M_1\triangleup M_2|\)?

### Experimental Setup I.

In our first experiment in this subsection, we consider the situation which is as different as possible from our setup with random preferences, that is, we assume that all agents from one side have the same preference relation. For this, we reran the experiments from Figure 2a but instead of drawing the preferences of agents uniformly at random from the set of all preferences, we only drew one preference relation over men, respectively, women and set the preferences of all women, respectively, men to this order. The results of this experiments can be found in Figure 2b.

### Evaluation I.

Comparing Figure 2a for random preferences and Figure 2b for identical preferences, there are three major differences.

First, for identical preferences few changes have an even stronger effect than for random preferences. That is, a 0.01 fraction of changes here makes it necessary to replace on average more than half of all edges in _M_<sub>1</sub>. To get a feeling for why this is the case (for Delete), observe that in a STABLE MARRIAGE instance where all agents from one side have identical preferences, there exists only one stable matching, namely, the one where the man appearing in the _i_th position of the women’s preference list is matched to the woman appearing in the _i_th position of the men’s preference list. If we now delete, without loss of generality, a man from the instance who appears on position _j_ of the women’s preferences, then there is still only a single stable matching. In this matching, for \(i\in[1,j-1]\), the man on the _i_th position of the women’s preference list is matched to the woman on the _i_th position of the men’s preference list, whereas for \(i\in[j,n-1]\), the woman on the _i_th position is matched to the man appearing on the _i_+1st position (and the last woman on the men’s preference list remains unmatched). Thus, both matchings share _j_-1 edges while there are _n_-(_j_-1) edges unique to _M_<sub>1</sub> and _n-j_ edges unique to _M_<sub>2</sub>. Observing that _j_ is, on average, \(\frac{n}{2}\), it follows that half of the matching, on average, needs to be replaced; this also fits Figure 2b. For Reorder and Swap the situation is less clean, yet a similar intuition applies.

Second, for identical preferences, the size of the symmetric difference to _M_<sub>1</sub> of all matchings that are stable in P<sub>2</sub> is quite similar (as the best and worst solution are nearly indistinguishable), which can be intuitively explained by the fact that, initially, there is only a single stable matching and even after some changes have been applied, a large part of the matching is still fixed.

Third, while for random preferences performing some number of Delete operations requires more adjustments than performing the same number of Reorder operations, for identical preferences, both produce nearly identical results.

### Experimental Setup II.

In addition to exploring the extremes, that are, random preferences and instances where all men or all women have the same preferences, we are also interested in what happens if the agent’s preferences have some "structure". For this, we generated agent’s preferences using the Mallows model \[Mallows, 1957\], which is parameterized by a central preference order \(\succ^*\) and a so- called dispersion parameter \(\phi\in[0,1]\). In the Mallows model, the probability of drawing a preference order \(\succ\) is proportional to \(\phi^{swap(\succ^*,\succ)}\), where \(swap(\succ^*,\succ)\) is the swap distance between \(\succ\) and \(\succ^*\). As pointed out by Boehmer et al. \[2021b\], one drawback of the Mallows model is that there exists no natural interpretation of \(\phi\) and that a uniform distribution of \(\phi\) does not lead to a uniform coverage of the spectrum of preferences. That is why, as proposed by Boehmer et al. \[2021b\], we use a normalized<tbc>

