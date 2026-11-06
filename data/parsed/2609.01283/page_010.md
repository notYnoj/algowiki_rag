force the repaired flow to saturate fewer or more of these buffer edges, allowing us to obtain the new max-flow value \(\lambda_{G+U}(s,t)\) directly off the buffer usage via binary search (Theorem 4.3).

By plugging this residual graph formulation back into our all-pairs bounded flow oracle with _k=O(f_), we drop the global capacity _n_ from the query time entirely. This resolves the open problem of \[BBP22\] by yielding an exact max-flow oracle bounded purely by \(\widetilde{O}(f^{3\omega})\) query time and _O_((_fn_)<sup>2</sup>log_n_) space. Costs are handled seamlessly by tracking the cost of the rerouting paths in the residual graph (Theorem 4.4).

### Strategy 2: The Subset Sensitivity Model (Decoupling)

While the residual rerouting strategy successfully removed _k_ from the query time, the query time still turns out to be \(O(f^{3\omega})\). This leads to a second question:

_Can we remove the dependence on k from the algebraic update time directly, maintaining an_ \(O(f^\omega)\) _query cost while simultaneously shrinking the space requirement?_

The algebraic bottleneck in the general model occurs because every physical edge update forces the oracle to explicitly rewrite _O(k_<sup>2</sup>) entries in the dense union representation.

We resolve this by _decoupling the updates from the representations_. We _freeze_ the representation matrices _A_:=_U_<sub>out</sub> and _B_:=_U_<sub>in</sub> at preprocessing. Instead of updating the matroids directly, we realize every network update as a simple _diagonal switch_ in the weight matrix _D_. An element is either toggled on, off, or reweighted. For an update set \(S\subseteq Q\) of size _f_, the query matrix becomes:<tbc>

\(L'=AD'B^T=L+A_S\Delta_SB_S^T\)

<tbc>and by Theorem 2.3,<tbc>

\(det(L')=det(L)\cdot det\big(I_f+B_S^TL^{-1}A_S\Delta_S\big).\)

<tbc>The only data a query needs is the \(f\times f\) matrix \(B_S^TL^{-1}A_S\). Interestingly, we observe that if the locus of edge updates is confined to a _susceptible set Q_ of size \(\sigma\) declared at preprocessing, then it suffices to compute and store the \(\sigma\times\sigma\) principal submatrix

\(U_Q:=B_Q^TL^{-1}A_Q.\)

This allows us to also introduce the **Subset Sensitivity Model**, where a susceptible set of elements _Q_ (of size \(\sigma\)) is designated at preprocessing time. We thus obtain the following result.

**Lemma 1.1** (Subset determinant oracle; see Theorem A.1)**.** _Let_ \(A,B\in\mathbb{F}_d[Y]^{r\times m}\)_, let D be diagonal, L=ADB<sup>T</sup> (possibly singular), and let_ \(Q\subseteq[m]\), \(|Q|=\sigma\)_, be fixed at preprocessing. There is a data structure that, for any_ \(D'\) _differing from D in_ \(\le f\) _positions within Q, computes_ \(det(AD'B^T)\)_: for d_=0_, with_ \(O(\sigma^2r^{\omega-2}+r^\omega)\) _preprocessing,_ \(O(\sigma^2)\) _space, and_ \(O(f^\omega)\) _query time._

By leveraging this subset determinant lemma on our fixed (_s,t_) flow formulations, we remove the dependence on matrix dimensions and packing parameters from the query time, yielding an exact (_s,t_)-max flow oracle with an optimal \(\widetilde{O}(f^\omega)\) query time and strict \(O(\sigma^2)\) space.

## 1.2.3 Other Applications of Matroid Intersection

Our algebraic framework extends far beyond (_s,t_)-flows. We discuss some of these applications below.

