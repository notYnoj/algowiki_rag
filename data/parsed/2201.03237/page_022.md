<tbc>higher precision. Similarly, for Faiss we increase the parameter n\_probe and for FALCONN we increase the parameter num\_probes. We record the time cost when achieving the required precision and calculate the QPS. The search performance of all algorithms on 4 datasets is shown in Figure 7. We can see that:

1. Our algorithm yields better or comparable search performance than all recent state-of-the-art algorithms. In the case of datasets with larger LID and queries with higher precision, the advantages are more obvious;<tbc>

2. The performance of graph-based algorithms is much better than other algorithms in queries with high precision. In addition, the graph-based algorithms can achieve a higher precision limit.<tbc>

3. The edge-selecting strategies of DPG, NSSG and TBSG are all based on angle. In DPG, the degree of each node must exceed a given value (mostly very large), which results in the over large out-degree. However, both NSSG and TBSG can adjust the out-degree with hyper-parameter. Compared with NSSG considering only one angle, we consider both angles and quantify their impact on the probability of the monotonic search. NSSG’ s advantage in Glove gradually disappears while TBSG’ s advantage continues to expand, indicating that our design is more reasonable.

## 4.2. Index Performance

We list some important information of the graph-based indexes in  3, including the average degree, maximum degree, index size and index time. In Glove and Crawl, the maximum degree of DPG is very large after adding reverse edges, which results in very low efficiency. So we undid the addition of reverse edges on these two datasets. According to  3, we can see that:

1. The average out-degree of TBSG, HNSW and NSSG is much smaller than that of DPG and KGraph. This is mainly because in the edge-selecting strategy the out-degree of nodes is not fixed, and the maximum value is set<tbc>

