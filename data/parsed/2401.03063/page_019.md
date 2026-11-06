**Theorem 3.7.** _There exists C\>_0 _such that for any function_ \(f:\{0,1\}^n\rightarrow\mathbb{R}\)_, the following inequality holds_

\(\text{\textit{Var}}S\le C\sum_{i=1}^n\frac{\|\tau_iS\|_2^2}{1+\mathrm{log}\left(\frac{\|\tau_iS\|_2}{\|\tau_iS\|_1}\right)},\)

_where S=f(X_<sub>1</sub>_,...,X<sub>n</sub>)._

We now prove a weaker form of this inequality using the \(B'_ks\), in the special case where there exists _a\>_0 such that for all \(i\in\{1,\dots,n\}\), \(|\tau_iS|\in\{0,a\}\). We can further assume without loss of generality by rescaling that _a_=1. Note that this particular case includes _LC<sub>n</sub>_ (changing a letter can only change _LC<sub>n</sub>_ by at most one).

Firstly, conditioning on whether \(X_{i_k}=X'_{i_k}\) or \(X_{i_k}\neq X'_{i_k}\), we can rewrite (1.4) as<tbc>

\(B_k=\mathbb{E}\frac{1}{4n!}\sum_{i\in\mathfrak{S}_n}(\tau_{i_k}S)(\tau_{i_k}S)^{i_1,\cdots,i_{k-1}},\) (3.6)

<tbc>so<tbc>

\(\text{Var}S=\sum_{k=1}^n\mathbb{E}\frac{1}{4n!}\sum_{i\in\mathfrak{S}_n}(\tau_{i_k}S)(\tau_{i_k}S)^{i_1,\cdots,i_{k-1}}\)<br>
\(=\frac{1}{4n!}\sum_{i\in\mathfrak{S}_n}\sum_{k=1}^n\mathbb{E}(\tau_{i_1}S)(\tau_{i_1}S)^{i_2,\cdots,i_k}.\)

<tbc>Let us fix \(i\in\mathfrak{S}_n\) and bound \(\sum_{k=1}^n\mathbb{E}(\tau_{i_1}S)(\tau_{i_1}S)^{i_2,\cdots,i_k}\). For ease of notation, by reindexing the _X<sub>i</sub>_’s, we may assume _i=Id_, also, let us write _X_:=(_X_<sub>2</sub>_,...,X<sub>n</sub>_). Since, by assumption, \(\tau_1S\) is boolean, there exists \(m\le 2^{n-1}\) and \(x^1,\dots,x^m\in\{0,1\}^{n-1}\) pairwise distinct such that \(|\tau_1S|=\sum_{i=1}^m\mathbb{1}_{X=x^i}\). Let, for \(\alpha\subset\{2,\dots,n\}\), \(N(\alpha):=|\{(i,j)\in\{1,\dots,m\}^2:\forall k\in\alpha,x_k^i=x_k^j\}|\). We have<tbc>

\(\mathbb{E}(\tau_1S)(\tau_1S)^{2,\cdots,k}\le\mathbb{E}|\tau_1S||\tau_1S|^{2,\cdots,k}=\frac{N(\{k+1,\dots,n\})}{2^{n+k-2}}.\)

<tbc>Let \(\ell\in\{1,\dots,n-1\}\) be such that \(2^{\ell-1}\le m\le 2^\ell\) (we may exclude the trivial case _m_=0). Using that for any \(k\in\{1,\dots,\ell\}\), \(N(\{k+1,\dots,n\})\le m2^{k-1}\), and the trivial bound \(N(\{k+1,\dots,n\})\le m^2\) when \(k>\ell\), we get

\(\sum_{k=1}^n\mathbb{E}(\tau_1S)(\tau_1S)^{2,\cdots,k}\le\sum_{k=1}^\ell\frac{m}{2^{n-1}}+\sum_{k=1+1}^n\frac{m^2}{2^{n+k-2}}\)<br>
\(\le\ell\frac{m}{2^{n-1}}+2\frac{m^2}{2^{n-1+\ell}}\)<br>
\(\le(\ell+2)\frac{m}{2^{n-1}}=(\ell+2)\|\tau_1S\|_2^2.\)

Note that \(\mathrm{log}\left(\frac{\|\tau_1S\|_2}{\|\tau_1S\|_1}\right)=\mathrm{log}\left(\sqrt{\frac{2^{n-1}}{m}}\right)=\mathrm{log}(2)(n-1-\mathrm{log}_2(m))/2\) so \(\ell+2\le n+2-\frac{2}{\mathrm{log}(2)}\mathrm{log}\left(\frac{\|\tau_1S\|_2}{\|\tau_1S\|_1}\right)\) hence<tbc>

\(\sum_{k=1}^n\mathbb{E}(\tau_1S)(\tau_1S)^{2,\cdots,k}\le\left(n+2-\frac{2}{\mathrm{log}(2)}\mathrm{log}\left(\frac{\|\tau_1S\|_2}{\|\tau_1S\|_1}\right)\right)\|\tau_1S\|_2^2.\)

<tbc>Finally,

\(\text{Var}S=\frac{1}{4n!}\sum_{i\in\mathfrak{S}_n}\sum_{k=1}^n\mathbb{E}(\tau_{i_1}S)(\tau_{i_1}S)^{i_2,\cdots,i_k}\)<br>
\(\le\frac{1}{4n!}\sum_{i\in\mathfrak{S}_n}\left(n+2-\frac{2}{\mathrm{log}(2)}\mathrm{log}\left(\frac{\|\tau_{i_1}S\|_2}{\|\tau_{i_1}S\|_1}\right)\right)\|\tau_{i_1}S\|_2^2\)<br>
\(\le\frac{1}{4}\sum_{j=1}^n\left(1+\frac{2}{n}-\frac{2}{n\mathrm{log}(2)}\mathrm{log}\left(\frac{\|\tau_jS\|_2}{\|\tau_jS\|_1}\right)\right)\|\tau_jS\|_2^2.\)

