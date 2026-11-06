measured question comprises two retrieval hops; we report paired hop1+hop2 latency. Scaling experiments use SIFT100M and SIFT1B from BIGANN [23], with synthetic 1KB payloads.

**RPAG layout construction.** For CCS segments built with RPAG, we use a K-prefix co-retrieval objective that uses cumulative top-_K_ prefixes at \(K\in\{10,20,40,80\}\) with weights 1.0, 0.3, 0.1, and 0.03, respectively. This gives lower-_K_ co- retrieval pairs more influence during partitioning and intra- segment ordering, prioritizing the more latency-sensitive small-_K_ cases while still retaining signal from larger retrieval sets.

**ANN engines.** Our ANN engines are DiskANN[46] and SPANN[6]. DiskANN is a graph-based SSD ANN engine: compact vector summaries stay in memory, while graph and data pages are served from SSD; we set the search width _L_ per _K_ (68-1600 for _K_=10-1600) for recall@_K_≈0.90 which is a common recall target in evaluation practice of related work [6, 13, 14, 19, 46, 48]. For SPANN we set SearchInternalResultNum per _K_ (110-1152 for _K_=10- 1600) for recall@_K_≈0.90 and issue posting-list reads in batches of 8. Together, these two engines cover graph-based and cluster-based SSD retrieval, and ConStore uses their returned document IDs plus engine-specific candidate hooks for SICP (§4.3). We select these representative backends to

evaluate both index families, rather than compare all search- engine variants. PipeANN optimizes DiskANN-style graph traversal, while OdinANN extends this line to maintain stable performance under updates [13, 14]; we do not evaluate them here. Faster vector search makes unchanged content fetch a larger fraction of retrieval latency, strengthening the motivation to optimize it, but can also shorten SICP’s overlap window. We bounded bandwidth of vector search of SPANN to simulate production concurrent environments.

**Baselines.** We compare against three baselines. (1) Seq\_ Random stores content in a single binary file under a random corpus insertion order and fetches results via per-document I/O request. Insertion-order payload storage follows current production practice [38, 51]. (2) Seq\_KMeans stores content in CCS segments organized by embedding K-Means, testing semantic co-location without co-retrieval-aware grouping. (3) Seq\_RPAG stores document content in CCS segments organized by RPAG and uses the same GCF-batched fetch path as ConStore, but fetches content only after ANN search completes. SICP-only adds speculative prefetch to the Random layout; ConStore combines prefetch with RPAG and GCF. These variants separate overlap from layout benefits while preserving the final top-_K_.

Seq_Random Seq_KMeans Seq_RPAG SICP-only ConStore Search Fetch 1
1 1
1 0.5 0.5 Norm. latency Norm. latency 0.5 0.5 0
0 0
0 10 20 40 80 160 1600 10 20 40 80 160 1600 10 20 40 80 160 1600 Top-K Top-K Top-K (a) 2Wiki. (b) HotpotQA. (c) MuSiQue.

Seq_Random Seq_KMeans Seq_RPAG SICP-only ConStore Search Fetch 1
1 1
0.5 0.5 0.5 Norm. latency Norm. latency 0
0 10 20 40 80 160 1600 10 20 40 80 160 1600 10 20 40 80 160 1600 Top-K Top-K (a) 2Wiki. (b) HotpotQA. (c) MuSiQue.

**Figure 8.** DiskANN end-to-end latency breakdown by Top-_K_ and dataset.

**Figure 9.** SPANN end-to-end latency breakdown by Top-_K_ and dataset.

