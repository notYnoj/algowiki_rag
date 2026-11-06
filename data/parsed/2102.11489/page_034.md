## 9 Approximate Splitter from Lossy Loose Compaction

### 9.1 Approximate Swapper Circuit

### Approximate swapper.

An (_n,w_)-approximate swapper obtains an input array where each element is marked with a label that is \(\perp\), `blue`, or `red`. Let _n_<sub>red</sub> and _n_<sub>blue</sub> denote the number of red and blue elements, respectively. The (_n,w_)-approximate swapper circuit swaps a subset of the `blue` elements with `red` ones and the swapped elements receive the label \(\perp\). We call elements marked `red` or `blue` _colored_ and those marked \(\perp\) _uncolored_.

Formally, an (_n,w_)-approximate swapper solves the following problem:

• **Input**: an input array containing _n_ elements where each element contains a _w_-bit payload string and a two-bit metadata label whose value is chosen from the set \(\{\mathtt{blue},\mathtt{red},\perp\}\). Henceforth we assume the first bit of the label encodes whether the element is colored or not, and the second bit of the label picks a color between `blue` and `red` if the element is indeed colored.<tbc>

• **Output**: a _legal swap_ of the input array such that at most _n/_128+|_n_<sub>red</sub>-_n_<sub>blue</sub>| elements remain colored, where the notion of a legal swap is defined below.<tbc>

<tbc>We say that an output array **O** is a _legal swap_ of the input array **I** iff there exist pairs \((i_1,j_1),(i_2,j_2),\dots,(i_\ell,j_\ell)\) of indices that are all distinct, such that for all \(k\in[\ell]\), **I**\[_i<sub>k</sub>_\] and **I**\[_j<sub>k</sub>_\] are colored and have opposite colors, and moreover **O** is obtained by swapping **I**\[_i_<sub>1</sub>\] with **I**\[_j_<sub>1</sub>\], swapping **I**\[_i_<sub>2</sub>\] with **I**\[_j_<sub>2</sub>\], ..., and swapping **I**\[_i<sub>k</sub>_\] with **I**\[_j<sub>k</sub>_\]; further, all swapped elements become uncolored.

**Theorem 9.1** (Approximate swapper)**.** _There exists an_ (_n,w)-approximate swapper circuit containing O(n_) _generalized boolean gates and O(n_) _number of w-selector gates, and of depth O_(1).

_Proof._ We can use Algorithm 6.10 in Asharov et al. \[AKL<sup>+</sup>20b\]: their algorithm is described for the oblivious PRAM model, and achieves _O(n_) work and _O_(1) depth. It is straightforward to check that the same algorithm can be implemented as a circuit with _O(n_) generalized boolean gates, _O(n_) number of _w_-selector gates, and _O_(1) in depth. Note that Algorithm 6.10 in Asharov et al. \[AKL<sup>+</sup>20b\] needs to compute the decomposed perfect matchings on the fly since their oblivious PRAM algorithm is uniform; however, we do not need to compute the matchings on the fly in the circuit model, since the circuit model is non-uniform.

### Swapper.

A swapper is defined in almost the same way as an approximate swapper, except that we require that the remaining colored elements do not exceed |_n_<sub>red</sub>-_n_<sub>blue</sub>|. In other words, if initially, the number of `red` elements equals the number of `blue` elements, then the swapper must swap every `red` element with a distinct `blue` element, leaving no colored elements behind.

**Theorem 9.2** (Slow swapper)**.** _There exists an_ (_n,w)-swapper circuit (henceforth denoted_ \(\mathbf{SlowSwap}(\cdot)\)_) with O(n_log_n_) _generalized boolean gates, and O(n_log_n_) _number of w-selector gates , and whose depth is O_(log_n)._

_Proof._ We can use the following algorithm:

1. Use an AKS sorting circuit \[AKS83\] to sort the input array such that all the `red` elements are in the front; and all the `blue` elements are at the end. Let the result be **X**.<tbc>

2. For each \(i\in 1,2,\dots,\lfloor n/2\rfloor\) in parallel: if **X**\[_i_\] is marked `red` and **X**\[_n_+1-_i_\] is marked `blue`, then swap **X**\[_i_\] and **X**\[_n_+1-_i_\] and mark both elements as uncolored.<tbc>

