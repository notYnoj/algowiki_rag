_Proof._ Since _A_ and _B_ are balanced, there is a character \(\sigma\in\Sigma\) that appears at least \(n/|\Sigma|\) times in both strings. Indeed, finding a solution of size \(n/|\Sigma|\) by restricting our attention to only character \(\sigma\) can be done in time _O(n_). If \(\mathsf{lcs}(A,B)\le n/|\Sigma|^{1/4}\) this already gives us an \(O(|\Sigma|^{3/4})\) approximate solution. Otherwise, \(||\mathsf{lcs}(A,B)||>1/|\Sigma|^{1/4}\) and the approximation factor of our \(\Omega(\lambda^3)\)-approximation algorithm would be bounded by \(O(|\Sigma|^{3/4})\).

Finally, we bring our results for LIS in Section 6. We show that

**Theorem 2.4.** _Given a length-n sequence A with_ \(\mathsf{lis}(A)=n\lambda\)_. We can approximate the length of the LIS within a factor of_ \(\Omega(\lambda^3)\) _in time_ \(\widetilde{O}(n^{17/20})\).

_Proof._ If \(\lambda<n^{-1/20}\) we sample the array with a rate of _n_<sup>-3/20</sup> and compute the LIS for the sampled array. The running time of the algorithm is \(\widetilde{O}(n^{17/20})\). The approximation factor is \(O(n^{-3/20})\ge\Omega(\lambda^3)\). Otherwise, by Theorem 6.8, we estimate the size of LIS up to an \(\Omega(\lambda^3)\) approximation factor in time \(\widetilde{\Omega}(\lambda^{-7}\sqrt{n})\le\widetilde{O}(n^{17/20})\).

