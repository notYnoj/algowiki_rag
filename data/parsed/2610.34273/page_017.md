(2) For all \(a,b,c\in\mathcal{S}\), \(a\unknown b\) implies \(a+c\unknown b+c\) and \(ac\unknown bc\).<tbc>

(3) For every \(a,b\in\mathcal{S}\) with \(b\neq 0_\mathcal{S}\), there exists a positive integer _r_ such that \(a\unknown r_\mathcal{S}b\).

<tbc>For complex tensors _S,T_ of a fixed order \(k\ge 2\), write \(S\lesssim T\) if there are positive integers _h<sub>N</sub>_, indexed by positive integers _N_, with log_h<sub>N</sub>=o(N_) such that

\(S^{\otimes_KN}\unknown T^{\otimes_KN}\otimes_K\mathsf{I}_k(h_N)\)

for every sufficiently large _N_. This is the _asymptotic restriction preorder_.

For S=Tens_<sub>k</sub>_(C), the element _r_<sub>S</sub> is I_<sub>k</sub>(r_), with I_<sub>k</sub>_(0)=0_<sub>k</sub>_; it is not entrywise scalar multiplication by _r_. Restriction is a Strassen preorder on this semiring for \(k\ge 2\). For the first property, a nontrivial flattening of I_<sub>k</sub>(r_) has matrix rank _r_, so a restriction \(\mathsf{I}_k(r)\unknown\mathsf{I}_k(s)\) requires \(r\le s\). Conversely, coordinate projection gives such a restriction whenever \(r\le s\). For the second property, a restriction with nonzero target is preserved under direct sum by block-diagonal local matrices and under Kronecker product by the corresponding Kronecker products of local matrices. If the target is zero, a direct sum can be restricted to its other summand by deleting the source summand, and a product restricts to zero. Thus the same property holds in every case. For the third property, if _a_ and _b_ are nonzero classes, then \(\mathsf{I}_k(1)\unknown b\) and \(a\unknown\mathsf{I}_k(\mathsf{R}(a))\). Taking R(_a_) direct-sum copies of the first restriction and composing gives \(a\unknown b^{\otimes_K\mathsf{R}(a)}\). If _a_ is the formal zero tensor, we may take _r_=1.

**Definition 2.15** (degeneration)**.** Let \(k\ge 2\) be an integer, and let _S,T_ be nonzero complex _k_-th order tensors. Fix coordinate representatives of dimensions (_m_<sub>1</sub>_,...,m<sub>k</sub>_) and (_n_<sub>1</sub>_,...,n<sub>k</sub>_), respectively. We write \(S\unknown T\), and say that _T degenerates to S_, if there are matrices \(L_d(\varepsilon)\in\mathbb{C}[\varepsilon]^{m_d\times n_d}\) for \(1\le d\le k\), integers _a,b_ with \(0\le a\le b\), and complex _k_-th order tensors _S<sub>j</sub>_, written in the same output coordinates for \(a+1\le j\le b\), such that

\(L(\varepsilon)\cdot T=\varepsilon^aS+\sum_{j=a+1}^b\varepsilon^jS_j.\)

The equality is coefficientwise in the fixed output coordinates; the _S<sub>j</sub>_ may be zero. Changing representatives only composes the local matrices with constant permutation matrices, so this relation is independent of the chosen representatives. Define \(0_k\unknown T\) for every tensor _T_, and let \(S\unknown 0_k\) hold only for _S_=0_<sub>k</sub>_. Equivalently, write \(T\rightsquigarrow S\), with the source on the left. An empty sum is allowed. Local matrices with Laurent-polynomial entries give the same notion: multiplying each matrix by a sufficiently large power of \(\varepsilon\) clears its negative exponents and increases all exponents in the identity by the same amount.

**Remark 2.16** (degenerations by weights)**.** Suppose that, after fixed local substitutions, every coordinate symbol _x_ has been assigned an integer weight _w(x_). Substitute \(x\mapsto\varepsilon^{w(x)}x\) independently on each leg. If every supported term has nonnegative total weight, the resulting coefficient table is a polynomial in \(\varepsilon\), and its constant coefficient consists exactly of the terms of total weight zero. This gives a degeneration to that coefficient tensor. Individual weights may be negative, since Laurent-polynomial local matrices are allowed. The constructions in Sections 3 and 4.2 use this form of degeneration.

**Lemma 2.17** (Bini’s interpolation argument \[Bin80\])**.** _For every integer_ \(k\ge 2\) _and all complex k-th order tensors S,T, if_ \(S\unknown T\)_, then_ \(S\lesssim T\).

_Proof._ If _S_=0_<sub>k</sub>_, the conclusion follows from \(0_k\unknown T^{\otimes_KN}\) for every positive integer _N_. We may therefore assume that _S_ and _T_ are nonzero. Fix the polynomial identity in Definition 2.15, and<tbc>

