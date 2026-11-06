<tbc>dispersion parameter \(\mathrm{norm}-\phi\in[0,1]\) which is internally converted into a value of \(\phi\) such that the expected swap distance between the central order and a preference order sampled from the Mallows model with parameter \(\mathrm{norm}-\phi\) is \(\frac{\mathrm{norm}-\phi}{2}\) times the number of possible swaps. Notably, \(\mathrm{norm}-\phi=1\) results in all preference orders being sampled with the same probability, while \(\mathrm{norm}-\phi=0\) results in all agents from one side having the same preferences and \(\mathrm{norm}-\phi=0.5\) results in a model that is, in some sense, exactly between the two.

For our experiment, we proceed analogously to our basic setup (Section 6.2.1): For our three different types of changes, for \(\mathrm{norm}-\phi\in\{0,0.05,\cdots,0.95,1\}\), we sampled 200 STABLE MARRIAGE instances with 50 men and 50 women whose preferences P<sub>1</sub> are drawn from the Mallows model with the same central order and normalized dispersion parameter \(\mathrm{norm}-\phi\). Subsequently, we compute _M_<sub>1</sub> as the men- optimal matching and apply a 0.1 fraction of changes sampled uniformly at random to P<sub>1</sub> to obtain P<sub>2</sub> (we also performed this experiments with a 0.05/0.15/0.2/0.25 fraction of changes and observed similar results). We visualize the results of this experiment in Figure 3.

## Evaluation II.

For Reorder and Swap, the more unstructured the preferences of agents are the lower is the minimum symmetric difference of _M_<sub>1</sub> and _M_<sub>2</sub> (which might be intuitively surprising). For the Gale-Shapley solution and even more the worst solution, the more unstructured the preferences of agents are, the larger becomes the gap between these two solutions and the best solution (this effect becomes particularly strong if the normalized dispersion parameter goes beyond 0.5). This can be explained by the fact that if the preferences of agents are similar to each other, then there might exist only few stable matchings being quite similar to each other (and in the extreme case with each agent having the same preferences only a unique stable matching), while for random preferences there is more flexibility when choosing a stable matching.

In contrast to the other two types of changes, for Delete the minimum achievable symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> first sharply decreases until around \(\mathrm{norm}-\phi=0.3\) and afterwards steadily increases again. Moreover, as already observed before, there is only a small difference between the worst and best solution.

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
0.6
0.5
0.4
0.0
0.2
0.4
0.6
0.8
1.0
Normalized dispersion parameter

Figure 3: For different types of changes and ways to compute _M_<sub>2</sub>, average normalized symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> if a 0.1 fraction of changes is performed for a varying normalized dispersion parameter used for the Mallows model to sample the preferences.

