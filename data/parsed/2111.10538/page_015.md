• We lose an additive error of \(8\epsilon'\lambda n\) in Step 0 (see Lemma 4.4).<tbc>

• We lose a multiplicative factor \(1-\epsilon'\) in Step 1 due to the fact that we ignore window pairs whose normalized LCS sizes drops below a threshold \(\epsilon'\lambda\).<tbc>

• We also lose a multiplicative factor \(1-\epsilon'\) in Step 3 (Lemma 5.1).

Since \(\epsilon'=\epsilon/200<1/200\), we can assume that all the above errors amount to an overall \(1-20\epsilon'\) factor. Now we are ready to discuss the loss in the approximation incurred in Step 1. If Step 1 did not incur any error, we would find a solution of size \((1-20\epsilon')\lambda n\) for the two strings. Suppose that \((w_1,w'_1),(w_2,w'_2),\dots\) is a such a window-compatible solution that provides a solution of total size \((1-20\epsilon')\lambda n\) if the estimations were correct. For each pair \((w_i,w'_i)\), define \(\lambda_i\) to be \(||\mathsf{LCS}(w_i,w'_i)||\). Since \(\sum|w_i|\le n\), \(\sum|w'_i|\le n\) and \(\sum\lambda_i\sqrt{|w_i|\cdot|w'_i|}\ge(1-20\epsilon')\lambda n\), it follows from Lemma A.7 and Cauchy-Schwarz inequality that

\(\sum\sqrt{|w_i|\cdot|w'_i|}(1-\epsilon')\lambda_i^3\ge(1-\epsilon')\sum\sqrt{|w_i|\cdot|w'_i|}\left(\frac{\sum\lambda_i\sqrt{|w_i|\cdot|w'_i|}}{\sum\sqrt{|w_i|\cdot|w'_i|}}\right)^3\)<br>
\(\ge(1-\epsilon')\frac{((1-20\epsilon')\lambda n)^3}{\left(\sum\sqrt{|w_i|\cdot|w'_i|}\right)^2}\)<br>
\(\ge(1-\epsilon')\frac{((1-20\epsilon')\lambda n)^3}{n^2}\)<br>
\(\ge(1-\epsilon')(1-20\epsilon')^3\lambda^3n\)<br>
\(\ge(1-\epsilon')(1-60\epsilon')\lambda^3n.\)

Thus, via the estimations we find in Step 1, we would be able to find a solution that loses a factor of at most \((1-\epsilon')(1-60\epsilon')\lambda^3\ge(1-\epsilon)\lambda^3\).

**Runtime:** The runtime of Step 0 is \(\widetilde{O}(k)=\widetilde{O}(\sqrt{n})\) which is negligible. By Theorem 3.13 and setting \(\gamma=1/10\), the runtime of Step 1 is equal to<tbc>

\(\widetilde{O}(\mathsf{w}_\mathsf{max}^2k^{1.1}+\mathsf{w}_\mathsf{max}k^{2.2})=\widetilde{O}(n^{1.6}).\)

<tbc>Moreover, the number of remaining edges in the graph is bounded by (see Theorem 3.13)<tbc>

\(\widetilde{O}(k^{2-\epsilon\lambda^3/(800\mathsf{w}_\mathsf{layers}\mathsf{w}_\mathsf{gap})})=\widetilde{O}(k^{2-\Omega(\epsilon\lambda^6/log(1/\lambda))})=\widetilde{O}(k^{2-\Omega(\epsilon\lambda^7)})\)

<tbc>This implies a runtime of (see Theorem 5.3)

\(\widetilde{O}(k^{2-\Omega(\epsilon\lambda^7)}\mathsf{w}_\mathsf{max}^2/\lambda^6)=\widetilde{O}(n^{2-\Omega(\epsilon\lambda^7/2)})=n^{2-\Omega_{\lambda,\epsilon}(1)}\)

for Step 2.

As an immediate corollary of Theorem 2.1, we present an algorithm that beats the \(1/|\Sigma|\) approximation factor in truly subquadratic time, when the strings are balanced.

**Corollary 2.3.** _Given a pair of strings_ (_A,B_) _of length n over alphabet_ \(\Sigma\) _that satisfy the balance condition, we can approximate their LCS within an_ \(O(|\Sigma|^{3/4})\) _factor in time O(n_<sup>39/20</sup>).

