### Parallel implementation

If we think dividing the problem into _m-l_+1 subproblems then the number of subproblems will be embarrassingly greater for parallelization. So a fixed number of subproblems are assigned to each processor. Scheduler then spawns a separate worker thread to avoid use of a processor just for scheduling. The scheduler loops until all the subproblems are solved and after the completion of all threads the motifs are given to scheduler and it outputs the result.

## 3.3 Our Proposal qpMS-Sigma

In this section we propose an algorithm qpMS-Sigma with some techniques to optimize the space complexity as well as the runtime to solve the Quorum Planted Motif Search problem. Our work is mainly based on the Algorithm TraverStringRef.

### 3.3.1 String Compression

We can compress the input strings _s_<sub>1</sub>_,...s<sub>n</sub>_ as a part of preprocessing of the algorithm. For our work we have compressed all the _l_-mers of the input strings into some group of unsigned 32-bit integers. Thus we make the motif matrix using the compressed _l_-mers. To be specific for an alphabet set \(\Sigma\) we compressed a _l_-mer into \(\lceil log_2(|\Sigma|)\rceil\) groups. Each of this group contains \(\lceil l/32\rceil\) 32-integers.

For example, for a DNA string of 32 characters, we need \(\lceil log_2(|\Sigma|)\rceil=2\) groups of unsigned 32-bit integers, where each group contains \(\lceil n/32\rceil=1\) integers.

We can calculate the hamming distance between two compressed _l_-mers in two steps. First for each group of integers find out the bitwise XOR values of the integers of both the _l_-mers. After that calculate the bitwise OR values among the XOR-ed values of each group. The number of set bits in the last set of integers is the hamming distance between the two strings.

An example of comparing two compressed _l_-mers is given in fig. 3.3.

\begin{tabular}{cccccccc}
**String** & **After Ordering the Characters** & **Group 1** & **Group 0** & **XOR 1** & **XOR 0** & **OR** & **Number of Set Bits**\\
AGGCTA & 022130 & 011010 & 000110 & \multirow{2}{*}{110001} & \multirow{2}{*}{000011} & \multirow{2}{*}{110011} & \multirow{2}{*}{4}\\
GAGCAT & 202103 & 101011 & 000101 & & & & \\
\end{tabular}

Figure 3.3: _l_-mer Compression Example

