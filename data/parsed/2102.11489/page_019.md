4. Next, reverse-route the array \(\mathbf{I}'\) by reversing the routing decisions made in Step 2, and output the result.

Therefore, oblivious distribution can be accomplished with the same asymptotical overhead as oblivious compaction. Just like compaction, here it also makes sense to consider a reverse-routing capability of our distribution algorithm.

**All prefix sums.** Given an array _A_ of length _n_, an all-prefix-sum algorithm outputs the prefix sums of all _n_ prefixes, i.e., _A_\[:1\], _A_\[:2\], _..._, and _A_\[:_n_\], respectively. It is promised that the sum of the entire array _A_ can be stored in _O_(1) memory words. It is well-known that there is a deterministic, oblivious algorithm that computes all prefix sums in _O(n_) work and _O_(log_n_) depth \[JáJ92\].

**Generalized binary-to-unary conversion.** Imagine that there are _n_ receivers where the _i_-th receiver is labeled with an indicator bit **x**\[_i_\]. We are given an integer \(\ell\in\{0,1,\dots,n\}\) expressed in binary representation, and we want to output an array of _n_ bits where the _i_-th bit represents the bit received by the _i_-th receiver. We want that the first \(\ell\) receivers marked with 1 receive 1, and all other receivers marked with 1 receive 0. The receivers marked with 0 may receive an arbitrary bit. Note that in the special case that all receivers are marked with 1, then the problem boils down to converting an integer \(\ell\in\{0,1,\dots,n\}\) expressed in binary representation to a corresponding unary string.

The generalized binary-to-unary conversion problem can easily be solved by invoking an all- prefix-sum computation on an oblivious parallel RAM, taking _O(n_) total work and _O_(log_n_) depth<sup>5</sup>.

**Sorting elements with ternary keys.** We will need a linear-work, and logarithmic-depth oblivious algorithm to sort an input array with ternary keys, as stated in the following theorem.

**Theorem 4.1** (Sort elements with ternary keys)**.** _There exists a deterministic, oblivious algorithm that can sort any input array A containing n elements each with a key from the domain_ {0,1,2} _in O(n_) _work and O_(log_n_) _depth._

_Proof._ Consider the following algorithm:

One can easily verify that the above algorithm sorts the input array _A_ with ternary keys, and moreover, the algorithm completes in _O(n_) total work and _O_(log_n_) depth.

Just like compaction, here it also makes sense to consider a reverse-routing capability of our ternary-key sorting algorithm.

<sup>5</sup>We explicitly differentiate the generalized binary-to-unary conversion from the all-prefix-sum because it is more convenient later for our circuit-model results. In the circuit model, the generalized binary-to-unary conversion can be solved with a circuit _O(n_) in size and _O_(log_n_) in depth, whereas all-prefix sum requires a circuit _O(n_log_n_) in size and _O_(log_n_) in depth (even when the input _A_ is a bit array).

Ternary-key sorting
1. For each key b = 0,1,2}, let Lb,Ub [n] denote the starting and ending index for b if the array A were to be fully sorted. We can accomplish this by counting for each b = 0,1,2
the total number of occurrences of b in A.
2. Relying on oblivious distribution three times, we can route all elements with the key b to the positions [Lb,Ub] of the output array. Output the result.

