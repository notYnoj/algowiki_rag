<tbc>only this canonical representation when multiple extensions lead to the same sum, we suppress redundant work and ensure each unique sum is discovered via a single, well-defined path.

### Bitmask Representation.

The algorithm represents each prefix by a bitmask of length _n_, where the _i_-th bit indicates whether _a<sub>i</sub>_ is included. Bitmask comparison to determine the lex-minimum takes _O(n_) time. The total number of unique sums is _U_, so we store at most _U_ bitmasks.

### Separation of concerns.

Conceptually, the enumerator factors into three orthogonal pieces: (i) _enumeration_ (systematically proposing extensions), (ii) _canonicality tests_ (lexicographic comparisons to select representatives), and (iii) _memoization_ (storing one representative per numeric sum). Invariant 1 links (ii) and (i), ensuring that only the current representative ever generates successors.

_Theorem_ 1 (Deterministic Runtime of the Enumerator). _Under the computational model of Section 3, the deterministic enumerator computes all_ \(U=|\Sigma(S)|\) _unique subset sums in_ \(O(U\cdot n^2)\) _time and_ \(O(U\cdot n)\) _space._

_Proof._ The runtime is dominated by the prefix extension and deduplication process. From each of the _U_ states, the algorithm attempts to extend its prefix with at most _n_ elements, resulting in \(O(U\cdot n)\) extension attempts. In the event of a sum collision, the algorithm must compare the existing and candidate _n_-bitmasks to select the canonical representative, costing _O(n_) time. Invariant 1 ensures that an overwritten representative is never expanded further. Multiplying \(O(U\cdot n)\) extension attempts by _O(n_) comparison cost gives the stated \(O(U\cdot n^2)\) runtime bound; space is \(O(U\cdot n)\) for storing all canonical bitmasks.

_Remark_ 1 (Degenerate Cases). The \(O(U\cdot n^2)\) bound in Theorem 1 is a worst-case guarantee. For instances with very low structural complexity (e.g., _U_=1 for an empty set, or _U=O(n_) for a set of identical elements), this bound correctly implies a fast, polynomial runtime.

_Theorem_ 2 (Randomized Runtime of the Enumerator). _Let_ \(U=|\Sigma(S)|\)_. Assume access to a_ 2_- universal hash family_ H _with O_(1) _evaluation time. Then a randomized variant of the enumerator computes all U unique subset sums in expected time_ \(O(U\cdot n)\)_, where the expectation is over the random draw of h_∼H _as specified in Section 3._

_Proof._ Assume the randomized model of Section 3. With _h_ drawn uniformly from a 2-universal family, the probability that two distinct bitmasks yield the same hash is at most 1/poly(_n,U_). Consequently, the full _O(n_) lexicographic comparison is needed only on (rare) hash-collision events, giving an expected _O_(1) time per canonicality check (Las Vegas correctness). Since there are \(O(U\cdot n)\) extension attempts (Theorem 1), this yields the stated expected runtime bound.

## 4.2 Discussion and Conditional Optimality

### A Local Deduplicating Enumeration Model.

We define a natural model of computation that captures the core constraints of real-time certificate construction. The _local deduplicating enumeration model_ assumes that the algorithm:

• maintains a growing set _P_ of seen prefixes, each encoding a valid subset sum and its associated path;<tbc>

• in each round, selects a candidate prefix \(p\in P\) and a next element _a<sub>i</sub>_ to extend it with;<tbc>

• uses local information about _p_ and _a<sub>i</sub>_ to decide whether to emit the new sum or prune it.<tbc>

