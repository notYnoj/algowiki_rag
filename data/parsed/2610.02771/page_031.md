By Lemma 25, \(k^\star\in A\). Hence, on E<sub>ph</sub>,<tbc>

\(m\ge\mathrm{LCB}_{k^\star,j}\ge\mu^\star-2r_j.\)

<tbc>For the suboptimal arm _k_,<tbc>

\(\mathrm{UCB}_{k,j}\le\mu_k+2r_j=\mu^\star-\Delta_k+2r_j.\)

<tbc>If \(\Delta_k>\varepsilon+4r_j\), then<tbc>

\(\mu^\star-\Delta_k+2r_j<\mu^\star-\varepsilon-2r_j.\)

<tbc>Since \(4r_j=\rho_j/4\), the condition \(\Delta_k>\varepsilon+\rho_j/4\) is exactly \(\Delta_k>\varepsilon+4r_j\). Combining the preceding displays,

\(\mathrm{UCB}_{k,j}<\mu^\star-\varepsilon-2r_j\le m-\varepsilon.\)

Thus _k_ satisfies the elimination rule \(\mathrm{UCB}_{k,j}<m-\varepsilon\) and is eliminated.

**Lemma 29** (Last relevant phase)**.** _Assume_ E<sub>ph</sub> _holds. For every arm k, the resolution of the last phase in which k is sampled is bounded below by a universal constant multiple of_<tbc>

\(\overline{\Delta_k}:=\mathrm{min}\{\mathrm{max}\{\Delta_k,\varepsilon\},\sigma\}.\)

<tbc>_More precisely, there exists a universal constant c\>_0 _such that if_ \(\rho\) _is the resolution of the last phase in which k is sampled, then_

\(\rho\ge c\overline{\Delta_k}.\)

_Proof._ We first consider a suboptimal arm \(k\neq k^\star\).

_Case 1:_ \(\Delta_k\ge 2\varepsilon\) _and_ \(\Delta_k\le\sigma\). Then \(\overline{\Delta_k}=\Delta_k\). Let _j<sub>k</sub>_ be the first phase index such that \(\rho_{j_k}\le\Delta_k\). By dyadicity,<tbc>

\(\frac{\Delta_k}{2}<\rho_{j_k}\le\Delta_k.\)

<tbc>Since \(\Delta_k\ge 2\varepsilon\), we have \(\varepsilon\le\Delta_k/2\). Therefore

\(\varepsilon+\frac{\rho_{j_k}}{4}\le\frac{\Delta_k}{2}+\frac{\Delta_k}{4}=\frac{3\Delta_k}{4}<\Delta_k.\)

Lemma 28 implies that arm _k_ is eliminated by the end of phase _j<sub>k</sub>_, unless the algorithm has already stopped. Thus _k_ is not sampled beyond phase _j<sub>k</sub>_, so its last sampled resolution is at least \(\rho_{j_k}>\overline{\Delta_k}/2\).

_Case 2:_ \(\Delta_k\ge 2\varepsilon\) _and_ \(\Delta_k>\sigma\). Then \(\overline{\Delta_k}=\sigma\). At phase 0, \(\rho_0=\sigma\). Since \(\varepsilon\le\Delta_k/2\) and \(\rho_0/4=\sigma/4<\Delta_k/4\),

\(\varepsilon+\frac{\rho_0}{4}<\frac{\Delta_k}{2}+\frac{\Delta_k}{4}=\frac{3\Delta_k}{4}<\Delta_k.\)

Thus Lemma 28 eliminates arm _k_ by the end of phase 0, unless the algorithm stops. If _k_ is sampled, its last sampled resolution is therefore \(\sigma=\overline{\Delta_k}\).

_Case 3:_ \(\Delta_k<2\varepsilon\). Then \(\overline{\Delta_k}\le 2\varepsilon\). Also \(J=\lceil\mathrm{log}_2(\sigma/\varepsilon)\rceil\), so

\(\rho_J\le\varepsilon<2\rho_J.\)

No arm is sampled after phase _J_. Hence the last sampled resolution satisfies \(\rho\ge\rho_J>\varepsilon/2\ge\overline{\Delta_k}/4\).

Now consider the optimal arm _k<sup>⋆</sup>_, with \(\Delta_{k^\star}=\mathrm{min}_{j\neq k^\star}\Delta_j\). If \(\Delta_{k^\star}\ge 2\varepsilon\) and \(\Delta_{k^\star}\le\sigma\), let _j<sub>⋆</sub>_ be the first phase with \(\rho_{j_\star}\le\Delta_{k^\star}\). The same calculation as in Case 1 shows that every suboptimal arm _a_ satisfies

\(\Delta_a\ge\Delta_{k^\star}>\varepsilon+\frac{\rho_{j_\star}}{4},\)

so all suboptimal arms are eliminated by the end of phase _j<sub>⋆</sub>_, unless the algorithm has already stopped. The active set then becomes singleton and the algorithm returns, so _k<sup>⋆</sup>_ is not sampled beyond this phase and its last sampled resolution exceeds \(\overline{\Delta_{k^\star}}/2\). If \(\Delta_{k^\star}\ge 2\varepsilon\) and \(\Delta_{k^\star}>\sigma\), the same argument applies at phase 0, giving last sampled resolution \(\sigma=\overline{\Delta_{k^\star}}\). If \(\Delta_{k^\star}<2\varepsilon\), the final-phase argument in Case 3 gives last sampled resolution greater than \(\overline{\Delta_{k^\star}}/4\). This proves the claim with _c_=1/4. Early stopping can only increase the last sampled resolution, so no upper bound on it is needed or asserted.

