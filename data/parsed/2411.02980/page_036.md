\(\bullet\) \(|\mathcal{E}''|\ge logn-1\), \(|V'|\ge|\mathcal{E}''|\), \(|\tilde{\mathcal{E}}|\ge 2k^3\alpha|V'|\), and \(\tilde{\mathcal{E}}\cap\mathcal{E}''=\emptyset\);<tbc>

\(\bullet\) Further, \(G_\Phi(\mathcal{E}'')\) is connected, \(V'\subset\bigcup_{e\in\mathcal{E}^{\prime\prime}} vbl(\mathcal{E}'')\) and \(vbl(e)\cap V'\neq\emptyset\) for all \(e\in\mathcal{E}''\).

Define \(r_1=|\mathcal{E}''|\), \(r_2=|V'|\), and \(r_3=|\tilde{\mathcal{E}}|\). Based on these observations, we define the events:

\(\bullet\) \(\mathcal{A}(\mathcal{E}'',V',\tilde{\mathcal{E}})\) to be the event when the above conditions are satisfied with \((\mathcal{E}'',V',\tilde{\mathcal{E}})\);<tbc>

\(\bullet\) \(\mathcal{A}(\mathcal{E}'')\) to be event that \(G_\Phi[\mathcal{E}'']\) is connected;<tbc>

\(\bullet\) \(\mathcal{A}(V',\tilde{\mathcal{E}})\) to be the event that \(vbl(e)\cap V'\neq\emptyset\) holds for all \(e\in\tilde{\mathcal{E}}\).

Now, using Proposition A.5, we get that<tbc>

\(\mathbf{Pr}\left[\mathcal{A}(\mathcal{E}'']\right)\le r_1^{r_1-2}\cdot\left(\frac{k^2}{n}\right)^{r_1-1}.\)

<tbc>Observe that since \(\mathcal{E}''\cap\tilde{\mathcal{E}}=\emptyset\), \(\mathcal{A}(\mathcal{E}'')\) and \(\mathcal{A}(V',\tilde{\mathcal{E}})\) are independent. Then,<tbc>

\(\mathbf{Pr}\left[\mathcal{A}(V',\tilde{\mathcal{E}})|\mathcal{A}(\mathcal{E}'')\right]=\mathbf{Pr}\left[\mathcal{A}(V',\tilde{\mathcal{E}})\right]\le\left(k\cdot\frac{r_2}{n}\right)^{r_3}.\)

<tbc>Therefore,<tbc>

\(\mathbf{Pr}\left[\mathcal{A}(\mathcal{E}'',V',\tilde{\mathcal{E}})\right]\le\mathbf{Pr}\left[\mathcal{A}(V',\tilde{\mathcal{E}})\right]\cdot\mathbf{Pr}\left[\mathcal{A}(\mathcal{E}'']\right)\le r_1^{r_1-2}\cdot\left(\frac{k^2}{n}\right)^{r_1-1}\left(k\cdot\frac{r_2}{n}\right)^{r_3}.\)

<tbc>We now use union bound over all possible (valid) sizes of \(\mathcal{E}'',V',\tilde{\mathcal{E}}\) to upper bound the probability that under the conditions mentioned above, \(r_3\ge 2k^3\alpha r_2\). We will show this is upper bounded by _o_(1_/n_), which then implies our result. By the union bound,<tbc>

\(\mathbf{Pr}\left[\exists such\mathcal{A}(\mathcal{E}'',V',\tilde{\mathcal{E}})\right]\le\sum_{r_1\ge logn-1}\sum_{r_2\ge r_1}\sum_{r_3\ge 2k^3\alpha r_2}\genfrac(){pt}{2}{m}{r_1}\genfrac(){pt}{2}{kr_1}{r_2}\genfrac(){pt}{2}{m}{r_3}r_1^{r_1-2}\cdot\left(\frac{k^2}{n}\right)^{r_1-1}\left(k\cdot\frac{r_2}{n}\right)^{r_3}.\)

<tbc>To simplify the above expression, we make following assumptions: \(\frac{\mathrm{e}k^2\alpha}{(2k^2/\mathrm{e})^{k^3\alpha}}\le\frac{1}{8}\) and \(\frac{\mathrm{e}k}{(2k^2/\mathrm{e})^{k^3\alpha}}\le\frac{1}{8}\). These assumptions are satisfied under \(k^3\alpha\ge 1\) and \(k\ge 30\). Then, we get that

\(\mathbf{Pr}\left[\exists such\mathcal{A}(\mathcal{E}'',V',\tilde{\mathcal{E}})\right]\le\frac{4n}{n^2(\mathrm{log}n-1)^2}=o(1/n).\)

For the case when \(|V'|<\lfloor k\mathrm{log}n\rfloor\), we can consider another connected set of vertices \(V''\supset V'\) such that \(|V''|=\lfloor k\mathrm{log}n\rfloor\). Applying the previous argument on \(V''\), the claim follows. □

Using Proposition A.7, We can also bound the fraction of high-degree variables in any connected set.

**Proposition A.8.** _Assume_ \(k\ge 2\), \(q\ge 2\)_, and_ \(\alpha\le q^k\) _are constants. Let p_<sub>1</sub> _be a parameter satisfying_ \(6k^5\le p_1\le\mathrm{e}^{k-2}\alpha\)_. Then with probability_ 1-_o_(1_/n_) _over the random formula_ \(\Phi\)_, the following holds for_ \(H_\Phi=(V,\mathcal{E})\)_: Let_ \(V'\subseteq V\) _be connected in_ \(H_\Phi\) _and_ \(|V'|\ge\mathrm{log}n\)_. Then_

\(|\{v\in V'|\mathrm{deg}(v)\ge p_1\alpha\}|\le 6k^5|V'|/p_1.\)

_Proof._ We prove this proposition by showing that if \(\mathrm{HD}(V')\) is too large then \(V'\) has too many neighbors, which contradicts to Proposition A.7.

We consider the number of edges that contain high-degree vertices in \(V'\). Let

\(\mathcal{E}'=\{e\in\mathcal{E}|e\cap\mathrm{HD}(V')\neq\emptyset\},\text{and}U=\bigcup_{e\in\mathcal{E}^\prime} e.\)

By setting \(\eta=1/2\) and \(\rho=\mathrm{e}^{-2}/(k\alpha)\) in Lemma A.3, we obtain that any \(\ell\le\rho m\) edges contain at least \(k\ell/2\) distinct vertices with probability 1-_o_(1_/n_). Thus, it gives that \(|U|\ge k\mathrm{min}\{|\mathcal{E}'|,\rho m\}/2\). Note that \(U=\Gamma_{H_\Phi}^+(\mathrm{HD}(V'))\subseteq\Gamma_{H_\Phi}^+(V')\). So we have \(\left|\Gamma_{H_\Phi}^+(V')\right|\ge k\mathrm{min}\{|\mathcal{E}'|,\rho m\}/2\).

Now we bound the size of \(\mathcal{E}'\). By a double counting on the size of \(\{(v,e)\in\mathrm{HD}(V')\times\mathcal{E}'|v\in e\}\), we have \(k|\mathcal{E}'|\ge p_1\alpha|\mathrm{HD}(V')|\), and thus<tbc>

(21) \(|\mathrm{HD}(V')|\le\frac{k}{p_1\alpha}|\mathcal{E}'|.\)

