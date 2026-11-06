### 4.4 A uniform-base lower bound

Jaffke and Jansen proved that, unless the Exponential Time Hypothesis (ETH) fails \[24\], there is no constant \(\theta\) that gives an \(\mathcal{O}(\theta^kn^{\mathcal{O}(1)})\) algorithm for _q_-Coloring parameterized by _k_=vc(_G_) simultaneously for all fixed _q_ \[25\]. This carries over to all three discovery models.

**Theorem 7.** _For each variant_ \(X\in\{\text{Flip-CD},\text{Swap-CD},\text{Slide-CD}\}\)_, there is no universal constant_ \(\theta\) _such that, for every fixed q, the restriction of X to q colors can be solved in_ \(\mathcal{O}(\theta^{\text{vc}(G)}n^{\mathcal{O}(1)})\) _time, unless ETH fails._

_Proof._ Let (_G,q_) be a _q_-Coloring instance on _n_ vertices. Assume _q\<n_, since the remaining instances are trivial. For flips, use _G_, the all-1 coloring, and budget _n_. The discovery instance is feasible exactly when _G_ is _q_-colorable, and its vertex- cover number is unchanged.

For swaps, add _n_ isolated reserve vertices of each color in \[_q_\], color _G_ entirely with color 1, and set the budget to _n_. Given a proper coloring of _G_, process its vertices one by one and swap every incorrectly colored vertex with an unused reserve vertex of its desired color. The reverse direction follows by restricting any proper target to _G_. Isolated vertices do not change the vertex-cover number.

For slides, start from the swap construction, add a universal vertex _z_ of color _q_+1, and use budget 3_n_. Each reserve swap is simulated through _z_ by three slides. In the reverse direction, every original color has multiplicity at least \(n\ge 2\), whereas color _q_+1 is unique. Properness therefore forces _z_ to retain color _q_+1, and the restriction to _G_ is a _q_-coloring. Adding _z_ increases the vertex-cover number by at most one. The constructed size is polynomial because _q\<n_. A uniform-base discovery algorithm would consequently contradict the cited lower bound.

## 5 Conclusion

The three modification step models lead to different complexity results. Under flips, the vertices outside a small modulator can be treated independently for calculating the number of required color flips. Under swaps, the size of color classes is preserved and a cycle decomposition of the color-transition multigraph permits calculating the exact swap distance through our ILP. Under slides, transition counts no longer determine the relevant distance, since the positions of the colors inside the graph matter as well. In the other direction, the common diameter-two reduction shows that even radius one and the presence of a dominating vertex do not by themselves make the repair task easy.

Several natural questions remain open. The first is whether Slide-CD is fixed-parameter tractable for vc(_G_)+_q_. We also leave open if the number of colors be removed from the parameter of the swap algorithm. Finally, it is worthwhile to establish whether the flip algorithm for distance to complete can be extended to the distance to cluster (that is, the disjoint union of cliques), where several cliques may each use the same color once.

