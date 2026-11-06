<tbc>For \(F'\) to become dense we require \(q\ge\underline{q}\equiv(n-m-1)/m\). For \(q\gg\underline{q}\) the cost of computing \(F'\) can be estimated as O(_qmn_<sup>2</sup>). A matrix chain product of length _q_ needs to be evaluated, where one factor has bandwidth 2_m_+1 and the other factor becomes dense for \(q\ge\underline{q}\). Superiority of the matrix-free Newton method follows immediately for \(m\checkmark n\) as O(_qm_<sup>2</sup>_n)\<_O(_qmn_<sup>2</sup>).

In most real-world scenarios the accumulation of \(F'\) is likely to dominate the overall computational cost yielding a reduction of the computational cost of the matrix-free Newton method over the cost of the standard Newton method by \(\mathcal{O}(\frac{n}{m})\). Nevertheless, let the computational cost of a Newton step be dominated by the solution of the linear Newton system. Superiority of the matrix-free Newton method requires O(_qm_<sup>2</sup>_n)\<_O(_n_<sup>3</sup>), which will only be violated for _q\>n_ assuming _n_=O(_m_<sup>2</sup>).

Let all \(F'_i\) be tridiagonal. For example, this scenario occurs in the context of implicit Euler integration for one-dimensional diffusion with spacial discretization performed by central finite differences. In-place _LU_ factorization using the Thomas algorithm \[23\] yields the tridiagonal _L<sub>i</sub>-I<sub>n</sub>-U<sub>i</sub>_ at a computational cost of O(_n_). The 2_q_ linear systems in Equation (2.8) can be solved with a cost of the same order, respectively. The total computational cost of the matrix-free Newton method adds up to O(_qn)\<_max(O(_qn_<sup>2</sup>),O(_n_<sup>3</sup>)). The speedup of \(\mathcal{O}(\frac{n}{m})=\mathcal{O}(n)\) is illustrated in Figure 3 showing the results of various experiments for a single Newton step and \(q/n=0.5,1,2,4,0<n\le 10^3\). The _"factorize first, then accumulate"_ approach implements the new matrix-free Newton method. It yields the bottom line in all four sub-figures of Figure 3. The _"accumulate first, then factorize"_ approach uses OpenBLAS’ `gbmv` method (`www.openblas.net`) for multiplying banded matrices with dense vectors. It exceeds the computational cost of the new method by roughly a factor of _n_. Our search for a dedicated method for multiplying banded matrices turned out unsuccessful. We would expect such an algorithm to be more efficient for

Chain Length q = n/2
Chain Length q = n
105
Factorized OpenBLAS: gbmv
105
Factorized OpenBLAS: gbmv
104
104
103
103
102
Time [ms]
Time [ms]
102
101
101
100
100
10-1
10-1
0
100
200
300
400
500
600
700
800
900
1000
0
100
200
300
400
500
600
700
800
900
1000
n
n
Chain Length q = 2n
Chain Length q = 4n
105
Factorized OpenBLAS: gbmv
105
Factorized OpenBLAS: gbmv
104
104
103
103
102
Time [ms]
Time [ms]
102
101
101
100
100
10-1
10-1
0
100
200
300
400
500
600
700
800
900
1000
0
100
200
300
400
500
600
700
800
900
1000
n
n

Fig. 3. _Tridiagonal Elemental Jacobians_

