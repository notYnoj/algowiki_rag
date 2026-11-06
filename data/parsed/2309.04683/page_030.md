for all \(x_1,\dots,x_k\in\{0,1\}^{b\cdot\ell}\).

**Recursive Construction for larger** _b_**:** When \(b\ge\ell\), we let _b_<sub>micro</sub> be such that

\(\ell^{(3k)^{\mathrm{log}^*b_\mathrm{micro}\cdot b_\mathrm{micro}}}=b\)

and pick _b/b_<sub>micro</sub> primes _q_<sub>1</sub>_,...,q<sub>b/b<sub>micro</sub>_ in \([b^k\ell,b^{2k}\ell^2]\). We use induction and assume that the theorem is true for all integers smaller than _b_, and use _q_<sub>1</sub>_,...,q<sub>b/b<sub>micro</sub>_ for our CRR encoding. Given a vector \(x\in\{0,1\}^{b\cdot\ell}\), we again use _x<sup>i</sup>_ to denote the _i_-th block. We further partition _x<sup>i</sup>_ into blocks of size _b_<sub>micro</sub>, and use _x<sup>i,j</sup>_ to denote the _j_-th block of _x<sup>i</sup>_. We use _x_<sup>\[_j_\]</sup> to denote the concatenation of the _j_-th micro group in each of the \(\ell\) groups. Since _b_<sub>micro</sub>_\<b_, we can use induction hypothesis to construct \(\psi_{b_\mathrm{micro},\ell}:\{0,1\}^{b_\mathrm{micro}\cdot\ell}\rightarrow\mathbb{Z}^\ell\) such that for every \(x,y,z\in\{0,1\}^{b_\mathrm{micro}\cdot\ell}\),<tbc>

\(\langle x_1,\dots,x_k\rangle=0\Longleftrightarrow\left\langle\psi_{b_\mathrm{micro},\ell}(x_1),\dots,\psi_{b_\mathrm{micro},\ell}(x_1)\right\rangle\in V_{b_\mathrm{micro},\ell}.\)

<tbc>We first define an encoding \(S:\{0,1\}^{b\cdot\ell}\rightarrow\mathbb{Z}^{b/b_\mathrm{micro}\cdot\ell}\):<tbc>

\(S(x):=\big(\psi_{b_\mathrm{micro},\ell}(x^{[1]})_1,\psi_{b_\mathrm{micro},\ell}(x^{[2]})_1,\dots,\psi_{b_\mathrm{micro},\ell}(x^{[b/b_\mathrm{micro}]})_1,\psi_{b_\mathrm{micro},\ell}(x^{[1]})_2,\psi_{b_\mathrm{micro},\ell}(x^{[2]})_2,\dots,\psi_{b_\mathrm{micro},\ell}(x^{[b/b_\mathrm{micro}]})_2,\dots,\dots,\dots,\dots,\psi_{b_\mathrm{micro},\ell}(x^{[1]})_\ell,\psi_{b_\mathrm{micro},\ell}(x^{[2]})_\ell,\dots,\psi_{b_\mathrm{micro},\ell}(x^{[b/b_\mathrm{micro}]})_\ell\big).\)

<tbc>We partition _S(x_) into \(\ell\) blocks shown above and denote them as \(S^1(x),\dots,S^\ell(x)\). We then define<tbc>

\(\psi_{b,\ell}(x):=\big(\mathsf{CRR}(S^1(x);\{q_j\}),\mathsf{CRR}(S^2(x);\{q_j\}),\dots,\mathsf{CRR}(S^\ell(x);\{q_j\})\big).\)

<tbc>Now we show that this encoding satisfies the conditions in the theorem statement. For any \(x,y,z\in\{0,1\}^{b\cdot\ell}\), we know

\(\langle x_1,\dots,x_k\rangle=0\Longleftrightarrow\left\langle x_1^{[j]},\dots,x_k^{[j]}\right\rangle=0\forall j\in[b/b_\mathrm{micro}]\Longleftrightarrow\left\langle\psi_{b_\mathrm{micro},\ell}(x_1^{[j]}),\dots,\psi_{b_\mathrm{micro},\ell}(x_k^{[j]})\right\rangle\in V_{b_\mathrm{micro}}\forall j\in[b/b_\mathrm{micro}],\text{(3)}\)

where the second equivalence comes from our inductive hypothesis on \(\psi_{b_\mathrm{micro},\ell}\). By construction of _b_<sub>micro</sub>, we have \(\psi_{b_\mathrm{micro}}(x_i^{[j]})_i<b\) for all _i_, and thus<tbc>

\(\left\langle\psi_{b_\mathrm{micro},\ell}(x_1^{[j]}),\dots,\psi_{b_\mathrm{micro},\ell}(x_k^{[j]})\right\rangle<b^k\cdot\ell,\)

<tbc>which implies \(V_\mathrm{micro}\subseteq[0,b^k\ell)\).

Now for any \(1\le k\le b/b_\mathrm{micro}\),

\(\left\langle\psi_{b,\ell}(x_1),\dots,\psi_{b,\ell}(x_k)\right\rangle\equiv\sum_{i=1}^\ell\left\langle\mathsf{CRR}(S^i(x_1);\{q_j\}),\dots,\mathsf{CRR}(S^i(x_k)\right\rangle\mathrm{mod}q_t\equiv\sum_{i=1}^\ell\prod_{d=1}^kS^i(x_d)_t\mathrm{mod}q_t\equiv\sum_{i=1}^\ell\prod_{i=1}^k\psi_{b_\mathrm{micro}}(x_d^{[t]})_i\mathrm{mod}q_t\equiv\left\langle\psi_{b_\mathrm{micro}}(x_1^{[t]}),\dots,\psi_{b_\mathrm{micro}}(x_k^{[t]})\right\rangle\mathrm{mod}q_t.\)

