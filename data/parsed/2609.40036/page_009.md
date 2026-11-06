_Proof._ We first derive the error-space representation of satisfaction for arbitrary fixed targets and amplitudes. Define

\(\mathsf{S}:=\sum_\mathbf{x}s(\mathbf{x})|\mathbf{x}\rangle\langle\mathbf{x}|,\mathsf{S}_\mathrm{err}:=\sum_{i=1}^m\Pi_i,\Pi_i:=\sum_{t\in C_i}|t\rangle\langle t|,\) (22)

where \(\Pi_i\) acts on coordinate _i_ of the error register. A tilde denotes conjugation by the Fourier transform on all coordinates. For \(X_\mathbf{z}|\mathbf{x}\rangle=|\mathbf{x}+\mathbf{z}\rangle\), Fourier expansion gives

\(\kappa_i(a):=\frac{1}{q}\sum_{t\in C_i}\chi_q(-at),\) (23)

\(\widetilde{\mathsf{S}}=\sum_{i,a}\kappa_i(a)X_{-a\mathbf{b}_i},\) (24)

\(\widetilde{\mathsf{S}}_\mathrm{err}=\sum_{i,a}\kappa_i(a)X_{-a\mathbf{e}_i}.\) (25)

Here and below, \(i\in[m]\) and \(a\in\unknown_q\) unless otherwise indicated. In particular, \(0\unknown\widetilde{\mathsf{S}}_\mathrm{err}\unknown mI\).

Let V be the shell isometry \(\mathsf{Vw}:=U\sum_kw_k|D_k^m\rangle=|\Gamma\rangle\). The local span of the uniform vector \(|u\rangle=q^{-1/2}\sum_x|x\rangle\) and \(|g_i\rangle=\sum_xg_i(x)|x\rangle\) is invariant under \(\Pi_i\), because both vectors are constant on _C<sub>i</sub>_ and on its complement. Using Eqs. (6) and (13) gives

\(U_i^\dagger\widetilde{\Pi}_iU_i=\left[\begin{array}{ c c }
\rho & \sqrt{\rho(1-\rho)} \\
\sqrt{\rho(1-\rho)} & 1-\rho
\end{array}\right].\) (26)

This matrix is independent of _i_, so its sum over coordinates preserves the symmetric qubit subspace. Thus ranV is invariant under \(\widetilde{\mathsf{S}}_\mathrm{err}\). The restriction \(T_\rho=\mathsf{V}^\dagger\widetilde{\mathsf{S}}_\mathrm{err}\mathsf{V}\) is tridiagonal, with entries

\((T_\rho)_{kk}=m\rho+(1-2\rho)k,(T_\rho)_{k,k+1}=(T_\rho)_{k+1,k}=\sqrt{\rho(1-\rho)(k+1)(m-k)}.\) (27)

Next consider decoding. Let \(\Pi_\mathcal{S}\) project onto the success set from (16), and define

\(Z_\mathbf{C}:=\sum_{\mathbf{y}\in\mathcal{S}}|\phi_\mathbf{C}(\mathbf{y})|^2.\) (28)

For _Z_**<sub>C</sub>**_\>_0, the normalized successful error and output states are

\(|\Gamma_\mathcal{S}\rangle:=Z_\mathbf{C}^{-1/2}\Pi_\mathcal{S}|\Gamma\rangle,\) (29)

\(|\widetilde{P}_\mathcal{S}\rangle:=Z_\mathbf{C}^{-1/2}\sum_{\mathbf{y}\in\mathcal{S}}\phi_\mathbf{C}(\mathbf{y})|B^T\mathbf{y}\rangle,|P_\mathcal{S}\rangle:=(\mathsf{F}_q^\dagger)^{\otimes n}|\widetilde{P}_\mathcal{S}\rangle.\) (30)

Measurement gives \(\unknown[s(\mathbf{X})]=\langle\widetilde{P}_\mathcal{S}|\widetilde{\mathsf{S}}|\widetilde{P}_\mathcal{S}\rangle\).

For \(\mathbf{y}\in\mathcal{S}\), define

\(F_{i,a}(\mathbf{y}):=D(B^T(\mathbf{y}-a\mathbf{e}_i)),\mathcal{S}_{i,a}^c:=\{\mathbf{y}\in\mathcal{S}:\mathbf{y}-a\mathbf{e}_i\in\mathcal{F}\}.\) (31)

Syndrome consistency gives _B<sup>T</sup>F<sub>i,a</sub>_(**y**)=_B<sup>T</sub>_(**y**-_a_**e**_<sub>i</sub>_) and _F_<sub>_i,,-a_</sub>(_F<sub>i,a</sub>_(**y**))=**y**. Thus _F<sub>i,a</sub>_ is a bijection of S, and maps \(\mathcal{S}_{i,a}^c\) bijectively onto \(\mathcal{S}_{i,-a}^c\). Expanding (24), the matrix element for _X_<sub>-_a_**b**_<sub>i</sub>_</sub><tbc>

