<tbc>We now consider the second summand of (C.8). We proceed under the further assumption on _x_ that

(C.9) \(\frac{|\mathcal{I}_x|}{B}\left(\frac{1+\beta(\alpha)}{2}\right)<\frac{1}{2}+\frac{\beta(\alpha)}{4}\Longleftrightarrow|\mathcal{I}_x^c|>B\left(1-\frac{\frac{1}{2}+\frac{\beta(\alpha)}{4}}{\frac{1}{2}+\frac{\beta(\alpha)}{2}}\right)=B\left(\frac{\beta(\alpha)}{2\left(1+\beta(\alpha)\right)}\right)=\Omega(N),\)

as if this assumption fails and (C.8) holds, then it is clear that<tbc>

\(T_\mathrm{ind}(x,Z)\ge^\text{(C.8)}\frac{|\mathcal{I}_x|}{B}\left(\frac{1+\beta(\alpha)}{2}\right)\ge\frac{1}{2}+\frac{\beta(\alpha)}{4}\ge\frac{1}{2}+\beta^\star(\alpha).\)

<tbc>A similar argument as that for the first summand in (C.6) (with the modification that we take the analogues of (C.5) to have mean _b/_2 instead) yields that for large _b_, it holds uniformly over \(i\notin\mathcal{I}_x\) that<tbc>

\(\mathbb{P}\left(A_\mathrm{loc}\big(x^{(i)},Z^{(i)}\big)=1\right)\ge\frac{1}{2}-\frac{\beta(\alpha)}{72}.\)

<tbc>Then by a similar application of Hoeffding’s inequality as in (C.7), it holds that

(C.10) \(\mathbb{P}\left(\frac{1}{|\mathcal{I}_x^c|}\sum_{i\notin\mathcal{I}_x}A_\mathrm{loc}\big(x^{(i)},Z^{(i)}\big)\le\frac{1}{2}-\frac{\beta(\alpha)}{36}\right)=^\text{(C.9)}e^{-\Omega(N)}.\)

Therefore, we conclude that with probability \(1-e^{-\Omega(N)}\),

\(T_\mathrm{ind}(x,Z)\ge^\text{(C.8)}\frac{|\mathcal{I}_x|}{B}\left(\frac{1+\beta(\alpha)}{2}\right)+\frac{1}{B}\sum_{i\notin\mathcal{I}_x}A_\mathrm{loc}\big(x^{(i)},Z^{(i)}\big)\)<br>
\(=\frac{|\mathcal{I}_x|}{B}\left(\frac{1+\beta(\alpha)}{2}\right)+\frac{|\mathcal{I}_x^c|}{B}\left(\frac{1}{|\mathcal{I}_x^c|}\sum_{i\notin\mathcal{I}_x}A_\mathrm{loc}\big(x^{(i)},Z^{(i)}\big)\right)\)<br>
\(\ge^\text{(C.10)}\frac{|\mathcal{I}_x|}{B}\left(\frac{1+\beta(\alpha)}{2}\right)+\frac{|\mathcal{I}_x^c|}{B}\left(\frac{1}{2}-\frac{\beta(\alpha)}{36}\right)=\frac{1}{2}+\left(\frac{|\mathcal{I}_x|}{B}\cdot\frac{\beta(\alpha)}{2}-\frac{|\mathcal{I}_x^c|}{B}\cdot\frac{\beta(\alpha)}{36}\right)\)<br>
\(\ge^\text{(C.3)}\frac{1}{2}+\left(\frac{\beta(\alpha)}{20}-\frac{\beta(\alpha)}{40}\right)=\frac{1}{2}+\frac{\beta(\alpha)}{40}=\frac{1}{2}+\beta^\star(\alpha).\)

Altogether, we conclude that

\(\mathbb{P}_x\big(\mathcal{A}(x)^c\big)=\mathbb{P}\left(Z\notin\mathcal{A}(x)\right)=\mathbb{P}\left(T_\mathrm{ind}(x,Z)<1/2+\beta^\star(\alpha)\right)=e^{-\Omega(N)}.\)

The uniformity of the guarantee over typical \(x\in\{0,1\}^N\) is now a consequence of the fact that the preceding argument did not depend on the particular choice of typical _x_. □

## Appendix D. Proof of Theorem 3.13

_Proof._ We begin by fixing auxiliary parameters \(\epsilon\) and _b_ for which the argument goes through. Throughout this section we take

\(\epsilon=1/24.\)

We also record the following quantitative Berry-Esseen bound for later use.

**Theorem D.1** (\[Zol67, Theorem 1\])**.** _Let_ \(\xi_1,\dots,\xi_n\) _be independent random variables with mean zero, vari ances_ \(\sigma_1^2,\dots,\sigma_n^2\)_, and finite absolute third moments_ \(\beta_1,\dots,\beta_n\)_. Let F denote the distribution function of_ \(\sum_{k=1}^n\xi_k/\sqrt{\sum_{k=1}^n\sigma_k^2}\)_. Then_

\(\mathrm{sup}_x|F(x)-\Phi(x)|\le\frac{\sum_{k=1}^n\beta_k}{\left(\sum_{k=1}^n\sigma_k^2\right)^{3/2}}.\)

