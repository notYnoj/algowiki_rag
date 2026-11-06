<tbc>F<sub>HNSW</sub>, and the public parameters. We provide the full proofs in the extended version \[49\].  2 summarizes the public parameters.

The ideal functionality and the threat model imply symmetric privacy and correctness. For **query privacy**, the database owner and all MPC servers learn nothing about \(\vec{q}\) beyond what is implied by the public parameters. For **database privacy**, the querier and all MPC servers learn nothing about D or G beyond the top-_k_ result vectors output by F<sub>HNSW</sub> and what is implied by the public parameters. For **correctness**, for any inputs \((\mathcal{D},\mathcal{G},\vec{q})\), the querier reconstructs the output of the ideal functionality F<sub>HNSW</sub>.

## 3.2 Single-Query

Even when all vectors and their distance to the query are kept secret, a single HNSW query is not oblivious in its control flow, data structures, or graph and vector access patterns, all depending on the underlying graph and query. Achieving obliviousness to prevent leakage requires a dedicated analysis of the performance features that HNSW presents, since a generic method that follows only worst-case conditions would introduce prohibitive overhead. In our protocol, we design customized optimizations to make each part oblivious by taking advantage of its unique features. For a single query, we traverse each layer without revealing the access pattern. At every layer, we use our oblivious data structure to maintain the search state, and we terminate the traversal using a tailored termination condition that prevents information leakage. We outline the key ideas here, with full details in Section 4.

\(\bullet\) **Control flow.** We eliminate data-dependent stopping conditions by replacing them with a fixed iteration bound derived from a detailed analysis of HNSW’s stopping behavior, ensuring obliviousness with only negligible recall loss (Section 4.1). Although there is no theoretical bound on the iterations, we found that in the specific context of RAG, we could set a tight upper bound on the number of iterations without degrading the end-to-end performance.

\(\bullet\) **Data structure.** We observe that both the candidate set and the result set exhibit a monotonic exclusion property: once a node is excluded, it will not be included in these sets again. Using this monotonicity, we design an oblivious data structure for both sets that keeps them at a fixed size and removes farther nodes through fixed-size tail truncation after oblivious sorting (Section 4.2).

\(\bullet\) **Graph and vector access pattern.** We use the fact that HNSW naturally avoids revisiting a node more than once per layer. To further reduce redundant access across the layers, we assign each layer an independently shuffled graph and vector tables so every address is accessed at most once, yielding fully oblivious access patterns.

## 3.3 Multiple-Query

Extending the single-query protocol to multiple queries introduces a fundamentally new challenge: different queries may revisit the same graph node and its associated vector. Hiding these repeated visits would require reshuffling the graph and vector tables after every query. However, such per-query reshuffling is impractical in an online setting due to the significant latency it entails. To address this, we rely on the insight that once data has been accessed, it can be cached and reused across queries rather than accessed repeatedly. We propose to use two global cross-query visited structures, one for graph neighbor lists and one for vector contents. These structures serve as a secure shared cache: once any query retrieves a node or vector, it is stored in the global visited array. Subsequent queries check this array first and reuse the cached data. As a result, each graph or vector access first scans the cache and then performs a real or dummy data-access step. Under this design, every node and vector is accessed at most once from the underlying shuffled tables globally, while subsequent revisits are served through oblivious cache scans. Combined with one-time random pre-shuffling, this keeps the overall access pattern oblivious; see Section 5.

## 3.4 Parallel-Enhanced Batch Model

Furthermore, we consider how the oblivious HNSW search can be executed in parallel. The single-query protocol already exhibits high parallelism, but its multiple-query extension is designed to process the _U_ queries sequentially, giving a linear circuit depth of _O(U_). In a batch setting where many queries are available simultaneously, it is natural to ask whether the computation can be reorganized to reduce this depth to better exploit parallel execution. As in the multiple-query setting, the fundamental challenge is to avoid accesses to the same nodes and vectors across queries. A naive approach is to cache every accessed element (neighbor lists and vectors), as in the sequential protocol. But in the batch setting, such a large cache is unnecessary. Our key insight is that, because all queries proceed in synchronized iterations, we do not passively wait for cache hits and reuse; instead, we force \(U\cdot M\) accessed vectors to be evaluated against _U_ queries: if a query later needs that vector, it can skip the inner path; if not, the extra evaluation does not affect correctness. This eliminates the need for a massive cache and naturally prevents redundant accesses. As a result, the batch-query protocol achieves a depth of _O_(log<sup>2</sup>_U_+log_N_), coming from the oblivious duplicate removal of the \(U\cdot M\) neighbors per iteration plus the _O_(log_N_) HNSW layers.

\begin{tabular}{cc}
**Category** & **Public Parameters** \\
Data characteristics & Vector dimension _d_; Dataset size _N_; Number of layers _L_; Degree bound _M_; Per-layer sizes \(\{N_t\}_{t=0}^{L-1}\) \\
Search hyperparameters & Result set size _ef_; Nearest neighbor output size _k_ \\
Multi/Batch-query setting & Number of queries _U_ \\
\end{tabular}

Functionality F<sub>HNSW</sub>[Q]
Public Input: Q: (Rd)N X G X Rd (Rd)k.
Inputs: D = {x}i
N-1 -
and G
Compute: Upon receiving (dataset, D, G) from DO, and (query, q) from Querier, where G is an HNSW graph, compute
Outputs: Upon receiving (continue) from all servers, send
(v0, , ,
to Querier.

**Figure 2: Ideal functionality for securely computing HNSW.**

** 2: Public parameters of the system.**

