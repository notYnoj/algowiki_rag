_where_ \(c=\mathrm{cos}\beta\) _and_ \(s=\mathrm{sin}\beta\)_. In particular, if_ \(\mathrm{tan}\beta=1/2\)_, then_ \(a_{D_\star}(\beta)\neq 0\)_, and so_

\(D_\star=\mathrm{max}\{k\in\mathbb{Z}:a_k(\beta)\neq 0\}.\)

_Hence, for this mixer angle_ |#MC(_G_)| _is recovered by division by a known nonzero algebraic factor._

_Proof._ Only the paths in Eq. (16) satisfying the equality conditions in Eq. (24) can contribute to _z_<sup>_D<sub>⋆</sub>_</sup>. The exponent in (16) attains _D<sub>⋆</sub>_=MC(_G_)+2_N_-4 if and only if _c<sub>G</sub>(x_)=MC(_G_), _c<sub>G</sub>(t_)=0, and _c<sub>G</sub>(y_)-_c<sub>G</sub>(T<sub>e<sub>⋆</sub></sub>y_)=2_N_-4 simultaneously. Fix such a path \((x,q_\sigma,\tau\mathbf{1})\) with \(x\in\#\text{MC}(G)\) and \(\sigma,\tau\in\{\pm 1\}\). First observe the endpoint factor is \(y_ry_s=(q_\sigma)_r(q_\sigma)_s=\sigma^2=1\) for both \(\sigma\). Next, by (25) the Hamming distance \(h=d_\mathrm{Hamm}(x,q_\sigma)=N/2\) is the same integer for every \(x\in\#\text{MC}(G)\) and both \(\sigma\), so by (15) we have

\(\prod_{w\in V(G)}K_\beta^+\left(x_w,(q_\sigma)_w\right)=c^{N-h}(\mathrm{i}s)^h=c^{N/2}(\mathrm{i}s)^{N/2},\) (28)

independently of _x_ and \(\sigma\). Finally, by (24) we have \(t_w=\tau\) for all _w_, and since \(T_{e_\star} q_\sigma=-\sigma\mathbf{1}\),

\(\prod_{w\in V(G)}K_\beta^-\left((T_{e_\star} q_\sigma)_w,t_w\right)=K_\beta^-\left(-\sigma,\tau\right)^N=\left\{\begin{array}{ c c }
c^N & \tau=-\sigma \\
(-\mathrm{i}s)^N & \tau=\sigma.
\end{array}\right.\) (29)

Summing (29) over \(\tau\in\{\pm 1\}\) gives _c<sup>N</sup>_+(-i_s)<sup>N</sup>_, independently of \(\sigma\). Since the endpoint factor, the product (28), and the \(\tau\)-sum are all independent of _x_ and \(\sigma\), the triple sum over the surviving paths factorizes as

\(a_{D_\star}(\beta)=-2^{-N}\sum_{x\in\#\text{MC}(G)}\sum_{\sigma\in\{\pm 1\}}\sum_{\tau\in\{\pm 1\}}y_ry_s\prod_wK_\beta^+\left(x_w,(q_\sigma)_w\right)K_\beta^-\left((T_{e_\star} q_\sigma)_w,t_w\right)\)<br>
\(=-2^{-N}\cdot\underbrace{|\#\text{MC}(G)|}_{x\text{-sum}}\cdot\underbrace{2}_{\sigma\text{-sum}}\cdot\underbrace{1}_{y_ry_s}\cdot\underbrace{c^{N/2}(\mathrm{i}s)^{N/2}}_{(28)}\cdot\underbrace{[c^N+(-\mathrm{i}s)^N]}_{\tau\text{-sum}},\)

which rearranges to give Eq. (27). For \(\mathrm{tan}\beta=1/2\), the two terms in the bracket always have unequal magnitudes and cannot cancel, which implies \(a_{D_\star}(\beta)\neq 0\).

For the global expectation,

\(\mathcal{F}_2(G;z,\beta):=F_2(G;\phi,\phi,\beta,\pi/4)=\frac{|E(G)|}{2}-\frac{1}{2}\sum_{e\in E(G)}H_e(z;\beta).\) (30)

Since _e<sub>⋆</sub>_ uniquely maximizes _R<sub>e</sub>_, the coefficient of _z_<sup>_D<sub>⋆</sub>_</sup> in (30) is exactly -_a_<sub>_D<sub>⋆</sub>_</sup>/2. Thus either the single correlator or the global objective contains the same count information.

## 2.2 Coefficient recovery and proof of the main theorem

Let _m_=|_E(G_)|. Every Laurent exponent in (16) lies in \[-2_m,_2_m_\]. Set

\(Q=4m+1,\omega=e^{2\pi\mathrm{i}/Q},\phi_j=\frac{2\pi j}{Q}.\) (31)

For either \(P(z)=H_{e_\star}(z;\beta)\) or \(P(z)=\mathcal{F}_2(G;z,\beta)\), query the oracle with \(\gamma_1=\gamma_2=\phi_j\) for _j_=0,1_,...,Q_-1, so \(z=e^{\mathrm{i}\phi_j}=\omega^j\). The exact values \(P(\omega^j)\) recover every coefficient by the inverse discrete Fourier transform

\(a_k(\beta)=[z^k]P(z)=\frac{1}{Q}\sum_{j=0}^{Q-1}P(\omega^j)\omega^{-jk}.\) (32)

