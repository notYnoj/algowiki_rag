_Proof._ Since \(\delta>0\), we have |_I|\>|N(I_)|. By Lemma 1, we can construct a blocking set \(S\subseteq I\) with \(|S|\le|N(I)|\). Since _I_ is independent,<tbc>

\(|I|+|N(I)|\le n.\)

<tbc>Together with |_I|\>|N(I_)|, this implies 2|_N(I_)|_\<n_. Hence

\(0<|S|=|N(S)|\le|N(I)|<\frac{n}{2}.\)

Thus, _S_ is a small blocking set.

## 3.2. Zero critical difference

**Theorem 1.** _Suppose that_ \(\delta=0\) _and I is a maximum-cardinality CIS. Then:_

1. _If_ \(I=\varnothing\)_, the graph contains no nonempty blocking set._<tbc>

2. _If_ 0_\<|I|\<n/_2_, then I itself is a small blocking set._<tbc>

3. _The only remaining case is_ |_I_|=_n/_2.

_Proof._ Suppose first that \(I=\varnothing\) and, for a contradiction, that there is a nonempty blocking set _S_. Then

\(d(S)=0=id_c(G),\)

so _S_ is a nonempty CIS, contradicting the choice of the empty set as a maximum-cardinality CIS.

If 0_\<|I|\<n/_2, then _d(I_)=0 gives |_I_|=|_N(I_)|, so _I_ itself is a small blocking set.

Finally, since _I_ is independent and _d(I_)=0,

\(2|I|=|I|+|N(I)|\le n.\)

Thus, \(|I|\le n/2\). After excluding the empty set and the case |_I|\<n/_2, only |_I_|=_n/_2 remains.

The maximum-cardinality requirement is used here primarily to justify the empty-set branch. If an arbitrary CIS is computed instead, the subroutine may return the empty set even when a nonempty blocking set exists.

