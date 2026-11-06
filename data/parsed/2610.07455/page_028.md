_Proof._ By Lemma 4.2, we may replace each arriving _R_-constraint by the _R<sup>⋆</sup>_-constraint on the same scope. We will describe a small representation of the value of every assignment for this _R<sup>⋆</sup>_-instance.

Fix a basepoint \(0\in C\). For a variable _x_ and a value \(a\in C\backslash\{0\}\), define the indicator \(X_{x,a}(\alpha)=\mathbf{1}[\alpha(x)=a]\). This indicator is 1 exactly when \(\alpha\) gives _x_ the value _a_, and it is 0 otherwise. By the definition of _d_=deg_<sub>C</sub>_(**1**_<sub>R<sup>⋆</sup></sub>_), membership in _R<sup>⋆</sup>_ can be written as a polynomial in the indicators of coordinate values, with every monomial involving at most _d_ coordinates. In other words, there are constants _c<sub>T,b</sub>_ such that, for every \(z=(z_1,\dots,z_k)\in C^k\),

\(\mathbf{1}_{R^\star}(z)=\sum_{T\subseteq[k]|T|\le d}\sum_{b\in(C\backslash\{0\})^T}c_{T,b}\prod_{j\in T}\mathbf{1}[z_j=b_j].\)

The relation is fixed, so this sum has _O<sub>R</sub>_(1) terms and all the constants _c<sub>T,b</sub>_ depend only on _R_. They are integers by the inclusion-exclusion description of the coefficients in Section 3.5.

Consider an arriving constraint _R<sup>⋆</sup>(x_<sub>_i_<sub>1</sub></sub>_,...,x<sub>i<sub>k</sub></sub>_). For this constraint, set \(z_j=\alpha(x_{i_j})\) for every \(j\in[k]\) in the formula above. We obtain

\(\mathbf{1}[R^\star(x_{i_1},\dots,x_{i_k})\text{is satisfied by}\alpha]=\sum_{T\subseteq[k]|T|\le d}\sum_{b\in(C\backslash\{0\})^T}c_{T,b}\prod_{j\in T}X_{x_{i_j},b_j}(\alpha).\)

This formula expresses whether \(\alpha\) satisfies this constraint as a sum of products of the indicators _X<sub>x,a</sub>_. Each product checks the values of at most _d_ variables from the scope. If the same variable appears twice in a product with the same required value, the two identical indicators can be replaced by one. If it appears with two different required values, no assignment can make both indicators equal to 1, so the product is always zero and can be omitted.

The algorithm keeps one integer counter for every product of the form \(\prod_{x\in U}X_{x,a_x}\) with \(|U|\le d\). When a constraint arrives, the algorithm writes its satisfaction indicator using the formula above and adds each _c<sub>T,b</sub>_ to the counter for the corresponding product. There are at most \(\sum_{j=0}^d\genfrac(){pt}{2}{n}{j}(|C|-1)^j=O_R(n^d)\) possible products. Each counter has magnitude _O<sub>R</sub>(m_) and therefore uses _O<sub>R</sub>_(log(_m_+1)) bits. Identifying its variables and values uses _O<sub>R</sub>_(log(_n_+1)) bits. The total space is _O<sub>R</sub>(n<sup>d</sup>_(log(_n_+1)+log(_m_+1))).

After the stream, the sum of the stored terms is exactly \(\mathrm{val}_{I^\star}(\alpha)\) for every assignment \(\alpha\), where _I<sup>⋆</sup>_ is the resulting _R<sup>⋆</sup>_-instance. The algorithm can try all assignments, evaluate this sum, and return its maximum. There is no restriction on the time used after the stream. By Lemma 4.3, this maximum is also OPT<sub>max</sub>(_I_) for the original _R_-instance _I_. Finally, a simple instance has at most _n<sup>k</sup>_ constraints, so log(_m_+1)=_O<sub>R</sub>_(log(_n_+1)).

This proves the upper bound in Theorem 7.1, including the case _d_=0. We now assume \(d\ge 1\) and prove the lower bound.

## 7.1 Lower bound for a core relation

We first prove the lower bound when _R_ is already a core. This is the main result of the subsection.

**Theorem 7.3** (Lower bound for Exact-CSP on a core relation)**.** _Let_ \(R\subseteq D^k\) _be a core relation and let_ \(d=\mathrm{deg}_D(\mathbf{1}_R)\ge 1\)_. Every randomized bounded-error one-pass algorithm for_ Exact-CSP(_R_) _on unweighted simple instances uses_ \(\Omega_R(n^d)\) _bits of space. If R is symmetric, the statement holds with unordered simplicity._

