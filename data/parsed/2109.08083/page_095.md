<tbc>The following proposition about the weight transferred over legal zero-sum configurations will be useful in proving the induction step.

Proposition 6.14. _Suppose we have reached iteration i of Algorithm 6.9 (where we transfer weight from all_ (_c<sub>g</sub>-i_+1)_-bad edges in H_<sub>1</sub>_), and we have that for every_ (_c<sub>g</sub>-i_+1)_-bad edge e,_

(6.9) \(w_1(e)(1-O(log^{-1}(n)))\le w_{(1,c_g-i+1)}(e)\le w_1(e)+\sum_{j=1}^{i-1}O\left(\frac{k_{c_g-j+1}}{p_\mathrm{gr}^3t_1^2}\right).\)

_Then every_ (_c<sub>g</sub>-i_+1)_-legal zero-sum configuration_ \(z\in\mathcal{Z}_{c_g-i+1,H_1}\) _carries a weight w(z_) _satisfying_

\(w(z)=\Theta\left(\frac{1}{p_\mathrm{gr}^{15}j_{c_g-i+1}t_1^2}\right).\)

Proof. It is clear by construction that this is the case for \(z\in\mathcal{Z}_{c_g-i+1,H_1}^2\). Consider now an edge _e_<sub>_c<sub>g</sub>-i_+1</sub> which is a (_c<sub>g</sub>-i_+1)-bad edge, and a configuration \(z\in\mathcal{Z}_{c_g-i+1,e_{c_g-i+1},H_1}^+(\mathrm{bad})\). First note that \(i\le c_g\) and hence for every iteration we have that \(\sum_{j=1}^{i-1}O\left(\frac{k_{c_g-j+1}}{p_\mathrm{gr}^3t_1^2}\right)\le O\left(\frac{c_gk_2}{p_\mathrm{gr}^3t_1^2}\right)\). Since \(c_g=\lceil\frac{0.99999\mathrm{log}(t_1)}{\mathrm{loglog}(n)}\rceil\), and \(k_2=\frac{t_1}{\mathrm{log}^3(n)}\), we get \(\sum_{j=1}^{i-1}O\left(\frac{k_{c_g-j+1}}{p_\mathrm{gr}^3t_1^2}\right)=O\left(\frac{1}{p_\mathrm{gr}^3t_1\mathrm{log}^2(n)\mathrm{loglog}(n)}\right)\), and in particular that

\(w_{(1,c_g-i+1)}(e)=\left(1\pm O\left(\mathrm{log}^{-1}(n)\right)\right)w_1(e).\)

Note that by Corollary 6.13 and Theorem 6.1 we have that

\(\sum_{z\in\mathcal{Z}_{c_g-i+1,e_{c_g-i+1},H_1}^2}w(z)=O\left(k_{c_g-i+1}t_1p_\mathrm{gr}^{12}\cdot\frac{1}{p_\mathrm{gr}^{15}j_{c_g-i+1}t_1^2}\right)\)<br>
\(=O\left(\frac{1}{p_\mathrm{gr}^3t_1\mathrm{log}(n)}\right)=O(w_1(e_{c_g-i+1})\mathrm{log}^{-1}(n)).\)

It follows, again using Corollary 6.13, as well as the assumption on _w_<sub>(1_,c<sub>g</sub>-i_+1)</sub>(_e_) for each (_c<sub>g</sub>-i_+1)-bad edge above, that

\(w(z)=\frac{w_{1,c_g-i+1}(e_{c_g-i+1})-\sum_{z\in\mathcal{Z}_{c_g-i+1,e_{c_g-i+1},H_1}^2}w(z)}{|\mathcal{Z}_{c_g-i+1,e_{c_g-i+1},H_1}^+(\mathrm{bad})\backslash\mathcal{Z}_{c_g-i+1,H_1}^2|}\)<br>
\(=\Theta\left(\frac{1}{p_\mathrm{gr}^3t_1}\cdot\frac{1}{p_\mathrm{gr}^{12}j_{c_g-i+1}t_1}\right)\)<br>
\(=\Theta\left(\frac{1}{p_\mathrm{gr}^{15}j_{c_g-i+1}t_1^2}\right),\)

as required. □

We now consider _w_<sub>(1_,c<sub>g</sub>-i_)</sub> for every \(i\in[c_g]\).

Lemma 6.15. _For every_ \(i\in[c_g]\) _the following holds:_

(_i)_ _w_<sub>(1_,c<sub>g</sub>-i_)</sub>(_e_)=0 _for every l-bad edge, where l\>c<sub>g</sub>-i,_<tbc>

_(ii)_ \(w_{(1,c_g-i)}(e)=\Theta\left(\frac{1}{p_\mathrm{gr}^3k_l\mathrm{log}(n)}\right)\) _for every edge of type_ \((\alpha,\beta,0)_l\) _with_ \(\alpha\neq 0\) _and l\>c<sub>g</sub>-i,_

