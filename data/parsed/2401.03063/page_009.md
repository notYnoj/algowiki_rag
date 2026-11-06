In order to compute the derivative in (2.1), fix \(\alpha\in(0,1)\) and \(\varepsilon\in(0,1-\alpha)\). Conditioning on \(A_{\alpha,\alpha+\varepsilon}\) and letting<tbc>

\(\Delta_{\alpha,\varepsilon}:=\frac{\mathbb{E}\left(S(X^{(0)})S(X^{(\alpha+\varepsilon)})\right)-\mathbb{E}\left(S(X^{(0)})S(X^{(\alpha)})\right)}{\varepsilon},\)

<tbc>we get<tbc>

\(\Delta_{\alpha,\varepsilon}=\sum_{1\le i_1<\cdots<i_k\le n,k\le n}\frac{\mathbb{E}\left(S(X^{(0)})\big(S(X^{(\alpha+\varepsilon)})-S(X^{(\alpha)})\big)|A_{\alpha,\alpha+\varepsilon}=\{i_1,\dots,i_k\}\right)}{\varepsilon}\mathbb{P}\left(A_{\alpha,\alpha+\varepsilon}=\big\{i_1,\dots,i_k\big\}\right),\)

<tbc>so for almost every \(\alpha\),<tbc>

\(\Delta_{\alpha,\varepsilon}-\rightarrow_{\varepsilon\rightarrow 0}\sum_{i=1}^n\mathbb{E}\left(S(X^{(0)})(S(X^{(\alpha),\hat{i}})-S(X^{(\alpha),i}))\right)\nu_i(\alpha),\)

<tbc>where \(X^{(\alpha),\hat{i}}\) is defined like \(X^{(\alpha)}\) but with _X<sub>i</sub>_ for its _i_-th coordinate, and \(X^{(\alpha),\hat{i}}\) is defined like \(X^{(\alpha)}\) but with \(X'_i\) for its _i_-th coordinate. So we get finally:

\(\mathrm{Var}S=\sum_{i=1}^n\int_0^1\mathbb{E}\left(S(X^{(0)})(S(X^{(\alpha),i})-S(X^{(\alpha),\hat{i}}))\right)\mathrm{d}\nu_i(\alpha).\) (2.2)

Let us further define, for \(i\in\{1,\dots,n\}\) and any \(x_1,\dots,x_n\in\mathbb{R}^n\), _d<sub>i</sub>S_ via,<tbc>

\(d_iS(x_1,\dots,x_n):=S(x_1,\dots,x_n)-\mathbb{E}S(x_1,\dots,x_{i-1},X_i,x_{i+1},\dots,x_n).\)

<tbc>Note that if _Z<sub>i</sub>_ is independent of all the other random variables and has same distribution as _X<sub>i</sub>_, we have<tbc>

\(d_iS(X)=\mathbb{E}_{Z_i}\left(S(X)-S(X_1,\dots,X_{i-1},Z_i,X_{i+1},\dots,X_n)\right).\)

<tbc>Therefore we notice, conditioning on _U<sub>i</sub>_, that<tbc>

\(\mathbb{E}\left(d_iS(X^{(0)})d_iS(X^{(\alpha)})\right)=\mathbb{P}(\alpha\le U_i)\mathbb{E}\left(S(X^{(0)})(S(X^{(\alpha),i})-S(X^{(\alpha),\hat{i}}))\right).\)

<tbc>We can rewrite the variance as

\(\mathrm{Var}S=\sum_{i=1}^n\int_0^1\mathbb{E}\left(d_iS(X^{(0)})d_iS(X^{(\alpha)})\right)\frac{1}{\int_\alpha^1\mathrm{d}\nu_i(\alpha)}\mathrm{d}\nu_i(\alpha).\) (2.3)

Note that in the special case where _U<sub>i</sub>_ are uniformly distributed on \[0,1\],

\(\mathrm{Var}S=\sum_{i=1}^n\int_0^1\mathbb{E}\left(d_iS(X^{(0)})d_iS(X^{(\alpha)})\right)\frac{1}{1-\alpha}\mathrm{d}\alpha,\)

and a simple change of variables allows us to recover again (2.3). Therefore, we will focus on the uniformly distributed case.

Next, from (2.2),

\(\mathrm{Var}S=\sum_{i=1}^n\int_0^1\mathbb{E}\left(S(X^{(0)})(S(X^{(\alpha),\hat{i}})-S(X^{(\alpha),\hat{i}}))\right)\mathrm{d}\alpha\)<br>
\(=\sum_{i=1}^n\int_0^1\sum_{k=0}^{n-1}\mathbb{E}\left(S(X^{(0)})(S(X^{(\alpha),i})-S(X^{(\alpha),\hat{i}}))\right)\mathbb{1}_{|A_{0,\alpha}\backslash\{i\}|=k}\mathrm{d}\alpha\)<br>
\(=\int_0^1n\sum_{k=0}^{n-1}\frac{1}{n}\sum_{i=1}^n\mathbb{E}\left(S\left(\Delta_iS\right)^{\beta_{k,i}}\right)\mathbb{P}\left(|A_{0,\alpha}\backslash\{i\}|=k\right)\mathrm{d}\alpha,\)

where \(\beta_{k,i}\) is a random set of _k_ elements chosen in {1_,...,n_}\\{_i_}. Clearly \(\mathbb{P}\left(|A_{0,\alpha}\backslash\{i\}|=k\right)=\genfrac(){pt}{2}{n-1}{k}\alpha^k(1-\alpha)^{n-1-k}\), and from the representations (1.4) and (1.5), we get for any \(k\in\{0,\dots,n-1\}\),<tbc>

\(\frac{1}{n}\sum_{i=1}^n\mathbb{E}\left(S\left(\Delta_iS\right)^{\beta_{k,i}}\right)=B_{k+1}.\)

