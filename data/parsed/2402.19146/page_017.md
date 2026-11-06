• _T_\[_j_\]=min(_T<sub>J</sub>)._

Moreover, a string _Q_ is said to be the _fixed longest common CT-subsequence_ (_f-CT-LCS_) of _S_ and _T_ with pivot (_i,j_) if there are no f-CT-CS with pivot (_i,j_) longer than _Q_ (see also Fig. 7).

Our solution is a dynamic programming based on the f-CT-LCS. We also consider the f-CT-LCS for substrings of _S_ and _T_. We will use positions \(i,j\in[n]\) of the input strings to indicate a pivot for substrings, namely, we say pivot \((i,j)\in[n]^2\) of substrings \(S'=S[\ell_1..r_1]\) and \(T'=T[\ell_2..r_2]\) instead of pivot \((i-\ell_1+1,j-\ell_2+1)\in[r_1-\ell_1+1]\times[r_2-\ell_2+1]\) of \(S'\) and \(T'\), where \(\ell_1\le i\le r_1\), \(\ell_2\le j\le r_2\). Let \(C(i,j,\ell_1,r_1,\ell_2,r_2)\) be the length of the f-CT-LCS of substrings \(S[\ell_1..r_1]\) and \(T[\ell_2..r_2]\) with pivot (_i,j_). It is clear from the definition that

\(\mathsf{ct}\text{\_}\mathsf{lcs}(S,T)=max\{C(i,j,1,n,1,n)|1\le i\le n,1\le j\le n\}\)

holds. The following lemma shows the main idea of computing _C(i,j,_1_,n,_1_,n_) by a dynamic programming (see also Fig. 8 for an illustration).

**Lemma 8** _For any_ \((i,j,\ell_1,r_1,\ell_2,r_2)\in[n]^6\) _that satisfies_ \(\ell_1\le i\le r_1\), \(\ell_2\le j\le r_2\)_, define_ C_<sub>L</sub> and_ C_<sub>R</sub> as follows:_

\(\mathcal{C}_L=\{C(i',j',\ell_1,i-1,\ell_2,j-1)\)<br>
\(|S[i']>S[i],T[j']>T[j],\ell_1\le i'\le i-1,\ell_2\le j'\le j-1\}\cup\{0\},\)<br>
\(\mathcal{C}_R=\{C(i',j',i+1,r_1,j+1,r_2)\)<br>
\(|S[i']>S[i],T[j']>T[j],i+1\le i'\le r_1,j+1\le j'\le r_2\}\cup\{0\}.\)

_Then the recurrence_ \(C(i,j,\ell_1,r_1,\ell_2,r_2)=max\mathcal{C}_L+max\mathcal{C}_R+1\) _holds._

_Proof_ Let _Q_ be the f-CT-LCS of \(S[\ell_1..r_1]\) and \(T[\ell_2..r_2]\) with (_i,j_). By Definition 4, there exist subscript sequences _I_=(_i_<sub>1</sub>_,...,i_<sub>|_Q_|</sub>) and _J_=(_j_<sub>1</sub>_,...,j_<sub>|_Q_|</sub>) that satisfy CT(_Q_)=CT(_S<sub>I</sub>_)=CT(_T<sub>J</sub>_). It is also clear from the definition that _S_\[_i_\]=min(_S<sub>I</sub>_) and _T_\[_j_\]=min(_T<sub>J</sub>_) hold. Let _q_=min\_id(_Q_). We show that _q_-1=maxC_<sub>L</sub>_ holds.

l1
i*
i
r1
S
l2
j*
j
r2
T
CT(Q)
q - 1
|Q| - q
max CL
max CR

**Fig. 8** Sketch of our recurrence by Lemma 8.

