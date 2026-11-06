Letting \(u\downarrow 0\) and using \(P(u)\ge 0\) gives \(P(v)\ge L_iv\). Thus _P(s)/L<sub>i</sub>-s_ is nonnegative and nondecreasing; the same holds for _Q_. Their sum is at most one by (G.1). Approaching both suprema at one sufficiently large _s_ proves \(c_{ij}+c_{ik}\le 1\). The affine upper bounds follow from the definition of the offsets. Since the residuals are nondecreasing and bounded, these suprema also equal their limits as \(s\rightarrow\infty\).

_Proof of Proposition 5.2._ If some _p<sub>i</sub>_=0, its summand is already \(\pi/2\). Assume all three parameters are positive. Lemma 5.1 gives six offsets and their three bounds<tbc>

\(c_{ij}\ge 0,c_{ij}+c_{ik}\le 1.\)

<tbc>The increment and affine bounds give<tbc>

\(\frac{P_{ij}(s+t)}{P_{ij}(s)}\ge 1+\frac{L_it}{P_{ij}(s)}\ge 1+\frac{t}{s+c_{ij}}.\)

<tbc>Using homogeneity, we obtain<tbc>

\(\frac{g_{ij}(r,s+t)}{g_{ij}(r,s)}\ge\left(1+\frac{t}{s+c_{ij}r}\right)^{p_i}.\) (G.2)

<tbc>Increase _r_ by \(\varepsilon r\), then _s_ by \(\varepsilon s\). Input interchange supplies the first bound and (G.2) supplies the second:

\(1+\varepsilon=\frac{g_{ij}((1+\varepsilon)r,(1+\varepsilon)s)}{g_{ij}(r,s)}\)<br>
\(\ge\left(1+\frac{\varepsilon r}{r+c_{ji}s}\right)^{p_j}\left(1+\frac{\varepsilon s}{s+c_{ij}(1+\varepsilon)r}\right)^{p_i}.\)

Take logarithms, divide by \(\varepsilon\), and let \(\varepsilon\downarrow 0\). The elementary limit \(log(1+\varepsilon x)/\varepsilon\rightarrow x\) gives<tbc>

\(1\ge\frac{p_is}{s+c_{ij}r}+\frac{p_jr}{r+c_{ji}s}(r,s>0).\)

<tbc>With _t=r/s_, this is equivalent to<tbc>

\((1-p_j)c_{ij}t^2+(1-p_i-p_j+c_{ij}c_{ji})t+(1-p_i)c_{ji}\ge 0(t>0).\)

<tbc>A quadratic _At_<sup>2</sup>+_Bt+C_ with \(A,C\ge 0\) is nonnegative on _t\>_0 exactly when \(B\ge-2\sqrt{AC}\). Indeed, divide by _t_ and use \(inf_{t>0}(At+C/t)=2\sqrt{AC}\); if _A_ or _C_ is zero, the infimum is zero, approached at an endpoint. Thus writing \(x=\sqrt{c_{ij}c_{ji}}\) gives \((x+\sqrt{(1-p_i)(1-p_j)})^2\ge p_ip_j\), or

\(\sqrt{c_{ij}c_{ji}}\ge\left(\sqrt{p_ip_j}-\sqrt{(1-p_i)(1-p_j)}\right)_+,\)

where (_z_)<sub>+</sub>=max{_z,_0}.

For any nonnegative _x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>3</sub>, AM-GM and (21) give<tbc>

\(\sum_{i<j}2\sqrt{c_{ij}c_{ji}}x_ix_j\le\sum_{i<j}(c_{ij}x_i^2+c_{ji}x_j^2)\le\sum_ix_i^2.\)

<tbc>Put \(\theta_i=arccos\sqrt{p_i}\) and suppose \(S=\theta_1+\theta_2+\theta_3<\pi/2\). Take \(x_i=cos\theta_i>0\). By (24), \(\sqrt{c_{ij}c_{ji}}\ge cos(\theta_i+\theta_j)\). For the other two indices _j,k_, the product-to-sum identities give

\(cos(\theta_i+\theta_j)x_j+cos(\theta_i+\theta_k)x_k=cos\theta_i+\frac{cos(\theta_i+2\theta_j)+cos(\theta_i+2\theta_k)}{2}\)<br>
\(=x_i+cosScos(\theta_j-\theta_k)>x_i.\)

