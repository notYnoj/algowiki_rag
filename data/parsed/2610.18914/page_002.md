## 2 Separation by polynomial multiplication

**Proposition 2.1** (Shared-leg separation)**.** _Let_ \(M,n\ge 1\)_, and suppose that F contains at least M+n_-1 _distinct elements. Let_<tbc>

\(A_h:X\times Y_h\times Z_h\longrightarrow F(1\le h\le M)\)

<tbc>_be trilinear forms, and define their matched sum by_<tbc>

\(A(x,y,z)=\sum_{h=1}^MA_h(x,y_h,z_h),y\in\oplus_hY_h,z\in\oplus_hZ_h.\)

<tbc>_Then_

\(\boxed{A^{\oplus(M+n-1)}\unknown\rightarrow\oplus_{h=1}^M(A_h\otimes B_X(n)).}\) (2.1)

_Here B<sub>X</sub>(n_) _is the dot-product tensor_

\(B_X(n):F\times J\times J^\vee\longrightarrow F,(c,j,\varphi)\longmapsto c\varphi(j),\)

_for any n-dimensional space J. The direct sum on the right of_ (2.1) _has independent spaces on all three legs._

_Proof._ We want the _h_th block to read only the _h_th copy of _X_. Polynomial interpolation provides exactly such coordinates. Choose distinct \(a_1,\dots,a_M\in F\) and put<tbc>

\(P=F[t]_{<M},J=F[u]/(u^n),\)

<tbc>where _F_\[_t_\]_<sub>\<d</sub>_ denotes the polynomials of degree less than _d_. The map

\(e:P\longrightarrow F^M,p\longmapsto(p(a_1),\dots,p(a_M))\) (2.2)

is an isomorphism: a polynomial of degree less than _M_ cannot vanish at all _M_ points unless it is zero, and the dimensions agree. Thus \(X\otimes P\) can supply the desired independent copies of _X_.

For each _h_, substitute \(t=a_h+\varepsilon u\) and define<tbc>

\(\sigma_h(p,j)=p(a_h+\varepsilon u)j\text{in}J[\varepsilon].\)

<tbc>The substitution is defined on all of _F_\[_t_\]; in particular, \(\sigma_h\) is bilinear on \(P\times J\). It has two useful properties. At \(\varepsilon=0\) it becomes \(\sigma_h(p,j)=p(a_h)j\), which reads exactly the evaluation coordinate in (2.2). For \(\varepsilon\neq 0\), substitution identifies _F_\[_t_\]_<sub>\<n</sub>_ with _J_:

\((t-a_h)^s\longmapsto\varepsilon^su^s(0\le s<n).\)

Both sides are bases, and all the displayed factors are invertible.

We now assemble these actions into one polynomial family on<tbc>

\(\widetilde{X}=X\otimes P,\widetilde{Y}=\oplus_h(Y_h\otimes J),\widetilde{Z}=\oplus_h(Z_h\otimes J^\vee).\)

<tbc>Define \(\Phi(\varepsilon)\) on matching components by

\(\Phi(\varepsilon)(x\otimes p,y_h\otimes j,z_h\otimes\varphi)=A_h(x,y_h,z_h)\varphi(\sigma_h(p,j)),\) (2.3)

