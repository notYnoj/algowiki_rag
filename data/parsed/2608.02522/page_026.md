## A Proof of Corollary 1.4

In this section, for the sake of completeness we supply the proof of Corollary 1.4 about infinite graphs with infinite chromatic number.

_Proof of Corollary 1.4._ Let _G_ be an infinite graph with infinite chromatic number and let \(g\ge 5\) be a fixed odd integer. We claim that there exists a sequence of pairwise vertex- disjoint finite subgraphs \((G_i)_{i\ge 1}\) of _G_ such that for every \(i\in\mathbb{N}\), we have \(\chi(G_i)\ge i\) and _G<sub>i</sub>_ has odd-girth at least _g_. Once we have established the claim, we can observe that the disjoint union \(\bigcup_{i=1}^\infty G_i\) forms a subgraph of _G_ with infinite chromatic number and odd-girth at least _g_.

We construct the sequence inductively: Suppose that for some \(i\ge 1\) we already constructed vertex-disjoint finite subgraphs _G_<sub>1</sub>_,...,G_<sub>_i_-1</sub> of _G_ such that \(\chi(G_j)\ge j\) and _G<sub>j</sub>_ has odd-girth at least _g_ for every \(1\le j<i\), and let us define _G<sub>i</sub>_ with the desired properties. For this purpose, first of all note that the induced subgraph \(G[\bigcup_{1\le j<i}V(G_j)]\) is finite, and thus has finite chromatic number. It follows that \(G':=G-\bigcup_{1\le j<i}V(G_j)\) has infinite chromatic number. By the de Bruijn-Erdős theorem, it follows that there exist finite subgraphs of \(G'\) with arbitrarily large chromatic number. Theorem 1.3 then implies that any such subgraph of \(G'\) with suitably large chromatic number must contain a subgraph with chromatic number at least _i_ and odd-girth at least _g_. We define _G<sub>i</sub>_ to be such a subgraph. By definition it is vertex-disjoint from _G_<sub>1</sub>_,...,G_<sub>_i_-1</sub>, and has all desired properties. Hence we may conclude the proof.

## References

