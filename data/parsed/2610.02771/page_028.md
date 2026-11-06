Summing over arms gives<tbc>

\(T=\sum_{k=1}^KN_k<c_0H_\text{fix}(\varepsilon)x_T.\)

<tbc>Therefore any _T_ satisfying \(T\ge c_0H_\text{fix}(\varepsilon)x_T\) forces the algorithm to have stopped by time _T_.

Now choose<tbc>

\(T=\left[CH_\text{fix}(\varepsilon)\left[log\frac{K}{\delta}+loglogH_\text{fix}(\varepsilon)\right]\right]\)

<tbc>for a sufficiently large universal constant _C_. For this choice,

\(x_T=O\big(log\frac{K}{\delta}+loglogH_\text{fix}(\varepsilon)\big),\)

because _x<sub>T</sub>_ contains only \(log(K/\delta)\) and the stitched term \(2log(1+\lfloor log_2T\rfloor)=O(loglogT)\), while _T_ is proportional to \(H_\text{fix}(\varepsilon)\) times logarithmic factors. Taking _C_ large enough gives \(T\ge c_0H_\text{fix}(\varepsilon)x_T\), proving the desired bound.

_Proof of Theorem 8._ By Lemma 19, Efix holds with probability at least \(1-\delta\). On this event, Lemma 20 proves that any returned arm is \(\varepsilon\)-optimal, and Lemma 23 proves that the stopping time is bounded by the displayed sample complexity. Proposition 32 additionally establishes termination on every realization. Hence FIXEDCLIP-1BITBAI is \((\varepsilon,\delta)\)-PAC and satisfies the claimed high-probability query bound.

## C.2 Phased adaptive clipping: proof of Theorem 10

We now analyze the restart phased algorithm. We first construct a high-probability event on which all arm-phase confidence intervals are valid simultaneously (Lemma 24). On this event, the elimination and stopping rules never discard the best arm and can only return an \(\varepsilon\)-optimal arm (Lemma 26). The sample complexity analysis then proceeds phase by phase. Lemma 27 gives the number of samples needed to certify a phase-_j_ interval at radius _r<sub>j</sub>_. Lemmas 28 and 29 show that each arm is sampled only down to a resolution comparable to its capped effective gap \(\overline{\Delta_k}\). Summing the resulting dyadic costs over phases and arms gives the claimed bound (Lemma 30).

For each phase \(j=0,1,\dots,J=\lceil log_2(\sigma/\varepsilon)\rceil\), recall<tbc>

\(\rho_j=2^{-j}\sigma,L_j=\frac{32\sigma^2}{\rho_j},r_j=\frac{\rho_j}{16},\alpha_j=1+log\frac{L_j}{\sigma}=1+log\frac{32\sigma}{\rho_j}.\)

<tbc>With \(\gamma=\delta/[K(J+1)]\), the phase-_j_ confidence radius is

\(\beta_j(n)=\frac{\rho_j}{64}+2\sqrt{\frac{3\alpha_j\sigma^2x_n(\gamma)}{n}}+\frac{32\alpha_j\sigma^2x_n(\gamma)}{\rho_jn}.\)

The restart version uses independent fresh estimators in each arm-phase pair (_k,j_).

**Lemma 24** (Phased good event)**.** _With probability at least_ \(1-\delta\)_, the event_

\(\mathcal{E}_\text{ph}:=\cap_{k=1}^K\cap_{j=0}^J\cap_{n\ge 1}\{|\widehat{\mu}_{k,j}(n)-\mu_k|\le\beta_j(n)\}\)

_holds throughout_ RESTARTPHASEDCLIP-1BITBAI.

_Proof._ Fix an arm-phase pair (_k,j_). During phase _j_, the algorithm uses clipping level _L<sub>j</sub>_ for arm _k_. Since<tbc>

\(\frac{\sigma^2}{2L_j}=\frac{\sigma^2}{2\cdot 32\sigma^2/\rho_j}=\frac{\rho_j}{64},\)

<tbc>Theorem 5 with failure probability \(\gamma\) gives<tbc>

\(Pr\left(\forall n\ge 1,|\widehat{\mu}_{k,j}(n)-\mu_k|\le\beta_j(n)\right)\ge 1-\gamma.\)

<tbc>There are _K(J_+1) arm-phase pairs, so the union bound gives

\(Pr(\mathcal{E}_\text{ph})\ge 1-K(J+1)\gamma=1-\delta.\)

Again, the confidence sequence is uniform in the local sample count _n_, so adaptive sampling inside the phase is allowed.

