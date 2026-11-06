leading term (Theorem 4.4) and an exactly unbiased estimator of the finite-sample covariance (Theorem 4.8). First-order covariances of the L-comoment ratios are given in Appendix E. The efficient computation of these estimators and their PSD and PD corrections are treated in Section 5.

For _m_=2,3 and \(c\le m\), let \(M_{m,c}(z_1,\dots,z_c)=(M_{m,c}^{[XY]}(z_1,\dots,z_c),M_{m,c}^{[YX]}(z_1,\dots,z_c))^\mathsf{T}\) be the two-direction vector of conditional kernels. Recall that \(\mathbb{E}(\mathbf{H}_m)=\unknown_m\) for _m_=2,3. The decomposition is based on the Hoeffding projections of the kernels (Hoeffding, 1948; Serfling, 1980). Define the centered first projections<tbc>

\(\mathbf{a}(z)=M_{2,1}(z)-\unknown_2,\mathbf{b}(z)=M_{3,1}(z)-\unknown_3.\) (4.1)

<tbc>For distinct _z_<sub>1</sub>_,z_<sub>2</sub> let<tbc>

\(\mathbf{c}(z_1,z_2)=\mathbf{H}_2(z_1,z_2)-\mathbf{a}(z_1)-\mathbf{a}(z_2)-\unknown_2,\) (4.2)

\(\mathbf{d}(z_1,z_2)=M_{3,2}(z_1,z_2)-\mathbf{b}(z_1)-\mathbf{b}(z_2)-\unknown_3,\)<br>
\(\mathbf{e}(z_1,z_2,z_3)=\mathbf{H}_3(z_1,z_2,z_3)-\sum_{k<l}M_{3,2}(z_k,z_l)+\sum_{k=1}^3M_{3,1}(z_k)-\unknown_3.\)

<tbc>The centered first projections have mean zero, E{**_a_**(_Z_)}=E{**_b_**(_Z_)}=0, by the law of iterated expectations. The kernels **_c_**, **_d_**, and **_e_** are canonical (completely degenerate) in the sense of Hoeffding (1948): integrating out any one of their arguments gives zero, that is,

\(\mathbb{E}\{\mathbf{c}(z_1,Z_2)\}=\mathbb{E}\{\mathbf{d}(z_1,Z_2)\}=0,\mathbb{E}\{\mathbf{e}(z_1,z_2,Z_3)\}=0\) (4.3)

for all _z_<sub>1</sub>_,z_<sub>2</sub>. By symmetry of the kernels, the same holds for any argument. This property makes the components uncorrelated (Hoeffding, 1948; Serfling, 1980). Let **_f_** and **_g_** be any two of **_a_**_,**b**,**c**,**d**,**e**_, evaluated at index sets _I_ and _J_ of the corresponding sizes. Then

\(\mathbb{E}\{\mathbf{f}(Z_I)\mathbf{g}(Z_J)^\mathsf{T}\}=0\text{whenever}I\neq J.\) (4.4)

Indeed, if \(I\neq J\), some index _i_ belongs to one set but not to the other, say \(i\in I\) and \(i\notin J\). Given all _Z<sub>k</sub>_ with \(k\neq i\), **_g_**(_Z<sub>J</sub>_) is fixed, and the conditional mean of **_f_**(_Z<sub>I</sub>_) over _Z<sub>i</sub>_ is zero by (4.3) (or by E{**_a_**(_Z_)}=E{**_b_**(_Z_)}=0 when |_I_|=1). Hence the conditional mean of the product is zero, and so is its expectation. Below, E(**_aa_**<sup>T</sup>) means E{**_a_**(_Z_<sub>1</sub>)**_a_**(_Z_<sub>1</sub>)<sup>T</sup>}, E(**_cc_**<sup>T</sup>) means E{**_c_**(_Z_<sub>1</sub>_,Z_<sub>2</sub>)**_c_**(_Z_<sub>1</sub>_,Z_<sub>2</sub>)<sup>T</sup>}, and similarly for the other products.

**Theorem 4.1** (Exact component expansion)**.** _The exact finite-sample covariance in Theorem 3.1 also admits the decomposition_

\(\mathrm{Cov}(\widehat{\unknown})=\frac{B_1}{n}+\frac{B_2}{\genfrac(){pt}{2}{n}{2}}+\frac{B_3}{\genfrac(){pt}{2}{n}{3}},\) (4.5)

