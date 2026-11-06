<tbc>To see this, we represent a vector in \(\mathcal{K}_m(\mathcal{L}_1\mathcal{L}_0^{-1},\mathrm{vec}_0(z))\) by<tbc>

\(v_m(y)=\left[\begin{array}{ c c }
z & 0 \\
0 & V_{m-1} \\
0 & 0
\end{array}\right]y.\)

<tbc>Its lifted residual satisfies

\((I-s\mathcal{L}_1\mathcal{L}_0^{-1})v_m(y)-\mathrm{vec}_0(z)\)<br>
\(=\left[\begin{array}{ c c }
z & 0 \\
0 & V_m \\
0 & 0
\end{array}\right]\left(\left[\begin{array}{ c }
I_m \\
0_{1\times m}
\end{array}\right]-s\left[\begin{array}{ c }
0_{1\times m} \\
I_m
\end{array}\right]\right)y-\mathrm{vec}_0(z)\)<br>
\(=\left[\begin{array}{ c c }
z/\|z\|_2 & 0 \\
0 & Q_m \\
0 & 0
\end{array}\right]\left(\left[\begin{array}{ c c }
\|z\|_2 & 0 \\
0 & R_m
\end{array}\right]\left(\left[\begin{array}{ c }
I_m \\
0_{1\times m}
\end{array}\right]-s\left[\begin{array}{ c }
0_{1\times m} \\
I_m
\end{array}\right]\right)y-\|z\|_2e_1\right).\)

The columns of diag(_z/_\(\|z\|_2,Q_m\)) are orthonormal, so this factorization preserves the residual norm and leads to the minimization in (3.2). Moreover, the first block row of \(\mathcal{L}_0^{-1}v_m(y)\) is \[_a_<sub>1</sub>_,...,a<sub>m</sub>_\]_y_, which gives the approximate solution.

A direct QR of _V<sub>m</sub>_ can be implemented in O(_nm_<sup>2</sup>+_m_<sup>3</sup>) arithmetic operations by modifying the previous Toeplitz QR methods \[4,5\]. However, these methods are undesirable when \(\{a_k\}_{k=1}^m\) becomes nearly aligned or increases exponentially, which can be caused by the recursive formula (3.1). In these cases, the QR factorization of _V<sub>m</sub>_ will lose accuracy. Meanwhile, the ill-conditioned _R<sub>m</sub>_ will also make minimizing (3.2) unreliable. We therefore turn to the original Arnoldi process of infGMRES and develop an incremental recurrence that updates only the QR data needed for solution recovery. The following lemma shows the needed QR data.

Lemma 3.1 (Arnoldi process from Toeplitz QR). _For_ \(m\ge 2\)_, let V<sub>m</sub>=Q<sub>m</sub>R<sub>m</sub> be a thin QR factorization, then the Hessenberg matrix in_ (2.3) _is_<tbc>

(3.3) \(\underline{H_m}=\left[\begin{array}{ c c }
0 & 0_{1\times(m-1)} \\
\frac{\|a_1\|_2}{\|z\|_2}e_1 & R_m(1:m,2:m)R_{m-1}^{-1}
\end{array}\right].\)

<tbc>_Moreover, if y<sub>s</sub> minimizes_ (2.4)_, then the approximate solution is_

(3.4) \(\widetilde{x}(s)=\left[\frac{a_1}{\|z\|_2},[a_2,\dots,a_m]R_{m-1}^{-1}\right]y_s.\)

_Proof._ The Krylov structure and the nested QR factorizations give

\(\mathcal{U}_m=\left[\begin{array}{ c c }
z & 0 \\
\|z\|_2 & 0 \\
0 & Q_{m-1} \\
0 & 0
\end{array}\right]=\left[\begin{array}{ c c }
z & 0 \\
0 & V_{m-1} \\
0 & 0
\end{array}\right]\left[\frac{1}{\|z\|_2} & 0 \\
0 & R_{m-1}^{-1}
\end{array}\right]\)

By direct multiplication, we obtain

\(\mathcal{L}_1\mathcal{L}_0^{-1}\mathcal{U}_m=\left[\begin{array}{ c }
0_{n\times m} \\
V_m
\end{array}\right]\left[\begin{array}{ c }
1 \\
\|z\|_2 \\
R_{m-1}^{-1}
\end{array}\right]\)

