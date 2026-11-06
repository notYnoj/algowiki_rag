Therefore, in total, this step can be implemented with _O(nw_) generalized boolean gates, _O(n_) number of _w_-selector gates, and in depth _O_(log_n_).<tbc>

• Now, all dense chunks mark all its super-elements as fillers. This can be done by having each chunk broadcast its dense/sparse indicator bit over a binary tree to all _d_ positions of the chunk. In total, we can implement it with a circuit of \(O(n')\) generalized boolean gates and _O_(log_d_)=_O_(loglog_n_) depth.<tbc>

• Finally, we need to compress all chunks on the left and the right to \(\left\lfloor d/(2log^2m)\right\rfloor\) super-elements. This can be accomplished by applying a **SlowTC** circuit to each chunk (Lemma 13.1), and the number of generalized boolean gates, _w_-selector gates, and depth are asymptotically the same as the earlier step in which we invoke a **SlowDistr** instance per chunk.

Summarizing the above, we get that the entire sparse loose compactor algorithm requires _O(nw_) generalized boolean gates, _O(n_) number of _w_-selector gates, and _O_(log_n_) depth.

**Remark 5.** So far, we have assumed that _n_ is divisible by \(\left\lfloor logn\right\rfloor\) and \(n':=n/\left\lfloor logn\right\rfloor\) is equal to \(m\cdot\left\lfloor d/2\right\rfloor\) for some perfect square _m_, and \(d=\Theta(log^cm)\) is the degree of the aforementioned bipartite expander graph \(G_{\epsilon,m}\) where _c\>_4 is an appropriate constant.

If the above is not satisfied, we can let \(n':=\left\lceil n/\left\lfloor logn\right\rfloor\right\rceil\). If \(n'\) does not satisfy the above, we can find the largest _m_<sup>∗</sup> such that \(n'\ge m^*\cdot\left\lfloor d^*/2\right\rfloor\) (note that _d_<sup>∗</sup> is a function of _m_<sup>∗</sup> for a fixed \(\epsilon\)). Now, we can round _m_<sup>∗</sup> up to the next perfect square _m_, and still use _d_<sup>∗</sup> as the degree of the bipartite expander graph. We can pad the array with fillers such that contains \(m\cdot d^*\) super-elements, and then run the sparse loose compactor algorithm. With this modification, one can check that Lemma 13.4 and Fact 13.5 still hold. Therefore, our earlier analyses hold. The padding incurs only 1+_o_(1) blowup in the array’s length, i.e., \(n''=(1+o(1))n'\). Our algorithm compresses the array to \(n''/(logm)^2\) in the number of super-elements, for sufficiently large _n_ and thus sufficiently large \(n'=\left\lceil n/logn\right\rceil\), the output length is upper bounded by \(\left\lfloor n/logn\right\rfloor\).

## 14 Linear-Sized, Logarithmic-Depth Tight Compaction Circuit

Putting it all together, we can now realize a linear-sized, logarithmic-depth tight compaction circuit, as stated in the following theorem:

**Theorem 14.1** (Linear-sized, logarithmic-depth tight compaction circuit)**.** _There is an_ (_n,w)- tight compaction circuit with_ \(O(nw)\cdot max(\mathsf{poly}(log^*n-log^*w),1)\) _generalized boolean gates,_ \(O(n)\cdot max(\mathsf{poly}(log^*n-log^*w),1)\) _number of w-selector gates, and of depth O_(log_n_).

Note that the above theorem and Lemma 6.1 together would imply the following corollary.

**Corollary 14.2.** _There is a circuit of size_ \(O(nw)\cdot max(\mathsf{poly}(log^*n-log^*w),1)\) _and depth O_(log_n_+log_w_) _that can sort any array containing elements with 1-bit keys and w-bit payloads._

**Proof of Theorem 14.1:** We construct a linear-sized, logarithmic-depth tight compaction circuit as follows.

