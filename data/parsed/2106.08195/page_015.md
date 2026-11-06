that our guess \(\hat{\lambda}\) is correct up to constant factors. Indeed, since the set B_<sub>g</sub>_ is a subset of the good blocks, the probability that \(\Theta((gT/\lambda)\mathrm{log}^2n)\) sampled blocks do not contain any good block is at most

\(\left(1-\frac{|\mathcal{B}_g|}{(n/m)^2}\right)^{\Theta((gT/\lambda)\mathrm{log}^2n)}\le^{(5)}\left(1-\frac{\lambda}{gT\mathrm{log}m}\right)^{\Theta((gT/\lambda)\mathrm{log}^2n)}\le\mathrm{exp}(-\Theta(\mathrm{log}n)),\)

which is negligible. For any bad block \((i,j)\in\mathcal{R}\) the test \(L_{ij}\ge g\) is unsuccessful, as Lemma 5 has no false positives. For any good block \((i,j)\in\mathcal{R}\) w.h.p. the test is successful, and w.h.p. there is at least one good block in R. It follows that w.h.p. Step 2 finds a good block (_i_<sub>0</sub>_,j_<sub>0</sub>) and proceeds to Step 3. Observe that (_i_<sub>0</sub>_,j_<sub>0</sub>) is chosen uniformly at random from all good blocks.

We call a diagonal _good_ if it contains at least \(\frac{|\mathcal{B}_g|m}{4n}\) good blocks, and _bad_ otherwise. Since there are _\<_2_n/m_ non-empty diagonals, the number of good blocks contained in bad diagonals is at most |B_<sub>g</sub>|/_2, which is at most half of all good blocks. Therefore, at least half of all good blocks are contained in good diagonals. It follows that the uniformly random good block (_i_<sub>0</sub>_,j_<sub>0</sub>) lies in a good diagonal with probability at least 1/2.

Hence, with probability at least 1/2-_o_(1) the diagonal D considered in Step 3 is good, that is, it contains at least \(\frac{|\mathcal{B}_g|m}{4n}\) blocks (_i,j_) with \(L_{ij}\ge g\). Since the approximations \(\widetilde{L}_{ij}\) computed in Step 3 w.h.p. satisfy \(\widetilde{L}_{ij}\ge L_{ij}/\beta\), we obtain<tbc>

\(\widetilde{L}\ge\widetilde{L}(g)\ge\frac{|\mathcal{B}_g|m}{4n}\cdot\frac{g}{\beta}.\)

<tbc>Inequality (5) and the definitions \(m=n/\sqrt{T}\) and \(\beta=\mathrm{max}\{1,\hat{\mu}/T\}\) now yield

\(\widetilde{L}=\widetilde{\Omega}\big(\mathrm{min}\big\{\frac{\lambda}{\sqrt{T}},\frac{\lambda\sqrt{T}}{\hat{\mu}}\big\}\big).\)

If our guess \(\hat{\mu}\approx\mu\) is correct up to a constant factor, then this yields the claimed approximation guarantee. Returning the maximum over _O_(log_n_) independent repetitions of this algorithm improves the success probability from 1/2-_o_(1) to w.h.p.

**Running Time:** By Lemma 5, the test \(L_{ij}\ge g\) runs in expected time \(\widetilde{O}((m+M_{ij})L_{ij}/g+m/g)=\widetilde{O}(m^2L_{ij}/g+m/g)\). Note that in expectation for random _i,j_ we have \(\mathbb{E}[L_{ij}]=\lambda/(n/m)^2=\lambda/T\). Therefore, the expected running time of one test is bounded by \(\widetilde{O}\big(\frac{n^2\lambda}{gT}+m/g\big)\). As Step 2 performs \(O\big((gT/\hat{\lambda})\mathrm{log}^2n\big)\) such tests, its expected running time is \(\widetilde{O}(m^2+mT/\lambda)\), assuming that our guess \(\hat{\lambda}\approx\lambda\) is correct up to a constant factor. We now use \(m^2=n^2/T\le T\) from \(n\le T\) and \(\lambda\ge\sqrt{T}\ge n/\sqrt{T}=m\) from (4) and \(n\le T\), to bound the expected running time of Step 2 by \(\widetilde{O}(T)\).

For Step 3, the expected running time is \(\widetilde{O}(n+\sum_{(i,j)\in\mathcal{D}}M_{ij}/\beta)\). Since D is a block sequence, we have \(\sum_{(i,j)\in\mathcal{D}}M_{ij}\le\mu\). Using \(\beta\ge\hat{\mu}/T=\Omega(\mu/T)\) (if our guess \(\hat{\mu}\approx\mu\) is correct up to a constant factor) we can bound the expected time by \(\widetilde{O}(n+T)=\widetilde{O}(T)\).

Over the _O_(log_n_) iterations of Step 1 and the _O_(log_n_) repetitions for boosting the success probability, the expected running time is still \(\widetilde{O}(T)\).

## 5.5 Algorithm 4: Large _L_, Small \(\mu\), and Small \(\lambda\)

Our next algorithm works well if \(\mu\) is small (i.e., every block sequence has a small total number of matching pairs), \(\lambda\) is small (i.e., on average every block has a small LCS), and _L_ is large (i.e., there is a long LCS). The goal of this algorithm is to detect a sufficiently large random subset of the block sequence G from Lemma 11. To this end, we first sample a random set of blocks R containing each block \((i,j)\in[n/m]^2\) with probability _p_. Then we use our basic decision algorithm to detect the blocks \((i,j)\in\mathcal{R}\) with \(L_{ij}\ge\frac{\hat{L}}{4\sqrt{T}}\), and for these<tbc>

