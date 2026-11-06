<tbc>i.e. output the column-major representation of _A_ which stores _n/B_ disk blocks for each column of _A_, each containing a consecutive range of _B_ entries from the column.

Based on Conjecture 1, Adler et al. \[1\] proved an \(\Omega(BlgB)\) lower bound on the number of I/Os needed for this problem when _n=B_, assuming that _M_=2_B_ and that the algorithm is oblivious. We strengthen the lower bound to the following:

**Theorem 5** _Assuming Conjecture 1, any randomized algorithm for the external memory matrix transpose problem with w bit integer entries, having error probability at most_ 1/3_, must make an expected_

\(\Omega\left(min\left\{\frac{n^2lg_{2M/B}B}{B},\frac{n^2w}{lg(n^2w)}\right\}\right)\)

_I/Os._

Notice that the first term in the min corresponds to their lower bound when _n=B_ (they have _M_=2_B_), but our new lower bound does not require the algorithm to be oblivious (and allows randomization). It is unclear whether the second term in the min is just an artifact of our proof, but we remark that it can only be the minimum when _B_ is very small.

Consider now the matrix transpose problem on the word-RAM with word size _b_ bits (and thus memory size _m=O(b_)). Given an \(n\times n\) matrix _A_ with _w_-bit integer entries, the lower bound in Theorem 5 implies (by setting _B=b/w_):

**Corollary 6** _Assuming Conjecture 1, any randomized word-RAM algorithm for computing the transpose of an_ \(n\times n\) _matrices with w-bit integer entries, having error probability at most_ 1/3 _and word size b bits, must spend_

\(\Omega\left(min\left\{\frac{n^2wlg(b/w)}{b},\frac{n^2w}{lg(n^2w)}\right\}\right)\)

_time._

The above corollary in particular implies that for \(b\times b\) bit matrices and word size _b_ bits, one needs \(\Omega(blgb)\) time to transpose, whereas linear time would have been _O(b_) as this is the time to read/write the input/output.

## 1.4 Other Related Work

Proving lower bounds for external memory algorithms and data structures without assumptions such as indivisibility and comparison based has been the focus of a number of recent papers. Quite surprisingly, Iacono and Pˇatraşcu \[11\] showed that for the _dictionary_ problem, one can indeed exploit integer input to beat the comparison based bounds. This is in sharp contrast to our new results for integer sorting. Iacono and Pˇatraşcu \[11\] complemented their upper bound by a matching unconditional lower bound proved in a version of the cell probe model of Yao \[18\] adapted to the external memory setting. Their lower bound improved over previous work by Yi and Zhang \[19\] and Verbin and Zhang \[17\]. In other very recent work, Jiang and Larsen \[13\] showed how to exploit integer input to develop external memory priority queues with DecreaseKeys that outperform their comparison based counterparts. Their upper bound almost matches an unconditional lower bound by Eenberg et al. \[6\] (also proved in the cell probe model).

Another active line of research has studied the benefits of network coding over the traditional routing-based solutions. Research on the network coding started by the work of Ahlswede et al.<tbc>

