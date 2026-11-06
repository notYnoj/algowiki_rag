_Proof._ We first prove this fact for \(\alpha\) a dyadic rational number, \(\alpha=a/2^b\in(0,1)\). Let \(m\ge b\) and _n_=2_<sup>m</sup>_, with \(m\ge b\). The proof is more convenient to write for a slightly different function: instead of computing the _B<sub>k</sub>_’s of _S<sub>n</sub>(n_=2_<sup>m</sup>_), we compute the _B<sub>k</sub>_’s of<tbc>

\(T_n:=G(X_{1,n}+\cdots+X_{n,n}+X_{n+1,n}).\)

<tbc>Since the difference between the former and latest has order O(1_/n_), this is enough to get the desired result. We have

\(B_{\lfloor\alpha n\rfloor+1}=\mathbb{E}\big(G\left(\sum_{i=1}^{n+1}X_{i,n}\right)\left(G\left(X_1+\sum_{i=2}^{2^{m-b}a+1}X'_{i,n}+\sum_{i=2^{m-b}a+2}^{n+1}X_{i,n}\right)-G\left(\sum_{i=1}^{2^{m-b}a+1}X'_{i,n}+\sum_{i=2^{m-b}a+2}^{n+1}X_{i,n}\right)\right)\big)\)<br>
\(=\mathbb{E}\left(G(Z_{1/n}+Y'_\alpha+Y''_{1-\alpha})\left(G(Z_{1/n}+Y_\alpha+Y''_{1-\alpha})-G(Z'_{1/n}+Y'_\alpha+Y''_{1-\alpha})\right)\right),\)

where _Z_ and \(Z'\) are two independent copies of _Y_ , since \((Z_{1/n},Z'_{1/n},Y_\alpha,Y'_\alpha,Y''_{1-\alpha})\) has the same distribution as \((X_1,X'_1,\sum_{i=2}^{2^{m-b}a+1}X_{i,n},\sum_{i=2}^{2^{m-b}a+1}X'_{i,n},\sum_{i=2^{m-b}a+2}^{n+1}X_{i,n})\).

Let \(G_{\alpha,1}(\cdot)=\mathbb{E}(G(\cdot+Y_\alpha+Y''_\alpha)|Y_\alpha,Y''_{1-\alpha})\) and \(G_{\alpha,2}(\cdot)=\mathbb{E}(G(\cdot+Y_\alpha+Y''_\alpha)|Y'_\alpha,Y''_{1-\alpha})\), we then have<tbc>

\(B_{\lfloor\alpha n\rfloor+1}=\mathbb{E}\left(G_{\alpha,1}(Z_{1/n})G_{\alpha,2}(Z_{1/n})-G_{\alpha,1}(0)G_{\alpha,2}(0)-(G_{\alpha,1}(Z_{1/n})G_{\alpha,2}(Z'_{1/n})-G_{\alpha,1}(0)G_{\alpha,2}(0))\right),\)

<tbc>so if _A_<sub>1</sub> be the infinitesimal generator of \((Y_t,Y_t)_{t\ge 0}\) and _A_<sub>0</sub> is the infinitesimal generator of \((Y_t,Y'_t)_{t\ge 0}\), then

\(nB_{\lfloor\alpha n\rfloor+1}-\rightarrow_{n\rightarrow\infty}\mathbb{E}\left((A_1-A_0)G_{\alpha,1}\otimes G_{\alpha,2}(0,0)\right)\)<br>
\(=\mathbb{E}\left(\sigma G'(Y_\alpha+Y''_{1-\alpha})G'(Y'_\alpha+Y''_{1-\alpha})+\int_\mathbb{R}\Delta_uG(Y_\alpha+Y''_{1-\alpha})\Delta_uG(Y'_\alpha+Y''_{1-\alpha})\mathrm{d}\nu\right),\) (3.5)

since \((A_1-A_0)(f\otimes g)(0,0)=\sigma f'(0)g'(0)+\int_\mathbb{R}\Delta_uf(0)\Delta_ug(0)\mathrm{d}\nu\). (This computation is in \[16, Proposition 2\].)

Since the finite sequence _B<sub>k</sub>_ is non-decreasing, a routine density argument shows that for any \(\alpha\in(0,1)\), \(nB_{\lfloor\alpha n\rfloor}\) has limit (3.5), which is the desired result.

**Corollary 3.6.**

\(\text{\textit{Var}}G(Y)=\int_0^1\mathbb{E}\left(\sigma G'(Y_\alpha+Y''_{1-\alpha})G'(Y'_\alpha+Y''_{1-\alpha})+\int_\mathbb{R}\Delta_uG(Y_\alpha+Y''_{1-\alpha})\Delta_uG(Y'_\alpha+Y''_{1-\alpha})\mathrm{d}\nu\right)\mathrm{d}\alpha.\)

This above representation of the variance stems from the decomposition \(\text{Var}G(Y)=\sum_{k=1}^nB_k\) and it can also be found, with a different approach, in \[16\]. Although we have only been concerned with representations of the variance, similar representations continue to hold for covariances in the spirit of the work just cited.

For example, we note that in the Poisson case, the limit (3.5) is simply<tbc>

\(\mathbb{E}\left(DG(Y_\alpha+Y''_{1-\alpha})DG(Y'_\alpha+Y''_{1-\alpha})\right),\)

<tbc>where _DG(x_)=_G(x_+1)-_G(x_), \(Y_\alpha,Y'_\alpha,Y''_{1-\alpha}\) are Poisson distributed independent random variables (with respective parameter \(\alpha\), \(\alpha\), and \(1-\alpha\)). In the Gaussian case, it is

\(\mathbb{E}\left(G'(Z_{1,\alpha})G'(Z_{2,\alpha})\right),\)

where \(Z_{1,\alpha}\), \(Z_{2,\alpha}\) are Gaussian random variables centered with variance one and covariance \(1-\alpha\).

## 3.3 A weaker Talagrand _L_<sub>1</sub>-_L_<sub>2</sub> inequality

Let us focus on the special case where the _X<sub>i</sub>_’s are Bernoulli with parameter 1/2. For \(i\in\{1,\dots,n\}\), let<tbc>

\(\tau_iS(X_1,\dots,X_n):=S(X_1,\dots,X_{i-1},0,X_{i+1},\dots,X_n)-S(X_1,\dots,X_{i-1},1,X_{i+1},\dots,X_n)\)

<tbc>(so this does not depend on _X<sub>i</sub>_). Then, Talagrand’s _L_<sub>1</sub>-_L_<sub>2</sub> inequality (\[22, Theorem 1.5\]) can be stated as follows:<tbc>

