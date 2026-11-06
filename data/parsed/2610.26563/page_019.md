## 6 Border-rank bounds by parameter scaling

We now develop border-rank constructions that eliminate mixed products by scaling the variable blocks by powers of \(\lambda\). This suppresses the unwanted products in B(S) of Definition 17, including conflicts between tripartitions, and can also suppress replicated terms without computing their corrections. Desired products have degree zero, while each unwanted product is either canceled by corrections or has positive degree and tends to zero with \(\lambda\). The resulting limit gives a border-rank bound \[9, 37\].

**Definition 18** (Grading)**.** _A grading of_ S _assigns_ \((a_t,b_t,c_t)\in\mathbb{Q}^3\) _for t_=1_,...,m such that_<tbc>

\(a_t+b_t+c_t=0\) (98)

<tbc>_and_

\(a_i+b_j+c_k>0((i,j,k)\in\mathcal{B}(\mathcal{S})).\) (99)

_The grading is integral when all exponents are integers._

Rational exponents permit rescaling the smallest positive degree of the remaining mixed products to one in Section 7.1. Replacing \(\lambda\) by a suitable positive integer power gives the same family of tensors with integer exponents.

**Lemma 7.** _If_ S _admits a grading, then each of the maps_ \(t\mapsto U_t\), \(t\mapsto V_t\)_, and_ \(t\mapsto W_t\) _is injective._

_Proof._ If _U<sub>i</sub>=U<sub>j</sub>_ for \(i\neq j\), then both (_i,j,j_) and (_j,i,i_) lie in B(S). Applying (99) to these choices and using _a<sub>t</sub>+b<sub>t</sub>+c<sub>t</sub>_=0 gives _a<sub>i</sub>-a<sub>j</sub>\>_0 and _a<sub>j</sub>-a<sub>i</sub>\>_0, a contradiction. The other two projections are analogous.

Replicated mixed terms of positive degree tend to zero with \(\lambda\). We therefore select corrections only for those of nonpositive degree.

**Definition 19** (Corrections for nonpositive degrees)**.** _For a grading of_ S_, define_

\(\mathcal{Q}_{\le 0}=\bigcup_{a_i+b_j+c_k\le 0}\{P:\emptyset\neq P\subseteq\mathcal{R}_{ijk}\},\) (100)

_where the union is over non-diagonal triples with_ \(\eta_r(i,j,k)\neq 2\) _for every_ \(r\in F\).

Correction sets can be shared, so this choice may also cancel terms of positive degree. A construction is _correction-free_ when its selected correction family is empty.

More generally, let \(\mathcal{Q}\subseteq\mathcal{P}(\mathcal{S})\) be any selected correction family. Using the multiplication budget \(\rho_\mathcal{S}(n)\) from (90), the budget for the main aggregate and the selected corrections is<tbc>

\(\rho_{\mathcal{S},\mathcal{Q}}(n)=(n+1)^d+\sum_{P\in\mathcal{Q}}(n+1)^{d-|P|}\le\rho_\mathcal{S}(n).\) (101)

<tbc>For \(\lambda>0\), substitute \(\lambda^{a_t}X^{(t)}\), \(\lambda^{b_t}Y^{(t)}\), and \(\lambda^{c_t}Z^{(t)}\) for the variable blocks in (82), and denote the resulting aggregate by \(\mathcal{A}_{\mathcal{S},\lambda}(P)\). Then<tbc>

\(\Phi_{\mathcal{S},\mathcal{Q}}(\lambda)=\mathcal{A}_{\mathcal{S},\lambda}(\emptyset)+\sum_{P\in\mathcal{Q}}(-1)^{|P|}(n+1)^{|P|}\mathcal{A}_{\mathcal{S},\lambda}(P).\) (102)

<tbc>Applying (87) to the scaled blocks gives

\(\Phi_{\mathcal{S},\mathcal{Q}}(\lambda)=\phi_\mathcal{S}+\sum_{(i,j,k)\text{non-diagonal}\eta_r(i,j,k)\neq 2\text{for all}r\in F}c_\mathcal{Q}(\mathcal{R}_{ijk})\lambda^{a_i+b_j+c_k}\phi_{ijk}.\) (103)

When Q=P(S), this is the scaled version of (92), with only the mixed products in B(S) remaining.

