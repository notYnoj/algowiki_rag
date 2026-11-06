cycle codes on alphabets of size three or more. This stands in contrast to cycle codes on the binary alphabet, for which nearest-codeword decoding is known to be solvable in polynomial time by a T-join decoding algorithm \[EJ73\].

**Theorem 2.** _For every fixed finite field_ F_<sub>q</sub> with q\>_2_, the following decision problem is NP- complete. Given a homological cycle code with parity-check matrix B<sup>T</sup>, a syndrome_ **s**_, and an integer_ \(w\ge 0\)_, decide whether there exists_ \(\mathbf{e}\in\mathbb{F}_q^m\) _with B<sup>T</sup>_**e**=**s** _and_ \(|\mathbf{e}|\le w\)_. Consequently, nearest-codeword decoding is NP-hard for these codes._

_Proof._ Membership in NP follows by checking the syndrome and weight. For hardness, we reduce from perfect three-dimensional matching \[GJ09\]: given disjoint sets _U_<sub>1</sub>_,U_<sub>2</sub>_,U_<sub>3</sub>, each of size _k_, and a set of triples \(\mathcal{T}\subseteq U_1\times U_2\times U_3\), decide whether there exists a subset of _k_ triples from T that covers every element exactly once.

Choose \(\alpha,\beta\in\mathbb{F}_q^\times\) with \(\alpha+\beta\neq 0\) (possible because _q\>_2) and put \(\gamma=-\alpha-\beta\). All three are nonzero, their sum is zero, and no nonempty proper subcollection has sum zero. This holds also in characteristic two.

Construct a bipartite incidence graph with vertex set \(V=P\sqcup L\), with "element vertices" \(P=U_1\sqcup U_2\sqcup U_3\), and "triplet vertices" _L_=T . Join each triplet vertex \(T\in\mathcal{T}\) to its three elements, orienting the edges from _T_ to those elements, and take _B<sup>T</sup>_ to be its oriented incidence matrix. Define a syndrome \(\mathbf{s}\in\mathbb{F}_q^V\) by assigning entries in _U_<sub>1</sub>_,U_<sub>2</sub>_,U_<sub>3</sub> values \(\alpha,\beta,\gamma\), respectively, and entries in T value 0. Set _w_=3_k_.

An exact cover yields an error \(\mathbf{e}\in\mathbb{F}_q^E\) of weight 3_k_ by assigning the three edges of each chosen triple the respective values \(\alpha,\beta,\gamma\). The triplet-vertex equations hold because their sum is zero. Conversely, all 3_k_ element syndromes are nonzero, so an error of weight at most 3_k_ has exactly one nonzero edge at each element. That edge’s value is forced to equal the element syndrome. At a triplet vertex, the selected incident values are a subcollection of \(\{\alpha,\beta,\gamma\}\), which sums to zero only if none or all three are selected. The selected triples therefore form an exact cover. This reduction gives a simple graph.

## 3.2 Decoding thresholds for even symbol-wise additive channels

We now study ML whole-word decoding for the homological cycle codes on _D_-regular graphs. Throughout this subsection, _B<sup>T</sup>_ is an oriented incidence matrix, _n_=|_V(G_)|, and _m_=|_E(G_)|=_Dn/_2. For a weighted homological incidence matrix, these results apply after multiplying each error coordinate by its incidence weight, provided the transformed errors have the common distribution specified below. Uniform nonzero replacement is preserved by this normalization.

We consider additive channels in which each symbol is corrupted by adding an error \(a\in\mathbb{F}_q\), whose distribution is as follows. Fix a probability distribution \(\theta\) on \(\mathbb{F}_q^\times\) which is _even_, i.e., \(\theta(a)=\theta(-a)\), and write

\(\nu_p(0)=1-p,\nu_p(a)=p\theta(a)(a\neq 0)\) (58)

We refer to \(\theta\) as the _replacement distribution_. An important special case, when all symbols are equally likely to occur given a flip, is the _q_-ary symmetric channel.

**Definition 3** (_q_-ary symmetric channel)**.** _The q-ary symmetric channel (qSC) has uniform replacement_ \(\theta(a)=1/(q-1)\) _for all_ \(a\neq 0\) _and_ \(0\le p\le 1-q^{-1}\).

