## 1 Introduction

### 1.1 Graph tensors and previous bounds

The rank of a tensor is the minimum number of simple tensors whose entrywise sum represents it in fixed coordinates. A simple tensor is a product of first-order tensors, with one factor for each leg. For a bilinear map, tensor rank measures the number of products of linear forms needed to compute its outputs. This connection has played a central role in the study of matrix multiplication since Strassen’s algorithm \[Str69, BCS97\]. When several copies of a tensor are computed together, their rank can be smaller than the product of their individual ranks. The corresponding asymptotic rank is

\(\widetilde{\mathrm{R}}(T)=\mathrm{lim}_{N\rightarrow\infty}\mathrm{R}(T^{\otimes_KN})^{1/N}.\)

Here a _leg_ is one coordinate direction of the tensor, and the Kronecker product \(\otimes_K\) pairs corresponding indices while preserving the number of legs. Definitions 2.2, 2.12, and 2.13 give the precise conventions. Throughout this paper, ranks are taken over the complex numbers.

Graph tensors provide a natural family in which to study this behavior beyond bilinear maps \[CVZ19, CZ19\]. Let _q_ be a positive integer. For a simple undirected graph _G_, place the two- party tensor \(\sum_{i=0}^{q-1}e_i^{(q)}\otimes_Ce_i^{(q)}\) on every edge, and group all indices incident with the same vertex into one leg. The resulting tensor GT_<sub>q</sub>(G_) has one leg for each vertex. The basis vectors \(e_i^{(q)}\) and the construction operation \(\otimes_C\) are defined in Definition 2.3; the complete coordinate definition of GT_<sub>q</sub>(G_) appears in Definition 2.20. In quantum information, this tensor describes pairwise maximally entangled states shared along the edges of a network. Rank and subrank describe conversions between these pairwise resources and a state shared by all parties \[VC17, CVZ19\].

For a triangle, each leg is indexed by a pair. With \(e_{(i,j)}=e_{iq+j}^{(q^2)}\) for \(0\le i,j\le q-1\), local coordinate permutations give

\(\mathsf{GT}_q(K_3)\cong\sum_{0\le i,j,h\le q-1}e_{(i,j)}\otimes_Ce_{(j,h)}\otimes_Ce_{(h,i)}.\)

This is precisely the matrix multiplication tensor. Let \(\omega\) be the infimum of the real numbers \(\gamma\) such that, for every \(\varepsilon>0\), two \(q\times q\) complex matrices can be multiplied using \(O_\varepsilon(q^{\gamma+\varepsilon})\) arithmetic operations. Then \(\omega=\mathrm{log}_2\widetilde{\mathrm{R}}(\mathsf{GT}_2(K_3))\). Thus, determining the asymptotic rank of graph tensors extends the matrix multiplication problem to an arbitrary number of parties.

Strassen’s seven-product algorithm gave \(\omega\le\mathrm{log}_27<3\) \[Str69\]. Approximate bilinear algorithms and interpolation introduced the use of degenerations \[BCRL79, Bin80\]. Schönhage’s asymptotic sum inequality converted simultaneous independent products into upper bounds on \(\omega\) \[Sch81\]. Strassen’s laser method and the Coppersmith–Winograd construction then provided a framework based on extracting useful components from large tensor powers \[Str86, Str87, CW90\]. Subsequent work improved the tensor-power analysis, the extraction of components, and the treatment of asymmetric parameters \[Sto10, DS13, VW12, LG14, AW21, DWZ23, VXXZ24, ADW<sup>+</sup>25\].  1 records selected milestones.

