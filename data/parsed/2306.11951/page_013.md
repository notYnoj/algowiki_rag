## APPENDIX USEFUL LEMMAS

Here, we introduce several important lemmas.

**Lemma A.1** (Le Cam’s Two Point Lemma, see e.g. (Yu, 1997))**.** _For any_ \(\theta_0,\theta_1\in\Theta\)_, suppose that the following separation condition holds for some loss function_ \(L(\theta,a):\Theta\times\mathcal{A}\rightarrow\mathbb{R}\):<tbc>

\(\forall a\in\mathcal{A},L(\theta_0,a)+L(\theta_1,a)\ge\Delta>0.\)

<tbc>_Then we have_<tbc>

\(inf_fsup_\theta\mathbb{E}_\theta[L(\theta,f(X))]\ge\frac{\Delta}{2}\left(1-\mathsf{TV}(\mathbb{P}_{\theta_0},\mathbb{P}_{\theta_1})\right).\)

<tbc>**Lemma A.2** (Point vs Mixture, see e.g. (Ingster et al., 2003))**.** _For any_ \(\theta_0\in\Theta\), \(\Theta_1\subset\Theta\)_, suppose that the following separation condition holds for some loss function_ \(L(\theta,a):\Theta\times\mathcal{A}\rightarrow\mathbb{R}\):<tbc>

\(\forall\theta_1\in\Theta_1,a\in\mathcal{A},L(\theta_0,a)+L(\theta_1,a)\ge\Delta>0.\)

<tbc>_Then for any probability measure_ \(\mu\) _supported on_ \(\Theta_1\)_, we have_

\(inf_fsup_\theta\mathbb{E}_\theta[L(\theta,f(X))]\ge\frac{\Delta}{2}\left(1-\mathsf{TV}(\mathbb{P}_{\theta_0},\mathbb{E}_{\mu(d\theta)}[\mathbb{P}_{\theta_1}])\right).\)

**Lemma A.3** (Divergence Decomposition (Auer et al., 1995))**.** _Let T<sub>i</sub> be the random variable denoting the number of times experiment_ \(i\in[K]\) _is performed under some policy_ \(\pi\)_, then for two distributions_ \(\mathbb{P}^\pi,\mathbb{Q}^\pi\) _under policy_ \(\pi\),<tbc>

\(D_\mathsf{KL}(\mathbb{P}^\pi,\mathbb{Q}^\pi)=\sum_{i\in[K]}\mathbb{E}_{\mathbb{P}^\pi}[T_i]D_\mathsf{KL}(\mathbb{P}_i^\pi,\mathbb{Q}_i^\pi).\)

<tbc>**Lemma A.4** (An upper Bound of Bretagnolle-Huber inequality ((Bretagnolle and Huber, 1979), and Lemma 2.6 in Tsybakov (2004)))**.** _For any distribution_ P<sub>1</sub>,P<sub>2</sub>_, one has_<tbc>

\(\mathsf{TV}(\mathbb{P}_1,\mathbb{P}_2)\le 1-\frac{1}{2}\mathrm{exp}(-D_\mathsf{KL}(\mathbb{P}_1,\mathbb{P}_2)).\)

<tbc>**Lemma A.5.** _(Chi-Square divergence for mixture of distributions, see e.g. (Ingster et al., 2003)) Let_ \((P_\theta)_{\theta\in\Theta}\) _be a family of distributions parametrized by_ \(\theta\)_, and Q be any fixed distribution. Then for any probability measure_ \(\mu\) _supported on_ \(\Theta\)_, we have_

\(\chi^2(\mathbb{E}_{\theta\sim\mu}[P_\theta],Q)=\mathbb{E}_{\theta\sim\mu,\theta^\prime\sim\mu}\left[\sum_x\frac{P_\theta(x)P_{\theta^\prime}(x)}{Q(x)}\right]-1.\)

_Here_ \(\theta,\theta'\) _in the expectation are independent._

**Lemma A.6.** _\[Chernoff’s bound for Binomial random variables (Mitzenmacher and Upfal, 2017, Exercise 4.7)\] If_ \(X\sim\mathrm{Bin}(n,\frac{\Delta}{n})\)_, then for any_ \(\eta\in(0,1)\)_, we have_

\(\mathbb{P}(X\ge(1+\eta)\lambda)\le\left(\frac{e^\eta}{(1+\eta)^{(1+\eta)}}\right)^\lambda\) (2)

\(\mathbb{P}(X\le(1-\eta)\lambda)\le\left(\frac{e^{-\eta}}{(1-\eta)^{(1-\eta)}}\right)^\lambda\le e^{-\eta^2\lambda/2}.\) (3)

