The fractional accuracy relative to the exact eigenvalues is better than 10<sup>-4</sup> for terrestrial energies and both orderings \[43, 44\], as in  3. A single Newton-Raphson correction,

\(\lambda_3\rightarrow\lambda_3-\frac{X(\lambda_3)}{X'(\lambda_3)},X(\lambda)=\lambda^3-A\lambda^2+B\lambda-C,\) (18)

improves the fractional precision by several orders of magnitude \[44\].

## 5.3 Eigenvectors via the Adjugate Method

Once the eigenvalues \(\lambda_i\) are known, the squared elements of the eigenvector matrix _V<sub>e</sub>_ follow from the adjugate of \((\lambda I-H_\mathrm{f})\), as developed by Abdullahi and Parke \[27\]:

\(|V_{e\alpha i}|^2=\frac{\lambda_i^2-S_{\alpha\alpha}\lambda_i+T_{\alpha\alpha}}{\Delta\lambda_{ij}\Delta\lambda_{ik}},\) (19)

where \(j,k\neq i\) and

\(S_{\alpha\alpha}=A-(2E)H_{f\alpha\alpha},\) (20)

\(T_{\alpha\alpha}=(2E)^2[\mathrm{Adj}(H_\mathrm{f})]_{\alpha\alpha}.\) (21)

The numerator quantities \(S_{\alpha\alpha}\) and \(T_{\alpha\alpha}\) are the diagonal elements of the adjugate of (2_EH_<sub>f</sub>); Eq. (19) is thus the adjugate formula of \[27\]. The closely related eigenvector- eigenvalue identity of Denton, Parke, Tao, and Zhang \[28\] expresses the same moduli through products of eigenvalue differences for sub-matrices; we use the adjugate form because Adj(_H_<sub>f</sub>) is already available from the Le Verrier-Faddeev coefficients of Section 4.2.

\begin{tabular}{ccc}
Expression & Order & \(|\Delta P|/P\) \\
Madrid \[49\] & \(\mathcal{O}(\epsilon,\alpha)\) & ∼10<sup>-2</sup> \\
AJLOS \[45\] & \(\mathcal{O}(\epsilon,\alpha)\) & ∼10<sup>-2</sup> \\
Freund \[50\] & \(\mathcal{O}(\epsilon)\) & ∼10<sup>-2</sup> \\
AKT \[51\] & \(\mathcal{O}(\epsilon,\alpha,a)\) & ∼10<sup>-3</sup> \\
MP \[46\] & \(\mathcal{O}(\alpha)\) & ∼10<sup>-2</sup> \\
DMP0 \[47\] & \(\mathcal{O}(\epsilon_0)\) & ∼10<sup>-3</sup> \\
DMP1 \[47\] & \(\mathcal{O}(\epsilon_0^2)\) & ∼10<sup>-5</sup> \\
AM5/2 \[52\] & \(\mathcal{O}(s_{13}^{5/2})\) & ∼10<sup>-3</sup> \\
NuFast(0) \[44\] & exact +0NR & ∼10<sup>-4</sup> \\
NuFast(1) \[44\] & exact +1NR & ∼10<sup>-9</sup> \\
Exact (ZS) \[21\] & -- & 0 (ref.) \\
\end{tabular}

3: Fractional eigenvalue/probability accuracy \(|\Delta P|/P\) at the first oscillation maximum for the DUNE configuration (_L_=1300km, \(\rho=2.84\mathrm{g}\mathrm{cm}^{-3}\)). Accuracy figures and the cross-scheme comparison are taken from \[43, 47, 44\]; the perturbative expressions are reproduced here as theoretical anchors and were not independently benchmarked for speed. As emphasized in \[44\], NuFast-LBL is both faster and more accurate than the pre-NuFast schemes; speed is therefore not compared in a common column.

