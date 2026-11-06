**x**<sub>1</sub>_,...,_**x**_<sub>q</sub>_. Hence, \(M'\) is indeed positive semidefinite. Finally, consider any two distinct \(u,v\in V(G)\) such that \(uv\notin E(G')\). Then, by definition of \(G'\), we must have \(uv\notin E(G)\) or \(u,v\in V_i\) for some \(i\in[q]\). In the first case, \(M\in\mathcal{M}_G\) implies that _M<sub>u,v</sub>_=0 and hence (_M<sub>V<sub>j</sub></sub>)<sub>u,v</sub>_=0 for all \(j\in[q]\) as well. Using the definition of \(M'\) and since \(u\neq v\), this implies that also \((M')_{u,v}=0\) in this case, as desired. In the second case, we have _M<sub>u,v</sub>_=(_M<sub>V<sub>i</sub></sub>)<sub>u,v</sub>_ and (_M<sub>V<sub>j</sub></sub>)<sub>u,v</sub>_=0 for all \(j\neq i\). Hence, also in this case we obtain \((M')_{u,v}=0\) from the definition of \(M'\). Thus, we have shown that \(M'\) has a zero-entry at position (_u,v_) whenever \(u\neq v\) are nonadjacent vertices of \(G'\). Summarizing, we have now verified all conditions defining membership of the set \(\mathcal{M}_{G^\prime}\) of matrices, and hence we have shown that \(M'\in\mathcal{M}_{G^\prime}\). By Definition 4.3, we thus find<tbc>

\(\overline{\vartheta}(G')\ge\lambda_{max}(M')=max_{\mathbf{x}\neq 0}\frac{\mathbf{x}^\top M'\mathbf{x}}{\mathbf{x}^\top\mathbf{x}}.\)

<tbc>To give the desired lower bound on \(\overline{\vartheta}(G')\), consider a unit vector \(\mathbf{x}_*\in\mathbb{R}^{V(G)}\) such that \(\mathbf{x}_*^\top M\mathbf{x}_*=\lambda_{max}(M)=z\). By inequality (7), we then find that

\(\overline{\vartheta}(G')\ge\mathbf{x}_*^\top M'\mathbf{x}_*\ge\frac{1}{4}\mathbf{x}_*^\top M\mathbf{x}_*=\frac{z}{4}\ge\frac{q}{8}.\)

Altogether, we have thus found a subgraph \(G'\) of _G_ satisfying that \(\overline{\vartheta}(G')\ge z/4\ge z/8=\overline{\vartheta}(G)/8\) and \(\chi(G')\le q\le 8\overline{\vartheta}(G')\). This concludes the proof of the lemma.

## 5 Concluding remarks

Several comments about Theorem 1.3 are in order. First of all, it shows that guaranteeing a _k_-chromatic subgraph avoiding a fixed _odd cycle_ requires only a chromatic number bound which is a tower of _bounded height_ (independent of _k_), while Pettie, Tardos and Walczak [PTW26] recently showed that to avoid _C_<sub>4</sub>, a tower whose height _depends on k_ (even linearly) is necessary. This suggests that preserving high chromatic number while avoiding short even cycles is significantly more difficult than avoiding short odd cycles.

The best _lower bounds_ for the functions \(h_g(\cdot)\) we know come from considering complete host graphs, i.e., by considering upper bounds on the maximum chromatic number of _n_-vertex graphs with (odd-)girth _g_. Concretely, Denley [Den94] showed that when \(g\ge 5\) is an odd number, then every _n_-vertex graph with odd-girth at least _g_ has independence number at least _n_<sup>(_g_-3)/(_g_-1)+_o_(1)</sup>. By a simple greedy process that repeatedly removes a largest independent set, this implies that such graphs have chromatic number at most _n_<sup>2/(_g_-1)+_o_(1)</sup>. Thus, we find that \(h_g(k)\ge k^{(g-1)/2+o(1)}\) for every odd \(g\ge 5\), and we are not aware of a better lower bound. This raises the following question, which remains unanswered here, as all our upper bounds are exponential towers of constant height.

**Question 5.1.** _Fix an odd number_ \(g\ge 5\)_. Is the function h<sub>g</sub> bounded polynomially?_

We suspect the answer may be negative.

Finally, it would be interesting to extend the list in Theorem 1.6 by identifying further meaningful and well-studied graph parameters that are \(\chi\)-amenable.

