<tbc>_Proof._ Let _L(d_) denote the maximum length of an interval at depth _d_. By construction, _L_(0)=_T_, and for any depth _d_, each child interval has length at most \(\lceil L(d)/2\rceil\). Thus \(L(d+1)\le\lceil L(d)/2\rceil\), which implies by induction that

\(L(d)\le T/2^d+1.\)

In particular, \(L(d)\le 1\) once \(d\ge log_2T+1\), so the depth is _O_(log_T_).

This decomposition provides a "coordinate system" for our recursive traceback: each node _I_ of R corresponds to a subproblem in which we care about paths whose internal vertices lie in the time window _I_.

## 4.2 Interval interfaces and local DPs

To evaluate the DP on a sub-interval _I_, we must formally define the input and output boundaries of the induced subgraph.

**Definition 6** (Restricted DAG and interfaces)**.** _Let I_=\[_i,j_\] _be an interval in_ R.

• _The_ restricted vertex set _is_ \(V_I=\{v\in V:v\in I\}\).<tbc>

• _The_ restricted edge set _is_ \(E_I=\{(u,v)\in E:u,v\in V_I\}\).<tbc>

• _The_ left interface _(or input boundary) is the set of vertices within I that depend on computations prior to i:_<tbc>

<tbc>\(F_I^\text{in}:=\{v\in V_I:\exists u<i\text{\textit{with}}(u,v)\in E\}.\)<tbc>

• _The_ right interface _(or output boundary) is the set of vertices within I that are needed by computations after j:_<tbc>

<tbc>\(F_I^\text{out}:=\{v\in V_I:\exists w>j\text{\textit{with}}(v,w)\in E\}.\)<tbc>

<tbc>It is important to distinguish the input interface (receivers) from the actual boundary (senders). The space required to restart the DP in _I_ is determined by the set of vertices _outside I_ that have edges into _I_. We define the _left boundary set_ as:

\(B_I:=\big\{u<i:\exists v\in V_I\text{with}(u,v)\in E\big\}.\)

By construction, \(B_I\subseteq\text{Front}(i-1)\) and \(F_I^\text{out}\subseteq\text{Front}(j)\), where the frontiers are defined with respect to the fixed topological order \(\tau\). In particular,

\(|B_I|\le\omega\text{and}|F_I^\text{out}|\le\omega.\)

Thus, every subproblem induced by an interval requires inputs from a set _B<sub>I</sub>_ of size at most \(\omega\), and produces outputs relevant for the future on a set of size at most \(\omega\).

We next formalize the fact that we can evaluate the DP within _I_ in a space bounded by \(\omega\), given boundary values on a small set of vertices before _i_.

**Lemma 3** (Local DP evaluation)**.** _Let I_=\[_i,j_\] _be an interval, and let_ \(U\subseteq V_I\) _be any target set. Suppose we are given the true global DP values_ \(\{x_u\}_{u\in B_I}\) _on the boundary set B<sub>I</sub>. Then the values_ \(\{x_v\}_{v\in U}\) _determined by the global recurrence (Assumption 2) can be recomputed using additional workspace_ \(O(\omega)\) _(in words)._

_Proof._ We describe a forward-pass algorithm A_<sub>I</sub>_ that recomputes the DP values for vertices in _I_, assuming the values on _B<sub>I</sub>_ are available.

Maintain a working buffer _M_ (the _active set_) intended to store the current active values within _I_ together with the fixed boundary values. We will ensure \(|M|\le\omega\) at all times.

1. Initialize _M_ to contain the pairs (_u,x<sub>u</sub>_) for all \(u\in B_I\).<tbc>

2. For _k_ increasing from _i_ to _j_:<tbc>

