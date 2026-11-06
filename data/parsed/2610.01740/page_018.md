<tbc>\(h(x)=e^{-\alpha x_1}\), \(\beta(x)=\mathrm{sin}(2\pi x_1)\), _f_<sub>1</sub>(_s_)=_s_, _f_<sub>2</sub>(_s_)=sin_s_, and \(\alpha=30\). Finite element discretization gives

\(A(s)=A_0+A_1s+2A_2s^2+A_3s^3+A_4\mathrm{sin}s,\)

with sparse coefficient matrices. We use the same sparse matrices _A<sub>i</sub>_ as in \[6\], and set _s_=2.5, with expansion center _s_<sub>0</sub>=0 and scaling factor _w_=5.

The iteration curves of each algorithm in Figure 2(a) overlap at the plotted scale. All four methods first reach 10<sup>-8</sup> at iteration 34 and finish with relative residuals near \(1.47\times 10^{-11}\). Figure 2(b) shows the residual histories versus runtime. The median end-to-end times are 40.46s for fully refreshed TiGMRES, 27.24s for Toeplitz infGMRES, 30.32s for Dynamic TiGMRES, and 19.96s for IR-TiGMRES. IR-TiGMRES uses 26.7% less time than basic Toeplitz, 34.2% less than Dynamic TiGMRES, and 50.7% less than fully refreshed TiGMRES.

Although Toeplitz infGMRES and IR-TiGMRES have the same asymptotic _O(np_<sup>2</sup>+_p_<sup>3</sup>) arithmetic complexity, their time performance differs in this test. Here are the reasons. For _p_=50, the Taylor convolution in the basic and refreshed Toeplitz implementations requires \(\sum_{k=2}^p(k-1)=1225\) sparse matrix-vector products, whereas the four-term action using the split form in IR-TiGMRES requires only 4(_p_-1)=196. So IR-TiGMRES appears faster than Toeplitz infGMRES.

Under Hypothesis 4.2, a similar grouping operation can also be easily applied to Toeplitz infGMRES and Dynamic TiGMRES, but we did not implement it in our experiments. This is because we regard these two methods as general-purpose algorithms, rather than methods specifically tailored to a split form with a small _d_.

**6.3. Contour-integral nonlinear eigensolvers.** Let \(T:\Omega\rightarrow\mathbb{C}^{n\times n}\) be analytic, and let the smooth contour \(\Gamma=\partial\Omega\) enclose only simple eigenvalues \(\lambda_1,\dots,\lambda_k\), and the corresponding eigenvectors _v_<sub>1</sub>_,...,v<sub>k</sub>_ of _T_.

We use the approach in \[16\] to compute the eigenpairs. Beyn’s method \[2\] forms

\(M_0=\frac{1}{2\pi\mathrm{i}}\oint_\Gamma T(\xi)^{-1}Zd\xi,M_1=\frac{1}{2\pi\mathrm{i}}\oint_\Gamma\xi T(\xi)^{-1}Zd\xi.\)

100
fully refreshed TIGMRES Toeplitz infGMRES Dynamic TIGMRES IR-TIGMRES
10-2
10-4
Relative residual
10-6
10-8
10-10
10-12
0
5
10
15
20
25
30
35
40
45
50
Iteration k

100
fully refreshed TIGMRES Toeplitz infGMRES Dynamic TIGMRES IR-TIGMRES
10-2
10-4
Relative residual
10-6
10-8
10-10
10-12
0
5
10
15
20
25
30
35
40
45
Time in sec

(a) Residual versus iteration.

(b) Residual versus runtime.

Fig. 2: Relative residual histories for the finite element Helmholtz problem with _s_=2.5. (a) shows the residual versus iteration results. (b) shows the residual versus runtime results.

