#### Step 3: Base case.

When the interval _I_ becomes sufficiently small (length at most _B_base, where \(B_\mathrm{base}=\lceil(\mathrm{log}T)^c\rceil\) for some fixed constant _c_), we solve the subproblem directly by constructing a local DP table over _I_ using \(O(\omega+B_\mathrm{base})\) space and then backtracking pointers within _I_.

We now formalize the recursive step.

## 5.3 Middle frontiers and midpoint vertices

We first make precise the analogue of the "middle column" in the grid setting.

**Definition 7** (Middle frontier)**.** _Let I_=\[_i,j_\] _be an interval in_ R_, and let m=m(I_) _be its midpoint. The_ middle frontier _of I is_

\(F_I^\mathrm{mid}:=\{v\in V_I:v\le m\text{\textit{and}}\exists w>m\text{\textit{with}}(v,w)\in E\}.\)

By construction, \(F_I^\mathrm{mid}\subseteq\mathrm{Front}(m)\), so

\(|F_I^\mathrm{mid}|\le\omega.\)

**Lemma 5** (Crossing existence)**.** _Let_ (_I,B_left_,s,_val) _be a traceback subproblem with I_=\[_i,j_\] _and m=m(I), and suppose s\>m. Let P be any optimal witness path from B_left _to s whose internal vertices lie in I (guaranteed by Lemma 4). Then P contains at least one vertex from_ \(F_I^\mathrm{mid}\).

_Proof._ Let _P_=(_v_<sub>0</sub>_,...,v<sub>k</sub>_), with \(v_0\in B_\mathrm{left}\) and _v<sub>k</sub>=s_. Since \(v_0<i\le m\) and \(s\in I\) with _s\>m_, there exists an index _r_ with \(v_r\le m\) and _v_<sub>_r_+1</sub>_\>m_. Because all internal vertices of _P_ lie in _I_ and \(v_0\notin I\), the vertex _v<sub>r</sub>_ lies in _V<sub>I</sub>_. The edge \((v_r,v_{r+1})\in E\) then certifies \(v_r\in F_I^\mathrm{mid}\).

Lemma 5 guarantees that any optimal path consistent with val must pass through at least one candidate vertex in \(F_I^\mathrm{mid}\) whenever _s_ lies to the right of the midpoint. Our goal is to identify a vertex on this frontier that lies on a canonical witness path.

## 5.4 Forward-only evaluation of prefix and suffix costs

The classical Hirschberg algorithm uses both a forward DP (from the source) and a backward DP (from the sink) to evaluate candidate midpoints. In our general DAG setting, the reverse graph need not have small frontier width, so backward DP may be space-inefficient. Instead, we compute both "prefix" and "suffix" costs using forward passes and local recomputation, relying on Lemma 3 and the invariant in Lemma 4.

Throughout this subsection we assume _s\>m(I_), so that the middle frontier is nontrivial in the sense of Lemma 5.

#### Prefix values _f(v_).

For the subproblem (_I,B_left_,s,_val), define _f(v_) for \(v\in F_I^\mathrm{mid}\) as

\(f(v):=\mathrm{optimal value of a path from some}u\in B_\mathrm{left}\text{to}v,\)

subject to the condition that all internal vertices of the path lie in \(I\cap[i,m]\). By Lemma 3 (applied to the interval \[_i,m_\] with boundary _B_left), we can compute all _f(v_) for \(v\in F_I^\mathrm{mid}\) in a _single_ forward DP pass over \[_i,m_\]:

• we treat _B_left as the boundary with known values;<tbc>

• we evaluate the DP recurrence forward from _i_ up to _m_, maintaining an \(O(\omega)\)-sized frontier buffer;<tbc>

• when we reach time _m_, all _x<sub>v</sub>_ for \(v\in F_I^\mathrm{mid}\) are available and we set _f(v_)=_x<sub>v</sub>_.

#### Suffix values _g(v_).

For the same subproblem, define _g(v_) for \(v\in F_I^\mathrm{mid}\) as

\(g(v):=\mathrm{optimal value of a path from}v\text{to}s\)

subject to the condition that all internal vertices of the path lie in _I_.

We compute _g(v_) for each \(v\in F_I^\mathrm{mid}\) by _repeated_ forward passes restricted to _I_:

1. Treat _v_ as a boundary vertex whose DP value is initialized to the multiplicative identity of the semiring S, and treat all vertices _u\<v_ as absent for this local DP.

