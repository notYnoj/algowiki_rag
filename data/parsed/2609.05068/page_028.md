**Theorem 5.1.** _Let_ \(E\subseteq\PazoBB{R}^+\times\PazoBB{R}^n\) _be a set and f be a continuous function_ \(E\rightarrow\PazoBB{R}\)_. Consider the conditional constraint_ \(f(x,\mathbf{y})\le 0\) _if x\>_0 _for variables_ \((x,\mathbf{y})\in E\)_. Any convex restriction of this constraint on E is either a restriction of the constraint_ \(f(x,\mathbf{y})\le 0\) _or a restriction of the constraint x_=0.

_Proof._ The proof results directly from Lemma 5.1 presented below.

Theorem 5.1 shows that there is no intermediate convex restriction for a conditional constraint and that any heuristic must make a distinct choice for each conditional constraint: it must either enforce the inequality \(f(x,\mathbf{y})\le 0\) unconditionally or force the value of the trigger variable _x_ to zero.

Consequently, any heuristic approach using convex restrictions is simply a constraint-selection process. To build a feasible solution, the algorithm must divide the conditional constraints into an active set, for which the constraint \(f(x,\mathbf{y})\le 0\) must be satisfied, and an inactive set, where the variables driving the conditions are forced to zero.

This result proves that searching for continuous convex restrictions for conditional constraints is futile. Instead, heuristic design must focus entirely on the combinatorial selection of the active constraints. Once this selection is made, the algorithm solves the resulting problem to obtain a feasible solution. If the original problem only involves convex (conditional) constraints and a convex objective function, this resulting problem is convex and computationally easy to solve.

**Lemma 5.1.** _Let_ \(E\subseteq\PazoBB{R}^+\times\PazoBB{R}^n\) _be a set and_ \(f:E\rightarrow\PazoBB{R}\) _be a continuous function. Any convex subset of_ \(\{(x,\mathbf{y})\in E|xf(x,\mathbf{y})\le 0\}\) _is either included in_ \(\{(x,\mathbf{y})\in E|f(x,\mathbf{y})\le 0\}\) _or in_ \(\{(x,\mathbf{y})\in E|x=0\}\).

_Proof._ Let us define the following sets:

\(D=\{(x,\mathbf{y})\in E|xf(x,\mathbf{y})\le 0\}\)<br>
\(D_\text{on}=\{(x,\mathbf{y})\in E|f(x,\mathbf{y})\le 0\}\)<br>
\(D_\text{off}=\{(x,\mathbf{y})\in E|x=0\}.\)

