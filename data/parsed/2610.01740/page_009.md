<tbc>At a refresh step _m_, we reconstruct _q_<sub>1_,m_</sub>_,...,q<sub>m,m</sub>_ from (3.14) and replace the generator sequence \(\{a_k\}_{k=1}^m\) by

\(a_i^\mathrm{new}=q_{m-i+1,m},i=1,\dots,m.\)

Then we continue the Arnoldi process using \(\{a_i^\mathrm{new}\}\) and \(t_m^\mathrm{new}=e_m\).

Suppose that at some step \(k\ge m\), we have

\(\left[\begin{array}{ c }
a_k^\mathrm{new} \\
\vdots \\
a_1^\mathrm{new}
\end{array}\right]=Q_kt_k^\mathrm{new},\)

while by definition this equation holds at the case _k=m_.

By the recurrence formula of \(\{a_i^\mathrm{new}\}\) and (3.5),

\(a_{k+1}^\mathrm{new}=-A_0^{-1}\sum_{i=1}^kA_ia_{k+1-i}^\mathrm{new}\)<br>
\(=-A_0^{-1}[A_1,\dots,A_k]Q_kt_k^\mathrm{new}=[u_2,\dots,u_{k+1}]t_k^\mathrm{new}.\)

Combining this with (3.17) gives

\(\left[\begin{array}{ c }
a_{k+1}^\mathrm{new} \\
a_k^\mathrm{new} \\
\vdots \\
a_1^\mathrm{new}
\end{array}\right]=\left[\begin{array}{ c }
[u_2,\dots,u_{k+1}] \\
Q_k
\end{array}\right]t_k^\mathrm{new}=Q_{k+1}S_{k+1}t_k^\mathrm{new}.\)

Thus, \(t_{k+1}^\mathrm{new}=S_{k+1}t_k^\mathrm{new}\) preserves the relationship between the generators and their coordinates, allowing the basic recurrence to continue unchanged.

With these techniques and the cancellation indicator \(\eta_m\) defined in (3.13), we propose Dynamic Toeplitz infGMRES (Dynamic TiGMRES); see Algorithm 3.2.

Refreshing at _m=m_<sub>1</sub>_,...,m<sub>r</sub>_ Arnoldi steps needs about \(2n\sum_{j=1}^rm_j^2\) extra operations, because of the effort required for computing the vectors \(\{q_{i,m_k}\},1\le i\le m_k,1\le k\le r\). Algorithm 3.2 refreshes during the first half of the iterations and when \(\eta_m\ge\tau\) thereafter, using the indicator and QR update above. The reason for refreshing every step during the first half is that precision of the early steps will deeply affect the latter steps. And the cost is \(2n\sum_{j=2}^{\lfloor p/2\rfloor} j^2\approx\frac{1}{12}np^3\), which is only about \(\frac{1}{8}\) of the time that refreshing all steps takes. In practice, a suitably chosen threshold \(\tau\) can balance stability and efficiency, as we will see in Section 6.

In the extreme case \(\tau=0\), Dynamic TiGMRES will refresh at every step, leading to its \(\frac{2}{3}np^3+\mathcal{O}(np^2+p^4)\) arithmetic and O(_np+p_<sup>3</sup>) storage complexity. We call this variant fully refreshed TiGMRES. For TOAR infGMRES, two-level orthogonalization costs O(_nm+m_<sup>3</sup>) at step _m_ \[16\]. Its _m_ dense _n_-by-_m_ basis products add 2_nm_<sup>2</sup> flops per step. The total arithmetic cost over _p_ steps is therefore \(\frac{2}{3}np^3+\mathcal{O}(np^2+p^4)\). Thus fully refreshed TiGMRES and TOAR infGMRES have identical arithmetic and storage complexity. The main difference between the two algorithms is: At step _m_, fully refreshed TiGMRES uses _G<sub>m</sub>_ as the basis to construct the full Arnoldi vectors, while TOAR infGMRES uses the orthonormal basis of the column space of _G<sub>m</sub>_ to construct them. We will see the benefit of directly using _G<sub>m</sub>_ as the basis in Section 4, where we can give a simple structured representation for _Q<sub>m</sub>_ in terms of _G<sub>m</sub>_.

