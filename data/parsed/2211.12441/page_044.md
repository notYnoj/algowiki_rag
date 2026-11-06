\(=\mathrm{cos}(bx)+\mathrm{cot}(kx)\mathrm{sin}(bx).\)

<tbc>Of course, \(\mathrm{cos}(bx)\le 1\). Furthermore, from Claim 62 and Claim 63, we can see that in this domain of _x_, \(\mathrm{sin}(bx)\le bx-\frac{b^3x^3}{\pi^2}\) and \(\mathrm{cot}(kx)\le\frac{1}{kx}\). Additionally, \(\mathrm{sin}(bx)\ge 0\). Therefore, using the fact that \(k\le b\),

\(\frac{k}{b+k}\cdot\frac{\mathrm{sin}((b+k)x)}{\mathrm{sin}(kx)}\le\frac{k}{b+k}\left(1+\frac{1}{kx}\left(bx-\frac{b^3x^3}{\pi^2}\right)\right)\)<br>
\(\le 1-\frac{b^3}{(b+k)\pi^2}x^2\le 1-\frac{b^2}{2\pi^2}x^2.\)

From this, we can now prove Lemma 60.

_Proof._ Recall that on this interval<tbc>

\(|\varphi_{a,b}(2t)|=\prod_{k=1}^a\frac{k}{b+k}\cdot\frac{\mathrm{sin}((b+k)t)}{\mathrm{sin}(kt)}.\)

<tbc>Claim 61 applies on all _t_ in the domain because \(\pi/(b+a)\le\pi/(b+k)\) for all _k_.

Therefore,

\(\int_0^\frac{\pi}{a+b}|\varphi_{a,b}(2t)|dt\le\int_0^\frac{\pi}{a+b}\left(1-\frac{b^2t^2}{2\pi^2}\right)^adt\le\int_0^\frac{\pi}{a+b}\mathrm{exp}\left(-\frac{ab^2t^2}{2\pi^2}\right)dt=O\left(\frac{1}{b\sqrt{a}}\right).\)

Here, we use the fact that \(1-x\le\mathrm{exp}(-x)\) for all _x_, and the Gaussian integral: the integral of exp(-_t_<sup>2</sup>) over R is constant, and by scaling the argument, the integral of exp(-_ct_<sup>2</sup>) over R is a constant factor of _c_<sup>-1/2</sup> for any parameter _c_.

## 9.3 Peripheral bound

We now bound \(|\varphi_{a,b}(t)|\) in the region away from 0, namely, the interval \([2\pi/(a+b),\pi]\). As for the other part of the integral on the right-hand side of (35), we substitute _t_ with 2_t_ in order to avoid the denominator of 2 in the sine terms of the integrand.

**Lemma 64 (peripheral bound).** _For integers_ \(b\ge a\ge 2\),

\(\int_\frac{2\pi}{a+b}^\pi|\varphi_{a,b}(t)|dt=2\int_\frac{\pi}{a+b}^\frac{\pi}{2}|\varphi_{a,b}(2t)|dt=O\left(\frac{1}{b\sqrt{a}}\right).\)

In this region, the main problem is that the denominator of \(|\varphi_{a,b}(2t)|\) often goes to zero, which could potentially blow up the integrand. However, the terms in the numerator always cancel out these blowups. The following lemma will be our main tool for bounding \(|\varphi_{a,b}(2t)|\) in this region; it will allow terms in the numerator to cancel out bad terms in the denominator.

**Lemma 65 (pole reduction).** _For every_ \(t\in\mathbb{R}\)_, there exists a bijection_ \(\beta_t:\{1,\dots,a\}\rightarrow\{b+1,\dots,b+a\}\) _(depending on t) such that for every k_=1_,...,a,_<tbc>

\(\left|\frac{1}{k}\mathrm{sin}(kt)\right|\ge\left|\frac{1}{\beta_t(k)}\mathrm{sin}(\beta_t(k)t)\right|.\)

