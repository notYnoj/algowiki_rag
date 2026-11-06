_5. The sum reduction in line 5 is performed (entry-wise) via the recursive, pairwise algorithm for inner products (see \[31, Section 3.1\])._<tbc>

_6. No over/underflow occurs during the computation._<tbc>

<tbc>_Then we have_<tbc>

\(\|\widehat{C}-C\|\le(k/k_0^L)\left[\sum_{j=1}^p\left(\prod_{i\neq j}\frac{|\varepsilon_i|}{|\varepsilon_i-\varepsilon_j|}\right)(g(\delta_1,\delta_2)f(\varepsilon_j)\mathbf{u}+(g(\delta_1,\delta_2)-1))E(\varepsilon_j)^L\right]\|A\|\|B\|+O(\mathbf{u}^2)\)

<tbc>_for_

\(f(\varepsilon_j)=(k/k_0^L)+Q(\varepsilon_j)L+\lceil log_2p\rceil+1\text{\textit{and}}g(\delta_1,\delta_2)=(1+\delta_2)^{6L}(1+\delta_1),\)

_where_ \(\|\cdot\|\) _is the maximum-entry norm,_ **u** _is the unit roundoff, and_ \(E(\varepsilon)\) _and_ \(Q(\varepsilon)\) _are the stability factor and prefactor, respectively, of_ **AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}\).

_Proof._ Let \(\widehat{\alpha}_1,\dots,\widehat{\alpha}_p\in\mathbb{C}\) and \(\widehat{C}_j\in\mathbb{C}^{m\times n}\) be the floating-point output of **Vandermonde-Solve**\((\varepsilon_1,\dots,\varepsilon_p)\) and **AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}(A,B,\varepsilon_j)\), respectively. The latter corresponds to encoding matrices \(\widetilde{U}_\phi(\varepsilon_j)\), \(\widetilde{V}_\psi(\varepsilon_j)\), \(\widetilde{W}_\nu(\varepsilon_j)\) and basis transformations \(\tilde{\phi}_{\varepsilon_j}\), \(\tilde{\psi}_{\varepsilon_j}\), and \(\tilde{\nu}_{\varepsilon_j}^{-1}\), which can be obtained from \(U_\phi(\varepsilon_j)\), \(V_\psi(\varepsilon_j)\), \(W_\nu(\varepsilon_j)\), \(\phi_{\varepsilon_j}\), \(\psi_{\varepsilon_j}\), and \(\nu_{\varepsilon_j}^{-1}\) by applying entry-wise relative perturbations of size at most \(\delta_2\). If \(\sum_{j=1}^p\widehat{\alpha}_j\widehat{C}_j\) is the _exact_ linear combination of the floating-point quantities \(\widehat{\alpha}_j\) and \(\widehat{C}_j\), and if \(\widetilde{C}_j\) is the exact- arithmetic output of the recursive, alternative basis bilinear algorithm corresponding to \(\widetilde{U}_\phi(\varepsilon_j)\), \(\widetilde{V}_\psi(\varepsilon_j)\), \(\widetilde{W}_\nu(\varepsilon_j)\), \(\tilde{\phi}_{\varepsilon_j}\), \(\tilde{\psi}_{\varepsilon_j}\), and \(\tilde{\nu}_{\varepsilon_j}^{-1}\), then we have

\(\|\widehat{C}-C\|=\left\|\widehat{C}-\sum_{j=1}^p\widehat{\alpha}_j\widehat{C}_j+\sum_{j=1}^p\widehat{\alpha}_j\widehat{C}_j-\sum_{j=1}^p\alpha_jC_j\right\|\le\left\|\widehat{C}-\sum_{j=1}^p\widehat{\alpha}_j\widehat{C}_j\right\|+\sum_{j=1}^p\|\widehat{\alpha}_j\widehat{C}_j-\alpha_jC_j\|,\) (4.5)

where the second term can be expanded as follows:

\(\sum_{j=1}^p\|\widehat{\alpha}_j\widehat{C}_j-\alpha_jC_j\|=\sum_{j=1}^p\|\widehat{\alpha}_j\widehat{C}_j-\widehat{\alpha}_j\widetilde{C}_j+\widehat{\alpha}_j\widetilde{C}_j-\alpha_j\widetilde{C}_j+\alpha_j\widetilde{C}_j-\alpha_jC_j\|\le\sum_{j=1}^p\left(|\widehat{\alpha}_j|\|\widehat{C}_j-\widetilde{C}_j\|+|\widehat{\alpha}_j-\alpha_j|\|\widetilde{C}_j\|+|\alpha_j|\|\widetilde{C}_j-C_j\|\right)\le\sum_{j=1}^p\left(|\alpha_j|\left(\|\widehat{C}_j-\widetilde{C}_j\|+\|\widetilde{C}_j-C_j\|\right)+|\widehat{\alpha}_j-\alpha_j|\left(\|\widetilde{C}_j\|+\|\widehat{C}_j-\widetilde{C}_j\|\right)\right)\le\sum_{j=1}^p\left(|\alpha_j|\left(\|\widehat{C}_j-\widetilde{C}_j\|+\|\widetilde{C}_j-C_j\|+\delta_1\left(\|\widetilde{C}_j\|+\|\widehat{C}_j-\widetilde{C}_j\|\right)\right)\right)=\sum_{j=1}^p\left(|\alpha_j|\left((1+\delta_1)\|\widehat{C}_j-\widetilde{C}_j\|+\|\widetilde{C}_j-C_j\|+\delta_1\|\widetilde{C}_j\|\right)\right).\text{(4.6)}\)

To similarly bound the first term of (4.5), we note that each entry of \(\widehat{C}\) can be interpreted as a floating-point inner product between the vector \(\widehat{\alpha}\in\mathbb{C}^p\) of approximate coefficients and a vector of corresponding entries of \(\widehat{C}_1,\dots,\widehat{C}_p\). Since we assume that the recursive, pairwise algorithm is used to compute this inner product, we have

\(\left\|\widehat{C}-\sum_{j=1}^p\widehat{\alpha}_j\widehat{C}_j\right\|\le(\lceil log_2p\rceil+1)\left(\sum_{j=1}^p|\widehat{\alpha}_j|\|\widehat{C}_j\|\right)\mathbf{u}+O(\mathbf{u}^2),\) (4.7)

where we have for all \(1\le j\le p\)

\(|\widehat{\alpha}_j|\|\widehat{C}_j\|\le(|\alpha_j|+|\widehat{\alpha}_j-\alpha_j|)\left(\|\widetilde{C}_j\|+\|\widehat{C}_j-\widetilde{C}_j\|\right)\le|\alpha_j|(1+\delta_1)\left(\|\widetilde{C}_j\|+\|\widehat{C}_j-\widetilde{C}_j\|\right).\) (4.8)

