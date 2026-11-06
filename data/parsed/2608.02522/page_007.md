We first note that by our choice of _C_ there exists a subgraph \(G'\) of _G_ such that \(f(G')\ge f(G)/C\) and \(\chi(G')\le Cf(G')\). In the following, we set \(\ell:=\lceil Cf(G')\rceil\). Let us fix a proper coloring \(c:V(G')\rightarrow[\ell]\) of \(G'\) using at most \(\ell\) colors. Let \(K\in\mathbb{N}\) be the smallest integer such that \(R_K(\mathcal{O}_p)>\ell\) (such a _K_ exists since \(R_K(\mathcal{O}_p)\rightarrow\infty\) as \(K\rightarrow\infty\), as demonstrated e.g. by Theorem 1.7). Note that since \(\ell\rightarrow\infty\) as \(k\rightarrow\infty\), with _k_ we may also assume \(\ell\), and thus also _K_, to be sufficiently large. By definition of the Ramsey number, \(R_K(\mathcal{O}_p)>\ell\) implies that there exists an edge-coloring of the complete graph \(K_\ell\) on vertex-set \([\ell]\) with _K_ colors such that there are no monochromatic subgraphs in O_<sub>p</sub>_. Let _H_<sub>1</sub>_,...,H<sub>K</sub>_ be the spanning subgraphs of \(K_\ell\) such that _H<sub>i</sub>_ contains exactly all the edges of color _i_, for _i_=1_,...,K_. Then each _H<sub>i</sub>_ has odd-girth at least _g_. Finally, for each \(i\in[K]\) let us define _G<sub>i</sub>_ as the spanning subgraph of \(G'\) where for every edge \(uv\in E(G')\) we have \(uv\in E(G_i)\) if and only if \(c(u)c(v)\in E(H_i)\).

We can then observe that for every \(i\in[K]\) the graph _G<sub>i</sub>_ also has odd-girth at least _g_: The color-map \(c:V(G_i)=V(G')\rightarrow[\ell]=V(H_i)\), by definition of _G<sub>i</sub>_, forms a homomorphism from _G<sub>i</sub>_ to _H<sub>i</sub>_. If _G<sub>i</sub>_ contained an odd cycle of length less than _g_, then the image of that cycle under _c_ would yield a closed odd walk of length less than _g_ in _H<sub>i</sub>_, within which we could find an odd cycle of length less than _g_ in _H<sub>i</sub>_, a contradiction since _H<sub>i</sub>_ has odd-girth at least _g_. In the remainder of this proof, our goal is to show that \(f(G_i)\ge k\) for some _i_, which will then demonstrate that \(G'\), and thus _G_, indeed has a subgraph of odd-girth at least _g_ on which _f_ takes on a value of at least _k_, as desired.

Towards a contradiction, suppose that _f(G<sub>i</sub>)\<k_ for every _i_. Then, since \(G'\) is the edge-disjoint union of the graphs _G_<sub>1</sub>_,...,G<sub>K</sub>_ and since _f_ is \(\chi\)-amenable, we obtain that:<tbc>

\(\ell\le 2Cf(G')\le 2C\prod_{i=1}^Kf(G_i)<2Ck^K.\)

<tbc>By our choice of _K_, we have \(R_{K-1}(\mathcal{O}_p)\le\ell\). Using Theorem 1.7 and that _K_ is sufficiently large, this implies that<tbc>

\((log^{(p-1)}K)^{K/3-\frac{\varepsilon}{100}\cdot K}\le(log^{(p-1)}(K-1))^{(K-1)/3-o(K-1)}\le R_{K-1}(\mathcal{O}_p)\le\ell<2Ck^K.\)

<tbc>Taking the _K_-th root, we find that<tbc>

\((log^{(p-1)}K)^{1/3-\varepsilon/100}<(1+o(1))k\)

<tbc>and thus<tbc>

\(K<exp^{(p-1)}\left(k^{1/(1/3-\varepsilon/100)+o(1)}\right)\le exp^{(p-1)}\left(k^{3+\varepsilon/2}\right).\)

<tbc>Using the well-known upper bound \(R_K(\mathcal{O}_p)\le R_K(C_3)\le 3K!\) (cf. \[GG55\]), we now obtain

\(exp^{(p)}(k^{3+\varepsilon})=exp^{\left(\frac{g-3}{2}\right)}(k^{3+\varepsilon})\le f(G)\le Cf(G')\le\ell<R_K(\mathcal{O}_p)\le 3K!\le 3\cdot K^K\)<br>
\(<exp(K^{1+\varepsilon/100})\le exp\left(\left(exp^{(p-1)}(k^{3+\varepsilon/2})\right)^{1+\varepsilon/100}\right)<exp^{(p)}(k^{3+\varepsilon}),\)

