\(\mathbb{E}\left(LCS(Z^{N,1})-LCS(Z^{N,0})\right)=\sum_{\ell=1}^{2n}\mathbb{E}\left(LCS(Z^{N,1})-LCS(Z^{N,0})|N_1(Z)\right)\mathbb{P}(N_1(Z^{N,1})=\ell)\)<br>
\(=\sum_{\ell=1}^{2n}f(\ell)p^{\ell-1}(1-p)^{n-\ell}\genfrac(){pt}{2}{n-1}{\ell-1}\)<br>
\(=\sum_{\ell=1}^{2n}f(\ell)-\rightarrow^\ell pn\mathbb{P}(N_1(Z)=\ell)\)<br>
\(=\mathbb{E}\left(f(N_1(Z))\frac{N_1(Z)}{pn}\right),\)

so by dominated convergence,<tbc>

\(\mathbb{E}\left(LCS(Z^{N,1})-LCS(Z^{N,0})\right)-\rightarrow_{n\rightarrow\infty}\mathbb{E}\left(LCS(Z)-LCS(\tilde{Z})\right).\)

<tbc>Therefore, for any \(\delta\in(0,\alpha_1-\alpha_2)\), for _n_ large enough,<tbc>

\(\mathbb{E}\left(LCS(Z^{N,1})-LCS(Z^{N,0})\right)\ge\delta,\)

<tbc>and using (4.1) and (4.2),

\(\frac{\mathrm{Var}LC_n}{n}\ge 2p(1-p)\delta^2.\)

## 4.3 On the order of the variance when one letter is omitted

Let the letters _X_<sub>1</sub>_,...,X<sub>n</sub>_ be drawn from an alphabet \(\alpha_1,\dots,\alpha_{m+1}\) and the letters _Y_<sub>1</sub>_,...,Y<sub>n</sub>_ drawn from an alphabet \(\alpha_1,\dots,\alpha_m\): so \(\alpha_{m+1}\) is an omitted letter, not belonging to any longest common subsequence. (Let _m\>_1, as the case _m_=1 is trivial and may be dealt with separately.) Let \(p:=\mathbb{P}(X_i=\alpha_{m+1})>0\), and in contrast to the binary-ternary case \[1\] or \[12\], no longer assume that the other letters are equiprobable and let \(p_{X,1}:=\mathbb{P}(X_i=\alpha_1),\dots,p_{X,m}:=\mathbb{P}(X_i=\alpha_m),p_{Y,1}:=\mathbb{P}(Y_i=\alpha_1),\dots,p_{Y,m}:=\mathbb{P}(Y_i=\alpha_m)\). Since

\(\mathrm{Var}LC_n\ge 2nB_{2n}(2n),\) (4.3)

it is therefore enough to find a constant lower bound on _B_<sub>2_n_</sub>(2_n_). Firstly, by conditioning,

\(B_{2n}(2n)=\frac{1}{4n}\sum_{j=1}^{2n}\mathbb{E}\left(\Delta_jLC_n(\Delta_jLC_n)^{1,\cdots,j-1,j+1,\dots,n}\right)\)<br>
\(=\frac{1}{4n}\sum_{j=1}^{2n}\sum_{i,i^\prime=1}^m\left(\mathbb{E}\Delta_jLC_n^{Z_j=\alpha_i,Z_j^\prime=\alpha_{i^\prime}}\right)^2\mathbb{P}(Z_j=\alpha_i)\mathbb{P}(Z'_j=\alpha_{i^\prime})\)<br>
\(\ge\frac{1}{4n}\sum_{j=1}^n\sum_{i=1}^m\left(\mathbb{E}\Delta_jLC_n^{X_j=\alpha_i,X_j^\prime=\alpha_{m+1}}\right)^2p_{X,ip}\)<br>
\(\ge\frac{1}{4n}\sum_{j=1}^n\left(\sum_{i=1}^m\mathbb{E}\Delta_jLC_n^{X_j=\alpha_i,X_j^\prime=\alpha_{m+1}}p_{X,i}\right)^2p.\)

Letting \(LC_{n-1,n}:=LCS(X_1\cdots X_{n-1};Y_1\cdots Y_n)\), we have for any \(j\in\{1,\dots,n\}\),<tbc>

\(\sum_{i=1}^m\mathbb{E}\Delta_jLC_n^{X_j=\alpha_i,X_j^\prime=\alpha_{m+1}}p_{X,i}=\mathbb{E}(LC_n)-\mathbb{E}(LC_{n-1,n}),\)

<tbc>and so,

\(B_{2n}(2n)\ge\frac{1}{4}\left(\mathbb{E}(LC_n)-\mathbb{E}(LC_{n-1,n})\right)p.\) (4.4)

