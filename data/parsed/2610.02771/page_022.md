_Proof of Theorem 5._ By Lemma 4,<tbc>

\(|\theta_L-\mathbb{E}[W]|\le\frac{\sigma^2}{2L}.\)

<tbc>Also,<tbc>

\(\hat{\mu}_n=c+\bar{Z}_n,\mu=c+\mathbb{E}[W].\)

<tbc>Therefore<tbc>

\(|\hat{\mu}_n-\mu|=|\bar{Z}_n-\mathbb{E}[W]|\le|\bar{Z}_n-\theta_L|+|\theta_L-\mathbb{E}[W]|.\)

<tbc>Combining this with Lemma 18, we conclude that with probability at least \(1-\gamma\), simultaneously for all \(n\ge 1\),<tbc>

\(|\hat{\mu}_n-\mu|\le\frac{\sigma^2}{2L}+2\sqrt{\frac{v_Lx_n(\gamma)}{n}}+\frac{b_Lx_n(\gamma)}{3n}.\)

<tbc>Finally, substituting

\(v_L=3\alpha_L\sigma^2,b_L=3\alpha_LL,\)

gives

\(|\hat{\mu}_n-\mu|\le\frac{\sigma^2}{2L}+2\sqrt{\frac{3\alpha_L\sigma^2x_n(\gamma)}{n}}+\frac{\alpha_LLx_n(\gamma)}{n}\text{for all}n\ge 1.\)

This is exactly the claimed confidence sequence.

## B.5 Sample-complexity inversion

_Proof of Corollary 6._ Let \(\beta>0\) be the desired accuracy. To balance the clipping bias and the variance, we choose the clipping level \(L=\frac{2\sigma^2}{\beta}\) . By Lemma 4, this ensures the clipping bias is bounded by \(\frac{\sigma^2}{2L}=\frac{\beta}{4}\) .

From Theorem 5, with probability at least \(1-\gamma\), simultaneously for all \(n\ge 1\):<tbc>

\(|\hat{\mu}_n-\mu|\le\frac{\beta}{4}+2\sqrt{\frac{3\alpha_L\sigma^2x_n(\gamma)}{n}}+\frac{\alpha_LLx_n(\gamma)}{n}\)

<tbc>where \(\alpha_L=1+log\frac{2\sigma}{\beta}\) and \(x_n(\gamma)=log\left(\frac{\pi^2(1+\lfloor log_2n\rfloor)^2}{3\gamma}\right)\).

To guarantee \(|\hat{\mu}_n-\mu|\le\beta\), we enforce that the concentration term is bounded by \(\frac{\beta}{2}\) and the Bernstein range term by \(\frac{\beta}{4}\) . Solving these individually for _n_:

\(2\sqrt{\frac{3\alpha_L\sigma^2x_n(\gamma)}{n}}\le\frac{\beta}{2}\Longrightarrow n\ge\frac{48\alpha_L\sigma^2x_n(\gamma)}{\beta^2}\) (1)

\(\frac{\alpha_LLx_n(\gamma)}{n}\le\frac{\beta}{4}\Longrightarrow n\ge\frac{8\alpha_L\sigma^2x_n(\gamma)}{\beta^2}\) (2)

Condition (1) is strictly dominant. Let us define<tbc>

\(H:=\frac{48\alpha_L\sigma^2}{\beta^2},\)

<tbc>so that our goal is to find an integer _n_ satisfying \(n\ge Hx_n(\gamma)\). Choose<tbc>

\(n:=\lceil CH\eta\rceil,\eta:=log\frac{1}{\gamma}+loglog(max\{H,e\}),\)

<tbc>where _C\>_0 is a sufficiently large universal constant. Since \(\eta\ge 1\), we have<tbc>

\(logH\le H,log\eta\le\eta.\)

<tbc>Moreover,

\(logn\le log(C+1)+logH+log\eta.\)

