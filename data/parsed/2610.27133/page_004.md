**Corollary 3** (Merging-based lower bound)**.** _For an arbitrary hypergraph H and for each integer_ \(k\le\chi_P\) _we obtain that_ \(\chi_B\ge\beta_k\)_. Furthermore, we have that_ \(\chi_B=\mathrm{max}_k\{\beta_k\}\).

**Lemma 4** (Equality cases and counterexample bounds)**.**

(i) _If_ \(\alpha\in\{0,1,2,\chi_P\}\)_, then_ \(\chi_B=\beta\)_. In particular, equality holds if_ \(\chi_P\le 3\).<tbc>

(ii) _If_ \(\chi_B\neq\beta\)_, then_ \(3\le\alpha\le\chi_P-1\) _and_ \(\left\lceil\chi_P/2\right\rceil\le\beta<\chi_B\le\chi_P-1\).

_Proof._ (i) Corollary 3 gives \(\chi_B\ge\beta\). If \(\alpha=0\), a \(\chi_P\)-coloring is already bipanchromatic, so \(\chi_B=\chi_P=\beta\). If \(\alpha>0\), no \(\chi_P\)-coloring is bipanchromatic, so \(\chi_B\le\chi_P-1\). For \(\alpha\in\{1,2\}\), \(\chi_B=\beta\). If \(\alpha=\chi_P\), then \(|V|=\chi_P\), so \(\chi_B\le\left\lfloor|V|/2\right\rfloor=\left\lfloor\chi_P/2\right\rfloor=\beta\), so \(\chi_B=\beta\).

(ii) By (i), \(3\le\alpha\le\chi_P-1\). Thus \(\beta\ge\chi_P-\left\lceil\frac{\chi_P-1}{2}\right\rceil=\left\lceil\frac{\chi_P}{2}\right\rceil\). Corollary 3 gives \(\beta<\chi_B\), and \(\alpha>0\) gives \(\chi_B\le\chi_P-1\) as above.

Let \(\rho=\chi_B/\beta\) denote the actual-to-conjectured ratio.

**Theorem 5** (Sharp ratio bounds)**.** _If_ \(|V|\ge 2\)_, then_ \(1\le\rho<2\)_, and the upper bound is asymptotically sharp. For_ \(\chi_P\ge 2\)_, the sharper bound_ \(\rho\le\frac{\chi_P-1}{\left\lceil\chi_P/2\right\rceil}\) _is attained for every fixed value of_ \(\chi_P\).

_Proof._ By Lemma 4 it holds that \(\rho\ge 1\), with equality precisely when (1) is true. Suppose that \(\chi_P\ge 2\). If \(\rho\neq 1\), then Lemma 4(ii) gives the upper bound. For \(n\ge 3\), Theorem 1 gives \(\rho(\mathcal{S}_n)=\frac{\chi_P-1}{\left\lceil\chi_P/2\right\rceil}\). The sharp bounds are strictly below 2 and tend to 2 as \(\chi_P\rightarrow\infty\).

_The order_ of a hypergraph _H_ is the number of its vertices |_V(H_)|. We show S<sub>2_n_+1</sub> has minimum order among hypergraphs satisfying \(\epsilon\ge n\).

**Theorem 6** (Excess-based minimum order)**.** _If a hypergraph H_=(_V,_E) _satisfies_ \(\epsilon(H)\ge n\)_, then_ \(|V|\ge|V(\mathcal{S}_{2n+1})|=4n+2\)_. Moreover, if_ \(\epsilon(H)=n\) _and_ |_V_|=4_n_+2_, then, after removing hyperedges that properly contain other hyperedges,_ \(H\cong\mathcal{S}_{2n+1}\).

_Proof._ By Lemma 4(ii), \(\beta\ge\left\lceil\chi_P/2\right\rceil\) and \(\chi_B\le\chi_P-1\). Hence

\(n\le\epsilon=\chi_B-\beta\le\chi_B-\left\lceil\chi_P/2\right\rceil\le\left\lfloor(\chi_B-1)/2\right\rfloor.\) (3)

Thus, \(\chi_B\ge 2n+1\), and consequently \(|V|\ge 2\chi_B\ge 4n+2=|V(\mathcal{S}_{2n+1})|\).

Suppose that \(\epsilon(H)=n\) and |_V_|=4_n_+2. It follows from (3) that \(\chi_B=2n+1\) and \(\beta=\left\lceil\chi_P/2\right\rceil=n+1\). Since \(\chi_P\neq\chi_B\) (\(\epsilon>0\)), we obtain \(\chi_P=2n+2\). Moreover, \(\left\lceil\frac{\alpha}{2}\right\rceil=\chi_P-\beta=n+1\). Since \(\alpha\neq\chi_P\) it follows that \(\alpha=2n+1\).

Consider a panchromatic \((\chi_P,\alpha)\)-coloring of _H_, and let _S_ be the set of its \(\alpha\) uniquely colored vertices. All remaining \(|V|-\alpha\) vertices have a common color _C_. For every vertex _v_ of color _C_, there is a hyperedge \(S\sqcup\{v\}\). Otherwise, if every hyperedge containing _v_ also contained another vertex of _v_’s color, recoloring _v_ with an existing unique color preserves panchromaticity and contradicts the supposed \(\alpha\). Removing hyperedges that properly contain other hyperedges leaves \(\mathcal{S}_{2\epsilon+1}\).

Every counterexample has at least three hyperedges. Choose a \(\chi_P\)-coloring attaining \(\alpha\). If every non-unique color occurred twice, then \(|V|=2\chi_P-\alpha\), so \(\chi_B\le\left\lfloor|V|/2\right\rfloor=\beta\), a contradiction. Thus some color _C_ occurs on at least three vertices. Since \(\alpha>0\), the same recoloring argument shows that each such vertex is the only _C_-colored vertex in some hyperedge. These hyperedges are distinct.

Proposition 2 attains this three-hyperedge minimum with \(\epsilon(\Delta_n)=n\) for every \(n\ge 1\). However, Theorem 6 implies that every hypergraph of minimum order satisfying \(\epsilon(H)\ge n\) has at least 2_n_+1 hyperedges. Thus, for \(n\ge 2\), the minimum numbers of vertices and hyperedges cannot be attained simultaneously.

