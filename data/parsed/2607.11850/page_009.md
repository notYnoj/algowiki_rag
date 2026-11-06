<tbc>datasets. As shown in Section 5, NFS Sort is highly competitive with established state-of-the-art sorting algorithms. Most notably, it consistently outperforms recent learned sorting techniques, such as Balanced Learned Sort (BLS), particularly on smaller datasets, while maintaining comparable and highly efficient performance on larger scales. Against other non-learned state-of-the-art sorts, NFS Sort is competitive or better across all scales.

Ultimately, NFS Sort successfully combines the theoretical advantages of distribution sorting with modern memory-management techniques to meet the practical demands of contemporary software systems. Future work could explore extending the algorithm’s distribution logic to non-numeric keys, parallelizing the recursive scatter steps to leverage multi-core architectures, and further fine-tuning the fallback heuristics for specialized hardware environments.

## A Naive NFS Sort Pseudocode

## References

\begin{tabular}{ccc}
Distribution & \(M=(b-a)\|f\|_\infty\) & Bound on B\[_D_\] \\
Uniform on \[0,10000\] & 1 & ≈3.00 \\
Normal, N(5000,250<sup>2</sup>) & 15.96 & ≈3.00 \\
Truncated exponential, \(\lambda=1/1000\) & 10.00 & ≈3.00 \\
Mixture distribution & 4950.01 & ≈4.00 \\
\end{tabular}

