CFI(_E<sub>n</sub>,_even).<sup>33</sup> Further, \[CFI92, Theorem 6.2\] yields that CFI(_E<sub>n</sub>,_odd) and CFI(_E<sub>n</sub>,_even) are non-isomorphic. Hence, CFI(CFI(_E<sub>n</sub>,_odd))=1 and CFI(CFI(_E<sub>n</sub>,_even))=0.

**Theorem 8.20.** _There exist an decision problem_ \(\Pi=(\mathcal{G},\mathrm{CFI}:\mathcal{G}\rightarrow\{0,1\})\) _such that_ \(\Pi\) _is polynomial time solvable and for all_ \(\ell\) _the problem_ \(\Pi\) _is not_ \(\ell\)-WL invariant.

_Proof._ Let \(\Pi\) be the problem that given a graph _G_ decides if CFI(_G_)=1. By Lemma 8.19, \(\Pi\) is polynomial time solvable but for all \(\ell\) the problem \(\Pi\) is not \(\ell\)_-WL invariant._

Theorem 8.3 shows that if a problem is \(\ell\)-WL invariant than it is polynomial time solvable inside the Isomorphic-Priors model. However, Theorem 8.20 demonstrates that there are problems that are in P (and that are therefore polynomial time solvable inside the Isomorphic-Priors model) but for which our Weisfeiler-Leman approach fails.

_Remark_ 8.21. The original CFI graph construction can be viewed as a graph-theoretic encoding of parity information. More specifically, the underlying idea of CFI graphs is closely related to the solvability of linear systems over the finite field F<sub>2</sub>, with the gadgets enforcing local parity constraints (see \[DGH<sup>+</sup>13\]). It follows that solving linear equations over F<sub>2</sub> is not invariant under \(\ell\)-WL for any \(\ell\). This therefore yields another polynomial-time solvable problem that cannot be captured by Weisfeiler-Leman.

We note that, using similar constructions, the same can be proved for several other hard problems, e.g., for counting certain (induced) subgraphs \[Neu24a, LB24, DMW24, CN25, DMW25\] or dominating set \[GGR24\].

## 9 Conditional Lower Bounds

In this section, we prove different hardness results for the Isomorphic-Priors model. As our source of hardness, we use the Graph Isomorphism problem.

**Definition 9.1** (Graph Isomorphism (GI))**.** In the Graph Isomorphism problem we are given a pair of graphs _I_=(_G_<sub>0</sub>_,G_<sub>1</sub>) and have to decide if \(G_0\cong G_1\).

Two problem instances _I_=(_G_<sub>0</sub>_,G_<sub>1</sub>) and _J_=(_H_<sub>0</sub>_,H_<sub>1</sub>) are isomorphic if \(G_0\cong H_0\) and \(G_1\cong H_1\).

Up to this date, it is not known whether GI is in P despite a lot of effort from many researchers \[Koz78\]. We can therefore use GI as a source of hardness and show that many problems are not polynomial time solvable inside the Isomorphic-Priors model unless \(\mathsf{GI}\in P\), which would be a breakthrough result.

Furthermore, it is not known if GI is in coMA.<sup>34</sup> Again, we can use this as a source of hardness. We show in Section 9.1 that GI is not polynomial time solvable within our model unless \(\mathsf{GI}\in\mathsf{coMA}\).

Next, we are utilizing the hardness of GI to obtain further hardness results within our model for "normal" decision problems \(\Pi\). To this end, we associate each problem \(\Pi\) with a specific promise version of the same problem that we denote as Iso-\(\Pi\). See Section 9.2 for a formal definition. We<tbc>

<sup>33</sup>By \[CFI92, Theorem 6.4\], we obtain \(\mathrm{CFI}(E_n,\mathrm{odd})\equiv_{\mathcal{C}_{\ell+1}}\mathrm{CFI}(E_n,\mathrm{even})\). By \[CFI92, Theorem 5.2\], this is equivalent to \(\mathrm{CFI}(E_n,\mathrm{odd})\equiv_{\ell\text{-}\mathsf{WL}}\mathrm{CFI}(E_n,\mathrm{even})\). <sup>34</sup>The complexity class MA consists of all languages _L_ for which there exist a polynomial-time deterministic Turing machine _M_ and polynomials _p_, _q_ such that for every input string _x_ of length _n_:=|_x_|, \(\bullet\) if \(x\in L\) then there exist a \(z\in\{0,1\}^{q(n)}\) with \(\mathrm{Pr}_{y\in\{0,1\}^{p(n)}}[M(x,y,z)=1]\ge 2/3\), \(\bullet\) if \(x\notin L\) then for all \(z\in\{0,1\}^{q(n)}\) we obtain \(\mathrm{Pr}_{y\in\{0,1\}^{p(n)}}[M(x,y,z)=0]\ge 2/3\). The class coMA consists of all languages whose complement is in MA.

