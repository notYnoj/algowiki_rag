To apply this matrix bound to every admissible algorithm, we express its success in the feature coordinates. This is the one-query case of the semidefinite characterization of quantum query algorithms \[31\]. Fix the private randomness of an algorithm, purify it, and absorb the processing after the call into the final measurement. Measurements before the call are input independent and can be deferred. Write the state before the call as \(\sum_{i,j}|i,j\rangle\big(|+\rangle|u_{ij}\rangle+|-\rangle|v_{ij}\rangle\big)+|\chi\rangle\), where \(|\chi\rangle\) is the component of branches that skip the call, flagged in the workspace. In the eigenbasis of the response bit the call fixes the + sector, multiplies the - sector at (_i,j_) with _i\<j_ by sgn(_x<sub>i</sub>-x<sub>j</sub>_), multiplies the reversed pair by the opposite sign, and fixes self-addresses. The state after the call is therefore \(|\Psi_x\rangle=\sum_\mu(\phi_x)_\mu|a_\mu\rangle\), where \((\phi_x)_\mu\) are the coordinates of \(\phi_x\) and<tbc>

\(|a_0\rangle=|\chi\rangle+\sum_{i,j}|i,j,+\rangle|u_{ij}\rangle+\sum_i|i,i,-\rangle|v_{ii}\rangle,|a_{ij}\rangle=|i,j,-\rangle|v_{ij}\rangle-|j,i,-\rangle|v_{ji}\rangle(i<j).\)

<tbc>These vectors have disjoint supports on the flag, address and response registers, so they are orthogonal, and \(\sum_\mu\|a_\mu\|^2=1\). For the output measurement \(\{\widetilde{E}_i\}\) put \((B_i)_{\mu\mu^\prime}=\langle a_\mu|\widetilde{E}_i|a_{\mu^\prime}\rangle\) and \(\lambda_\mu=\|a_\mu\|^2\). Then \(B_i\unknown 0\), \(\sum_iB_i=\mathrm{diag}(\lambda)\) and \(\sum_\mu\lambda_\mu=1\). The matrices _B<sub>i</sub>_ may be complex Hermitian, and since _M<sub>i</sub>_ is real only their real parts contribute to the success. The average success is

\(\sum_i\mathrm{tr}(M_iB_i)\le\sum_i\mathrm{tr}(\mathcal{L}B_i)=\mathrm{tr}(\mathcal{L}\mathrm{diag}(\lambda))=Q.\)

The worst-case success is at most the average, so \(Q_1(n,r)\le Q\).

## A.4 Attainment

The attaining construction uses the kernels of the slack blocks in the upper-bound proof. We give the initial state and measurement, then verify that the measurement is complete and that the success probability equals the bound for every order.

Let \(N=\genfrac(){pt}{2}{n}{2}=nm/2\), \(\alpha=2mR/(n\zeta^2+2mR)\) and \(\beta=(1-\alpha)/N\). Prepare<tbc>

\(|\psi_\mathrm{in}\rangle=\sqrt{\alpha}|1,1,+\rangle+\sqrt{\beta}\sum_{i<j}|i,j,-\rangle.\)

<tbc>One call gives \(|\psi_x\rangle=C_\alpha\phi_x\) with \(C_\alpha=\sqrt{\alpha}P_0+\sqrt{\beta}(P_V+P_C)\), in the encoding \(|0\rangle=|1,1,+\rangle\) and \(|ij\rangle=|i,j,-\rangle\). In the decomposition (13) define the seed effect

\(E_1=\frac{1}{n}\left(\begin{array}{ c c }
1 & -\sqrt{mR} \\
-\sqrt{mR} & mR
\end{array}\right)\oplus\oplus_{a=1}^k\frac{m}{2n}\left(\begin{array}{ c c }
\gamma^2 & \gamma \\
\gamma & 1
\end{array}\right)\oplus 0,\)

and \(E_i=U_\sigma E_1U_\sigma^\mathsf{T}\) for any permutation \(\sigma\) with \(\sigma(1)=i\), where \(U_\sigma\) fixes \(|0\rangle\) and relabels the oriented edges. The seed is invariant under the stabilizer of label 1, so _E<sub>i</sub>_ is well defined. Its traces on the global sectors are 1_/n_, \(mR/n+km\gamma^2/(2n)=m/n\) and _mk/_(2_n_). A label- invariant symmetric matrix on the edge space is a combination of _I_ and \(D_n^\mathsf{T}D_n\), which act as scalars on V and C, and there is no invariant coupling between \(|0\rangle\) and the edges. Since \(\sum_iE_i\) is invariant and its sector traces equal the sector dimensions, \(\sum_iE_i=I\). On the full query space the effects are completed by adding _n_<sup>-1</sup> times the projector onto the complement of the encoded subspace, which the prepared states never reach.

