and that the length of the interval

\(d(\Sigma_{S^\prime}-2\lambda_{S^\prime})\ge\frac{3\Sigma_S}{4}-c_A\cdot\frac{w\mu_S\Sigma_S}{d|S|^2}\)<br>
\(=\frac{\mu_S\Sigma_S}{|S|^2}(\frac{3|S|^2}{4\mu_S}-c_A\cdot\frac{w}{d})\text{(since}|S|=\mu_S|\mathsf{supp}_S|\text{and}d\ge 1)\)<br>
\(\ge\frac{\mu_S\Sigma_S}{|S|^2}(\frac{3|\mathsf{supp}_S|^2\mu_S^2}{4\mu_S}-c_A\cdot w)\text{(since}|\mathsf{supp}_S|\ge c_Aw^{2/5}\mathrm{log}^2w\text{and}\mu_S=w^{1/5})\)<br>
\(\ge\frac{\mu_S\Sigma_S}{|S|^2}(\frac{3c_A^2w}{4}-c_Aw)\text{(since}c_A\text{is sufficiently large)}\)<br>
\(\ge 4\cdot\frac{\mu_S\Sigma_S}{|S|^2}\cdot w\text{(since}d\le 4\mu_S\Sigma_S/|S|^2)\)<br>
\(\ge dw.\)

To complete the proof, it suffices to show that there is a subset \(B'\) of _B_ whose sum is a multiple of _d_ and is within the interval \([d\lambda_{S^\prime},d(\Sigma_{S^\prime}-\lambda_{S^\prime})]\). We claim that as long as _B_ has at least _d_ numbers, there must be a non-empty subset of _B_ whose sum is at most _dw_ and is a multiple of _d_. Assume the claim is true. We can repeatedly extract such subsets from _B_ until _B_ has less than _d_ numbers. Note that the total sum of these subsets is at least

\(\Sigma_B-wd\ge c_Bw^{8/5}-w\cdot\frac{4\mu_S\Sigma_S}{|S|^2}\ge c_Bw^{8/5}-\frac{16w\Sigma_{\mathsf{supp}_S}}{|\mathsf{supp}_S|^2}\ge c_Bw^{8/5}-16w^{8/5}\ge\frac{c_B}{2}w^{8/5}.\)

That is, the total sum of these subset is at least the left endpoint of \([d\lambda_{S^\prime},d(\Sigma_{S^\prime}-\lambda_{S^\prime})]\). Also note that the sum of each subset is at most _dw_, which does not exceed the length of the interval. As a result, there must be a collection of subsets whose total sum is within the interval. Since the sum of each subset is a multiple of _d_, so is the any collection of these subset.

## C Proof of Lemma 5.2

Lemma 5.2. _There exits a partition of W_<sup>∗</sup> _into W_<sup>+</sup> _and <o>W</o>_<sup>+</sup>=_W_<sup>∗</sup>\\_W_<sup>+</sup> _such that_

(i) \(|W^+|\le 4c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\),<tbc>

(ii) \(\Delta(\overline{\mathcal{I}^{W^+}})\le 8c_Bw_\mathrm{max}^{9/5}\),

_where c<sub>A</sub> and c<sub>B</sub> are two large constants used in Lemma 3.2._

_Proof._ Recall that we label the items in decreasing order of efficiency. Without loss of generality, we assume that for any two items _i\<j\<b_, if _i_ and _j_ have the same efficiency, then \(w_i\le w_j\), and that for any two items _b\<i\<j_, if _i_ and _j_ have the same efficiency, then \(w_i\ge w_j\). For a set \(\mathcal{I}'\) of items, we say a weight _w_ is _frequent_ in \(\mathcal{I}'\) if \(\mathcal{I}'\) contains at least \(2w_\mathrm{max}^{1/5}\) items with weight _w_.

**Defining _W_**<sup>+</sup> **via Partition of I**<sup>_W_<sup>∗</sup></sup>**.** _W_<sup>+</sup> will be defined via a partition of I<sup>_W_<sup>∗</sup></sup>. We partition them into four subsets (I<sub>1</sub>,I<sub>2</sub>,I<sub>3</sub>,I<sub>4</sub>) as follows. For _i\<b_, let I<sub>\[_i,b_\]</sub> be the set of items {_i,...,b_-1} whose weight is in _W_<sup>∗</sup>. Let _i_<sup>∗</sup> be the minimum index _i_ such that exactly \(2c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights are frequent in I<sub>\[_i,b_\]</sub>. Let I<sub>2</sub>=I<sub>\[_i_<sup>∗</sup>_,b_\]</sub>, and let I<sub>1</sub>=I<sub>_\<i_<sup>∗</sup></sub>. When no such _i_<sup>∗</sup> exists, let I<sub>2</sub>=I<sub>_\<b_</sub>, and let \(\mathcal{I}_1=\emptyset\). I<sub>3</sub> and I<sub>4</sub> are defined similarly as follows. For any \(j\ge b\), define I<sub>\[_b,j_\]</sub> to be the set of items {_b,...,j_} whose weight is in _W_<sup>∗</sup>. Let _j_<sup>∗</sup> be the maximum index _j_ such that exactly \(2c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\) weights are frequent. Let I<sub>3</sub>=I<sub>\[_b,j_<sup>∗</sup>\]</sub>, and let I<sub>4</sub>=I<sub>_\>j_<sup>∗</sup></sub>. When no such _j_<sup>∗</sup> exists, let \(\mathcal{I}_3=\mathcal{I}_{\ge b}\), and let \(\mathcal{I}_4=\emptyset\).

_W_<sup>+</sup> is define to be the set of weights that are frequent in I<sub>2</sub> or I<sub>3</sub>, and <o>_W_<sup>+</sup></sub>=_W_<sup>∗</sup>\\_W_<sup>+</sup>.

**Verifying Properties.** It is straightforward that \(|W^+|\le 4c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\). It is left to show \(\Delta(\overline{\mathcal{I}^{W^+}})\le 8c_Bw_\mathrm{max}^{9/5}\). We first partition I<sup><o>_W_<sup>+</sup></sup></sup> into \(\mathcal{I}_k^{W^+}=\mathcal{I}^{\overline{W^+}}\cap\mathcal{I}_k\) for \(k\in\{1,2,3,4\}\). Next we show \(\Delta(\mathcal{I}_k^{\overline{W^+}})\le 2c_Bw_\mathrm{max}^{9/5}\) for \(k\in\{1,2\}\).

