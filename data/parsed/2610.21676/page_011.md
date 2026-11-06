operating points, ConStore lowers device read bandwidth by 23.4% on DiskANN and 19.7% on SPANN. Engine-accounted content traffic and I/O requests also fall, consistent with grouped fetch reducing pressure on search-phase I/O.

### 6.5 Scaling with Top-_K_ and Index Size

We evaluate SICP on SIFT100M and SIFT1B at recall targets 0.90, 0.95, and 0.99. Sequential fetches the synthetic payloads after search; SICP overlaps reads from the same insertion- order file.

Figure 14 shows that overlap remains useful at both scales without changing the final top-_K_. At recall targets 0.90/0.95, DiskANN’s latency reductions reach 42% on SIFT100M and 40% on SIFT1B; SPANN saves 30-43% at _K_=1600 across the two scales. The gain depends on the search/fetch balance, not scale alone: at SPANN’s 0.99 target, search dominates and the corresponding savings fall to 6-11%. Thus, larger result sets create more work to overlap, but a search-dominated pipeline limits the relative end-to-end benefit.

### 6.6 Content Fetch Speedup

We now turn to the second technique and isolate the layout side, measuring content fetch after search completes with no prefetch involved.

**Page-aware fetch and local ordering.** Figure 15 compares Serial (no page-aware coalescing), Page-aware planner (same layout, aligned coalesced reads), and PA + RPAG local reorder (intra-segment reordering followed by the planner). Planning helps both K-Means and RPAG; reordering further places co-retrieved documents on nearby pages, making each read more useful. With both optimizations, RPAG lowers fetch latency by 45-47% over Random and 19-22% over K-Means using the same optimized fetch path. The advantage therefore comes from co-retrieval locality as well as the shared planner.

**Cross-hop reuse opportunity.** RPAG places about half of hop-2 results in segments touched by hop-1, versus roughly 15% for K-Means and 4% for Random ( 2). Grouping co-retrieved evidence thus creates reuse opportunities across hops on both engines. This is a layout-derived upper bound, not a measured cache-hit rate: hop-1 may read only some pages of a segment, and actual reuse requires those pages to remain cached.

### 6.7 Layout Staleness and Adaptation

We replay the DiskANN hop traces as a chronological stream of 500-query epochs under a zipfian query popularity. Four warm-up epochs build the initial layout; each later epoch is evaluated before its queries reach the monitor. For example, "WASR 0.5%" adds rewrite allowance equal to 0.5% of corpus bytes each epoch. Unused allowance accumulates in a capped token bucket, so a single reorganization can exceed one epoch’s allowance; rewrites occur only when the adaptation checks in §5.3 pass. Benefit retention is (_L_<sub>kmeans</sub>-<tbc>

<tbc>_L_<tbc>

<tbc>)/(_L_<sub>kmeans</sub>-_L_<sub>oracle</sub>), where _L_ is the mean number of segments touched per two-hop query under the evaluated policy, and _L_<sub>kmeans</sub> and _L_<sub>oracle</sub> are the corresponding means for K- Means and the oracle. These quantities measure segment accesses, not latency. The oracle is a full rebuild that knows the confirmed graph of the next four epochs.

Figure 16(a) shows that static RPAG loses its locality advantage after the workload shift. WASR detects the degradation and restores locality through selective reorganization: with a 1% per-epoch budget, it rewrites 10.8% of the corpus in total, versus 25% for periodic full rebuilds. Targeting affected segments thus adapts the layout with substantially less rewriting.

Across the seven scenarios in Figure 16(b), WASR rewrites 2.5-12% of the corpus, compared with 15-26% for periodic full rebuilds. Its recurrence and gain checks focus this budget on shifts with reusable co-retrieval patterns rather than rebuilding on a fixed schedule. On the unique-query replay, WASR avoids rewriting entirely because there is insufficient recurring evidence, while periodic rebuilds still incur rewrite cost.

## 7 Related Work

**Vector search optimization.** A long line of ANN work reduces the cost of candidate generation through compression, graph navigation, filtering, and specialized hardware execution. FAISS, product quantization, optimized product quantization, ScaNN, HNSW, and NSG improve vector representation or in-memory search efficiency [8, 11, 15, 22, 26, 35]. DiskANN and SPANN move billion-scale search to SSDs; Filtered-DiskANN, FreshDiskANN, SPFresh, Starling, and FusionANNS extend this line with filters, updates, disk-layout optimization, or CPU/GPU execution [6, 12, 45, 46, 48, 52, 55]. ANN benchmarking work characterizes the recall/latency tradeoff of such indexes [3]. These systems optimize Phase 1 search I/O or scoring; they do not optimize Phase 2 content fetch.

**Retrieval and RAG models.** Neural retrieval systems such as REALM, DPR, RAG, FiD, RETRO, and Atlas show that generation quality depends on retrieving external evidence, often at large _K_ or over very large corpora [5, 17, 20, 21, 27, 32]. More recent active, self-reflective, corrective, and interleaved retrieval methods make retrieval part of the generation loop [2, 10, 24, 50, 56]. Dense and late-interaction retrievers such as ColBERT, ColBERTv2, and PLAID further improve retrieval quality and efficiency, while BEIR and Natural Questions broaden retrieval evaluation [29, 30, 42, 43, 47]. These works motivate larger and repeated evidence fetches, but they do not change how retrieved payloads are placed on storage.

**RAG and LLM serving systems.** RAGCache, Mooncake, and RAGO optimize RAG serving through KV-cache reuse,<tbc>

