\(\genfrac(){pt}{2}{n}{t}\le\left(\frac{\mathrm{e}n}{(k-6)\ell}\right)^{(k-6)\ell}.\) Now,

\(\mathbf{Pr}\left[\exists\text{such an}(\mathcal{E}',Y,\tilde{\mathcal{E}})\right]\le n\cdot\left(\frac{\mathrm{e}\alpha n}{\ell-1}\right)^{2\ell}\cdot\left(\frac{\mathrm{e}n}{(k-6)\ell}\right)^{(k-6)\ell}\cdot(4k\varepsilon\ell)^{k\ell}\)<br>
\(\le n\cdot\left(\frac{\mathrm{e}^{k-4}\cdot\alpha^2\cdot 2^{2k}\cdot n^{k-4}\cdot\varepsilon^k\cdot k^k}{\ell^{k-6}\cdot(\ell-1)^2(k-6)^{k-6}}\right)^\ell.\)

Now, to further evaluate the R.H.S., we use the fact that \(\frac{k^k}{(k-6)^{k-6}}\le(\mathrm{e}k)^6.\) Also, \(\ell\le\varepsilon n\) and \(\ell-1\ge\varepsilon n/2.\) Then, we get that

\(\mathbf{Pr}\left[\exists\text{such an}(\mathcal{E}',Y,\tilde{\mathcal{E}})\right]\le n\cdot\left(\mathrm{e}^{k+2}2^{2k}\cdot\alpha^2\cdot\varepsilon^4\cdot k^6\right)^\ell:=\tilde{p}.\)

Observe that since \(\varepsilon\le 4^{-k}\alpha^{-1/2}+\frac{1}{n},\) we get that \(\mathrm{e}^{k+2}2^{2k}\cdot\alpha^2\cdot\varepsilon^4\cdot k^6\le\frac{1}{2}\) since \(k\ge 12.\) Now, based on whether \(\varepsilon n\ge 5\mathrm{log}n\) or \(\varepsilon n<5\mathrm{log}n,\) we make two cases:

\(\bullet\) If \(\varepsilon n\ge 5\mathrm{log}n,\) we get that \(\tilde{p}\le n\cdot(\frac{1}{2})^{\varepsilon n}=o(1/n^3);\)<tbc>

\(\bullet\) If \(\varepsilon n<5\mathrm{log}n,\) we assume \(n\ge 2^{\Omega(k)}\) (for an appropriately large constant), which implies that \(\mathrm{e}^{k+2}2^{2k}\cdot\alpha^2\cdot\varepsilon^4\cdot k^6=o(1/n^3)\) and we also have that \(\ell\ge 2,\) which again implies that \(\tilde{p}=o(1/n^3).\)

Observe that we have shown the above probability bound for \(\mathcal{E}'\) of a specific size, which, in our case was \(\mathrm{min}\{\ell-1,m-\ell\}.\) Then, by union bound over all possible sizes of \(\mathcal{E}',\) we get that \(\mathbf{Pr}\left[\exists\text{no}(\mathcal{E}',Y,\tilde{\mathcal{E}})\right]\ge 1-o(1/n).\) □

Using Proposition A.9, we can bound the size of bad vertices and bad hyperedges in any connected sets. Given a hypergraph _H_=(_V,_E), we now simplify _V_bad(_V_) to _V_bad and Ebad(_V_) to Ebad. We first present the following facts.

**Fact A.10.** _For any_ \(V'\subseteq V,\) _it holds that_ \(V_\mathrm{bad}(V')\subseteq V_\mathrm{bad}\) _and_ \(\mathcal{E}_\mathrm{bad}(V')\subseteq\mathcal{E}_\mathrm{bad}.\)

**Fact A.11** (\[GGGY21, Lemma 8.9\])**.** _For any_ \(V'\subseteq V_\mathrm{bad}\) _such that_ \(V'\) _is a connected component in the induced subgraph H_\[_V_bad\]_, it holds that_ \(V_\mathrm{bad}(V')=V'.\)

If Proposition A.9 holds for \(H_\Phi,\) we can prove that Property 3.10 is also satisfied, which states that the number of bad variables is bounded by the number of high-degree variables.

**Lemma A.12.** _For any fixed k and_ \(\alpha,\) _if_ \(\eta k\ge 4,\mathrm{e}(\rho k\alpha)^\eta\le 1,\varepsilon_1>\eta,\) _and_ \(6k^5\le p_1\le\mathrm{e}^{k-2}\alpha,\) _then with probability_ 1-_o_(1_/n_) _over the choice of random formula_ \(\Phi,\) _it holds for_ \(H_\Phi=(V,\mathcal{E})\) _that:_

(_1)_ _for any_ \(V'\subseteq V,\) _we have_ \(|V_\mathrm{bad}(V')|\le 2|\mathrm{HD}(V')|/(\varepsilon_1-\eta),\) _in particular,_ \(H_\Phi\) _satisfies Property 3.10 if_ \(\varepsilon_1=2\eta;\)<tbc>

_(2)_ _for any_ \(V'\subseteq V_\mathrm{bad}\) _such that_ \(V'\) _consists of some connected components in_ \(H_\Phi[V_\mathrm{bad}],\) _we have_ \(|V'|\le 2|\mathrm{HD}(V')|/(\varepsilon_1-\eta).\)

_Proof._ We only need to prove item (1). Item (2) is a direct corollary of item (1) and Fact A.11.

By Proposition A.2, we have \(|\mathrm{HD}(V')|\le|\mathrm{HD}(V)|\le\mathrm{e}^{-k}\alpha^{-2}n.\) Let<tbc>

\(\mathcal{E}'=\{e\in\mathcal{E}||e\cap\mathrm{HD}(V')|\ge\varepsilon_1k\}.\)

<tbc>By setting \(b=\varepsilon_1\) in Lemma A.3 and Corollary A.4, it follows that

\(|\mathrm{HD}(V')|\ge(\varepsilon_1-\eta)k|\mathcal{E}'|.\)

In particular, \(|\mathcal{E}'|\le|\mathrm{HD}(V')|\le\mathrm{e}^{-k}\alpha^{-2}n.\) Observe that, in Algorithm 1, if there exist more than one hyperedge that can be added into \(\mathcal{E}_\mathrm{bad}(V'),\) we can add them in an arbitrary order without changing the output of Algorithm 1. So we start by adding all hyperedges in \(\mathcal{E}'\) into \(\mathcal{E}_\mathrm{bad}(V')\) first. After that, each hyperedge newly added to \(\mathcal{E}_\mathrm{bad}(V')\) intersects at least \(\varepsilon_1k\) vertices with existing hyperedge in \(\mathcal{E}_\mathrm{bad}(V').\) Hence, applying Proposition A.9, we obtain that \(|\mathcal{E}_\mathrm{bad}(V')\backslash\mathcal{E}'|\le|\mathcal{E}'|,\) which implies that<tbc>

\(|\mathcal{E}_\mathrm{bad}(V')|\le 2|\mathcal{E}'|\le\frac{2}{(\varepsilon_1-\eta)k}|\mathrm{HD}(V')|\)

