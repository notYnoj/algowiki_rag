**Definition A.2** (CRR encoding)**.** _Let_ \(b,\ell\) _be two positive integers. For any vector_ \(z\in\mathbb{Z}^b\) _and a set of b primes q<sub>i</sub>, let_ CRR(_z_;{_q<sub>i</sub>_}) _denote the unique integer in_ \(\left[\prod q_i\right]\) _such that_ \(\mathsf{CRR}(\{z_i\};\{q_i\})\equiv z_imodq_i\) _for all_ \(1\le i\le b\)_. For a vector_ \(x\in\mathbb{Z}^{b\cdot\ell}\)_, partition x into_ \(\ell\) _blocks, each of length b and let x<sup>i</sup> be the i-th block. Define_<tbc>

\(\mathsf{CRR}_{b,\ell}(x,\{q_i\})=\big(\mathsf{CRR}(x^1,\{q_i\}),\mathsf{CRR}(x^2,\{q_i\}),\dots,\mathsf{CRR}(x^\ell,\{q_i\})\big).\)

<tbc>**Theorem A.3.** _Let_ \(b,\ell\) _be two sufficiently large integers. There is a reduction_ \(\psi_{b,\ell}:\{0,1\}^{b\cdot\ell}\rightarrow\mathbb{Z}^\ell\) _and a set_ \(V_{b,\ell}\subset\mathbb{Z}\) _such that for every_ \(x_1,\dots,x_k\in\{0,1\}^{b\cdot\ell}\),

\(\langle x_1,x_2,\dots,x_k\rangle=0\Longleftrightarrow\left\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\right\rangle\in V_{b,\ell}\)

_and_ \(0\le\psi_{b,\ell}(x)_i<\ell^{(3k)^{log^*b\cdot b}}\) _for all possible x and_ \(i\in[\ell]\)_. Moreover, the computation of_ \(\psi_{b,\ell}(x)\) _takes_ \(poly(b\cdot\ell)\) _time, and_ \(V_{b,\ell}\) _can be constructed in_ \(O\big(\ell^O\big(^{(3k)^{log^*b\cdot b}}\big)\cdot poly(b,\ell)\big)\) _time._

_Proof._ When _b_ is small (compared to \(\ell\)), we will define \(\psi_{b,\ell}\) directly; when _b_ is large, we will recursively define \(\psi_{b,\ell}\).

**Direct CRR for small** _b_**:** When \(b<\ell\), we pick _b_ primes _q_<sub>1</sub>_,...,q<sub>b</sub>_ in \([\ell+1,\ell^2]\), and we use them for our CRR encoding. Let<tbc>

\(\psi_{b,\ell}(x)=\mathsf{CRR}_{b,\ell}(x,\{q_i\})=\big(\mathsf{CRR}(x^1,\{q_i\}),\mathsf{CRR}(x^2,\{q_i\}),\dots,\mathsf{CRR}(x^\ell,\{q_i\})\big)\)

<tbc>with _q_<sub>1</sub>_,...,q<sub>b</sub>_ for any \(x\in\{0,1\}^{b\cdot\ell}\). Notice that for any \(x_1,\dots,x_k\in\{0,1\}^{b\cdot\ell},1\le t\le b\), we have

\(\left\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\right\rangle\equiv\left\langle\mathsf{CRR}_{b,\ell}(x_1,\{q_j\}),\dots,\mathsf{CRR}_{b,\ell}(x_k,\{q_j\})\right\rangle modq_t\)<br>
\(\equiv\sum_{d=1}^\ell\prod_{i=1}^k\mathsf{CRR}(x_i^d,\{q_j\})modq_t\)<br>
\(\equiv\sum_{d=1}^\ell\prod_{i=1}^kx_i^d[t]modq_t.\)

Since<tbc>

\(\sum_{d=1}^\ell\prod_{i=1}^kx_i^d[t]\le\ell\)

<tbc>and \(q_t>\ell\), we know<tbc>

\(\sum_{d=1}^\ell\prod_{i=1}^kx_i^d[t]=0\Longleftrightarrow\left\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\right\rangle\equiv 0modq_t.\)

<tbc>As a result, \(\langle x_1,\dots,x_k\rangle=0\) if and only if<tbc>

\(\left\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\right\rangle\equiv 0modq_t\)

<tbc>for all \(1\le t\le b\). Finally, \(\psi_{b,\ell}(x)_d=\mathsf{CRR}(x^d,\{q_j\})\le\ell^{2b}<\ell^{(3k)^{log^*b\cdot b}}\). In addition,<tbc>

\(\left\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\right\rangle\le\ell\cdot(\ell^{2b})^k\le\ell^{(3k)^{log^*b\cdot kb+1}}.\)

<tbc>Let \(V_{b,\ell}\) be the set of all integers in \([0,\ell^{(3k)^{log^*b\cdot kb+1}}]\) that are multiples of all _q<sub>j</sub>_’s, and we know<tbc>

\(\langle x_1,\dots,x_k\rangle=0\Longleftrightarrow\left\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\right\rangle\in V_{b,\ell}\)

