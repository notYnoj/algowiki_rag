# The Parameterized Complexity of Coloring Discovery

3

We use FPT and NP for fixed-parameter tractability and nondeterministic polynomial time, respectively. W\[1\] and para-NP denote the standard parameterized complexity classes and the ETH refers to the Exponential Time Hypothesis. The parameters vc(_G_), dtc(_G_), tw(_G_), td(_G_), fvs(_G_), bw(_G_), ddp(_G_), and diam(_G_) denote, respectively, the vertex-cover number, distance to complete, treewidth, treedepth, feedback vertex-set number, bandwidth, distance to disjoint paths, and diameter of _G_. Finally, _n_=|_V(G_)| and _m_=|_E(G_)| denote the number of vertices and edges, _q_ the number of colors, and _b_ the budget. Recall that a problem is fixed-parameter tractable with respect to a parameter _k_ if an encoded instance I can be solved in time _f(k_)|I|<sup>O(1)</sup> for some computable function _f_. Unless FPT = W\[1\], a W\[1\]-hard problem is not fixed-parameter tractable.

Before the present work, the following results were known.

- Garnero et al. prove that the flip variant is polynomial-time solvable for \(q\le 2\) and, for every fixed \(q\ge 3\), NP-complete even on planar bipartite graphs. When _q_ is part of the input, it is W\[1\]-hard parameterized by the budget. They give fixed-parameter algorithms parameterized by _q+b_ and by _q_+tw(_G_) \[17\].<tbc>

- De Biasi and Lauri prove that, for every fixed \(q\ge 3\), the swap variant is NP-complete even on planar bipartite graphs and W\[1\]-hard parameterized by the budget. When _q_ is part of the input, both the flip and swap variants are W\[1\]-hard parameterized by treewidth alone \[11\].<tbc>

**-** Fellows et al. introduce the slide variant of Coloring Discovery and give polynomial-time algorithms for the swap and slide variants with two colors. They extend the planar-bipartite NP-completeness result to the slide variant through a unified proof for all three variants, give fixed-parameter algorithms on structurally nowhere dense classes parameterized by _q+b_, and prove that, on general graphs, the slide variant is W\[1\]-hard parameterized by _q+b_ and by treewidth \[13\].

### Our results.

1 summarizes our main new results.

\begin{tabular}{ccc}
Operation & Parameter & Result \\
flip & _k_=vc(_G_) & FPT, 2<sup>O(_k_log_k_)</sup>(_n+m_) \\
flip & _k_=dtc(_G_) & FPT, 2<sup>O(_k_<sup>2</sup>)</sup>_n_<sup>3</sup> \\
swap & vc(_G_)+_q_ & FPT \\
flip & td(_G_)+fvs(_G_) & W\[1\]-hard \\
swap, slide & _q_+bw(_G_) & W\[1\]-hard \\
swap, slide & _q_+ddp(_G_) & W\[1\]-hard \\
all three & _q_+diam(_G_) & NP-complete already on connected graphs with _q_=4 and diam(_G_)=2 \\
all three & _k_=vc(_G_) & no universal \(\theta^kn^{\mathcal{O}(1)}\)-time algorithm for all fixed _q_, unless ETH fails \\
\end{tabular}

** 1.** Main complexity results proved in this paper.

