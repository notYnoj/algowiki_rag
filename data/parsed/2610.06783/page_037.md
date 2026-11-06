polynomially smaller than the _D_ operations that it would take to compute that entry as an inner product. Second, we let the parameters of our construction vary. This will give larger time savings than _D_<sup>1/18</sup>, and trade-offs between the time savings, how thin the product must be, the query time, and the density of the set _W_ of wanted entries. We assume that the reader is familiar with Section 2, whose notation we use throughout, although we will begin with a brief reminder of the relevant notions.

In Section 4.1, we state the main results, Theorems 24 and 25, with explicit parameter examples in  2, as well as Corollary 26, the instance of Theorem 24 that our reductions in Sections 3 and 5 use. In Section 4.2, we will introduce the key new idea, the partial sums that our data structure stores, which we call boxes. In Section 4.3, we will then give the data structure in terms of the parameters (listed in  1), and finally we will set the parameters in Section 4.4.

\begin{tabular}{cccc}
symbol & meaning & in Section 2 & in this section \\
_m_, _D_=4_<sup>m</sup>_ & the number of inner levels, and the inner dimension of the product _XY_ & & \\
_L_, _c=L/m_ & the number of levels of the recursion, and its ratio to _m_ & _L_=19_m_ & _L=cm_, _c\>_10 \\
_N_<sub>0</sub>=3<sup>_L-m_</sup> & the number of rows of a row block, and of columns of a column block & & \\
\(K=\genfrac(){pt}{2}{L}{m}\) & the number of products _X<sub>Q</sub>Y<sub>Q</sub>_ of a tile, one for each set _Q_ of _m_ levels & & \\
\(M=KN_0^2\) & the number of output entries of a tile & & \\
\(\alpha_d=\genfrac(){pt}{2}{m}{d}9^d\) & the number of leaves of order _d_ contributing to one output entry & & \\
\(\beta_d=\genfrac(){pt}{2}{L}{m-d}9^{L-m+d}\) & the number of leaves of order _d_ in a tile & \(\beta_d\le 2^{-d}M\) & \(\beta_d\le\rho^dM\) \\
\(\rho=9m/(L-m+1)\) & the decay rate of the \(\beta_d\): \(\beta_d/\beta_{d-1}\le\rho\), see (7) & \(\rho<\frac{1}{2}\) & \(\rho<1\) \\
_t_ & the switching order: a query reads the leaves of order below _t_, and the preprocessing puts the others into boxes; in Section 2, the order at which the count of Lemma 11 splits & _t=m/_9 & \(t=\theta m\), \(0<\theta<0.9\) \\
\(\gamma\) & the preprocessing, or the whole computation when _W_ is given in advance, takes \(O(N^2log^2D/D^\gamma)\) time & \(\gamma=1/18\) & see  2 \\
\(\varepsilon\) & the results hold for \(D\le N^\varepsilon\) & \(\varepsilon=1/18\) & \(\varepsilon<R_c(\gamma)<0.1204\dots\) \\
_q_ & a query takes _O(D<sup>q</sup>_log_D_) time & no queries & see  2 \\
\(\kappa\) & the set _W_ of wanted entries has \(|W|\le N^2/D^\kappa\) & \(\kappa=\frac{1}{2}\) & see  2 \\
\end{tabular}

1: The parameters of our construction. The last two columns give their values or bounds in Section 2 and in this section. Where these columns are empty, the parameter is given by the formula in the first column in both sections. In this section, _L_ and _t_ are _cm_ and \(\theta m\) rounded up to integers, and the bound \(R_c(\gamma)\) is defined in Section 4.4.

