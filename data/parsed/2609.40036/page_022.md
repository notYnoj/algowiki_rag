The observed useful decoding range extends well beyond the lower bound presented in Corollary 2. For example, at _D_=7_,q_=5 the certified rate is approximately \(1.30\times 10^{-4}\), whereas all 56 errors tested at _p_=0.00686 across _n_=4096,16384,65536 were recovered. The eight largest-size samples contained between 1512 and 1620 erroneous symbols. The cycle value provides a second reference for the numerical curves, although the explicit small-alphabet lower bracket does not apply at these modest degrees. Finite-size transition points above the cycle value are consistent with an asymptotic strong converse.

## 4 DQI performance and classical comparison

In this concluding section, we combine the analysis of §2 with the decoding results of §3 to study DQI performance on problems dual, in the Regev sense, to decoding homological cycle codes. In particular, we focus on the Linial-Simkin ensemble and DQI instantiated by LP decoding in superposition. The following corollary provides the direct connection needed to make our performance claims below.

**Corollary 3** (DQI from cycle-code reliability)**.** _Fix_ \(D\ge 3\)_, a finite field_ F_<sub>q</sub>, and_ \(c\in(0,1)\)_. Consider Max-2-LINSAT instances on the LS ensemble G_∼L_<sub>n,D,c</sub> (Definition 4) with target sets of common size r such that the corresponding noise channels all have a shared error distribution_ \(\theta\)_. Let_ \(\rho=r/q\)_. Call a cutoff rate_ \(p\in[0,1/2]\) _reliable if there are syndrome decoders returning zero on the zero syndrome for which the failure probability in Theorem 1, with_ \(\ell=\lfloor pm\rfloor\)_, tends to zero in ensemble mean. Let_ \(F_{D,\theta,r}^\text{DQI}\) _be the supremum of the limiting expected satisfaction fractions obtained by optimizing the weights_ **w** _at reliable cutoff rates. Then_

\(F_{D,\theta,r}^\text{DQI}\le F_\rho(min\{\delta_\text{cyc}(D,\theta),1-\rho\}).\) (88)

_If_ \(\gamma=q/D^{2/3}\le 1/32\)_, then also_

\(F_{D,\theta,r}^\text{DQI}\ge F_\rho(min\{(1-16\gamma)\delta_\text{cyc}(D,\theta),1-\rho\}).\) (89)

_For q_=2_, the upper bound is attained for every_ \(D\ge 3\).

The bounds concern cutoffs for which decoding is asymptotically reliable. If \(\delta_\text{cyc}(D,\theta)<1/2\), the upper bound also excludes reliable cutoff rates above 1/2. This includes uniform replacement at every _D,q_.

_Proof._ At a reliable rate _p_, the optimized fraction converges in probability to \(F_\rho(min\{p,1-\rho\})\) by Theorem 1. It also converges in mean, because satisfaction fractions lie in \[0,1\]. If \(p>\delta_\text{cyc}(D,\theta)\), choose \(\delta_\text{cyc}(D,\theta)<p'<min\{p,1/2\}\). A binomial error count at rate \(p'\) is at most \(\lfloor pm\rfloor\) with probability tending to one. The assumed uniform shell recovery would therefore imply reliable channel decoding at \(p'\), contradicting Theorem 4. This proves (88).

Conversely, Theorem 5 and Lemma 6 give one-coordinate recovery for the lexicographically first minimum-weight decoder at every \(p'\le(1-16\gamma)\delta_\text{cyc}(D,\theta)\). For any smaller _p_, Lemma 7 transfers this guarantee to all shells through \(\lfloor pm\rfloor\). Apply Theorem 1 and let _p_ increase to the certified endpoint to obtain (89). For _q_=2, the binary recovery proof establishes the same property at every \(p'<\delta_\text{cyc}(D,2)\). Substitute (79) into \(F_{1/2}(p)=1/2+\sqrt{p(1-p)}\).

