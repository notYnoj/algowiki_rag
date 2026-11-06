### Unique rank-one exactness.

If _f_ has a unique Boolean minimizer _x<sub>⋆</sub>_, define the first order of _unique rank-one exactness_,

\(d_\star(f):=\mathrm{min}\big\{1\le d\le n:\mathrm{deg}f\le 2d,\mathrm{argmin}(\mathrm{P}_d)=\{b_d(x_\star)b_d(x_\star)^\top\}\big\}.\) (2.5)

This is well defined with \(d_\star(f)\le n\), and it persists upward: unique rank-one exactness at _d_<sub>0</sub> implies it at every \(d_0\le d\le n\) (Theorem 6.1). Throughout the Boolean sections, §2 and §4-§5, we fix an order \(d\ge d_\star(f)\) and abbreviate \(X_\star=uu^\top=Nqq^\top\) with \(u:=b_d(x_\star)\in\{\pm 1\}^N\) and \(q:=u/\sqrt{N}\).

_Remark_ 2.1 (Symmetric objectives need a gauge). A unique Boolean minimizer excludes symmetric models such as MAX-CUT or zero-field Ising objectives, whose minimizers come in \(\pm\) pairs; they enter after a standard gauge fixing (fixing one spin), and we use them as motivation only.

### Merged squares and degeneracy.

Every optimal certificate annihilates _u_, since \(u^\top Su=f(x_\star)-f_\star=0\) and \(S\unknown 0\); so S_<sub>⋆</sub>_ lives on the cone \(\mathbb{S}_+(V):=\{S\unknown 0:\mathrm{ran}(S)\subseteq V\}\), where _U_:=ran(_X<sub>⋆</sub>_)=span{_q_} and \(V:=\mathrm{ker}(X_\star)=q^\perp\). Now let \(d\ge 2\), choose two coordinates \(i\neq j\), put _a_:=_x<sub>⋆,i</sub>x<sub>⋆,j</sub>_, and define two vectors in R_<sup>N</sup>_: \(w_1:=e_\emptyset-ae_{\{i,j\}}\) and _w_<sub>2</sub>:=_e_<sub>{_i_}</sub>-_ae_<sub>{_j_}</sub>. Both are orthogonal to _u_, and because \((x^{\{i,j\}})^2\equiv(x^{\{i\}})^2\equiv 1\), both rank-one Gram matrices represent the _same_ Boolean polynomial:

\(b_d(x)^\top w_1w_1^\top b_d(x)\equiv 2\big(1-ax_ix_j\big)\equiv b_d(x)^\top w_2w_2^\top b_d(x)(\mathrm{mod}I_\mathrm{B}).\) (2.6)

Quotienting by \(x_i^2=1\) thus merges distinct squares and creates nonzero _same-polynomial directions_ such as \(w_1w_1^\top-w_2w_2^\top\). These directions live in the subspace \(\mathcal{L}:=\mathrm{ran}(\mathcal{A}_d^*)\cap\mathbb{S}(V)\), where S(_V_) denotes the symmetric matrices supported on _V_ . Differences of optimal certificates always lie in L, and under strict complementarity L is the direction space of S_<sub>⋆</sub>_ (Theorem C.2).

**Proposition 2.2** (Primal degeneracy at every order \(d\ge 2\))**.** _For the independent encoding_ A_<sub>d</sub>, primal nondegeneracy of X<sub>⋆</sub> \[AHO97\] holds if and only if m=N, and_ \(\mathrm{dim}\mathcal{L}=m-N=\frac{N(N-1)}{2}-|\mathcal{I}_{2d}|+1\)_. At d_=1 _one has m=N; at every_ \(2\le d\le n\) _one has m\>N (indeed_ \(w_1w_1^\top-w_2w_2^\top\in\mathcal{L}\backslash\{0\}\)_), so the rank-one primal optimum is degenerate. If, in addition,_ S_<sub>⋆</sub> contains a_ strictly complementary _certificate S_<sub>sc</sub>_, i.e._ rank(_S_<sub>sc</sub>)=_N_-1_, then_ affS_<sub>⋆</sub>=S_<sub>sc</sub>+L_, so_ S_<sub>⋆</sub> is positive-dimensional with_ dimS_<sub>⋆</sub>=m-N._

The proof is in Appendix B. Degeneracy here concerns the optimum relative to the constraints rather than singularity of the matrix _X<sub>⋆</sub>_ itself. The encoding is always _injective_ on the tangent space of the rank-one PSD manifold, while nondegeneracy asks for _surjectivity_ onto R_<sup>m</sup>_.

### The geometric problem.

Suppose from now on that S_<sub>⋆</sub>_ contains one strictly complementary certificate _S_<sub>sc</sub>; equivalently, \(X_\star+S_\mathrm{sc}\succ 0\). Then \(\mathcal{S}_\star=(S_\mathrm{sc}+\mathcal{L})\cap\mathbb{S}_+(V)\) (Theorem C.2), a compact convex slice of the PSD cone supported on _V_ . The certificate _S_<sub>sc</sub> lies in the relative interior of this slice, every certificate on its relative boundary loses rank, and by Theorem 2.2 the boundary is nonempty for \(d\ge 2\). A first-order method is free to converge to any point of the slice; at a relative-boundary point, analyses that require strict complementarity at the selected limit do not apply, and general conic programming _does_ produce arbitrarily slow regions there \[KY26a\].

## 3 Residual-Field Rigidity

This section is Boolean-free. Theorem 3.1 below asks only for compact optimal sets and one strictly complementary pair; neither optimum needs to be unique. The result is a theorem that makes five<tbc>

