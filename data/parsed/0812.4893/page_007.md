## 3 Related Work

The stable marriage problem remains a subject of active research. The book by Gusfield and Irving [9] is a comprehensive survey on the problem; see the MATCH-UP workshop [10] for the latest developments.

### 3.1 Almost Stable Matching

Abraham et al. [1] study almost stable matchings in the stable roommates problem. The recent work by Biró et al. [3] is particularly close to ours: they, too, consider the stable marriage problem with incomplete preference lists, and aim at finding a matching with few unstable edges. However, in terms of computational complexity, their work goes in the opposite direction. Their task is to find a _maximum_ matching that minimises the number of unstable edges. It turns out that this makes the problem computationally much more _difficult_: the problem is NP-hard, unlike the classical stable marriage problem. In contrast, we do not require that the matching is a maximum matching, which makes the problem computationally _easier_: the problem admits a constant-time distributed algorithm, unlike the classical stable marriage problem. The algorithm works even when ties in the preferences lists are allowed; this should be contrasted with the fact that if ties are allowed, it is NP-hard to find a stable perfect matching [11,16,17].

### 3.2 Distributed Stable Matching

Everyone witnesses evolution of matchings in real-world and virtual-world social networks; in its simplest form, the matchings attempt to attain stability by switching along unstable edges. In a seminal work, Knuth [20] showed that such a switching may go in cycles, never resulting in a stable matching. Roth and Vande Vate [31] showed that switching _randomly_ almost surely leads to stability.

Note that switching partners along unstable edges can be done in a distributed manner. The Gale-Shapley algorithm is also parallel by its nature: the proposals/rejects can be undertaken by all men/women simultaneously during synchronised _rounds_ (albeit it can happen that only one man is free at a round [9, Section A.3], [34]). Lower bounds on the running time of the algorithm [9, Section 1.5] show that a linear number of rounds is required to attain stability. But can a _nearly_ stable matching be obtained with fewer rounds?

Several works have addressed the last question with experiments. Quinn [30] observes experimentally that a matching with only a fraction of unstable edges emerges long before the Gale-Shapley algorithm converges. Lu and Zheng [24] propose a parallel algorithm that outperforms the Gale-Shapley algorithm in practice. Theorem 1 gives theoretical support to the findings in<tbc>

