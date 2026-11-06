<tbc>only share the same level-\(\ell Z\)-variable block while each _X_- and _Y_ -variable block needs to be contained in a unique level-\(\ell\) subtensor. (More generally, their technique works when level-\(\ell\) variable blocks are shared in exactly one of _X_-, _Y_ -, _Z_-variables). In order to set up the tensor satisfying the required constraints, they need to zero out the _Z_-variable blocks asymmetrically with respect to the _X_- and _Y_ -variables. It still remains an open question whether the techniques in \[DWZ23\] can be symmetrized over the three dimensions.

Another technical detail is that the obtained independent copies of tensors in \[DWZ23\] are not all necessarily full copies of \(\mathcal{T}'\). That is, some variables of the independent tensors are zeroed out. This creates independent copies of \(\mathcal{T}'\) but with some "holes". Because of the asymmetry of their method, such holes can only appear in _Z_-variables. In order to overcome this issue, they showed that, as long as the fraction of holes is small, and all holes are in _Z_-variables, one can degenerate a small number of independent copies of \(\mathcal{T}'\) with holes to a full copy of T . Prior to their work, Schönhage \[Sch81\] also studied this problem of degenerating multiple independent copies of a tensor with holes to a full copy of the tensor. Schönhage’s method applied to the case when two of the three dimensions can have holes, but it focuses only on matrix multiplication tensors.

(CW 4)) )
(CW 4)) )
(CW 4)) )
(CW 4)) )
Zero out level-3 blocks inconsistent with a
Zero out level-3 blocks inconsistent with a
Zero out level-3 blocks inconsistent with a
Hash level-3 blocks
Hash level-3 blocks
Global
Zero out level-2 blocks inconsistent with β
Zero out level-1 blocks inconsistent with γ
Level-3 independent copies of T
Level-2 independent copies of T
Level-1 independent copies of T
Zero out level-2 blocks inconsistent with β
Hash level-2 blocks
Hash level-2 blocks
Level-2
Level-2 independent copies of T'
Level-1 independent copies of T'
Level-1 independent copies of T'
Zero out level-1 blocks inconsistent with γ
Hash level-1 blocks
Level-1
Level-1 independent copies of T"
Level-1 independent copies of T"
Level-1 independent copies of T"

(a) \[Vas12, DS13, LG14, AV21\]

(b) \[DWZ23\]

(c) This work

Figure 1: High-level comparison between this work and prior works on \((\mathrm{CW}_q^{\otimes 4})^{\otimes n}\). Here, \(\alpha\) is a distribution over level-3 constituent tensors, \(\beta\) is a collection of distributions over level-2 constituent tensors, and \(\gamma\) is a collection of distributions over level-1 constituent tensors.

