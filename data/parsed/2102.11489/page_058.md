1. Divide input into chunks, each consists of 2<sup>5_k_</sup> integers. For each chunk, sort integers in the chunk using AKS sorting network. This takes size _O(nk_<sup>2</sup>) and depth _O(k_).<tbc>

2. For each chunk, count the number of occurrences for all integer \(i\in[2^k]\), which yields a short list of \(2^k\cdot 5k\) bits (compared to chunk size, \(2^{5k}\cdot k\)). To do so, for each chunk, the following is performed.<tbc>

(a) The sorted chunk is sub-divided into 2<sup>3_k_</sup> pieces, each consists of 2<sup>2_k_</sup> integers. Because it is sorted, the chunk has at most 2_<sup>k</sup>_ pieces that are non-uniform (that is, having more than 1 distinct integers).<tbc>

(b) Counting is straightforward for each uniform piece.<tbc>

(c) The non-uniform pieces are collected into a short list of 2<sup>3_k_</sup> integers using AKS sorting network. Then on the short list, a counting is performed for each integer \(i\in[2^k]\) (e.g., Fact 6.4), resulting the counts of the short list.<tbc>

(d) The counts of all pieces and the short list are summed up, resulting the counts of this chunk.<tbc>

<tbc>Notice that the cost of AKS is the same as previous step, and that counting the short list takes circuit size \(O(2^k\cdot 2^{3k})\) and depth _O(k_). Hence for all chunks, this takes size _O(nk_<sup>2</sup>) and depth _O(k_).<tbc>

3. Sum up the counts from all _n/_2<sup>5_k_</sup> chunks, and then calculate the "desired counts" for each chunk when all _n_ integers are sorted. The counts from all chunks are just \((n/2^{5k})\cdot(2^k\cdot 5k)\) bits, so this can be implemented in circuit size _O(nk_) and depth _O(k_+log_n_), e.g., using delayed-carry addition and all prefix sums (Facts 6.4).<tbc>

4. With the desired counts, each chunk restore integers from its counts using a reversed procedure of Step 2.<tbc>

5. The concatenation of all restored chunks is the sorted output.

This concludes the improved circuit depth _O(k_+log_n_); notice that the depth is achieves using the above pipelined AKS, compared to depth _O(k_log_k_+log_n_) in Kouckỳ and Kràl.

## C Epilogue: Reducing the polylog<sup>∗</sup> to log<sup>∗</sup>

While Kouckỳ and Král achieved a sub-optimal depth _O_(log<sup>3</sup>_n_), their circuit size is \(O(nk(w+k)\cdot(1+log^*n-log^*(w+k)))\), which is slightly better than our circuit size, \(O(nk(w+k))\cdot(1+\mathsf{poly}(log^*n-log^*(w+k)))\). It turns out that we can combine the techniques in the two papers, and achieve optimal depth and \(O(nk(w+k)\cdot(1+log^*n-log^*(w+k)))\) circuit size for sorting _k_-bit keys. Note that besides this section which is added in hindsight, the rest of the paper is concurrent and independent work to Koucký and Král \[KK21\].

Specifically, we will prove the following slightly improved theorem in this section.

**Theorem C.1.** _Suppose that n\>_2<sup>4_k_+7</sup>_. There is a constant fan-in, constant fan-out boolean circuit that correctly sorts any array containing n elements each with a k-bit key and a w-bit payloads, whose size is_ \(O(nk(w+k))\cdot(1+log^*n-log^*(w+k))\) _and whose depth is O_(log_n_+log_w)._

