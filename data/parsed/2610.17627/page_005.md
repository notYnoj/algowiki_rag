<tbc>with fusion distance, however, recalls by these graphs are lower than FilteredVamana graphs. This indicates boolean label filtering surpasses in the graph construction phase, while we proved that our continuous approach results in better recall on the same graph.

AiSAQ-in-Filtering also needs to adjust the label weight \(\beta\) manually. In the non-compressed fusion distance search, larger \(\beta\) just means a search metric of boolean label filtering. However in LiPQ, larger \(\beta\) also enlarges quantization errors of the label vectors, which leads tradeoffs between label importance and accuracy.

Despite promising results above, further investigation remains as a future work necessary within the multiple-label search tasks, particularly regarding the generation of proper datasets. Search conditions characterized by multiple non-zero elements within query labels consistently yielded low recall rates. It might be one of that reasons that query labels were generated utilizing Zipf’s distribution, resulting in no object which has all labels of each query, including minor ones. Therefore preparation of consistent datasets and labels should help multiple-label search experiments and analysis.

### 5.2 Applications

The label distance metric used in AiSAQ-in-Filtering is essentially inner product of sparse vectors. In this paper, label vectors have binary elements (0 or 1), however, values of that elements **_a_**_<sub>i</sub>_ can be continuous. For example, label vectors can be sparse keyword vectors like BM25[9] score vectors. This means that semantic-and- keyword hybrid document retrieval can be performed with small memory footprint, though ranking metrics other than fusion distance are to be assessed.

## 6 Conclusion

We proposed AiSAQ-in-Filtering in this paper, a filtering ANNS method which offloads label information to the storage without increase of storage and memory footprint. This also acheived short index load time and higher recall with lower disk I/Os compared with existing methods.

AiSAQ-in-Filtering also have possible applications like hybrid document search and other LLM-intensive tasks. This can be scaled out to larger datasets as shown in original AiSAQ.

100
100
80
80
60
60
40
40
Recall@1
Recall@1
20
20
0
0
0
50
100
150
200
0
50
100
150
200
Mean IOs
Mean IOs
AiSAQ-in-Filtering, label=1
AiSAQ-in-Filtering, label=10
Filtered-DiskANN, label=1
Filtered-DiskANN, label=10
AiSAQ-in-Filtering, label=1 (B=0)
AiSAQ-in-Filtering, label=10 (B=0)

100
100
80
80
60
60
40
40
Recall@1
Recall@1
20
20
0
0
0
50
100
150
200
0
50
100
150
200
Mean IOs
Mean IOs
AiSAQ-in-Filtering
Filtered-DiskANN

**Figure 6: AiSAQ-in-Filtering and Filtered-DiskANN with Zipf labels (left: SIFT1M, right: KILT E5 1M)**

**Figure 7: AiSAQ-in-Filtering and Filtered-DiskANN with uniform labels (left: SIFT1M, right: KILT E5 1M)**

