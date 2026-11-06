Observe that

\(m/B\le(a_{i,j}/a_{i,j-1})^c=(a_{i-1,a_{i,j-1}})^c.\)

We apply the induction hypothesis at (_i,j_-1_,t_) to local 1s at (_i,j,t_-1) to first/last 1s, at (_i,j_-1_,t_-2) to heavy middle 1s, and at (_i_-1_,a_<sub>_i,j_-1</sub>_,t_) to light-first/light-last 1s. Plugging these bounds into Eqn. (7) and applying Theorem 2.1 yields the following upper bound.

\(\mathrm{Ex}(Q_{a,b},n,m)\)<br>
\(\le\mu_{i,t}(n-n^*)+\mu_{i,t}(c(j-1))^{t-3}(2k-1)(m-2m/B)\text{local}\)<br>
\(+2\mu_{i,t-1}n^*+2\mu_{i,t-1}(cj)^{t-4}(2k-1)(m-2)\text{first/last}\)<br>
\(+C_k(n^*/G+m/B)\left(\mu_{i,t-2}G+\mu_{i,t-2}(c(j-1))^{\mathrm{max}\{0,t-5\}}(2k-1)(B-2)\right)\text{heavy}\)<br>
\(+2\mu_{i-1,t}n^*+2\mu_{i-1,t}(c(a_{i,j-1}))^{t-3}(2k-1)(m/B-2)\text{light-first/last}\)<br>
\(+C'_k(Bn^*/G+m)\text{light-middle}\)

Note that by choice of _G_, the line for heavy 1s is exactly \(2C_k\mu_{i,t-2}(n^*+Gm/B)\). Continuing,

\(\le\mu_{i,t}(n+(cj)^{t-3}(2k-1)(m-2))\) (8)

\(+\left[-\mu_{i,t}+2\mu_{i,t-1}+2C_k\mu_{i,t-2}+2\mu_{i-1,t}+C'_k\right]n^*\) (9)

\(+\left[-\mu_{i,t}c(cj)^{t-4}+2\mu_{i,t-1}(cj)^{t-4}+2C_k\mu_{i,t-2}(c(j-1))^{\mathrm{max}\{0,t-5\}}\right.\) (10)

\(+2\mu_{i-1,t}c^{t-3}a_{i,j-1}^{(t-3)-c}+C'_k\right](2k-1)(m-2)\)<br>
\(\le\mu_{i,t}(n+(cj)^{t-3}(2k-1)(m-2)).\) (11)

Lines (8-10) follow from the fact that \((c(j-1))^{t-3}\le(cj)^{t-3}-c(cj)^{t-4}\). Line (11) completes the induction so long as the bracketed terms in Lines (9,10) are non-positive. These will hold whenever Eqns. (12,13) hold.

\(\mu_{i,t}\ge 2\mu_{i,t-1}+2C_k\mu_{i,t-2}+2\mu_{i-1,t}+C'_k,\) (12)

\(\mu_{i,t}\ge\frac{2\mu_{i,t-1}}{c}+\frac{2C_k\mu_{i,t-2}}{c}+\frac{2\mu_{i-1,t}}{2^{3k-1}}+\frac{C'_k}{2^{t-4}c^{t-3}}.\) (13)

Eqn. (13) was obtained by dividing through by _c(cj_)<sup>_t_-4</sup> and noting that \(j\ge 2\) and \(a_{i,j-1}\ge 2\). Clearly any values \((\mu_{i,t})_{i\ge 1,t\ge 0}\) that satisfy Eqn. (12) also satisfy (13) so we may focus solely on the former. We argue that the lemma is satisfied for \(\mu_{i,t}\) defined as follows. Let \(C=C'_k\ge C_k\).

\(\mu_{i,t}=(2C+3i)^{t-2}(2^i-1).\) (14)

When \(t\in\{2,3\}\) the claim follows from Lemma 3.2 since \(\mu_{i,3}\ge 2\) and \(\mu_{i,2}\ge 1\). When _i_=1 and \(t\ge 4\), \(m\le(a_{1,j})^c=a_{1,cj}=2^{cj}\) and the claim follows from Lemma 3.3 since \(\mu_{i,t}\ge 2^{t-2}\). Now<tbc>

