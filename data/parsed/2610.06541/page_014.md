The _T_ factors are ordered by decreasing sample index. The piece for sample _H(j/T_) is \([j-\frac{1}{2},j+\frac{1}{2}]\cap[0,T]\), a full unit interval for 0_\<j\<T_ and a half interval for _j_=0_,T_. The _rounded clock_ is \(q(t)=\lfloor t+1/2\rfloor\) for \(t\ge 0\).

For \(\mu_\mathrm{c}=\sum_{j\ge 0}\delta_{j+1/2}\), the rounded clock is \(q(t)=[t]_{\mu_\mathrm{c}}\). Thus, _q(t_)=_j_ on \([j-1/2,j+1/2)\cap[0,T]\), including the half pieces at _j_=0_,T_, so the Hamiltonian _H(q(t)/T_) is constant on these intervals. If _V_ is its evolution, then (2.2) and the endpoint half pieces give

(6.2) \(W_T=e^{iH(1)/2}V(T)e^{-iH(0)/2}.\)

This includes _T_=1, when there are no full pieces.

## 6.1. The comparison with the path.

We compare _W<sub>T</sub>_ with _U(T_) one piece at a time. Freezing the generator at each sample leaves a first-order error \(\tau D\), whose norms sum to _O_(1) over _T_ pieces, so we remove this linear drift from the comparison by inserting 1-_iY_ . Stein’s equation \(e^{ih}\bar{Y}e^{-ih}-\bar{Y}=R\), the discrete- time Sylvester or Lyapunov equation of Stein \[26\], determines the endpoint value \(\bar{Y}\), where _R_ is the integral of the conjugated linear drift below. We then extend \(\bar{Y}\) across the piece by \(\dot{Y}+i[h,Y]=\tau D\), so that _Y_ has the same value at both ends and neighboring endpoint corrections nearly cancel. Under the bounds below, only their differences and the second-order remainders accumulate, giving _O_(1_/T_) by (5.1).

**Lemma 6.2.** _Let h be Hermitian, with the frame operator_ \(\Theta_h\) _defined and_ \(\|\Theta_h\|\le N\)_, let D be any matrix, and let K be a continuous Hamiltonian on_ \([-\frac{1}{2},\frac{1}{2}]\)_. Put_ \(\bar{Y}=\Theta_h(D)\), \(\Delta(\tau)=K(\tau)-h\)_, and_ \(\omega(\tau)=N+\frac{1}{8}-\tau^2/2\).

(1) _The solution of_ \(\dot{Y}+i[h,Y]=\tau D\), \(Y(-\frac{1}{2})=\bar{Y}\)_, satisfies_ \(Y(\frac{1}{2})=\bar{Y}\).<tbc>

(2) _For unitary evolutions_ \(i\dot{U}=KU\), \(i\dot{V}=hV\)_, the comparison M=U_<sup>†</sup>(1-_iY)V satisfies_<tbc>

<tbc>\(\|M(\frac{1}{2})-M(-\frac{1}{2})\|\le\int_{-1/2}^{1/2}\big[\|\Delta(\tau)-\tau D\|+\omega(\tau)\|\Delta(\tau)\|\|D\|\big]d\tau.\)<tbc>

<tbc>_Proof._ Substituting \(\sigma=\tau+\frac{1}{2}\) in (2.5) gives<tbc>

\(e^{ih}\bar{Y}e^{-ih}-\bar{Y}=\int_{-1/2}^{1/2}\tau e^{i(\tau+1/2)h}De^{-i(\tau+1/2)h}d\tau=R.\)

<tbc>Write _E(s_)=_se_<sup>_i(s_+1/2)_h_</sup>_De_<sup>-_i(s_+1/2)_h_</sup>, so that \(\|E(s)\|=|s|\|D\|\). Then

\(Y(\tau)=e^{-i(\tau+1/2)h}\big[\bar{Y}+\int_{-1/2}^\tau E(s)ds\big]e^{i(\tau+1/2)h}\text{variation of constants,}\)<br>
\(=e^{-i(\tau-1/2)h}\big[\bar{Y}-\int_\tau^{1/2}e^{-ih}E(s)e^{ih}ds\big]e^{i(\tau-1/2)h}\text{by the Stein equation,}\)<br>
\(\|Y(\tau)\|\le\big(N+\int_{|\tau|}^{1/2}sds\big)\|D\|=\omega(\tau)\|D\|\text{first line if}\tau\le 0\text{, second if}\tau\ge 0\text{,}\)

by unitary invariance and \(\|\bar{Y}\|\le N\|D\|\), and the second line at \(\tau=\frac{1}{2}\) gives \(Y(\frac{1}{2})=\bar{Y}\). The product rule and the equation for _Y_ give \(\dot{M}=U^\dagger[i(\Delta-\tau D)+\Delta Y]V\) , so integration and \(\|\Delta Y\|\le\|\Delta\|\|Y\|\) give (2). □

By Lemma 2.9, the bound _N_ may be \(N_\gamma\) under separation, or N(_w_) at width at most \(w<2\pi\).

**Definition 6.3.** For the unit-step comparison, using the frame-operator bounds \(N_\gamma\) and \(N'_\gamma\) of Lemma 2.9, define

(6.3) \(c_0=\frac{1}{4}+2N_\gamma,c_1=\frac{1}{64}+\frac{1}{4}N_\gamma+N'_\gamma,c_2=\frac{1}{12}+2N_\gamma.\)

At width \(w<2\pi\), write _c<sub>i</sub>(w_) for the explicit values obtained by replacing \(N_\gamma,N'_\gamma\) with \(\mathcal{N}(w),2\mathcal{N}'(w)\).

Euler’s bound \(|B_n|/n!\le 4(2\pi)^{-n}\) majorizes the series \(\mathcal{N}(w)=\sum_{m\ge 0}|B_{2m+2}|w^{2m}/(2m+2)!\) (proof of Lemma 2.9) and its derivative termwise, and \(4\pi^2-w^2=\gamma(2\pi+w)\) for \(\gamma=2\pi-w\), so

(6.4) \(\mathcal{N}(w)\le\frac{4}{4\pi^2-w^2}\le\frac{2}{\pi\gamma},\mathcal{N}'(w)\le\frac{8w}{(4\pi^2-w^2)^2}\le\frac{2}{\pi\gamma^2}(0<w<2\pi).\)

