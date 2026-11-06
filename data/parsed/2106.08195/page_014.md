_Proof._ Note that the theorem statement is trivial if \(\lambda\le\sqrt{T}\). Indeed, in time _O(n_) we can compute _M=M(x,y_). If _M_=0 then \(L=\lambda=0\) and we return \(\widetilde{L}=0\). If \(M\ge 1\), then we return \(\widetilde{L}=1\). This ensures \(\widetilde{L}\le L\), since any matching pair gives a common subsequence of length 1. Moreover, in case \(\lambda\le\sqrt{T}\) the returned value \(\widetilde{L}=1\) satisfies the approximation guarantee \(\widetilde{L}=\Omega(\lambda/\sqrt{T})\). Therefore, we can assume

\(\lambda>\sqrt{T}.\) (4)

Algorithm 3 repeats the following procedure _O_(log_n_) times to boost its success probability.

1. Repeat the following for _g_ being any power of two with \(max\{1,\hat{\lambda}/(4T)\}\le g\le m\):<tbc>

2. _Sampling a good block:_ Pick a random set of blocks \(\mathcal{R}\subseteq[n/m]^2\) of size \(O\big((gT/\hat{\lambda})log^2n\big)\). For each block \((i,j)\in\mathcal{R}\), test whether \(L_{ij}\ge g\) using our basic decision algorithm (Lemma 5). If no test was successful, then set \(\widetilde{L}(g)=0\) and continue with the next value of _g_. Otherwise, pick a random successfully tested block (_i_<sub>0</sub>_,j_<sub>0</sub>) and proceed to Step 3.<tbc>

3. _Approximating along a diagonal:_ Let D be the diagonal containing the block (_i_<sub>0</sub>_,j_<sub>0</sub>). For each \((i,j)\in\mathcal{D}\): Run our basic approximation algorithm (Lemma 4) with approximation ratio \(\beta=max\{1,\hat{\mu}/T\}\) on _x<sub>i</sub>,y<sub>j</sub>_ to obtain an estimate \(\widetilde{L}_{ij}\). Finally, \(\widetilde{L}(g)=\sum_{(i,j)\in\mathcal{D}}\widetilde{L}_{ij}\) is the result of iteration _g_.<tbc>

4. Return \(\widetilde{L}=max_g\widetilde{L}(g)\).

### Upper Bound:

Again it is easy to see that \(\widetilde{L}\le L\), since Lemma 4 yields \(\widetilde{L}_{ij}\le L_{ij}\).

### Approximation Guarantee:

Let B_<sub>g</sub>_ be the set of all blocks (_i,j_) with \(g\le L_{ij}\le 2g\).

**Claim 16.** _If_ \(\lambda/2\le\hat{\lambda}\le\lambda\) _then for some power of two g with_ \(max\{1,\hat{\lambda}/(4T)\}\le g\le m\) _we have_<tbc>

\(g\cdot|\mathcal{B}_g|=\Omega(\lambda/logm).\) (5)

<tbc>_Proof._ Write _G_ for the set of all powers of two _g_ with \(max\{1,\hat{\lambda}/(4T)\}\le g\le m\). Note that blocks (_i,j_) with \(L_{ij}\le\frac{\lambda}{2T}\) in total contribute at most \(\lambda/2\) to \(\lambda=\sum_{i,i}L_{ij}\), since the total number of blocks is (_n/m_)<sup>2</sup>=_T_. Hence, the blocks with \(L_{ij}>\frac{\lambda}{2T}\) contribute at least \(\lambda/2\), that is,<tbc>

\(\frac{\lambda}{2}\le\sum_{i,jL_{ij}>\lambda/(2T)}L_{ij}.\)

<tbc>Note that the sets B_<sub>g</sub>_ for powers of two \(g\ge max\{1,\lambda/(4T)\}\ge max\{1,\hat{\lambda}/(4T)\}\) cover all blocks with \(L_{ij}>\frac{\lambda}{2T}\). Moreover, the sets B_<sub>g</sub>_ are empty for _g\>m_. Therefore, the blocks with \(L_{ij}>\frac{\lambda}{2T}\) are covered by the sets B_<sub>g</sub>_ with \(g\in G\), that is,

\(\frac{\lambda}{2}\le\sum_{i,jL_{ij}>\hat{\lambda}/(2T)}L_{ij}\le\sum_{g\in G}\sum_{(i,j)\in\mathcal{B}_g}L_{ij}\le\sum_{g\in G}2g|\mathcal{B}_g|.\)

If for all _g_ appearing in the sum on the right hand side we would have \(g\cdot|\mathcal{B}_g|<\lambda/(4logm+4)\) then the right hand side would be less than \(\lambda/2\), so we would obtain a contradiction. This proves the claim.

In the following we focus on an iteration of Step 1 in which we pick a value of _g_ as promised by Claim 16.

We call a block (_i,j_) _good_ if \(L_{ij}\ge g\), and _bad_ otherwise. Note that any \((i,j)\in\mathcal{B}_g\) is good, but not every good block is in B_<sub>g</sub>_. In Step 2, we claim that the set R w.h.p. contains at least one good block, assuming<tbc>

