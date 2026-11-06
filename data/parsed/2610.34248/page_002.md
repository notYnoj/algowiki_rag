<tbc>and returns only the results to the querier. However, delegating all sensitive information in plaintext to a single, fully trusted entity may violate privacy regulations like GDPR and introduce severe risks of data breaches or misuse.

This motivates people to seek cryptographic solutions that can remove the need for trusted third parties. One natural solution is to implement ANN search in the secure multi-party computation (MPC) model \[47\]. In these solutions, the database owner and the querier secret-share the vector database and queries across multiple servers. The servers then jointly execute the ANN search protocol on these shares. The security of MPC ensures that no single server can reconstruct any input. Several recent efforts pursue this direction. However, most existing solutions either relax privacy guarantees by assuming a public database \[50\], or incur high computational overhead \[11, 28\]. Specifically, the two closest MPC solutions to our setting \[11, 28\] rely on cluster-based ANN pipelines: the database of size _N_ is partitioned into clusters, and the protocol identifies and searches the clusters most relevant to a query. Their efficiency depends heavily on the number of clusters, which is typically set to \(\sqrt{N}\) to balance cluster selection and in-cluster search costs. As a result, their search time becomes \(O(\sqrt{N})\) for each query. This quickly becomes impractical at modern database scales, because under MPC, each additional vector access incurs heavy communication, particularly for high-dimensional vectors. Earlier secure _k_NN works \[34, 36, 38, 53\] target smaller-scale or specialized two-party settings rather than scalable secret-shared ANN.

This motivates us to develop a more efficient MPC ANN protocol. The natural idea is to deploy a state-of-the-art hierarchical graph-based ANN algorithm, such as HNSW \[32\], under the MPC setting. By building a multi-layer graph index over the database, such algorithms enable efficient search: the query starts at the top layer, takes only a few steps per layer, and then moves to lower layers. It is widely accepted that, in practice, these indexes visit only _O_(log_N_) out of _N_ vectors per query in expectation, where _N_ is the database size.

However, implementing this hierarchical graph-based search in MPC is very challenging. At a high level, we must make two parts of the algorithm oblivious: (i) the search logic, e.g., when to stop the search, and (ii) the access pattern. The stopping condition in HNSW is highly data- and query-dependent and replacing it with data-independent predicates without careful consideration totally compromises efficiency. For the access pattern, the search process may revisit the same node or vector multiple times, creating highly non-uniform and query-dependent memory accesses. Some naive approaches to hide such redundant access patterns, such as ORAM \[18\], would incur prohibitive communication overhead. Therefore, this naturally raises a fundamental research question:

### 1.1 Our Results

In this paper, we give a positive answer to the above question by proposing the first MPC ANN protocol with logarithmic online query complexity. Our protocol starts from the SOTA hierarchical graph index HNSW. We first study the single-query setting. To make the search logic fully oblivious, we design a data-independent control flow with a fixed search-termination bound and redesign all data structures as fixed-size arrays that support oblivious updates.

To achieve an oblivious access pattern, we combine offline random reshuffling with a duplicated vector database, yielding _O_(1) online overhead for each graph-index and vector access. Overall, our single-query MPC protocol achieves logarithmic online search complexity with at most a \(2\times\) increase in vector storage. Moreover, we extend this design to support multiple queries. To handle repeated accesses across queries while avoiding additional online reshuffling, we introduce cross-query "double visited" structures that cache the graph nodes and vectors accessed by earlier queries, enabling later queries to reuse the cached information without revisiting the graph index and vector database. In summary, our results are as follows:

(1) **Single query.** For a single query, HNSecW achieves _O_(log_N_) online searching complexity over a database of size _N_. As  1 shows, HNSecW substantially outperforms state-of-the-art secure ANN baselines (SANNS \[11\], PANTHER \[28\]), whose clustering- based pipelines have online communication that scales as \(\sqrt{N}\).

(2) **Multiple queries.** For _U_ sequential queries, we propose a multi-query protocol with an amortized cost of _O(U_log_N_). Unlike schemes requiring reshuffling per query (e.g., PANTHER \[28\]), our protocol allows _U_ queries to share a single offline reshuffle, avoiding additional online overhead.

(3) **Parallelism and batch queries.** Additionally, we design parallel implementations of the above protocols: for the single-query protocol, the critical-path length is _O_(log_N_), and for the multiple- query protocol, it is _O(U_log_N_). We also propose a batch-query protocol with higher parallelism that processes a batch of _U_ queries simultaneously with a much lower critical-path length of _O_(log<sup>2</sup>_U_+log_N_).

(4) **Empirical evaluation.** We conduct a comprehensive experiment on large-scale ANN benchmarks. HNSecW reaches recall over 0.9, matching the state-of-the-art plaintext ANN algorithm. At the same target recall, HNSecW achieves up to \(22\times\) WAN speedup and \(46\times\) less communication versus 2PC PANTHER; against the exact- top-_k_ 3PC SORT baseline, it achieves up to \(1.6k\times\) WAN speedup and \(617\times\) less communication. All code is now available <sup>1</sup>.

## 2 PRELIMINARIES

We introduce notation and background on ANN search, HNSW algorithm, secure multi-party computation, and oblivious RAM.

<sup>1</sup>https://github.com/Kleenex-ultrasoft/Secure\_ANN. Accessed: 2026-09-23.

\begin{tabular}{ccccc}
 & \multicolumn{2}{c}{**Single Query**} & \multicolumn{2}{c}{**Multiple Queries**} \\
**Scheme** & **Communication** & **Round** & **Communication** & **Round** \\
SANNS \[11\] & \(\tilde{O}(N^{1/2}d)\) & \(\tilde{O}(1)\) & \(\tilde{O}(UN^{1/2}d)\) & \(\tilde{O}(U)\) \\
PANTHER \[28\] & \(\tilde{O}(N^{1/2}d)\) & \(\tilde{O}(1)\) & \(\tilde{O}(UN^{1/2}d)\) & \(\tilde{O}(U)\) \\
HNSecW (Ours) & \(\tilde{O}(d)\) & \(\tilde{O}(1)\) & \(\tilde{O}(Ud+U^2)\) & \(\tilde{O}(U)\) \\
\end{tabular}

** 1: Online costs for top-**_k_ **ANN. Communication and round complexity for one query and** _U_ **sequential queries over** _N_ **vectors of dimension** _d_**, with** _k=O_(1)**.** \(\tilde{O}(\cdot)\) **hides polylogarithmic factors in** _N_ **and** _d_**.**

