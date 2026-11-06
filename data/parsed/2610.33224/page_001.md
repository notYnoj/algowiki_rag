# Holo-NN: Holographic Nearest Neighbor Search via Compressive Sensing

### Abstract

In the age of AI, privacy-preserving approximate nearest neighbor (ANN) search over high-dimensional embeddings has emerged as a critical yet frustratingly challenging domain, dominated by tradeoffs between speed, privacy, and accuracy. Traditional tree and graph-based indexing structures (e.g., HNSW, ScaNN) rely fundamentally on non-linear operations that are computationally intractable under Fully Homomorphic Encryption (FHE) or blind server-side constraints.

In this paper, we introduce **Holo-NN** (**Holographic Nearest Neighbor Search**), an algebraic framework that replaces data-dependent branching with a single linear projection. Our key observation is that while distances across a database are dense, neighborhood membership is inherently sparse: only a handful of points ever lie close to a query. By pairing locality-preserving feature transforms with Compressive Sensing, Holo-NN folds the entire database offline into a compact holographic sensing matrix. At query time, encrypted search reduces to a single, non-interactive matrix-vector multiplication--requiring no FHE bootstrapping, no multi-round interaction, and no client-side index state. This turns private retrieval into an embarrassingly parallel, accuracy-tunable computation that runs out of the box on both CPUs and GPUs, scaling efficiently to production databases. We offer a comparison against other state-of-the-art Private ANN algorithms to help situate the method in the broader context of production-grade private retrieval.

### 1 Introduction

#### 1.1 Motivation & Private Retrieval Landscape

Published in 1750, Cramer’s rule [19] established an exceptionally inefficient and computationally intensive method for solving systems of linear equations based on an exhaustive calculation of determinants. And yet, despite its inefficiency, it introduced an embarrassingly parallel mathematical primitive that modern high-throughput computational hardware can execute with extreme efficiency.

A similar paradigm shift governs modern privacy-

preserving computation. The constraints imposed by fully end-to-end secure computation--such as Fully Homomorphic Encryption (FHE) and Private Information Retrieval (PIR)--fundamentally alter algorithmic tradeoffs, introducing choices that would be sub-optimal in most other settings. In unconstrained plaintext environments, Approximate Nearest Neighbor (ANN) search is dominated by hierarchical graphs (e.g., HNSW [35]) and quantized inverted files (e.g., ScaNN [28]), which exploit non-linear geometric branching to achieve sublinear query times (O(log_N_) for hierarchical graphs such as HNSW). In contrast, in private, blind-server settings, data-dependent branching leaks memory access patterns, rendering graph traversals either insecure, reliant on non-colluding multi-server assumptions (e.g., PRECO [40]), or subject to heavy multi-round cryptographic overheads across garbled circuits, oblivious RAM, or sublinear PIR (e.g., SANNS [14], Tiptoe [29], Pacmann [48], Panther [32], Compass [49]). Under strict single-server privacy constraints, non-interactive systems are forced into an O(_N_) linear scan of the entire database. When server compute and memory capacity are abundant relative to communication bandwidth and cryptographic circuit depth, algorithm design shifts toward strictly linear, non-interactive mathematical formulations.

#### 1.2 Compressed Sensing

Beginning with Claerbout and Muir in 1973 [18], it was discovered that seismological reflection data could be algorithmically improved, even with apparent "violations" of the Nyquist-Shannon sampling criterion [41]. Formalized later into the robust field of Compressive Sensing, it was shown that the supposed violation was backed by the inherent sparsity of the underlying signals [22, 10]. Specifically, for a signal that admits a _k_- sparse representation where \(k\checkmark N\), significantly fewer measurements than _N_ are required for high-fidelity reconstruction. Intuitively, reconstruction is possible because one is attempting to solve for _k_ non-zero elements in an _N_-dimensional space, which can be solved efficiently via convex \(\ell_1\)-optimization algorithms. Formally, given an underdetermined system of linear measurements \(y=As\in\mathbb{R}^M\) with \(M\checkmark N\), an unknown _k_-sparse signal \(s\in\mathbb{R}^N\) can be recovered by solving the convex program \(min_s\left\|s\right\|_1\) subject to _As=y_ (or \(\left\|As-y\right\|_2\le\epsilon\) under

**Bryant Gipson**

Google `bryantgipson@google.com`

arXiv:2610.33224v1 [cs.CR] 23 Oct 2026

