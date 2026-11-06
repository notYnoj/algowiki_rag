# Panorama: Fast-Track Nearest Neighbors

### ABSTRACT

Candidate _verification_ is the primary bottleneck in Approximate Nearest-Neighbor Search (ANNS) pipelines for high-dimensional neural embeddings. We introduce Panorama, a state-of-the-art refinement technique that accelerates verification by exploiting the inherent spectral decay of these embeddings. Using PCA to compact signal energy, Panorama evaluates candidate distances incrementally. At each step, it computes a strict lower bound on the full-vector distance, dynamically pruning candidates the moment this bound exceeds the running _k_-th nearest neighbor distance. While PCA’s concentration of variance facilitates pruning, it breaks the uniform-variance assumption required by Product Quantization (PQ). To resolve this, we introduce a variance-shaping step that redistributes energy across subvectors to render accretive refinement compatible with quantized indexes. Optimized for modern memory hierarchies via vectorized bulk-pruning and cache-conscious data layouts, Panorama has been upstreamed into the Faiss library across major index families (IVFPQ/Flat, HNSW, and Refine). Panorama achieves higher QPS at any target recall with a cost that provably scales inversely with dataset spectral decay, delivering end-to-end speedups of up to 28.9\(\times\) and outperforming probabilistic methods across all recall bands.

### 1 INTRODUCTION

The proliferation of large-scale neural embeddings has transformed machine learning applications, from computer vision and recommendation systems [27, 32] to bioinformatics [1] and retrieval- augmented generation (RAG) pipelines [18, 29]. As embedding models produce vectors with thousands of dimensions--OpenAI’s text-embedding-3-large [41] reaches 3072--the need for real-time Approximate Nearest-Neighbor Search (ANNS) intensifies.

_The refinement bottleneck._ Current ANNS methods fall into four major families: _graph-based_ (HNSW [37], DiskANN [43]), _clustering- and-quantization-based_ (IVFPQ [24, 25], ScaNN [20]), _tree-based_ (kd-trees [7], FLANN [40]), and _hash-based_ (LSH [3, 23], multi- probe LSH [35]). All families share a pipeline of two phases [5]: _filtering_ reduces the database to a set of candidates \(\Gamma\) and _refinement_ (verification) selects _k_ candidates nearest to the query. Prior work in ANNS has almost exclusively targeted the filtering phase, assuming that refinement is inconsequential. This assumption holds on low- dimensional embeddings; on modern neural embeddings, however,

refinement consumes most of end-to-end query latency, with the share rising monotonically in dimensionality [16].

_Why existing remedies underperform._ Prior work addresses the refinement bottleneck primarily through _probabilistic_ distance estimation: ADSampling [16] randomly subsamples coordinates, while FINGER and KS2 [11, 34] approximate inner products via angle estimation. Consequently, these methods hit a structural recall ceiling and cannot guarantee exact k-NN regardless of the time budget. Furthermore, they are poorly suited for cluster-based indexes that utilize sequential scans. PDX [28] mitigates the memory bottleneck via a columnar layout, yet suffers this same recall deficiency or, in its deterministic variant PDX-BOND, low throughput. Finally, none of these approaches composes with _product quantization_ (PQ) [25], a ubiquitous compression primitive in billion-scale ANNS. This paper introduces Panorama, a deterministic and hardware-friendly refinement method that eliminates this compromise. By providing a mathematically principled pruning bound, Panorama delivers superior throughput at _every_ target recall band--up to and including 100% recall--while natively integrating with PQ and other existing index families.

_Contributions._ Our contributions are as follows:

\(\bullet\) **Accretive refinement.** Panorama accumulates _L_<sub>2</sub> distance terms incrementally along the PCA basis, maintains tight Cauchy- Schwarz lower bounds on the fly, and prunes any candidate whose lower bound exceeds the running _k_th-nearest-neighbor threshold. This pruning is controlled by a tunable parameter \(\varepsilon\), exact at \(\varepsilon=1\), and relaxed for the sake of efficiency with \(\varepsilon<1\). This scheme fits into graph, tree, clustering, and hash-based indexes without changing their filtering phase.

\(\bullet\) **Theoretical grounding.** We show that the expected verification cost scales inversely with an exponential PCA decay factor observed in real-world embeddings (Proposition 5.1) and generalize this guarantee to out-of-distribution queries (Proposition 5.2).

\(\bullet\) **Compatibility with product quantization.** While PCA’s aggressive variance concentration aids pruning, it destabilizes downstream product quantization (PQ) and erodes recall. To counteract this, we apply an orthogonal transformation _R_ that flattens coordinate variances to a target diagonal \(t\prec\lambda\) while preserving covariance eigenvalues \(\lambda\). We construct _R_ by a Robin Hood sequence of Haar-random rotations that transfers surplus variance across PQ blocks, followed by an intra-block Haar-random rotation to reduce residual anisotropy. Together, these steps preserve PCA’s pruning efficacy while ensuring PQ compatibility.

<sup>†</sup>Denotes equal contribution.

Alexis Schlomer<sup>†</sup> Carnegie Mellon University aschlome@cs.cmu.edu

Akash K. Nayar<sup>†</sup> Carnegie Mellon University akashnay@cs.cmu.edu

Vansh Ramani<sup>†</sup> IIT Delhi & CMU & UCPH cs5230804@cse.iitd.ac.in

Sayan Ranu Indian Institute of Technology Delhi sayanranu@cse.iitd.ac.in

Jignesh M. Patel Carnegie Mellon University jigneshp@cs.cmu.edu

Panagiotis Karras University of Copenhagen piekarras@gmail.com

