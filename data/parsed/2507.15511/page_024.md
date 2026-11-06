## B.2 Core Pseudocode (Modular)

We write `State(sum, mask, split, doNotExtend)` for a per-half enumeration state. Lexicographic comparisons of bitmasks use Algorithm 4 (Appendix A). The solution checks are given in Algorithms 10 and 11 (Appendix C).

**Algorithm 6** DoubleMIM-IC-SubsetSum (interleaved, alias-aware)

**Require:** Multiset _S_; target _t_; flag `AliasingEnabled`;<br>
alias pairs \((x_0^{(0)},x_1^{(0)})\) at indices \((i_0^{(0)},i_1^{(0)})\) on \(\ell_0\), and \((x_0^{(1)},x_1^{(1)})\) at \((i_0^{(1)},i_1^{(1)})\) on \(\ell_1\)

**Ensure:** Returns a witness if \(t\in\Sigma(S)\); else reports failure

1: Split _S_ into \(\ell_0,\ell_1\) (e.g., alternating indices)

2: Initialize per-half tables: \(\mathtt{Memo}_b\leftarrow\emptyset,\mathtt{Rep}_b\leftarrow\emptyset\) for \(b\in\{0,1\}\)

3: Initialize per-half frontiers with the empty state:

\(\mathtt{Frontier}\leftarrow\{\mathtt{State}(0,\mathbf{0},0,\mathtt{false}),\mathtt{State}(0,\mathbf{0},1,\mathtt{false})\}\)

4: Insert the empty key on both halves:

`InsertOrImprove`(0,**0**,0); `InsertOrImprove`(0,**0**,1)

5: **for** _r_=0 **to** \(\lfloor n/2\rfloor\) **do** \(\triangleright\) interleave by "column"/Hamming weight

6: \(\mathtt{NextFrontier}\leftarrow\emptyset\)

7: **for all** \(p\in\mathtt{Frontier}\) **do**

8: **if** _p_.doNotExtend **then** continue

9: \(b\leftarrow p.\mathtt{split};L\leftarrow\ell_b;k\leftarrow|L|\)

10: **for** _i_=0 **to** _k_-1 **do**

11: **if** _p_.mask\[_i_\]=0 **then**

12: \(s'\leftarrow p.\mathtt{sum}+L[i];e'\leftarrow p.\mathtt{mask}\) with bit \(i\leftarrow 1\)

13: \(\mathtt{ProcessExtension}(b,s',e')\triangleright\) Algorithm 7

14: \(\mathtt{Frontier}\leftarrow\mathtt{NextFrontier}\)

15: **if** \(\mathtt{Frontier}=\emptyset\) **then break**

16: **return** "No solution found"

**Algorithm 7** ProcessExtension\((b,s',e')\)

**Require:** Half index \(b\in\{0,1\}\); candidate sum \(s'\) and mask \(e'\)

1: /\* Compute per-half key (aliased or not) \*/

2: \(\mathtt{key}\leftarrow\) KeyOf\((b,s',e')\triangleright\) Algorithm 8

3: \(wasNew\leftarrow\mathtt{InsertOrImprove}(\mathtt{key},e',b)\triangleright\) Algorithm 9

4: **if** _wasNew_ **then**

5: \(q\leftarrow\mathtt{State}(s',e',b,\mathtt{false})\)

6: **if** `AliasingEnabled` **and not** Expandable\((e',i_0^{(b)},i_1^{(b)})\) **then** \(\triangleright\) CNF gate

7: \(q.\mathtt{doNotExtend}\leftarrow\mathtt{true}\)

8: \(\mathtt{NextFrontier}\leftarrow\mathtt{NextFrontier}\cup\{q\}\)

9: **if** `AliasingEnabled` **then** CheckAliased(_q_) **else** Check(_q_)

