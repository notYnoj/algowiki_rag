<tbc>previous two examples, we see that with \(\varepsilon_\mathrm{cg}=10^{-1}\) we need less than twice as many iterations than with "exact" solves (\(\varepsilon_\mathrm{cg}=10^{-12}\)), and this number of iterations is this time exceeded by just 1 for \(\varepsilon_\mathrm{cg}=10^{-2}\). We need between 4 and 6 (unpreconditioned) CG iterations with _H_ to reduce the initial residual by the factor \(\varepsilon_\mathrm{cg}=10^{-1}\) in each step of \(\ell\)MR, and between 43 and 49 to reduce it by the factor \(\varepsilon_\mathrm{cg}=10^{-12}\).

In the three plots for \(\varepsilon_\mathrm{cg}=10^{-1},10^{-2}\) and 10<sup>-12</sup> we in addition plot the _H_-norms of the residuals in a variant of FMR which differs from FMR only by the fact that in the underlying preconditioned Lanczos algorithm, Algorithm 3.2, we do not compute \(\gamma_k\) but rather put \(\gamma_k=\beta_{k-1}\). This method is termed "non-flexible MR". The plots show that for the larger values of \(\varepsilon_\mathrm{cg}\) this modification results in a significantly to dramatically delayed convergence.

In a similar spirit, the bottom right plot of Figure 3 show the _H_<sup>-1</sup>-norm of the residual for the non-flexible \(\ell\)MR method of Rapoport (left preconditioning), where we solve for _H_ with CG at different accuracies. Not really surprisingly, and convincingly, the plot illustrates that this "inexact" version of \(\ell\)MR stagnates sooner the less accurately we solve for _H_. A similar behavior can be observed for non-flexible inexact \(\ell\)GAL, for which we do not report results here. In contrast, the flexible methods reach high accuracies for the overall system even when \(\varepsilon_\mathrm{cg}\) is large.

_Example 4._ We take the coupled electro-thermal DAE system from [2], from which we treat the thermal part after applying the decoupling described in [2]. This again yields an ODE of the form (5.1). Similar to the previous example, we consider the linear systems arising when using the implicit midpoint Euler method for time<tbc>

cg tolerance = 0.1
cg tolerance = 0.01
100
100
non-flexible MR
non-flexible MR FMR
FMR
a posteriori bound
a posteriori bound
10-5
10-5
10-10
10-10
10-15
10-15
0
5
10
15
20
0
2
4
6
8
10
cg tolerance = 1e-12
100
100
Inexact left preconditioned MR
non-flexible MR FMR
eps
cg = 1e-1
eps
cg = 1e-2
10-2
eps
cg = 1e-4
eps
cg = 1e-12
10-5
10-4
10-6
10-10
10-8
10-15
10-10
0
1
2
3
4
5
6
7
0
1
2
3
4
5
6
7

Fig. 3. _Convergence plots for the spring mass system of dimension_ 10<sup>6</sup>_, Example 3,_ \(\tau/2=10^{-1}\)_, three choices for_ \(\varepsilon_\mathrm{cg}\)_. Bottom right plot is for non-flexible_ \(\ell\)_MR with inexact solves for H._

