**Lemma 3.11.** _Denote by_ \(\widetilde{U}:=T_{<B}(S)\) _the set that contains every vertex v with d(v)\<B and the shortest path to v visits some vertex of S. After running Algorithm 3,_ \(min\{|\widetilde{U}|,k|S|\}\le|U|\) _and_ \(|S|\le|U|\).

_Proof._ If it is a successful execution, then \(S\subseteq\widetilde{U}=U\). If it is partial, then \(k|S|\le k2^{lt}\le|U|\).

For a vertex set _U_ and two bounds _c\<d_, denote \(N^+(U)=\{(u,v):u\in U\}\) as the set of outgoing edges from _U_, and \(N_{[c,d)}^+(U)=\{(u,v):u\in U\text{and}d(u)+w_{uv}\in[c,d)\}\).

**Lemma 3.12** (Time Complexity)**.** _Suppose a large constant C upper-bounds the sum of the constants hidden in the big-O notations in all previously mentioned running times: in find-pivots, in the data structure, in relaxation, and all other operations. Algorithm 3 solves the problem in Lemma 3.1 in time_

\(C(k+2t/k)(l+1)|U|+C(t+llogk)|N_{[min_{x\in S}d(x),B)}^+(U)|.\)

_With_ \(k=\lfloor log^{1/3}(n)\rfloor\) _and_ \(t=\lfloor log^{2/3}(n)\rfloor\)_, calling the algorithm with_ \(l=\lceil(logn)/t\rceil,S=\{s\},B=\infty\) _takes O(m_log<sup>2/3</sup>_n_) _time._

_Proof._ We prove by induction on the level _l_. When _l_=0, the algorithm degenerates to the classical Dijkstra’s algorithm (Algorithm 2) and takes time _C|U_|log_k_, so the base case is proved. Suppose the time complexity is correct for level _l_-1. Now we analyze the time complexity of level _l_.

By Remark 3.5, each insertion takes amortized time _Ct_ (note that log_k\<t_); each batch prepended element takes amortized time _C_log_k_; each pulled term takes amortized constant time. But we may ignore PULL’s running time because each pulled term must have been inserted/batch prepended, and the constant of PULL can be covered by _C_ in those two operations.

By Remark 3.8, _U<sub>i</sub>_’s are disjoint and \(\sum_{i\ge 1}|U_i|\le|U|\).

Now we are ready to calculate total running time of Algorithm 3 on level _l_ by listing all the steps.

By Lemma 3.2, the \(\text{FindPivots}\) step takes time \(C\cdot min\{|\widetilde{U}|,k|S|\}k\) and \(|P|\le min\{|\widetilde{U}|/k,|S|\}\). Inserting _P_ into D takes time _C|P|t_. And by Lemma 3.11, their time is bounded by _C(k+t/k_)|_U_|.

In the _i_-th iteration, the sub-routine takes _C(k_+2_t/k)l|U<sub>i</sub>_|+_C(t_+(_l_-1)log_k_)|\(N_{[min_{x\in S_i}d(x),B_i)}^+(U_i)|\) time by the induction hypothesis. Taking the sum, by Lemma 3.10, \(N_{[min_{x\in S_i}d(x),B_i)}^+(U_i)\subseteq N_{[B_{i-1}^\prime,B_i)}^+(U_i)\). Then the sum of time spent by all the sub-routines is bounded by

\(C(k+2t/k)l|U|+\overbrace{C(t+(l-1)logk)\sum_{i\ge 1}^{\mathcal{N}_1}|N_{[B_{i-1}^\prime,B_i)}^+(U_i)|}^{\mathcal{N}_1}.\)

In the following relaxation step, for each edge (_u,v_) originated from _U<sub>i</sub>_, if \(\widehat{d}[u]+w_{uv}\in[B_i,B)\), they are directly inserted; if \(\widehat{d}[u]+w_{uv}\in[B'_i,B_i)\), they are batch prepended. Again by Remark 3.8, all _U<sub>i</sub>_’s are complete, so for the previous statements we can replace \(\widehat{d}[\cdot]\) with \(d(\cdot)\). Thus in total, it takes time

\(\overbrace{Ct\sum_{i\ge 1}^{\mathcal{N}_2}|N_{[B_i,B)}^+(U_i)|}^{\mathcal{N}_3}|+\overbrace{C(logk)\sum_{i\ge 1}^{\mathcal{N}_3}|N_{[B_i^\prime,B_i)}^+(U_i)|}^{\mathcal{N}_3}.\)

Vertices in _S<sub>i</sub>_ were also batch prepended, and this step takes time \(O(|\{x\in S_i:\widehat{d}[x]\in[B'_i,B_i)\}|logk)\). This operation takes non-zero time only if \(B'_i<B_i\), i.e., the _i_-th sub-routine is a partial execution. Thus in total this step takes time \(C\sum_{partial_i}|S_i|logk\le(C|U|logk)/k\le C|U|t/k\).

Therefore, the total running time on the level _l_ is<tbc>

\(C(k+2t/k)(l+1)|U|+\mathcal{N},\)

