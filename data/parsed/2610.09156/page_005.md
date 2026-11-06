\(\bullet\) **B0 - No compiler support.** Direct lowering of the recurrence: no tiling, no tier awareness, one PU class.<tbc>

\(\bullet\) **B1 - Standard PIM pass.** A standard affine pipeline with loop tiling (tuned _B_), vectorization, and bufferization, but no tier model, PU specialization, or communication synthesis.<tbc>

\(\bullet\) **B2 - Achievable bound.** A performance ceiling: the 32- PU throughput limit for APSP, and wavefront critical-path bound for alignment. No implementation, hand-tuned included, can exceed it, so B3/B2 lower-bounds the fraction of that bound GenMLIR recovers automatically.<tbc>

\(\bullet\) **B3 - GenMLIR.** The full pipeline of §3.

Speedups against B0 quantify how much the pass pipeline contributes; the ratio B3/B2 measures how close GenMLIR comes to the achievable bound.

## 4.2 Performance

Figure 3 reports speedup over B0, a lowering without compiler support (PU mapping kept; tiling, tier placement, and communication off). B1 is a standard affine-tiling compiler pass for PIM that we also implement (G3-G4 off); B2 is an _achievable bound_ (32-PU throughput for APSP, wavefront critical-path for alignment), so B3/B2 lower-bounds the fraction of the achievable bound GenMLIR recovers automatically.

On APSP (Fig. 3a), B3 reaches 5.2, 5.2, and 5.8\(\times\) on ca-GrQc, p2p- Gnutella08, and OSM (geo-mean 5.4\(\times\)), 90% of the throughput bound and meeting it at OSM. The curve is flat by construction: every graph exposes far more than 32 blocks of per-phase parallelism, so all saturate the PU array, and B0\(\rightarrow\)B3 isolates per-tile efficiency, a ratio independent of graph size. Size instead surfaces as memory capacity (§4.3).

On alignment (Fig. 3b,c), B3 grows with read length (2.8 \(\rightarrow\) 9.9\(\times\) PacBio, 4.1 \(\rightarrow\) 16.7\(\times\) ONT over 2-10 kbp) and lies _on_ the critical- path bound throughout (B3/B2= 100%): GenMLIR is optimal for the banded DP, as no schedule beats the anti-diagonal dependency. This is wavefront scaling (band work \(\propto\) length<sup>2</sup>, sweep \(\propto\) length); the 2 kbp point is lowest as a short read has too few diagonals to amortize the wavefront barrier, and ONT’s wider band (30% vs. 15% error) exposes more parallelism than PacBio. Throughout, B3 beats the standard affine-tiling PIM pass B1 by 1.2-1.4\(\times\), the gain from tier-aware placement and communication a size-agnostic pipeline forgoes.

## 4.3 Memory Behavior

Figure 4(a) reports DRAM traffic measured by replaying the blocked Floyd-Warshall op stream through an LRU cache the size of the PU’s on-chip SRAM, counting fetches and dirty write-backs. Traffic tracks the 4_N_<sup>3</sup>_/B_ trend but tile reuse holds it below the closed-form model, and the working set hits a hard capacity wall: at _B\>_256 the three-tile working set (3_wB_<sup>2</sup>) exceeds the 768KB budget, so _B<sup>⋆</sup>_=256 is both the traffic-minimizing and the largest feasible tile the compiler can pick (Eq. (3)). At _B<sup>⋆</sup>_, tiling cuts APSP traffic 192\(\times\) versus the untiled baseline; the already-local alignment DP sees 1.8\(\times\) ( 2).

Figure 4b shows the placement G3 emits for the genomics pipeline. Ranking objects by criticality \(\sigma(o)\), it fills the fast tiers T0-T4 with<tbc>

<tbc>the 17 GB of latency-critical PTR/CAL tables and spills the streaming reads and DP buffers across the slower tiers T4-T7. The distance matrix behaves analogously: B3 keeps the reused pivot working set in T0, whereas the untiled baseline holds only 25% of its 16 GB footprint there, so average access latency drops from 37.4 to 34.6 ns. For alignment, where the tiering deliberately trades the latency of the scoring matrix _H_ for that of the PTR/CAL tables, B3 places _H_ at tier 4 (43.7 ns) against tier 7 (55.1 ns) untilered ( 2).

## 4.4 Compilation Cost and Programmability

Figure 5(a) reports compile time normalized to end-to-end runtime,  3 the input the programmer writes. Compilation is a ∼10<sup>-6</sup> fraction of runtime for every workload, orders of magnitude below the synthesis cycle an HLS flow like DP-HLS \[5\] needs, since the compiler runs once and amortizes over the whole execution. Figure 5(b) attributes it: the back-end is ∼88%, but this is command-stream _emission_, not lowering effort. The compiler serializes a separate command program per PU, so the stage is bounded by writing the 32 per-PU streams out; the front-end and mid-end passes work in memory on compact IR and are cheap.

On programmability, blocked APSP is 4 lines of GenDSL and alignment 9, against an estimated ∼300 and ∼500 lines for the equivalent hand-written device-level mapping, nearly two orders of magnitude. That saving comes from the abstraction, not the engineering: adding a new semi-ring (widest-path,  1) took 5 lines and no new passes, since tiling, placement, PU assignment, and communication are all independent of the operator pair. Only APSP and alignment are evaluated end-to-end because the GenDRAM hardware provides kernels for these two alone; the compiler handles all seven through the same passes with only the operator-pair change above, so the limit is the hardware’s coverage, not the compiler’s reach.

## 4.5 Discussion

The two workloads exercise GenDRAM oppositely, APSP as synchronized broadcast phases over a dense matrix and alignment as an asynchronous producer-consumer pipeline, yet both are the same dp.grid\_update lowered by the same passes, diverging only at mode selection. That is the claim the evaluation supports: the semi-ring abstraction is sufficient structure for a compiler to derive a tile size, memory layout, PU assignment, and communication<tbc>

\begin{tabular}{ccccc}
 & \multicolumn{2}{c}{**APSP (OSM)**} & \multicolumn{2}{c}{**Align (10 kbp)**} \\
**Metric** & B0 & B3 & B0 & B3 \\
Off-chip DRAM traffic (GB) & 3.15\(\times\)10<sup>6</sup> & 1.63\(\times\)10<sup>4</sup> & 0.92 & 0.50 \\
Traffic reduction & 1\(\times\) & 192\(\times\) & 1\(\times\) & 1.8\(\times\) \\
Resident in fastest tier T0 (%) & 25.0 & 100.0 & 0.0 & 0.0 \\
Avg. memory latency (ns) & 37.4 & 34.6 & 55.1 & 43.7 \\
\end{tabular}

\begin{tabular}{ccc}
**Metric** & **APSP** & **Alignment** \\
GenDSL source (LoC) & 4 & 9 \\
Hand-tuned mapping (LoC) & ∼300 & ∼500 \\
\end{tabular}

** 2: Memory statistics for the OSM APSP and 10 kbp PacBio workloads.**

** 3: Programmer effort.**

