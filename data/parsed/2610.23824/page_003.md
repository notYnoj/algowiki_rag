## 1.2 The Random-Order Model

The _random-order model_, which assumes that the input order is chosen uniformly at random, is widely studied in the context of online algorithms. The most well-known problem is arguably the _secretary problem_, in which _n_ candidates arrive for a job interview in random order, and the interviewer must decide immediately after each interview whether to hire the candidate. Only one candidate can be hired overall. Thanks to random arrivals, the classical secretary algorithm [Lin61] selects the best candidate with probability at least \(\frac{1}{e}\approx 0.368\). In contrast, under an adversarial arrival order, no algorithm can guarantee a success probability greater than \(\frac{1}{n}\). The random-order model also leads to improved performance in many other online problems, including the following examples (see [GS21] for a survey):

• For the online bipartite matching problem, the optimal (tight) randomized competitive ratio is \(1-\frac{1}{e}\approx 0.632\) under adversarial arrivals [KVV90]. However, under the random-order model, an algorithm achieves a competitive ratio of 0.696 [MY11].<tbc>

• For the online knapsack problem, no algorithm can achieve a bounded competitive ratio under adversarial arrivals. However, under the random-order model, an algorithm achieves a competitive ratio of 0.153 [KK26].

### Online Coloring.

In online coloring with random arrivals, the given graph _G_=(_V,E_) is fixed, and the arrival order of the _n_ vertices is chosen uniformly at random from the _n_! possibilities, each with probability \(\frac{1}{n!}\). This setting has been particularly well-studied for First-Fit.

• For trees, First-Fit uses \(\Theta(\mathrm{log}n)\) colors under adversarial arrivals [Bea76; GL88], but it drops to \(\Theta(\frac{\mathrm{log}n}{\mathrm{loglog}n})\) colors in expectation under the random-order model [FGK+24; BGL+24].<tbc>

• For crown graphs (Figure 2), First-Fit uses _n/_2 colors under adversarial arrivals, but it drops to \(2.5+O(\frac{1}{n})\) colors in expectation under the random-order model [YXW+26].<tbc>

• For general bipartite graphs, it was conjectured that First-Fit only uses polylogarithmic number of colors in the random-order model [BGL+24], but it is claimed to be disproved; a very recent preprint shows a lower bound of \(\Omega(n^{1/2000})\) colors in expectation [LL26].

However, due to the inherent difficulty of online coloring, few studies have investigated random arrivals beyond First-Fit. In particular, it remained open whether algorithms for _k_-colorable graphs could be improved under the random-order model; for example, whether an \(O(n^{1/2-\varepsilon})\)-color algorithm exists for 3-colorable graphs, which would improve upon the result of [Vis92].

1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
3
3

**Figure 2:** An _n_-vertex bipartite graph on which First-Fit uses _n/_2 colors.

