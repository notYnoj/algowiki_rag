so

\(\mathrm{Var}LC_n\ge\sum_{k=1}^{2n}\left(\mathbb{E}\left(LC_n(Z^{k,0})-LC_n(Z^{k,1})\right)\right)^2p_0(1-p_0)\)<br>
\(\ge 2n\left(\frac{1}{2n}\sum_{k=1}^{2n}\mathbb{E}_{p_1}\left(LC_n^{k,0}-LC_n^{k,1}\right)\right)^2p_0(1-p_0),\)

and finally

\(\mathrm{limsup}_{n\rightarrow\infty}\frac{\mathrm{Var}LC_n}{n}\ge 2p_0(1-p_0)\left(\frac{\gamma(p_0)-\gamma(1/2)}{1/2-p_0}\right)^2.\)

**Remark 4.3.** _As already mentioned, it is expected that the function_ \(\gamma\) _is strictly convex, but even proving that_ \(\gamma\) _is non-increasing on_ \[0,1/2\] _and non-decreasing on_ \[1/2,1\] _seems to be lacking. It also seems reasonable that for a fixed alphabet, say binary uniform, the sequence_ \((\mathbb{E}LC_n/n)_{n\ge 1}\) _is non-decreasing, but again a proof is lacking._

## 4.5 On the order of the variance in the binary uniform case

A long-standing open problem is to find the order of the variance of _LC<sub>n</sub>_ when the distribution is uniform. In this section, we focus on the uniform binary case, so \(\mathrm{lim}_{n\rightarrow\infty}\mathbb{E}LC_n/n=\gamma(1/2):=\gamma_2\). We recall, from \[14\], the definition of the function \(\widetilde{\gamma}\): for any _p\>_0,

\(\widetilde{\gamma}(p):=\mathrm{lim}_{n\rightarrow\infty}\frac{\mathbb{E}\left(LCS(X_1\cdots X_n;Y_1\cdots Y_{\lfloor np\rfloor})\right)}{n(1+p)/2}.\)

By a superadditivity argument, this limit is well defined and \(\widetilde{\gamma}\) is concave, non-decreasing on \[0,1\] and non-increasing on \([1,+\infty)\) (for the details, and further properties of \(\widetilde{\gamma}\), we refer the reader to \[14\]).

By symmetry, in this case, _B_<sub>2_n_</sub>(2_n_)=0. However, letting _Z_<sub>1</sub>=(_X_<sub>1</sub>_,Y_<sub>1</sub>)_,Z_<sub>2</sub>=(_X_<sub>2</sub>_,Y_<sub>2</sub>)_,...,Z<sub>n</sub>_=(_X<sub>n</sub>,Y<sub>n</sub>_), then we may see the last _B<sub>k</sub>_ is _B<sub>n</sub>(n_) (_LC<sub>n</sub>=LC(Z_<sub>1</sub>_,...,Z<sub>n</sub>_)), which can be written as, by conditioning,

\(B_n(n)=\frac{1}{2n}\sum_{j=1}^n\mathbb{E}\left(\Delta_jLC_n(\Delta_jLC_n)^{1,\cdots,j-1,j+1,\dots,n}\right)\)<br>
\(=\frac{1}{2n}\sum_{j=1}^n\sum_{\varepsilon,\varepsilon^\prime\in\{0,1\}^2}\left(\mathbb{E}\Delta_jLC_n^{Z_j=\varepsilon,Z_j^\prime=\varepsilon^\prime}\right)^2\mathbb{P}(Z_j=\varepsilon)\mathbb{P}(Z'_j=\varepsilon')\)<br>
\(=\frac{1}{2n}\sum_{j=1}^n8\left(\mathbb{E}\Delta_jLC_n^{Z_j=(0,0),Z_j^\prime=(0,1)}\right)^2\mathbb{P}(Z_j=(0,0))\mathbb{P}(Z'_j=(0,1),\)

where we used symmetry and the fact that when \(\varepsilon'=\varepsilon\) or \(\varepsilon'=(1,1)-\varepsilon\), \(\mathbb{E}\Delta_jLC_n^{Z_j=\varepsilon,Z_j^\prime=\varepsilon^\prime}=0\). Finally,<tbc>

\(B_n(n)=\frac{1}{4n}\sum_{j=1}^n\left(\mathbb{E}\Delta_jLC_n^{Z_j=(0,0),Z_j^\prime=(0,1)}\right)^2\)

<tbc>which may also be written

\(B_n(n)=\frac{1}{n}\sum_{j=1}^n\frac{1}{4}\left(\mathbb{E}\left(LCS(Z^{j,(0,0)})-LCS(Z^{j,(0,1)})\right)\right)^2.\)

So it is enough to find a lower bound on this quantity, which is doable for the terms on the edge (1 or _n_) but seems tricky for the terms in the middle.

