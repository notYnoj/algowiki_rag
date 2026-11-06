## 8 Related Work

We briefly survey connections to prior work on space-efficient dynamic programming, checkpointing and adjoint computation, and time-space tradeoffs in complexity theory and graph algorithms.

### Space-efficient sequence DP and Hirschberg-type schemes.

Hirschberg’s algorithm [1] is the classical archetype for space-efficient sequence alignment and LCS. It shows that, on an \(m\times n\) edit graph, one can reconstruct an optimal alignment in _O(m+n_) words of space instead of _O(mn_) by recursively bisecting along the longer dimension and combining forward and backward DP values at a midpoint column. Numerous refinements and variants exist in the string algorithms and computational biology literature, including Myers’ _O(ND_) difference algorithm and banded alignment schemes that trade time and bandwidth for memory in practical aligners.

These algorithms, however, are typically tightly coupled to the 2D geometry and symmetry of the grid and its reverse: both the forward and backward DPs live on the same state space and have the same width. Our contribution can be viewed as lifting the underlying control-flow pattern--balanced bisection plus meet-in-the-middle valuation--from this specific geometry to arbitrary time-ordered DAGs with bounded frontier width, and showing that backward traversal can be replaced by forward-only re-computation without asymptotic space loss in the offline random-access model. In particular, the max-type semiring and deterministic witness structure are sufficient to recover a canonical optimal path in \(O(\omega logT+polylogT)\) bits of space, even when the reverse graph has much larger frontier width.

### Adjoint computation, automatic differentiation, and checkpointing.

In reverse-mode automatic differentiation (AD), gradients are propagated backward through a computation graph whose forward execution may involve millions (or billions) of intermediate states. Storing all intermediate values yields optimal time but maximal memory usage; checkpointing schemes such as Griewank and Walther’s Revolve algorithm [3] carefully trade recomputation for space by storing a small number of snapshots and replaying segments between them. These methods are analyzed in terms of schedules that minimize either the number of recomputations or the peak memory, subject to a given forward execution trace.

Our height-compressed recursion can be interpreted as a particular checkpointing strategy for witness reconstruction: we store only a logarithmic number of recursion frames plus a single frontier buffer of size \(O(\omega)\), and we willingly pay polynomial re-computation costs. Conceptually, the recursion tree plays the role of an explicit checkpoint schedule adapted to the topological order. The emphasis is different from most AD work--we prioritize _space_ over recomputation counts, and we restrict to max-type recurrences with deterministic witnesses rather than general differentiable programs--but the structural parallels suggest that ideas from our setting may be transferrable to adjoint computation on structured DAGs, especially when memory is the primary bottleneck and random access to the computation graph is available.

### Time-space tradeoffs and pebbling games.

The study of time-space tradeoffs for Turing machines and circuits has a rich history. The pebbling game on DAGs (e.g. Paul, Pippenger, Szemerédi, and Trotter [2]) provides a combinatorial abstraction in which one places and removes pebbles on vertices under rules that mimic space-bounded computation. Pebbling numbers and reversible pebbling sequences translate into lower and upper bounds on time and space for evaluating the DAG, and have been used to show that certain computations require nontrivial time-space products.

Our construction effectively gives a concrete pebbling strategy for the _traceback_ problem on DP DAGs in the random-access model: we use \(O(\omega)\) "value pebbles" to represent the current frontier and an additional _O_(polylog_T_) control pebbles to navigate the recursion tree. The ability to jump to arbitrary vertices and recompute local DPs means that we never need to maintain more than one frontier at a time. In contrast, classic results on multitape Turing machines (and related streaming models) show that, without random access, simulating a length-_t_ computation may require \(\Theta(\sqrt{t})\) space, reflecting the cost of replaying long segments of the input tape. The contrast highlights how access patterns and model constraints (streaming vs. random access, single-pass vs. multi-pass) fundamentally alter the achievable time-space tradeoffs even on the same underlying DAG.

### Width parameters: treewidth, pathwidth, and DP formulations.

In parameterized complexity, treewidth and pathwidth play a central role in designing fixed-parameter tractable algorithms for NP- hard problems. Bodlaender’s survey [4] and subsequent work show that many problems become tractable<tbc>

