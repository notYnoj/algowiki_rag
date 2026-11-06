In particular, assuming SETH, it follows that the straightforward algorithms for all the problems in the diagram cannot be substantially improved. The results depicted in this diagram, more precisely stated, are described by the following four theorems.

Building on Chen’s reduction \[Che20\] from SAT to Min-IP<sub>_n,_2<sup>_O_(log<sup>∗</sup>_n_)</sup></sub>, we show that more generally, SAT also reduces to kMin-IP. (Note that kMin-IP reduces to (k-1)Min-IP in a straightforward way, but a reduction in the other direction is not known.)

**Theorem** (Theorem A.6)**.** _Assuming_ SETH_, there is no algorithm for_ kMin-IP<sub>_n,_2<sup>_O_(log<sup>∗</sup>_n_)</sup></sub> _running in time_ \(O(n^{k-\varepsilon})\) _for any_ \(\varepsilon>0\).

Just as Min-IP reduces to LWS, we show that kMin-IP reduces to (k-1)D LWS.

**Theorem** (Theorem 3.1)**.** _Suppose there exists an algorithm for_ (k-1)D LWS _with rank d with running time_ \(O(n^{k-\varepsilon})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ kMin-IP _with rank d with running time_ \(O(n^{k-\delta})\) _for some_ \(\delta>0\).

By a divide and conquer method similar to \[KPS17, Lemma 3.5\], we show that kD LWS can be reduced to \[Static\]kD LWS.

**Theorem** (Theorem 3.2)**.** _Suppose there exists an algorithm for_ \[Static\]kD LWS<sub>_n,N,d_</sub> _with running time_ \(O(N^{2-\varepsilon}\cdot n^{k-1})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ kD LWS<sub>_n,d_</sub> _with running time_ \(O(n^{k+1-\delta})\) _for some_ \(\delta>0\).

In addition, we show that \[Static\]kD LWS also exhibits a hierarchy similar to kMin-IP.

**Theorem** (Theorem 3.4)**.** _Suppose there exists an algorithm for_ \[Static\](k-1)D LWS<sub>_n,N,d_</sub> _with running time_ \(O(N^{2-\varepsilon}\cdot n^{k-2})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ \[Static\]kD LWS<sub>_n,N,d_</sub> _with running time_ \(O(N^{2-\delta}\cdot n^{k-1})\) _for some_ \(\delta>0\).

As one consequence of these reductions, \[Static\]kD LWS,kD LWS all reduce to Min-IP, which has a truly sub-quadratic algorithm when the vector length is constant, leading to a polynomial speedup:

**Corollary.** _For every constant c\>_0 _there is an_ \(\varepsilon>0\) _such that_ kD LWS,\[Static\]kD LWS _can be solved in time_ \(O(n^{k+1-\varepsilon})\), \(O(N^{2-\varepsilon}\cdot n^{k-1})\) _respectively if the rank of the tensor w is at most c._

For one application of this corollary, we show in Section 5.1 that the generalized airplane refueling problem \[HL87\] in higher dimensions can be solved polynomially faster than the straightforward DP formulation.

Our reductions from SAT also give hardness of kD LWS assuming SETH, showing that the fast algorithm cannot extend much beyond constant rank:

**Corollary.** _Under_ SETH_, for any k\>_1 _and_ \(\varepsilon>0\)_, there is no algorithm running in time_ \(O(n^{k+1-\varepsilon})\) _for_ kD LWS _when the weight tensor has rank_ 2<sup>_O_(log<sup>∗</sup>_n_)</sup>.

SAT
Theorem A.6
[Wil05, Che20]
kMin-IP
(k-1)Min-IP
3Min-IP
Min-IP
Lemma 2.7
Theorem 3.1
[KPS17]
(k - 1)D LWS
(k - 2)D LWS
2D LWS
LWS
Theorem 3.2
[KPS17]
[Static](k - 1)D LWS
[Static](k - 2)D LWS
[Static]2D LWS
[Static]LWS
Theorem 3.4

