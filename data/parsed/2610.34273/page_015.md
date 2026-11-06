using different sectors on the two legs are zero. A zero block uses the zero coefficient table in its specified ambient dimensions. If every block is zero, _A_ is the formal zero tensor written in the stated output coordinates. For _M_=2, the notation is \(T_0\boxplus_eT_1\). Iterating this binary construction in the displayed order gives the same coordinates as the formula above.

This construction requires the aligned representatives, as in Remark 2.7; independent changes of coordinates on a shared leg of different blocks need not give the same tensor. Thus \(\boxplus_e\) is not an operation on tensor classes alone, and it is not one of the tensor semiring operations. In particular, a specified zero block retains its coordinate sector. Section 3 uses these partial sums to state the separation problem. The formal expressions in Definition 5.2 retain their specified representatives, so their partial sums use precisely this convention.

We also record two forms of notation used to describe local maps and to change the roles of the legs.

**Definition 2.10** (formal multilinear notation)**.** Let _k,n_<sub>1</sub>_,...,n<sub>k</sub>_ be positive integers, and let _T_ be a complex _k_-th order tensor in specified coordinates of dimensions (_n_<sub>1</sub>_,...,n<sub>k</sub>_). Introduce distinct commuting indeterminates \(x_i^{(d)}\) for \(1\le d\le k\) and \(0\le i<n_d\). The _formal multilinear expression_ of _T_ in these coordinates is<tbc>

\(\sum_{0\le i_d<n_d1\le d\le k}T_{i_1,\dots,i_k}\prod_{d=1}^kx_{i_d}^{(d)}.\)

<tbc>For positive integers _m_<sub>1</sub>_,...,m<sub>k</sub>_ and matrices \(L_d\in\mathbb{C}^{m_d\times n_d}\) for \(1\le d\le k\), the local map _L_=(_L_<sub>1</sub>_,...,L<sub>k</sub>_) is represented by the substitutions

\(x_i^{(d)}\longmapsto\sum_{j=0}^{m_d-1}(L_d)_{j,i}y_j^{(d)}(1\le d\le k,0\le i<n_d),\)

where the \(y_j^{(d)}\) are distinct commuting output indeterminates. Expanding gives the formal multilinear expression of \(L\cdot T\) from Definition 2.4.

A product of symbols records one basis tensor and keeps the _k_ legs separate. This notation lets us specify local maps by their action on coordinate symbols and read their effect on the supported terms. We use it for simultaneous separation in Theorem 3.1, the two polynomial constructions in Lemmas 4.8 and 4.9, and the local weights in the proof of Theorem B.4.

**Definition 2.11** (permutations of tensor legs)**.** For every positive integer _k_, let _S<sub>k</sub>_ be the set of permutations of {1_,...,k_}. For \(\pi\in S_k\) and a nonzero complex _k_-th order tensor _T_ of dimension (_n_<sub>1</sub>_,...,n<sub>k</sub>_), define \(\pi T\) by the dimensions \((n_{\pi^{-1}(1)},\dots,n_{\pi^{-1}(k)})\) and the coordinate formula

\((\pi T)_{j_1,\dots,j_k}=T_{j_{\pi(1)},\dots,j_{\pi(k)}}\)

for \(0\le j_d<n_{\pi^{-1}(d)}\) and \(1\le d\le k\), and set \(\pi 0_k=0_k\).

A change of representative for _T_ induces a change of representative for \(\pi T\), so this action is well-defined. Thus old leg _d_ becomes new leg \(\pi(d)\). This operation permutes the participants, whereas \(\equiv_\mathrm{perm}\) only permutes coordinates within each fixed leg.

## 2.2 Asymptotic rank and the spectrum

We now use local maps to define rank and subrank, and then describe their behavior under large Kronecker powers. Strassen’s spectral duality will provide the link between these tensor parameters and the numerical inequalities in our proof.

