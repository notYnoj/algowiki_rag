<tbc>**Lemma 4.10** (Closed-form partition function)**.** _For all x,y\>_0 _with_ (1-_x-xy_)<sup>2</sup>_\>_4_x_<sup>2</sup>_y,_

(4.28) \(Z(x,y)=\frac{xy}{\sqrt{(1-x-xy)^2-4x^2y}}.\)

_Moreover,_ \(Z(x,y)=\infty\) _for all x,y\>_0 _that fail to satisfy this condition._

_Proof._ We begin by rewriting the partition function using a shift of indices together with Vandermonde’s identity. Shifting indices _m_:=_a_-1, _k_:=_b_-1 gives<tbc>

(4.29) \(Z(x,y)=xy\sum_{m=0}^\infty x^m\sum_{k=0}^m\genfrac(){pt}{2}{m}{k}^2y^k.\)

<tbc>For fixed _m_, the inner sum equals [_t<sup>m</sup>_](1+_t)<sup>m</sup>_(1+_yt)<sup>m</sup>_. Indeed,<tbc>

\((1+t)^m=\sum_i\genfrac(){pt}{2}{m}{i}t^i;(1+yt)^m=\sum_j\genfrac(){pt}{2}{m}{j}y^jt^j,\)

<tbc>and extracting the coefficient of _t<sup>m</sup>_ from their product gives<tbc>

\(\sum_{k=0}^m\genfrac(){pt}{2}{m}{k}\genfrac(){pt}{2}{m}{m-k}y^k=\sum_k\genfrac(){pt}{2}{m}{k}^2y^k.\)

<tbc>Hence, we have that

(4.30) \(Z(x,y)=xy\sum_{m=0}^\infty[t^m]\left(x(1+t)(1+yt)\right)^m.\)

We now evaluate the resulting expression via residue computations. We write _f(t_):=_x_(1+_t_)(1+_yt_) and consider the "diagonal sum"<tbc>

\(\Sigma:=\sum_{m\ge 0}[t^m]f(t)^m.\)

<tbc>Since we have that<tbc>

\([t^m]f(t)^m=\frac{1}{2\pi i}\oint f(t)^mt^{-m-1}dt,\)

<tbc>summing the geometric series inside the integral yields<tbc>

\(\Sigma=\frac{1}{2\pi i}\oint\frac{dt}{t-f(t)},\)

<tbc>valid for a contour encircling the origin inside the region of convergence. The equation _t=f(t_), i.e., _t=x_(1+_t_)(1+_yt_), rearranges to

(4.31) \(Q(t):=xyt^2+(x+xy-1)t+x=0,\)

a quadratic in _t_ with discriminant

(4.32) \(D=D(x,y):=(1-x-xy)^2-4x^2y=\left(1-x(1+\sqrt{y})^2\right)\left(1-x(1-\sqrt{y})^2\right).\)

The two roots are

\(t_\pm=\frac{(1-x-xy)\pm\sqrt{D}}{2xy},\)

and _t_<sub>-</sub> is the small root enclosed by the contour. Since \(f'(t)=x(1+y)+2xyt\), we have

\(1-f'(t_-)=1-x(1+y)-2xyt_-=1-x-xy-\left[(1-x-xy)-\sqrt{D}\right]=\sqrt{D}.\)

