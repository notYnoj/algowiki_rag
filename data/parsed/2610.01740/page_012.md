<tbc>For each \(\ell\), define the analytic divided difference of \(f_\ell\) at the origin by<tbc>

\(\phi_\ell(z)=\left\{\begin{array}{ c c }
\left(f_\ell(z)-f_\ell(0)\right)/z, & z\neq 0, \\
f'_\ell(0), & z=0.
\end{array}\right.\)

<tbc>Theorem 4.3 (Recovery vector from the structured representation). _Under Hypothesis 4.2, the recovery vector u_<sub>_m_+1</sub> _can be expressed as_<tbc>

(4.5) \(u_{m+1}=-A_0^{-1}\sum_{\ell=1}^{d-1}M_\ell G_m\phi_\ell(K_m)e_m.\)

<tbc>_Proof._ The _i_th block of the last column of _Q<sub>m</sub>_ is \(q_{i,m}=G_mK_m^{i-1}e_m\). Equation (3.5) gives<tbc>

\(u_{m+1}=-A_0^{-1}\sum_{i=1}^mA_iq_{i,m}.\)

<tbc>Substitution of (4.4), followed by an interchange of the two finite sums, gives

\(-A_0^{-1}\sum_{\ell=1}^{d-1}M_\ell G_m\left(\sum_{i=1}^mf_{\ell,i}K_m^{i-1}\right)e_m.\)

The polynomial in parentheses is the degree-(_m_-1) Taylor polynomial of \(\phi_\ell\) at _K<sub>m</sub>_. Since \(K_m^m=0\), it equals \(\phi_\ell(K_m)\) exactly. □

(4.5) requires only _G<sub>m</sub>_ and the vectors \(\phi_\ell(K_m)e_m\). In the next section, we will discuss how to evaluate \(\phi_\ell(K_m)e_m\) efficiently.

**4.3. Incremental evaluation of matrix-function actions.** The recovery formula (4.5) requires the vectors \(\phi_\ell(K_m)e_m\). We now describe how to update these vectors as _K<sub>m</sub>_ gains a column. Since \(K_m^m=0\), evaluating an analytic function at _K<sub>m</sub>_ requires only its Taylor polynomial of degree at most _m_-1. Moreover, the nested form of _K<sub>m</sub>_ implies that \(\phi_\ell(K_{m-1})\) is the leading principal block of \(\phi_\ell(K_m)\) \[9\]. The following application-specific updates attain the O(_m_<sup>2</sup>) cost per step.

_Fixed-degree polynomials._ Let _f_ have a fixed degree _r_. Horner’s rule computes \(\phi(K_m)e_m\) in O(_rm_<sup>2</sup>)=O(_m_<sup>2</sup>) operations.

_Rational functions._ Let _f=P/Q_ and assume \(Q(0)\neq 0\). Since _P-f_(0)_Q_ is divisible by _z_, \(\phi(K_m)\) can be evaluated as

\(\phi(K_m)=Q(K_m)^{-1}\left(\frac{P-f(0)Q}{z}\right)(K_m).\)

The quotient in parentheses is a polynomial. Because _K<sub>m</sub>_ is strictly upper triangular, _Q(K<sub>m</sub>_) is upper triangular with the nonzero diagonal entry _Q_(0). For fixed degrees, updating the last column and solving the triangular system cost O(_m_<sup>2</sup>).

_Affine square roots._ For \(f(z)=\gamma\sqrt{c+\omega z}\) with \(c\neq 0\), choose the analytic branch by fixing the scalar value \(\sqrt{c}\), and define \(T_m=(I+(\omega/c)K_m)^{1/2}\). If \(K_m=[\genfrac..{pt}{2}{K_{m-1}}{0}k_0]\), then<tbc>

\(T_m=\left[\begin{array}{ c c }
T_{m-1} & t \\
0 & 1
\end{array}\right],(T_{m-1}+I)t=(\omega/c)k,\)

<tbc>which is the scalar-border form of the classical triangular square-root recurrence \[3\]. The divided difference satisfies

\(\phi(K_m)e_m=\gamma\frac{\omega}{\sqrt{c}}(T_m+I)^{-1}e_m.\)

