_DP workspace._ Every forward DP pass (global valuation, prefix computation for _f(v_), suffix computations for _g(v_), and base-case local tables) uses at most \(O(\omega)\) words to store a frontier and a constant amount of local metadata (indices, loop counters). These passes do not run concurrently: at any moment, at most one forward DP is active. Since one word corresponds to _O_(log_T_) tape cells, the total DP workspace is \(O(\omega logT)\) cells.

_Recursion stack._ The recursion tree has depth _O_(log_T_) by Lemma 2, and the additional "\(s\le m\)" branch cannot increase this depth asymptotically because it simply discards the right half without further branching. Each stack frame stores:

• the interval endpoints _i,j_ (requiring _O_(log_T_) bits),<tbc>

• the sink index _s_ (another _O_(log_T_) bits),<tbc>

• the target value val (whose representation we assume to be _O_(polylog_T_) bits under standard encodings of weights in the semiring S),<tbc>

• a constant number of control flags (e.g. whether we are in the \(s\le m\) or _s\>m_ case, which child is active, where to resume).

We do _not_ store the entire set _B_<sub>left</sub> explicitly at each level: for the right child, _B_<sub>left</sub> is always a singleton {_v<sup>⋆</sup>_} with its value _g(v<sup>⋆</sup>_), and for the left child, _B_<sub>left</sub> coincides with that of the parent and can be recovered from the parent frame. In either case, the additional metadata per frame is _O_(polylog_T_) bits.

Multiplying by the recursion depth, the total stack space is \(O(logT\cdot polylogT)=O(polylogT)\) bits.

Combining the two contributions yields the stated bound \(O(\omega logT+polylogT)\) cells.

**Remark 1** (Time complexity)**.** _The algorithm may perform multiple forward DP passes per recursion level when s\>m(I_) _(one for_ \(f(\cdot)\) _and up to_ \(|F_I^\mathrm{mid}|\le\omega\) _for the various_ \(g(\cdot)\)_). In the worst case, summing over all recursion levels yields total time_

\(T_\mathrm{total}=T\cdot\mathsf{poly}(\omega,logT),\)

_for constant_ \(\Delta_\mathrm{max}\)_. We do not optimize time here: our focus is on space. In settings where the reversed graph G<sup>R</sup> also has frontier width_ \(O(\omega)\)_, one can replace the per-candidate forward suffix passes by a single backward DP, recovering Hirschberg-like O(T_) _time while preserving the space bound._

## 6 Applications

Theorem 2 gives a structural upper bound on traceback space in terms of the frontier width \(\omega\) and the number of states _T_. We now instantiate this result for several standard DP families, recovering known bounds as special cases and obtaining new guarantees in asymmetric and constrained regimes.

Throughout this section, we work in the machine model of Section 2. We assume that:

• weights and DP values admit an encoding using _O_(log_T_) tape cells (one machine word);<tbc>

• primitive semiring operations and comparisons run in time and space polynomial in log_T_;<tbc>

• the DP recurrences fit the max-type semiring framework of Assumption 2 with deterministic tie- breaking, so that the canonical predecessor map `pred` is well-defined.

As in Theorem 2, we write polylog_T_ as shorthand for (log_T_)<sup>_O_(1)</sup> (base 2 unless stated otherwise).

### 6.1 Asymmetric sequence alignment

Let \(\Sigma\) be a finite alphabet. Given strings \(A\in\Sigma^m\) and \(B\in\Sigma^n\) with \(m\le n\), the global alignment problem (including edit distance, Needleman–Wunsch, or affine-gap variants) is naturally formulated as a DP on the grid DAG _G<sub>m,n</sub>_ described in Section 3.

Recall:

• \(T=|V|=(m+1)(n+1)=\Theta(mn)\);<tbc>

• under a column-major or row-major topological order, the frontier width satisfies<tbc>

<tbc>\(\omega(G_{m,n})=\Theta(\mathrm{min}\{m,n\})=\Theta(m)\text{when}m\le n;\)<tbc>

