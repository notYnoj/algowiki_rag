### IC-SUBSETSUM as a Certifier.

As discussed above, the raw certificate \(\Sigma(S)\) must be paired with an input-checking wrapper to form a canonical IC program. What distinguishes IC-SubsetSum is that it does not merely verify membership in \(\Sigma(S)\); it constructs the entire certificate from scratch. Our deterministic algorithm achieves this in \(O(U\cdot n^2)\) worst-case time, while our randomized variant does so in \(O(U\cdot n)\) expected time.

### Implication.

This gives new meaning to our certificate-sensitive runtime. It says not just that the algorithm is efficient, but that it implicitly performs instance-specific program synthesis. The certificate \(\Sigma(S)\) serves as a compressed, self-contained representation of the computation needed to decide (_S,t_), and IC-SubsetSum acts as a just-in-time compiler for that program--whose runtime tracks its size.

While Instance Complexity is classically defined in a _non-uniform_ setting--allowing a different short program for each instance--IC-SubsetSum provides a _uniform_, deterministic algorithm that adapts to the structure of each input, synthesizing the decision procedure on the fly and thus resolving the long-standing tension between the theoretical power of IC and its historically non-constructive formulation.

## 5 Solver with a Sub-2<sup>_n/_2</sup> Worst-Case Bound

### 5.1 Double Meet-in-the-Middle Solver

We now describe how to solve Subset-Sum given only the enumerators for \(\Sigma(S)\). The detailed pseudocode for the full solver is presented in Appendix B.

### Clarifying Certificate Scope.

While the unique-subset-sum enumerator described above can be applied to the full input _S_ to construct the complete certificate \(\Sigma(S)\) in time \(O(U\cdot n^2)\), our solver employs a more efficient strategy. It splits _S_ into halves \(\ell_0\) and \(\ell_1\) and applies the enumerator separately to each side, yielding certificates \(\Sigma(\ell_0)\) and \(\Sigma(\ell_1)\). This avoids ever constructing \(\Sigma(S)\) explicitly. The solver answers the query \(t\in\Sigma(S)\) by testing cross-split combinations on the fly. It trades away post hoc queryability: to check a new target \(t'\), the merge logic must be repeated. Throughout the paper, we use \(U=|\Sigma(S)|\) as a global proxy for instance complexity, but emphasize that our solver’s runtime depends operationally on _U_<sub>0</sub> and _U_<sub>1</sub>.

### Splitting the instance.

Let \(S=\ell_0\cup\ell_1\) be a partition into left and right halves. We enumerate \(\Sigma(\ell_0)\) and \(\Sigma(\ell_1)\) using the prefix-unique method described above. Let \(U_0=|\Sigma(\ell_0)|\) and \(U_1=|\Sigma(\ell_1)|\). Note that the additive structure within each half can lead to a significant imbalance (e.g., \(U_0\checkmark U_1\)), though this does not affect the overall asymptotic bound.

### Solving and certifying.

To decide whether any subset of _S_ sums to _t_, we check for each sum \(x\in\Sigma(\ell_0)\) whether a corresponding match can be found in \(\Sigma(\ell_1)\). This check is more comprehensive than a simple search for _t-x_, as it also considers complements and mixed cases to cover all solution structures, as detailed in the lemmas of Appendix C. To certify all solutions, we can track all such valid (_x,y_) pairs and output their associated bitmasks.

_Theorem_ 4 (Certificate-Sensitive Solver)_. Let S be split into two halves_ \(\ell_0\) _and_ \(\ell_1\) _of sizes_ \(\lfloor n/2\rfloor\) _and_ \(\lceil n/2\rceil\)_, and let_ \(U_0=|\Sigma(\ell_0)|\) _and_ \(U_1=|\Sigma(\ell_1)|\) _denote the number of distinct subset sums in each half. There exists a deterministic algorithm that solves_ Subset-Sum _in time_<tbc>

\(O\big((U_0+U_1)\cdot n^2\big)\)

