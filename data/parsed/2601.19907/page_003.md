### C. Phase Change Memory

PCM \[25\] encodes data by switching a chalcogenide cell between high-resistance amorphous state (reset, 0) and low- resistance crystalline state (set, 1) via Joule heating. Cells form 1T1R cross-point arrays whose wordlines and bitlines are managed by selection transistors. PCM offers fast random reads, low leakage, and non-volatility, making it ideal for in- place parallel updates and persistent storage in our PIM system.

Our PCM array supports bit-serial logic primitives inspired by FELIX \[26\]. Single-cycle NOR, NOT, NAND, minority, OR and 2-cycle XOR operations execute natively in crossbar memory via voltage-controlled switching. These primitives enable efficient composition of more complex functions: 1-bit addition and min-comparison are implemented via FELIX \[26\] primitives. Addition computes the sum bit \(S=A\oplus B\oplus C_{in}\), and the carry-out _C<sub>out</sub>=Maj(A,B,C<sub>in</sub>_). Min-comparison uses bit-serial subtraction \(S=A\oplus(\neg B)\oplus 1\), where most significant bit of _S_ is the sign bit gating selective updates.

## III. RAPID-GRAPH SOFTWARE-HARDWARE CO-DESIGN

### A. Recursive Partitioned APSP

To efficiently scale APSP computation on large graphs, we design a recursive partitioning strategy that enables fully independent subgraphs sized to fit within PIM tile limits. Accordingly, we partition each component at \(|V|\le 1024\), matching practical array dimensions per PCM tile and the maximum parallelism achievable with dense, high-yield fabrication. The input graph _G_=(_V,E,w_), with vertex set _V_ , edge set _E_, and non-negative weights _w_, is first partitioned by METIS \[24\] into base-level components \(C_1^{(0)},\dots,C_k^{(0)}\). Each component \(C_i^{(0)}\) contains internal vertices and boundary vertices, where boundary vertices connect to other components. We extract boundary vertices from \(C_i^{(0)}\) to construct the level-0 boundary graph \(G_B^{(0)}\). If boundary graph \(G_B^{(\ell)}\) at level \(\ell\) exceeds the 1024- vertex tile limit, we recursively partition it, creating a coarser graph \(G_B^{(\ell+1)}\). This continues until \(|V(G_B^{(n)})|\le 1024\), ensuring all graphs fit entirely within tiles.  I summarizes key variables. At each recursion level, APSP is computed locally within components and boundary graphs, propagating distances back into components and performing cross-component updates via MP products. Fig. 3 illustrates this process. After recursive partitioning each memory array holds one dense distance block with \(N\le 1024\) vertices. To maximize parallelism during the FW updates, we adopt a specialized data remapping strategy. This strategy logically separates the current pivot row and column (the `Panel\_Row` and `Panel\_Col`) from the rest of the distance matrix (the `Main\_Block`). This layout allows the FW die to perform massively parallel updates on the `Main\_Block`. The detailed mapping and scheduling schemes for this process are described in Section III-D.

Algorithm 2 summarizes the recursive APSP procedure across hierarchy levels. It follows the same four steps as Algorithm 1, but operates bottom-up: starting from base-level partitions, each level computes local APSP and propagates boundary summaries upward. This structure maximizes tile<tbc>

<tbc>level parallelism and fits within constrained PIM resources without requiring global synchronization.

### B. Heterogeneous Architecture Overview

To scale APSP, we build a heterogeneous multi-die architecture that integrates high-bandwidth in-memory compute with large nonvolatile storage, as shown in Fig.4(a). We co- package the PCM-FW die, PCM-MP die, logic base die, and HBM3 using a 2.5D silicon interposer with a UCIe v1.0 raw interface \[27\], delivering 64 full-duplex lanes at 32 Gb/s each, as illustrated in Fig. 4(b). Off-package FeNAND is an external storage array mounted on the PCB and connected via ONFI 5.1 ×16 channels. It delivers several key advantages over conventional charge-trap NAND, including higher capacity, lower program voltage, faster access, and a shorter string length \[28\]. This multi-die design maps the recursive APSP algorithm’s FW and MP kernels onto dedicated PIM compute dies. Fine- grained partitioning, coupled through the high-bandwidth UCIe link, creates a tailored dataflow that eases the memory and communication bottlenecks of large-scale APSP.

Inside the package, the system components are organized by function. The logic base die serves as the central controller, managing system-wide dataflow and leveraging its dual stream engines for high-throughput CSR-to-dense format conversion. In-memory computation is executed on two specialized 2GB PCM compute dies: the FW die is tailored for intra-component updates, while the MP die accelerates cross-partition merges. This processing core is supported by a tiered memory hierarchy, where a 16GB HBM3 stack provides high-bandwidth<tbc>

\begin{tabular}{cc}
**Variable** & **Description** \\
_G_=(_V,E,w_) & Graph with vertices _V_ , edges _E_, edge weights _w_ \\
\(C_i^{(\ell)}\) & Component at level \(\ell\) (\(\ell\)=1,...,n and i=1,...,k) \\
\(B_i^{(\ell)}\) & Boundary vertex set of component \(C_i^{(\ell)}\) \\
\(G_B^{(\ell)}\) & Level-\(\ell\) boundary graphs \\
\(DB^{(\ell)}\) & Boundary-to-boundary distance matrix at level \(\ell\) \\
_D<sub>C</sub>_ & Intra-component APSP distance of component _C_ \\
_D_<sub>_C_1</sub>\[_m,n_\] & Cross-component distance from \(m\in C_1\) to \(n\in C_2\) \\
\end{tabular}

Ln
V
Memory size
Base case
Ln-1
Ln-2
Cn-2
B
B
-
-
-
Pass down result
Lo
Step 1
Step 2
Step 3
Step 4

Fig. 3. Illustration of recursive partitioned APSP

TABLE I

KEY VARIABLES IN RECURSIVE PARTITIONED APSP

