<tbc>Each thread block loads the local CDF of its target range tile from global memory into dynamic shared memory. Each thread starts at within-tile output position

\(i=512\cdot\mathtt{blockIdx.x}+\mathtt{threadIdx.x}\)

and cooperatively handles the _N<sub>t</sub>_ output positions in the tile using a grid-stride loop that advances by \(512\cdot g_\mathrm{out}(t)\) positions per iteration. For each output position, the thread performs a binary search in the local CDF in shared memory and writes the corresponding value to the output array _B_. Output generation therefore does not reread the input array and distributes the output positions within a tile among the threads.

2 summarizes the launch configurations of these kernels.

The histogram-construction and output-generation kernels use 4_T_ bytes of dynamic shared memory to store tile-local arrays. If the dynamic shared-memory requirement for tile width _T_ exceeds the default shared-memory limit per thread block, the implementation uses CUDA’s opt-in configuration to increase the permitted dynamic shared-memory allocation up to the GPU’s supported limit.<sup>∗</sup><sup>3</sup> The tile widths used in the evaluation and their selection procedure are described in Section 4.1.

## 4 Experimental Evaluation

This section evaluates the RT-CDF implementation on an NVIDIA GeForce RTX 4090. Section 4.1 first examines the performance characteristics of the output-generation methods considered for RT-CDF and uses preliminary experiments to select the tile width for the main evaluation. Section 4.2 then describes the baselines and measurement conditions for the main evaluation. Section 4.3 compares RT- CDF with CUB, RefHP, and an implementation based on the algorithm of Kolonias et al., and Section 4.4 discusses the results.

### 4.1 Preliminary Evaluation of Implementation Choices

This subsection evaluates the performance characteristics of the output-generation method used by RT-CDF and selects the tile width used in the main evaluation. The preliminary experiments in this<tbc>

<sup>∗</sup><sup>3</sup> The implementation sets this option using `cudaFuncSetAttribute` from the CUDA Runtime API.

\begin{tabular}{ccc}
Operation & threads / block & blocks / grid \\
Histogram construction & 512 & \(m\cdot g_\mathrm{hist}\) \\
Local-CDF construction & 1024 & _m_ \\
Tile-offset construction & 1 & 1 \\
Output generation & 512 & _g_<sub>out</sub>(_t_) \\
\end{tabular}

2: Kernel launch configurations in RT-CDF

