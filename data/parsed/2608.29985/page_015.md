<tbc>\(f(\alpha,\gamma)\) which relies on the Frobenius norm of the matrix R

\(f(\alpha,\gamma)=\|\mathscr{R}_\mathrm{VBP}\|_F^2=\mathrm{tr}(\mathscr{R}_\mathrm{VBP}^T\mathscr{R}_\mathrm{VBP}).\) (49)

By minimizing this objective function with respect to the involved parameters, we can analytically derive their quasi-optimal values. Consequently, we have

\(f(\alpha,\gamma)=\mathrm{tr}(\mathscr{R}_\mathrm{VBP}^T\mathscr{R}_\mathrm{VBP})=\alpha^2n-2\alpha\gamma\mathrm{tr}(W^2)+\gamma^2\mathrm{tr}(W^4)+\mathrm{tr}(W^2)-2\gamma\mathrm{tr}(W^2T)+\gamma^2\mathrm{tr}(WT^2W).\text{(50)}\)

To obtain the quasi-optimal parameters in the VBP preconditioner, we regard the parameter \(\gamma\) as a constant and analyze only the parameter \(\alpha\). By minimizing the function \(f(\alpha,\gamma)\), we get the quasi-optimal parameter \(\alpha\) in the VBP preconditioner as follows

\(\alpha_\mathrm{VBP}=\alpha_\mathrm{qopt}=\frac{\gamma\|W\|_F^2}{n}\) (51)

## 5 Numerical Experiments

In this section, we evaluate the numerical performance of the proposed P<sub>VBP</sub> for (2) through a series of comprehensive numerical experiments. All computations are carried out using Matlab (R2020a) on a Windows 10 system equipped with an Intel Core i5 processor running at 2.6 GHz and 8 GB of RAM.

In each experiment, the iterative process is initiated with a zero initial guess, i.e., **x**<sub>0</sub>=**0**. This approach ensures a consistent and reliable assessment of the convergence behavior and the overall effectiveness of the proposed preconditioner.

We compare the performance of the proposed preconditioner P<sub>VBP</sub> with three existing preconditioners, namely P<sub>BS</sub> \[35\], P<sub>VHSS</sub> \[31\], and P<sub>MBP</sub> \[9\], whose formulations are given in (3), (4), and (5), respectively. Proper parameter selection is essential for achieving fast convergence with the preconditioned FGMRES solver. According to the parameter selection strategies proposed in \[31\], the quasi-optimal parameter \(\alpha\) for both the VHSS preconditioners is chosen as

\(\alpha_\mathrm{VHSS}=\sqrt{\lambda_\mathrm{min}(T)\lambda_\mathrm{max}(T)},\) (52)

where \(\lambda_\mathrm{min}(T)\) and \(\lambda_\mathrm{max}(T)\) denote the smallest and largest eigenvalues of the matrix _T_, respectively.

Following the approach introduced in \[35\], the parameter \(\alpha_\mathrm{BS}\) for the BS preconditioner is determined by

\(\alpha_\mathrm{BS}=\sqrt{\frac{\mathrm{tr}(TW^2T)}{n}},\) (53)

where \(\mathrm{tr}(\cdot)\) denotes the trace operator and _n_ is the dimension of the matrices involved.

