Comparing the coefficients of \(x^{m+2},m\ge 0\), we obtain

\(-\frac{1}{r}\sum_{n=0}^m\sum_{j=0}^n\sum_{j^\prime=0}^{m-n}g_{n-j}g_{m-n-j^\prime}\pi_{j+2}(\mathbf{P})\pi_{j^\prime+2}(\mathbf{P})\)<br>
\(+2\sum_{k=0}^mf_{m-k+1}\pi_{k+2}(\mathbf{P})+q_{m+2}=0,m\ge 0.\) (42)

Taking _m_=0 in (42) yields the Riccati equation of the linearization of the original system (1) at the origin,

\(q_2+2\pi_2(\mathbf{P})f_1-\frac{g_0^2}{r}\big(\pi_2(\mathbf{P})\big)^2=0,\) (43)

whose unique positive solution is given by (33). Taking \(m\ge 1\) in (42) gives

\(2\big(f_1-r^{-1}g_0^2\pi_2(\mathbf{P})\big)\pi_{m+2}(\mathbf{P})\)<br>
\(=\frac{1}{r}\sum_{n=1}^{m-1}\sum_{j=0}^n\sum_{j^\prime=0}^{m-n}g_{n-j}g_{m-n-j^\prime}\pi_{j+2}(\mathbf{P})\pi_{j^\prime+2}(\mathbf{P})\)<br>
\(+\frac{2g_0}{r}\pi_2(\mathbf{P})\sum_{j=0}^{m-1}g_{m-j}\pi_{j+2}(\mathbf{P})\)<br>
\(-2\sum_{k=0}^{m-1}f_{m-k+1}\pi_{k+2}(\mathbf{P})-q_{m+2}.\) (44)

Then the inductive definition in (34) for \(\pi_{m+2}(\mathbf{P})\), \(m\ge 1\), is obtained by dividing by \(-2\sqrt{\Delta}\) on both sides of (44) and observing that \(f_1-r^{-1}g_0^2\pi_2(\mathbf{P})=-\sqrt{\Delta}<0\) by (33). Since \(-2\sqrt{\Delta}\neq 0\), the solution is unique. Conversely, for \(\pi_m(\mathbf{P})=v_{m-1}/2\) in (26) with _v<sub>k</sub>_ as in (14), the series \(\sum_{m=2}^\infty\pi_m(\mathbf{P})x^m\) converges by (15), has \(\pi_2(\mathbf{P})>0\) by (12), and satisfies (27) by the computation in the proof of Corollary 1, since _V<sub>x</sub>_ solves (7). Hence, by the uniqueness of this solution, \(2\pi_m(\mathbf{P})=v_{m-1}\) for all \(m\ge 2\). \(\blacksquare\)

### D. Proof of Theorem 3

Let \(v_k,k\ge 1\), be Maclaurin coefficients of the derivative _V<sub>x</sub>_ of the value function _V_ in (14). By Corollary 1, _U_ in (30) solves (7) and so does _V<sub>x</sub>_ in (12). Since \(2\pi_2(\mathbf{P})=v_1\) by (33) and (12), and the level equations (42) fix all later coefficients uniquely, we see that

\(2\pi_m(\mathbf{P})=v_{m-1},m\ge 2.\) (45)

This together with (15), (35) and (36) implies that

\(|U_N(x)-V_x|=\big|\sum_{k=N+1}^\infty v_kx^k\big|\le M\sum_{k=N+1}^\infty(|x|/\rho)^k\)<br>
\(=M(1-|x|/\rho)^{-1}(|x|/\rho)^{N+1},\)

and the desired estimate (37) follows. \(\blacksquare\)

## REFERENCES

