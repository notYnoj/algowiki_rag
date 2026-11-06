_Proof of Theorem 7._ Apply Theorem 8 to problem (1) by treating its Gram matrix _X_ as one \(n\times n\) block and every finite-cost scalar variable _x<sub>z</sub>_ as a \(1\times 1\) block. Maintain only the Gram-matrix block, so K consists of this single block. The constraints _X<sub>ii</sub>_=1 imply `Tr`(_X_)=_n_, and hence we take _R=n_ and _n_<sub>max</sub>=_n_. The update for the maintained block in Algorithm 2 is then exactly the update in Algorithm 1.

For the Gram-matrix block, the matrix _N_<sup>(_t_)</sup>=-_S<sub>X</sub>(y_<sup>(_t_)</sup>) is precisely the feedback matrix \(\mathtt{diag}(y)+\sum_pf_pT_p+\sum_Sz_SK_S-\sum_{ij}\lambda_{ij}L_{ij}\) used in Algorithm 1. Positive semidefiniteness of the unmaintained \(1\times 1\) slacks says exactly that \(\mathrm{deg}(G^\lambda)\le w|_V\) and \(\lambda_{ij}\le w(ij)\), while \(b^\top y\ge\alpha\) is the displayed lower bound on the dual objective. Thus the oracle conditions in the two algorithms agree. Finally, |K|=1, so Theorem 8 gives the lower bound \(\alpha-\delta\); substituting _R=n_ and _n_<sub>max</sub>=_n_ also gives \(\eta=\frac{\delta}{2n\rho^2}\), \(T=\left\lceil\frac{4n^2\rho^2\mathrm{ln}n}{\delta^2}\right\rceil\). These are exactly the conclusion and parameter choices of Theorem 7.

## 4 Implementation of Algorithm 1

Consider the matrix _X=X_<sup>(_t_)</sup> computed at the _t_-th step of Algorithm 1. It can be seen that _X_ is positive semidefinite, so we can consider its Gram decomposition: _X=V<sup>T</sup>V_ . Let _v_<sub>1</sub>_,...,v<sub>n</sub>_ be the columns of _V_ ; clearly, they uniquely define _X_. Note that computing _v_<sub>1</sub>_,...,v<sub>n</sub>_ requires matrix exponentiation, which is a tricky operation because of accuracy issues. Furthermore, even storing these vectors requires \(\Theta(n^2)\) space and thus \(\Omega(n^2)\) time, which is too slow for our purposes. To address these issues, Arora and Kale compute approximations \(\tilde{v}_1,\dots,\tilde{v}_n\) to these vectors using the following result.

**Theorem 9** (\[3, Lemma 7.2\])**.** _For any constant c\>_0 _there exists an algorithm that does the following: given values_ \(\gamma\in(0,\frac{1}{2})\), \(\lambda_\mathrm{max}>0\), \(\tau=O(n^{3/2})\) _and (implicit) symmetric matrix_ \(A\in\mathbb{R}^{n\times n}\) _of spectral norm_ \(\|A\|\le\lambda_\mathrm{max}\)_, it computes a matrix_ \(\tilde{V}\in\mathbb{R}^{d\times n}\) _with column vectors_ \(\tilde{v}_1,\dots,\tilde{v}_n\) _of dimension_ \(d=O(\frac{\mathrm{log}n}{\gamma^2})\) _such that matrix_ \(\tilde{X}=\tilde{V}^T\tilde{V}\) _has trace n, and with probability at least_ 1-_n_<sup>-_c_</sup>_, one has_

\(\|\|\tilde{v}_i\|^2-\|v_i\|^2|\le\gamma(\|\tilde{v}_i\|^2+\tau)\forall i\) (6a)

\(\|\|\tilde{v}_i-\tilde{v}_j\|^2-\|v_i-v_j\|^2|\le\gamma(\|\tilde{v}_i-\tilde{v}_j\|^2+\tau)\forall i,j\) (6b)

_where v_<sub>1</sub>_,...,v<sub>n</sub> are the columns of a Gram decomposition of_ \(X=n\cdot\frac{\mathrm{exp}(A)}{\mathtt{Tr}(\mathrm{exp}(A))}\)_. The complexity of this algorithm equals the complexity of computing kd matrix-vector products of the form_ \(A\cdot u\), \(u\in\mathbb{R}^n\)_, where_ \(k=O(\mathrm{max}\{\lambda_\mathrm{max}^2,\mathrm{log}\frac{n^{5/2}}{\tau}\})\).

If we use this theorem inside Algorithm 1, then the matrices _A_ will have the form \(A=\eta\sum_{r=1}^{t-1}N^{(r)}\); their spectral norm will be bounded by \(\eta\rho T\). Therefore, we can set \(\lambda_\mathrm{max}=\eta\rho T=\Theta(\frac{\rho n\mathrm{log}n}{\alpha})\) in Theorem 9. Parameters \(\gamma\) and \(\tau\) will be specified later.

We will write \((v_1,\dots,v_n)\approx_{\gamma,\tau}\) (\(\tilde{v}_1,\dots,\tilde{v}_n\)) if conditions (6) hold. We now need to show how to solve the following problem.

Input: (unobserved) matrix \(V\in\mathbb{R}^{n\times n}\) with columns \(v_1,\dots,v_n\in\mathbb{R}^n\) and (observed) matrix \(\tilde{V}\in\mathbb{R}^{d\times n}\) with columns \(\tilde{v}_1,\dots,\tilde{v}_n\in\mathbb{R}^d\) such that \((v_1,\dots,v_n)\approx_{\gamma,\tau}\) (\(\tilde{v}_1,\dots,\tilde{v}_n\)) and \(\mathtt{Tr}(X)=\mathtt{Tr}(\tilde{X})=n\) where _X=V<sup>T</sup>V_ and \(\tilde{X}=\tilde{V}^T\tilde{V}\).<br>
Output: either<br>
(i) matrix _N_ of the form \(N=\mathtt{diag}(y)+\sum_pf_pT_p+\sum_Sz_SK_S-\sum_{ij}\lambda_{ij}L_{ij}\) where \(f_p\ge 0\), \(z_S\ge 0\), \(\sum_iy_i+\xi n^2\sum_Sz_S\ge\alpha\), \(\lambda_{ij}\) are non-negative variables with \(\mathrm{deg}(G^\lambda)\le w|_V\) and \(\lambda_{ij}\le w(ij)\), and \(N\bullet X\le 0\); or<br>
(ii) a \(\Theta(1)\)-balanced element cut of value at most \(\kappa\alpha\).

