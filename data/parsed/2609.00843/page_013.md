and cooperatively scans the input array using a grid-stride loop that advances by \(512\cdot g_\mathrm{hist}\) positions per iteration. Only when the loaded value belongs to the target range tile [_b<sub>t</sub>,b<sub>t</sub>+w<sub>t</sub>_) does the thread perform `atomicAdd` on the corresponding bin in dynamic shared memory. After scanning the input array, each thread block adds the partial histogram obtained in shared memory to _H[b<sub>t</sub>..b<sub>t</sub>+w<sub>t</sub>_-1] in global memory. Thus, rather than performing a global-memory atomic addition for every input element, each thread block adds its aggregate count for each bin to global memory once.

After histogram construction, the local-CDF construction kernel computes the prefix sums of each range-tile histogram and writes the result back to the same region of _H_. This kernel is launched once with _m_ thread blocks of 1024 threads each, with one block assigned to each range tile. The block assigned to tile _t_ partitions _H[b<sub>t</sub>..b<sub>t</sub>+w<sub>t</sub>_-1] among its threads. Each thread first computes partial sums over its contiguous subrange, then computes the sum of all preceding subranges by applying a block-level prefix sum to the per-thread totals, and adds that sum to every element of its own subrange. This constructs the local CDFs for all range tiles in parallel in one kernel launch.

The range-tile offset kernel is launched with one thread block containing one thread. It processes the range tiles in order and obtains the number of input elements in each tile from the final entry of its local CDF. It sequentially accumulates the number of elements appearing before each tile and stores the output starting position of tile _t_ in _O[t_]. Because the number of repeated input scans during histogram construction grows with the number of tiles _m_, the implementation is intended for ranges in which _m_ is relatively small. Consequently, the _O(m_) tile-offset construction has little effect on total execution time and is performed sequentially by one thread.

For output generation, range tiles are not processed concurrently; instead, a kernel is launched sequentially for each tile containing output elements. Let _N<sub>t</sub>_ be the number of input elements in range tile _t_. The value _N<sub>t</sub>_ is needed both to decide whether to launch the kernel and to determine the number of thread blocks in the launch.

When _m_=1, _N_<sub>0</sub>=_n_ and this value is used directly. When \(m\ge 2\), the range-tile offset array _O_ of size _m_ is copied once from the device to the host, and the host computes

\(N_t=\left\{\begin{array}{ c c }
O[t+1]-O[t] & (t<m-1), \\
n-O[t] & (t=m-1).
\end{array}\right.\)

No output-generation kernel is launched for a tile with _N<sub>t</sub>_=0.

The output-generation kernel uses a fixed block size of 512 threads. As for histogram construction, let _a_<sub>out</sub> be the number of blocks that can reside concurrently on one SM when the kernel uses 4_T_ bytes of dynamic shared memory. If the GPU has _S_ SMs, the number of thread blocks launched for a nonempty tile _t_ is

\(g_\mathrm{out}(t)=\mathrm{min}\left\{a_\mathrm{out}\cdot S,\left\lceil\frac{N_t}{512}\right\rceil\right\}.\)

Unlike histogram construction, one output-generation launch processes only one range tile, so the number of blocks that can reside concurrently on the entire GPU is not divided by _m_. This permits enough thread blocks to be assigned to the output of a tile even when input elements are concentrated in only a few tiles, reducing load imbalance caused by unequal tile populations.

