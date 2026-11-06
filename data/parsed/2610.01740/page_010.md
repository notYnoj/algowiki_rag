<tbc>**Algorithm 3.2** Dynamic Toeplitz infGMRES (Dynamic TiGMRES)

**Require:** Inputs of Algorithm 3.1, threshold \(\tau\ge 0\)

1: Initialize as in Algorithm 3.1; set \(a_1^{(0)}=a_1\) (because _a_<sub>1</sub> will be updated during the iteration); set \(G_1=a_1/\|a_1\|\), _e_<sup>1,1</sup>=1

2: **for** _m_=2_,...,p_ **do**

3: Compute _a<sub>m</sub>_ from the current generators by (3.1)

4: Recover _u<sub>m</sub>_ by (3.12), with \(u_2=a_2/\|a_1\|\)

5: Update the QR factorization (3.7) by incremental Gram-Schmidt; form _G<sub>m</sub>_ and _S<sub>m</sub>_ from (3.10)-(3.11), using the initial \(a_1^{(0)}\)

6: Set _t<sub>m</sub>=S<sub>m</sub>t_<sub>_m_-1</sub>

7: Compute _e<sup>i,m</sup>_, _i_=1_,...,m_, by (3.15)-(3.16), and \(\eta_m\) by (3.13)

8: **if** \(m\neq p\) and \(\big(m\le\lfloor p/2\rfloor\) or \(\eta_m\ge\tau\big)\) **then**

9: Set _a<sub>i</sub>=G<sub>m</sub>e_<sup>_m-i_+1_,m_</sup> for _i_=1_,...,m_, and _t<sub>m</sub>=e<sub>m</sub>_

10: **end if**

11: **end for**

12: Form <u>_H_</u><sub>p</sub> by (3.3), using the initial \(a_1^{(0)}\)

13: For each _s<sub>j</sub>_, solve (2.4) for _y<sub>s<sub>j</sub></sub>_ and return \(\widetilde{x}(s_j)=[a_1^{(0)}/\|z\|,u_2,\dots,u_p]y_{s_j}\)

1 compares basis construction of each algorithm over \(p\le q\) steps without assuming the separated representation in Hypothesis 4.2. Solving the reduced problems and forming _N_ approximations adds O(_N(p_<sup>2</sup>+_np_)) arithmetic for every method.

**4. Implicitly rebased Toeplitz infGMRES.** In this section, we present implicitly rebased Toeplitz infGMRES (IR-TiGMRES) for _A(s_) with a split form.

**4.1. A structured representation of the Arnoldi basis.** Dynamic TiGMRES in Section 3.4 uses _G<sub>m</sub>_ as the basis to construct every Arnoldi vector. This motivates us to represent _Q<sub>m</sub>_ in terms of _G<sub>m</sub>_.

Let \(J_m\in\mathbb{C}^{m\times m}\) have ones on the first superdiagonal and zeros elsewhere. Then the Toeplitz structure of _V<sub>m</sub>_ gives<tbc>

\((J_m\otimes I_n)V_m=V_mJ_m.\)

<tbc>Using the thin QR factorization _V<sub>m</sub>=Q<sub>m</sub>R<sub>m</sub>_, we can derive that

\((J_m\otimes I_n)Q_m=Q_m(R_mJ_mR_m^{-1}).\)

Let \(K_m:=R_mJ_mR_m^{-1}\), we can prove the following theorem.

\begin{tabular}{ccc}
Method & Arithmetic complexity & Storage complexity \\
TOAR infGMRES & \(\frac{2}{3}np^3+\mathcal{O}(np^2+p^4)\) & O(_np+p_<sup>3</sup>) \\
Toeplitz infGMRES & O(_np_<sup>2</sup>+_p_<sup>3</sup>) & O(_np+p_<sup>2</sup>) \\
Dynamic TiGMRES & \(\frac{1}{12}np^3+2n\sum_{i\ge\lfloor p/2\rfloor}^rm_i^2+\mathcal{O}(np^2+p^4)\) & O(_np+p_<sup>3</sup>) \\
fully refreshed TiGMRES & \(\frac{2}{3}np^3+\mathcal{O}(np^2+p^4)\) & O(_np+p_<sup>3</sup>) \\
\end{tabular}

1: Basis-construction complexities without Hypothesis 4.2. Here _m_<sub>1</sub>_,...,m<sub>r</sub>_ denote the refresh steps of Dynamic TiGMRES, and we assume \(m_i=i+1,\forall i=1,\dots,\lfloor p/2\rfloor-1\).

