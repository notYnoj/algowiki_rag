<tbc>We next compute the expected post-round-_t_ posterior variance of \(\theta_i=e^{\eta_i}\), rather than of \(\eta_i\). After \(\Delta_i\) further samples, \(\eta_i\) has Gaussian posterior with deterministic variance<tbc>

\(s_i^2(\Delta_i):=\left(\frac{1}{s_i^2}+\frac{\Delta_i}{\sigma_i^2}\right)^{-1}\)

<tbc>and random mean \(M_i(\Delta_i)\). The Gaussian update and the law of total variance give<tbc>

\(M_i(\Delta_i)|\mathcal{H}_t\sim N(m_i,s_i^2-s_i^2(\Delta_i)).\)

<tbc>Conditional on \(M_i(\Delta_i)\), \(\theta_i\) is lognormal with parameters \((M_i(\Delta_i),s_i^2(\Delta_i))\), so<tbc>

\(\mathbb{V}(\theta_i|M_i(\Delta_i))=(e^{s_i^2(\Delta_i)}-1)e^{2M_i(\Delta_i)+s_i^2(\Delta_i)}.\)

<tbc>The Gaussian MGF gives \(\mathbb{E}_t[e^{2M_i(\Delta_i)}]=exp(2m_i+2(s_i^2-s_i^2(\Delta_i)))\), so

\(\bar{v}_i(t,\Delta_i)=(e^{s_i^2(\Delta_i)}-1)e^{2m_i+2s_i^2-s_i^2(\Delta_i)},c_i(t,\Delta_i)^2=\frac{1-e^{-s_i^2(\Delta_i)}}{1-e^{-s_i^2}}.\)

This does not have the form (10) in general, so Proposition 2(ii) does not apply.

Finally, for _z\>_0,

\(\mathbb{E}_t[(z-\theta_i)^+]=z\Phi\left(\frac{logz-m_i}{s_i}\right)-\mu_i(t)\Phi\left(\frac{logz-m_i-s_i^2}{s_i}\right).\)

Combined with \(c_i(t,\Delta_i)\) and (7), this yields the closed form for \(\ell_{i,t}(\Delta_i)\).

## Appendix C: Proofs for §4

## C.1. Proof of consistency

To prove Proposition 4 we first prove three useful lemmas.

LEMMA 5 (**Conditional posterior consistency**). _Under Assumption 1, there exists a set_ \(\Theta^*\subseteq\mathcal{J}^I\) _with prior probability one such that, for every_ \(\theta^0\in\Theta^*\)_, almost surely under_ \(\mathbb{P}_{\theta^0}\)_: if_ \(N_i(t)\rightarrow\infty\) _as_ \(t\rightarrow\infty\)_, then_ \(\mu_i(t)\rightarrow\theta_i^0\) _and_ \(v_i(t)\rightarrow 0\).

_Proof_ For each _i_, Assumption 1 provides the conditions for Doob’s theorem (Doob 1949, Miller 2018): the mean-parametrization \(\mathbb{E}_\theta[Y_{i,n}]=\theta\) makes the family \(\{P_i(\cdot|\theta):\theta\in\mathcal{J}\}\) identifiable, and \(\mathbb{E}_{\Pi_{i,0}}[\theta_i^2]<\infty\) allows the choice \(g(\theta_i)=\theta_i^2\). Doob’s theorem applied to \(g(\theta_i)=\theta_i\) and \(g(\theta_i)=\theta_i^2\) gives a set \(J_i^*\subseteq\mathcal{J}\) with \(\Pi_{i,0}(J_i^*)=1\) such that, for every \(\theta_i^0\in J_i^*\), \(\mathbb{P}_{\theta_i^0}\)-almost surely: if \(N_i(t)\rightarrow\infty\), then \(\mu_i(t)\rightarrow\theta_i^0\) and \(\mathbb{E}_t[\theta_i^2]\rightarrow(\theta_i^0)^2\). Thus, \(v_i(t)=\mathbb{E}_t[\theta_i^2]-\mu_i(t)^2\rightarrow 0\). Define \(\Theta^*:=J_1^*\times\cdots\times J_I^*\subseteq\mathcal{J}^I\). Since the priors are independent across items, \(\Theta^*\) has prior probability \(\prod_{i=1}^I\Pi_{i,0}(J_i^*)=1\). □

LEMMA 6 (**Uniform improvement from one observation**). _Let_ \(\Pi\) _be a distribution on_ J _with continuous positive density, mean_ \(\mu:=\mathbb{E}_\Pi[\theta]\)_, and variance_ \(v:=\mathbb{V}_\Pi(\theta)>0\)_. Let_ \(\theta\sim\Pi\) _and_ \(Y|\theta\sim P(\cdot|\theta)\) _with_ \(\mathbb{E}[Y|\theta]=\theta\) _and finite predictive second moment_ \(\mathbb{E}[Y^2]<\infty\)_. Define_ \(\bar{v}:=\mathbb{E}[\mathbb{V}(\theta|Y)]\), \(c:=\sqrt{\bar{v}/v}\)_, and_ \(X_c:=\mu+c(\theta-\mu)\)_. Then c\<_1_, and for every compact_ \(K\subset\mathcal{J}\) _there exists_ \(\eta>0\) _such that_<tbc>

\(\mathbb{E}[(q-\theta)^+]-\mathbb{E}[(q-X_c)^+]\ge\eta\text{\textit{for every}}q\in K.\)

