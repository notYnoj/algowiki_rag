\(\bullet\) Advantages of AiSAQ, DRAM-free, fast index switching and scalability can be kept by our AiSAQ-in-Filtering.<tbc>

\(\bullet\) Our proposal can be applicable to complex search usecases beyond label-filtering search, such as keyword search and range search.

## 2 Preliminaries

### 2.1 Notations

Figure 1 illustrates vector and label notations. The object set O={**o**<sub>1</sub>_,...,**o**<sub>N</sub>_} consists of _N_ objects, each with its ID _i_. Each object **o**_<sub>i</sub>_ represents an item (e.g., document, image, dialogue) and has an associated (unstructured) data vector **v**_<sub>i</sub>_.

In a filtering search, we use a structured label set L with _L_ labels (e.g., ‘dog’, ‘cat’, ‘white’). Each object **o**_<sub>i</sub>_ is associated with a label set \(\mathcal{L}_i\subseteq\mathcal{L}\), representing its features (e.g., this is a ‘white’ ‘dog’, not a ‘cat’). Often, this label set is translated into a sparse vector representation **a**_<sub>i</sub>_, and an object is then described as **o**_<sub>i</sub>={**v**_<sub>i</sub>_,**a**_<sub>i</sub>}.

### 2.2 Approximate Nearest Neighbor Search (ANNS)

Given a dataset D with _N_ objects, each object **o**_<sub>i</sub>_ has an unstructured data vector **v**_<sub>i</sub>_. Nearest neighbor search (NNS) aims to find the closest vector to the query **q**, \(\text{argmin}_{\mathbf{v}_i\in\mathcal{D}}d(\mathbf{v}_i,\mathbf{q})\), where \(d(\cdot,\cdot)\) is a distance metric (e.g., L2 or inner product). To shorten _O(N_) time complexity of the naive NNS, approximate nearest neighbor search (ANNS) methods like graph-based[7\][5], hash-based[3], and cluster-based approaches[6] have been developed. Graph-based ANNS offers good recall-speed tradeoffs, utilizing directed graphs as an index. These methods typically have _O_(log_N_) time complexity and store the graph data in DRAM[2].

### 2.3 Filtering Search and Fusion Distance

Filtering ANNS and NNS considers query labels. Each object **o**_<sub>i</sub>_ is associated with its label set L_<sub>i</sub>_, and the search finds nearest vectors within objects sharing the same query label **lq**.

Two primary filtering strategies exist: boolean label filtering[4\][15] and continuous label filtering[13\][14]. Boolean filtering directly utilizes objects’ label sets L_<sub>i</sub>_ for edge construction and search traversal. Continuous filtering employs encoded _L_-dimensional label vectors **a**_<sub>i</sub>_ and a ‘fusion distance’ - a linear combination of vector distance and label distance--for index construction and search.

\(d_\mathrm{F}(\mathbf{o}_1,\mathbf{o}_2)=d(\mathbf{v}_1,\mathbf{v}_2)+\beta d_\mathrm{L}(\mathbf{a}_1,\mathbf{a}_2)\) (1)

Specifically, the fusion distance is defined as Equation 1. \(\beta\) is a weighting factor representing the importance of labels (\(\beta=0\) meaning no label consideration).

### 2.4 DiskANN and Its Variants

DiskANN[5] is a widely used graph-based ANNS method. It stores graph data and full-precision vectors on an SSD, while compressed vectors reside in DRAM. During the search phase, DiskANN retrieves neighboring vectors from the SSD and uses DRAM for distance computations. This architecture enables efficient vector search, however, its DRAM footprint is still proportional to dataset size.

Filtered-DiskANN[4] adds boolean label filtering to DiskANN, using FilteredVamana and StitchedVamana graph indices to incorporate label information. Filtered-DiskANN is designed to store label data onto DRAM and its usage by labels is inevitable.

AiSAQ[11] further optimizes DiskANN by offloading PQ vector data from DRAM to the SSD (Figure 2), reducing DRAM usage to near-zero regardless of dataset size. This also minimizes index switching time and spatial cost in multi-tenant environments.

### 2.5 Product Quantization

DiskANN utilizes product quantization (PQ)[6] for its vector compression. This involves splitting each vector **v**_<sub>i</sub>_ into _M_ subvectors. Subvectors at the same position are then grouped into _b_ clusters (typically _b_=256) using k-means. Each subvector is encoded with the cluster ID of its group. During the search phase, DiskANN precomputes distances between query subvectors and the centroids of these clusters, storing them in a lookup table. The original vector is then decoded by summing the distances from the lookup table, using the vector’s cluster IDs.

Figure 3 is an example of product quantization for 4-dimensinoal vectors with _M_=2, _b_=4 (2-bits). This shows a vector **v**_<sub>1</sub> is quantized as (_a,d_) and is decoded as (**c**_<sub>1a</sub>_,**c**_<sub>2d</sub>)=(_c_<sub>1_a_1</sub>_,c_<sub>1_a_2</sub>_,c_<sub>2_d_3</sub>_,c_<sub>2_d_4</sub>).

As a limitation of PQ, the distance metric must be the summation of calculation for each element in the vectors (described below).

\(d(\mathbf{x},\mathbf{y})=\sum_{i=1}^Df(x_i,y_i)\) (2)

L2 distance, inner product and cosine similarity as distance functions \(f(\cdot,\cdot)\) satisfy this constraint.

Object set O ID Vector Label 1
v1 L1 2
v2 L2 N
VN LN Object 01 = (0.1, 0.7, 0.3, 0.5) dog cat mouse black white gray = {dog, white} a1 1
0 0
0 1
0

SSD DRAM SSD Current full vector and edges Neighboring PQ vectors Current full vector and edges Neighboring PQ vectors

**Figure 1: Object with vector and label**

**Figure 2: Data Placement of DiskANN (left) and AiSAQ (right)**

