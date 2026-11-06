\(\bullet\) Let _M_=(_r_<sub>1</sub>_,c_<sub>1</sub>),(_r_<sub>2</sub>_,c_<sub>2</sub>)_,...,(r<sub>k</sub>,c<sub>k</sub>_) be an arbitrary matching of _L<sub>R</sub>_ and _L<sub>C</sub>_.<tbc>

\(\bullet\) Set _R_(0):=_Q(T_).<tbc>

\(\bullet\) For _i_=1,2_,...,k_:<tbc>

- If \(\mathcal{B}_i:=\mathcal{B}_{R(i-1)}(r_i,c_i)=\emptyset\) abort.<tbc>

**-** Otherwise, choose some \((x_i,y_i)\in\mathcal{B}_i\) and set \(R(i):=(Q(i-1)\backslash\{(x_i,y_i)\})\cup\{(x_i,c_i),(r_i,y_i)\}\).

Clearly, if Algorithm 2.2 does not abort then _R(k_) is an _n_-queens configuration. In Section 4 we show that w.h.p. _Q(T_) satisfies a combinatorial condition that guarantees the success of Algorithm 2.2.

## 3. Random queens on a torus

In this section we analyze Algorithm 2.1.<br>
For \(0\le t\le T\) define the functions

\(p(t)=1-\frac{t}{n},\varepsilon(t)=\frac{n^{0.51}}{p(t)^{50}}.\)

We refer to rows, columns, and toroidal diagonals collectively as **lines**. Let L be the set of lines. We note that |L|=4_n_ and that each line has length _n_. For each \(\ell\in\mathcal{L}\) and \(0\le t\le T\), let \(S_\ell(t)\) denote the number of available elements in line \(\ell\) at time _t_. We say that a line is **occupied at time** _t_ if _Q(t_) contains a position in the line.

**Proposition 3.1.** _The following holds with probability_ \(1-exp\left(-\Omega\left(n^{0.01}\right)\right)\)_. For every_ \(\ell\in\mathcal{L}\) _and_ \(0\le t\le T\)_, if line_ \(\ell\) _is unoccupied at time t then_

\(S_\ell(t)=np(t)^3\pm\varepsilon(t).\)

_Additionally, with probability_ \(1-exp\left(-\Omega\left(n^{0.01}\right)\right)\)_, for every_ \(0\le t\le T\)_, it holds that_ \(|\mathcal{A}(t)|=n^2p(t)^4\pm np(t)\varepsilon(t)\).

A particular consequence of this proposition is that with probability \(1-exp\left(-\Omega\left(n^{0.01}\right)\right)\) the algorithm does not abort. This is because for large enough _n_, for every \(0\le t\le T\) there holds \(n^2p(t)^4-np(t)\varepsilon(t)>0\).

Proposition 3.1 can be interpreted as justifying the following independence heuristic: For every _t_ and every line \(\ell\in\mathcal{L}\), the probability that line \(\ell\) is unoccupied at time _t_ is _p(t_). If we assume independence then for every position the probability that it is available at time _t_ is _p(t_)<sup>4</sup>. Hence, the expected number of available positions is _n_<sup>2</sup>_p(t_)<sup>4</sup>. If we condition on a specific line being unoccupied, then the expected number of available positions in it is _np(t_)<sup>3</sup>.

We will use the following version of the Azuma-Hoeffding inequality.

**Theorem 3.2** (\[15, Lemma 1\])**.** _Let X_<sub>0</sub>_,X_<sub>1</sub>_,... be a supermartingale with respect to a filtration_ F<sub>0</sub>,F<sub>1</sub>_,... For every_ \(i\in\mathbb{N}\)_, let a<sub>i</sub> satisfy_ \(a_i\ge|X_i-X_{i-1}|\)_. Then, for every_ \(\lambda>0\) _and_ \(t\ge 0\)_, it holds that_

\(\mathbb{P}\left[X_t\ge X_0+\lambda\right]\le exp\left(-\frac{\lambda^2}{2\sum_{i=1}^ta_i^2}\right).\)

