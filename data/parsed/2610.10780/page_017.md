For every edge (_a,b_) of _G<sub>t</sub>_, where \(a\in A_t\) and \(b\in B_t\), we associate the distance \(\|ab\|\). The resulting collection of distances is denoted by _E_. The size of _E_ is therefore _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>). Moreover, every distance of _E_ lies in the interval _I_<sub>_j_-1</sub>.

We next assign a weight to every value of _E_. The weight assignment is chosen so that the total weight of all distances of _E_ is proportional to \(N(\Gamma)\). Since every graph _G<sub>tf</sub>_ is _d_-regular, it has at most (|_A<sub>tf</sub>_|+|_B<sub>t</sub>_|)_d/_2 edges. We assign each distance contributed by _G<sub>tf</sub>_ the weight<tbc>

\(\frac{|A_{tf}||B_t|}{|A_{tf}|+|B_t|}.\)

<tbc>The total weight of all values in _E_ is therefore at most

\(\sum_{t,f}(|A_{tf}|+|B_t|)\cdot\frac{d}{2}\cdot\frac{|A_{tf}||B_t|}{|A_{tf}|+|B_t|}=\frac{d}{2}\cdot\sum_{t,f}|A_{tf}||B_t|=\frac{d}{2}\cdot N(\Gamma).\)

Recall that \(N(\Gamma)>c_1n^{4/3}(log^{(i)}n)^4\). We may assume \(N(\Gamma)\ge 16\). Furthermore, every value of _E_ has weight at most \(|A_{tf}||B_t|/(|A_{tf}|+|B_t|)\le\frac{1}{2}\sqrt{|A_{tf}||B_t|}\le\frac{1}{2}\sqrt{N(\Gamma)}\le N(\Gamma)/8\).

Using these weights, we choose values \(\delta_1<\delta_2<\cdots<\delta_h\) from _E_, where \(1\le h\le 2d\), so that they partition _I_<sub>_j_-1</sub> into _h_+1 intervals and the total weight of the values of _E_ in each interval lies between \(N(\Gamma)/4\) and \(N(\Gamma)/2\). The partition can be computed in _O_(|_E_|) time using the linear-time selection algorithm \[7\], and therefore requires _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) time.

## Computing _I<sub>j</sub>_ by testing the values of _E_.

We now use the values of _E_ to compute the next interval _I<sub>j</sub>_.

Assume that \(I_{j-1}=(\alpha,\beta]\). Let \(\delta_0=\alpha\) and \(\delta_{h+1}=\beta\). For \(1\le u\le h+1\), define \(I'_u=(\delta_{u-1},\delta_u]\). Let \(\mathcal{I}=\{I'_u|1\le u\le h+1\}\). Clearly, the intervals of I form a partition of _I_<sub>_j_-1</sub>.

Ideally, we would like to identify the interval of I containing \(\delta^*\) and return it as _I<sub>j</sub>_. Previous deterministic algorithms accomplish this by repeatedly invoking an exact decision procedure, which computes, for a given value \(\delta\), the number \(K_\delta\) of distances in _S_ that are at most \(\delta\). Since \(\delta<\delta^*\) if and only if \(K_\delta<K\), such a procedure can be used to locate the interval containing \(\delta^*\).

The exact decision algorithm requires _O(n_<sup>4/3</sup>) time \[10, 24\]. Consequently, using it in every iteration leads to the _O(n_<sup>4/3</sup>log_n_)-time algorithm of Wang and Zhao \[28\]. To achieve an _O(n_<sup>4/3</sup>)-time algorithm, we instead use the quasi-decision algorithm of Theorem 2.

For every _u_, \(1\le u\le h\), we apply Theorem 2 to the interval \(I''_u=[0,\delta_u]\). Note that \(\kappa(I''_u)=K_{\delta_u}\).

Let _u_<sub>1</sub> be the largest index such that the algorithm of Theorem 2 reports \(\kappa(I''_{u_1})<K\) (implying that \(\delta_{u_1}<\delta^*\)). If no such index exists, we set _u_<sub>1</sub>=0. Since \(\delta_0=\alpha\) and \(\delta^*\in I_{j-1}=(\alpha,\beta]\), we always have \(\delta_{u_1}<\delta^*\).

Similarly, let _u_<sub>2</sub> be the smallest index such that the algorithm reports \(\kappa(I''_{u_2})>K\) (implying that \(\delta^*\le\delta_{u_2}\)). If no such index exists, we set _u_<sub>2</sub>=_h_+1. In either case, \(\delta^*\le\delta_{u_2}\).

Therefore, \(\delta^*\in(\delta_{u_1},\delta_{u_2}]\).

We terminate the current iteration and return \(I_j=(\delta_{u_1},\delta_{u_2}]\).

Since \(h\le 2d\) and _d=O_(1), only _O_(1) calls to Theorem 2 are required. Each call takes _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) time. Therefore, the total running time of the iteration remains _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>).

The correctness of the algorithm is established by the following lemma, whose proof is given in the next subsection.

**Lemma 7.** _There exists a constant_ \(\rho\in(0,1)\) _such that_ \(|S\cap I_j|\le\rho|S\cap I_{j-1}|\).

