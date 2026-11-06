<tbc>However, when we apply this technique to piecewise affine ranking functions, we get nonlinear constraints [23].

Abstract interpretation is also applied to segmented synthesis of ranking functions and implemented in Function [31, 33, 34]. In this series of work, decision tree representation of ranking functions is used in [34] for better handling of disjunctions. Compared to their work, we believe that our method is more easily extensible to other theories than linear integer arithmetic as long as the theories are supported by SMT solvers (although such extensions are out of the scope of this paper).

Other state-of-the-art termination verifiers include the following. Ultimate Automizer [21] is an automata-based method. It repeatedly finds a trace and computes a termination argument that contains the trace until termination arguments cover the set of all traces. Büchi automata are used to handle such traces. AProVE [10, 13] is based on term rewriting systems.

## 8 Conclusions and Future Work

In this paper, we proposed a novel decision tree-based synthesizer for ranking functions, which is integrated into the CEGIS architecture. The key observation here was that we need to cope with explicit and implicit cycles contained in given examples. We designed a decision tree learning algorithm using the theoretical observation of the cycle detection theorem. We implemented the framework and observed that its performance is comparable to state-of-the-art termination analyzers. In particular, it solved three benchmarks that no other tool solved, a result that demonstrates the potential of the current combination of CEGIS, segmented synthesis, and transition examples.

We plan to extend our ranking function synthesizer to a synthesizer of piecewise affine ranking supermartingales. Ranking supermartingales [11] are probabilistic version of ranking functions and used for verification of almost-sure termination of probabilistic programs.

We also plan to implement a mechanism to automatically select a suitable set of halfspaces with which decision trees are built. In our ranking function synthesizer, intervals/octagons/octahedron/polyhedra can be used as the set of halfspaces. However, selecting an overly expressive set of halfspaces may cause the problem of overfitting [24] and result in poor performance. Therefore, applying heuristics that adjusts the expressiveness of halfspaces based on the current examples may improve the performance of our tool.

_Acknowledgement._ We thank Andrea Peruffo and the anonymous referees for many suggestions. This work was supported by JST ERATO HASUO Meta- mathematics for Systems Design Project (No. JPMJER1603) and JSPS KAKENHI Grant Numbers 20H04162, 20H05703, 19H04084, and 17H01720.

## References

1. llvm2KITTeL. https://github.com/hkhlaaf/llvm2kittel

