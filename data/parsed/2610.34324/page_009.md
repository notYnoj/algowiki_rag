<tbc>Indeed, \(\mathbb{E}\sqrt{g^\top Qg}\) is symmetric and concave in the eigenvalues of _Q_, whose sum is one; it is maximized at _Q=I/r_. This is where the dimension-dependent gap enters.

Each cell maximum is \(\sqrt{2n}\)-Lipschitz in the independent standard Gaussian coordinates generating _B_: the squared coefficient norm of _H<sub>U</sub>_ is \((2/n)\|UU^\top\|_F^2\le 2n\). Write _Z<sub>k</sub>_ for the maximum over the _k_-th nonempty cell. Gaussian concentration \[21, Theorem 5.2.2\] and a union bound give, for \(t\ge 0\),<tbc>

\(\mathbb{P}\big\{max_k(Z_k-\mathbb{E}Z_k)>t\big\}\le min\{1,Ke^{-c_1t^2/n}\}.\)

<tbc>Here _c_<sub>1</sub>_\>_0 is absolute, and no independence between the cell maxima is required. Integrating this bound, splitting the integral at \(\sqrt{(n/c_1)log(2K)}\), yields<tbc>

\(\mathbb{E}max_kZ_k\le max_k\mathbb{E}Z_k+C\sqrt{nlog(2K)}.\)

<tbc>Here _C_ is absolute. Since \(log(2K)\le Cr^2logn\), the contribution after division by _n_ is at most \(Cr\sqrt{logn/n}\). For any symmetric _T_, approximating each unit row within \(\delta\) changes \(\langle T,UU^\top\rangle\) by at most \(2n\delta\|T\|_\text{op}\). Since E∥_B_∥op=_O_(1), we obtain<tbc>

\(\frac{\mathbb{E}M_r(B)}{n}\le 2c_r+Cr\sqrt{\frac{logn}{n}}.\) (4)

<tbc>To compare with the zero-diagonal matrix _W_, put \(B^\circ=B-Diag(B_{11},\dots,B_{nn})\). Every feasible matrix has unit diagonal, so, pointwise,

\(M_r(B)=M_r(B^\circ)+trB.\)

As Etr_B_=0, these two maxima have the same expectation. The same identity holds when the maximum is restricted to the row net. Thus only the off-diagonal entries need to be replaced.

## 2. Replacing Gaussian entries by symmetric signs.

We now transfer the estimate to the random graph. The maximum is not smooth in the matrix entries, so we first replace it by a logarithm of a sum of exponentials. This allows a Taylor expansion as entries are replaced one at a time, following the approach for random semidefinite programs in \[17\]. On the same row net, put

\(h_U(\xi)=\frac{2}{\sqrt{n}}\sum_{i<j}\xi_{ij}u_i^\top u_j,\)<br>
\(f_\beta(\xi)=\frac{1}{n\beta}log\sum_{U\in\mathcal{N}}e^{\beta h_U(\xi)}.\)

The smooth maximum differs from _n_<sup>-1</sup>max_<sub>U</sub>h<sub>U</sub>_ by a quantity between zero and \(log|\mathcal{N}|/(n\beta)\le Crlogn/\beta\). For one coordinate, \(|\partial_{ij}h_U|\le 2/\sqrt{n}\). The fourth derivative of \(f_\beta\) is \(\beta^3/n\) times the difference between the fourth centered moment and three times the squared variance of these slopes under the exponential weights. The bound on the slopes therefore gives<tbc>

\(|\partial_{ij}^4f_\beta|\le C\beta^3/n^3.\)

<tbc>For completeness, fix one coordinate and condition on all the others in the current mixture of Gaussian and sign entries. Write \(\phi(t)\) for the resulting smooth maximum. Taylor’s formula gives

\(\phi(t)=\sum_{j=0}^3\frac{\phi^{(j)}(0)}{j!}t^j+R(t),|R(t)|\le\frac{C\beta^3}{n^3}|t|^4.\)

The derivative bound is uniform in _t_ and in the conditioned entries. A standard Gaussian _g_ and a symmetric sign \(\varepsilon\) have the same moments through degree three, while E_g_<sup>4</sup>=3 and \(\mathbb{E}\varepsilon^4=1\). Their conditional expectations therefore cancel in the polynomial part, leaving

\(|\mathbb{E}_g\phi(g)-\mathbb{E}_\varepsilon\phi(\varepsilon)|\le C\beta^3/n^3.\)

