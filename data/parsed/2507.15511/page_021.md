## Minimal Recursive Specification (for clarity)

**Algorithm 2** EnumerateUniqueSubsetSums-Recursive (spec; with suppression-on-overwrite)

**Require:** _S_={_a_<sub>1</sub>_,...,a<sub>n</sub>_} with fixed index order

**Ensure:** `Memo` maps each numeric sum to its canonical (lex-min) bitmask

1: \(\mathtt{Memo}\leftarrow\{0\mapsto\mathtt{empty\_bitmask}\}\); `doNotExtend`\[\(\mathtt{empty\_bitmask}\]\leftarrow\mathtt{false}\)

2: **procedure** Recurse(`mask`, `sum`, `next`) \(\triangleright\) include-only-forward indices ensure a unique generation path

3: **if doNotExtend**\[`mask`\] **then return**

4: **for** _i_=`next` to _n_ **do**

5: \(\mathtt{new\_sum}\leftarrow\mathtt{sum}+a_i;\mathtt{new\_mask}\leftarrow\mathtt{SetBit}(\mathtt{mask},i)\)

6: **if** \(\mathtt{new\_sum}\notin\mathtt{Memo}\) **then**

7: \(\mathtt{Memo}[\mathtt{new\_sum}]\leftarrow\mathtt{new\_mask};\mathtt{doNotExtend}[\mathtt{new\_mask}]\leftarrow\mathtt{false}\)

8: Recurse(`new\_mask`, `new\_sum`, _i_+1)

9: **else if** IsLexicographicallySmaller(`new\_mask`, `Memo`\[`new\_sum`\]) **then**

10: \(\mathtt{old}\leftarrow\mathtt{Memo}[\mathtt{new\_sum}];\mathtt{doNotExtend}[\mathtt{old}]\leftarrow\mathtt{true}\triangleright\) suppress-on-overwrite

11: \(\mathtt{Memo}[\mathtt{new\_sum}]\leftarrow\mathtt{new\_mask};\mathtt{doNotExtend}[\mathtt{new\_mask}]\leftarrow\mathtt{false}\)

12: Recurse(`new\_mask`, `new\_sum`, _i_+1)

13: Recurse(`empty\_bitmask`, 0, 1); **return** `Memo`

## Mechanics of Frontier/Rep/doNotExtend (matches Inv. 1)

• `Frontier` holds exactly the canonical states scheduled to be _expanded next_. We advance by columns (subset size), so each state in `Frontier` is expanded at most once per Inv. 1.<tbc>

• \(\mathtt{Rep}[\sigma]\) points to the _current representative state_ for numeric sum \(\sigma\) in this column’s scheduler. It lets us (i) find and (ii) immediately suppress a displaced representative when a lex-smaller mask appears.<tbc>

• `doNotExtend` is a per-state flag. When a representative is overwritten by a lex-smaller mask, we set `doNotExtend` on the displaced state. Even if a displaced state were still present in some queue, the flag enforces _no further expansion_, ensuring each canonical sum expands exactly once.<tbc>

• **Optional unscheduling.** We also remove the displaced state from the current `NextFrontier` if it was tentatively enqueued, which avoids a wasted dequeue in this same column. This is a micro-optimization; correctness relies only on `doNotExtend`.

## A.1 Iterative Column-wise Implementation (optimized)

.

