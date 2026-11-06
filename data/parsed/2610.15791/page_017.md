## Author contribution and use of AI tools

The author used AI tools to assist with literature research, mathematical analysis, code development, and manuscript preparation. The author assumes full responsibility for the content of the article.

## A Proof of Theorem 3

We first isolate the root used in the theorem and establish positivity of the parameters. We then compute the target-conditioned moments, use them to bound success for every admissible algorithm and construct a state and measurement that attain the bound.

Throughout, \(n\ge 3\) and \(1\le r<n\), with _m=n_-1, _k=n_-2, _p=r/n_, \(\upsilon=n-r\) and _h=n_-2_r_. For _n_=2, one classical comparison suffices.

### A.1 Root isolation and positivity

The constraints give \(|h|\le k\) and \(nk-h^2\ge 2k>0\). Direct substitution gives

\(F_{n,r}(1)=-3(h+k)^2=-12(n-r-1)^2.\) (12)

If _h\>_0, the coefficients of _F<sub>n,r</sub>_ have signs +,+,-,- in descending degree, so Descartes’ rule gives exactly one positive root. Equation (12) implies that the root exceeds 1. Since \(h\le n-2\), _F<sub>n,r</sub>_(3)=(21_n_+6)_k+h_(30_n_+36-27_h)\>_0, so the root is less than 3. If _h_=0, the polynomial is 3_nkz_<sup>2</sup>-6_mk_, which gives the stated radical. If _h\<_0 and _r\<n_-1, write _a_=-_h_, so 0_\<a\<k_. Then _F<sub>n,r</sub>(k/a_)=_nk(k_<sup>2</sup>_/a_<sup>2</sup>-1)_\>_0, so there is a root between 1 and _k/a_. The negative leading coefficient gives another positive root above _k/a_, and Descartes’ rule allows at most two, so the first is the smallest. At _r=n_-1, _F_<sub>_n,n_-1</sub>(_z_)=-2_k(z_-1)\(\big[\)_nz_<sup>2</sup>+(_n_-3)_z_-3_m_\(\big]\), and the bracket has one positive root, which exceeds 1 because the bracket equals -_n_ at _z_=1. The smallest positive root is then 1.

Define

\(\kappa=3k+2h\zeta,\rho=\frac{\zeta}{\sqrt{m}},\gamma=\frac{h\zeta}{\sqrt{m}\kappa},R=1-\frac{k\gamma^2}{2}.\)

For _h\>_0, \(\kappa\ge 3k\) and \(0<\gamma<1/(2\sqrt{m})\). For _h_=0, \(\gamma=0\). For _h\<_0, the selected root satisfies \(\zeta\le k/(-h)\), so \(\kappa\ge k\) and \(|\gamma|\le 1/\sqrt{m}\), which gives \(R\ge 1-k/(2m)=n/(2m)>0\). So \(\kappa>0\) and _R\>_0 in all cases.

### A.2 Target-conditioned moments

Use the real feature space \(\mathcal{H}=\mathbb{R}|0\rangle\oplus\Lambda^2\mathbb{R}^n\) with \(\phi_x=|0\rangle+\sum_{i<j}\mathrm{sgn}(x_i-x_j)e_i\wedge e_j\), where the oriented edges \(e_i\wedge e_j\), _i\<j_, are orthonormal. Let \(\omega=n^{-1/2}\sum_ie_i\), and let \(\mathcal{H}_0=\mathbb{R}|0\rangle\), \(\mathcal{V}=\{v\wedge\omega:v\perp\omega\}\) and \(\mathcal{C}=\Lambda^2(\omega^\perp)\), of dimensions 1, _m_ and _mk/_2, with orthogonal projectors _P_<sub>0</sub>, _P<sub>V</sub>_ and _P<sub>C</sub>_. For output label 1 put \(b=\sqrt{n/m}(e_1-n^{-1}\sum_ie_i)\) and \(W=\{w\in\mathbb{R}^n:w_1=0,\sum_{j\ge 2}w_j=0\}\), of dimension _k_, with an orthonormal basis _f_<sub>1</sub>_,...,f<sub>k</sub>_. Use the decomposition

\(\mathcal{H}=\mathrm{span}\{|0\rangle,b\wedge\omega\}\oplus\oplus_{a=1}^k\mathrm{span}\{f_a\wedge\omega,b\wedge f_a\}\oplus\Lambda^2W.\) (13)

