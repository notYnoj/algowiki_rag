By assumption \(q_k\in[b^k\ell,b^{2k}\ell^3]\), so along with Equation (3), we know \(\langle x_1,\dots,x_k\rangle=0\) is equivalent to<tbc>

\(\big(\big\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\big\rangle\mathrm{mod}q_t\big)\in V_{b_\mathrm{micro}}\)

<tbc>for all \(1\le t\le b/b_\mathrm{micro}\). We finally upper bound \(\psi_{b,\ell}(x)_i\) by

\(\psi_{b,\ell}(x)_i<\prod_{j=1}^{b/b_\mathrm{micro}}q_j\)<br>
\(\le(b^{2k}\ell^2)^{b/b_\mathrm{micro}}\)<br>
\(\le 2^{(2k+2)b/b_\mathrm{micro}\cdot\mathrm{log}b}\)<br>
\(\le 2^{(2k+2)b/b_\mathrm{micro}\cdot(3k)^{\mathrm{log}^*b_\mathrm{micro}\cdot b_\mathrm{micro}\cdot\mathrm{log}\ell}}\)<br>
\(=\ell^{(2k+2)b\cdot(3k)^{\mathrm{log}^*b_\mathrm{micro}}}\)<br>
\(\le\ell^{(3k)^{\mathrm{log}^*b\cdot b}},\)

where the third inequality comes from \(b\ge\ell\) and the last inequality comes from<tbc>

\(\mathrm{log}^*b_\mathrm{micro}\le\mathrm{log}^*\mathrm{log}b=\mathrm{log}^*b-1.\)

<tbc>We set _V<sub>b</sub>_ to be the set of all integers _c_ in \([0,\ell^{(3k)^{\mathrm{log}^*b\cdot 2b+1}}]\) such that \(c\mathrm{mod}q_t\in V_{b_\mathrm{micro}}\) for all \(1\le t\le b/b_\mathrm{micro}\). By our previous analysis _V<sub>b</sub>_ will satisfy the statement in the theorem.

Constructing \(\psi_{b,\ell}(x)\) takes \(O(\mathrm{poly}(b\cdot\ell))\) time, and constructing _V<sub>b</sub>_ takes

\(O\big(\ell^O\big(^{(3k)^{\mathrm{log}^*b\cdot b}}\big)\cdot\mathrm{poly}(b\cdot\ell)\big)\)

time because we enumerate all possible values of \(\big\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\big\rangle\) and for each of them check whether they are in _V_<sub>_b_<sub>micro</sub></sub> after mod_q<sub>t</sub>_ in \(O(\mathrm{poly}(b\cdot\ell))\) time.

**Lemma A.4.** _Let_ \(1\le\ell\le d\)_. There is an_ \(O\big(n\cdot\ell^O\big(^{(3k)^{\mathrm{log}^*d\cdot d/\ell}}\big)\cdot\mathrm{poly}(d)\big)\) _time reduction from_ kOV_<sub>n,d</sub> to_ \(\ell^O\big(^{(3k)^{\mathrm{log}^*d\cdot d/\ell}}\big)\) _instances of_ Z-3OV\(_{n,\ell+1}\)_, with vectors of entries with bit-length_ \(O(d/\ell\cdot\mathrm{log}\ell\cdot(3k)^{\mathrm{log}^*d})\).

_Proof._ Given _k_ sets _X_<sub>1</sub>_,...,X<sub>k</sub>_ of _n_ vectors from {0,1}_<sup>d</sup>_, we apply \(\psi_{d/\ell,\ell}\) to each vector to obtain \(X'_i\subset\mathbb{Z}^\ell\) for all \(1\le i\le k\). By Theorem A.3,<tbc>

\(\exists(x_1,\dots,x_k)\in X_1\times\dots\times X_k\text{such that}\langle x_1,\dots,x_k\rangle=0\Longleftrightarrow\exists(x'_1,\dots,x'_k)\in X'_1\times\dots\times X'_k\text{such that}\langle x'_1,\dots,x'_k\rangle\in V_{d/\ell,\ell}.\)

<tbc>For each \(t\in V_{d/\ell,\ell}\), we construct sets \(X_1^t,\dots,X_k^t\) of vectors from \(\mathbb{Z}^{\ell+1}\) such that<br>
\(\exists(x'_1,\dots,x'_k)\in X'_1\times\dots\times X'_k\text{such that}\langle x'_1,\dots,x'_k\rangle=t\Longleftrightarrow\exists(x_1^t,\dots,x_k^t)\in X_1^t\times\dots\times X_k^t\text{such that}\langle x_1^t,\dots,x_k^t\rangle=0\).

Indeed, let

\(X_1^t=\{[x'_1,-t]:x'_1\in X'_1\}\)<br>
\(X_2^t=\{[x'_2,1]:x'_2\in X'_2\}\)<br>
\(\cdots\)<br>
\(X_k^t=\{[x'_k,1]:x'_k\in X'_k\}.\)

There are at most \(\ell^O\big(^{(3k)^{\mathrm{log}^*d\cdot d/\ell}}\big)\) numbers in \(V_{d/\ell,\ell}\), so we have at most \(\ell^O\big(^{(3k)^{\mathrm{log}^*d\cdot d/\ell}}\big)\) many Z-3OV\(_{n,\ell+1}\) instances. By Theorem A.3, the reduction takes \(O\big(n\cdot\ell^O\big(^{(3k)^{\mathrm{log}^*d\cdot d/\ell}}\big)\cdot\mathrm{poly}(d)\big)\) time. The bit-length of reduced vectors is bounded by

\(\mathrm{log}\ell^{(3k)^{\mathrm{log}^*d/\ell}\cdot d/\ell}=O(\mathrm{log}\ell\cdot d/\ell\cdot(3k)^{\mathrm{log}^*d}).\)

