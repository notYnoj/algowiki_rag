<tbc>_and space_<tbc>

\(O\big((U_0+U_1)\cdot n\big).\)

<tbc>_A randomized Las Vegas variant achieves an expected runtime of_

\(O\big((U_0+U_1)\cdot n\big)\)

_with the same space bound._

_Proof._ The solver enumerates \(\Sigma(\ell_0)\) and \(\Sigma(\ell_1)\) in an _interleaved_ fashion, matching candidates on the fly rather than tabulating both halves in full before merging.

Without loss of generality let \(U_0\ge U_1\) (so \(\ell_0\) is dominant). By the _suppression-on-overwrite_ invariant (§1), each canonical sum \(\sigma\in\Sigma(\ell_0)\) is generated and expanded exactly once; this _generation step_ is the atomic work unit.

For each canonical \(\sigma\) on \(\ell_0\):

• There are at most _O(n_) _successor attempts_ (adding an unset index in the canonical mask).<tbc>

• Each attempt performs _O_(1) same-half memo probes and _O_(1) cross-half probes (direct / complement / mixed; Appendix C).<tbc>

• If a same-half probe finds an existing representative for the same numeric sum, we perform a canonicality test between bitmasks. This costs _O(n_) in the deterministic model (lexicographic mask comparison), and _O_(1) in expectation in the randomized model (pairwise hashing to filter to a single lex-compare with constant probability).

When a collision leads to an overwrite (the new mask is lexicographically smaller), the previous representative is suppressed and never expanded; cross-half feasibility checks already performed for the displaced representative are not revisited. Thus every cross-half probe and every canonical comparison can be _injectively charged_ to the unique successor attempt that initiated it on the dominant side.

Pricing per attempt:

• Deterministic: _O_(1) probes + <u>at mostone</u> _O(n_) canonical comparison on collision \(\Rightarrow O(n)\) per attempt, hence \(O(U_0\cdot n^2)\) total.<tbc>

• Randomized: _O_(1) expected time per canonical check \(\Rightarrow O(1)\) per attempt, hence \(O(U_0\cdot n)\) expected total.<tbc>

<tbc>Therefore,

\(T(n)=O(max\{U_0,U_1\}\cdot n^2)(deterministic),\mathbb{E}[T(n)]=O(max\{U_0,U_1\}\cdot n)(randomized).\)

Since \(max\{U_0,U_1\}\le U_0+U_1\le 2max\{U_0,U_1\}\), this is asymptotically equivalent to the theorem’s \(O\big((U_0+U_1)\cdot n^2\big)\) and \(O\big((U_0+U_1)\cdot n\big)\) forms. We state the sum form to emphasize that both halves fully enumerate their unique sums, while the max form reflects the dominant-half accounting.

_Remark_ 2. The "dominant-half" view is often more intuitive: in heavily imbalanced instances (\(U_0\gg U_1\) or vice versa), the larger partial certificate drives the total cost. The sum form is preferable for theorem statements because it is conservative and avoids any suggestion that the non-dominant half is not fully enumerated.

