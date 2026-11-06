<tbc>_Lemma_ 5 (Mixed Case Match)_. A subset_ \(A\subseteq\ell_0\) _and the complement of a subset_ \(B\subseteq\ell_1\) _form a solution if and only if_

\(\sigma(A)+\sigma(\ell_1\backslash B)=t.\)

_Proof sketch._ All statements follow from elementary algebra on disjoint subsets and set complements (e.g., \(\sigma(\ell_i\backslash A)=\sigma(\ell_i)-\sigma(A)\) and \(\ell_0\) is disjoint from \(\ell_1\)). These identities justify the conditional checks performed by the Check routine in the main solver. Since the enumerator generates all elements of \(\Sigma(\ell_i)\) correctly (§A), all valid witnesses are discoverable by the algorithm.

Full derivations appear in §6.1-6.3 of \[Sal25\].

**Real-Time Solution Check Procedures (invoked during enumeration).**

**Algorithm 10** Check(_q_) -- standard (no aliasing)

**Require:** _q_ -- a _k_-permutation state

**Ensure:** Verifies whether _q_ completes a valid solution to the target

1: Let _t_ be the target

2: \(b\leftarrow q.\text{\texttt{split}},b'\leftarrow 1-b\)

3: \(\mathrm{Sum}_b\leftarrow\sum_{x\in\ell_b}x;\mathrm{Sum}_{b^\prime}\leftarrow\sum_{x\in\ell_{b^\prime}} x\)

4: \(s_\mathrm{real}\leftarrow q.\text{\texttt{sum}}\triangleright\) true sum on split _b_

5: \(\mathtt{Memo}'\leftarrow\mathtt{Memo}_{b^\prime}\)

_Intra-half direct/self-complement:_

6: **if** _s_<sub>real</sub>=_t_ **or** Sum_<sub>b</sub>-s_<sub>real</sub>=_t_ **then**

7: **Output:** direct solution found

8: **return**

_Cross-half patterns:_

9: **(D)** check \(t-s_\mathrm{real}\in\mathtt{Memo}'\triangleright\sigma(A)+\sigma(B)=t\)

10: **if** \(t-s_\mathrm{real}\in\mathtt{Memo}'\) **then**

11: **Output:** solution across splits; **return**

12: **(RC)** check \(\mathrm{Sum}_{b^\prime}-(t-s_\mathrm{real})\in\mathtt{Memo}'\triangleright\sigma(A)+\sigma(\ell_{b^\prime}\backslash B)=t\)

13: **if** \(\mathrm{Sum}_{b^\prime}-(t-s_\mathrm{real})\in\mathtt{Memo}'\) **then**

14: **Output:** mixed (right-complement); **return**

15: \(s_\mathrm{comp}\leftarrow\mathrm{Sum}_b-s_\mathrm{real}\triangleright\) left complement

16: **(LC)** check \(t-s_\mathrm{comp}\in\mathtt{Memo}'\triangleright\sigma(\ell_b\backslash A)+\sigma(B)=t\)

17: **if** \(t-s_\mathrm{comp}\in\mathtt{Memo}'\) **then**

18: **Output:** mixed (left-complement); **return**

19: **(DC)** check \(\mathrm{Sum}_{b^\prime}-(t-s_\mathrm{comp})\in\mathtt{Memo}'\triangleright\sigma(\ell_b\backslash A)+\sigma(\ell_{b^\prime}\backslash B)=t\)

20: **if** \(\mathrm{Sum}_{b^\prime}-(t-s_\mathrm{comp})\in\mathtt{Memo}'\) **then**

21: **Output:** double complement; **return**

