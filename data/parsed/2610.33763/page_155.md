As it can be seen, the quantity \(\alpha_j\) stabilizes around 2 as _n_ increases. This is in perfect agreement with the fact that the minimal eigenvalue of _A<sub>n</sub>_ converges to zero as _n_<sup>-4</sup>, while the minimal eigenvalue of _B<sub>n</sub>_ converges monotonically from above to \(min\xi=1\). The key point is that the minimal eigenvalue of the geometric mean behaves asymptotically as the geometric mean of the minimal eigenvalues of _A<sub>n</sub>_ and _B<sub>n</sub>_, respectively. Similar remarks can be made in the subsequent case with respect to **Example 2**.

The observed numerical evidences are not implied by the theoretical derivations and this is an interesting fact that deserves to be investigated theoretically in the future. In particular, we would like to prove formally that that \(\alpha_j\) converges to 2 for the first example,  9.1, and it converges to 4 in the second example,  9.2, even from the preliminary numerical results the convergence does not look monotonic.

**Example 2: minimal eigenvalue**

• _X<sub>n</sub>=G(A<sub>n</sub>,B<sub>n</sub>_)

• Take \(n_j=40\cdot 2^j\), _j_=0,1,2,3,

• Compute \(\tau_j=\lambda_{min}(X_{n_j})\), _j_=0,1,2,3,

• Compute \(\alpha_j=log_2(\frac{\tau_j}{\tau_{j+1}})\), _j_=0,1,2.

## 9.2.4 Numerical study: noncommuting, rank-deficient symbols

In this section, through numerical test, we investigate the eigenvalue distribution of the geometric means {_G(A<sub>n</sub>,B<sub>n</sub>_)}_<sub>n</sub>_ with

\(G(A_n,B_n)=A_n^{1/2}\big(A_n^{-1/2}B_nA_n^{-1/2}\big)^{1/2}A_n^{1/2},\)

where {_A<sub>n</sub>}<sub>n</sub>_ and {_B<sub>n</sub>}<sub>n</sub>_ are HPD GLT matrix sequences with \(r\times r\) matrix-valued symbols \(\kappa,\xi\). The GLT matrix sequences are specifically chosen with GLT symbols so that:

1. they are rank-deficient on a subset of positive Lebesgue measure; and

2. they do not commute pointwise on a set of positive measure.

These hypotheses clearly set the problem outside the scope of commuting or almost everywhere invertible cases treated in Theorems 9.2 and in Theorem 9.4.

Our tests provide evidence for two phenomena:

\begin{tabular}{ccc}
_n_ & \(\tau_j\) & \(\alpha_j\) \\ 40 & \(3.9177\times 10^{-7}\) & 4.0003 \\ 80 & \(2.4480\times 10^{-8}\) & 4.0040 \\ 160 & \(1.5259\times 10^{-9}\) & 4.0009 \\ 320 & \(9.5367\times 10^{-11}\) & \\ \end{tabular}

9.2: Numerical behaviour of the minimal eigenvalue.

