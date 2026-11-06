**_Computing_** _ND_<sub>0</sub>

By the definitions of _ND_ and _ND_<sub>0</sub>, The following relation holds.

\(ND_0(\ell,j)=\left\{\begin{array}{ c c }
ND(\ell,j) & \text{if}T[ND(\ell,j)]=0, \\
prev_0(ND(\ell,j)) & \text{otherwise.}
\end{array}\right.\)

This relation implies that, for every \(j\in[n]\), if we already have _ND(m_-|_w|,j_), then _ND_<sub>0</sub>(_m_-|_w|,j_) can be obtained _O_(1) time. Thus, we can compute the values of _ND_<sub>0</sub>(_m_-|_w|,j_) for all \(j\in[n]\) in _O(nm_) time using _O(n_) space.

**_Computing_** _L<sub>w</sub>_

We note that the definition of _L<sub>w</sub>_ is equivalent to the definition of the table, named _S_, used in \[7\] for the episode matching problem. Thus, we can use the same recurrence as in \[7\] to compute _L<sub>w</sub>_:

\(L_w(i,j)=\left\{\begin{array}{ c c }
L_w(i-1,j-1) & \text{if}w[i]=T[j], \\
L_w(i,j-1) & \text{otherwise,}
\end{array}\right.\)

with the initialization _L<sub>w</sub>(i,_0)=0 for each \(i\in[|w|]\) and _L<sub>w</sub>_(0_,j_)=_j_+1 for each \(0\le j\le n\). We can obtain _L<sub>w</sub>_(|_w|,j_) for all \(j\in[n]\) in \(O(n|w|)\subseteq O(nm)\) time using _O(n_) space \[7\].

From the above discussion, we can compute the values of _ND(m,j_), _ND_<sub>0</sub>(_m_-|_w|,j_) and _L<sub>w</sub>_(|_w|,j_) for all \(j\in[n]\) in _O(nm_) time and _O(n_) space. Therefore, we obtain the following theorem:

**Theorem 1** _CT-MSeq on binary strings can be solved in O(nm_) _time and O(n_) _space._

## 4.2 Conditional lower bound for CT-MSeq

In this section, we prove the following theorem.

**Theorem 2** _If there is an_ \(\epsilon>0\) _such that CT-MSeq for an alphabet of size_ 4 _can be solved in_ \(O((|T||P|)^{1-\epsilon})\) _time, then OVH and SETH are false._

We show the proof of Theorem 2 in the end of this section. To prove Theorem 2, we reduce the OV problem to the _shortest-CT-MSeq_ problem (s-CT-MSeq) defined as follows, which is a relaxed version of CT-MSeq.

_Problem 3_ (Shortest Cartesian-Tree Subsequence Matching problem (s-CT-MSeq)) Given two strings _T_ and _P_, find a shortest substring in _T_ such that _P_ is a CT-subsequence of the substring.

