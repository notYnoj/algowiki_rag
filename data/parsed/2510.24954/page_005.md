For example, if \(V_+=\emptyset\) (there are no Steiner vertices) then the thickness is 1, and all prior lower bounds \[Hes03, HP21, LVWX22, VXX24, HXX25\] are merely for 1-thick shortcut graphs. A 2-thick shortcut graph is one for which the in- and out-neighbors of _V_<sub>+</sub>-vertices are all original _V_ -vertices.

It turns out that almost all existing lower bounds - including the state of the art from \[VXX24, HXX25\] - break once we allow Steiner shortcuts of thickness two. Our main result in Section 3 is to show that thickness two is nonetheless insufficient for general graphs:

**Theorem 1.3.** _For_ \(t\ge 1\)_, there exists an m-edge graph G such that every t-thick Steiner shortcut graph G_<sub>+</sub> _for G either has diameter_ \(m^{\Omega(1/t)}\) _or_ \(m^{1+\Omega(1/t)}\) _edges._

In other words, Theorem 1.3 refutes Conjecture 2 for any fixed _t_, and in fact the proof goes through for any _t=o_(log_n/_loglog_n_). This implies that any upper bound for Conjecture 2 would require a somewhat intricate connection between the Steiner vertices.

Roughly speaking, the "hard" graphs used to prove Theorem 1.3 are a family G_<sub>k</sub>_, which are constructed as the _k_-fold product of a base graph, where _k\>t_. This graph class is _highly structured_, which actually makes it too easy to shortcut with Steiner vertices; in particular, the _k_-fold product G_<sub>k</sub>_ can be shortcut with thickness _t=k_+1. A natural and generic way to make this graph class more difficult to shortcut is to discard each edge with some probability _p_ inversely proportional to the diameter; denote this noised class as \(\widetilde{\mathcal{G}}_k(p)\). It is an open problem whether \(\widetilde{\mathcal{G}}_k(p)\) suffices to refute Conjecture 2. As mild evidence of the hardness of this graph family, we show that, unlike G_<sub>k</sub>_, it is resistant to _t_-thick Steiner shortcuts for \(t\le 8k/7\). See Section 3 for a more detailed discussion.

## Potential Implications.

If Conjecture 2 turns out to be true, this would have exciting algorithmic applications. Most notably, it would suggest a promising approach for solving parallel directed reachability with near-linear work and polylog depth.

In the directed reachability problem, we are given as input a graph _G_ and a vertex pair _s,t_, and asked to report whether there exists any path from _s_ to _t_. While low-depth algorithms are known if we allow polynomial work, it is still unclear what depth is possible if we restrict ourselves to _m_<sup>1+_o_(1)</sup> work. A depth of _n_ is trivial and was the best known for a long time. A breakthrough of Fineman in 2018 achieved depth _n_<sup>2/3</sup> \[Fin20\], which was later improved to _n_<sup>1/2+_o_(1)</sup> \[JLS19\]. The _n_<sup>1/2+_o_(1)</sup> bound can also be generalized to exact shortest paths \[CFR20, RHM<sup>+</sup>23b\].

All known _m_<sup>1+_o_(1)</sup>-work algorithms with sublinear depth rely on the following basic approach: **1)** compute a shortcut _E_<sub>+</sub> with diameter _h_ **2)** run BFS from _s_ in \(G_+=(V,E\cup E')\). The existing work has focused on optimizing step 1, and there is still potential for further progress in this direction. But such progress has a hard barrier: even with the perfect hopset construction, the lower bounds of \[HXX25\] proves that this approach could never lead to depth _o(n_<sup>2/9</sup>).

Observe, however, that the framework would work just as well if we replaced \(E'\) with a _Steiner_ shortcut. So if Conjecture 2 turned out to be true, this would suggest a natural approach for overcoming the above barrier and achieving polylog(_n_) depth. An analogous framework is also frequently used in other models of computation (dynamic, distributed, streaming), and in all those cases a Steiner shortcut would work just as well as a regular one.

The main body of the paper focuses exclusively on the simplest case of (Steiner) shortcuts for reachability because even here we are not sure if Conjecture 2 is true or false. But if the conjecture ends up being true, then one can state a natural generalization of the conjecture for shortest paths (a Steiner hopset) and maximum flow (a low-congestion Steiner shortcut): see Section 4 for more details.

## Connection to Circuit Complexity.

While Steiner shortcuts are primarily motivated by the algorithmic applications mentioned above, they are also a natural combinatorial question in their own<tbc>

