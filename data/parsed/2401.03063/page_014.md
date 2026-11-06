Assume _L<sub>i</sub>_=2<sup>_i_-1</sup>, \(\lambda_i=1/n\). Then for any \(\theta\in(1/2^n,1)\), there exists \(i_0\in\{1,\dots,n\}\) such that \(1/2^{i_0}\le\theta\le 1/2^{i_0-1}\), and<tbc>

\(\left(\sum_{i=1}^n\lambda_iL_i\mathrm{e}^{-L_i\theta}\right)^{1/2}\ge\left(\lambda_{i_0}L_{i_0}\mathrm{e}^{-L_{i_0}\theta}\right)^{1/2}\ge\left(\frac{L_{i_0}\theta\mathrm{e}^{-L_{i_0}\theta}}{n\theta}\right)^{1/2}\ge\frac{\sqrt{2\mathrm{e}^{-2}}}{\sqrt{n\theta}},\)

<tbc>so

\(R\ge\frac{2\sqrt{\mathrm{e}^{-2}}}{\sqrt{n}}\int_{1/2^n}^1\frac{\mathrm{d}\theta}{\theta}\ge 2\sqrt{\mathrm{e}^{-2}}\mathrm{log}(2)\sqrt{n}\ge\frac{2\sqrt{\mathrm{e}^{-2}}}{\mathrm{log}(2)}\sqrt{\mathrm{max}_{i\in\{1,\dots,n\}}L_i}.\)

Thus in this case, \(\frac{I^2}{\sum_{i=1}^nd_i^2/L_i}\) is lower bounded by \(C\sigma(S)\), for some constant _C\>_0.

## 3 Further applications to some generic inequalities

### 3.1 Iterated gradients and Gaussian (in)equalities

It is well known that one can transfer the finite samples results of the previous section to functions of normal random variables, somehow reversing the analogies between iterated jackknives and iterated gradients first unveiled in \[9\]. This transfer is then followed by a study of the infinitely divisible framework and by the semigroup approach to these inequalities.

Let _Z_ be a standard random variable and _G_ be an absolutely continuous function. As well known, the Gaussian Poincaré inequality asserts that

\(\mathrm{Var}G(Z)\le\mathbb{E}\left(G'(Z)^2\right),\)

while in \[11\], this inequality is generalized with higher order gradients. Lemma 1.4 and Proposition 1.5 allows us to quickly recover Gaussian results. Indeed, e.g., see \[3\] in the case _k_=1, one can infer from the discrete decomposition of the variance a decomposition for Var_G(Z_).

**Lemma 3.1.** _Let G be a real-valued m-times continuously differentiable function, such that_ \(\mathbb{E}\left(G^{(k)}(Z)^2\right)<+\infty\)_, k_=0_,...,m. Let_ \(X_1,\dots,X_n,X'_1,\dots,X'_n\) _be independent Rademacher random variables and let_ \(S(X_1,\dots,X_n):=G\left(\frac{X_1+\cdots+X_n}{\sqrt{n}}\right)\)_. Then for all_ \(k\in\{1,\dots,m\}\),<tbc>

\(J_k(n)-\rightarrow_{n\rightarrow+\infty}\mathbb{E}\left(G^{(k)}(Z)^2\right)\text{\textit{and}}K_k(n)-\rightarrow_{n\rightarrow+\infty}\left(\mathbb{E}\left(G^{(k)}(Z)\right)\right)^2.\)

<tbc>_Proof._ It is enough to prove the theorem for _Gm_+1-times continuously differentiable with compact support. From (1.9), we have<tbc>

\(J_k=k!\genfrac(){pt}{2}{n}{k}D^{k-1}B_1,\)

<tbc>so (using (1.6)),<tbc>

\(J_k=k!\genfrac(){pt}{2}{n}{k}\mathbb{E}\frac{1}{2^kn!}\sum_{i\in\mathfrak{S}_n}\left(\Delta_{i_1,\dots,i_k}S\right)^2.\)

<tbc>By symmetry of the function \(S(X_1,\dots,X_n)=G\left(\frac{X_1+\cdots+X_n}{\sqrt{n}}\right)\), this simplifies to<tbc>

\(J_k=k!\genfrac(){pt}{2}{n}{k}\mathbb{E}\frac{1}{2^k}\left(\Delta_{1,\dots,k}S\right)^2.\) (3.1)

<tbc>For any \(i\in\{1,\dots,k\}\),<tbc>

\(\Delta_iS=(D_iS)2\mathbb{1}_{X_i=X_i^\prime}\)

<tbc>with<tbc>

\(D_iS(x):=\frac{S(x_1,\dots,x_i,\dots,x_n)-S(x_1,\dots,-x_i,\dots,x_n)}{2}.\)

