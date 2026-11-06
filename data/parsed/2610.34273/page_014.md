\(S\otimes_C0_q=0_{p+q}\). Scalar multiplication descends in the same way, with scalar zero giving the formal zero tensor.

The relations \(\unknown\), \(\cong\), and ∼ descend to nonzero tensors: changing input and output representatives only composes their local maps with permutation matrices. Extend them by \(0_k\unknown T\) for every _T_, by \(T\unknown 0_k\) only for _T_=0_<sub>k</sub>_, and by \(0_k\cong 0_k\). Thus ∼ still means mutual restriction and is not the equivalence used to define tensors. In particular, adding zero coordinates can change a tensor, although it gives a mutually restricting tensor.

Entrywise addition and the action of a specified local matrix require chosen, aligned coordinates. For example, \((1,0)\equiv_\mathrm{perm}(0,1)\), but (1,0)+(1,0)=(2,0) and (1,0)+(0,1)=(1,1) are not coordinate-permutation equivalent over C. Throughout the paper, a formula for tensor entries, an entrywise sum, or a local substitution uses the displayed coordinate representatives. The labels in \(e_d^{(q)}\) refer to those coordinates. With this convention, coordinate calculations describe tensors without identifying them under arbitrary invertible local maps or under mutual restriction.

**Remark 2.8** (tensor construction and Kronecker product)**.** The operation \(\otimes_C\) concatenates the legs, whereas \(\otimes_K\) pairs corresponding legs and retains their number. For example, over C, the tensor \(e_0^{(2)}\otimes_Ce_0^{(2)}+e_1^{(2)}\otimes_Ce_1^{(2)}\) is a second-order tensor of rank 2, whereas

\(e_0^{(2)}\otimes_Ke_0^{(2)}+e_1^{(2)}\otimes_Ke_1^{(2)}=(1,0,0,1)\)

is a nonzero first-order tensor of rank 1. Tensor rank, defined in Definition 2.12, is invariant under invertible changes of coordinates within each fixed leg. It need not be invariant under regrouping the legs. Our notation records this distinction.

The separation construction uses a partial direct sum: two legs have separate coordinates for each block, while the other legs use the same coordinates. The following definition makes these shared coordinates part of the data.

**Definition 2.9** (partial direct sum in aligned coordinates)**.** Let \(k\ge 2\) and \(M\ge 1\) be integers, and let _e_=(_u,v_) with \(1\le u<v\le k\). For \(0\le h<M\), let _T<sub>h</sub>_ be a complex _k_-th order tensor in specified coordinates of positive ambient dimensions (_n_<sub>1_,h_</sub>_,...,n<sub>k,h</sub>_). Assume that _n<sub>d,h</sub>=n<sub>d</sub>_ for every \(d\notin\{u,v\}\) and every \(0\le h<M\), and identify these coordinates in the displayed order. Put<tbc>

\(\beta_h=\sum_{t=0}^{h-1}n_{u,t},\gamma_h=\sum_{t=0}^{h-1}n_{v,t}(0\le h\le M),\)

<tbc>where the sums are empty when _h_=0. Define \(m_u=\beta_M\), \(m_v=\gamma_M\), and _m<sub>d</sub>=n<sub>d</sub>_ for \(d\notin\{u,v\}\). For \(1\le d\le k\) and \(0\le h<M\), let<tbc>

\(\eta_{d,h}=\left\{\begin{array}{ c c }
\beta_h, & d=u, \\
\gamma_h, & d=v, \\
0, & d\notin\{u,v\}.
\end{array}\right.\)

<tbc>The _partial direct sum_ \(A=T_0\boxplus_e\cdots\boxplus_et_{M-1}\) is specified in ambient dimensions (_m_<sub>1</sub>_,...,m<sub>k</sub>_) by

\(A_{i_1+\eta_{1,h},\dots,i_k+\eta_{k,h}}=(T_h)_{i_1,\dots,i_k}\)

for every \(0\le h<M\) and every (_i_<sub>1</sub>_,...,i<sub>k</sub>_) with \(0\le i_d<n_{d,h}\) for \(1\le d\le k\). All entries not assigned by this formula are zero. The sectors assigned to different _h_ are disjoint: the _u_-th coordinate lies in \([\beta_h,\beta_{h+1})\) and the _v_-th coordinate lies in \([\gamma_h,\gamma_{h+1})\). In particular, entries<tbc>

