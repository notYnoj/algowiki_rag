## 5.6 The recursive procedure

We summarize the above reasoning into a recursive algorithm. Fix a base-case threshold \(B_\mathrm{base}=\lceil(\mathrm{log}T)^c\rceil\) for a constant \(c\ge 1\), and write polylog_T_ for (log_T_)<sup>_O_(1)</sup>.

**Algorithm 1** Universal Hirschberg Traceback (high-level)

1: Compute _x<sub>t</sub>_ by a forward DP sweep over _G_ using \(O(\omega)\) space.

2: Call Traceback(\[1_,T_\]_,S_src_,t,x<sub>t</sub>_).

**Procedure** Traceback(_I_=\[_i,j_\]_,B_left_,s,_val):

1. **Base case:** If \(|I|\le B_\mathrm{base}\), perform a local DP restricted to _I_:<tbc>

• treat _B_left as a boundary with fixed values \(\{x_u\}_{u\in B_\mathrm{left}}\);<tbc>

• run a forward DP on the induced subgraph of vertices in _I_, recomputing _x<sub>v</sub>_ and recording the predecessor pred(_v_) for all \(v\in I\) (using the local edge tie-breaking \(\prec\));<tbc>

• backtrack along \(\mathsf{pred}(\cdot)\) from _s_ until the predecessor lies in _B_left (or equals \(\perp\)), outputting the corresponding path segment from left to right.

This uses \(O(\omega+B_\mathrm{base})\) space (in words) by Lemma 3 and the bounded size of _I_.

2. **Recursive step:** If |_I|\>B_<sub>base</sub>:

(a) Let _m=m(I_).<tbc>

(b) **If** \(s\le m\)**:** then all vertices on any path from _B_left to _s_ lie in \[_i,m_\] by monotonicity of \(\tau\). Recurse on the left child:<tbc>

<tbc>Traceback(\[_i,m_\]_,B_left_,s,_val).<tbc>

(c) **If** _s\>m_**:**<tbc>

i. Form the middle frontier \(F_I^\mathrm{mid}\).<tbc>

ii. Using Lemma 3, compute _f(v_) for all \(v\in F_I^\mathrm{mid}\) via a single forward DP on \[_i,m_\] with boundary _B_left.<tbc>

iii. For each \(v\in F_I^\mathrm{mid}\), compute _g(v_) by a forward DP on \[_v,j_\] with boundary {_v_} as described above.<tbc>

iv. Let _v<sup>⋆</sup>_ be the canonical maximizer of \(f(v)\otimes g(v)\) over \(v\in F_I^\mathrm{mid}\).<tbc>

v. Recursively call<tbc>

<tbc>Traceback(\[_i,m_\]_,B_left_,v<sup>⋆</sup>,f(v<sup>⋆</sup>_)),<tbc>

<tbc>and output the resulting path segment.<tbc>

vi. Then call<tbc>

<tbc>Traceback(\[_m_+1_,j_\],{_v<sup>⋆</sup>},s,g(v<sup>⋆</sup>_)),<tbc>

<tbc>and output the resulting path segment, concatenating them.

The recursion terminates because each call either reduces the interval length by at least one (in the case \(s\le m\)) or splits _I_ into two strictly smaller subintervals (in the case _s\>m_), and we stop once \(|I|\le B_\mathrm{base}\).

## 5.7 Space analysis

We now bound the work-tape space used by Algorithm 1.

**Theorem 2** (Space complexity)**.** _Under Assumptions 1 and 2, the Universal Hirschberg algorithm computes a canonical optimal witness path to t using space_

\(\mathsf{SPACE}_\mathrm{traceback}=O(\omega\mathrm{log}T+\mathrm{polylog}T),\)

_measured in tape cells over a fixed finite alphabet._

_Proof._ The space usage consists of two components: (i) DP evaluation workspace and (ii) recursion stack.

