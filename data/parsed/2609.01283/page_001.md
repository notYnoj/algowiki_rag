# Sensitivity Oracles for Matroid Packing, Matroid Covering, and Matching Problems with Applications

Keerti Choudhary<sup>∗</sup><br> Amit Kumar<sup>†</sup><br> Lakshay Saggi<sup>‡</sup>

**Abstract**

Sensitivity oracles preprocess a graph so that queries can be answered after any _f_ edge insertions and deletions, without recomputing from scratch. For structural optimization problems the known landscape is limited: for flows and cuts, all known compact oracles handle only \(f\le 2\) failures; existing oracles for _s_- and global min-cut apply only to undirected graphs; and for matchings, arborescence and spanning-tree packings, and arboricity, no efficient oracle is known for _f\>_1. We present a unified algebraic framework based on sensitivity oracles for matroid packing, covering, and parity of sparse linear matroids, yielding the first oracles supporting an arbitrary number _f_ of updates across all of these problems (all constructions randomized Monte-Carlo).

Concretely, we obtain efficient oracles for exact (_s,t_)-max-flow/min-cut, resolving an open problem of Baswana, Bhanja, and Pandey (ICALP’22) with near-optimal space; for all-pairs _k_- bounded flow, generalizing the near-optimal reachability oracle of Brand and Saranurak (FOCS’19, the case _k=_1); the first oracles for any _f_ for directed _s_- and global min-cut; oracles for _k_-disjoint arborescences, _k_-disjoint spanning trees, colorful spanning trees, and arboricity; and oracles for the existence of an \(\alpha\)-factor, with perfect matching as the case \(\alpha=1\).

We further introduce the _subset sensitivity model_, in which updates are confined to a susceptible edge set of size \(\sigma\) fixed during preprocessing. Here we decouple updates from the matroid representation and eliminate the dependence on _k_ and the matroid density altogether: all of the above are supported with \(\widetilde{O}(f\omega)\) query time and \(O(f\sigma^2)\) space. We also prove a matching \(\Omega(min\{\sigma^2,n^2\})\)-bit lower bound when \(f\ge 2\), establishing optimality.

<sup>∗</sup>Department of Computer Science and Engineering, IIT Delhi, India. Email: keerti@cse.iitd.ac.in <sup>†</sup>Department of Computer Science and Engineering, IIT Delhi, India. Email: amitk@cse.iitd.ac.in <sup>‡</sup>Department of Computer Science and Engineering, IIT Delhi, India. Email: csz228231@cse.iitd.ac.in

