<tbc>and a _k_-partial _k_-coloring under the condition \(\Delta\ge k+2\) and \(k\ge 4\) (see \[2\]). The same work also establishes lower bounds: computing a 2-partial 2-coloring in \(\Delta\)-regular graphs requires \(\Omega(logn)\) rounds deterministically and \(\Omega(loglogn)\) rounds randomized, for any \(\Delta\ge 2\). More generally, any _k_- partial _c_-coloring in \(\Delta\)-regular graphs with \(k\ge\frac{\Delta(c-1)}{c}+1\) also requires \(\Omega(logn)\) deterministic rounds and \(\Omega(loglogn)\) randomized rounds \[2\]. Additionally, Brandt \[6\] recently proved that 1-partial 2- coloring in odd-degree graphs cannot be solved in \(o(log^\star\Delta)\) rounds, matching the 30-year-old upper bound from \[22\]. Finally, both _k_-partial _O(k_<sup>2</sup>)-coloring and _d_-defective \(O(\Delta^2/d^2)\)-coloring can be computed in _O_(log<sup>⋆</sup>_n_) rounds \[18\].

## 3 Our Results

The problem of _k_-partial _k_-coloring has been studied in the restrictive settings by \[2\] where they showed that for constant degree _d_-regular graphs, a _k_-partial _k_-coloring can be computed in _O_(log<sup>⋆</sup>_n_) rounds provided that \(d\ge k+2\) and \(k\ge 4\). Contrary to these results and the existence of efficient round complexity for _k_-partial (_k_+1)-coloring in general graphs, our results show that the problem of _k_-partial _k_-coloring becomes "hard" in the classical (centralized) setting and "global" in the local distributed setting for general (constant degree) graphs for every fixed integer \(k\ge 3\). In Section 5, we characterize the hard instances of partial coloring which have to be properly colored even when relaxed to partial coloring restrictions. We leverage such structure to prove the next two theorems which form the crux of our contribution.

### Classical Complexity.

We proved that determining whether a given graph is _k_-partially _k_- colorable is NP-complete for every constant \(k\ge 3\), revealing a sharp threshold between the problem of _k_-partial (_k_+1)-coloring which admits a simple _O(n_) step greedy algorithm.

**Theorem 1.** _For every fixed integer_ \(k\ge 3\)_, the problem of deciding whether an input graph G is k-partially k-colorable is NP-complete._

### Distributed Complexity.

The problem of 2-partial 2-coloring on general graphs trivially admits an \(\Omega(n)\) lower bound as 2-partial 2-coloring implies a proper 2-coloring on paths which readily admits an \(\Omega(n)\) round lower bound (refer to Section 7.5 of \[25\]). We show that the problem of _k_-partial _k_-coloring of graphs which are _k_-partially _k_-colorable, admits an \(\Omega(n)\) round lower bound for every constant \(k\ge 3\), demonstrating an exponential separation as we reduce the number of colors from _k_+1 to _k_.

**Theorem 2.** _For every fixed integer_ \(k\ge 3\) _and for any k-partial k-coloring LOCAL algorithm_ A _for k-partially k-colorable graphs, there exists an n-node k-partially k-colorable graph G such that_ A _requires_ \(\Omega(n/k^3)\) _rounds to color G._

## 4 Distributed LOCAL model

The standard LOCAL model of distributed computing is a _synchronous_ model of distributed computing which was introduced in \[20\]. The exposition of LOCAL model here has been adapted from \[8\]. It comprises of an _n_-vertex communication network _G_=(_V,E_). Each edge \(\{u,v\}\in E\) is a bi-directional communication channel between _u_ and _v_. Each vertex gets assigned a unique<tbc>

