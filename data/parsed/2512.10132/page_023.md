## A Detailed Algorithmic Procedures

This appendix provides pseudocode for the Universal Hirschberg algorithm described in the main text. We strive to present each major procedure in sufficient detail for implementation, using notation consistent with Sections 2-5.

**Algorithmic components.** The appendix is organized around the following procedures:

1. **Algorithm 2**: Universal Hirschberg main driver.<tbc>

2. **Algorithm 3**: Global forward DP to compute _x<sub>t</sub>_ using a rolling frontier.<tbc>

3. **Algorithm 4**: Recursive traceback on intervals _I_=\[_i,j_\].<tbc>

4. **Algorithm 5**: Computation of the middle frontier \(F_I^\mathrm{mid}\).<tbc>

5. **Algorithm 6**: Forward-only computation of prefix values _f(v_) on \[_i,m(I_)\].<tbc>

6. **Algorithm 7**: Forward-only computation of suffix values _g(v_) on _I_.<tbc>

7. **Algorithm 8**: Canonical midpoint selection from \(F_I^\mathrm{mid}\).<tbc>

8. **Algorithm 9**: Base-case DP and direct traceback on short intervals.

Throughout:

• \(G=(V,E,S_\mathrm{src},T_\mathrm{sink},\tau)\) denotes the input DP DAG with |_V_|=_T_ vertices in topological order.<tbc>

• \(\oplus\) and \(\otimes\) denote the semiring operations (supremum and multiplication).<tbc>

• \(\omega\) denotes the frontier width \(\omega(G)\).<tbc>

• For an interval _I_=\[_i,j_\], we write \(m(I)=\lfloor(i+j)/2\rfloor\) for its midpoint.<tbc>

• \(\prec\) denotes the fixed total order on edges _E_ used for deterministic tie-breaking.<tbc>

• Space complexities are generally stated in machine words (each word is _O_(log_T_) bits); time complexities count primitive operations.

In recursive subproblems, we work with a _local_ DP induced by a boundary. Each traceback subproblem carries:

• a boundary set _B_<sub>left</sub> of vertices that may serve as sources for this subproblem, and<tbc>

• a map \(\beta_\mathrm{left}:B_\mathrm{left}\rightarrow\mathcal{S}\) giving the DP value at each boundary vertex for this _subproblem_ (with respect to the same recurrence as globally, but restricted to paths starting in _B_<sub>left</sub> and staying inside the current interval thereafter).

All local forward DPs below are understood to use these boundary values as their initial conditions.

We assume standard data structures (dictionaries, sets, lists) with _O_(1) access in the RAM model, and that the input graph _G_ supports:

• predecessors(_v_) returning \(\{u:(u,v)\in E\}\) in time _O_(deg<sup>-</sup>(_v_)),<tbc>

• successors(_v_) returning \(\{w:(v,w)\in E\}\) in time _O_(deg<sup>+</sup>(_v_)),<tbc>

• edge weights _w<sub>u,v</sub>_ accessible in _O_(1) time.

**Algorithm correctness and space complexity.**

**Theorem 3** (Correctness and Space Complexity)**.** _Under Assumptions 1 and 2 from the main text, Algorithm 2 correctly computes a canonical optimal witness path from a source in S_<sub>src</sub> _to the target sink t, and uses work-tape space_

\(\mathsf{SPACE}_\mathrm{traceback}=O(\omega\mathrm{log}T+\mathrm{polylog}T)\)

_cells over a fixed finite alphabet._

