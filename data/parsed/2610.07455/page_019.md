that _r<sub>t</sub>=a_ and \(r^{t\leftarrow b}\notin R\). The corresponding constraint from the second family is assigned the tuple \(\sigma(r^{t\leftarrow b})\), which is not in _R_ because \(\sigma\) is an automorphism. This contradicts that \(\alpha\) satisfies _P<sub>s</sub>_. Hence \(\alpha(x)=\sigma(s(x))\) for every \(x\in X\).

Conversely, fix any \(\sigma\in Aut(R)\) and assign \(y_a\mapsto\sigma(a)\) and \(x\mapsto\sigma(s(x))\). Every constraint in both families is then assigned a tuple of the form \(\sigma(r)\) for some \(r\in R\), so all constraints are satisfied. The restrictions of satisfying assignments to _X_ are therefore exactly the assignments \(\sigma\circ s\) with \(\sigma\in Aut(R)\).

The gadget therefore behaves like a genuine pinning whenever the objective is unchanged by a common automorphism. For exact optimization we need more because the goal is not merely to satisfy the whole instance. An assignment may gain constraints in the original instance by violating some constraints in the pinning gadget. We therefore need to ensure that deviating from the intended assignment loses more gadget constraints than it can gain in the original instance. We do this next.

## 4.3 Pinning for exact optimization

We now strengthen the construction for exact optimization. The input instance _P_ may reward an assignment for moving away from _s_, so a merely satisfiable pinning gadget is not enough. Intuitively, we replace each domain value by a block of many variables. The constraints among the blocks create a large loss unless their most frequent values form an automorphism, and the constraints joining _P_ to the blocks create a large loss whenever an original variable disagrees with _s_ under that automorphism.

**Lemma 4.6.** _Let_ \(R\subseteq D^k\) _be a core relation with_ \(k\ge 2\)_, and fix_ \(1\le d\le k\)_. Let P be a simple R-instance on O<sub>R</sub>(N_) _variables, with at most N<sup>d</sup> constraints and maximum variable degree at most N_<sup>_d_-1</sup>_. For every assignment s to the variables of P, there is an unweighted R-instance H<sub>s</sub>, using the variables of P and O<sub>R</sub>(N_) _additional variables, such that_ \(P\cup H_s\) _is simple and_

\(\mathrm{OPT}_{\mathrm{max}}(P\cup H_s)=|H_s|+\mathrm{val}_P(s).\)

_If R is symmetric and P has no repeated unordered scope, then_ \(P\cup H_s\) _has no repeated unordered scope. Moreover, H<sub>s</sub> can be constructed from R, the variable set of P, the assignment s, and the public parameters N and d. It does not depend on the constraints of P._

_Proof of Lemma 4.6._ Let _X_ be the variable set of _P_, let _B_ be the number of constraints in _P_, and let \(\Delta\) be its maximum variable degree. Thus \(B\le N^d\) and \(\Delta\le N^{d-1}\). We will choose a constant _C<sub>R</sub>_ below and set _m=C<sub>R</sub>N_.

The construction follows the same idea as Lemma 4.4. We first create many variables that represent each value of the domain up to one common automorphism. We then connect the variables of _P_ to these new variables. More formally, for every \(a\in D\), create a _block Z<sub>a</sub>_ of _m_ new variables. For every tuple \(r=(r_1,\dots,r_k)\in R\) and every choice of pairwise distinct variables \(z_i\in Z_{r_i}\), add the constraint _R(z_<sub>1</sub>_,...,z<sub>k</sub>_). We call these the _block constraints_. Next fix \(x\in X\) and put _a=s(x_). For every \(r\in R\), every \(t\in[k]\) with _r<sub>t</sub>=a_, and every choice of pairwise distinct variables \(z_j\in Z_{r_j}\) for \(j\neq t\), add the constraint _R(z_<sub>1</sub>_,...,z_<sub>_t_-1</sub>_,x,z_<sub>_t_+1</sub>_,...,z<sub>k</sub>_). We call these the _attached constraints for x_. If the same ordered scope arises more than once, keep only one constraint. When _R_ is symmetric, keep only one constraint for each unordered scope. Let _H<sub>s</sub>_ be the union of the block constraints and all the attached constraints.

Firstly note that the instance \(P\cup H_s\) is simple. This is because the constraints of _P_ use only variables in _X_, block constraints use only variables from the blocks, and an attached constraint for<tbc>

