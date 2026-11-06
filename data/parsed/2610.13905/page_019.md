### 3.2.3 Sparsifying Algorithms Obtained by Term Deletion

We close this subsection by considering the sparsification of the APA algorithms obtained from the search procedure discussed in Section 2. These algorithms have special structure: their parameter dependence comes from a De-Groote transformation applied to an exact decomposition. As a result, verified below, we can always construct alternative bases whose corresponding encoding matrices \(U_\phi\), \(V_\psi\), and \(W_\nu\) are independent of \(\varepsilon\). Moreover, this does not come at the expense of sparsity (again, as measured by weight\((\cdot)\)).

**Proposition 3.4.** _Let_ \(U(\varepsilon)\), \(V(\varepsilon)\)_, and_ \(W(\varepsilon)\) _be obtained from an exact algorithm as in Section 2. Consider any invertible, symbolic alternative-basis transformations_ \(\phi_\varepsilon\), \(\psi_\varepsilon\)_, and_ \(\nu_\varepsilon\) _for which the encoding matrices_

\(U_\phi(\varepsilon)=\phi_\varepsilon^{-1}\cdot U(\varepsilon),V_\psi(\varepsilon)=\psi_\varepsilon^{-1}\cdot V(\varepsilon),W_\nu(\varepsilon)=\nu_\varepsilon\cdot W(\varepsilon)\)

_have Laurent-polynomial entries. The following hold:_

1. _There are equivalent alternative-basis transformations_ \(\tilde{\phi}_\varepsilon\), \(\tilde{\psi}_\varepsilon\)_, and_ \(\tilde{\nu}_\varepsilon\) _for which_ \(U_\tilde{\phi}(\varepsilon)\), \(V_\tilde{\psi}(\varepsilon)\)_, and_ \(W_\tilde{\nu}(\varepsilon)\) _are constant. The maps_ \(\tilde{\phi}_\varepsilon^{-1}\), \(\tilde{\psi}_\varepsilon^{-1}\)_, and_ \(\tilde{\nu}_\varepsilon\) _have Laurent-polynomial entries._<tbc>

_2._ _If the parameter p in_ (3.4) _satisfies_ \(p\ge 1\)_, the weight of each constant encoding matrix is no greater than that of its original counterpart._

_Proof._ We prove both claims for \(U(\varepsilon)\). Let _U_ be the encoding matrix of the parent decomposition after the selected terms have been deleted. With the row-wise vectorization used here, set \(D_\varepsilon=R^{-1}\otimes S^T\), where _R_ and _S_ are the De-Groote transformations from Section 2. Then \(U(\varepsilon)=D_\varepsilon U\), and \(D_\varepsilon\) and \(D_\varepsilon^{-1}\) have Laurent-polynomial entries. Set<tbc>

\(G_\varepsilon=\phi_\varepsilon^{-1}D_\varepsilon.\) (3.20)

<tbc>Because the coefficient field is infinite and \(G_\varepsilon\) is invertible over \(\mathbb{C}(\varepsilon)\), we can choose a nonzero \(\varepsilon_0\) at which \(G_{\varepsilon_0}\) is defined and invertible. Define<tbc>

\(\tilde{\phi}_\varepsilon^{-1}=G_{\varepsilon_0}D_\varepsilon^{-1}.\) (3.21)

<tbc>This map has Laurent-polynomial entries, and

\(U_\tilde{\phi}(\varepsilon)=\tilde{\phi}_\varepsilon^{-1}U(\varepsilon)=G_{\varepsilon_0}U\) (3.22)

is constant. Moreover, \(U_\tilde{\phi}(\varepsilon)\) is obtained by evaluating \(U_\phi(\varepsilon)=G_\varepsilon U\) at \(\varepsilon_0\). Hence, every constant entry retains its value, and every nonconstant entry becomes a constant. This implies that the weight cannot increase. For \(V(\varepsilon)\) and \(W(\varepsilon)\), the proof is the same, using \(\psi_\varepsilon^{-1}\) and \(\nu_\varepsilon\), respectively, as the maps that produce their encoding matrices.

The benefit of sparsifying this way (when possible) is straightforward: if \(U_\phi\), \(V_\psi\), and \(W_\nu\) have no \(\varepsilon\) dependence, then we can perform the approximate-to-exact procedure of Bini \[9\] by applying several basis transformations in parallel before evaluating the bilinear algorithm corresponding to \(U_\phi\), \(V_\psi\), and \(W_\nu\) in a batched fashion.

## 3.3 Results

To evaluate the arithmetic complexity of the resulting algorithms, we compute the leading coefficients using the framework of \[32\]. For each sparsified algorithm, we first compute the base-case linear-operation counts _q<sub>U</sub>_, _q<sub>V</sub>_, and _q<sub>W</sub>_ of its encoding and decoding matrices. In the APA setting, these counts are evaluated symbolically in \(\varepsilon\), and we use _p_=2 for the weight calculation in (3.4). We then apply the recursion-order optimization of \[32\], which uses dynamic programming to evaluate recursive compositions of the algorithm and its permutations for square matrix multiplication. Among the resulting recursion orders, we report the minimum leading coefficient returned by this procedure. An example is given in Section B.3.

The sparsification results recorded in  2 were obtained on a laptop with an Intel Core Ultra 9. Most encoding matrices could be successfully sparsified after running Algorithm 3 for less than an hour. Only three required a run time of more than a day: two completed in two days and the last in three. While, in general, larger matrices took longer to sparsify, this is not the only factor determining the run time of Algorithm 3. In fact, it seems that the complexity of the matrix entries matter more than the size of the matrix.

