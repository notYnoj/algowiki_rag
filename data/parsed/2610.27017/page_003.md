design and optimization of smoothers. In this work, we adopt Gaussian Process Regression (GPR) to learn and select the relaxation parameters of the weighted Jacobi smoother, so as to improve the convergence speed of the multigrid method.

GPR is a Bayesian nonparametric learning method that places a Gaussian process prior on the unknown mapping from problem features to the desired relaxation parameter. Given a small set of training samples, the correlations among the samples are characterized by a covariance kernel, and conditioning the prior on the observed data yields a posterior predictive distribution for a new problem instance. Its mean can be used as the predicted relaxation parameter, while its variance provides a quantitative measure of prediction uncertainty. It can capture nonlinear parameter dependence without prescribing a fixed functional form, perform well with relatively small datasets, and, once trained, deliver predictions at a low online cost.

The paper is organized as follows. In Section 2,we discretize the original equations and analyze the basic spectral properties of the coefficient matrix. In Section 3, with the aid of the Ruge-Stuben two grid framework, we design and analyze the convergence of the two grid method. In Section 4, we introduce the principles of GPR and its procedure for predicting parameters. In Section 5, we present numerical experiments to demonstrate the effectiveness and superiority of the multigrid method and GPR for parameter prediction. In Section 6, we summarize the conclusions and future work.

## 2. Discretization and matrix properties

In this section, we will introduce the specific discrete schemes and analyze the properties of the coefficient matrices obtained from the discretization, which will help us design the multigrid method. Below, we review the left- and right-sided Riemann-Liouville fractional derivatives:<tbc>

\(x_LD_x^{\gamma_1}u(x,y,t)=\frac{1}{\Gamma(2-\gamma_1)}\frac{d^2}{dx^2}\int_{x_L}^x\frac{u(\xi,y,t)}{(x-\xi)^{\gamma_1-1}}d\xi,x_D_{x_R}^{\gamma_1}u(x,y,t)=\frac{1}{\Gamma(2-\gamma_1)}\frac{d^2}{dx^2}\int_x^{x_R}\frac{u(\xi,y,t)}{(\xi-x)^{\gamma_1-1}}d\xi,\)<br>
\(y_LD_y^{\gamma_2}u(x,y,t)=\frac{1}{\Gamma(2-\gamma_2)}\frac{d^2}{dy^2}\int_{y_L}^y\frac{u(x,\xi,t)}{(y-\xi)^{\gamma_2-1}}d\xi,y_D_{y_R}^{\gamma_2}u(x,y,t)=\frac{1}{\Gamma(2-\gamma_2)}\frac{d^2}{dy^2}\int_y^{y_R}\frac{u(x,\xi,t)}{(\xi-y)^{\gamma_2-1}}d\xi,\)

<tbc>where \(\Gamma(\cdot)\) is the Gamma function. Let _N,M_ be positive integers. Take the step sizes \(\Delta x=\frac{x_R-x_L}{N+1}\) , \(\Delta y=\frac{y_R-y_L}{N+1}\) , \(\Delta t=\frac{T}{M}\) to discretize the _x_-direction, _y_-direction and time, yielding

\(\{x_i|x_i=x_L+i\Delta x,0\le i\le N+1\},\)<br>
\(\{y_j|y_j=y_L+j\Delta y,0\le j\le N+1\},\)<br>
\(\{t_m|t_m=m\Delta t,0\le m\le M\}.\)

Define \(u_{i,j}^{(m)}=u(x_i,y_j,t_m)\), \(f_{i,j}^{(m)}=f(x_i,y_j,t_m)\), \(d_{i,j}^{(m)}=d(x_i,y_j,t_m)\). Using the shifted Grünwald formula\[19, 18\], we can obtain the approximation of the fractional derivative at the point (_x<sub>i</sub>,y<sub>j</sub>,t<sub>m</sub>_):<tbc>

\(x_LD_x^{\gamma_1}(x_i,y_j,t_m)=\frac{1}{\Delta x^{\gamma_1}}\sum_{k=0}^{i+1}g_k^{(\gamma_1)}u_{i-k+1,j}^{(m)}+\mathcal{O}(\Delta x),\)<br>
\(x_D_{x_R}^{\gamma_1}(x_i,y_j,t_m)=\frac{1}{\Delta x^{\gamma_1}}\sum_{k=0}^{N-i+2}g_k^{(\gamma_1)}u_{i+k-1,j}^{(m)}+\mathcal{O}(\Delta x),\)

<tbc>and<tbc>

\(y_LD_y^{\gamma_2}(x_i,y_j,t_m)=\frac{1}{\Delta_y^{\gamma_2}}\sum_{k=0}^{j+1}g_k^{(\gamma_2)}u_{i,j-k+1}^{(m)}+\mathcal{O}(\Delta y),\)<br>
\(y_D_{y_R}^{\gamma_2}(x_i,y_j,t_m)=\frac{1}{\Delta_y^{\gamma_2}}\sum_{k=0}^{N-j+2}g_k^{(\gamma_2)}u_{i,j+k-1}^{(m)}+\mathcal{O}(\Delta y),\)

