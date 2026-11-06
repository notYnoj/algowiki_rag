\(O(r^2)\cdot O\left(\frac{q^{4/3}}{(log^{(i)}q)^2}\right)=O\left(\frac{m^{2/3}n^{2/3}}{(log^{(i)}q)^2}\right).\)

Adding the _O(n_log_m_) time of the standard subroutine completes the proof.

Lemma 14 immediately yields the following quasi-decision lemma, whose proof is similar to that of Theorem 2.

**Lemma 15** (Quasi-Decision)**.** _Given an interval I and an integer K with_ \(1\le K\le mn\)_, for every i with_ \(1\le i\le O(log^*q)\)_, there exists an algorithm whose output has one of the following three outcomes: (1) the algorithm reports_ \(\kappa(I)<K\)_; (2) the algorithm reports_ \(\kappa(I)>K\)_; (3) the algorithm reports "unsure", in which case_ \(|\kappa(I)-K|\le c_0^*m^{2/3}n^{2/3}(log^{(i)}q)^4\) _for some constant_ \(c_0^*>0\)_. The running time is O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>/log<sup>(_i_)</sup>_q_) _for i_=1,2_, and O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>/log<sup>(_i_)</sup>_q_)<sup>2</sup>) _for_ \(i\ge 3\).

We now describe the second main procedure. The framework is identical to that of Section 5.

Recall that \(|S\cap I|=O(m^2)\) and \(\delta^*\in I\). The algorithm proceeds in phases. For _i_=1,2_,...,O_(log<sup>∗</sup>_q_), the goal of the _i_-th phase is to transform an interval _I_ satisfying<tbc>

\(|S\cap I|=O(m^{2/3}n^{2/3}(log^{(i-1)}q)^4)\)

<tbc>(and _O(m_<sup>2</sup>) when _i_=1) into a smaller interval \(I'\subseteq I\) satisfying

\(|S\cap I'|=O(m^{2/3}n^{2/3}(log^{(i)}q)^4)\)

while maintaining \(\delta^*\in I'\).

Initially, \(|S\cap I|=O(m^2)\). After _O_(log<sup>∗</sup>_q_) phases, we obtain an interval _I_ satisfying \(|S\cap I|=O(m^{2/3}n^{2/3})\), which is precisely the goal of the second main procedure. Each phase consists of _O_(log<sup>(_i_)</sup>_q_) iterations. Each iteration runs in _O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>/log<sup>(_i_)</sup>_q_) time for _i_=1,2, and in _O(n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>/(log<sup>(_i_)</sup>_q_)<sup>2</sup>) time for \(i\ge 3\). Consequently, the total running time over all phases is<tbc>

\(O(nlogm)\cdot\sum_{i=1}^{O(log^*q)}log^{(i)}q+O(m^{2/3}n^{2/3})\cdot\left(1+\sum_{i=3}^{O(log^*q)}\frac{1}{log^{(i)}q}\right),\)

<tbc>which is

\(O(nlogmlogq)+O(m^{2/3}n^{2/3})=O(nlog^2m+m^{2/3}n^{2/3}),\)

since \(q=m^2/n\le m\).

## Algorithm description.

We describe a general _i_-th phase. Before the phase begins, we are given an interval _I_ satisfying \(|S\cap I|=O(m^{2/3}n^{2/3}(log^{(i-1)}q)^4)\) and containing \(\delta^*\). The goal is to compute a subinterval \(I'\subseteq I\) such that \(|S\cap I'|=O(m^{2/3}n^{2/3}(log^{(i)}q)^4)\) and \(\delta^*\in I'\).

As in Section 5, the phase proceeds in iterations. At the beginning of the _j_-th iteration, we are given an interval _I_<sub>_j_-1</sub> containing \(\delta^*\), with _I_<sub>0</sub>=_I_. Each iteration either

1. produces a smaller interval \(I_j\subseteq I_{j-1}\) such that \(\delta^*\in I_j\) and \(|S\cap I_j|\le\rho|S\cap I_{j-1}|\) for some constant \(\rho<1\); or<tbc>

2. produces a smaller interval \(I_j\subseteq I_{j-1}\) such that \(\delta^*\in I_j\) and \(|S\cap I_j|\le c^*m^{2/3}n^{2/3}(log^{(i)}q)^4\) for a sufficiently large constant _c_<sup>∗</sup>.<tbc>

