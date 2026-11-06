Input: Input set S, minimum solution size \(\ell\), replacement count k, and prime bound p<sub>max</sub><br>
Output: An ESS solution for S if one exists; otherwise, NO<br>
Apply Algorithm 1 to the input set S with replacement count k to obtain a modified input<br>
set \(S'\) and the set of new elements E={e<sub>1</sub>,...,e<sub>2k</sub>}.<br>
Pick a random prime p in [p<sub>max</sub>,2p<sub>max</sub>], and a random residue r in [0,p-1].<br>
Let \(C=\{X\subseteq S'|\sum(X)\equiv_pr\}\). Enumerate the elements of C and store them one by one. If the number of stored elements exceeds \(n^d\cdot\frac{2^n}{p_\mathrm{max}}\) for some fixed constant d\>2, halt and return NO.<br>
For each \(X\in C\), let \(v_X\in\{0,1\}^k\) be the vector defined by<br>
\((v_X)_i=|X\cap\{e_{2i-1},e_{2i}\}|\mathrm{mod}2\text{for every}i\in[k]\).<br>
Let \(C'=\{(X,v_X)|X\in C\}\). Enumerate and store all elements of \(C'\).<br>
Find \((X,v_X),(Y,v_Y)\in C'\) such that \(\sum(X)=\sum(Y)\) and v<sub>X</sub>+v<sub>Y</sub>=1, where vector<br>
addition is componentwise and 1 denotes the all-one vector of length k; if no such pairs<br>
exist, return NO.<br>
Apply Lemma 3.1 to the ESS solution (X\\Y,Y\\X) for \(S'\) to recover an ESS solution for<br>
the original input set S.

and e<sub>2i</sub>. Since the algorithm outputs \(A'=X\backslash Y\) and \(B'=Y\backslash X\), we have \(A'\cup B'=X\Delta Y\) . Thus, it suffices to ensure that, for every \(i\in[k]\),

\((|X\cap\{e_{2i-1},e_{2i}\}|\mathrm{mod}2)+(|Y\cap\{e_{2i-1},e_{2i}\}|\mathrm{mod}2)=1.\)

The vector \(v_X\in\{0,1\}^k\) stored in \(C'\) records these parities for all pairs {e<sub>2i-1</sub>,e<sub>2i</sub>}. Hence, the constraint v<sub>X</sub>+v<sub>Y</sub>=1 enforces the above condition for every \(i\in[k]\). In Lemmas 3.3 and 3.4, we lower bound the probability that Algorithm 2 outputs a solution.

**Lemma 3.3.** _Assume that the solution described in Lemma 3.2 exists, and let_

\(\Phi=\left\{\sum(X)\left|\begin{array}{ c }
X\subseteq S',\exists Y\subseteq S'\text{\textit{such that}}X\neq Y,\sum(X)=\sum(Y), \\
X\Delta Y\text{\textit{contains exactly one of}}e_{2i-1}\text{\textit{and}}e_{2i}\text{\textit{for every}}i\in[k]
\end{array}\right\}.\) (1)

_Then we have_

\(|\Phi|\ge\left\{\begin{array}{ c c }
2^{n-(\ell-k)} & \text{\textit{if}}\ell-k>\frac{n}{2}, \\
\genfrac(){pt}{2}{n-(\ell-k)}{\lfloor\frac{\ell-k-1}{2}}\rfloor & \text{\textit{otherwise}}.
\end{array}\right.\)

_Proof._ Let \(A',B'\subseteq S'\) be the solution described in Lemma 3.2, and let \(Z=S'\backslash(A'\cup B')\). For any subset \(Z'\subseteq Z\), define \(X=A'\cup Z'\) and \(Y=B'\cup Z'\). Then \(X\neq Y\) and \(\sum(X)=\sum(A')+\sum(Z')=\sum(B')+\sum(Z')=\sum(Y)\). Moreover, since the same set \(Z'\) is added to both \(A'\) and \(B'\), we have \(X\Delta Y=A'\cup B'\). By the property of the solution in Lemma 3.2, \(A'\cup B'\) contains exactly one of e<sub>2i-1</sub> and e<sub>2i</sub> for every \(i\in[k]\). Hence, X and Y satisfy the defining conditions of \(\Phi\).

Therefore, every distinct value of \(\sum(Z')\) with \(Z'\subseteq Z\) gives rise to a distinct element of \(\Phi\), shifted by the fixed value \(\sum(A')\). Consequently, \(|\Phi|\ge|\{\sum(Z')|Z'\subseteq Z\}|\). It remains to lower bound the number of distinct subset sums of Z.

First, consider the case \(\ell-k>n/2\). We claim that all subset sums of Z are distinct. Suppose, for contradiction, that there exist distinct subsets \(Z_1,Z_2\subseteq Z\) such that \(\sum(Z_1)=\sum(Z_2)\). Then<tbc>

**Algorithm 2:** RandomReplacedBalancedESS

