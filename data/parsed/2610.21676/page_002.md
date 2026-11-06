reads and scores posting lists in batches. In both cases, likely results emerge before search finishes, allowing some content reads to overlap with the remaining search I/O.

Choosing when and what to prefetch is non-trivial. Early candidates can change, wasting content reads; late prefetches leave too little search time to hide their cost. Variable search tails and competition for SSD bandwidth therefore require selective, budgeted speculation.

Another challenge is that content is commonly stored in insertion or key order, unrelated to which items are retrieved together [38, 51, 53]. Co-retrieved payloads are consequently scattered, requiring many random reads and limiting opportunities for coalescing.

Embedding-based clustering is an imperfect alternative: proximity in vector space need not imply co-access. A multi- hop query can retrieve a film page and its director’s biography from different semantic clusters. Grouping content by observed co-retrieval patterns can capture this locality that insertion order and embedding clusters miss.

We present ConStore, a content storage engine for disk- based ANNS that reduces end-to-end retrieval latency through two complementary techniques: overlapping content fetch with search and reducing fetch cost through co-retrieval-aware layout. Either technique can be deployed independently. Our contributions are:

1. Content-fetch profiling: Across million- to billion-vector indexes, we show that content-fetch cost grows approximately linearly with _K_ and can match or exceed vector- search latency, motivating optimization of the complete search-plus-fetch pipeline.<tbc>

2. Speculative Inline Content Prefetch (SICP): Using the shared progressive-I/O abstraction, SICP prefetches content for stable leading candidates under a bounded I/O budget and fetches missing payloads after search. It preserves the final top-_K_ and requires only a document-to- extent lookup, independent of content layout.<tbc>

3. Co-Retrieval Content Segments (CCS) with Group Content Fetch (GCF): Retrieval-Pattern-Aware Grouping (RPAG) uses query logs to group frequently co-retrieved documents into contiguous CCS segments. At query time, GCF coalesces requested content into batched, page-aware reads. Together they reduce fetch cost without changing the ANN engine, with or without SICP. Workload-Adaptive Segment Reorganization (WASR) adapts the layout to workload shifts by selectively regrouping segments under a bounded rewrite budget when recurring co-retrieval patterns change.<tbc>

4. Evaluation: On three multi-hop QA workloads, ConStore reduces end-to-end retrieval latency by up to 48% on DiskANN and 25% on SPANN over the best per-document- read baseline, while preserving retrieval results. Ablations isolate each technique, and synthetic-payload experiments<tbc>

on 100M- and billion-vector indexes demonstrate SICP at larger scales.

## 2 Background and Motivation

### 2.1 ANNS Retrieval Pipeline

ANNS-based applications that consume retrieved payloads have two coupled storage phases: vector search and content fetch. The vector-search phase probes an ANN index to identify the top-_K_ item IDs; the content-fetch phase loads the associated text, item content, or features from a content store. In the conventional pipeline, these reads begin after search returns its final IDs. Content fetch therefore adds its own storage I/O to end-to-end retrieval latency rather than being part of the vector-search operation.

ANNS supports more than RAG: semantic search retrieves candidate documents [27, 29], recommendation and advertising retrieve items for downstream ranking or filtering [19], and visual similarity search retrieves related images [26]. In RAG, retrieved passages supply external knowledge to an LLM [32, 50].

### 2.2 Disk-Based ANN Indexes

Disk-based ANN indexes are used because billion-scale vector corpora cannot keep all full-precision vectors and search metadata in DRAM at reasonable cost. Modern disk-based ANN systems mainly fall into two families. The first is graph-based search, including DiskANN, PipeANN, OdinANN, and Starling [13, 14, 46, 52]. DiskANN keeps a compact in-memory structure, such as entry points and compressed vectors, while storing full-precision vectors and graph neighborhoods on SSD. Query processing performs a beam search over the graph: each hop reads a batch of candidate neighbors from SSD, scores the newly loaded vectors, updates the candidate queue, and issues the next batch of graph reads. Thus the top-_K_ result is refined over multiple SSD-I/O rounds rather than being produced by a single blocking lookup.

