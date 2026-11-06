## 2 Organization of the Paper

Our algorithm for LCS is explained in Section 4 (Step 0), Section 3 (Step 1), and Section 5 (Step 2).

In both our results for LCS and LIS, we assume that the goal is to find approximate solutions, provided that the solution size is at least \(\lambda_0n\). After the algorithms terminate, if the output is smaller than what we expect, we realize that the solution is smaller than \(\lambda_0n\). Therefore, we begin by setting \(\lambda_0=1\) and iteratively multiply \(\lambda_0\) by a \(1-\epsilon\) factor until we obtain a solution. This only adds a multiplicative factor of \(\mathrm{log}1/\lambda\) to the running time and a multiplicative factor of \(1-\epsilon\) to the approximation. Since we present two different sparsification techniques, we obtain two theorems: one is Theorem 2.1 and the other is Theorem 2.2.

**Theorem 2.1.** _Given strings A,B of length_ |_A_|=|_B_|=_n with_ ||lcs(_A,B_)||=\(\lambda\)_, we can approxi mate the length of the LCS between the two strings within a factor_ \(\Omega(\lambda^3)\) _in time_ \(\widetilde{O}(n^{39/20})\).

_Proof._ Fix a sufficiently small constant \(\epsilon\) (e.g. \(\epsilon=1/10000\)). Since we do not know the value of \(\lambda\), we start with \(\lambda=1\) and iteratively try to solve the problem within a factor \(\Omega(\lambda^3)\). Each time we are not able to find a solution, we multiply the value of \(\lambda\) by \(1-\epsilon\) and proceed. This imposes a \(1-\epsilon\) factor to the approximation and a logarithmic factor to the runtime that can be hidden in the \(\widetilde{O}\) and \(\Omega\) notations. Thus, in what follows, we assume that we fix a \(\lambda\) and we know that the solution size is \(\lambda n\). Also, we define \(\kappa=n^{-1/140}\).

If \(\lambda\le\kappa\) we run the following algorithm: we choose \(n\lambda^3\) characters of _A_ uniformly at random to obtain a string \(A'\). With high probability, the LCS of \(A'\) and _B_ is at least \((1-\epsilon)\lambda^4n\). Therefore, we set our aim to find such a solution. To this end, we spend a preprocessing time of _O(n_log_n_) on string _B_ and then we will be able to find such a solution in time \(O(|A'|\lambda^4n\mathrm{log}n)\) (see Theorem A.8). Thus, the overall runtime would be bounded by

\(\widetilde{O}(|A'|\lambda^4n)\le\widetilde{O}(n\lambda^7n)\le\widetilde{O}(n^{2-7/140})=\widetilde{O}(n^{39/20}).\)

Moreover, the approximation factor is also \(\Omega(\lambda^3)\) as desired.

When \(\lambda\ge\kappa\) we run the three steps of our algorithm (Step 0 stated in Fact 4.6, Step 1 stated in Theorem 3.21, and Step 2 stated in Lemma 5.1) by setting \(d=\sqrt{n}\lambda\), \(\gamma=2/3\), \(\mathsf{w}_\mathsf{max}=\sqrt{n}\) and \(k=\widetilde{O}(\sqrt{n}/\lambda)\le\widetilde{O}(n^{71/140})\). After constructing the windows in Step 0 (Fact 4.6), we run the algorithm of Theorem 3.21 (Step 1) for every \(\lambda'\in\{\epsilon\lambda,\epsilon(1+\epsilon)\lambda,\epsilon(1+\epsilon)^2\lambda,\dots,1\}\). If for a pair of windows _w<sub>i</sub>,w<sub>j</sub>_ our algorithm in Step 1 detects an edge at \(\lambda'\) then we update the solution size for such a pair to \(\mathrm{max}\{|w_i|,|w_j|\}\lambda'^4/16\). We then run the algorithm of Step 2 (Lemma 5.1) to find a solution. In what follows, we bound the approximation factor and the runtime of the algorithm.

**Approximation factor:** For now, we only consider the multiplicative and additive approximation losses that are incurred in Steps 0, 1, and 2 but we assume that for each \(\lambda\), the output of Step 1 is without any errors. We then incorporate those errors to bound the overall approximation factor. These errors are listed below:

• We lose a multiplicative constant factor in Step 0 followed by an additive error of \(\epsilon\lambda n\) (see Lemma 4.7).<tbc>

• We lose a multiplicative factor \(1-2\epsilon\) in Step 1 due to the fact that we ignore window pairs whose LCS sizes drops below a threshold \(\epsilon\lambda\) times the maximum window size.<tbc>

• We also lose a multiplicative factor \(1-\epsilon\) in Step 3 (Lemma 5.1).<tbc>

