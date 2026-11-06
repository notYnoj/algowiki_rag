Sparse analogs of the LU factorization, such as the KLU algorithm, retain the analysis, factorization, and solve structure while confining the computation to the nonzero matrix entries \[36\]. In general, the factors of a sparse matrix are generally much denser than the matrix itself due to fill in during elimination, so the analysis phase must compute a fill-reducing ordering and pay careful attention to the interaction between ordering, pivoting, and sparsity \[73\]. For matrices arising from two- and three-dimensional meshes under nested dissection orderings, the factorization costs _O(n_<sup>3/2</sup>) and _O(n_<sup>2</sup>) respectively in the total number of unknowns _n_, a substantial reduction from the dense _O(n_<sup>3</sup>) although still superlinear \[76, 73\]. Sparse elimination is inherently serial and branching heavy, so these methods have traditionally struggled to exploit CPU and GPU parallelism. `SuperLU\_MT` achieved a CPU-parallel factorization by scheduling the independent subtrees of the elimination tree across threads and pipelining the remaining panel updates, and we refer the reader to Demmel et al. \[77\] for the details of the algorithm. Practical GPU implementations have emerged only recently, most notably NVIDIA’s cuDSS, a GPU-accelerated sparse direct solver. We have developed `diff-soup` around `cuDSS`, mapping its three phases onto the caching structure of the integrator: the symbolic analysis is performed once per sparsity pattern, which the discretization fixes _a priori_, the numeric factorization is repeated only when the setup gate refreshes _W<sub>n</sub>_, and the cached factors serve every Newton iterate in between through cheap triangular solves. This solver has also allowed us to explore GPU-specific strategies for accelerating the computation, such as working in reduced precision, batching independent solves in parallel, and employing multi-GPU execution, as we discuss in Section 4.

Finally, the partitioning of the state into local and global variables allows us to accelerate the linear solves through a Schur complement. We partition the Newton system of Eq. (4) conformally with the state as

\(\left(\begin{array}{ c c }
A & B \\
C & D
\end{array}\right)\left(\begin{array}{ c }
\delta_l \\
\delta_g
\end{array}\right)=-\left(\begin{array}{ c }
G_l \\
G_g
\end{array}\right),\) (7)

where _l_ collects the local differential and algebraic states and _g_ the global variables. Through the pencil \(W_n=\frac{1}{\gamma_n}M-J_n\), each block inherits the structure of the corresponding Jacobian block: _A_ carries the sparse local coupling of \(\partial f_l/\partial y_l\), _D_ is the small dense \(n_g\times n_g\) global block of \(\partial f_g/\partial y_g\), and _B_ and _C_ carry the dense coupling columns \(\partial f_l/\partial y_g\) and rows \(\partial f_g/\partial y_l\). Eliminating \(\delta_l\) from the first block row and substituting into the second reduces the system<tbc>

