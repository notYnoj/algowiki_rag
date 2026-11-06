## 4.1 Algorithm for binary CT-MSeq

Our algorithm for CT-MSeq on binary strings is based on Lemma 2 and Lemma 3. Firstly, we present some definitions to describe our algorithm. For any integers \(\ell\in[m]\) and \(j\in[n]\), let \(ND(\ell,j)\) be the largest integer _k_ such that _T_\[_k..j_\] contains a non- decreasing subsequence of length \(\ell\) and \(ND_0(\ell,j)\) be the largest integer _k_ such that _T_\[_k..j_\] contains a non-decreasing subsequence of length \(\ell\) _including at least one_ 0_’s._ Further, for a string _w_ and integers _i,j_ with \(i\in[|w|]\) and \(j\in[n]\), let _L<sub>w</sub>(i,j_) be the largest integer _k_ such that _T_\[_k..j_\] contains _w_\[1_..i_\] as a subsequence. If no such _k_ exists, let the values of \(ND(\ell,j)\), \(ND_0(\ell,j)\), and _L<sub>w</sub>(i,j_) be 0, respectively. For convenience, we define \(ND(\ell,0)=ND_0(\ell,0)=L_w(i,0)=0\) for any \(\ell,i\), and _w_. By the definition of _ND_, string \(T[ND(\ell,j)..j]\) is a minimal substring which contains a non-decreasing subsequence of length \(\ell\) if and only if \(ND(\ell,j-1)<ND(\ell,j)\) holds. Similarly, string \(T[ND_0(\ell,j)..j]\) is a minimal substring which contains a non-decreasing subsequence of length \(\ell\) including at least one 0’s if and only if \(ND_0(\ell,j-1)<ND_0(\ell,j)\) holds. Let \(q=min\{i\in[m]|P[i..m]\text{is a non-decreasing sequence}\}\). We also define M as the set of all minimal CT-occurrence intervals for _P_ over _T_. If _q_=1, i.e., _P_\[1_..m_\] is a non-decreasing sequence, by Observation 1, M is the set of all minimal intervals \([\ell,r]\) such that \(T[\ell..r]\) contains a non-decreasing subsequence of length _m_=|_P_|. If _q\>_1, by Lemma 3, M is the set of all minimal intervals \([\ell,r]\) such that \(T[\ell..r]\) contains _w_0<sup>_i_</sup>1<sup>_m_-|_w_|-_i_</sup> for some \(i\ge 1\) as a subsequence where _w=P_\[1_..q_-1\]. Note that the longest non-decreasing suffix _P_\[_q..m_\] of _P_ starts with character 0 if _q\>_1. Thus, the following observation holds for M (see Fig. 4 for the case of _q\>_1):

_Observation 2_ If _q_=1, \(\mathcal{M}=\{[\ell,r]|\ell=ND(m,r),r\in R\}\) holds, where \(R=\{j\in[n]|ND(m,j-1)<ND(m,j)\}\). If _q\>_1, let \(\mathcal{M}'=\{[\ell,r]|\ell=L_w(|w|,ND_0(m-|w|,r)-1),r\in[n]\}\) where _w=P_\[1_..q_-1\]. Then, \(\mathcal{M}=\{[\ell,r]\in\mathcal{M}'|\text{there is no interval}[\ell',r']\in\mathcal{M}'\text{such that}[\ell',r']\unknown[\ell,r]\}\) holds.

Now we describe an algorithm based on the above discussion which runs in _O(nm_) time with _O(n_) space.

Bw (|w|, - 1)
A'(m - |w|,r)
1
l
C
r
n
T
1
q
m
P
W

**Fig. 4** Illustration for an element \([\ell,r]\) of \(\mathcal{M}'\). By Lemma 3, if _P_ is a CT-subsequence of a substring of _T_ ending at some position \(r\in[n]\), then _P_\[_q..m_\], a non-decreasing suffix of _P_ including 0, is a CT-subsequence of _T_\[_c..r_\] where _c=ND_<sub>0</sub>(_m-q_+1_,r_) and _P_\[1_..q_-1\] is a subsequence of _T_\[_L<sub>w</sub>_(|_w|,c_-1)_..c_-1\] where _w=P_\[1_..q_-1\]. Note that \([\ell,r]\) is not necessarily a minimal CT- occurrence interval for _P_ over _T_.

