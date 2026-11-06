<tbc>**Algorithm 1** Adaptive refinement algorithm

**Require:** Error tolerance TOL_\>_0, marking parameter \(\theta\in(0,1)\), and maximum iteration limit \(\ell_\mathrm{max}>0\).

1: **Initialize:** Construct an initial uniform background mesh \(\hat{\mathcal{T}}_h^{(0)}\) with \(N_0\times N_0\) cells. Set \(\ell\leftarrow 0\) and \(\eta^{(0)}\leftarrow+\infty\).

2: **while** \(\eta^{(\ell)}>\) TOL and \(\ell\le\ell_\mathrm{max}\) **do**

3: **Step 1:** From the background mesh \(\hat{\mathcal{T}}_h^{(\ell)}\) construct the active mesh \(\mathcal{T}_h^{(\ell)}\subset\hat{\mathcal{T}}_h^{(\ell)}\) based on the current level-set function \(\phi_h^{(\ell)}\).

4: **Step 2:** Assemble the discrete system on \(\mathcal{T}_h^{(\ell)}\) and solve the resulting linear system to obtain \(u_h^{(\ell)}\).

5: **Step 3:** Compute the local indicators \(\eta_T^{(\ell)}=\|\Delta u_h^{(\ell)}+f\|_{L^2(T)}\) for \(T\in\mathcal{T}_h^{(\ell)}\), and the global indicator \(\eta^{(\ell)}:=\left(\sum_{T\in\mathcal{T}_h^{(\ell)}}(\eta_T^{(\ell)})^2\right)^{1/2}\).

6: **Step 4:** Find a minimal set of marked cells \(\mathcal{M}^{(\ell)}\subset\mathcal{T}_h^{(\ell)}\) such that

\(\sum_{T\in\mathcal{M}^{(\ell)}}(\eta_T^{(\ell)})^2\ge\theta\sum_{T\in\mathcal{T}_h^{(\ell)}}(\eta_T^{(\ell)})^2=\theta\big(\eta^{(\ell)}\big)^2.\)

7: **Step 5:** Apply one-to-four (one-to-eight in 3D) subdivision to each marked cell \(T\in\mathcal{M}^{(\ell)}\) and recursively refine the necessary neighboring cells to strictly enforce the 1-regular constraint. This process yields the valid hierarchical refined mesh \(\hat{\mathcal{T}}_h^{(\ell+1)}\).

8: **Update:** Set \(\ell\leftarrow\ell+1\).

9: **end while**

the active computational mesh \(\mathcal{T}_h^{(\ell+1)}\) is dynamically identified by selecting the elements intersecting the discrete domain \(\{\phi_h^{(\ell+1)}<0\}\).

## 5. Numerical experiments

All numerical experiments are implemented using the MATLAB-based package `IGAPack` \[2\], employing the hierarchical T-mesh described in the previous sections. Unless otherwise specified, we utilize bicubic PHT-splines (polynomial degree _k_=3) for the discrete space _V<sub>h</sub>_. In the following tests, we take tolerance TOL=10<sup>-8</sup>, marking parameter \(\theta=0.25\) and maximum iteration \(\ell_\mathrm{max}=20\) in Algorithm 1.

### 5.1. Example 1.

We consider a smooth level-set function,

\(\phi(x,y)=(x-0.5)^2+(y-0.5)^2-r^2,(x,y)\in(0,1)^2,\) (5.1)

with _r_=0.3. The exact solution is chosen as \(u_\mathrm{ex}(x,y)=\phi(x,y)\mathrm{exp}(x+y)\), and the corresponding right-hand side is computed analytically. Here _u_<sub>ex</sub> is explicitly defined on the entire background domain \(\hat{\Omega}\), so the errors evaluated on \(\Omega_h\) involve this fixed extension and have no extension ambiguity.

We consider uniformly refined meshes, starting from an initial coarse mesh consisting of \(16\times 16\) cells. These meshes do not contain hanging nodes and satisfy _h<sub>M</sub>/h<sub>m</sub>_=1. The accuracy is evaluated by computing the errors \(\|u_h-u_\mathrm{ex}\|_{H^1(\Omega_h)}\) and \(\|u_h-u_\mathrm{ex}\|_{H^2(\Omega_h)}\) on the background mesh. As reported in  1, the proposed method achieves the optimal convergence rates predicted by the theory: O(_h_<sup>3</sup>) in the _H_<sup>1</sup>-norm and O(_h_<sup>2</sup>) in the _H_<sup>2</sup>-norm.

### 5.2. Example 2.

Consider the shifted coordinates \(X:=x-\frac{1}{2}\), \(Y:=y-\frac{1}{2}\) with the level-set function:

\(\phi(x,y):=X^2+Y^2-r_0^2-A\sum_{j=0}^5\mathrm{exp}\big(-\frac{(X-X_j)^2+(Y-Y_j)^2}{\sigma_0^2}\big),\) (5.2)

