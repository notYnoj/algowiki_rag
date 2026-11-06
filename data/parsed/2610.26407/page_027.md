<tbc>Define \(\Delta'\) by transferring one sample from _i_ to _j_: \(\Delta'_i=\Delta_i-1\), \(\Delta'_j=\Delta_j+1\), and \(\Delta'_\ell=\Delta_\ell\) for \(\ell\notin\{i,j\}\). Then \(\sum_\ell\Delta'_\ell=B_t\), and

\(G(\Delta')-G(\Delta)=D_{j,t}(\Delta_j)-D_{i,t}(\Delta_i-1)\ge 0.\)

Repeating these exchanges transforms \(\Delta\) into \(\Delta^G\) without ever decreasing the gain. Therefore \(G(\Delta^G)\ge G(\Delta)\), and \(\Delta^G\) minimizes \(\sum_j\ell_{j,t}(\Delta_j)\) over the feasible set. \(\square\)

_Proof of Proposition 2(ii)_ Fix item _i_ and round _t_, and write _c(d_):=_c<sub>i</sub>(t,d_), \(\lambda:=\lambda_i(t)\), \(\ell(d):=\ell_{i,t}(d)\), \(\theta:=\theta_i\), \(\mu:=\mu_i(t)\), _q_:=_q(t_), and \(\pi(\cdot)\) for the density of the posterior \(\Pi_{i,t}\). By the definitions of \(\widetilde{\theta}_i(d)\) and \(\ell_{i,t}(d)\),

\(\ell(d)=\mathbb{E}\big[(q-\mu-c(d)(\theta-\mu))^+\big].\)

We will relax \(\ell(\cdot)\) to the reals \(d\ge 0\) and show \(\ell\) is convex in _d_, thus \(D_{i,t}(d)=\ell(d)-\ell(d+1)\) is nonincreasing in \(d\in\mathbb{Z}_{\ge 0}\), which is (9).

We first compute the derivatives of _c_. By assumption, \(c(d)=(1+\lambda d)^{-1/2}\), so

\(c'(d)=-\frac{\lambda}{2}(1+\lambda d)^{-3/2}=-\frac{\lambda}{2}c(d)^3.\)

Differentiating again,<tbc>

\(c''(d)=-\frac{\lambda}{2}\cdot 3c(d)^2\cdot c'(d)=-\frac{\lambda}{2}\cdot 3c(d)^2\cdot\big(-\frac{\lambda}{2}c(d)^3\big)=\frac{3\lambda^2}{4}c(d)^5\ge 0.\)

<tbc>Next we differentiate \(\ell\). Let \(U(d):=\mu+(q-\mu)/c(d)\) so<tbc>

\(\ell(d)=\int_\mathbb{R}\big(q-\mu-c(d)(\theta-\mu)\big)^+\pi(\theta)d\theta=\int_{-\infty}^{U(d)}\big(q-\mu-c(d)(\theta-\mu)\big)\pi(\theta)d\theta.\)

<tbc>Define \(I(\tau):=\int_{-\infty}^\tau(\theta-\mu)\pi(\theta)d\theta\), taking \(\pi=0\) outside J . Since \(\mathbb{E}[|\theta-\mu|]<\infty\), differentiating under the expectation gives<tbc>

\(\ell'(d)=-c'(d)\int_{-\infty}^{U(d)}(\theta-\mu)\pi(\theta)d\theta=-c'(d)I(U(d)).\)

<tbc>For \(U(d)\in\mathcal{J}\), differentiating again gives

\(\ell''(d)=-c''(d)I(U(d))-c'(d)I'(U(d))U'(d)\)<br>
\(=-c''(d)I(U(d))-c'(d)\cdot\frac{q-\mu}{c(d)}\pi(U(d))\cdot\big(-\frac{q-\mu}{c(d)^2}c'(d)\big)\)<br>
\(=-c''(d)I(U(d))+c'(d)^2\frac{(q-\mu)^2}{c(d)^3}\pi(U(d)).\)

Both terms are nonnegative. To see this, \(c''(d)\ge 0\), and \(I(\tau)\le 0\) for \(\tau\le\mu\). For \(\tau\ge\mu\), using \(\mathbb{E}[\theta-\mu]=0\) gives

\(I(\tau)=-\int_\tau^\infty(\theta-\mu)\pi(\theta)d\theta\le 0.\)

Thus \(\ell''(d)\ge 0\) whenever \(U(d)\in\mathcal{J}\). On any interval where _U(d_) is outside J, \(\ell\) is constant. Since \(\ell'(d)=-c'(d)I(U(d))\) is continuous also when _U(d_) crosses an endpoint of J, \(\ell'\) is nondecreasing on \([0,\infty)\). Therefore \(\ell\) is convex, so _D<sub>i,t</sub>(d_) is nonincreasing in _d_. \(\square\)

