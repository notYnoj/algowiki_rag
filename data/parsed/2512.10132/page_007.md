## 3.2 Hirschberg’s algorithm: a structural view

Hirschberg’s algorithm circumvents the quadratic traceback space requirement by exploiting the product structure of the grid and the reversibility of the recurrence. We rephrase its logic as a recursive identification of optimal-path crossings through a balanced separator in the topological order. This makes the structural pattern more visible and prepares the ground for generalization.

For simplicity, assume \(m\le n\) and use a column-major order so that the frontier width is \(\omega=\Theta(m)\). The algorithm proceeds as follows:

1. **Midpoint selection.** Fix a column index \(k=\lfloor n/2\rfloor\). This defines a vertical cut through the grid, separating the problem into a _left_ half (columns 0_,...,k_) and a _right_ half (columns _k,...,n_). In terms of the topological order, this is a balanced cut of the time axis.<tbc>

2. **Forward valuation.** Compute, using space _O(m_) words, the optimal value<tbc>

<tbc>\(f(i)=\text{optimal score of a path from}(0,0)\text{to}(i,k)\)<tbc>

<tbc>for all \(0\le i\le m\), via a standard forward DP restricted to columns 0_,...,k_.<tbc>

3. **Backward valuation.** Compute, again using _O(m_) words, the optimal value<tbc>

<tbc>\(g(i)=\text{optimal score of a path from}(i,k)\text{to}(m,n)\)<tbc>

<tbc>for all \(0\le i\le m\). This step relies on the symmetry of the grid: the backward problem is isomorphic to a forward DP on the reversed strings _A_<sup>rev</sup>, _B_<sup>rev</sup> over a grid of the same width _m_, with the same frontier width \(\Theta(m)\) under the reversed topological order.<tbc>

4. **Crossing identification.** By the principle of optimality, any optimal path from (0,0) to (_m,n_) must cross the column _k_. Thus there exists some row _i<sup>⋆</sup>_ such that the vertex (_i<sup>⋆</sup>,k_) lies on an optimal path. Moreover,<tbc>

<tbc>\(i^\star=argmax_{0\le i\le m}\big(f(i)+g(i)\big),\)<tbc>

<tbc>and (_i<sup>⋆</sup>,k_) is a canonical midpoint vertex on an optimal witness path when the same deterministic tie-breaking rule is used in both the forward and backward DPs.<tbc>

5. **Recursion.** The problem decomposes into two independent subproblems:<tbc>

• an LCS (or alignment) problem from (0,0) to (_i<sup>⋆</sup>,k_) on the left subgrid, and<tbc>

• an LCS problem from (_i<sup>⋆</sup>,k_) to (_m,n_) on the right subgrid.<tbc>

The algorithm recurses on these two subproblems, accumulating the witness path segments.

### Space complexity.

Let _S(m,n_) denote the work-tape space required (in machine words) to reconstruct an alignment via Hirschberg, in the machine model of Section 2 where the input strings _A_ and _B_ reside on a read-only input tape. At each recursive call, the algorithm maintains two line buffers of length \(\Theta(m)\) for the forward and backward passes, plus a constant amount of metadata (including the current column index and recursion state) on the recursion stack. The recursion depth is _O_(log_n_), and the additional per-level metadata is _O_(1) words. Thus we obtain the recurrence<tbc>

\(S(m,n)\le max\{S(m,\lfloor n/2\rfloor),O(m)\}+O(1),\)

<tbc>which solves to

\(S(m,n)=O(m+logn).\)

In particular, the traceback workspace is linear in the shorter dimension _m_, plus a logarithmic term for the recursion depth, representing a substantial improvement over the naive \(\Theta(mn)\) pointer-storage scheme in regimes where \(m\checkmark n\). Translating to tape cells using our encoding assumptions, this corresponds to \(O\big((m+logn)log(mn)\big)\) cells.

