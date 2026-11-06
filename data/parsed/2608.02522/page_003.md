**Theorem 1.3.** _Let_ \(g\ge 5\) _be a fixed odd integer and_ \(\varepsilon>0\)_. For every sufficiently large_ \(k\in\mathbb{N}\)_, every graph G with_ \(\chi(G)\ge exp^\genfrac(){pt}{2}{g-3}{2}\big(k^{3+\varepsilon}\big)\) _contains a subgraph with chromatic number at least k and odd-girth at least g. In particular, every graph with chromatic number at least_ \(e^{k^{3+\varepsilon}}\) _contains a triangle-free subgraph of chromatic number at least k._

**Corollary 1.4.** _Every infinite graph G with infinite chromatic number contains a subgraph with infinite chromatic number and odd-girth at least g, for every odd integer_ \(g\ge 5\).

In fact, we generalize Theorem 1.3 to a more general meta-theorem which yields that for a much larger family of graph parameters which we call \(\chi\)_-amenable_, an analogous statement holds true. We defer the formal and slightly technical definition of \(\chi\)-amenability to Section 2, and instead give several examples of such parameters.

**Theorem 1.5.** _Let_ \(f(\cdot)\) _be a_ \(\chi\)_-amenable graph parameter, let_ \(g\ge 5\) _be a fixed odd integer and let_ \(\varepsilon>0\)_. Then for every sufficiently large_ \(k\in\mathbb{N}\)_, every graph G with_ \(f(G)\ge exp^\genfrac(){pt}{2}{g-3}{2}\big(k^{3+\varepsilon}\big)\) _contains a subgraph_ \(G'\) _with_ \(f(G')\ge k\) _and odd-girth at least g._

The following result shows that in addition to the chromatic number itself, several other well-studied graph parameters are \(\chi\)-amenable. For each of the parameters, we reference a book, survey or some selected papers on this parameter, which the unfamiliar reader may consult at their convenience. We will give the formal definitions of these parameters in Section 4.

**Theorem 1.6.** _Each of the following graph parameters is_ \(\chi\)_-amenable:_

• _the_ chromatic number \(\chi(\cdot)\),<tbc>

• _the_ fractional chromatic number \(\chi_f(\cdot)\) _[SU97],_<tbc>

• _the_ Hall-ratio \(\rho(\cdot)\) _[Joh94, CJGL00, DMW20], and_<tbc>

• _the_ strict vector-chromatic number _(a.k.a. Lovász-Theta function of the complement) [Lov79, Knu94, KMS98], i.e., the graph parameter_ \(\overline{\vartheta}(\cdot)\) _defined as_ \(\overline{\vartheta}(G)=\vartheta(\overline{G})\) _where_ \(\vartheta(\cdot)\) _denotes the Lovász-Theta function._<sup>3</sup>

By Theorem 1.5, for all these parameters, it is true that if they are large on some graph, then we can find a locally bipartite (i.e., large odd-girth) subgraph on which they are still large. To the best of our knowledge, this is a new result in each of the listed cases. The chromatic number case directly corresponds to Theorem 1.3 (and so in particular, proving Theorems 1.5 and 1.6 will automatically also prove Theorem 1.3). The case of the fractional chromatic number reproves the main result of Mohar and Wu [MW22] on the existence of triangle-free subgraphs of high fractional chromatic number, and provides an improved quantitative bound (dropping from tower-type to single-exponential). It also proves the odd-girth variant of their fractional analogue of the Erdős-Hajnal conjecture (cf. Conjecture 4 in [MW22]).

To prove Theorem 1.5, we create a surprising link between the previously discussed problems and the problem of finding superexponential _lower_ bounds on the multicolor Ramsey number of the collection of the first _p_ odd cycles O_<sub>p</sub>_:={_C_<sub>3</sub>_,C_<sub>5</sub>_,...,C_<sub>2_p_+1</sub>}, and along the way prove a novel bound on this Ramsey number. Concretely, extending<tbc>

<sup>3</sup>We remark that this is a natural parameter to consider in this context, since Lovász’ sandwich-theorem famously states that \(\omega(G)\le\overline{\vartheta}(G)\le\chi(G)\), i.e., \(\overline{\vartheta}(G)\) interpolates between the clique and chromatic number of a graph.

