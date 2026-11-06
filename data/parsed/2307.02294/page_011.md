_Proof._ First consider _t_=3. _Q<sub>a,b</sub>_ contains only three 1s and either 2_k_-2 or 2_k_-3 all-zero rows. Those three 1s are equivalent to \((\bullet)\), \(\left(\bullet\right)\), or \(\left(\bullet\right)\). Suppose _A_ is _Q<sub>a,b</sub>_-free. Remove the first and last 1 in each row of _A_, then remove the first 2_k_-11s in each of _m_-2 columns, excluding the first and last, which are now all zero. If any 1 remains, then there must have been an occurrence of _Q<sub>a,b</sub>_ in _A_. The _t_=2 case is proved similarly.

**Lemma 3.3.** _If_ \(m\le 2^j\), \(\mathrm{Ex}(Q_{a,b},n,m)\le 2^{t-2}n+(2k-1)j^{\mathrm{max}\{0,t-3\}}(m-2)\)_, where t_=3_k_-(_a+b)._

_Proof._ The cases \(t\in\{2,3\}\) follow from Lemma 3.2, so we may assume _t\>_3. We consider a simplified version of (7) in which _B_=\[_m/_2\], i.e., _m_<sub>1</sub>=\[_m/_2\] and _m_<sub>2</sub>=\[_m/_2\]. There are only two slabs, all 1s are classified as _local_, _first_, or _last_, and we have<tbc>

\(\mathrm{Ex}(Q_{a,b},n,m)\le\sum_{i\in\{1,2\}}\mathrm{Ex}(Q_{a,b},n_i,m_i)+\mathrm{Ex}(Q_{a,b+1},n^*,m_1)+\mathrm{Ex}(Q_{a+1,b},n^*,m_2).\)

<tbc>Applying the inductive hypothesis to each term, this is at most

\(\le 2^{t-2}(n_1+n_2)+(2k-1)(j-1)^{t-3}\left(\lceil m/2\rceil-2+\lfloor m/2\rfloor-2\right)\)<br>
\(+2\cdot 2^{t-3}n^*+(2k-1)(j-1)^{t-4}\left(\lceil m/2\rceil-2+\lfloor m/2\rfloor-2\right)\)<br>
\(=2^{t-2}n+(2k-1)\left((j-1)^{t-3}+(j-1)^{t-4}\right)(m-4)\)<br>
\(\le 2^{t-2}n+(2k-1)j^{t-3}(m-2).\)

We use the following version of Ackermann’s function and its inverses.

\(a_{1,j}=2^j\text{for}j\ge 1,\)<br>
\(a_{i,1}=2\text{for}i\ge 2,\)<br>
\(a_{i,j}=w\cdot a_{i-1,w},\text{where}w=a_{i,j-1}.\text{for}i,j\ge 2,\)<br>
\(\alpha(n,m)=\mathrm{min}\{i:a_{i,j}\ge m,\text{where}j=\mathrm{max}\{3,\lceil n/m\rceil\}\}\)<br>
\(\alpha(n)=\alpha(n,n)\)

Observe that in the table of Ackermann values, the 1st column is constant (_a_<sub>_i,_1</sub>=2) and the second merely exponential (_a_<sub>_i,_2</sub>=2<sup>_i_+1</sup>) so we have to look to the third column to see Ackermann- type growth, which is why we set _j_ as _j_=max{3,\[_n/m_\]}.

**Lemma 3.4.** _Fix a constant c_=3_k. Suppose_ \(m\le(a_{i,j})^c\)_. Then_

\(\mathrm{Ex}(Q_{a,b},n,m)\le\mu_{i,t}(n+(cj)^{\mathrm{max}\{0,t-3\}}(2k-1)(m-2)),\)

_where t_=3_k_-(_a+b_) _and_ \(\mu_{i,t}=(2^{O(kt)}+O(i)^{t-2})2^i\).

_Proof._ The proof is by induction on _i,j_, and _t_. The cases \(t\in\{2,3\}\) were already handled, so assume \(t\ge 4\). Let _A_ be a _Q<sub>a,b</sub>_-free \(n\times m\) matrix, where \(m\le(a_{i,j})^c\). We apply Eqn. (7) with _B,G_ set as follows:

\(B=a_{i,j-1}^c,\)<br>
\(G=(c(j-1))^{\mathrm{max}\{0,t-5\}}(2k-1)(B-2).\)

