# A Predictive Framework for Base-_n_ Radix Sort Optimization

**-** It is 1.30x faster than AFS, confirming that the iterative linear scanning of SP-LSD is architecturally superior to the recursive MSD approach for fixed-width integers.<tbc>

Surpassing Introsort, a hybrid-adaptive standard library algorithm with aggressive optimizations, using a core logical implementation suggests a significant algorithmic advantage for the target dataset. Unlike the approach of AFS, SP-LSD’s fine-grained, iterative pruning model capitalized on data skew without incurring heavy structural overhead. Consequently, despite Introsort’s efficiency on smaller arrays (\(n\le 10,000\)), SP-LSD is validated as the optimal choice for the target heavy-tailed dataset.

While the ‘standard’ adaptive approach (AFS) failed to outperform the baseline, SP-LSD bridged the gap to establish SP-LSD as the optimal algorithm for this dataset, proving that iterative binary pruning is the correct architectural choice for adaptive integer sorting.

### 7 Conclusion

In this paper, we tackled the zero-padding inefficiency in Base-_n_ Radix Sort by developing the Stable Partitioned LSD (SP-LSD) model. Through the Radix Crossover Framework (RCF), we deterministically established the asymptotic, round-feasibility and pruning crossovers where SP-LSD outperforms both comparison and non-comparison sorting algorithms on both skewed and uniform distributions. The practical implementation of the work is benchmarked with Introsort, BNRS, AFS and from the results found that for the input size exceeding 10,000, the proposed SP-LSD outperforms the competition in terms of execution time, repetitions, and overall operational cost. Future work will focus on extending the RCF to highly specialized high-performance systems, specifically exploring different optimization models targeting parallelization of the partition step and integrating within database query engines.

### References

