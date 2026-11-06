The _m_ blocks are ordered from 1 (most important) to _m_ (least important) and within each block, the three clauses<sup>2</sup> are ordered as shown above.

Now if we have a local optimum of this LocalLexMax-4-SAT instance, then by the same reasoning as in Section 4.1, all circuits are correctly evaluated and BOTTOM’s input is TOP’s output and thus (**v**_<sup>A</sup>,_**z**_<sup>A</sup>_)=_C_(**x**_<sup>A</sup>_) and (**v**_<sup>I</sup>,_**z**_<sup>I</sup>_)=_C_(**x**_<sup>I</sup>_)=_C_(**z**_<sup>A</sup>_). Additionally, it holds that **o**=**v**_<sup>A</sup>_. If \(\mathbf{v}^I\le_{lex}\mathbf{v}^A\) we have found a solution to the original Flip instance. Otherwise, **v**_<sup>I</sup>\><sub>lex</sub>_**v**_<sup>A</sup>_=**o**. Let _i_ be the first position where they differ, so \(v_i^I=1\) and \(v_i^A=0\) (and thus _o<sub>i</sub>_=0). Now flipping the value _f_ and simultaneously setting _o<sup>i</sup>_ to 1 keeps Group 1 satisfied; the clauses in blocks \(1,\cdots\le i-1\) of Group 2 do not change; in block _i_ we gain (_o<sub>i</sub>_) and now satisfy all three clauses; we might wreak havoc in blocks _i_+1_,...,m_ and Group 3, but gaining (_o<sub>i</sub>_) outweighs all this. Thus, if we are not at a local optimum for Flip, we aren’t at one for LocalLexMax-4-SAT, either, and the reduction is correct.

## 4.3 Replacing double flips with single flips

In the previous section, we need to flip two variables to simulate a flip in the circuit instance. Flipping only _o<sub>i</sub>_ from 0 to 1 will violate the _i_<sup>th</sup> control clause of the active circuit, and flipping _f_ alone does not increase and likely reduces the payoff. We introduce new variables that we call _shadow variables_, denoted by \(s_i^B\) and \(s_i^T\) for every output bit. Their purpose is to temporarily fulfill a control clause so that we can flip _o<sub>i</sub>_. Then we can flip _f_ and continue as above.

We need to introduce two new groups of hard clauses, 0 and 1b, the latter located between group 1 and 2; modify group 2; and add groups 5 and 6. Groups 1, 3, and 4 are as above.

**0. Both inputs are equal or neighbors of the flip instance.** These hard clauses prevent assignments where the inputs of both circuits have a Hamming distance greater than one. They are not strictly needed for PLS-completeness but ensure _tightness_ of the reduction (see Section D).

\(\forall i\neq j:x_i^T\neq x_i^B\rightarrow x_j^T=x_j^B\) (4.8)

The ordering among Group 0 clauses is arbitrary.

**1b. Proper use of shadow variables.** These hard clauses have the purpose to disallow using shadow variables if there is no flip to be done. All clauses in this group can be satisfied by setting a shadow variable to false.

Shadow variables should be turned on only when the corresponding circuit is correctly evaluated and, in case it is the inactive circuit, it is reading its correct input, namely the best-neighbor output of the active circuit. Thus, for every output position \(1\le i\le m\) and every input position \(1\le j\le n\) we produce

\((s_i^B\wedge f)\rightarrow(z_j^T=x_j^B)\text{and}(s_i^T\wedge\neg f)\rightarrow(z_j^B=x_j^T)\) (4.9)

saying that a "shadowed inactive" circuit must read the correct input. Second, we require a shadowed circuit to be correct in all gates. Thus, if a gate _g<sub>j</sub>_ has inputs _y_<sub>1</sub> and _y_<sub>2</sub>, we produce

\(s_i^T\rightarrow(g_j^T\leftrightarrow\mathrm{NAND}(y_1^T,y_2^T))\text{and}s_i^B\rightarrow(g_j^B\leftrightarrow\mathrm{NAND}(y_1^B,y_2^B))\) (4.10)

<sup>2</sup> \(C_i^T\) and \(C_i^B\) are indeed clauses: \((\neg f\vee\neg o_i\vee v_i^T)\) and \((f\vee\neg o_i\vee v_i^B)\).

