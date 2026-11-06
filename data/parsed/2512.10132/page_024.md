**Algorithm 2** Universal Hirschberg: Main Algorithm

**Input:** DP DAG \(G=(V,E,S_\text{src},T_\text{sink},\tau)\), target sink \(t\in T_\text{sink}\)<br>
**Output:** Canonical optimal witness path P from a source to t<br>
1: \(\triangleright\) Phase 1: Compute optimal global value at sink t<br>
   \(x_t\leftarrow\text{GlobalForwardDP}(G,t)\)<br>
   \(\triangleright\) Phase 2: Set up root subproblem<br>
   \(I\leftarrow[1,T]\)<br>
   \(B_\text{left}\leftarrow S_\text{src}\)<br>
   \(\beta_\text{left}\leftarrow\emptyset\)<br>
    for each \(u\in B_\text{left}\leftarrow\)<br>
   to do\(\beta_\text{left}[u]\leftarrow a_u\triangleright\) Source initialization values<br>
   end for<br>
   \(s\leftarrow t\)<br>
   \(\text{val}\leftarrow x_t\)<br>
   \(\triangleright\) Recursive traceback<br>
   \(P\leftarrow\text{RecursiveTraceback}(G,I,B_\text{left},\beta_\text{left},s,\text{val})\)<br>
   return P<br>
   \(\text{\textbf{Space:}}O(\omega+\text{polylog}T)\text{words \textbf{Time:} poly(}T)\)

_Proof sketch._ Correctness follows from the invariant maintained throughout the recursion (Lemma 4), which ensures that at each recursive call \((I,B_\text{left},\beta_\text{left},s,\text{val})\):

1. There exists at least one optimal witness path P from Bleft to s whose internal vertices all lie in I and whose semiring value is val with respect to the local DP induced by \((B_\text{left},\beta_\text{left})\).<tbc>

2. The canonical midpoint v<sup>⋆</sup> selected by Algorithm 8 lies on at least one such optimal path P<sup>⋆</sup>.

The tie-breaking logic is hierarchical:

• At internal nodes (|I|_\>B_base), Algorithm 8 resolves ties between candidate vertices in \(F_I^\text{mid}\) using a deterministic order (e.g., smallest index), ensuring a unique choice of v<sup>⋆</sup>.<tbc>

• At base-case nodes (\(|I|\le B_\text{base}\)), Algorithm 9 resolves ties between incoming edges using the fixed global edge order \(\prec\).

This combination defines a unique canonical witness path. The properties are preserved inductively by the crossing and decomposition arguments in Lemma 5 and Proposition 1, together with the monotonicity of the max-type semiring and consistent use of the same recurrence in all local DPs.

For space complexity:

• **DP workspace:** All forward DP passes (Algorithms 3, 6, 7, 9) maintain a frontier buffer of size at most \(\omega\) by Lemma 3 and the definition of frontier width in Section 2. These buffers are reused across passes, contributing \(O(\omega)\) words of space, i.e., \(O(\omega logT)\) tape cells.<tbc>

• **Recursion stack:** The recursion tree has depth O(logT) by Lemma 2. Each stack frame stores interval endpoints, vertex indices, the scalar val, and a succinct encoding of the boundary set Bleft and its value map \(\beta_\text{left}\) (for right children, Bleft is always a singleton {v<sup>⋆</sup>} with value \(\mathbf{1}_\otimes\); for left children, Bleft and \(\beta_\text{left}\) are inherited from the parent). Each of these pieces requires O(polylogT) bits under standard encodings for S. Total stack space is \(O(logT\cdot polylogT)=O(polylogT)\) bits.

Combining these contributions yields the stated bound \(O(\omega logT+polylogT)\) cells.

**Remark 2** (Time complexity)**.** _The time complexity is dominated by the suffix value computations (Algorithm 7), which perform_ \(|F_I^\text{mid}|\le\omega\) _forward DP passes per recursion level when s\>m(I). Summing_<tbc>

