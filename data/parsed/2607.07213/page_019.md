#### Two-flavor limit.

Setting \(\theta_{12}=0\) (\(\alpha\rightarrow 0\) in _T_int_,T_sol), \(P_{\mu e}\rightarrow 4s_{23}^2s_{13}^2c_{13}^2sin^2[(1-\hat{A})\Delta]/(1-\hat{A})^2\), the two-flavor MSW appearance formula. Unitarity \(\sum_\beta P_{\alpha\beta}=1\) holds algebraically for the exact solver and to \(\mathcal{O}(\alpha^3)\) for the perturbative expressions.

## 15 Extensions and Positioning

### 15.1 Positioning Relative to NuFast-LBL

The NuFast-LBL algorithm \[44\] runs at \(\sim 0.1\mu\)s per evaluation, with fractional precision \(\le 10^{-4}\) at zeroth order and \(\le 10^{-9}\) with a single Newton–Raphson step, surpassing full eigensystem computations by \(\sim 50\times\). The exact and perturbative expressions in this paper are positioned strictly as _exact theoretical anchors_: they provide analytic continuity in all six parameters, closed-form Jacobians (Section 13.2), transparent algebraic limiting cases (Section 14), and the explicit resummation structure (Section 10)--capabilities iterative solvers do not provide by construction. For production Monte Carlo analyses requiring O(10<sup>6</sup>)-O(10<sup>7</sup>) evaluations, NuFast-LBL is the recommended tool.

### 15.2 Constant-Density Validity and Longer Baselines

As noted in Section 2.3, the path-averaged constant density reproduces the exact DUNE probability to O(1%) \[53\], with no residual profile-shape sensitivity at DUNE’s expected precision. For longer baselines (\(L\unknown 5000\)km) where the chord samples upper-mantle material, a piecewise-layer treatment \(S_\text{total}=\prod_ke^{-iH_f(\rho_k)L_k}\) is required.

### 15.3 Parameter Degeneracies, NSI, and Sterile States

The appearance probability is invariant at leading order under \[60\] \(\delta_\text{CP}\rightarrow\pi-\delta_\text{CP}\), \(\theta_{23}\rightarrow\pi/2-\theta_{23}\); this degeneracy is lifted at \(\mathcal{O}(\alpha^2)\) by \(T_\text{sol}\propto c_{23}^2\). The density-matrix formalism accommodates non-standard interactions through an upgraded matter potential \[18, 64\], \(V_\text{mat}^\text{NSI}=\sqrt{2}G_FN_e(\mathbf{1}+\unknown)\), with \(\unknown\) the NSI matrix now constrained by COHERENT \[66, 67\]; the LMA-Dark degeneracy \[65\] requires \(\epsilon_{ee}\approx-2\). For a sterile state \[68, 69, 70\], the PMNS matrix becomes \(4\times 4\) and the Cayley–Hamilton polynomial for _S(L_) rises to cubic order, \(S(L)=c_0\mathbf{1}+c_1H_\text{f}+c_2H_\text{f}^2+c_3H_\text{f}^3\), with a quartic characteristic equation solvable by Ferrari’s method \[71\]; the algebraic logic of Sections 4-5 carries over directly.

### 15.4 Future Landscape

DUNE Phase II targets \(5\sigma\) CP sensitivity over more than 75% of \(\delta_\text{CP}\) values \[12\]; HK \[13\] adds complementary _L/E_ coverage; JUNO will fix \(\Delta m_{31}^2\) to 0.3% \[14\]; and IceCube- Gen2 \[77\] and KM3NeT/ORCA will probe the ordering via Earth matter effects. The algorithmic frontier continues to move toward more complex propagation scenarios beyond the constant-density LBL setting of this work.

## 16 Conclusion

None of the individual results here is new in isolation; the value lies in how they fit together. The starting point is the Cayley–Hamilton structure of _S(L_). Any analytic<tbc>

