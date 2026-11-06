\(\ell_i^\mathrm{far}(x',y')\) for some _i_=1,2 and some \((x',y')\in\mathcal{B}_{Q_1}(r,c)\). In this case (_x,y_) shares a toroidal diagonal with one of \((r,y')\) and \((x',c)\). Hence, one of the following hold modulo _n_:<tbc>

\(x+y=r+y',x-y=r-y',x+y=x'+c,x-y=x'-c.\)

<tbc>For each \(x'\) that solves one of these equations, there is at most one \(y'\) such that \((x',y')\in Q_1\). Similarly, for each \(y'\) solving an equation there is at most one \(x'\) such that \((x',y')\in Q_1\). Therefore, in this way, adding (_x,y_) to _Q_<sub>1</sub> may contribute at most 4 absorbers to S<sub>_Q_<sub>2</sub></sub>(_r,c_). In summary:

\(|\mathcal{S}_{Q_2}(r,c)\backslash\mathcal{S}_{Q_1}(r,c)|\le 5,\)

as desired. □

_Proof of Claim 4.13._ We will now show that for \(\beta:=(40e)^{-5}\) with high probability \(\tilde{R}\) contains at least \(\beta n\) safe absorbers for every position.

Let \((r,c)\in[n]^2\). We will show that

\(\mathbb{P}\left[|\mathcal{S}_\tilde{R}(r,c)|<\beta n\right]\le\mathrm{exp}\left(-\Omega(n)\right).\)

A union bound over the _n_<sup>2</sup> positions will then imply that w.h.p. this holds simultaneously for all positions.

Let \(X_{(r,c)}:=|\mathcal{S}_\tilde{R}(r,c)|\). We will apply Theorem 4.11 to _X_<sub>(_r,c_)</sub>. For \((x,y)\in[n]^2\), let _Y_<sub>(_x,y_)</sub> indicate the event \((x,y)\in R\). Then the random variables \(\{Y_{(x,y)}\}_{(x,y)\in[n]^2}\) are independent. Furthermore, each _Y_<sub>(_x,y_)</sub> has Bernoulli distribution with parameter _p_. Additionally, \(R,\tilde{R}\), and hence _X_<sub>(_r,c_)</sub> are determined by these random variables. Therefore _X_<sub>(_r,c_)</sub> is a function of the i.i.d. Bernoulli random variables \(\{Y_{(x,y)}\}_{(x,y)\in[n]^2}\).

We note that adding a queen (_x,y_) to _R_ changes \(\tilde{R}\) by at most 4. Indeed, if (_x,y_) is the unique queen in the lines incident to it in _R_, then \(|\tilde{R}|\) increases by one. On the other hand, (_x,y_) occupies four lines. If any of these contains a queen from \(\tilde{R}\), then that queen will be removed from \(\tilde{R}\) once (_x,y_) is added to _R_. Hence, \(|\tilde{R}|\) may decrease by at most 4. Hence, By Claim 4.14, changing the value of some _Y_<sub>(_x,y_)</sub> can change the value of _X_<sub>(_r,c_)</sub> by at most 20.

Next we bound E_X_<sub>(_r,c_)</sub> from below, with the goal of showing that \(\mathbb{E}X_{(r,c)}-\beta n=\Omega(n)\). By Claim 4.10 there are at least _n_<sup>2</sup>/5 positions (_x,y_) such that (_r,c_) and (_x,y_) do not share a line and (_r,y),(x,c_) are balanced. Let _P_ be the set of these positions. For each \((x,y)\in P\) let _Z_<sub>(_x,y_)</sub> indicate the event that \((x,y)\in\mathcal{S}_\tilde{R}(r,c)\). Then<tbc>

\(X_{(r,c)}\ge\sum_{(x,y)\in P}Z_{(x,y)}.\)

<tbc>By Claim 4.6:<tbc>

\(\mathbb{E}Z_{(x,y)}=\mathbb{P}[Z_{(x,y)}=1]\ge|\ell_1^\mathrm{far}(r,y)||\ell_2^\mathrm{far}(r,y)||\ell_1^\mathrm{far}(x,c)||\ell_2^\mathrm{far}(x,c)|p^5(1-p)^{20n}-O\left(\frac{1}{n^2}\right).\)

<tbc>If \((x,y)\in P\) then (_r,y_) and (_x,c_) are balanced. Thus:<tbc>

\(|\ell_1^\mathrm{far}(r,y)||\ell_2^\mathrm{far}(r,y)||\ell_1^\mathrm{far}(x,c)||\ell_2^\mathrm{far}(x,c)|\ge\left(\frac{n}{10}\right)^4.\)

