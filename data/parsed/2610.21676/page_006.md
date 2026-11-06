<tbc>those selected documents into content extents and merges nearby extents into page-aligned read windows.

The first prefetch can size its budget from the estimated remaining search tail. Subsequent prefetches use a small per-prefetch budget so that the worker continues to track the queue as it evolves, rather than spending the entire budget on one early snapshot. SICP keeps a compact coverage record for scheduled and completed content windows, so later prefetches avoid both document-level duplicates and page-level duplicates caused by adjacent documents sharing the same content page.

**(3) Residual content fetch - handling misses.** The residual path ensures complete final results even when speculation misses, without duplicating pending reads. After vector search returns, the final top-_K_ is authoritative. SICP subtracts all documents covered by completed prefetch reads. It also treats documents scheduled by an in-flight prefetch as pending, so the foreground path does not immediately duplicate the same content work. The foreground then fetches the remaining final documents with the same page-aware planner while the prefetch worker finishes outstanding work.

### 4.3 Per-Engine Instrumentation

Each engine provides a read-only callback that publishes candidate snapshots and a progress counter to the shared prefetch worker. The callback leaves search logic unchanged and requires no suspension or restart.

**DiskANN.** On-disk beam search advances through graph- search hops, reading candidate neighborhoods from SSD and refining the candidate queue. An optional callback at configurable hop intervals publishes the current queue and hop counter. The background worker uses successive snapshots to check stability and select bounded content reads, allowing multiple prefetches as candidates evolve. The callback does not modify the queue or traversal; the foreground search continues to completion.

**SPANN.** An in-memory head search selects candidate posting lists, which are read from SSD and scored to refine the result buffer. We instrument this refinement loop to publish capped, sorted candidate snapshots at configurable posting-count intervals. The processed-posting count supplies the progress signal in place of DiskANN’s hop counter, letting the same worker apply stability checks and budgeted prefetching. Head-index navigation, posting-list selection, and foreground refinement remain unchanged, preserving the final top-_K_.

## 5 Co-Retrieval-Aware Content Layout and Group Fetch

SICP (§4) hides content I/O behind the search tail but does not change how much I/O each fetch costs: with an insertion- order payload store, every prefetched or residual document is still a separate random read. This section presents the<tbc>

<tbc>second, independent technique of ConStore, which reduces the per-fetch cost itself. It consists of an on-disk segment format (CCS, §5.1), an offline co-retrieval-aware layout policy (RPAG, §5.2), and an online grouped, page-aware fetch path (GCF, §5.4). The three are used by the post-search fetch path on their own, and by SICP’s prefetch worker when the two techniques are combined.

### 5.1 Co-Retrieval Content Segments (CCS)

A _Co-Retrieval Content Segment_ (CCS) stores a bounded group of documents contiguously in the order chosen by the layout policy. Grouping by co-retrieval rather than embedding proximity lets jointly requested documents share content reads, reducing random I/O even when their embeddings are far apart. The offset-addressed format comprises a fixed-size metadata header, a per-document index of (_offset_, _length_) pairs, and a contiguous content block. Embeddings, graph edges, and posting lists remain in the ANN engine’s index, keeping content placement independent of the search backend.

Offsets support direct lookup of individual payloads. When requested documents share a segment, GCF (§5.4) reads their index slab once and coalesces their extents into page-aware windows. Both post-search fetch and SICP use this path to exploit the locality created by RPAG (§5.2).

ConStore maintains a single doc\_map that resolves any document ID to its segment and local index in _O_(1). The runtime representation is a packed pair of 32-bit integers, so the map costs 8 B per document, roughly one percent of the embedding-side ANN index memory in our workloads. This small fixed metadata cost keeps the fetch path independent of the ANN engine while avoiding a per-query hash lookup or external metadata lookup on the critical path.

### 5.2 Co-Retrieval-Pattern-Aware Grouping (RPAG)

The effectiveness of CCS depends critically on which documents share a segment. Documents grouped together pay one batched page-aware read plan per top-_K_ overlap; documents in different segments require separate segment-level plans. The layout policy is therefore the lever that controls the per-fetch-cost axis of  1.

**Co-retrieval graph and partition objective.** RPAG treats the training retrieval log as a weak supervision signal for physical locality. Each document is a vertex in a graph _G_=(_V,E_). For a query _q_, let _R<sub>q</sub>_ be the ANN result list and \(\rho_q(d)\) be the rank of document _d_ in that list. For every pair of documents that co-occur in _R<sub>q</sub>_, RPAG adds an undirected edge whose contribution depends on the worse rank of the pair. For wider training lists, RPAG can avoid treating all top-_K_ co-occurrences equally by using prefix-weighted edges: pairs that co-occur in the head of the result list receive the largest weight, and pairs that co-occur only in deeper prefixes receive progressively smaller weight. RPAG instantiates this rule with an ordered prefix set \(\mathcal{C}=\{\kappa_1<\cdots<\kappa_L=K\}\) and<tbc>

