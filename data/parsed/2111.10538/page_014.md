Since \(\epsilon\) is very small and all the multiplicative loss factors are constant, we can assume that all the above errors amount to an overall 1_/c_ for a **constant** factor _c_. Now we are ready to discuss the loss in the approximation incurred in Step 1. If Step 1 did not incur any error, we would find a solution of size \(1/c\lambda n\) for the two strings. Suppose that \((w_1,w'_1),(w_2,w'_2),\dots\) is a such a window- compatible solution that provides a solution of total size \(1/c\lambda n\) if the estimations were correct. We put these pairs in two sets based on whether the _A_ side window is larger or the _B_ side window is larger. At least one set gives us a solution of size \(1/(2c)\lambda n\). Without loss of generality, we assume that these are the pairs whose _B_ side is at least as large as their _A_ side and in the rest of the proof we restrict ourselves to such pairs.

For each pair \((w_i,w'_i)\), define \(\lambda_i\) to be the ratio of the actual LCS of _w<sub>i</sub>_ and \(w'_i\) divided by \(|w'_i|\). Since \(\sum|w'_i|\le n\) and \(\sum\lambda_i|w'_i|\ge 1/(2c)\lambda n\) then it follows from Lemma A.7 that

\(\sum|w'_i|\lambda_i^4\ge(\frac{1/(2c)n\lambda}{\sum|w'_i|})^4\sum|w'_i|=(1/(2c)\lambda)^4n(n/\sum|w'_i|)^3\ge(1/(2c)\lambda)^4n,\)

and therefore \(\sum|w'_i|\lambda_i^4/16\ge\frac{\lambda^4n}{256c^4}=\Omega(\lambda^4n)\). Thus, via the estimations we find in Step 1, we would be able to find a solution that loses a factor of at most \(\Omega(\lambda^3)\).

**Runtime:** The runtime of Step 0 is \(\widetilde{O}(k)=\widetilde{O}(\sqrt{n}/\lambda)=\widetilde{O}(n^{71/140})\) which is negligible. By Theorem 3.21, the runtime of Step 1 is equal to<tbc>

\(\widetilde{O}(k^{1+\gamma}\mathsf{w}_\mathsf{max}^2+k^{2+\gamma}\mathsf{w}_\mathsf{max})\le\widetilde{O}(n^{1+71/140(5/3)}+n^{1/2+71/140(8/3)})\le\widetilde{O}(n^{1.86}).\)

<tbc>Moreover, the number of remaining edges in the graph is bounded by (see Theorem 3.21)<tbc>

\(\widetilde{O}(k^{2-\gamma}/\lambda)\le\widetilde{O}(k^{2-2/3+1/70})\simeq\widetilde{O}(k^{1.35}).\)

<tbc>This implies a runtime of (see Theorem 5.2)

\(\widetilde{O}(k^{2-(2-1.35)/2}\mathsf{w}_\mathsf{max}^2/\lambda^6)=\widetilde{O}(k^{1.675}\mathsf{w}_\mathsf{max}^2/\lambda^6)\le\widetilde{O}(n^{1+6/140+71/140(1.675)})\le\widetilde{O}(n^{1.9})\)

for Step 2.

**Theorem 2.2.** _Given strings A,B of length_ |_A_|=|_B_|=_n with_ ||lcs(_A,B_)||=\(\lambda\) _where_ \(\lambda\) _is constant, we can approximate the length of the LCS between the two strings within a factor_ \((1-\epsilon)\lambda^2\) _in_ \(n^{2-\Omega_{\epsilon\lambda}(1)}\) _time for any constant_ \(0<\epsilon<1\).

_Proof._ Let \(\epsilon'=\epsilon/200\). Since we do not know the value of \(\lambda\), we start with \(\lambda=1\) and iteratively try to solve the problem within a factor \((1-\epsilon')\lambda^2\). Each time we are not able to find a solution, we multiply the value of \(\lambda\) by \(1-\epsilon'\) and proceed. This imposes a \(1-\epsilon'\) factor to the approximation and a constant factor to the runtime. Thus, in what follows, we assume that we fix a \(\lambda\) and we know that the solution size is at least \(\lambda n\).

We run the three steps of our algorithm (Step 0 stated in Fact 4.3, Step 1 stated in Theorem 3.13, and Step 2 stated in Lemma 5.1) by setting \(d=\sqrt{n}\), \(\mathsf{w}_\mathsf{max}=\sqrt{n}\) and \(k=\widetilde{O}(\sqrt{n})\) (Notice that here \(\lambda\) is constant). After constructing the windows in Step 0 (Fact 4.3), we run the algorithm of Theorem 3.13 (Step 1) for every \(\lambda'\in\{\epsilon\lambda,\epsilon(1+\epsilon')\lambda,\epsilon(1+\epsilon')^2\lambda,\dots,1\}\). If for a pair of windows _w<sub>i</sub>,w<sub>j</sub>_ our algorithm in Step 1 detects an edge at \(\lambda'\) then we update the solution size for such a pair to \(\sqrt{|w_i||w_j|(1-\epsilon')\lambda'^3}\). We then run the algorithm of Step 2 (Lemma 5.1) to find a solution. In what follows, we bound the approximation factor and the runtime of the algorithm.

**Approximation factor:** For now, we only consider the multiplicative and additive approximation losses that are incurred in Steps 0, 1, and 2 but we assume that for each \(\lambda\), the output of Step 1 is without any errors. We then incorporate those errors to bound the overall approximation factor. These errors are listed below:

