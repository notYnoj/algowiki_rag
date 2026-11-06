### Validation.

The program was checked against known enumerative results. In the orientable case the number of one-cycle _rooted_ codes equals the Harer-Zagier number \(\varepsilon_g(2g)=\frac{(4g)!}{4^g(2g+1)!}\) Harer and Zagier (1986): 1,21,1485 for _g_=1,2,3. The numbers _N_=1,4,82 of equivalence classes under the dihedral group for _g_=1,2,3 coincide with the numbers of maximal chord diagrams up to all isomorphisms computed by Krasko (2017). For arbitrary sign vectors, the numbers of rooted one-cycle codes (orientable and non-orientable together) 1,5,41,509,8229 for _k_=1_,...,_5 coincide with the numbers of rooted one-vertex one-face maps with _k_ edges on all closed surfaces given there. Moreover, in both cases the sum of the orbit sizes 4_k/_|Stab| over all classes equals the number of rooted one-cycle codes (e.g. 21 for _k_=4 orientable and 41 for _k_=3 non-orientable), and for every class its dual is found in C.

## 7 Conclusion

In this paper, we have established a unified combinatorial framework for the topological classification of optimal Morse flows on closed surfaces based on single-cycle chord diagrams. By leveraging Smale’s theorem, we demonstrated that setting equal values at all saddle critical points naturally translates polar Morse flows into Morse functions corresponding to Fomenko atoms with a single input and output, which map to degree-2 edges on Kronrod-Reeb graphs. The upgraded indexing convention-assigning matching labels \(i\in\{1,\dots,k\}\) to chord endpoints-provides a compact and canonical representation suitable for algorithmic enumeration and dual graph embeddings.

The upgraded indexing convention -- assigning matching labels \(i\in\{1,\dots,k\}\) to chord endpoints -- provides a compact and canonical representation suitable for algorithmic enumeration. Moreover, the dual chord diagram describes the same flow with reversed time: replacing the vector field _X_ by -_X_ interchanges the source and the sink, and the diagram is replaced by its dual. Our algorithm therefore not only lists the diagrams but also finds the pairs of dual diagrams, i.e. the pairs of mutually reversed flows, and the self-dual diagrams, i.e. the flows equivalent to their reverses. For example, among the 82 diagrams of genus _g_=3 there are 30 self-dual ones and 26 dual pairs, so there are 56 classes of flows up to time reversal.

The methodology developed here opens several natural avenues for further research and generalizations:

1. **Multi-cycle chord diagrams:** Extending the canonical chord encoding from single-source (polar) flows to arbitrary Morse-Smale flows with multiple sources and sinks on higher-genus closed surfaces.<tbc>

2. **Manifolds with boundary:** Adapting the chord-diagram formalism to capture boundary critical points, sliding vector fields, and boundary-parallel trajectories on surfaces with non-empty boundary.<tbc>

3. **Higher-dimensional generalizations:** Applying multi-dimensional handle decomposition codes and generalized Reeb graphs to classify Morse-Smale flows on 3-manifolds and 4-manifolds.<tbc>

4. **Software ecosystem and visualization:** Integrating our single-cycle chord diagram algorithms with interactive software packages on Zenodo Prishlyak (2026a,b) to facilitate the automated generation, dual transformation, and visual rendering of complex dynamical phase portraits.<tbc>

\begin{tabular}{cccc}
**Genus** _g_ & **Total** _N_ & **Dual Pairs** _K_ & **Self-Dual** 2_K-N_ \\
-8 & 3534490 & 1775258 & 16026 \\
-7 & 144904 & 73220 & 1536 \\
-6 & 7190 & 3847 & 504 \\
-5 & 473 & 266 & 59 \\
-4 & 47 & 35 & 23 \\
-3 & 8 & 6 & 4 \\
-2 & 2 & 2 & 2 \\
-1 & 1 & 1 & 1 \\
0 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 \\
2 & 4 & 4 & 4 \\
3 & 82 & 56 & 30 \\
4 & 7258 & 3827 & 396 \\
\end{tabular}

1: Enumeration metrics for one-cycle signed chord diagrams across surface genus _g_. Here _N_ is the total count of non-equivalent diagrams, _K_ is the number of distinct dual pairs, and 2_K-N_ is the number of self-dual diagrams.

