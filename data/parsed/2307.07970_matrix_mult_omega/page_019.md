where \(X_i^{(\ell)}\) (\(0\le i\le 2^\ell\)) is the _i_-th part in the level-\(\ell\) partition of \(T^{(\ell)}\). We call _X<sub>I</sub>_ a _level-_\(\ell\) _variable block_ and _I_ its _level-_\(\ell\) _index sequence_. The level-\(\ell Y\) - and _Z_-variable blocks _Y<sub>J</sub>_ and _Z<sub>K</sub>_ are defined similarly for level-\(\ell\) index sequences \(J,K\in\{0,1,\dots,2^\ell\}^n\). Similarly, the level-\(\ell\) variable blocks _X<sub>I</sub>,Y<sub>J</sub>,Z<sub>K</sub>_ form a nonzero subtensor of \((T^{(\ell)})^{\otimes n}\) when \(I_t+J_t+K_t=2^\ell\) for all \(t\in[n]\). So we can write

\((T^{(\ell)})^{\otimes n}=\sum_{\hat{I},\hat{J},\hat{K}\in\{0,1,2^\ell\}^nI_t+J_t+K_t=2^\ell\forall t\in[N]}(T^{(\ell)})^{\otimes n}|_{X_I,Y_J,Z_K}.\)

For convenience, we use the notation _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ to denote the subtensor \((T^{(\ell)})^{\otimes n}|_{X_I,Y_J,Z_K}\) and we call such _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ a _level-_\(\ell\) _triple_.

In addition, note that since the level-\(\ell\) partition of \(T^{(\ell)}\) is a coarsening of the partition induced by the level- 1 partition of _T_<sup>(1)</sup>, a level-1 variable block \(X_\hat{I}\) is contained in a level-\(\ell\) variable block _X<sub>I</sub>_ if the sequence \(I'=(I'_1,\dots,I'_n)\) formed by taking \(I'_t=\sum_{i=1}^{2^{\ell-1}}\hat{I}_{(t-1)\cdot 2^{\ell-1}+i}\) satisfies \(I'_t=I_t\) for all \(t\in[n]\). Namely, if taking the sum of consecutive length-\(2^{\ell-1}\) subsequences in \(\hat{I}\) yields the sequence _I_, then \(X_\hat{I}\) is contained in _X<sub>I</sub>_. In this case, we use the notation \(\hat{I}\in I\) and \(X_\hat{I}\in X_I\).

## 3.9 Distributions and Entropy

In this paper, we only consider distributions with a finite support. Let \(\alpha\) be a distribution supported on a set _S_, we have \(\alpha(s)\ge 0\) for all \(s\in S\) and \(\sum_{s\in S}\alpha(s)=1\). The _entropy_ of \(\alpha\), denoted as \(H(\alpha)\), is defined as

\(H(\alpha):=-\sum_{s\in S\alpha(s)>0}\alpha(s)log\alpha(s),\)

where the log has base 2. We will frequently use the following well-known combinatorial fact.

**Lemma 3.3.** _Let_ \(\alpha\) _be a distribution over the set_ \[_s_\]={1_,...,s}. Let N\>_0 _be a positive integer, then we have_<tbc>

\(\genfrac(){pt}{2}{N}{\alpha(1)N,\dots,\alpha(s)N}=2^{N(H(\alpha)\pm o(1))}.\)

<tbc>For two distributions \(\alpha\) and \(\beta\) over the sets _S_ and \(S'\) respectively, we define the joint distribution \(\alpha\times\beta\) as the distribution over \(S\times S'=\{(s,s')|s\in S,s'\in S'\}\) such that<tbc>

\((\alpha\times\beta)(s,s')=\alpha(s)\cdot\beta(s').\)

<tbc>When _S_ and \(S'\) are sets of integer sequences, we will instead define \(\alpha\times\beta\) as a distribution over all integer sequences that can be obtained by concatenating one sequence in _S_ and one sequence in \(S'\), such that

\((\alpha\times\beta)(s\circ s')=\alpha(s)\cdot\beta(s'),\)

where \(s\circ s'\) denotes the concatenation of _s_ and \(s'\).

