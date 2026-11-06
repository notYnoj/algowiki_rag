**Running Time:** For Step 1 note that Lemma 8 runs in expected time \(\widetilde{O}(n+M/q)=\widetilde{O}(T)\). Step 2 can be easily seen to run in time _O_((_n/m_)<sup>2</sup>)=_O(T_) by our choice of \(m=n/\sqrt{T}\). This finishes the proof.

**Remark 14.** _Our Algorithm 2 is similar to \[24, Algorithm 3\], which works as follows. For each block_ (_i,j), their algorithm selects a random symbol_ \(\sigma\) _and uses the minimum of the frequencies_ \(\#_\sigma(x_i),\#_\sigma(y_j)\) _as the estimate_ \(\widetilde{L}_{ij}\)_. It can be shown that this yields_ \(\mathbb{E}[\widetilde{L}_{ij}]=M_{ij}/(2m)\)_, which is a similar lower bound as provided by Lemma 8, but only in expectation. The summation_ \(\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\) _over a block sequence_ S _then allows to apply concentration inequalities to obtain a w.h.p. error guarantee, assuming_ \(\mu\gg m^2\).

_However, in the regime_ \(\mu\le m^2\) _the value_ \(\mu\) _could be dominated by a single block with_ \(M_{ij}\approx\mu\)_. In this case, we cannot hope to get concentration by summing over many blocks. Thus, picking a random symbol per block does not suffice to obtain a w.h.p. error guarantee._

_Since our improved approximation ratio makes it necessary to use Algorithm 2 in the regime_ \(\mu\checkmark m^2\)_, their algorithm is not sufficient in our context. Thus, we replace sampling a single symbol by our new Lemma 8._

## 5.4 Algorithm 3: Large _L_, Small \(\mu\) and Large \(\lambda\)

Our next algorithm works well if \(\mu\) is small (i.e., every block sequence has a small total number of matching pairs) and \(\lambda\) is large (i.e., on average every block has a large LCS).

Let us start with the intuition. The idea is to _pick some diagonal_ D_<sub>d</sub> and run the basic approximation algorithm (Lemma 4) with approximation ratio_ \(\beta=max\{1,\mu/T\}\) _on each block along the diagonal._ Since every diagonal is a block sequence, we have \(\sum_{(i,j)\in\mathcal{D}_d}M_{ij}\le\mu\), which bounds the running time of this algorithm by \(\widetilde{O}(n+\sum_{(i,j)\in\mathcal{D}_d}M_{ij}/\beta)=\widetilde{O}(T)\). Moreover, this algorithm produces an estimate \(\widetilde{L}\le L\) that w.h.p. satisfies<tbc>

\(\widetilde{L}\ge\sum_{(i,j)\in\mathcal{D}_d}L_{ij}/\beta.\)

<tbc>Since \(\sum_d\sum_{(i,j)\in\mathcal{D}_d}L_{ij}=\sum_{i,j}L_{ij}=\lambda\) and there are _O(n/m_) diagonals, on average a diagonal D_<sub>d</sub>_ satisfies \(\sum_{(i,j)\in\mathcal{D}_d}L_{ij}=\Omega(\lambda m/n)=\Omega(\lambda/\sqrt{T})\). If we pick an above-average diagonal, then we obtain an estimate

\(\widetilde{L}\ge\sum_{(i,j)\in\mathcal{D}_d}L_{ij}/\beta=\Omega\big(\frac{\lambda}{\sqrt{T}\beta}\big)=\Omega\big(min\big\{\frac{\lambda}{\sqrt{T}},\frac{\lambda\sqrt{T}}{\mu}\big\}\big).\)

If \(\lambda\) is large and \(\mu\) is small, then this is a good estimate.

The main difficulty in translating this idea to an actual algorithm is how to pick the diagonal. A natural approach is to pick a random diagonal, as then the _expected_ LCS sum of the diagonal is sufficiently large. However, in situations where the diagonal sums are highly unbalanced, so that \(\lambda\) is dominated by very few diagonals that have a very large LCS sum, a random diagonal is unlikely to have an above-average LCS sum. In this situation, a random diagonal works only with negligible probability.

Therefore, we need a sampling process that favors diagonals with large LCS sum. To this end, we first "guess" a value _g_ such that the sum \(\lambda\) is dominated by summands \(L_{ij}=\Theta(g)\). We call blocks (_i,j_) with \(L_{ij}=\Omega(g)\) _good._ Next we sample a random good block (_i_<sub>0</sub>_,j_<sub>0</sub>); for this we simply keep sampling random _i,j_ until we find a good block. Finally, we pick the diagonal D_<sub>d</sub>_ containing the "seed" block (_i_<sub>0</sub>_,j_<sub>0</sub>) and run the above algorithm on this diagonal. This sampling procedure favors diagonals with large LCS sum, because such diagonals contain more good blocks (_i,j_) to start from, and thus we are more likely to pick the "seed" (_i_<sub>0</sub>_,j_<sub>0</sub>) in a diagonal with large LCS sum. This yields the following result.

**Theorem 15** (Algorithm 3)**.** _We can compute in expected time_ \(\widetilde{O}(T)\) _an estimate_ \(\widetilde{L}\le L\) _that w.h.p. satisfies_<tbc>

\(\widetilde{L}=\widetilde{\Omega}\big(min\big\{\frac{\lambda}{\sqrt{T}},\frac{\lambda\sqrt{T}}{\mu}\big\}\big).\)

