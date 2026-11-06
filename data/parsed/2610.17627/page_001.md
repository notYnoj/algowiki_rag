# AiSAQ-in-Filtering for DRAM-free Filtered Information Retrieval

### Abstract

Filtering search is one of the crucial applications of approximate nearest neighbor search (ANNS). In filtering search, label information is used in conjunction with unstructured vector data. ANNS provides efficient similarity search in large-scale datasets, however, the memory footprint of storing both vector data and their associated label becomes a significant cost factor as dataset sizes grow. To address this problem of increasing DRAM usage, we propose AiSAQ-in-Filtering, with a novel quantization method called LiPQ (Label-inclusive Product Quantization). LiPQ combines unstructured data and structured labels into a single representation, leading no growth of encoded data. Our proposal increased recall@1 of single-label searches by up to 55% and fewer disk I/Os compared with existing methods. This also retains the main advantages of AiSAQ, which can reduce DRAM footprint by up to 1/78 and index switching time comparing with existing methods. This proposal can also be applied to sparse-dense hybrid search beyond label filtering such as semantic and keyword search of documents.

### CCS Concepts

• **Information systems** \(\rightarrow\) **Retrieval efficiency**; _Novelty in information retrieval._

### Keywords

approximate nearest neighbor search, ANN, vector search, graph search, DiskANN, AiSAQ, filtering search, hybrid search, label search, fusion distance, AiSAQ-in-Filtering, Pruduct Quantization, PQ, large-scale search

**ACM Reference Format:**

Kento Tatsuno, Daisuke Miyashita, Kazunari Sumiyoshi, Hiroaki Yamanaka, Kosuke Nakata, and Jun Deguchi. 2026. AiSAQ-in-Filtering for DRAM-free Filtered Information Retrieval. In . ACM, New York, NY, USA, 6 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnnn

### 1 Introduction

Vector search is one of key techniques of information retrieval. The use of approximate nearest neighbor search (ANNS) have spread to reduce search time. Among various strategies of ANNS methods, graph-based approaches acheive good tradeoffs between search latency and recall.

Filtering search (or hybrid search) is one of applications of ANNS. Each object in the dataset has its label and search queries are also have their label. Primitive methods of filtering search are classified into two approaches: pre-filtering and post-filtering. However, both of which cost a lot in large-scale searches: the former approach requires maintaining multiple indices corresponding to each label, and the latter has to scan ANNS result linearly for filtering[15]. To avoid such computational costs, one-stage methods[13\][4] are proposed: the index construction procedure considers the label information. In the search phase, a query vector and its label are simultaneously utilized in the index.

DiskANN[5] is a major graph-based ANNS algorithm which uses storage devices such as SSDs to save DRAM usage. It stores PQ (Pruduct Quantization)[6] compressed vectors on DRAM and graph edges and full-precision vectors on SSD. It has smaller DRAM footprint compared to all-DRAM ANNS methods, however, DRAM usage by compressed vectors is proportional to the scale of the dataset. The authors added filtering function to DiskANN as Filtered-DiskANN[4]. It has separated label data on DRAM in addition to PQ compressed vectors which still cannot solve increased DRAM usage for large- scale datasets. Our past proposal called AiSAQ[11] achieves almost- zero DRAM footprint and fast index switching regardless the scale of datasets. Methodologies of Filtered-DiskANN can be ported to AiSAQ easily, but it causes label data remaining in DRAM or increase of SSD usage.

In this paper we propose AiSAQ-in-Filtering, a novel method of DRAM-free filtering search inspired by AiSAQ and fusion distance[13]. This keeps the advantages of AiSAQ and acheived higher recall than Filtered-DiskANN. The main comparison of our proposal with existing methods is described in  1.

Our contributions in this paper are as follows:

\(\bullet\) AiSAQ-in-Filtering achieves ∼90% recall@1 in single-label filtering search, much higher than the baseline of Filtered- DiskANN.

\(\bullet\) Our new product quantization method named LiPQ (Label- inclusive Product Quantization) can encode label data along with unstructured vector data without increase of compressed vector size.

Kento Tatsuno<br> Koxia Corporation Japan

Hiroaki Yamanaka<br> Koxia Corporation Japan

Daisuke Miyashita<br> Koxia Corporation Japan

Kosuke Nakata<br> Koxia Corporation Japan

Kazunari Sumiyoshi<br> Koxia Corporation Japan

Jun Deguchi<br> Koxia Corporation Japan

