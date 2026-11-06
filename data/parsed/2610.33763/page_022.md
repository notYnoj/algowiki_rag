It is evident that, for \(\vartheta=0\), the exponential tempering disappears and the tempered fractional derivatives reduce to the classical R-LFDs.<br>
Another widely used definition is the Caputo fractional derivative (CFD), introduced by the Italian mathematician Michele Caputo \[105\], which is defined as follows.

**Definition 1.6** _\[105\] Let_ \(\xi\in(n-1,n)\), \(n\in\mathbb{N}^+\)_, and assume that the n<sup>th</sup> derivative of u(z_) _is absolutely integrable, then the left- and right-sided CFDs of order_ \(\xi\) _are defined as_

\(^C\mathcal{D}_{a_{+,z}}^\xi u(z)=\frac{1}{\Gamma(n-\xi)}\int_a^z\frac{1}{(z-\sigma)^{\xi-n+1}}\frac{d^nu(\sigma)}{d\sigma^n}d\sigma,\) (1.5)

\(^C\mathcal{D}_{b_{-,z}}^\xi u(z)=\frac{(-1)^n}{\Gamma(n-\xi)}\int_z^b\frac{1}{(\sigma-z)^{\xi-n+1}}\frac{d^nu(\sigma)}{d\sigma^n}d\sigma.\) (1.6)

**Remark 1.1** \[74\] If \(\xi\notin\mathbb{N}\) and _u(x_) are such that the Caputo and R-LFDs exist then they are linked through the following relation

\(\mathcal{D}_{a_{+,z}}^\xi u(z)=^C\mathcal{D}_{a_{+,z}}^\xi u(z)+\sum_{i=0}^{n-1}\frac{(z-a)^{i-\xi}}{\Gamma(i-\xi+1)}\frac{d^iu(a)}{dz^i},\)<br>
\(\mathcal{D}_{b_{-,z}}^\xi u(z)=^C\mathcal{D}_{b_{-,z}}^\xi u(z)+\sum_{i=0}^{n-1}\frac{(-1)^i(b-z)^{i-\xi}}{\Gamma(i-\xi+1)}\frac{d^iu(b)}{dz^i}.\)

In the case where \(\frac{d^iu(a)}{dz^i}=\frac{d^iu(b)}{dz^i}=0\), then the R-LFDs (1.3) and (1.4) coincide with the CFDs (1.5) and (1.6).

A tempered extension of the CFD has been introduced to account for finite memory effects through exponential damping. This formulation, known as the Caputo tempered fractional derivative, combines the regularity advantages of the CFD with the flexibility of tempered fractional operators and is defined as follows \[4, 110\].

**Definition 1.7** _\[4, 110\] Let_ \(\xi\in(n-1,n)\), \(n\in\mathbb{N}^+\), \(\vartheta\ge 0\) _and let_ \(u(z)\in AC([a,b])\)_. Then, the left- and right-sided Caputo tempered fractional derivatives are defined as_

\(^C\mathcal{D}_{a_{+,z}}^\xi u(z)=\frac{\mathrm{e}^{-\vartheta\mathrm{z}}}{\Gamma(n-\xi)}\int_a^z\frac{1}{(z-\sigma)^{\xi-n+1}}\frac{d^n\left(\mathrm{e}^{\vartheta\sigma}\mathrm{u}(\sigma)\right)}{d\sigma^n}d\sigma,\)<br>
\(^C\mathcal{D}_{b_{-,z}}^\xi u(z)=\frac{(-1)^n\mathrm{e}^{\vartheta z}}{\Gamma(n-\xi)}\int_z^b\frac{1}{(\sigma-z)^{\xi-n+1}}\frac{d^n\left(\mathrm{e}^{-\vartheta\sigma}\mathrm{u}(\sigma)\right)}{d\sigma^n}d\sigma.\)

## 1.2 Mittag-Leffler type functions

This section is devoted to the introduction of the multinomial MLF and to the presentation of its key analytical properties, which will be used throughout the subsequent analysis.

**Definition 1.8** _\[82\] For_ \(\xi_i,\gamma>0,z_i\in\mathbb{C},i=1,2,\dots,n,n\in\mathbb{N}\)_, the multinomial MLF is defined as_

\(E_{(\xi_1,\xi_2,\dots,\xi_n),\gamma}(z_1,z_2,\dots,z_n):=\sum_{k=0}^\infty\sum_{l_1+l_2+\dots+l_n=kl_1\ge 0,\dots,l_n\ge 0}(k;l_1,\dots,l_n)\frac{\prod_{i=1}^nz_i^{l_i}}{\Gamma\left(\gamma+\sum_{i=1}^n\xi_il_i\right)},\)

