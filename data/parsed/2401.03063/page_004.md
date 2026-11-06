Then, since \(\alpha\) and \(\beta\) are disjoint, and by independence,

\(\mathbb{E}\left(\mathrm{Var}^\alpha\mathbb{E}^\beta S\right)=\mathbb{E}\left(\mathbb{E}^{(i_1)}(\mathrm{Var}^{(i_2,\dots,i_{k+1})}\mathbb{E}^\beta S)-\mathrm{Var}^{(i_2,\dots,i_{k+1})}(\mathbb{E}^{(i_1)}\mathbb{E}^\beta S)\right)\)<br>
\(=\mathbb{E}\left(\mathrm{Var}^{(i_2,\dots,i_{k+1})}\mathbb{E}^\beta S\right)-\mathbb{E}\left(\mathrm{Var}^{(i_2,\dots,i_{k+1})}\mathbb{E}^{(i)}S\mathbb{E}^\beta S\right)\)<br>
\(=\mathbb{E}\left(S(\Delta_{(i_2,\dots,i_{k+1})}S)^\beta\right)-\mathbb{E}\left(S(\Delta_{(i_2,\dots,i_{k+1})}S)^{\beta,i}\right)\)<br>
\(=\mathbb{E}(S(\Delta_\alpha S)^\beta),\)

where in the middle equality we have used the induction hypothesis.

Recalling (1.7), we get from (1.8) that for all \(k\in\{1,\dots,n\}\),

\(J'_k=\genfrac(){pt}{2}{n}{k}D^{k-1}B_1\text{and}K'_k=\genfrac(){pt}{2}{n}{k}D^{k-1}B_{n-k+1}.\) (1.9)

It is easy to check that for any finite sequence \((a_k)_{1\le k\le n}\) and any positive integers \(k\in\{1,\dots,n\}\),

\(a_k=\sum_{j=0}^{k-1}(-1)^j\genfrac(){pt}{2}{k-1}{j}D^ja_1=\sum_{j=0}^{n-k}\genfrac(){pt}{2}{n-k}{j}D^ja_{n-j}.\) (1.10)

In particular, for all \(k\in\{1,\dots,n\}\),

\(B_k=\sum_{j=0}^{k-1}(-1)^j\frac{\genfrac(){pt}{2}{k-1}{j}}{\genfrac(){pt}{2}{n}{j+1}}J'_{j+1},\) (1.11)

\(B_k=\sum_{j=0}^{n-k}\frac{\genfrac(){pt}{2}{n-k}{j}}{\genfrac(){pt}{2}{n}{j+1}}K'_{j+1}.\) (1.12)

We can now connect the \(J'_k\)’s and \(K'_k\)’s to the variance.

**Lemma 1.4.** _For all_ \(k\in\{1,\dots,n\}\),

\(\mathrm{\textit{Var}}S-J'_1+J'_2-\cdots+(-1)^kJ'_k=(-1)^k\sum_{1\le i_1<\cdots<i_{k+1}\le n}D^kB_{i_1},\) (1.13)

\(\mathrm{\textit{Var}}S-K'_1-K'_2-\cdots-K'_k=\sum_{1\le i_1<\cdots<i_{k+1}\le n}D^kB_{i_{k+1}}.\) (1.14)

_Proof._ Let us prove (1.13) by induction on \(k\in\{1,\dots,n\}\). For the base case:

\(\mathrm{Var}S-J'_1=B_1+\cdots+B_n-nB_1=\sum_{j=2}^n(B_j-B_1)=-\sum_{j=2}^n\sum_{i=1}^{j-1}DB_i.\)

For the inductive step: assume it is true for \(k\in\{1,\dots,n-1\}\). Then,

\(\mathrm{Var}S-J'_1+J'_2-\cdots+(-1)^kJ'_k+(-1)^{k+1}J'_{k+1}=(-1)^k\left(\left(\sum_{1\le i_1<\cdots<i_{k+1}\le n}D^kB_{i_1}\right)-J'_{k+1}\right)\)<br>
\(=(-1)^k\sum_{1\le i_1<\cdots<i_{k+1}\le n}\left(D^kB_{i_1}-D^kB_1\right)\)<br>
\(=(-1)^k\sum_{1\le i_1<\cdots<i_{k+1}\le n}\sum_{1\le i_0<i_1}-D^{k+1}B_{i_0}\)<br>
\(=(-1)^{k+1}\sum_{1\le i_0<i_1<\cdots<i_{k+1}\le n}D^{k+1}B_{i_0}.\)

