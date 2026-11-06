<tbc>_Proof_ We first show _c\<_1. By the law of total variance,<tbc>

\(v=\mathbb{E}[\mathbb{V}(\theta|Y)]+\mathbb{V}(\mathbb{E}[\theta|Y])=\bar{v}+\mathbb{V}(\mathbb{E}[\theta|Y]).\)

<tbc>\(\mathbb{V}(\mathbb{E}[\theta|Y])>0\) since

\(\mathrm{Cov}(\mathbb{E}[\theta|Y],Y)=\mathbb{E}[\mathbb{E}[\theta|Y]\cdot Y]-\mathbb{E}[\mathbb{E}[\theta|Y]]\mathbb{E}[Y]=\mathbb{E}[\theta Y]-\mu^2=v,\)

so \(\bar{v}<v\) and \(c=\sqrt{\bar{v}/v}<1\).

Next we show the inequality for a fixed _q_. Fix \(q\in\mathcal{J}\) and let \(\phi_q(x):=(q-x)^+\). Since \(X_c=c\theta+(1-c)\mu\) is a convex combination of \(\theta\) and \(\mu\), convexity of \(\phi_q\) gives,<tbc>

\(\phi_q(X_c)\le c\phi_q(\theta)+(1-c)\phi_q(\mu).\)

<tbc>Taking expectations,<tbc>

\(\mathbb{E}[\phi_q(X_c)]\le c\mathbb{E}[\phi_q(\theta)]+(1-c)\phi_q(\mu)<\mathbb{E}[\phi_q(\theta)].\)

<tbc>The second inequality follows from Jensen’s inequality, and is strict since \(\Pi\) has continuous positive density on J and J is open so \(\mathbb{P}(\theta<q)>0\) and \(\mathbb{P}(\theta>q)>0\). Define

\(\delta(q):=\mathbb{E}[(q-\theta)^+]-\mathbb{E}[(q-X_c)^+]>0.\)

For any \(q'\in\mathbb{R}\), \(|(q'-x)^+-(q-x)^+|\le|q'-q|\) so \(\delta(q)\) is 2-Lipschitz and thus is continuous in _q_. Thus for compact _K_, \(\eta:=\mathrm{inf}_{q\in K}\delta(q)>0\). \(\square\)

LEMMA 7 (Every item is sampled infinitely often). _Under the hypotheses of Proposition 4, for every_ \(\theta^0\in\Theta^*\),

\(N_i(t)\rightarrow\infty\text{\textit{for every}}i=1,\dots,I\)

\(\mathbb{P}_{\theta^0}\)_-almost surely._

_Proof_ Fix \(\theta^0\in\Theta^*\) and a sample path in the probability-one event on which the conclusions of Lemma 5 hold. For the asymptotic claim, we consider the procedure of Algorithm 3 extended to infinitely many rounds, with \(B_t\in\mathbb{Z}_+\) for every _t_, thus \(\sum_{t=1}^TB_t\rightarrow\infty\) as \(T\rightarrow\infty\). Assume by contradiction that some items are sampled only finitely often, and define<tbc>

\(F:=\{i:\mathrm{sup}_{t\ge 1}N_i(t)<\infty\}.\)

<tbc>Since the sum of samples diverges, \(F^c\neq\varnothing\). All items \(i\in F\) eventually stop getting sampled, so for all sufficiently large _t_ we write \(\Pi_{i,t}=\Pi_i^\infty\), \(\mu_i(t)=\mu_i^\infty\), and \(v_i(t)=v_i^\infty>0\). For each \(j\notin F\), \(N_j(t)\rightarrow\infty\), so by Lemma 5, \(\mu_j(t)\rightarrow\theta_j^0\) and \(v_j(t)\rightarrow 0\). We begin by showing that each of _q_<sup>∗</sup>(_t_) and _q_<sup>†</sup>(_t_) is contained in a compact interval for all sufficiently large _t_. Choose \(a,b\in\mathcal{J}\) with \(a<\mathrm{min}_{j\in F^c}\theta_j^0\) and \(b>\mathrm{max}_{j\in F^c}\theta_j^0\). For each \(j\in F^c\), \(\mu_j(t)\rightarrow\theta_j^0\) and \(v_j(t)\rightarrow 0\), so Chebyshev’s inequality gives \(\mathbb{P}_t(\theta_j\ge a)\rightarrow 1\) and \(\mathbb{P}_t(\theta_j\ge b)\rightarrow 0\).<tbc>

