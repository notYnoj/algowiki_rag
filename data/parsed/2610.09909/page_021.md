### 5.3. Example 3.

In the last test, we move on to the three-dimensional case. Following \[7,18\], we denote the shifted coordinates \(X:=x-\frac{1}{2}\), \(Y:=y-\frac{1}{2}\), \(Z:=z-\frac{1}{2}\), and the parameters \(r_0=0.25,\sigma_0=0.15,A=1,c=\frac{1}{\sigma_0^2}\). Define the 12 bump centers on the sphere of radius _r_<sub>0</sub> as follows. Let \(s:=r_0/\sqrt{5}\). For _j_=0,1,2,3,4,<tbc>

\((X_j,Y_j,Z_j)=\big(2scos\theta_j,2ssin\theta_j,s\big),\theta_j=\frac{2j\pi}{5}.\)

<tbc>For _j_=5,6,7,8,9,<tbc>

\((X_j,Y_j,Z_j)=\big(2scos\theta_j,2ssin\theta_j,-s\big),\theta_j=\frac{(2(j-5)-1)\pi}{5}.\)

<tbc>Finally, the two poles are<tbc>

\((X_{10},Y_{10},Z_{10})=(0,0,r_0),(X_{11},Y_{11},Z_{11})=(0,0,-r_0).\)

<tbc>The level-set function \(\phi\) is defined by

\(\phi=X^2+Y^2+Z^2-r_0^2-\sum_{j=0}^{11}Aexp\big(-c\big((X-X_j)^2+(Y-Y_j)^2+(Z-Z_j)^2\big)\big).\)

Next, define \(u_\text{base}(x,y,z)=sin(\pi x)sin(\pi y)sin(\pi z)\), and the exact solution is taken as \(u_\text{ex}(x,y,z)=\phi(x,y,z)u_\text{base}(x,y,z)\).

Figure 4 illustrates the zero-contour surface \(\Gamma\) of the bumpy sphere, alongside a representative cutaway of the adaptively refined 3D hierarchical T-mesh. We evaluate the accuracy of the proposed method by tracking the errors on both uniformly and adaptively refined meshes. As depicted in Fig. 5, the computed _H_<sup>1</sup> and _H_<sup>2</sup> errors retain their optimal asymptotic convergence rates. These 3D results confirm two critical properties of the proposed UnCut FEM framework: first, the PHT-spline discretization perfectly preserves its optimal high-order accuracy under aggressive local refinement; second, the presence of hanging nodes does not compromise the convergence behavior of the scheme.

## 6. Conclusion

We proposed and analyzed a least-squares UnCut FEM for the Poisson problem on level- set domains. The method combines a \(\phi\)-FEM unfitted construction with _C_<sup>1</sup> continuous PHT-splines, which enables a fully primal formulation based on the _L_<sup>2</sup> residual \(\|\Delta u_h+f\|_{L^2(\Omega_h)}\). All terms are assembled on the active background domain \(\Omega_h\) using standard element-wise quadrature, thereby avoiding geometric integration over curved boundaries or cut subregions of boundary elements. Consequently, the method is simple to implement and computationally efficient. We proved existence and uniqueness of the discrete solution and



Figure 3. The computational mesh and its zoomed-in view of the region

\([0.2,0.5]\times[0.5,0.8]\) with 3328 leaf cells.

