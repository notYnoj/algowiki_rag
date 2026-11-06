<tbc>right. Our Conjecture 2 can be recast in terms of circuit complexity. Consider a multi-input, multi- output circuit _C_ consisting solely of unbounded fan-in OR gates. We would like to "compress" _C_ into an equivalent circuit of comparable size but smaller depth. Conjecture 2 is equivalent to Conjecture 3 below; none of the prior work on depth-reduction \[Hås86, Sch82, Sch83, RM97, DRNV16, GKW21\] directly applies to Conjecture 3.

**Conjecture 3.** _Suppose_ \(C:\{0,1\}^a\rightarrow\{0,1\}^b\) _is a circuit consisting solely of OR gates and m wires. There is a logically equivalent circuit_ \(C_+:\{0,1\}^a\rightarrow\{0,1\}^b\) _that has_ \(\widetilde{O}(m)\) _wires and depth_ polylog(_m)._

### Organization.

In Section 2 we give a self-contained exposition of Hesse’s lower bound for (non- Steiner) shortcuts, which we denote by graph family G_<sub>k</sub>_; we will later use this same graph for Theorem 1.3. We then show that the lower bound fails once Steiner vertices are allowed. In Section C we also show how Steiner vertices break the lower bound of \[VXX24\].<sup>3</sup> All other existing lower bounds that we know of can be broken in a similar fashion using Steiner vertices, but we omit the details.

Section 3 contains our thickness lower bounds. We prove Theorem 1.3. We also formalize the noised graph family \(\widetilde{\mathcal{G}}_k\)--our candidate hard instance for Conjecture 2--and prove that shortcutting \(\widetilde{\mathcal{G}}_k\) requires strictly higher thickness than the one for G_<sub>k</sub>_.

In Section 4 we discuss generalizations of Steiner shortcuts to Steiner hopsets and Steiner low-congestion shortcuts.

## 2 Hesse’s Counterexample Graphs G_<sub>k</sub>_

In this section we review Hesse’s lower bound construction \[Hes03\] and illustrate why his argument breaks down when Steiner vertices are allowed.<sup>4</sup> The attack presented for Hesse’s construction also applies, with suitable modifications, to all subsequent lower bound \[HP21, LVWX22, VXX24, HXX25\]; for details of how to do this with \[VXX24\] in particular, see Appendix C. The reason we describe Hesse’s counterexample in detail is that it is the basis for the lower bounds of Section 3.

Following \[Hes03\] we construct a family of graphs G_<sub>k</sub>_, \(k\ge 2\). Each graph \(G=(V,E)\in\mathcal{G}_k\) will have an associated set of critical vertex pairs \(P\subseteq V\times V\) such that any reachability shortcut of _G_ has size at least |_P_| or hop diameter at least poly(_n_) between some pair of vertices \((s,t)\in P\). The properties of graph family G_<sub>k</sub>_ can be summarized in the following theorem.

**Theorem 2.1** (Cf. \[Hes03, Theorem 4.1\])**.** _Let k\>_1 _be an integer and_ \(\epsilon=\Omega(1/k)\). G_<sub>k</sub> is an infinite family of n-vertex, n_<sup>1+_O_(1_/k_)</sup>_-edge directed graphs. Each graph_ \(G=(V,E)\in\mathcal{G}_k\) _has an associated set of critical vertex pairs_ \(P\subseteq V\times V\) _of size_ \(|P|=\Omega(n^{1.5-\epsilon})\)_. For any shortcut set_ \(E_+\subseteq E^*\) _of G, where G_<sup>∗</sup>=(_V,E_<sup>∗</sup>) _is the transitive closure of G, either_

• \(|E_+|\ge|P|\)_, or_<tbc>

• _There is a pair of vertices_ \((s,t)\in P\) _such that_ \(dist_{G_+}(s,t)=n^{\Omega(1/k)}\) _in_ \(G_+=(V,E\cup E_+)\).

In Section 2.3, we show that Hesse’s construction and argument fails in the presence of Steiner vertices, as captured by the following theorem.

<sup>3</sup>The most recent \(\Omega(n^{2/9})\) lower bound of \[HXX25\] is a slightly optimized version of \[VXX24\] and can be broken in the same way. <sup>4</sup>Technically, we consider a slight variation of Hesse’s construction, decreasing the density of the graph to improve our achievable thickness lower bounds from \(\sqrt{logn}\) to log_n/_loglog_n_. This modification has no significant effect on the analysis in the non-Steiner setting nor for breaking the construction via Steiner points.

