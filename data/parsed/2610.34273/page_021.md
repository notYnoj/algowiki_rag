_for_ \(0\le h<M\), \(0\le b<b_h\), \(0\le c<c_h\)_, and_ \(0\le a_j<d_j\) _for_ \(1\le j\le\ell\)_; set all other entries to zero. Thus the last two legs use the same block label h, while the first_ \(\ell\) _legs are shared by all blocks. When_ \(\ell=0\)_, the shared coordinates are omitted. Zero blocks are allowed, with their specified coordinate dimensions. Then_

\(A^{\oplus_K(2k-1)M}\unknown\oplus_{h=0}^{M-1}(A_h\otimes_KE_{k-1,k}^{(M)}).\)

_The sum on the right is a full Kronecker direct sum: every nonzero summand has its own coordinates on every one of the k legs._

_Proof._ If every _A<sub>h</sub>_ is zero, both sides of the claimed degeneration are zero, so the assertion holds. Otherwise, let \(\mathcal{A}=\prod_{j=1}^\ell[d_j]_0\); when \(\ell=0\), this set consists of the empty tuple. Write _x<sub>j,a</sub>_ for coordinate _a_ on shared leg _j_, where \(1\le j\le\ell\) and \(0\le a<d_j\). On the last two legs, write _y<sub>h,b</sub>_ for coordinate \(\beta_h+b\) and _z<sub>h,c</sub>_ for coordinate \(\gamma_h+c\), where \(0\le h<M\), \(0\le b<b_h\), and \(0\le c<c_h\). In the formal multilinear notation of Definition 2.10, put \(\alpha_{h,\mathbf{a},b,c}=(A_h)_{a_1,\dots,a_\ell,b,c}\). Then

\(A=\sum_{h=0}^{M-1}\sum_{\mathbf{a}\in\mathcal{A}}\sum_{0\le b<b_h0\le c<c_h}\alpha_{h,\mathbf{a},b,c}\left(\prod_{j=1}^\ell x_{j,a_j}\right)y_{h,b}z_{h,c}.\)

An empty product of coordinate symbols is 1. As in the preliminaries, a product of symbols records a basis tensor, and substitutions for symbols act independently on the individual legs.

Put \(L=(2\ell+3)M=(2k-1)M\), and let \(\zeta\) be a primitive _L_-th root of unity. Index the _L_ direct-sum copies of _A_ by \(0\le r<L\). Introduce target coordinates _X<sub>j,a,g</sub>_, _Y<sub>h,b,u</sub>_, and _Z<sub>h,c,v</sub>_, where the original indices have the ranges just specified and \(0\le g,u,v<M\). On each copy _r_, use the following local linear substitutions:

\(x_{j,a}^{(r)}\longmapsto\sum_{g=0}^{M-1}\zeta^{2rg}X_{j,a,g}(1\le j\le\ell,0\le a<d_j),\)<br>
\(y_{h,b}^{(r)}\longmapsto\sum_{u=0}^{M-1}\zeta^{r(u-\ell h)}Y_{h,b,u}(0\le h<M,0\le b<b_h),\)<br>
\(z_{h,c}^{(r)}\longmapsto\frac{1}{L}\sum_{v=0}^{M-1}\zeta^{r(-v-\ell h)}Z_{h,c,v}(0\le h<M,0\le c<c_h).\)

All source copies map into the same target coordinates on each leg. In a term with target indices \(g_1,\dots,g_\ell,u,v\), define the integer \(\nu=u-v+2\sum_{j=1}^\ell(g_j-h)\). Summing that term over the source-copy index _r_ multiplies its coefficient by<tbc>

\(\frac{1}{L}\sum_{r=0}^{L-1}\zeta^{r\nu}=\left\{\begin{array}{ c c }
1, & L|\nu, \\
0, & L\nmid\nu.
\end{array}\right.\)

<tbc>Indeed, when \(L|\nu\), every summand is 1. Otherwise \(\zeta^\nu\neq 1\), and the geometric sum is \((1-\zeta^{L\nu})/(1-\zeta^\nu)=0\). Since all the new indices lie between 0 and _M_-1, we also have<tbc>

\(|\nu|\le|u-v|+2\sum_{j=1}^\ell|g_j-h|\le(2\ell+1)(M-1)<L.\)

