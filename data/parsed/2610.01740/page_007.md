<tbc>**Algorithm 3.1** Toeplitz infinite GMRES (Toeplitz infGMRES)

**Require:** Taylor coefficients _A_<sub>0</sub>_,...,A<sub>q</sub>_, maximum Arnoldi length \(2\le p\le q\), right- hand side _z_, parameter values _s_<sub>1</sub>_,...,s<sub>N</sub>_

**Ensure:** Approximations \(\widetilde{x}(s_j)\), _j_=1_,...,N_

1: Compute and store one LU factorization of _A_<sub>0</sub>

2: Solve _A_<sub>0</sub>_a_<sub>1</sub>=_z_ with the stored factors; set \(t_1=\|a_1\|\); apply \(P_1v=v-a_1(a_1^*v)/\|a_1\|_2^2\) implicitly

3: **for** _m_=2_,...,p_ **do**

4: Solve \(A_0a_m=-\sum_{j=1}^{m-1}A_ja_{m-j}\) using the stored factors

5: **if** _m_=2 **then**

6: _u_<sub>2</sub>=_a_<sub>2</sub>_/t_<sub>1</sub>

7: **else**

8: \(u_m=\left(a_m-[u_2,\dots,u_{m-1}]t_{m-1}(1:m-2)\right)/t_{m-1}(m-1)\)

9: **end if**

10: Update \(\left[\begin{array}{ c }
P_1[u_2,\dots,u_m] \\
I_{m-1}
\end{array}\right]=\widehat{Q}_{m-1}\widehat{R}_{m-1}\) by incremental Gram-Schmidt

11: \(S_m=\left[\begin{array}{ c }
a_1^*[u_2,\dots,u_m]/\|a_1\| \\
\widehat{R}_{m-1}
\end{array}\right]\)

12: _t<sub>m</sub>=S<sub>m</sub>t_<sub>_m_-1</sub>

13: **end for**

14: Form <u>_H_</u><sub>p</sub> from (3.3)

15: **for** _j_=1_,...,N_ **do**

16: Solve (2.4) for _y<sub>s<sub>j</sub></sub>_

17: \(\widetilde{x}(s_j)=[a_1/\|z\|_2,u_2,\dots,u_p]y_{s_j}\)

18: **end for**

<tbc>of \(\{a_m\}_{m=1}^p\) costs _F_<sub>LU</sub>(_n_)+_pS_<sub>LU</sub>(_n_)+O(_np_<sup>2</sup>) arithmetic operations. The overall arithmetic complexity of Algorithm 3.1 is

\(F_\mathrm{LU}(n)+pS_\mathrm{LU}(n)+\mathcal{O}(np^2+p^3).\)

Storing \(\{a_m\}_{m=1}^p\), \(\{u_m\}_{m=2}^p\), \(\widehat{Q}_{p-1}\), \(\widehat{R}_{p-1}\) and _S<sub>p</sub>_ requires O(_np+p_<sup>2</sup>). In the complexity bounds below, we omit the common arithmetic cost _F_<sub>LU</sub>(_n_)+_pS_<sub>LU</sub>(_n_) and the storage of LU-factors.

**3.3. Cancellation in the recovery recurrence.** Algorithm 3.1 can lose stability. The main unstable step is computing _u<sub>m</sub>_:<tbc>

(3.12) \(u_m=\frac{a_m-[u_2,\dots,u_{m-1}]t_{m-1}(1:m-2)}{t_{m-1}(m-1)}.\)

<tbc>Let<tbc>

\(c_m=[u_2,\dots,u_{m-1}]t_{m-1}(1:m-2).\)

<tbc>This step subtracts _c<sub>m</sub>_ from _a<sub>m</sub>_ and divides by _t_<sub>_m_-1</sub>(_m_-1). A standard cancellation indicator is

\(\kappa_m^\mathrm{canc}=\frac{\|a_m\|_2+\|c_m\|_2}{\|a_m-c_m\|_2}.\)

When \(\{a_m\}_{m=1}^p\) becomes nearly linearly dependent, \(\kappa_m^\mathrm{canc}\) can be large and measures the potential amplification caused by the subtraction. The unmodified Toeplitz method then propagates the resulting error.

