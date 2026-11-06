where _N_(G<sub>1</sub>) is the number of distances between points of _A<sub>tf</sub>_ and points of _B<sub>t</sub>_ that are in \(I''\) for all graphs \(G_{tf}\in\mathcal{G}_1\).

Since<tbc>

\(\sum_{G_{tf}\in\mathcal{G}_1}|A_{tf}||B_t|\le\sum_t|A_t||B_t|=m_{j-1},\)

<tbc>we conclude that \(N(\mathcal{G}_1)\le 0.01\cdot m_{j-1}\).

### The set G<sub>2</sub>.

For each \(G_{tf}\in\mathcal{G}_2\), at least 3(|_A<sub>tf</sub>_|+|_B<sub>t</sub>_|) distances in \(E\cap I''\) are contributed, and therefore _G<sub>tf</sub>_ contributes at least 3|_A<sub>tf</sub>_||_B<sub>t</sub>_| to the total weight of distances in \(E\cap I''\). Recall that the total weight of distances in \(E\cap I''\) is at most _m_<sub>_j_-1</sub>/2 by our algorithm. Hence,<tbc>

\(\sum_{G_{tf}\in\mathcal{G}_2}|A_{tf}||B_t|\le\frac{m_{j-1}}{6}.\)

<tbc>Let _N_(G<sub>2</sub>) denote the number of distances between points of _A<sub>tf</sub>_ and points of _B<sub>t</sub>_ that lie in \(I''\) for all graphs \(G_{tf}\in\mathcal{G}_2\). Then<tbc>

\(N(\mathcal{G}_2)\le\sum_{G_{tf}\in\mathcal{G}_2}|A_{tf}||B_t|\le\frac{m_{j-1}}{6}.\)

### Summary.

<tbc>By definition, \(|S(\Gamma)\cap I''|=N(\mathcal{G}_1)+N(\mathcal{G}_2)\). Since \(N(\mathcal{G}_1)\le 0.01m_{j-1}\) and \(N(\mathcal{G}_2)\le m_{j-1}/6\), we obtain

\(|S(\Gamma)\cap I''|\le\left(0.01+\frac{1}{6}\right)m_{j-1}.\)

Setting \(\rho''=0.01+1/6\), we have \(\rho''\in(0,0.18)\), and the lemma follows.

By Lemma 10, and since _I_<sup>∗</sup> consists of two basic intervals, we have

\(|S(\Gamma)\cap I'|\le 2\rho''m_{j-1}<0.36m_{j-1},\)

where \(\rho''\in(0,0.18)\).

Combining this bound with (8) and (9), we obtain

\(q_j\le\frac{2c_0}{c_1}m_{j-1}+0.36m_{j-1}.\)

Choosing _c_<sub>1</sub> sufficiently large so that \(2c_0/c_1\le 0.01\) yields \(q_j\le 0.37m_{j-1}\), which proves Lemma 8.

## 5.3 The distance-reporting step

As discussed above, after _O_(log<sup>∗</sup>_n_) phases, we are left with an interval \(I=(\alpha,\beta]\) such that \(|S\cap I|=O(n^{4/3})\) and \(\delta^*\in I\). In this distance-reporting step, we compute \(\delta^*\) in an additional _O(n_<sup>4/3</sup>) time.

We first compute the number of distances in _S_ that are at most \(\alpha\), which can be done in _O(n_<sup>4/3</sup>) time \[24\]. Let \(K_\alpha\) denote this number. Our goal is then to find the \(K'\)-th smallest distance in \(S\cap I\), where \(K'=K-K_\alpha\). To this end, we first explicitly enumerate all distances in \(S\cap I\), and then apply the linear-time selection algorithm to compute \(\delta^*\). Since \(|S\cap I|=O(n^{4/3})\), the selection step takes _O(n_<sup>4/3</sup>) time. Therefore, the remaining task is to enumerate \(S\cap I\) within the same time bound.

A natural approach is to apply Lemma 1 to compute \(\Gamma\) and \(\Pi\) with \(\Pi=\emptyset\). We refer to this as a _full biclique partition_ (called _full batched range searching_ in \[28\]). Since \(\Pi=\emptyset\), the bicliques in \(\Gamma\) record all distances in \(S\cap I\), and thus all such distances can be enumerated from \(\Gamma\) in additional \(O(|S\cap I|)\) time. To compute a full biclique partition, the algorithm of \[28\] recursively applies Lemma 1. However, the resulting running time is \(n^{4/3}\cdot 2^{O(\mathrm{log}^*n)}\) because of the constant-factor blowup in the recurrence \[28\]. Moreover, the bound obtained in \[28\] for \(\sum_{A_t\times B_t\in\Gamma}(|A_t|+|B_t|)\) is also \(n^{4/3}\cdot 2^{O(\mathrm{log}^*n)}\), again due to the constant-factor blowup.

