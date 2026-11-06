### 3.5.2. _Explicit capacity lower bound._

We now revisit the proof of Theorem 1.1, keeping track of constants in order to obtain an explicit strictly positive lower bound on _C_<sub>unif</sub>(_p_). Towards this end, for \(\alpha\in(0,1)\), we define the quantity

\(\kappa(\alpha):=\left\lceil\frac{1920^{96}}{\alpha^{24}\beta(\alpha)^{96}(1-\alpha)^{12}}\right\rceil.\)

We stress that we do not attempt to optimize the resulting bound; our objective is simply to extract a fully explicit positive capacity lower bound for uniform random codebooks in the likely deletion regime.

**Theorem 3.13** (Explicit capacity lower bound)**.** _For_ \(p\in(0,1)\)_, we have that_

\(C_\mathrm{unif}(p)\ge\frac{\left(\beta(1-p)\right)^3}{51200\cdot\left(\kappa(1-p)\right)^5}>0.\)

Since the proof of Theorem 3.13 mainly consists of verifying a collection of routine inequalities and parameter constraints, we defer it to Appendix D.

## 4. Annealed Free Energy Under the Planted Model

In this section, we derive an exact formula for the _annealed free energy_ of the planted model,

\(f_\mathrm{pl}^\mathrm{ann}(\alpha)=\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}\mathrm{log}\mathbb{E}\left[Z_{X,Y}\right],\)

which by Jensen gives an upper bound on \(f_\mathrm{pl}(\alpha)\). We note that \[PIW24\] gave an efficient algorithm to approximate \(f_\mathrm{pl}^\mathrm{ann}(\alpha)\) to any desired precision. Here we improve on their result by proving Theorem 1.3 and giving an exact asymptotic formula.

It will be convenient for us to identify sets \(S\in\genfrac(){pt}{2}{[N]}{M}\) with functions \(\sigma\in\Sigma=\Sigma_{N,M}\) such that \(\mathrm{Im}(\sigma)=S\). Moreover, for \(\sigma,\tau\in\Sigma\), we use the notations

\(I(\sigma,\tau)=\{j\in[M]:\sigma_j=\tau_j\};\)<br>
\(\langle\sigma,\tau\rangle=\sum_{j=1}^M\unknown\{\sigma_j=\tau_j\}=|I(\sigma,\tau)|.\)

Given a string \(X\in\{0,1\}^N\), we use the notation<tbc>

\(X_\sigma:=X|_{\mathrm{Im}(\sigma)}.\)

<tbc>Note that we have<tbc>

\(\mathbb{E}\left[Z_{X,Y}\right]=\frac{1}{\genfrac(){pt}{2}{N}{M}}{\genfrac(){pt}{2}{N}{M}}\sum_{\sigma,\tau\in\Sigma}\mathbb{P}\left(X_\sigma=X_\tau\right)=\frac{1}{\genfrac(){pt}{2}{N}{M}}\sum_{\sigma,\tau\in\Sigma} 2^{-\left(M-\langle\sigma,\tau\rangle\right)}=\frac{1}{\genfrac(){pt}{2}{N}{M}2^M}\sum_{\sigma,\tau\in\Sigma} 2^{\langle\sigma,\tau\rangle}.\)

<tbc>Hence, to prove Theorem 1.3, it suffices to show that, letting<tbc>

\(\overline{Z}=\sum_{\sigma,\tau\in\Sigma} 2^{\langle\sigma,\tau\rangle},\)

<tbc>we have

(4.1) \(\mathrm{lim}_{M\rightarrow\infty}\frac{1}{N}\mathrm{log}\overline{Z}=-\mathrm{log}x_\alpha-\alpha\mathrm{log}y_\alpha.\)

The remainder of Section 4 proves (4.1) and hence Theorem 1.3. We begin from the elementary identity

\(2^{\langle\sigma,\tau\rangle}=\sum_{J\subseteq I(\sigma,\tau)}1=\sum_{\ell=0}^M\sum_{J\in\genfrac(){pt}{2}{[M]}{\ell}}\unknown\{J\subseteq I(\sigma,\tau)\}.\)

