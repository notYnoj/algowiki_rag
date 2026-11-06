<tbc>with _M_<sub>1</sub>), as the size of all stable matchings in P<sub>2</sub> is the same. As proven by Vande Vate \[1989, Theorem 1\], the LP relaxation of the resulting ILP has integral extreme points, implying that we can solve the formulation as an LP.

## 6.2 Relationship between \(|\mathcal{P}_1\oplus\mathcal{P}_2|\) and \(|M_1\triangle M_2|\)

In this section, we analyze the relationship between the number of changes that are applied to P<sub>1</sub> to obtain P<sub>2</sub> and the size of the symmetric difference between the given matching _M_<sub>1</sub> that is stable in P<sub>1</sub> and a stable matching _M_<sub>2</sub> in P<sub>2</sub> for different methods to compute _M_<sub>2</sub>. We start in Section 6.2.1 by considering instances with 100 agents having uniformly at random sampled preferences. Afterwards, we vary our setting in three different ways: We analyze in Section 6.2.2 the influence of the structure of the preferences on our results, and in Section 6.2.3 the influence of the number of agents. Lastly, in Section 6.2.4, with Reorder (inverse) and Add we consider two further types of changes in addition to Reorder, Delete, and Swap.

### 6.2.1 Basic Setup: 100 Agents with Random Preferences

We start in this subsection with our basic setup with 100 agents having random preferences, addressing the following fundamental question:

### Research Question.

What is the relationship between the number of changes that are applied to P<sub>1</sub> and the difference between _M_<sub>1</sub> and _M_<sub>2</sub>? Can only few changes already require that the matching needs to be fundamentally restructured?

### Experimental Setup.

For each of the three considered types of changes, for \(r\in\{0,0.01,0.02,\dots,0.3\}\) we sampled 200 STABLE MARRIAGE instances with 50 men and 50 women with random preferences (collected in the preference profile P<sub>1</sub>). For each of these instances, we set _M_<sub>1</sub> to be the men-optimal matching.<sup>3</sup> Afterwards, we applied a uniformly at random sampled _r_-fraction of all possible changes of the considered type to profile P<sub>1</sub> to obtain profile P<sub>2</sub>. Subsequently, we computed a stable matching _M_<sub>2</sub> in P<sub>2</sub> with minimum/maximum normalized symmetric difference \(\frac{|M_1\triangle M_2|}{|M_1|+|M_2|}\) to _M_<sub>1</sub>.<sup>4</sup> We denote the solution with minimum symmetric difference as "Best" and the solution with maximum symmetric difference as "Worst". Moreover, we computed the men-optimal matching in P<sub>2</sub> using the Gale-Shapley algorithm and denote this as "Gale-Shapley". The results of this experiment are depicted in Figure 2a.

### Evaluation.

We start by focusing on the optimal solution ("Best"; solid line in Figure 2a). What stands out from Figure 2a is that already very few or even one change in P<sub>1</sub> requires a fundamental restructuring of the given matching _M_<sub>1</sub>. To be precise, for Reorder, one reordering (which corresponds to a 0.01 fraction of changes) results in an average normalized symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> of 0.1. For Swap, a 0.01-fraction of all swaps, which corresponds to making twelve random swaps per preference order (the total number of swaps is \(\frac{n\cdot(n-1)}{2}\) ), results in an average normalized symmetric difference of 0.28, whereas a single swap per preference order already results in an average normalized symmetric difference of 0.05. For Delete, the effect was strongest, as deleting a single agent leads to an average normalized symmetric difference of 0.38. Ashlagi et al. \[2017\], Cai and Thomas \[2021\], Knuth et al. \[1990\] and Pittel \[1989\] offer some theoretical intuition of this phenomenon for Delete:<tbc>

<sup>3</sup>We used the implementation of the Gale-Shapley algorithm of Wilde et al. \[2020\]. <sup>4</sup>Note that the denominator is independent of the selected matchings _M_<sub>1</sub> and _M_<sub>2</sub>, as all stable matching in P<sub>1</sub> and P<sub>2</sub> have the same size by the Rural Hospitals theorem.

