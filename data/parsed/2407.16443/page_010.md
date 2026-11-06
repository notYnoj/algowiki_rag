<tbc>dyadic \(\phi=(\phi_1,\dots,\phi_m)\) is ordered in non decreasing fashion, then (30) becomes<tbc>

\(\mathbb{E}[C]\le H(\phi)+1-2\phi_1-\phi_m,\)

<tbc>that is better than the bound (20). On the other hand, if a dyadic \(\phi=(\phi_1,\dots,\phi_m)\) is ordered according to the "saw- tooth" order, that is, is such that<tbc>

\(\phi_1<\phi_2>\phi_3<\phi_4>\dots>\phi_{m-1}<\phi_m,\)

<tbc>with _m_ even, then (30) becomes

\(\mathbb{E}[C]\le H(\phi)+2\phi_2+2\phi_4\dots+2\phi_{m-2}-\phi_1.\) (33)

One can easily see that there are dyadic probability distributions \(\phi=(\phi_1,\dots,\phi_m)\) for which (20) is better than (33).

**Remark 2.** It might be worthwhile to point out a way to (possibly) improve the upper bound (22) of Theorem 3. For simplicity, let us assume that all probabilities \(\phi_i\) have distinct values (but the reasoning holds in general).

The idea is the following. Let us consider the lengths defined in (25). After the pruning phase described in Theorem 3 we have that between \(\phi_i\) and \(\phi_{i+1}\) it is the smaller probability to be bumped up, in the worst case. Therefore, let _S_<sub>1</sub> be the set of all indexes \(i\in\{2,\dots,m-1\}\) for which holds that \(\phi_i=min(\phi_{i-1},\phi_i)\) _and_ \(\phi_i=min(\phi_i,\phi_{i+1})\), i.e., the set of the symbols that in the worst case are bumped up at least two times. Similarly, let _S_<sub>2</sub> be the set of all indexes \(i\in\{2,\dots,m-1\}\) for which holds that \(\phi_i=min(\phi_{i-1},\phi_i)\) or \(\phi_i=min(\phi_i,\phi_{i+1})\) (but not both), i.e., the set of all symbols that in the worst case are bumped up at least one time (except the first and last symbol). Whereas, for the first and last symbol, let \(S_3\subseteq\{1,m\}\) be a set such that \(1\in S_3\) if \(min(\phi_1,\phi_2)=\phi_1\), and similarly \(m\in S_3\) if \(min(\phi_{m-1},\phi_m)=\phi_m\). Finally, let _S_<sub>4</sub> be the set of the remaining indexes (expect the first and the last one) that in the worst case are not bumped up, i.e. \(S_4=\{2,\dots,m-1\}\backslash(S_1\cup S_2)\). Consequently, we can upper bound the average length of the obtained alphabetic code in the following way:

\(\mathbb{E}[C]\le\sum_{i=2}^{m-1}\phi_i(\lceil-log_2\phi_i\rceil+1)+\phi_1(\lceil-log_2\phi_1\rceil)\)<br>
\(+\phi_m(\lceil-log_2\phi_m\rceil)-2\sum_{i\in S_1}\phi_i-\sum_{i\in S_2}\phi_i-\sum_{i\in S_3}\phi_i\)<br>
\(=\sum_{i\in S_4}\phi_i(\lceil-log_2\phi_i\rceil+1)\)<br>
\(+\sum_{i\in S_1\cup S_2\cup\{1,m\}}\phi_i(\lceil-log_2\phi_i\rceil)-\sum_{i\in S_1}\phi_i-\sum_{i\in S_3}\phi_i\) (34)

\(<\sum_{i\in S_4}\phi_i(-log_2\phi_i+2)+\sum_{i\in S_1\cup S_2\cup\{1,m\}}\phi_i(\lceil-log_2\phi_i\rceil)\)<br>
\(-\sum_{i\in S_1}\phi_i-\sum_{i\in S_3}\phi_i\) (since \(\lceil x\rceil<x+1\))<br>
\(=\sum_{i\in S_4}\phi_i(-log_2\phi_i+2)+\sum_{i\in S_1\cup S_2\cup\{1,m\}}\phi_i(\lceil-log_2\phi_i\rceil)\)

