according to Theorems 5.3, 6.1 and 6.3. Plugging them into (27) would verify the correctness of the claimed bound on \(\omega(1,\kappa,1)\).

## Optimization strategy.

Finding a set of parameters that lead to the best bound of \(\omega(1,\kappa,1)\) can be modeled as a constrained optimization problem:

\(\begin{array}{ c c }
\text{minimize} & \omega' \\
\text{subjectto} & \text{allconstraintsinTheorems5.3,6.1and6.3} \\
 & \mathrm{lim}_{\varepsilon\rightarrow 0}\mathrm{lim}_{n\rightarrow\infty} V^{1/n}\cdot\mathrm{min}\big\{A,B^{1/\kappa},C\big\}^{\omega^\prime/n}\ge(q+2)^{2^{\ell^*-1}}.
\end{array}\) (28)

We used _sequential quadratic programming (SQP)_ to solve this optimization problem, which is a well-known iterative approach for solving nonlinear constrained optimization. The software package SNOPT \[GMS05\] is used for performing SQP. Like all other optimization methods for nonlinear optimization, SQP does not guarantee finding the global optimum or a specific convergence rate; the quality of the solution and the time performance both rely on the _initial point_ of the iterative process, which could be provided by the user.

For \(\kappa=1\), we take the parameters from \[LG14\] which Le Gall used to analyze \(\mathrm{CW}_q^{\otimes 2^{\ell^*-1}}\) for square matrix multiplication, and transform it into a feasible solution to the optimization problem (28), which we set as the initial point. Specifically, Le Gall’s parameters consist of a distribution \(\alpha\) over level-\(\ell^*\) constituent tensors (for the global stage) together with a split distribution \(\alpha_{i,j,k}\) for every constituent tensor _T<sub>i,j,k</sub>_ (for the constituent stages). We specify our parameters as follows:

