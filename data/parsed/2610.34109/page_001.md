# Geo-Filtered Approximate Nearest-Neighbor Search on a Single Proximity Graph

### Abstract

Geo-filtered approximate nearest-neighbor (GFANN) search retrieves the objects inside a query-specified geographic disk whose feature vectors are closest to a query vector, a core operation in location-aware Web search. A disk filter on a standard proximity graph invalidates out-of-disk routing vertices; on selective disks, these removals break greedy paths and recall drops sharply. Existing methods scan all in-disk objects, over-fetch unfiltered candidates, or maintain separate sub-indexes across spatial partitions, trading latency for index overhead. We propose REACH, a single-graph index based on _row-local active-order invariance_: if every vertex stores its outgoing neighbors in a fixed-width row sorted by vector distance, any disk filter masks out-of-disk entries while surviving in-disk (_active_) neighbors remain vector-sorted. Offline, each vertex merges globally closest vector candidates with a nearest-first geographic stream into one row; online, beam search evaluates vector distances only for the first \(\ell\) active entries of each visited row. Because collected objects share the same distance to every query center, every disk admits a coordinate group in full or not at all, decomposing active connectivity into intra-group and inter-coordinate conditions. Under a spatial marked-site model with repeated coordinates, we prove that polylogarithmic out-degree guarantees strong connectivity across all disks and constant-factor distance reduction per hop on compact disks, while a cut-rank threshold characterizes the minimum scan budget \(\ell\). Across four datasets up to 10<sup>7</sup> objects, one REACH index per dataset outperforms SOTA methods, achieving 2.49\(\times\) higher geometric-mean QPS than the strongest baseline at 0.95 Recall@10 on selective queries, while building 3.8\(\times\)-11.9\(\times\) faster and using 37%-45% less space than a SOTA spatial-graph index.

### CCS Concepts

• **Information systems** \(\rightarrow\) **Retrieval models and ranking: Spatial-temporal systems.**

### Keywords

Approximate nearest neighbor search, geo-filtered vector search, proximity graph index, spatial-vector retrieval

### 1 Introduction

Approximate nearest-neighbor (ANN) search in high-dimensional vector spaces is a core operation in Web search, recommendation, and retrieval-augmented generation [20, 27]. Proximity graphs such as HNSW [25], NSG [13], and DiskANN [17] achieve the strongest trade-off between recall and latency [41] by linking each object to proximate vector neighbors and routing queries through best-first beam search. In location-aware Web services, vector similarity is often paired with a spatial range filter: a user may search for geo- tagged photos visually similar to a query image within a kilometer of a landmark, or retrieve points of interest (POIs) matching a text query within walking distance. We call this problem _geo-filtered approximate nearest-neighbor_ (GFANN) search: given a query vector and a query-centered geographic disk, return the _k_ in-disk objects closest to the query in vector space.

Applying a geographic disk filter to a standard proximity graph breaks its navigation structure. Because semantic similarity is independent of physical location, a vertex’s closest vector neighbors are scattered globally; restricting traversal to a disk removes out-of-disk routing vertices, which severs multi-hop paths and disconnects the in-disk subgraph (_filter-induced path erosion_, Section 2). Existing filtered ANN methods struggle as disk selectivity varies [8]. Filter-agnostic strategies fail at one extreme: (1) _pre- filtering_ (_Spatial-First_ [7]) scans all in-disk objects, which is fast on tiny radii but slows by orders of magnitude on neighborhood- or city-scale disks (10<sup>2</sup>-10<sup>6</sup> objects); (2) _post-filtering_ (_Vector-First_, VBASE [46]) retrieves global vector candidates before spatial filtering, wasting most distance evaluations on selective disks; and (3) _in-filtering_ (ACORN [28]) explores two-hop unfiltered neighborhoods, which still disconnect under selective disks. Predicate-aware indexes encode filters into the graph for discrete labels [6, 15, 24, 42], workload-tuned sub-indexes [21], weighted attribute–vector metrics [40, 45], or 1D numeric intervals [12, 23, 43, 47, 48]. However, 1D range graphs rely on a global attribute order under which every interval is contiguous; 2D disks admit no such order even on three objects and induce \(\Omega(n^2)\) distinct active sets (Section 2), whereas spatial partitions [37, 44] either split queries across cell graphs or duplicate edges across tree levels.

In this paper, we show that a _single_ static graph of fixed out- degree can support arbitrary geographic disks through _Ranked Active-Graph Recovery_. Rather than sorting the dataset along a global axis, we use _row-local active-order invariance_: each vertex

Zhiqiu Zou<br> Beijing Institute of Technology<br> Beijing, China<br> fall@bit.edu.cn

Qiangqiang Dai<br> Beijing Institute of Technology<br> Beijing, China<br> qiangd66@gmail.com

Rong-Hua Li<br> Beijing Institute of Technology<br> Beijing, China<br> lironghuabit@126.com

Guoren Wang<br> Beijing Institute of Technology<br> Beijing, China<br> wanggrbit@126.com

