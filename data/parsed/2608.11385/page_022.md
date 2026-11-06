<tbc>_correlator_ \(\langle Z_rZ_s\rangle\) _and for connected, unweighted, simple graphs of diameter two. At depth two the hard instances may be restricted to_

\(\beta_1=\beta_2=\frac{\pi}{4},\gamma_1=\gamma_2=\phi,e^{\mathrm{i}\phi}=\zeta_q,\) (38)

_where_ \(\zeta_q\) _has polynomial order. For p\>_2_, all later angles may be set to zero._

_Proof._ We use the explicit one-query hardness reduction for counting maximum cuts in simple graphs given by Dell et al. \[64, full version, Lemmas C.2-C.3\]. Given a source graph _H_ with _n_ vertices, set<tbc>

\(\widehat{H}=\left\{\begin{array}{ c c }
H, & n\mathrm{odd}, \\
H\sqcup K_1, & n\mathrm{even},
\end{array}\right.\rho=|V(\widehat{H})|-n\in\{0,1\}.\) (39)

<tbc>Then \(\widehat{n}=|V(\widehat{H})|\) is odd, \(\mathrm{MC}(\widehat{H})=\mathrm{MC}(H)\), and \(|\#\mathrm{MC}(\widehat{H})|=2^\rho|\#\mathrm{MC}(H)|\). Apply the construction of Section 2 to \(\widehat{H}\). Because both \(\widehat{n}\) and _L_ are odd, the resulting graph \(G=\mathcal{G}(\widehat{H})\) satisfies

\(N=2\widehat{n}L+2\equiv 0(\mathrm{mod}4),|\#\mathrm{MC}(G)|=2^{\rho+1}|\#\mathrm{MC}(H)|.\) (40)

It retains all graph restrictions in the theorem.

Set \(\beta_1=\beta_2=\pi/4\) and write the anchor correlator as \(H_{e_\star}(z)=\sum_{k=-2m}^{2m}a_kz^k\), where _m_=|_E(G_)|. Theorem 2.4 and \(N\equiv 0(\mathrm{mod}4)\) give

\(a_{D_\star}=-|\#\mathrm{MC}(G)|2^{2-2N}\mathrm{i}^{N/2}\neq 0.\) (41)

For the global expectation, Eq. (30) gives the corresponding coefficient -_a_<sub>_D<sub>⋆</sub>_</sub>/2. Thus either coefficient determines |#MC(_G_)|.

All Laurent coefficients lie in \(K_0=\mathbb{Q}(\zeta_8)\). Bertrand’s postulate gives an odd prime 4_m_+1_\<q\<_2(4_m_+1), so _q=O(m_). Such a prime can be found in polynomial time by testing integers in this interval. For the query field, take \(K=\mathbb{Q}(\theta)\) with \(\theta=\zeta_{8q}\) and cyclotomic defining polynomial \(\Phi_{8q}\). This polynomial has degree 4(_q_-1) and coefficients in \(\{0,\pm 1\}\), and isolating data for the chosen root can be computed with polynomial bit complexity. Encode the phases and mixers using \(z=\theta^8\), \(\mathrm{i}=\theta^{2q}\), and \(c_j=s_j=(\theta^q+\theta^{7q})/2\) for _j_=1,2, reducing powers modulo \(\Phi_{8q}\). These input lists have polynomial total bit length. Query once at \(z=\zeta_q\). Since gcd(8_,q_)=1,<tbc>

\([K:K_0]=q-1>4m.\) (42)

<tbc>Consequently \(1,\zeta_q,\dots,\zeta_q^{4m}\) are linearly independent over _K_<sub>0</sub>, and

\(\zeta_q^{2m}P(\zeta_q)=\sum_{j=0}^{4m}[z^{j-2m}]P(z)\zeta_q^j\) (43)

for either _P=H<sub>e<sub>⋆</sub></sub>_ or the global expectation. Multiply the returned value by \(\zeta_q^{2m}\) and convert its rational coordinates to the basis \(\{\zeta_8^r\zeta_q^j:0\le r<4,0\le j<q-1\}\) of _K_. Grouping the four coordinates at each _j_ gives the _K_<sub>0</sub>-coefficient \[_z_<sup>_j_-2_m_</sup>\]_P(z_) for \(0\le j\le 4m\). All remaining groups are zero. This recovers every Laurent coefficient from the single answer. The basis conversion uses polynomial-time exact linear algebra in degree 4(_q_-1)=_O(m_).

For the bit-length bound, each path in Eq. (16) at these mixer angles contributes 2<sup>-2_N_</sup> times one of \(\{\pm 1,\pm\mathrm{i}\}\) to a Laurent coefficient. There are at most 2<sup>3_N_</sup> summands, so each Laurent coefficient of the correlator has _O(N_)-bit rational coordinates in Q(i). Summing over edges gives _O(N_+log_m_)-bit coordinates for the global expectation. Substitution of \(\zeta_q\) and reduction in the<tbc>

