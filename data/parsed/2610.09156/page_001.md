# Compiling Semi-Ring Dynamic Programming to Tier-Aware 3D-DRAM Processing-in-Memory

### Abstract

Processing-in-Memory (PIM) on monolithic 3D (M3D) DRAM is a promising answer to the memory wall for data-intensive dynamic programming (DP), yet extracting its performance today demands hand-written kernels: the programmer must pick a tile size, place data across non-uniform-latency memory tiers, partition work between heterogeneous processing units, and insert the right broadcasts and queues by hand. We present _GenMLIR_, an MLIR compiler that automates this mapping for tier-aware 3D PIM. GenMLIR encodes the semi-ring generalized grid update, the algebraic form shared by all-pairs shortest path (APSP) and sequence alignment, as a first-class IR abstraction, and lowers it through four GenDRAM- aware pass groups that derive blocked tiling, tier-aware placement, tile-to-PU assignment, and explicit communication. We also characterize precisely which DP recurrences the abstraction admits and which it does not. On the GenDRAM architecture, GenMLIR- generated code runs up to 5.8\(\times\) (APSP) and 16.7\(\times\) (alignment) faster than a lowering without compiler support, and 1.2-1.4\(\times\) faster than a standard affine-tiling PIM compiler we also implement, reaching 90-100% of an achievable-performance bound. It expresses these workloads in 4-9 lines instead of ∼300-500 and compiles in a negligible fraction of runtime.

### Keywords

Processing-in-Memory, MLIR, Monolithic 3D DRAM, Dynamic Programming, Compiler, Tier-Aware Data Placement

### 1 Introduction

Monolithic 3D DRAM bonds a logic die directly beneath a stack of DRAM layers, exposing tens of TB/s of internal bandwidth to compute units placed next to the banks [20]. This makes it an attractive substrate for dynamic programming (DP) workloads such as all-pairs shortest path (APSP) and genomic sequence alignment, whose runtime is dominated by data movement rather than arithmetic [1, 7, 14]. Recent PIM accelerators exploit exactly this [15, 24].

The hardware, however, has outrun the software. A modern 3D PIM part such as GenDRAM [15] presents the programmer with a stack whose row-access latency varies by 1.6\(\times\) from the bottom tier to the top, two functionally distinct classes of processing unit, an inter-PU ring that must be driven in either broadcast or pipelined mode, and a bank-group geometry that dictates how tiles may be laid out. Achieving good performance means choosing a tile size against an on-chip SRAM budget, pinning latency-critical tables to fast tiers while interleaving bandwidth-bound tensors across channels, assigning tiles to PUs so that neighbors do not collide in the same bank, and inserting broadcasts, barriers, and queues that respect the recurrence. Today all of this is done by hand, once per

kernel. The resulting code is unportable and, more importantly, it is not reusable: a change of recurrence means starting over.

Our starting point is an observation made by the GenDRAM authors [15] and, before them, by the GraphBLAS community [11]: APSP and sequence alignment are the same computation over different semi-rings. Both repeatedly update a cell of a grid by combining (\(\otimes\)) two neighbors and accumulating (\(\oplus\)) the result. GenDRAM used this isomorphism to justify a _single hardware substrate_. We argue it also supports a single _compilation_ strategy--and that this is where the abstraction pays off most, because the tiling, dependence, placement, and communication decisions listed above are all independent of which semi-ring is instantiated. What is workload-specific is only the execution mode.

This paper turns that argument into a compiler. **GenMLIR** is an MLIR stack that takes a semi-ring DP recurrence plus a small configuration record and emits a GenDRAM command stream. Its contributions are:

\(\bullet\) **An IR for tier-aware DP.** We encode the generalized grid update as an MLIR dialect and pair it with a device-level dialect that exposes tiers, bank-groups, PU classes, and communication primitives, so that placement and scheduling become IR rewrites rather than hand edits (§3).

\(\bullet\) **A characterization of the abstraction’s reach.** We identify the algebraic conditions a recurrence must satisfy to be admitted, enumerate seven DP problems that qualify, and state explicitly which ones do not and why (§3.5). This scopes a claim that was previously left open.

\(\bullet\) **Tier-aware and heterogeneity-aware passes.** We give a capacity model that derives the tile size directly from the PU SRAM budget, a tier assignment driven by access-latency sensitivity, and a mode-selection pass that chooses between broadcast and producer--consumer lowering (§3.3). We separate these from the standard transformations we reuse.

\(\bullet\) **An evaluation against strong baselines.** We compare against an achievable bound and a standard affine-tiling PIM pass, not only against a lowering without compiler support, and add a memory-traffic analysis and compile-time and lines-of-code measurements (§4).

### 2 Background and Related Work

#### 2.1 Dynamic Programming as a Semi-Ring

A semi-ring is a set equipped with an associative combination operator \(\otimes\) and an associative, commutative accumulation operator \(\oplus\) over which \(\otimes\) distributes. A large family of DP algorithms updates a matrix _D_ by

Mahbod Afarin University of California San Diego La Jolla, California, USA mafarin@ucsd.edu

Tsung-Han Lu University of California San Diego La Jolla, California, USA tsl012@ucsd.edu

Tajana Rosing University of California San Diego La Jolla, California, USA tajana@ucsd.edu

arXiv:2610.09156v1 [cs.AR] 6 Oct 2026

