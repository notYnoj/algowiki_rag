# Sorting under Partial Information with Optimal Preprocessing Time via Unified Bound Heaps

Daniel Rutschmann <sup>∗</sup>

**Abstract**

In 1972, Fredman proposes the problem of sorting under partial information: preprocess a directed acyclic graph _G_ with vertex set _X_ so that you can sort _X_ in _O_(log_e(G_)) time, where _e(G_) is the number of sorted orders compatible with _G_. Cardinal, Fiorini, Joret, Jungers and Munro [S’10] show that you can preprocess _G_ in _O(n_<sup>2.5</sup>) time and then sort _X_ in _O_(log_e(G_)+_n_) time and _O_(log_e(G_)) comparisons. Recent work of van der Hoog and Rutschmann [FOCS’24] implies an algorithm with \(O(n^\omega)\) preprocessing time where \(\omega<2.372\) and _O_(log_e(G_)) sorting time. Haeupler, Hladík, Iacono, Rozhoň, Tarjan and Tˇtek [SODA’25] achieve an overall running time of _O_(log_e(G_)+_m_). In this paper, we achieve tight bounds for this problem: _O(m_) preprocessing time and _O_(log_e(G_)) sorting time.

As a key ingredient, we design a new fast heap data structure that might be of independent theoretical interest. Our heap satisfies the _unified bound_, which has previously been studied for dictionaries and binary search trees.

Funding. This research was conducted partly at the IT University in Copenhagen, Copenhagen, Denmark and partly at ISTA. Daniel Rutschmann was supported by the Carlsberg Foundation Young Researcher Fellowship CF21-0302 – “Graph Algorithms with Geometric Applications”; and by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (No. 101019564).

For open access purposes, the author has applied a CC BY public copyright license to this version of the manuscript. Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them.

<sup>∗</sup>Institute of Science and Technology Austria (ISTA), Klosterneuburg, Austria. `https://orcid.org/0009-0005-6838-2628`

arXiv:2604.12653v2 [cs.DS] 8 Oct 2026

