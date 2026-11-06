memory usage to sublinear growth, and performing a fully parallel localized key update algorithm that minimizes data transfers, improves SIMD utilization, and ensures high bandwidth efficiency \[17\].

## III. SYSTEM ARCHITECTURE

The FractalSortCPU algorithm consists of key-based threads performing sequential updates to each layer of the histogram. The keys are grouped in batches and processed in parallel on CPU using SIMD vectorization via Numba JIT to maximize throughput as shown in Figure 1 \[45\].

### A. Local Thread Histogram Update

Each key is mapped to a thread which updates node counter variables along the path encoded by the key bit sequence. Collisions are mitigated using atomic operations supported by the Arithmetic Logic Unit (ALU) \[52\].

#### 1) High Precision Histogram Update:

In high-precision sorting where the histogram is too large to fit in the CPU last-level cache, with _n_ nodes and counter variables encoding _n_ keys, the update algorithm involves two steps \[53\]. In the first step, a local merge on CPU where node updates are computed from key bits, and the updates are aggregated in _O(log(n_)) into a single local compressed tree. In the second step, the on-chip tree is transferred to memory using a parallel _O(log(n_)) merge operation based on a depth-first traversal from the local parent node.

### B. Global CPU Histogram Update

The thread-based updates are merged into a single global histogram by threads co-resident on the CPU. The global<tbc>

<tbc>merge tree is stored both in main memory and in the CPU last-level cache (LLC) \[53\]. Multi-thread updates are coordinated using Atomic Read-Modify-Write (RMW) and the Fractal RMW \[52\].

#### 1) Fractal RMW:

For each key _k_ of _p_ bits, the histogram tree is updated by walking a root-to-leaf path determined by the key’s bit sequence. At each level \(l\in\{0,\dots,L-1\}\) where \(L=min(p,\lceil log_2(n)\rceil)\), the algorithm reads bit _l_ of the key to select the left (0) or right (1) child, and atomically increments the counter at the selected node. The full path update for one key touches exactly _L_ nodes, each requiring one Atomic RMW operation.

On x86 architecture, each atomic increment is executed in the integer ALU pipeline as a single transaction: read the counter from the cache line into a register, compute the new value, and write it back with a cache-line lock when necessary \[52\]. For histogram nodes in the CPU LLC, these operations are served from cache with no DRAM traffic.

Contention between threads drops exponentially with depth: at the root node all _n_ keys contend on a single counter, but at level _l_ the _n_ keys are distributed across 2_<sup>l</sup>_ nodes, giving an expected \(\frac{n}{2l}\) updates per node. At level \(l\ge\lceil log_2(n)\rceil\), the expected contention falls below one, making leaf-level updates effectively contention-free. This exponential decay is what enables the fully parallel update without locks or synchronization barriers beyond the atomic instruction itself.

### C. Batch Size Selection

The batch size parameter determines the balance between locality and parallelism, where large batch sizes reduce synchronization frequency and relatively lower the cost<tbc>

Layeri
Layeri+1
Layeri
Layeri+1
Layeri
Layeri+1
Key 0
Key 1
Key n
Countk
Countk
Countk
Countk+1
Countk+1
Countk+1
DRAM
Count1
DRAM
Count1
DRAM
Count1
Counto
Counto
Count2
Count2
Count2
Count2
Countk+2
Countk+2
Countk+2
Cache
Countk+3
Cache
Countk+3
Cache
Countk+3
Fractal RMW
ALU - Atomic RMW

Fig. 1. FractalSortCPU Logical Layout _p_=16

