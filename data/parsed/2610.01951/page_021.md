_Proof of Lemma D.1._ For each arm \(i\in[K]\), let \((Y_{i,s})_{s\ge 1}\) be the reward sequence of arm _i_, indexed by pull number. Since arm _i_ is Bernoulli\((\mu_i)\), the sequence \((Y_{i,s})_{s\ge 1}\) is i.i.d. Bernoulli\((\mu_i)\). For \(n\ge 1\), define

\(\overline{Y_{i,n}}:=\frac{1}{n}\sum_{s=1}^nY_{i,s}.\)

By construction,

\(\widehat{\mu}_{t,i}=\overline{Y_{i,N_{t,i}}}\text{for all}t\ge K.\)

Since the algorithm pulls each arm once initially, \(N_{t,i}\ge 1\).

Apply the one-dimensional time-uniform KL confidence-sequence bound for one-parameter exponential families from Kaufmann and Koolen \[13, Section 3.3.2, Equation (14)\], specialized to Bernoulli distributions. There is a universal constant _c_<sub>0</sub>_\>_0 such that, for every \(\gamma\in(0,1)\), there exists an event \(\mathcal{E}_i(\gamma)\) with \(\mathbb{P}_\mu(\mathcal{E}_i(\gamma))\ge 1-\gamma\) and such that, on \(\mathcal{E}_i(\gamma)\), simultaneously for all \(n\ge 1\),

\(nd(\overline{Y_{i,n}},\mu_i)\le c_0\left(log\frac{1}{\gamma}+loglog(en)\right).\)

Choose \(\gamma=\eta/K\) and define \(\mathcal{K}_\eta:=\cap_{i=1}^K\mathcal{E}_i(\eta/K)\). A union bound gives \(\mathbb{P}_\mu(\mathcal{K}_\eta)\ge 1-\eta\).

Because the confidence-sequence bound is uniform over all \(n\ge 1\), we may evaluate it at the random sample size _n=N<sub>t,i</sub>_. On \(\mathcal{K}_\eta\), simultaneously for all \(t\ge K\) and all \(i\in[K]\),

\(N_{t,i}d(\widehat{\mu}_{t,i},\mu_i)\le c_0\left(log\frac{K}{\eta}+loglog(eN_{t,i})\right)\le c_0\left(log\frac{K}{\eta}+loglog(et)\right).\)

Pinsker’s inequality, \(d(p,q)\ge 2(p-q)^2\), yields the displayed radius bound.

## D.2 Local Lipschitz control of the Bernoulli GLR

**Lemma D.2** (Bregman representation and local Lipschitz control)**.** _Fix_ \(m,\ell\ge 1\) _and_ \(p,q\in(0,1)\)_. Let_<tbc>

\(\alpha:=\frac{m}{m+\ell},F(x):=xlogx+(1-x)log(1-x),\)

<tbc>_with the continuous extension to_ \[0,1\]_. Then_<tbc>

\(V_{m,\ell}(p,q)=(m+\ell)\left[\alpha F(p)+(1-\alpha)F(q)-F(\alpha p+(1-\alpha)q)\right],\)

<tbc>_where_<tbc>

\(V_{m,\ell}(p,q):=inf_{x\in(0,1)}\left\{md(p,x)+\ell d(q,x)\right\}.\)

<tbc>_Moreover, for every_ \(\varepsilon\in(0,1/2)\) _and all_ \(p,q,u,v\in[\varepsilon,1-\varepsilon]\),<tbc>

\(|V_{m,\ell}(p,q)-V_{m,\ell}(u,v)|\le\frac{2}{\varepsilon(1-\varepsilon)}\frac{m\ell}{m+\ell}\left(|p-u|+|q-v|\right).\)

<tbc>_Proof of Lemma D.2._ The minimizer in the definition of \(V_{m,\ell}(p,q)\) is \(r=\alpha p+(1-\alpha)q\). Substitution gives the Bregman representation.

For the Lipschitz bound, write<tbc>

\(V_{m,\ell}(p,q)=(m+\ell)\left[\alpha F(p)+(1-\alpha)F(q)-F(r)\right],r=\alpha p+(1-\alpha)q.\)

<tbc>Then<tbc>

\(\partial_pV_{m,\ell}(p,q)=m(F'(p)-F'(r)),\partial_qV_{m,\ell}(p,q)=\ell(F'(q)-F'(r)).\)

<tbc>Since \(F''(x)=1/[x(1-x)]\), on \([\varepsilon,1-\varepsilon]\) one has<tbc>

\(|F'(x)-F'(y)|\le\frac{|x-y|}{\varepsilon(1-\varepsilon)}.\)

<tbc>Moreover,<tbc>

\(|p-r|=(1-\alpha)|p-q|\le 1-\alpha,|q-r|=\alpha|p-q|\le\alpha.\)

<tbc>Thus

\(|\partial_pV_{m,\ell}(p,q)|\le\frac{m(1-\alpha)}{\varepsilon(1-\varepsilon)}=\frac{m\ell}{m+\ell}\frac{1}{\varepsilon(1-\varepsilon)},\)

and the same bound holds for \(|\partial_qV_{m,\ell}(p,q)|\). Applying the mean value theorem first in the _p_ coordinate and then in the _q_ coordinate proves the displayed inequality. The factor 2 is a harmless slack that keeps the bound uniform over the two coordinate changes.

