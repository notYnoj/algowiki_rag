## 5 Nondetermination

By Corollary 3 and Lemma 4, if \(\chi_P>\alpha\ge 3\), then \(\chi_P-\lceil\alpha/2\rceil\le\chi_B<\chi_P\). We will show that every integer value of \(\chi_B\) in this range can be realized for the given pair \((\chi_P,\alpha)\). Thus, \(\chi_B\) cannot be expressed as a function of \(\chi_P\) and \(\alpha\) alone.

**Proposition 7** (Realization of prescribed coloring parameters)**.** _Let p, a, b be integers satisfying_

\(3\le a<p\text{\textit{and}}p-\lceil a/2\rceil\le b<p.\) (4)

_Then there exists a hypergraph satisfying_ \(\chi_P=p,\alpha=a,\chi_B=b\).

_Proof._ Start with two hyperedges _e_<sub>0</sub> and _e_<sub>_n_+1</sub>, each of size _p_, whose intersection is a set _S_ of size _a_, as shown in Figure 2(a). Choose vertices \(x_0\in e_0\backslash S\) and \(x_{n+1}\in e_{n+1}\backslash S\), and write<tbc>

\(e_0=S\sqcup U\sqcup\{x_0\},e_{n+1}=S\sqcup W\sqcup\{x_{n+1}\},\)

<tbc>where |_U_|=|_W_|=_p-a_-1.<br>
Since any hypergraph admitting a bipanchromatic _b_-coloring has at least 2_b_ vertices, we set<tbc>

\(n=max\{0,2b-(2p-a)\}\) (5)

<tbc>and add _n_ new vertices _x_<sub>1</sub>_,...,x<sub>n</sub>_. Let _X_={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>n</sub>,x_<sub>_n_+1</sub>}. We then add _n_ new hyperedges<tbc>

\(e_i=\big(e_0\backslash\{x_0\}\big)\cup\{x_i\},\text{for all}i\in[n],\)

<tbc>see in Figure 2(b). This gives a _p_-uniform hypergraph _H_=(_V,_E), where

\(V=S\sqcup U\sqcup W\sqcup X,\mathcal{E}=\{e_0,\dots,e_{n+1}\}.\) (6)

By (4) and the definition of _n_, \(|V|\in\{2b,2b+1\}\). We define a _p_-panchromatic coloring of _H_ as follows:

(1) The vertices of _S_ receive pairwise distinct colors.<tbc>

(2) The vertices of _U_ and _W_ are paired, with each pair receiving its own color. This introduces _p-a_-1 additional colors.<tbc>

(3) Introduce one new color. Assign that same color to every vertex of _X_.

See Figure 2(b) for details. Every hyperedge contains all _p_ colors, so \(\chi_P=p\). Moreover, exactly the colors assigned to the vertices of _S_ are unique in any \((\chi_P,\alpha)\)-coloring, and hence \(\alpha=a\).

To obtain a bipanchromatic _b_-coloring of _H_ (Figure 2(c)), we retain the colors assigned to the vertices of \(U\cup W\). Since \(|X|\le|S|\), we can pair the vertices of _X_ with a subset of _S_. We then merge the colors of the remaining vertices of _S_ in pairs, as indicated in the figure. We recolor any leftover vertex with an existing pair’s color. The resulting coloring is bipanchromatic and uses _b_ colors. Thus, \(\chi_B=b\).

The construction realizes the prescribed parameters using at most \(\alpha\) hyperedges, each of size \(\chi_P\). Together with Lemma 4(i), this shows that \(\chi_P\) and \(\alpha\) uniquely determine \(\chi_B\) only when \(\alpha\in\{0,1,2,\chi_P\}\).

The minimum number of vertices in a hypergraph _H_ with prescribed feasible parameters \((\chi_P,\alpha,\chi_B)\) is \(max\{2\chi_P-\alpha,2\chi_B\}\). Indeed, a \(\chi_P\)-coloring attaining \(\alpha\) gives \(|V|\ge\alpha+2(\chi_P-\alpha)=2\chi_P-\alpha\). A bipanchromatic \(\chi_B\)-coloring also gives \(|V|\ge 2\chi_B\).

