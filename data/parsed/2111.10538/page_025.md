<tbc>by

\(\frac{\#\text{degenerate}3\text{-walks}}{\#3\text{-walks}}\approx_{(1\pm O(\epsilon^\prime))\text{-factor}}\frac{2l_xl_y\cdot|V_C|}{\lambda^3(l_xl_y)^{1.5}|V_C|}=\frac{2}{\lambda^3\sqrt{l_xl_y}}\le\frac{2}{4/\epsilon'}\text{(Def. of}X',Y')=\epsilon'/2.\)

Hence, the total number of 3-paths (3-walks that are not degenerate) is at least

\(\#3\text{-paths}\unknown_{(1\pm\epsilon^\prime)^{2.5\text{-factor}}}\lambda^3(l_xl_y)^{1.5}|V_C|.\)

On the other hand, the number of 4-tuples of windows that contribute to those 3-paths of characters is \(8\genfrac(){pt}{2}{l_x}{2}\genfrac(){pt}{2}{l_y}{2}\le 2l_x^2l_y^2\). Thus, there must exist a 4-tuple containing at least

\(\frac{\#3\text{-paths}}{\#4\text{-tuples}}\unknown_{(1\pm\epsilon^\prime)^{2.5\text{-factor}}}\frac{\lambda^3(l_xl_y)^{1.5}|V_C|}{2l_x^2l_y^2}=\frac{\lambda^3|V_C|}{\sqrt{l_xl_y}}\approx_{\sqrt{1\pm\epsilon^\prime}\text{-factor}}\frac{\lambda^3\sqrt{l_xd_xl_yd_y}}{\sqrt{l_xl_y}}=\lambda^3\sqrt{d_xd_y}\text{(Eq. (2))}\)

many 3-walks. This means that such a 4-tuple is \((\epsilon,\lambda)\)-constructive.

## 3.1.3 Guarantees of the sparsification algorithm

**Theorem 3.13** (Sparsification for constant \(\lambda\) (Step 1 of Theorem 2.2))**.** _Given k windows_ \(w_1,\cdots,w_k\)_. Let_ \(\mathsf{w}_\mathsf{max}=max_{i\in[k]}|w_i|\), \(\mathsf{w}_\mathsf{min}=min_{i\in[k]}|w_i|\) _and_ \(\mathsf{w}_\mathsf{gap}=\mathsf{w}_\mathsf{max}/\mathsf{w}_\mathsf{min}\)_. Let the number of different window sizes be_ \(\mathsf{w}_\mathsf{layers}\)_. For any constant_ \(\lambda\in(0,1)\) _and_ \(0<\epsilon<1\)_, there is a randomized algorithm (Algorithm 1) that runs in time_<tbc>

\(O(\mathsf{w}_\mathsf{max}^2k^{1.1}logk+\mathsf{w}_\mathsf{max}k^{2.2}log^2k),\)

<tbc>_outputs a table_ \(\widehat{\mathsf{O}}_{\lambda^2}\in\{0,1\}^{k\times k}\) _such that_<tbc>

\(||\mathsf{lcs}(w_i,w_j)||\ge(1-\epsilon)\lambda^3,\text{if}\widehat{\mathsf{O}}_{\lambda^2}[i][j]=1\)

<tbc>_and_

\(\left|\left\{(i,j)\right||||\mathsf{lcs}(w_i,w_j)||\ge\lambda,\text{and}\widehat{\mathsf{O}}_{\lambda^2}[i][j]=0\right\}\right|\le k^{2-\epsilon\lambda^3/(800\mathsf{w}_\mathsf{layers}\mathsf{w}_\mathsf{gap})}.\)

_The algorithm has success probability at least_ 1-1/poly(_k)._

