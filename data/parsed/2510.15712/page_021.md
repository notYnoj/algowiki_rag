**3.** If the transition graph of _TG(f(I_)) contains a path from _q_ to \(q'\) such that both _q_ and \(q'\) are in R and all other intermediate nodes are not in R, let _p=g(I,q_) and \(p'=g(I,q')\) be the corresponding solutions in _P_. Then either \(p=p'\) or there is an arc from _p_ to \(p'\) in _TG(I_).

We now show that the reductions are tight. We start with the reductions from Flip to LocalLexMax-4-SAT. This reduction uses many steps (often called a super step) to simulate a single step in the Flip instance. We have to make sure that there is no earlier switch in a super step.

\(\blacktriangleright\) **Proposition 21.** _The reduction from_ Flip _to_ LocalLexMax-4-SAT _in Section 4 is tight._

**Proof.** Let _C_ be the instance of Flip and _F_ be the formula obtained by our reduction. We define R to be the set of assignments to _F_ where all clauses of group 0, 1 and 1b are fulfilled. If this is true, then we know that the active circuit is correct and the Hamming distance between the inputs of both circuits is at most 1. By Lemma 13 and Lemma 15 we know that any local optimum is in R. This shows that Point 1 holds.

We can take any solution **x** of Flip, set the input **x**_<sup>T</sup>_ of TOP to **x** and set all variables in the circuit such that all gates are correct and **z**_<sup>T</sup>_=**x**_<sup>B</sup>_ and _f_=1. The resulting assignment \(\alpha\) satisfies \(g(C,\alpha)=\mathbf{x}\). This shows that Point 2 holds.

Let us now show Point 3. First observe that if \(\alpha\in\mathcal{R}\) and there is an improving step \((\alpha,\beta)\) in _TG(F_), then \(\beta\) also satisfies groups 0, 1b, and 1, since they stay fulfilled along any improving path. So \(\beta\in\mathcal{R}\), too. Now let \(q,q'\in\mathcal{R}\) as in Point 3: there is a path in _TG(F_) from _q_ to \(q'\) and no other vertex on the path is in R. We have seen that _all_ vertices on an improving path starting in R are in R, so actually \((q,q')\) is an arc in _TG(F_), so \(q=\alpha\) and \(q'=\beta\), an assignment obtained from \(\alpha\) by changing one variable. Without loss of generality, assume that TOP is active.

There are two possibilities. If \(\alpha\) and \(\beta\) differ in a shadow variable, global output variable, or a variable in the inactive circuit, then \(\alpha\) and \(\beta\) represent the same solution to _C_, namely \(\alpha(\mathbf{x}^T)\). The other possibility is that it was created by flipping _f_. This only occurs when the inactive circuit is correct and its output is better than the output of the active circuit. But then \(g(C,\beta)=\alpha(\mathbf{x}^B)\) is an improving Flip-neighbor of \(g(C,\alpha)=\alpha(\mathbf{x}^T)\), which means that this is an arc in _TG(I_). \(\blacktriangleleft\)

In fact, the CNF formula resulting from our reduction can be designed to be _sensitive_, meaning that for every assignment \(\alpha\) and any variable _v_ there exists a clause _C_ such that changing the value of _v_ changes the truth value of _C_: \(\alpha(C)\neq\beta(C)\) for \(\beta:=\alpha[v\mapsto ¬\alpha(v)]\).

\(\blacktriangleright\) **Proposition 22.** _Sensitive_ LocalLexMax-4-SAT _is PLS-complete under a tight reduction._

**Proof.** Note that our reduction from Section 4.3 fulfills the sensitivity condition almost all variables: the global output variables change clauses in group 2; shadow variables in group 6; gate variables in group 4; and input variables of the inactive circuit in group 3.

The only remaining variables are _f_ and input variables in the active circuit. It might be that changing one input does not change the correctness of any clause stemming from a NAND-gate. In order to counter that, we can route each input through an "identity gate" behind each input (and simulate it by two NAND-gates). This does not change the circuit semantics, but changing the input now either fulfills or violates a gate clause.

For _f_ we can add a single clause that fixes _f_ to some value. This clause has the lowest weight of all. For the tightness this however this leads to problems as in the case of neighbors with equal outputs as the input of the top circuit is preferred to the input of the bottom

