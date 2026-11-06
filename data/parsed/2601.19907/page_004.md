**Algorithm 2** Recursive Partition APSP Pseudocode

1: **for** \(\ell=n\) down to 0 **do**

2: **parallel for** _C_ in levels\([\ell]\) **do** \(\triangleright\) Step 1

3: \(D_C\leftarrow\) FloydWarshall(_C_)

4: \(B_C\leftarrow\) find\_boundary(_C_)

5: **if** DB\_prev == \(\varnothing\): \(DB_C\leftarrow\) restrict(_D<sub>C</sub>,B<sub>C</sub>_)

6: **if** DB\_prev == \(\varnothing\): \(\triangleright\) Step 2

7: \(G_B\leftarrow\) build\_boundary\_graph({_DB<sub>C</sub>_ for all _C_})

8: DB\_prev \(\leftarrow\) FloydWarshall(_G<sub>B</sub>_)

9: **parallel for** _C_ in levels\([\ell]\) **do** \(\triangleright\) Step 3

10: \(D_C\leftarrow\) inject(_DB\_prev,B<sub>C</sub>_)

11: **parallel for** (_C_<sub>1</sub>_,C_<sub>2</sub>) in levels\([\ell]\) **do** \(\triangleright\) Step 4

12: **for** _m_ in _B_<sub>_C_<sub>1</sub></sub>_,n_ in _B_<sub>_C_<sub>2</sub></sub> **do**

13: \(D_{C_1}[m,n]\leftarrow min_{i\in B_{C_1}}\left(D_{C_1}[m,i]+\text{DB\_prev}[i,j]+D_{C_2}[j,n]\right)\)

14: DB\_prev \(\leftarrow\) merge({restricted(_D<sub>C</sub>,B<sub>C</sub>_}})

15: **return** DB\_prev

scratchpad buffering, and a 16TB FeNAND \[29\] array offers dense persistent storage for boundary data and final results in compressed CSR format.

This purpose-built hardware enables a multi-stage dataflow, orchestrated by the logic die to execute the recursive APSP algorithm across the memory hierarchy. Fig. 4(a) summarizes the recursive APSP dataflow across the memory hierarchy:

1 CSR-partitioned components are streamed from the cold- storage region of the PCM-FW die into its compute region and expanded into dense matrices. 2 The PCM-FW die performs local FW updates, and results are streamed back to HBM3 in row-wise segments. 3 HBM3 (i) extracts boundary nodes and edges to construct a boundary graph for the next FW iteration, and (ii) prefetches next intra-component FW blocks for pipelined execution. 4 The PCM-MP die fetches submatrices from HBM3 to perform cross-partition MP merges. 5 HBM3 synchronizes boundary data across partitions to prepare for the next boundary-aware FW round. 6 (i) Updated boundary matrices are stored in dense format in FeNAND, whereas final cross-partition APSP results from PCM-MP and (ii) intra-component APSP from PCM-FW are compressed to CSR format before writing to FeNAND. 7 The PCM-MP die fetches interleaved boundary matrices from FeNAND to complete final cross-partition merges.

## C. Hardware Design and Implementation

Both PCM-FW and PCM-MP dies use the same 1T1R SLC PCM cell technology \[23\], organized into \(1024\times 1024\) units. The parameters for the SLC cells are listed in  II. Each unit, together with its peripheral circuits, forms a macro, as shown in Fig.5(a). Each tile contains 130 parallel units connected via an H-tree interconnect \[30\] for efficient data exchange (Fig. 5(b)). The design ensures full crossbar activity<tbc>

<tbc>without idle cycles. Same-colored arrows represent concurrent unit-to-unit transfers. Tiles operate concurrently, each with a local controller linked to a global main controller for coordinated execution (Fig. 5(c)). In-memory operations are triggered by row-segment broadcasts, with each tile controller managing parallel processing across its units. In addition to shared peripheral logic, each PCM die integrates specialized circuits for its role. The PCM-FW tile includes a permutation unit for rearranging data blocks, while the PCM-MP tile integrates a 32-bit 6-level min-comparator tree for efficient MP reductions.

**PCM-FW Permutation Unit.** The PCM-FW die includes a dedicated permutation macro that locally rearranges data blocks, avoiding off-die data movement. As shown in Fig. 5(d), the permutation macro comprises:

1) a 32-row burst row-buffer controller,<tbc>

2) a reorder buffer for panel masking and block pruning,<tbc>

3) a lightweight on-tile DMA engine (1-cycle read, 10-cycle write) with address remapper, and<tbc>

4) a four-stage FSM pipeline (Prefetch\(\rightarrow\) Permute \(\rightarrow\) Compute \(\rightarrow\) Write-back),

so that data movement overlaps computation. The permutation unit packs `Panel\_Row` and mirrored `Panel\_Col` into 32- row windows for coalesced bursts without H-tree stalls, while a `prefetch` buffer hides DMA latency and skip futile writes, sustaining near-peak occupancy and reducing wear.

**PCM-MP Min-Compare & Update.** Each unit integrates a pipelined comparator tree (Fig. 5(e)) that reduces 1024 32-bit inputs to one 32-bit minimum in following periods: A 1024 \(\times\) 32-bit row is streamed into the buffer in 1 cycle. Thirty- two parallel five-level carry look-ahead (CLA) trees extract sign bits and 5-bit indices for block minima in 6 cycles. A second five-level tree reduces these to a global minimum in another 6 cycles, totaling 13 cycles per row. The final sign- bit mask gates PCM writes, updating only entries with smaller values. Two staging buffers hold operands across adds while _DB_\[_i,j_\] streams, enabling one 1024-wide vector per cycle. The reduction tree outputs an update mask that enables compare<tbc>

\begin{tabular}{cc}
**Parameter** & **Value** \\
Reset pulse & \(40\mu\)A @ 0.70V \\
Programming energy & ≈0.56pI \\
Resistance (LRS) & ≈30k\(\Omega\), \(150\times\) on/off ratio \\
Set/reset time & 20ns / 20ns \\
Clock cycle & 2ns (500MHz) \\
\end{tabular}

