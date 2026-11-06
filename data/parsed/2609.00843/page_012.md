In practice, this is supplemented by kernel-launch costs, global-memory merging proportional to the number of blocks, and atomic-operation costs at the different levels of the memory hierarchy.<sup>∗1</sup>

Excluding the input and output arrays, the primary global-memory workspaces are _H_[0_..R_-1], which stores local CDFs, and _O_[0_..m_-1], which stores tile offsets. The workspace is therefore _O(R+m_). Furthermore, with 32-bit integers, the histogram-construction and output-generation kernels use 4_T_ bytes of dynamic shared memory.

This analysis identifies the effective range of the implementation. When _R_ is small and _m_ is one or a small number, the number of input scans is low and handling local CDFs in shared memory provides a substantial advantage. As _R_ grows, _m_ increases and histogram construction scans the input array repeatedly. The _O(mn_) term then becomes dominant, reducing the advantage over radix sort and RefHP. Accordingly, RT-CDF is positioned as an improvement to counting-sort- and H-P-sort-based implementations for integer arrays with sufficiently small ranges.

## 3.3 GPU Implementation

We implemented RT-CDF in CUDA C++. The operations in Algorithm 4 are executed by four kernel types: histogram construction for range tiles, prefix sums for constructing local CDFs, range-tile offset construction, and output generation from local CDFs. We next describe the GPU implementation of each operation.

The histogram-construction kernel processes all range tiles in parallel in one kernel launch. We fix the block size at 512 threads. Given a dynamic shared-memory allocation of 4_T_ bytes, let _a_<sub>hist</sub> be the number of thread blocks that can reside concurrently on one SM, as determined from the kernel’s resource usage.<sup>∗2</sup> If the GPU has _S_ SMs, the number of thread blocks assigned to each range tile is

\(g_\mathrm{hist}=\mathrm{min}\left\{\mathrm{max}\left(1,\left\lfloor\frac{a_\mathrm{hist}\cdot S}{m}\right\rfloor\right),\left\lceil\frac{n}{512}\right\rceil\right\},\)

and the grid size of the entire kernel is

\(G_\mathrm{hist}=m\cdot g_\mathrm{hist}.\)

Here, \(a_\mathrm{hist}\cdot S\) is the number of thread blocks that can reside concurrently on the entire GPU after accounting for the kernel’s resource use; these blocks are divided evenly among the _m_ range tiles.

Each thread block derives its assigned range tile _t_ and its block number _q_ within that tile from the block index as

\(t=\mathtt{blockIdx.x}modm,q=\left\lfloor\frac{\mathtt{blockIdx.x}}{m}\right\rfloor.\)

A thread assigned to range tile _t_ starts at input position

\(i=512\cdot q+\mathtt{threadIdx.x}\)

<sup>∗1</sup> Each tile also merges block-local histograms into global memory. If _G_ thread blocks are assigned to one range tile, this entails bin-merging work equivalent to _O(mGT_). Both _T_ and _G_ are implementation parameters, and this cost is included in the measurements. <sup>∗2</sup> The implementation uses `cudaOccupancyMaxActiveBlocksPerMultiprocessor` from the CUDA Runtime API.

