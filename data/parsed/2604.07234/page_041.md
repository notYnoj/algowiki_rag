<tbc>**Proposition 4.12** (Explicit solution of the algebraic system)**.** _Writing_ \(c=1/\alpha\) _for algebraic convenience, for c\>_1 _(equivalently_ \(\alpha<1\)_), the system Z(x,y_)=1 _together with the stationarity condition from Proposition 4.11 has a unique solution_ \((x,y)\in(0,1)\times(0,\infty)\) _given by_ \(x=x_\alpha\) _and_ \(y=y_\alpha\) _as defined in Theorem 1.3._

_Proof._ By Lemma 4.10, _Z(x,y_)=1 is equivalent to<tbc>

\(xy=\sqrt{(1-x-xy)^2-4x^2y}.\)

<tbc>Squaring both sides yields<tbc>

\(x^2y^2=(1-x-xy)^2-4x^2y.\)

<tbc>Expanding the right-hand side and cancelling _x_<sup>2</sup>_y_<sup>2</sup> yields

(I) \(x^2(1-2y)-2x(1+y)+1=0,\)

which can be solved for _y_ as \(y=(1-x)^2/\big[2x(1+x)\big].\)

On the surface _Z_=1, the optimality of \(\mathsf{R}(\alpha)=-\mathrm{log}x-\alpha\mathrm{log}y\) requires stationarity with respect to (_x,y_) constrained to (I). Writing<tbc>

\(Q(x,y):=x^2(1-2y)-2x(1+y)+1,\)

<tbc>the Lagrange condition \(\nabla[-\mathrm{log}x-\alpha\mathrm{log}y]=\lambda\nabla Q\) gives (after dividing the two components)

(II) \(\frac{(1+y)-x(1-2y)}{y(x+1)}=c.\)

This can be solved for _y_ as \(y=(1-x)/\big[(c-1)+(c-2)x\big].\)

Equating the two expressions for _y_ from (I) and (II) (and dividing by \(1-x\neq 0\) for _c\>_1) gives<tbc>

\(\frac{1-x}{2x(1+x)}=\frac{1}{(c-1)+(c-2)x}.\)

<tbc>Cross-multiplying: \((1-x)\big[(c-1)+(c-2)x\big]=2x(1+x)\), which expands and simplifies to the quadratic

(4.43) \(cx^2+3x-(c-1)=0.\)

By the quadratic formula, the unique positive root is<tbc>

\(x=\frac{-3+\sqrt{9+4c(c-1)}}{2c}=\frac{-3+\sqrt{4c^2-4c+9}}{2c}.\)

<tbc>Since \(\sqrt{4c^2-4c+9}=c\sqrt{9c^{-2}-4c^{-1}+4}=c\Delta(c)\), we obtain \(x=\big(\Delta(c)-3c^{-1}\big)/2=x_c\). Substituting back into _y_=(1-_x_)<sup>2</sup>/\[2_x_(1+_x_)\] and using \(\Delta-3/c=2x_c\) (hence \(3/c+2-\Delta=2(1-x_c)\) and \(2+\Delta-3/c=2(1+x_c)\)), we get

\(y_c=\frac{4(1-x_c)^2}{2\cdot 2x_c\cdot 2(1+x_c)}=\frac{(3c^{-1}+2-\Delta(c))^2}{2(\Delta(c)-3c^{-1})(2+\Delta(c)-3c^{-1})},\)

matching the definition in Theorem 1.3. Since \(\sqrt{4c^2-4c+9}>3\) for _c\>_1, we have _x<sub>c</sub>\>_0, and since 0_\<x<sub>c</sub>\<_1 we have _y<sub>c</sub>\>_0. □

_Proof of Theorem 1.3._ By Theorem 4.8, \(\mathrm{lim}_{M\rightarrow\infty}\frac{1}{N}\mathrm{log}\overline{Z}=\mathsf{R}(\alpha)\). By Propositions 4.11 and 4.12,

\(\mathsf{R}(\alpha)=-\mathrm{log}x_\alpha-\alpha\mathrm{log}y_\alpha,\)

which gives (4.1). By the discussion at the beginning of Section 4, this proves Theorem 1.3. □

## 5. Open Problems

We conclude the paper with several suggestions for future research.

