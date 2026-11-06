## _High-level description_

First, we compute \(q=\mathrm{min}\{i\in[m]|P[i..m]\text{is a non-decreasing sequence}\}\) in _O(m_) time. If _q_=1, we compute the values of _ND(m,j_) for all integers \(j\in[n]\). By Observation 2, M can be computed in _O(n_) time from the values of \(ND(m,\cdot)\).

If _q\>_1, let _w=P_\[1.._q_-1\]. We compute the values of _ND_<sub>0</sub>(_m_-|_w|,j_) and _L<sub>w</sub>_(|_w|,j_) for all integers \(j\in[n]\). By Observation 2, \(\mathcal{M}'\) can be computed in _O(n_) time from the values of \(ND_0(m-|w|,\cdot)\) and \(L_w(|w|,\cdot)\). Then, we can obtain M by removing non-minimal intervals from \(\mathcal{M}'\). Since every interval in \(\mathcal{M}'\) is a sub-interval of \[1_,n_\], we can remove such non-minimal intervals in _O(n_) time by using bucket sort.

Therefore, in each of the cases _q_=1 and _q\>_1, the remaining task is to compute the values of _ND(m,j_), _ND_<sub>0</sub>(_m_-|_w|,j_) and _L<sub>w</sub>_(|_w|,j_) for all \(j\in[n]\).

## _Computing ND_

Let \(prev_0(j)=\mathrm{max}(\{i<j|T[i]=0\}\cup\{0\})\). The values of _prev_<sub>0</sub>(_j_) for all \(j\in[n]\) can be computed in _O(n_) time by scanning _T_ from right to left. Let \(Z(\ell,j)\) be the staring position of the longest suffix of _T_\[1.._j_\] that contains \(0^\ell\) as a subsequence. If no such suffix exists, let \(Z(\ell,j)=0\). The values of _Z_ can be computed in _O(nm_) time by using the following recurrence:

\(Z(\ell,j)=\left\{\begin{array}{ c c }
Z(\ell-1,prev_0(j)) & \text{if}T[j]=0, \\
Z(\ell,j-1) & \text{if}T[j]=1.
\end{array}\right.\)

Then, we show how to compute _ND_ (along with _Z_). We first initialize \(ND(\ell,0)=0\) for all \(\ell\in[m]\) and _ND_(1_,j_)=_j_ for all \(j\in[n]\). Then, we can compute _ND(m,j_) for incremental \(\ell=1,2,\dots,m\) and _j_=1,2_,...,n_ by using the following recurrence:

\(ND(\ell,j)=\left\{\begin{array}{ c c }
\mathrm{max}\{Z(\ell,j),ND(\ell,j-1)\} & \text{if}T[j]=0, \\
ND(\ell-1,j-1) & \text{if}T[j]=1.
\end{array}\right.\)

We describe the above recurrence in detail in below. Let \(k=ND(\ell,j)>0\). By the definition of _ND_, there exists a subscript sequence \(I(k,j_1,\dots,j_{\ell-1})\) satisfying \(k<j_1<\cdots<j_{\ell-1}\le j\) such that _T_\[_k..j_\] contains a non-decreasing subsequence _T<sub>I</sub>_. If _T_\[_j_\]=0 and \(j_{\ell-1}=j\), then \(T[j_{\ell-1}]=0\) holds, and thus, \(T_I=0^\ell\). Hence, \(k=Z(\ell,j)\) holds. If _T_\[_j_\]=0 and \(j_{\ell-1}<j\), then _T_\[_k..j_-1\] also contains _T<sub>I</sub>_ as a subsequence. Thus, \(k=ND(\ell,j-1)\) holds. Finally, if _T_\[_j_\]=1, then \(j_{\ell-1}=j\) always holds, and thus, _T_\[_k..j_-1\] contains a non-decreasing subsequence of length \(\ell-1\). This leads to \(k=ND(\ell-1,j-1)\). Therefore, the above recurrence for _ND_ holds.

The time complexity of computing values of _ND_ is _O(nm_). Although _ND_ has \(\Theta(nm)\) values, the working space can be reduced to _O(n_) since we only refer to the \(\ell\)th or the \((\ell-1)\)th rows of _ND_ and _Z_ when computing the \(\ell\)th rows of _ND_ and _Z_, respectively.

