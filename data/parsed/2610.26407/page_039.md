<tbc>We first bound the logarithm of the likelihood product term. We have<tbc>

\(log\prod_{r=1}^m\frac{p_i(Y_r|x)}{p_i(Y_r|\theta_i^0)}=\{\eta_i(x)-\eta_i(\theta_i^0)\}\sum_{r=1}^mT_i(Y_r)-m\{A_i(\eta_i(x))-A_i(\eta_i(\theta_i^0))\}\)<br>
\(\ge-|\eta_i(x)-\eta_i(\theta_i^0)|\left|\sum_{r=1}^mT_i(Y_r)\right|-m|A_i(\eta_i(x))-A_i(\eta_i(\theta_i^0))|.\)

<tbc>To bound \(\left|\sum_{r=1}^mT_i(Y_r)\right|\), fix \(\varepsilon\in(0,1)\) and choose _M_ so that<tbc>

\(\mathbb{P}_{\theta_i^0}\left(max_{1\le r\le m}|T_i(Y_r)|\le M\right)\ge 1-\varepsilon.\)

<tbc>If \(max_{1\le r\le m}|T_i(Y_r)|\le M\), then \(\left|\sum_{r=1}^mT_i(Y_r)\right|\le mM\). By continuity of \(\eta_i\) and _A<sub>i</sub>_, choose \(V=[\theta_i^0-\delta,\theta_i^0+\delta]\subset\mathcal{J}\) so that for \(x\in V\)<tbc>

\(mM|\eta_i(x)-\eta_i(\theta_i^0)|+m|A_i(\eta_i(x))-A_i(\eta_i(\theta_i^0))|\le\varepsilon.\)

<tbc>Thus, whenever \(max_{1\le r\le m}|T_i(Y_r)|\le M\), for \(x\in V\) we have<tbc>

\(\prod_{r=1}^m\frac{p_i(Y_r|x)}{p_i(Y_r|\theta_i^0)}\ge e^{-\varepsilon}.\)

<tbc>Plugging this into the expression for \(\bar{v}_i(t,m)\) gives

\(\bar{v}_i(t,m)\ge e^{-\varepsilon}(1-\varepsilon)min_{a\in\mathbb{R}}\int_V(x-a)^2\Pi_{i,t}(dx)\ge e^{-\varepsilon}(1-\varepsilon)\left\{v_i(t)-(U-L)^2\Pi_{i,t}(V^c)\right\}.\)

For the second inequality, the minimizing _a_ belongs to _V_ . The integral over _V<sup>c</sup>_ is therefore at most \((U-L)^2\Pi_{i,t}(V^c)\), while the integral over J is at least _v<sub>i</sub>(t_).

By (20) and \(-n^{-1}logv_{i,n}\rightarrow 0\), \(\Pi_{i,t}(V^c)/v_i(t)\rightarrow 0\) when \(N_i(t)\rightarrow\infty\). Dividing by _v<sub>i</sub>(t_) and taking the liminf gives

\(liminf_{t\rightarrow\infty}\frac{\bar{v}_i(t,m)}{v_i(t)}\ge e^{-\varepsilon}(1-\varepsilon).\)

Letting \(\varepsilon\downarrow 0\) proves (19). \(\square\)

_Proof of Theorem 1_ We first show that every item is sampled infinitely often. Since \(q(t)\rightarrow q_0\in(\theta_{k+1}^0,\theta_k^0)\), eventually _q(t_) belongs to a compact interval \(K\subset\mathcal{J}\) . The proof of Lemma 7 then applies, using Lemma 9 for items sampled infinitely often and Lemma 6 for items that stop receiving samples. Thus \(N_i(t)\rightarrow\infty\) and \(\mu_i(t)\rightarrow\theta_i^0\) for every _i_.

For part (i), we first establish the rates of _D<sub>i,t</sub>(d_). We will show that<tbc>

\(max_{0\le d<B}\left|-\frac{logD_{i,t}(d)}{N_i(t)}-d_i(\theta_i^0,q_0)\right|\longrightarrow 0.\) (21)

<tbc>We will then use these rates and optimality of each batch to prove \(\widehat{w}_i(t)\rightarrow w_i(q_0)\). To prove (21), define<tbc>

\(J_{i,t}(d):=\ell_{i,t}(d)-(q(t)-\mu_i(t))^+.\)

<tbc>We first establish the bounds<tbc>

\(\frac{\bar{v}_i(t,B-1)}{2\mathbb{V}_t(Y)}J_{i,t}(B-1)\le D_{i,t}(d)\le J_{i,t}(0),0\le d<B,\) (22)

