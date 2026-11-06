Combining (4.6) with (4.7) and (4.8) yields<tbc>

\(\|\widehat{C}-C\|\le\sum_{j=1}^p|\alpha_j|\left((1+\delta_1)((\lceil\mathrm{log}_2p\rceil+1)\mathbf{u}+1)\|\widehat{C}_j-\widetilde{C}_j\|+((1+\delta_1)(\lceil\mathrm{log}_2p\rceil+1)\mathbf{u}+\delta_1)\|\widetilde{C}_j\|+\|\widetilde{C}_j-C_j\|\right)+O(\mathbf{u}^2).\) (4.9)

<tbc>Now Theorem 4.5 guarantees<tbc>

\(\|\widehat{C}_j-\widetilde{C}_j\|\le(k/k_0^L+\widetilde{Q}(\varepsilon_j)L)(k/k_0^L)\widetilde{E}(\varepsilon_j)^L\|A\|\|B\|\mathbf{u}+O(\mathbf{u}^2)\) (4.10)

<tbc>for \(\widetilde{E}(\varepsilon_j)\) and \(\widetilde{Q}(\varepsilon_j)\) the stability factor and prefactor corresponding to \(\widetilde{U}_\phi(\varepsilon_j)\), \(\widetilde{V}_\psi(\varepsilon_j)\), \(\widetilde{W}_\nu(\varepsilon_j)\), \(\tilde{\phi}\), \(\tilde{\psi}\), and \(\tilde{\nu}^{-1}\). Moreover, recalling (4.4), \(\|\widetilde{C}_j\|\le(k/k_0^L)\widetilde{E}(\varepsilon_j)^L\|A\|\|B\|\). Finally, Theorem A.3 implies

\(\|\widetilde{C}_j-C_j\|\le\left((1+\delta_2)^{6L}-1\right)(k/k_0^L)E(\varepsilon_j)^L\|A\|\|B\|.\) (4.11)

We complete the proof by applying these to (4.9) and simplifying, inserting the definition of \(\alpha_j\), and noting \(\widetilde{E}(\varepsilon_j)\le(1+\delta_2)^6E(\varepsilon_j)\) and \(\widetilde{Q}(\varepsilon_j)=Q(\varepsilon_j)\) (since entry-wise relative perturbations of size \(0<\delta_2<1\) preserve the sparsity structure of the encoding matrices/basis transformations).

## 4.3 Parameter Selection for Improved Stability

Theorem 4.6 suggests that, from the point of view of stability, a good choice for the evaluation parameters \(\varepsilon_1,\dots,\varepsilon_p\) is the _p_-th roots of unity - i.e., \(\varepsilon_j=e^{2\pi ij/p}\). In this case, the factor \(\prod_{i\neq j}\frac{|\varepsilon_i|}{|\varepsilon_i-\varepsilon_j|}\) simplifies to 1_/p_, and we do not have to worry about \(E(\varepsilon_j)\) blowing up due to large positive/negative powers of \(\varepsilon\) in the encoding matrices or basis transformations.

There is, however, one catch: the roots of unity, with the exception of \(\pm 1\) and \(\pm i\), are _not_ floating-point numbers, and hence Theorem 4.6 does not apply (in general) when \(\varepsilon_j=e^{2\pi ij/p}\). Instead, the best we can do is use the rounded roots of unity \(\tilde{\varepsilon}_1,\dots,\tilde{\varepsilon}_p\), which take the form \(\tilde{\varepsilon}_j=e^{2\pi ij/p}\cdot(1+\delta_j)\) for some \(|\delta_j|\le\mathbf{u}\). Importantly, for _p_ not too large, these approximate roots satisfy \(\prod_{i\neq j}\frac{|\tilde{\varepsilon}_i|}{|\tilde{\varepsilon}_i-\tilde{\varepsilon}_j|}=1/p+O(\mathbf{u})\). In particular, applying Theorem A.2 with \(\delta=\mathbf{u}\) and since the spacing between the _p_-th roots of unity is \(2\mathrm{sin}(\pi/p)\), we have the bound

\(\frac{|\tilde{\alpha}_j-1/p|}{1/p}\le\frac{(p-1)\mathbf{u}}{\mathrm{sin}(\pi/p)-p\mathbf{u}}\) (4.12)

for \(\tilde{\alpha}_1,\dots,\tilde{\alpha}_p\) the coefficients that solve the Vandermonde system corresponding to \(\tilde{\varepsilon}_1,\dots,\tilde{\varepsilon}_p\).

This implies the following corollary of Theorem 4.6, which assumes (1) that rounded roots of unity are used as evaluation points in Algorithm 4, and (2) that \(\tilde{\alpha}_1,\dots,\tilde{\alpha}_p\) and the entries of the encoding matrices/basis transformations at \(\tilde{\varepsilon}_1,\dots,\tilde{\varepsilon}_p\) are computed to high enough relative accuracy that \(g(\delta_1,\delta_2)\le 1+cp\mathbf{u}+O(\mathbf{u}^2)\) for some small constant _c\>_0. This specific bound is motivated by Theorem A.1.

**Corollary 4.7** (Simplified version of Theorem 4.6)**.** _Let_ \(A,B\in\mathbb{C}^{n\times n}\) _with C=AB and let ALG be a floating-point, alternative basis matrix multiplication routine, which implements recursively a degree d base-case algorithm for_ \(k\times k\) _approximate matrix multiplication (where we assume n is a power of k and accordingly that the algorithm is applied over L_=log_<sub>k</sub>(n_) _recursive steps). Suppose that_ \(\widehat{C}\) _is the output of the approximate-to-exact procedure of Bini \[9\] applied to ALG in floating-point arithmetic, taking the evaluation parameters_ \(\varepsilon_1,\dots,\varepsilon_p\) _to be floating-point approximations of the p-th roots of unity, where p=d_log_<sub>k</sub>n_+1_. Assume further that all conditions of Theorem 4.6 hold, with in particular the solution to the corresponding Vandermonde system and the entries of the encoding matrices/basis transformations (at each_ \(\varepsilon_j\)_) computed to sufficiently high relative accuracy to guarantee_ \(g(\delta_1,\delta_2)\le 1+cp\mathbf{u}+O(\mathbf{u}^2)\) _for a constant c\>_0 _and_ **u** _the unit roundoff. In this case, we have_<tbc>

\(\|\widehat{C}-C\|\le f_{ALG}(n)\|A\|\|B\|\mathbf{u}+O(\mathbf{u}^2)\)

<tbc>_for_

\(f_{ALG}(n)=\frac{1}{p}\sum_{j=1}^p\left(2+Q(\varepsilon_j)\mathrm{log}_kn+\lceil\mathrm{log}_2(p)\rceil+cp\right)n^{\mathrm{log}_kE(\varepsilon_j)},\)

_where_ \(\|\cdot\|\) _is the maximum entry norm and_ \(Q(\varepsilon)\) _and_ \(E(\varepsilon)\) _are the stability prefactor and factor, respectively, of ALG (see Theorem 4.3 and Theorem 4.4)._

