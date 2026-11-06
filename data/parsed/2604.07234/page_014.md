<tbc>and we let<tbc>

\(\ell=\ell(M):=2^{2^{\phi(M)-2}}\in\mathcal{S};L=L(M):=M/\ell(M)\ge\sqrt{M}.\)

<tbc>We define \(\mu\in\mathcal{A}_N\) and \(\nu\in\mathcal{A}_M\) such that for all \(i\in[L-1]\), we have that \(\mu(i)=\ell/\alpha\) and \(\nu(i)=\ell\). We decompose \(X'\) and _Y_ via<tbc>

\(X'=X_\mu^{(1)}X_\mu^{\prime(2)}\cdots X_\mu^{\prime(L)};Y=Y_\nu^{(1)}Y_\nu^{(2)}\cdots Y_\nu^{(L)}.\)

<tbc>By considering those configurations of \(S_{X^\prime,Y}\) where \(Y_\nu^{(i)}\) is assigned to \(X_\mu^{\prime(i)}\) for \(i\in[L]\), it follows that

\(\frac{1}{M}\mathbb{E}\left[\mathrm{log}Z_{X^\prime,Y}\right]\ge\frac{1}{M}\sum_{i=1}^L\mathbb{E}\left[\mathrm{log}Z_{X_\mu^{\prime(i)},Y_\nu^{(i)}}\right]=\frac{1}{\ell L}\sum_{i=1}^L\mathbb{E}\left[\mathrm{log}Z_{X_\mu^{\prime(i)},Y_\nu^{(i)}}\right]\)<br>
\(=\frac{1}{\ell}\mathbb{E}\left[\mathrm{log}Z_{X_\mu^{\prime(1)},Y_\nu^{(1)}}\right]+\frac{1}{M}\mathbb{E}\left[\mathrm{log}Z_{X_\mu^{\prime(L)},Y_\nu^{(L)}}-\mathrm{log}Z_{X_\mu^{\prime(1)},Y_\nu^{(1)}}\right]\)<br>
\(=\frac{1}{\ell}\mathbb{E}\left[\mathrm{log}Z_{X_{1:\ell/\alpha}^\prime,Y_{1:\ell}}\right]+o(1).\) (2.8)

On the other hand, we define<tbc>

\(u=u(M):=2^{2^{\phi(M)+1}}\in\mathcal{S};U=U(M):=u(M)/M\ge M.\)

<tbc>We define \(\tilde{\mu}\in\mathcal{A}_N\) and \(\tilde{\nu}\in\mathcal{A}_M\) so for all \(i\in[U-1]\), we have that \(\tilde{\mu}(i)=N\) and \(\tilde{\nu}(i)=M\). We decompose \(X'_{1:u/\alpha}\) and _Y_<sub>1:_u_</sub> via<tbc>

\(X'_{1:u/\alpha}=X_\tilde{\mu}^{\prime(1)}X_\tilde{\mu}^{\prime(2)}\cdots X_\tilde{\mu}^{\prime(U)};Y_{1:u}=Y_\tilde{\nu}^{(1)}Y_\tilde{\nu}^{(2)}\cdots Y_\tilde{\nu}^{(U)}.\)

<tbc>By considering those configurations of \(S_{X_{1:u/\alpha}^\prime,Y_{1:u}}\) for which \(Y_\tilde{\nu}^{(i)}\) is assigned to \(X_\tilde{\mu}^{\prime(i)}\) for \(i\in[U]\), it follows that

\(\frac{1}{u}\mathbb{E}\left[\mathrm{log}Z_{X_{1:u/\alpha}^\prime,Y_{1:u}}\right]\ge\frac{1}{u}\sum_{i=1}^U\mathbb{E}\left[\mathrm{log}Z_{X_\tilde{\mu}^{\prime(i)},Y_\tilde{\nu}^{(i)}}\right]=\frac{1}{M}\cdot\frac{1}{U}\sum_{i=1}^U\mathbb{E}\left[\mathrm{log}Z_{X_\tilde{\mu}^{\prime(i)},Y_\tilde{\nu}^{(i)}}\right]\)<br>
\(=\frac{1}{M}\mathbb{E}\left[\mathrm{log}Z_{X_\tilde{\mu}^{\prime(1)},Y_\tilde{\nu}^{(1)}}\right]+\frac{1}{U}\cdot\frac{1}{M}\mathbb{E}\left[\mathrm{log}Z_{X_\tilde{\mu}^{\prime(U)},Y_\tilde{\nu}^{(U)}}-\mathrm{log}Z_{X_\tilde{\mu}^{\prime(1)},Y_\tilde{\nu}^{(1)}}\right]\)<br>
\(=\frac{1}{M}\mathbb{E}[\mathrm{log}Z_{X^\prime,Y}]+o(1).\) (2.9)

Altogether, we have that

\(\frac{1}{\ell}\mathbb{E}\left[\mathrm{log}Z_{X_{1:\ell/\alpha}^\prime,Y_{1:\ell}}\right]+o(1)\le^\text{(2.8)}\frac{1}{M}\mathbb{E}\left[\mathrm{log}Z_{X^\prime,Y}\right]\le^\text{(2.9)}\frac{1}{u}\mathbb{E}\left[\mathrm{log}Z_{X_{1:u/\alpha}^\prime,Y_{1:u}}\right]+o(1),\)

from which we conclude that \(\frac{1}{M}\mathbb{E}[\mathrm{log}Z_{X^\prime,Y}]\) converges. □

_Proof of Equation_ (1.7). Taking expectations in (2.6) with normalization by _N_ yields<tbc>

\(\frac{1}{N}\mathbb{E}\left[\mathrm{log}Z_{X^\prime,Y}\right]=\frac{1}{\sqrt{M}/\alpha}\mathbb{E}\left[\mathrm{log}Z_{X_{1:\sqrt{M}/\alpha}^\prime,Y_{1:\sqrt{M}}}\right]+\mathbb{E}\left[\frac{1}{N}\left(\mathrm{log}Z_{X^\prime,Y}(\mu^*)-\mathrm{log}Z_{X^\prime,Y}(\bar{\mu})\right)\right]+o(1).\)

<tbc>Lemma 2.2 and Markov’s inequality now imply that

(2.10) \(0\le\frac{1}{N}\left(\mathrm{log}Z_{X^\prime,Y}(\mu^*)-\mathrm{log}Z_{X^\prime,Y}(\bar{\mu})\right)=o_p(1).\)

Therefore, we may write (2.6) with normalization by _N_ as

(2.11) \(\frac{1}{N}\mathrm{log}Z_{X^\prime,Y}=\frac{1}{\sqrt{N}}\sum_{i=1}^\sqrt{M}\frac{1}{\sqrt{N}}\mathrm{log}Z_{X_\tilde{\mu}^{\prime(i)},Y_\tilde{\nu}^{(i)}}+o_p(1),\)

