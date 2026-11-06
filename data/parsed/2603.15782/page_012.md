A procedure that solves the problem above will be called an "`Oracle`", and the spectral norm \(\|N\|\) of matrix _N_ will be called the _width_ of the oracle.

First, we will handle an easy case that returns early if triggered.

Let us denote \(S=\{i\in V:\|\tilde{v}_i\|^2\le 4/c\}\). We have \(\sum_{i\in V}\|\tilde{v}_i\|^2=\mathtt{Tr}(\tilde{V}^T\tilde{V})=n\) and thus \(|S|\ge(1-c/4)n\).

**Proposition 10.** _Suppose that_ \(K_S\bullet\tilde{X}<\frac{\xi n^2}{4}\) _. Then setting_ \(y_i=-\frac{\alpha}{n}\) _for all_ \(i\in V\) , \(z_S=\frac{2\alpha}{\xi n^2}\) , \(z_{S^\prime}=0\) _for all_ \(S'\neq S\)_, and_ \(\lambda_{ij}=0\) _gives a valid output of the oracle with width_ \(\rho=O(\frac{\alpha}{n})\) _assuming that parameters_ \(\tau,\gamma\) _in Theorem 9 satisfy_ \(\gamma\le\frac{1}{2}\) _and_ \(\tau\le\frac{\xi}{2}\) .

_Proof._ Denote \(z_{ij}=\|v_i-v_j\|^2\) and \(\tilde{z}_{ij}=\|\tilde{v}_i-\tilde{v}_j\|^2\). We know that \(\tilde{Z}:=\sum_{ij}\tilde{z}_{ij}=K_S\bullet\tilde{X}<\frac{\xi n^2}{4}\) where the sum is over \(i,j\in S\) with _i\<j_. Also, \(|z_{ij}-\tilde{z}_{ij}|\le\gamma(\tilde{z}_{ij}+\tau)\) for all _i,j_. This implies that

\(K_S\bullet X=\sum_{i,j\in S:i<j}z_{ij}<\tilde{Z}+\gamma\tilde{Z}+\frac{n^2}{2}\gamma\tau\le(1+\gamma)\frac{\xi n^2}{4}+\frac{n^2}{2}\gamma\tau\le\frac{\xi n^2}{2}\)

Note that \(N=-\frac{\alpha}{n}I+\frac{2\alpha}{\xi n^2}K_S\). We have \(\sum_iy_i+\xi n^2\sum_{S^\prime} z_{S^\prime}=n\cdot(-\frac{\alpha}{n})+\xi n^2\cdot\frac{2\alpha}{\xi n^2}=\alpha\) and \(N\bullet X=-\frac{\alpha}{n}I\bullet X+\frac{2\alpha}{\xi n^2}(K_S\bullet X)\le-\frac{\alpha}{n}\cdot n+\frac{2\alpha}{\xi n^2}\cdot\frac{\xi n^2}{2}=0\), as desired. Also, \(\|N\|\le\|-\frac{\alpha}{n}I\|+\|\frac{2\alpha}{\xi n^2}K_S\|=O(\frac{\alpha}{n})\).

From now on we make the following assumption.

**Assumption 1.** \(\|\tilde{v}_i\|^2\le 4/c\) _for all_ \(i\in S\), \(|S|\ge(1-c/4)n\) _and_ \(\sum_{i,j\in S:i<j}\|\tilde{v}_i-\tilde{v}_j\|^2=K_S\bullet\tilde{X}\ge\frac{\xi n^2}{4}\) .

Let us set \(y_i=\frac{\alpha}{n}\) for all \(i\in V\) and \(z_{S^\prime}=0\) for all \(S'\), then \(\sum_iy_i+\xi n^2\sum_{S^\prime} z_{S^\prime}=\alpha\). Note that \(N=\frac{\alpha}{n}I+\sum_pf_pT_p-\sum_{ij}\lambda_{ij}L_{ij}\) and \(\frac{\alpha}{n}I\bullet X=\frac{\alpha}{n}\mathtt{Tr}(X)=\alpha\), so condition \(N\bullet X\le 0\) is equivalent to \((\sum_pf_pT_p-\sum_{ij}\lambda_{ij}L_{ij})\bullet X\le-\alpha\). With a variable substitution, our goal thus becomes as follows.<sup>3</sup>

_Find either_

_(i) a matrix N of the form_ \(N=\sum_pf_pT_p-\sum_{ij}\lambda_{ij}L_{ij}\) _where_ \(f_p\ge 0\), \(\lambda_{ij}\ge 0\), \(\mathrm{deg}(G^\lambda)\le w|_V\) _and_ \(\lambda_{ij}\le w(ij)\)_, and_ \(N\bullet X\le-\alpha\)_; or_

_(ii) a_ \(\Theta(1)\)_-balanced element cut of value at most_ \(\kappa\alpha\).

A procedure for solving this problem will be called a "reduced Oracle", and the norm \(\|N\|\) will be its width. Note that the width of the full oracle is at most \(\frac{\alpha}{n}\) plus the width of the reduced oracle, since \(\|\frac{\alpha}{n}I+N\|\le\frac{\alpha}{n}+\|N\|\). We will show the following.

**Theorem 11.** _Assume that the reduced oracle has the same input as_ Oracle _that additionally satisfies Assumption 1. Then it can be implemented so that it_

• _runs in_ \(m^{1+o(1)}n^{O(\varepsilon)}\mathrm{polylog}(n)\) _time and has parameter_ \(\kappa=\Theta(\sqrt{\beta}/\varepsilon)\)_, assuming that parameters_ \(\Gamma\) _and_ \(\beta\in[1,O(\sqrt{\mathrm{log}n})]\) _of the padded bound are known;_<tbc>

• _runs in_ \(O\left(n^{O(\varepsilon)}\cdot T_\mathrm{maxflow}(m,m)\cdot\mathrm{polylog}(n)\right)\) _time and has parameter_ \(\kappa=\Theta(\sqrt{\mathrm{log}n/\varepsilon})\).

_In both cases the oracle succeeds (i.e. produces either output (i) or (ii)) with probability at least_ \(1-n^{-\Theta(1)}\)_. Both cases use_ \(\tau=\Theta(1)\) _and_ \(\gamma=\Omega(1/\mathrm{log}n)\)_. Matrix N satisfies_ \(\|N\|\le\alpha n^{-1+O(\varepsilon)}\mathrm{polylog}(n)\) _and has_ \(O(mn^{O(\varepsilon)}\mathrm{polylog}(n))\) _non-zero entries._

Assuming this result, we can easily prove Theorems 1 and 5.

<sup>3</sup>An analogous specification (for the balanced edge separator problem) appeared in \[24\], but in \[24\] it was further assumed that _S=V_ . However, the justification for this simplification in Appendix A.2 is incorrect: it works if the oracle returns a feedback matrix, but does not work if the oracle returns a cut. A similar simplification claim also appeared in \[40\]. In this work we do not assume that _S=V_ .

