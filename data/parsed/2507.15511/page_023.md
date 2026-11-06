**Algorithm 4** IsLexicographicallySmaller (1-indexed, 0_\<_1)

function IsLexicographicallySmaller(_A_, _B_) \(\triangleright A\), _B_ are _n_-bit masks<br>
   for i=1 to n do<br>
   \(a_i\leftarrow\) bit i of A; \(b_i\leftarrow\) bit i of B<br>
   if \(a_i\neq b_i\) then return (a<sub>i</sub>_\<b<sub>i</sub>_)<br>
   \(\triangleright\) prefer 0 at first difference<br>
   return false \(\triangleright\) equal masks

**Algorithm 5** SetBit (helper)

function SetBit(_M,i_)<br>
   return M with bit i set to 1

### A.2 Implementation Invariants

To guarantee correctness and performance, the enumerator maintains:

• **Deterministic tie-breaking.** For any numeric sum \(\sigma\), the lex-minimal bitmask (Algorithm 4) is the unique representative. This ensures global canonicity across columns.<tbc>

• **Efficient storage.** We store at most _U_ representatives, each as an _n_-bit mask, for total space \(O(U\cdot n)\).<tbc>

• **Duplication elimination.** A numeric sum may be _discovered_ multiple times, but its canonical representative is _expanded_ at most once. All non-canonical discoveries either lose the tie or overwrite and suppress the previous representative.<tbc>

• **Suppression on overwrite.** When a representative for \(\sigma\) is overwritten by a lex-smaller mask, the displaced state is marked _non-expandable_ (`doNotExtend`\(\leftarrow\)`true`) and, if queued, is optionally unscheduled. Consequently, each canonical sum is expanded exactly once over the entire enumeration.

## B Double-MIM Solver: Detailed Pseudocode and Analysis

### B.1 Algorithm Sketch

We split _S_={_a_<sub>1</sub>_,...,a<sub>n</sub>_} into two halves \(\ell_0\) and \(\ell_1\) (sizes within \(\pm 1\)) and run the unique-subset-sum enumerator on both sides _interleaved_. Each time a new canonical state is discovered on one half, we immediately invoke a constant-time family of membership tests on the other half (the Check or CheckAliased routines from §C) to detect solutions _online_. This avoids materializing \(\Sigma(S)\) in full.

When _Controlled Aliasing_ is enabled (Section 5.2; Appendix E), each half uses 2-lane memoization keyed by \((\tilde{\sigma},\chi)\) and enforces the count-based canonical normal form (CNF): only masks _b_ with

\(c(b):=b[i_0]+b[i_1]\in\{0,2\}\text{or}\big(c(b)=1\wedge b[i_1]=0\big)\)

are enqueued for expansion; non-canonical states are stored but marked `doNotExtend`. This yields the \(\frac{3}{4}\) expansion factor used in the worst-case bound.

