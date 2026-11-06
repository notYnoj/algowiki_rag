## Core Procedures (per half)

**Tag and Canonicality.**

1: **function** ChiTag(_b,i_<sub>1</sub>)

2: **return** _b_\[_i_<sub>1</sub>\]

3: **function** IsCanonical(_b,i_<sub>0</sub>_,i_<sub>1</sub>)

4: **return** _b_=`canon`(_b_)

**Insert into Memo .**

1: **function** Insert(\(\tilde{\sigma}\), _b,i_<sub>1</sub>)

2: \(\chi\leftarrow\mathrm{ChiTag}(b,i_1)\)

3: **if** \(\mathtt{Memo}[\tilde{\sigma}][\chi]=\perp\) **or** \(b\prec\mathtt{Memo}[\tilde{\sigma}][\chi]\) **then**

4: \(\mathtt{Memo}[\tilde{\sigma}][\chi]\leftarrow b\)

**Expansion Predicate (aliased runs).**

1: **function** Count(_b,i_<sub>0</sub>_,i_<sub>1</sub>)

2: **return** _b_\[_i_<sub>0</sub>\]+_b_\[_i_<sub>1</sub>\]

3: **function** Expandable(_b,i_<sub>0</sub>_,i_<sub>1</sub>)

4: \(c\leftarrow\mathrm{Count}(b,i_0,i_1),\chi\leftarrow\mathrm{ChiTag}(b,i_1)\)

5: **return** \((c=0)\vee(c=2)\vee(c=1\wedge\chi=0)\)

_Hook._ When a new state is created under aliasing, set

\(\mathtt{state.doNotExtend}\leftarrow\neg\mathrm{Expandable}(\mathtt{state.mask},i_0,i_1).\)

**Aliasing Maps.**

1: **function** CorrectedSum(\(\tilde{\sigma}\), \(\chi\), _x_<sub>0</sub>, _x_<sub>1</sub>)

2: **return** \(\tilde{\sigma}+\chi\cdot(x_1-x_0)\)

3: **function** AliasedValue(\(\sigma_\mathrm{real}\), \(\chi\), _x_<sub>0</sub>, _x_<sub>1</sub>)

4: **return** \(\sigma_\mathrm{real}-\chi\cdot(x_1-x_0)\)

### Interface with CheckAliased.

In the solver (Alg. 6), replace the single-key probe by the compound key (\(\tilde{\sigma},\chi\)), computed via AliasedValue and ChiTag. Use IsCanonical/Expandable to gate expansion (CNF). Cross-half tests call the 2-lane CheckAliased routine.

## Compensatory Witness Recovery

To ensure correctness during merging, the algorithm performs a \(2\times 2\) compensatory check across \(\chi\)-tags of both halves. For each left-side aliased sum, it computes the required right-side partner under both interpretations.

### FindSolution Routine.

1: **function** FindSolution(_t_, MemoLeft, MemoRight, _x_<sub>0</sub>, _x_<sub>1</sub>, _y_<sub>0</sub>, _y_<sub>1</sub>)

2: **for all** \(\tilde{\sigma}_L\in\mathtt{MemoLeft}\) **do**

3: **for** \(\chi_L\in\{0,1\}\) **do**

4: \(b_L\leftarrow\mathtt{MemoLeft}[\tilde{\sigma}_L][\chi_L]\)

5: **if** \(b_L=\perp\) **then continue**

