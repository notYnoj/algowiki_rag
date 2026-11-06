**Proposition A.5** (\[GGGY21, Lemma 8.5\])**.** _Let U be any subset of indices of clauses in_ \(\Phi\) _and T be any tree on the vertex set U. Then the probability that T is a subgraph of_ \(G_\Phi\) _is at most_ (_k_<sup>2</sup>_/n_)<sup>|_U_|-1</sup>.

**Lemma A.6.** _Suppose_ \(\alpha\le 2^k\)_. With probability_ 1-_o_(1_/n_) _over the choice of random k-SAT formula_ \(\Phi=\Phi(k,n,m)\) _with fixed density_ \(\alpha\), \(H_\Phi\) _satisfies Property 3.6, namely, for every clause c in_ \(\Phi\) _and_ \(\ell\ge 1\)_, there are at most_ \(n^3(\mathrm{e}k^2\alpha)^\ell\) _many connected sets of clauses in_ \(G_\Phi\) _that contains c and has size_ \(\ell\).

_Proof._ If \(\ell=1\), this lemma is trivial. Now we assume \(\ell\ge 2\). Let _c_ be an arbitrary clause in \(\Phi\) and _U_ be a set of clauses of size \(\ell\) where \(c\in U\). Let _T<sub>U</sub>_ be the set of all trees with vertex set _U_. By standard results, we have \(|T_U|=\ell^{\ell-2}\). In addition, any fixed tree \(T\in T_U\) is a subgraph of \(G_\Phi\) with probability at most \((k^2/n)^{\ell-1}\), by Proposition A.5. Thus, the union bound gives that<tbc>

\(\mathbf{Pr}\left[G_\Phi[U]\text{is connected}\right]\le\ell^{\ell-2}(k^2/n)^{\ell-1}.\)

<tbc>Let \(Z_{\ell,c}\) be the number of connected sets of clauses with size \(\ell\) containing _c_. Then, we have

\(\mathbf{E}[Z_{\ell,c}]=\sum_{U:c\in U,|U|=\ell}\mathbf{Pr}\left[G_\Phi[U]\text{is connected}\right]\)<br>
\(\le\genfrac(){pt}{2}{m-1}{\ell-1}\cdot\ell^{\ell-2}\cdot\genfrac(){pt}{2}{k^2}{n}^{\ell-1}\)<br>
\(\le\frac{(\mathrm{e}m)^{\ell-1}}{(\ell-1)^{\ell-1}}\ell^{\ell-2}\genfrac(){pt}{2}{k^2}{n}^{\ell-1}\)<br>
\(=\frac{(\mathrm{e}k^2\alpha)^{\ell-1}}{\ell}\genfrac(){pt}{2}{\ell}{\ell-1}^{\ell-1}\)<br>
\(\le\frac{\mathrm{e}}{\ell}\cdot(\mathrm{e}k^2\alpha)^{\ell-1}.\)

By Markov’s inequality, it further implies that<tbc>

\(\mathbf{Pr}\left[Z_{\ell,c}\ge n^3(\mathrm{e}k^2\alpha)^\ell\right]\le\frac{\mathrm{e}(\mathrm{e}k^2\alpha)^{\ell-1}}{\ell n^3(\mathrm{e}k^2\alpha)^\ell}=\frac{1}{n^3k^2\alpha\ell}.\)

<tbc>Finally, using a union bound again, we obtain that

\(\mathbf{Pr}\left[\exists 2\le\ell\le m\text{and clause}c\text{such that}Z_{\ell,c}\ge n^3(\mathrm{e}k^2\alpha)^\ell\right]\)<br>
\(\le\sum_{\ell=2}^m\frac{m}{n^3k^2\alpha\ell}=\frac{1}{k^2n^2}\sum_{\ell=2}^m\frac{1}{\ell}\le\frac{\mathrm{log}m}{k^2n^2}=o(1/n).\) □

Next, we show that \(H_\Phi\) satisfies Property 3.10 and Property 3.11 with probability 1-_o_(1_/n_) in Lemma A.12 and Lemma A.14. To prove these two lemmas, we also need the following properties for random formulas and for Algorithm 1.

In a hypergraph _H_=(_V,_E), let \(\Gamma_H(V')\) denote the set of neighbors of vertices in \(V'\), and let \(\Gamma_H^+(V')=V'\cup\Gamma_H(V')\). Then we have the following technical propositions.

**Proposition A.7** (\[HWY23, Proposition 3.6\])**.** _Let_ \(\Phi=(k,n,m)\) _be a random k-SAT formula with_ \(k\ge 30\) _and density_ \(\alpha\)_. Then with probability_ 1-_o_(1_/n), we have_

\(\left|\Gamma_{H_\Phi}^+(V')\right|\le 3k^4\alpha\mathrm{max}\{|V'|,k\mathrm{log}n\}\)

_for every connected subset_ \(V'\) _of vertices in_ \(H_\Phi\).

_Proof._ Define \(\mathcal{E}'=\{e\in\mathcal{E}|\mathrm{vbl}(e)\cap V'\neq\emptyset\}\). It suffices to bound \(|\mathcal{E}'|\le 3k^3\alpha\mathrm{max}\{|V'|,k\mathrm{log}n\}\) since \(|\Gamma_{H_\Phi}^+(V')|\le k|\mathcal{E}'|\).

We turn our focus to the case when \(|V'|\ge\lfloor k\mathrm{log}n\rfloor\). Since \(H_\Phi(V')\) is connected, there exists a \(\mathcal{E}''\subset\mathcal{E}'\) such that \(V'\) is connected using hyperedges in \(\mathcal{E}''\) and \(|V'|/k\le\mathcal{E}''\le|V'|\). We get that

\(|\mathcal{E}''|\ge\mathrm{log}n-1.\)

Now, define \(\tilde{\mathcal{E}}=\mathcal{E}'\backslash\mathcal{E}''\). Since \(k^3\alpha\ge 1\), we will focus on bounding \(|\mathcal{E}'|\le 2k^3\alpha|V'|+|V'|\). Using the fact that \(|\tilde{\mathcal{E}}'|\le|\tilde{\mathcal{E}}|+|\mathcal{E}''|\) and \(|\mathcal{E}''|\le|V'|\), we focus our attention on bounding \(|\tilde{\mathcal{E}}|\le 2k^3\alpha|V'|\). Consider any fixed \(\mathcal{E}'',V',\tilde{\mathcal{E}}\) which satisfy:

