\(T[j']>T[j],i+1\le i'\le r_1,j+1\le j'\le r_2\}\cup\{0\}.\)

<tbc>It follows from the definitions that

\(\mathtt{ct\text{\_}l\text{cs}}(S,T)=max\{L(i,j,1,1)+R(i,j,n,n)+1|1\le i\le n,1\le j\le n\}.\)

Then we can obtain an _O(n_<sup>6</sup>)-time and _O(n_<sup>4</sup>)-space algorithm for solving CT-LCS based on Lemma 9. Our algorithm computes two dimensional tables _L_ and _R_. For each fixed \((i,j)\in[n]^2\) (i.e., _O(n_<sup>2</sup>) iterations), we can compute \(L(i,j,\cdot,\cdot)\) and \(R(i,j,\cdot,\cdot)\) in _O(n_<sup>4</sup>) time. The algorithm finally returns \(\mathtt{ct\text{\_}l\text{cs}}(S,T)=max\{L[i][j][1][1]+R[i][j][n][n]+1|1\le i\le n,1\le j\le n\}\). Therefore, we can compute table _C_ in _O(n_<sup>6</sup>) time and _O(n_<sup>4</sup>) space.

**Theorem 4** _CT-LCS can be solved in O(n_<sup>6</sup>) _time and O(n_<sup>4</sup>) _space._

We can compute a CT-LCS by storing the following additional information: We store pivot \((i',j')\) with \(L(i,j,\ell_1,\ell_2)\) that satisfies \(L[i][j][\ell_1][\ell_2]=L[i'][j'][\ell_1][\ell_2]+R[i'][j'][i-1][j-1]+1\) (also for _R_). If we do so, we can compute a CT-LCS by tracking back the tables from the pivot (_i,j_) that gives ct\_lcs(_S,T_) in _O_(|ct\_lcs(_S,T_)|)=_O(n_) time.

**Corollary 1** _A CT-LCS can be computed in O(n_<sup>6</sup>) _time and O(n_<sup>4</sup>) _space._

## 5.2 CT-LCS algorithm for binary

In this section, we propose an algorithm for solving CT-LCS for the binary alphabet {0,1}. Throughout this section, we assume that the strings _S_ and _T_ are binary strings and discard the assumption that all characters are distinct in _S_ and in _T_.

Similarly to our algorithm for CT-MSeq for binary alphabets, which was proposed in Section 4.1, our algorithm for CT-MSeq on binary strings is based on Lemma 2 and Lemma 3.

Let _N_<sub>1</sub>(_S_) be the number of occurrences of 1 in string _S_, and _L_<sub>01</sub>(_S_) the length of the longest non-decreasing subsequence of _S_ that contains 0. If there is no such subsequence, let _L_<sub>01</sub>(_S_)=0. We also define cand(_S,T_) as the maximum integer \(k=|w|+i+j=|w|+i'+j'\) such that _w_0_<sup>i</sup>_1_<sup>j</sup>_ is a subsequence of _S_ and \(w0^{i^\prime} 1^{j^\prime}\) is a subsequence of _T_ for some string _w_, and integers \(i,i'\ge 1,j,j'\ge 0\). Then the following properties hold for subsequences \(S'\) and \(T'\) of _S_ and _T_ that give ct\_lcs(_S,T_).

• If 0 appears in both \(S'\) and \(T'\), ct\_lcs(_S,T_)=cand(_S,T_) (by Lemma 3).<tbc>

• If either \(S'\) or \(T'\) does not contain 0, ct\_lcs(_S,T_) equals min(_N_<sub>1</sub>(_S),L_<sub>01</sub>(_T_)) or min(_N_<sub>1</sub>(_T),L_<sub>01</sub>(_S_)), respectively (from Lemma 2).<tbc>

• If 0 does not appears in both \(S'\) and \(T'\), ct\_lcs(_S,T_)=min(_N_<sub>1</sub>(_S),N_<sub>1</sub>(_T_)).<tbc>

<tbc>Due to the above properties, ct\_lcs(_S,T_)=max(cand(_S,T),m_<sub>1</sub>_,m_<sub>2</sub>_,m_<sub>3</sub>) holds for _m_<sub>1</sub>=min(_N_<sub>1</sub>(_S),L_<sub>01</sub>(_T_)), _m_<sub>2</sub>=min(_N_<sub>1</sub>(_T),L_<sub>01</sub>(_S_)), and _m_<sub>3</sub>=min(_N_<sub>1</sub>(_S),N_<sub>1</sub>(_T_)).<tbc>

