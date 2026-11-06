<tbc>**Remark 2.4.** A weaker version of Theorem 1.1 in which all inequalities are non-strict now follows. Indeed, since the sequence \(\frac{1}{N}logZ_{X^\prime,Y}\) is uniformly bounded, it follows that

(2.15) \(f_\mathrm{null}(\alpha)=\mathrm{lim}_{N\rightarrow\infty}\mathbb{E}\left[\frac{1}{N}logZ_{X^\prime,Y}\right]\le^{(\mathrm{Jensen})}\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}log\mathbb{E}\left[Z_{X^\prime,Y}\right]=f_\mathrm{null}^\mathrm{ann}(\alpha).\)

Towards proving the other non-strict inequality, we let \(\sigma^*\in\Sigma_{N,M}\) denote the planted embedding, so that

(2.16) \(Y=X_{\sigma^*}.\)

We let \(x\in\{0,1\}^M\) be an independent uniform random binary string. For \(z\in\mathbb{N}\), via explicitly pinning down the collection _A_ of _M_-subsequences of _X_ corresponding to embeddings of _Y_ , we can write

\(\mathbb{P}\left(Z_{X,Y}=z\right)=\mathbb{E}_{\sigma^*,X}\left[\sum_{A\subseteq\genfrac(){pt}{2}{[N]}{M}:|A|=z}\unknown\left\{X|_S=Y\text{for all}S\in A;X|_S\neq Y\text{for all}S\notin A\right\}\right]\)<br>
\(=2^M\mathbb{E}_{\sigma^*,X,x}\left[\sum_{A\subseteq\genfrac(){pt}{2}{[N]}{M}|A|=z}\unknown\left\{X|_S=x\text{for all}S\in A;X|_S\neq x\text{for all}S\notin A\right\}\unknown\left\{Y=x\right\}\right]\)<br>
\(=^{(\mathrm{2}.16)}\frac{2^M}{\genfrac(){pt}{2}{N}{M}}\mathbb{E}_{X,x}\left[\sum_{\sigma^*\in\Sigma_{N,M}}\sum_{A\subseteq\genfrac(){pt}{2}{[N]}{M}|A|=z}\unknown\left\{X|_S=x\text{for all}S\in A;X|_S\neq x\text{for all}S\notin A\right\}\unknown\left\{X_{\sigma^*}=x\right\}\right]\)<br>
\(=\frac{2^M}{\genfrac(){pt}{2}{N}{M}}\mathbb{E}_{X,x}\left[Z_{X,x}\cdot\unknown\left\{Z_{X,x}=z\right\}\right]=\frac{2^M}{\genfrac(){pt}{2}{N}{M}}\mathbb{E}\left[Z_{X^\prime,Y}\cdot\unknown\left\{Z_{X^\prime,Y}=z\right\}\right].\) (2.17)

We remark that the above calculation is an application of Nishimori’s identity. Indeed, the planted law is obtained from the null law by reweighting with the partition function. Concretely, the distribution of _Z<sub>X,Y</sub>_ under the planted model is the \(Z_{X^\prime,Y}\)-size-biased tilt of its distribution under the null model. Altogether, we conclude that

\(\mathbb{E}\left[logZ_{X,Y}\right]=\sum_{z\ge 0}logz\cdot\mathbb{P}\left(Z_{X,Y}=z\right)=^{(\mathrm{2}.17)}\frac{2^M}{\genfrac(){pt}{2}{N}{M}}\sum_{z\ge 0}logz\cdot\mathbb{E}\left[Z_{X^\prime,Y}\cdot\unknown\left\{Z_{X^\prime,Y}=z\right\}\right]\)<br>
\(=\frac{2^M}{\genfrac(){pt}{2}{N}{M}}\mathbb{E}\left[Z_{X^\prime,Y}logZ_{X^\prime,Y}\right]\ge^{(\mathrm{Jensen})}\frac{2^M}{\genfrac(){pt}{2}{N}{M}}\mathbb{E}\left[Z_{X^\prime,Y}\right]log\mathbb{E}\left[Z_{X^\prime,Y}\right]=log\mathbb{E}\left[Z_{X^\prime,Y}\right].\) (2.18)

We establish that the Jensen gaps in (2.15) and (2.18) are nontrivial in forthcoming sections. \(\triangleup\)

## 3. Proof of the Quenched-Annealed Gaps

### 3.1. Definitions and notation.

We begin by recording the conventions that will remain in force unless explicitly stated otherwise. Throughout, lowercase letters, such as \(x\in\{0,1\}^N\) and \(y\in\{0,1\}^M\), denote deterministic binary strings to distinguish them from random strings, which are denoted using uppercase letters. We also fix the density parameter \(\alpha\in(0,1)\) and the block length \(b\in\mathbb{N}\). The quantity \(\alpha b\) should be interpreted as the typical block length of an _x-random string_, i.e., a uniformly chosen length-_M_ subsequence of _x_. In particular, in the planted variant of the Random Subsequence Model, _Y_ is an _X_-random

