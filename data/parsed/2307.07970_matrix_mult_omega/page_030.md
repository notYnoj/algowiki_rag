## 5.4 Compatibility Zero-Out II: Unique Triple

In this step, we zero out level-1 _Z_-blocks that are compatible with more than one level-\(\ell\) triples. To do so, we check if each level-1 _Z_-block \(Z_\hat{K}\) is compatible with multiple level-\(\ell\) triples. If so, we zero it out and it becomes a "hole". Note that after this step, each remaining level-1 _Z_-block \(Z_\hat{K}\in Z_K\) is compatible with a unique level-\(\ell\) triple (_X<sub>I</sub>,Y<sub>J</sub>,Z<sub>K</sub>_) containing it.

## 5.5 Usefulness Zero-Out

Next, we further zero out some level-1 _Z_-blocks using the following definition of _usefulness_.

**Definition 5.10** (Usefulness)**.** For a level-1 block \(Z_\hat{K}\) and a level-\(\ell\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ containing it, if for all (_i,j,k_) we have \(\text{split}(\hat{K},S_{i,j,k})=\beta_{Z,i,j,k}\), then we say that \(Z_\hat{K}\) is _useful_ for _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_.

For each \(Z_\hat{K}\), it appears in a unique triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ by the previous zeroing out. Furthermore, if \(Z_\hat{K}\) is not useful for this triple, we zero out \(Z_\hat{K}\). We call the current tensor T<sub>useful</sub>.

If there is no hole, then the subtensor of the remaining tensor over _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is isomorphic to<tbc>

\(\mathcal{T}^*=\otimes_{i+j+k=2^\ell} T_{i,j,k}^{\otimes A_1\cdot\alpha(i,j,k)\cdot n}[\beta_{X,i,j,k},\beta_{Y,i,j,k},\beta_{Z,i,j,k}],\)

<tbc>i.e., it is the level-\(\ell\) interface tensor with parameter list

\(\{(A_1\cdot\alpha(i,j,k)\cdot n,i,j,k,\beta_{X,i,j,k},\beta_{Y,i,j,k},\beta_{Z,i,j,k})\}_{i+j+k=2^\ell}.\)

More formally:

**Claim 5.11.** _For any level-_\(\ell\) _block triple X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub> contained in_ T<sub>comp</sub> _(or equivalently,_ T<sub>hash</sub>_), the subtensor of_ T<sub>useful</sub> _restricted to blocks X<sub>I</sub>,Y<sub>J</sub>,Z<sub>K</sub> is a subtensor of_ T<sup>∗</sup>_, where the missing variables in this subtensor are exactly those in level-1 blocks_ \(Z_\hat{K}\) _that are compatible with multiple level-_\(\ell\) _triples in_ T<sub>comp</sub>.

_Proof._ Initially,

\(\mathcal{T}_\text{hash}|_{X_IY_JZ_K}\equiv\otimes_{i+j+k=2^\ell} T_{i,j,k}^{\otimes A_1\cdot\alpha(i,j,k)\cdot n}.\)

To show T<sub>useful</sub>|_<sub>X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub></sub>_ is a subtensor of T<sup>∗</sup>, it suffices to show that the level-1 _X_-blocks (_Y_ -blocks or _Z_- blocks resp.) remaining in T<sub>useful</sub>|_<sub>X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub></sub>_ have the property that \(\text{split}(\hat{I},S_{i,j,k})=\beta_{X,i,j,k}\) (\(\text{split}(\hat{J},S_{i,j,k})=\beta_{Y,i,j,k}\) or \(\text{split}(\hat{K},S_{i,j,k})=\beta_{Z,i,j,k}\) resp.) for every _i,j,k_. This is true because we enforced these constraints on _X_- and _Y_ -blocks in the compatibility zeroing-out step, and enforced the constraints on _Z_-blocks by zeroing out \(Z_\hat{K}\) that is not useful for the unique level-\(\ell\) triple that contains it. Furthermore, these are the only constraints we have on the level-1 _X_- and _Y_ -blocks, so the set of _X_- and _Y_ -variables in T<sub>useful</sub>|_<sub>X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub></sub>_ is the same as that in T<sup>∗</sup>. It remains to analyze which level-1 _Z_-blocks are missing in T<sub>useful</sub>|_<sub>X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub></sub>_.

There are three constraints we enforced on level-1 _Z_-blocks:

1. In the compatibility zeroing-out, we enforced that for every index \(k\in\{0,1,\dots,2^\ell\}\), \(\text{split}(\hat{K},S_{*,*,k})=\overline{\beta_{Z,*,*,k}}\).<tbc>

2. In the unique triple zeroing-out, we zeroed out \(Z_\hat{K}\) that is compatible with multiple level-\(\ell\) triples.<tbc>

