If \(|\mathcal{E}'|\le\rho m\), then by Proposition A.7, it follows that<tbc>

\(\frac{k|\mathcal{E}'|}{2}\le\left|\Gamma_{H_\Phi}^+(V')\right|\le 3k^4\alpha max\{|V'|,klogn\}\le 3k^5\alpha|V'|.\)

<tbc>Combining with (21), it yields that \(|\mathcal{E}'|\le 6k^4\alpha|V'|\), and thus<tbc>

\(|\mathrm{HD}(V')|\le\frac{6k^5}{p_1}|V'|.\)

<tbc>If \(|\mathcal{E}'|>\rho m\), using Proposition A.7 again, we obtain<tbc>

\(\frac{k\rho m}{2}\le\left|\Gamma_{H_\Phi}^+(V')\right|\le 3k^4\alpha max\{|V'|,klogn\}\le 3k^5\alpha|V'|,\)

<tbc>which gives<tbc>

\(|V'|\ge\frac{k\rho m}{6k^5\alpha}=\frac{n}{6\mathrm{e}^2k^5\alpha}.\)

<tbc>On the other hand, it is clear that \(|\mathrm{HD}(V')|\le|\mathrm{HD}(V)|\le\mathrm{e}^{-k}\alpha^{-2}n\) by Proposition A.2. So we obtain that

\(|\mathrm{HD}(V')|\le\frac{6\mathrm{e}^2k^5\alpha}{\mathrm{e}^k\alpha^2}|V'|\le\frac{6k^5}{p_1}|V'|.\) □

The following result is adapted from \[COF14, Lemma 2.4\] and \[HWY23, Lemma A.2\], but uses tighter parameters.

**Proposition A.9.** _Assume_ \(k\ge 12\), \(q\ge 2\) _and_ \(\alpha\le q^k\) _are constants. Then with probability_ 1-_o_(1_/n_) _over the random formula_ \(\Phi\)_, the following holds for_ \(H_\Phi=(V,\mathcal{E})\)_: Fix an arbitrary_ \(\mathcal{E}'\subseteq\mathcal{E}\) _of size_ \(|\mathcal{E}'|\le 4^{-k}\alpha^{-1/2}n\)_. Let_ \(e_{i_1},\dots,e_{i_\ell}\in\mathcal{E}\backslash\mathcal{E}'\) _be hyperedges of distinct indices. For each_ \(s\in[\ell]\)_, define_ \(V_s=(\bigcup_{e\in\mathcal{E}^\prime} e)\cup(\bigcup_{j=1}^{s-1}e_{i_j})\)_. If_ \(|e_{i_s}\cap V_s|\ge 6\) _holds for all_ \(s\in[\ell]\)_, then_ \(\ell\le|\mathcal{E}'|\).

_Proof._ We prove the statement by contradiction. Hence, assume that \(\mathcal{E}'\) and \(e_{i_1},\dots,e_{i_\ell}\) violate the statement for \(\ell>|\mathcal{E}'|\). We can discard additional clauses from \(\mathcal{E}'\) and in fact, assume that \(\ell=|\mathcal{E}'|+1\) for which the statement is violated. Further, observe that we can assume that \(|\mathcal{E}'|\le m-\ell\). Define \(\varepsilon>0\) such that \(\ell=\lfloor\varepsilon n\rfloor+1\). Since \(|\mathcal{E}'|\ge 1\), we have that \(\varepsilon\ge\frac{1}{n}\). From the bound on \(|\mathcal{E}'|\), we get that \(\varepsilon\le 4^{-k}\alpha^{-1/2}+\frac{1}{n}\).

Define \(Y:=\bigcup_{j=1}^{j=\ell}\mathrm{vbl}(e_{i_j})\backslash\bigcup_{e\in\mathcal{E}^\prime}\mathrm{vbl}(e)\). Then, the following are true:

\(\bullet\) \(|Y|=\sum_{r=1}^{r=\ell}|\mathrm{vbl}(e_{i_r})|-|\mathrm{vbl}(e_{i_r})\cap V_r|\le(k-6)\ell\);<tbc>

\(\bullet\) There is a \(\tilde{\mathcal{E}}\subset\mathcal{E}\backslash\mathcal{E}'\) such that \(|\tilde{\mathcal{E}}|=\ell\) and \(\mathrm{vbl}(\tilde{e})\subseteq Y\cup\bigcup_{e\in\mathcal{E}^\prime}\mathrm{vbl}(e)\) for all \(e\in\tilde{\mathcal{E}}\). For this, we can just take \(\tilde{\mathcal{E}}=\{e_{i_1},\dots,e_{i_\ell}\}\).

Now, consider fixed \(\mathcal{E}',Y,\tilde{\mathcal{E}}\) such that \(|Y|=t\le(k-6)\ell\), \(|\tilde{\mathcal{E}}|=\ell\) and \(|\mathcal{E}'|=\mathrm{min}\{m-\ell,\ell-1\}\). Define \(\mathcal{A}(\mathcal{E}',Y,\tilde{\mathcal{E}})\) to be the event that \(\mathrm{vbl}(\tilde{\mathcal{E}})\subset Y\cup\mathrm{vbl}(\mathcal{E}')\). We have that<tbc>

\(\mathbf{Pr}\left[\mathcal{A}(\mathcal{E}',Y,\tilde{\mathcal{E}})\right]\le\left(\frac{k|\mathcal{E}'|+|Y|}{n}\right)^{k\tilde{\mathcal{E}}}\le\left(\frac{k(\ell-1)+(k-6)\ell}{n}\right)^{k\ell}\le(4k\varepsilon)^{k\ell}.\)

<tbc>The last inequality follows from the fact that \(\ell\le\varepsilon n+1\le 2\varepsilon n\). Now, by union bound over all choices of \((\mathcal{E}',Y,\tilde{\mathcal{E}})\), we get that

\(\mathbf{Pr}\left[\exists\text{such an}(\mathcal{E}',Y,\tilde{\mathcal{E}})\right]\le\sum_{t=1}^{t=k-6}\genfrac(){pt}{2}{m}{\ell-1}\cdot\genfrac(){pt}{2}{m}{\ell}\cdot\genfrac(){pt}{2}{n}{t}(4k\varepsilon)^{k\ell}.\)

We can upper bound both \(\genfrac(){pt}{2}{m}{\ell}\) and \(\genfrac(){pt}{2}{m}{\ell-1}\) by \((\frac{\varepsilon m}{\ell-1})^\ell\). Further, \((k-6)\ell\le(k-6)(\varepsilon n+1)\le 2k\varepsilon n\le n/2\) if we assume \(\varepsilon\le 1/(4k)\). But we have that \(\varepsilon\le 4^{-k}\alpha^{-1/2}+\frac{1}{n}\) and we can use that \(k\ge 12\). Then,<tbc>

