## 7.1 Approximation error

For the selected corrections Q, the remaining mixed products J of Definition 20 contribute to the approximation error with coefficients (86).

For \(\mathcal{J}\neq\emptyset\), let _g\>_0 be the smallest value of _a<sub>i</sub>+b<sub>j</sub>+c<sub>k</sub>_ among \((i,j,k)\in\mathcal{J}\). In the error analysis we divide all block exponents by _g_, keeping the correction family fixed. The resulting tensor at parameter \(\lambda\) is the original tensor in (102) at parameter \(\lambda^{1/g}\). Thus we may normalize the smallest degree among the remaining mixed products to one.

**Definition 21** (Normalized grading and growth exponent)**.** _For_ \(\mathcal{J}\neq\emptyset\)_, a grading is normalized if_

\(min_{(i,j,k)\in\mathcal{J}}(a_i+b_j+c_k)=1.\) (109)

_Its growth exponent is_

\(h=-min_{1\le t\le m}a_t-min_{1\le t\le m}b_t-min_{1\le t\le m}c_t.\) (110)

_For exact constructions, we use zero exponents and h_=0.

**Definition 22** (Parameter-dependent bilinear map)**.** _For a normalized grading from Definition 21, let_<tbc>

\(e_{ijk}=a_i+b_j+c_k((i,j,k)\in\mathcal{J}).\) (111)

<tbc>_For_ \(0<\lambda\le 1\)_, let z stack the variables Z_<sup>(_t_)</sup> _in the output order of_ (108)_. Define_ \(\mathcal{M}_\lambda\) _by_

\(\big\langle\mathcal{M}_\lambda(x,y),z\big\rangle=\phi_\mathcal{S}(X,Y,Z)+\sum_{(i,j,k)\in\mathcal{J}}c_\mathcal{Q}(\mathcal{R}_{ijk})\lambda^{e_{ijk}}\phi_{ijk}.\) (112)

_This is the form in_ (103)_, evaluated with the normalized grading._

**Definition 23** (Approximation bound)**.** _For the construction in Definition 22, define_<tbc>

\(\beta(\lambda)=\sum_{(i,j,k)\in\mathcal{J}}|c_\mathcal{Q}(\mathcal{R}_{ijk})|(n+1)^{|\mathcal{R}_{ijk}|}\lambda^{e_{ijk}},0\le\lambda\le 1.\) (113)

<tbc>**Lemma 8** (Approximation error)**.** _For_ \(\mathcal{M}_\lambda\) _from Definition 22 and_ \(0<\lambda\le 1\),

\(\|\mathcal{M}_\lambda-\mathcal{M}\|\le\beta(\lambda).\) (114)

_Proof._ For \((i,j,k)\in\mathcal{J}\), set \(\bar{X}=\mu^{\otimes|U_i^c|}(X^{(i)})\), \(\bar{Y}=\mu^{\otimes|V_j^c|}(Y^{(j)})\), and \(\bar{Z}=\mu^{\otimes|W_k^c|}(Z^{(k)})\). By (81), \(\Gamma_{U_i}(X^{(i)})\unknown=\bar{X}\unknown_{|U_i^c}\), and similarly for _Y,Z_. Coordinates in R_<sub>ijk</sub>_ contribute _n_+1 each. Group the coordinates retained by all three tensors into **u**, and the coordinates retained by each pair into **a**,**b**,**c**. After ordering the modes accordingly,

\(\phi_{ijk}=(n+1)^{|\mathcal{R}_{ijk}|}\sum_{\mathbf{u},\mathbf{a},\mathbf{b},\mathbf{c}}\bar{X}_{\mathbf{u},\mathbf{a},\mathbf{b}}\bar{Y}_{\mathbf{u},\mathbf{b},\mathbf{c}}\bar{Z}_{\mathbf{u},\mathbf{a},\mathbf{c}}.\) (115)

For each matrix slice, use \(|\langle AB,C\rangle|\le\|A\|_F\|B\|_F\|C\|_F\). Bound one slice norm by its full tensor norm and apply Cauchy-Schwarz to the other two slice norms. The isometry of \(\mu\) then gives

\(|\phi_{ijk}|\le(n+1)^{|\mathcal{R}_{ijk}|}\|X^{(i)}\|_F\|Y^{(j)}\|_F\|Z^{(k)}\|_F.\) (116)

For \(0<\lambda\le 1\), apply the triangle inequality to (112) and bound each block norm by the norm of its stacked vector. Taking the supremum over unit vectors gives \(\|\mathcal{M}_\lambda-\mathcal{M}\|\le\beta(\lambda)\).

