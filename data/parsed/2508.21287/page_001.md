\(\Delta\)-Motif: Parallel Subgraph Isomorphism via Tabular Operations for Scalable Layout Selection

**_Abstract_--As quantum processors scale to hundreds and eventually thousands of qubits, selecting optimal qubit layout during circuit compilation becomes a critical bottleneck. Layout selection requires solving subgraph isomorphism, a fundamental graph analysis problem: enumerating all occurrences of a pattern graph within a larger data graph while preserving structural relationships. This NP-complete problem underpins a wide range of applications beyond quantum compilation, including biological network analysis and data mining. Classical algorithms such as VF2 rely on backtracking search, which suffers from sequential bottlenecks that limit scalability on modern parallel hardware.**

**We introduce** \(\Delta\)**_-Motif_**, a GPU-accelerated subgraph isomorphism algorithm that reformulates the problem through the lens of database operations. Our key insight is to represent graphs in tabular format, transforming subgraph isomorphism into database primitives including joins, sorts, merges, and filters. \(\Delta\)**_-Motif_** decomposes graphs into small building blocks called motifs and systematically combines these using scalable relational operations. By leveraging highly optimized libraries from the NVIDIA RAPIDS ecosystem, our solution achieves massive parallelization without specialized low-level GPU kernels, while remaining portable across any system supporting standard relational primitives.

**We evaluate** \(\Delta\)**_-Motif_** on graph workloads motivated by quantum computing, which capture the structural properties of quantum circuits and device topologies arising in layout selection. On scaling benchmarks with large device topologies, \(\Delta\)**_-Motif_** substantially outperforms established methods such as VF2 and GSI, achieving speedups of up to \(595\times\) on GPU architectures. On realistic workloads using a state-of-the-art 156-qubit quantum processor, our end-to-end transpilation benchmarks show up to two orders of magnitude faster layout generation.

**_Index Terms_--Subgraph Isomorphism, GPU Acceleration, Quantum Circuit Compilation, Parallel Computing, Graph Algorithms**

### I. INTRODUCTION

Graphs have emerged as one of the most flexible and powerful data structures to represent complex relationships, leading to their ubiquitous presence across various computational domains. From modeling molecular interactions in bioinformatics [1] and tracking social connections in network analysis [2] to mapping dependencies in cybersecurity systems [3], graphs provide an intuitive and mathematically rigorous framework for capturing the intricate patterns that define real- world systems.

Central to many graph-based applications is the subgraph isomorphism problem, which seeks to find all instances of a pattern graph within a larger data graph while preserving

structural relationships. This problem is known to be NP- complete [4], yet it remains essential for tasks including circuit mapping in quantum devices [5], motif discovery in biological networks [6], social networks analysis [7], data mining [8] and drug discovery [9]. The ubiquity of its application to various use cases can create critical bottlenecks in compute and workload execution. Driving efficiencies for subgraph isomorphism will alleviate key barriers to the incorporation of emerging technologies like quantum computing into high- performance computing environments, and thereby its adoption for meaningful impact.

Traditional approaches such as VF2 [10], VF2++ [11], and VF3 [12] rely on backtracking with a largely DFS- like traversal, making them inherently sequential and hard to parallelize.  specialization techniques have been proposed to mitigate these limitations [13], and a range of systems have explored distributed execution, accelerator-based designs, and commercial data-processing frameworks such as Hadoop [14], Cassandra [15], and Spark [16]. Workloads also vary widely--weighted or unweighted graphs, small structured or large random patterns, and diverse connectivity--so no single algorithm is optimal across all settings, and existing work spans many complementary approaches. We discuss these trade-offs in more detail in Sec. II.

A key motivation for this work is the use of subgraph isomorphism in quantum circuit compilation, where the pattern graph represents a circuit’s qubit interaction structure and the data graph represents the physical connectivity of the target quantum processor. Recent work by Nation et al. [5] applied a Rust-based implementation of VF2 [17] in this setting, illustrating both the practicality and limitations of classical backtracking approaches. In our own evaluation, we found that such algorithms limit effective utilization of hundreds of CPU cores and modern GPU architectures. In quantum computing, the pattern graphs of interest are relatively large, typically dozens to around one hundred vertices, and at these sizes, many existing parallel subgraph isomorphism algorithms perform poorly or fail to scale effectively, whereas our algorithm remains efficient.

To overcome the sequential bottlenecks and limited parallelism of existing subgraph isomorphism enumeration, we developed a novel data-science centric solution that reformulates the problem as a series of tabular data operations. By representing both data and pattern graphs in tabular for

Yulun Wang<sup>1</sup>, Esteban Ginez<sup>1</sup>, Jamie Friel<sup>2</sup>, Yuval Baum<sup>1</sup>, Jin-Sung Kim<sup>3</sup>, Alex Shih<sup>1</sup>, Oded Green<sup>3</sup>

<sup>1</sup>Q-CTRL Inc., Los Angeles, USA

<sup>2</sup>Oxford Quantum Circuits, United Kingdom

<sup>3</sup>NVIDIA, USA

arXiv:2508.21287v4 [cs.DS] 2 Sep 2026

