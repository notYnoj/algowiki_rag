<tbc>budget, and further border-rank degenerations allow larger sets of products to be aggregated. This connects the Coppersmith–Winograd approach to Pan’s trilinear aggregation and to bilinear algorithms for symmetric tensor contraction.

These finite constructions improve on the multiplication counts of the reference algorithms compared here for selected numbers and dimensions of independent matrix products. The benefit is not a new best bound on \(\omega\), but explicit constructions for moderate matrix dimensions and numbers of independent matrix- matrix products. Our error analysis quantifies error due to border-rank degenerations and finite-precision evaluation. This analysis allows us to search for constructions with a prescribed limiting retained fraction of accuracy.

We expect the finite constructions, particularly the border-rank variants, to be improvable. The searches are heuristic and use modest budgets, and their objectives emphasize multiplication counts at prescribed limiting accuracy. A practical formulation should also optimize finite-precision error constants and implementation costs rather than rely on these asymptotic criteria alone.

An intriguing future direction is to consider the use of the introduced embeddings and the inclusion- exclusion principle to develop aggregations that allow extraction of non-independent matrix-matrix products. Another open direction is to extend this approach to contractions of tensor cliques, starting with the _K_<sub>4</sub> contractions studied in [12, 13], and possibly to other contraction graphs.

Further analysis of numerical stability should account for how the embeddings and corrections are evaluated, alongside experimental evaluation of both the exact and approximate algorithms. High-performance implementations should examine encoding and decoding costs as well as bilinear multiplication counts. Their communication cost, including data movement within memory hierarchies and between processors, is another important subject for study.

## 10 Acknowledgments

The work of Edgar Solomonik was supported by the U.S. Department of Energy, Office of Science, Office of Advanced Scientific Computing Research, under Award No. DE-SC0023483, as part of Sarsitute: A Mathematical Institute for Sparse Computations in Science and Engineering.

The initial idea of aggregation of tensor contraction was developed when both authors were participating as long-term visitors in the Fall 2025 program on Complexity and Linear Algebra at the Simons Institute for the Theory of Computing, University of California, Berkeley. After the conclusion of that program, the first author used large language models to further advance and analyze the numerical algorithm, as well as establish connections to prior literature. Gemini (Google) was initially used and helped establish the connection between Coppersmith and Winograd’s construction and aggregation of tensor contractions. The centering and weighting embeddings were developed with assistance from Gemini and ChatGPT (OpenAI). The connection to Sierpinski’s triangle was picked up from a ChatGPT exploration. Both ChatGPT and Claude (Anthropic) helped develop and analyze centered corrections as well as border rank degenerations and their numerical stability. ChatGPT was used to generate the final versions of the computational search algorithm and verification infrastructure, as well as to draft parts of the manuscript and edit text. The authors iterated on, edited, and ultimately hand-wrote much of the manuscript; they also tested the verification infrastructure and assume responsibility for all contents of the manuscript and software artifacts.

## A Recursive Proof of the Equal-Size Asymptotic Sum Bound

Assume that an exact rank-_r_ construction computes a direct sum of _m_ independent products \(\langle n,n,n\rangle\), and that _m_ divides _r_. Apply this construction to \(n\times n\) block matrices whose blocks have size \(n^{k-1}\times n^{k-1}\). The construction reduces the _m_ products of block matrices to _r_ independent products of blocks. Partition these _r_ block products into _r/m_ groups of _m_ and compute each group recursively by the same construction. If _R<sub>k</sub>_ denotes the resulting rank for _m_ independent products of dimension _n<sup>k</sup>_, then

\(R_1=r,R_k=\frac{r}{m}R_{k-1},\) (166)

