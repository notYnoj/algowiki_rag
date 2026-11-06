<tbc>and thus

\(|V_\text{bad}(V')|\le k|\mathcal{E}_\text{bad}(V')|\le\frac{2}{\varepsilon_1-\eta}|\text{HD}(V')|.\) □

Now we can prove Property 3.11. The following two results are adapted from \[HWY23, Lemma 4.4 & Corollary 4.2\] using our parameters.

**Proposition A.13.** _For any fixed k and_ \(\alpha\)_, assume_ \(\eta,\rho,p_1,\varepsilon_1\) _are parameters satisfying_ \(\eta k\ge 4\), \(\mathrm{e}(\rho k\alpha)^\eta\le 1\), \(\varepsilon_1\ge\eta+1/k\) _and_ \(6k^5\le p_1\le\mathrm{e}^{k-2}\alpha\)_. Then with probability_ 1-_o_(1_/n_) _over the choice of random formula_ \(\Phi\)_, for any_ \(V'\subseteq V\) _of size_ \(|V'|\ge\mathrm{log}n\) _connected in_ \(H_\Phi=(V,\mathcal{E})\)_, it holds that_ \(|V'\cap V_\text{bad}|\le\frac{12k^5}{(\varepsilon_1-\eta)p_1}|V'|\).

_Proof._ Let \(V_1,V_2,\dots,V_\ell\) be connected components in \(H_\Phi[V_\text{bad}]\) that intersects \(V'\), and let

\(\tilde{V}=V'\cup V_1\cup V_2\cup\cdots\cup V_\ell.\)

Note that \(\tilde{V}\) is connected in \(H_\Phi\), and \(\text{HD}(\tilde{V})=\text{HD}(V_1)\cup\text{HD}(V_2)\cup\cdots\cup\text{HD}(V_\ell)\).

By Lemma A.12, we have \(|V_i|\le 2|\text{HD}(V_i)|/(\varepsilon_1-\eta)\). By Proposition A.8, we have \(\left|\text{HD}(\tilde{V})\right|\le 6k^5\left|\tilde{V}\right|/p_1\). Thus, it follows that<tbc>

\(\left|\tilde{V}\cap V_\text{bad}\right|=\sum_{i=1}^\ell|V_i|\le\frac{2}{\varepsilon_1-\eta}\sum_{i=1}^\ell|\text{HD}(V_i)|\le\frac{2}{\varepsilon_1-\eta}\cdot\frac{6k^5\left|\tilde{V}\right|}{p_1}.\)

<tbc>Since \(\tilde{V}\backslash V'\subseteq V_\text{bad}\), we conclude that

\(\frac{|V'\cap V_\text{bad}|}{|V'|}\le\frac{|V'\cap V_\text{bad}|+\left|\tilde{V}\backslash V'\right|}{|V'|+\left|\tilde{V}\right|}=\frac{\left|\tilde{V}\cap V_\text{bad}\right|}{\left|\tilde{V}\right|}\le\frac{12k^5}{(\varepsilon_1-\eta)p_1}.\) □

As a corollary, we obtain the proof of Property 3.11.

**Lemma A.14.** _For any fixed k and_ \(\alpha\)_, assume_ \(\eta,\rho,p_1,\varepsilon_1\) _are parameters satisfying_ \(\eta k\ge 4\), \(\mathrm{e}(\rho k\alpha)^\eta\le 1\), \(\varepsilon_1\ge\eta+1/k\) _and_ \(6k^5\le p_1\le\mathrm{e}^{k-2}\alpha\)_. Then with probability_ 1-_o_(1_/n_) _over the choice of random formula_ \(\Phi\)_, for any_ \(\mathcal{E}'\subseteq\mathcal{E}\) _of size_ \(|\mathcal{E}'|\ge\mathrm{log}n\) _connected in the line graph of_ \(H_\Phi=(V,\mathcal{E})\) _(namely, connected in_ \(G_\Phi\)_), it holds that_ \(|\mathcal{E}'\cap\mathcal{E}_\text{bad}|\le\frac{12k^5}{(1-\eta)(\varepsilon_1-\eta)p_1}|\mathcal{E}'|\)_. In particular,_ \(H_\Phi\) _satisfies Property 3.11 if_ \(\varepsilon_1=2\eta\) _and_ \(\varepsilon_2=\frac{12k^5}{(1-\eta)\eta p_1}\).

_Proof._ Let \(V'=\cup_{e\in\mathcal{E}^\prime} e\). Clearly, \(V'\) is connected in \(H_\Phi\), and \(|V'|\le k|\mathcal{E}'|\).

We first assume that \(|\mathcal{E}'|\le\rho|\mathcal{E}|\). Then Lemma A.3 applies. It implies that \(|V'|\ge(1-\eta)k|\mathcal{E}'|\ge\mathrm{log}n\), and thus Proposition A.13 applies. Therefore, we obtain<tbc>

\(|V'\cap V_\text{bad}|\le\frac{12k^5}{(\varepsilon_1-\eta)p_1}|V'|\le\frac{12k^6}{(\varepsilon_1-\eta)p_1}|\mathcal{E}'|.\)

<tbc>Note that, each hyperedge in \(\mathcal{E}'\cap\mathcal{E}_\text{bad}\) is a subset of \(V'\cap V_\text{bad}\). Applying Lemma A.3 again, we have<tbc>

\(|\mathcal{E}'\cap\mathcal{E}_\text{bad}|\le\frac{|V'\cap V_\text{bad}|}{(1-\eta)k}\le\frac{12k^5}{(1-\eta)(\varepsilon_1-\eta)p_1}|\mathcal{E}'|.\)

<tbc>Now we consider the case where \(|\mathcal{E}'|>\rho|\mathcal{E}|\). Again, note that each hyperedge in \(\mathcal{E}'\cap\mathcal{E}_\text{bad}\) is a subset of _V_bad, and \(|V_\text{bad}|\le 2\mathrm{e}^{-k}\alpha^{-2}|V|/(\varepsilon_1-\eta)<\rho|\mathcal{E}|/((1-\eta)k)\) by Proposition A.2 and Lemma A.12 if we set \(\eta\ge 4/k\) and \(\mathrm{e}(\rho k\alpha)^\eta=1\). So Lemma A.3 applies to _V_bad, and we conclude that

\(|\mathcal{E}'\cap\mathcal{E}_\text{bad}|\le\frac{|V_\text{bad}|}{(1-\eta)k}\le\frac{2|\mathcal{E}|}{\mathrm{e}^kk\alpha^3(1-\eta)(\varepsilon_1-\eta)}<\frac{12k^5}{(1-\eta)(\varepsilon_1-\eta)p_1}|\mathcal{E}'|.\) □

Finally, it is a direct corollary of Property 3.11 that \(H_\Phi\) has no connected components of size \(\ell\ge\mathrm{log}n\) in the line graph induced by bad hyperedges.