\(-\sum_{i\in S_1}\phi_i-\sum_{i\in S_3}\phi_i-\sum_{i\in S_1\cup S_2\cup\{1,m\}}\phi_i(-log_2\phi_i+2)\)<br>
\(+\sum_{i\in S_1\cup S_2\cup\{1,m\}}\phi_i(-log_2\phi_i+2)\)<br>
\(=\sum_{i=1}^m\phi_i(-log_2\phi_i+2)\)<br>
\(-\sum_{i\in S_1\cup S_2\cup\{1,m\}}\phi_i(2-log_2\phi_i-\lceil-log_2\phi_i\rceil)\)<br>
\(-\sum_{i\in S_1}\phi_i-\sum_{i\in S_3}\phi_i\)<br>
\(=H(\phi)+2-\sum_{i\in S_1\cup S_2\cup\{1,m\}}\phi_i(2-log_2\phi_i-\lceil-log_2\phi_i\rceil)\)<br>
\(-\sum_{i\in S_1}\phi_i-\sum_{i\in S_3}\phi_i\) (35)<br>
\(<H(\phi)+2-\phi_1(2-log_2\phi_1-\lceil-log_2\phi_1\rceil)\)<br>
\(-\phi_m(2-log_2\phi_m-\lceil-log_2\phi_m\rceil)-\sum_{i\in S_1\cup S_2}\phi_i-\sum_{i\in S_1\cup S_3}\phi_i\)<br>
\(\text{(since}2-log_2\phi_i-\lceil-log_2\phi_i\rceil>1\))<br>
\(=H(\phi)+2-\phi_1(2-log_2\phi_1-\lceil-log_2\phi_1\rceil)\)<br>
\(-\phi_m(2-log_2\phi_m-\lceil-log_2\phi_m\rceil)-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1})\)<br>
\(\text{(since}\sum_{i\in S_1\cup S_2}\phi_i+\sum_{i\in S_1\cup S_3}\phi_i=\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1})).\)

Therefore, (35) and (34) _cannot be worse_ than the upper bound (22) of Theorem 3. We notice that the right-hand side of (34) and (35) depends on the content of the sets _S_<sub>1</sub>_,S_<sub>2</sub>, _S_<sub>3</sub> and _S_<sub>4</sub>. Working out an explicit estimate of the sums appearing on the right-hand side of (34) and (35) would provide further improvements to (22). However, so doing seems challenging. We leave it as an open problem for future investigations.

Theorem 3 can be explicitly improved (under a slightly stronger hypothesis), as shown in the following Corollary.

**Corollary 4.2.** _For any probability distribution_ \(\phi=(\phi_1,\dots,\phi_m)\) _on the symbols_ \(s_1\prec\cdots\prec s_m\)_, with_ \(\phi_1,\phi_2,\phi_{m-1},\phi_m>0\)_, we can construct in linear time an alphabetic code C with_

\(\mathbb{E}[C]\le H(\phi)+2-\phi_1(2-log_2\phi_1-\lceil-log_2\phi_1\rceil)\)<br>
\(-\phi_m(2-log_2\phi_m-\lceil-log_2\phi_m\rceil)\)<br>
\(-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1})\)<br>
\(-\phi_1max(0,\lceil-log_2\phi_1\rceil-\lceil-log_2\phi_2\rceil-2)\)<br>
\(-\phi_mmax(0,\lceil-log_2\phi_m\rceil-\lceil-log_2\phi_{m-1}\rceil-2).\)

_Proof._ Assume first that \(\phi\) is non dyadic. We consider the same code _C_ (equivalently, tree) constructed in Theorem 3, and we take advantage of the knowledge of the lengths of the codewords of the first two symbols and of the last two symbols. In fact, such knowledge in these two particular cases allows us to state more precisely how many levels we bump up the first and last symbol during the construction of the code _C_.

