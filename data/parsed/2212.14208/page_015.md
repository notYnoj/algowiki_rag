<tbc>integration. The system has dimension \(n=7.2\times 10^5\), and we take \(\tau/2=10^{-2}\). Since the positive definite diagonal matrix _E_ is highly ill-conditioned, we scaled the system from left and right with the square root of the inverse of _E_.

The results are reported in Figure 4. To solve the systems with _H_ we use preconditioned CG with a threshold dropping incomplete Cholesky preconditioner with drop tolerance 10<sup>-4</sup>. This results in a very efficient preconditioner, since on average we need just slightly less than two iterations to decrease the residual by one order of magnitude. Similarly to the previous example, FMR and FGAL perform very similarly and would be indistinguishable in the plots, which is why we only report the results for FMR. As before, we observe that FMR (and FGAL) require about twice the iterations with \(\varepsilon_\mathrm{cg}=10^{-1}\) than with "exact" solves (\(\varepsilon_\mathrm{cg}=10^{-12}\)). Both flexible methods again achieve small final residuals even when large values of \(\varepsilon_\mathrm{cg}\) are used.

For non-flexible MR, the iterations stagnate quite early, except for \(\varepsilon_\mathrm{cg}=10^{-12}\), in which case the non-flexible method cannot be distinguished from FMR.

_Acknowledgement._ We are very grateful to the authors of [9], Candan Güdücü, Jörg Liesen, Volker Mehrmann and Daniel Szyld for stimulating dicussions and for making their example matrices available to us with the precise parameter settings, as well to Nicodemus Banagaaya for providing us with the matrix for Example 4 from [2].

## REFERENCES

cg tolerance = 0.1
100
cg tolerance = 0.01
non-flexible MR
100
non-flexible MR
FMR
FMR
10-2
a posteriori bound
10-2
a posteriori bound
10-4
10-4
10-6
10-6
10-8
10-8
10-10
10-10
10-12
10-12
10-14
10-14
0
5
10
15
20
25
30
35
40
0
5
10
15
20
25
30
35
40
cg tolerance = 0.001
cg tolerance = 1e-12
100
100
non-flexible MR
non-flexible MR
FMR
FMR
a posteriori bound
a posteriori bound
10-2
10-4
10-5
10-6
10-8
10-10
10-10
10-12
10-14
0
5
10
15
20
25
30
35
40
10-15
0
1
2
3
4
5
6

Fig. 4. _Results for the coupled electro-thermal problem in Example 4 with_ \(\tau/2=10^{-2}\) _and four choices for_ \(\varepsilon_\mathrm{cg}\) _are considered._

