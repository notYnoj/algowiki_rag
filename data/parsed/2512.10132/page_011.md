Intuitively, (_I,B_left_,s,_val) represents a subproblem in which we have "compressed" everything before time _i_ into boundary vertices and wish to reconstruct the portion of the canonical witness path whose internal vertices lie between _i_ and _j_.

The algorithm maintains the following invariant.

**Lemma 4** (Subproblem invariance)**.** _In the initial call and at every recursive call of the traceback procedure, the subproblem_ (_I,B_left_,s,_val) _satisfies:_

1. \(B_\mathrm{left}\subseteq\{1,\dots,i-1\}\cup S_\mathrm{src}\) _and_ \(s\in I\),<tbc>

_2._ _there exists at least one optimal witness path P from B_left _to s whose internal vertices all lie in I and whose semiring value is_ val.

_In particular, for the initial call we have_ val=_x<sub>t</sub>._

_Proof._ For the initial call, we set _I_=\[1_,T_\], _B_left=_S_src, _s=t_, and val=_x<sub>t</sub>_. By definition of _x<sub>t</sub>_, there exists an optimal path from _S_src to _t_ with value _x<sub>t</sub>_, and all its internal vertices lie in _I_=\[1_,T_\]. Thus items (1) and (2) hold. Note that for _I_=\[1_,T_\], the condition \(B_\mathrm{left}\subseteq\{1,\dots,0\}\cup S_\mathrm{src}\) simplifies to \(B_\mathrm{left}\subseteq S_\mathrm{src}\), which holds.

Assume the lemma holds for a parent subproblem (_I,B_left_,s,_val) with _I_=\[_i,j_\]. Let _m=m(I_).

• If \(s\le m\), then any path from _B_left to _s_ contained in _I_ must lie entirely in \[_i,m_\]=_I<sub>L</sub>_, as indices strictly increase. Since an optimal path _P_ exists for the parent, that same _P_ is valid for the child subproblem (_I<sub>L</sub>,B_left_,s,_val). Thus the invariant holds.<tbc>

• If _s\>m_, let _P_ be an optimal witness path guaranteed by the parent invariant. Lemma 5 (proved below) shows that _P_ intersects the middle frontier \(F_I^\mathrm{mid}\) at some vertex \(v^\circ\). Proposition 1 (proved later) establishes that<tbc>

\(\mathrm{val}=\mathrm{max}_{v\in F_I^\mathrm{mid}}(f(v)\otimes g(v)).\)

The algorithm selects a canonical maximizer \(v^\star\in F_I^\mathrm{mid}\) deterministically. Since _v<sup>⋆</sup>_ achieves the maximum, there exists an optimal path _P<sup>⋆</sup>_ passing through _v<sup>⋆</sup>_ with value val.<tbc>

<tbc>Split _P<sup>⋆</sup>_ at _v<sup>⋆</sup>_ into a prefix _P_<sub>pref</sub> (from _B_left to _v<sup>⋆</sup>_) and a suffix _P_<sub>suff</sub> (from _v<sup>⋆</sup>_ to _s_). The value of _P_<sub>pref</sub> is _f(v<sup>⋆</sup>_) and the value of _P_<sub>suff</sub> is _g(v<sup>⋆</sup>_).<tbc>

<tbc>Hence, the left subproblem (_I<sub>L</sub>,B_left_,v<sup>⋆</sup>,f(v<sup>⋆</sup>_)) admits _P_<sub>pref</sub> as an optimal witness, and the right subproblem (_I<sub>R</sub>,{v<sup>⋆</sup>},s,g(v<sup>⋆</sup>_)) admits _P_<sub>suff</sub> as an optimal witness. The invariant is preserved for both children.

A formal induction on the recursion depth completes the proof.

## 5.2 High-level algorithmic structure

At a high level, the Universal Hirschberg algorithm consists of three components:

1. a global forward DP to compute _x<sub>t</sub>_;<tbc>

2. a recursive traceback procedure structured by the recursion tree R;<tbc>

3. a base case that performs explicit local DP and backtracking within small intervals.

### Step 1: Global valuation.

We first execute a standard forward DP sweep over _G_ in topological order, using a rolling frontier as in Lemma 3, to compute all _x<sub>v</sub>_ and in particular _x<sub>t</sub>_. This requires \(O(\omega)\) space and _O(T_) time. The values of intermediate states are _not_ stored persistently; only _x<sub>t</sub>_ (and, implicitly, the instance description on the read-only tape) is retained.

### Step 2: Recursive traceback.

We then invoke a recursive procedure

Traceback(_I,B_left_,s,_val)

which outputs the segment of the witness path whose internal vertices lie in _I_. The recursion follows the decomposition of _I_ into balanced sub-intervals; at each level, if _s_ lies strictly to the right of the midpoint, we identify a "midpoint" vertex _v<sup>⋆</sup>_ through which an optimal path contributing to val must pass, and we recurse on the two resulting subproblems.

