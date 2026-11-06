This algorithm just computes for all formulas \(\Phi\) that are given in the preprocessing and query phase the Gap-_k_-Coverage instance \(R(\Phi)\), using the reduction from Lemma 9.27, and applies the preprocessing and query algorithm for Gap-Max-_k_-Coverage\(_{1,1-1/e+\varepsilon}\) to them.

The same argument can be made for data structures of polynomial size.

Because in \[GK99\] it is argued that the reduction in Lemma B.30 is also a reduction from Gap-Max-_k_-Coverage\(_{1,1-1/e+\varepsilon}\) and Gap-_k_-Median\(_{1,1+2/e+2\varepsilon}\). We can repeat both arguments above for _k_-Median.

## 10 Conclusion

We conclude by presenting the proofs of our main theorems, referring to the relevant results established throughout the paper, and by discussing some hypotheses within our model and their consequences.

### 10.1 Proof of the Main Theorems

_Proof of Theorem 1.1._ By Theorem 7.2, we can solve CSP inside the Isomorphic-Priors model with \(\widetilde{O}(km)\) preprocessing time and \(\widetilde{O}(m)\) query time. By Theorem 6.3, we can solve CST randomized inside the Isomorphic-Priors model with \(\widetilde{O}(kn^\omega)\) preprocessing time and \(\widetilde{O}(n^\omega)\) query time.

The extensions from Constrained Shortest Path to Constrained Shortest Path _and_ \(\ell_p\)-Shortest Path, and from Constrained Spanning Tree to Constrained Spanning Tree _and_ \(\ell_p\)-Spanning Tree, are both straightforward generalizations of the presented algorithm. To this end, note that the technique of walk lifting (see Lemma 7.8) also works in this setting.

_Proof of Theorem 1.2._ By Theorem A.6 there is an algorithm that solves Replacement Path inside the Isomorphic-Priors model using \(\widetilde{O}(km)\) preprocessing time and \(\widetilde{O}(m)\) query time. By Theorem 6.2, there is an algorithm that solves Negative Triangle inside the Isomorphic-Priors model randomized using \(\widetilde{O}(kn^\omega)\) preprocessing time and \(\widetilde{O}(n^\omega)\) query time.

_Proof of Theorem 1.3._ By Theorem 7.4, we can solve Energy Game inside the Isomorphic-Priors model with \(\widetilde{O}(km)\) preprocessing time and \(\widetilde{O}(m)\) query time. Our Weisfeiler-Leman techniques also yield the same result for Parity Game, Mean Payoff Game, and Simple Stochastic Game. To be more specific, we show in Theorem A.2 that this can be extended to value-determined games (a general concept including the above games).

_Proof of Theorem 1.4._ The proof is a direct consequence of Theorem 9.3 and Theorem 9.4. The approximation results follow from the corresponding gap results.

### 10.2 _k_-Clique Hypothesis and Consequence

One of the foundational hypotheses in fine-grained complexity \[Vas18\] states that, for every fixed integer \(k\ge 3\), no randomized algorithm can detect a _k_-clique in an _n_-vertex graph in \(O(n^\frac{\omega k}{3}-\epsilon)\) time for any constant \(\epsilon>0\). It is natural to ask whether this fundamental computational barrier translates to the Isomorphic-Priors model. We observe that if this hypothesis extends to our setting, then Graph Isomorphism is not polynomial-time solvable.

Recall our hypothesis from earlier:

**Hypothesis 3.1.** _(Isomorphic-Priors k_**-Clique _Hypothesis) For every fixed integer_ \(k\ge 3\) _and constant_ \(\epsilon>0\)_, no isomorphic-priors algorithm can detect a k-clique in an n-vertex graph with both preprocessing and query times_ \(O(n^{\omega k/3-\epsilon})\)_, even with O_(1) _prior graphs._

