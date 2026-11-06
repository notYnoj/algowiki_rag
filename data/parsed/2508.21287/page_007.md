<tbc>efficiency for parallelism by allowing vertices to be processed earlier at the cost of potentially revisiting them. Similarly, our \(\Delta\)_-Motif_ exposes parallelism at multiple granularities: across multiple paths all within the same motif, across the entire _join_-and-_filter_ operations, and across the preparation of all the motif embeddings in pre-processing computation. These parallelization opportunities apply uniformly to both CPU and GPU backends; we quantify their performance impact in Sec. VI.

## V. EXPERIMENTAL SETUPS

### A. Software and Hardware Configurations

\(\Delta\)**-Motif Implementation:** Our CPU implementation leverages both `Pandas` 2.2.3 \[60\] and `NumPy` 2.0.0 \[61\], representing motif embeddings and candidate isomorphisms as DataFrames. On GPU, \(\Delta\)_-Motif_ uses `cuPy` \[19\] and `cuDF` 25.6.0 \[20\], which serve as drop-in replacements for `NumPy` and `Pandas`, respectively. Thanks to strong interoperability across the NVIDIA RAPIDS ecosystem and adherence to Apache Arrow standards, the algorithm transitions between CPU and GPU execution with only minimal changes to Python imports. Although subgraph isomorphism is a graph problem, our implementation relies not on `cuGraph` or `NetworkX` \[62\] but directly on tabular representations using `cuDF` and `cuPy`.

**VF2 and rustworkx:** We use the VF2 algorithm as our baseline, representing the broader class of tree-search- and-prune methods for subgraph isomorphism. We selected `rustworkx`, a high-performance Rust implementation that delivers up to 100\(\times\) speedup than python `NetworkX` and is used in production systems such as IBM’s Qiskit quantum computing framework \[63\]. This ensures that our comparisons reflect true algorithmic differences rather than implementation bottlenecks.

**GSI:** We also include GPU-friendly Subgraph Isomorphism (GSI) \[30\], \[64\] as a representative GPU-based baseline designed to improve parallel efficiency through GPU-centric execution strategies. We compare against GSI where the reference implementation is applicable; however, for most of our benchmark configurations involving larger pattern graphs, GSI did not complete within reasonable execution time or encountered out-of-memory errors.

**Hardware Configurations:** Our GPU-based experiments were conducted on the NVIDIA H200 GPU, part of the Hopper architecture family, equipped with 16,896 scalar processors and 144GB of HBM3e memory. For CPU-based benchmarking and the VF2 baseline, we used an AMD Ryzen Threadripper PRO 3995WX running at 4.3 GHz with 64 physical cores, 128 threads, and 1TB of DDR4-3200 system memory.

### B. Benchmark Metrics on Runtime

The execution time of the \(\Delta\)_-Motif_ algorithm comprises two phases: data preparation and computation. In the data preparation phase, the embeddings of required motif set, _Res(M_), are computed and stored as dataframes for reuse.<tbc>

<tbc>The computation phase then decomposes the pattern graph and executes dataframe _join_-and-_filter_ operations to produce the final matches.

In many scenarios, the same data graph is queried repeatedly with different pattern graphs, as in quantum circuit compilation \[5\] or streaming subgraph isomorphism \[65\] across social network analysis, chemistry, and biology. Here the data preparation phase can be performed once, cached, and reused, excluding its cost from subsequent queries and leaving only the pattern-searching phase, delivering significant runtime savings and further speedups. To highlight this potential, we also report results with data preparation time omitted, in Section VI marked as \(\Delta\)_-Motif_ GPU<sup>∗</sup>.

We observed minimal runtime variance across repeated runs using VF2 and \(\Delta\)_-Motif_; therefore, we report results from a single execution for each (_G<sub>d</sub>,G<sub>p</sub>_) configuration.

## VI. BENCHMARKS AND RESULTS

We evaluate our GPU-accelerated, motif-based subgraph isomorphism approach on graph workloads motivated by quantum circuit compilation, which feature structured data graphs and comparatively large pattern graphs.

### A. Subgraph Enumeration With Synthetic Subgraphs

In this section, we benchmark \(\Delta\)_-Motif_ on quantum device topologies relevant to layout selection in circuit compilation. We use the heavy-hex lattice and the 2D square grid topologies, shown in Fig. 1(a) and (b). For each topology, we consider two sizes that reflect the projected number of qubits for near-future quantum devices: 1990 and 4485 vertices for the heavy-hex topology and 1600 and 3600 vertices for the square grid topology. Thus, our data graphs represent real- world graphs. For \(\Delta\)_-Motif_, we select motif sets tailored to each topology: {_M_<sub>2</sub>, _M_<sub>4</sub>} for heavy-hex and {_M_<sub>2</sub>, _M_<sub>4_-O_</sub>, _M_<sub>6_-O_</sub>} for square grid.

For each data graph, we generate random connected subgraphs as pattern graphs of sizes 20,40,60,80,100 vertices. For each pattern size, we sample 200 random seeds to capture structural variability. For each case, we enumerate all isomorphic mappings using \(\Delta\)_-Motif_ on GPU and the VF2 baseline on CPU. Speedups are reported as the ratio \(T_{\mathrm{VF}2}/T_{\Delta\text{\textit{-Motif}}}\), with minimum, mean, and maximum values shown in  I.

I confirms a consistent advantage for \(\Delta\)_-Motif_ GPU across all configurations, with mean speedups ranging from \(3\times\) on small patterns (which typically under-utilize the GPU) and up to \(53.43\times\) on the largest cases. For smaller patterns, \(\Delta\)_-Motif_ under-utilizes the GPU, and fixed launch and data- movement overheads constitute a larger fraction of the total runtime. Larger data graphs generally yield higher speedups; for example, increasing the square grid size from 1600 to 3600 vertices raises the mean speedup for 100-node patterns from \(15.20\times\) to \(53.43\times\). Medium-to-large patterns (60 nodes and above) generally achieve the highest speedups, particularly for the 3600-node square grid and 4485-node heavy-hex, where the parallel _join_-and-_filter_ phase is fully leveraged, reaching maximum observed speedups of \(415.20\times\) and \(594.92\times\),<tbc>

