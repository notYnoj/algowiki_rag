<tbc>RNSG \[7\] and iRangeGraph \[8\] target range predicates; STABLE \[9\] fuses metric and attribute signals into one joint- semantic graph. All build a _single static_, single-tenant index over the joint space; we add streaming inserts/deletes/tenancy- migration, multi-tenant isolation, and an analytical bound. These designs secure same-label reachability at build time; our repair must preserve it under churn, which shapes the<tbc>

<tbc>scheduler’s ordering.

### b) Streaming / dynamic graph ANN.:

FreshDiskANN \[10\] (two-pass StreamingMerge, our substrate), SPFresh \[11\], IP-DiskANN \[12\], CleANN \[13\], Wolverine \[14\], and Mycelium-Index \[15\] operate on unfiltered, single-tenant data with at best empirical recall stability. PipeANN \[16\] (OSDI’25) and OdinANN \[17\] (FAST’26) are the current single-tenant SOTA, their pipelined-SSD search and direct-insert (no-merge) design sidestepping the scheduling problem we solve rather than solving it; neither has a tenant concept or a recall bound, so we cede the single-tenant axis and compare against a per-tenant _sharding_ of each. LSM-VEC \[18\] organizes a vector index as an LSM tree, and UBIS \[19\] is the closest streaming competitor, scheduling concurrent updates to keep recall stable under high update rates but reporting that empirically with no bound. None provides filtering \(\times\) multi-tenancy \(\times\) a bound jointly.

### c) Multi-tenant ANN.:

Curator \[20\] is the closest prior art, a multi-tenant graph ANN with per-tenant navigability (clustering sub-trees) that is static and in-memory, with no per-tenant SLA scheduling and no bound; we build it and compare (conceding static recall, leading on streaming/SLA/bound/disk-scale). Pinecone Metadata Filtering \[4\] provides filter + multi-tenant + streaming on an IVF/serverless substrate with no analytical bound; GaussDB- Vector \[21\] is a production filtered vector database with real- time inserts/deletes but no per-tenant isolation, SLA scheduling, or bound.

### d) Caches over vector indexes.:

MicroNN \[22\], QVCache \[23\], and LiveVectorLake \[24\] are read-side, or filter- /tenant-blind, or a different layer; our cache is jointly filter and tenant-keyed, on the query path, and is the structure the theorem binds.

### e) Theoretical bounds.:

\[25\] bounds _quantization_ under streaming updates, not a graph’s recall; Random-Walk Dynamic Graph ANN \[26\] bounds hitting-time topology preservation, not recall@_k_ under an SLA; Quake \[27\] estimates recall for _query-time_ parameters, not background work. Distribution-Aware HNSW \[28\] informs our predicted-recall- impact scheduler term. Ours is, to our knowledge, the first per<tbc>

\begin{tabular}{ccccc}
_N_ & ours serving & ours merge-peak & Curator (in-mem) & status \\
18,000 (_T_=6) & 0.77 GB & 1.04 GB & 0.10 GB & measured \\
100,000 (_T_=6) & 0.98 GB & 1.72 GB & -- & measured \\
1,000,000 & ≈ 1.0 GB<sup>‡</sup> & ≈ 9 GB & 5.6 GB & projected \\
10,000,000 & ≈ 2 GB<sup>‡</sup> & -- & 56 GB (OOM) & projected \\
\end{tabular}

F11: bounded RSS (recall 99.70)
ours (measured) linear-in-N ref
4000
steady RSS (MB)
3000
2000
1000
20
40
60
80
100
working set N (K)
F12: memory/scale inversion
16 GB
104
RAM (MB)
103
ours (measured) ours (projected) Curator in-mem (measured) Curator (projected)
102
105
106
107
N (points)

TABLE IV

MEMORY VS. _N_ ON THE MATCHED _T_=6 PAIR, ON _consistent_ CONVENTIONS: _serving_ = WHOLE-PROCESS FIRST STABLE RSS (ITS PER-VECTOR PQ+TAGS COMPONENT IS 0.115 KB/POINT); _merge peak_ = PROCESS PEAK RSS (A RELEASED TRANSIENT, 8.3 KB/POINT). CURATOR IS IN-MEMORY (\(\propto N\)). 1M/10M ARE RESIDENCY-MODEL PROJECTIONS; SERVING<sup>‡</sup> IS QUOTED ON THE PQ+TAGS TERM, THE 1M MERGE PEAK IS UNRUN. (THE SINGLE-TENANT 100K POINT, ≈ 1.06 GB, IS FIG. 3A; IT IS NOT A _T_=6 PAIR MEMBER AND IS OMITTED HERE TO KEEP CONVENTIONS MATCHED.)

<sup>‡</sup> **Convention (measured vs projected serving differ and must be read together).** The measured 18K/100K serving cells are _whole-process_ first stable RSS (fixed baseline ≈ 0.9 GB + configured allocations + the PQ+tags residency); across the matched pair this rises at ≈ 2.6 kB/point. The projected 1M/10M serving cells grow the _only_ \(\propto N\) _term_, the PQ+tags residency at 0.115 kB/point (matching the PQ-code size architecturally, ≈ 102 B/point at 100K), holding the bounded remainder fixed, justified because the RSS decomposition (Fig. S3) attributes the 2.6 kB/point excess to the C2 cache (bounded by high-water, _not_ \(\propto N\)) and per-thread buffers (fixed), not to _N_-growth. Hence the projection ≈ 0.9 GB baseline +0.115 kB/point \(\cdot N\). A naive linear extrapolation of the 2.6 kB/point two-point whole-process slope gives the pessimistic ≈ 3.4 GB at 1M; we report the architectural term as primary because the excess is measured-bounded, and both stay far under the in-memory \(\propto N\) baseline. The two-point marginal is not yet filmed by a third matched point.

Fig. 3. (a, top) Does-it-run: the prototype is bounded and correct at 100K (≈ 1.06 GB, recall 99.70 on-curve). (b, bottom) Memory/scale inversion (log- log): a disk-resident index keeps graph and full vectors off-RAM so only PQ codes grow with _N_, while an in-memory index scales \(\propto N\); measured to 100K, _modelled_ at 1M-10M, with the like-for-like two-point slope shown as the pessimistic alternative.

