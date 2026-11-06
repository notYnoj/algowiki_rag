## III. METHODOLOGY AND DESIGN

Approximate computing improves hardware efficiency across multiple domains. Approximate multipliers \[17\] target MAC operations, trading computational accuracy for power reduction, while coarse bucket approximation \[18\] targets sorting operations, trading perfect ordering for improved efficiency. The latter approach motivates our application of approximation.

The research goal is to reduce power by minimizing BTs on interconnect links while maintaining a low hardware implementation cost in terms of area overhead.

### A. Baseline comparison-free popcount-sorting unit

The baseline for our work is an Accurate Popcount-Sorting Unit (ACC-PSU) with comparison-free design, adapted from Yang _et al._ \[19\]. This architecture comprises a popcount unit and a sorting unit, organized into 3 stages: the popcount stage, the prefix sum stage, and the index mapping stage, as illustrated in Fig. 1. The popcount unit computes the Hamming Weight using 4-bit lookup tables (LUTs) whose outputs are aggregated by adders to produce the ’1’-bit count for each input element. The sorting unit encodes ’1’-bit count into one-hot representation, generates a frequency histogram, computes starting addresses for each specific ’1’-bit count value via prefix sum, and scatters indices into the sorted output. Transmitting units then rearrange input data according to sorted indices and forward data through links.

### B. Approximate computing inside popcount-sorting unit

To reduce hardware overhead, we propose an Approximate Popcount-Sorting Unit (APP-PSU). This design integrates approximate techniques into the population count module. The key innovation lies in grouping exact population counts into coarse-grained buckets, thereby reducing datapath width.

#### 1) Effectiveness of approximate sorting:

Order-insensitive nature of convolution accumulation enables approximate sorting to preserve most benefits of accurate sorting by preventing large transitions, yielding nearly identical BT reduction. Python simulations in Section IV validate this statement.

#### 2) Approximation Design:

The approximation strategy groups exact ’1’-bit counts into _k_ coarse-grained buckets through a deterministic mapping. For _W_-bit inputs, each exact ’1’-bit count value \(P_{exact}\in[0,W]\) is assigned to one of<tbc>

<tbc>_k_<tbc>

<tbc> buckets, producing a compact bucket index requiring only _log_<sub>2</sub>(_k_) bits (e.g., a 2-bit index for _k_=4 buckets). Rather than preserving the full ’1’-bit count range, only these bucket indices are forwarded to the sorting stage, compressing the value space from _W_+1 possible ’1’-bit counts to _k_ buckets.

For example, for _W_=8-bit inputs and _k_=4 buckets, the mapping assigns \(\{0,1,2\}\rightarrow Bucket0\), \(\{3,4\}\rightarrow Bucket1\), \(\{5,6\}\rightarrow Bucket2\), and \(\{7,8\}\rightarrow Bucket3\). An input sequence with exact ’1’-bit counts {4,1,7,5,3,5} would thus map to bucket indices {1,0,3,2,1,2}.

#### 3) Hardware Implementation and Architecture:

The APP- SU architecture, as in Fig.1, retains the same dataflow as ACC- PSU while introducing a mapping LUT in popcount bucket encoder for approximation. During synthesis, the compiler eliminates logic paths that do not affect the final bucket index, so the synthesized netlist is a simplified approximate ’1’-bit count circuit that directly produces bucket indices.

The primary area reduction comes from reducing the number of buckets, which determines the datapath width throughout the sorting unit - all sorting logic scales proportionally with the bucket count rather than the full ’1’-bit count range. For _W_=8-bit data, ACC-PSU requires _W_+1=9 buckets to cover every possible ’1’-bit count value, whereas APP-PSU aggregates adjacent ’1’-bit count values into _k_=4 buckets.

## IV. EXPERIMENT

We evaluate four configurations: a non-optimized baseline, column-major ordering, ACC ordering, and APP ordering with _k_=4 buckets. All experiments use 8-bit fixed-point representation. We also compare our PSUs with other sorting implementations. For the hardware evaluation, ACC-PSU and APP-PSU are implemented on our platform, whereas the baseline is implemented as a bypass path.

### A. Results of Software Simulation Experiment

We simulate packet transfers over a 128-bit link using Python. A total of 100000 packets are sent, each consisting of 4 flits with random inputs and weights. As shown<tbc>

\begin{tabular}{ccccc}
**Order** & \multicolumn{4}{c}{**Bit Transitions per 128-bit flit**} \\
**strategy** & **_Input_** & **_Weight_** & **_Overall_** & **_Reduction_** \\
Non-optimized & 31.035 & 32.036 & 63.072 & - \\
Column-major & 26.004 & 28.007 & 54.011 & 14.366% \\
ACC Ordering & 22.333 & 28.013 & 50.346 & 20.177% \\
**APP Ordering** & 22.887 & 28.009 & 50.896 & **19.305%** \\
\end{tabular}

