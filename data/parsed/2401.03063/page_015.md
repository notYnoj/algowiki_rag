Iterating,<tbc>

\(\Delta_{1,\dots,k}S=(D_{1,\dots,k}S)2^k\mathbb{1}_{X_1=X_1^\prime,\dots,X_k=X_k^\prime},\)

<tbc>hence<tbc>

\(\mathbb{E}\frac{1}{2^k}\left(\Delta_{1,\dots,k}S\right)^2=\mathbb{E}\left(D_{1,\dots,k}S\right)^2.\) (3.2)

<tbc>We now expand, for any \(x\in\{-1,1\}^n\), _D_<sub>1_,...,k_</sub>_S(x_). Let us denote for \(A\subset\{1,\dots,k\}\),<tbc>

\(x^A:=(2\mathbb{1}_{1\in A}-1,\dots,2\mathbb{1}_{k\in A}-1,x_{k+1},\dots,x_n).\)

<tbc>It is straightforward to prove by induction that<tbc>

\(D_{1,\dots,k}S(x)=(-1)^{|i\in\{1,\dots,k\}:x_i=1|}\frac{1}{2^k}\sum_{A\subset\{1,\dots,k\}}(-1)^{|A|}S(x^A),\)

<tbc>which simplifies to<tbc>

\(D_{1,\dots,k}S(x)=(-1)^{|i\in\{1,\dots,k\}:x_i=1|}\frac{1}{2^k}\sum_{i=0}^k\genfrac(){pt}{2}{k}{i}(-1)^iG\left(\frac{2i-k+x_{k+1}+\cdots+x_n}{\sqrt{n}}\right).\)

<tbc>By Taylor’s formula, and using the fact that \(\sum_{i=0}^k\genfrac(){pt}{2}{k}{i}(-1)^i^\ell/\ell!=(-1)^k\mathbb{1}_{\ell=k}\) for any \(\ell\in\{0,\dots,k\}\), we get that<tbc>

\(|D_{1,\dots,k}S(x)|=\left|\frac{1}{\sqrt{n}^k}G^{(k)}\left(\frac{-k+x_{k+1}+\cdots+x_n}{\sqrt{n}}\right)\right|+\mathcal{O}\left(\frac{1}{\sqrt{n}^{k+1}}\right),\)

<tbc>with O uniform in _x_ (thanks to the compact support assumption). This leads to<tbc>

\(\mathbb{E}n^k\left(D_{1,\dots,k}S\right)^2\longrightarrow_{n\rightarrow\infty}\mathbb{E}\left(G^{(k)}(Z)\right)^2,\)

<tbc>and using (3.1) and (3.2), we get the desired result

\(\mathbb{E}J_k(n)\longrightarrow_{n\rightarrow\infty}\mathbb{E}\left(G^{(k)}(Z)\right)^2.\)

The other limit in the theorem is obtained in a very similar fashion.

We now see, using (1.11) and (1.12), that for any fixed \(k\ge 1\),<tbc>

\(B_k(n)\sim_{n\rightarrow+\infty}\frac{1}{n}\mathbb{E}\left(G'(Z)^2\right)\text{and}B_{n-k}(n)\sim_{n\rightarrow+\infty}\frac{1}{n}\left(\mathbb{E}\left(G'(Z)\right)\right)^2.\)

<tbc>More generally, for any \(a\in(0,1)\),<tbc>

\(B_{\lfloor an\rfloor}(n)\sim_{n\rightarrow+\infty}\frac{1}{n}\sum_{i=0}^\infty\frac{a^i(-1)^i}{i!}\mathbb{E}\left(G^{(i+1)}(Z)^2\right).\)

<tbc>Note that

\(\int_0^1B_{\lfloor an\rfloor}(n)\mathrm{d}a\longrightarrow_{n\rightarrow+\infty}\sum_{i=0}^\infty\frac{(-1)^i}{(i+1)!}\mathbb{E}\left(G^{(i+1)}(Z)^2\right)=\mathrm{Var}G(Z),\)

as one could expect.

**Proposition 3.2.** _Under similar assumptions on G, for all_ \(k\in\{1,\dots,m\}\),

\(\frac{\left(\mathbb{E}\left(G^{(k+1)}(Z)\right)\right)^2}{(k+1)!}\le(-1)^k\left(\mathrm{\textit{Var}}G(Z)-\mathbb{E}\left(G'(Z)^2\right)+\cdots+(-1)^k\frac{\mathbb{E}\left(G^{(k)}(Z)^2\right)}{k!}\right)\le\frac{\mathbb{E}\left(G^{(k+1)}(Z)^2\right)}{(k+1)!}.\)<br>
\(\frac{\left(\mathbb{E}\left(G^{(k+1)}(Z)\right)\right)^2}{(k+1)!}\le\mathrm{\textit{Var}}G(Z)-\left(\mathbb{E}\left(G'(Z)\right)\right)^2-\frac{\left(\mathbb{E}\left(G''(Z)\right)\right)^2}{2}-\dots-\frac{\left(\mathbb{E}\left(G^{(k)}(Z)\right)\right)^2}{k!}\le\frac{\mathbb{E}\left(G^{(k+1)}(Z)^2\right)}{(k+1)!}.\)

