common neighbors. Note that any \((\sigma,\ell,r)\in U_{ij}\) represents all matching pairs of symbol \(\sigma\) in _x<sub>i</sub>_ and _y<sub>j</sub>_, and the number of these matching pairs is \(\#_\sigma(x_i)\cdot\#_\sigma(y_j)\in[2^{\ell+r},2^{\ell+r+2})\).<tbc>

2. _Subsampling:_ We sample a subset \(\widetilde{U}\subseteq U\) by removing each node \((\sigma,\ell,r)\in U\) independently with probability \(1-p_{\ell,r}\), where \(p_{\ell,r}:=min\{1,2^{\ell+r+3}/q\}\).<tbc>

3. _Determine Common Neighbors:_ For each \((\sigma,\ell,r)\in\widetilde{U}\) enumerate all pairs of neighbors \(i\in L\) and \(j\in R\). For each such 2-path, add \((\sigma,\ell,r)\) to an initially empty set \(\widetilde{U}_{ij}\). This step computes the sets \(\widetilde{U}_{ij}:=U_{ij}\cap\widetilde{U}\) in time proportional to their total size.<tbc>

4. _Output:_ Return the values \(\widetilde{M}_{ij}:=\sum_{(\sigma,\ell,r)\in\widetilde{U}_{ij}}2^{\ell+r}/p_{\ell,r}\).<tbc>

<tbc>**Correctness:** To analyze this algorithm, we consider the numbers \(\overline{M_{ij}}:=\sum_{(\sigma,\ell,r)\in U_{ij}}2^{\ell+r}\). Observe that we have \(\overline{M_{ij}}\le M_{ij}\le 4\overline{M_{ij}}\), since each \((\sigma,\ell,r)\in U_{ij}\) corresponds to at least \(2^{\ell+r}\) and at most \(2^{\ell+r+2}\) matching pairs of _x<sub>i</sub>_ and _y<sub>j</sub>_. It therefore suffices to show that \(\widetilde{M}_{ij}\) is close to <o>_M_</o><sub>ij</sub>. Using Bernoulli random variables \(\mathrm{Ber}(p_{\ell,r})\) to express whether \((\sigma,\ell,r)\) survives the subsampling, we write<tbc>

\(\widetilde{M}_{ij}=\sum_{(\sigma,\ell,r)\in U_{ij}}\frac{2^{\ell+r}}{p_{\ell,r}}\cdot\mathrm{Ber}(p_{\ell,r}).\)

<tbc>This yields an expected value of \(\mathbb{E}[\widetilde{M}_{ij}]=\overline{M_{ij}}\), so by Markov’s inequality we obtain \(\widetilde{M}_{ij}\le 4\overline{M_{ij}}\le 4M_{ij}\) with probability at least 3/4. Since \(\widetilde{M}_{ij}\) is a linear combination of independent Bernoulli random variables, we can also easily express its variance as<tbc>

\(\mathbb{V}[\widetilde{M}_{ij}]=\sum_{(\sigma,\ell,r)\in U_{ij}}\big(2^{\ell+r}/p_{\ell,r}\big)^2\cdot p_{\ell,r}(1-p_{\ell,r})=\sum_{(\sigma,\ell,r)\in U_{ij}}2^{\ell+r}\cdot 2^{\ell+r}\big(\frac{1}{p_{\ell,r}}-1\big).\)

<tbc>We now use the definition of \(p_{\ell,r}:=min\{1,2^{\ell+r+3}/q\}\) to bound<tbc>

\(2^{\ell+r}\big(\frac{1}{p_{\ell,r}}-1\big)=2^{\ell+r}\big(max\big\{1,\frac{q}{2^{\ell+r+3}}\big\}-1\big)=max\{0,q/8-2^{\ell+r}\}\le q/8.\)

<tbc>This yields \(\mathbb{V}[\widetilde{M}_{ij}]\le\overline{M_{ij}}q/8\). We now use Chebychev’s inequality \(\mathrm{Pr}[X<\mathbb{E}[X]-\lambda]\le\mathbb{V}[X]/\lambda^2\) on \(\lambda=0.5\mathbb{E}[X]\) and \(X=\widetilde{M}_{ij}\) to obtain

\(\mathrm{Pr}[\widetilde{M}_{ij}<\overline{M_{ij}}/2]\le\frac{q}{2\overline{M_{ij}}}.\)

In case \(M_{ij}\ge 8q\), we have \(\overline{M_{i,j}}\ge M_{ij}/4\ge 2q\) and hence \(\mathrm{Pr}[\widetilde{M}_{ij}\ge M_{ij}/8]\ge\mathrm{Pr}[\widetilde{M}_{ij}\ge\overline{M_{ij}}/2]\ge 3/4\). Otherwise, in case _M<sub>ij</sub>\<_8_q_, we can only use the trivial \(\widetilde{M}_{ij}\ge 0>M_{ij}/8-q\).

Hence, each inequality \(\widetilde{M}_{ij}\le 4M_{ij}\) and \(\widetilde{M}_{ij}\ge M_{ij}/8-q\) individually holds with probability at least 3/4. Finally, we boost the success probability by repeating the above algorithm _O_(log_n_) times and returning for each _i,j_ the median of all computed values \(\widetilde{M}_{ij}\).

**Running Time:** Steps 1 and 2 can be easily seen to run in time \(\widetilde{O}(n)\). Steps 3 and 4 run in time proportional to the total size of all sets \(\widetilde{U}_{ij}\), which we claim to be at most 8_M/q_ in expectation. Over _O_(log_n_) repetitions, we obtain a total expected running time of \(\widetilde{O}(n+M/q)\). (We remark that here we consider a succinct output format, where only the non-zero numbers \(\widetilde{M}_{ij}\) are listed; otherwise additional time of \(\widetilde{O}((n/m)^2)\) is required to output the numbers \(\widetilde{M}_{ij}=0\).)

