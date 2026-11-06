## 4 Results and Discussion

### 4.1 ODE benchmarks

Figure 1 summarizes the three one-dimensional ODE benchmarks. In all cases, the continuum-feature kernel solution closely tracks the exact solution over the full interval. For the first-order oscillatory problem, the solution RMSE and maximum error are \(1.70\times 10^{-6}\) and \(6.30\times 10^{-5}\), respectively. The second-order problem gives an RMSE of \(9.96\times 10^{-5}\) and a maximum error of \(2.24\times 10^{-4}\), while the multiscale case yields \(2.24\times 10^{-5}\) and \(8.28\times 10^{-4}\).

The corresponding residual RMS values are \(1.74\times 10^{-4}\), \(2.03\times 10^{-4}\), and \(2.26\times 10^{-3}\) for the first-order, second-order, and multiscale problems, respectively. In each case, the pointwise error is smallest at the constrained location _x_=0 and tends to increase toward the ends of the interval. The imposed value constraint is satisfied to machine precision in all three cases; for the second-order problem, the derivative condition \(u'(0)=-1/15\) is likewise recovered to machine precision.

Overall, these results verify the first- and second-derivative population kernels and show that the same continuum-feature representation can resolve both rapidly oscillating and multiscale solutions without introducing separate finite feature sets.

2 reports the computational cost of the principal stages of the continuum-feature solve. For all three problems, the dominant cost is the assembly of the operator-kernel matrices, followed by the SVD of the reduced system. The null-space construction contributes only a small fraction of the total cost. The second-order problem is moderately more expensive because additional differentiated kernel blocks are required to represent both the second-order differential operator and the two physical constraints.

\begin{tabular}{ccccc}
**Problem** & **Governing equation and domain** & **Conditions** & & **Reference solution** \\
First-order ODE & \(u'=\mathrm{cos}(15x),x\in[-2\pi,2\pi]\) & _u_(0)=0 & & \(u_\mathrm{ex}=\frac{1}{15}\mathrm{sin}(15x)\) \\
Second-order ODE & \(u''=\mathrm{sin}(15x),x\in[-2\pi,2\pi]\) & _u_(0)=0, \(u'(0)=-1/15\) & & \(u_\mathrm{ex}=-\frac{1}{225}\mathrm{sin}(15x)\) \\
Multiscale ODE & \(u'=\mathrm{cos}x+15\mathrm{cos}(15x),x\in[-2\pi,2\pi]\) & _u_(0)=0 & & _u_<sub>ex</sub>=sin_x_+sin(15_x_) \\
Poisson & \(-\Delta u=f\) on the five-petal domain & _u=u_<sub>ex</sub> on \(\partial\Omega\) & & \(u_\mathrm{ex}=\mathrm{sin}(4\pi x)\mathrm{cos}(4\pi y);f=32\pi^2u_\mathrm{ex}\) \\
Biharmonic & \(\Delta^2u=f\) on the five-petal domain & _u=u_<sub>ex</sub>, \(\partial_nu=\nabla u_\mathrm{ex}\cdot\mathbf{n}\) on \(\partial\Omega\) & & \(u_\mathrm{ex}=\mathrm{sin}(5\pi x)\mathrm{cos}(5\pi y);f=2500\pi^4u_\mathrm{ex}\) \\
Singular perturbation & \(u'-\nu u''=0,x\in(0,1),\nu=10^{-3}\) & _u_(0)=0, _u_(1)=1 & & \(u_\mathrm{ex}=\frac{e^{(x-1)/\nu}-e^{-1/\nu}}{1-e^{-1/\nu}}\) \\
Linear advection & \(u_t+u_x=0,(x,t)\in[-1,1]\times(0,1]\) & _u_(-1_,t_)=_u_(1_,t_); _u_(_x,_0)=_e_<sup>-(25_x_)<sup>2</sup></sup> & & \(u_\mathrm{ex}=\mathrm{exp}\left[-25^2(\mathrm{mod}(x-t+1,2)-1)^2\right]\) \\
Advection- diffusion & \(u_t+au_x-\nu u_{xx}=0,(x,t)\in[0,1]\times(0,1],a=0.5,\nu=10^{-3}\) & \(u(x,0)=e^{-(x-0.2)^2/\nu};u(0,t)=u_\mathrm{ex}(0,t),u(1,t)=\) & & \(u_\mathrm{ex}=\frac{1}{\sqrt{4t+1}}\mathrm{exp}\left[-\frac{(x-0.2-at)^2}{\nu(4t+1)}\right]\) \\
Viscous Burgers & \(u_t+uu_x-\nu u_{xx}=0,(x,t)\in[-1,1]\times(0,1],\nu=0.01\) & \(u(x,0)=-\mathrm{sin}(\pi x);u(-1,t)=u(1,t)=0\) & & Cole-Hopf reference solution \\
\end{tabular}

\begin{tabular}{ccccc}
**Case** & **Kernel assembly** & **Null-space** & **Reduced SVD/solve** & **Total solve** \\
 & **(s)** & **(s)** & **(s)** & **(s)** \\
First-order ODE & 1.518 & 0.022 & 0.603 & 2.155 \\
Second-order ODE & 2.427 & 0.036 & 0.823 & 3.296 \\
Multiscale ODE & 1.778 & 0.004 & 0.759 & 2.546 \\
\end{tabular}

1: Summary of the numerical test problems.

2: Computational timing for the three ODE benchmarks.

