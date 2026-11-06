Input: Strings \(S[1..n],T[1..n]\in\Sigma^*\)<br>
Output: ct\_lcs(S,T)<br>
Find i<sub>1</sub>,i<sub>2</sub>,...,i<sub>n</sub> that satisfy \(S[i_1]>S[i_2]>\cdots>S[i_n]\);<br>
Find j<sub>1</sub>,j<sub>2</sub>,...,j<sub>n</sub> that satisfy \(T[j_1]>T[j_2]>\cdots>T[j_n]\);<br>
\(ctlcs\leftarrow 0\);<br>
for \(i\leftarrow i_1\) to i<sub>n</sub> do<br>
   for \(j\leftarrow j_1\) to j<sub>n</sub> do<br>
   for \(\ell_1\leftarrow 1\) to i do<br>
   for \(r_1\leftarrow i\) to n do<br>
   for \(\ell_2\leftarrow 1\) to j do<br>
   for \(r_2\leftarrow j\) to n do<br>
   \(\mathcal{C}_L\leftarrow 0\);<br>
   if \(\ell_1\neq i\) and \(\ell_2\neq j\) then<br>
   for \(i'\leftarrow\ell_1\) to i-1 do<br>
   for \(j'\leftarrow\ell_2\) to j-1 do<br>
   if \(S[i']>S[i]\) and \(T[j']>T[j]\) then<br>
\(\mathcal{C}_L\leftarrow max(\mathcal{C}_L,C[i'][j'][\ell_1][i-1][\ell_2][j-1])\)<br>
;<br>
   \(\mathcal{C}_R\leftarrow 0\);<br>
   if \(r_1\neq i\) and \(r_2\neq j\) then<br>
   for \(i'\leftarrow i+1\) to r<sub>1</sub> do<br>
   for \(j'\leftarrow j+1\) to r<sub>2</sub> do<br>
   if \(S[i']>S[i]\) and \(T[j']>T[j]\) then<br>
\(\mathcal{C}_R\leftarrow max(\mathcal{C}_R,C[i'][j'][i+1][r_1][j+1][r_2])\)<br>
;<br>
   \(C[i][j][\ell_1][r_1][\ell_2][r_2]\leftarrow\mathcal{C}_L+\mathcal{C}_R+1\);<br>
   \(ctlcs\leftarrow max(ctlcs,C[i][j][1][n][1][n])\);<br>
return ctlcs

<tbc>Then we can represent \(C(i,j,\ell_1,r_1,\ell_2,r_2)\) as

\(C(i,j,\ell_1,r_1,\ell_2,r_2)=L(i,j,\ell_1,\ell_2)+R(i,j,r_1,r_2)+1.\)

Based on this recurrence, we can obtain the following alternative lemma.

**Lemma 9** _For any_ \((i,j,\ell_1,r_1,\ell_2,r_2)\in[n]^6\) _that satisfies_ \(\ell_1\le i\le r_1\), \(\ell_2\le j\le r_2\)_, the following recurrences hold:_

\(L(i,j,\ell_1,\ell_2)=max\{L(i',j',\ell_1,\ell_2)+R(i',j',i-1,j-1)+1|S[i']>S[i],\)<br>
\(T[j']>T[j],\ell_1\le i'\le i-1,\ell_2\le j'\le j-1\}\cup\{0\},\)<br>
\(R(i,j,r_1,r_2)=max\{L(i',j',i+1,j+1)+R(i',j',r_1,r_2)+1|S[i']>S[i],\)

**Algorithm 1:** Algorithm for solving CT-LCS

