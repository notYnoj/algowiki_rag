<tbc>weighted graphs running in \(\tilde{\mathcal{O}}(n^{2.25})\) time. Baswana and Kavitha \[BK06\] designed an algorithm that computes a (2_,W_<sub>s,t</sub>)-APSP in \(\tilde{\mathcal{O}}(n^2)\) time, where _W_<sub>s,t</sub> is the maximum edge weight on the shortest path between s and t.

## 2 Overview

Using Theorem 1.1, a +O(1)-APSP implies a 2-approximation for all pairs at a constant distance from each other. In the overview, we describe the intuition behind an algorithm that provides a constant additive approximation for the shortest path between s and t. However, our algorithm relies on certain structural assumptions that do not hold in general. We first introduce the notation used in this overview and throughout the paper.

### 2.1 Basic notations

**Definition 2.1** (Estimate between a pair of vertices)**.** _For every pair_ (s,t) _we maintain_ est(s,t)_, which is our current best estimate of the length of the_ st _path. Several known algorithms compute_ (2,1)_-approximate all-pairs shortest paths in_ \(\tilde{\mathcal{O}}(n^2)\) _time \[BK07, Som16, Knu17, PR10\]. We therefore assume that_ \(|\mathrm{st}|\le\mathrm{est}(\mathrm{s},\mathrm{t})\le 2|\mathrm{st}|+1\) _is maintained throughout the algorithm. Whenever we update_ est(s,t)_, we also update_ est(t,s).

Let A be a set of vertices obtained by sampling each vertex of V independently with probability \(\frac{1}{n^{0.05}}\). Hence, with high probability, \(|A|=\tilde{\mathcal{O}}(n^{0.95})\). The exponent 0.05 does not play any special role in the analysis. Any sufficiently small constant exponent would suffice for our purposes. We now introduce some additional notations.

**Definition 2.2** (Pivots, Balls and Clusters)**.** _For each_ \(\mathrm{s}\in\mathrm{V}\)_, let_ pivot<sub>A</sub>(s) _denote the vertex in_ A _closest to_ s _in_ G_, breaking ties arbitrarily. Let_ ball<sub>A</sub>(s) _be the set of vertices strictly closer to_ s _than_ pivot<sub>A</sub>(s)_. Formally,_<tbc>

\(\mathrm{ball}_\mathrm{A}(\mathrm{s})=\{\mathrm{v}||\mathrm{sv}|<|\mathrm{spivot}_\mathrm{A}(\mathrm{s})|\}\)

<tbc>_For each_ \(\mathrm{v}\in\mathrm{V}\)_, let_ cluster<sub>A</sub>(v) _be the set of vertices whose ball contains_ v_. Formally,_<tbc>

\(\mathrm{cluster}_\mathrm{A}(\mathrm{v})=\{\mathrm{s}|\mathrm{v}\in\mathrm{ball}_\mathrm{A}(\mathrm{s})\}\)

<tbc>Balls and clusters are well known concepts in the literature on approximate shortest paths. One can show that \(|\mathrm{ball}_\mathrm{A}(\mathrm{s})|=\tilde{\mathcal{O}}(n^{0.05})\) with high probability. However, \(|\mathrm{cluster}_\mathrm{A}(\mathrm{v})|\) may be large.<tbc>

\begin{tabular}{ccc}
Running Time & Works for pairs that are at least at a distance & Reference \\
\(\tilde{\mathcal{O}}(n^{3/2}m^{1/2})\) & all pairs & \[CZ01\] \\
\(\tilde{\mathcal{O}}(m\sqrt{n}+n^2)\) & all pairs & \[BK06\] \\
\(\tilde{\mathcal{O}}(n^{2.25})\) & all pairs & \[Rod23\] \\
\(\tilde{\mathcal{O}}(n^{2.031})\) & all pairs & \[DFK<sup>+</sup>24, SY24\] \\
\(\tilde{\mathcal{O}}(n^2)\) & O(logn) & \[DHZ00\] \\
\(\tilde{\mathcal{O}}(n^2)\) & O(loglogn) & \[Gup25\] \\
\(\tilde{\mathcal{O}}(n^2)\) & a constant c & Theorem 1.2 \\
\end{tabular}

1: A snapshot of relevant results for 2-APSP.

