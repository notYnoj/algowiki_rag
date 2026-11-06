**Algorithm 3** EnumerateUniqueSubsetSums (with suppression-on-overwrite)

**Require:** Set _S_={_a_<sub>1</sub>_,...,a<sub>n</sub>_} (indices 1.._n_)

**Ensure:** `Memo` maps each numeric sum to its canonical (lex-min) bitmask

1: \(\mathtt{Memo}\leftarrow\{0\mapsto\mathtt{empty\_bitmask}\}\triangleright\) initial canonical rep for sum 0

2: \(\mathtt{Frontier}\leftarrow\{\mathtt{State}(0,\mathtt{empty\_bitmask},\mathtt{doNotExtend}=\mathtt{false})\}\)

3: \(\mathtt{Rep}\leftarrow\{0\mapsto\) the element of `Frontier`\(\}\triangleright\) `Rep` tracks the _current_ representative state per sum

4: **for** _k_=1 **to** _n_ **do** \(\triangleright\) BFS by columns (subset size); each canonical state expands at most once

5: \(\mathtt{NextFrontier}\leftarrow\emptyset\)

6: **for all** \(\mathtt{state}\in\mathtt{Frontier}\) **do**

7: **if** `state.doNotExtend** **then continue** \(\triangleright\) Inv. 1: suppressed reps never expand

8: **for** _i_=1 **to** _n_ **do**

9: **if** bit _i_ **is not set in** `state.mask` **then**

10: \(\mathtt{new\_sum}\leftarrow\mathtt{state}.\mathtt{sum}+a_i\)

11: \(\mathtt{new\_mask}\leftarrow\mathtt{SetBit}(\mathtt{state}.\mathtt{mask},i)\)

12: **if** \(\mathtt{new\_sum}\notin\mathtt{Memo}\) **then** \(\triangleright\) first time we see this numeric sum: install canonical rep and schedule it

13: \(\mathtt{Memo}[\mathtt{new\_sum}]\leftarrow\mathtt{new\_mask}\)

14: \(\mathtt{new\_state}\leftarrow\mathtt{State}(\mathtt{new\_sum},\mathtt{new\_mask},\mathtt{false})\)

15: \(\mathtt{Rep}[\mathtt{new\_sum}]\leftarrow\mathtt{new\_state}\)

16: \(\mathtt{NextFrontier}\leftarrow\mathtt{NextFrontier}\cup\{\mathtt{new\_state}\}\)

17: **else if** IsLexicographicallySmaller(`new\_mask`, `Memo\[new\_sum\]`) **then** \(\triangleright\) lex-smaller: overwrite the rep and suppress the displaced one (Inv. 1)

18: **if** \(\mathtt{Rep}[\mathtt{new\_sum}]\neq\mathtt{nil}\) **then**

19: \(\mathtt{Rep}[\mathtt{new\_sum}].\mathtt{doNotExtend}\leftarrow\mathtt{true}\triangleright\) suppress old representative from any future expansion

20: _/\* optional micro-optimization: if scheduled, unschedule it in this column_

_\*/_

21: remove `Rep\[new\_sum\]` from `NextFrontier` if present

22: \(\mathtt{Memo}[\mathtt{new\_sum}]\leftarrow\mathtt{new\_mask}\triangleright\) install the new canonical representative

23: \(\mathtt{new\_state}\leftarrow\mathtt{State}(\mathtt{new\_sum},\mathtt{new\_mask},\mathtt{false})\)

24: \(\mathtt{Rep}[\mathtt{new\_sum}]\leftarrow\mathtt{new\_state}\triangleright\) `Rep` now points at the (unique) expandable canonical state

25: \(\mathtt{NextFrontier}\leftarrow\mathtt{NextFrontier}\cup\{\mathtt{new\_state}\}\)

26: **else** \(\triangleright\) non-canonical duplicate: no scheduling; current rep remains unique expandable state

27: \(\mathtt{Frontier}\leftarrow\mathtt{NextFrontier}\triangleright\) advance one column; each canonical sum’s representative is expanded at most once

28: **if** \(\mathtt{Frontier}=\emptyset\) **then break**

29: **return** `Memo`

