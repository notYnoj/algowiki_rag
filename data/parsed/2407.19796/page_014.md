## A Algorithm for IndSegLCS

For a non-empty finite set _X_ of strings, define mxl(_X_) to be the length of a longest element of _X_. If _X_ is empty, let \(\mathrm{mxl}(X)=-\infty\).

In this appendix, we consider the following alternative generalization of the LCS problem.

**Problem 6** (IndSegLCS)**.** Given two strings _T_<sub>1</sub> and _T_<sub>2</sub> and two positive integers _f_<sub>1</sub> and _f_<sub>2</sub>, compute \(\mathrm{mxl}(SubSeq^{\le f_1}(T_1)\cap SubSeq^{\le f_2}(T_2))\).

This problem IndSegLCS is different from SegLCS, even when _f_<sub>1</sub>=_f_<sub>2</sub>. Consider _T_<sub>1</sub>=`abcxdexf` and _T_<sub>2</sub>=`abycdef`. The longest 2-SegLCSs of _T_<sub>1</sub> and _T_<sub>2</sub> are `abde`, which is witnessed by the 2- segmentation (`ab,de`). On the other hand, in IndSegLCS, embeddings to _T_<sub>1</sub> and _T_<sub>2</sub> are independent. The string `abcde` has two 2-segmentations (`abc,d`) and and (`ab,cd`), which are embedded to _T_<sub>1</sub> and _T_<sub>2</sub>, respectively. One may consider a more general case where \(f_1\neq f_2\). For example, \(\mathtt{abcdef}\in SubSeq^{\le 3}(T_1)\cap SubSeq^{\le 2}(T_2)\) is considered in IndSegLCS.

This section shows the following theorem.

**Theorem 6.** _The problem IndSegLCS can be solved in O(g_<sub>1</sub>_g_<sub>2</sub>_n_<sub>1</sub>_n_<sub>2</sub>) _time for input T_<sub>1</sub>_,T_<sub>2</sub>_,f_<sub>1</sub>_,f_<sub>2</sub>_, where n_<sub>1</sub>=|_T_<sub>1</sub>|, _n_<sub>2</sub>=|_T_<sub>2</sub>|, \(g_1=\mathrm{min}\{f_1,\mathrm{max}\{\lceil|T_1|/2\rceil-f_1,1\}\}\)_, and g_<sub>2</sub>=min{_f_<sub>2</sub>,max{\(\lceil|T_2|/2\rceil-f_2,1\}\}\).

Particularly when \(f_1=\lceil n_1/2\rceil\) and \(f_2=\lceil n_2/2\rceil\), the IndSegLCS problem is no different than the standard LCS problem and the time complexity of our algorithm becomes _O(n_<sub>1</sub>_n_<sub>2</sub>).

The basic idea for small segmentation numbers is quite straightforward. We maintain four four-dimensional dynamic programming tables, among which _L_<sub>BB</sub> records the values \(\mathrm{mxl}(SubSeq^{\le h_1}(T_1[1..i_1])\cap SubSeq^{\le h_2}(T_2[1..i_2]))\) for \(0\le i_a\le n_a\) and \(0\le h_a\le f_a\) with _a_=1,2. By definition, this gives the answer when (_i_<sub>1</sub>_,i_<sub>2</sub>_,h_<sub>1</sub>_,h_<sub>2</sub>)=(_n_<sub>1</sub>_,n_<sub>2</sub>_,f_<sub>1</sub>_,f_<sub>2</sub>). When extending a current LCS candidate, we should pay attention on whether we start a new segment or extend the last segment. Define<tbc>

\(SufSeq^{\le f}(T)=\{u_1\cdots u_f|T=v_0u_1v_1\dots v_{f-1}u_f\text{for some}v_0,\dots,v_{f-1}\in\Sigma^*\},\)

<tbc>which is a subset of \(SubSeq^{\le f}(T)\), with the restriction that the last segment must be a suffix of _T_. Obviously, \(SubSeq^{\le f-1}(T)\subseteq SufSeq^{\le f}(T)\subseteq SubSeq^{\le f}(T)\). By maintaining the following four tables, one can solve IndSegLCS.

\(L_\mathrm{BB}[i_1,i_2,h_1,h_2]=\mathrm{mxl}(SubSeq^{\le h_1}(T_1[1..i_1])\cap SubSeq^{\le h_2}(T_2[1..i_2])),\)<br>
\(L_\mathrm{BF}[i_1,i_2,h_1,h_2]=\mathrm{mxl}(SubSeq^{\le h_1}(T_1[1..i_1])\cap SufSeq^{\le h_2}(T_2[1..i_2])),\)<br>
\(L_\mathrm{FB}[i_1,i_2,h_1,h_2]=\mathrm{mxl}(SufSeq^{\le h_1}(T_1[1..i_1])\cap SubSeq^{\le h_2}(T_2[1..i_2])),\)<br>
\(L_\mathrm{FF}[i_1,i_2,h_1,h_2]=\mathrm{mxl}(SufSeq^{\le h_1}(T_1[1..i_1])\cap SufSeq^{\le h_2}(T_2[1..i_2])).\)

If any of _i_<sub>1</sub>_,i_<sub>2</sub>_,h_<sub>1</sub>_,h_<sub>2</sub> is zero, then _L_<sub>∗</sub>\[_i_<sub>1</sub>_,i_<sub>2</sub>_,h_<sub>1</sub>_,h_<sub>2</sub>\]=0 holds for all \(*\in\{\mathrm{BB},\mathrm{BF},\mathrm{FB},\mathrm{FF}\}\). One can easily compute _L_<sub>∗</sub>\[_i_<sub>1</sub>_,i_<sub>2</sub>_,h_<sub>1</sub>_,h_<sub>2</sub>\] inductively for _i_<sub>1</sub>_,i_<sub>2</sub>_,h_<sub>1</sub>_,h_<sub>2</sub>_\>_0.

Now, we present an improvement on the naive algorithm particularly for the case where the segmentation number _f<sub>a</sub>_ is close to _n<sub>a</sub>/_2 (but not larger than \(\lceil n_a/2\rceil\)). Consider a factorization (_v_<sub>0</sub>_,u_<sub>1</sub>_,v_<sub>1</sub>_,...,u<sub>h</sub>,v<sub>h</sub>_) of \(T=v_0u_1v_1\cdots u_hv_h\) that witnesses \(u_1\cdots u_h\in SubSeq^{\le f}(T)\) with \(h\le f\). To make the segmentation number _h_ small, some of the factors _u<sub>i</sub>_ and _v<sub>i</sub>_ must be long enough. More formally, \(u_1\cdots u_h\in SubSeq^{\le f}(T)\) if and only if \(\mathcal{S}(v_0,u_1,\dots,u_h,v_h)\ge|T|-2f\) for the _score_ S of the factorization defined by<tbc>

\(\mathcal{S}(w_0,\dots,w_m)=|w_0|+\sum_{j=1}^m(|w_i|-1).\)

