(v) _Asymptotic normality_ (their Proposition 8). Under finite second moments of _X_, the vector of sample L-comoments of orders 2_,...,k_ is asymptotically normal, with covariance matrix of order _n_<sup>-1</sup> given by the first-projection covariances; this agrees with the leading term _B_<sub>1</sub>_/n_ in Theorem 4.1.

Our contribution is the exact finite-sample covariance of these estimators, its estimation, and its efficient computation.

## U-statistics.

See Hoeffding (1948), Serfling (1980, Chapter 5), Lee (1990), and van der Vaart (1998). Let _Z_<sub>1</sub>_,...,Z<sub>n</sub>_ be iid, and let _h_ be a symmetric kernel of order _m_ with a finite second moment. Write \(\theta=\mathbb{E}\{h(Z_1,\dots,Z_m)\}\). The complete U-statistic \(U_n=\genfrac(){pt}{2}{n}{m}^{-1}\sum_{|I|=m}h(Z_I)\) is an unbiased estimator of \(\theta\); a sample mean is the case _m_=1. For \(1\le c\le m\), put

\(h_c(z_1,\dots,z_c)=\mathbb{E}\{h(Z_1,\dots,Z_m)|Z_1=z_1,\dots,Z_c=z_c\},\)

so that _h<sub>m</sub>=h_ and \(\mathbb{E}\{h_c(Z_1,\dots,Z_c)\}=\theta\).

## Overlap formula.

Let _U<sub>n</sub>_ and _V<sub>n</sub>_ be U-statistics with kernels _h_ of order _m_ and _g_ of order _s_. Then

\(\text{Cov}(U_n,V_n)=\sum_{c=1}^{min(m,s)}\frac{\genfrac(){pt}{2}{m}{c}\genfrac(){pt}{2}{n-m}{s-c}}{\genfrac(){pt}{2}{n}{s}}\text{Cov}\{h_c(Z_1,\dots,Z_c),g_c(Z_1,\dots,Z_c)\}.\) (A.1)

Terms with disjoint index sets contribute zero, and a term whose index sets share _c_ observations contributes the covariance of the conditional kernels given those observations (Hoeffding, 1948).

## Hoeffding decomposition.

Define the canonical kernels recursively by \(h^{(1)}(z_1)=h_1(z_1)-\theta\) and, for \(c\ge 2\),<tbc>

\(h^{(c)}(z_1,\dots,z_c)=h_c(z_1,\dots,z_c)-\theta-\sum_{j=1}^{c-1}\sum_{1\le i_1<\cdots<i_j\le c}h^{(j)}(z_{i_1},\dots,z_{i_j}).\)

<tbc>Each _h_<sup>(_c_)</sup> has zero conditional mean given any proper subset of its arguments. With \(U_n^{(c)}=\genfrac(){pt}{2}{n}{c}^{-1}\sum_{|I|=c}h^{(c)}(Z_I)\),

\(U_n-\theta=\sum_{c=1}^m\genfrac(){pt}{2}{m}{c}U_n^{(c)},\) (A.2)

and the terms are uncorrelated across _c_. In particular, \(\text{Var}(U_n)=\sum_{c=1}^m\genfrac(){pt}{2}{m}{c}^2\genfrac(){pt}{2}{n}{c}^{-1}\text{Var}\{h^{(c)}\}\), whose leading term is _m_<sup>2</sup>Var{_h_<sub>1</sub>(_Z_<sub>1</sub>)}_/n_ (Lee, 1990).

