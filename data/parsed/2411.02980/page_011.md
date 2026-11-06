The following structural properties are useful in our counting and sampling algorithms.

**Property 3.10** (bounded number of bad vertices)**.** _Given a hypergraph H_=(_V,_E)_, for any_ \(V_0\subseteq V\), \(|V_\mathrm{bad}(V_0)|\le 4\varepsilon_1^{-1}|\mathrm{HD}(V_0)|\)_, where V_<sub>bad</sub>(_V_<sub>0</sub>) _is obtained from Algorithm 1._

**Property 3.11** (bounded fraction of bad hyperedges)**.** _Given a hypergraph H_=(_V,_E)_, let_ E<sub>bad</sub>=E<sub>bad</sub>(_V_) _be the set of bad hyperedges obtained from Algorithm 1. For any_ \(\ell\ge\mathrm{log}n\) _and any connected subset of hyperedges in_ Lin(_H_) _of size_ \(\ell\)_, the number of bad hyperedges among them is at most_ \(\varepsilon_2\ell\).

**Definition 3.12** (nice hypergraph)**.** We say a hypergraph _H_=(_V,_E) is \((k,\alpha,\varepsilon_1,\varepsilon_2,\eta,\rho,p_1,p_2)\)_-nice_ if with the choice of _p_<sub>1</sub> at Definition 3.7 and \(\varepsilon_1\) at Algorithm 1, the hypergraph _H_:

\(\bullet\) is in \(\mathcal{H}_{\le k}\) and has density \(\alpha\) where \(\alpha\le q^k\);<tbc>

\(\bullet\) satisfies bounded maximum degree defined at Property 3.4;<tbc>

\(\bullet\) satisfies \((\eta,\rho)\)-constraint expansion defined at Property 3.5;<tbc>

\(\bullet\) satisfies bounded neighbourhood growth with parameter _p_<sub>2</sub> at Property 3.6;<tbc>

\(\bullet\) satisfies bounded number of bad vertices with parameter \(\varepsilon_1\) at Property 3.10;<tbc>

\(\bullet\) satisfies bounded fraction of bad hyperedges with parameter \(\varepsilon_2\) at Property 3.11;<tbc>

\(\bullet\) has no connected components of size \(\ell\ge\mathrm{log}n\) in the line graph induced by bad hyperedges.

The following key lemma shows that if all parameters \((k,\alpha,\varepsilon_1,\varepsilon_2,\eta,\rho,p_1,p_2)\) satisfy Condition 3.1, then the underlying incidence hypergraphs of random _k_-SAT formulas is nice with probability 1-_o_(1_/n_).

**Lemma 3.13.** _For any fixed parameters_ \(k,\alpha,\eta,\rho,\varepsilon_1,p_1,\varepsilon_2,p_2\) _where_ \(\eta k\ge 4\), \(\mathrm{e}(\rho k\alpha)^\eta\le 1\), \(\varepsilon_1=2\eta\), \(6k^5\le p_1\le\mathrm{e}^{k-2}\alpha\), \(\varepsilon_2=12k^5/((1-\eta)\eta p_1)\) _and p_<sub>2</sub>=e_k_<sup>2</sup>_, with probability_ 1-_o_(1_/n_) _over the choice of random k-SAT formulas_ \(\Phi=\Phi(k,n,m)\) _with density_ \(\alpha\), \(H_\Phi\) _is_ \((k,\alpha,\varepsilon_1,\varepsilon_2,\eta,\rho,p_1,p_2)\)_-nice._

The proof of Lemma 3.13 is deferred to Appendix A. In fact, the same result also holds for random _k_-uniform hypergraphs. The following lemma states that if the incidence hypergraph of a random _k_-SAT formula satisfies some structural property with high probability, then a random hypergraph also satisfies the same property with high probability.

**Lemma 3.14.** _Suppose_ \(k\ge 3\) _and_ \(\alpha\) _are constants. Let_ P _be a property for hypergraphs (i.e.,_ P _is a subset of hypergraphs). If the probability of_ \(H_\Phi\) _belonging to_ P _is_ 1-_o_(1_/n), over the choice of random k-SAT formulas_ \(\Phi\sim\Phi(k,n,\lfloor\alpha n\rfloor)\) _with density_ \(\alpha\)_, then a random k-uniform hypergraph_ \(H\sim H(k,n,\lfloor\alpha n\rfloor)\) _with density_ \(\alpha\) _belongs to_ P _with probability_ 1-_o_(1_/n_) _as well._

_Proof._ Let \(m=\lfloor\alpha n\rfloor\), and E_<sub>k,n,m</sub>_ be the event that the incidence hypergraphs \(H_\Phi\) is a _k_-uniform hypergraph with _n_ vertices and _m_ distinct hyperedges. It is easy to see that

\(\mathbf{Pr}_{\Phi\sim\Phi(k,n,m)}[H_\Phi=H|\mathcal{E}_{k,n,m}]=\mathbf{Pr}_{H(k,n,m)}[H],\)

namely, the distribution of the incidence hypergraph \(H_\Phi\) conditional on it being _k_-uniform and having _m_ distinct hyperedges is the uniform distribution _H(k,n,m_).

Note that if _n_ is sufficiently large, we obtain that

\(\mathbf{Pr}_{\Phi\sim\Phi(k,n,m)}[H_\Phi\text{is}k\text{-uniform}]=\left(\frac{n-1}{n}\cdot\frac{n-2}{n}\cdots\frac{n-k+1}{n}\right)^m\)<br>
\(\ge\left(1-\frac{k-1}{n}\right)^{(k-1)m}\ge\mathrm{e}^{-k^2\alpha},\)

and

\(\mathbf{Pr}_{\Phi\sim\Phi(k,n,m)}[H_\Phi\text{has two identical hyperedges}]\le\genfrac(){pt}{2}{m}{2}\frac{k!}{n^k}\le\frac{k!\alpha^2}{2n^k},\)

which further implies that

\(\mathbf{Pr}_{\Phi\sim\Phi(k,n,m)}[\mathcal{E}_{k,n,m}]\ge\mathrm{e}^{-k^2\alpha}-\frac{k!\alpha^2}{2n^k}\ge\frac{1}{2}\mathrm{e}^{-k^2\alpha}\)

