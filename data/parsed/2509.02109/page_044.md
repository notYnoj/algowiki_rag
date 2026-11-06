<tbc>Fig. 22, we flow a point cloud initialised as random normal noise, towards a barycentre of _K_=15 GMMs fitted from (_Y<sub>i</sub>_).

We can also compute a generalised barycentre _X_ in \(\mathbb{R}^{n\times 3}\), such that every projection \(P_i(X)\in\mathbb{R}^{n\times 2}\) orthogonal to the canonical direction _e<sub>i</sub>_ coincides with _Y<sub>i</sub>_. Specifically, we solve

\(min_{X\in\mathbb{R}^{n\times 2}}\sum_{i=1}^3\mathrm{MW}_2^2\left(P_i\#\mu(F_X^T(\theta_0)),\nu_i\right).\)

The GMMs \((\nu_i)\in\mathrm{GMM}_2(40)^3\) are fitted beforehand with the point clouds (_Y<sub>i</sub>_), and \(\mu_X\) is the running EM estimation of optimised cloud _X_. The projected GMM \(P_i\#\mu(F_X^T(\theta_0))\) is defined by projecting the means and covariances of the three-dimensional GMM \(\mu(F_X^T(\theta_0))\). We sample _n_=1000 points and fit _K_=100 Gaussian components in each cloud. Example results are shown in Fig. 23. We obtained very similar results with an alternative loss which estimates three GMMs in R<sup>2</sup> instead of one in R<sup>3</sup>. In all our barycenter experiments, we set \(\varepsilon_r=10^{-3}\).

## A.9.4 Colour Transfer

### Optimiser choice.

We use gradient descent with fixed step size. Indeed, optimisers such as Adam have per-parameter learning rates that are adapted dynamically. As a result, points are treated differently and move at different speeds. For instance, imagine that we independently sample points \(x_1,\cdots,x_n\) in R_<sup>d</sup>_ following the law N(0_<sub>d</sub>,I<sub>d</sub>_) and want to match them to N(0_<sub>d</sub>,_2_I<sub>d</sub>_) using the Mixture Loss. Optimisers like Adam might focus on moving the points on the boundary to make the cloud’s variance larger. Fixed-step gradient descent, on the contrary, will treat each point equally, and will rescale the cloud as a whole.

### Fixing mixture weights.

As discussed in Section 3.3, fixing the mixture weights to be uniform (using Algorithm 2) avoids local minima, as illustrated in Fig. 24. For a colour transfer task with<tbc>

GMM#1 median
GMM#1 quantiles
GMM#2 median
GMM#2 quantiles
GMM#3 median
GMM#3 quantiles
Fixed Point MSE
Max Eigenvalue of dF/dTheta
relative MSE: OS vs AD
relative MSE: AI vs AD
10-3
100
100
10-3
10-6
10-1
10-9
10-9
10-2
10-15
10-12
10-1
10-3
10-21
10-15
10-27
10-4
5
10
15
5
10
15
5
10
15
5
10
15
K
K
K
K



Figure 21: Varying the number of components _K_, we study the convergence of EM, the local contractivity of _F_, and the MSEs of the OS and AI gradients.

Figure 22: Left: EM - \(\mathrm{MW}_2^2\)-Barycentre flow; right: input point clouds.

