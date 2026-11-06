For instance, the _r-rank Exact Triangle_ problem is to solve an Exact Triangle instance (_A,B,C_) for which we additionally receive access to a select-plus rank-_r_ decomposition of _A_, _B_ or _C_. We also introduce the following notation. We write<tbc>

\(\mathrm{MinPlus}(n_1,n_2,n_3|constraint;\dots;constraint)\)

<tbc>and<tbc>

\(\mathrm{ExactTri}(n_1,n_2,n_3|constraint;\dots;constraint)\)

<tbc>to denote the best-possible running times of the Min-Plus Product and Exact Triangle problems, respectively, restricted to instances that satisfy the list of constraints. Each _constraint_ takes two possible forms. The first is _parameter_ \(\le\) _value_, for any of the parameters defined above, to indicate that this parameter is bounded by _value_. E.g., \(\mathrm{MinPlus}(n,n,n|d\le n^{0.9})\) refers to the running time of the _n_<sup>0.9</sup>-slice-uniform Min-Plus Product problem (where in one of the two matrices the rows or columns contain at most _n_<sup>0.9</sup> distinct entries each). The second form is a free parameter. E.g., the fact that Min-Plus Product with entries in {0_,...,u_} can be solved in time \(\tilde{O}(n^\omega u)\) \[9\] can be expressed concisely as \(\mathrm{MinPlus}(n,n,n|u)=\tilde{O}(n^\omega u)\). As a more complicated example consider

\(\mathrm{ExactTri}(n,n,n|D\le n^{0.9};\rho\le 1/D;K).\)

This expresses the running time of the Exact Triangle problem, restricted to matrices _A,B,C_ with at most _D_ distinct non-\(\perp\) entries such that \(D\le n^{0.9}\), where each entry in _A,B_ and _C_ appears in at most a 1_/D_-fraction of its row and column, and where the set of integer entries in the three matrices has doubling at most _K_. (We will indeed encounter this problem in Lemma 4.13.)

**Remark 2.10.** _Note that many of these parameters are trivially related to each other. For instance, each u-universe instance is trivially u-uniform, and each D-uniform instance is trivially D-slice-uniform. It is also not hard to see that each d-slice-uniform instance is trivially d-rank. In Section 4 we will essentially show the opposites of some of these trivial directions, thereby proving that many of these parameters are_ equivalent _in terms of subcubic-time algorithms._

**Remark 2.11.** _We will usually assume that all entries are polynomially bounded, so we always implicitly add the constraint_ \(u\le(n_1n_2n_3)^{O(1)}\)_. Having said that, all reductions here also apply to larger universes u with an overhead of_ (log_u_)<sup>_O_(1)</sup>.<sup>14</sup>

**Remark 2.12.** _It is straightforward to verify that Vassilevska W. and Williams’ \[97\] reduction from Min Plus Product to Exact Triangle,_ MinPlus(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>|_u_)=_O_(ExactTri\((n_1,n_2,n_3|u)\cdot\mathrm{log}u\)_), also preserves the parameters r, d, and D._

## 2.3 Potential Adjustments

It turns out to be useful to define a particularly constrained type of fine-grained reductions. We often want to transform an Exact Triangle instance (_A,B,C_) into one or more instances that are equivalent in the following sense: Each exact triangle is preserved, and for all other triangles (_i,k,j_) we do not change the value _A_\[_i,k_\]+_B_\[_k,j_\]-_C_\[_i,j_\]. Informally, this requirement is exactly what allows us to simulate reductions for Min-Plus Product (see Lemma 5.7). The following definitions make these requirements formal:

**Definition 2.13** (Potential Adjustment)**.** _Let_ \((A,B,C),(A',B',C')\) _be Exact Triangle instances of the same size_ \(n_1\times n_2\times n_3\)_. We say that_ \((A',B',C')\) _is a_ potential adjustment _of_ (_A,B,C_) _if there are_ potential functions \(u\in\mathbb{Z}^{n_1},v\in\mathbb{Z}^{n_2},w\in\mathbb{Z}^{n_3}\) _so that_

\(A'[i,k]=A[i,k]+u[i]+v[k]orA'[i,k]=\perp forall(i,k)\in[n_1]\times[n_2],B'[k,j]=B[k,j]-v[k]+w[j]orB'[k,j]=\perp forall(k,j)\in[n_2]\times[n_3],C'[i,j]=C[i,j]+u[i]+w[j]orC'[i,j]=\perp forall(i,j)\in[n_1]\times[n_3].\)

<sup>14</sup>There is a technical detail: Somewhere along our chain of reductions, in Lemma 4.9, we rely on a deterministic algorithm with a running time overhead of \(2^{\tilde{O}(\sqrt{\mathrm{log}u})}=u^{o(1)}\). However, this deterministic algorithm can be replaced by a randomized algorithm with only polylogarithmic overhead.

