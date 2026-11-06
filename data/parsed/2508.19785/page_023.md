which is negative as soon as \(\rho>\frac{8pq+10(p-q)}{1-p-q}\) , as per our hypothesis.

The claim follows by using Hoeffding’s inequality:

\(Pr\left(\widetilde{X}\ge 0\right)=Pr\left(\widetilde{X}-\mathbb{E}[\widetilde{X}]\ge-\mathbb{E}[\widetilde{X}]\right)\le exp\left(-\frac{\mathbb{E}[\widetilde{X}]^2}{2(|I|-1)}\right)\le exp\left(-\frac{\mathbb{E}[\widetilde{X}]^2}{18w-2}\right)\)<br>
\(<exp\left(-w\cdot\frac{(\rho(1-p-q)-10(p-q)-8pq)^2}{4\cdot 18}\right)=exp\left(-w\cdot\kappa(p,q,\rho)\right).\) □

Lemma 5.8. _Consider two elements_ \(x\in B_i\) _and_ \(y\in B\backslash\{x\}\) _such that_ \(y\notin I_M\) _and y\<x (resp. y\>x). If all elements in B_<sup>+</sup> _are good and all elements in B are happy, then the probability that_ \(\text{score}(x)\le\text{score}(y)\) _(resp._ \(\text{score}(x)\ge\text{score}(y)\)_) is at most_ \(exp\left(-w\cdot\kappa(p,q,\rho)\right)\).

Proof. We focus on the case _y\<x_ since the complementary case is symmetric.

Let the random variables _X<sub>z</sub>_ and \(\widetilde{X}_z\) for \(z\in I\backslash\{y\}\) be defined as in the proof of Lemma 5.7 so that \(\text{score}(y)-\text{score}(y)=\sum_{z\in B\backslash\{y\}}X_z\le\sum_{z\in I_M}\widetilde{X}_z+\sum_{z\in I_L\cup I_R\backslash\{y\}}\widetilde{X}_z\).

Notice that, since \(y\notin I_M\) and all elements in _B_ are good, we have \(y\le(i-3)w\) and \(x\ge(i-1)w+1-w=(i-2)w+1\) and hence there are at least _w_ elements _z_ such that _y\<z\<x_. Since the same bounds of Lemma 5.7 apply for E\[_X<sub>z</sub>_\] when \(z\in I_m\), we have:<tbc>

\(\mathbb{E}\left[\sum_{z\in I_M}\widetilde{X}_z\right]\le(x-y)\cdot(2p-1)+(|I_M|-(x-y))\cdot(p-q)\le w(2p-1)+4w(p-q).\)

<tbc>We now consider the elements \(z\in(I_L\cup I_R)\backslash\{y\}\). If _z\<y_ or _z\>x_, then \(Pr(\widetilde{X}_z=1)=pq\le p^2\). If _y\<z\<x_, then \(Pr(\widetilde{X}_z=1)=p_{\{z,y\}}p_{\{z,x\}}\le p^2\). Thus, we have \(\mathbb{E}[\sum_{z\in(I_L\cup I_R)}\widetilde{X}_z]\le 4wp^2\) and, defining \(\widetilde{X}=\sum_{z\in I\backslash\{y\}}\widetilde{X}_z\), we obtain:

\(\mathbb{E}[\widetilde{X}]\le w(2p-1)+4w(p-q)+4wp^2=-\frac{w}{2}\left(2(1-2p)-8(p-q)-8p^2\right)\)<br>
\(\le-\frac{w}{2}\left(\rho(1-2p)-10(p-q)-8p^2+2(p-q)\right)\le-\frac{w}{2}\left(\rho(1-2p)-10(p-q)-8pq\right),\)

where we used -8_p_<sup>2</sup>+2(_p-q)\>8pq_ for \(q\le p<\frac{1}{4}\), which follows from observing that, whenever \(p\ge q\ge\frac{1}{4}\), we have \(\frac{8pq+10(p-q)}{1-p-q}\ge 1\) and that this inequality violates the hypothesis on the value of \(\rho\). Then, \(\mathbb{E}[\widetilde{X}]<0\) since \(\rho>\frac{8pq+10(p-q)}{1-p-q}\) .

The claim follows by applying Hoeffding’s inequality on \(\widetilde{X}\) similarly to the corresponding part in the proof of Lemma 5.7. □

The following lemma provides a sufficient condition for \(\tau_w(x)\) to be a good approximation of rank(_x,S<sub>w</sub>_)=_x_.

Lemma 5.9. _Consider an element_ \(x\in B_i\)_. If all elements in B_<sup>+</sup> _are good and all elements in B are happy, then_ \(|x-\tau_w(x)|\le\rho\cdot\frac{w}{2}\) _with probability at least_ \(1-9w\cdot exp\left(-w\cdot f\left(p,\rho\right)\right)\).

Proof. By construction (see Line 10 of Algorithm 2), \(\tau_w(x)=max\{0,i-4\}\cdot w+pos(x,A)\), and, since _x_ is happy, \(x=max\{0,i-4\}\cdot w+rank(x,B)\). Therefore, we have \(|x-\tau_w(x)|=|rank(x,B)-pos(x,A)|\).

Lemmas 5.7 and 5.8 ensure that, for any element \(y\in B\) with \(y\le x-\rho\cdot\frac{w}{2}\) (resp. \(y\ge x+\rho\cdot\frac{w}{2}\) ), the probability that score(_y)\<_score(_x_) (resp. score(_y)\>_score(_x_)) does not hold is at most \(exp(-w\cdot\kappa(p,q,\rho))\). Using the union bound over all the (at most 9_w_) elements \(y\in B\), we have that all elements \(y\in B\) with \(|x-y|>\rho\frac{w}{2}\) are in the correct relative order w.r.t. _x_ in _A_ with probability at least<tbc>

