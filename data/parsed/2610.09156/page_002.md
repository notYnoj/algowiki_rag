\(D[i,j]\leftarrow D[i,j]\oplus\big(D[i,k]\otimes D[k,j]\big),\) (1)

instantiating \((\oplus,\otimes)\) per domain. Floyd-Warshall APSP relaxes edges over the (min,+) semi-ring; Smith-Waterman alignment maximizes a score over (max,+). The two are structurally identical and differ only in the operator pair and in how the resulting dependence graph is traversed--globally, in pivot-broadcast super- steps, versus locally, along a diagonal wavefront. This algebraic unification is long-established in the graph-analytics literature [11] and was applied to 3D PIM hardware design by GenDRAM [15]; Eq. (1) is reproduced from the latter. Our contribution is not the abstraction but its use as a compiler IR, together with a precise statement of its limits (§3.5).

## 2.2 Target Architecture: GenDRAM

**Relationship to prior work.** GenMLIR targets GenDRAM [15], a recently proposed M3D DRAM PIM accelerator. GenDRAM contributes _all_ of the hardware in this subsection: the tiered stack, the heterogeneous PU organization, the modulo tile-to-PU mapping rule of Eq. (2), the decision to pin the PTR/CAL tables to Tier 0, the two execution modes, and the cycle-accurate simulator used in §4. Fig. 1 is redrawn after Fig. 8 of [15]. What GenDRAM does _not_ provide, and what this paper supplies, is a way to reach any of it from a program rather than from a hand-written mapping.

**Structure.** The logic die carries 32 PUs in a 1:1 coupling with the DRAM bank-groups, so an ACTIVATE delivers a full row into the owning PU’s scratchpad over the hybrid-bond interface. Eight PUs are _Search PUs_, built for the irregular, latency-critical PTR\(\rightarrow\)CAL lookups of genomic seeding; the remaining 24 are _Compute PUs_, each a 16-PE cluster whose reconfigurable adder/comparator implements (min,+) or (max,+) directly. Three properties drive every compiler decision that follows:

_(i) Tiered latency._ The staircase wordline routing of a 1024-layer stack makes _t_<sub>RCD</sub> rise ∼10\(\times\) (2.29 to 22.88ns), widening full row- access time _t_<sub>RC</sub> by 1.6\(\times\) (35 to 55ns). Placement is therefore not latency-neutral.

_(ii) Bank-group geometry._ A tile’s owner PU is fixed by

\(\mathrm{PU}(i,j)=(i\times M+j)\mathrm{mod}(C\times G),\) (2)

with _M_ tiles per row, _C_ channels and _G_ bank-groups per channel, so logically adjacent tiles land on distinct PUs and wavefront neighbors do not contend.

_(iii) Two execution modes._ APSP runs homogeneously: a pivot PU updates _A<sub>kk</sub>_, broadcasts it over the ring, and all PUs then update row/column and internal tiles in lockstep. Genomics runs as a heterogeneous pipeline: Search PUs stream candidate locations into queues consumed by Compute PUs.

## 2.3 MLIR

MLIR [12] supports coexisting abstraction levels in one pipeline via user-defined dialects that interoperate with existing passes. Halide [21] and TVM [6] showed the value of separating algorithm from schedule; MLIR makes that separation extensible. It fits here because the object being lowered, a grid update, must successively acquire a tile structure, an owner PU, a memory tier, and a communication schedule, each naturally a distinct IR level rather than a compiler-internal side table.

## 2.4 Related Work

**Synthesis of DP hardware.** ROCC generates systolic arrays for wavefront algorithms from C [3]; DWARV derives pipelined DP datapaths by recursive variable expansion [18]; Cinnabar synthesizes DP energy controllers [22]; and DP-HLS supplies a C++ template library over Vitis HLS for bioinformatics kernels [5]. All emit a frozen hardware instance per recurrence, so any algorithmic<tbc>

Monolithic 3D DRAM stack + logic die
Processing Unit and its DRAM bank-group
BK0
BK1
BK2
BK3
BK4
BK15
Tier 7
tRCD 22.88 ns
Tier 6
1024-bit hybrid-bond I/O Channel x 16
Tier 5
PU (near-bank PE cluster)
wordline RC delay
Tier 4
PE0
PE1
PE2
PE3
PE4
PE15
Tier 3
Tier 2
Tier 1
Shared Memory 256 KB SRAM
Combiner
Tier 0
tRCD 2.29 ns
Cu-Cu hybrid bonding ( - 1 μm pitch)
Max/Min Engine
Seq-additional Unit
A+B
min max
Logic die
APSP-Subtract Unit
Dold Dnew
Data Fusion Unit
Switch
Host CPU
32 PUs, one per bank-group
Inter-PU Interconnect (Ring Router, 128 GB/s)
8 Search PUs
24 Compute PUs

**Figure 1: The GenDRAM target. Left: an M3D DRAM stack of eight latency tiers (**_t_<sub>RCD</sub> **2.29-22.88 ns; wordline RC delay grows with distance from the logic die), bonded at** ∼1**\(\mu\)**m pitch to a logic die holding 32 PUs--one per bank-group, since 16 channels** \(\times\) **2 bank-groups per channel =** 32. **Right: a PU (dashed) is a near-bank PE cluster of 16 lightweight PEs, a 256 KB shared scratchpad and combiner, a multiplier-less Max/Min engine with its Seq-additional and APSP-subtract sub-units, and an interconnect interface (data fusion unit and switch). The DRAM banks, the bank/channel bus, and the inter-PU ring lie outside the PU. Redrawn after Fig. 8 of [15].**

