3. In the unique triple zeroing-out, we zeroed out \(Z_\hat{K}\) that is not useful for the unique level-\(\ell\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ that contains it. Thus, we will have that \(\mathsf{split}(\hat{K},S_{i,j,k})=\beta_{Z,i,j,k}\) for every _i,j,k_ if \(Z_\hat{K}\) remains.<tbc>

<tbc>The third constraint implies the first constraint, because if the third constraint holds, then for every _k_,

\(\mathsf{split}(\hat{K},S_{*,*,k})=\frac{1}{\sum_{i,j}\alpha(i,j,k)}\sum_{i+j=2^\ell-k}\alpha(i,j,k)\cdot\mathsf{split}(\hat{K},S_{i,j,k})\)<br>
\(=\frac{1}{\sum_{i,j}\alpha(i,j,k)}\sum_{i+j=2^\ell-k}\alpha(i,j,k)\cdot\beta_{Z,i,j,k}=\overline{\beta_{Z,*,*,k}}.\)

Therefore, we can ignore the first condition. As a result, the set of level-1 _Z_-blocks not in \(\mathcal{T}_\mathsf{useful}|_{X_IY_JZ_K}\) but in T<sup>∗</sup> are exactly those that are compatible with multiple block triples in T<sub>comp</sub>.

Also, note that for different remaining block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_, \(\mathcal{T}_\mathsf{useful}|_{X_IY_JZ_K}\) are level-1-independent, i.e., they do not share the same level-1 blocks. This is because _X<sub>I</sub>_ and _Y<sub>J</sub>_ are already in unique level-\(\ell\) triples in T<sub>hash</sub>; for every level-1 block \(Z_\hat{K}\), Claim 5.9 shows that \(Z_\hat{K}\) is compatible with every level-\(\ell\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ containing it, and then we zeroed out \(Z_\hat{K}\) that are compatible with multiple triples. Thus, every remaining \(Z_\hat{K}\) in T<sub>useful</sub> is contained a unique level-\(\ell\) triple as well. As a result, we can write

\(\mathcal{T}_\mathsf{useful}=\oplus_{X_IY_JZ_K\text{remaining}}\mathcal{T}_\mathsf{useful}|_{X_IY_JZ_K}\) (8)

as a direct sum of broken copies of T<sup>∗</sup>.

## 5.6 Fixing Holes

Next, we analyze the fraction of holes in the broken copies of T<sup>∗</sup> contained in T<sub>useful</sub>. To do so, we define the following notion of _typicalness_, which will then be used to define the quantity _p_<sub>comp</sub>:

**Definition 5.12** (Typicalness)**.** A level-1 _Z_-block \(Z_\hat{K}\) in some level-\(\ell Z\)-block _Z<sub>K</sub>_ is _typical_ if \(\mathsf{split}(\hat{K},S_{*,*,k})=\overline{\beta_{Z,*,*,k}}\) for every _k_. When _Z<sub>K</sub>_ is consistent with \(\alpha_Z\), this condition can be equivalently written as \(\mathsf{split}(\hat{K},[A_1n])=\overline{\beta_{Z,*,*,*}}\), where we recall that \(\overline{\beta_{Z,*,*,*}}=\sum_{i,j,k}\alpha(i,j,k)\cdot\beta_{Z,i,j,k}\).

**Definition 5.13** (_p_<sub>comp</sub>)**.** For fixed \(Z_\hat{K}\) and _Z<sub>K</sub>_ where \(Z_\hat{K}\in Z_K\) and \(Z_\hat{K}\) is typical, _p_<sub>comp</sub> is the probability that a uniformly random block triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ consistent with \(\alpha\) is compatible with \(\hat{K}\).

By symmetry, this probability is the same for different \(Z_\hat{K}\) and _Z<sub>K</sub>_ where \(Z_\hat{K}\in Z_K\) and \(Z_\hat{K}\) is typical, so _p_<sub>comp</sub> is well-defined. Since holes only arise when some \(Z_\hat{K}\) is compatible with multiple triples, the value of _p_<sub>comp</sub> is closely related to the fraction of holes, and is given by the following claim.

**Claim 5.14.** _The value of p_<sub>comp</sub> _is_<tbc>

\(2^{\left(\lambda_Z-H(\overline{\beta_{Z,*,*,*}})+H(\alpha_Z)\right)A_1\cdot n\pm o(n)},\)

<tbc>_where we recall that_<tbc>

\(\lambda_Z=\sum_{i,j,k:i=0\text{or}j=0}\alpha(i,j,k)\cdot H(\beta_{Z,i,j,k})+\sum_k\alpha(\mathsf{+},\mathsf{+},k)\cdot H(\overline{\beta_{Z,\mathsf{+},\mathsf{+},k}}),\)

