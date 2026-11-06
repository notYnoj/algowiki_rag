\(\le\frac{Bd_i(\theta_i^0,q_0)}{\sum_jN_j(t)}+2\varepsilon_{\tau_i(t)}\longrightarrow 0.\)

<tbc>Dividing by \(d_i(\theta_i^0,q_0)\), summing over _i_, and using \(\sum_i\widehat{w}_i(t)=1\) gives

\(\frac{min_jd_j(\theta_j^0,q_0)N_j(t)}{\sum_jN_j(t)}\longrightarrow\left(\sum_i\frac{1}{d_i(\theta_i^0,q_0)}\right)^{-1}.\)

Hence

\(\widehat{w}_i(t)\longrightarrow\frac{1/d_i(\theta_i^0,q_0)}{\sum_j1/d_j(\theta_j^0,q_0)}=w_i(q_0),\)

proving part (i). Part (ii) follows from Lemma 8 and continuity of \(\Gamma\).

For part (iii), \(w_i(q_0)d_i(\theta_i^0,q_0)=\left(\sum_{\ell=1}^I1/d_\ell(\theta_\ell^0,q_0)\right)^{-1}\) for every _i_. For any \(i\le k<j\) and \(x\in[\theta_j^0,\theta_i^0]\), monotonicity gives

\(w_i(q_0)d_i(\theta_i^0,x)+w_j(q_0)d_j(\theta_j^0,x)\ge\left\{w_i(q_0)d_i(\theta_i^0,q_0)=\left(\sum_{\ell=1}^I1/d_\ell(\theta_\ell^0,q_0)\right)^{-1},x\le q_0,w_j(q_0)d_j(\theta_j^0,q_0)=\left(\sum_{\ell=1}^I1/d_\ell(\theta_\ell^0,q_0)\right)^{-1},x\ge q_0.\right.\)

Taking the minimum over _x_ and then over \(i\le k<j\) in (12) gives \(\Gamma(w(q_0);\theta^0)\ge\left(\sum_{\ell=1}^I1/d_\ell(\theta_\ell^0,q_0)\right)^{-1}\). □

_Proof of Remark 3_ Fix **_x_** with _x_<sub>\[_k_\]</sub>_\>x_<sub>\[_k_+1\]</sub>. The objective \(\sum_i1/d_i(x_i,q)\) is continuous on (_x_<sub>\[_k_+1\]</sub>_,x_<sub>\[_k_\]</sub>) and tends to infinity at its endpoints, so it attains a minimum. We prove uniqueness for each family by strict convexity in _q_ or in a strictly increasing function of _q_.

For Gaussian observations, each term is strictly convex in _q_, since<tbc>

\(\frac{1}{d_i(x_i,q)}=\frac{2\sigma_i^2}{(x_i-q)^2},\frac{d^2}{dq^2}\frac{1}{d_i(x_i,q)}=\frac{12\sigma_i^2}{(x_i-q)^4}>0.\)

<tbc>For lognormal observations, set _z_=log_q_. Then<tbc>

\(\frac{1}{d_i(x_i,e^z)}=\frac{2\sigma_i^2}{(logx_i-z)^2},\frac{d^2}{dz^2}\frac{1}{d_i(x_i,e^z)}=\frac{12\sigma_i^2}{(logx_i-z)^4}>0.\)

<tbc>For Bernoulli observations, write _q=e<sup>z</sup>/_(1+_e<sup>z</sup>_). We show that 1_/d<sub>i</sub>(x<sub>i</sub>,q_) is strictly convex in _z_. Differentiating gives<tbc>

\(\frac{d^2}{dz^2}\frac{1}{d_i(x_i,q)}=\frac{2(q-x_i)^2-d_i(x_i,q)q(1-q)}{d_i(x_i,q)^3}.\)

<tbc>To show that the numerator is positive, we bound _d<sub>i</sub>(x<sub>i</sub>,q_) from above. Using \(logu\le u-1\),<tbc>

\(d_i(x_i,q)=x_ilog\frac{x_i}{q}+(1-x_i)log\frac{1-x_i}{1-q}\le x_i\left(\frac{x_i}{q}-1\right)+(1-x_i)\left(\frac{1-x_i}{1-q}-1\right)=\frac{(x_i-q)^2}{q(1-q)}.\)

<tbc>Substituting gives

\(\frac{d^2}{dz^2}\frac{1}{d_i(x_i,q)}\ge\frac{(q-x_i)^2}{d_i(x_i,q)^3}>0,\)

since \(q\in(x_{[k+1]},x_{[k]})\) implies \(q\neq x_i\).

