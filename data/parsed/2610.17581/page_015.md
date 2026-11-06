weights are described by some vector \(w\in\mathbb{R}^{|E(G)|}\), and so live in some |_E(G_)|-dimensional subspace. Since each cut query only imposes a linear constraint on _w_, the weights still live in an (|_E(G_)|-_q_)-dimensional subspace after _q_ queries, and hence require |_E(G_)| queries to be found exactly. We now formally define D_k_SH dimension and its related terms.

**Definition 2.** For any subset \(S\subseteq V\) of cardinality _k_, we denote the _DkSH vector_ of _S_ by \(x(S)\in\mathbb{R}^{|E(H)|}\), which is defined as follows:

\(x(S)_e=\left\{\begin{array}{ c c }
1, & \text{if}e\subseteq S, \\
0, & \text{o.w.}
\end{array}\right.\)

We define the _DkSH dimension_ of _H_ to be equal to the dimension of the span of

\(\{x(S):S\text{is a densest}k\text{-subhypergraph of}H\},\)

and we call this span the _DkSH space_ of _H_.

Since our definitions mirror those of max cut dimension, we can use the result of Plevrakis et al. to reduce proving query complexity lower bounds to proving D_k_SH dimension lower bounds.

**Proposition 7** (\[33, Lemma A.3, Lemma A.10\])**.** Suppose there exists a hypergraph _H_ on _n_ vertices with D_k_SH dimension _d_. Then any deterministic cut algorithm that finds the total weight of the densest _k_-subhypergraph exactly must use at least _d_ queries.

\[33, Lemma A.4\] argues that the complete graph has max cut dimension \(\genfrac(){pt}{2}{n}{2}\); our primary technical contribution in Theorem 5.1 is to generalize this result to hypergraphs. To show that the D_k_SH space of the complete _r_-uniform hypergraph contains the standard basis of R<sup>|_E(H_)|</sup> and thus has dimension \(\genfrac(){pt}{2}{n}{r}\), we introduce a novel hypergraph structure parameterized to capture an incremental shift from the set of _k_-subhypergraphs to the set of single _r_-hyperedges.

**Lemma 5.2.** For any \(n\ge 4\), \(r\ge 2\), \(r\le k\le n-r\), let \(H=K_n^r\) be the complete _r_-uniform hypergraph on _n_ vertices. Then the D_k_SH dimension of _H_ is \(\genfrac(){pt}{2}{n}{r}\).

_Proof._ Let _V_ be the vertices of _H_, and let _X_ be the D_k_SH space of _H_. Note that any sub- hypergraph of size _k_ has total weight \(\genfrac(){pt}{2}{k}{r}\), so \(x(S)\in X\) for all \(S\in\genfrac(){pt}{2}{V}{k}\). For each \(e\in E(H)\), define \(v_e\in\mathbb{R}^{|E(H)|}\) to be the indicator vector that is 1 for the hyperedge _e_ and 0 everywhere else. Consider two disjoint sets of vertices \(A\subseteq V\) and \(L\subseteq V\backslash A\). We define a _hyperstar_ centered at _A_ with leaves _L_ to be the set of all _r_-edges over \(A\cup L\) fully containing _A_. When |_A_|=_t_ and \(|L|=\ell\), we call this a \((t,\ell)\)-hyperstar (note that a \((1,\ell)\)-hyperstar on a 2-uniform hypergraph is simply a star with \(\ell\) leaves). For a hyperstar centered at _A_ with leaves _L_, we define its indicator vector _v<sub>A,L</sub>_ to be the sum of the indicator vectors of its hyperedges:

\(v_{A,L}=\sum_{U\in\genfrac(){pt}{2}{L}{r-|A|}}v_{A\cup U}.\)

We abuse notation and refer to the hyperstar centered at _A_ with leaves _L_ simply by its indicator vector, _v<sub>A,L</sub>_. Lastly, we define two \((t,\ell)\)-hyperstars _v<sub>A,L</sub>_ and \(v_{A^\prime,L^\prime}\) to be _adjacent_ if \(L=L'\) and \(|A\cap A'|=t-1\).

We will now prove inductively that all (_t,k_)-hyperstars are contained in _X_ for _t_=0,1_,...,r_. As any \((r,\ell)\)-hyperstar _v<sub>A,L</sub>_ satisfies _v<sub>A,L</sub>=v<sub>A</sub>_, this will show that _X_ contains _v<sub>U</sub>_ for each \(U\in\genfrac(){pt}{2}{V}{r}\), which is an orthonormal basis for R<sup>|_E(H_)|</sup>. We can then conclude that _X_ has D_k_SH dimension \(\genfrac(){pt}{2}{n}{r}\) from the the fact that \(|E(H)|=\genfrac(){pt}{2}{n}{r}\).

## Base Case.

For any (0_,k_)-hyperstar _v<sub>A,L</sub>_, we have \(v_{A,L}=x(L)\in X\) since all sets of cardinality _k_ are densest _k_-subhypergraphs.

