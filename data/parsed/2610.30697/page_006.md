## 4 Evaluation

### 4.1 Experimental Setup

#### Datasets.

The evaluation covers eleven datasets of text and image embeddings and local descriptors, from one million to one billion vectors and from 96 to 960 dimensions, which test the certified screening on wide and narrow vectors at every scale ( 1). ImageNet DINOv2 holds the DINOv2 ViT-B/14 embeddings \[45\] of the training images of ImageNet \[11, 49\], queried by its validation images. GIST1M holds the 960-dimensional GIST descriptors \[43\] of the ANN-Benchmarks suite \[2\]. DataComp holds the CLIP ViT-L/14 embeddings \[47\] of 12.79 million web images of DataComp \[17\], which contain large groups of duplicate images. SIFT1M and the BIGANN prefixes hold the SIFT descriptors \[37\] of the BIGANN dataset \[30\] as 8-bit integers, the Deep1B prefixes hold the 96-dimensional image descriptors of Deep1B \[5\], and MS MARCO holds the 768-dimensional embeddings of its 8.8 million passages \[40\] by msmarco-distilbert-cos-v5 \[48\], normalized so that Euclidean distance ranks as cosine similarity, with the 6,980 labeled development queries. Ground truth is the exact top 10, which an exhaustive float64 search provides for the Deep1B prefixes and corrects for three queries of the official Deep1B list.

#### Platforms.

The experiments run on two GPU servers with the same GPU model and software stack, namely CUDA 12.6 with driver 560.35, PyTorch 2.14, and cuVS 26.10. The first server has one NVIDIA H100 GPU \[41\] with 94 GB of memory, 48 cores of an Intel Xeon Platinum 8468 processor, and 240 GB of host memory. It runs Lychee, IVF-Flat, IVF-PQ, and CAGRA on ImageNet DINOv2, SIFT1M, BIGANN-10M, BIGANN-100M, and DataComp, together with the width and list studies on ImageNet DINOv2 and SIFT1M. The second server has four H100 GPUs of the same model, which NVLink connects pairwise, 192 cores of the same processor, and 960 GB of host memory. It runs every method on GIST1M, Deep-10M, and Deep- 100M, the remaining baselines on the other datasets, and the billion-scale experiments on all four GPUs; every single- GPU experiment uses one of its GPUs. Every search pro<tbc>

<tbc>cesses all queries of a dataset at once.

#### Metrics.

Recall at 10 is the fraction of the true 10 nearest neighbors in the returned list, averaged over the queries. On DataComp, whose duplicate images make the ids of tied neighbors interchangeable, a returned vector counts as a true neighbor if its distance is at most the 10th true distance, as in standard benchmarks with ties \[52\]. Throughput is the number of queries divided by the wall-clock time of the search, including the probe, the screening, and the verification, as the best of two or three runs after one warm-up run. The throughput of one configuration differs by up to 4% between the separately timed runs of different sections. Exactness is checked separately: on every dataset, at 1 to 128 probed lists, every answer of Lychee equals the float64 top 10 of its probed lists, with the same ids or the same distances under ties, for 1,000 queries per dataset of up to ten million vectors and 500 per larger dataset.

#### Baselines.

The evaluation compares Lychee against ten baselines that cover the inverted-file, graph, and exhaustive families on GPUs and CPUs ( 2). IVF-Flat of cuVS \[42\] scans the probed lists at full precision and computes the answer of Eq. (2) in float32 on its own _k_-means lists. IVF-PQ compresses the vectors to _D/_2 bytes of 8-bit codes, and IVF- SQ quantizes every coordinate to 8 bits; both refine their top 4_k_ candidates with the full vectors. IVF-RaBitQ \[18, 19, 51\] stores 7-bit extended RaBitQ codes and runs with and without the same refinement; it failed to build on DataComp. CAGRA \[44\] builds a graph of degree 64 and sweeps its search width from 16 to 512, on every dataset except DataComp, whose duplicate groups made the CAGRA build fail. The exhaustive search of cuVS computes all float32 distances. On the CPU, the IVF-Flat index of Faiss \[14\], the HNSW index of hnswlib \[38\] with 32 links per node and a construction width of 200, and ScaNN \[26\] with its anisotropic 4-bit quantization and exact reordering run on all 192 cores of the second server. Finally, CertEx \[64\] returns the exact top 10 over the whole dataset by certified exclusion on one GPU. The IVF indexes use the lists of  1 and sweep the number of probed lists from 1 to 500, or to 1,000 on the datasets of 100 million vectors, whereas HNSW sweeps its search width from 16 to 1,024.

\begin{tabular}{cccccc}
Dataset & Vectors & Dim. & Type & Queries & Lists \\
ImageNet DINOv2 & 1.28M & 768 & float32 & 50,000 & 1,024 \\
GIST1M & 1M & 960 & float32 & 1,000 & 1,024 \\
SIFT1M & 1M & 128 & float32 & 10,000 & 1,024 \\
Deep-10M & 10M & 96 & float32 & 10,000 & 4,096 \\
BIGANN-10M & 10M & 128 & uint8 & 10,000 & 4,096 \\
MS MARCO & 8.8M & 768 & float32 & 6,980 & 4,096 \\
DataComp & 12.8M & 768 & float32 & 10,000 & 4,096 \\
Deep-100M & 100M & 96 & float32 & 10,000 & 16,384 \\
BIGANN-100M & 100M & 128 & uint8 & 10,000 & 16,384 \\
BIGANN-1B & 1B & 128 & uint8 & 10,000 & 4 \(\times\) 16,384 \\
Deep1B & 1B & 96 & float32 & 10,000 & 4 \(\times\) 16,384 \\
\end{tabular}

\begin{tabular}{ccc}
Baseline & Index and hardware & Answer \\
IVF-Flat (cuVS) & inverted lists, GPU & probed top 10 \\
IVF-PQ + refine (cuVS) & quantized lists, GPU & approximate \\
IVF-SQ + refine (cuVS) & quantized lists, GPU & approximate \\
IVF-RaBitQ (cuVS) & RaBitQ lists, GPU & approximate \\
CAGRA (cuVS) & proximity graph, GPU & approximate \\
Brute force (cuVS) & exhaustive float32, GPU & exact (float32) \\
IVF-Flat (Faiss) & inverted lists, CPU & probed top 10 \\
HNSW (hnswlib) & proximity graph, CPU & approximate \\
ScaNN & quantized partitions, CPU & approximate \\
CertEx & certified exclusion, GPU & exact \\
\end{tabular}

1: The eleven datasets of the evaluation.

2: The baselines and their answers.

