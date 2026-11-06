**Definition 1.2** (\[KPW26\])**.** Let (_P,_d) be a finite metric space and \(\beta\ge\alpha\ge 1\). A directed graph _G_=(_P,E_) is a \((\alpha,\beta)\)_-bricriteria c-approximation_ to the sparsest \(\alpha\)-navigable graph if _G_ is \(\alpha\)-navigable and

\(|E|\le c\cdot min_H\text{is}\beta\text{-navigable}|E(H)|.\)

To unify notation, the single criterion problem of approximating \(\alpha\)-navigable graphs can be written as a \((\alpha,\alpha)\)-bricriteria problem. In \[KPW26\], it was shown that a \((\alpha,2(1+\epsilon)\alpha)\)-bricriteria _O_(log_n_)-approximation can be computed by an algorithm in \(\tilde{O}(n^\omega log\Delta/\epsilon)\) time, where \(\Delta\) is the aspect ratio of metric (_P,_d) and \(\omega\) is the matrix multiplication exponent. The following question was left open in \[KPW26\].

_Question_ 1.3. Is there a quadratic-time algorithm for (bricriteria) _O_(log_n_)-approximation of the sparsest \(\alpha\)-navigable graph?

## 1.1 Our Results.

As our main algorithmic result, we answer Question 1.3 affirmatively up to polylogarithmic factors in the bicriteria setting. More precisely, we give a near-quadratic-time construction whose bicriteria guarantees improve upon the previous fastest algorithm and are essentially tight in the large-\(\alpha\) regime.

**Theorem 1.4.** _Let_ (_P,_d) _be an n-point metric space with aspect ratio_ \(\Delta\) _and_ \(\alpha\ge 1\) _be a constant parameter. Then, there is an algorithm with runtime_ \(\tilde{O}(n^2log\Delta)\) _which builds an_ \(\alpha\)_-navigable graph G_=(_P,E_) _with the following bicriteria approximation guarantees simultaneously._

• _G is an_ \((\alpha,\beta)\)_-bricriteria_ 5_-approximation, where_ \(\beta=2\alpha+8+4/\alpha\le 2\alpha+12\);<tbc>

• _G is an_ \((\alpha,\beta')\)_-bricriteria O_(ln_n)-approximation, where_ \(\beta'=\alpha+5+2/\alpha\le\alpha+7\).

The first guarantee shows that the Set Cover barrier can be bypassed by allowing an almost factor-2 relaxation in the bicriteria parameter: instead of an _O_(log_n_)-approximation, we obtain a constant-factor approximation against the sparsest \((2\alpha+O(1))\)-navigable graph. The second guarantee gives an _O_(log_n_)-approximation with a smaller bicriteria loss than the previous fast bicriteria algorithm of \[KPW26\]; in particular, for large constant \(\alpha\), the leading coefficient improves from roughly \(2\alpha\) to roughly \(\alpha\). Another main contribution is the running time: both guarantees are achieved in \(\widetilde{O}(n^2log\Delta)\) time, improving over the \(\widetilde{O}(n^\omega log\Delta/\epsilon)\)-time fast bicriteria algorithm of \[KPW26\]. Since the input metric is specified by \(\Theta(n^2)\) pairwise distances, this running time is optimal up to logarithmic factors if pairwise distances are given explicitly.

Our second result shows that the factor 2 appearing above is essentially unavoidable. Below \(2\alpha\), the Set Cover barrier persists.

**Theorem 1.5.** _For every constant_ \(\alpha\ge 1\) _and every constant_ \(\eta\in(0,1)\)_, there exists a constant_ \(c_\eta>0\) _such that it is NP-hard to compute an_ \((\alpha,2\alpha-\eta)\)_-bricriteria_ \(c_\eta lnn\)_-approximation of the sparsest_ \(\alpha\)_-navigable graph on a metric_ (_P,_d) _with n points._

Together with Theorem 1.4, Theorem 1.5 shows that our two upper-bound guarantees are nearly optimal in complementary ways. First, the lower bound shows that the Set Cover barrier persists for every bicriteria parameter strictly below \(2\alpha\): even if the algorithm is allowed to compare against the sparsest \((2\alpha-\eta)\)-navigable graph, an _o_(log_n_)-approximation remains NP-hard. Therefore, in the entire sub-\(2\alpha\) bicriteria regime, the best possible approximation factor is \(\Theta(logn)\); our \((\alpha,\alpha+O(1))\)-bricriteria _O_(log_n_)-approximation matches this approximation factor while using bicriteria<tbc>

