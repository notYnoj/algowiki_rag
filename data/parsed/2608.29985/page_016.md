<tbc>Furthermore, for the MBP preconditioner, the parameter \(\alpha_\mathrm{MBP}\) is set according to the formulation given in \[9\] as

\(\alpha_\mathrm{MBP}=\frac{\delta_\mathrm{max}^2+\delta_\mathrm{min}^2+2}{2},\) (54)

where \(\delta_\mathrm{max}\) and \(\delta_\mathrm{min}\) are defined in \[9\]. Since our proposed preconditioner is two-parameter based, we fix the parameter \(\gamma=1e-06\) throughout all numerical experiments.

The flexible GMRES (FGMRES) method was applied to solve the preconditioned systems, allowing at most 1000 iterations and using a stopping tolerance of 10<sup>-6</sup> based on the relative residual<tbc>

\(\mathrm{RES}=\frac{\|\mathbf{d}-\tilde{\mathcal{A}}\mathbf{x}_k\|_2}{\|\mathbf{d}\|_2}\le 10^{-6}.\)

<tbc>To measure solution quality, we record the relative error (ERR)

\(\mathrm{ERR}=\frac{\|\mathbf{x}_k-\mathbf{x}_*\|_2}{\|\mathbf{x}_*\|_2},\)

where **x**_<sub>k</sub>_ is the computed solution after _k_ steps and **x**<sub>∗</sub> is the exact one.

The inner linear systems arising within the FGMRES framework are solved inexactly using the conjugate gradient (CG) method. For each inner iteration, the CG solver is employed with a relative tolerance of 10<sup>-2</sup> and a maximum allowable number of iterations set to 500. To ensure statistical reliability, all reported CPU times (in seconds) and iteration counts are averaged over three independent runs.

**Example 1** ( \[13, 35\])**.** _As the first test problem, we consider the complex symmetric linear system of the form_ (1)_, given by_

\(\left[\left(\mathbf{K}-(3-\sqrt{3})\omega^2\mathbf{I}\right)+i\left(\mathbf{K}+(3+\sqrt{3})\tau^2\mathbf{I}\right)\right]\mathbf{x}=\mathbf{d},\) (55)

_where_ \(\tau\) _and_ \(\omega\) _are positive parameters. The matrix_ \(\mathbf{K}\in\mathbb{R}^{n\times n}\) _represents the five-point centered difference approximation of the negative Laplacian operator subject to homogeneous Dirichlet boundary conditions on the unit square_ \([0,1]\times[0,1]\) _with uniform mesh size_ \(h=\frac{1}{m+1}\)_. Specifically,_ **K** _admits the tensor-product form_

\(\mathbf{K}=\mathbf{I}\otimes\mathbf{V}_m+\mathbf{V}_m\otimes\mathbf{I},\) (56)

_with_ **V**_<sub>m</sub>=h_<sup>-2</sup> _tridiag_\((-1,2,-1)\in\mathbb{R}^{m\times m}\)_. Consequently,_ **K** _is a block tridiagonal matrix of dimension n=m_<sup>2</sup>.

_In our numerical experiments, the right-hand side vector is chosen as_ \(\mathbf{d}=(1+i)\unknown*\) _**ones**_(2_m_<sup>2</sup>,1)_., and we set_ \(\tau=1\)_. Additionally, the linear system_ (55) _is normalized by multiplying both sides by h_<sup>2</sup>_. To facilitate the application of preconditioning techniques, we define the real matrices_

\(W=h^2\left(\mathbf{K}-(3-\sqrt{3})\omega^2\mathbf{I}\right),T=h^2\left(\mathbf{K}+(3+\sqrt{3})\tau^2\mathbf{I}\right).\) (57)

