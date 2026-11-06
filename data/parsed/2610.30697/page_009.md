<tbc>fore the method of choice when a dataset is too large for exact screening of every row, while CertEx remains the exact choice for datasets of a few million vectors.

## 4.5 Billion-Scale Search on Multiple GPUs

Figure 9 evaluates one billion vectors on the four GPUs of the second server, which tests whether the gain of Lychee holds at the scale of the largest public benchmarks [52]. Both methods split the dataset into four contiguous shards of 250 million vectors with 16,384 _k_-means lists each, one shard per GPU. A query probes the _n<sub>p</sub>_ nearest lists of every shard, every shard returns the exact top 10 of its probed lists, and the host merges the four answers by distance. Lychee keeps the full vectors of its shard in pinned host memory and only its lifted rows and anchors on its GPU, whereas IVF-Flat keeps its shard on the GPU.

On BIGANN-1B, Lychee answers 21,108 queries per second at recall 0.998 (_n<sub>p</sub>_=200), 16,615 at recall 0.9998 (_n<sub>p</sub>_=500), and 13,032 at recall 0.9999 (_n<sub>p</sub>_=1,000), against 1,455, 583, and 293 for IVF-Flat, which is 14.5\(\times\), 28.5\(\times\), and 44.5\(\times\) faster at equal recall. The build of Lychee takes 122 s against 398 s for IVF-Flat. On Deep1B, a float32 shard of 250 million vectors occupies 96 GB and exceeds the memory of an H100, so that IVF-Flat cannot build its index on the four GPUs. The lifted rows and anchors of Lychee occupy about 70 GB per GPU, and Lychee answers 59,466 queries per second at recall 0.998, 43,333 at recall 0.9996, and 32,082 at recall 0.9999 after a build of 270 s. Lychee therefore searches one billion float32 vectors on a single server at recall 0.9999, a configuration that the full-precision lists of IVF-Flat cannot hold.

## 4.6 Workload per Query

Figure 10 counts the probed vectors, the survivors of the certified screening, and the verified vectors per query as _n<sub>p</sub>_ grows, which tests the cost model of Section 3.6. On ImageNet DINOv2, the probed vectors grow from 1,361 to 653,749 per query in proportion to _n<sub>p</sub>_, while the survivors grow from 602 to 2,905 and the verified vectors only from 131 to 152. On BIGANN-10M, the probed vectors grow to 1,206,157 per query, whereas the survivors stay below 330 and the verification ends after its first round of 32 vectors. The lists that a larger _n<sub>p</sub>_ adds lie far from the query, so that<tbc>

<tbc>their vectors fail the certified test and never reach the verification. At _n<sub>p</sub>_=200 on ImageNet DINOv2, Lychee therefore reads 151 full vectors per query against 282,650 for IVF-Flat, 1,870 times fewer.

Survivors grow faster than verified vectors because the list-local threshold is looser than the final _k_-th distance. However, ordered verification (Algorithm 1) sorts survivors by lower bound and halts once a bound reaches the running _k_-th distance, reading 16.0\(\times\) fewer vectors than verifying all survivors on ImageNet DINOv2 (_n<sub>p</sub>_=200,  3).

## 4.7 Build Time and Host-Resident Vectors

Figure 11 reports the build time of every index and the throughput of the host-resident configuration, which test the cost of the index and the memory that it needs. The build time of Lychee covers the _k_-means training and assignment of its lists followed by one projection and encoding pass, building in 0.6 to 1.6 s on datasets up to 10M vectors and 12.4 s on BIGANN-100M. In contrast, CAGRA requires 1.9 to 20.3 s on smaller datasets and 362.7 s on BIGANN-100M (29\(\times\) slower), while HNSW needs 10.2 to 185.8 s on 192 CPU cores. Lychee’s index is therefore ready in seconds wherever a graph index takes minutes.

The host-resident configuration keeps full vectors in pinned host memory and only lifted rows and anchors on the GPU, reading survivors over PCIe. On ImageNet DINOv2, this uses 2.0 GB GPU memory (vs 3.9 GB for float32 vectors) while serving 74,627 QPS at recall 0.999 (_n<sub>p</sub>_=200, 22\(\times\) faster than device-resident IVF-Flat). On BIGANN-10M, it retains 95% of device throughput at 200 probed lists. De<tbc>

IVF-Flat, 4 GPUs
Lychee, 4 GPUs
BIGANN-1B
Deep1B
100k
10k
Queries per second
1k
IVF-Flat: shards exceed the memory of a GPU
.9
.99
.999
.999
.999
Recall at 10
Recall at 10

Probed (IVF-Flat)
Survivors
Verified (Lychee)
ImageNet DINOv2
BIGANN-10M
106
106
104
104
Vectors per query
102
100
101
102
100
101
102
Probed lists
Probed lists

Lychee IVF-Flat IVF-PQ CAGRA
DINOv2
BIG-10M
Index build
Full vectors on host
104
500k
Build time (s)
200k
102
Queries per second
100k
50k
100
20k
1
10
100
500
DINOv2
GIST
SIFT
Deep-10M
BIG-10M
BIG-10M
Probed lists

Figure 9: Billion-scale search on four H100 GPUs.

Figure 10: Probed, surviving, and verified vectors per query.

Figure 11: Index build time and host-resident throughput.

