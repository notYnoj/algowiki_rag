We begin by invoking the standard subroutine. The running time is _O(n_log_m_). Recall that \(N(\Gamma)\) denote the number of pairs recorded by the bicliques of \(\Gamma\). Let _M_ denote the total number of uncertain pairs contained in the recursive subproblems _T(q,q_). As shown in the proof of Lemma 12, _M=O(m_<sup>2</sup>). Thus we may assume that \(M\le c_1m^2\) for some constant _c_<sub>1</sub>_\>_0.

If \(N(\Gamma)\le c_2m^2\) for a sufficiently large constant _c_<sub>2</sub>, then \(|S\cap I_{j-1}|=N(\Gamma)+M=O(m^2)\). Hence, in this case, the first main procedure terminates and returns _I_<sub>_j_-1</sub>. Assume therefore that \(N(\Gamma)>c_2m^2\).

We next construct the expander graphs for the bicliques of \(\Gamma\) and form a weighted distance set _E_ exactly as in Section 5.1. Since the total size of the bicliques in \(\Gamma\) is _O(n_log_m_), this step takes _O(n_log_m_) time. We then partition _E_ into _O_(1) basic intervals and use Lemma 13 in place of the quasi-decision algorithm from Section 5.1. This yields an interval _I<sub>j</sub>_.

Using analysis similar to Section 5.2, we can prove \(|S\cap I_j|\le\rho\cdot|S\cap I_{j-1}|\) for some constant \(\rho<1\). Intuitively, we can make _c_<sub>2</sub> large enough so that _M_ and the term _c_<sub>0</sub>_m_<sup>2</sup> in Lemma 13 can be neglected compared to _c_<sub>2</sub>_m_<sup>2</sup>. For example, if we follow the same notation as in Section 5.2, then we have _m_<sub>_j_-1</sub>=_N(T_) and \(m'_{j-1}\le M\). Since \(M\le c_1m^2\) and \(N(\Gamma)>c_2m^2\), we have \(m'_{j-1}\le\frac{c_1}{c_2}\cdot m_{j-1}\). Since \(n_{j-1}=m_{j-1}+m'_{j-1}\), it follows that \(m'_{j-1}\le\frac{c_1}{c_1+c_2}\cdot n_{j-1}\). This inequality can be used to replace \(m'_{j-1}\le 0.6n_{j-1}\) that was obtained by Theorem 3 (note that here \(\Gamma\) plays the role of Theorem 3 and that is why we do not have an explicit distance representation theorem here). Similarly, we can prove \(|S\cap\hat{I}|\le 2c_0m^2\) as a counterpart to Lemma 9.

Therefore, each iteration runs in _O(n_log_m_) time and reduces the number of candidate distances by a constant factor. After _O_(log(_n/m_)) iterations, we obtain an interval _I_ containing \(\delta^*\) such that \(|S\cap I|=O(m^2)\). The total running time of the first main procedure is _O(n_log<sup>2</sup>_m_).

## 6.2.2 The second main procedure

We now describe the second main procedure, which is the most challenging part of the asymmetric distance selection algorithm.

Given an interval _I_ containing \(\delta^*\) with \(|S\cap I|=O(m^2)\), the goal is to shrink _I_ so that \(|S\cap I|=O(m^{2/3}n^{2/3})\) while maintaining \(\delta^*\in I\).

We begin with the following approximate counting lemma.

**Lemma 14** (Approximate Counting)**.** _Let I be an interval. For every integer i with_ \(1\le i\le O(\mathrm{log}^*q)\)_, one can compute an integer_ \(\hat{\kappa}(I)\) _such that_

\(|\kappa(I)-\hat{\kappa}(I)|\le c_0^*m^{2/3}n^{2/3}(\mathrm{log}^{(i)}q)^4\)

_for some constant_ \(c_0^*>0\)_. The running time is O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>/log<sup>(_i_)</sup>_q_) _for i_=1,2_, and O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>/(log<sup>(_i_)</sup>_q_)<sup>2</sup>) _for_ \(i\ge 3\).

_Proof._ We only discuss the case \(i\ge 3\); the cases _i_=1,2 are analogous.

We first invoke the standard subroutine in _O(n_log_m_) time and add the number of pairs recorded by the resulting bicliques \(\Gamma\) to \(\hat{\kappa}(I)\).

For each recursive subproblem _T(q,q_) in Recurrence (11), it is for a subset \(A'\subseteq A\) and \(B'\subseteq B\) with \(|A'|\le q\) and \(|B'|\le q\). Let \(\kappa'(I)\) denote the number of distances between \(A'\) and \(B'\) lying in _I_. Apply Theorem 1 to \((A',B')\) with _i_ and _I_ yields a number \(\hat{\kappa}'(I)\) that approximates \(\kappa'(I)\) with error bounded by _c_<sub>0</sub>_q_<sup>4/3</sup>(log<sup>(_i_)</sup>_q_)<sup>4</sup>. The runtime is _O(q_<sup>4/3</sup>/(log<sup>(_i_)</sup>_q_)<sup>2</sup>). We add \(\hat{\kappa}'(I)\) to \(\hat{\kappa}(I)\).

Since there are _O(r_<sup>2</sup>) subproblems, the total error is bounded by

\(O(r^2)\cdot c_0q^{4/3}(\mathrm{log}^{(i)}q)^4=O(m^{2/3}n^{2/3}(\mathrm{log}^{(i)}q)^4),\)

where we use the identity _r_<sup>2</sup>_q_<sup>4/3</sup>=_m_<sup>2/3</sup>_n_<sup>2/3</sup>.

Similarly, the total time spent on all subproblems is

