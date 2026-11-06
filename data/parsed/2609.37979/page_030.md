### Runtime.

The straightforward mathematical definition of 1-WL constructs nested multisets as colors, leading to exponentially growing color representations (as strings) that are highly inefficient to compute and store. However, by replacing these unwieldy nested tuples with canonical integer identifiers at each iterative step, one obtains the near-linear runtimes required for our analysis \[CC82, PT87, BBG17\]. More precisely, we rely on the following result.

**Theorem 7.9** (\[BBG17\])**.** _There is an algorithm, that given an edge-labeled graph G, outputs a vertex-coloring_ \(\chi^G:V(G)\rightarrow[|V(G)|]\) _in time_

\(O((|V(G)|+|E(G)|)log|V(G)|)\)

_such that the following properties hold:_

1. _For every graph G it holds that_ \(\chi^G\equiv\chi_\infty^G\).<tbc>

_2._ _For every two graphs G,H such that_ \(G\equiv_{1\text{-}\mathrm{WL}}H\) _it holds that_ \((G,\chi^G)\equiv_{1\text{-}\mathrm{WL}}(H,\chi^H)\).<tbc>

_3._ _For every two isomorphic graphs G,H and every isomorphism_ \(\varphi:G\cong H\) _it holds that_ \(\chi^G(v)=\chi^H(\varphi(v))\) _for all_ \(v\in V(G)\).

Note that the output coloring can effectively be treated as the 1-WL coloring. One key difference is that, although \(\chi_\infty^G(v)\neq\chi_\infty^H(w)\), it may be that \(\chi^G(v)=\chi^H(w)\) since the exponentially growing color representations are compressed into a set of size _n_. However, this usually does not cause any problems.

The coloring from Theorem 7.9 can be used to obtain a _complete invariant_ for 1-WL equivalence (see, e.g., \[Ott17\]). For the Constrained Shortest Path and Energy Game (and other problems; see Appendix A), this gives a Invariant and Solution-Preserving Signature.

**Theorem 7.10.** _There is a deterministic algorithm that, given an attributed graph G, outputs a string_ \(\mathrm{WL}_1(G)\in\{0,1\}^*\) _in time O_((|_V(G_)|+|_E(G_)|)log|_V(G_)|)_, such that for every two input graphs G,H it holds that_ \(G\equiv_{1\text{-}\mathrm{WL}}H\) _if and only if_ WL<sub>1</sub>(_G_)=WL<sub>1</sub>(_H)._

_Proof Sketch._ On the input \(G=(V,E,\alpha_V,\alpha_E)\), we can compute the coloring \(\chi^G\) via Theorem 7.9. Now, we build the string \(\mathrm{WL}_1(G)\in\{0,1\}^*\) to encode the following information:

• For each color _a_ in the image \(\chi^G\), the size of \((\chi^G)^{-1}(a)\) and \(\alpha_V(v)\) for some (and thus for all) \(v\in(\chi^G)^{-1}(a)\) (in increasing order of colors \(a\in[|V(G)|]\)).<tbc>

• For each pair of colors \(a,a'\) in the image \(\chi^G\), and each edge attribute \(\ell\) in the image of \(\alpha_E\), the number of edges from \((\chi^G)^{-1}(a)\) to \((\chi^G)^{-1}(a')\) with edge attribute \(\ell\). If this number is zero, then we do not explicitly encode this information in the string.

Note that the resulting string has length at most _O_((|_V(G_)|+|_E(G_)|)log|_V(G_)|), and can be computed in the same time. It is easily seen that \(G\equiv_{1\text{-}\mathrm{WL}}H\) if and only if WL<sub>1</sub>(_G_)=WL<sub>1</sub>(_H_).

## 7.3 1-WL Equivalence Implies Equal Optimality

Now, let us return to Constrained Shortest Path and Energy Game. In order to prove Theorems 7.2 and 7.4 we argue that 1-WL equivalent instances achieve the same optimal value. As a result, it suffices to compute complete invariants for 1-WL for all priors, and store optimal solutions for them.<tbc>

