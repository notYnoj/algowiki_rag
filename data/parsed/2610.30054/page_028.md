We have seen that \(1-g(u)/A\ge r\lambda/A\) and \(1-h(v)/B\ge s\lambda/B\), and that \(\lambda D\ge A+B\). Using this and also \(A^{-1}+B^{-1}\ge 4/(A+B)\), Equation (4.3) can be upper bounded by

\(\frac{s(1-r\lambda/A)+r(1-s\lambda/B)}{r+s}=1-\frac{rs\lambda}{r+s}\left(\frac{1}{A}+\frac{1}{B}\right)\le 1-\frac{4rs}{(r+s)D}.\)

Taking reciprocals and raising to the power _r+s_ proves the result.

**Proposition 4.14.** _For every_ \(\phi\in\Delta_\mathbb{F}\) _and all real numbers_ \(x_1,x_2,x_3\ge 0\),<tbc>

\(\phi(\langle 1,1,2\rangle)^{x_2x_3}\phi(\langle 2,1,1\rangle)^{x_1x_3}\phi(\langle 1,2,1\rangle)^{x_1x_2}\le 2^{(x_1+x_2+x_3)^2/4}.\)

<tbc>_Proof._ Let _p_<sub>1</sub>, _p_<sub>2</sub> and _p_<sub>3</sub> be the logarithms of \(\phi(\langle 1,1,2\rangle)\), \(\phi(\langle 2,1,1\rangle)\) and \(\phi(\langle 1,2,1\rangle)\), and let _S=x_<sub>1</sub>+_x_<sub>2</sub>+_x_<sub>3</sub> and _B=p_<sub>1</sub>_x_<sub>2</sub>_x_<sub>3</sub>+_p_<sub>2</sub>_x_<sub>1</sub>_x_<sub>3</sub>+_p_<sub>3</sub>_x_<sub>1</sub>_x_<sub>2</sub>. Taking logarithms, the claim is \(4B\le S^2\). Both sides of \(4B\le S^2\) are homogeneous of degree 2 in (_x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>3</sub>) and continuous, so we may assume that _x_<sub>1</sub>, _x_<sub>2</sub> and _x_<sub>3</sub> are positive integers. For every integer \(n\ge 1\), let<tbc>

\(G_n:=\prod_{\pi\in\mathfrak{S}_3}\phi_\pi\big(nx_{\pi(1)},nx_{\pi(2)}\big)^{x_{\pi(3)}}.\)

<tbc>Since \(1\le\phi_\pi(a,b)<a+b\) (Lemma 4.10(i) for \(\phi_\pi\)) and \(\sum_{\pi\in\mathfrak{S}_3}x_{\pi(3)}=2S\), we have \(G_1\ge 1\) and \(G_n\le(nS)^{2S}\). For \(\sigma\in\mathfrak{S}_3\) and \(a\in\{n,n+1\}\), let<tbc>

\(R_\sigma(a):=\frac{\phi_\sigma\big(ax_{\sigma(1)},(n+1)x_{\sigma(2)}\big)}{\phi_\sigma\big(ax_{\sigma(1)},nx_{\sigma(2)}\big)}\)

<tbc>be the growth factor of \(\phi_\sigma\) in the second argument, at the first argument \(ax_{\sigma(1)}\). Let \(\pi\in\mathfrak{S}_3\). Using \(\phi_\pi(a,b)=\phi_{\pi\circ(12)}(b,a)\) we find<tbc>

\(\frac{\phi_\pi\big((n+1)x_{\pi(1)},(n+1)x_{\pi(2)}\big)}{\phi_\pi\big(nx_{\pi(1)},nx_{\pi(2)}\big)}=R_\pi(n+1)R_{\pi\circ(12)}(n).\)

<tbc>We raise this to the power \(x_{\pi(3)}\), which equals \(x_{(\pi\circ(12))(3)}\), and multiply over \(\pi\in\mathfrak{S}_3\). Since \(\pi\mapsto\pi\circ(12)\) is a bijection of S<sub>3</sub>, this gives<tbc>

\(\frac{G_{n+1}}{G_n}=\prod_{a\in\{n,n+1\}}\prod_{\sigma\in\mathfrak{S}_3}R_\sigma(a)^{x_{\sigma(3)}}.\)

<tbc>The six permutations form three pairs \(\{\sigma,\sigma\circ(23)\}\), one for each \(i\in\{1,2,3\}\), with \(\sigma(1)=i\). Let \(j=\sigma(2)\) and \(k=\sigma(3)\). Let \(a\in\{n,n+1\}\). If _p<sub>i</sub>\>_0, then by Lemma 4.10, applied to \(\phi_\sigma\) and \(\phi_{\sigma\circ(23)}\), the functions \(m\mapsto\phi_\sigma(ax_i,m)^{1/p_i}\) and \(m\mapsto\phi_{\sigma\circ(23)}(ax_i,m)^{1/p_i}\) satisfy the hypotheses of Lemma 4.13 with _ax<sub>i</sub>_ in place of _a_. Here we use that both spectral points take the value 2_<sup>p<sub>i</sub></sup>_ at \(\langle 1,1,2\rangle\), since \(\sigma\) and \(\sigma\circ(23)\) move its one-dimensional first leg to leg _i_, and that \(\phi_\sigma((23)\cdot T)=\phi_{\sigma\circ(23)}(T)\) and \(\phi_{\sigma\circ(23)}((23)\cdot T)=\phi_\sigma(T)\) for every tensor _T_, since \(\pi\cdot(\rho\cdot T)=(\pi\circ\rho)\cdot T\) for all \(\pi,\rho\in\mathfrak{S}_3\). That lemma with _u=nx<sub>j</sub>_, _v=nx<sub>k</sub>_, _r=x<sub>j</sub>_ and _s=x<sub>k</sub>_, raised to the power _p<sub>i</sub>_, gives<tbc>

\(R_\sigma(a)^{x_k}R_{\sigma\circ(23)}(a)^{x_j}\ge\big(\frac{D}{D-c}\big)^{p_i(x_j+x_k)},\)

<tbc>where _D_=(_n_+1)(_x<sub>j</sub>+x<sub>k</sub>_)+_ax<sub>i</sub>_-1 and _c_=4_x<sub>j</sub>x<sub>k</sub>/(x<sub>j</sub>+x<sub>k</sub>)\>_0. Since \(D\le(n+1)S\) and \(t:=c/S\le(x_j+x_k)/S\le 1\), we find, using Bernoulli’s inequality (which says that \((1+y)^t\le 1+ty\) for every real number \(0\le t\le 1\) and \(y\ge-1\)) in the last step, that<tbc>

\(\frac{D}{D-c}\ge 1+\frac{c}{D}\ge 1+\frac{t}{n+1}\ge\big(\frac{n+2}{n+1}\big)^t.\)

