<tbc>_Proof._ We first establish an a priori bound. By Weyl’s inequality for symmetric matrices (see, e.g., \[4, 16\]), \(|\lambda_i(t)-\lambda_i|\le t\left\|E\right\|_2\) for every _t_. Hence, for \(0\le t\le g_i/(2\left\|E\right\|_2)\), \(|\lambda_i(t)-\lambda_i|\le g_i/2\). Since, for every \(j\neq i\), \(|\lambda_i-\lambda_j|\ge g_i\), this gives

(3.6) \(|\lambda_i(t)-\lambda_j|\ge|\lambda_i-\lambda_j|-|\lambda_i(t)-\lambda_i|\ge\frac{g_i}{2}.\)

Consequently, (3.6) implies that, for \(0\le t\le g_i/(2\left\|E\right\|_2)\),

(3.7) \(\left\|(\lambda_i(t)I_{n-1}-\underline{\lambda_i})^{-1}\right\|_2\le\frac{2}{g_i}.\)

Let \(0\le t\le g_i/(4\left\|E\right\|_2)\), we next show that \(\lambda_i(t)\) remains simple. For \(j\neq i\),

\(|\lambda_i(t)-\lambda_j(t)|\ge|\lambda_i-\lambda_j|-|\lambda_i(t)-\lambda_i|-|\lambda_j(t)-\lambda_j|\ge|\lambda_i-\lambda_j|-2t\left\|E\right\|_2\ge g_i-2t\left\|E\right\|_2\ge\frac{g_i}{2},\)

where we have used in the last inequality that \(0\le t\le g_i/(4\left\|E\right\|_2)\). Thus \(\lambda_i(t)\) is simple. We now derive exact equations for the perturbed eigenpair. Let _s<sub>i</sub>(t_) be a unit eigenvector associated with \(\lambda_i(t)\) and write _s<sub>i</sub>(t_)=_a(t)s<sub>i</sub>_+<u>_S_</u><sub>i</sub>d(_t). Its eigenvalue equation is

(3.8) \((A+tE)s_i(t)=\lambda_i(t)s_i(t).\)

Multiplying (3.8) by \(\underline{S_i^\top}\) and using \(\underline{S_i^\top} As_i=0\), \(\underline{S_i^\top} A\underline{S_i}=\underline{\Lambda_i}\), and \(\underline{S_i^\top} s_i=0\), gives

(3.9) \(\left(\lambda_i(t)I_{n-1}-\underline{\Lambda_i}\right)d(t)=t\underline{S_i^\top} Es_i(t).\)

The matrix in (3.9) is invertible by (3.7), and hence

(3.10) \(d(t)=t\left(\lambda_i(t)I_{n-1}-\underline{\Lambda_i}\right)^{-1}\underline{S_i^\top} Es_i(t).\)

Because <u>_S_</u><sub>i</sub> has orthonormal columns and \(\left\|s_i(t)\right\|_2=1\), taking norms in (3.10) and applying (3.7) yields,

(3.11) \(\left\|d(t)\right\|_2\le t\frac{2}{g_i}\left\|\underline{S_i^\top} Es_i(t)\right\|_2\le\frac{2t\left\|E\right\|_2}{g_i}.\)

Since \(a(t)^2+\left\|d(t)\right\|_2^2=1\), combining (3.11) and \(\frac{2t\left\|E\right\|_2}{g_i}\le\frac{1}{2}\), gives \(|a(t)|\ge\sqrt{3}/2>1/2\).

The eigenvalue and eigenvector gap can be bounded as follows. Multiplying (3.8) by \(s_i^\top\) gives

(3.12) \(a(t)\left(\lambda_i(t)-\lambda_i-ts_i^\top Es_i\right)=ts_i^\top E\underline{S_i}d(t).\)

Because |_a(t_)|_\>_1/2, combining (3.12) and (3.11) gives,

\(\left|\lambda_i(t)-\lambda_i-ts_i^\top Es_i\right|\le\frac{1}{|a(t)|}t\left\|E\right\|_2\left\|d(t)\right\|_2\le 2t\left\|E\right\|_2\left\|d(t)\right\|_2\le\frac{4\left\|E\right\|_2^2}{g_i}t^2.\)

On the other hand,

(3.13) \(\left\|s_i(t)-s_i-t\underline{S_i}R_0\underline{S_i^\top} Es_i\right\|_2\le|a(t)-1|+\left\|d(t)-tR_0\underline{S_i^\top} Es_i\right\|_2,\)

where \(R_0:=\left(\lambda_iI_{n-1}-\underline{\Lambda_i}\right)^{-1}\). We bound the two terms on the right-hand side of (3.13) separately. Choose the sign of _s<sub>i</sub>(t_) so that _a(t)\>_0. Since \(a(t)^2+\left\|d(t)\right\|_2^2=1\),

(3.14) \(0\le 1-a(t)=\frac{\left\|d(t)\right\|_2^2}{1+a(t)}\le\left\|d(t)\right\|_2^2\le\frac{4t^2\left\|E\right\|_2^2}{g_i^2}.\)

