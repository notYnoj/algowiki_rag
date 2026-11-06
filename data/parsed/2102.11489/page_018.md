## 4 Building Blocks for the Oblivious PRAM Model

In this section, we present some building blocks that can be implemented as deterministic, oblivious parallel algorithms. This means that the algorithms’ memory access patterns are fixed a-priori and independent of the input (once we fix the input’s length).

**Compaction.** Compaction (short for "tight compaction") solves the following problem: given an array in which every element is tagged with a 1-bit key, move all elements tagged with 0 to the front of the array, and move elements tagged with 1 to the end. Asharov et al. \[AKL<sup>+</sup>20b\] showed a deterministic algorithm that obliviously compacts any array containing _n_ elements each of which encoded as \(\ell\) words; and their algorithm achieves \(O(\ell\cdot n)\) total work and _O_(log_n_) depth.

Furthermore, their compactor supports a "reverse routing" capability. Specifically, their compactor can be thought of a network consisting of _O(n_) selector gates of depth _O_(log_n_), with _n_ inputs and _n_ outputs. Each selector gate takes in a 1-bit flag and two input elements that are \(\ell\) words long, and the flag is used to decide which of the two input elements to output. The first phase of their algorithm, takes _O(n_) work and _O_(log_n_) depth: it computes on the elements’ 1-bit keys, and populates all selector gates’ 1-bit flags. The second phase of their algorithm then routes the input elements to the output layer over this selector network. This takes \(O(\ell\cdot n)\) work and _O_(log_n_) depth. Since each selector gate can remember its flag, it is possible to later on route elements in the reverse direction, from the output layer back to the input layer.

We stress that Asharov et al. \[AKL<sup>+</sup>20b\]’s oblivious compaction algorithm is _not stable_, i.e., it does not preserve the relative order of elements with the same key as they appeared in the input array. In fact, Lin, Shi, Xie \[LSX19\] showed that this is inherent: any oblivious algorithm in the indivisibility model that achieves _stable_ compaction must incur \(\Omega(n\mathrm{log}n)\) work. Here, an algorithm in the indivisibility model is one that does not perform encoding or computation on the elements’ payload strings. Afshani et al. \[AFKL19\] shows that the \(\Omega(n\mathrm{log}n)\) lower bound holds for oblivious, deterministic stable compaction even without the indivisibility requirement, but instead assuming that the Li-Li network coding conjecture holds \[LL04\].

**Distribution.** Distribution solves the following problem. We are given an input array **I** of length _n_ in which each element carries a _w_-bit payload and a 1-bit label indicating whether the element is _real_ or a _filler_. Additionally, we are given a bit-vector **v** of length _n_, where **v**\[_i_\] indicates whether the _i_-th output position is available to receive a real element. It is promised that the number of available positions is at least as many as the number of real elements in **I**. We want to output an array **O** such that the multiset of real elements in **O** is the same as the multiset of real elements in **I**, and moreover if **O**\[_i_\] contains a real element, then it must be that **v**\[_i_\]=1, i.e., only available positions in the output array **O** can receive real elements.

The following algorithm accomplishes the aforementioned distribution task using compaction as a building block:

\begin{tabular}{cc}
\multicolumn{2}{c}{**Distribution**} \\
1. Let **X** be an array in which all payloads are fillers and each **X**\[_i_\] is marked with the label **v**\[_i_\]. & \\
2. Now, apply tight compaction to **X** routing all entries with 1-labels to the front, and all entries with 0-labels to the end. & \\
3. Apply another instance of tight compaction to the input array **I** routing all real elements to the front and all filler elements to the end; let the outcome be \(\mathbf{I}'\). & \\
\end{tabular}

