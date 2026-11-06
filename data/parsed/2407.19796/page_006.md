**Theorem 4.** _The problem SegE with input f_=2 _can be decided in O_(|_T_|+|_P_|) _time with O_(|_P_|) _space._

For a text _T_ of length _n_ and a pattern _P_ of length _m_, we define three arrays of size _n_ as follows:

\(lpf[i]=max\{l|P[1..l]=T[i-l+1..i]\},\)<br>
\(lsf[i]=max\{l|P[m-l+1..m]=T[i..i+l-1]\},\)<br>
\(llpf[i]=max\{lpf[j]|j\le i\},\text{for each}1\le i\le n.\)

The value _lpf_\[_i_\] (resp. _lsf_\[_i_\]) represents the length of the longest prefix (resp. suffix) of _P_, whose occurrence ends (resp. begins) at position _i_ in _T_.  1 shows an example.

We can easily verify the next lemma.

**Lemma 1.** _The following three conditions are equivalent._

(_1)_ \(P\in SubSeq^{\le 2}(T)\).<tbc>

_(2)_ \(lpf[i]+lsf[j]\ge|P|\) _for some_ \(1\le i<j\le n\).<tbc>

_(3)_ \(llpf[i]+lsf[i+1]\ge|P|\) _for some_ \(1\le i<n\).

We now show a sketch of the proof of Theorem 4. At first, we remark that by using the Knuth- Morris-Pratt (KMP) automaton \[11\] for _P_, we can compute all values of _lpf_ from left to right in _O(n_) time with _O(m_) space. Symmetrically, _lsf_ can be computed from right to left, by KMP automaton for the reverse of _P_. Moreover, _llpf_ is easily obtained from _lpf_.

After constructing these two KMP automata, our algorithm consists of the following two phases. The first phase computes both _lpf_ and _llpf_ from left to right. In the second phase, as soon as computing _lsf_ at each position _i_ from right to left, we check the condition (3) in Lemma 1. If the condition is satisfied, report it and terminate immediately. Otherwise, at the end, we conclude that \(P\unknown\in SubSeq^{\le 2}(T)\). The total running time is _O(n+m_). However, the space requirement looks like _O(n_) due to the three arrays. We reduce it to _O(m_) as follows. In the second phase, the array _lsf_ actually does not need to be memorize, because each value is used only once to check the condition. In the first phase, _lpf_ is just used to compute _llpf_, so that we only need _llpf_ for the second phase. Moreover, remark that the values in _llpf_ are non-decreasing and range from 0 to _m_. Thus, we memorize only pairs of the value _llpf_\[_i_\] and the position _i_ at which _llpf_\[_i_-1\]_\<llpf_\[_i_\] holds. (See  1, where these values are in bold.) It fits in _O(m_) space.

## 5 Fast Algorithm for SegLCS

In this section, we present an efficient algorithm for SegLCS when the length of the solution is sufficiently long. Our solution works for any non-fixed _f_ given as input unlike the problem discussed in \[14\]. We show the following theorem in this section:

\begin{tabular}{ccccccccccccccccccccc}
_i_ & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 & 21 \\
_T_ & b & a & a & c & a & b & a & b & b & a & b & c & a & a & c & a & b & c & b & a \\
_lpf_ & 0 & 1 & 1 & 0 & 1 & 2 & 1 & 2 & 3 & 4 & 5 & 0 & 1 & 1 & 0 & 1 & 1 & 2 & 0 & 0 & 1 \\
_llpf_ & 0 & **1** & 1 & 1 & 1 & **2** & 2 & 2 & **3** & **4** & **5** & 5 & 5 & 5 & 5 & 5 & 5 & 5 & 5 & 5 & 5 \\
_lsf_ & 0 & 1 & 3 & 2 & 1 & 0 & 1 & 0 & 0 & 1 & 0 & 2 & 1 & 3 & 2 & 1 & 1 & 0 & 0 & 0 & 1 \\
\end{tabular}

1: The three arrays _lpf_, _lsf_, and _llpf_ for _T_=`baacabbabcaaabcba` and _P_=`abbabaca`. In _llpf_, the **bold type** emphasizes the values that are greater than their left neighbors.

