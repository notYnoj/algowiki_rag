<tbc>We then have \(\nu(G_F)=\nu(G)-\nu(F)\ge f-\nu(F)\). We then let \(F'\) be a non-circular flow of _G<sub>F</sub>_ with value \(f-\nu(F)\) and set \(Q=F'\backslash H\). We then see that \(\nu(H\cup Q)\ge\nu(F')+\nu(F)=f\) and \(|Q|\le|F'|\le O(n\sqrt{f-\nu(F)})\le O(n\sqrt{k})\) due to Lemma 2.2. As a result, we derive:

\(\sum_{(u,v)\in H\cup Q}|\hat{z}_u-\hat{z}_v|\ge\sum_{i\in[f]}\sum_{\left(u,v\right)\text{in}i^\text{th}s\text{-}t\text{flow}}|\hat{z}_u-\hat{z}_v|\)<br>
\(\ge\sum_{i\in[f]}|\hat{z}_t-\hat{z}_s|\) (triangle inequality)<br>
\(=f(\hat{z}_s=0\text{and}\hat{z}_t=1.)\)

This implies

\(\sum_{(u,v)\in Q}|\hat{z}_u-\hat{z}_v|\ge k'+1\)

which means some edge \((u,v)\in Q\subseteq G\backslash H\) must have \(|\hat{z}_u-\hat{z}_v|\ge\frac{k'+1}{|Q|}\ge\Omega\left(\frac{k'}{n\sqrt{k}}\right)\).

By combining Claim 5.5 and Claim 5.6, there must exist of an edge \((u,v)\in G\backslash H\) that kills a \(\frac{k'+1}{k}\cdot\left(\alpha\cdot\frac{k'}{n\sqrt{k}}\right)\approx\frac{\alpha}{4}\cdot\frac{\sqrt{k}}{n}\) fraction of the remaining witnesses, via the fact that \(k'=\frac{k}{2}\). In the next section, we introduce a subroutine that, using only _O_(log_n_) cut queries, enables us to find an edge in _G_\\_H_ that is (asymptotically) as effective as such edge (_u,v_).

## 5.3 Useful Subroutines

Consider the following problem called `FindLongEdge`. We are given the following items as an input.

• An underlying graph _G_=(_V,E_) to which we are able to make cut-query.<tbc>

• A potential function \(\phi:V\rightarrow[0,1]\) that maps \(v\in V\) to its position between 0 and 1.<tbc>

• A threshold \(\delta\in(0,1)\).

There is also a hidden parameter \(\delta_\mathrm{max}:=\mathrm{max}_{(u,v)\in E}|\phi(u)-\phi(v)|\) not known to us. We are asked to identify a _long_ edge--if one exists--whose endpoints are mapped far apart, by making cut queries to _G_. Formally, we must output either

• \((u,v)\in G\) with \(|\phi(u)-\phi(v)|\ge\frac{\delta}{2}\), or<tbc>

• "FAIL" which means \(\delta>\delta_\mathrm{max}\).

Another helpful interpretation is as follows. If \(\delta\le\delta_\mathrm{max}\), then we must output \((u,v)\in G\) with \(|\phi(u)-\phi(v)|\ge\delta/2\). On the other hand, if \(\delta>\delta_\mathrm{max}\), it is acceptable to output either such (_u,v_), if existed, or "FAIL".

We first describe a useful object that will shortly help us design an algorithm for `FindLongEdge`. Let \(\ell\) be an arbitrary positive integer. We call \(A=((p_1,q_1),\dots,(p_\ell,q_\ell))\) an _assignment_ iff for each _i_ we have \((p_i,q_i)\in\{1,2,3\}\times\{1,2\}\) and \(p_i\neq p_{i+1}\). We say a pair \((i,j)\in[\ell]^2\) is _matched_ by _A_ iff _p<sub>i</sub>=p<sub>j</sub>_ and \(q_i\neq q_j\). By the description of assignments, we notice that any pairs (_i,j_) with \(|i-j|\le 1\) is never matched. The following claim shows that all remaining pairs can be matched at least once if we are allowed to have \(O(\mathrm{log}\ell)\) assignments.

**Claim 5.7.** _There exists a set of_ \(t=O(\mathrm{log}\ell)\) _assignments_ A={_A_<sup>(1)</sup>_,...,A_<sup>(_t_)</sup>} _such that every pair_ \((i,j)\in[\ell]^2\) _with_ \(|i-j|\ge 2\) _is matched by at least one assignment among_ A.

