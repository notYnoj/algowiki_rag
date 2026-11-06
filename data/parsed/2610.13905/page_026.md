where \(|\alpha_j^t|=1/p\) for all \(1\le j\le p\) since \(\varepsilon_1,\dots,\varepsilon_p\) are roots of unity.

If _C=AB_ and <o>_C_</o> is the exact-arithmetic output of Algorithm 5 - i.e.,

\(\overline{C}=C+\left(\sum_{j=1}^r\alpha_j\varepsilon_j^r\right)R_r+\cdots+\left(\sum_{j=1}^r\alpha_j\varepsilon_j^{p-1}\right)R_{p-1},\) (4.13)

the previous lemma implies

\(\|\overline{C}-C\|=\left\|\left(\sum_{j=1}^r\alpha_j\varepsilon_j^r\right)R_r+\cdots+\left(\sum_{j=1}^r\alpha_j\varepsilon_j^{p-1}\right)R_{p-1}\right\|\le\left(\sum_{s=r}^{p-1}\sum_{j=1}^r|\alpha_j||\varepsilon_j|^s\right)\frac{(k/k_0^L)}{p}\left[\sum_{j=1}^pE(e^{2\pi ij/p})^L\right]\|A\|\|B\|=\left(\sum_{s=r}^{p-1}\sum_{j=1}^r|\varepsilon_j|^s\prod_{i\neq j}\frac{|\varepsilon_i|}{|\varepsilon_i-\varepsilon_j|}\right)\frac{(k/k_0^L)}{p}\left[\sum_{j=1}^pE(e^{2\pi ij/p})^L\right]\|A\|\|B\|.\text{(4.14)}\)

The key insight now is that Theorem 4.6, whose proof does not use the fact that the output of Algorithm 4 is the exact product of _A_ and _B_, can be used to bound the error in a floating-point implementation of Algorithm 5. That is, if \(\widehat{C}\) is the corresponding floating-point output (and assuming the same conditions as Theorem 4.6), then

\(\|\widehat{C}-C\|\le\|\widehat{C}-\overline{C}\|+\|\overline{C}-C\|\le(k/k_0^L)\left[\sum_{j=1}^r\left(\prod_{i\neq j}\frac{|\varepsilon_i|}{|\varepsilon_i-\varepsilon_j|}\right)(g(\delta_1,\delta_2)f(\varepsilon_j)\mathbf{u}+(g(\delta_1,\delta_2)-1))E(\varepsilon_j)^L\right]\|A\|\|B\|+O(\mathbf{u}^2)+\left(\sum_{s=r}^{p-1}\sum_{j=1}^r|\varepsilon_j|^s\prod_{i\neq j}\frac{|\varepsilon_i|}{|\varepsilon_i-\varepsilon_j|}\right)\frac{(k/k_0^L)}{p}\left[\sum_{j=1}^pE(e^{2\pi ij/p})^L\right]\|A\|\|B\|.\text{(4.15)}\)

This decomposes the error in Algorithm 5 as the sum of the loss of accuracy due to the truncation (term two) and the loss of accuracy due to floating-point arithmetic (term one). The latter can be made arbitrarily small by choosing _r_ and \(\varepsilon,\dots,\varepsilon_r\) appropriately. If, for example, we want

\(\sum_{s=r}^{p-1}\sum_{j=1}^r|\varepsilon_j|^s\prod_{i\neq j}\frac{|\varepsilon_i|}{|\varepsilon_i-\varepsilon_j|}=\Theta(\mathbf{u})\) (4.16)

so that (4.15) essentially implies (weak) forward stability for this algorithm, and additionally if we take \(\varepsilon_j=\beta\cdot e^{2\pi ij/r}\) for some \(0<\beta<1\) (ignoring the fact that this is not a floating-point number) then (4.16) reduces to

\(\sum_{s=r}^{p-1}\beta^s=\Theta(\mathbf{u}),\) (4.17)

which we can simplify further by noting

\(\sum_{s=r}^{p-1}\beta^s\le\sum_{s=r}^\infty\beta^s=\sum_{s=0}^\infty\beta^s-\sum_{s=0}^{r-1}\beta^s=\frac{1}{1-\beta}-\frac{1-\beta^r}{1-\beta}=\frac{\beta^r}{1-\beta}.\) (4.18)

Hence, it is sufficient to choose \(\beta\) and _r_ such that \(\frac{\beta^r}{1-\beta}=\Theta(\mathbf{u})\), a condition that we note is independent of _n_.

