**Lemma 4.8** (Low-Doubling Containment for All Sets)**.** _Let_ \(\epsilon>0\)_. There is a randomized algorithm that, given a 3SUM instance_ (_A,B,C_) _along with a_ (_K,N)-container H of A, computes_

• \(O(n^\epsilon)\) _subinstances_ \((A,B'\subseteq B,C'\subseteq C)\) _so that_ \(B'\) _is contained in a translate of H and_ \(C'\) _is contained in a translate of H+H, and_

• _a set of 3SUM solutions_ \(\mathcal{T}\subseteq A\times B\times C\),

_so that each solution is either part of exactly one subinstance or part of_ T _. The algorithm runs in time_ \(\widetilde{O}(KNn^\epsilon+Kn^{2-\epsilon})\).

The proof closely follows Jin and Xu’s algorithm for low-doubling 3SUM \[JX23, Section 3.3\]. The key ingredient is the following covering-type lemma \[JX23\].

**Lemma 4.9** (\[JX23, Lemma 3.6\])**.** _There is a randomized algorithm that, given integer sets H,B,C of size at most N with_ \(|H+H|\le K|H|\)_, computes subsets_ \(B_1,\dots,B_m\subseteq B\) _and_ \(C_1,\dots,C_m\subseteq C\) _such that:_

(_i)_ _B_<sub>1</sub>_,...,B<sub>m</sub> form a partition of B,_<tbc>

(_ii)_ \(\sum_i|C_i|\le O(|C|KlogN)\),<tbc>

_(iii)_ _for all_ \(1\le i\le m\)_, there is a translate s<sub>i</sub> so that_ \(B_i\subseteq(s_i+H)\cap B\) _and_ \(C_i=(s_i+H+H)\cap C\).

_The algorithm runs in time_ \(\widetilde{O}(NKlogu)\) _whenever_ \(H,B,C\subseteq[-u,u]\).

**Proof of Lemma 4.8.** The sets _H,B,C_ satisfy the premise of Lemma 4.9, yielding sets _B_<sub>1</sub>_,...,B<sub>m</sub>_ and _C_<sub>1</sub>_,...,C<sub>m</sub>_. By Properties (i) and (iii) and the fact that \(A\subseteq H\), each 3SUM solution from (_A,B,C_) must be contained in a subinstance (_A,B<sub>i</sub>,C<sub>i</sub>_).

Consider all such subinstances, distinguishing two cases. If \(|B_i|\le|B|^{1-\epsilon}\), we simply solve the subinstance by brute-force in time \(O(|B_i||C_i|)=O(|B|^{1-\epsilon}|C_i|)\). Otherwise, we keep it as one of the designated subinstances. Property (iii) guarantees that _B<sub>i</sub>_ is contained in a translate of _H_ and _C<sub>i</sub>_ is a translate of _H+H_, as claimed. Moreover, we designate at most \(|B|^\epsilon\) subinstances in total, recalling that the sets _B_<sub>1</sub>_,...,B<sub>m</sub>_ form a partition of _B_ by Property (i). This completes the description of the algorithm. The correctness is immediate.

We focus on the running time. The initial call to Lemma 4.9 takes time \(\widetilde{O}(NKlogu)\) where _N_ is the maximum size of _H,B,C_. Solving the subinstance (_A,B<sub>i</sub>,C<sub>i</sub>_) takes time \(\widetilde{O}(|B|^{1-\epsilon}|C_i|)\) by brute-force, or linear time to copy the instance to the set of reported instances. Therefore, the total time across all subinstances is<tbc>

\(O\left(\sum_{i=1}^m|B|^{1-\epsilon}|C_i|+n^{1+\epsilon}\right)=\widetilde{O}(|B|^{1-\epsilon}\cdot K|C|+n^{1+\epsilon})=\widetilde{O}(Kn^{2-\epsilon}+n^{1+\epsilon}),\)

<tbc>by Property (ii). Hence, the total time of the algorithm is

\(\widetilde{O}(NK+Kn^{2-\epsilon}+n^{1+\epsilon})=\widetilde{O}(KNn^\epsilon+Kn^{2-\epsilon})\)

as claimed.

Finally, the proof of Lemma 4.3 is now a simple combination of Lemmas 4.5 and 4.8.

