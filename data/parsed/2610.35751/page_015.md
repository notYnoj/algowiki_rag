## A APPLICABILITY TO OTHER DUAL ATTRIBUTES

**Datasets with Additional Dual Attributes.** ACTIVE is not limited to image-text data, but supports arbitrary combinations of data types. To further examine the applicability of ACTIVE , we add two geo-tagged datasets, as shown in  3. The first is Regions (RS) \[1\], a multilingual geotagged social-media corpus collected from Twitter, where each text post is embedded using BERT \[13\]. The second is MP16-Pro (MP) \[24\], a geo-tagged image collection from Flickr, where each image is embedded into a 768-dimensional vector using DINOv2 ViT-B/14 \[35\]. We conduct both static search and dynamic update experiments on RS and MP.

**Static Search Performance.** The accuracy-efficiency trade-off results of ACTIVE , DEG, and MR on RS and MP are shown in Figure 27. Under the same search latency, the Recall@10 of ACTIVE is on average 0.83% and 0.32% lower than that of DEG on RS and MP, respectively. Meanwhile, ACTIVE substantially outperforms MR, improving Recall@10 by 33.10% on RS and by 15.17% on MP under the same latency. These results show that Pareto-frontier-based indices remain effective for text-coordinate and image-coordinate attribute pairs, and that ACTIVE preserves search quality close to DEG while clearly surpassing multi-index retrieval.

**Update Throughput.** We evaluate the update throughput of ACTIVE on RS and MP under 1% batch deletions and insertions, as shown in Figures 28 and 29. For deletions, ACTIVE consistently achieves higher throughput than both RBR and NRBR, improving the average deletion throughput by 13.78-23.88\(\times\) over RBR and 1.42-1.64\(\times\) over NRBR. For insertions, ACTIVE improves the average throughput by 1.31-1.48\(\times\) over DEG.

**Search Accuracy under Updates.** We further evaluate the search accuracy of ACTIVE under 1% batch deletions and insertions on RS and MP, as shown in Figures 30 and 31. For deletions, ACTIVE achieves Recall@10 comparable to that of RBR and 0.30%-0.58% higher than that of NRBR on average. For insertions, ACTIVE maintains Recall@10 comparable to that of DEG.

## B ANALYSIS OF AFFECTED NODES

By default, ACTIVE treats in-neighbors of deleted nodes as affected nodes, since deletions mainly cause connectivity loss of in- neighbors. We argue that repairing only in-neighbors is sufficient to largely restore connectivity. To validate this, we compare ACTIVE (In) with two variants on OI under 1% batch deletions. ACTIVE (Out) repairs only out-neighbors, while ACTIVE (In+Out) repairs both in-neighbors and out-neighbors of deleted nodes. As shown in Figure 32, ACTIVE (In) consistently achieves higher update throughput and better search accuracy than other repair strategies.

\begin{tabular}{ccccc}
Dataset & _D<sub>x</sub>_ & _D<sub>y</sub>_ & #Vectors & Contents \\
Regions (RS) & 768 & 2 & 614,000 & Text-Coord. \\
MP16-Pro (MP) & 768 & 2 & 1,000,000 & Image-Coord. \\
\end{tabular}

1.0
0.9
Recall 10@10
0.8
0.7
0.6
0.5
Latency (ms)
1.0
1.5
(a) Regions
(b) MP16-Pro

2000
Throughput (ops/s)
1000
D. + RBR
ACTIVE
D. + NRBR
200
D. + NRBR
0
1
2
3
4
5
6
7
8
9
Batches
Batches
(a) Regions
(b) MP16-Pro

450
Throughput (ops/s)
350
DEG
ACTIVE
250
0
1
2
3
4
5
6
7
8
9
Batches
(a) Regions
(b) MP16-Pro

0.985
0.990
Recall 10@10
0.980
Recall 10@10
0.975
0
2
4
6
8
10
0
2
4
6
8
10
Batches
Batches
(a) Regions
(b) MP16-Pro

1.00
0.990
0.98
Recall 10@10
0.988
0.96
0
2
4
6
8
10
0
2
4
6
8
10
Batches
Batches
(a) Regions
(b) MP16-Pro

ACTIVE (In + Out)
ACTIVE (Out)
ACTIVE (In)
0.975
1500
0.970
Recall 10@10
1000
0.965
0
2
4
6
8
10
0
1
2
3
4
5
6
7
8
9
Batches
(a) Search accuracy
(b) Deletion Throughput

** 3: Dataset statistics.** _D<sub>x</sub>_ and _D<sub>y</sub>_ **denote the vector dimensions of the** _x_**- and** _y_**-attributes, respectively. Each dataset contains 1,000 query vectors.**

**Figure 27: Comparison of the trade-offs between search accuracy and latency. The top left is better.**

**Figure 28: Deletion throughput comparison.**

**Figure 29: Insertion throughput comparison.**

**Figure 30: Recall comparison under deletions.**

**Figure 31: Recall comparison under insertions.**

**Figure 32: Impact of different affected node definitions.**

