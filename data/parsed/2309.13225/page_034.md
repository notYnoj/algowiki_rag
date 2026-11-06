<tbc>interval are identical. Now, _C_<sup>∗</sup> has \(O(n^{\mu-\alpha})\) intervals in each row. Within each interval, _C_<sup>(_l_)</sup> has \(O\left(\frac{n^\alpha}{2^l}\right)\) intervals, so that _C_<sup>(_l_)</sup> has \(O\left(\frac{n^\mu}{2^l}\right)\) such intervals in each row.

**Definition 5.4.** _(Definition 3.1 of \[CDXZ22\]) A segment_ (_i,k,(j_<sub>0</sub>_,j_<sub>1</sub>)) _with respect to B_<sup>(_l_)</sup>_,C_<sup>(_l_)</sup> _where_ \(i\in[n^a],k\in[n^b],j_0,j_1\in[n^c]\) _and_ \(j_0\le j_1\) _satisfies that for all_ \(j_0\le j\le j_1\), \(B_{kj}^{(l)}=B_{k,j_0}^{(l)}\), \(B_{kj}^*=B_{k,j_0}^*\), \(C_{ij}^{(l)}=C_{i,j_0}^{(l)}\)_, and_ \(C_{ij}^*=C_{i,j_0}^*\).

We will also maintain sets \(T_b^{(l)}\) for \(-10\le b\le 10\) where \(T_b^{(l)}\) consists of segments (_i,k,(j_<sub>0</sub>_,j_<sub>1</sub>)) satisfying \(A_{ik}<\infty\) and \(A_{ik}^*+B_{kj}^*\neq C_{ij}^*\) and \(A_{ik}^{(l)}+B_{kj}^{(l)}=C_{ij}^{(l)}+b\) for all \(j\in[j_0,j_1]\). Finally, we turn to the computation of each _C_<sup>(_l_)</sup> matrix.

**Computing** _C_<sup>(_l_)</sup>

1. Since _p\<_2_<sup>h</sup>_, _A_<sup>(_h_)</sup>_,B_<sup>(_h_)</sup> are zero-matrices. Likewise, _C_<sup>(_h_)</sup>=0 satisfies the required properties. For \(b\neq 0\), \(T_b^{(h)}=\emptyset\) and \(T_0^{(h)}\) includes all segments (_i,k,(j_<sub>0</sub>_,j_<sub>1</sub>)) where \(A_{ik}<\infty\) and \(A_{i,k}^*+B_{k,j_0}^*\neq C_{i,j_0}^*\).<tbc>

2. Let _l\<h_. We will construct \(C^{(l)},T_b^{(l)}\) from \(C^{(l+1)},T_b^{(l+1)}\).<tbc>

(a) **Polynomial Matrix Multiplication**<br>
Construct \(A_{ik}^p=x^{A_{ik}^{(l)}-2A_{ik}^{(l+1)}}y^{A_{ik}^{(l+1)}}\) if _A<sub>ik</sub>_ finite and 0 otherwise. Define \(B_{kj}^p\) analogously. Compute _C<sup>p</sup>=A<sup>p</sup>B<sup>p</sup>_. Since the _x_ degree is either 0 or 1, and the _y_ degree is at most \(n^\alpha\), this phase requires \(\tilde{O}(n^{\omega(a,b,c)+\alpha})\) time.<tbc>

(b) **Subtracting Error Terms**<br>
If \(C_{ij}^p=0\), then \(C_{ij}^{(l)}=\infty\). Otherwise, for all _b_, we collect all monomials \(\lambda x^cy^d\) where \(d=C_{ij}^{(l+1)}+b\) and let \(C_{ijb}^p(x)\) be the sum of all such \(\lambda x^c\). Next, we compute,<tbc>

<tbc>\(R_{ijb}^p(x)=\sum_{(i,k,(j_0,j_1))\in T_b^{(l+1)},j\in[j_0,j_1]}x^{A_{ik}^{(l)}-2A_{ik}^{(l+1)}+B_{kj}^{(l)}-2B_{kj}^{(l+1)}}\)<tbc>

<tbc>Let _s<sub>ijb</sub>_ be the minimum degree of _x_ in \(C_{ijb}^p(x)-R_{ijb}^p(x)\) and compute _c<sub>ijb</sub>_=2_d+s<sub>ijb</sub>_ (or \(c_{ijb}=\infty\) if _s<sub>ijb</sub>_=0). Finally, output \(C_{ij}^{(l)}=min_bc_{ijb}\).<br>
Constructing \(C_{ijb}^p(x)\) requires \(\tilde{O}(n^{a+c+\alpha})\) time. Notice each \(T_b^{(l+1)}\) has at most 2 different \(B_{kj}^{(l)}\) and thus two \(R_{ijb}^p(x)\). Since each interval in \(B_{kj}^{(l+1)}\) is broken into at most 2 intervals, we can compute \(C_{ijb}^p(x)-R_{ijb}^p(x)\) using segment trees in \(\tilde{O}(|T_b^{(l+1)}|)\)-time. The overall time required in this stage is therefore \(\tilde{O}(n^{a+c+\alpha}+|T_b^{(l+1)}|)\).<tbc>

(c) **Computing Triples** \(T_b^{(l)}\)<br>
It is shown in \[CDXZ22\] that each segment with respect to _B_<sup>(_l_+1)</sup>_,C_<sup>(_l_+1)</sup> splits into _O_(1) segments with respect to _B_<sup>(_l_)</sup>_,C_<sup>(_l_)</sup> and furthermore \(\bigcup_BT_b^{(l)}\subset\bigcup_BT_b^{(l+1)}\), so it suffices to enumerate \(T_b^{(l+1)}\), breaking each segment into _O_(1) sub-segments. The time required is \(\tilde{O}(|T_b^{(l+1)}|)\).<tbc>

<tbc>It then suffices to bound the size of the sets \(T_b^{(l)}\), which we do below in Lemma 5.5. Finally, we can optimize parameter \(\alpha\) and compute the overall running time. Note that the overall running time is,<tbc>

<tbc>\(\tilde{O}\left(n^{(a+b+\mu)-\alpha}+n^{\omega(a,b,c)+\alpha}+n^{a+c+\alpha}\right)=\tilde{O}\left(n^{(a+b+\mu)-\alpha}+n^{\omega(a,b,c)+\alpha}\right)\)<tbc>

