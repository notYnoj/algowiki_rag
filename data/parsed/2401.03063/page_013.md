**Theorem 2.4.** _Let_ \((E,\|\cdot\|_E)\) _be a Banach space of Rademacher type 2. Then there exists C=C(E)\>_0 _such that for any function S of the i.i.d. Rademacher random variables X_<sub>1</sub>_,...,X<sub>n</sub> taking values in E,_

\(\|S-\mathbb{E}S\|_{E,2}^2\le C\sigma(S)\sum_{i=1}^n\frac{\|D_iS\|_{E,2}^2}{1+\mathrm{log}\left(\frac{\|D_iS\|_{E,2}}{\|D_iS\|_{E,1}}\right)},\)

_where_ \(\sigma(S)=\mathrm{max}_{i\in\{1,\dots,n\}}\mathrm{log}\left(1+\mathrm{log}\left(\frac{\|D_iS\|_{E,2}}{\|D_iS\|_{E,1}}\right)\right)\).

It is still unclear whether or not the logarithmic term \(\sigma(S)\) is needed, but we now show how hypercontractivity can come short to removing it.

As noted in \[6\], one may apply (2.6) to _P<sub>t</sub>S_ instead of _S_ (for a fixed _t_), while the chain rule and semigroup properties give:

\(-\frac{\mathrm{d}P_{2t}S}{\mathrm{d}t}=\frac{2}{\sqrt{\mathrm{e}^{2t}-1}}\mathbb{E}_{\xi^\prime(t)}\left(\sum_{i=1}^n\delta'_i(t)D_iP_tS(\xi'(t)X)\right).\)

Hence, since _E_ is of Rademacher type 2, denoting by _K_ its constant, we get (see e.g. \[6, (57)\]):

\(\|S-\mathbb{E}S\|_{E,2}\le 4K\int_0^{+\infty}\left(\sum_{i=1}^n\|D_iP_tS\|_{E,2}^2\right)^{1/2}\frac{\mathrm{d}t}{\sqrt{\mathrm{e}^{2t}-1}}.\) (2.8)

We now show that in some cases hypercontractivity may not be enough to get rid of the factor \(\sigma(S)\). (A different (related?) approach for Boolean functions is presented in \[17\].) More precisely, let

\(I=\int_0^{+\infty}\left(\sum_{i=1}^n\|D_iS\|_{E,2}^2\left(\frac{\|D_iS\|_{E,1}}{\|D_iS\|_{E,2}}\right)^{2\frac{1-\mathrm{e}^{-2t}}{1+\mathrm{e}^{-2t}}}\right)^{1/2}\frac{\mathrm{d}t}{\sqrt{\mathrm{e}^{2t}-1}},\)

which is the upper bound on the right term of (2.8) one gets using hypercontractivity.

We let \(L_i=\mathrm{log}\left(\mathrm{e}\frac{\|D_iS\|_{E,2}}{\|D_iS\|_{E,1}}\right)\), \(d_i=\|D_iS\|_{E,2}\) and \(\theta(t)=\frac{1-\mathrm{e}^{-2t}}{1+\mathrm{e}^{-2t}}\), so<tbc>

\(I\sim\int_0^{+\infty}\left(\sum_{i=1}^nd_i^2\mathrm{e}^{-2L_i\theta(t)}\right)^{1/2}\frac{\mathrm{d}t}{\sqrt{\mathrm{e}^{2t}-1}}.\)

<tbc>With a change of variables,

\(I\sim\int_0^1\left(\sum_{i=1}^nd_i^2\mathrm{e}^{-2L_i\theta}\right)^{1/2}\frac{\mathrm{d}\theta}{\sqrt{\theta(1-\theta)}}\)<br>
\(\sim\int_0^{1/2}\left(\sum_{i=1}^nd_i^2\mathrm{e}^{-2L_i\theta}\right)^{1/2}\frac{\mathrm{d}\theta}{\sqrt{\theta}}+\frac{\mathrm{e}^{-1}}{\sqrt{2}}\int_{1/2}^1\frac{\mathrm{d}\theta}{\sqrt{1-\theta}}\sqrt{\sum_{i=1}^n\frac{d_i^2}{L_i}},\)

<tbc>so bounding \(\frac{I^2}{\sum_{i=1}^nd_i^2/L_i}\) (we already know it is bounded by \(\sigma(S)\)) is equivalent to bounding<tbc>

\(R:=\frac{\int_0^{1/2}\left(\sum_{i=1}^nd_i^2\mathrm{e}^{-2L_i\theta}\right)^{1/2}\frac{\mathrm{d}\theta}{\sqrt{\theta}}}{\sqrt{\sum_{i=1}^nd_i^2/L_i}}.\)

<tbc>Letting \(\lambda_i:=\frac{d_i^2/L_i}{\sum_{i=1}^nd_i^2/L_i}\), we get

\(R=\sqrt{2}\int_0^{1/2}\left(\sum_{i=1}^n\lambda_iL_i\mathrm{e}^{-L_i\theta}\right)^{1/2}\frac{\mathrm{d}\theta}{\sqrt{\theta}}.\)

