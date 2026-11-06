## 1.2 Lower Bounds for Sorting

Our main result for external memory integer sorting is the following connection to Conjecture 1:

**Theorem 2** _Assuming Conjecture 1, any randomized algorithm for the external memory sorting problem with_ \(w=\Omega(lgn)\) _bit integers, having error probability at most_ 1/3_, must make an expected_

\(\Omega\big(min\big\{n,\frac{n}{B}\cdot lg_{2M/B}\frac{n}{B}\big\}\big)\)

_I/Os._

Thus if we believe Conjecture 1, then even for randomized algorithms, there is no hope of exploiting integer input to improve over the simple external memory comparison based algorithms (when \(B\ge lgn\) such that the latter term in the lower bound is the min).

Now observe that since our lower bound only counts I/Os, the lower bound immediately holds for word-RAM algorithms when the word size is some \(b=\Omega(lgn)\) by setting _m=O(b_) and _B=b/w_ in the above lower bound (the CPU’s internal state, i.e. registers, can hold only a constant number of words). Thus we get the following lower bound:

**Corollary 3** _Assuming Conjecture 1, any randomized word-RAM algorithm for sorting_ \(w=\Omega(lgn)\) _bit integers, having error probability at most_ 1/3 _and word size_ \(b\ge w\) _bits, must spend_

\(\Omega\big(min\big\{n,\frac{nw}{b}\cdot lg\frac{nw}{b}\big\}\big)\)

_time._

We note that the a standard assumption in the word-RAM is a word size and key size of \(b,w=\Theta(lgn)\) bits. For that choice of parameters, our lower bound degenerates to the trivial \(t=\Omega(n)\). This has to be the case, as Radix Sort gives a matching upper bound. Nonetheless, our lower bound shows that when the key size is much smaller than the word size, one cannot sort integers in linear time (recall linear is _O(nw/b_) as this is the time to read/write the input/output).

Finally, we show that the obliviousness assumption made in the previous paper by Adler et al. \[1\] allows one to prove very strong sorting lower bounds that even surpass the known (non-oblivious) Radix Sort upper bound:

**Theorem 4** _Assuming Conjecture 1, any oblivious randomized word-RAM algorithm for sorting_ \(\Theta(lgn)\) _bit integers, having error probability at most_ 1/3 _and word size_ \(\Theta(lgn)\)_, must spend_ \(\Omega(nlgn)\) _time._

Thus at least for the natural problem of integer sorting, being oblivious has a huge impact on the possible performance of algorithms. Our results are therefore not just an application of the previous technique to a new problem, but a great strengthening. Moreover, as we discuss in Section 3, removing the obliviousness assumption requires new and deep ideas that result in significantly more challenging lower bound proofs.

## 1.3 Lower Bounds for Matrix Transpose

We also reprove an analog of the lower bounds by Adler et al. \[1\] for the matrix transpose problem, this time without any assumptions of obliviousness. In the matrix transpose problem, the input is an \(n\times n\) matrix _A_ with _w_-bit integer entries. The matrix is given in row-major order, meaning that each row of _A_ is stored in _n/B_ blocks of _B_ consecutive entries each. The goal is to compute _A<sup>T</sup>_,<tbc>

