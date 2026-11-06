## 4.6 A note on a potential implication of \[10\]

In this section, \(\alpha\in(0,1)\), \(\upsilon=n^\alpha\), and \(\overrightarrow{r}\) is a random alignment. Let \(X'_1,\dots,X'_n,Y'_1,\dots,Y'_n\) be independent Bernoulli variables with parameter 1/2, independent from all the previous variables. As previously, we write _Z_=(_Z_<sub>1</sub>_,...,Z_<sub>2_n_</sub>):=(_X_<sub>1</sub>_,...,X<sub>n</sub>,Y_<sub>1</sub>_,...,Y<sub>n</sub>_), and as in \[10\], for \(j\in\{1,\dots,2n\}\), let

\(\Delta_j:=LCS(Z)-LCS(Z_1\cdots Z'_j\cdots Z_{2n})\)<br>
\(\widetilde{\Delta}_j:=LCS\left(P_i\right)-LCS\left(P'_i\right)\)

where _P<sub>i</sub>_ is the cell of length \(\upsilon\) containing _Z<sub>j</sub>_ and \(P'_i\) is the same cell but with \(Z'_j\) instead of _Z<sub>j</sub>_. We also write for \(j,k\in\{1,\dots,m\}\):

\(LC_n^j:=LCS(Z_1\cdots Z'_j\cdots Z_{2n})\)<br>
\(LC_n^{j,k}:=LCS(Z_1\cdots Z'_j\cdots Z'_k\cdots Z_{2n})\)<br>
\(\Delta_{j,k}:=LC_n-LC_n^j-LC_n^j+LC_n^{j,k}.\)

It is claimed in \[10\] that \(\mathbb{E}\left|\widetilde{\Delta}_j-\Delta_j\right|=\mathbb{E}\left(\widetilde{\Delta}_j-\Delta_j\right)\) is exponentially small in _n_. The equality comes from the fact that \(\widetilde{\Delta}_j-\Delta_j\ge 0\) (as explained in \[10\]). Furthermore, \(\mathbb{E}\Delta_j=0\), so the problem boils to controlling \(\widetilde{\Delta}_j\). Let us assume, in this section, that \(\mathbb{E}\widetilde{\Delta}_j\le exp(-tn)\) for some _t\>_0 not depending on _j,n_, and let us denote by _A<sub>j</sub>_ the event \(\widetilde{\Delta}_j-\Delta_j=0\). Of course, \(\mathbb{P}(A_j^c)\le exp(-tn)\). Finally, let _C<sub>j,k</sub>_ be the event "_Z<sub>j</sub>_ and _Z<sub>k</sub>_ are not in the same cell". Let \(j,k\in\{1,\dots,n\}\) and suppose _A<sub>j</sub>_, _A<sub>k</sub>_ and _C<sub>j,k</sub>_ are all realized, then when _X<sub>j</sub>_ is flipped to \(X'_j\), the alignment \(\overrightarrow{r}=\overrightarrow{r}(Z)\) is still an alignment for \((Z_1,\dots,Z'_j,\dots,Z_{2n})\), so<tbc>

\(LC_n^{j,k}-LC_n^j\ge-\widetilde{\Delta}_k=LC_n^k-LC_n\)

<tbc>so, in other terms,

\(\Delta_{j,k}\mathbb{1}_{A_j}\mathbb{1}_{A_k}\mathbb{1}_{C_{j,k}}\ge 0.\) (4.8)

Let us write \(\Delta_{j,k}=\Delta_{j,k}^+-\Delta_{j,k}^-\) (the positive and negative parts), using the bounds \(|\Delta_{j,k}|\le 2\) and (4.8) we get<tbc>

\(\Delta_{j,k}^-\le 2(1-\mathbb{1}_{A_j}\mathbb{1}_{A_k}\mathbb{1}_{C_{j,k}})\)

<tbc>so \((\Delta_{j,k}^-)^2\le 4(1-\mathbb{1}_{A_j}\mathbb{1}_{A_k}\mathbb{1}_{C_{j,k}})\), and<tbc>

\(\mathbb{E}(\Delta_{j,k}^-)^2\le 4\left(\mathbb{P}(A_j^c)+\mathbb{P}(A_k^c)+\mathbb{P}(C_{j,k}^c)\right),\)<br>
\(\mathbb{E}(\Delta_{j,k}^+)^2\le 2\mathbb{E}\Delta_{j,k}^+=2\mathbb{E}\Delta_{j,k}^-\le 4\left(\mathbb{P}(A_j^c)+\mathbb{P}(A_k^c)+\mathbb{P}(C_{j,k}^c)\right),\)

<tbc>hence<tbc>

\(\mathbb{E}(\Delta_{j,k})^2\le 8\left(\mathbb{P}(A_j^c)+\mathbb{P}(A_k^c)+\mathbb{P}(C_{j,k}^c)\right).\)

<tbc>We may now give an upper bound on _B_<sub>1</sub>(2_n_)-_B_<sub>2</sub>(2_n_):

\(B_1(2n)-B_2(2n)=\frac{1}{4(2n)(2n-1)}\sum_{j\neq kj,k\in\{1,\dots,2n\}}\mathbb{E}(\Delta_{j,k})^2\)<br>
\(=\frac{2}{4(2n)(2n-1)}\sum_{j\neq kj\in\{1,\dots,n\},k\in\{1,\dots,2n\}}\mathbb{E}(\Delta_{j,k})^2\text{(by symmetry)}\)<br>
\(\le\frac{2}{n(2n-1)}\mathbb{E}\left(\sum_{j\neq kj\in\{1,\dots,n\}}\mathbb{1}_{C_{j,k}^c}\right)+\frac{2}{n(2n-1)}\sum_{j\neq kj\in\{1,\dots,n\}}\left(\mathbb{P}(A_j^c)+\mathbb{P}(A_k^c)\right)\)<br>
\(\le\frac{2}{n(2n-1)}(2nv-n)+2exp(-tn).\)

