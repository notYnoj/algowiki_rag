model, we note that the above implies that the search problem "given a list _L_, output \((L',L'')\) such that \(L'\oplus L''=\mathsf{SORTED}(L)\)" is possible with low product of time and clean space for catalytic transducers, but not for non-catalytic transducers.

Finally, to get a lower bound for the product of time and clean space against 1-output-pass catalytic algorithms, we directly adapt the Borodin-Cook branching program approach. We consider _catalytic_ branching programs, which have a large number of start vertices, each with corresponding end vertices, and the requirement that computation from a given start vertex must always end at the corresponding end vertex. As in existing lower bounds, we argue that, on a random input, most nodes of the branching program can’t result in outputting too many values. Then, we observe that _every_ path from a start to an end vertex must pass through many nodes that output many values. Since these paths have to be disjoint, this gives a large lower bound on the size of the branching program.

## 2 Preliminaries

We assume basic familiarity with computational complexity \[AB09\] and arithmetic circuit complexity \[SY10\].

**Notation.** We use \[_N_\] to denote the set \(\{1,2,\cdots,N\}\). We write _x_mod_N_ to refer to the representative of _x_’s modular equivalence class in \[_N_\], as opposed to the whole equivalence class. We use base 2 for the logarithm, log_n_:=log<sub>2</sub>(_n_). The set \(\mathbb{N}=\{1,2,\cdots\}\) excludes 0.

**Symmetric circuits.** A function \(f:\{0,1\}^m\rightarrow\{0,1\}\) is _symmetric_ if \(f\circ\pi=f\) for every bitwise-permutation \(\pi\). Equivalently, _f_’s output depends only on the number of 1s in its input. (Examples of symmetric functions include `AND`, `OR`, or `MAJORITY`.) A _symmetric circuit_ is a circuit (of arbitrary fan-in) whose gates are all labeled with symmetric functions.

**Catalytic algorithms.** Consider an algorithm with read-only access to an input and read-write access to both a "clean" work-tape, as well as a "dirty" work-tape consisting of _d(n_) bits. We say that such an algorithm is _catalytic_ if, on every input _x_ and every possible initial assignment \(z\in\{0,1\}^{d(n)}\) to dirty space, the algorithm halts with dirty space set to _z_. We design our algorithms under the assumption that the model has RAM access to all of these tapes.

**A note on catalytic space complexity.** It is known (see e.g. \[FLMV05\]) that any RAM computation using time _T=T(n_) accessing memory cells up to index, say, 2<sup>_O(T_)</sup> can be converted to a time \(T\cdot\mathrm{poly}(\mathrm{log}T)\) equivalent algorithm using _O(T_log_T_) contiguous bits of space. However, we do not yet know of a generic way to perform this conversion for _catalytic_ RAM algorithms running in time _T_. For this reason, we explicitly state the catalytic space bounds for the algorithms throughout this paper. All our algorithms have the feature that the catalytic space complexity is at most the runtime (up to polylog factors).

**Low-space output models.** For space-bounded computation of multi-bit functions, it is crucial to only allow restricted access to the output tape to retain a fair measure of the space. There are several possible ways to restrict the access, which we briefly survey, that could be of material consequence when measuring runtime.<sup>5</sup> For all the subsequent definitions, we say TM _M_ computes function family \(f_n:\{0,1\}^n\rightarrow\{0,1\}^\star\) if, for all \(x\in\{0,1\}^n\), whenever the input tape is initialized with _x_ the machine halts with _f(x_) on the output tape.

The most restricted model is the bit-by-bit one-way output tape model, where the machine must _commit_ to the value of the _i_th output bit before continuing to the (_i_+1)<sup>st</sup> bit.

<sup>5</sup>All of the following notions are equivalent with respect to space, disregarding time complexity, by simply recording all the changes applied to the _i_th bit of the output tape (for each _i_ at a time) and recomputing as necessary.

