requirement turns out to be too strict for our analysis of the total dislocation. We therefore relax such requirement in a way that is convenient for the sequel. Formally, given an element \(x\in S\) and a window size _w_, we say that _x_ is _happy_ if _x_ is larger than all the elements lying apart by more than 2_w_ positions on the left of _x_ in _S<sub>w</sub>_ and _x_ is smaller than all the elements lying apart by more than 2_w_ positions on the right of _x_ in _S<sub>w</sub>_. Notice that an element can be any combination of happy and/or good; however, if all elements are good, then they are also all happy (the converse is not necessarily true).

Fix a window size _w_ and a basket _B<sub>i</sub>_ (of _S<sub>w</sub>_). Consider the union _B_ (resp. _B_<sup>+</sup>) of _B<sub>i</sub>_ with the 3 (resp. 6) closest buckets to its left and to its right, if they exist. Formally, \(B=\bigcup_{j=max\{1,i-3\}}^{min\{i+3,\lceil m/w\rceil\}}B_j\) (which matches the definition in the pseudocode of `BasketSort`) and \(B^+=\bigcup_{j=max\{1,i-6\}}^{min\{i+6,\lceil m/w\rceil\}}B_j\). In other words, _B_ contains all elements _x_ with \(\sigma_w(x)\in\{(i-4)w+1,\dots,(i+3)w\}\) and _B_<sup>+</sup> contains all the elements _x_ with \(\sigma_w(x)\in\{(i-7)w+1,\dots,(i+6)w\}\).

Lemma 5.6. _If all elements in B_<sup>+</sup> _are good and all elements in B are happy, then_ {(_i_-3)_w_+1_,...,_(_i_+2)_w_} \(\subseteq B\subseteq\{(i-5)w+1,\dots,(i+4)w\}\).

Proof. We start by proving \(\{(i-3)w+1,\dots,(i+2)w\}\subseteq B\). Let \(x\in\{(i-3)w+1,\dots,(i+2)w\}\). If \(x\in B^+\) then _x_ is good and \(x+(i-4)w+1\le x-w\le\sigma_w(x)\le x+w\le(i+3)w\), which implies \(x\in B\).

The complementary case \(x\notin B^+\) cannot happen, as shown by the following two sub-cases. If \(x\notin B^+\) and \(\sigma_w(x)\le(i-7)w\), let _y_ be the first element of _B_, i.e., \(\sigma_w(y)=(i-4)w+1\). Since _y_ is good, we must have \(|y-((i-4)w+1)|\le w\) and hence \(y\le(i-3)w+1\le x\). However, since _y_ is happy and \(\sigma_w(y)-\sigma_w(x)>2w\), we must have _x\<y_, which is impossible.

If \(x\notin B^+\) and \(\sigma_w(x)>(i+6)w\), let _z_ be the last element of _B_, i.e., \(\sigma_w(z)=(i+3)w\). Since _z_ is good, we must have \(|(i+3)w-z|\le w\) and hence \(z\ge(i+2)w\ge x\). However, since _z_ is happy and \(\sigma_w(x)-\sigma_w(z)>2w\), we must have _z\<x_, which is impossible.

We now prove \(B\subseteq\{(i-5)w+1,\dots,(i+4)w\}\). For \(x\in B\), it trivially holds that \(0\le x\le m\) and, since _x_ is good, \(|x-\sigma_w(x)|\le w\), which implies \((i-5)w+1\le\sigma_w(x)-w\le x\le\sigma_w(x)+w\le(i+4)w\). □

For the following lemmas, it is convenient to define the quantity

\(\kappa\left(p,q,\rho\right)=\frac{(\rho(1-p-q)-10(p-q)-8pq)^2}{72},\)

which depends on the constants _p_ and _q_ and on the choice of \(\rho\). Notice that, since \(\rho\in\left(\frac{8pq+10(p-q)}{1-p-q},1\right)\) by hypothesis, we always have \(\kappa(p,q,\rho)\in(0,\frac{1}{3})\). We also let \(I=S\cap\{(i-5)w+1,\dots,(i+4)w\}\), and we partition _I_ into three subsets _I<sub>L</sub>_, _I<sub>M</sub>_ and _I<sub>R</sub>_, defined as \(I_L=S\cap\{(i-5)w+1,\dots,(i-3)w\}\), \(I_M=S\cap\{(i-3)w+1,\dots,(i+2)w\}\), and \(I_R=S\cap\{(i+2)w+1,\dots,(i+4)w\}\).

Lemma 5.7. _Consider two elements_ \(x\in B_i\) _and_ \(y\in B\backslash\{x\}\) _such that_ \(y\le x-\rho\frac{w}{2}\) _(resp._ \(y\ge x+\rho\frac{w}{2}\) _) and_ \(y\in I_M\)_. If all elements in B_<sup>+</sup> _are good and all elements in B are happy, then the probability that_ \(\mathrm{score}(x)\le\mathrm{score}(y)\) _(resp._ \(\mathrm{score}(x)\ge\mathrm{score}(y)\)_) is at most_ \(\mathrm{exp}(-w\cdot\kappa(p,q,\rho))\).

Proof. We will only analyze the case \(y\le x-\rho\frac{w}{2}\) , as the complementary case \(y\ge x+\rho\frac{w}{2}\) is symmetric.

In order to compare score(_x_) with score(_y_), we study how the outcome of the comparison between _x_ and each element \(z\in I\backslash\{x,y\}\) differs from the outcome of the comparison between _y_ and _z_. To this aim, we encode the differences in the comparison results using a collection of random<tbc>

