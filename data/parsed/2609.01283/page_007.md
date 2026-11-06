<tbc>flow, _s_- and global min-cut, all-pairs bounded flow, arborescences, spanning trees, colorful spanning trees, arboricity, matroid parity, and arbitrary-degree \(\alpha\)-factors with \(O(f^\omega)\) query time for decision variants (see  4). This trade-off is inherent: we prove that \(\Omega(\mathrm{min}\{\sigma^2,n^2\})\) bits are necessary for flows, cuts, colorful spanning trees, and matching in this model, already for _f_=2 (see Section 9), establishing the optimality of our \(O(\sigma^2)\) space bounds.

As a direct application with _k_=1, we obtain subset sensitivity oracles (see Theorem 8.2) for reachability with \(O(\sigma^2)\) space and \(O(f^\omega)\) query time, and distances with \(\widetilde{O}(Wn\sigma^2)\) space and \(\widetilde{O}(Wnf^\omega)\) query time. This matches the query time of the general-model reachability and distance oracle of \[vdBS19\], while replacing the _n_<sup>2</sup> space dependence by \(\sigma^2\).

## 1.2 Technical Overview

We now describe the main ideas underlying our framework. To illustrate the key techniques, we develop our algebraic approach through the lens of the (_s,t_)-max-flow sensitivity oracle. We first restrict attention to the decision (unweighted) versions; the weighted versions follow naturally by introducing an indeterminate _Y_ whose exponents encode weights. Throughout, \(\omega\) is the matrix multiplication exponent and F is a sufficiently large finite field.

### 1.2.1 From Reachability to _k_-Bounded Flow

Consider the problem of preprocessing a directed graph _G_ such that for any query consisting of a subset of _f_ edge updates, the updated (_s,t_)-max-flow value can be quickly reported. Prior sensitivity oracles for cuts and flows have been predominantly combinatorial \[BBP22, ACP<sup>+</sup>26, BP22\]. These methods analyze the structure of minimum and near-minimum (_s,t_)-cuts and how failures interact with them. While successful for small _f_, this analysis becomes increasingly intricate as the number of failures grows, causing query times or space to blow up exponentially with the flow value \[ACP<sup>+</sup>26\].

We instead take an algebraic approach. Our starting point is the work of Brand and Saranurak \[vdBS19\], who obtained reachability and distance sensitivity oracles for any number of failures. Since reachability is the special case of deciding whether the (_s,t_)-max-flow is at least 1, a natural question is:

\begin{tabular}{cccc}
**Problem** & **Space** & **Query Time** & **Ref** \\
\(V_0\times V_0\) Bounded Flow \((V_0\subseteq V)\) & \(O((\sigma+k|V_0|)^2)\) & \(O((f+k)^\omega)\) & Thm 8.1 \\
(_s,t_)-Max-Flow & \(O(\sigma^2)\) & \(\widetilde{O}(f^\omega)\) & Thm 8.3 \\
_s_-Min-Cut Value & \(O(f\sigma^2)\) & \(\widetilde{O}(f^\omega)\) & Cor 8.7 \\
Global Min-Cut Value & \(O(f\sigma^2)\) & \(\widetilde{O}(f^\omega)\) & Cor 8.7 \\
_k_-Arborescences & \(O(\sigma^2)\) & \(O((f+k)^\omega)\) & Thm 8.6 \\
_k_-Spanning Trees & \(O(\sigma^2)\) & \(O(f^\omega)\) & Thm 8.8 \\
Colorful Spanning Tree & \(O(\sigma^2)\) & \(O(f^\omega)\) & Thm 8.9 \\
_k_-Forest Covering & \(O(\sigma^2)\) & \(O(f^\omega)\) & Thm 8.10 \\
_r_-rank Matroid Parity & \(O(\sigma^2)\) & \(O(f^\omega)\) & Thm 8.11 \\
Arbitrary degree \(\alpha\)-factor & \(O(\sigma^2)\) & \(O(f^\omega)\) & Thm 8.13 \\
\end{tabular}

4: Subset sensitivity oracles (decision variants).

