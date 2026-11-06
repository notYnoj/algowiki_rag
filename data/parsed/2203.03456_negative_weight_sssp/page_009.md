## 3.2 The Interface of the Two Main Algorithms

Our two main algorithms are called ScaleDown and SPmain. The latter is a relatively simple outer shell. The main technical complexity lies in ScaleDown, which calls itself recursively.

**Theorem 3.4** (SPmain)**.** _There exists an algorithm_ SPmain(_G<sub>in</sub>,s<sub>in</sub>_) _that takes as input a graph G<sub>in</sub> and a source s<sub>in</sub> satisfying the properties of Assumption 2.1. If the algorithm terminates, it outputs a shortest path tree T from s<sub>in</sub>. The running time guarantees are as follows:_

• _If the graph G<sub>in</sub> contains a negative-weight cycle then the algorithm never terminates._<tbc>

• _If the graph G<sub>in</sub> does not contain a negative-weight cycle then the algorithm has expected running time_ T<sub>_spmain_</sub>=_O(m_log<sup>5</sup>(_n_)).

**Theorem 3.5** (ScaleDown)**.** _There exists the following algorithm_ \(\mathrm{ScaleDown}(G=(V,E,w),\Delta,B)\).

1. _INPUT REQUIREMENTS:_<tbc>

(_a)_ _B is positive integer, w is integral, and_ \(w(e)\ge-2B\) _for all_ \(e\in E\)<tbc>

(_b)_ _If the graph G does not contain a negative-weight cycle then the input must satisfy_ \(\eta(G^B)\le\Delta\)_; that is, for every_ \(v\in V\) _there is a shortest sv-path in_ \(G_s^B\) _with at most_ \(\Delta\) _negative edges (Definitions 2.3 and 2.4)_<tbc>

(_c)_ _All vertices in G have constant out-degree_<tbc>

_2._ _OUTPUT: If it terminates, the algorithm returns an integral price function_ \(\phi\) _such that_ \(w_\phi(e)\ge-B\) _for all_ \(e\in E\)<tbc>

_3._ _RUNNING TIME: If G does not contain a negative-weight cycle, then the algorithm has expected runtime_ \(O\left(m\mathrm{log}^3(n)\mathrm{log}(\Delta)\right)\)_. Remark: If G contains a negative-weight cycle, there is no guarantee on the runtime, and the algorithm might not even terminate; but if the algorithm does terminate, it always produces a correct output._

**Remark: Termination and Negative-Weight Cycles.** Note that for both algorithms above, if _G<sub>in</sub>_ contains a negative-weight cycle then the algorithm might simply run forever, i.e. not terminate and not produce any output. In fact the algorithm SPmain _never_ terminates if _G<sub>in</sub>_ contains a negative-weight cycle. The algorithm ScaleDown may or may not terminate in this case: our guarantee is only that if it does terminate, it always produces a correct output.

In short, neither algorithm is required to produce an output in the case where _G<sub>in</sub>_ contains a negative-weight cycle, so we recommend the reader to focus on the case where _G<sub>in</sub>_ does not contain a negative-weight cycle.

**Proof sketch of Theorem 1.1.** Algorithm SPmain is almost what we need for the main result in Theorem 1.1, but the guarantees of SPmain are slightly weaker: it is Monte Carlo (rather than Las Vegas), and it cannot return a negative cycle. We show in Section C that a combination of simple probabilistic bootstrapping and binary search can be used to transform SPmain into the main result promised in Theorem 1.1.

