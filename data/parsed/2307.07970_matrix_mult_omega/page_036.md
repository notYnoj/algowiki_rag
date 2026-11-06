Next, we assume that we already used Theorem 6.1 to handle terms with _i<sub>t</sub>_=0, _j<sub>t</sub>_=0 or _k<sub>t</sub>_=0, and assume without loss of generality that we are left with the first \(s'\) terms for some \(s'\le s\).

For a triple of level-\(\ell\) complete split distributions \((\beta_X,\beta_Y,\beta_Z)\) associated with the tensor power of the constituent tensor _T<sub>i<sub>t</sub>,j<sub>t</sub>,k<sub>t</sub></sub>_, we define a distribution \(\gamma_X\) on \(\{0,\dots,2^{\ell-1}\}^2\) as follows:

\(\gamma_X(l_X,r_X):=\sum_{(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2\ell-1}):\hat{i}_1+\cdots+\hat{i}_{2\ell-2}=l_X,\hat{i}_{2\ell-2+1}+\cdots+\hat{i}_{2\ell-1}=r_X}\beta_X(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2\ell-1}).\)

It describes how every level-\(\ell\) index _i<sub>t</sub>_ splits into two level-\((\ell-1)\) indices. We similarly define \(\gamma_Y\) and \(\gamma_Z\).

Let \(\alpha\) be a distribution on possible combinations of (_l<sub>X</sub>,l<sub>Y</sub>,l<sub>Z</sub>_) such that the marginals of \(\alpha\) are consistent with \(\gamma_X(l_X,i-l_X),\gamma_Y(l_Y,j-l_Y)\), \(\gamma_Z(l_Z,k-l_Z)\). Moreover, let \(\beta_{X,i^\prime,j^\prime,k^\prime}\), \(\beta_{Y,i^\prime,j^\prime,k^\prime}\), \(\beta_{Z,i^\prime,j^\prime,k^\prime}\) be level-\((\ell-1)\) complete split distributions. We then define the following quantities:

• _D_ is the set of distributions whose marginal distributions on the three dimensions are consistent with \(\gamma_X(l_X,i-l_X)\), \(\gamma_Y(l_Y,j-l_Y)\), \(\gamma_Z(l_Z,k-l_Z)\) respectively, and let the penalty term \(P_\alpha:=max_{\alpha^\prime\in D}H(\alpha')-H(\alpha)\ge 0\).<tbc>

• For every \(k'\), \(\alpha(+,+,k'):=\sum_{i^\prime>0,j^\prime>0}\alpha(i',j',k')\); for every \(j'\), \(\alpha(+,j',+):=\sum_{i^\prime>0,k^\prime>0}\alpha(i',j',k')\); and for every \(i'\), \(\alpha(i',+,+):=\sum_{j^\prime>0,k^\prime>0}\alpha(i',j',k')\).<tbc>

• For every \(k'\), \(\alpha(\text{\<},\text{\<},k'):=\sum_{i^\prime<i_t,j^\prime<j_t}\alpha(i',j',k')\); for every _j_, \(\alpha(\text{\<},j',\text{\<}):=\sum_{i^\prime<i_t,k^\prime<k_t}\alpha(i',j',k')\); and for every \(i'\), \(\alpha(i',\text{\<},\text{\<}):=\sum_{j^\prime<j_t,k^\prime<k_t}\alpha(i',j',k')\).<tbc>

• For every \(k'\), \(\overline{\beta_{Z,+,+,k^\prime}}:=\frac{1}{\alpha(+,+,k')}\sum_{i^\prime>0,j^\prime>0}\alpha(i',j',k')\cdot\beta_{Z,i^\prime,j^\prime,k^\prime}\), while \(\overline{\beta_{Y,+,j^\prime,+}}\) and \(\overline{\beta_{X,i^\prime,+,+}}\) are defined similarly.<tbc>

• \(\lambda_Z:=\sum_{i^\prime,j^\prime,k^\prime:i^\prime=0\text{or}j^\prime=0}\big(\alpha(i',j',k')+\alpha(i_t-i',j_t-j',k_t-k')\big)\cdot H(\beta_{Z,i^\prime,j^\prime,k^\prime})\)<br>
\(+\sum_{k^\prime}\big(\alpha(+,+,k')+\alpha(\text{\<},\text{\<},k_t-k')\big)\cdot H(\overline{\beta_{Z,+,+,k_t-k^\prime}})\), while \(\lambda_X\) and \(\lambda_Y\) are defined similarly.<tbc>

<tbc>In the following proposition, we will use the above definitions for different \(t\in[s']\) and \(r\in[3]\). We will use _t_ in the subscripts and (_r_) in the superscripts on variables to denote that they are computed using values of \(\alpha_t^{(r)},\beta_{X,t}^{(r)},\beta_{Y,t}^{(r)},\beta_{Z,t}^{(r)},\{\beta_{X,t,i^\prime,j^\prime,k^\prime}^{(r)}\}_{i^\prime,j^\prime,k^\prime},\{\beta_{Y,t,i^\prime,j^\prime,k^\prime}^{(r)}\}_{i^\prime,j^\prime,k^\prime},\{\beta_{Z,t,i^\prime,j^\prime,k^\prime}^{(r)}\}_{i^\prime,j^\prime,k^\prime}\).

**Proposition 6.2.** _An_ \(s'\)_-term level-_\(\ell\varepsilon\)_-interface tensor with parameters_<tbc>

\(\{(n_t,i_t,j_t,k_t,\beta_{X,t},\beta_{Y,t},\beta_{Z,t})\}_{t\in[s^\prime]}\)

<tbc>_for_ \(\varepsilon>0,i_t,j_t,k_t>0\forall t\in[s']\) _can be degenerated into_<tbc>

\(2^{(E_1+E_2+E_3)-o(n)-o_{1/\varepsilon}(n)}\)

<tbc>_independent copies of a level-_\((\ell-1)\) _interface tensor with parameter list_

\(\big\{\big(n_t\cdot A_{t,r}\cdot\big(\alpha_t^{(r)}(i',j',k')+\alpha_t^{(r)}(i_t-i',j_t-j',k_t-k')\big),i',j',k',\beta_{X,t,i^\prime,j^\prime,k^\prime}^{(r)},\beta_{Y,t,i^\prime,j^\prime,k^\prime}^{(r)},\beta_{Z,t,i^\prime,j^\prime,k^\prime}^{(r)}\big)\big\}\)

_for_ \(t\in[s']\), \(r\in[3]\), \(i'+j'+k'=2^{\ell-1}\), \(0\le i'\le i_t\), \(0\le j'\le j_t\), \(0\le k'\le k_t\)_, where_

