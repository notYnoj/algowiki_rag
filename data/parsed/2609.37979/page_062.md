**Observation 10.1.** _Under Hypothesis 3.1,_ Graph Isomorphism _cannot be solved in polynomial time (i.e._ \(\mathsf{GI}\notin\mathsf{P}\)_)._

_Proof sketch._ Assume for contradiction that Graph Isomorphism can be solved in _O(n<sup>b</sup>_) time for some constant \(b\ge 1\). Let \(k=\lceil 10b\rceil\). We construct an isomorphic-priors algorithm for _k_-Clique to handle _O_(1) prior graphs that requires _O_(1) preprocessing time and _O(n<sup>b</sup>_) query time.

During preprocessing, the algorithm does nothing. Upon receiving a query graph _H_, it simply runs the _O(n<sup>b</sup>_)-time GI algorithm to test whether \(H\cong G_i\) for any _i_. If such _G<sub>i</sub>_ exists, it outputs the precomputed answer _OPT(G<sub>i</sub>_); otherwise, it correctly declares \(H\unknown\cong G_i\) for any _i_. This satisfies the correctness guarantees of the Isomorphic-Priors model.

Since we chose \(k=\lceil 10b\rceil\), our query time is _O(n<sup>b</sup>_)=_O(n_<sup>_k/_10</sup>). Because the matrix multiplication exponent \(\omega\ge 2\), we have \(\frac{\omega k}{3}\ge\frac{2k}{3}\) . Since \(k=\lceil 10b\rceil\ge 10\), _n_<sup>_k/_10</sup> is asymptotically faster than \(O(n^\frac{\omega k}{3}-0.001)\). This implies we can solve _k_-Clique in our model in \(O(n^\frac{\omega k}{3}-0.001)\) time, which contradicts Hypothesis 3.1.

Note that the implication \(\mathsf{GI}\notin\mathsf{P}\) in the observation above remains true under weaker variants of the hypothesis, specifically as long as _k_-Clique requires \(\Omega(n^{f(k)})\) time in our model for any monotonically increasing, unbounded function _f(k_). Consequently, refuting Hypothesis 3.1 would serve as an intermediate step toward a polynomial-time algorithm for Graph Isomorphism. Conversely, resolving the hypothesis, or any of its weaker variants, in the affirmative would prove that no such algorithm exists (i.e., \(\mathsf{GI}\notin\mathsf{P}\)).

### 10.3 Acknowledgments and AI Disclosure

The authors thank Maximilian Thiessen for helpful comments on an earlier draft of this paper.

The authors used Gemini and ChatGPT as interactive writing and proofreading assistants, including for figure generation. While preparing the camera-ready version for FOCS 2026, ChatGPT was also used to suggest references, discuss technical formulations and possible extensions, and assist with the formulation and proof of the observation relating the Isomorphic-Priors model to invariant graph predictors (Section 4). These interactions informed revisions to the abstract, introduction, related-work and open-problems discussions, and the observation mentioned above. The authors substantially revised the generated material and take full responsibility for the manuscript, including all mathematical claims, proofs, and references.

Separately, after the FOCS 2026 submission, the authors used the ChatGPT models `5.6-Sol` and `6-Pro` to explore alternative proofs of results in this paper and extensions to other problems. No additional proofs or results from these post-submission experiments are included in this paper.

##

