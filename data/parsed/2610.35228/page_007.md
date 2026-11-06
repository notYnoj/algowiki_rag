_Proof._ The conditional marginals are well defined because

\(|S\cup T|\le|S|+2(r-|S|)\le 2r.\)

The first step uses \(|S\cup T|\le|S|+|T|\) and the bound \(|T|\le 2(r-|S|)\), and the second step uses \(|S|\ge 0\). The condition in Definition 3.1-(a) is immediate. For Definition 3.1-(b), if _T_ contains an edge, then so does \(S\cup T\), so \(\nu_S(T)=0\).

For Definition 3.1-(c), let \(r':=r-|S|\) and \(x\in\mathbb{R}^{\mathcal{V}_{r^\prime}}\). The map \(\phi(A):=A\cup S\) sends \(\mathcal{V}_{r^\prime}\) into V_<sub>r</sub>_. Define \(y\in\mathbb{R}^{\mathcal{V}_r}\) by \(y_C:=\sum_{A\in\mathcal{V}_{r^\prime}:\phi(A)=C}x_A\). Since \(\phi(A)\cup\phi(B)=A\cup B\cup S\),

\(x^\top M_{r^\prime}[\nu_S]x=\frac{1}{\nu(S)}\sum_{A\in\mathcal{V}_{r^\prime}}\sum_{B\in\mathcal{V}_{r^\prime}} x_Ax_B\nu(\phi(A)\cup\phi(B))=\frac{1}{\nu(S)}y^\top M_r[\nu]y\ge 0.\)

The first step substitutes Eq. (8) into the quadratic form; the second step groups indices with the same image under \(\phi\) and uses the definition of _y_; and the third step follows from Definition 3.1-(c) and \(\nu(S)>0\).

The identity \(\nu(S\cup\{v\})=\nu(S)\nu_S(v)\) follows from the definition of \(\nu_S(v)\). Under the additional assumption \(|S|\le r-2\), the pseudo-distribution \(\nu_{S\cup\{v\}}\) has at least one level. Finally,

\(\nu_{S\cup\{v\}}(u)=\frac{\nu(S\cup\{u,v\})}{\nu(S\cup\{v\})}=\frac{\nu(S\cup\{u,v\})/\nu(S)}{\nu(S\cup\{v\})/\nu(S)}=\frac{\nu_S(u,v)}{\nu_S(v)}.\)

The first step is the definition of conditioning; the second step divides numerator and denominator by the positive number \(\nu(S)\); and the third step uses Eq. (8). The pair {_u,v_} lies in V<sub>2(_r_-|_S_|)</sub>, as required.

The normalized covariance matrix of a pseudo-distribution is positive semidefinite, and its entrywise powers have nonnegative sums. For odd powers, this forces positive correlations to compensate for the negative contribution of edges.

**Lemma 3.4** (Odd moments of the normalized covariance)**.** _Let_ \(\nu\) _be a level-r pseudo-distribution with_ \(r\ge 1\)_. Let_ \(U\subseteq V\) _be nonempty with_ \(\nu(u)>0\) _for every_ \(u\in U\)_. For_ \(u,v\in U\) _define_<tbc>

\(M(u,v):=\frac{\nu(u,v)}{\nu(u)\nu(v)}-1.\) (10)

<tbc>_Then the matrix_ \(M=(M(u,v))_{u,v\in U}\) _is positive semidefinite. Moreover, for every positive integer_ \(\ell\),

\(\sum_{u\in U}\sum_{v\in U}M(u,v)^\ell\ge 0.\) (11)

_Proof._ Let \(a\in\mathbb{R}^U\). Define \(b\in\mathbb{R}^{\mathcal{V}_r}\) by \(b_{\{u\}}:=a_u/\nu(u)\) for \(u\in U\), \(b_\emptyset:=-\sum_{u\in U}a_u\), and _b<sub>A</sub>_:=0 otherwise. By Definition 3.1-(a) and Definition 3.1-(c),

\(0\le b^\top M_r[\nu]b=\sum_{u\in U}\sum_{v\in U}\frac{a_ua_v\nu(u,v)}{\nu(u)\nu(v)}-2(\sum_{u\in U}a_u)^2+(\sum_{u\in U}a_u)^2=a^\top Ma.\)

The first step follows from Definition 3.1-(c); the second step expands the quadratic form using the definition of _b_ and Definition 3.1-(a); and the third step collects terms and uses Eq. (10). Thus _M_ is positive semidefinite.

