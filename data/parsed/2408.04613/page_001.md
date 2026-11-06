# Core-Sparse Monge Matrix Multiplication

# Improved Algorithm and Applications

**Paweł Gawrychowski** \(\unknown\) University of Wrocław, Poland

**Egor Gorbachev** \(\unknown\) Saarland University and Max Planck Institute for Informatics, Saarland Informatics Campus, Germany

**Tomasz Kociumaka** \(\unknown\) Max Planck Institute for Informatics, Saarland Informatics Campus, Germany

**Abstract**

_Min-plus matrix multiplication_ is a fundamental tool for designing algorithms operating on distances in graphs and different problems solvable by dynamic programming. We know that, assuming the APSP hypothesis, no subcubic-time algorithm exists for the case of general matrices. However, in many applications the matrices admit certain structural properties that can be used to design faster algorithms. For example, when considering a planar graph, one often works with a _Monge matrix A_, meaning that the _density matrix A_ \(\unknown\) has non-negative entries, that is, \(A_{i,j}^\unknown:=A_{i+1,j}+A_{i,j+1}-A_{i,j}-A_{i+1,j+1}\ge 0\). The min-plus product of two \(n\times n\) Monge matrices can be computed in O(_n_<sup>2</sup>) time using the famous SMAWK algorithm.

In applications such as longest common subsequence, edit distance, and longest increasing subsequence, the matrices are even more structured, as observed by Tiskin [J. Discrete Algorithms, 2008]: they are (or can be converted to) _simple unit-Monge matrices_, meaning that the density matrix is a permutation matrix and, furthermore, the first column and the last row of the matrix consist of only zeroes. Such matrices admit an implicit representation of size O(_n_) and, as shown by Tiskin [SODA 2010 & Algorithmica, 2015], their min-plus product can be computed in O(_n_log_n_) time. Russo [SPIRE 2010 & Theor. Comput. Sci., 2012] identified a general structural property of matrices that admit such efficient representation and min-plus multiplication algorithms: the _core size_ \(\delta\), defined as the number of non-zero entries in the density matrices of the input and output matrices. He provided an adaptive implementation of the SMAWK algorithm that runs in \(\mathcal{O}((n+\delta)log^3n)\) or \(\mathcal{O}((n+\delta)log^2n)\) time (depending on the representation of the input matrices).

In this work, we further investigate the core size as the parameter that enables efficient min-plus matrix multiplication. On the combinatorial side, we provide a (linear) bound on the core size of the product matrix in terms of the core sizes of the input matrices. On the algorithmic side, we generalize Tiskin’s algorithm (but, arguably, with a more elementary analysis) to solve the core-sparse Monge matrix multiplication problem in \(\mathcal{O}(n+\delta log\delta)\subseteq\mathcal{O}(n+\delta logn)\) time, matching the complexity for simple unit-Monge matrices. As witnessed by the recent work of Gorbachev and Kociumaka [S’25] for edit distance with integer weights, our generalization opens up the possibility of speed-ups for weighted sequence alignment problems. Furthermore, our multiplication algorithm is also capable of producing an efficient data structure for recovering the witness for any given entry of the output matrix. This allows us, for example, to preprocess an integer array of size _n_ in \(\widetilde{\mathcal{O}}(n)\) time so that the longest increasing subsequence of any sub-array can be reconstructed in \(\widetilde{\mathcal{O}}(\ell)\) time, where \(\ell\) is the length of the reported subsequence. In comparison, Karthik C. S. and Rahul [arXiv, 2024] recently achieved \(\mathcal{O}(\ell+n^{1/2}polylogn)\)-time reporting after O(_n_<sup>3/2</sup>polylogn)-time preprocessing.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Design and analysis of algorithms

**Keywords and phrases** Min-plus matrix multiplication, Monge matrix, longest increasing subsequence

**Funding** _Egor Gorbachev:_ This work is part of the project TIPEA that has received funding from the European Research Council (ERC) under the European Unions Horizon 2020 research and innovation programme (grant agreement No. 850979).







