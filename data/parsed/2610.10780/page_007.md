Applying (2) to each subproblem of (1) with the same parameter _r_ yields

\(T(m,n)=O(mrlogr+nr)+O(r^4)\cdot T\big(\frac{m}{r^3},\frac{n}{r^3}\big).\) (3)

The balanced recurrence implies that, in _O(mr_log_r+nr_) time, one can compute a collection of _O(r_<sup>4</sup>) edge-disjoint bicliques \(A_t\times B_t\) such that every pair \((a,b)\in A_t\times B_t\) satisfies \(\|ab\|\in I\). Furthermore, \(\sum_t(|A_t|+|B_t|)=O(mrlogr+nr)\). We return this collection as \(\Gamma\).

In addition, we obtain _O(r_<sup>4</sup>) bicliques \(A'_s\times B'_s\) corresponding to the subproblems _T(m/r_<sup>3</sup>_,n/r_<sup>3</sup>). For these bicliques, we do not know whether \(\|ab\|\in I\) for pairs \((a,b)\in A'_s\times B'_s\). We return the collection of all such bicliques as \(\Pi\). Consequently, \(|A'_s|\le m/r^3\) and \(|B'_s|\le n/r^3\) for every \(A'_s\times B'_s\in\Pi\), and the total number of uncertain pairs recorded in \(\Pi\) is _O(mn/r_<sup>2</sup>). This proves Lemma 1.

We remark that Recurrence (3) is the key algorithmic consequence of the partial biclique partition framework. It will serve as the starting point for both the approximate counting algorithm in Section 3 and the distance representation algorithm in Section 4.

## 3 Approximate counting and quasi-decision

In this section and the next two sections, we assume that |_A_|=|_B_|=_n_.

This section develops an approximate counting algorithm for interval distances. The quasi-decision theorem then follows immediately by comparing the approximate count with a given threshold.

For an interval _I_, let \(\kappa(I)=|S\cap I|\) denote the number of distances of _S_ whose values lie in _I_.

Our main goal in this section is to prove the following approximate counting theorem.

**Theorem 1** (Approximate Counting)**.** _Let I be any interval. For every integer i with_ \(1\le i\le O(log^*n)\)_, one can compute an integer_ \(\hat{\kappa}(I)\) _such that_

\(|\kappa(I)-\hat{\kappa}(I)|\le c_0\cdot n^{4/3}(log^{(i)}n)^4\)

_for some constant c_<sub>0</sub>_\>_0.

_The runtime is O(n_<sup>4/3</sup>/log<sup>(_i_)</sup>_n_) _for i_=1,2_, and O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) _for_ \(i\ge 3\).

### Remark.

Ideally, we would like to compute \(\kappa(I)\) exactly. However, exact computation requires _O(n_<sup>4/3</sup>) time \[10,24\], which is optimal in a restricted computational model. The purpose of Theorem 1 is to obtain a faster algorithm by computing only an approximation of \(\kappa(I)\) while controlling the approximation error. Furthermore, the theorem provides a trade-off between running time and error: allowing a larger error leads to a faster algorithm.

Theorem 1 immediately yields the following quasi-decision theorem, which will be used later in the distance selection algorithm of Section 5.

**Theorem 2** (Quasi-Decision)**.** _Given an interval I and an integer K with_ \(1\le K\le n^2\)_, for every i with_ \(1\le i\le O(log^*n)\)_, there exists an algorithm whose output has one of the following three outcomes:_

1. _the algorithm reports_ \(\kappa(I)<K\);<tbc>

2. _the algorithm reports_ \(\kappa(I)>K\);<tbc>

_3._ _the algorithm reports "unsure", in which case_<tbc>

<tbc>\(|\kappa(I)-K|\le c_0\cdot n^{4/3}(log^{(i)}n)^4\)<tbc>

<tbc>_for some constant c_<sub>0</sub>_\>_0.<tbc>

