We first record the pathwise drift implication on the good event. Fix \(s<T_\eta\wedge\tau_M\wedge t_\mathrm{sep}(\overline{\eta})\) and suppose that \(\mathcal{E}_\overline{\eta}\) holds. Since \(s<t_\mathrm{sep}(\overline{\eta})\), at least one arm is separation-deficient. If some separation- deficient arm is not the current leader _B_<sub>_s_+1</sub>, then Lemma G.1 implies that the greedy challenger selected by the unguarded rule has count \(N_{s,C_{s+1}}<M_\eta\). Thus _X_<sub>_s_+1</sub>=1 whenever the challenger is pulled. If no separation-deficient nonleader exists, then every separation-deficient arm must be the current leader. In that case \(N_{s,B_{s+1}}<n_\star(\overline{\eta})\le M_\eta\), so _X_<sub>_s_+1</sub>=1 whenever the leader is pulled. In both cases,

\(\mathbb{E}[X_{s+1}|\mathcal{F}_s]\ge p\text{on}\mathcal{E}_\overline{\eta}\cap\{s<T_\eta\wedge\tau_M\wedge t_\mathrm{sep}(\overline{\eta})\}.\) (G.1)

On \(\mathcal{E}_\overline{\eta}\cap\{t_\mathrm{sep}(\overline{\eta})>T_\eta\}\), one also has \(\tau_M>T_\eta\), because \(\tau_M\le T_\eta\) would imply \(t_\mathrm{sep}(\overline{\eta})\le\tau_M\le T_\eta\). Therefore (G.1) applies for every \(s=K,\dots,T_\eta-1\). Moreover, \(D_{T_\eta}>0\), so<tbc>

\(\sum_{s=K}^{T_\eta-1}X_{s+1}=D_K-D_{T_\eta}<D_K=K(M_\eta-1).\)

<tbc>Consequently,

\(\mathcal{E}_\overline{\eta}\cap\{t_\mathrm{sep}(\overline{\eta})>T_\eta\}\subseteq\left\{\sum_{s=K}^{T_\eta-1}Y_{s+1}\le-a_\eta\right\},a_\eta:=p(T_\eta-K)-K(M_\eta-1).\) (G.2)

By the definition of \(T_\eta\),<tbc>

\(T_\eta-K\ge\frac{2K}{p}(M_\eta-1)+\frac{16}{p^2}\mathrm{log}\frac{6}{\eta},\)

<tbc>so \(a_\eta\ge p(T_\eta-K)/2\). Azuma-Hoeffding gives<tbc>

\(\mathbb{P}_\mu\left(\sum_{s=K}^{T_\eta-1}Y_{s+1}\le-a_\eta\right)\le\mathrm{exp}\left(-\frac{a_\eta^2}{2(T_\eta-K)}\right)\le\mathrm{exp}\left(-\frac{p^2(T_\eta-K)}{8}\right)\le\eta/6.\)

<tbc>Since \(\mathbb{P}_\mu(\mathcal{E}_\overline{\eta}^c)\le 2\overline{\eta}=\eta/3\), (G.2) yields

\(\mathbb{P}_\mu\left(t_\mathrm{sep}(\eta/6)>T_\eta\right)\le\eta/2.\)

Because \(T_\eta\) has the polynomial form stated in Lemma G.1, the first claim follows.

For the consequent statement, set \(\overline{\eta}:=\eta/12\) in the preceding high-probability entry argument. Then<tbc>

\(\mathbb{P}_\mu\left(t_\mathrm{sep}(\overline{\eta})\le T_\overline{\eta}\right)\ge 1-\eta/4\)

<tbc>after changing the instance-dependent constants. Intersect this event with the armwise confidence event \(\mathcal{K}_\overline{\eta}\), which has probability at least \(1-\eta/12\), and with the leader-fraction event \(\mathcal{A}_{\eta/4}\) of Proposition F.1, which has probability at least \(1-\eta/4\). On the intersection, Proposition 6.1 implies<tbc>

\(B_{t+1}=i^\star\forall t\ge T_\overline{\eta}.\)

<tbc>Lemma F.2 then gives a _U_-stabilization time satisfying<tbc>

\(t_U\le C_{\beta,U}\left(T_\overline{\eta}+K+\mathrm{log}\frac{e(T_\overline{\eta}+1)^2}{\eta}\right).\)

<tbc>The failure probability of the intersection is at most

\(\eta/4+\eta/12+\eta/4<\eta.\)

Since \(T_\overline{\eta}\) has the same polynomial form in \(1/\eta\) after changing constants, the claimed upper-quantile bound follows.

_Proof of Corollary 6.3._ Combine Proposition 6.2 with Theorem 5.2. The upper-quantile bound for _t<sub>U</sub>_ is polynomial in \(1/\eta\), so the resulting theorem is unconditional in high probability but not necessarily integrable.

