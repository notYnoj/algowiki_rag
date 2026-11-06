In the context of knapsack algorithms (e.g., \[KP04, AT19, PRW21\]), SMAWK algorithm is used to find the (max,+)-convolution \(c[i]:=\mathrm{max}_{0\le j\le i}\{a[j]+b[i-j]\}\) between an array _a_\[0_..n_\] and a _concave_ array _b_\[0_..m_\] (that is, \(b[i]-b[i-1]\ge b[i+1]-b[i]\)). To do this, define matrix \(A[i,j]=\left\{\begin{array}{ c c }
a[j]+b[i-j] & j\le i \\
-\infty & j>i
\end{array}\right.\). Note that _A_ is a reverse falling staircase matrix. One can verify that _A_ is convex Monge: for \(i<i',j<j'\) such that all four terms in Eq. (21) are finite, we have

\(A[i,j]+A[i',j']-A[i,j']-A[i',j]\)<br>
\(=b[j-i]+b[j'-i']-b[j'-i]-b[j-i']\)<br>
\(\ge 0\)

by the concavity of _b_. So SMAWK algorithm can compute all row maxima of _A_, which correspond to the answer of the (max,+)-convolution.

## B Omitted proofs

### B.1 Proof of Lemma 2.1

**Lemma 2.1** (Break ties)**.** _Given a 0-1 Knapsack instance I, in O(n_) _time we can deterministically reduce it to another 0-1 Knapsack instance_ \(I'\) _with n,w_<sub>max</sub> _and t unchanged, and_ \(p'_\mathrm{max}\le\mathrm{poly}(p_\mathrm{max},w_\mathrm{max},n)\)_, such that the items in_ \(I'\) _have_ distinct efficiencies _and distinct profits._

_Proof._ Suppose instance _I_ has capacity _t_ and _n_ items (_w_<sub>1</sub>_,p_<sub>1</sub>)_,...,(w<sub>n</sub>,p<sub>n</sub>_). Define instance \(I'\) with capacity _t_ and items \((w_1,p'_1),\dots,(w_n,p'_n)\) with modified profits<tbc>

\(p'_i:=(p_i\cdot M+i)\cdot w_\mathrm{max}+1,\)

<tbc>where \(M:=1+n+\sum_{i=1}^ni\). Then, for any item set \(S\subseteq[n]\), we have<tbc>

\(0\le\sum_{i\in S}p'_i-Mw_\mathrm{max}\sum_{i\in S}p_i=|S|+\sum_{i\in S}iw_\mathrm{max}<Mw_\mathrm{max},\)

<tbc>and hence

\(\sum_{i\in S}p_i=\left\lfloor\frac{\sum_{i\in S}p'_i}{Mw_\mathrm{max}}\right\rfloor,\)

so any optimal solution for \(I'\) must also be an optimal solution for _I_.

For any \(i\neq j\), note that \(p'_i\mathrm{mod}(Mw_\mathrm{max})=iw_\mathrm{max}+1\neq jw_\mathrm{max}+1=p'_j\mathrm{mod}(Mw_\mathrm{max})\), so \(p'_i\neq p'_j\). If \(p'_i/w_i=p'_j/w_j\), then from \(p'_iw_j\equiv w_j(\mathrm{mod}w_\mathrm{max})\) and \(p'_jw_i\equiv w_i(\mathrm{mod}w_\mathrm{max})\) we have _w<sub>j</sub>=w<sub>i</sub>_, which then contradicts \(p'_i\neq p'_j\). So \(p'_i/w_i\neq p'_j/w_j\).

### B.2 Proof of Lemma 3.2

**Lemma 3.2** (Extension of \[CLMZ24, Lemma 4.1\])**.** _The set_ W _of input item weights can be partitioned in O(n+w_<sub>max</sub>log_w_<sub>max</sub>) _time into_ \(\mathcal{W}=\mathcal{W}_1\unknown\mathcal{W}_2\unknown\cdots\unknown\mathcal{W}_s\)_, where_ \(s<\mathrm{log}_2(\sqrt{w_\mathrm{max}})\)_, with the following property:_

_Denote_ \(\mathcal{W}_{\le j}=\mathcal{W}_1\cup\cdots\cup\mathcal{W}_j\) _and_ \(\mathcal{W}_{>j}=\mathcal{W}\backslash\mathcal{W}_{\le j}\)_. For every optimal exchange solution_ (_A,B_) _and every_ \(1\le j\le s\),

