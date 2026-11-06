The above indicates that the difference between the variance and each partial sum is squeezed between the Cauchy-Schwarz inequality. We may also get equalities, when _G_ is infinitely differentiable, with additional conditions. Indeed,

**Corollary 3.3.** _Let G be a real-valued infinitely-differentiable function, such that, for all_ \(k\ge 0\), \(\mathbb{E}(G^{(k)}(Z))^2<+\infty\)_. Then,_<tbc>

\(\text{\textit{Var}}G(Z)=\sum_{i=1}^{+\infty}(-1)^{i-1}\frac{\mathbb{E}\left(G^{(i)}(Z)^2\right)}{i!},\)

<tbc>_if and only if_ \(lim_{k\rightarrow\infty}\mathbb{E}(G^{(k)}(Z))^2/k!=0\)_, and under such a condition,_<tbc>

\(\text{\textit{Var}}G(Z)=\sum_{i=1}^{+\infty}\frac{\left(\mathbb{E}\left(G^{(i)}(Z)\right)\right)^2}{i!}.\)

<tbc>_For any_ \(k\ge 1\),

\(\text{\textit{Var}}G(Z)=\mathbb{E}\left(G'(Z)^2\right)-\frac{\mathbb{E}\left(G''(Z)^2\right)}{2}+\cdots+(-1)^{k-1}\frac{\mathbb{E}\left(G^{(k)}(Z)^2\right)}{k!}+(-1)^k\sum_{j=k+1}^\infty\genfrac(){pt}{2}{j-1}{k}\frac{\left(\mathbb{E}\left(G^{(j)}(Z)\right)\right)^2}{j!}.\) (3.3)

_For any_ \(a\in[0,1]\),

\(\text{\textit{Var}}G(Z)=\sum_{i=1}^{+\infty}\left((-1)^{i-1}a^i\frac{\mathbb{E}\left(G^{(i)}(Z)^2\right)}{i!}+(1-a)^i\frac{\left(\mathbb{E}\left(G^{(i)}(Z)\right)\right)^2}{i!}\right).\) (3.4)

_Proof._ This is nothing but Lemma 3.1 together with Proposition 1.5. To get the last equality, apply (1.17) to \(k=\lfloor an\rfloor\).

The equality (3.3) is a generalization of the equality in \[4\], where _k_=1. Note that (3.4) can be rewritten as<tbc>

\(\text{Var}G(Z)=\sum_{i=1}^{+\infty}\frac{\left(\mathbb{E}\left(G^{(i)}(Z)\right)\right)^2}{i!}+\sum_{i=1}^{+\infty}\left((-1)^{i-1}\frac{\mathbb{E}\left(G^{(i)}(Z)^2\right)}{i!}+\sum_{j\ge i}(-1)^i\genfrac(){pt}{2}{j}{i}\frac{\left(\mathbb{E}\left(G^{(j)}(Z)\right)\right)^2}{j!}\right)a^i,\)

<tbc>which gives us the additional equality: for all \(i\ge 1\),<tbc>

\(\frac{\mathbb{E}\left(G^{(i)}(Z)^2\right)}{i!}=\sum_{j\ge i}\genfrac(){pt}{2}{j}{i}\frac{\left(\mathbb{E}\left(G^{(j)}(Z)\right)\right)^2}{j!}.\)

<tbc>This gives an alternative way to find (3.1) again:

\(\sum_{i=k+1}^{+\infty}(-1)^{i-1}\frac{\mathbb{E}\left(G^{(i)}(Z)^2\right)}{i!}=\sum_{j\ge i\ge k+1}(-1)^{i-1}\genfrac(){pt}{2}{j}{i}\frac{\left(\mathbb{E}\left(G^{(j)}(Z)\right)\right)^2}{j!}\)<br>
\(=\sum_{j=k+1}^{+\infty}\left(\sum_{i=k+1}^j(-1)^{i-1}\genfrac(){pt}{2}{j}{i}\right)\frac{\left(\mathbb{E}\left(G^{(j)}(Z)\right)\right)^2}{j!}\)<br>
\(=\sum_{j=k+1}^{+\infty}\genfrac(){pt}{2}{j-1}{k}\frac{\left(\mathbb{E}\left(G^{(j)}(Z)\right)\right)^2}{j!}.\)

Multivariable versions of the above results remain true, and in fact, so do infinite-dimensional ones on Wiener space or Poisson space or even Fock space. In each case, what is needed is a proper definition of the gradient, e.g., see \[15\] for some infinite dimensional setting (Wiener and Poisson spaces). In the multivariate setting here is a small sample of results which can be easily obtained via the techniques developed to this point: Let \(m\ge 1\), let \(G:\mathbb{R}^m\rightarrow\mathbb{R}\)<tbc>

