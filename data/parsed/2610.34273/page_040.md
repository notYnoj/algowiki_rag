**Lemma 5.8** (properties of the comparison function)**.** _For every integer_ \(d\ge 2\)_, the function H<sub>d</sub> is nondecreasing and concave in each coordinate separately. For every_ \(\mathbf{a}\in[1,\infty)^d\)_, with_ \(D=1+\sum_{i=1}^d(a_i-1)\)_, it satisfies_<tbc>

\(H_d(\mathbf{a})\le\prod_{i=1}^da_i,H_d(\mathbf{a})^{(d+1)/(2d)}\le D.\)

<tbc>_For all real numbers_ \(b,h,m,t\ge 1\) _and all_ \(\mathbf{a}\in[1,\infty)^{d-1}\)_, writing_ \(S=\sum_{i=1}^{d-1}(a_i-1)\)_, we also have_<tbc>

\(H_d(1,\dots,1,b)=b,H_d(\mathbf{a},3h+S)\ge 3H_d(\mathbf{a},h),\)

<tbc>_and_<tbc>

\(H_d(m,\dots,m,t)\ge tm^{(d-1)/(d+1)}.\)

<tbc>_Finally, for every real_ \(a\ge 1\),<tbc>

\(H_d(a,\dots,a)=\left(\frac{(d+1)a-(d-1)}{2}\right)^{2d/(d+1)}.\)

<tbc>_Proof._ First note the identities and inequalities<tbc>

\(\sum_{j=1}^dc_j=2\sum_{r=1}^d\left(\frac{1}{r}-\frac{1}{r+1}\right)=\frac{2d}{d+1},L_{j+1}-L_j=(d+1-j)(b_{j+1}-b_j)\ge 0(1\le j<d).\)

<tbc>If _r=d_+1-_j_, then<tbc>

\(L_j\ge(r+1)b_j-(r-1)\ge 2b_j.\)

<tbc>Moreover,

\(2D-L_j=\sum_{i=1}^{j-1}(b_i-1)+\sum_{i=j+1}^d(2b_i-b_j-1)\ge 0.\)

Every factor _L<sub>j</sub>/_2 therefore lies between 1 and _D_. Its exponent in \(H_d^{(d+1)/(2d)}\) is positive, and these exponents sum to one. This proves the interpolation bound.

Fix all coordinates except one, denoted _x_, and consider an interval on which its sorting position is _j_. Put _r=d_+1-_j_, _z_=1_/L<sub>j</sub>_, and<tbc>

\(B=\sum_{i=j+1}^d\frac{c_i}{L_i},C=\sum_{i=j+1}^d\frac{c_i}{L_i^2},W=\sum_{i=j+1}^dc_i=2-\frac{2}{r}.\)

<tbc>All three sums are zero if _j=d_. Differentiation on this interval gives<tbc>

\(\frac{\partial lnH_d}{\partial x}=\frac{2z}{r}+B,\frac{1}{H_d}\frac{\partial^2H_d}{\partial x^2}=\left(\frac{2z}{r}+B\right)^2-\frac{2(r+1)}{r}z^2-C.\)

<tbc>The first derivative is nonnegative. Since \(L_i\ge L_j\ge 2x\) for _i\>j_, it also satisfies

\(0\le\frac{\partial lnH_d}{\partial x}\le\frac{2/r+W}{L_j}=\frac{2}{L_j}\le\frac{1}{x}.\) (5)

If _r_=1, then _B=C=W_=0 and the second derivative is zero. Suppose \(r\ge 2\). Then \(W\ge 1\), \(0\le B\le Wz\), and the weighted Cauchy-Schwarz inequality gives \(C\ge B^2/W\). Put _y=B/z_. The second derivative divided by _H<sub>d</sub>z_<sup>2</sup> is at most<tbc>

\(f_r(y)=\left(\frac{2}{r}+y\right)^2-\frac{2(r+1)}{r}-\frac{y^2}{W},0\le y\le W.\)

