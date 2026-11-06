### 1.2 Organization

We provide an overview of our arguments in Section 2, which we believe already gives readers the key ideas and enough intuition to reconstruct the full proofs. We discuss open problems, related work and formally define the model and necessary notations in Sections 3 to 5. In Section 6, we present algorithms based on randomized polynomial evaluation for Negative Triangle, Constrained Spanning Tree and \(\ell_p\)-Spanning Tree. Then, we switch to Weisfeiler-Leman techniques: Section 7 presents an elementary argument based on WL coloring for Constrained Shortest Path and Energy Game and Section 8 present the same results based on connections to graph homomorphism counting, as well as a deterministic algorithm for Constrained Spanning Tree and \(\ell_p\)-Spanning Tree. Our lower bounds are presented in Section 9. We conclude in Section 10 by presenting the proofs of our main theorems, referring to the relevant results established throughout the paper, and by discussing some hypotheses within our model and their consequences. Sections A and B provide additional algorithmic results based on WL coloring and additional lower bound results.

## 2 Overview

In this section, we outline the core technical ideas underlying our main results. We emphasize again that our primary contribution lies not in the invention of these individual techniques, but in their synthesis across different fields to demonstrate how worst-case computational barriers can be bypassed within the Isomorphic-Priors framework, alongside the establishment of tight conditional lower bounds.

We present three main ideas below: (1) algorithms via randomized polynomial evaluation, (2) algorithms via Weisfeiler-Leman (WL) color refinement, and (3) conditional lower bounds via isomorphism-preserving reductions. We strive to present these concepts without assuming a specialized background, with the goal of enabling a general theoretical computer science audience to reconstruct our proofs after reading this section.

### 2.1 Algorithms via Randomized Polynomial Evaluation (Details in Section 6)

Let us consider Negative Triangle as a guiding example. We define the _triangle polynomial_ of a weighted undirected graph _G_ as

\(P_\Delta(G):=\sum_{w_1\le w_2\le w_3}c_{w_1,w_2,w_3}(G)x_{w_1}x_{w_2}x_{w_3}\)

where _c_<sub>_w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>3</sub></sub>(_G_) is the number of triangles in _G_ whose edges possess the weight multiset {_w_<sub>1</sub>_,w_<sub>2</sub>_,w_<sub>3</sub>}. For example, the first term of \(P_\Delta(G)\) in Figure 1 is \(2x_{-2}^2x_1\), because there are two triangles in _G_ with edge weights {-2,-2,1}.

Obviously, if \(P_\Delta(G)\equiv P_\Delta(H)\) (i.e., they are identically equal as polynomials), then _G_ contains a negative triangle if and only if _H_ does. (Note that this does not imply \(G\cong H\), as exemplified in Figure 1). Our goal is therefore to efficiently identify a prior graph _G<sub>i</sub>_ such that \(P_\Delta(G_i)\equiv P_\Delta(H)\) or rule out the existence of such _G<sub>i</sub>_.

To achieve this without explicitly constructing the polynomials, we rely on randomized Polynomial Identity Testing. By the Schwartz-Zippel lemma, since \(P_\Delta\) is a multivariate polynomial of degree 3, evaluating it at a random point drawn uniformly from a sufficiently large finite field F distinguishes non-identical polynomials with high probability. Specifically, we assign each possible variable _x<sub>w</sub>_ a random value \(r_w\in\mathbb{F}\).

For APSP, ordered pairs receiving the same color have the same distance, allowing the stored distances to be transferred to the query graph.

