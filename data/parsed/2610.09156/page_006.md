<tbc>schedule for non-uniform-latency hardware. The generated code reaches the achievable bound on both workloads, compiles in a negligible fraction of runtime, and takes nearly two orders of magnitude less source than a hand mapping, a new recurrence costing only a change of operator pair. Two limits deserve emphasis. First, our hand-tuned comparison is an achievable bound (Figure 3), not measured expert code, so a cycle-level baseline remains future work. Second, the abstraction excludes data-dependent schedules (§3.5), where production aligners live. Neither is a property of the IR design.

## 5 Conclusion

We presented GenMLIR, an MLIR compiler that lowers semi-ring dynamic programming recurrences onto tier-aware 3D-DRAM PIM. By making the recurrence, tile size, memory tier, owner PU, and<tbc>

<tbc>communication schedule explicit in the IR, it derives the hand- written mapping from a short specification: recovering the capacity- optimal tile size analytically, deriving a tier placement that reaches near the performance ceiling, and beating a standard affine-tiling PIM pass by 1.2-1.4\(\times\), and up to 5.8\(\times\) (APSP) and 16.7\(\times\) (alignment) over a lowering without compiler support.

## Acknowledgments

This work was supported in part by PRISM and CoCoSys, centers in JUMP 2.0, an SRC program sponsored by DARPA (SRC grant number 2023-JU-3135). This work was also supported by NSF grants #2003279, #1911095, #2112167, #2052809, #2112665, #2120019, and #2211386.

## References

(a) APSP
(b) PacBio
(c) ONT 2D
8
12
20
18
9.9x
16.7x
10
16
6
5.8x
8.1x
13.6x
5.2x
5.2x
8
14
Speedup over BO
8
6.4x
12
10.4x
4
6
10
7.2x
4.6x
8
4
2.8x
6
4.1x
2
2
4
2
0
0
0
ca-GrQc N=5k
p2p-Gnutella08 N=6k
OSM N=65k
2
4
6
8
10
2
4
6
8
10
Read length (kbp)
Read length (kbp)
B0 (baseline)
B1 (generic affine)
B2 (achievable bound)
B3 (GenMLIR)

(a) APSP DRAM traffic (measured)
21
20
DRAM traffic (GB)
capacity wall B' = 256 (B> 256: 3-tile set > SRAM)
2-1
2-2
2-3
4N3/B model
2-4
measured (SRAM-cache sim)
23
24
25
26
27
28
Tile size B
(b) Tier placement (genomics)
4
3
Occupancy (GB)
2
1
0
35
36
38
41
44
47
51
55
0
1
2
3
4
5
6
7
DRAM tier (0 = fastest): bar labels = tRC (ns)
PTR/CAL (latency-critical)
reads / DP buffers (streaming)

(a) Compilation vs. runtime
end-to-end runtime (= 1)
APSP (OSM graph)
6e-6
Alignment (1.5M-read run)
1e-6
10-7
10-6
10-5
10-4
10-3
10-2
10-1
100
Fraction of end-to-end runtime
(b) Compile-time breakdown
APSP (OSM graph)
7%
88%
Alignment (1.5M-read run)
8%
87%
0.0
0.2
0.4
0.6
0.8
1.0
Share of compile time
Front-end + G1-G2
G3-G4 place & comm.
Back-end + emission

**Figure 3: Speedup over a lowering without compiler support (B0). B1: standard affine-tiling PIM pass; B2: _achievable bound_ (32-PU throughput for APSP, wavefront critical-path for alignment); B3: GenMLIR. (a) APSP over three graphs: B3 reaches 90% of the bound, meeting it at OSM. (b,c) Alignment vs. read length: B3 lies on the critical-path bound throughout, gains growing with length.**

**Figure 4: Memory analysis. (a) Measured blocked-APSP DRAM traffic (SRAM-sized LRU replay; dashed =** 4_N_<sup>3</sup>_/B_ **model): reuse holds it below the model, and the three-tile working set exceeds SRAM past** _B<sup>⋆</sup>_=256. **(b) G3 fills the fast tiers (T0–T4) with the** ∼17 **GB of latency-critical PTR/CAL tables, the slower tiers with streaming reads and DP buffers.**

**Figure 5: Compilation cost, normalized to end-to-end runtime. (a) Total compile time is a** ∼10<sup>-6</sup> **fraction of runtime, since the compiler runs once and amortizes over the full execution (OSM APSP; a 1.5 M-read genomics run). (b) Command- stream emission dominates the compile time (**∼88%**).

