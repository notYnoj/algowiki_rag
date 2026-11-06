<tbc>Taking expectation over the other entries and telescoping over the \(\genfrac(){pt}{2}{n}{2}\) replacements gives total error at most \(C\beta^3/n\), with a constant independent of _r_. Adding the smoothing errors and the _O(n_<sup>-3</sup>) expected net errors gives<tbc>

\(\left|\frac{\mathbb{E}M_r(W)-\mathbb{E}M_r(B)}{n}\right|\le C\left(\frac{rlogn}{\beta}+\frac{\beta^3}{n}+n^{-3}\right).\)

<tbc>Here both ensembles have bounded expected operator norm. The choice \(\beta=(nrlogn)^{1/4}\) balances the smoothing and replacement errors; applying (4) now gives the desired expectation bound. To pass to a probability bound, observe that changing one sign changes _M<sub>r</sub>(W)/n_ by at most 4_n_<sup>-3/2</sup>. The bounded-differences inequality \[21, Theorem 2.9.1\] gives

\(\mathbb{P}\{M_r(W)-\mathbb{E}M_r(W)>nt\}\le e^{-cnt^2}.\)

Choosing \(t=C\sqrt{logn/n}\) proves (2), with failure probability any prescribed negative power of _n_ after increasing _C_. Matching the third moments is essential to this error estimate and is available here because the graph density is 1/2.

## 3. A feasible matrix near the spectral bound.

We seek a positive semidefinite matrix concentrated on eigenvectors whose eigenvalues are close to 2. Its diagonal must also be close to constant, so that enforcing unit diagonal changes the objective only slightly. The local semicircle law provides this control. Set _d=n_<sup>-1/5</sup> and _z_=2+_d_. Spectral-edge rigidity \[3, Theorem 2.9\] gives \(\lambda_{max}(W)\le 2+d/4\) with probability tending to one. On this event let

\(P=(zI-W)^{-4},D=Diag(P_{11},\dots,P_{nn}),\)<br>
\(X=D^{-1/2}PD^{-1/2}.\)

The matrix _P_ assigns weight \((z-\lambda)^{-4}\) to an eigenvector with eigenvalue \(\lambda\), favouring those near the upper spectral edge. Diagonal normalization gives \(X\unknown 0\) and diag_X_=**1**. We will check both its objective value and the mean penalty in _F<sub>n</sub>_.

Write \(Z_n=O_\prec(a_n)\) when, for every fixed \(\eta,D_0>0\), \(\mathbb{P}\{|Z_n|>n^\eta a_n\}\le n^{-D_0}\) for all sufficiently large _n_, including maxima over the indicated indices. Put \(q(w)=\int(w-x)^{-1}d\mu_\mathrm{sc}(x)\), where \(\mu_\mathrm{sc}\) is the semicircle law, with density \(\sqrt{4-x^2}/(2\pi)\) on \[-2,2\]. We justify its application on the contour explicitly. The matrix _W_ satisfies \[3, Definition 2.2\]: its upper-triangular entries are independent and centered, the off-diagonal variances are 1_/n_, and every moment of \(\sqrt{n}W_{ij}\) is uniformly bounded. The variance condition there is \(\mathbb{E}|W_{ij}|^2=n^{-1}(1+O(\delta_{ij}))\), where \(\delta_{ij}\) is the Kronecker delta; it permits zero diagonal variance.

Let \(\Gamma=\{w:|w-z|=d/4\}\). On its upper semicircle, \(\kappa=\Re w-2\in[3d/4,5d/4]\) and \(0<\unknown w\le d/4\). Taking, for example, \(\tau=1/10\), we have \(3d/4\ge n^{-2/3+\tau}\) for large _n_. Thus these points belong to the domain \(\{E+i\eta:|E|\ge 2+n^{-2/3+\tau},\eta>0\}\) of \[3, Theorem 10.3\]. This theorem imposes no positive lower cutoff on \(\eta\), so net points may approach the real endpoints arbitrarily closely. Its entrywise estimate, with \(\kappa+\unknown w\unknown d\), gives

\([(wI-W)^{-1}]_{ii}=q(w)+O_\prec(n^{-1/2}d^{-1/4})\)

uniformly in the deterministic upper-semicircle point _w_ and in _i_. The source uses (_W-wI_)<sup>-1</sup> and the opposite sign for the semicircle transform; changing both signs gives our convention.

To obtain a simultaneous bound, choose a deterministic _n_<sup>-3</sup>-net of the upper semicircle using points with positive imaginary part, also approximating its two real endpoints. It has at most _Cn_<sup>3</sup> points. A union bound over the net and the _n_ diagonal entries preserves stochastic domination, since the local law permits any prescribed polynomial failure exponent. On the rigidity event above, the closed disk bounded by \(\Gamma\) lies at distance at least _d/_2 from the spectrum of _W_. For _R(w_)=(_wI-W_)<sup>-1</sup> and points _w,v_ in this disk, the resolvent identity gives

\(\|R(w)-R(v)\|_\mathrm{op}\le 4d^{-2}|w-v|.\)

