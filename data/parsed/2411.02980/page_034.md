Now we show that \(H_\Phi\) satisfies Property 3.5 and Property 3.6 with probability 1-_o_(1_/n_). For Property 3.5, we present Lemma A.3 and its corollary, which are adapted from \[HWY23, Proposition 3.3 & 3.4\]. For Property 3.6, we have Lemma A.6, which is adapted from \[GGGY21, Lemma 8.6\] and \[HWY23, Proposition 3.5\], but gives a better bound.

**Lemma A.3.** _For any fixed k and_ \(\alpha\)_, if_ \(\eta k\ge 4\), \(\rho<1\) _and_ \(\mathrm{e}(\rho k\alpha)^\eta\le 1\)_, then with probability_ 1-_o_(1_/n_) _over the choice of random k-SAT formula_ \(\Phi=\Phi(k,n,m)\) _with density_ \(\alpha\), \(H_\Phi\) _satisfies Property 3.5._

_Proof._ Let \(\ell\le\rho m\) and fix \(r=\lfloor(1-\eta)k\ell\rfloor\). For any \(U\subseteq V\) of size _r_ and any \(\ell\) edges \(e_1,\dots,e_\ell\), the probability that \(e_i\subseteq U\) for every _i_ is<tbc>

\(\left(\frac{r}{n}\right)^{k\ell}\le\left(\frac{(1-\eta)k\ell}{n}\right)^{k\ell}.\)

<tbc>Thus, let \(\mathcal{E}_\ell\) be the event that there exists \(U\subseteq V\) of size _r_ and \(\ell\) edges \(e_1,\dots,e_\ell\) such that \(e_i\subseteq U\) for every _i_. We obtain that

\(\mathbf{Pr}\left[\mathcal{E}_\ell\right]\le\genfrac(){pt}{2}{n}{r}\genfrac(){pt}{2}{m}{\ell}\big(\frac{(1-\eta)k\ell}{n}\big)^{k\ell}\le\left(\frac{\mathrm{e}n}{r}\right)^r\left(\frac{\mathrm{e}m}{\ell}\right)^\ell\left(\frac{(1-\eta)k\ell}{n}\right)^{k\ell}\)<br>
\(\le\left(\frac{\mathrm{e}n}{(1-\eta)k\ell}\right)^{(1-\eta)k\ell}\left(\frac{\mathrm{e}m}{\ell}\right)^\ell\left(\frac{(1-\eta)k\ell}{n}\right)^{k\ell}\)<br>
\(\le\left(\frac{\mathrm{e}^{(1-\eta)k+1}((1-\eta)k\ell)^{\eta k}m}{n^{\eta k}\ell}\right)^\ell\)<br>
\(\le\left(\frac{\mathrm{e}^kk^{\eta k}\alpha n\ell^{\eta k}}{n^{\eta k}\ell}\right)^\ell\le\left((\mathrm{e}k^\eta)^k\alpha\left(\frac{\ell}{n}\right)^{\eta k-1}\right)^\ell.\)

If \(\ell\le n^{1/3}\), we have<tbc>

\(\mathbf{Pr}\left[\mathcal{E}_\ell\right]\le(\mathrm{e}k^\eta)^k\alpha n^{-2(\eta k-1)/3}\le(\mathrm{e}k^\eta)^k\alpha n^{-2}\)

<tbc>as long as \(\eta k\ge 4\). If \(n^{1/3}\le\ell\le\rho m\), noting that \((\rho\alpha)^{\eta k-1}\le 1/(\mathrm{e}^kk^{\eta k}\rho\alpha)\), we have<tbc>

\(\mathbf{Pr}\left[\mathcal{E}_\ell\right]\le\left((\mathrm{e}k^\eta)^k\alpha\left(\rho\alpha\right)^{\eta k-1}\right)^{n^{1/3}}\le\rho^{n^{1/3}}\le n^{-3}.\)

<tbc>Therefore, by the union bound, the probability that there exists \(\ell\le\rho m\) edges \(e_1,\dots,e_\ell\) where<tbc>

\(\left|\bigcup_{i=1}^\ell e_i\right|\le(1-\eta)k\ell\)

<tbc>is at most

\(\sum_{\ell=1}^{\rho m}\mathbf{Pr}\left[\mathcal{E}_\ell\right]\le\frac{(\mathrm{e}k^\eta)^k\alpha n^{1/3}}{n^2}+n^{-2}=o(1/n).\) □

<tbc>**Corollary A.4.** _Let_ \(H=(V,\mathcal{E})\in\mathcal{H}_{\le k}\) _be a hypergraph satisfying_ \((\eta,\rho)\)_-edge expansion. Then for any_ \(\eta<b\le 1\) _and_ \(V'\subseteq V\) _of size less than_ \((b-\eta)k\rho|\mathcal{E}|\)_, it holds that_

\(|V'|\ge(b-\eta)k|\{e\in\mathcal{E}||e\cap V'|\ge bk\}|,\)

_namely, the number of hyperedges e such that_ \(|e\cap V'|\ge bk\) _is at most_ \(\lfloor|V'|/((b-\eta)k)\rfloor\).

_Proof._ For the sake of contradiction, assume that there is a set \(V'\subseteq V\) of size \(|V'|<(b-\eta)k\rho m\) and \(\ell=\lfloor|V'|/((b-\eta)k)\rfloor+1\) hyperedges \(e_1,\dots,e_\ell\) such that each hyperedge contains at least _bk_ vertices in \(V'\). Then it is clear that \(|V'|<(b-\eta)k\ell\) and thus

\(\left|\bigcup_{i=1}^\ell e_i\right|\le(1-b)k\ell+|V'|<(1-\eta)k\ell.\)

Since \(\ell\le\rho m\), it contradicts with Lemma A.3. □

