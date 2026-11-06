related to the _Polynomial Freiman-Ruzsa_ (PFR) Conjecture for integers, which, if true, would almost resolve Hypothesis 1.7. Currently, the state-of-the-art bounds \[Rag25\] together with the work of \[ABC18\] imply that one can take exp((log_K_)<sup>1+_o_(1)</sup>) instead of _K<sup>c</sup>_ in Hypothesis 1.7. We therefore hope that Hypothesis 1.7 will eventually be resolved alongside the PFR Conjecture. We refer to \[Fis26\] for a more detailed discussion of this hypothesis and its plausibility.

Under Hypothesis 1.7 we do obtain the full universe reduction:

**Theorem 1.8** (Large-Universe Reduction)**.** _Under Hypothesis 1.7, the Strong Min-Plus Convolution Hypothesis and the Min-Plus Convolution Hypothesis are equivalent._

In summary, under Hypothesis 1.7, Theorems 1.6 and 1.8 fully characterize the complexity of Min-Plus Convolution as \(min\{n^2,nu\}^{1\pm o(1)}\) for all universe sizes \(u=n^{\Theta(1)}\). If this algorithm can be improved in any regime, then the Min-Plus Convolution Hypothesis fails.

## 1.5 Application to Intermediate Convolution Problems

Fischer \[Fis26\] also showed a list of APSP-based tight conditional lower bounds for "intermediate" problems, a well-studied class of matrix problems whose running times are about _n_<sup>2.5</sup> when \(\omega=2\). Likewise, our techniques also allow us to show matching conditional lower bounds for a range of intermediate sequence problems, whose best known running times are \(\widetilde{O}(n^{1.5})\).

### Min-Max Convolution.

In the Min-Max Convolution problem, we are given sequences _A,B_ of length _n_, and need to compute a sequence _C_ where _C_\[_k_\]=min<sub>_i+j=k_</sub>max{_A_\[_i\],B_\[_j_\]}. Bringmann, Künnemann and Wegrzycki \[BKW19\] showed that this problem is equivalent to approximate Min- Plus Convolution. An \(\widetilde{O}(n^{1.5})\) time algorithm for computing Min-Max Convolution was known as early as 1989 \[Kos89\]. However, no further improvements were known since then, and there is also no strong evidence why this running time might be optimal. We show a tight conditional lower bound for Min-Max Convolution.

**Theorem 1.9** (Min-Max Convolution)**.** _Min-Max Convolution cannot be solved in time_ \(O(n^{3/2-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

### Min-Equality Convolution.

In the Min-Equality Convolution problem, we are given sequences _A,B_ of length _n_, and need to compute a sequence _C_ where

\(C[k]=min_{i+j=kA[i]=B[j]}A[i].\)

Previously, it was studied by Chan, Vassilevska Williams and Xu \[CVX23\], who showed that Min- Equality Convolution requires _n_<sup>12/11-_o_(1)</sup> time, under the Strong Min-Plus Convolution Hypothesis (they also showed an _n_<sup>7/6-_o_(1)</sup> lower bound based on the Strong APSP Hypothesis and an _n_<sup>5/4-_o_(1)</sup> lower bound based on the unweighted directed APSP Hypothesis, but neither matches the \(\widetilde{O}(n^{1.5})\) upper bound). In our work, we significantly improve their result, by showing a tight lower bound based on the Strong Min-Plus Convolution Hypothesis.

**Theorem 1.10** (Min-Equality Convolution)**.** _Min-Equality Convolution cannot be solved in time_ \(O(n^{3/2-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

