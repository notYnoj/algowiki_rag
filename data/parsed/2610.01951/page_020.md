For the upper bound, note that 0_\<w<sub>j</sub>\<_1, hence \(\mathrm{log}w_j\le 0\). Therefore<tbc>

\(\mathrm{min}_{j\neq i^\star}\Phi_j(n,m_j)\le\mathrm{log}t+t\mathrm{min}_{j\neq i^\star} I_j^\alpha(w_j)\le\mathrm{log}t+\frac{t}{T_\alpha^\star(\mu)}.\)

<tbc>Maximizing over feasible _m_ yields<tbc>

\(\Gamma_{n,s}^\mathrm{disc}(\mu)\le\frac{t}{T_\alpha^\star(\mu)}+\mathrm{log}t.\)

<tbc>For the lower bound, let \(w^\alpha(\mu)\) be the optimizer from Proposition C.3. Since \(\alpha\mapsto w^\alpha(\mu)\) is continuous on _U_ and all coordinates are positive,<tbc>

\(c_U:=\mathrm{inf}_{\alpha\in U}\mathrm{min}_{j\neq i^\star} w_j^\alpha(\mu)>0.\)

<tbc>Similarly,<tbc>

\(L_U:=\mathrm{sup}_{\alpha\in U}\mathrm{sup}_{j\neq i^\star}\mathrm{sup}_{u\in[c_U/2,1]}\left|\frac{d}{du}I_j^\alpha(u)\right|<\infty.\)

<tbc>Assume first that \(t\ge 2/c_U\). Then \(a_j:=tw_j^\alpha(\mu)\ge 2\), so Lemma C.5 gives integers \(m_j\ge 1\) such that<tbc>

\(\sum_{j\neq i^\star} m_j=s,|m_j-tw_j^\alpha(\mu)|\le 1.\)

<tbc>Hence<tbc>

\(\left|\frac{m_j}{t}-w_j^\alpha(\mu)\right|\le\frac{1}{t},\frac{m_j}{t}\ge\frac{c_U}{2}.\)

<tbc>By the mean value theorem,<tbc>

\(\left|I_j^\alpha\left(\frac{m_j}{t}\right)-I_j^\alpha(w_j^\alpha(\mu))\right|\le\frac{L_U}{t}.\)

<tbc>Since \(I_j^\alpha(w_j^\alpha(\mu))=T_\alpha^\star(\mu)^{-1}\),<tbc>

\(tI_j^\alpha\left(\frac{m_j}{t}\right)\ge\frac{t}{T_\alpha^\star(\mu)}-L_U.\)

<tbc>Moreover, \(\mathrm{log}(m_j/t)\ge\mathrm{log}(c_U/2)\). Therefore<tbc>

\(\Phi_j(n,m_j)\ge\frac{t}{T_\alpha^\star(\mu)}+\mathrm{log}t-L_U+\mathrm{log}(c_U/2)\forall j\neq i^\star.\)

<tbc>Taking the minimum over _j_ gives

\(\Gamma_{n,s}^\mathrm{disc}(\mu)\ge\frac{t}{T_\alpha^\star(\mu)}+\mathrm{log}t-C_{1,\mu}(U),\)

where \(C_{1,\mu}(U):=L_U-\mathrm{log}(c_U/2)\).

If _t\<_2_/c<sub>U</sub>_, only finitely many admissible triples (_n,s,t_) satisfy _n+s=t_ and \(n/(n+s)\in U\), so their contribution can be absorbed into a finite constant \(C_{0,\mu}(U)\). Taking \(C_\mu(U):=\mathrm{max}\{C_{0,\mu}(U),C_{1,\mu}(U)\}\) completes the proof.

## D Time-Uniform Pairwise GLR Control

### D.1 Armwise KL confidence sequences

**Lemma D.1** (Armwise KL confidence sequences)**.** _There exists a universal constant c_<sub>0</sub>_\>_0 _such that for every_ \(\eta\in(0,1)\) _there is an event_ \(\mathcal{K}_\eta\) _with_ \(\mathbb{P}_\mu(\mathcal{K}_\eta)\ge 1-\eta\) _and, on_ \(\mathcal{K}_\eta\)_, simultaneously for all_ \(t\ge K\) _and all arms_ \(i\in[K]\),<tbc>

\(N_{t,i}d(\widehat{\mu}_{t,i},\mu_i)\le c_0\left(\mathrm{log}\frac{K}{\eta}+\mathrm{loglog}(et)\right).\)

<tbc>_Consequently,_<tbc>

\(|\widehat{\mu}_{t,i}-\mu_i|\le\sqrt{\frac{c_0H_t(\eta)}{2N_{t,i}}}.\)

