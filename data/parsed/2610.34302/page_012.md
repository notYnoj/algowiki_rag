Thus each greedy step assigns total weight 1 to the points newly covered at that step. For each \(j\in J_{i,s}\), the total weight of the points in _C<sub>j</sub>_ is<tbc>

\(\sum_{v\in C_j}y_v=1.\)

<tbc>Therefore

\(\sum_{v\in\mathcal{U}_{i,s}}y_v=\sum_{j\in J_{i,s}}\sum_{v\in C_j}y_v=|J_{i,s}|=|E_s^i|.\) (2.2)

For this fixed level _i_, the weights _y<sub>v</sub>_ are determined by the greedy Set Cover execution on all of _P_ and do not depend on the source _s_. We use these same weights to bound \(|E_s^i|\) for every local instance (U_<sub>i,s</sub>,_F_<sub>i,s</sub>_).

We next bound the total weight in any radius-\(\rho_i\) ball: for every \(c\in P\),

\(\sum_{v\in B(c,\rho_i)}y_v\le H_n\le lnn+1,\) (2.3)

where \(H_n=1+1/2+\cdots+1/n\). Fix such a ball \(Q=B(c,\rho_i)\). Consider only the greedy steps that cover at least one point of _Q_. Immediately before such a step _j_, let<tbc>

\(k_j=|Q\cap U^{(j)}|\)

<tbc>be the number of still-uncovered points of _Q_, and let<tbc>

\(q_j=|Q\cap C_j|\)

<tbc>be the number of points of _Q_ covered at this step. Since _Q_ itself is one of the available radius-\(\rho_i\) balls, the candidate center _c_ would cover all _k<sub>j</sub>_ currently uncovered points of _Q_. Hence, by (2.1),<tbc>

\(|C_j|\ge k_j.\)

<tbc>The total weight of the _q<sub>j</sub>_ points of _Q_ covered at step _j_ is<tbc>

\(\frac{q_j}{|C_j|}\le\frac{q_j}{k_j}.\)

<tbc>If the nonzero values of _k<sub>j</sub>_ along these steps are denoted by<tbc>

\(k^{(1)}>k^{(2)}>\cdots>k^{(a)}>0,\)

<tbc>and _q_<sup>(_h_)</sup>=_k_<sup>(_h_)</sup>-_k_<sup>(_h_+1)</sup> with _k_<sup>(_a_+1)</sup>=0, then

\(\sum_{v\in B(c,\rho_i)}y_v\le\sum_{h=1}^a\frac{q^{(h)}}{k^{(h)}}\le\sum_{h=1}^a\sum_{\ell=k^{(h+1)}+1}^{k^{(h)}}\frac{1}{\ell}=H_{k^{(1)}}\le H_n.\)

This proves (2.3).

Now let B<sup>opt</sup> be an optimal cover of U_<sub>i,s</sub>_ by sets from F_<sub>i,s</sub>_, so |B<sup>opt</sup>|=OPT_<sub>i,s</sub>_. Each set in B<sup>opt</sup> has the form \(B(c,\rho_i)\cap\mathcal{U}_{i,s}\) for some \(c\in P\). Since \(y_v\ge 0\) for every \(v\in P\) and B<sup>opt</sup> covers U_<sub>i,s</sub>_,

\(|E_s^i|=\sum_{v\in\mathcal{U}_{i,s}}y_v\text{by (2.2)}\)<br>
\(\le\sum_{B(c,\rho_i)\cap\mathcal{U}_{i,s}\in\mathcal{B}^\mathrm{opt}}\sum_{v\in B(c,\rho_i)\cap\mathcal{U}_{i,s}}y_v\)<br>
\(\le\sum_{B(c,\rho_i)\cap\mathcal{U}_{i,s}\in\mathcal{B}^\mathrm{opt}}\sum_{v\in B(c,\rho_i)}y_v\)<br>
\(\le H_n\cdot|\mathcal{B}^\mathrm{opt}|\le(lnn+1)\mathrm{OPT}_{i,s},\)

where the penultimate inequality uses (2.3). This proves the claim.

