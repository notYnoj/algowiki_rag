### Algorithm Correctness.

Using an argument analogous to the proof of Lemma 7, one can show that

\(|S_{02}\cap I_j|\le\rho'|S_{02}\cap I_{j-1}|\) (13)

for some constant \(\rho'<1\). The only additional ingredient is that, for every unbounded subproblem \(p\in P_2\), by definition, \(N(\Gamma_p)>c_1q^{4/3}(\mathrm{log}^{(i)}q)^4\). Since \(|S_p\cap I_{j-1}|\ge N(\Gamma_p)\), we have \(|S_p\cap I_{j-1}|>c_1q^{4/3}(\mathrm{log}^{(i)}q)^4\). Consequently, \(N(\Gamma_p)\ge 0.4|S_p\cap I_{j-1}|\) by Theorem 3.

We now prove that

\(|S\cap I_j|\le\rho|S\cap I_{j-1}|\)

for some constant \(\rho<1\).

Since _S_<sub>02</sub> and _S_<sub>1</sub> form a partition of _S_,<tbc>

\(|S\cap I_j|=|S_1\cap I_j|+|S_{02}\cap I_j|.\)

<tbc>Because \(I_j\subseteq I_{j-1}\), we have \(S_1\cap I_j\subseteq S_1\cap I_{j-1}\). Therefore,<tbc>

\(|S\cap I_j|\le|S_1\cap I_{j-1}|+|S_{02}\cap I_j|.\)

<tbc>Combining (12) and (13) yields

\(|S\cap I_j|\le\frac{c'}{c^*}|S\cap I_{j-1}|+\rho'|S_{02}\cap I_{j-1}|\le\left(\frac{c'}{c^*}+\rho'\right)|S\cap I_{j-1}|.\)

Since \(\rho'<1\), choosing _c_<sup>∗</sup> sufficiently large and defining \(\rho=\frac{c'}{c^*}+\rho'\) gives \(\rho<1\). This proves the first outcome of the iteration.

The above analysis assumes that \(|S\cap I_{j-1}|\ge c^*m^{2/3}n^{2/3}(\mathrm{log}^{(i)}q)^4\). Otherwise, we simply run the same algorithm, which obtains an interval \(I_j\subseteq I_{j-1}\) containing \(\delta^*\). Since \(|S\cap I_j|\le|S\cap I_{j-1}|\le c^*m^{2/3}n^{2/3}(\mathrm{log}^{(i)}q)^4\), the second outcome holds automatically.

Therefore, in each iteration, we simply run the same algorithm as above. Every iteration either reduces the number of candidate distances by a constant factor or reaches the target bound _O(m_<sup>2/3</sup>_n_<sup>2/3</sup>(log<sup>(_i_)</sup>_q_)<sup>4</sup>).

### Summary.

We conclude that, within _O(n_log<sup>2</sup>_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>) time, we can compute an interval _I_ containing \(\delta^*\) such that \(|S\cap I|=O(m^{2/3}n^{2/3})\).

## 6.2.3 The distance-reporting procedure

We are given an interval _I_ containing \(\delta^*\) such that \(|S\cap I|=O(m^{2/3}n^{2/3})\). The goal of this procedure is to compute \(\delta^*\).

Assume that \(I=(\alpha,\beta]\). We first compute \(K_\alpha\), the number of distances in _S_ that are at most \(\alpha\). This can be done in _O(m_log_n+n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>) time \[24\]. Consequently, \(\delta^*\) is the \((K-K_\alpha)\)-th smallest distance in \(S\cap I\). Thus it suffices to enumerate all distances in \(S\cap I\) and then apply the linear-time selection algorithm. The latter step takes _O(m_<sup>2/3</sup>_n_<sup>2/3</sup>) time since \(|S\cap I|=O(m^{2/3}n^{2/3})\).

The remaining task is therefore to enumerate all distances in \(S\cap I\). For this, we have the following more general result.

**Lemma 16.** _Given any interval I, all distances in_ \(S\cap I\) _can be enumerated in_ \(O(n\mathrm{log}m+m^{2/3}n^{2/3}+|S\cap I|)\) _time._

