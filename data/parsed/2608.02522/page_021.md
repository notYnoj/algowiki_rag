## 4.2 Strict vector chromatic number

In this section, we prove that also the strict vector chromatic number \(\overline{\vartheta}\) is \(\chi\)-amenable, thereby completing the proof of Theorem 1.6. Before we go into the details of this, let us start by giving a convenient definition of \(\overline{\vartheta}\) in terms of positive semidefinite matrices. While many different but equivalent definitions of \(\overline{\vartheta}\) and \(\vartheta\) are known and used in the literature, we choose to present the following definition since it is particularly useful for our goal of showing \(\chi\)-amenability. The validity of this definition can be immediately verified by applying \[Lov19, Proposition 11.9\] to the complement of _G_.

**Definition 4.3.** Let _G_ be a graph. Let M_<sub>G</sub>_ denote the set of all positive semidefinite matrices \(M\in\mathrm{Sym}_{V(G)}\) such that _M<sub>u,u</sub>_=1 for all \(u\in V(G)\) and _M<sub>u,v</sub>_=0 for all distinct \(u,v\in V(G)\) such that \(uv\notin E(G)\). Then

\(\overline{\vartheta}(G)=\mathrm{max}\{\lambda_\mathrm{max}(M)|M\in\mathcal{M}_G\}.\)

The first part of the definition of \(\chi\)-amenability, namely the submultiplicativity for graph unions, is well-known and can be explicitly found in the literature on the topic:

**Lemma 4.4** (cf. Corollary 4.5 in \[GRŠS16\])**.** _For all graphs G_<sub>1</sub> _and G_<sub>2</sub> _on the same vertex-set, it holds that_

\(\overline{\vartheta}(G_1\cup G_2)\le\overline{\vartheta}(G_1)\overline{\vartheta}(G_2).\)

Hence, it remains to verify that \(\overline{\vartheta}\) satisfies the second condition in the definition of \(\chi\)- amenability. We verify this by proving the following lemma, showing that the condition holds with the absolute constant _C_:=8.

**Lemma 4.5.** _For every graph G there exists a subgraph_ \(G'\subseteq G\) _such that_ \(\overline{\vartheta}(G')\ge\overline{\vartheta}(G)/8\) _and_ \(\chi(G')\le 8\overline{\vartheta}(G')\).

The rest of this section will be devoted to the proof of this lemma (which will then complete the proof of Theorem 1.6). In the proof of Lemma 4.5, we combine Definition 4.3 with the following deep result proved by Marcus, Spielman and Srivastava \[MSS15\] in their resolution of the Kadison-Singer problem. We note that the formulation of the following result is slightly different but very easily deduced from Corollary 1.5 in \[MSS15\]. Namely, we only state the result for real-valued vectors, rather than for complex vectors as in \[MSS15\].

**Theorem 4.6** (Marcus, Spielman and Srivastava, cf. Corollary 1.5 in \[MSS15\])**.** _Let_ \(r,d,m\in\mathbb{N}\), \(\delta\in(0,1]\)_, and let_ \(u_1,\dots,u_m\in\mathbb{R}^d\) _satisfy_<tbc>

\(\sum_{i=1}^mu_iu_i^\top=I_d\text{\textit{and}}u_i^\top u_i\le\delta\text{\textit{for every}}i\in[m].\)

<tbc>_Then there is a partition_ \([m]=T_1\sqcup\cdots\sqcup T_r\) _(empty parts allowed) such that_

\(\left\|\sum_{i\in T_j}u_iu_i^\top\right\|\le\left(\frac{1}{\sqrt{r}}+\sqrt{\delta}\right)^2\)

_for every_ \(j\in[r]\).

