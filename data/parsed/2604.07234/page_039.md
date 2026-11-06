<tbc>In particular, _t-f(t_) is increasing at \(t_-\neq 0\), so there exist values of _t_ for which |_f(t_)|_\<t_, and such a contour exists (e.g., via a circle with the appropriate radius). The residue at the simple pole _t_<sub>-</sub> of 1/(_t-f(t_)) is thus \(1/\sqrt{D}\), giving \(\Sigma=1/\sqrt{D}\), so \(Z=xy/\sqrt{D}\).

Finally, we show that once the discriminant condition fails, the series defining _Z(x,y_) diverges. It is clear that _Z(x,y_) is increasing in _x_. We fix _x,y\>_0 such that \(D(x,y)\le 0\). Taking \(0<x'<x\) small enough so that \(D(x',y)>0\) (which can be done, observed via the latter expression of (4.32)), it holds that

\(\frac{x'y}{\sqrt{D(x',y)}}\le Z(x,y).\)

Choosing \(x'\) arbitrarily close to \(x_y:=(1+\sqrt{y})^{-2}>0\), for which _D(x<sub>y</sub>,y_)=0, implies the result. □

**Proposition 4.11** (Unique interior maximizer and normalization)**.** _Let_<tbc>

\(g(\rho):=\alpha\rho\Phi(\rho),\rho\in(0,1).\)

<tbc>_Then g attains its maximum at a unique point_ \(\rho^*\in(0,1)\)_. If_ (_x_<sup>∗</sup>_,y_<sup>∗</sup>) _denotes the pair of parameters from Lemma 4.9 corresponding to_ \(\rho=\rho^*\)_, then_<tbc>

(4.33) \(Z(x^*,y^*)=1,\)

<tbc>_and consequently_

(4.34) \(\mathsf{R}(\alpha)=-\mathrm{log}x^*-\alpha\mathrm{log}y^*.\)

_Proof._ For each \(\rho\in(0,1)\), let \(x=x(\rho)\) and \(y=y(\rho)\) be the unique positive parameters given by Lemma 4.9. By (4.27),

(4.35) \(g(\rho)=\alpha\rho\mathrm{log}Z(x,y)-\mathrm{log}x-\alpha\mathrm{log}y.\)

We first compute \(g'(\rho)\). The Lagrange multipliers for the inner problem are<tbc>

\(\alpha_1=-\mathrm{log}x\text{and}\alpha_2=-\mathrm{log}y,\)

<tbc>corresponding respectively to the constraints<tbc>

\(\mathbb{E}_{\nu^*}[a]=\frac{1}{\alpha\rho},\mathbb{E}_{\nu^*}[b]=\frac{1}{\rho}.\)

<tbc>By the envelope theorem,<tbc>

\(\frac{d\Phi}{d\rho}=\alpha_1\frac{d(1/(\alpha\rho))}{d\rho}+\alpha_2\frac{d(1/\rho)}{d\rho}=\frac{\frac{1}{\alpha}\mathrm{log}x+\mathrm{log}y}{\rho^2}.\)

<tbc>Therefore,

(4.36) \(g'(\rho)=\alpha\Phi(\rho)+\alpha\rho\Phi'(\rho)=\alpha\big[\mathrm{log}Z-\frac{\frac{1}{\alpha}\mathrm{log}x+\mathrm{log}y}{\rho}\big]+\alpha\frac{\frac{1}{\alpha}\mathrm{log}x+\mathrm{log}y}{\rho}=\alpha\mathrm{log}Z(x(\rho),y(\rho)).\)

Next we compute \(x(\rho),y(\rho)\), and \(Z(x(\rho),y(\rho))\) explicitly. By Lemma 4.10,<tbc>

\(Z(x,y)=\frac{xy}{\sqrt{D(x,y)}},D(x,y):=(1-x-xy)^2-4x^2y.\)

<tbc>Hence<tbc>

\(\mathrm{log}Z(x,y)=\mathrm{log}x+\mathrm{log}y-\frac{1}{2}\mathrm{log}D(x,y).\)

<tbc>On the other hand, by the exponential family form of \(\nu^*\), we have

\(\mathbb{E}_{\nu^*}[a]=x\partial_x\mathrm{log}Z(x,y),\mathbb{E}_{\nu^*}[b]=y\partial_y\mathrm{log}Z(x,y).\)

