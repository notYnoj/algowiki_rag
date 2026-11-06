<tbc>vector accesses. We explain why this extension remains oblivious. To hide whether a lookup hits a cache, both cases follow the same fixed schedule. With this design, the control flow is identical for every graph access. Regarding the access pattern, all nodes, including dummy nodes, are accessed at most once, thereby guaranteeing non- repetitive access. In addition, the graph is pre-shuffled to ensure data anonymization. By the same argument, these vector accesses are also non-repetitive and data-anonymized, and hence oblivious. Thus, the multi-query protocol securely realizes _U_ sequential invocations of the ideal functionality in Figure 2. The full proof is in the extended version \[49\].

#### 5.1.2 Complexity Analysis.

For _U_ queries, at the base layer we keep _ef=O(k_) and run _T=O(k_) iterations per query. Each iteration performs: _M=O_(1) distance evaluations in R_<sup>d</sup>_; _M_ oblivious scans over _V_<sup>D</sup> and _V_<sup>G</sup> of size _O(Uk_); and two oblivious sort network evaluations over _C_ and _W_, each of size _O(k_). Thus, both communication and local computation costs at the base layer are _O(Ukd+Uk_<sup>2</sup>log<sup>2</sup>_k+U_<sup>2</sup>_k_<sup>2</sup>), and for the _O_(log_N_) non-base layers with _ef=_1 they are _O_((_Ud+U_<sup>2</sup>)log_N_). Therefore, the multiple- query protocol has total communication and local computation costs \(O\big(Uk(d+klog^2k+Uk)+(Ud+U^2)logN\big)\).

## 6 BATCH QUERY PROOL IN PARALLEL

The preceding multiple-query protocol processes queries sequentially. We further consider the batch setting, where _U_ queries arrive together. We propose a batch protocol that processes the _U_ queries in parallel, reducing the round complexity from _O(U_) to _O_(log<sup>2</sup>_U_).

The key idea is to share vectors fetched by any query across all _U_ queries, so every query steps forward together by updating its own _C_ and _W_. Each iteration has two stages. First, the protocol obliviously deduplicates the nearest candidate from each query’s _C_, replaces duplicates with dummies, and issues _U_ distinct graph accesses. Second, it obliviously deduplicates the \(U\cdot M\) returned neighbor IDs and fetches \(U\cdot M\) vectors. Each query evaluates its distance to all \(U\cdot M\) fetched vectors, regardless of which query requested each vector. The batch therefore performs \(U^2\cdot M\) distance evaluations in parallel. These distances update the query’s own candidate set _C_ and result set _W_. The protocol records all fetched vectors in one global visited array _V_ shared by all queries. Each of the two oblivious deduplication steps sorts _O(U_) elements, requiring an oblivious sort network of depth _O_(log<sup>2</sup>_U_), which determines the per-iteration round cost. The full algorithm and the round-complexity proof appear in the extended version \[49\].

## 7 EVALUATION

In this section, we empirically evaluate HNSecW and aim to answer the following questions:

\(\bullet\) **Search quality.** What search quality does HNSecW achieve, and how does it perform when integrated into downstream RAG?

\(\bullet\) **Overhead.** What computation and communication overhead does HNSecW incur, and how does it perform against state-of-the- art secure ANN constructions?

### 7.1 Experimental Setup

**MPC Backends.** HNSecW can be instantiated with any semi- honest MPC protocol tolerating _t_ corruptions among _s_ servers. We evaluate two common configurations:

\(\bullet\) **Semi-honest 2PC (** _s=_2_,t=_1**).** Our 2PC uses ABY’s semi- honest mixed-protocol backend \[12\]. Arithmetic sharing handles distance computation. Boolean sharing handles visited checks. Yao’s garbled circuits handle comparisons, sorting, and candidate updates. ABY provides secure conversions among these representations.

\(\bullet\) **Semi-honest 3PC (** _s=_3_,t=_1**).** Our 3PC uses MP-SPDZ’s semi- honest replicated secret-sharing protocol over a 64-bit ring \[25\].

**Hardware and Network Environment.** All experiments run on a single server with an AMD EPYC 9554P CPU (64 physical cores, 3.1 GHz) and 565 GB of RAM, where each MPC party runs as a separate single-threaded process. We emulate two networks: a LAN with 4000 Mbps bandwidth and 1 ms RTT (a standard MPC LAN setting \[11, 28\]), and a WAN with 320 Mbps bandwidth and 50 ms RTT, following typical U.S. East–West latency per cloudping.co<sup>3</sup>.

**Datasets.** We evaluate on 10 widely-used ANN benchmarks \[3, 37\] ( 3), spanning \(N\in[6\times 10^4,10^9]\), \(d\in[96,960]\), and both \(\ell_2\) and cosine metrics. The selected scale range covers the practical RAG deployment regime. Due to space limitations, the main text reports four representative datasets covering both scales (SIFT-1M, GIST-1M, BIGANN-1B, DEEP-100M); results for the remaining six datasets are provided in the extended version \[49\]. All recall experiments use 10<sup>3</sup> queries per dataset and report the 95th percentile.

**Comparison Baselines.** As Section 2.4 explains, existing secure ANN protocols target different security models and thus provide no direct baseline for our symmetric MPC setting. PANTHER \[28\] is a notable exception: like our protocol, its search algorithm is fully oblivious. However, under its client-server setting, the client accesses the plaintext query and the server stores the plaintext database, enabling lightweight PIR and distance computation between encrypted queries and plaintext vectors by ciphertext–plaintext multiplications. We adapt PANTHER by replacing PIR with DORAM \[16\] and computing distances by ciphertext–ciphertext multiplications. This adds overhead but preserves its search algorithm. We compare the asymptotic performance of PANTHER’s cluster- based search and our graph search under the same security model. Figure 9 reports PANTHER’s original cost and the adaptation overhead separately. Pacmann \[50\] is another related graph-based ANN algorithm for query-private search, but it assumes a public database and graph index, with the client retrieving entries through PIR and searching locally in plaintext. Although PIR can be replaced with DORAM, securely realizing local search would require a complete<tbc>

<sup>3</sup>https://www.cloudping.co/. Accessed: 2026-09-23.

\begin{tabular}{cccccccc}
**Dataset** & & **N** & **d Metric** & \multicolumn{2}{c}{**Dataset**} & **N** & **d Metric** \\
SIFT-1M & & 10<sup>6</sup> & 128 & \(\ell_2\) & DEEP-image & 10<sup>7</sup> & 96 Cos. \\
DEEP-1M & & 10<sup>6</sup> & 96 & \(\ell_2\) & DEEP-100M & 10<sup>8</sup> & 96 & \(\ell_2\) \\
GIST-1M & & 10<sup>6</sup> & 960 & \(\ell_2\) & BIGANN-1B & 10<sup>9</sup> & 128 & \(\ell_2\) \\
MNIST-60K & & 6\(\times 10^4\) & 784 & \(\ell_2\) & SPACEV-1B & 10<sup>9</sup> & 100 & \(\ell_2\) \\
Fashion-60K & & 6\(\times 10^4\) & 784 & \(\ell_2\) & SSNPP-1B & 10<sup>9</sup> & 256 & \(\ell_2\) \\
\end{tabular}

** 3: ANN datasets used in our evaluation \[3, 37\].**

