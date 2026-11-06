**Lemma 31** (Reusable phased clipping has the same order)**.** _Consider the phased algorithm with the same active-arm, stopping, and elimination rules as_ RESTARTPHASEDCLIP-1BITBAI_, but replace the restarted phase-j estimator by the following reusable slab estimator. Let L_<sub>-1</sub>:=0_, let_<tbc>

\(I_0:=[0,L_0],I_s:=(L_{s-1},L_s](s\ge 1),\)

<tbc>_and define_<tbc>

\(A_s:=\int_{I_s}\frac{dt}{max\{\sigma,t\}},q_s(t):=\frac{1}{A_smax\{\sigma,t\}},t\in I_s.\)

<tbc>_For each arm k and slab s, draw S_∼Unif{-1,+1}_, T∼q<sub>s</sub>, query_<tbc>

\(Y=\mathbf{1}\{S(X_k-c_k)\ge T\},\)

<tbc>_and define_<tbc>

\(Z_{k,s}:=\frac{2S}{q_s(T)}Y.\)

<tbc>_In phase j, form_<tbc>

\(\widehat{\mu}_{k,j}^\text{reuse}:=c_k+\sum_{s=0}^j\overline{Z_{k,s}},\)

<tbc>_where <o>Z</o><sub>k,s</sub> is the empirical average of the retained samples from slab s. For_<tbc>

\(\Gamma_j:=log\frac{K(J+1)}{\delta}+loglog\left(e^e\frac{\sigma}{\rho_j}\right)+loglog\left(e^e\frac{K(J+1)}{\delta}\right),\)

<tbc>_there is a universal constant C_<sub>0</sub>_\>_0 _such that it is enough to top up each slab_ \(s\le j\) _to_<tbc>

\(m_{s,j}:=\left|C_0\frac{A_s\sigma^2}{\rho_j^2}\Gamma_j\right|\)

<tbc>_samples in order to guarantee the phase-j radius_ \(r_j=\rho_j/16\)_. Consequently, on an event of probability at least_ \(1-\delta\)_, the reusable phased algorithm uses at most_<tbc>

\(O\left(\sum_{k=1}^K\Lambda(\overline{\Delta_k})\frac{\sigma^2}{\Delta_k^2}\Gamma(\overline{\Delta_k};K,J,\delta)\right)\)

<tbc>_1-bit queries, where_

\(\Lambda(u)=1+log\frac{\sigma}{u}\)

_and_

\(\Gamma(u;K,J,\delta)=log\frac{K(J+1)}{\delta}+loglog\left(e^e\frac{\sigma}{u}\right)+loglog\left(e^e\frac{K(J+1)}{\delta}\right).\)

_Thus reuse preserves the order of Theorem 10._

_Proof._ Fix an arm _k_, and write _W<sub>k</sub>=X<sub>k</sub>-c<sub>k</sub>_. First note that _q<sub>s</sub>_ is a density on _I<sub>s</sub>_, and<tbc>

\(\sum_{s=0}^jA_s=\int_0^{L_j}\frac{dt}{max\{\sigma,t\}}=1+log\frac{L_j}{\sigma}=\alpha_j.\)

<tbc>Moreover, by the same tail-integral calculation used in Lemma 2,<tbc>

\(\mathbb{E}[Z_{k,s}]=\int_{I_s}\left(Pr(W_k\ge t)-Pr(W_k\le-t)\right)dt.\)

<tbc>Therefore

\(\sum_{s=0}^j\mathbb{E}[Z_{k,s}]=\mathbb{E}[[W_k]_{L_j}],\)

so the reusable phase-_j_ estimator is unbiased for the clipped target _c<sub>k</sub>_+E[[_W<sub>k</sub>]<sub>L<sub>j</sub></sub>_].

