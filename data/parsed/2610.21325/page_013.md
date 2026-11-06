### 4.8 Exact Search on an A100

The certificate of CertEx assumes only half-precision products with fp32 accumulation \[10\], which the tensor cores of other GPUs provide as well. We therefore repeat the exact search of SIFT1M, GIST1M, GloVe, and BIGANN- 10M with the same code on an NVIDIA A100 80GB PCIe GPU ( 2). The A100 runs as one MIG instance of the 7g.80gb profile, which provides 98 of its 108 streaming multiprocessors and its full memory. On this instance, CertEx searches the anchor strides 8, 16, and 32 at the widths around its H100 configuration. The baseline is the fastest configuration of the same cuVS \[47\] fp32 grid on the same instance.

On all four datasets, CertEx is exact for every query at \(8.8\times\) to \(11.8\times\) the throughput of the fastest cuVS fp32 configuration, against \(7.7\times\) to \(15.5\times\) on the H100. In addition, the boundary validation of Section 4.3 keeps every pair in all 24 runs. As on the H100, the largest speedup belongs to BIGANN-10M \[33\], the largest of the four datasets. Moving from the H100 to the A100, CertEx loses \(2.3\times\) to \(2.5\times\) of its throughput, whereas exhaustive search loses \(1.9\times\) on three datasets and \(2.75\times\) on the 960 dimensions of GIST1M. The speedup on GIST1M therefore rises from \(7.7\times\) to \(9.3\times\). Moreover, the fastest width changes on two datasets: GIST1M prefers _m_=379 instead of 507, and BIGANN-10M prefers _m_=59 instead of 123. Because the width affects only the cost, every width remains exact on both GPUs.

## 5 Conclusion

Exact kNN search for image retrieval, deduplication, and the memory of LLM agents has so far required either a full- precision distance to every vector or an index that gives up exactness. CertEx shows that exact search needs neither: a lifted lower bound with a certificate for its rounding error excludes almost every vector in one half-precision tensor- core pass without a false dismissal. On sixteen datasets of up to 100M vectors, CertEx is exact for every query at up to \(18.0\times\) the throughput of the fastest exhaustive GPU search. Exact search thus becomes a practical default for visual retrieval, deduplication, and representation evaluation.

## References

\begin{tabular}{cccccccccc}
Data & _N_ & _D_ & _m_ & _s_ & Surv. & CertEx & cuVS fp32 & A100 & H100 \\
SIFT1M & 1M & 128 & 123 & 8 & 91 & 312.1k & 34.7k & 9.0\(\times\) & \(11.0\times\) \\
GIST1M & 1M & 960 & 379 & 8 & 380 & 69.1k & 7.44k & 9.3\(\times\) & \(7.7\times\) \\
GloVe & 1.18M & 100 & 99 & 8 & 88 & 272.9k & 31.1k & 8.8\(\times\) & \(11.0\times\) \\
BIGANN-10M & 10M & 128 & 59 & 8 & 1531 & 40.8k & 3.46k & 11.8\(\times\) & \(15.5\times\) \\
\end{tabular}

2: Exact search on one A100 (_k_=10): fastest exact CertEx, fastest cuVS fp32, and speedups on both GPUs.

