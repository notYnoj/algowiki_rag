<tbc>queries, the retina pass evaluates only the pairs (**x**_<sub>i</sub>,_**x**_<sub>j</sub>_) with _i\<j_, so that each pair is tested once. In practice, the radius _r_ follows from the criterion of deduplication pipelines such as SemDeDup \[1\], which keep the pairs whose cosine similarity is at least \(\tau\). For unit vectors, such as normalized image embeddings, this criterion corresponds to the radius \(r=\sqrt{2-2\tau}\). Because the self-join is defined by a radius rather than by a number of neighbors, it places no limit on the number of duplicates per vector. In contrast, a kNN graph keeps at most _k_ neighbors of each vector and therefore misses every duplicate beyond the _k_-th neighbor.

## 4 Evaluation

### 4.1 Experimental Setup

#### Datasets and encoders.

The evaluation covers sixteen descriptor, word, and image-embedding datasets that span dimension and scale ( 1). Specifically, SIFT1M, GIST1M, and the BIGANN prefixes up to 100M vectors \[33, 37\] contain SIFT \[42\] and GIST \[48\] descriptors, whereas Deep-image \[72\] and GloVe \[52\] contain 9.99M CNN descriptors and 1.18M word embeddings. Moreover, the ImageNet-1K datasets \[15, 57\] use 1.28M training images as the database and 10,000 validation images as queries, both embedded by seven vision encoders, which are vision transformers \[16\] of the CLIP \[56\], SigLIP \[73\], DINOv2 \[50\], and DINOv3 \[61\] families. In addition, a cross-modal workload queries the CLIP image embeddings with 10,000 CLIP text prompts of the 1,000 class names. At web scale, DataComp \[21\] contributes the CLIP ViT-L/14 embeddings of 12.79M web image-text pairs with 10,000 image and caption queries.

#### Platform, metrics, and baselines.

Unless stated otherwise, every experiment runs on one NVIDIA H100 GPU with the kernels of CertEx written in Triton \[64\] on top of PyTorch \[51\]. Section 4.8 repeats four datasets on an A100, at 8.8\(\times\) to 11.8\(\times\) cuVS. Every experiment keeps the<tbc>

<tbc>database in device memory next to the retina, which adds 2(_m_+5) bytes per vector. Because the fovea reads only the survivors, the database could also reside in host memory. Throughput counts the queries per second over all queries with _k_=10 after a warm-up pass. For exactness, we recompute the squared distances of the returned neighbors by direct differences in fp64 and call a query exact when these sorted distances equal those of the true neighbors to a relative 10<sup>-12</sup>, which accepts ties among equidistant vectors and no other deviation. The true neighbors come from an fp64 search that is reranked by direct differences in fp64. We compare CertEx with six GPU baselines: the exhaustive search of NVIDIA cuVS \[47\] in fp32 at its fastest selection size, the same search in half precision with exact reranking, and the cuVS indexes IVF-Flat \[62\], IVF-PQ \[37\], IVF- RaBitQ \[22\], and CAGRA \[49\]. For a fair comparison, each baseline uses the best configuration of a grid, with exact reranking for the quantized indexes, as does CertEx with a few widths and anchor strides per dataset.

### 4.2 Exact Search Throughput

We next compare the exact throughput of CertEx with exhaustive cuVS search in fp32 and in fp16 with exact reranking ( 1). On all sixteen datasets, CertEx is exact and 7.1\(\times\) to 18.0\(\times\) faster than the fastest cuVS \[47\] fp32 configuration. In contrast, exhaustive fp32 search evaluates the expanded distance in fp32, which leaves 1 to 108 of the 10,000 queries inexact on ten of the datasets. Half- precision exhaustive search with exact reranking remains 1.8\(\times\) to 12.9\(\times\) slower than CertEx, so that half precision explains only part of the speed. Another part comes from the width, because the ImageNet embeddings concentrate their variance in fewer directions than their dimension and therefore leave only 139 to 327 survivors per query. Conversely, isotropic data enlarge the term \(4\rho(\mathbf{q})\rho(\mathbf{x})\) of Proposition 5 and thus the survivors.

Figure 3 then varies the database size and compares all methods. On seven BIGANN prefixes \[33\] from 1M to 100M vectors (Figure 3(a)), the speedup over the fastest<tbc>

\begin{tabular}{ccccccccccccccccc}
 & & & & \multicolumn{2}{c}{CertEx} & \multicolumn{2}{c}{cuVS fp32} & fp16 + rerank & & & & & & \multicolumn{2}{c}{CertEx} & \multicolumn{2}{c}{cuVS fp32} & fp16 + rerank \\
Data & _N_ & _D_ & _m_ & QPS & inexact & speedup & speedup & ImageNet & _N_ & _D_ & _m_ & QPS & inexact & speedup & speedup & speedup \\
SIFT1M & 1M & 128 & 123 & 719.6k & 0 & 11.0\(\times\) & 8.0\(\times\) & CLIP-B & 1.28M & 512 & 507 & 195.1k & 1 & 7.5\(\times\) & & 3.4\(\times\) \\
GIST1M & 1M & 960 & 507 & 157.6k & 0 & 7.7\(\times\) & 2.4\(\times\) & CLIP-L & 1.28M & 768 & 507 & 179.6k & 2 & 9.1\(\times\) & & 3.5\(\times\) \\
GloVe & 1.18M & 100 & 99 & 642.8k & 1 & 11.0\(\times\) & 8.7\(\times\) & SigLIP & 1.28M & 1152 & 635 & 157.7k & 4 & 10.9\(\times\) & & 3.6\(\times\) \\
Deep-image & 9.99M & 96 & 95 & 104.1k & 3 & 14.3\(\times\) & 11.2\(\times\) & DINOv2-B & 1.28M & 768 & 635 & 152.2k & 0 & 7.7\(\times\) & & 3.0\(\times\) \\
BIGANN-10M & 10M & 128 & 123 & 103.3k & 0 & 15.5\(\times\) & 11.1\(\times\) & DINOv2-L & 1.28M & 1024 & 891 & 121.0k & 2 & 7.7\(\times\) & & 2.6\(\times\) \\
BIGANN-100M & 100M & 128 & 59 & 12.0k & 0 & 18.0\(\times\) & 12.9\(\times\) & DINOv3-L & 1.28M & 1024 & 763 & 131.3k & 1 & 8.4\(\times\) & & 2.9\(\times\) \\
DataComp img. & 12.79M & 768 & 507 & 14.1k & 108 & 7.1\(\times\) & 2.3\(\times\) & DINOv3-7B & 1.28M & 4096 & 3579 & 36.2k & 2 & 7.9\(\times\) & & 1.8\(\times\) \\
DataComp txt. & 12.79M & 768 & 635 & 18.1k & 1 & 9.1\(\times\) & 2.9\(\times\) & CLIP text & 1.28M & 512 & 507 & 192.5k & 0 & 7.4\(\times\) & & 3.4\(\times\) \\
\end{tabular}

1: Exact search (_k_=10, one H100): QPS of CertEx, inexact queries of cuVS fp32, and speedups of CertEx over both baselines.

