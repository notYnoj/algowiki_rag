## Preprocessing

At a high level, the basic framework is similar and involves recursion. However, here we have _O_(log_n_) stages, and in each stage we focus on Max-Flow values that are in the range \[_k,_2_k_). In each stage the number of terminals, i.e., nodes _u_ such that \(\alpha(u)\ge k\), is at most \(\alpha(V)/k\). At the same time, the size of the optimal separators between node pairs in this stage is smaller than 2_k_. Consequently, if such pairs are in instances of size \(\ge 60klog^3n\) then many pivots can be chosen to separate them properly, which motivates making \(\tilde{O}(k)\) repetitions of the recursion tree (we may use the terms repetitions and recursion trees interchangeably) and arguing that a high enough number of pivots will be chosen throughout the repetitions. This will guarantee that each pair _u,v_ has at least one repetition where the corresponding pivot does not belong to _C<sub>uv</sub>_. The resulting partitions after running the \(\tilde{O}(k)\) repetitions will (almost) satisfy property (\*\*\*) that was discussed in Section 1.3.1. Indeed, we demonstrate that when the algorithm terminates, with _certainty_ for every _u,v_ query the correct answer can be obtained from one of the recursion trees, or that we have queried the pair _u,v_ directly.

Let us focus on a range \[_k,_2_k_), and set \(V_{\ge k}=\{u\in V:\alpha(u)\ge k\}\) as the set of terminals for the current stage. The following is the expansion operation on a subset of terminals \(V'\subseteq V_{\ge k}\). If \(V'=V_{\ge k}\) (i.e., in the beginning of the current stage) then repeat 60_k_log<sup>3</sup>_n_ times.

1. pick a pivot node \(p\in V'\) uniformly at random.<tbc>

2. for every node \(u\in V'\backslash\{p\}\) perform a query Max-Flow(_p,u_) to get a vertex-cut (_S<sub>p,u</sub>,C<sub>p,u</sub>,S<sub>u,p</sub>_) where \(p\in S_{p,u}\), \(u\in S_{u,p}\), and the vertex-cut separating _u_ and _v_ (i.e. a _uv_-separator) is _C<sub>p,u</sub>_. Then, compute the intersection with \(V'\) of the side of _u_ in the cut, that is \(S_{u,p}\cap V'\), and denote this set by \(S'_{u,p}\), and similarly define \(S'_{p,u}\) and \(C'_{p,u}\).<tbc>

3. perform a reassignment process \(f:V'\rightarrow V'\cup\{\perp\}\) on the nodes \(V'\) and the corresponding cuts, similar to the Monte Carlo algorithm above, and set \(n'=|V'|\).<tbc>

4. if either<tbc>

(a) \(|V_{small}|<n'/4\), or<tbc>

(b) _p_ is an overused pivot, i.e., _p_ was selected as a pivot in 8log_n_ previous repetitions, then<tbc>

<tbc>_p_ is a failed pivot. In this situation, re-start the expansion operation at step 1 and continue choosing new pivots until both \(|V_{small}|\ge n'/4\) and _p_ not an overused pivot. We will show that with high probability, the number of pivot choices is _O_(log_n_).<tbc>

5. recursively compute the expansion operation on each set within the resulting partition whose size is larger than 60_k_log<sup>3</sup>_n_. Let us describe what we store at the recursion node \(t_{V^\prime}\) corresponding to the just-completed expansion operation on \(V'\) with pivot _p_. We store \((|V'|-1)+\alpha(V')\) cuts in \(t_{V_{\ge k}^\prime}\), including:<tbc>

(a) for each \(u,v\in V'\) that we computed directly, we store _C<sub>u,v</sub>_.<tbc>

(b) for each node \(u_{big}\in V'_{big}\backslash\{p\}\) we store the cut (_S<sub>p,u<sub>big</sub></sub>,C<sub>p,u<sub>big</sub></sub>,S<sub>u<sub>big</sub>,p</sub>_).<tbc>

(c) for each node _u_ in one of the other sets of the partition \(\{f^{-1}(i)\}_{i\in IM(f)}\) we store the cut it was reassigned to (_S<sub>p,f(u_)</sub>_,C<sub>p,f(u_)</sub>_,S<sub>f(u),p</sub>_).<tbc>

<tbc>We also keep an array of pointers from each node to its corresponding cuts and also their values, and we call this array _A_. We also store, for each node of \(V'\), the name of the set in the partition that it belongs to, in an array _B_.

