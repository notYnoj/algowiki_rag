as desired. This concludes the inductive proof of (6).

Finally, fix the integer _p_ from the theorem and a constant \(\delta\in(0,1/3)\), and let<tbc>

\(n=\lfloor(log^{(p-1)}k)^{(1/3-\delta)k}\rfloor.\)

<tbc>As \(k\rightarrow\infty\),<tbc>

\(logn=(1/3-\delta+o(1))klog^{(p)}k,log^{(p+1)}n=(1+o(1))log^{(p)}k.\)

<tbc>Therefore (6) gives<tbc>

\(a_p(n)\le(1-3\delta+o(1))k<k\)

<tbc>for all sufficiently large _k_. Hence _K<sub>n</sub>_ has a _k_-edge-coloring with no monochromatic member of O_<sub>p</sub>_, so _R<sub>k</sub>_(O_<sub>p</sub>)\>n_. Since \(\delta>0\) was arbitrary, we have shown that

\(R_k(\mathcal{O}_p)\ge(log^{(p-1)}k)^{k/3-o(k)},\)

as desired. This concludes the proof of the theorem.

## 4 \(\chi\)-amenable graph parameters

This section is devoted to proving Theorem 1.6. We split the proof into two subsections based on the graph parameters treated, where we bundle the chromatic number, the fractional chromatic number and the Hall ratio together, since the proofs for their \(\chi\)- amenability are related. The proof for \(\chi_f\) uses linear programming duality, while the proof for the \(\chi\)-amenability of the strict vector chromatic number \(\overline{\vartheta}\) relies on linear algebra as well as a deep theorem of Marcus, Spielman and Srivastava [MSS15] from their resolution of the famous Kadison-Singer problem, and is presented in a separate section.

### 4.1 Chromatic number, fractional chromatic number and Hall ratio

In this section, we prove that each parameter \(f\in\{\chi,\chi_f,\rho\}\) is \(\chi\)-amenable. We start by verifying the submultiplicativity condition \(f(G_1\cup G_2)\le f(G_1)f(G_2)\) for these parameters. For the chromatic number, this is a well-known fact and can be verified by considering a product-coloring of optimal colorings of _G_<sub>1</sub> and _G_<sub>2</sub>. For the fractional chromatic number and Hall ratio, this inequality is also easy to verify, but we include a proof for completeness. In the following we will use the following definitions which can be easily checked to be consistent with those in the literature (cf. [BLM<sup>+</sup>22, DMW20]): Given a graph _G_, its Hall-ratio is \(\rho(G):=max_{\varnothing\neq H\subseteq G}\frac{|V(H)|}{\alpha(H)}\), where \(\alpha\) denotes the independence number and the maximum is taken over all nonempty subgraphs _H_ of _G_. The fractional chromatic number \(\chi_f(G)\) of a graph _G_ is defined as the optimal value of the following linear program. Here, I(_G_) denotes the collection of independent vertex subsets in _G_.

