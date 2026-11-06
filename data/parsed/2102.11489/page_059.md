<tbc>To get the above theorem, it suffices to replace the (tight) compaction circuit in the proof of Theorem 15.7 with one that achieves logarithmic depth and _O(nw_(1+log<sup>∗</sup>_n_-log<sup>∗</sup>_w_)) size. Recall that the proof of Theorem 15.7 performs a 1-bit to _k_-bit upgrade using the new techniques developed earlier in our paper. Henceforth, we focus on constructing a compaction circuit satisfying the above requirements. More specifically, to prove the above Theorem C.1, it suffices to prove the following:

**Theorem C.2.** _There exists a tight compaction circuit of size_ \(O(nw\cdot(1+\mathrm{log}^*(n)-\mathrm{log}^*(w)))\) _and depth O_(log_n), where w is the width of the payload._

Inspired by Koucký and Král [KK21], we will start with a logarithmic-depth compaction circuit that is a loglog_n_ factor non-optimal in size, and then use a recursive bootstrapping technique to compress the circuit size while preserving the asymptotical depth.

## C.1 Compaction Circuit Optimal in Depth but Slightly Non-Optimal in Size

As a starting point, we will use a compaction circuit that is optimal in depth but a loglog_n_ factor non-optimal in size, as stated in the following theorem:

ProposeAcceptFinalize, const-degree expander, loglogn iterations (Pippenger [Pip96])
1 -lossy loose compact (output size n/2)
Circuit size: nw + n log log n depth: O(log0.1 n)
Pippenger-style recurse [Pip96] for log log iterations, §12
ProposeAcceptFinalize re-parameterized with (poly logn)-degree expander and log logn iterations + (poly log)-depth tight compact [Pip96,ALS21], §13
1 -approx tight compact (output size n/ log n)
poly log n (output size n/ log n)
Circuit size: nw + n log log n depth: O(log0.2 n)
AKS [AKS83]
Circuit size: O(nw) depth: O(logn)
Circuit variant of Asharov et al. [AKL+20b, Algorithm 5.2], §14
tight compact
Circuit size: nw + n log log n depth: O(logn)
Koucký and Krål [KK21, Lemma 19], see §C.2
tight compact
Circuit size: nw log* n depth: O(logn)

**Figure 3:** Blueprint of the improved circuit size, putting together our techniques with that of Koucký and Krål. Notice that the underlined circuit sizes are larger than the corresponding ones in Figure 1.

