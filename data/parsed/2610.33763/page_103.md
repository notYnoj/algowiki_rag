**Theorem 7.5** _With_ \(A_\widetilde{\mathbf{N}}\) _as in_ (7.18) _and_ \(P_\widetilde{\mathbf{N}}\) _as in_ (7.22)_, it holds_<tbc>

\(\{P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_{\mathrm{GLT},\sigma} 1.\)

<tbc>_Moreover,_<tbc>

\(\{P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_\lambda 1.\)

<tbc>**Proof:** Define \(R_\widetilde{\mathbf{N}}:=A_\widetilde{\mathbf{N}}-P_\widetilde{\mathbf{N}}\). Then,<tbc>

\(P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}}=I_\widetilde{\mathbf{N}}+P_\widetilde{\mathbf{N}}^{-1}R_\widetilde{\mathbf{N}}.\)

<tbc>Since \(\mathrm{rank}R_\widetilde{\mathbf{N}}\le\nu(\mathbf{n})\), it follows that \(\mathrm{rank}(P_\widetilde{\mathbf{N}}^{-1}R_\widetilde{\mathbf{N}})\le\nu(\mathbf{n})=o(\widetilde{\mathbf{N}})\) as \(m,\mathbf{n}\rightarrow\infty\). By Theorem 4.1, the sequence \(\{P_\widetilde{\mathbf{N}}^{-1}R_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\) is zero-distributed; therefore, by GLT 2, it follows that<tbc>

\(\{P_\widetilde{\mathbf{N}}^{-1}R_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_\mathrm{GLT}0.\)

<tbc>Hence, by exploiting part 2 of axiom GLT 3 and by the fact that \(\{I_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_\mathrm{GLT}1\), we infer<tbc>

\(\{P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_\mathrm{GLT}1.\)

<tbc>Thus, by GLT 1, we immediately obtain<tbc>

\(\{P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\sim_\sigma 1.\)

<tbc>Turning to the eigenvalue distribution, we observe that<tbc>

\(\lambda_n(P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}})=1+\lambda_n(P_\widetilde{\mathbf{N}}^{-1}R_\widetilde{\mathbf{N}}),n=1,\dots,\widetilde{\mathbf{N}},\)

<tbc>therefore

\(\#\left\{n=1,\dots,\widetilde{\mathbf{N}}:\lambda_n(P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}})\neq 1\right\}\le\mathbf{n}=o(\widetilde{\mathbf{N}}).\)

Thus, the eigenvalues of \(\{P_\widetilde{\mathbf{N}}^{-1}A_\widetilde{\mathbf{N}}\}_\widetilde{\mathbf{N}}\) are weakly clustered at 1 in the sense of Definition 2.2, which, by Remark 2.1, is equivalent to saying that the sequence is spectrally distributed as 1.

**Remark 7.2** _We emphasize that the given sequence of theoretical steps for studying the distribution and clustering in the eigenvalue and singular value sense can be adapted with little effort to a great variety of different situations. Here we mention two of them, one concerning a generalization of problem_ (7.1) _and one regarding other classes of discretizations for the regularized FDEs in_ (7.2).

1. _If the square_ \([0,1]\times[0,1]\) _is replaced by a bounded_ \(\Omega\subset\mathbb{R}^2\)_, with_ \(\Omega\) _simply Peano-Jordan measurable, then the domain_ \(\Omega_T\) _in_ (7.1)-(7.2) _is replaced by_ \(\Omega\times(0,T)\)_. Hence, simply adapting the steps in Section 7.2 and Section 7.3, the same conclusions are obtained, using the reduced GLT theory \[8\] in place of the classical one; for the reduced GLT theory refer to \[124\]\[pp. 395-399\] and \[125\]\[Section 3.1.4\] for an example, the initial proposal, the related terminology, and \[8\] for a complete theoretical development._<tbc>

