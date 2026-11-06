For \(n\ge 2\), integration by parts gives the recursion

\(J_n=-\frac{\sigma^2}{2}\left[(b-m)^{n-1}e^{-(b-m)^2/\sigma^2}-(a-m)^{n-1}e^{-(a-m)^2/\sigma^2}\right]+\frac{(n-1)\sigma^2}{2}J_{n-2}.\) (100)

This recursion provides a convenient analytic route to the high-order kernel derivatives required by elliptic, advection- diffusion, and biharmonic operators.

### B.9 Extension to multiple dimensions

Suppose the _d_-dimensional Gaussian feature is separable,

\(\phi_\mathbf{c}(\mathbf{x})=\prod_{r=1}^d\mathrm{exp}\left(-\frac{(x_r-c_r)^2}{2\sigma_r^2}\right),\) (101)

and the center coordinates are independently distributed as

\(c_r\sim\mathcal{U}[a_r,b_r].\) (102)

The mean density factorizes,

\(\rho(\mathbf{c})=\prod_{r=1}^d\frac{1}{b_r-a_r},\) (103)

and therefore the multidimensional kernel also factorizes:

\(k_\rho(\mathbf{x},\mathbf{y})=\mathbb{E}_\mathbf{c}\left[\phi_\mathbf{c}(\mathbf{x})\phi_\mathbf{c}(\mathbf{y})\right]\)<br>
\(=\prod_{r=1}^dk_{[a_r,b_r]}^{(r)}(x_r,y_r).\) (104)

Consequently, mixed derivatives also factorize:

\(D_\mathbf{x}^\alpha D_\mathbf{y}^\beta k_\rho(\mathbf{x},\mathbf{y})=\prod_{r=1}^d\partial_{x_r}^{\alpha_r}\partial_{y_r}^{\beta_r}k_{[a_r,b_r]}^{(r)}(x_r,y_r).\) (105)

This property is particularly useful for Cartesian embedding domains and space-time formulations. For example, a two-dimensional Laplacian kernel can be assembled from one-dimensional derivative factors, while space-time advection-diffusion kernels can be constructed from separate spatial and temporal mean kernels.

### B.10 Summary

The continuum-center Gaussian feature model therefore admits the exact bounded-support kernel

\(k_{[a,b]}(x,y)=\frac{\sqrt{\pi}\sigma}{2(b-a)}e^{-(x-y)^2/(4\sigma^2)}\left[\mathrm{erf}\left(\frac{b-\frac{x+y}{2}}{\sigma}\right)-\mathrm{erf}\left(\frac{a-\frac{x+y}{2}}{\sigma}\right)\right],\) (106)

which reduces to a Gaussian/squared-exponential kernel in the full-support limit after normalization.

More importantly for PDE collocation, the differentiated mean kernel satisfies

\(D_x^\alpha D_y^\beta k_\rho(x,y)=\mathbb{E}_{c\sim\rho}\left[D_x^\alpha\phi_c(x)D_y^\beta\phi_c(y)\right].\) (107)

Hence, the differential-operator kernel matrices used by the proposed method are exactly the continuum limits of the corresponding finite Gaussian-RBF operator Gram matrices.

## CRediT authorship contribution statement

**Vikas Dwivedi:** Conceptualization, Methodology, Software, Writing - Original Draft, **Bruno Sixou** and **Monica Sigovan:** Supervision and Writing - Review & Editing.

