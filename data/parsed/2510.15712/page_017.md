and 1 since \(s_i^B\) does not occur there. In group 1b all clauses stay fulfilled since by Lemma 13 all gate variables are correct and the input of the inactive circuit BOTTOM matches the neighbor output of the active circuit TOP by Lemma 15. Also since \(\alpha(v_i^B)=1\) and \(\alpha(v_i^T)=0\) holds, the final type of clause in group 1b is fulfilled: \(s_i^B\rightarrow v_i^B\) and \(s_i^B\rightarrow\neg v_i^T\) (4.11).

In group 2, \(s_i^B\) occurs in \(f\rightarrow(o_i\le v_i^T)\vee s_i^B\) (4.13) and \((o_i\wedge s_i^B)\rightarrow\neg f\) (4.16). The former is satisfied with \(\alpha(s_i^B)=1\), the latter is and stays satisfied by \(\alpha(o_i)=0\).

**Case 01:** \(\alpha(o_i)=0\) and \(\alpha(s_i^B)=1\). Consider setting _o<sub>i</sub>_ to 1. This affects only block _i_ of group 2. The control clause \(f\rightarrow(o_i\le v_i^T)\vee s_i^B\) (4.13) is and stays satisfied by \(\alpha(s_i^B)=1\); the control clause \(\neg f\rightarrow(o_i\le v_i^B)\vee s_i^T\) (4.14) is and stays satisfied by \(\alpha(f)=1\). The third clause in block i, (_o<sub>i</sub>_) (4.15), becomes newly satisfied and thus the overall satisfied weight improves.

**Case 11:** \(\alpha(o_i)=1\) and \(\alpha(s_i^B)=1\). Then changing _f_ to 0 wins us the flip clause \((o_i\wedge s_i^B)\rightarrow\neg f\) of group 2 (4.16). Clauses in earlier blocks _j\<i_ of group 2 are not affected: control clauses like \(\neg f\rightarrow(o_j\le v_j^B)\vee s_i^T\) (4.14) stay satisfied since _o<sub>j</sub>_ and \(v_j^B\) agree due to Lemma 16; flip clauses \((o_j\wedge s_j^T)\rightarrow f\) (4.17) stay satisfied because all shadow variables of TOP are 0 by Lemma 10. Also, we know by Lemma 13 that all gate clauses are correct, so all clauses in group 1 stay correct, too. Finally _f_ does not occur in any clause of group 0 or 1b, so they stay satisfied.

Note that this flip process would also start when \(v_i^T>v_i^B\) but \(v_k^T<v_k^B\)) for some _k\>i_. It would flip \(s_k^B\) to 1 (Case 00) and then _o<sub>k</sub>_ (Case 01) but would fail to flip _f_ (Case 11) since that would violate the control clause \(\neg f\rightarrow(o_i\le v_i^B)\vee s_i^T\) (4.14).

We conclude that \(\alpha(\mathbf{x}^T)\) is indeed a solution to the Flip instance _C_. This concludes the proof of Theorem 9.

## B The Max-3-SAT/2-Flip problem

There is currently a gap between the PLS-completeness of LocalLexMax-4-SAT and the polynomial algorithm for LocalLexMax-2-SAT. We can only show hardness for LocalLexMax-3-SAT if we allow double flips.

\(\blacktriangleright\) **Theorem 17.** LocalLexMax-3-SAT_/2-FLIP is PLS-complete._

The reduction is almost identical to the one in Section 4.2, with one crucial modification: for each gate _g<sub>j</sub>_ we introduce not one but _three_ variables _g<sub>j</sub>,g_<sub>_j,_1</sub>_,g_<sub>_j,_2</sub>, and then two copies of each corresponding to TOP and BOTTOM: \(g_j^T,g_{j,1}^T,g_{j,2}^T,g_j^B,g_{j,1}^B,g_{j,2}^B\). The idea is that _g_<sub>_j,_1</sub> and _g_<sub>_j,_2</sub> represent the two inputs of the gate and _g<sub>j</sub>_ the output. We introduce a "Group 0" of 3-clauses with the highest priority that state gates should be correct at all times:

\(g_j^T\leftrightarrow\mathrm{NAND}(g_{j,1},g_{j,2}).\) (Group 0)

We modify the clauses in Group 1; we replace the 4-clauses constructed in (4.1) and (4.2), namely

\(f\rightarrow(g_j^T\leftrightarrow\mathrm{NAND}(y_1^T,y_2^T))\)<br> \(\neg f\rightarrow(g_j^B\leftrightarrow\mathrm{NAND}(y_1^B,y_2^B))\) (The Group 1 in the previous reduction)

by clauses requiring that the input of gate _g<sub>j</sub>_ must agree with the output of the gate feeding into it; in other words, if the output of gate _g<sub>i</sub>_ feeds into the first output of gate _g<sub>j</sub>_, we add

