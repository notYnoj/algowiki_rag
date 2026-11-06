cuVS fp32 configuration rises monotonically from 11.0\(\times\) to 18.0\(\times\), because only the retina pass scales with _N_ whereas the anchors and the fovea cost nearly the same at every size. At 99.9% exact queries (Figure 3(b)), CertEx is 27.2\(\times\) to 84.9\(\times\) faster than IVF-Flat [62], 3.7\(\times\) to 124\(\times\) faster than IVF-PQ [37], and 2.3\(\times\) to 10.7\(\times\) faster than IVF- RaBitQ [22], which is the strongest index on the ImageNet embeddings. Moreover, CertEx is exact for all queries on every dataset, whereas CAGRA [49] reaches this level only on SIFT1M among the thirteen datasets on which it can be built. In addition, the retina is built in 0.03 to 2.47 seconds, against 2.2 to 29.7 seconds for each CAGRA graph. On the 12.79M DataComp images [21], CertEx is the only method that is exact for every image query. Finally, Figure 3(c) compares the survivors of all datasets and BIGANN strides with the estimate _ks_. Specifically, survivors lie at most 1.15\(\times\) above _ks_ wherever the width nears the dimension and further above it for narrow widths (Proposition 5).

## 4.3 Ablation of the Design Elements

We then ask where the speed of CertEx comes from and what its certificate costs, with every element isolated on the same kernel and threshold (Figure 4). For 2048 queries, a complete CertEx search takes 5.0 ms against 37.2 ms for exhaustive search on SIFT1M and 170 ms against 3.6 s on BIGANN-100M, of which the anchors and the fovea take only 2.2 ms and 22 ms (Figure 4(a)). Most of the remain<tbc>

<tbc>ing time therefore belongs to the retina pass, which costs less than a plain fp16 matrix multiplication (GEMM) over the same vectors (2.3 ms against 4.1 ms on SIFT1M and 148 ms against 289 ms on BIGANN-100M) because it compares every product with its threshold inside one kernel instead of writing the matrix of all products. In contrast, exhaustive search must select the top 100 candidates among all _N_ products, which costs 3.3\(\times\) to 12.5\(\times\) the GEMM alone. Moreover, the ablation in Figure 4(b) shows that certified exclusion provides most of the speed: the top-_k_ selection instead slows the pass by 5.6\(\times\) to 24.3\(\times\), whereas TF32 instead of fp16 and the width _D_ instead of _m_ slow it by only 1.2\(\times\) to 1.5\(\times\) and 1.1\(\times\) to 2.1\(\times\).

In addition, the certificate makes the half-precision decision exact (Figure 4(c)). The hardest test places every pair exactly on the decision boundary: for four million random pairs per dataset and width, we set the threshold of each pair to its own lower bound. In this test, the retina keeps every pair, whereas the same retina without the error terms of Eq. (10) excludes 1.996M to 2.007M of the 4M pairs, because half-precision rounding errs in either direction with equal frequency. Moreover, the largest accumulation error over up to 10<sup>8</sup> pairs per dataset and every kernel configuration is 0.42% to 0.76% of the certified bound, so that the certificate holds with a margin of more than two orders of magnitude. The certificate costs only 0.4% to 2.7% of throughput, yet it decides real boundary pairs: without it, the exact self-join of the DINOv2 [50] embeddings misses

(a) scaling
(b) all methods at 99.9% exact queries
(c) survivors
11.0x
106
cuVS fp32
105
106
15.5x
fp16 + rerank
DataComp
18.0x
104
105
IVF-Flat
104
50M, 100M
Exact QPS
102
cuVS fp32
QPS, 99.9% exact
IVF-PQ
103
m=59
104
RaBitQ
CertEx, m=123
CAGRA
GIST
CertEx, m=59
KS
102
103
CertEx
1M
10M
100M
101
102
BIGANN database size
SIFT1M
GloVe
Deep
DINOv2
DataComp
KS (anchor prediction)
BIGANN-10M

(a) time per batch
(b) ablation
(c) certificate
4
no certificate
104
104
exhaustive search retina pass
24.3x
Certified
Latency (ms)
3
3601
Retina latency (ms)
2.1x
with top-k selection
1.996
170
16.0x
with TF32
1.2x
2
102
37.2
60.4
102
5.6x
with width D
1.998
2.007
1.997
2.000
14.5
1.5x
1.1x
1
5.0
1.2x
1.5x
100
0
0
0
0
0
0
0
0
SIFT1M DINOv2 BIGANN 100M
SIFT1M DINOv2 BIGANN 100M
SIFT
GloVe Deep
DINOv2
Deep
DINOv2

Figure 3: Scaling with _N_, all methods at 99.9% exact queries (\(\times\): never reached), and survivors against _ks_ (dashed).

Figure 4: Time per batch of 2048 queries, ablation of the retina pass, and violations without the certificate.

