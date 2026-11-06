<tbc>Assuming that agents have random preferences (as in our experiments), with high probability in a men- optimal matching the average rank that a man has for the woman matched to him is log(_n_) \[Knuth et al., 1990, Pittel, 1989\], whereas in an instance with _n_ men and _n_-1 women the average rank a man has for the woman matched to him in any stable matching is \(\frac{n}{3\mathrm{log}(n)}\) \[Ashlagi et al., 2017, Cai and Thomas, 2021\]. Thus, if we delete a single woman from the instance (which happens with 50% probability when we delete a single agent), then already only to realize these average ranks, the given matching needs to be fundamentally restructured. Notably, if we delete two agents from the instance, which results only with a 25% probability in a higher number of men than women, then the minimum normalized symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> is only 0.28.

While ISM is solvable in polynomial time, in a matching market in practice, decision makers might simply rerun the initially employed matching algorithm (the popular Gale-Shapely algorithm in our case) to compute the new matching _M_<sub>2</sub>. In Figure 2a, in the dotted line, we indicate the normalized symmetric difference between _M_<sub>1</sub>, which is the men-optimal matching in P<sub>1</sub>, and the men-optimal matching in P<sub>2</sub>. Overall, for all three types of changes and independent of the applied fraction of changes, the normalized symmetric difference between the two men-optimal matchings is quite close to the minimum achievable normalized symmetric difference, being, on average, always only at most 0.05 higher (i.e., 5 edges larger) than for the optimal solution.

Since the Gale-Shapley solution has such a good quality, one might conjecture that all stable matchings in P<sub>2</sub> are roughly similarly different from _M_<sub>1</sub>. To check this hypothesis, in Figure 2a, in the dashed line, we display the average normalized symmetric difference of _M_<sub>1</sub> and the stable matching in P<sub>2</sub> that is furthest away from _M_<sub>1</sub>. For Delete, the above hypothesis actually gets confirmed: after few changes, the worst, the men-optimal, and the best stable matching in P<sub>2</sub> have a similar distance to _M_<sub>1</sub>, indicating that after randomly deleting some agents it does not really matter which stable matching in P<sub>2</sub> is chosen.<sup>5</sup> In contrast to this, for the other two types of changes, there is a significant difference between the best and worst solution.

<sup>5</sup>On a theoretical level, a possible explanation for this is a result of Ashlagi et al. \[2017\], who proved that in SM instances with an unequal number of men and women and random preferences, stable matchings are "essentially unique".

Reorder Delete Swap
Best Gale-Shapley Worst
0.8
0.6
M1 M2
0.4
0.2
0.0
0.00
0.05
0.10
0.15
0.20
0.25
0.30
fraction of changes

Reorder Delete Swap
Best Gale-Shapley Worst
1.0
0.8
0.6
M1 M2
0.4
0.2
0.0
0.00
0.05
0.10
0.15
0.20
0.25
0.30
fraction of changes

(a) Random preferences.

(b) Identical preferences.

Figure 2: For different types of changes and ways to compute _M_<sub>2</sub>, average normalized symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> for a varying fraction of change between P<sub>1</sub> and P<sub>2</sub>.

