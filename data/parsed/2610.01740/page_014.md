<tbc>**Algorithm 4.1** Implicitly rebased Toeplitz infGMRES (IR-TiGMRES)

**Require:** Split form (4.3), maximum Arnoldi length \(2\le p\le q\), right-hand side _z_, parameter values _s_<sub>1</sub>_,...,s<sub>N</sub>_ and a specified matrix-function evaluator for every \(f_\ell\)

**Ensure:** Approximations \(\widetilde{x}(s_j)\), _j_=1_,...,N_

1: Compute and store one LU factorization of _A_<sub>0</sub>

2: Solve _A_<sub>0</sub>_a_<sub>1</sub>=_z_ with the stored factors; apply \(P_1v=v-a_1(a_1^*v)/\|a_1\|_2^2\) implicitly

3: \(G_1=a_1/\|a_1\|_2\), _K_<sub>1</sub>=0

4: **for** _m_=2_,...,p_ **do**

5: **for** \(\ell=1,\dots,d-1\) **do**

6: Evaluate \(\widehat{v}_{\ell,m-1}\approx\phi_\ell(K_{m-1})e_{m-1}\) on the specified branch

7: **end for**

8: Solve \(A_0u_m=-\sum_{\ell=1}^{d-1}M_\ell G_{m-1}\widehat{v}_{\ell,m-1}\) using the stored factors

9: Update \(\left[\begin{array}{ c }
P_1[u_2,\dots,u_m] \\
I_{m-1}
\end{array}\right]=\widehat{Q}_{m-1}\widehat{R}_{m-1}\) by incremental Gram-Schmidt

10: Form _G<sub>m</sub>_, _K<sub>m</sub>_ from (4.1)-(4.2), and _S<sub>m</sub>_ from (3.11)

11: **end for**

12: Form <u>_H_</u><sub>p</sub> from (3.3)

13: **for** _j_=1_,...,N_ **do**

14: Solve (2.4) for _y<sub>s<sub>j</sub></sub>_

15: \(\widetilde{x}(s_j)=[a_1/\|z\|_2,u_2,\dots,u_p]y_{s_j}\)

16: **end for**

Since _d_ is fixed, the coordinate sums cost O(_dm_<sup>2</sup>) and the basis products and sparse matrix actions cost O(_dnm_) per step. We call this variant Grouped TOAR infGMRES (G-TOAR infGMRES). The coordinate orthogonalization of _c<sup>i,m</sup>_ still needs O(_m_<sup>3</sup>) arithmetic and O(_m_<sup>2</sup>) storage per step. Thus, for _p_ steps, G-TOAR infGMRES has arithmetic complexity O(_d(np_<sup>2</sup>+_p_<sup>3</sup>)+_p_<sup>4</sup>) and storage complexity O(_np+p_<sup>3</sup>).  2 compares it with IR-TiGMRES using the same split form. So compared with G-TOAR, IR-TiGMRES shows advantages both in arithmetic and storage complexity, especially when the number of steps _p_ is large.

**5. A residual lower bound and parameter scaling.** The structured representation of _Q<sub>m</sub>_ in Section 4.1 also yields a residual lower bound for infGMRES.

We denote the minimized norm in (2.4) by R_<sub>m</sub>(s_):

\(\mathcal{R}_m(s)=min_{y\in\mathbb{C}^m}\left\|\left(\left[\begin{array}{ c }
I_m \\
0_{1\times m}
\end{array}\right]-s\underline{H_m}\right)y-\|z\|_2e_1\right\|_2.\)

Let _K<sub>m</sub>_ have the form given in (4.2). Its strict upper triangularity and \(G_m^*G_m+K_m^*K_m=I_m\) give \(K_m^m=0\) and \(\|K_m\|_2\le 1\).

\begin{tabular}{ccc}
Method & Arithmetic complexity & Storage complexity \\
G-TOAR infGMRES & O(_d(np_<sup>2</sup>+_p_<sup>3</sup>)+_p_<sup>4</sup>) & O(_np+p_<sup>3</sup>) \\
IR-TiGMRES & O(_d(np_<sup>2</sup>+_p_<sup>3</sup>)) & O(_np+dp_<sup>2</sup>) \\
\end{tabular}

2: Basis-construction complexities under Hypothesis 4.2. The IR-TiGMRES additionally requires each \(f_\ell\) in the discussed area of Section 4.3.

