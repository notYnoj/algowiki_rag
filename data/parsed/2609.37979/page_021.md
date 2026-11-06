_Proof._ Let _G_<sub>1</sub>_,...,G<sub>k</sub>_ denote the prior instances, which all have size at most _n_. In the preprocessing phase, we compute all signatures \(f(G_i)\in\{0,1\}^*\) and store them together with the corresponding _OPT<sub>i</sub>_ in a trie. Note that storing a single signature string in a trie takes time proportional to the length of the string, which is bounded by _O(T(n_)). Hence, the preprocessing phase runs in time \(O(k\cdot T(n))\).

In the query phase, we are getting an instance _H_. We first compute the signature _f(H_) and search this string (together with the corresponding optimal value) in the trie. If there is some \(i\in[k]\) such that _f(G_)=_f(H_), then \(OPT_\Pi(G_i)=OPT_\Pi(H)\), and we return the stored optimal value \(OPT_\Pi(G_i)\). If no matching signature is found, then we return that \(H\unknown\cong G_i\) for ever \(i\in[k]\).

We stress that, although all our algorithms follow the basic approach outlined above, we usually do not rely on Theorem 5.4 as a black-box. First, in several cases, our algorithms are randomized, i.e., the output of the signature function _f_ depends on random bits. In this case, the preservation of solutions is usually achieved only with high probability.

Also, in all cases discussed in this paper, the Invariant and Solution-Preserving Signatures we build can even be used to reconstruct optimal solutions (and not only the value). However, as already discussed above, the reconstruction is problem-specific, and does not follow from the general argument above (see also From Values to Solutions).

## 6 Algorithms via Randomized Polynomial Evaluation

In this section, we show how to utilize basic ideas from the field of randomized algorithm to obtain fast algorithms in the Isomorphic-Priors model. Our approach maps the multiset of edge weights of specific subgraphs (e.g. triangles, spanning trees) to the monomials of a formal multivariate polynomial. To efficiently compare these polynomials without explicitly expanding them, we rely on Polynomial Identity Testing (PIT) over finite fields. To this end, we use the Schwartz-Zippel Lemma.

**Lemma 6.1** (Schwartz-Zippel Lemma)**.** _Let P(x_<sub>1</sub>_,...,x<sub>m</sub>_) _be a non-zero multivariate polynomial of total degree d over a field_ F_. If r_<sub>1</sub>_,...,r<sub>m</sub> are chosen independently and uniformly at random from a finite subset_ \(S\subseteq\mathbb{F}\)_, then_ \(Pr[P(r_1,\dots,r_m)=0]\le\frac{d}{|S|}\).

We start with Negative Triangle where we are presented with a weighted graph _G_ and have to decide if _G_ contains a negative triangles (see Definition 6.4). The assumption that no algorithm solves this problem in time \(O(n^{3-\varepsilon})\) for any \(\varepsilon>0\) is a widely used hardness assumption in fine-grained complexity theory (see \[VW10\]). However, we show that inside the Isomorphic-Priors model, we can solve the problem in time \(O(n^\omega)\), where \(\omega<2.373\) denote the matrix multiplication exponent.

**Theorem 6.2.** _There is an algorithm that solves_ Negative Triangle _with k prior instances each having at most n vertices in_ \(\widetilde{O}(k\cdot n^\omega)\) _preprocesses time and_ \(\widetilde{O}(n^\omega)\) _query time with high probability._

_Additionally, if each prior G<sub>i</sub> that contains a negative triangle is equipped with a weight multiset_ \(\{w_1^{(i)},w_2^{(i)},w_3^{(i)}\}\)_, then we can output the specific vertices of a negative triangle in H in_ \(\widetilde{O}(n^\omega)\) _time with high probability._

Next, we study the Constrained Spanning Tree (CST) problem. Here, the input is graph with cost and length attributes attached to each edge and a budget _B_. The problem is to find a spanning tree that minimizes the cost and respect a budget constraint (see Definition 6.6). It is well-known that this problem is NP-complete. However, we show that inside the Isomorphic-Priors model, we can solve the problem in time \(O(n^\omega)\).

**Theorem 6.3.** _There is an algorithm that solves the_ CST _problem with k prior instances each having at most n vertices in_ \(\widetilde{O}(k\cdot n^\omega)\) _preprocesses time and_ \(\widetilde{O}(n^\omega)\) _query time with high probability._

