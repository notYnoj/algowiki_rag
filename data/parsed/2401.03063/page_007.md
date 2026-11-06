_Following \[4\], for_ \(i\in\{1,\dots,n\}\)_, let_<tbc>

<tbc>\(H_\Phi^{(i)}(S)=\mathbb{E}^{(i)}\Phi(S)-\Phi(\mathbb{E}^{(i)}(S)),\)<tbc>

<tbc>_while for_ \(i\neq j\in\{1,\dots,n\}\),<tbc>

<tbc>\(H_\Phi^{(j,i)}(S):=\mathbb{E}^{(j)}H_\Phi^{(i)}(S)-H_\Phi^{(i)}(\mathbb{E}^{(j)}S)=H_\Phi^{(i,j)}(S).\)<tbc>

<tbc>_Still iterating, for_ \(i_1\neq\dots\neq i_k\in\{1,\dots,n\}\),<tbc>

<tbc>\(H_\Phi^{(i_1,\dots,i_k)}(S):=\mathbb{E}^{(i_1)}H_\Phi^{(i_2,\dots,i_k)}(S)-H_\Phi^{(i_2,\dots,i_k)}(\mathbb{E}^{(i_1)}S).\)<tbc>

<tbc>_Define the corresponding B<sub>k</sub>’s as,_<tbc>

<tbc>\(B_k:=\mathbb{E}\frac{1}{n!}\sum_{i\in\mathfrak{S}_n}H_\Phi^{(i_k)}(\mathbb{E}^{(i_1,\dots,i_{k-1})}S),\)<tbc>

<tbc>_for all_ \(k\in\{1,\dots,n\}\)_. Once again the sum is telescopic:_<tbc>

<tbc>\(\sum_{k=1}^nB_k=\mathbb{E}\frac{1}{n!}\sum_{i\in\mathfrak{S}_n}\mathbb{E}^{(i_k)}\Phi(\mathbb{E}^{(i_1,\dots,i_{k-1})}S)-\Phi(\mathbb{E}^{(i_1,\dots,i_k)}S)=H_\Phi S.\)<tbc>

<tbc>_By the conditional Jensen inequality, the B<sub>k</sub>’s are non-negative. Just like in the variance case, it is clear by induction that for all_ \(\ell\in\{0,\dots,n-1\}\),<tbc>

<tbc>\(D^\ell B_k=\mathbb{E}\frac{1}{n!}\sum_{i\in\mathfrak{S}_n}H_\Phi^{(i_1,\dots,i_{\ell+1})}(\mathbb{E}^{(i_{\ell+2},\dots,i_{k+\ell})}S).\)<tbc>

<tbc>_Let us now look for the class of convex functions_ \(\Phi\) _such that for any S and X_<sub>1</sub>_,...,X<sub>n</sub> satisfying the basic independence and integrability assumptions,_ \((B_k)_{1\le k\le n}\) _is non-increasing. In particular, for any random variable Z defined on a product space_ \(\Omega_1\times\Omega_2\) _satisfying the integrability conditions, choosing S and X_<sub>1</sub>_,...,X<sub>n</sub> such that S=Z (S=f(X_<sub>1</sub>_,X_<sub>2</sub>) _for some function f), we have that_<tbc>

\(D^1B_k=\frac{1}{n!}\mathbb{E}\sum_{i\in\mathfrak{S}_n}H_\Phi^{(i_1,i_2)}(\mathbb{E}^{(i_3,\dots,i_{k+1})}S)\)<br>
\(=\frac{2}{n!}\mathbb{E}H_\Phi^{(1,2)}(S)\)<br>
\(=\frac{2}{n!}\mathbb{E}\left(\Phi(Z)-\Phi(\mathbb{E}^{(1)}Z)-\Phi(\mathbb{E}^{(2)}Z)+\Phi(\mathbb{E}^{(1,2)}Z)\right),\)

_so_ \(\mathbb{E}\left(\Phi(Z)-\Phi(\mathbb{E}^{(1)}Z)-\Phi(\mathbb{E}^{(2)}Z)+\Phi(\mathbb{E}^{(1,2)}Z)\right)\ge 0\)_. Reciprocally, if for any random variable Y defined on a product space_ \(\Omega_1\times\Omega_2\) _satisfying the integrability conditions,_<tbc>

<tbc>\(\mathbb{E}\left(\Phi(Y)-\Phi(\mathbb{E}^{(1)}Y)-\Phi(\mathbb{E}^{(2)}Y)+\Phi(\mathbb{E}^{(1,2)}Y)\right)\ge 0,\)<tbc>

<tbc>_then clearly_ \(D^1B_k\ge 0\) _for all_ \(k\in\{1,\dots,n-1\}\)_. Theorem 1 in \[23\] tells us that this happens if and only if_ \(\Phi\) _is affine or is twice differentiable with_ \(\Phi''>0\) _and_ \(1/\Phi''\) _concave._<tbc>

_(ii)_ _One may further wonder what conditions on_ \(\Phi\) _would guarantee_ \((B_k)_{1\le k\le n}\) _to be completely monotone, or, at least, to have_ \(D^2B_k\ge 0\) _for all_ \(k\in\{1,\dots,n-2\}\)_. Unfortunately, the variance is basically the only case for which this holds true. Indeed, if the condition_ \(D^2B_k\ge 0\) _is satisfied for all S, then, as before, choosing S=f(X_<sub>1</sub>_,X_<sub>2</sub>_,X_<sub>3</sub>)_, we get_<tbc>

<tbc>\(D^1B_k=\frac{1}{n!}\mathbb{E}\sum_{i\in\mathfrak{S}_n}H_\Phi^{(i_1,i_2,i_3)}(\mathbb{E}^{(i_3,\dots,i_{k+2})}S)\)<br>
\(=\frac{6}{n!}\mathbb{E}H_\Phi^{(1,2,3)}(S)\)<br>
\(=\frac{6}{n!}\mathbb{E}\sum_{\alpha\subset\{1,2,3\}}(-1)^{|\alpha|}\Phi(\mathbb{E}^\alpha S).\)

