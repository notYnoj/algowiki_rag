## 1 Introduction

Real-world networks, including communication, transportation, and infrastructure networks, are inherently subject to failures and transient perturbations. Links may fail, capacities may fluctuate, and new connections may be introduced.

This motivates the study of _sensitivity oracles_ (also called fault-tolerant oracles): compact data structures that preprocess a graph (or a more general combinatorial object) so that, for any small set of _f_ updates (edge insertions, deletions, or weight changes), queries about the updated object can be answered without recomputation. Over the past two decades, the sensitivity setting has been studied extensively for shortest paths and distances \[DTCR08, DP09, WY13, vdBS19, CC20, GW19, GR21, KS23a\], reachability \[BCR16, Cho16, vdBS19\], and connectivity \[PT07, DP09, BCR16, LS22\].

In contrast, the landscape is starkly different for _structural optimization_ problems such as maxflows and min-cuts, arborescence and spanning-tree packings, matchings and degree-constrained subgraphs, and matroid intersection or parity. Here, essentially all known oracles handle only \(f\le 2\) failures, and the underlying combinatorial techniques appear inherently tied to small values of _f_:

• For a fixed pair (_s,t_), Baswana, Bhanja, and Pandey \[BBP22\] designed an (_s,t_)-min-cut oracle for \(f\le 2\) edge failures with _O(n_<sup>2</sup>) space and _O_(1) query time, using the submodularity structure of minimum and near-minimum cuts, and posed the case _f\>_2 as an open problem. Recently, the authors in \[ACP<sup>+</sup>26\] handled general _f_ via directed flow augmentation \[KKPW22\], but with space and query time scaling as \(2^{O_f(\lambda^4logk)}\) in the flow value \(\lambda\), which is quite expensive for graphs with large cuts or multiple failures. For \(f\ge 3\) the relevant minimum cuts interact in increasingly complex ways, and no compact oracle avoiding this exponential dependence is known.

• For all-pairs min-cut, the only known result is the single-failure oracle of Baswana and Pandey \[BP22\]; for _s_-min-cut and global min-cut, oracles are known only for \(f\le 2\) and only in undirected graphs \[DN95, Bha25\]; in directed graphs nothing non-trivial is known.

• For matchings, degree-constrained subgraphs (\(\alpha\)-factors), disjoint arborescences, colorful spanning trees, arboricity, and matroid packing/covering/parity, no sensitivity oracles were known for any _f\>_1, even though the _dynamic_ versions of some of these problems have received attention in the past \[BMNT23, dVG26, GP13, BS15, BS16, dVC26, BKSW23, Kis23, ABR24, Beh23\], along with results about fault-tolerant subgraphs \[AB19, BGRS22, BCDW24\].

Even seemingly simple decision questions like _does the graph remain strongly connected after f updates? does it still admit a perfect matching?_ had no efficient answer. This raises the following central question of this paper:

Is there a unifying technique that yields compact, efficient sensitivity oracles, for an arbitrary number f of updates, across a vast class of structural optimization problems?

We answer this question affirmatively, and our route is _algebraic_. Algebraic techniques involving maintaining determinants and inverses of symbolic matrices under low-rank updates have recently proven remarkably effective for dynamic and fault-tolerant variants of shortest paths and reachability \[San05, WY13, vdBS19, GR21, KS23a\], dynamic matchings \[vdBNS19, vdBKZ26\], dynamic SCC \[KS23b\] along with many other applications \[vdB21\]. Yet no general framework for _sensitivity_ oracles for matroid problems has previously been studied. We bridge this gap: rather than solving each graph problem separately, we design sensitivity oracles for the fundamental matroid primitives that underlie them all: _matroid packing_, _matroid covering_, and _matroid matching (parity)_.

