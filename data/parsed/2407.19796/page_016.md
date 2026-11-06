## Recurrence relations.

The algorithm recursively compute _L_<sub>_X_<sub>1</sub>_X_<sub>2</sub></sub>\[_i_<sub>1</sub>_,i_<sub>2</sub>_,p_<sub>1</sub>_,p_<sub>2</sub>\] for \(0\le p_a\le g_a\) and \(0<i_a\le n_a\).

Suppose \(T_1[i_1]\neq T_2[i_2]\). In this case, any common subsequence _u_ of _T_<sub>1</sub>\[1_..i_<sub>1</sub>\] and _T_<sub>2</sub>\[1_..i_<sub>2</sub>\] is a common subsequence of _T_<sub>1</sub>\[1_..i_<sub>1</sub>-1\] and _T_<sub>2</sub>\[1_..i_<sub>2</sub>\] or _T_<sub>1</sub>\[1_..i_<sub>1</sub>\] and _T_<sub>2</sub>\[1_..i_<sub>2</sub>-1\]. Every subsequence _u_ of _T_\[1_..i_-1\] is that of _T_\[1_..i_\], where it may be classified with different parameters. Notice that

• if \(u\in SubSeq^{\le h}(T[1..i-1])\) or \(u\in SufSeq^{\le h}(T[1..i-1])\),<br>
then \(u\in SubSeq^{\le h}(T[1..i])\) and \(u\in SufSeq^{\le h+1}(T[1..i])\);<tbc>

• if \(u\in\overline{SubSeq_{\ge\ell}}(T[1..i-1])\), then \(u\in\overline{SubSeq_{\ge\ell+1}}(T[1..i])\);<tbc>

• if \(u\in\overline{ SufSeq_{\ge\ell}}(T[1..i-1])\), then \(u\in\overline{SubSeq_{\ge\ell}}(T[1..i])\).

The converse of the above observation holds provided that the last character _T_\[_i_\] of _T_\[1_..i_\] is not used in _u_. Say, \(u\in\overline{SubSeq_{\ge\ell}}(T[1..i])\) implies \(u\in\overline{SubSeq_{\ge\ell-1}}(T[1..i-1])\) or \(u\in\overline{ SufSeq_{\ge\ell}}(T[1..i-1])\) for \(\ell\ge 1\). On the other hand, the definition of \(\overline{ SufSeq_{\ge\ell}}(T[1..i])\) requires to use the last character _T_\[_i_\] in its member subsequences. Based on this argument, we obtain

\(L_{X_1X_2}[i_1,i_2,p_1,p_2]=max(\{L_{X_1Y_2}[i_1,i_2-1,p_1,p_2-q]|(Y_2,q)\in\Phi(X_2,p_2)\}\)<br>
\(\cup\{L_{Y_1X_2}[i_1-1,i_2,p_1-q,p_2]|(Y_1,q)\in\Phi(X_1,p_1)\})\)

where

\(\Phi(\mathrm{B},p)=\{(\mathrm{B},p),(\mathrm{F},p)\},\Phi(\mathrm{F},p)=\left\{\begin{array}{ c c }
\{(\mathrm{B},p-1),(\mathrm{F},p-1)\} & \text{if}p>0, \\
\emptyset & \text{if}p=0,
\end{array}\right.\)<br>
\(\Phi(\overline{\mathrm{B}},p)=\left\{\begin{array}{ c c }
\{(\overline{\mathrm{B}},p-1),(\overline{\mathrm{F}},p)\} & \text{if}p>0, \\
\{(\overline{\mathrm{B}},p),(\overline{\mathrm{F}},p)\} & \text{if}p=0,
\end{array}\right.\Phi(\overline{\mathrm{F}},p)=\emptyset.\)

Suppose _T_<sub>1</sub>\[_i_<sub>1</sub>\]=_T_<sub>2</sub>\[_i_<sub>2</sub>\]. In this case, a common subsequence _u_ of _T_<sub>1</sub>\[1_..i_<sub>1</sub>\] and _T_<sub>2</sub>\[1_..i_<sub>2</sub>\] may use the last characters of _T_<sub>1</sub>\[1_..i_<sub>1</sub>\] and _T_<sub>2</sub>\[1_..i_<sub>2</sub>\], and _u_\[1_..|u_|-1\] is a common subsequence of _T_<sub>1</sub>\[1_..i_<sub>1</sub>-1\] and _T_<sub>2</sub>\[1_..i_<sub>2</sub>-1\].

Observe that for \(u=u'T[i]\),

• if \(u'\in SubSeq^{\le h}(T[1..i-1])\),<br>
then \(u\in SubSeq^{\le h+1}(T[1..i])\) and \(u\in SufSeq^{\le h+1}(T[1..i])\);<tbc>

• if \(u'\in SufSeq^{\le h}(T[1..i-1])\),<br>
then \(u\in SubSeq^{\le h}(T[1..i])\) and \(u\in SufSeq^{\le h}(T[1..i])\);<tbc>

• if \(u'\in\overline{SubSeq_{\ge\ell}}(T[1..i-1])\), then \(u\in\overline{ SufSeq_{\ge\ell}}(T[1..i])\);<tbc>

• if \(u'\in\overline{ SufSeq_{\ge\ell}}(T[1..i-1])\), then \(u\in\overline{ SufSeq_{\ge\ell+1}}(T[1..i])\).

Since the longest common subsequence does not necessarily use the last matching characters of _T_<sub>1</sub>\[1_..i_<sub>1</sub>\] and _T_<sub>2</sub>\[1_..i_<sub>2</sub>\], we obtain

\(L_{X_1X_2}[i_1,i_2,p_1,p_2]=max\big(\big\{L_{X_1Y_2}[i_1,i_2-1,p_1,p_2-q]|(Y_2,q)\in\Phi(X_2,p_2)\big\}\)<br>
\(\cup\big\{L_{Y_1X_2}[i_1-1,i_2,p_1-q,p_2]|(Y_1,q)\in\Phi(X_1,p_1)\big\}\)<br>
\(\cup\big\{1+L_{Y_1Y_2}[i_1-1,i_2-1,p_1-q_1,p_2-q_2]|\)<br>
\((Y_1,q_1)\in\Psi(X_1,p_1)\text{and}(Y_2,q_2)\in\Psi(X_2,p_2)\big\}\big)\)

