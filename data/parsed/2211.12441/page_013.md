Based on Claim 19, a natural choice for _f_ is any convex function that satisfies \(f(x)=\frac{1}{n}\frac{(x+1)!}{n!}\) for \(x\in\{0,\dots,n-1\}\). The factor of \(\frac{1}{n}\) comes from the fact that there are _n_ terms to sum together after the weights have been normalized. For every \(i\in[k]\) we then have<tbc>

\(\sum_{\rho\in R_i}w(\rho)=\sum_{d=0}^{n-1}\big|\{\rho\in R_i:\mathrm{deg}_\overline{H}(\rho)=d\}\big|\cdot f(d)\le\sum_{d=0}^{n-1}\frac{1}{n}\frac{(d+1)!}{n!}\cdot\frac{n!}{(d+1)!}=\sum_{d=0}^{n-1}\frac{1}{n}=1.\)

<tbc>Similar to (1) we conclude

\(k\ge\sum_{i=1}^k\sum_{\rho\in R_i}w(\rho)=\sum_\rho w(\rho)=\sum_\rho f(\mathrm{deg}_\overline{H}(\rho))\ge n!\cdot f(\mathbb{E}(\mathrm{deg}_\overline{H}(\rho)))=n!\cdot f(\mathrm{deg}_\mathrm{avg}(\overline{H})).\) (2)

Setting \(f(x)=\frac{1}{n}\frac{g(x+1)}{n!}\) turns the requirements for _f_ into those for _g_ in the statement of the lemma, and yields that \(k\ge n!\cdot f(\mathrm{deg}_\mathrm{avg}(\overline{H}))=g(\mathrm{deg}_\mathrm{avg}(\overline{H})+1)/n\).

We now turn to proving Claim 19. The comparisons and outcomes that constitute a particular execution trace of _A_ can be thought of as directed edges between the items in _X_. We refer to the resulting digraph on the vertex set _X_ as the comparison graph _C_. Since the outcomes of the comparisons are consistent with some underlying ranking, the digraph _C_ is acyclic. The rankings in _R_ are in one-to-one and onto correspondence with the linear orderings of the DAG _C_. For a given ranking \(\rho\in R\), the degree \(\mathrm{deg}_\overline{H}(\rho)\) equals the number of \(r\in\{2,\dots,n\}\) such that swapping ranks _r_-1 and _r_ in \(\rho\) results in a ranking \(\rho'=\tau\rho\) that is not in _R_, where \(\tau\) denotes the adjacent- rank transposition (_r_-1_,r_). The ranking \(\rho'\) not being in _R_ means that it is inconsistent with the combined comparisons and outcomes of the underlying execution trace, which happens exactly when there is a path in _C_ from the item \(\rho^{-1}(r-1)\) of rank _r_-1 in \(\rho\) to the item \(\rho^{-1}(r)\) with rank _r_ in \(\rho\). Thus, the degree \(\mathrm{deg}_\overline{H}(\rho)\) equals the number of \(r\in\{2,\dots,n\}\) such that there is a path from \(\rho^{-1}(r-1)\) to \(\rho^{-1}(r)\) in _C_. See Figure 5 for an illustration, where a squiggly edge \(u\unknown v\) denotes that there exists a path from _u_ to _v_ in _C_. We only draw squiggly edges from one position to the next, so \(\mathrm{deg}_\overline{H}(\rho)\) equals the number of squiggly edges in Figure 5.

Our strategy is to give a _compressed encoding_ of the rankings in _R_ such that there is more compression as the number of squiggly edges increases. Our encoding is based on the well-known algorithm to compute a linear order of a DAG. Algorithm 1 provides pseudocode for the algorithm, which we refer to as BuildRanking.

In our formulation, BuildRanking is nondeterministic: There is a choice to make in step 3 for each _r_=1_,...,n_. The possible executions of BuildRanking are in one-to-one and onto correspondence with the linear orders of _C_, and thus with the rankings in _R_.

Our encoding is a compressed description of how to make the decisions in BuildRanking such that the output is \(\rho\). Note that if \(\rho^{-1}(r-1)\unknown\rho^{-1}(r)\), then the item _x_ with rank _r_ cannot enter the set _S_ before iteration _r_. This is because before \(\rho^{-1}(r-1)\) is removed from _T_ at the<tbc>

