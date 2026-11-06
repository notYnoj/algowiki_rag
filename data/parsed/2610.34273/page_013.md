**Definition 2.5** (coordinate-permutation equivalence)**.** Let _k_ be a positive integer, and let \(A,B\in\mathsf{Arr}_k(\mathcal{R})\). Write \(A\equiv_\mathrm{perm}B\) if dim(_A_)=dim(_B_)=(_n_<sub>1</sub>_,...,n<sub>k</sub>_) and there are permutations \(\sigma_d:[n_d]_0\rightarrow[n_d]_0\), for \(1\le d\le k\), such that

\(B_{i_1,\dots,i_k}=A_{\sigma_1(i_1),\dots,\sigma_k(i_k)}\)

for \(0\le i_d<n_d\) and \(1\le d\le k\). The permutations act independently within the legs; they do not exchange the legs. Identity permutations, inverse permutations, and composition show that \(\equiv_\mathrm{perm}\) is an equivalence relation.

**Definition 2.6** (tensors and the tensor semiring)**.** Let _k_ be a positive integer. For this definition, assume that R has no zero divisors: for all \(x,y\in\mathcal{R}\), the equality _xy_=0<sub>R</sub> implies _x_=0<sub>R</sub> or _y_=0<sub>R</sub>. Let \(\mathsf{Arr}_k^\times(\mathcal{R})\) be the set of nonzero arrays in Arr_<sub>k</sub>_(R), and put<tbc>

\(\mathsf{Tens}_k(\mathcal{R})=\left(\mathsf{Arr}_k^\times(\mathcal{R})/\equiv_\mathrm{perm}\right)\sqcup\{0_k\},\)

<tbc>where 0_<sub>k</sub>_ is a new formal element. An element of Tens_<sub>k</sub>_(R) is a _k-th order tensor over_ R; when R=C, it is a _complex k-th order tensor_. For nonzero classes, define

\([A]\oplus_K\left[B\right]=[A\oplus_KB],[A]\otimes_K\left[B\right]=[A\otimes_KB].\)

Extend these operations by \(T\oplus_K0_k=0_k\oplus_KT=T\) and \(T\otimes_K0_k=0_k\otimes_KT=0_k\) for every \(T\in\mathsf{Tens}_k(\mathcal{R})\). The unit is the class of l_<sub>k</sub>_(1), and we set l_<sub>k</sub>_(0)=0_<sub>k</sub>_. We use the same notation for a nonzero array and its class, and write 0 for 0_<sub>k</sub>_ when the order is clear. For every tensor _T_, set \(T^{\oplus_K0}=0_k\) and \(T^{\otimes_K0}=\mathsf{l}_k(1)\).

The extra assumption on R is used only to construct this semiring and holds in particular for C. It ensures that a product of two nonzero arrays is nonzero. The array definitions themselves apply to every commutative coefficient semiring. Our use of coordinate-permutation classes follows Wigderson and Zuiddam \[WZ26, Example 2.20\]; we explicitly adjoin the zero element, as permitted by their semiring convention \[WZ26, Definition 2.1\].

We verify the semiring properties. Permutations on _A_ and _B_ combine into a block permutation on each leg of \(A\oplus_KB\). For \(A\otimes_KB\), the permutations on leg _d_ act on the paired index by \((i,j)\mapsto(\sigma_d(i),\tau_d(j))\). Thus both operations are independent of the representatives. Associativity follows by concatenating three coordinate blocks for direct sums and by identifying the three paired indices for products. Swapping the two blocks on every leg proves commutativity of \(\oplus_K\). The permutation \(im_d+j\mapsto jn_d+i\) on leg _d_ proves commutativity of \(\otimes_K\).

For distributivity, the coordinates on each leg of \(A\otimes_K\left(B\oplus_KC\right)\) have the form (_i,j_) with _j_ in either the _B_ block or the _C_ block. List the pairs from the _B_ block first and those from the _C_ block second. This gives the coordinate order of \((A\otimes_KB)\oplus_K\left(A\otimes_KC\right)\). Terms choosing different blocks on different legs have coefficient zero on both sides, and the remaining coefficients agree by the definition of \(\otimes_K\). Hence distributivity also holds. The class of l_<sub>k</sub>_(1) is a multiplicative unit. Finally, all identities involving 0_<sub>k</sub>_ follow from its defining rules. Therefore Tens_<sub>k</sub>_(R) is a commutative semiring.

**Remark 2.7** (coordinates and tensor relations)**.** For a nonzero tensor, its dimension vector is the common dimension vector of its representatives. The formal zero tensor has no fixed positive dimension vector. In a coordinate identity, it is written as the zero coefficient table of the stated ambient dimensions. This convention is used for entrywise sums and local maps, not to replace the defining rules for \(\oplus_K\) and \(\otimes_K\) involving 0_<sub>k</sub>_.

The operation \(\otimes_C\) also descends to nonzero classes, because coordinate permutations of its factors act on disjoint groups of legs. For \(S\in\mathsf{Tens}_p(\mathcal{R})\) and \(T\in\mathsf{Tens}_q(\mathcal{R})\), set \(0_p\otimes_CT=\)<tbc>

