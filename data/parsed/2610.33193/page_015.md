Note that we have defined two distinct ways to apply functions to distributions, reflecting whether the co-domain is a scalar or an entire distribution: \(\mathcal{L}_f(\mathcal{D})\in\mathbb{R}\) is an example of the former, and Definition 2.3, a new distribution resulting from applying the function _f_ to a sample, is an example of the latter. Our intended meaning should be clear based off the context. However, in general we will use capital letters such as S and L_<sub>f</sub>_ are functions that compute some property of the input distribution whereas lower case letters are used for mappings that define new distributions.

**Definition 2.4.** _The_ mutual information _between two random variables X,Y is given by:_

\(\mathcal{I}(X;Y)=\mathcal{S}(X)+\mathcal{S}(Y)-\mathcal{S}(X,Y).\)

**Definition 2.5** (Data processing inequality, \[CT06\])**.** _Let f be any function with domain D and_ D _be any distribution over D. Then_ \(\mathcal{S}(\mathcal{D})\ge\mathcal{S}(f(\mathcal{D}))\).

**Definition 2.6.** _The_ Kullback-Leibler divergence _between two distributions_ D _and_ \(\mathcal{D}'\) _is_<tbc>

\(D_\mathrm{KL}(\mathcal{D}||\mathcal{D}')=\mathbb{E}_{x\sim\mathcal{D}}\left[\mathrm{log}\frac{\mathrm{Pr}_\mathcal{D}[x]}{\mathrm{Pr}_{\mathcal{D}^\prime}[x]}\right].\)

<tbc>**Proposition 2.7** (Data processing inequality for KL divergence, \[CT06\])**.** _Let_ \(f:D\rightarrow R\) _be an arbitrary function and_ \(\mathcal{D},\mathcal{D}'\) _be two distributions over D. If_ \(\mathrm{supp}(\mathcal{D})\subseteq\mathrm{supp}(\mathcal{D}')\)_, then:_<tbc>

\(D_\mathrm{KL}(\mathcal{D}||\mathcal{D}')\ge D_\mathrm{KL}(f(\mathcal{D})||f(\mathcal{D}')).\)

<tbc>**Definition 2.8.** _If X and Y are random variables over D and R respectively, then the_ conditional _entropy of X given Y is_

\(\mathcal{S}(X|Y)=\sum_{x\in D,y\in R}\mathrm{Pr}[X=x,Y=y]\mathrm{log}\left(\frac{\mathrm{Pr}[Y=y]}{\mathrm{Pr}[X=x,Y=y]}\right)\)

.

**Proposition 2.9.** _If X is a random variable and f is a deterministic mapping, then_

\(\mathcal{S}(X|f(X))=\mathcal{S}(X)-\mathcal{S}(f(X))\)

.

**Proposition 2.10** (Gibbs’ Inequality)**.** _Let_ \(\mathcal{D},\mathcal{D}'\) _be two distributions over D. Then:_

\(D_\mathrm{KL}(\mathcal{D}||\mathcal{D}')\ge 0\)

_with equality only when_ \(\mathcal{D}=\mathcal{D}'\).

**Definition 2.11.** _Let_ \(f:D\rightarrow\mathbb{R}_{\ge 0}\cup\{\infty\}\) _be a function. We define the_ Gibbs distribution G_<sub>f</sub> over_ D _with respect to f, where for any_ \(x\in D\)_, (recall_ \(2^{-\infty}=0\))

\(\mathrm{Pr}_{\mathcal{G}_f}[x]=\frac{2^{-f(x)}}{\sum_{x^\prime\in D}2^{-f(x^\prime)}}.\)

We prove the following lemma in Appendix A.

