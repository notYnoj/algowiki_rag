Thus, the bit string \(v=s\circ\pi^l\) has a 1 on a bad-color position if _v_ does not represent a Boolean assignment to the variables; if it does represent a Boolean assignment \(\alpha\), then _v_ has a 1 on the clause-violating position of clause _C_ if and only if \(\alpha\) violates _C_.

For each variable _x<sub>i</sub>_ and each \(r\in\mathbb{Z}_{pi_i}\) let _m_ be such that

\(m\equiv rmodp_i\)<br> \(m\equiv 0modp_j\) (for all \(j\neq i\))

and set \(\pi_{xi_i,r}:=\pi^m\). The idea is that the permutation \(\pi_{xi_i,r}\) changes the value of _x<sub>i</sub>_ but not of any other variable. The generators for our Polm instances are now all \(\pi_{xi_i,r}\). This gives a polynomially long list of permutations \(\pi^{e_1},\pi^{e_2},\dots,\pi^{e_M}\), all powers of a single permutation \(\pi\).

\(\blacktriangleright\) **Lemma 20.** _Let l be such that_ \(s\circ\pi^l\) _is a local minimum, i.e.,_ \(s\circ\pi^l\circ\pi^{e_i}\ge_\mathrm{lex}s\circ\pi^l\) _for all_ \(1\le i\le M\)_. Then_ \(s\circ\pi^l\) _encodes an assignment_ \(\{x_1,\dots,x_n\}\rightarrow\{0,1\}\) _that is locally optimal for F under 2-flips._

**Proof.** Let \(v:=s\circ\pi^l\). Each variable cycle contains exactly one position where _v_ has a 1. This assigns each _x<sub>i</sub>_ a value \(b\in\{0,1,\dots,p_i-1\}\). Now if \(b\unknown\in\{0,1\}\) then _v_ has a 1 at position _b_ of this cycle--a bad-color-position. Applying \(\pi_{xi_i,p_i-b}\) moves the 1 on this cycle to the 0-position but leaves all other variable cycles as they are. We have moved a 1 away from a bad-color-position and thus decreased the cost of _v_; hence _v_ is not a local minimum.

Conversely, if _v_ is a local minimum, then _v_ has no 1 at any bad-color position and thus _v_ encodes, as described above, a truth assignment \(\alpha\) to the variables _x_<sub>1</sub>_,...,x<sub>n</sub>_. Suppose \(\alpha\) is not locally optimal for _F_ but can be improved by flipping a variable _x<sub>i</sub>_. This flip can be realized by the permutation \(\pi_{xi_i,r}\) where _r_ is 1 if we want to flip _x<sub>i</sub>_ from 0 to 1 and _p<sub>i</sub>_-1 if we want to flip it from 1 to 0. Since flipping _x<sub>i</sub>_ is an improving step, it additionally satisfies some clause _C_ and does not additionally violate any higher priority clause \(C'\); thus, applying \(\pi_{xi_i,r}\) moves the 1 of _v_ away from the clause-violating position of _C_ but places no new 1 on any clause-violating position of any higher-priority clause \(C'\). Also, it does not move a 1 onto any bad-color-position. Thus, _v_ is not a local minimum, either.

We infer that every local minimum \(v=s\circ\pi^l\) under the permutations \(\pi^{e_1},\dots,\pi^{e_M}\) corresponds to a local maximum of the 4-SAT/1-FLIP instance _F_. This concludes the proof of Theorem 19.

## D Tightness

The notion of _tightness_ was introduced by Schäffer and Yannakakis in [19] to also reason about the complexity of the standard algorithm. The standard algorithm uses a starting solution and always follows the best neighbor until it finds a local optimum. Finding the solution of the standard algorithm for Flip is PSPACE-complete [17]. Tight reductions preserve the PSPACE-completeness of the standard algorithm.

For this, we consider the transition graph _TG(I_). Its vertices are the solutions to instance _I_, and each feasible solution _x_ has a directed edge to each of its improving neighbors in _N(x_). A PLS-reduction (_f,g_) from _P_ to _Q_ is called _tight_ if for every instance _I_ of _P_ there exists a set R of feasible solutions for _f(I_) such that

1. R contains all local optima of _f(I_)

2. For every solution _s_ of _I_ it is possible to construct in polynomial time a feasible solution \(t\in\mathcal{R}\) such that _g(I,t_)=_s_

