<tbc>which is exactly (1.1). Thus, the Random Subsequence Model may be viewed as a natural slice of the partition-function framework for the longest common subsequence problem. We therefore believe that a better understanding of the Random Subsequence Model is likely to be of interest for the longest common subsequence problem as well.

Lastly, we also note that longest common subsequences play a central role in deletion coding more broadly \[GHL22\]. For adversarial deletions, extremal bounds on pairwise LCS govern codebook feasibility, and even the analysis of random deletion codes is limited by the current lack of sharp estimates for the expected LCS of two random binary strings.

## 1.1.3. _Mean-field variants and directed polymers._

Our third and final connection is to _directed polymers_ in statistical physics. This connection is nontrivial, and will help us frame the discussion by using the experience of the directed polymers literature to identify which models can be expected to admit exact analytic solutions (see Section 1.2).

Given \((X,Y)\in\{0,1\}^N\times\{0,1\}^M\), \(n\le N\) and \(m\le M\), we use _X_<sub>1:_n_</sub>_,Y_<sub>1:_m_</sub> to denote the prefixes of _X,Y_ from index 1 to _n,m_, respectively. We also denote<tbc>

\(Z_{n,m}:=Z_{X_{1:n},Y_{1:m}},\)

<tbc>noting that _Z<sub>N,M</sub>=Z<sub>X,Y</sub>_. By partitioning<tbc>

\(S_{X_{1:n},Y_{1:m}}=(S_{X_{1:n},Y_{1:m}}\cap\{\sigma_m=n\})\sqcup(S_{X_{1:n},Y_{1:m}}\cap\{\sigma_m\neq n\}),\)

<tbc>we observe the recurrence relation

(1.4) \(Z_{n,m}=Z_{n-1,m}+\unknown\{X_n=Y_m\}\cdot Z_{n-1,m-1}.\)

Note that the above gives an efficient dynamic programming algorithm to compute _Z<sub>N,M</sub>_ exactly. It also leads to a natural generalization of our model. Rather than specifying two strings _X_ and _Y_, we can instead specify a matrix \(B\in\mathbb{R}_+^{N\times M}\) and _define_ the partition function _Z<sub>N,M</sub>_ via the recurrence relation

(1.5) \(Z_{n,m}=Z_{n-1,m}+B_{n,m}\cdot Z_{n-1,m-1},1\le n\le N,1\le m\le M,\)

with the initial condition \(Z_{0,m}=\delta_{0,m}\). This can be interpreted as a directed polymer model, and in the case that _B_ has entries in {0,1}, a directed percolation model, in a random environment determined by _B_. Indeed, consider a box in Z<sup>2</sup> with bottom-left endpoint at (0,0) and top-right endpoint at (_N,M_). Put an edge between any two horizontal neighbors (_n_-1_,m),(n,m_) with weight 1 and an edge between diagonal neighbors (_n_-1_,m_-1),(_n,m_) with weight _B<sub>n,m</sub>_. Then _Z<sub>N,M</sub>_ counts weighted paths from (0,0) to (_N,M_) that are monotonically increasing in the first coordinate.

This kind of model has received considerable attention in the directed polymers literature. An insight of those investigations is that only distributions of _B_ with special algebraic structure admit exact analytic solutions with existing techniques. The case where _B_ has i.i.d. Gamma-distributed entries falls in that category, and its exact analytic solution was found in the important work \[CSS15\]. We refer the reader to the next section for a discussion of how this relates to the Random Subsequence Model. As far as the authors are aware, the Random Subsequence Model itself, which corresponds to a natural "rank-one" random environment _B_, has not been explicitly studied in the directed polymers literature. Cases where the entries of _B_ are i.i.d. represent a natural _mean field_ version of the Random Subsequence Model, and the setting where _B_ has i.i.d. Unif{0,1} entries has been studied under the name "Bernoulli Matching Model" in connection to the longest common subsequence problem (see \[Bou99; MN05\]).

## 1.2. Our results.

Our first result gives strict bounds on the free energies of the null and planted variants of the Random Subsequence Model. For the rest of the paper, following the statistical physics terminology, we use the term _annealed_ free energy to refer to the quantities of the form

\(\frac{1}{N}log\mathbb{E}[Z],\)

