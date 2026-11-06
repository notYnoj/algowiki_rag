<tbc>through graph coloring. We begin with Karp’s SAT to Coloring reduction, which is isomorphism- preserving. In the second step, we employ Lovász’s reduction from Coloring to 3-Coloring \[Lov73\].<sup>15</sup> Finally, a standard mapping from 3-Coloring back to 3-SAT completes the chain, yielding the desired isomorphism-preserving reduction from SAT to 3-SAT. Figure 3 provides an overview of our reduction chains.

## 3 Open Problems

Our results raise several questions about the power and limitations of the Isomorphic-Priors model. We begin with four central directions: which fine-grained complexity barriers persist in our model, an Isomorphic-Priors _k_-Clique hypothesis with consequences for Graph Isomorphism, the approximability of hard optimization problems, and extensions beyond exact isomorphism. We then discuss structural questions about the sources of tractability and the broader scope of the framework.

#### Fine-Grained Complexity.

Many questions remain for problems in P. For example, our algorithm for Negative Triangle uses randomness to achieve \(\widetilde{O}(kn^\omega)\) preprocessing time and \(\widetilde{O}(n^\omega)\) query time. Can the same bounds be achieved deterministically? Can we improve them to near-linear time?

More broadly, the standard weighted versions of Negative Triangle, Replacement Path, All-Pairs Shortest Paths (APSP), Minimum-Weight Cycle, Second Shortest Simple Path, and Radius are equivalent under subcubic reductions in the classical setting without priors \[VW10, AGV15\]. Yet our algorithms achieve different query bounds for Negative Triangle and Replacement Path, and it remains unclear whether the classical equivalences extend to our model. Doing so requires isomorphism- preserving reductions. Can we solve all the problems in this equivalence class in near-linear query time?

Beyond the APSP equivalence class, it is natural to ask whether fine-grained barriers based on OV, Hitting Set, and combinatorial Triangle Detection persist in the Isomorphic-Priors model, and whether such lower bounds can be transferred via isomorphism-preserving fine-grained reductions.

#### Isomorphic-Priors _k_-Clique Hypothesis.

For every fixed integer \(k\ge 3\) divisible by three, fast matrix multiplication solves _k_-Clique in \(n^{\omega k/3+o(1)}\) time. The standard _k_-Clique Hypothesis rules out any constant improvement in the exponent \[Vas18\]. We hypothesize that this barrier persists with isomorphic priors.

**Hypothesis 3.1.** _(Isomorphic-Priors k_-Clique _Hypothesis) For every fixed integer_ \(k\ge 3\) _and constant_ \(\epsilon>0\)_, no isomorphic-priors algorithm can detect a k-clique in an n-vertex graph with both preprocessing and query times_ \(O(n^{\omega k/3-\epsilon})\)_, even with O_(1) _prior graphs._

**This hypothesis implies** \(\mathsf{GI}\notin\mathsf{P}\)**:** A polynomial-time algorithm for Graph Isomorphism would allow us to compare a query graph against _O_(1) priors and retrieve a matching prior’s answer, or report that none exists, in _n_<sup>_O_(1)</sup> time. This would contradict the hypothesis for sufficiently large fixed _k_. We provide further details and discuss weaker variants in Section 10. An important open direction is to refute these hypotheses or establish them under more standard complexity assumptions.

### Approximability.

Although we establish conditional lower bounds for exact computation and for some approximation problems, much of the approximation landscape remains open. For example, can we achieve a 0.876-approximation for Max 3-SAT, a 0.879-approximation for MaxCut, a 1.99-approximation for Vertex Cover, or an _n_<sup>0.99</sup>-approximation for Max Clique, with polynomial pre- processing and query times? Can isomorphic priors also enable a 1.385-approximation for Steiner Tree<tbc>

<sup>15</sup>We refer the interested reader to `https://users.encs.concordia.ca/~chvatal/notes/color.html`

