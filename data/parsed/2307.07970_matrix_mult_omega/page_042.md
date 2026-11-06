1. For every _t_ and every \((i',j',k')\in\mathbb{Z}_{\ge 0}^3\cap[0,i_t]\times[0,j_t]\times[0,k_t]\) with \(i'+j'+k'=2^{\ell-1},i'=0\) or \(j'=0\), there is \(\text{split}(\hat{K},S_{t,i^\prime,j^\prime,k^\prime})=\beta_{Z,t,i^\prime,j^\prime,k^\prime}\).<tbc>

2. For every _t_ and every index \(k'\in\{0,1,\dots,min\{2^{\ell-1},k_t\}\}\), \(\text{split}(\hat{K},S_{t,*,*,k^\prime})=\overline{\beta_{Z,t,*,*,k^\prime}}\).

**Claim 6.10.** _In_ T<sub>comp</sub>_, for every remaining level-1 block triple_ \(X_\hat{I}Y_\hat{j}Z_\hat{K}\) _and the level-_\((\ell-1)\) _block triple X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub> that contains it,_ \(Z_\hat{K}\) _is compatible with X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>._

The proof of this claim is the same as Claim 5.9.

## 6.4 Compatibility Zero-Out II: Unique Triple

In this step, we zero out all level-1 _Z_-block \(Z_\hat{K}\) that are compatible with more than one level-\((\ell-1)\) triples and they become holes. After this step, each remaining level-1 _Z_-block \(Z_\hat{K}\in Z_K\) is compatible with a unique level-\((\ell-1)\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ containing it.

## 6.5 Usefulness Zero-Out

Next, we further zero out some level-1 _Z_-blocks using the following definition of _usefulness_.

**Definition 6.11** (Usefulness)**.** For a level-1 block \(Z_\hat{K}\) and a level-\((\ell-1)\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ containing it, if for all \(t,i',j',k'\) we have \(\text{split}(\hat{K},S_{t,i^\prime,j^\prime,k^\prime})=\beta_{Z,t,i^\prime,j^\prime,k^\prime}\), then we say that \(Z_\hat{K}\) is _useful_ for _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_.

For each \(Z_\hat{K}\), it appears in a unique triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ by the previous zeroing out. Furthermore, if \(Z_\hat{K}\) is not useful for this triple, we zero out \(Z_\hat{K}\). We call the current tensor T<sub>useful</sub>.

Ideally, we want the subtensor of T<sub>useful</sub> over each triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ to be isomorphic to

\(\mathcal{T}^*=\otimes_{t\in[s^\prime]}\otimes_{i^\prime+j^\prime+k^\prime=2^{\ell-1}}T_{i^\prime,j^\prime,k^\prime}^{\otimes A_{t,1}\cdot(\alpha_t(i^\prime,j^\prime,k^\prime)+\alpha_t(i_t-i^\prime,j_t-j^\prime,k_t-k^\prime))\cdot n_t}[\beta_{X,t,i^\prime,j^\prime,k^\prime},\beta_{Y,t,i^\prime,j^\prime,k^\prime},\beta_{Z,t,i^\prime,j^\prime,k^\prime}].\)

However, there will be two types of holes. The first type of holes is caused by the fact that some level-1 subtensors are already missing in the input tensor because we enforced complete split distributions \(\beta_{X,t},\beta_{Y,t},\beta_{Z,t}\) on it; the second type of holes is caused by zeroing out \(Z_\hat{K}\) that are compatible with multiple level-\((\ell-1)\) triples. In the next section, we will analyze and fix these two types of holes.

## 6.6 Fixing Holes

First, we analyze the fraction of holes that are caused by the complete split distributions enforced in the input. To do so, we focus on a fixed triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ and the subtensor T<sup>∗</sup> we desire. Then we take a random level-1 block that is not zeroed out in T<sup>∗</sup>, and upper bound the probability that this level-1 block is zeroed out in the input level-\(\ell\varepsilon\)-interface tensor. By symmetry, it suffices to focus on _X_-blocks.

Fix any \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\), let us analyze the fraction of its occurrences in a random level-1 _X_-block in T<sup>∗</sup>. For every \(t\in[s']\), and for every \(i',j',k'\), we first focus on the level-\(\ell\) positions in the _t_-th term where (_i<sub>t</sub>,j<sub>t</sub>,k<sub>t</sub>_) is split into \((i',j',k')\) and \((i_t-i',j_t-j',k_t-k')\) (thus, there are \(A_{t,1}\cdot\alpha_t(i',j',k')\cdot n_t\) such positions). Among these positions, we want to analyze the number of positions that correspond to the level-1 chunk \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-1}})\). Therefore, the first half-chunk, which corresponds to \((i',j',k')\), should be \((\hat{i}_1,\dots,\hat{i}_{2^{\ell-2}})\), and the second half-chunk, which corresponds to \((i_t-i',j_t-j',k_t-k')\), should be \((\hat{i}_{2^{\ell-2}+1},\dots,\hat{i}_{2^{\ell-1}})\).

There are \(A_{t,1}\cdot(\alpha_t(i',j',k')+\alpha_t(i_t-i',j_t-j',k_t-k'))\cdot n_t\) level-\((\ell-1)\) positions corresponding to \((i',j',k')\), and among them, \(A_{t,1}\cdot\alpha_t(i',j',k')\cdot n_t\) are in odd positions. By definition of T<sup>∗</sup>, the fraction of<tbc>

