<tbc>described in Definition 4.4. For example, the bipartite component spanned by the three vertices 1,2,5 induces a pure layered tripartite sub-DAG \(\hat{G}\) of _G_ including -2 and -1. (Similarly, the bipartite component spanned by -2,1,3 yields the pure layered tripartite sub-DAG of _G_ including 5 and 6.) Application of the chain rule of differentiation as in Lemma 4.1 to \(\hat{G}\) yields a local Jacobian \(A\in\mathbb{R}^{m\times n}\) (here, \(A\in\mathbb{R}^{1\times 2}\) is the gradient of _v_<sub>5</sub> with respect to _v_<sub>-2</sub> and _v_<sub>-1</sub>).

Replacing \(\hat{G}\) with the bipartite DAG of _A_ violates the requirement for _G_ to be layered. Decomposition of _A_ as \(A=I_m\cdot A\) (or \(A=A\cdot I_n\)) takes care of this violation by substitution of a modified pure layered tripartite sub-DAG \(\hat{G}\) as shown in Figure 5(b). The number of intermediate vertices in \(\hat{G}\) is equal to \(\tilde{p}=min(n,m)\) implying a reduction of the number of intermediate vertices in _G_ if \(\tilde{p}<p\). Figure 5 yields \(1=\tilde{p}<p=2\) making the resulting DAG uniformly layered.

Ultimately, preaccumulation always yields the uniformly layered DAG preserving all intermediate layers of size _n_ from the original DAG. In the worst case we get the bipartite DAG of \(F'\). Our objective is to apply preaccumulation selectively as illustrated above. The resulting uniformly layered DAG is made is meant to preserve the sparsity of all local Jacobians as well as possible.

Decomposition of a bipartite graph (similarly, DAG) _G_=(_V,E_) into its connected components turns out to be straightforward. Each vertex belongs to exactly one connected component. Repeated (e.g., depth-first) searches starting from unassigned vertices yield a decomposition into connected components at a computational cost of O(|_V_|+|_E_|).

The following definitions formalize the above followed by the proof of the numerical correctness of preaccumulation in combination with bipartite DAG splitting.

Definition 4.4 (Pure Layered Tripartite sub-DAG). _A layered tripartite sub- DAG G_=(_V,E), V_=(_X,Z,Y), as in Definition 2.3 is_ pure _if P(Z_)=_X and S(Z_)=_Y._

Definition 4.5 (Preaccumulation). _Let G be a pure layered tripartite sub-DAG as in Definition 4.4 representing a local Jacobian product_ \(F'=F'_2\cdot F'_1\). Preaccumulation _replaces G by the bipartite sub-DAG representing_ \(F'\).

Lemma 4.6. _Let a DAG G induce an invertible Jacobian_ \(F'\in\mathbb{R}^{n\times n}\) _under the chain rule of differentiation as in Lemma 4.1._

1. _The Jacobian is invariant under preaccumulation as in Definition 4.5._

5
6
7
5
6
7
1
1,1
a1,2
1
2
3
4
1,2
3
4
b1,1
b2,2
a1,1b1,1
a1,2b2,2
-2
-1
0
-2
-1
0

(a) (b)

Fig. 5. _Preaccumulation_

