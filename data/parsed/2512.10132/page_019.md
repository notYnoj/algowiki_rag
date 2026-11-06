must either buffer parts of the stream or maintain checkpointed summaries, reintroducing a dependence on _T_ reminiscent of time-space tradeoffs for Turing machines.

Motivated by this analogy, we formulate the following conjecture.

**Conjecture 1** (Streaming traceback barrier)**.** _There exist absolute constants_ \(c,c'>0\) _such that the following holds. For every sufficiently large T, there is a family of DP DAGs on T vertices with frontier width_

\(\omega(T)=O\big((logT)^{c^\prime}\big)\)

_for which any single-pass streaming algorithm that outputs an optimal witness path with success probability at least_ 2/3 _(over its internal randomness) must use space at least_ \(c\sqrt{T}\) _bits._

The conjecture is inspired by the "progress ledger" and checkpointing constructions used for deterministic multitape Turing machines, where one shows inclusions of the form

\(\mathsf{TIME}[t]\subseteq\mathsf{SPACE}\big(\widetilde{O}(\sqrt{t})\big)\)

by organizing the computation into blocks of size _b_, storing _O(t/b_) block summaries, and balancing _b_ against _t/b_. In that setting, the \(\sqrt{t}\) term arises from the inability to jump back to earlier tape cells without replaying the stream.

Our offline algorithm exploits precisely the opposite situation: re-computation is "cheap" in space because random access lets us restart a forward DP from any desired vertex and time index. As a result, the recursion overhead collapses from \(O(\sqrt{T})\) in the Turing-machine model to _O_(polylog_T_) here. If Conjecture 1 holds, it would formalize the intuition that \(\sqrt{T}\)-type terms are not intrinsic to traceback itself, but rather to streaming-like constraints on how the DP DAG is accessed, and that substantial additional space may be needed in streaming even when frontier width is polylogarithmic.

## 7.3 Thin graphs and absence of universal _T_-carriers

It is equally important to understand when large values of _T do not_ force large traceback space. Lower bounds such as \(\Omega(\sqrt{T})\) or \(\Omega(\omega)\) are statements about _graph families_, not bare functions of _T_.

Consider the "thin" DAG that is just a directed path:

\(V=\{1,\dots,T\},E=\{(i,i+1):1\le i<T\}.\)

Here the frontier width is \(\omega=1\), independently of _T_.

• The unique witness path is the entire chain \(1\rightarrow 2\rightarrow\cdots\rightarrow T\), regardless of the specific max-type weights on the edges (assuming no edges are deleted and ties are broken deterministically).<tbc>

• A trivial algorithm can output this path using _O_(log_T_) bits of space to store a counter that walks along the chain; indeed, _O_(log_T_) bits are necessary just to index the vertices in binary, so this is optimal up to constant factors.

Thus no lower bound of the form \(\Omega(T^\alpha)\) for any fixed \(\alpha>0\) can hold uniformly over all DAGs of size _T_. Structural parameters such as frontier width, pathwidth, or treewidth are indispensable to capture the true space complexity of traceback.

Our upper bound

\(S(T,\omega)=O\big(\omega logT+polylogT\big)\text{bits}\)

respects this structural picture:

• For lines and more generally constant-width chains, \(\omega=O(1)\) and _S=O_(polylog_T_).<tbc>

• For \(N\times N\) grid-like families, \(T=\Theta(N^2)\) and \(\omega=\Theta(N)=\Theta(\sqrt{T})\), so \(S=\Theta(\sqrt{T})\) up to lower-order polylogarithmic factors.

This matches the intuition that traceback space depends primarily on the width of the DP frontiers, not on the sheer number of states, except for mild logarithmic indexing overhead.

Overall, Theorem 2, Proposition 2, and the examples in Section 6 suggest the following picture: in the offline random-access model, the right first-order parameter governing traceback space is frontier width, and the Universal Hirschberg algorithm is essentially optimal with respect to this parameter. The precise role of the polylog_T_ overhead, and the extent to which it can be reduced or shown necessary under natural assumptions, remains an open direction.

