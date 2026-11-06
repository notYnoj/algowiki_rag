and-swap selective writes, avoiding read–modify–write and lowering energy and wear.

### D. Mapping and Scheduling Schemes

To execute FW and MP efficiently in PCM tiles, we co- optimize software layout and hardware design through tailored intra-tile mapping and scheduling. Fig. 6(a) illustrates the FW DP update flow. Since diagonal pivot elements _p<sub>k</sub>_ always have zero distance, their propagation along pivot row (_r_<sub>1</sub>_...r<sub>n</sub>_) and column (_c_<sub>1</sub>_...c<sub>n</sub>_) is omitted. Instead, row and column elements propagate into the main block to perform add and min operations, updating main block values with MP products. Each pivot element triggers one such update; the process repeats until all diagonal pivots _p<sub>k</sub>_ (_k_=1,...,n) are processed. Fig. 6(b) shows our remapping strategy that maximizes array parallelism. We extract the pivot row, copy its column beneath it, and form an \((n-1)\times(n-1)\) block; this lets all updates finish with one add and one min. The next pivot element is then permuted, and the process repeats.

Fig. 6(c) shows the PCM-FW tile architecture, comprising 130 units. The pivot column elements are streamed into `Panel\_Col`\[1:_n_-1\], the pivot row into `Panel\_Row`, and all other entries into `Main\_Block`. Additions are implemented by FELIX \[26\]-style bit-serial units using `Temp\_Add` and `Temp\_Carry`. A FELIX \[26\] bit-serial subtraction compares the intermediate results in `Temp\_Main\_Block` against `Main\_Block`; the resulting sign bit gates selective writes back to `Main\_Block`, completing one full main-block update. A dedicated permutation unit then reorders `Panel\_Row`, `Panel\_Col` and `Main\_Block` for the next pivot iteration,<tbc>

<tbc>as detailed in Section III-C. Fig. 6(d) shows the PCM-MP tile architecture, comprising 130 units that execute a two-stage MP merge. In the first stage, a logical row \((1\times 1024)\) from _C_<sub>1</sub> is loaded into _D_<sub>_C_<sub>1</sub></sub>\[_m,i_\], while _DB_\[_i,j_\] and the corresponding row _D_<sub>_C_<sub>2</sub></sub>\[_j,n_\], representing paths from boundary _j_ to internal node _n_ in _C_<sub>2</sub>, are presented in parallel. The merge proceeds via two successive MP operations: _D_<sub>_C_<sub>1</sub></sub>\[_m,i_\] + _DB_\[_i,j_\] followed by \((\cdot)+D_{C_2}[j,n]\), each performing a 1024-way Min reduction. Computation is performed using FELIX-style bit-serial adders (`Temp\_Add1`, `Temp\_Carry`, `Temp\_Add2`), and a pipelined comparator tree reduces all candidates to a single minimum.

## IV. EXPERIMENTAL RESULTS AND ANALYSIS

### A. Experimental Setup

We benchmark RAPID-Graph on the real-world OGBN- products graph \[31\] for fair SOTA comparison, and on synthetic Newman–Watts–Strogatz (NWS) \[32\] and Erdős–Rényi (ER) \[33\] graphs generated via NiemaGraphGen \[34\] for controlled scalability and topology analysis. NWS preserves dense intra-community but sparse inter-community links, while ER has uniformly random edges. These datasets reveal how graph topology impacts RAPID-Graph’s scalability.

We compare against CPU, GPU, SOTA PIM method Temporal PIM SSSP \[16\], and SOTA GPU distributed methods including Partitioned APSP \[10\] and Co-Parallel APSP \[11\]. Since no SOTA PIM methods directly implement APSP, we estimate the performance of the Temporal PIM SSSP \[16\] to establish a comparable APSP PIM baseline, hereafter referred as PIM-APSP. Graph partitioning is performed using METIS 5.1.0 \[24\]. Consistent with prior work \[10\], \[11\], the METIS partitioning overhead is not included in our results as it is a preprocessing step. The baseline configurations are:

1) **CPU**: Intel i7-11700K (64 GB)<tbc>

2) **GPU A100**: NVIDIA A100-SXM4 (80 GB)<tbc>

3) **Estimated GPU H100 \[35\]**: NVIDIA H100 (80 GB)

We develop an in-house cycle-accurate simulator to model RAPID-Graph’s functionality. PCM arrays and peripheral circuits are modeled with NeuroSim \[36\] for device-level accuracy. We synthesized the RTL in System Verilog using Synopsys Design Compiler with a 40nm CMOS PDK at 500MHz, including custom permutation unit, min-comparator tree, and controller; all results are scaled to 14 nm using models \[37\].

### B. Hardware Configurations

Each PCM-FW tile integrates a permutation unit for FW, while each PCM-MP tile includes a min-comparator tree for MP. As shown in  III, 82% of unit area stems from peripheral circuits (sense amplifiers, 1-bit comparators, WL/SL drivers, decoders, D latch buffers), while compute units contribute negligible overhead, supporting dense integration and efficient APSP execution. PIM logic integration lowers PCM density but removes costly data movement, delivering higher performance and efficiency.

System-level supporting components contribute moderate power and area: HBM3 (16 GB) adds 8.6 W and 121_mm_<sup>2</sup> \[38\]; FeNAND (16 TB) adds 6.4 W across 3000_mm_<sup>2</sup>; the SM2508<tbc>

(a)
(c) PCM FW Tile (130 units)
(d) PCM MP Tile (130 units)
k = 0,1,...n
D_C1[m,]
Panel_Col_1
Pk
DB[i,]
Col_n-1
Permutation Unit
Pivot element (dist=0)
Panel Row
Panel row (r1,...rn)
Panel column (C,...Cn)
Main block
Temp_Add
(b)
r1
r2
r3
C1
C2
C3
Temp_Carry
C2
C3
C1
Temp_Carry
C3
C1
C2
Temp_Add2
Min Comp
Temp_Main Block
Min & Update
Update
Temp_Min1
Permutate
Main Block
D_C2[j,N]
Sign Bit
Cont.
Temp_Min 2

Fig. 6. SW/HW mapping for recursive partitioned APSP (a) FW illustration (b) FW remapping, every step includes add, min update and permutation (c) PCM-FW tile performing FW (d) PCM-MP tile performing two-stage MP

