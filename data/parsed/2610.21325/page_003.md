<tbc>among tree and k-means partitions. In contrast, graph indexes such as HNSW \[43\], DiskANN \[63\], SONG \[75\], GGNN \[26\], and CAGRA \[49\] walk a proximity graph toward the query. Benchmarks \[5, 60\] accordingly rank these methods by recall at a given throughput, whereas CertEx examines every vector and returns exact results.

#### Nearest neighbors in visual recognition.

Visual recognition uses nearest neighbors as a component whose errors enter the task metric. For instance, object retrieval \[3, 32, 53, 62\] is evaluated against exhaustive ground truth \[55\]. Similarly, copy detection \[17, 54\] and dataset curation \[1, 21\] remove near and semantic duplicates from web-scale corpora. In representation learning, weighted kNN classifiers evaluate self-supervised representations \[12, 50, 61\]. Retrieval-augmented classification \[41\] even feeds the retrieved neighbors into the model. In practice, these pipelines obtain their neighbors from approximate indexes, cluster-restricted comparisons, or kNN graphs of fixed degree. In contrast, CertEx returns exact neighbors faster than exhaustive search and answers deduplication with an exact similarity self-join (Section 3.6).

#### Foveation and certified low-precision arithmetic.

Vision models allocate resolution unevenly, for instance through recurrent glimpses \[45\], foveal-peripheral segmentation \[2\], or foveated rendering \[27, 31\]. Numerical computing allocates precision in the same way, for instance in mixed-precision training \[44\]. Computational geometry goes further: its floating-point filters evaluate a predicate in fast arithmetic together with an error bound \[10, 29\] and fall back to exact arithmetic only near zero \[20, 59\]. Following this idea, CertEx folds the error bound into the same half- precision product, so that every low-precision decision of CertEx carries a proof of no false dismissal, unlike approximate foveation.

## 3 Methodology

### 3.1 Overview

Exact kNN search must examine all _N_ database vectors, although only the few vectors near the query need full precision. Human vision solves the same problem by dividing its work between two parts of the retina \[13\] (Figure 2(a)): the periphery covers the whole scene at low resolution, whereas the fovea sees only one spot at full resolution. Our exact kNN method divides its work in the same way (Figure 2(b)). We call this method CertEx, which stands for certified exclusion.

The left half of Figure 2(b) shows the retina of CertEx, which stores one half-precision vector \(\hat{\mathbf{x}}\) for each of the _N_ database vectors **x**. We call \(\hat{\mathbf{x}}\) the _retina vector_ of **x**. The first part of \(\hat{\mathbf{x}}\) keeps a few principal coordinates of **x** and summarizes the rest by one norm. We call this part the _lifted projection_ of **x** (Section 3.3). The inner product of two lifted projections determines a lower bound on the distance between their vectors. Although half precision is the fastest arithmetic of GPU tensor cores \[10\], rounding to half precision can overestimate the distance of a true neighbor. To guard against this error, the second part of \(\hat{\mathbf{x}}\) records how large the rounding error of \(\hat{\mathbf{x}}\) can be. We call this part the _certificate_ of \(\hat{\mathbf{x}}\). With the certificate, the test excludes a vector only if the vector would be excluded even under the worst possible rounding. Moreover, the tensor cores evaluate this worst case within the same product (Section 3.4). Concretely, a tensor-core pass over the retina keeps a vector **x** only if \(\langle\hat{\mathbf{q}},\hat{\mathbf{x}}\rangle\ge\theta(\mathbf{q})\), where the retina vector \(\hat{\mathbf{q}}\) encodes the query **q** in the same form as \(\hat{\mathbf{x}}\) and the threshold \(\theta(\mathbf{q})\) follows from an upper bound _U_ on the distance of the _k_-th nearest neighbor (Section 3.5). Because _U_ is needed before the pass, CertEx obtains it from a few sampled vectors. The test of each vector therefore depends on no other database vector, so that one pass over the retina decides all _N_ vectors without ranking them. We call this pass the _retina pass_. As Figure 2(b) shows, the pass excludes most vectors (crosses) but never a true neighbor; we call the kept vectors (checks)<tbc>

(a) Human vision
(b) CertEx
Retina: all N vectors, half precision
Fovea: survivors, full precision
q
x
#1
#2
peripheral retina: wide, coarse
lifted projection
certificate
original vector
exact distance
 fovea: one spot, sharp
one tensor-core pass: keep if (q, x) 2 (q)
#1, #2: the exact k nearest (k = 2)

Figure 2: Overview of CertEx and the visual system that motivates it.

