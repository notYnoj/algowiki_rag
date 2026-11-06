_Proof._ (i) Let \(\phi_s\) be the flow of _X_. Since \(\phi_s\) is an isometry that maps \(\Omega\) and its wall onto themselves and preserves \(\rho\) and \(\gamma\), the bilinear form of Eq. (18) satisfies \(a(\phi_s^*w,\phi_s^*v)=a(w,v)\), and similarly for the load. Hence \(\phi_s^*w\) is the solution for the load \(\phi_s^*f\). By differentiating at _s_=0, we obtain that L_<sub>X</sub>w_ is the solution for the load L_<sub>X</sub>f_. The two statements follow from the linearity and uniqueness of the solution. (ii) Since _P_ commutes with _A_, it commutes with _e_<sup>-_iAT_</sup> and with _A_<sup>-1</sup>. Hence \(Pe^{-iAT}b=\chi e^{-iAT}b\) and \(Px^*=\chi x^*\). For a vector _v_ with \(Pv=\chi v\), we have \(\chi_z(Fv)_z=(FPF^\dagger Fv)_z=\chi(Fv)_z\), so (_Fv)<sub>z</sub>_=0 when \(\chi_z\neq\chi\).

Part (ii) is the discrete form of part (i). It requires a grid that is mapped onto itself by the isometry, so that _P_ is a permutation of grid points. Part (ii) also shows that a filter that keeps the indices with \(\chi_z=\chi\) satisfies the requirement of Algorithm 1: it removes only shots that the ideal sampler never produces and keeps every coefficient that can be nonzero. The parity filter of the lens (Sec. 4.8) is this rule for the two reflections \(\sigma\rightarrow 2\pi-\sigma\) and \(\tau\rightarrow-\tau\). For the disk, the Killing field \(\partial_\vartheta\) restricts a rotationally symmetric load to the modes with zero angular momentum. Conversely, if a coefficient field is not invariant, the selection rule is lost. In a curved vessel the coefficient \(\rho=H\) is not invariant under one of the reflections, and Sec. 5.7 shows that the number of nonzero modes doubles.

## 4.5 Curved and twisted vessels

For a vessel whose centerline has curvature \(\kappa_c\) and torsion \(\tau_c\), we use the orthogonal tube coordinates of Germano \[19\]. In these coordinates the metric is orthogonal, and the effect of torsion on the axial flow appears only at second order \[19\]. Let \(H=1-\kappa_c\rho cos\vartheta\) be the metric factor along the centerline, where \((\rho,\vartheta)\) are polar coordinates in the cross section and _H\>_0 is required throughout the tube. In the Stokes limit, with the secondary flow neglected, we use the reduced scalar model of the form (18) with

\(\rho=H,\gamma=\Gamma H+\frac{\kappa_c^2}{H}.\) (20)

The secondary (Dean) flow \[20\] enters through the convective terms. In an implicit-explicit scheme these terms are moved to the right-hand side, so that the matrix remains of the form (19). Unlike the conformal case, the curvature enters the stiffness matrix through \(\rho=H\). By Proposition 11, the theory applies to this positive-definite reduced model. Its reaction term and load conventions require independent validation against the full vector Stokes equations before quantitative curved-vessel predictions are claimed. Torsion and secondary-flow effects are not validated by the tests of Sec. 5.7.

## 4.6 Spectral bounds from the geometry

The time schedules of Sec. 3.1 and the residual certificate of Eq. (14) require the bounds _a_ and _B_ of Eq. (1). The following proposition supplies them from the geometry alone.

**Proposition 14** (Spectral bounds)**.** _Let C be diagonal with entries in_ \[_c_min_,c_max\]_. Then_

\(\lambda_\mathrm{min}(K)+c_\mathrm{min}\le\lambda_\mathrm{min}(A)\le\lambda_\mathrm{max}(A)\le\lambda_\mathrm{max}(K)+c_\mathrm{max}.\) (21)

_For conformal coordinates on a rectangle of side lengths L_<sub>1</sub>_,L_<sub>2</sub> _with N interior points per direction and_ \(\rho=1\)_, the eigenvalues of K are_ \(\sum_{j=1,2}(4/\Delta_j^2)\mathrm{sin}^2(\pi k_j/(2N+2))\) _with_ \(\Delta_j=L_j/(N+1)\).

_Proof._ For any unit vector _v_, \(\langle v,Av\rangle=\langle v,Kv\rangle+\langle v,Cv\rangle\), and both terms lie between the extreme eigenvalues of the respective matrix.

For the lens of Sec. 4.8 with _N_=32 and \(\Gamma=100\), Eq. (21) gives \(a=2.32\le\lambda_\mathrm{min}=3.07\) and \(\lambda_\mathrm{max}=1045\le B=1062\). For the disk it gives \(1.07\le 1.83\) and \(509\le 552\). These certified values can be used directly in Eq. (1). Weyl’s law \[21\] states that the number of eigenvalues below \(\lambda\) grows as \(|\Omega|_g\lambda/(4\pi)\), where \(|\Omega|_g\) is the area. It is a high-frequency asymptotic statement and does not certify low-lying gaps or a finite dephasing window.

