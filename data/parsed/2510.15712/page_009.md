Within this group, the ordering of the clauses follow the topological ordering of the gates (when _g_ feeds into _h_, then _g_ comes before _h_ and the clauses thusly produced come first, too. Within the eight clauses of (4.1-4.2) for a single gate, the order is arbitrary.

**2. The value output of the active circuit should be large.** For each value output position \(1\le i\le m\) we create two 2-clauses: \((f\rightarrow v_i^T)\) and \((\neg f\rightarrow v_i^B)\). The clauses are ordered from _i_=1 (most important) to _i=m_ (least important), and for the same _i_, the two clauses have equal weight (here we lose perfect lexicographicality).

**3. Successor output of active circuit should be input of inactive circuit.** We write this as

\(f\rightarrow(z_j^T=x_j^B)\text{and}\neg f\rightarrow(z_j^B=x_j^T).\) (4.3)

The ordering within this group is arbitrary.

**4. All gates should be correctly evaluated,** whether in the active or inactive circuit.

\(g_j^T\leftrightarrow\mathrm{NAND}(y_1^T,y_2^T)\text{and}g_j^B\leftrightarrow\mathrm{NAND}(y_1^B,y_2^B)\) (4.4)

We call clauses in Group 1 _hard clauses_ because they would always stay satisfied on an improving path, and if violated can be easily corrected. It is straightforward to check that in a local optimum of this LocalMax-4-SAT-instance, all gates are evaluated correctly and the output of the active circuit agrees with the input of the inactive. Thus, it holds that (**v**_<sup>A</sup>,_**z**_<sup>A</sup>_)=_C_(**x**_<sup>A</sup>_) and (**v**_<sup>I</sup>,_**z**_<sup>I</sup>_)=_C_(**x**_<sup>I</sup>_)=_C_(**z**_<sup>A</sup>_). If **v**_<sup>I</sup>\><sub>lex</sub>_** **v**_<sup>A</sup>_, then flipping the value of _f_ would (i) keep clauses in Group 1 satisfied; (ii) improve the weight of satisfied clauses in Group 2, and (iii) possibly violate clauses in Group 3. By the chosen weights, this would be an improving flip. Thus, if we have a local optimum of this LocalMax-4-SAT-instance, then \(\mathbf{v}^I\le_{lex}\mathbf{v}^A\) and **x**_<sup>A</sup>_ is indeed a solution of the original Flip instance.

## 4.2 Making Weights Fully Lexicographic By Allowing Double Flips

The trouble lies in Group 2. If we naively decree that \((f\rightarrow v_i^T)\) be more valuable than (actually, twice as) \((\neg f\rightarrow v_i^B)\), then the reduction would become incorrect: if **v**_<sup>T</sup>_=(01_..._) and **v**_<sup>B</sup>_=(00_..._) and BOTTOM is active, then flipping _f_ from 0 to 1 would improve the output but violate \((f\rightarrow v_i^T)\) instead of \((\neg f\rightarrow v_i^B)\), thus reducing the weight of satisfied clauses. We are stuck in a local optimum that does not correspond to a local optimum of Flip.

To solve this problem, we create a _global output register_ **o** consisting of _m_ variables _o_<sub>1</sub>_,...,o<sub>m</sub>_. The idea is now that (1) **o** should be large, but (2) not larger than the active output. When switching active and inactive circuits, we can flip _f and simultaneously_ the improving position of **o**, improving (1) but temporarily violating (2). To make this work we need to choose the order of the clauses in Group 2 carefully.

**2. The global output register should be large, but not larger than the active output.** For each \(1\le i\le m\), we replace the two old clauses \((f\rightarrow v_i^T)\) and \((\neg f\rightarrow v_i^B)\) by

\(\text{the}i^\mathrm{th}\text{TOP control clause}C_i^T:=(f\rightarrow(o_i\le v_i^T))\) (4.5)

\(\text{the}i^\mathrm{th}\text{BOTTOM control clause}C_i^B:=(\neg f\rightarrow(o_i\le v_i^B))\) (4.6)

\(\text{the}i^\mathrm{th}\text{output clause}C_i^O:=(o_i)\) (4.7)

