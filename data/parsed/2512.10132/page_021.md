on graphs of bounded treewidth via DP over tree or path decompositions, and that the _width_ of the decomposition directly governs the memory required to store DP tables.

Our frontier width \(\omega\) is essentially a pathwidth-like parameter aligned with a particular topological order. Corollary 4 makes this connection explicit: once a problem admits a bounded-width DP formulation in our sense, the additional space needed to reconstruct a witness beyond computing the DP values is only polylogarithmic in _T_. In that sense, the "price of reconstruction" is negligible for all width-bounded formulations, complementing the existing literature that focuses primarily on decision versions. An interesting direction, discussed in Section 9, is to understand how far this picture extends to other structural width measures (e.g. treewidth, clique-width, or DAG-width) and to what extent frontier width can be minimized by choosing an appropriate topological order.

## 9 Open Problems

The Universal Hirschberg framework resolves the deterministic offline case for max-type DP recurrences on DAGs with bounded frontier width, up to polylogarithmic slack in _T_, in the random-access model of Section 2. Several directions remain open for sharpening, extending, or qualitatively changing the picture.

1. **Beyond max-type semirings and into counting.** Our algorithm heavily exploits max-type structure and deterministic tie-breaking to obtain a _single_ canonical witness. For counting DPs over \((\mathbb{N},+,\times)\), we often want either the number of optimal witnesses or a random witness drawn from an appropriate distribution (e.g. the Boltzmann distribution). One natural question is:<tbc>

<tbc>Can we design \(O(\omega logT+polylogT)\)-space algorithms that (approximately) count witnesses, or that sample witnesses from a specified distribution, for counting DPs on width- bounded DAGs?<tbc>

<tbc>Even for grid-based alignment problems, space-efficient sampling algorithms that match the evaluation- space bounds are not known in general; understanding the right structural conditions for counting and sampling in near-frontier space remains largely open.<tbc>

2. **Refined structural parameters and tighter overhead.** Our polylog_T_ overhead comes from a generic balanced binary recursion and from storing DP values and indices in a standard bit model. For more structured graph families (e.g. planar DAGs, series-parallel graphs, leveled networks), it is plausible that one can exploit specialized decompositions or canonical embeddings to reduce recursion depth or share information across levels. This raises:<tbc>

<tbc>Are there natural graph classes where traceback can be done in space \(O(\omega logT+logT)\), or even \(O(\omega logT)\), in the worst case?<tbc>

<tbc>Conversely, can one prove unconditional lower bounds showing that an additive \(\Omega(logT)\) term is necessary for certain families, even when \(\omega=O(1)\)? For instance, can one exhibit bounded-width DAGs on which any algorithm must store \(\Omega(logT)\) bits of index information to output a witness, beyond the trivial \(\Omega(logT)\) needed to address vertices in binary?<tbc>

3. **Streaming vs. offline: closing the** \(\sqrt{T}\) **gap.** Conjecture 1 posits an \(\Omega(\sqrt{T})\) barrier for single- pass streaming algorithms on certain DAG families whose frontier width is only polylogarithmic in _T_. At the same time, our offline algorithm shows that with random access the space can be reduced to \(O(\omega(T)logT+polylogT)\), which is \(\widetilde{O}(1)\) for those families and \(\widetilde{O}(\sqrt{T})\) for grid-like families with \(\omega=\Theta(\sqrt{T})\). Two concrete questions are:<tbc>

• Can one prove nontrivial lower bounds for randomized streaming traceback algorithms on grid-like DAGs, beyond the trivial \(\Omega(\omega)\), and relate them to classical streaming lower bounds (e.g. via reductions from communication problems)?<tbc>

• Are there intermediate models (e.g. few-pass streaming, semi-streaming with \(O(\sqrt{T})\) memory, or streaming with limited random access) where one can match or beat the offline space bound for natural DP families?<tbc>

