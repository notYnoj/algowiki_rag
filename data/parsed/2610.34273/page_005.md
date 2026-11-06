A direct way to use a matrix multiplication bound for a larger complete graph is to cover its edges by triangles. The strength of this comparison depends on the matrix multiplication bound available at the time. Christandl, Vrana, and Zuiddam \[CVZ19, Corollary 1.2.6\] compared their higher-order Coppersmith–Winograd construction with the triangle-cover exponent 0.790955 obtained from Le Gall’s bound \[LG14\]; their bound 0.772943 was strictly better. The later improvement of Brand et al. \[BCK<sup>+</sup>26, Appendix C of the full version\] also uses higher-order Coppersmith–Winograd tensors and predates the OpenAI result. With \(\omega\le 9/4\) now available, the same covering argument \[CVZ19, Proposition 1.1.25\] gives the new baseline

\(\mathrm{log}_2\widetilde{\text{R}}\big(\mathsf{G}\mathsf{T}_2(K_n)\big)\le\frac{\omega}{3}\genfrac(){pt}{2}{n}{2}\le\frac{3}{4}\genfrac(){pt}{2}{n}{2}(n\ge 3).\)

Here the final inequality uses the OpenAI bound \[Ope26a\]; Theorem A.5 gives the full covering argument. This new baseline improves the preceding uniform bounds to 3/4 per edge, but still leaves a quadratic gap from \(\mathrm{MaxCut}(K_n)=\lfloor n^2/4\rfloor\). This leads to the question that motivates our work:

_Can the polynomial multiplication construction itself be extended to complete graph tensors, while keeping every vertex as a separate tensor leg?_

## 1.2 Our rank bound and its context

We answer this question affirmatively by extending the polynomial multiplication method of OpenAI \[Ope26a\] from third-order tensors to complex _n_-th order tensors. The auxiliary tensor now multiplies _n_-1 independently supplied polynomials. Extending the separation and growth arguments to these additional legs gives a stronger bound than triangle covering with the OpenAI exponent alone.

**Theorem 1.1** (complete graph tensors)**.** _For every integer_ \(n\ge 2\)_, over the complex numbers,_

\(\left\lfloor\frac{n^2}{4}\right\rfloor\le\mathrm{log}_2\widetilde{\text{R}}\big(\mathsf{G}\mathsf{T}_2(K_n)\big)\le\frac{n^2}{4}.\)

The theorem is proved as Theorem 4.11 in Subsection 4.5. The lower bound is the standard cut bound; our contribution is the upper bound. For every even _n_, the two bounds coincide. For every odd _n_, the gap between them is only 1/4. This remaining gap also motivates our second result: Theorem 1.2 shows that a specified system of these polynomial constructions and combination rules cannot improve the threshold _n_<sup>2</sup>/4.

2 compares the upper bounds on both the logarithmic asymptotic rank and the exponent per edge. Our bound gives \(\tau(K_n)\le n/(2(n-1))\). Compared with triangle covering, it decreases the logarithmic upper bound by _n(n_-3)/8 for every \(n\ge 3\). In particular, it is strictly better for every \(n\ge 4\), and the exponent per edge tends to 1/2 as _n_ grows. The maximum-cut lower bound has the same limit.

