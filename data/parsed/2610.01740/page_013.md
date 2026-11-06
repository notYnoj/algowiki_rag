<tbc>Both _T_<sub>_m_-1</sub>+_I_ and _T<sub>m</sub>+I_ are upper triangular with diagonal entries 2. The two triangular solves therefore cost O(_m_<sup>2</sup>).

_Exponentials and trigonometric functions._ For \(f(z)=\mathrm{exp}(\alpha z)\), we specialize the incremental triangular evaluation strategy of \[14\] to the coupled exponential and divided-difference quantities. Let _r_<sub>13</sub>(_z_)=_P_<sub>13</sub>(_z)/Q_<sub>13</sub>(_z_) be the \[13/13\] Padé approximant to the exponential function _e<sup>z</sup>_, normalized by _P_<sub>13</sub>(0)=_Q_<sub>13</sub>(0)=1. Using the binary64 threshold \(\theta_{13}=5.371920351148152\) from \[8,  2.3\], we choose<tbc>

\(\nu=\lceil\mathrm{log}_2\mathrm{max}\{1,|\alpha|/\theta_{13}\}\rceil,h=\alpha/2^\nu,\)

<tbc>so that the scaling is fixed throughout the nested updates. Define<tbc>

\(D_h(z)=\frac{P_{13}(hz)-Q_{13}(hz)}{z}.\)

<tbc>The numerator has zero constant term, so _D<sub>h</sub>_ is a polynomial and no inversion of the singular matrix _K<sub>m</sub>_ is involved. Initialize<tbc>

\(E^{(0)}=Q_{13}(hK_m)^{-1}P_{13}(hK_m),\Phi^{(0)}=Q_{13}(hK_m)^{-1}D_h(K_m),\)

<tbc>where _E_<sup>(0)</sup> and \(\Phi^{(0)}\) can be seen as approximate matrix-function values at _K<sub>m</sub>_ of functions _e<sup>hz</sup>_ and (_e<sup>hz</sup>_-1)_/z_, respectively. The scalar identity _e_<sup>2_hz_</sup>-1=(_e<sup>hz</sup>_-1)(_e<sup>hz</sup>_+1), with analytic continuation of the divided differences at zero, yields the recovery recurrences

\(E^{(j+1)}=(E^{(j)})^2,\Phi^{(j+1)}=\Phi^{(j)}(E^{(j)}+I),j=0,\dots,\nu-1.\)

Then \(\Phi^{(\nu)}e_m\) approximates the required action \(\phi(K_m)e_m\). Since _K<sub>m</sub>_ extends _K_<sub>_m_-1</sub> by one column, the leading blocks of all intermediate matrices can be retained from the previous step. Updating only the new last columns in the polynomial evaluations, solves, and recovery stages costs \(\mathcal{O}((13+\nu)m^2)\) arithmetic and storage. Sine and cosine are handled by fixed linear combinations of the corresponding complex-exponential actions.

**4.4. Algorithm and complexity.** Algorithm 4.1 summarizes the method above. We call this algorithm Implicitly rebased Toeplitz infGMRES (IR-TiGMRES).

Now we analyze the computational complexity of IR-TiGMRES. Following the convention in Section 3.2, the bounds below omit the common arithmetic cost _F_<sub>LU</sub>(_n_)+_pS_<sub>LU</sub>(_n_) and LU-factor storage. Under Hypothesis 4.2, suppose that the matrix- function actions are computed using the incremental evaluators of Section 4.3. As discussed in Section 4.3, the matrix-function actions require O(_dm_<sup>2</sup>) arithmetic operations at step _m_. The products with _G_<sub>_m_-1</sub>, the sparse matrix actions, and the incremental QR update together require O(_dnm+nm+m_<sup>2</sup>) arithmetic operations per step. Summing over _m_=2_,...,p_, including initialization, therefore gives O(_d(np_<sup>2</sup>+_p_<sup>3</sup>)) arithmetic operations. The recovery vectors, compact matrices, and nested evaluator data require O(_np+dp_<sup>2</sup>) storage.

_Remark_ 4.4 (Grouped TOAR infGMRES under the split form). Hypothesis 4.2 also permits a cheaper companion action in TOAR infGMRES. Write _q<sub>i,m</sub>_ as _q<sub>i,m</sub>=O<sub>m</sub>c<sup>i,m</sup>_, where \(c^{i,m}\in\mathbb{C}^m\) and \(O_m\in\mathbb{C}^{n\times m}\) is the orthonormal basis of _G<sub>m</sub>_. Grouping the Taylor coefficients by the fixed matrices \(M_\ell\) gives

\(\sum_{i=1}^mA_iq_{i,m}=\sum_{\ell=1}^{d-1}M_\ell O_m\left(\sum_{i=1}^mf_{\ell,i}c^{i,m}\right).\)

