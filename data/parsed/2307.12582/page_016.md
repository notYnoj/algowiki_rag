(i) _at least c<sub>A</sub>w_<sup>2/5</sup>log<sup>2</sup>_w distinct integers in A have multiplicity of at least w_<sup>1/5</sup>,<tbc>

(ii) \(\Sigma_B\unknown c_Bw^{8/5}\),

_where c<sub>A</sub> and c<sub>B</sub> are two sufficiently large constants. Then there must exist a non-empty subset_ \(A'\) _of A and a non-empty subset_ \(B'\) _of B such that_ \(\Sigma_{A^\prime}=\Sigma_{B^\prime}\).

_Proof._ Let _S_ a maximal subset of _A_ such that each integer has multiplicity _w_<sup>1/5</sup> in _S_. Note that \(|\mathsf{supp}_S|\unknown c_Aw^{2/5}log^2w\). What we actually prove is that there is a non-empty subset \(S'\) of _S_ such that some subset \(B'\) of _B_ have the same total weight as _S_. We characterize the set of integers that can be hit by _S_. Then we show that _B_ can hit at least one of these integers.

Since the items in _S_ has the same multiplicity, we obtain the following two equalities that will be frequently used in the proof.

\(\mu_S\Sigma_{\mathsf{supp}_S}=\Sigma_S,\)<br>
\(\mu_S|\mathsf{supp}_S|=|S|.\)

Note that \(\mathfrak{m}_S\unknown w\), \(\mu_S=w^{1/5}\), \(|\mathsf{supp}_S|=|\mathsf{supp}_A|\unknown c_Aw^{2/5}log^2w\). Since _c<sub>A</sub>_ is sufficiently large, we have that<tbc>

\(|S|^2=\mu_S^2|\mathsf{supp}_S|^2\unknown\mu_S^2\cdot c_A^2w^{4/5}log^4w\unknown c_A^2log^4w\cdot\mathfrak{m}_S\mu_S.\)

<tbc>The last inequality is due to \(\mu_A\unknown w^{1/5}\). Since \(|\mathsf{supp}_A|\unknown w\) and \(\mu_A\unknown w\),

\(c_\delta=\Theta\left(log(2|S|)log^2(2\mu_S)\right)\)<br>
\(=\Theta\left(log(\mu_S|\mathsf{supp}_S|)log^2(\mu_S)\right)\)<br>
\(=\Theta\left(log(w^2)log^2(w)\right)\)<br>
\(=\Theta(log^3w).\)

When _c<sub>A</sub>_ is sufficiently large, \(c_S^2log^4w\unknown c_\delta\), so _S_ is \(c_\delta\)-dense.

By Theorem 2.2, there exists an integer _d_ such that \(S':=S(d)/d\) is \(c_\delta\)-dense and has no \(c_\alpha\)-almost divisor. And the followings hold.

(i) \(d\unknown 4\mu_S\Sigma_S/|S|^2\).<tbc>

(ii) \(|S'|\unknown 0.75|S|\).<tbc>

(iii) \(\Sigma_{S^\prime}\unknown 0.75\Sigma_S/d\).<tbc>

<tbc>Note that \(\mu_{S^\prime}\unknown\mu_S\), \(\mathfrak{m}_{S^\prime}\unknown w/d\), and \(\Sigma_{S^\prime}\unknown\Sigma_S/d\). Applying Theorem 2.1 on \(S'\), we get \(S'\) can hit any integer in \([\lambda_{S^\prime},\Sigma_{S^\prime}-\lambda_{S^\prime}]\) where

\(\lambda_{S^\prime}=\frac{c_\lambda\mu_{S^\prime}\mathfrak{m}_{S^\prime}\Sigma_{S^\prime}}{|S'|^2}\unknown\frac{c_\lambda\mu_Sw\Sigma_S}{(0.75|S|)^2d^2}\unknown\frac{min\{c_A,c_B\}}{2}\cdot\frac{w}{d^2}\cdot\frac{\mu_S\Sigma_S}{|S|^2}.\)

The last inequality holds since _c<sub>A</sub>_ and _c<sub>B</sub>_ are sufficiently large constants. We can conclude that _S_ can hit any multiple of _d_ in \([d\lambda_{S^\prime},d(\Sigma_{S^\prime}-\lambda_{S^\prime})]\). We also have that the left endpoint of this interval

\(d\lambda_{S^\prime}\unknown\frac{c_B}{2}\cdot\frac{w}{d}\cdot\frac{\mu_S\Sigma_S}{|S|^2}=\frac{c_B}{2}\cdot\frac{w}{d}\cdot\frac{\Sigma_{\mathsf{supp}_S}}{|\mathsf{supp}_S|^2}\unknown\frac{c_B}{2}\cdot\frac{w^2}{|\mathsf{supp}_S|}\unknown\frac{c_B}{2}\cdot w^{8/5},\)

