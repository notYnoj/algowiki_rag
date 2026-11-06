subsample each window with probability \(p=(10logn)k^{-\eta/2}/\epsilon_\text{nbs}=\widetilde{O}(k^{-\eta/2}/\lambda^4)\). Therefore, the number of sampled windows would be \(\widetilde{O}(k^{1-\eta/2}/\lambda^4)\) with high probability and therefore the runtime for detecting the underestimated pairs of windows would be

\(\widetilde{O}(\mathsf{w}_\text{max}^2k^{2-\eta/2}/\lambda^4).\)

Since the total number of underestimated pairs is bounded by \(k^{2-\eta}\) and we sample the _A_-side windows with probability \(\widetilde{O}(k^{-\eta/2}/\lambda^4)\), the expected number of underestimated pairs we detect in the first step is \(\widetilde{O}(k^{2-3\eta/2}/\lambda^4)\). Moreover, for each underestimated pair of windows that we detect, we recompute the LCS of all the nearby pairs of windows. The number of nearby windows on the _A_-side is \(O(k^{\eta/2}/\lambda)\) and the number of nearby windows on the _B_ side is \(\widetilde{O}(k^{\eta/2}/\lambda)\). This makes a total runtime of \(\widetilde{O}(\mathsf{w}_\text{max}^2k^{2-\eta/2}/\lambda^6)\).

Notice that the runtime of the algorithm is in expectation since it depends on the number of underestimated edges we detect in the sampling phase. To make the runtime fixed, we observe that with probability at least 1/2, the algorithm terminates after \(\widetilde{O}(\mathsf{w}_\text{max}^2k^{2-\eta/2}/\lambda^6)\) operations. Thus, we run the algorithm in parallel 10log_n_ times and report the output of any instance that terminates before \(\widetilde{O}(\mathsf{w}_\text{max}^2k^{2-\eta/2}/\lambda^6)\) operations. This comes with a constant factor overhead in the error rate of the algorithm which remains smaller than 1_/n_<sup>3</sup>.

**Theorem 5.3** (nearby searching for \((1-\epsilon)\lambda^2\) approximation)**.** _Given that the number of underestimated pairs in Step 1 is bounded by_ \(k^{2-\eta}\)_, for an arbitrary small constant_ \(\epsilon>0\)_, Step 2 takes time_ \(\widetilde{O}(\mathsf{w}_\text{max}^2k^{2-\eta/2}/\lambda^6)\) _and has approximation factor_ \(1-\epsilon\) _with probability at least_ 1-1_/n_<sup>3</sup>.

_Proof._ To make sure the multiplicative factor in the approximation remains \(1-\epsilon\), we set \(\epsilon_\text{nbs}=\Theta(\lambda^3)\). Thus, the runtime of the algorithm would be as follows: In the sampling process, we subsample each window with probability \(p=(10logn)k^{-\eta/2}/\epsilon_\text{nbs}=\widetilde{O}(k^{-\eta/2}/\lambda^3)\). Therefore, the number of sampled windows would be \(\widetilde{O}(k^{1-\eta/2}/\lambda^3)\) with high probability and therefore the runtime for detecting the underestimated pairs of windows would be<tbc>

\(\widetilde{O}(\mathsf{w}_\text{max}^2k^{2-\eta/2}/\lambda^3).\)

<tbc>Since the total number of underestimated pairs is bounded by \(k^{2-\eta}\) and we sample the _A_-side windows with probability \(\widetilde{O}(k^{-\eta/2}/\lambda^3)\), the expected number of underestimated pairs we detect is \(\widetilde{O}(k^{2-3\eta/2}/\lambda^3)\). Moreover, for each underestimated pair of windows that we detect, we recompute the LCS of all the nearby pairs of windows. The number of nearby windows on the _A_-side is \(O(k^{\eta/2}/\lambda)\) and the number of nearby windows on the _B_ side is \(\widetilde{O}(k^{\eta/2}/\lambda^2)\). This makes a total runtime of<tbc>

\(\widetilde{O}(\mathsf{w}_\text{max}^2k^{2-\eta/2}/\lambda^6).\)

<tbc>Similar to Theorem 5.2, one can make sure the runtime of the algorithm is

\(\widetilde{O}(\mathsf{w}_\text{max}^2k^{2-\eta/2}/\lambda^6)\)

and the error remains bounded by 1_/n_<sup>3</sup>.

