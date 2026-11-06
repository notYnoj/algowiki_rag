**Lemma 30** (Phased counting bound)**.** _On_ E<sub>ph</sub>, RESTARTPHASEDCLIP-1BITBAI _uses at most_<tbc>

\(O\left(\sum_{k=1}^K\Lambda(\overline{\Delta_k})\frac{\sigma^2}{\overline{\Delta_k^2}}\Gamma(\overline{\Delta_k};K,J,\delta)\right)\)

<tbc>_1-bit queries, where_<tbc>

\(\Lambda(u)=1+log\frac{\sigma}{u}\)

<tbc>_and_<tbc>

\(\Gamma(u;K,J,\delta)=log\frac{K(J+1)}{\delta}+loglog\left(e^e\frac{\sigma}{u}\right)+loglog\left(e^e\frac{K(J+1)}{\delta}\right).\)

<tbc>_Proof._ By Lemma 27, in phase _j_ each active arm receives at most<tbc>

\(n_j^\circ=O\left(\frac{\alpha_j\sigma^2}{\rho_j^2}\Gamma_j\right)\)

<tbc>queries. By Lemma 29, arm _k_ is sampled only in phases whose resolution is at least a universal constant multiple of \(\overline{\Delta_k}\). Thus the total number of samples of arm _k_ is bounded by<tbc>

\(\sum_{j:\rho_j\unknown\overline{\Delta_k}}O\left(\frac{\alpha_j\sigma^2}{\rho_j^2}\Gamma_j\right).\)

<tbc>Let _j<sub>k</sub>_ be the last phase in this sum. Since \(\rho_j\) decreases geometrically,<tbc>

\(\sum_{j=0}^{j_k}\frac{1}{\rho_j^2}=\frac{1}{\sigma^2}\sum_{j=0}^{j_k}4^j\le\frac{4}{3}\frac{1}{\rho_{j_k}^2}.\)

<tbc>Moreover, both \(\alpha_j\) and \(\Gamma_j\) are nondecreasing as \(\rho_j\) decreases, so for \(j\le j_k\),<tbc>

\(\alpha_j\le\alpha_{j_k},\Gamma_j\le\Gamma_{j_k}.\)

<tbc>Therefore the contribution of arm _k_ is at most a constant times<tbc>

\(\alpha_{j_k}\frac{\sigma^2}{\rho_{j_k}^2}\Gamma_{j_k}.\)

<tbc>The largest scheduled index _j<sub>k</sub>_ satisfying \(\rho_{j_k}\unknown\overline{\Delta_k}\) has \(\rho_{j_k}=\Theta(\overline{\Delta_k})\) by dyadicity and the final-scale cap. This index bounds the cost even if the actual last sampled phase is earlier. Hence

\(\alpha_{j_k}=1+log\frac{32\sigma}{\rho_{j_k}}=O\big(1+log\frac{\sigma}{\overline{\Delta_k}}\big)=O(\Lambda(\overline{\Delta_k})),\)<br>
\(\frac{\sigma^2}{\rho_{j_k}^2}=O\left(\frac{\sigma^2}{\overline{\Delta_k^2}}\right),\)

and<tbc>

\(\Gamma_{j_k}=O\big(\Gamma(\overline{\Delta_k};K,J,\delta)\big).\)

<tbc>Thus arm _k_ contributes at most

\(O\left(\Lambda(\overline{\Delta_k})\frac{\sigma^2}{\overline{\Delta_k^2}}\Gamma(\overline{\Delta_k};K,J,\delta)\right).\)

Summing this bound over _k_=1_,...,K_ proves the lemma.

_Proof of Theorem 10._ By Lemma 24, E<sub>ph</sub> holds with probability at least \(1-\delta\). On this event, Lemma 26 proves that every possible return is \(\varepsilon\)-optimal. Lemma 30 gives the stated high- probability query bound. Proposition 33 establishes termination on every realization. Hence RESTARTPHASEDCLIP-1BITBAI is \((\varepsilon,\delta)\)-PAC and satisfies the claimed sample complexity. The displayed main-text bound follows because \(\overline{\Delta_k}\ge\varepsilon\), \(J+1=O(1+log(\sigma/\varepsilon))\), and the remaining iterated logarithms in \(\Gamma\) are absorbed into \(log(K/\delta)+loglog(e^e\sigma/\varepsilon)\).

