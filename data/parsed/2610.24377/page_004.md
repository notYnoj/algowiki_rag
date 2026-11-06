**Corollary 1.3.** There exists a catalytic algorithm using _O_(log(_n+b_)) clean space and _bn_<sup>1+_o_(1)</sup> time which takes as input a length-_n_ list of _b_-bit numbers, and computes the sorted list.

Corollaries 1.2 and 1.3 follow from direct applications of Theorem 1.1. We show that one can evaluate structured low-degree arithmetic circuits quickly, yielding several further algorithmic consequences:

**Theorem 1.4.** There is a catalytic algorithm which takes in a pair of integer matrices \(A,B\in[\text{poly}(n)]^{n\times n}\) and computes their product _AB_, using _O_(log_n_) clean space and \(n^{\omega+o(1)}\) time.<sup>2</sup>

**Theorem 1.5** (Informal)**.** Over any "reasonable" ring K, there exists a catalytic algorithm which takes in a vector \(x\in\mathcal{K}^n\) and computes the discrete Fourier transform, using _O_(log_n_) clean space and \(n\cdot\text{poly}(logn)\) time.<sup>3</sup>

Using near-linear-time sorting, FFT, and fast matrix multiplication as building blocks, we observe that we can obtain fast catalytic algorithms for a host of downstream applications, for instance:

**Corollary 1.6** (kSUM)**.** Let \(A_1,A_2,\cdots,A_k\) be lists of _n_<sup>_o_(1)</sup>-bit integers. Let _n_=max_<sub>i</sub>_{|_A<sub>i</sub>_|}. There exists a catalytic algorithm which, using \(n^{\lceil k/2\rceil+o(1)}\) time, \(n^{\lceil k/2\rceil+o(1)}\) catalytic space, and _O_(log_n_) clean space, decides whether there exists a _k_-tuple \((a_1,\cdots,a_k)\in A_1\times\cdots\times A_k\) such that \(a_1+\cdots+a_k=0\) .

**Corollary 1.7** (Triangle counting)**.** Let _G_ be an _n_-vertex simple undirected graph, given as an adjacency matrix. There exists a catalytic algorithm which, using \(n^{\omega+o(1)}\) time, \(n^{\omega+o(1)}\) catalytic space, and _O_(log_n_) clean space, counts the number of triangles in _G_.

We similarly observe that we can attain fast catalytic algorithms for integer multiplication (Corollary 3.2), polynomial multiplication (Corollary 4.7), frequency moments (Corollary 3.4), small universe #3SUM (Corollary 4.8), string matching with wildcards (Corollary 4.9), _k_-path detection (Corollary 4.14), _k_-cycle detection (Corollary 4.15), and 3_k_-clique counting (Corollary 4.12).

**Relationship to lower bounds.** None of the above runtimes are known or believed to be possible for (non- catalytic) algorithms with only _n_<sup>_o_(1)</sup> free space. So, these are cases where dirty space seems to be genuinely necessary for fast algorithms. Indeed, recall that we know _unconditional_ time-space lower bounds for several of these problems (sorting, DFT, integer multiplication, and matrix multiplication). Our catalytic algorithms achieve runtimes for these problems that are therefore _provably_ impossible for non-catalytic algorithms.

At this point, one might justifiably object that we are not making a fair comparison. These lower bounds are for multi-output functions, where the algorithm is given a separate output tape to which it has limited access (e.g., it must output all of the bits in a single left-to-right pass -- this is known as the "transducer" output model). However, our catalytic algorithms are instead designed to give the output by XORing into the catalytic tape. So it is unclear whether the provable<sup>4</sup> advantage is due to using dirty space to aid computation, or simply due to the different output model.

In Section 5, we therefore give some apples-to-apples comparisons. We define the **_k-output-pass_** output model, where the algorithm makes _k_ left-to-right passes over an output tape, to which it may XOR bits (but may not read existing values). (Note that the case _k_=1 corresponds to the transducer model.) We then observe that all of our catalytic algorithms can be implemented in the 2-output-pass model, and that all known time-space lower bounds (for non-catalytic algorithms) hold in the _k_-output-pass model for any constant _k_. Thus, in this model, having dirty space is provably necessary for achieving fast runtimes.

<sup>2</sup>See further results about matrix multiplications over modular rings in Section 4. <sup>3</sup>See Section 4 for a formal statement. <sup>4</sup>We stress that for any applications to decision problems (e.g. 3SUM or triangle detection), this output distinction is irrelevant, because we could simply copy the first bit of the dirty space into the free space. So, even without any careful model bookkeeping, our results do show an advantage from dirty space, conditional on believable assumptions about the hardness of those problems. The interesting question here is whether we can get something _unconditional_.

