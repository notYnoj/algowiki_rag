Can We Break Fine-Grained and NP-Hardness Barriers if We’ve Seen the Graph Before? The Isomorphic-Priors Model

**Abstract**

If we run a heavy-duty computation on prior data, can we avoid repeated computation for similar future inputs? Inspired by this question, we introduce a new computational model for graph problems called _algorithms with isomorphic priors_. Solving a graph problem \(\Pi\) in this model involves two phases: (i) The _preprocessing_ phase quickly analyzes _prior graphs G_<sub>1</sub>_,...,G<sub>k</sub>_ along with the (previously computed) exact optimal values _OPT(G<sub>i</sub>_). (ii) Subsequently, given a new graph _H_, a fast _query_ phase must either (a) output the exact solution _OPT(H_), or (b) correctly report that _H_ is not isomorphic to any _G<sub>i</sub>_.<sup>1</sup> _Can we avoid computing OPT(H_) from _scratch when H is isomorphic to some G<sub>i</sub>?_ We show that this is the case for a number of problems; for many others, we establish conditional lower bounds.

**(1)** Some _NP-hard_ problems, including Constrained Shortest Path and \(\ell_p\)-Shortest Path and Constrained Spanning Tree, admit polynomial preprocessing and query times in our model. In contrast, almost all of Karp’s 21 NP-complete problems and \((2-\varepsilon)\)-approximate _k_-Center, for every fixed \(\varepsilon>0\), admit no such algorithms unless Graph Isomorphism (GI) is in P, even with _O_(1) priors. Unless GI ∈ coMA, these lower bounds persist with _unbounded preprocessing_ provided the data structure size and query time remain polynomial.

**(2)** In contrast to conditional _n_<sup>3-_o_(1)</sup> fine-grained lower bounds, our framework achieves an \(O(n^\omega)\) query time for Negative Triangle and a near-linear query time for Replacement Path. It also achieves near-linear query time for Maximum Flow.

**(3)** While it remains a major open problem whether _infinite-duration games_ (such as Parity Game, Mean Payoff Game, Energy Game, and Stochastic Game) admit polynomial-time algorithms, they can be easily solved in near-linear time within our model.

Our proofs rely on a simple combination of existing tools and are accessible to readers without specialized background in these methods. The model leads to open questions about, e.g., approximation guarantees and fine-grained speedups, including whether isomorphic priors enable faster algorithms for _k_-Clique. We formulate a _k_-Clique hypothesis which implies GI \(\notin\) P.

<sup>∗</sup>Martin G. Herold was initially funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – Project number 399223600. <sup>1</sup>Our algorithms sometimes return _OPT(H_) even though no graph _G<sub>i</sub>_ is isomorphic to _H_. We focus on problems \(\Pi\) for which isomorphic instances yield identical optimal values, a property that holds for most natural graph problems.

Dani Dorfman <unknown> Max Planck Institute for Informatics Saarland Informatics Campus

Martin G. Herold<unknown> Max Planck Institute for Informatics Saarland Informatics Campus

Danupon Nanongkai <unknown> Max Planck Institute for Informatics Saarland Informatics Campus

Simon Döring <unknown> Max Planck Institute for Informatics Saarland Informatics Campus

Daniel Neuen <unknown> TU Dresden

Joachim Spoerhase <unknown> University of Liverpool

Zihang Wu <unknown> Max Planck Institute for Informatics Saarland Informatics Campus

arXiv:2609.37979v1 [cs.DS] 29 Sep 2026

