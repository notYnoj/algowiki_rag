## 6 The Competitive Ratio

We consider online coloring with random arrivals for general graphs. In online coloring, a lower bound of \(\Omega(\frac{n}{\mathrm{log}^2n})\) on the competitive ratio is known for both deterministic and randomized algorithms \[HS94\]. However, with the random-order model, we can do better.

**Theorem 2** (restated)**.** _In the random-order model, when n is known in advance, there exists a randomized online algorithm that attains a competitive ratio of_ \(\widetilde{O}(n^{2/3})\).

_Proof._ The idea is to simulate the behavior of Algorithm 1 for 2_<sup>q</sup>_-colorable graphs, COLORING<sub>2_<sup>q</sup>_</sub>(_n_), on the same input graph _G_, for each \(q=0,1,\dots,\lceil\mathrm{log}_2n\rceil\) in parallel processes. We assume disjoint sets of colors for different processes. For each arrival of vertex \(v\in V\) , we color _v_ using the color selected by the process that has used the fewest colors so far.

We now analyze the number of colors used. Let \(q^*:=\lceil\mathrm{log}_2\chi(G^*)\rceil\). Since _G_<sup>∗</sup> is 2_<sup>q</sup>_<sup>∗</sup>-colorable, by Theorem 1, the number of colors used by the process with _q=q_<sup>∗</sup>, denoted by _c_<sub>_q_<sup>∗</sup></sub>, satisfies

\(\mathbb{E}[c_{q^*}]=O((2^{q^*})^3\mathrm{log}^2(2^{q^*})\mathrm{log}^4n)=O(\chi(G^*)^3\mathrm{log}^2\chi(G^*)\mathrm{log}^4n).\)

Moreover, for each process, at most _c_<sub>_q_<sup>∗</sup></sub> colors are used in the _actual_ online coloring, so the number of colors used overall is at most \(c_{q^*}(\lceil\mathrm{log}_2n\rceil+1)\). Therefore, this algorithm uses \(O(\chi(G^*)^3\mathrm{log}^2\chi(G^*)\mathrm{log}^5n)\) colors in expectation. Also, it is obvious that we use at most _n_ colors. Thus, we attain a competitive ratio of _O(n_<sup>2/3</sup>log<sup>7/3</sup>_n_), with the worst-case bound attained when \(\chi(G^*)=\Theta(\frac{n^{1/3}}{\mathrm{log}^{7/3}n})\). □

## 7 Conclusion

In this paper, we presented an algorithm for online coloring with random arrivals that uses _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>4</sup>_n_) colors for _k_-colorable graphs. For online coloring as a whole, we improved the performance for the case _k=_3 from \(\widetilde{O}(n^{1/2})\) colors \[Vis92\] to _O_(log<sup>4</sup>_n_) colors. We also achieved a competitive ratio of \(\widetilde{O}(n^{2/3})\), which is better than the conventional lower bound \(\Omega(\frac{n}{\mathrm{log}^2n})\) \[HS94\] and is better than an \(\Omega(n^{1-\varepsilon})\) inapproximability bound for graph coloring \[Zuc06\]. These results demonstrate that the random-order model unlocks new possibilities for improving the performance of online coloring algorithms. It is now natural to pose the following conjectures.

**Conjecture 25.** _In the random-order model, when both n and k are known in advance, there exists a randomized online algorithm that colors any k-colorable n-vertex graph using O(k_log_n_) _colors in expectation._

**Conjecture 26.** _In the random-order model, when n is known in advance, there exists a randomized online algorithm that attains a competitive ratio of O_(log_n)._

Finally, a limitation of our result is that it relies on the random-order model and does not extend to adversarial arrivals. It is natural to ask whether the following conjecture holds.

**Conjecture 27.** _For any constant_ \(k\ge 3\)_, there exists a (randomized) online algorithm for coloring k-colorable graphs with n_<sup>_o_(1)</sup> _colors, even without assuming random arrivals._

