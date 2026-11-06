<tbc>layout. Production vector databases commonly organize payloads by insertion or key order, not co-retrieval \[38, 51, 53\]. Frequently co-retrieved items can therefore remain scattered, requiring separate reads and limiting coalescing.

Embedding-based clustering is only a proxy for co- retrieval locality. A question about a film director’s birthplace may need both the film page and the director’s biography, even if their embeddings lie in different clusters. Such documents benefit from co-location based on observed co-access rather than embedding proximity alone.

## 3 ConStore Overview

ConStore reduces end-to-end retrieval latency by overlapping content reads with vector search and reducing the I/O required to fetch content. Prefetching exploits available SSD bandwidth during search under a bounded I/O budget; layout optimization reduces content-I/O demand.

The two techniques are complementary and independently applicable (Figure 4). First, SICP (§4) prefetches likely result payloads from the evolving ANN candidate queue, overlapping reads with search while preserving the final top-_K_. It works with any content layout that provides a document-to-extent lookup.

Second, co-retrieval-aware layout with grouped fetch (§5) reduces per-fetch cost. RPAG groups frequently co-retrieved documents into CCS segments, and GCF coalesces requested content into page-aware reads. Workload-Adaptive Segment Reorganization (WASR, §5.3) adapts this layout to workload shifts by selectively regrouping segments under a bounded rewrite budget when recurring co-retrieval patterns change. This path requires no ANN-engine changes and benefits both prefetching and post-search fetch.

1 separates _when_ reads execute from _how much I/O_ they require. Combined, SICP issues GCF’s grouped reads during search, sharing the same planner with post-search fetch.

**_Lifetime of a query._** While the foreground ANN search runs, one background worker observes read-only candidate snapshots and prefetches through GCF when stability and budget checks pass. Search runs to completion with its final top-_K_ unchanged. ConStore then joins the worker and fetches any missing result payloads through the same GCF path.

§4 first presents SICP, the more general of the two techniques; §5 then formalizes the storage and layout primitives that make each fetched window cheaper.

## 4 Speculative Inline Content Prefetch

Prefetching must balance early candidate churn against a shrinking search tail. SICP exploits the key insight that leading candidates can stabilize before the full search completes: it checks read-only _candidate snapshots_, admits a bounded set of likely results, and overlaps their page-aware content reads with search. Repeated small prefetches adapt to later candidates without committing the entire budget to an early snapshot. A post-search _residual fetch_ serves any final top- _K_ documents not covered by speculation, preserving the search results and recall. The mechanism requires only a document-to-extent lookup, so it works with both insertion- order payload files and the layout of §5.

§4.1 presents the overall design, §4.2 develops the policy that decides when each prefetch starts and which content windows it admits, and §4.3 describes the engine-level hooks that expose search progress.

### 4.1 Overall Design

Figure 5 shows the SICP process and contrasts it with the sequential baseline. SICP performs one full ANN search, but instruments the existing DiskANN/SPANN search loop with a lightweight read-only progress callback. Each callback reports how far the search has advanced and copies the current ranked candidate state into a candidate snapshot. For DiskANN, progress is measured in graph-search hops; for SPANN, progress is measured by SSD posting-list entries processed during refinement. A background _prefetch worker_ consumes these snapshots and issues content reads; it cannot modify, prune, or reorder the foreground vector search.

Before issuing a prefetch, the worker applies the stability and progress checks of §4.2 to avoid spending bandwidth on transient candidates. It admits only a bounded number of new candidates, skipping documents covered by earlier<tbc>

\begin{tabular}{ccc}
 & **Wall-clock time** & **Per-fetch cost** \\
**Runtime path** & SICP (§4) & GCF (§5.4) \\
**Storage layout** & -- & CCS + RPAG \\
 & & (§5.1, §5.2) \\
\end{tabular}

DiskANN
$4 Speculative Inline content Prefetch
Residual Contet Fetch
SPANN
CB Hook
CB Hook
Candidate Queue
Candidate Queue
$5.4 Group Content Fetch
# P1
# P2
# Pr
Segment Grouping
Page-aware Planner
Doc. Seg ID map
Fetch Executor
Memory
SSD
Full Vector 1
Centroid
Neighbor ID
$5.1 Co-Retrieval Content Segment
V_ID Vector Data
Noighbor ID
Query Dataset
V_ID Vector Data
Graph Node Pages
$5.2 Co-Retrieval Pattern Aware Grouping
Posting-list Files
$5.3 Workload Adaptive Segment Reorganization
Co-retrieved Docs
Online
Offline

**Figure 4.** ConStore architecture.

** 1.** The two techniques of ConStore and their promises

