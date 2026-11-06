If we run the **AllPrefixSum** algorithm using the delayed-carry representation, the outcome will be _n_ prefix sums where the _i_-th prefix sum is expressed the sum of two numbers, _s<sub>i</sub>_ and _t<sub>i</sub>_. Finally, we can compute _s<sub>i</sub>+t<sub>i</sub>_ in parallel for all \(i\in[n]\) in parallel, taking \(O(log\ell)\le O(logn)\) depth. The entire circuit for computing all _n_ prefix sums takes \(O(n\ell)\) generalized boolean gates and _O_(log_n_) depth.

## Generalized binary-to-unary conversion.

The generalized binary-to-unary conversion problem has been defined earlier in Section 4. Earlier, we also showed how to solve it on an oblivious PRAM in linear total work and logarithmic depth. It turns out that it is a little trickier if we want to accomplish the same with a linear-sized and logarithmic depth circuit. This is because on a PRAM, arithmetic and boolean operations on log_n_ bits can be performed in unit cost, whereas in a circuit model, we charge _O_(log_n_).

We can solve the generalized binary-to-unary conversion problem with the following algorithm. Without loss of generality, we can assume that _n_ is a power of 2; if not, we can round _n_ up to the nearest power of 2.

\begin{tabular}{cc}
\multicolumn{2}{c}{**AllPrefixSum**(_A_)} \\
\multicolumn{2}{c}{**Input:** An array _A_ containing _n_ bits, where _n_ is a power of 2. We assume that each bit _A_\[_i_\] is represented in a delayed-carry representation as the sum of _A_\[_i_\] and 0.} \\
\multicolumn{2}{c}{**Algorithm:**} \\
1. If _n_=1, return the only element of _A_. Else proceed with the following \\
2. Let \(A'\) be the array of length _n/_2 containing sums of adjacent pairs in _A_. \(A'\) can be computed from _A_ using _n/_2 shallow additions. \\
3. Compute \(S:=\mathbf{AllPrefixSum}(A')\). \\
4. Compute the all-prefix-sum array for _A_ from _S_, filling the gaps by performing _n/_2 shallow additions. \\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{**Generalized binary-to-unary conversion circuit**} \\
1. First, we apply the counting circuit of Fact 6.3 to the input array **x**. Specifically, we compute & \\
the sum over a binary tree using the delayed-carry representation of numbers. At the end & \\
of this step, every tree node stores the sum of its subtree, in delayed-carry representation. & \\
Henceforth, let _S(v_) denote the sum of the subtree rooted at the node _v_. We may assume & \\
that all numbers below use a delayed-carry representation. & \\
2. For convenience, assume that the root receives \(\ell\) from an imaginary parent. & \\
From level _i_=0 to log_n_-1: every node in level _i_ performs the following. Let _S_ be the & \\
number received from its parent, and let `lc` and `rc` denote the node’s left child and right & \\
child, respectively. Send _S_ to `lc` and send _S-S_(`lc`) to `rc`. & \\
3. For convenience, assume that the root receives the label "`M`" from an imaginary parent. & \\
From level _i_=0 to log_n_-1, every node in level _i_ does the following where `lc` and `rc` denote & \\
its left child and right child, respectively: & \\
• If the label received from its parent is not "`M`", then pass the label to both children; & \\
\end{tabular}

