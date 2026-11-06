\((\hat{i}_1,\dots,\hat{i}_{2^{\ell-2}})\) in these \(A_{t,1}\cdot(\alpha_t(i',j',k')+\alpha_t(i_t-i',j_t-j',k_t-k'))\cdot n_t\) positions is \(\beta_{X,t,i^\prime,j^\prime,k^\prime}(\hat{i}_1,\dots,\hat{i}_{2^{\ell-2}})\), and if we take a random level-1 _X_-block in T<sup>∗</sup>, the fraction of \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-2}})\) among the odd positions corre sponding to \((i',j',k')\) is \(\beta_{X,t,i^\prime,j^\prime,k^\prime}(\hat{i}_1,\dots,\hat{i}_{2^{\ell-2}})\pm o(1)\) with 1-1/poly(_n_) probability, by concentration bounds. Furthermore, the subset of positions in these \(A_{t,1}\cdot\alpha_t(i',j',k')\cdot n_t\) positions is also random. Simi larly, with 1-1/poly(_n_) probability, the fraction of \((\hat{i}_{2^{\ell-2}+1},\dots,\hat{i}_{2^{\ell-1}})\) in the even positions corresponding to \((i_t-i',j_t-j',k_t-k')\) is \(\beta_{X,t,i^\prime,j^\prime,k^\prime}(\hat{i}_{2^{\ell-2}+1},\dots,\hat{i}_{2^{\ell-1}})\pm o(1)\), and the positions are also random. Apply ing concentration bounds again, we get that the fraction of level-\(\ell\) positions corresponding to \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\) among positions that split into \((i',j',k')\) and \((i_t-i',j_t-j',k_t-k')\) is<tbc>

\(\beta_{X,t,i^\prime,j^\prime,k^\prime}(\hat{i}_1,\dots,\hat{i}_{2^{\ell-2}})\cdot\beta_{X,t,i_t-i^\prime,j_t-j^\prime,k_t-k^\prime}(\hat{i}_{2^{\ell-2}+1},\dots,\hat{i}_{2^{\ell-1}})\pm o(1).\)

<tbc>Summing over all \(i',j',k'\), we get that with probability 1-1/poly(_n_), the fraction of level-\(\ell\) positions with \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\) is

\(\sum_{i^\prime,j^\prime,k^\prime}\alpha_t(i',j',k')\cdot\beta_{X,t,i^\prime,j^\prime,k^\prime}(\hat{i}_1,\dots,\hat{i}_{2^{\ell-2}})\cdot\beta_{X,t,i_t-i^\prime,j_t-j^\prime,k_t-k^\prime}(\hat{i}_{2^{\ell-2}+1},\dots,\hat{i}_{2^{\ell-1}})\pm o(1)\)<br>
\(=\beta_{X,t}(\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\pm o(1).\) (by Eq. (20))

The _o_(1) term can become less than \(\varepsilon\), and the 1-1/poly(_n_) probability can be bounded by 1-1_/n_<sup>2</sup> for sufficiently large _n_. Therefore, a random level-1 _X_-block appears in T with probability at least 1-1_/n_<sup>2</sup>. This means that the fraction of holes caused by the complete split distributions enforced in the input is 1-1_/n_<sup>2</sup> for the _X_-dimension. By symmetry, the same also holds for the _Y_ - and _Z_-dimensions.

Next, we focus on holes caused by zeroing out \(Z_\hat{K}\) that are compatible with multiple level-\((\ell-1)\) triples. The analysis will be similar to Section 5.6.

First, notice that for every level-1 _Z_-block \(Z_\hat{K}\) that appears in the input of the constituent stage, its complete split distribution \(\xi_{Z,t}\) in the _t_-th term must be within \(\varepsilon L_\infty\)-distance to the given parameter \(\beta_{Z,t}\). Then we define _p_<sub>comp</sub> as follows:

**Definition 6.12** (_p_<sub>comp</sub>)**.** For fixed \(Z_\hat{K}\) and _Z<sub>K</sub>_ where \(Z_\hat{K}\in Z_K\) and \(\hat{K}\) has level-\(\ell\) complete split distributions \(\{\xi_{Z,t}\}_{t\in[s^\prime]}\), we define \(p_\mathrm{comp}^*(\{\xi_{Z,t}\}_{t\in[s^\prime]})\) as the probability that a uniformly random block triple \(X_IY_JZ_K\) consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\) is compatible with \(Z_\hat{K}\). We further define \(p_\mathrm{comp}:=\mathrm{max}_{\{\xi_{Z,t}\}_{t\in[s^\prime]}:\left\|\xi_{Z,t}-\beta_{Z,t}\right\|_\infty\le\varepsilon\forall t}p_\mathrm{comp}^*(\{\xi_{Z,t}\}_{t\in[s^\prime]})\).

By symmetry between level-\(\ell\) positions, this probability \(p_\mathrm{comp}^*(\{\xi_{Z,t}\}_{t\in[s^\prime]})\) is the same for different \(\hat{K}\) that have the same complete split distributions, so \(p_\mathrm{comp}^*\) and _p_<sub>comp</sub> is well-defined.

**Claim 6.13.** _The value of_ \(p_\mathrm{comp}^*(\{\xi_{Z,t}\}_{t\in[s^\prime]})\) _is at most_<tbc>

\(2^{\sum_{t\in[s^\prime]}\big(\lambda_{Z,t}-H(\xi_{Z,t})+H(\gamma_{Z,t})\big)A_{t,1}\cdot n_t\pm o(n)},\)

<tbc>_where we recall that_

\(\lambda_{Z,t}=\sum_{i^\prime,j^\prime,k^\prime:i^\prime=0\text{or}j^\prime=0}\big(\alpha_t(i',j',k')+\alpha_t(i_t-i',j_t-j',k_t-k')\big)\cdot H(\beta_{Z,t,i^\prime,j^\prime,k^\prime})\)<br>
\(+\sum_{k^\prime}\big(\alpha_t(\mathsf{+},\mathsf{+},k')+\alpha_t(\mathsf{<},\mathsf{<},k_t-k')\big)\cdot H(\overline{\beta_{Z,\mathsf{+},\mathsf{+},k_t-k^\prime}}),\)

