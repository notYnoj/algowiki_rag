Step 4, we remember for each position of the output array, from which array \(B'_u\) it received an element. In this way, we can reverse Step 4 and reconstruct the arrays \(B'_0,\dots,B'_{K-1}\) from the output. Now, we can reverse the routing decisions of the ternary sorter to reconstruct the arrays _B_<sub>0</sub>_,...,B_<sub>_K_-1</sub>. For each \(i\in[n]\), there is only one _B<sub>u</sub>_ such that _B<sub>u</sub>_\[_i_\] is not a filler element, and this element _B<sub>u</sub>_\[_i_\] will be routed back to the _i_-th position of the input array. Clearly, the reverse routing does not cost more than the forward direction in terms of work and depth.

### Slow alignment.

We define a variant of the slow sorter algorithm, called \(\text{\textbf{SlowAlign}}^{K,K^\prime}(A)\). \(\text{\textbf{SlowAlign}}^{K,K^\prime}\) receives an input array _A_ in which every element _A_\[_i_\] is not only tagged with a key _A_\[_i_\].key from the domain \[0_,K_-1\], but also an index _A_\[_i_\].idx which can be expressed in \(k':=logK'\) bits. As before, we assume that each element, including its tagged key and index, can fit in _O_(1) words. We want to output a permutation of _A_ such that in the ordering the keys become consistent with the ordering of the indices in the input array. In other words, suppose that _B_ is the output array in which each element is tagged with only a key, then,

\(\forall i,j\in[n]\text{and}i\neq j:(A[i].\text{idx}<A[j].\text{idx})\Longrightarrow(B[i].\text{key}\le B[j].\text{key})\) (1)

**Theorem 5.2** \((\text{\textbf{SlowAlign}}^{K,K^\prime})\)**.** _There is a deterministic, oblivious_ \(\text{\textbf{SlowAlign}}^{K,K^\prime}(A)\) _algorithm that solves the above alignment problem and outputs an array B that is a permutation of the input array A satisfying Equation_ (1)_; and moreover, the algorithm takes_ \(O((K+K')n)\) _total work and_ \(O(logK+logK'+logn)\) _depth where n is the length of the input array._

_Proof._ The oblivious algorithm **SlowAlign**<sup>_K,K_<sup>\(^\prime\)</sup> is described below:

\(\text{\textbf{SlowAlign}}^{K,K^\prime}(A)\text{\textbf{Input: An array}}A\text{of length}n\text{, and for every}i\in[n]\text{, the element}A[i]\text{is tagged with a key}A[i].\text{key and an index}A[i].\text{idx.
\textbf{Algorithm:} 1. Call \textbf{SlowSort}}^K(A)\text{using the key field as the key to sort the array}A\text{, and let}B\text{be the outcome. 2. Call \textbf{SlowSort}}^{K^\prime}(A[1].\text{idx},A[2].\text{idx},\dots,A[n].\text{idx})\text{and let idx}_1,\dots,\text{idx}_n\text{be the resulting ordered list of indices. 3. Reverse route}B\text{by reversing the routing decisions made in Step 2.}\)

Correctness is easy to verify. For performance bounds, observe that Step 1 takes _O(nK_) work and _O_(log_n_+log_K_) depth, Step 2 takes \(O(nK')\) work and \(O(logn+logK')\) depth, Step 3’s work and depth are not more than Step 2.

## 5.2 Finding the Dominant Key

Let \(\epsilon\in(0,1/2)\). We say that an array _A_ of length _n_ is \((1-\epsilon)\)-uniform iff except for at most \(\epsilon n\) elements, all other elements in _A_ have the same key -- henceforth this key is said to be the _dominant_ key.

We want an algorithm that can correctly identify the dominant key when given an input array _A_ that is \((1-\epsilon)\)-uniform. If the input array _A_ is not \((1-\epsilon)\)-uniform, the output of the algorithm may be arbitrary.

