<tbc>start by showing that for GI the new problem Iso-GI is GI-complete (i.e., as hard as GI). Therefore, Iso-GI can be used as a source hardness within our model.

Having a source of hardness, we introduce in Section 9.3 the notion of an _isomorphism-preserving reduction_. This new kind of reduction allows us to propagate the hardness results from Iso-GI to other Iso-\(\Pi\) problems as long as there exists an isomorphism-preserving reduction between GI and \(\Pi\). We then use isomorphism-preserving reductions to obtain hardness results for each problem Iso-\(\Pi\) where \(\Pi\) is an element of

\(\mathcal{H}:=\{0/1\text{-Integer Linear Programming, Gap-}k\text{-Center}_{1,2},\text{Clique, Clique Cover, Coloring,}3\text{-Coloring,}\)<br>
\(\text{3D-Matching, Exact Cover, Feedback Arc Set, Feedback Vertex Set, Directed Hamiltonian Cycle,}\)<br>
\(\text{Undirected Hamiltonian Cycle, Hitting Set, IS, MaxCut,}k\text{-Median, SAT,}3\text{-SAT, Max}2\text{-SAT,}\)<br>
\(\text{Set Cover, Set Packing, Steiner Tree, Gap-TSP}_{1,c}\text{, Metric TSP, VC}\text{.}\)

The problem definitions can be found in Section B.1. The hardness of most problems can be shown by utilizing standard reductions from the literature. However, to obtain hardness of 3-SAT, we need to take a non-standard route through 3-Coloring. For this, we need a reduction by Lovász. See Section 9.4 for more details. Finally, utilizing the hardness of Iso-GI again, we then show in Section 9.5 that each problem in H cannot be solved efficiently in our model. To be more specific, we obtain two different kind of hardness results.

We show that no problem from H can be solved with fast preprocessing and queries, unless \(\mathsf{GI}\in\mathsf{P}\).

_Remark_ 9.2. Note that in the following theorem, we state only the dependence of the running time on _n_, although it may also depend on _k_. Here, "polynomial in _n_" means polynomial in _n_ with _k_ held fixed. The same convention applies to space requirements and to the remaining theorems in this section.

**Theorem 9.3.** _Unless_ \(\mathsf{GI}\in\mathsf{P}\)_, for every problem_ \(\Pi\in\mathcal{H}\)_, the problem_ \(\Pi\) _cannot be solved inside the Isomorphic-Priors model with k prior instances each of size at most n with preprocessing and query time polynomial in n, even when k_=1 _prior instance is given._

Under the stronger assumption \(\mathsf{GI}\notin\mathsf{coMA}\), we can also rule out a data structure of polynomial size and query time.

**Theorem 9.4.** _Unless_ \(\mathsf{GI}\in\mathsf{coMA}\)_, for every problem_ \(\Pi\in\mathcal{H}\)_, the problem_ \(\Pi\) _cannot be solved inside the Isomorphic-Priors model with k prior instances each of size at most n with a data structure of size polynomial in n, and query time polynomial in n, even when k_=1 _prior instance is given._

After showing hardness for decision problems, we move on in Section 9.6 to show different hardness results for approximation problems. To this end, we first show that Max-_k_-Coverage cannot be efficiently approximated better than 1-1_/e_ in our model, unless Max 3-SAT can be approximated arbitrarily well. The assumption on Max 3-SAT serves as our analogue to the PCP theorem. We have not been able to formulate the PCP theorem directly, because it is unclear how to define an appropriate notion of isomorphism for probabilistically checkable proofs.

**Theorem 9.5.** _Assume that there is an_ \(\varepsilon>0\) _such that_ Gap-Max-3-\(\mathsf{SAT}_{1,1-\varepsilon}\) _cannot be solved in the Isomorphic-Priors model with k prior instances each of size at most n with preprocessing time polynomial in k and n and query time polynomial in n, even when k_=1 _prior instance is given._

_Then there is an_ \(\varepsilon'>0\) _such that_ Max-_k_-Coverage _cannot be approximated within_ \((1-1/e+\varepsilon')\) _in the Isomorphic-Priors model with preprocessing and query time polynomial in n, even when k_=1 _prior instance is given. Also, there is an_ \(\varepsilon''>0\) _such that k_-Median _cannot be approximated within_ \((1+2/e-\varepsilon'')\) _in the Isomorphic-Priors model with preprocessing and query time polynomial in n, even when k_=1 _prior instance is given._

