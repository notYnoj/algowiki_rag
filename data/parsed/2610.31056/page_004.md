**Theorem 1.3.** _Let_ \(M=\Theta\left(2^n\right)\)_. There exists a deterministic algorithm that given a set A of n random integers sampled uniformly from the set_ {1_,...,M}, finds distinct_ \(X,Y\subseteq A\) _such that_ \(\Sigma(X)=\Sigma(Y)\) _with probability_ \(\Omega\left(n^{-2}\right)\) _in_ \(\tilde{\mathcal{O}}(2^{n/4})\) _time._

Note that this result holds in the _average case_, whereas previous work guaranteed solutions in the worst case. The algorithm is a modification of the algorithm behind Theorem 1.1; however, the analysis is much more involved. Curiously, we can show that our algorithm also works for the _modular version_ of Equal Subset Sum. In that setting, the best algorithm is due to Allcock et al. \[AHJ<sup>+</sup>22\], who gave an O_<sup>⋆</sup>(M_<sup>1/2</sup>)-time algorithm. In fact, obtaining a faster algorithm in the modular setting is posed as an open question in \[Jin24\].

**Theorem 1.4.** _Let the modulus_ \(M=\Theta\left(2^n\right)\)_, where M=pqr,_ \(p,q=\Theta\left(M^{1/4}\right)\) _and p, q, and r are pairwise co-prime integers. There exists a deterministic algorithm that given a set A of n random modular integers sampled uniformly from_ Z_<sub>M</sub>, finds distinct_ \(X,Y\subseteq A\) _such that_ \(\Sigma(X)\equiv_M\Sigma(Y)\) _with probability_ \(\Omega\left(1\right)\) _in_ \(\tilde{\mathcal{O}}(2^{n/4})\) _time._

Notice that in this setting, we require _M_ to be a product of three pairwise co-prime integers, but the probability of success is higher. If the modulus is not a product of such integers, then using Theorem 1.3, trivially we can solve the modular problem with success probability \(\Omega(n^{-2})\). A faster average-case algorithm often leads to improved worst-case algorithms. This happened for Subset Balancing, a generalization of Equal Subset Sum, where recent average-case results \[CJRS22\] motivated improved worst-case algorithms \[RW26\]. Because our analysis is already quite technical in the average-case setting, we hope it will eventually yield worst-case algorithms with comparable running time. Note that the algorithm behind Theorem 1.1 is deterministic, albeit less efficient for small densities. In the following figure, we summarize all our results with the related previous work.

## 2 Our Techniques

### 2.1 Technique behind Theorem 1.1

#### Ingredient 1: Dynamic Programming.

First, there is a straightforward \(\mathrm{poly}(n)\cdot M\) algorithm for Equal Subset Sum: enumerate subsets of \[_n_\] and stop as soon as a collision is found. Since a collision must occur within the first _M_ nonzero sums, this procedure runs in \(\mathrm{poly}(n)\cdot M\) time.<tbc>

\begin{tabular}{ccc}
Runtime & Reference & Comment \\
O_<sup>⋆</sup>(M_) & \[Vas22\] & \\
O_<sup>⋆</sup>(M_<sup>1/2</sup>) & \[AHJ<sup>+</sup>22\] & \\
O_<sup>⋆</sup>(M_<sup>0.4</sup>) & \[JW24\] & \\
O_<sup>⋆</sup>(M_<sup>1/3</sup>) & \[JWZ25\] & \\
O_<sup>⋆</sup>(M_<sup>_o_(1)</sup>) & Theorem 1.1 & _M_=2<sup>_o(n_)</sup> \\
No _M_<sup>_o_(1/log_n_)</sup> & Theorem 1.2 & Under Hypothesis 1 \\
O_<sup>⋆</sup>(M_<sup>1/4</sup>) & Theorem 1.3 & Average-case for \(M\le 2^n\) \\
O_<sup>⋆</sup>(M_<sup>1/4</sup>) & Theorem 1.4 & Average-case Z_<sub>M</sub>_ for \(M=pqr\le 2^n\) \\
\end{tabular}

1: Summary of prior and our results for Equal Subset Sum in the pigeonhole regime. Notice that \[Vas22, AHJ<sup>+</sup>22, JW24, JWZ25\] also work in the regime when the sum is less than 2_<sup>n</sup>_-1.

