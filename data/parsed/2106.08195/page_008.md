It remains to prove the claimed bound of \(\mathbb{E}[\sum_{i,j}|\tilde{U}_{ij}|]\le 8M/q\). Since \(2^{\ell+r}/p_{\ell,r}=max\{2^{\ell+r},q/8\}\ge q/8\), from the definition of \(\widetilde{M}_{ij}=\sum_{(\sigma,\ell,r)\in\tilde{U}_{ij}}2^{\ell+r}/p_{\ell,r}\) we infer \(\widetilde{M}_{ij}\ge\frac{q}{8}|\tilde{U}_{ij}|\). Therefore,

\(\mathbb{E}\big[\sum_{i,j}|\tilde{U}_{ij}|\big]\le\mathbb{E}\big[\frac{8}{q}\sum_{i,j}\widetilde{M}_{ij}\big]=\frac{8}{q}\sum_{i,j}\overline{M_{ij}}\le\frac{8}{q}\sum_{i,j}M_{ij}=\frac{8M}{q}.\)

## 4.3 Single Symbol Approximation Algorithm

For strings _x,y_ that have a large number of matchings pairs _M=M(x,y_), some symbol must appear often in _x_ and in _y_. This yields a common subsequence using (several repetitions of) a single alphabet symbol.

**Lemma 7** (Cf. Lemma 6.6.(ii) in \[20\] or Algorithm 3 in \[24\])**.** _For any_ \(x,y\in\Sigma^n\) _there exists a symbol_ \(\sigma\in\Sigma\) _that appears at least_ \(\frac{M}{2n}\) _times in x and in y. Therefore, in time_ \(\widetilde{O}(n)\) _we can compute a common subsequence of x,y of length at least_ \(\frac{M}{2n}\)_. In particular, we can compute a value_ \(\widetilde{L}\le L\) _that satisfies_ \(\widetilde{L}\ge\frac{M}{2n}\).

_Proof._ Let _k_ be maximal such that some symbol \(\sigma\in\Sigma\) appears at least _k_ times in _x_ and at least _k_ times in _y_. Let \(\Sigma^w:=\{\sigma\in\Sigma|\#_\sigma(w)\le k\}\) for \(w\in\{x,y\}\). Since no symbol appears more than _k_ times in _x_ and in _y_, we have \(\Sigma^x\cup\Sigma^y=\Sigma\). We can thus bound

\(M=M(x,y)=\sum_{\sigma\in\Sigma}\#_\sigma(x)\cdot\#_\sigma(y)\le\sum_{\sigma\in\Sigma^x}k\cdot\#_\sigma(y)+\sum_{\sigma\in\Sigma^y}\#_\sigma(x)\cdot k\le 2kn,\)

since the frequencies \(\#_\sigma(x)\) sum up to at most _n_, and similarly for \(\#_\sigma(y)\). It follows that \(k\ge\frac{M}{2n}\). Computing _k_, and a symbol \(\sigma\in\Sigma\) attaining _k_, in time \(\widetilde{O}(n)\) is straightforward.

We devise a variant of Lemma 7 in the following setting. For strings _x_<sub>1</sub>_,...,x<sub>n/m</sub>_, \(y_1,\dots,y_{n/m}\in\Sigma^m\) we write _L<sub>ij</sub>=L(x<sub>i</sub>,y<sub>j</sub>_), _M<sub>ij</sub>=M(x<sub>i</sub>,y<sub>j</sub>_) and \(M=\sum_{i,j}M_{ij}\). We want to find for each block (_i,j_) a frequent symbol in _x<sub>i</sub>_ and _y<sub>j</sub>_, or equivalently we want to find a common subsequence of _x<sub>i</sub>_ and _y<sub>j</sub>_ using a single alphabet symbol. Similarly to Lemma 6, we relax Lemma 7 to obtain a fast running time.

**Lemma 8.** _Given_ \(x_1,\dots,x_{n/m},y_1,\dots,y_{n/m}\in\Sigma^m\) _and any q\>_0_, we can compute for each i,j a num ber_ \(\widetilde{L}_{ij}\le L_{ij}\) _such that w.h.p._ \(\widetilde{L}_{ij}\ge\frac{M_{ij}-q}{16m}\)_. The algorithm runs in total expected time_ \(\widetilde{O}(n+M/q)\).

_Proof._ We run the same algorithm as in Lemma 6, except that in Step 4 for each _i,j_ with non-empty set \(\widetilde{U}_{ij}\) we let \(\widetilde{L}_{ij}\) be the maximum of \(2^{min\{\ell,r\}}\) over all \((\sigma,\ell,r)\in\widetilde{U}_{ij}\). For each empty set \(\widetilde{U}_{ij}\), we implicitly set \(\widetilde{L}_{ij}=0\), i.e., we output a sparse representation of all non-zero values \(\widetilde{L}_{ij}\).

The running time analysis is the same as in Lemma 6.

For the upper bound on \(\widetilde{L}_{ij}\), since \(\sigma\) appears at least \(2^\ell\) times in _x<sub>i</sub>_ and at least 2_<sup>r</sup>_ times in _y<sub>j</sub>_, there is a common subsequence of _x<sub>i</sub>_ and _y<sub>j</sub>_ of length at least \(\widetilde{L}_{ij}\). Thus, we have \(\widetilde{L}_{ij}\le L_{ij}\).

For the lower bound on \(\widetilde{L}_{ij}\), fix _i,j_ and order the tuples \((\sigma,\ell,r)\in U_{ij}\) in ascending order of \(2^{min\{\ell,r\}}\), obtaining an ordering \((\sigma_1,\ell_1,r_1),\dots,(\sigma_k,\ell_k,r_k)\). For \(h\in[k]\) we let \(\mathcal{S}:=\{(\sigma_1,\ell_1,r_1),\dots,(\sigma_h,\ell_h,r_h)\}\) and \(\mathcal{L}:=\{(\sigma_h,\ell_h,r_h),\dots,(\sigma_k,\ell_k,r_k)\}\). Recall that \(\overline{M_{ij}}=\sum_{(\sigma,\ell,r)\in U_{ij}}2^{\ell+r}\), and observe that we can pick _h_ with<tbc>

\(\sum_{(\sigma,\ell,r)\in\mathcal{S}}2^{\ell+r}\ge\overline{M_{ij}}/2\text{and}\sum_{(\sigma,\ell,r)\in\mathcal{L}}2^{\ell+r}\ge\overline{M_{ij}}/2.\) (1)

<tbc>Then we have

\(\overline{M_{ij}}\le\sum_{(\sigma,\ell,r)\in\mathcal{S}}2^{\ell+r}=\sum_{(\sigma,\ell,r)\in\mathcal{S}}2^{min\{\ell,r\}}\cdot 2^{max\{\ell,r\}}\le 2^{min\{\ell_h,r_h\}}\sum_{(\sigma,\ell,r)\in\mathcal{S}}2^{max\{\ell,r\}}.\)

Note that for any \((\sigma,\ell,r)\in\mathcal{S}\) the symbol \(\sigma\) appears at least \(2^{max\{\ell,r\}}\) times in _x<sub>i</sub>_ or in _y<sub>j</sub>_, and thus the sum on the right hand side is at most 2_m_. Rearranging, this yields \(2^{min\{\ell_h,r_h\}}\ge\frac{M_{ij}}{4m}\ge\frac{M_{ij}}{16m}\), where we used \(\overline{M_{ij}}\ge M_{ij}/4\) as in the proof of Lemma 6. In particular, due to our ordering we have for any \((\sigma,\ell,r)\in\mathcal{L}\):

