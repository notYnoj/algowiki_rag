2.

## 3.2. TBSG v.s. SOTA methods

### 3.2.1. Evaluation

We compare the search performance using queries-per-second (QPS) v.s. precision. The QPS is how much queries an algorithm can process per second at given precision. The precision is defined as

\(precision=\frac{|R\cap G|}{|G|}\)

where _R_ is result returned by algorithm and _G_ is groundtruth.

### 3.2.2. Compared Algorithms

We select some current state-of-the-art algorithms for comparison, including tree based, product quantization based and graph based methods. We don’t select the hash based methods because we’re more concerned with efficiency at high precision, and they’re too slow at high precision. We care more about the graph based algorithm, which are much more competitive. The algorithms to compare are as follows:

1. HNSW<sup>8</sup>: Hierarchical NSW Graph is an improved version of the NSW Graph with superior search performance.<tbc>

<sup>8</sup>https://github.com/nmslib/hnswlib

\begin{tabular}{ccccc}
Dataset & Nd & Nq & D & LID \\
Sift & 1,000,000 & 10,000 & 128 & 9.3 \\
Gist & 1,000,000 & 1,000 & 960 & 18.9 \\
Glove & 1,183,514 & 10,000 & 100 & 20.0 \\
Crawl & 1,989,995 & 10,000 & 300 & 15.7 \\
\end{tabular}

2: We list characteristics of the datasets including the number of data points(Nd) and query points(Nq), dimension(D), local intrinsic dimensionality (LID), where LID are used to describe the hardness of the datasets.

