**Algorithm 12** Recursive Estimate LIS

procedure RecursiveLIS\((A,\lambda,\ell,r)\triangleright\) Lemma 6.11<br>
   \(\triangleright\) input: sequence A, parameter \(\lambda\), domain interval \([\ell,r]\)<br>
   \(\triangleright\) assume \(\mathsf{sa}_1,\mathsf{sa}_2,\dots,\mathsf{sa}_{n^\kappa}\) are subarrays of A<br>
   if the length of A is greater than \(n^{2\kappa}\) then<br>
   return RecursiveLISWithOracle(RecursiveLIS,\(A,\lambda,\ell,r)\) with \(\zeta=n^\kappa\)<br>
   else<br>
   for \(i\in[n^\kappa]\) do<br>
   \(\mathsf{cdi}_i\leftarrow\) ConstructCandidateDomains(sa<sub>i</sub>)<br>
   discard all the intervals which are not in \([\ell,r]\) from cdi<sub>i</sub><br>
   end for<br>
   \(\{\mathsf{ps}_1,\dots,\mathsf{ps}_t\}\leftarrow\) ConstructPseudoSutions(cdi<sub>1</sub>,...,cdi<sub>n<sup>\kappa</sup></sub>)<br>
   if EvaluatePseudoSutions\((\mathsf{ps}_1,\dots,\mathsf{ps}_t)\ge\lambda|A|\) then<br>
   return<br>
accept<br>
   else<br>
   return<br>
repeat<br>
   end if<br>
   end if<br>
end procedure

We show that Algorithm 12 is \(h_i(\lambda)\)-approximate if the length of the input sequence is \(n^{i\cdot\kappa}\).

If the length of input sequence is \(n^{2\kappa}\), then \(h_2(\lambda)=\frac{\lambda^4}{2^{32}}\). By Corollary 6.2, Lemma 6.4, and Lemma 6.6, Algorithm 12 is \(h_2(\lambda)\)-approximate.

In the induction step, for an integer \(2\le i<1/\kappa\), we assume Algorithm 12 is \(h_i(\lambda)\)-approximate for input instance of length \(n^{i\cdot\kappa}\). By Lemma 6.9, Algorithm 12 is \(\left(h_i\left(\frac{\lambda^4}{2^{32}}\right)\frac{\lambda^4}{2^{33}}\right)\)-approximate for input instance of length \(n^{(i+1)\cdot\kappa}\). Since

\(h_i\left(\frac{\lambda^4}{2^{32}}\right)\frac{\lambda^4}{2^{33}}=\frac{\lambda^{4\cdot(2\cdot 4^{(i-1)}-4)}\cdot\lambda^4}{256^{4\cdot(2\cdot 4^{(i-1)}-4)}\cdot 256^{2\cdot 4^{(i-1)}+3\cdot 4^{(i-2)}-7}\cdot 2^{33}}\)<br>
\(=\frac{\lambda^{2\cdot 4^i-12}}{256^{2\cdot 4^i+2\cdot 4^{(i-1)}+3\cdot 4^{(i-2)}-18.875}}\)<br>
\(>\frac{\lambda^{2\cdot 4^i-4}}{256^{2\cdot 4^i+3\cdot 4^{(i-1)}-7}}\)<br>
\(=h_{i+1}(\lambda),\)

by Fact 6.10, Algorithm 12 is \(h_{i+1}(\lambda)\)-approximate for input instance of length \(n^{(i+1)\cdot\kappa}\). Since

\(h_{1/\kappa}(\lambda)>\frac{\lambda^{2\cdot 4^{((1/\kappa)-1)}}}{256^{3\cdot 4^{((1/\kappa)-1)}}},\)

by Fact 6.10, Algorithm 12 is \(\left(\frac{\lambda^{2\cdot 4^{((1/\kappa)-1)}}}{256^{3\cdot 4^{((1/\kappa)-1)}}}\right)\)-approximate for input instance of length _n_.

By Corollary 6.2, Lemma 6.4, Lemma 6.6 and Lemma 6.9, we have the desired running time. The success probability is obtained by same corollaries/lemmas and union bound.

Finally, by starting with \(\lambda=1\) and iteratively multiplying \(\lambda\) by a \(1/(1+\epsilon)\) factor until a solution is found, we can approximate lis(_A_) within an approximation factor of \(\lambda^{O(4^{1/\kappa})}\).

