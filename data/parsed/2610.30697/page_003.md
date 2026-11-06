#### Graph indexes.

Graph indexes such as NSG \[16\], HNSW \[38\], DiskANN \[54\], Starling \[59\], and their filtered variants \[22, 46\] visit few vectors per query through greedy search on a neighborhood graph built by methods such as NN-Descent \[13\]. On GPUs, SONG \[65\], GGNN \[23\], CAGRA \[44\], BANG \[55\], and PilotANN \[25\] parallelize the search. Surveys \[58\] and benchmarks \[2, 52\] show that graph searches reach high throughput at moderate recall but saturate as the search width grows. Lychee instead reaches the recall of the inverted lists at every _n<sub>p</sub>_, up to 0.9999 on DINOv2, with a cost that grows with the survivors of the screening.

#### Exact search and lower bounds.

Lower-bounding filters for exact search date back to the GEMINI framework \[15\], the VA-file \[60\], metric trees such as AESA \[56\], vp-trees \[62\], M-trees \[10\], and cover trees \[8\], and iDistance \[29\], which exclude candidates whose lower bound exceeds a current threshold. In high dimensions these bounds lose their power \[7, 60\], so that GPU exact search falls back to brute force \[20, 31\]. CertEx \[64\] restores the power of the lower bound in high dimensions through a principal-component lift with a rounding certificate for tensor cores. Lychee applies this bound inside the probed lists of an IVF index under a list-local threshold, which yields the answer of IVF-Flat on the same lists.

## 3 Methodology

### 3.1 Preliminaries and Background

#### Inverted-file search.

An inverted-file index \[32, 53\] partitions a dataset \(\mathcal{X}=\{\mathbf{x}_1,\dots,\mathbf{x}_N\}\subset\mathbb{R}^D\) into _P_ lists _L_<sub>1</sub>_,...,L<sub>P</sub>_ around centers **c**<sub>1</sub>_,...,_**c**_<sub>P</sub>_ from _k_-means, assigning every vector to its nearest center. A query **q** ranks the centers by distance and probes the _n<sub>p</sub>_ nearest ones. The probed lists form the candidate set _S_(**q**), from which IVF-Flat returns the _k_ vectors that lie nearest to **q** under the squared Euclidean distance. Recall therefore depends on the lists and on _n<sub>p</sub>_ alone, because the scan of _S_(**q**) is exact up to floating- point rounding. Multi-index structures \[3\], learned routing \[6\], and balanced partitions for disk-resident data \[9\] refine the choice of _S_(**q**), although each of them still reads the vectors of the chosen lists. The scan of the probed lists dominates the cost of a high-recall query. A query reads |_S_(**q**)|≈_n<sub>p</sub>N/P_ vectors of 4_D_ bytes each, so that its memory traffic grows linearly with _n<sub>p</sub>_. GPU implementations such as Faiss \[31\] and cuVS \[42\] therefore spend the time of a high-recall query on this traffic. Compressed lists reduce the bytes per vector through product quantization \[21, 32\], anisotropic quantization \[26\], or randomized binary codes \[18, 51\]. However, the compressed distances reorder the candidates, so that high recall requires a refinement step \[30\] that reads the full vectors of a multiple of _k_ candidates per query. The cost of a high-recall IVF query is therefore set by its full-precision reads, either of the whole probed set or of the refined candidates.

#### Certified exclusion.

Recently, certified exclusion (CertEx) \[64\] was proposed to replace most full-precision reads with a certified test. Consider an orthonormal matrix \(V\in\mathbb{R}^{D\times m}\) of the _m_ principal directions of the dataset and its mean \(\mu\). CertEx lifts every vector to

\(\ell(\mathbf{x})=\big[V^\top(\mathbf{x}-\mu);\|(I-VV^\top)(\mathbf{x}-\mu)\|\big]\in\mathbb{R}^{m+1},\) (1)

The Cauchy-Schwarz inequality on the residual components then gives \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|\le\|\mathbf{q}-\mathbf{x}\|\) for every pair. The lifted rows are stored in half precision together with four certificate coordinates that bound their rounding errors, so that one tensor-core product of a query row with a vector row yields a lower bound \(\beta(\mathbf{q},\mathbf{x})\le\|\mathbf{q}-\mathbf{x}\|^2\) that holds under every rounding of the product. A vector **x** survives the screening of a query only if \(\beta(\mathbf{q},\mathbf{x})\le U(\mathbf{q})\), where _U_(**q**) bounds the squared distance of the _k_-th nearest neighbor from above. CertEx sets _U_(**q**) from the exact distances of sampled anchors, since any _k_ distinct vectors bound the _k_-th distance, and verifies the survivors in increasing order of \(\beta\) until the next bound exceeds the _k_-th exact distance found. Every vector that the screening excludes costs 2(_m_+5) bytes instead of 4_D_, because only the survivors are read at full precision. CertEx applies this test to the whole dataset, so that its exact search still screens all _N_ rows per query. In contrast, an inverted-file query needs only the _k_ nearest vectors of its probed lists, which requires a threshold that bounds the _k_-th distance within these lists.

### 3.2 Lychee Overview

Lychee performs approximate nearest-neighbor search by returning the exact top-_k_ candidates of the probed lists, matching the full-precision candidate ranking of IVF-Flat. Given a query \(\mathbf{q}\in\mathbb{R}^D\) and probed set \(S(\mathbf{q})=L_{j_1}\cup\cdots\cup L_{j_{n_p}}\), the target answer _A<sub>k</sub>_(**q**) minimizes the sum of squared distances over any _k_-subset:

\(A_k(\mathbf{q})=argmin_{T\subseteq S(\mathbf{q}),|T|=k}\sum_{\mathbf{x}\in T}\|\mathbf{q}-\mathbf{x}\|^2,\) (2)

with ties broken by index. Evaluating Eq. (2) exactly attains the recall of the inverted lists at every _n<sub>p</sub>_, leaving query latency and throughput as the only quantities to improve.

The cost of Eq. (2) is dominated by full-precision reads. Define _r<sub>k</sub>_(**q**) as the _k_-th smallest squared distance from **q** to _S_(**q**). Every vector of _S_(**q**) farther than _r<sub>k</sub>_(**q**) is excluded from _A<sub>k</sub>_(**q**), although a full-precision scan learns this fact only after reading the vector. Lychee instead proves exclusion from the low-dimensional lifted row of the vector, under a threshold \(U(\mathbf{q})\ge r_k(\mathbf{q})\) that the probed lists themselves provide.

Figure 2 illustrates the resulting search pipeline of a query batch across its three algorithmic stages. In Stage 1, the search identifies _n<sub>p</sub>_ probed lists and gathers exact distances to their anchors (Definition 3.1) to establish a list-local threshold \(U(\mathbf{q})\ge r_k(\mathbf{q})\) (Figure 2, panel 1). In Stage 2, a routed tensor-core pass groups queries probing the same<tbc>

