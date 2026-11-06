## 6.2.3 Influence of the Number of Agents

Now, we analyze whether our observations from Figure 2a are still applicable for varying number of agents.

### Research Question.

How do the number of agents influence our study of the relationship between \(|\mathcal{P}_1\oplus\mathcal{P}_2|\) and \(|M_1\triangle M_2|\)?

### Experimental Setup.

For our three different types of changes, for \(n\in\{10,20,\dots,140,150\}\), we sampled 200 instances of ISM with _n_ men and _n_ women having random preferences, where a 0.1 fraction of changes is performed (as described in Section 6.2.1). Again as in Section 6.2.1, we computed the stable matching in P<sub>2</sub> with maximum/minimum symmetric difference with _M_<sub>1</sub> and a stable matching in P<sub>2</sub> using the Gale-Shapely algorithm. Our results can be found in Figure 4. We also repeated the same experiment where a 0.05/0.15/0.2/0.25 fraction of changes is applied producing very similar results.

### Evaluation.

The general trends we observed in Figure 2a, e.g., concerning the relationships between the different types of changes or between the three different types of solutions examined, can still be found for different numbers of agents. However, while for Reorder the minimum normalized symmetric difference between _M_<sub>1</sub> and a stable matching _M_<sub>2</sub> in P<sub>2</sub> and the normalized symmetric difference between _M_<sub>1</sub> and the Gale-Shapley matching in P<sub>2</sub> stays more or less constant for increasing number of agents, for Delete and even more for Swap, the average normalized symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> for all three ways of computing _M_<sub>2</sub> slowly increases. For our sampled ISM instances, we also measured the fraction of pairs that block _M_<sub>1</sub> in P<sub>2</sub>. For each of the three types of changes, this value is, on average, the same for all considered numbers of agents (which is in contrast to our previous observations that the fraction of necessary adjustments increases for Delete and Swap when the number of agents increases).

## 6.2.4 Two Further Types of Changes

Finally, we briefly discuss two further types of change, i.e., Reorder (inverse) where we reverse the preferences of one agent, and Add where we add an agent with random preferences. We repeated the<tbc>

Reorder
Best
Delete
Gale-Shapley
Swap
Worst
0.9
0.8
0.7
M1 M2
+ 0.6
0.5
0.4
0.3
50
100
150
200
250
number of agents

Figure 4: For different types of changes and solutions, average normalized symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> if a 0.1 fraction of changes is performed for a varying number of agents with random preferences.

