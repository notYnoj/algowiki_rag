followed by a sequential Python-based scoring function for candidate scoring \[5\].<sup>2</sup> Note that although the design of scoring cost functions is an active research topic in quantum computing, it is not the focus of this work. Here, we adopt the same cost function as used in \[5\].

The data graph was derived from the qubit connectivity of IBM’s `ibmq\_fez`, a state-of-the-art 156-qubit quantum processor (represented as a 156-node graph). We benchmark our pipeline on a diverse set of pattern graphs obtained from quantum circuits in the `QASMBench` benchmark suite \[66\], covering sizes from 30 to 70 qubits and including a scaling set of Bernstein-Vazirani (BV) circuits.<sup>3</sup>

Results are presented in Fig. 5. Panel (a) reports the total wall-clock time for layout selection, broken down into layout generation and other components (primarily scoring). For `VF2PostLayout`, the sequential Python-based scoring often dominates the runtime, whereas \(\Delta\)_-Motif_ maintains highly efficient scoring through its tabular design. To highlight our core algorithmic innovation, panel (b) only reports speedups for layout generation (i.e., subgraph isomorphism) relative to VF2. Across this varied workload, GPU implementations of \(\Delta\)_-Motif_ consistently outperform VF2 by up to two orders of magnitude. For very small circuits or cases with small number of layouts, all methods complete layout generation quickly and GPU launch overheads dominate the runtime, so speedups are modest. However in these cases, the sequential layout<tbc>

<tbc>scoring in VF2 becomes the main bottleneck. In contrast, when circuits yield many valid layouts on the 156-qubit device, the larger intermediate search spaces amplify GPU advantages. This trend is especially clear in the BV scaling experiments, where the 40-qubit BV circuit produces the most layouts and exposes greater parallelism.

These results illustrate a realistic challenge in quantum layout selection: even when data graphs are only a few hundred nodes, large pattern graphs can yield enormous search spaces. Here, `VF2PostLayout` suffers from sequential bottlenecks in both layout generation and scoring, whereas \(\Delta\)_-Motif_ delivers strong and stable execution with total runtimes well under one second. Our tabular-based scoring adds minimal overhead. As quantum devices scale to hundreds or even thousands of qubits in the coming years, the scalability trends observed in this work provide strong evidence that our method can continue to deliver substantial performance benefits.

## VII. CONCLUSION

In this paper, we introduced \(\Delta\)_-Motif_, a parallel subgraph isomorphism algorithm motivated by the layout-selection bottleneck in quantum circuit compilation. It transforms the traditional sequential search into a massively parallel data- processing task, decomposing pattern graphs into smaller motifs and recombining them through database primitives without specialized GPU kernels.

We implement \(\Delta\)_-Motif_ using open-source, commodity software that exploits the parallelism of NVIDIA GPUs. By avoiding hardware-specific kernels and leveraging optimized RAPIDS libraries, our design remains portable across accelerator platforms. On quantum device topologies, this implementation consistently achieves order-of-magnitude performance improvements over VF2, with observed speedups of up to \(595\times\), and outperforms the GPU-based approach GSI where direct comparison is applicable. In end-to-end transpilation benchmarks, \(\Delta\)_-Motif_ delivers up to two orders of magnitude faster layout generation on a state-of-the-art 156-qubit quantum processor. To the best of our knowledge, \(\Delta\)_-Motif_ is the first GPU-based subgraph isomorphism approach implemented entirely using database-style relational primitives. As quantum devices scale to thousands of qubits, the scalability trends shown here position \(\Delta\)_-Motif_ as a practical tool for next-generation quantum compilation and open new research directions at the intersection of graph algorithms, quantum, and high-performance computing.

## ACKNOWLEDGMENT

We thank Bradley Dice for valuable discussions and support. We are also grateful to our colleagues at Q-CTRL, NVIDIA, and Oxford Quantum Circuits, whose technical expertise, product engineering, and design efforts contributed significantly to the results presented in this paper.

## REFERENCES

<sup>2</sup>The scoring stage is sequential for undirected data graphs, which we use because they yield more isomorphisms. While some quantum hardware supports only directed two-qubit operations, reversing the direction in the postprocessing is trivial in practice, allowing us to consider a much larger space of feasible layouts using the undirected model. <sup>3</sup>Before layout selection, all input logical circuits are pre-transpiled with Qiskit (opt\_level=1) to ensure that every two-qubit operation is mapped to physically connected qubits, making the resulting pattern graphs valid subgraphs of the device connectivity. \[1\] D. N. Nicholson and C. S. Greene, "Constructing knowledge graphs and their biomedical applications," _Computational and Structural Biotechnology Journal_, vol. 18, pp. 1414-1428, 2020. \[Online\]. Available: https://www.sciencedirect.com/science/article/pii/S2001037020302804

VF2PostLayout Layout Gen.
VF2PostLayout Total Time
A-Motif GPU Layout Gen.
A-Motif GPU Total Time
(a)
102
Wall time (s)
100
10-2
103
(b)
102
101
Speedups
(Layout Gen.)
100
10-1
bv n30
bv n40
bv n50
bv n60
bv n70
Cat n35
ghz n40
jging n34
knn n31
knn n41
Knn n67
Knn n67
Wstate n36
Wstate n36

Fig. 5. Quantum layout selection benchmarks on IBM’s `ibmq\_fez` topology (156 qubits), comparing \(\Delta\)_-Motif_ with Qiskit’s `VF2PostLayout` across selected circuits from the `QASMBench` suite. (a) Wall-clock time for completing layout selection, broken into layout generation and other components (primarily layout scoring). In some VF2 cases, scoring dominates the runtime. (b) Speedups in layout generation time, comparing \(\Delta\)_-Motif_ GPU against VF2. Labels follow the format `\<algorithm\>\<n\<qubits\>`, e.g., `bv\_n30` denotes a 30-qubit Bernstein-Vazirani circuit.

