_Proof of Theorem 1.1._ We can assume that _n_ is sufficiently large as otherwise, we can sort the input using any standard comparison-based sorting algorithm without affecting the asymptotic runtime.

Set \(k=\lceil log^{(3)}n\rceil\) where log<sup>(_t_)</sup>_n_ denotes the logarithm base 2 iterated _t_ times. Now, we split _S_ into \(\lceil n/k\rceil\) sequences \(S_1,\dots,S_{\lceil n/k\rceil}\) of _k_ elements, except possibly \(S_{\lceil n/k\rceil}\), which can be shorter. We sort \(S_1,\dots,S_{\lfloor n/k\rfloor}\) using Algorithm 3 and additionally, we sort \(S_{\lceil n/k\rceil}\) using any _O(k_log_k_) comparison-based sorting algorithm. By Theorem 4.1, this takes \(O((logc_\pi+1)\cdot n)+2^{2^{O(klogk)}}\) time. Plugging in _k_, we see that \(2^{2^{O(klogk)}}\subseteq o(n)\) and thus, this step takes only \(O((logc_\pi+1)\cdot n)\) time.<sup>1</sup>

Now it suffices to perform a bottom-up merge sort using Algorithm 2 and starting with \(S_1,\dots,S_{\lceil n/k\rceil}\). To be precise, we first merge \(\frac{log^{(2)}n}{log^{(3)}n}\)-tuples of consecutive sequences in order to reduce the number of sequences to at most \(\frac{n}{log^{(2)}n}\). Afterwards, we repeat the same step with \(\frac{logn}{log^{(2)}n}\)-tuples reducing the number of sequences to at most \(\frac{n}{logn}\). Finally, all remaining sequences can be merged by a single run of Algorithm 2. These can be seen as three layers of recursive merge sort where each layer takes \(O((logc_\pi+1)\cdot n)\) time by Theorem 3.1. Therefore, the merging as a whole finishes in \(O((logc_\pi+1)\cdot n)\) time and the same bound applies to the whole algorithm.

## References

<sup>1</sup>It would in fact suffice to set \(k=C\cdot\frac{log^{(2)}n}{log^{(3)}n}\) for a suitably small constant _C_.

