short elements. Let _U<sub>i</sub>_ be the cardinality of U_<sub>i</sub>_ ( _U<sub>i</sub>_=2_<sup>ij</sup>_). For every U_<sub>i</sub>_ do the following :

• Starting from the left, divide the set U_<sub>i</sub>_ into groups of size _B_.<tbc>

• Let _G<sub>ir</sub>_={_v_<sub>1</sub>_,...,v<sub>B</sub>_} be such a group of nodes (\(1\le r\le U_i/B\)). Let A_<sub>ir</sub>_ be the union of the search spaces of these nodes (union of the leaves of their subtrees).<tbc>

• Build the trees _T_(A_<sub>ir</sub>,_2_<sup>B</sup>,j_) for all groups _G<sub>ir</sub>_ above.

## Querying Phase

Here we describe how to perform the query search :

1. Divide the set of _k_ large elements into groups of _B_ long elements arbitrarily. For every group, bring it in memory and perform the search on _T(k,_2_<sup>B</sup>,j_) (sending every large element _j_ levels down the binary tree on _k_).<tbc>

2. If all large elements have been flushed at least _ij_ levels down (where \(1\le i\le g\)), for each group _G<sub>ir</sub>_ in U_<sub>i</sub>_, do the following :

• Find the set of large elements pointing to a node in _G<sub>ir</sub>_ (in other words, all large elements which have been found to belong to A_<sub>ir</sub>_, which, by definition, is the union of the search spaces of nodes in _G<sub>ir</sub>_). Let this set be Q, with _Q_ long elements. _Note that by the definition of the k-k problem (large and small elements perfectly interleaved), Q=A, i.e., there are as many large elements pointing to a node in G<sub>ir</sub> as the number of small elements/leaves in the subtrees rooted at nodes in G<sub>ir</sub>_.<tbc>

• Divide Q into groups of size _B_, bring each group into memory one at a time and flush it through _T_(A_<sub>ir</sub>,_2_<sup>B</sup>,j_).

**Lemma 20** (Complexity Analysis)**.** _The I/O complexity of the above algorithm is O_((_k_log_k)/B+kw/B_) _I/Os._

_Proof._ Each short block I/O gets a fan-out of 2_<sup>B</sup>_, as it halves the search space of _B_ large elements in memory. The total fan-out required is _k_!, so the number of short block I/Os is _O_((_k_log_k)/B_.

The large elements are swiped _g_ times (once after every _j_ levels). Each time costs _kw/B_ I/Os, requiring a total of \(O\left(kw\frac{logk}{loglog_{M/B}k}\right)\) I/Os (by definition of _g_), which is _O(kw/B_) since _k_ is sufficiently big to guarantee _Bw\<_loglog<sub>_M/B_</sub>_k_.

