**Lemma 8.** _If_ I=(_G,_**w**_,k_) _is a yes-instance of_ \(MAS/MaxST(\mathbb{Q}_{\ge 1})\)_, then there exists a solution X to_ I _with S=E(T_)\\_E(X_) _such that the weight of_

\(B'=\bigcup_{s_1,s_2\in S_1\neq s_2}(\mathrm{Inv}(s_1)\cap\mathrm{Inv}(s_2))\)

_is at most_ (**w**(_A_)+_k_)<sup>2</sup>_. Additionally, if_ I _admits a solution of the form_ \(T-S+\mathrm{Inv}(S)+A'\) _for some_ \(S\subseteq E(T)\) _and_ \(A'\subseteq A\)_, then X can be required to have the same form._

_Proof._ If I does not admit a solution of the required form, let _X_ be an arbitrary solution that minimizes |_S_|. Otherwise, let _X_ be a solution of the required form with the minimum |_S_|. Since _X_ is acyclic, by Observation 2 we have that \(X\subseteq T-S+\mathrm{Inv}(S)+A\). Consequently, \(\mathbf{w}(X)\le\mathbf{w}(T)+\mathbf{p}(S)+\mathbf{w}(A)\). Assume that \(\mathbf{w}(B')>(\mathbf{w}(A)+k)^2\). We aim to derive a contradiction by constructing a solution of the form \(T-S'+\mathrm{Inv}(S')\) with \(|S'|<|S|\).

Consider a subset \(C\subseteq S\) of minimum size such that \(B'\subseteq\mathrm{Inv}(C)\). Since \(\mathbf{w}(B')>(\mathbf{w}(A)+k)^2\ge 0\), \(B'\) is not empty, and hence we have \(|C|\ge 1\). Additionally, by definition, every element of \(B'\) is inverse to at least two edges from _S_. Hence for each \(s\in S\), we have \(B'\subseteq\mathrm{Inv}(S\backslash\{s\})\). Therefore, |_C|\<|S_|. Let _I_:=_S_\\_C_. We now consider two cases.

Suppose that |_C|\<_**w**(_A_)+_k_. Since \(B'\subseteq\mathrm{Inv}(C)\), we have \(B'=\bigcup_{c\in C}(\mathrm{Inv}(c)\cap B')\) which implies that<tbc>

\(\sum_{c\in C}\mathbf{w}(\mathrm{Inv}(c)\cap B')\ge\mathbf{w}(B')>(\mathbf{w}(A)+k)^2\)

<tbc>Let \(c\in C\) be an element with the maximum value of \(\mathbf{w}(\mathrm{Inv}(c)\cap B')\). This weight is at least<tbc>

\(\frac{\sum_{c\in C}\mathbf{w}(\mathrm{Inv}(c)\cap B')}{|C|}\ge\frac{(\mathbf{w}(A)+k)^2}{\mathbf{w}(A)+k}=\mathbf{w}(A)+k\)

<tbc>Let \(S':=S\backslash\{c\}\). As shown above, \(B'\subseteq\mathrm{Inv}(S')\). Consequently, \(\mathrm{Inv}(c)\cap B'\subseteq\mathrm{Inv}(c)\cap\mathrm{Inv}(S')\). Since \(B'\) is not empty, \(|S|\ge 2\), and thus the subgraph _T-c_+Inv(_c_) is not a feasible solution of I. Because Lemma 1 guarantees its acyclicity, we have that **p**(_c)\<k_. It follows that

\(\mathbf{rp}(S',c)=\mathbf{w}(\mathrm{Inv}(c)\backslash\mathrm{Inv}(S'))-\mathbf{w}(c)\)<br>
\(=(\mathbf{w}(\mathrm{Inv}(c))-\mathbf{w}(c))-\mathbf{w}(\mathrm{Inv}(c)\cap\mathrm{Inv}(S'))\)<br>
\(\le(\mathbf{w}(\mathrm{Inv}(c))-\mathbf{w}(c))-\mathbf{w}(\mathrm{Inv}(c)\cap B')\)<br>
\(\le\mathbf{p}(c)-(\mathbf{w}(A)+k)\)<br>
\(\le-\mathbf{w}(A)\)

Then \(X':=T-S'+\mathrm{Inv}(S')\) is also a solution of I. Indeed, by Lemma 1 it is acyclic. Moreover,

\(\mathbf{w}(X')=\mathbf{w}(T)+\mathbf{p}(S')=\mathbf{w}(T)+(\mathbf{p}(S')+\mathbf{rp}(S',s))-\mathbf{rp}(S',s)\)<br>
\(=\mathbf{w}(T)+\mathbf{p}(S)-\mathbf{rp}(S',s)\)<br>
\(=(\mathbf{w}(T)+\mathbf{p}(S)+\mathbf{w}(A))-(\mathbf{rp}(S',s)+\mathbf{w}(A))\)<br>
\(\ge\mathbf{w}(X)-(-\mathbf{w}(A)+\mathbf{w}(A))\)<br>
\(=\mathbf{w}(X)\ge\mathbf{w}(T)+k\)

But this contradicts the choice of _X_ because \(|S'|<|S|\).

