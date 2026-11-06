kernel is ker L=span{**1**<sub>_N_<sup>3</sup></sub>} with \(\mathbf{1}_{N^3}=\mathbf{1}_N\otimes\mathbf{1}_N\otimes\mathbf{1}_N\). It follows that H is spanned by \((\mathbf{1}_{N^3},\mathbf{0},\mathbf{0})^\top\), \((\mathbf{0},\mathbf{1}_{N^3},\mathbf{0})^\top\), and \((\mathbf{0},\mathbf{0},\mathbf{1}_{N^3})^\top\), which are the vectors \(\{\mathbf{o}_i\}_{i=1}^3\).

To ensure \(\gamma\lambda_1^\mathcal{B}\ge\lambda_m^\mathcal{A}\): if \(\mathbf{k}\neq\mathbf{0}\), Proposition 2.4 reveals \(\lambda_1^\mathcal{B}=\|\mathbf{k}\|_2^2\), the condition is satisfied; if **k**=**0**, the smallest nonzero eigenvalue of \(\mathbf{K}_i^\dagger\mathbf{K}_i\) equals \(\frac{4}{h^2}sin^2(\pi h)\). Since \(\frac{sinx}{x}>sin1\) within the bound \(x=\pi h\in(0,1)\), there holds \(\lambda_1^\mathcal{B}>4\pi^2(sin1)^2\). Thus \(\gamma=max\{1,\lambda_m^\mathcal{A}\}\) is sufficient.

**Remark 2.6.** _Condition_ (2.20) _is reasonable:_ \(|\mathbf{k}_i|\le\pi\) _is satisfied by construction at high symmetry points, as is shown in_ (4.2) _in Section 4;_ \(N>\pi\) _holds for any reasonable grid. Furthermore, in our numerical experiments the desired eigenvalues are such that_ \(\lambda_m^\mathcal{A}<4\pi^2\) _(more precisely, the normalized frequency_ \(\sqrt{\lambda_m^\mathcal{A}}/(2\pi)<1\)_). Thus_ (2.25) _reduces to a more practical formula, where_ \(\gamma\) _is independent of the grid division N:_

\(\gamma=\left\{\begin{array}{ c c }
4\pi^2, & \mathbf{k}=\mathbf{0}or\|\mathbf{k}\|_2>1, \\
4\pi^2\|\mathbf{k}\|_2^{-2}, & \|\mathbf{k}\|_2\in(0,1).
\end{array}\right.\) (2.26)

_We also point out that, for a general coordinate change matrix_ **A**_, the corresponding results of Lemma 2.4 (1), Proposition 2.5 (1) still hold. Meanwhile, the choice of_ \(\gamma\) _in_ (2.26) _for_ **A**=_I_<sub>3</sub> _case is also valid for our numerical examples._

In summary, Proposition 2.5 provides a rigorous justification for our kernel compensation formulation (2.13). It proves that for any nonzero **k**, the null space H is completely eliminated. When **k**=**0**, H is reduced to a three-dimensional space corresponding to constant fields. Moreover, it provides a simple and effective rule (2.26) for choosing the penalty coefficient \(\gamma\).

**Remark 2.7.** _A notable advantage of our finite-difference-based formulation lies in the modest penalty required, which leads to a relatively well-conditioned system. Our analysis shows_ \(\gamma=O(1)\) _is sufficient. In contrast, kernel compensation within a finite element framework necessitates a much larger penalty, typically O(h_<sup>-3</sup>)_, to counteract the scaling of the mass matrix. As noted in \[15\], where the penalty coefficient is chosen to be_ \(\gamma=\frac{2}{h^3}\) _in the experiment, spurious eigenvalues are still likely to occur._

## 2.4. Matrix-free Operations and Preconditioning

In this subsection, we aim for matrix-free operation \(\mathbf{H}_h\mapsto(\mathcal{A}\mathcal{M}_\varepsilon\mathcal{A}^\dagger+\gamma\mathcal{B}^\dagger\mathcal{B})\mathbf{H}_h\) and the approach to preconditioning the system matrix \(\mathcal{A}\mathcal{M}_\varepsilon\mathcal{A}^\dagger+\gamma\mathcal{B}^\dagger\mathcal{B}\) effectively using DFT. We define the \(N^3\times N^3\) 3D DFT matrix F as the tensor product of three 1D DFT matrices:

\(\mathcal{F}=\mathbf{F}\otimes\mathbf{F}\otimes\mathbf{F}.\) (2.27)

Applying the mixed product property (2.15) and Lemma 2.1, we establish the F-diagonalization of matrices D_<sub>i</sub>_ for _i_=1,2,3.

**Proposition 2.8.** _Assuming_ \(\mathbf{D}_i=\mathbf{F}\Lambda_i\mathbf{F}^\dagger\) _for i_=0,1_, where diagonal matrices_ \(\Lambda_i\) _are derived from_ (2.14)_, the matrices_ D_<sub>i</sub> admit the factorization_

\(\mathcal{D}_i=\mathcal{F}\mathcal{K}_i\mathcal{F}^\dagger,i=1,2,3,\text{\textit{where}}\left\{\begin{array}{ c }
\mathcal{K}_1=I_{N^2}\otimes(\Lambda_1+\mathrm{i}\mathrm{k}_1\Lambda_0), \\
\mathcal{K}_2=I_N\otimes(\Lambda_1+\mathrm{i}\mathrm{k}_2\Lambda_0)\otimes I_N, \\
\mathcal{K}_3=(\Lambda_1+\mathrm{i}\mathrm{k}_3\Lambda_0)\otimes I_{N^2}.
\end{array}\right.\) (2.28)

_If we further define_ F<sub>3</sub>:=diag(F,F,F)_, the matrices_ A,B<sup>†</sup>B _are factorized as:_

\(\mathcal{A}=\mathcal{F}_3\mathcal{K}_\mathcal{A}\mathcal{F}_3^\dagger,\mathcal{B}^\dagger\mathcal{B}=\mathcal{F}_3\mathcal{K}_B\mathcal{F}_3^\dagger,\text{\textit{where}}\mathcal{K}_\mathcal{A}=\left(\begin{array}{ c c c }
 & -\mathcal{K}_3 & \mathcal{K}_2 \\
\mathcal{K}_3 &  & -\mathcal{K}_1
\end{array}\right),\mathcal{K}_B=\left(\begin{array}{ c }
\mathcal{K}_1^\dagger \\
\mathcal{K}_2^\dagger \\
\mathcal{K}_3^\dagger
\end{array}\right)\big(\mathcal{K}_1\mathcal{K}_2\mathcal{K}_3\big).\) (2.29)

