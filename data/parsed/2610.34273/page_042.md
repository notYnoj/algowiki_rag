If two largest entries are equal, admissibility forces all other entries to be one, so the remaining multiset does not depend on which largest entry is removed. Extend V_<sub>n</sub>_ recursively to F_<sub>n</sub>_ by

\(\mathcal{V}_n(X\oplus_KY)=\mathcal{V}_n(X)+\mathcal{V}_n(Y),\)<br>
\(\mathcal{V}_n(X\otimes_KY)=\mathcal{V}_n(X)\mathcal{V}_n(Y),\)<br>
\(\mathcal{V}_n(X\boxplus_eY)=\left(\mathcal{V}_n(X)^{1/\eta_n}+\mathcal{V}_n(Y)^{1/\eta_n}\right)^{\eta_n}.\)

All values are positive. The definition is invariant under permutations of the legs, but depends on the formal expression.

For _n_=3 and \(1\le a\le b\), this gives

\(\mathcal{V}_3(\mathsf{C}_3(a,b))=\left(\frac{3a-1}{2}\right)^{1/4}\left(\frac{a+2b-1}{2}\right)^{3/4}.\)

Thus the construction agrees exactly with the symmetric square-multiplication certificate of Amanov, van den Berg, and Zuiddam \[ABZ26, Equation (5.3)\]. The function _H_<sub>_n_-1</sub> and the simultaneous separation budget provide the extension to arbitrary order.

It remains to check that no permitted rule increases the certificate when passing from its source to its target. The verification below treats the rules in Definition 5.5 one by one; in particular, it checks the separation rule for arbitrary block counts and retained edge dimensions.

**Lemma 5.10** (monotonicity of the certificate)**.** _For every integer_ \(n\ge 3\) _and all_ \(X,Y\in\mathcal{F}_n\)_, if_ \(X\unknown_{\mathrm{poly},n}Y\) _, then_ \(\mathcal{V}_n(X)\le\mathcal{V}_n(Y)\).

_Proof._ Write \(\eta=\eta_n\), so \(0<\eta<1\). We check every generator in Definition 5.5. Ordinary addition and multiplication of positive numbers preserve inequalities, as do leg permutations because \(\mathcal{V}_n(\pi X)=\mathcal{V}_n(X)\). This proves compatibility with rule (i).

For the algebraic identities, the full operations evaluate to ordinary addition and multiplication. A partial sum of values _w_<sub>1</sub>_,...,w<sub>m</sub>_ evaluates to \((\sum_{i=1}^mw_i^{1/\eta})^\eta\), independent of its order and bracketing. For products of partial sums, the corresponding identity is<tbc>

\(\left(\sum_{i=1}^rw_i^{1/\eta}\right)^\eta\left(\sum_{j=1}^sz_j^{1/\eta}\right)^\eta=\left(\sum_{i=1}^r\sum_{j=1}^s(w_iz_j)^{1/\eta}\right)^\eta.\)

<tbc>The normalization in Lemma 5.8 gives

\(\mathcal{V}_n(\mathbf{I}_n(R))=R,\mathcal{V}_n(\mathbf{E}_{i,j}^{(q)})=q^\eta(R,q\ge 1,1\le i<j\le n).\)

Thus edge products preserve value, and _r_ equal partial summands of value _w_ have value \(r^\eta w\), as required for the repeated-block identity.

For block deletion and passage from a full sum to a partial sum, use

\(\mathrm{max}_{1\le i\le m}w_i\le\left(\sum_{i=1}^mw_i^{1/\eta}\right)^\eta\le\sum_{i=1}^mw_i.\)

The first inequality follows by retaining one summand. For the second, put \(r=1/\eta\ge 1\) and \(W=\sum_{i=1}^mw_i\). Then \(w_i^r\le w_iW^{r-1}\) for every _i_, and summing gives \(\sum_{i=1}^mw_i^r\le W^r\). Polynomial truncation follows from coordinate monotonicity of _H<sub>d</sub>_. The interpolation and star comparisons are exactly the two upper bounds in Lemma 5.8, raised to the power \(\eta\) where appropriate.

