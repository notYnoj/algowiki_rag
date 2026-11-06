The proof of (1.14) is very similar and so it is omitted. The following proposition recovers and extends some of the results obtained in \[4\].

**Proposition 1.5.**<tbc>

\(\text{\textit{Var}}S=J'_1-J'_2+\cdots+(-1)^{n-1}J'_n=K'_1+K'_2+\cdots+K'_n,\) (1.15)

<tbc>_and for all_ \(k\in\{1,\dots,n-1\}\),

\(K'_{k+1}\le(-1)^k\left(\text{\textit{Var}}S-J'_1+J'_2-\cdots+(-1)^kJ'_k\right)\le J'_{k+1},\)<br>
\(K'_{k+1}\le\text{\textit{Var}}S-K'_1-K'_2-\cdots-K'_k\le J'_{k+1}.\)<br>
\(\text{\textit{Var}}S=J'_1-J'_2+\cdots+(-1)^{k-1}J'_k+(-1)^k\sum_{j=k+1}^n\genfrac(){pt}{2}{j-1}{k}K'_j.\) (1.16)

\(\text{\textit{Var}}S=\frac{\genfrac(){pt}{2}{k}{1}}{\genfrac(){pt}{2}{n}{1}}J'_1-\frac{\genfrac(){pt}{2}{k}{2}}{\genfrac(){pt}{2}{n}{2}}J'_2+\cdots+(-1)^{k-1}\frac{\genfrac(){pt}{2}{k}{k}}{\genfrac(){pt}{2}{n}{k}}J'_k+\frac{\genfrac(){pt}{2}{n-k}{1}}{\genfrac(){pt}{2}{n}{1}}K'_1+\frac{\genfrac(){pt}{2}{n-k}{2}}{\genfrac(){pt}{2}{n}{2}}K'_2+\cdots+\frac{\genfrac(){pt}{2}{n-k}{n-k}}{\genfrac(){pt}{2}{n}{n-k}}K'_{n-k}.\) (1.17)

_Proof._ Above, the first two equalities simply follow from the fact that the right-hand terms in Lemma 1.4 are zero when _k=n_. Then, the first two inequalities follow from Lemma 1.4 and the complete monotonicity of the _B<sub>k</sub>_’s: for \(1\le i_1\le n-k\), \(D^kB_{n-k}\le D^kB_{i_1}\le D^kB_1\). Let us turn to the identity (1.16).

Applying the inversion formula (1.10) to \((D^kB_i)_{1\le i\le n-k}\), with \(i\le n-k\), we get

\(\sum_{1\le i_1<\cdots<i_{k+1}\le n}D^kB_{i_1}=\sum_{i=1}^{n-k}\genfrac(){pt}{2}{n-i}{k}D^kB_i\)<br>
\(=\sum_{i=1}^{n-k}\sum_{j=0}^{n-k-i}\genfrac(){pt}{2}{n-i}{k}\genfrac(){pt}{2}{n-k-i}{j}D^{k+j}B_{n-k-j}\)<br>
\(=\sum_{i=1}^{n-k}\sum_{j=0}^{n-k-i}\genfrac(){pt}{2}{n-i}{k}\genfrac(){pt}{2}{n-k-i}{j}\frac{K'_{k+j+1}}{\genfrac(){pt}{2}{n}{k+j+1}}\)<br>
\(=\sum_{j=0}^{n-1}\sum_{i=1}^{n-k-j}\genfrac(){pt}{2}{n-i}{k+j}\genfrac(){pt}{2}{k+j}{k}\frac{K'_{k+j+1}}{\genfrac(){pt}{2}{n}{k+j+1}}\)<br>
\(=\sum_{j=0}^{n-1}\genfrac(){pt}{2}{k+j}{k}K'_{k+j+1},\)

where the last equality stems from the hockey-stick formula and reindexing.

To finish, let us prove (1.17) which will follow from \(\text{Var}S=B_1+\cdots+B_k+B_{k+1}+\cdots+B_n\). Indeed, the equality (1.15) remains valid for any sequence \((a_n)_{n\ge 1}\), namely, the same proof shows that<tbc>

\(a_1+\cdots+a_n=\genfrac(){pt}{2}{n}{1}D^0a_1-\genfrac(){pt}{2}{n}{2}D^1a_1+\cdots+(-1)^{n-1}\genfrac(){pt}{2}{n}{n}{n}D^{n-1}a_1.\)

<tbc>In particular,

\(B_1+\cdots+B_k=\genfrac(){pt}{2}{k}{1}D^0B_1-\genfrac(){pt}{2}{k}{2}D^1B_1+\cdots+(-1)^{k-1}\genfrac(){pt}{2}{k}{k}D^{k-1}B_1\)<br>
\(=\frac{\genfrac(){pt}{2}{k}{1}}{\genfrac(){pt}{2}{n}{1}}J'_1-\frac{\genfrac(){pt}{2}{k}{2}}{\genfrac(){pt}{2}{n}{2}}J'_2+\cdots+(-1)^{k-1}\frac{\genfrac(){pt}{2}{k}{k}}{\genfrac(){pt}{2}{n}{k}}J'_k.\)

The second part, \(B_{k+1}+\cdots+B_n\), is treated similarly.

