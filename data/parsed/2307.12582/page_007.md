Lemma 3.1. _Let w be a positive integer. Let p be an arbitrary real number such that_ \(0.5\le p<1\)_. Let A be a multiset of integers from_ {1_,...,w_} _such that_ \(|\mathsf{\textit{supp}}_A|\ge c_Aw^p\mathrm{log}w\)_, B be a multiset of integers from_ {1_,...,w_} _such that_ \(\Sigma_B\ge c_Bw^{2-p}\)_, where c<sub>A</sub> and c<sub>B</sub> are two sufficiently large constants. Then there must exist a non-empty subset_ \(A'\) _of A and a non-empty subset_ \(B'\) _of B such that_ \(\Sigma_{A^\prime}=\Sigma_{B^\prime}\).

_Proof._ Let _S_=supp_<sub>A</sub>_. Note that \(|S|\ge c_Aw^p\mathrm{log}w\). What we actually prove is that there is a non-empty subset \(S'\) of _S_ such that some subset \(B'\) of _B_ have the same total weight as \(S'\). We first characterize the set of integers that can be hit by _S_. Then we show that _B_ can hit at least one of these integers.

Note that \(\mathfrak{m}_S\le w\), \(\mu_S=1\), and \(|S|\le w\). Since _c<sub>A</sub>_ is sufficiently large, we have that

\(|S|^2\ge c_A^2w^{2p}\mathrm{log}^2w\ge c_A^2w\mathrm{log}w\ge c_A^2\mu_S\mathfrak{m}_S\mathrm{log}|S|\ge c_\delta\mu_S\mathfrak{m}_S.\)

By definition, _S_ is \(c_\delta\)-dense. By Theorem 2.2, there exists an integer _d_ such that \(S':=S(d)/d\) is \(c_\delta\)-dense and has no \(c_\alpha\)-almost divisor. And the followings hold.

(i) \(d\le 4\mu_S\Sigma_S/|S|^2\),<tbc>

(ii) \(|S'|\ge 0.75|S|\).<tbc>

(iii) \(\Sigma_{S^\prime}\ge 0.75\Sigma_S/d\).

<tbc>Note that \(\mu_{S^\prime}=1\), \(\mathfrak{m}_{S^\prime}\le w/d\), and \(\Sigma_{S^\prime}\le\Sigma_S/d\). Applying Theorem 2.1 on \(S'\), we get \(S'\) can hit any integer in the range \([\lambda_{S^\prime},\Sigma_{S^\prime}-\lambda_{S^\prime}]\) where<tbc>

\(\lambda_{S^\prime}=\frac{c_\lambda\mu_{S^\prime}\mathfrak{m}_{S^\prime}\Sigma_{S^\prime}}{|S'|^2}\le\frac{c_\lambda w\Sigma_S}{(0.75|S|)^2d^2}\le\frac{\mathrm{min}\{c_A,c_B\}}{2}\cdot\frac{w\Sigma_S}{d^2|S|^2}.\)

<tbc>The last inequality holds since _c<sub>A</sub>_ and _c<sub>B</sub>_ are sufficiently large constants. We can conclude that _S_ can hit any multiple of _d_ in the range \([d\lambda_{S^\prime},d(\Sigma_{S^\prime}-\lambda_{S^\prime})]\). We also have that the left endpoint of this interval<tbc>

\(d\lambda_{S^\prime}\le\frac{c_B}{2}\cdot\frac{w\Sigma_S}{d|S|^2}\le\frac{c_B}{2}\cdot\frac{w^2|S|}{|S|^2}\le\frac{c_B}{2}\cdot\frac{w^2}{|S|}\le\frac{c_B}{2}\cdot w^{2-p},\)

<tbc>and that the length of the interval

\(d(\Sigma_{S^\prime}-2\lambda_{S^\prime})\ge\frac{3\Sigma_S}{4}-c_A\cdot\frac{w\Sigma_S}{d|S|^2}\)<br>
\(\ge\frac{\Sigma_S}{|S|^2}(\frac{3|S|^2}{4}-c_A\cdot\frac{w}{d})\text{(since}|S|\ge c_Aw^{1/2}\mathrm{log}w\text{and}d\ge 1)\)<br>
\(\ge\frac{\Sigma_S}{|S|^2}(\frac{3c_A^2}{4}\cdot w-c_A\cdot w)\text{(since}c_A\text{is sufficiently large)}\)<br>
\(\ge 4\cdot\frac{\Sigma_S}{|S|^2}\cdot w\text{(since}d\le 4\mu_S\Sigma_S/|S|^2\text{and}\mu_S=1)\)<br>
\(\ge dw\)

To complete the proof, it suffices to show that there is a subset \(B'\) of _B_ whose sum is a multiple of _d_ and is within the interval \([d\lambda_{S^\prime},d(\Sigma_{S^\prime}-\lambda_{S^\prime})]\). We claim that as long as _B_ has at least _d_ numbers, there must be a non-empty subset of _B_ whose sum is at most _dw_ and is a multiple of _d_. Assume the claim is true. We can repeatedly extract such subsets from _B_ until _B_ has less than _d_ numbers. Note that the total sum of these subsets is at least

\(\Sigma_B-wd\ge c_Bw^{2-p}-w\cdot\frac{4\Sigma_S}{|S|^2}\ge c_Bw^{2-p}-\frac{4w^2}{|S|}\ge c_Bw^{2-p}-w^{2-p}\ge\frac{c_Bw^{2-p}}{2}.\)

That is, the total sum of these subsets is at least the left endpoint of \([d\lambda_{S^\prime},d(\Sigma_{S^\prime}-\lambda_{S^\prime})]\). Also note that the sum of each subset is at most _dw_, which does not exceed the length of the interval. As a result, there must be a collection of subsets whose total sum is within the interval. Since the sum of each subset is a multiple of _d_, so is any collection of these subsets.

