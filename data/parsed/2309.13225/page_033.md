**Assumption 5.2.** _(Assumption 3.1 of \[CDXZ22\]) Let_ \(i\in[n^a],k\in[n^b],j\in[n^c]\)_. For all i,k, A<sub>ik</sub> is either_ \(\infty\) _or_ \((A_{ik}modp)<\frac{p}{3}\)_. For all k,j, B<sub>kj</sub> is either_ \(\infty\) _or_ \(\left(B_{kj}modp\right)<\frac{p}{3}\)_. Each row of B is monotone._

**Lemma 5.3.** _(Lemma 3.4 of \[CDXZ22\]) Let A be a_ \(n^a\times n^b\) _integer matrix with non-negative entries bounded by O(n). Let B be a_ \(n^b\times n^c\) _row-monotone integer matrix with non-negative entries bounded by O(n). The computation A∗B can be reduced to a constant number of A<sup>i</sup>∗B<sup>i</sup> where A<sup>i</sup>,B<sup>i</sup> satisfy Assumption 5.2._

_Proof._ We only define the relevant matrices, leaving the proof to \[CDXZ22\]. Define for \(i\in\{1,2,3\}\),

\(A_{ik}^{((i)}=\left\{\begin{array}{ c c }
A_{ik} & \frac{(i-1)p}{3}<(A_{ik}modp)<\frac{ip}{3} \\
\infty & \text{o/w}
\end{array}\right.\)<br>
\(B_{kj}^{(1)}=\left\{\begin{array}{ c c }
B_{kj} & (B_{kj}modp)<\frac{p}{3} \\
p\left\lfloor B_{kj}/p+1\right\rfloor & \frac{p}{3}\le(B_{kj}modp)<\frac{2p}{3} \\
p\left\lfloor B_{kj}/p+1\right\rfloor & \frac{2p}{3}\le(B_{kj}modp)
\end{array}\right.\)<br>
\(B_{kj}^{(2)}=\left\{\begin{array}{ c c }
p\left\lfloor B_{kj}/p\right\rfloor+\left\lceil p/3\right\rfloor & (B_{kj}modp)<\frac{p}{3} \\
B_{kj} & \frac{p}{3}\le(B_{kj}modp)<\frac{2p}{3} \\
p\left\lfloor B_{kj}/p+1\right\rfloor & \frac{2p}{3}\le(B_{kj}modp)
\end{array}\right.\)<br>
\(B_{kj}^{(3)}=\left\{\begin{array}{ c c }
p\left\lfloor B_{kj}/p\right\rfloor+\left\lceil 2p/3\right\rfloor & (B_{kj}modp)<\frac{p}{3} \\
p\left\lfloor B_{kj}/p\right\rfloor+\left\lceil 2p/3\right\rfloor & \frac{p}{3}\le(B_{kj}modp)<\frac{2p}{3} \\
B_{kj} & \frac{2p}{3}\le(B_{kj}modp)
\end{array}\right.\)

Then, the matrices,

\(A^{(1)},A^{(2)}-\left\lceil p/3\right\rceil,A^{(3)}-\left\lceil 2p/3\right\rceil,B^{(1)},B^{(2)}-\left\lceil p/3\right\rceil,B^{(3)}-\left\lceil 2p/3\right\rceil\)

all satisfy Assumption 5.2.

Define _h_ such that \(2^{h-1}\le p<2^h\). For all \(0\le l\le h\), define \(A_{ik}^{(l)}=\left\lfloor\frac{A_{ik}modp}{2^l}\right\rfloor\) if _A<sub>ik</sub>_ is finite and \(\infty\) otherwise. Define \(B_{kj}^{(l)}=\left\lfloor\frac{B_{kj}modp}{2^l}\right\rfloor\) if _B<sub>kj</sub>_ is finite and \(\infty\) otherwise. Define \(A_{ik}^*=\left\lfloor A_{ik}/p\right\rfloor\) if _A<sub>ik</sub>_ is finite and \(\infty\) otherwise. Define \(B_{kj}^*=\left\lfloor B_{kj}/p\right\rfloor\) if _B<sub>kj</sub>_ is finite and \(\infty\) otherwise. Since _A_<sup>∗</sup>_,B_<sup>∗</sup> are monotone, _C_<sup>∗</sup>=_A_<sup>∗</sup>∗_B_<sup>∗</sup> can be computed in \(\tilde{O}(n^{(a+b+\mu)-\alpha})\) time using segment trees as described in \[CDXZ22\]. If _C<sub>ij</sub>_ is finite, then by Assumption 5.2 \(C_{ij}modp<\frac{2p}{3}\) so that \(C_{ij}^*=\left\lfloor C_{ij}/p\right\rfloor\).

In the next phase, we compute _C_<sup>(_l_)</sup> for _l=h,h_-1_,...,_0. Note that _C_<sup>(_l_)</sup> is not necessarily _A_<sup>(_l_)</sup>∗_B_<sup>(_l_)</sup>. We require _C_<sup>(_l_)</sup> to satisfying the following properties if _C<sub>ij</sub>_ is finite:

1. \(\left\lfloor\frac{(C_{ij}modp)-2(2^l-1)}{2^l}\right\rfloor\le C_{ij}^{(l)}\le\left\lfloor\frac{(C_{ij}modp)+2(2^l-1)}{2^l}\right\rfloor\)<tbc>

2. If \(C_{i,j_0}^*=C_{i,j_1}^*\) for _j_<sub>0</sub>_\<j_<sub>1</sub>, the elements \(C_{i,j_0}^{(l)},C_{i,j_0+1}^{(l)},\dots,C_{i,j_1}^{(l)}\) are monotonically non- decreasing.

Notice that when _l_=0, we have \(C_{ij}^{(0)}=C_{ij}modp\), which combined with \(C_{ij}^*\) allows us to recover _C<sub>ij</sub>_.

The entries of _A_<sup>(_l_)</sup>_,B_<sup>(_l_)</sup>_,C_<sup>(_l_)</sup> are therefore non-negative integers at most \(O\left(\frac{n^\alpha}{2^l}\right)\) or \(\infty\). Since _B_<sup>(_l_)</sup> is monotone, every row is composed of at most \(O\left(\frac{n^\alpha}{2^l}\right)\) intervals, where all the values in each<tbc>

