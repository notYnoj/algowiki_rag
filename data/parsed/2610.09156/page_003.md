<tbc>change costs a full synthesis cycle. GenMLIR instead targets fixed, programmable PIM hardware.

**Mapping onto programmable accelerators.** GenDP couples a generic DP accelerator with DPMap, which lowers data-flow graphs to control instructions [10]; GMX adds DP-oriented ISA extensions to RISC-V [9]; Darwin-WGA exposes a co-processor through OpenCL [8, 23]; GenASM accelerates approximate string matching [4]. All assume a flat, uniform-latency memory. None must decide which of eight tiers a table belongs in, or how to split a kernel across two PU classes, the two decisions that dominate performance on M3D PIM, and the reason a new pass design is needed rather than a port. Likewise, HPVM-HDC compiles across CPUs, GPUs and accelerators from a heterogeneous IR [2]; we adopt its philosophy, but to our knowledge no existing MLIR pipeline models non-uniform DRAM tier latency or heterogeneous near- bank PU classes as first-class IR concepts.

## 3 The GenMLIR Compiler

GenMLIR lowers a DP specification to a GenDRAM command stream in three phases: a front-end that captures algorithm, data, and configuration; a mid-end of four GenDRAM-aware pass groups; and a back-end that emits device API calls and command streams. Fig. 2 shows the full pipeline.

### 3.1 What Is New, and What Is Reused

Because a compiler is assembled largely from known transformations, we state the boundary explicitly rather than leave it to inference; it is also drawn in Fig. 2.

_General-purpose MLIR passes:_ loop canonicalization, blocked tiling of an affine nest, bufferization and memory-space assignment, SIMD lowering onto PE lanes, and instruction selection. These form the lowering backbone that the passes below extend with DP and tier-specific reasoning.

_New to this work:_ (1) _DP pattern extraction_, which recovers a semi-ring dp.grid\_update from a scalar add/compare/select nest, so that downstream passes reason about an algebraic operator rather than a fixed opcode sequence; (2) _dependence materialization_, which synthesizes either the three-phase blocked Floyd-Warshall dependence structure or a diagonal wavefront order from the same dp.grid\_update, selected by operator signature; (3) _tier-aware placement_, which ranks memory objects by latency sensitivity and assigns them to physical tiers under a capacity constraint (§3.3); (4) _mode selection_, which commits the module to broadcast or producer- consumer lowering; and (5) _communication synthesis_, which turns ownership plus dependence edges into ring broadcasts, barriers, or queue send/recv pairs. Items (1)-(2) are what make the semi-ring abstraction operational; (3)-(5) are what make it _tier-aware_, and have no analogue in flat-memory accelerator compilers.

### 3.2 Front-End: GenDSL

GenDSL is a small declarative language with three sections. _Algorithm_ names the semi-ring (\(\oplus,\otimes\)) and the recurrence’s index pattern. _Data_ declares the matrices, the PTR/CAL lookup tables, and the producer-consumer streams between seeding and alignment. _Configuration_ exposes the knobs a user may wish to override: tile size _B_, execution mode, the Search/Compute PU split,<tbc>

<tbc>tier hints, and datapath precision. These all default to compiler- derived values, so a correct program need not mention them. GenDSL lowers to two dialects: a _DP dialect_ that makes the recurrence and the intended traversal explicit, and a _GenDRAM dialect_ whose types carry a tier, a channel, and a bank-group, and whose operations include gendram.broadcast, gendram.barrier, and gendram.send/recv.

### 3.3 Mid-End: Four Pass Groups

**G1: DP recognition and normalization.** Pattern extraction replaces the scalar update nest with a single dp.grid\_update annotated with its semi-ring; canonicalization then normalizes loop bounds, index expressions, and boundary handling. The point of G1 is stability: tiling and dependence construction must not depend on incidental syntax in the input program.

**G2: Tiling and dependence formation.** Rather than taking _B_ as a tuning parameter, we derive it. A blocked update \(A_{ij}\oplus=A_{ik}\otimes A_{kj}\) has a working set of three \(B\times B\) tiles. At _w_ bytes per element these must fit in the PU’s on-chip SRAM, of capacity _S_ (on GenDRAM, a 256 KB shared scratchpad plus \(16\times 32\) KB of PE-local memory, so _S=_768 KB):

\(3wB^2\le S\Longrightarrow B^\star=\left|\sqrt{S/3w}\right|.\) (3)

For _w=_4 (the 32-bit APSP datapath), _B<sup>⋆</sup>=_256. The pass then materializes the three blocked Floyd-Warshall phases-pivot _A<sub>kk</sub>_, row/column, internal-- as separate IR regions with explicit dependence edges between them, or, for alignment, splits the program into seeding and alignment kernels and constructs a legal diagonal wavefront order over the banded DP.

**G3: Mapping and tier-aware placement.** Mode selection records broadcast or pipeline style as a module attribute. Tile-to-PU assignment applies Eq. (2), annotating each tile with owner\_pu. Placement then ranks each memory object _o_ by a latency sensitivity \(\sigma(o)=a(o)/\beta(o)\), the ratio of dependent (pointer-chasing) accesses to streamed bytes, and greedily assigns objects in decreasing \(\sigma\) to the lowest free tier subject to that tier’s capacity. Seeding’s PTR/CAL tables have \(\sigma\gg 1\) and occupy the fast tiers; distance matrices and read buffers have \(\sigma\approx 0\) and are instead channel- interleaved across the upper tiers to maximize bank parallelism. This reproduces GenDRAM’s hand-chosen placement as the output of a policy rather than as a constant, which is what allows the same pass to place a workload GenDRAM’s authors never considered.

**G4: Communication and synchronization synthesis.** Ownership plus dependence edges determine communication. For APSP the compiler emits a broadcast of each updated pivot tile and barriers that separate the three phases. For alignment it emits queue-based send/recv between Search and Compute PUs, and chooses queue depth from the modeled seeding/alignment throughput ratio, exposing it as a runtime parameter when the estimate is uncertain.

### 3.4 Back-End

The back-end lowers the placed, scheduled IR onto GenDRAM’s datapath in three general-purpose steps. Bufferization turns each tile into a buffer in the memory space G3 assigned, so tier decisions<tbc>

