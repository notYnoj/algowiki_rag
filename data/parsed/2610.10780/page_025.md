### A standard subroutine.

A recurring step in our algorithm is to apply Recurrence (1) with _r=n/m_. We refer to this as the _standard subroutine_. Substituting _r=n/m_ into Recurrence (1) yields

\(T(m,n)=O(nlogr)+O(r^2)\cdot T(q,q),q=\frac{m^2}{n}.\) (11)

The standard subroutine runs in _O(n_log_r_) time and produces a collection \(\Gamma=\{A_t\times B_t\}\) of bicliques whose total size is _O(n_log_r_). Throughout the remainder of the section, we always use _r=n/m_, _q=m_<sup>2</sup>_/n_, and let \(N(\Gamma)\) denote the number of distances recorded by \(\Gamma\).

Since \(m\le n<m^2\), we have \(r\le m\) and therefore log_r=O_(log_m_). Consequently, the running time of the standard subroutine is _O(n_log_m_), which is the bound we will use in the following discussions.

The significance of Recurrence (11) is that every recursive subproblem has the form _T(q,q_). In other words, after one application of the recurrence, the problem becomes symmetric. Therefore, the tools developed in the previous sections (e.g., Theorems 1 and 3) can be applied directly to _T(q,q_).

It is also useful to observe that _r_<sup>2</sup>_q_<sup>4/3</sup>=_m_<sup>2/3</sup>_n_<sup>2/3</sup>, which is precisely the complexity term appearing in Theorem 6.

## 6.2.1 The first main procedure

We begin with the following approximate counting lemma.

**Lemma 12** (Approximate Counting)**.** _For any interval I, one can compute in O(n_log_m_) _time an integer_ \(\hat{\kappa}(I)\) _satisfying_ \(|\kappa(I)-\hat{\kappa}(I)|\le c_0m^2\) _for some constant c_<sub>0</sub>_\>_0.

_Proof._ We invoke the standard subroutine and return \(\hat{\kappa}(I)=\sum_{A_t\times B_t\in\Gamma}|A_t||B_t|\). The running time is _O(n_log_m_).

Clearly, \(|\kappa(I)-\hat{\kappa}(I)|\) is bounded by the number of uncertain pairs recorded in the recursive subproblems of _T(q,q_). There are _O(r_<sup>2</sup>) such subproblems, each contributing at most _O(q_<sup>2</sup>) pairs. Hence \(|\kappa(I)-\hat{\kappa}(I)|=O(r^2q^2)=O(m^2)\), since _r=n/m_ and _q=m_<sup>2</sup>_/n_. \(\square\)

Lemma 12 immediately yields the following quasi-decision lemma, whose proof is similar to that of Theorem 2.

**Lemma 13** (Quasi-Decision)**.** _Given an interval I and an integer K with_ \(1\le K\le mn\)_, there exists an O(n_log_m)-time algorithm whose output has one of the following three outcomes: (1) the algorithm reports_ \(\kappa(I)<K\)_; (2) the algorithm reports_ \(\kappa(I)>K\)_; (3) the algorithm reports "unsure", in which case_ \(|\kappa(I)-K|\le c_0m^2\) _for some constant c_<sub>0</sub>_\>_0.

We now describe the first main procedure. Its goal is to reduce the number of candidate distances from _O(mn_) to _O(m_<sup>2</sup>) while maintaining an interval _I_ containing \(\delta^*\).

Initially, \(I=(0,+\infty)\), and therefore \(|S\cap I|=O(mn)\). The algorithm proceeds in iterations. In each iteration, which runs in _O(n_log_m_) time, the number of candidate distances is reduced by a constant factor. After _O_(log(_n/m_)) iterations, we obtain an interval _I_ containing \(\delta^*\) such that \(|S\cap I|=O(m^2)\).

Since each iteration takes _O(n_log_m_) time, the total running time of the procedure is bounded by _O(n_log_m_log(_n/m_)), which is _O(n_log<sup>2</sup>_m_) since _n\<m_<sup>2</sup>.

### A general _j_-th iteration.

Suppose we are given an interval _I_<sub>_j_-1</sub>. The goal is to compute an interval _I<sub>j</sub>_ such that either

1. \(|S\cap I_j|=O(m^2)\), in which case the first main procedure terminates; or<tbc>

2. \(|S\cap I_j|\le\rho|S\cap I_{j-1}|\) for some constant \(\rho<1\).<tbc>

