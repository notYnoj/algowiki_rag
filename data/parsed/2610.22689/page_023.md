<tbc>for all \(1\le r<s\le D\). In the full unitary case g|_<sub>V</sub>_=u(_V_), this construction is extended to include the individual diagonal phase flows _e<sup>itE<sub>rr</sub></sup>_.

**Step 2. Application of global unitary decomposition.** Once arbitrary two-level _SU_(2) operations are accessible, we assemble them into an arbitrary element of _U(D_) or _SU(D_). Specifically, Spengler, Huber, and Hiesmayr \[27\] provided an explicit composite parameterization of _U(D_) directly in terms of exponentials appearing in (80). Namely, every \(g\in U(D)\) can be factored as

\(g=\prod_{j=1}^{D-1}\prod_{s=j+1}^D\left(e^{i\widehat{\theta}_{j,s}E_{ss}}e^{i\theta_{j,s}Y_{js}}\right)\cdot\prod_{l=1}^De^{i\widehat{\theta}_lE_{ll}},\) (81)

for suitable parameters \(\widehat{\theta}_{j,s},\widehat{\theta}_l\in[0,2\pi]\) and \(\theta_{j,s}\in\left[0,\frac{\pi}{2}\right]\).

To formulate this quantitatively, suppose every diagonal unitary on _V_ (modulo a scalar phase in the _SU(D_) case) can be synthesized using at most _K_<sub>diag</sub> native pulses, and every _e<sup>itY<sub>rs</sub></sup>_ flow using at most _K<sub>Y</sub>_ pulses. The total parameterized circuit depth of global synthesis is then bounded by<tbc>

\(L_\mathrm{glob}\le\genfrac(){pt}{2}{D}{2}\big(K_Y+K_\mathrm{diag}\big)+K_\mathrm{diag}.\) (82)

<tbc>**Remark VIII.1.** An equivalent global synthesis bound can be formulated using the generators _X<sub>rs</sub>=E<sub>rs</sub>+E<sub>sr</sub>_ from (79). Using the diagonal unitary operator

\(R_{rs}:=e^{-\frac{i\pi}{4}\left(E_{rr}-E_{ss}\right)},\) (83)

one obtains the relation<tbc>

\(Y_{rs}=R_{rs}X_{rs}R_{rs}^{-1},\text{and consequently},e^{itY_{rs}}=R_{rs}e^{itX_{rs}}R_{rs}^{-1}.\) (84)

<tbc>To determine the resulting circuit cost, set \(M:=\genfrac(){pt}{2}{D}{2}\) and express the composite parameterization (81) schematically as<tbc>

\(U=A_1e^{it_1Y_1}A_2e^{it_2Y_2}\cdots A_Me^{it_MY_M}A_\mathrm{f},\)

<tbc>where _A_<sub>1</sub>_,...,A<sub>M</sub>,A_<sub>f</sub> are diagonal unitaries. Substituting (84) yields

\(U=(A_1R_{r_1s_1})e^{it_1X_{r_1s_1}}\left(R_{r_1s_1}^{-1}A_2R_{r_2s_2}\right)e^{it_2X_{r_2s_2}}\cdots\left(R_{r_{M-1}s_{M-1}}^{-1}A_MR_{r_Ms_M}\right)e^{it_MX_{r_Ms_M}}\left(R_{r_Ms_M}^{-1}A_\mathrm{f}\right).\) (85)

As each parenthesized factor is a product of diagonal matrices, it remains strictly diagonal. The full product therefore consists of _M_ two-level _X_-flows interleaved with _M_+1 diagonal unitaries.

The following general theorem establishes explicit circuit depth bounds for synthesizing arbitrary group elements and state-to-state transitions when the restricted dynamical Lie algebra is u(_D_) or su(_D_). These bounds are parameterized by the primitive native synthesis costs _K<sub>X</sub>_ (for off-diagonal generator flows) and _K_<sub>diag</sub> (for diagonal unitaries). The formal proof is provided in Appendix D.

In the special unitary case, the diagonal factors in (84) may be chosen within SU(_V_). Indeed, if _A_<sub>1</sub>_,...,A_<sub>_M_+1</sub> are the diagonal factors and \(U\in\mathrm{SU}(V)\), choose scalars \(\lambda_r\) satisfying

\(\lambda_r^D=\mathrm{det}(A_r),\prod_{r=1}^{M+1}\lambda_r=1,\)

where the branches of the _D_-th roots are chosen so that the second condition holds. Then \(\widetilde{A}_r:=\lambda_r^{-1}A_r\) is diagonal and belongs to SU(_V_), while replacing every _A<sub>r</sub>_ by \(\widetilde{A}_r\) leaves the total product unchanged.

**Theorem VIII.2.** Let \(V\cong\mathbb{C}^D\) be a _D_-dimensional Hilbert space equipped with an orthonormal basis \(\{|e_1\rangle,\dots,|e_D\rangle\}\). Suppose the restricted dynamical Lie algebra satisfies g|_<sub>V</sub>_=u(_D_) or su(_D_). Let _K<sub>X</sub>_ denote a uniform depth bound for synthesizing any two-level flow _e<sup>itX<sub>rs</sub></sup>_ for all parameters \(t\in\mathbb{R}\) and indices \(1\le r<s\le D\), and let _K_<sub>diag</sub> denote a uniform depth bound for synthesizing an arbitrary diagonal unitary on _V_ (or arbitrary diagonal unitary within SU(_V_) if g|_<sub>V</sub>_=su(_V_)). Then the following bounds hold:

