## 2 Preliminaries

A hypergraph _H_=(_V,_E) consists of a non-empty set _V=V(H_) (the vertices of _H_) and a hyperedge set \(E(H)=\mathcal{E}\subset\mathcal{P}(V)\). If every hyperedge of _H_ contains exactly _r_ vertices, _H_ is _r_-uniform. A proper coloring of a hypergraph assigns colors to its vertices so that no hyperedge of size at least two is monochromatic.

**Definition 1** (Panchromatic colors)**.** A _panchromatic k-coloring_ of _H_ assigns _k_ colors to its vertices so that each hyperedge contains at least one vertex of each color. The maximum such _k_ is the _panchromatic number_ \(\chi_P(H)\).

**Definition 2** (Minimum unique-color count)**.** A color is _unique_ in a panchromatic coloring of _H_ if it is used on exactly one vertex. For every integer \(k\in[\chi_P(H)]\), let \(\alpha_k(H)\) denote the minimum number of vertices with unique colors among all panchromatic _k_-colorings of _H_. By convention, \(\alpha_0(H)=0\).

**Definition 3** (Bipanchromatic colors)**.** A panchromatic _k_-coloring is _bipanchromatic_ \[1\] if no color is unique. The _bipanchromatic number_ \(\chi_B(H)\) of _H_ is the maximum _k_ such that _H_ admits a bipanchromatic coloring. <sup>1</sup>

Observe that \(\chi_B(H)=max\{k\in\mathbb{N}:\alpha_k=0\}\). Since every color appears on at least two vertices, it follows that \(\chi_B(H)\le\lfloor|V|/2\rfloor\).

When the hypergraph _H_ is implied, we omit the argument _H_ and write \(\chi_P\), \(\chi_B\), and \(\alpha_k\). Write \(\alpha=\alpha_{\chi_P}\). Lalou et al. \[1, Conjecture 1\] conjectured that

\(\chi_B=\chi_P-\left\lceil\frac{\alpha}{2}\right\rceil.\) (1)

This equality was disproved in \[5, Proposition 1\]. For \(|V|\ge 2\), choose a panchromatic \(\chi_P\)- coloring with \(\alpha\) unique colors. Merge the unique colors in pairs. If one unique color remains, merge it with any other color. This results in a bipanchromatic coloring with \(\chi_P-\lceil\alpha/2\rceil\) colors. Thus, \(\chi_P-\lceil\alpha/2\rceil\) is a lower bound for \(\chi_B\). The equality in \[1, Conjecture 1\] would mean that this merging procedure is optimal. The examples in Section 3 have bipanchromatic colorings with more colors than this procedure produces. We define _excess_ \(\epsilon=\chi_B-(\chi_P-\lceil\alpha/2\rceil)\) which measures the difference between \(\chi_B\) and the lower bound in (1).

## 3 Counterexamples

The _sunflower_ S_<sub>n</sub>_=(_V,_E) is an (_n_+1)-uniform hypergraph with 2_n_ vertices and _n_ hyperedges. The set of vertices is \(V=S\sqcup P\), where _S_={_s_<sub>1</sub>_,...,s<sub>n</sub>_} and _P_={_p_<sub>1</sub>_,...,p<sub>n</sub>_} are disjoint, and its hyperedges are \(e_i=S\cup\{p_i\}\) for all \(i\in[n]\).

**Theorem 1** (Sunflower counterexamples)**.** _For_ S_<sub>n</sub> with_ \(n\ge 3\),

\(\chi_P=n+1,\alpha=n,\chi_B=n.\) (2)

_Consequently,_ \(\epsilon=\lceil\frac{n}{2}\rceil-1\ge 1\)_, so every_ S_<sub>n</sub> is a counterexample to \[1, Conjecture 1\]. In particular, for every_ \(n\in\mathbb{N}\), S<sub>2_n_+1</sub> _has_ 4_n_+2 _vertices,_ 2_n_+1 _hyperedges, and_ \(\epsilon(\mathcal{S}_{2n+1})=n\).<tbc>

<sup>1</sup>Lalou et al. \[1\] use \(\chi_p\) and \(\chi_p^2\). We write \(\chi_P\) and \(\chi_B\), respectively.

