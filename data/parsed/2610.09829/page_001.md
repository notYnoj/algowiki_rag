Packing Diverse Short Cycles

**Abstract**

Bentert, Fomin, Golovach, Korhonen, Lochet, Panolan, Ramanujan, Saurabh, and Simonov (SODA 2025) initiated the parameterized study of Edge-Disjoint Shortest Cycle Packing: given a weighted graph _G_ and an integer _k_, decide whether _G_ contains _k_ edge-disjoint cycles of minimum weight. They showed that the problem admits an algorithm running in time _n_<sup>O(_k_<sup>6</sup>)</sup> and asked whether it is fixed-parameter tractable or W[1]-hard parameterized by _k_. We resolve this question by proving that Edge-Disjoint Shortest Cycle Packing is W[1]-hard parameterized by _k_, even on unweighted subcubic graphs. The same lower bound also applies to the vertex-disjoint variant.

For planar graphs, the same paper provides a construction of a kernel with O(_k_<sup>2</sup>) vertices and an algorithm running in time \(k^{\mathcal{O}(k)}\cdot n^{\mathcal{O}(1)}\), and explicitly asked whether the problem admits a single-exponential algorithm of running time \(2^{\mathcal{O}(k)}\cdot n^{\mathcal{O}(1)}\). Rather than addressing this question in isolation, we introduce a more general framework, Diverse Shortest Cycle Coverage, which asks for _k_ shortest cycles that may overlap in a controlled way while maximizing the total weight of covered edges. This framework simultaneously captures edge-disjoint shortest cycle packing, the problem of finding diverse shortest cycles, and the problem of maximizing edge coverage by shortest cycles. Our main algorithmic result shows that Diverse Shortest Cycle Coverage can be solved on planar graphs in time \(2^{\mathcal{O}(k)}\cdot n^{\mathcal{O}(1)}\), thereby establishing a single-exponential algorithm for Edge-Disjoint Shortest Cycle Packing as a special case.

The key ingredient behind our algorithm is a structural analysis of the _Laminar Shortest Cycles Tree_, a tree-like decomposition that reveals a laminar interaction pattern among shortest cycles in planar graphs and enables an efficient dynamic programming algorithm.

This work was supported by the Research Council of Norway under the BWCA (grant no. 314528) and Extreme-Algorithms (grant no 355137) projects, the European Research Council (ERC) via grant NewPC, reference 101199930, and the Trond Mohn forskningsstiftelse (grant no. TMS2023TMT01). Email addresses: `akanksha@cse.iitm.ac.in`, `fedor.fomin@uib.no`, `petr.golovach@uib.no`, `guptavinod439@gmail.com`, `yash.h.more@uib.no`, and `vidyasagartifr@gmail.com`.

Akanksha Agrawal<sup>1</sup>, Fedor V. Fomin<sup>2</sup>, Petr A. Golovach<sup>2</sup>, Vinod Gupta<sup>1</sup>, Yash Hiren More<sup>2</sup>, and Vidya Sagar Sharma<sup>1</sup>

<sup>1</sup>Indian Institute of Technology Madras, Chennai, India

<sup>2</sup>University of Bergen, Bergen, Norway

October 8, 2026

