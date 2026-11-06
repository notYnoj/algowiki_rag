<tbc>where _t_ is the current epoch, _W_ is the number of retained buckets, _a_ is a bucket’s age, \(0<\gamma\le 1\) is the decay factor, and _c_<sub>_t-a_</sub>(_u,v_) is that epoch’s pair weight using RPAG’s rank-prefix weighting (§5.2). Bucket rotation expires old evidence. The monitor also keeps the undecayed occurrence count _n<sub>t</sub>(u,v_) over these buckets; a pair is _confirmed_ when \(n_t(u,v)\ge\theta\), where \(\theta\) is the minimum repeat count. This filters one-off co-occurrences before they can trigger rewrites.

**Layout-quality signal and trigger.** To avoid rewriting for frequency changes that do not harm locality, WASR tracks the _confirmed cut ratio_ of assignment _P_, where _P(u_) is document _u_’s segment:

\(\chi_t(P)=\frac{\sum_{(u,v):n_t\ge\theta,P(u)\neq P(v)}w_t(u,v)}{\sum_{(u,v):n_t\ge\theta} w_t(u,v)},\)

the fraction of confirmed edge weight split across segments. With no confirmed edges, there is no evidence to reorganize. Otherwise, WASR compares \(\chi_t\) with the reference \(\chi^*\) recorded at layout publication. Planning requires a rise greater than \(\delta\) for _h_ consecutive epochs and recurrence \(r_t\ge r_\mathrm{min}\). Here \(\delta\) is the tolerated degradation, _h_ filters transient shifts, and _r_<sub>min</sub> requires repeated evidence. A plan must also clear the gain threshold below, avoiding rewrites with little expected benefit.

**Budgeted bundle planning.** WASR reorganizes bundles of whole segments to preserve balanced groups and page locality without leaving partially dead segments. The planner charges each confirmed cross-segment edge to both endpoints’ segments, ranks segments by cut weight per byte, and selects them with their heaviest cut partners under a byte budget. Joint selection lets newly co-retrieved documents be regrouped. METIS repartitions the bundle into segments of at most _B_ documents, followed by RPAG’s intra-segment ordering; documents without recent edges retain their previous grouping, packed first-fit. A plan is accepted only if the recovered cut weight is at least a fraction _g_<sub>min</sub> of total confirmed weight.

A token bucket adds _b_ times the corpus bytes per epoch and caps accumulated credit, bounding rewrite volume and bursts after quiet periods. Foreground queue-depth and tail- latency guardrails further limit the active rewrite rate.

**Immuitable generations and reclamation.** To keep queries consistent during reorganization, each layout generation contains segment files and its own doc\_map. Publication writes new segments under fresh IDs, hard-links untouched files, records a manifest, fsyncs, and atomically renames the staging directory. Each query pins one generation, so it never mixes old and new layouts; the ANN index and recall remain unchanged. Retired segments are deleted only after the last reader of the old generation exits. Replacing whole segments avoids holes and garbage collection within partially live files.

### 5.4 Group Content Fetch (GCF)

GCF is the runtime mechanism that consumes the locality created by CCS and RPAG. For each query, ConStore uses the document-to-segment map and per-document content index described in §5.1 to collect requested documents that fall in the same CCS segment. The segment is the planning scope, but the read unit is a page-aware content window rather than the whole segment.

Within a segment, GCF turns the requested documents into a small window-planning problem. It first orders the requested local document IDs, reads the corresponding contiguous content-index slab, and converts each (_offset, length_) entry into an absolute file extent. Alignment is performed on these absolute offsets, so the planned windows correspond to the device pages actually read rather than to offsets relative to the segment’s content block.

To reduce requests without excessive overfetch, GCF scans extents in offset order and greedily merges their page-aligned windows. A merge that adds no pages is always accepted; otherwise it must satisfy caps on window size, read amplification (aligned bytes divided by useful bytes), and the gap between extents. If a cap fails, the planner starts a new window; a single large document still receives a complete aligned window. Nearby requested content thus shares I/O, while distant content is fetched separately rather than reading the whole segment.

The same window plan is used by both SICP’s prefetch worker and the post-search residual fetch. After a planned window is issued, documents whose content ranges are fully covered by fetched pages are marked warm, allowing the residual path to skip them and fetch only uncovered final top-_K_ documents. This bookkeeping does not change the ANN result or the window-building rule; it only shares page coverage between the speculative and residual uses of GCF.

The result is fewer content read requests and fewer device pages per top-_K_ fetch. A GCF hit amortizes the segment’s content-index access and serves multiple co-retrieved documents from one shared window; a miss simply degenerates to the normal single-document window. This lowers IOPS demand and queueing pressure without changing ANN search results or depending on a particular ANN backend.

## 6 Evaluation

### 6.1 Setup

Experiments run on a two-socket Intel Xeon Gold 6230N server with 2.30 GHz 40 cores, 251 GiB DRAM and a 1.6 TB Intel SSDPEDME016T4 NVMe SSD.

**Datasets.** The primary corpus is Wikipedia DPR [27], with 21M passages averaging 1 KB and 768-dimensional embeddings. We use three multi-hop QA workloads: 2WikiMultihopQA [18], HotpotQA [57], and MuSiQue [49], containing 12,576, 7,405, and 2,417 questions, respectively. Each<tbc>

