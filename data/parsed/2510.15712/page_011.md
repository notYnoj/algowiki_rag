Lastly, shadow variables must not be used in vain--meaning they should be used only when they indicate a position where the inactive output is better than the active one. Why is this necessary? When _i_ is the most significant bit in which the active output is 0 but the inactive is 1 (so _i_ is where we can improve things), we can be sure that all shadow variables of the positions 1_,...,i_-1 are off, which will be important later.

\(s_i^B\rightarrow v_i^B\text{and}s_i^B\rightarrow\neg v_i^T\) (4.11) \(s_i^T\rightarrow v_i^T\text{and}s_i^T\rightarrow\neg v_i^B\) (4.12)

The order among the clauses in this group is arbitrary. All clauses so far (correctness clauses and proper use clauses) stay fulfilled along the canonical path and are never violated when only doing improving steps. If violated, we can always satisfy them by correcting the input of the inactive circuit (group 0), correcting the output of gates (group 1), or by deactivating shadow variables (group 1b).

**2. The global output register should be large, but not larger than the active output.**<br> The first three clauses are almost exactly the same as in the previous section, except that control clauses can also be fulfilled by the shadow variables of the other circuit. The last clauses are used to switch the active circuit after the global output was improved via a shadow variable.

\(C_i^T:=f\rightarrow(o_i\le v_i^T)\vee s_i^B\) (4.13) \(C_i^B:=\neg f\rightarrow(o_i\le v_i^B)\vee s_i^T\) (4.14) \(C_i^O:=o_i\) (4.15) \((o_i\wedge s_i^B)\rightarrow\neg f\) (4.16) \((o_i\wedge s_i^T)\rightarrow f\) (4.17)

**5. Use shadow variables at improvable positions.** If the inactive circuit is better at a position _i_ than the active circuit, these clauses will be false unless the shadow variable is turned on. Shadow variables of the active circuit have, however, no incentive to be switched on from here. The order is arbitrary in this group.

\((f\wedge v_i^B\wedge\neg v_i^T)\rightarrow s_i^B\text{and}(\neg f\wedge v_i^T\wedge\neg v_i^B)\rightarrow s_i^T\) (4.18)

**6. Turn off shadow variables**<br> The final set of clauses allows deactivating any shadow variable. The order is arbitrary in this group.

\(\neg s_i^B\text{and}\neg s_i^T\) (4.19)

Previously, we flipped both _f_ and a global output _o<sub>i</sub>_ in order to gain an improvement. The new idea is to first set the shadow variable \(s_i^B\) to 1 (without loss of generality BOTTOM is inactive), for which clause (4.18) gives us an incentive. Now the control clause \(f\rightarrow(o_i\le v_i^T)\vee s_i^B\) (4.13) is additionally satisfied by \(s_i^B\), which enables us to flip the global output _o<sub>i</sub>_ to 1; finally this leads to flipping _f_. As a last step we can turn all shadow variables off again in the now active circuit BOTTOM using group 6. PLS-completeness now follows from the following lemma, which we prove in Section A:

\(\blacktriangleright\) **Lemma 8.** _Let_ \(\alpha\) _be a locally optimal assignment to the 4-CNF just constructed and consider_ **x**_<sup>A</sup>, the input variables of the active circuit. Then_ \(\alpha(\mathbf{x}^A)\) _is a local optimum of the_ Flip _instance C._

