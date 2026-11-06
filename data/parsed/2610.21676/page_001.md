# ConStore: Search-Overlapped Prefetch and Co-Retrieval-Aware Content Storage for Disk-Based ANNS

### Abstract

Disk-based approximate nearest-neighbor search (ANNS) supports retrieval-augmented generation (RAG), search, recommendation, and advertising over corpora that exceed memory capacity. Existing ANNS research often focuses on vector search at small top-_K_, whereas industrial-scale applications require larger retrieval sets. Fetching the corresponding content from storage remains comparatively unexplored. Our profiling across million- to billion-vector corpora shows that, at large _K_, content fetch latency can match or exceed vector-search latency and cannot be ignored in end-to-end retrieval.

We present ConStore, a content storage engine combining two complementary techniques to reduce end-to-end retrieval latency. Speculative Inline Content Prefetch (SICP) commonly abstracts graph-based and cluster-based ANNS as progressive SSD I/O that refines an in-flight candidate queue. It prefetches content for stable leading candidates under a bounded I/O budget, overlapping content reads with search without changing the final top-_K_ results. Co-Retrieval- Pattern-Aware Grouping (RPAG) uses query logs to place frequently co-retrieved documents in contiguous segments. Workload-Adaptive Segment Reorganization (WASR) adapts this layout to workload shifts by selectively regrouping segments under a bounded rewrite budget. Group Content Fetch (GCF) exploits this layout to coalesce per-document random reads into batched, page-aware I/O requests. SICP works independently of the content layout, while RPAG and GCF reduce fetch cost even without prefetching.

Across three multi-hop QA workloads with _K_ from 10 to 1600, ConStore reduces end-to-end retrieval latency over the best per-document-read baseline by up to 48% on DiskANN and 25% on SPANN. Separate experiments on 100M- and billion-vector indexes demonstrate SICP’s applicability at larger scales.

### 1 Introduction

Disk-based approximate nearest-neighbor search (ANNS) has been widely adopted to overcome the memory limitations of large-scale vector search [6, 19, 46]. By keeping large indexes on SSD rather than entirely in DRAM, these systems support retrieval-augmented generation (RAG), search,

recommendation, and advertising over corpora containing millions to billions of vectors [19, 32].

Once a query is embedded, the storage-facing ANNS retrieval pipeline has two phases: _vector search_ identifies the top-_K_ item IDs, and _content fetch_ loads their associated payloads from storage for downstream processing. For example, RAG loads passages for an LLM prompt, while search and recommendation retrieve item content or features for re-ranking and presentation. Both phases contribute to end- to-end retrieval latency.

Prior work has heavily optimized vector search through two main families of disk-based indexes. Graph-based systems, including DiskANN, PipeANN, OdinANN, and Starling, optimize graph traversal, storage layout, or update handling [13, 14, 46, 52]. Clustering-based systems, including SPANN and FusionANNS, organize vectors into clusters for efficient candidate retrieval [6, 48]. In contrast, the content- fetch phase that delivers the selected payloads has received comparatively little attention.

Much ANNS research emphasizes small top-_K_ settings such as _K_=10, but industrial applications retrieve hundreds or thousands of candidates. Recent study reports search workloads with _K_ around 100-3,000 to supply downstream re-ranking models and advertising workloads with _K_ up to 3,000 [19]. These larger retrieval sets challenge the assumption that content fetch is only a minor overhead. Our profiling across million- to billion-vector indexes shows that content-fetch latency can match or exceed vector-search latency at large _K_ (Figures 2 and 3). At small _K_, vector search pays an initial cost to locate promising regions of the index. As _K_ grows, expanding and scoring the candidate set adds work, while fetching fixed-size payloads requires proportionally more content reads. In the measured large-_K_ regime, both phases exhibit approximately linear growth with _K_, making content fetch a first-class retrieval cost rather than a negligible follow-up.

Conventional retrieval serializes content fetch after vector search, waiting for the final top-_K_ IDs before issuing content reads. We study graph-based and clustering-based ANNS and it reveals a shared opportunity: both can be viewed as _progressive SSD I/O processes that iteratively refine a candidate queue_. DiskANN reads graph neighborhoods, while SPANN

Zhutao Zhuang<sup>1,2</sup> Nong Xiao<sup>1</sup> Zhiguang Chen<sup>1</sup> Yue Yu<sup>2</sup>

<sup>1</sup>Sun Yat-sen University <sup>2</sup>Pengcheng Laboratory zhuangzht@mail2.sysu.edu.cn xiaon6@mail.sysu.edu.cn chenzhg29@mail.sysu.edu.cn yuy@pcl.ac.cn

