<tbc>and IVF-RaBitQ with refinement) lag by \(7.7\times\) to \(35\times\), because every query still scans the codes of all its probed vectors. Graph-based CAGRA saturates at recall 0.986 on DINOv2 and 0.996 on GIST1M, where Lychee delivers \(6.3\times\) and \(6.8\times\) higher throughput at higher recall. On SIFT1M and Deep-10M, Lychee is \(19.7\times\) and \(30\times\) faster than IVF-Flat at _n<sub>p</sub>_=200; although CAGRA is faster at lower recall (\(\le 0.995\)) on SIFT1M, it saturates at recall 0.9992, where Lychee delivers \(3.6\times\) higher throughput at recall 0.9998.

Figure 6 compares Lychee with CPU indexes running on all 192 cores of the second server. ScaNN, the strongest CPU baseline, reaches recall 0.999 at 18,866 QPS on DINOv2 and 105,628 on SIFT1M (\(11.7\times\) and \(5.7\times\) below Lychee), and saturates at recall 0.985 on GIST1M and 0.9987 on BIGANN-10M (\(45\times\) and \(23\times\) below Lychee). HNSW reaches at most recall 0.998 on DINOv2 and 0.992 on GIST1M, trailing Lychee by \(14\times\) to \(15\times\) at recall 0.999 on SIFT1M and BIGANN-10M. Faiss IVF-Flat serves 205 to 5,594 QPS at recall 0.999, which is \(108\times\) to \(894\times\) below Lychee.

Figure 7 extends the evaluation to BIGANN-10M, BIGANN-100M, Deep-100M, and DataComp, where probed lists contain up to one million vectors per query. Lychee is \(9.7\times\) to \(10.4\times\) faster than IVF-Flat at _n<sub>p</sub>_=200, widening to \(25\times\) on BIGANN-100M (\(75,053\) vs 2,959 QPS at recall 0.9998) and \(65\times\) on Deep-100M (\(67,548\) vs 1,036 QPS at recall 0.9997) with full vectors in pinned host memory. Quantized indexes lag by \(14\times\) to \(42\times\), while CAGRA saturates at recall 0.998 on BIGANN-100M and 0.996 on Deep-100M. On DataComp, Lychee serves 75,565 QPS at recall 0.997 (\(63\times\) faster than IVF-Flat, reaching \(107\times\) at _n<sub>p</sub>_=500). At recall 0.999 on DataComp, Lychee is also \(18\times\) faster than the exact search of CertEx, which answers 3,126 queries per second. Exact brute-force search is \(36\times\) to \(246\times\) slower than Lychee at recall 0.999 and suffers from float32 distance inaccuracies that return incorrect top-10 neighbors on Deep-10M and Deep-<tbc>

<tbc>100M.

## 4.4 Data Size Scalability

Figure 8 plots the throughput at recall 0.999 against the number of vectors on the BIGANN and Deep1B prefixes, which tests the cost analysis of Section 3.6. The exact methods screen or scan every vector, so that their throughput falls in proportion to the dataset: CertEx answers 449,676, 168,264, and 19,427 queries per second on SIFT1M, BIGANN-10M, and BIGANN-100M. Lychee instead screens only the probed lists, whose share of the dataset shrinks as the dataset grows, so that its throughput at recall 0.999 reaches \(1.3\times\), \(2.0\times\), and \(5.7\times\) that of CertEx on the same three datasets.

The Deep1B prefixes show the same trend. Lychee is \(1.9\times\) faster than CertEx on Deep-10M and \(5.0\times\) faster on Deep- 100M, with the full vectors of Deep-100M in host memory. IVF-Flat, in contrast, stays \(10\times\) to \(69\times\) below Lychee at recall 0.999 on all five prefixes, because it reads every vector of the probed lists at full precision. Lychee is there-<tbc>

Lychee ScaNN (CPU) HNSW (CPU) IVF-Flat (Faiss) ImageNet DINOv2
GIST1M
100k
100k
10k
10k
Queries per second
1k
1k
100
100
.9
.99
.999
.9999
.9
.99
.999
.9999
SIFT1M
BIGANN-10M
1M
100k
100k
Queries per second
10k
1k
1k
1k
.9
.99
.999
.9999
.9
.99
.999
.999
Recall at 10
Recall at 10

Lychee
IVF-Flat
CAGRA
IVF-PQ + ref.
IVF-SQ + ref.
IVF-RaBitQ + ref.
CertEx (exact)
BIGANN-10M
BIGANN-100M
1M
1M
100k
100k
Queries per second
10k
10k
10k
.9
.99 .999.9999 exact
.9
.99 .999.9999 exact
Deep-100M
DataComp
100k
1M
100k
10k
Queries per second
10k
10k
1k
1k
.9
.99 .999.9999 exact
.9
.99 .999.9999 exact
Recall at 10
Recall at 10

Lychee
IVF-Flat
IVF-PQ + ref.
CertEx (exact)
Brute force
BIGANN, recall 0.999
Deep1B, recall 0.999
100k
100k
Queries per second
10k
10k
1k
1k
106
107
108
107
108
Vectors
Vectors

Figure 6: Throughput vs. CPU baselines on 192 cores.

Figure 7: Recall at 10 and throughput on 10M-100M datasets.

Figure 8: Throughput at recall 0.999 against dataset size.

