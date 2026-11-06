After two recursive levels, each uncertain biclique corresponds to a subproblem _T(q,q_), where _q_=log<sup>6</sup>log_n_. Hence, the total running time satisfies

\(T(n,n)=O(n^{4/3}/\mathrm{loglog}n)+O(n^{4/3}/\mathrm{log}^8\mathrm{log}n)\cdot T(q,q).\) (5)

We next solve the subproblem _T(q,q_). Since _q_ is sufficiently small (e.g., 2<sup>poly(_q_)</sup>=_O(n_) for any polynomial function \(\mathrm{poly}(\cdot))\), we can exploit the \(\Gamma\)-framework of Chan and Zheng \[10\].

Let _g_=log<sup>(_i_-2)</sup>_q_. We first apply Recurrence (2) with _m=n=q_ and _r=q_<sup>1/3</sup>_/g_<sup>2</sup>, obtaining

\(T(q,q)=O\left(\frac{q^{4/3}}{g^2}\right)+O\left(\frac{q^{2/3}}{g^4}\right)\cdot T\big(q^{1/3}g^4,q^{2/3}g^2\big).\) (6)

As before, we add the number of certified pairs produced by the recurrence to \(\hat{\kappa}(I)\).

### Solving subproblems _T(q_<sup>1/3</sup>_g_<sup>4</sup>_,q_<sup>2/3</sup>_g_<sup>2</sup>).

We now solve the subproblem _T(q_<sup>1/3</sup>_g_<sup>4</sup>_,q_<sup>2/3</sup>_g_<sup>2</sup>), which corresponds to an uncertain biclique \(A'\times B'\) with \(A'\subseteq A\), \(B'\subseteq B\), \(|A'|\le q^{1/3}g^4\), and \(|B'|\le q^{2/3}g^2\). Let \(m'=|A'|\) and \(n'=|B'|\).

Let \(\mathcal{D}'\) be the set of annuli defined by the points of \(A'\) with respect to the interval _I_. We compute a hierarchical \((1/r')\)-cutting \(\{\Xi_0,\Xi_1,\dots,\Xi_k\}\) for \(\mathcal{D}'\), where \(r'=m'/g^6\). This takes \(O(m'r')\) time. For every cell \(\sigma\) of the last cutting \(\Xi_k\), let \(m'_\sigma\) denote the number of annuli of \(\mathcal{D}'\) that completely contain \(\sigma\). Since each cutting cell has _O_(1) children, all values \(m'_\sigma\) can be computed in \(O(m'r')\) time by traversing the cutting tree.

Next, we locate every point of \(B'\) in the last cutting \(\Xi_k\). A straightforward point location procedure would require \(O(\mathrm{log}r')\) time per point, which is not efficient enough for our purpose. To avoid this overhead, we apply the \(\Gamma\)-framework of Chan and Zheng \[10\].

Since _q_=log<sup>6</sup>log_n_, the subproblem size is sufficiently small for the framework to be effective. In a manner similar to \[10, Lemma 4.4\], each point location can be performed in amortized _O_(1) time (say, after _O(n_<sup>5/4</sup>)-time preprocessing for _A_ and _B_). Note that the point location problem in \[10, Lemma 4.4\] is on a line arrangement, whereas our point location problem is on a cutting \(\Xi_k\). Nevertheless, the same idea applies by exploiting the hierarchical structure of the cuttings; see Section 5.3 of the arXiv version of \[26\] for a similar problem.

Consequently, all point locations for the points of \(B'\) can be performed in \(O(n')\) amortized time. After that, we obtain the canonical subsets \(B'(\sigma)=B'\cap\sigma\) for all cells \(\sigma\in\Xi_k\).

For each cell \(\sigma\), we add \(m'_\sigma\cdot|B'(\sigma)|\) to \(\hat{\kappa}(I)\). This is the key difference from the cases _i_=1,2: certified pairs are counted implicitly through cutting cells rather than explicitly through bicliques.

The unresolved pairs are represented by bicliques \(\hat{A}'_\sigma\times B'(\sigma)\), where \(\hat{A}'_\sigma=\{a\in A'|D_a\in\mathcal{D}'_\sigma\}\). Since \(|\hat{A}'_\sigma|\le m'/r'\) and \(\sum_\sigma|B'(\sigma)|=n'\), the total number of unresolved pairs for the subproblem \(T(m',n')\) is \(O(m'n'/r')\). The running time of the subproblem is \(O(m'r'+n')\).

Since \(r'=m'/g^6\), \(m'\le q^{1/3}g^4\), and \(n'\le q^{2/3}g^2\), we obtain \(T(m',n')=O(q^{2/3}g^2)\), while the number of unresolved pairs is _O(q_<sup>2/3</sup>_g_<sup>8</sup>). Substituting these bounds into (6) yields _T(q,q_)=_O(q_<sup>4/3</sup>_/g_<sup>2</sup>), and the total number of unresolved pairs is _O(q_<sup>4/3</sup>_g_<sup>4</sup>).

Substituting these bounds into (5) yields _T(n,n_)=_O(n_<sup>4/3</sup>_/g_<sup>2</sup>), and the total number of unresolved pairs is _O(n_<sup>4/3</sup>_g_<sup>4</sup>). Recalling that _g_=log<sup>(_i_-2)</sup>_q_, we conclude that the total running time is _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>), while \(|\hat{\kappa}(I)-\kappa(I)|=O(n^{4/3}(\mathrm{log}^{(i)}n)^4)\).

This proves Theorem 1 for all \(i\ge 3\).

## 4 Distance representation

The approximate counting algorithm of Section 3 is sufficient for quasi-decision. However, it does not directly yield an _O(n_<sup>4/3</sup>)-time distance selection algorithm, because distance selection ultimately<tbc>

