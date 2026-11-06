### 6.5 Memory footprint

Panorama precomputes per-point cumulative tail energies for the Cauchy-Schwarz bound: 4(_L_+1) bytes per point, O(_nL_) in total. The overhead per index family relative to the base storage is:

\(\bullet\) **IVFFlat** / **Refine**: \(\frac{L+1}{d}\) , dwarfed by the 4_d_-byte vector.<tbc>

\(\bullet\) **HNSW**: \(\frac{L+1}{d+2M_\mathrm{HNSW}}\) , where the \(2M_\mathrm{HNSW}\times 4\) bytes denominator term represents the memory overhead of each node’s graph topology (the adjacency lists). Because the graph structure itself consumes substantial memory, the relative Panorama overhead is further diluted compared to purely flat structures.<tbc>

\(\bullet\) **IVFPQ**: \(\frac{4(L+1)}{M_\mathrm{PQ}}\) , the only nontrivial case, since PQ codes are al ready 1B per dimension. While standard 8-bit scalar quantization could compress these values and cut the overhead by 4x, evaluating the impact of this quantization noise on the exactness of our accretive pruning bounds is left to future work.

## 7 EXPERIMENTAL RESULTS

We evaluate Panorama across three axes: (i) end-to-end QPS under fully-recall-preserving exhaustive search, (ii) QPS vs. recall when integrated into state-of-the-art indexes, and (iii) the isolated performance impacts of our algorithmic knobs and systems optimizations. Across these evaluations, Panorama consistently delivers tremendous performance, yielding up to a 28.9\(\times\) speedup over Faiss’ baselines while preserving the recall of the underlying index.

_Methodology._ We run three repetitions of 1000 10-NN queries randomly sampled from each benchmark’s query set and report averages. We evaluate all methods using a single thread on an Intel Xeon Gold 5416S CPU @ 2.0 GHz with 128 GB DDR5-6400 RAM, running Ubuntu 24.04 LTS. Binaries are compiled with GCC 13.3.0 using -03 and AVX-512 optimization. We wrap each Panorama index with Faiss’ IndexPreTransform to apply the PCA transformation and include its overhead in the reported query time. We also minimally modify the PDX source code to support batched queries, batched transformations, and feature-processing metrics.

### 7.1 Datasets and baselines

_Datasets._  2 lists the six benchmark datasets that we use; the two highest-dimensional datasets (**Ada**, **Large**) are OpenAI’s text-embedding-ada-002 and text-embedding-3-large.

_Baselines._ We compare Panorama against the following implementations for each index family:

\(\bullet\) **IVFFlat**: Faiss-IVFFlat, PDX-IVFFlat (including both ADSampling and BOND configurations).<tbc>

\(\bullet\) **IVFPQ**: Faiss-IVFPQ.<tbc>

\(\bullet\) **HNSW**: Faiss-HNSW, ADSampling-HNSW, KS2-HNSW.<tbc>

\(\bullet\) **Refine**: Faiss-FastScan-Refine.

PDX does not natively compose with PQ, leaving Faiss-IVFPQ as the sole baseline for that family; KS2-HNSW is the state-of-the-art graph baseline. We also implemented Panorama for Annoy \[8\] and MRPT \[22\] but omit their results for brevity, as their non-contiguous layouts mirror HNSW’s noncontiguous dynamics.

### 7.2 Speedup on exhaustive search

We first isolate Panorama’s algorithmic gains under exhaustive search (nprobe = nlist), where all methods reach their maximum recall (Figure 5). Operating with \(\varepsilon=1\) (the exact variant), Panorama- IVFFlat outperforms Faiss by 3.2\(\times\) on Deep and 5.7\(\times\) on SIFT, with the speedup trending up with dimensionality to 18.7\(\times\) on GIST and 17.2\(\times\) on Large; the gain reflects the growing share of query time spent in the refinement pass on high-dimensional embeddings. We compare against PDX-BOND rather than PDX’s default ADSampling configuration, as ADSampling probabilistically drops dimensions and loses recall at this target (Figure 12). By contrast, PDX-BOND employs exact bounds to preserve recall on every dataset; however, because its bounds are looser than Panorama’s, our approach widens the performance gap by an additional 2.0\(\times\) on Deep and 2.4\(\times\) on SIFT, up to 7.6\(\times\) on Ada and 11.2\(\times\) on GIST.

3 isolates this pruning efficiency: Panorama’s empirical fraction of dimensions scanned tightly tracks the theoretical \(1/\alpha\) prediction (Proposition 5.1). Conversely, lacking a spectrum- shaping transform, PDX-BOND’s heap-top bound remains loose, forcing it to evaluate 1.5-11.1\(\times\) more dimensions.

### 7.3 Main results: integrated indexes

Figures 6 and 7 plot QPS against recall for every index-dataset combination, organized by index family (rows) and dataset (columns). For each dataset, we select the \(\varepsilon\) that optimizes the QPS-recall trade- off. In the IVFFlat row, a star (⋆) denotes the peak QPS achieved at full recall (\(\varepsilon\)=1).

_IVFFlat._ Panorama outperforms PDX and Faiss across the entire recall range on the four highest-dimensional datasets, achieving<tbc>

\begin{tabular}{ccccc}
**Dataset** & **Semantics** & **Size** & **N. Queries** & **Dim.**\(\downarrow\) \\
Deep & Image embeddings & 9,990,000 & 10,000 & 96 \\
SIFT & Image features & 10,000,000 & 1,000 & 128 \\
arXiv & Text embeddings & 2,240,000 & 10,000 & 768 \\
GIST & Image features & 1,000,000 & 1,000 & 960 \\
Ada & Text embeddings & 900,000 & 100,000 & 1536 \\
Large & Text embeddings & 900,000 & 100,000 & 3072 \\
\end{tabular}

\begin{tabular}{ccccc}
**Dataset** & \(\alpha\) & **Theory (1/\(\alpha\))** & **Panorama** & **PDX-BOND** \\
Deep/96 & 3.6 & 28.1% & 25.6% & 39.0% \\
SIFT/128 & 6.9 & 14.6% & 12.7% & 38.8% \\
arXiv/768 & 8.3 & 12.1% & 7.5% & 46.5% \\
GIST/960 & 26.6 & 3.8% & 4.1% & 45.5% \\
Ada/1536 & 10.3 & 9.7% & 8.1% & 49.8% \\
Large/3072 & 12.2 & 8.2% & 6.1% & 36.2% \\
\end{tabular}

Panorama
PDX-BOND
FAISS
100
10
QPS
Deep/96
SIFT/128
arXiv/768
GIST/960
Ada/1536
Large/3072

** 2: Datasets used, sorted by dimensionality.**

**Figure 5: Throughput at exhaustive IVF probe (nprobe = nlist).**

** 3: Fraction of dimensions scanned at exhaustive IVF probe (nprobe = nlist).**

