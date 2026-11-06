Since _a_ minimizes _P<sub>u</sub>_ and \(|P_u(j)-Q_u(j)|\le\varepsilon_u\) on \(\mathcal{G}_\eta\),<tbc>

\(Q_u(a)\le Q_u(j^+)+2\varepsilon_u.\)

<tbc>Thus \(\gamma_{n_u,S_u}-Q_u(a)\) is bounded below by \(c_\mu(U)M_u-C_\mu(U)(\varepsilon_u+u|\alpha_u-\beta|+1)\). In the present case this lower bound is positive, so _e<sub>u,a</sub>\>_0, and the slope upper bound yields

\(e_{u,a}\ge c'_\mu(U)M_u-C'_\mu(U)(\varepsilon_u+u|\alpha_u-\beta|+1).\)

Combining this with (E.2) proves (E.3).

Define \(P_u^+:=\sum_{j\in\mathcal{J}}(D_{u,j})_+\). Since the deficits sum to zero, \(M_u\le P_u^+\). Fix the final time _s_ and set<tbc>

\(\Xi_s:=\varepsilon_s+sup_{t_U\le v\le s}v|\alpha_v-\beta|+1,\Lambda_s:=\frac{A_\mu(U)\Xi_s+1}{\kappa_\mu(U)}.\)

<tbc>The sequence \(\varepsilon_u\) is nondecreasing, so (E.3) implies that every regular challenger pull \(u+1\le s\) with \(u\ge s_\bullet\) satisfies<tbc>

\(D_{u,C_{u+1}}\ge\kappa_\mu(U)M_u-A_\mu(U)\Xi_s.\)

<tbc>If _u_+1 is a leader pull, then _D_<sub>_u_+1</sub>=_D<sub>u</sub>_. If it is a challenger pull of arm _a_, then<tbc>

\(D_{u+1,j}=D_{u,j}+p_j^\beta-\mathbf{1}\{j=a\}.\)

<tbc>Consider a regular challenger pull. If \(M_u>\Lambda_s\), then _D<sub>u,a</sub>\>_1. Adding \(p^\beta\) can increase _P_<sup>+</sup> by at most \(\sum_jp_j^\beta=1\), while subtracting one from coordinate _a_ decreases the positive mass by exactly one. Hence \(P_{u+1}^+\le P_u^+\). If \(M_u\le\Lambda_s\), then \(P_u^+\le d_K\Lambda_s\), and a single challenger update can increase _P_<sup>+</sup> by at most one. Therefore every regular challenger pull satisfies

\(P_{u+1}^+\le max\{P_u^+,d_K\Lambda_s+1\}.\)

A guard pull is adversarial: if it pulls _i<sup>⋆</sup>_, _D_ is unchanged, and if it pulls a challenger, the same update holds for an arbitrary arm, increasing _P_<sup>+</sup> by at most one.

Induction from \(s_\bullet\) to _s_ gives<tbc>

\(P_s^+\le max\{P_{s_\bullet}^+,d_K\Lambda_s+1\}+G_s^\mathrm{tot}.\)

<tbc>Moreover,<tbc>

\(P_{s_\bullet}^+\le\sum_{j\in\mathcal{J}}p_j^\beta S_{s_\bullet}=S_{s_\bullet}\le s_\bullet\le t_U+s_\mathrm{eq},\)

<tbc>and _s_<sub>eq</sub> is absorbed into the constant. Hence<tbc>

\(P_s^+\le C_\mu(U)\left(t_U+G_s^\mathrm{tot}+\varepsilon_s+sup_{t_U\le u\le s}u|\alpha_u-\beta|+1\right).\)

<tbc>By (E.2), this implies<tbc>

\(max_{j\in\mathcal{J}}(r_{j,n_s,S_s}-N_{s,j})_+\le C_\mu(U)\left(t_U+G_s^\mathrm{tot}+\varepsilon_s+sup_{t_U\le u\le s}u|\alpha_u-\beta|+1\right).\)

<tbc>Let the right-hand side be _E<sub>s</sub>_. Then \(N_{s,j}\ge r_{j,n_s,S_s}-E_s\) for all _j_. If \(N_{s,j}\ge r_{j,n_s,S_s}\), monotonicity gives \(Q_s(j)\ge\gamma_{n_s,S_s}\). Otherwise Lemma E.1 gives \(Q_s(j)\ge\gamma_{n_s,S_s}-C_\mu(U)E_s\). Thus

\(min_{j\in\mathcal{J}}Q_s(j)\ge\gamma_{n_s,S_s}-C_\mu(U)E_s.\)

Using \(\gamma_{n_s,S_s}\ge\Gamma_{n_s,S_s}^\mathrm{disc}(\mu)-C_\mu(U)\) from Lemma E.2 proves the lemma.

## E.4 Proof of Proposition 5.1

_Proof of Proposition 5.1._ Write<tbc>

\(\widetilde{H}_s(\eta):=\mathrm{log}\frac{K}{\eta}+\mathrm{log}(es).\)

