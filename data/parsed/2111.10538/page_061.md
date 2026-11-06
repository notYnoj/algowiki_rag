Using definition of \(\lambda\), we have

\(\lambda^{1+y}\le\frac{\sum n_i\lambda_i^{1+y}}{\sum n_i}.\)

**Theorem A.8** (A well-known algorithm also used in \[HSSS19\])**.** _Given two strings A and B, one can with preprocessing time O_(|_B_|log|_B_|) _verify if the LCS of A and B is at least q or not in time O_(|_A|q_log|_B_|)_. In case the answer is positive, finding such a common subsequence can be done in time O_(|_A|q_log|_B_|).

_Proof._ In the preprocessing step, for each character _x_ in _B_, we construct a binary tree that keeps track of all the places that _x_ appears in _B_. This enables us to answer the following queries in _O_(log|_B_|) time: _Given an index i of B and a character x, what is the smallest index_ \(i'\ge i\) _such that_ \(B_{i^\prime}=x\)?

To find the LCS of _A_ and _B_, we slightly modify the conventional dynamic program for computing LCS and construct a two-dimensional array _T_<sup>∗</sup> that stores the following information

\(T^*[i][j]=\left\{\begin{array}{ c c }
\text{the smallest}k\text{s.t.} & \text{if}|\mathsf{lcs}(A[1,i],B)|\ge j \\
|\mathsf{lcs}(A[1,i],B[1,k])|=j & 
\end{array}\right.\)

Using the above definition, we can construct table _T_<sup>∗</sup> via the following recursive formula:

\(T^*[i][j]:=\mathrm{min}\left\{\begin{array}{ c }
T^*[i-1][j], \\
f(T^*[i-1][j-1]+1,A_i)
\end{array}\right\}\) (24)

where _f(T_<sup>∗</sup>\[_i_-1\]\[_j_-1\]+1_,A<sub>i</sub>_) is the index of the first occurrence of _A<sub>i</sub>_ in _B_ after position _T_<sup>∗</sup>\[_i_-1\]\[_j_-1\] (or \(\infty\) if \(A_i^*\) does not appear in _B_ after position _T_<sup>∗</sup>\[_i_-1\]\[_j_-1\]). Since such queries can be answered in _O_(log|_B_|) time then the overall runtime of the algorithm is _O_(|_A|q_log|_B_|).

