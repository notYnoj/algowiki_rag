Now we are ready to describe our algorithm. Let _LND<sub>S</sub>(i_)=_L_<sub>01</sub>(_S_\[_i..n_\]) for any integer _i_ with \(1\le i\le n\). For convenience, let _LND<sub>S</sub>(n_+1)=0. Firstly, we compute _N_<sub>1</sub>(_S_\[_i..n_\]), _N_<sub>1</sub>(_T_\[_i..n_\]), _LND<sub>S</sub>(i_), and _LND<sub>T</sub>(i_) for all _i_ that satisfies \(1\le i\le n\). We can easily compute _N_<sub>1</sub>(_S_\[_i..n_\]) and _N_<sub>1</sub>(_T_\[_i..n_\]) for all _i_ in _O(n_) time and space. We can also compute _LND<sub>S</sub>(i_) (and _LND<sub>T</sub>(i_) in a similar way) by using the following recurrence:

\(LND_S(i)=\left\{\begin{array}{ c c }
max(LND_S(i+1)+1,N_1(S[i+1..n])+1) & \text{if}S[i]=0, \\
LND_S(i+1) & \text{if}S[i]=1.
\end{array}\right.\)

These values can also be computed in _O(n_) time and space.

Since cand(_S,T_) requires the length of _w_ which is described in the above discussion, we use a data structure for computing the longest common subsequence LCS(_i,j_) of _S_\[1_..i_\] and _T_\[1_..j_\]. For convenience, we set LCS(_i,_0)=LCS(0_,i_)=0 for all \(i\in[n]\cup\{0\}\). By using the Four-Russians method \[12\], we can compute an _O(n_<sup>2</sup>/log_n_)-space data structure in _O(n_<sup>2</sup>/log_n_) time that can answer LCS(_i,j_) in _O_(log<sup>2</sup>_n_) time for any \(i\in[n]\cup\{0\}\) and \(j\in[n]\cup\{0\}\). By the definition of cand, the following equation can be obtained:

\(\mathsf{cand}(S,T)=max_{1\le\ell\le n}\{\mathsf{LCS}(p_\ell-1,q_\ell-1)+\ell\}\)

where \(p_\ell=max\{p|LND_S(p)=\ell\}\) and \(q_\ell=max\{q|LND_T(q)=\ell\}\) (see also Fig. 9 for an illustration). Since we have already computed _LND<sub>S</sub>(i_), _LND<sub>S</sub>(i_), and the data structure for LCS, we can compute cand(_S,T_) in _O(n_log<sup>2</sup>_n_) time based on the above equation. Finally, we can obtain ct\_lcs(_S,T_) by computing max(cand(_S,T),m_<sub>1</sub>_,m_<sub>2</sub>_,m_<sub>3</sub>) in constant time (see also Algorithm 2).

**Theorem 5** _CT-LCS on binary strings can be solved in O(n_<sup>2</sup>/log_n_) _time and O(n_<sup>2</sup>/log_n_) _space._

We can reconstruct a CT-LCS of _S_ and _T_ in _O(n_log_n_) time as follows: If one of _m_<sub>1</sub>, _m_<sub>2</sub>, and _m_<sub>3</sub> gives ct\_lcs(_S,T_), we can easily obtain a CT-LCS in _O(n_) time by using _LND<sub>S</sub>(i_) and _LND<sub>T</sub>(i_). Otherwise, two subsequences \(S'\) and \(T'\) which give ct\_lcs(_S,T_) can be represented as \(S'=w0^i1^{\ell-i}\) and \(T'=w0^j1^{\ell-j}\) for some _i_ and _j_. Integers _i_ and _j_ can be obtained by _LND<sub>S</sub>(i_) and _LND<sub>T</sub>(i_). In the Four-Russians<tbc>

P
S
0i1e-i
W
0j1e-j
LCS(pe - 1,qe - 1)
l
T
qe

**Fig. 9** Illustration for our idea for computing cand(_S,T_).

