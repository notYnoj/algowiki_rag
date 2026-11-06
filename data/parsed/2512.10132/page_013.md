2. Apply a forward scanning procedure analogous to Lemma 3 to the interval \[_v,j_\] with boundary {_v_} to recompute the DP in \(I\cap[v,j]\). As shown in the proof of Lemma 3, this maintains an active set that is a subset of the global frontier Front(_k_), thus using at most \(O(\omega)\) workspace.<tbc>

3. At the index _s_, read off the recomputed value _x<sub>s</sub>_ and set _g(v_):=_x<sub>s</sub>_.

Because the invariant in Lemma 4 ensures that all internal vertices of the relevant suffix paths lie in _I_, ignoring vertices outside _I_ does not change the optimal values. Each such pass uses \(O(\omega)\) space (in words). Since we process candidates \(v\in F_I^\mathrm{mid}\) sequentially and \(|F_I^\mathrm{mid}|\le\omega\), the total workspace remains \(O(\omega)\), at the cost of an extra factor of \(\omega\) in time.

## 5.5 Midpoint selection and recursive decomposition

We now argue that the values _f(v_) and _g(v_) are sufficient to locate a canonical midpoint on the optimal path when _s\>m(I_).

**Proposition 1** (Value decomposition)**.** _Let_ (_I,B_<sub>left</sub>_,s,_val) _be a traceback subproblem with midpoint m=m(I), and suppose s\>m. Then_

\(\mathrm{val}=\oplus_{v\in F_I^\mathrm{mid}}\big(f(v)\otimes g(v)\big).\)

_Proof._ Let _P_ be any optimal witness path from _B_<sub>left</sub> to _s_ whose internal vertices lie in _I_, as in Lemma 4. By Lemma 5, _P_ crosses the cut at _m_ at some vertex \(v^\circ\in F_I^\mathrm{mid}\). Split _P_ at \(v^\circ\) into a prefix path _P_<sub>pref</sub> from _B_<sub>left</sub> to \(v^\circ\) with internal vertices in \(I\cap[i,m]\) and a suffix path _P_<sub>suff</sub> from \(v^\circ\) to _s_ with internal vertices in \(I\cap[v^\circ+1,j]\subseteq I\).

By definition of \(f(\cdot)\), the semiring value along _P_<sub>pref</sub> is at most \(f(v^\circ)\), and by optimality of _P_ and consistency of local recomputation (Lemma 1) we in fact have equality:<tbc>

\(\mathrm{value}(P_\mathrm{pref})=f(v^\circ).\)

<tbc>Similarly, the semiring value along _P_<sub>suff</sub> is at most \(g(v^\circ)\) by definition of \(g(\cdot)\), with equality for the same reasons:<tbc>

\(\mathrm{value}(P_\mathrm{suff})=g(v^\circ).\)

<tbc>The value of _P_ is then<tbc>

\(\mathrm{val}=\mathrm{value}(P)=\mathrm{value}(P_\mathrm{pref})\otimes\mathrm{value}(P_\mathrm{suff})=f(v^\circ)\otimes g(v^\circ).\)

<tbc>Conversely, for any \(v\in F_I^\mathrm{mid}\), consider an optimal path _Q_<sub>pref</sub> from _B_<sub>left</sub> to _v_ achieving _f(v_) (within \(I\cap[i,m]\)) and an optimal path _Q_<sub>suff</sub> from _v_ to _s_ achieving _g(v_) (within _I_). Concatenating _Q_<sub>pref</sub> and _Q_<sub>suff</sub> yields a valid path _Q_ from _B_<sub>left</sub> to _s_ whose internal vertices lie in _I_. Its semiring value is exactly \(f(v)\otimes g(v)\) by associativity of \(\otimes\). Since val is the optimal value over all such paths (by the definition of the traceback subproblem), we must have<tbc>

\(\mathrm{val}\unknown f(v)\otimes g(v)\)

<tbc>for every \(v\in F_I^\mathrm{mid}\), and equality holds for \(v=v^\circ\). Taking the supremum (which is \(\oplus\)) over _v_ yields

\(\mathrm{val}=\oplus_{v\in F_I^\mathrm{mid}}\big(f(v)\otimes g(v)\big),\)

as claimed.

Because the semiring is max-type and we apply a deterministic tie-breaking rule at this step (e.g., selecting the vertex with the smallest index), the algorithm makes a _canonical_ choice:

\(v^\star=\mathrm{argmax}_{v\in F_I^\mathrm{mid}}\big(f(v)\otimes g(v)\big).\)

This selection defines a hierarchy of tie-breaking: structural ties at the midpoint are resolved by vertex order, while local ties within the base case are resolved by edge order (Assumption 2). Proposition 1 guarantees that _v<sup>⋆</sup>_ lies on at least one optimal path, decomposing the subproblem into two strictly smaller ones:

• a left subproblem (_I<sub>L</sub>,B_<sub>left</sub>_,v<sup>⋆</sup>,f(v<sup>⋆</sup>_)) for paths from _B_<sub>left</sub> to _v<sup>⋆</sup>_ with internal vertices in _I<sub>L</sub>_;<tbc>

• a right subproblem (_I<sub>R</sub>,{v<sup>⋆</sup>},s,g(v<sup>⋆</sup>_)) for paths from _v<sup>⋆</sup>_ to _s_ with internal vertices in _I<sub>R</sub>_.<tbc>

