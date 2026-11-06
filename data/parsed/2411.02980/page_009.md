<tbc>In particular, when the context of \(\Phi\) is clear, we say a subset of variables \(V'\subseteq V\) is connected if the induced sub-graph \(H_\Phi[V']\) is connected and say a subset of constraints \(\mathcal{C}'\subseteq\mathcal{C}\) is connected if the induced sub-graph \(G_\Phi[\mathcal{C}']\) is connected.

Similar to the density of random formulas (the ratio between the number of clauses and the number of variables), we define the density of hypergraphs as the ratio between the number of hyperedges and the number of vertices.

### 2.2. Lovász local lemma.

The Lovász local lemma is a gem in the probabilistic method of combinatorics and has inseparable connections with the solution space of CSPs \[EL75\]. By viewing the violation of each constraint as a bad event, the celebrated (variable framework) Lovász local lemma gives a sufficient criterion for a CSP solution to exist:

**Theorem 2.3** (Erdós and Lovász \[EL75\])**.** _Given a CSP formula_ \(\Phi=(V,[q],\mathcal{C})\)_, if the following holds_<tbc>

(2) \(\exists x\in(0,1)^C\text{\textit{s.t.}}\forall c\in\mathcal{C}:\mathcal{P}\left[\neg c\right]\le x(c)\prod_{c^\prime\in\mathcal{C}\text{vbl}(c)\cap\text{vbl}(c^\prime)\neq\emptyset}(1-x(c')),\)

<tbc>_then_

\(\mathcal{P}\left[\wedge_{c\in\mathcal{C}}c\right]\ge\prod_{c\in\mathcal{C}}(1-x(c))>0.\)

When the condition (2) is met, the probability of any event in the uniform distribution \(\mu\) over all satisfying assignments can be well approximated by the probability of that event in the product distribution. This was observed in \[HSS11\]:

**Theorem 2.4** (Haeupler, Saha, and Srinivasan \[HSS11\])**.** _Given a CSP formula_ \(\Phi=(V,[q],\mathcal{C})\)_, if_ (2) _holds, then for any event A that is determined by the assignment on a subset of variables_ \(\text{vbl}(A)\subseteq V\),

\(\mathcal{P}\left[A|\wedge_{c\in\mathcal{C}}c\right]\le\mathcal{P}\left(A\right)\prod_{c\in\mathcal{C}\text{vbl}(c)\cap\text{vbl}(A)\neq\emptyset}(1-x(c))^{-1}.\)

## 3. Structural properties of random hypergraphs

Our strategy to prove main results in Theorem 1.2 and Theorem 1.4 is to establish that both instances possess certain _structural properties_ that enable efficient counting and sampling algorithms. In this section, we will develop a "nice property" (formally defined in Definition 3.12) for the underlying incidence hypergraph. We claim that once this nice property holds for the hypergraph with specific parameters, we can efficiently count and sample solutions. Finally, we demonstrate that the conditions in Theorem 1.2 and Theorem 1.4 fulfill the desired property.

Recall the definition of incidence hypergraphs in Definition 2.2. We then present our claim as Theorem 3.2, with the "nice property" formally defined later in this section in Definition 3.12. We note that Condition 3.1 only makes assumptions to the hypergraph \(H_\Phi\), but not the atomic bad events for each constraint.

**Condition 3.1** (structural condition for atomic CSPs)**.** _For the atomic CSP instance_ \(\Phi=(V,[q],\mathcal{C})\)_, its incidence hypergraph_ \(H_\Phi\) _is_ \((k,\alpha,\varepsilon_1,\varepsilon_2,\eta,\rho,p_1,p_2)\)_-nice with parameters satisfying:_

\(\bullet\) \(k\ge 30\), \(\alpha\le q^k\), \(\eta k\ge 4\)_, and_ \(\mathrm{e}(\rho k\alpha)^\eta=1\);<tbc>

\(\bullet\) \(\varepsilon_1=2\eta\), \(p_1=6k^7\), \(\varepsilon_2=\frac{12k^5}{(1-\eta)\eta p_1}=\frac{2}{k^2(1-\eta)\eta}\le\frac{1}{k}\)_, and p_<sub>2</sub>=e_k_<sup>2</sup>.

**Theorem 3.2** (counting/sampling for atomic CSPs)**.** _Assume_ \(\Phi=(V,[q],\mathcal{C})\) _is a satisfiable atomic CSP instance satisfying Condition 3.1. Then for any_ \(\varepsilon>0\)_, there exist the following algorithms, both with running time_ \((n/\varepsilon)^{\text{poly}(\mathrm{log}q,k,\alpha)}\):

\(\bullet\) _(counting) A deterministic algorithm that outputs_ \(\hat{Z}\) _which is an_ \(\varepsilon\)_-approximation of the number of solutions_ \(Z(\Phi)\) _of_ \(\Phi\)_, i.e.,_ \((1-\varepsilon)Z(\Phi)\le\hat{Z}\le(1+\varepsilon)Z(\Phi)\);<tbc>

\(\bullet\) _(sampling) An algorithm that outputs a random assignment_ \(X\in[q]^V\) _that is_ \(\varepsilon\)_-close in total variation distance to_ \(\mu_\Phi\)_, the uniform distribution over all solutions of_ \(\Phi\).

