\(\|\mathbf{u}_2-\mathbf{v}_2\|+\|\mathbf{u}_2\|\), so that \(\|\mathbf{u}_2-\mathbf{v}_2\|\ge\|\|\mathbf{u}_2\|-\|\mathbf{v}_2\|\). Squaring both nonnegative sides gives

\(\|\mathbf{u}_2-\mathbf{v}_2\|^2\ge(\|\mathbf{u}_2\|-\|\mathbf{v}_2\|)^2.\) (7)

Combining the four relations,

\(\|\mathbf{q}-\mathbf{x}\|^2=^{(6)}\|\mathbf{u}_1-\mathbf{v}_1\|^2+\|\mathbf{u}_2-\mathbf{v}_2\|^2\ge^{(7)}\|\mathbf{u}_1-\mathbf{v}_1\|^2+(\|\mathbf{u}_2\|-\|\mathbf{v}_2\|)^2=^{(5)}\|\mathbf{V}(\mathbf{u}_1-\mathbf{v}_1)\|^2+(\|\mathbf{u}_2\|-\|\mathbf{v}_2\|)^2=^{(4)}\|\ell(\mathbf{q})-\ell(\mathbf{x})\|^2.\)

Taking the square root of both nonnegative sides proves the claim.

Proposition 2 turns the lifted projection into an exclusion test. Specifically, if \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|>U\), then \(\|\mathbf{q}-\mathbf{x}\|>U\) as well, so that excluding **x** never removes a vector within _U_. However, the test must take a form that tensor cores evaluate quickly. This form is an inner product, because tensor cores multiply matrices and thus compute the inner products of many pairs of vectors at once. We therefore rewrite the test in terms of one inner product per pair. To this end, expanding the squared norm of a difference with \(a(\mathbf{x}):=\|\ell(\mathbf{x})\|^2\) gives

\(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|^2=a(\mathbf{q})+a(\mathbf{x})-2\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle.\) (8)

Since both sides of the test \(\|\ell(\mathbf{q})-\ell(\mathbf{x})\|\le U\) are nonnegative, the test holds exactly when the squared test holds. By Eq. (8), the squared test reads

\(a(\mathbf{q})+a(\mathbf{x})-2\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle\le U^2.\)

Moving the inner product to the right-hand side and _U_<sup>2</sup> to the left-hand side gives \(a(\mathbf{q})+a(\mathbf{x})-U^2\le 2\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle\). Dividing by 2 and moving _a_(**x**)/2 to the right-hand side finally gives the equivalent test

\(\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle-\frac{a(\mathbf{x})}{2}\ge\frac{a(\mathbf{q})-U^2}{2}.\) (9)

In this form, the right-hand side depends only on the query, so that CertEx computes it once per query. Similarly, on the left-hand side, _a_(**x**) depends only on the database vector and is computed once when the retina is built. The test of one pair therefore costs one inner product and one comparison, so that one matrix product on the tensor cores tests all pairs.

## 3.4 Certified Half-Precision Retina

To evaluate Eq. (9) for all vectors in one tensor-core pass, CertEx stores each lifted projection in half precision inside<tbc>

<tbc>its retina vector. However, rounding to half precision may underestimate the inner product, which overestimates the bound and can discard a true neighbor. To bound this effect, denote by \(\tilde{\ell}(\cdot)\) the rounding of \(\ell(\cdot)\) to the nearest half- precision numbers and by \(\delta(\cdot):=\|\ell(\cdot)-\tilde{\ell}(\cdot)\|\) its rounding error. Splitting the inner product into its rounded part and two error terms and applying the Cauchy-Schwarz inequality to the error terms gives

\(\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle\le\langle\tilde{\ell}(\mathbf{q}),\tilde{\ell}(\mathbf{x})\rangle+\delta(\mathbf{q})\|\ell(\mathbf{x})\|+\|\tilde{\ell}(\mathbf{q})\|\delta(\mathbf{x}).\text{(10)}\)

Eq. (10) follows from the exact split

\(\langle\ell(\mathbf{q}),\ell(\mathbf{x})\rangle=\langle\tilde{\ell}(\mathbf{q}),\tilde{\ell}(\mathbf{x})\rangle+\langle\ell(\mathbf{q})-\tilde{\ell}(\mathbf{q}),\ell(\mathbf{x})\rangle+\langle\tilde{\ell}(\mathbf{q}),\ell(\mathbf{x})-\tilde{\ell}(\mathbf{x})\rangle,\)

since the Cauchy-Schwarz inequality bounds the last two terms by \(\delta(\mathbf{q})\|\ell(\mathbf{x})\|\) and \(\|\tilde{\ell}(\mathbf{q})\|\delta(\mathbf{x})\). A second error arises in the tensor cores, which multiply half-precision operands exactly but accumulate the products in fp32. This accumulation adds an error of at most \(\gamma\) times the sum of the absolute products, where \(\gamma\) depends only on the padded length _L_ of the retina vectors \[10, 29\].

CertEx folds both error terms into the same dot product, in the manner of floating-point filters \[59\]. Specifically, each database retina vector \(\hat{\mathbf{x}}\) appends four coordinates to \(\tilde{\ell}(\mathbf{x})\), which form its certificate: upper bounds <o>_n_</o><sub>**x**</sub> on \(\|\ell(\mathbf{x})\|\) and <o>_e_</o><sub>**x**</sub> on the rounding error \(\delta(\mathbf{x})\) plus an accumulation term, and a high part _h_<sub>**x**</sub> and a low part _l_<sub>**x**</sub> of _a_(**x**)/2 (the bars mark upper bounds). Correspondingly, the retina vector \(\hat{\mathbf{q}}\) of a query appends an upper bound <o>_e_</o><sub>**q**</sub> on \(\delta(\mathbf{q})\), an upper bound <o>_n_</o><sub>**q**</sub> on \(\|\tilde{\ell}(\mathbf{q})\|\), a coefficient \(1-\varepsilon\) with \(\varepsilon\) slightly larger than \(\gamma\), and a one. The two retina vectors thus read

\(\hat{\mathbf{x}}^\top=[\tilde{\ell}(\mathbf{x})^\top,\overline{n_\mathbf{x}},\overline{e_\mathbf{x}},-h_\mathbf{x},-l_\mathbf{x}],\hat{\mathbf{q}}^\top=[\tilde{\ell}(\mathbf{q})^\top,\overline{e_\mathbf{q}},\overline{n_\mathbf{q}},1-\varepsilon,1],\)

where the columns show which coordinates multiply each other. Denote by _P_ the exact inner product of \(\hat{\mathbf{q}}\) and \(\hat{\mathbf{x}}\). By construction,

\(P=\langle\tilde{\ell}(\mathbf{q}),\tilde{\ell}(\mathbf{x})\rangle+\overline{e_\mathbf{q}}\overline{n_\mathbf{x}}+\overline{n_\mathbf{q}}\overline{e_\mathbf{x}}-(1-\varepsilon)h_\mathbf{x}-l_\mathbf{x}.\) (11)

In Eq. (11), the products <o>_e_</o><sub>**q**</sub><o>_n_</o><sub>**x**</sub> and <o>_n_</o><sub>**q**</sub><o>_e_</sub><sub>**x**</sub> bound the two error terms of Eq. (10) from above, whereas _h_<sub>**x**</sub>+_l_<sub>**x**</sub> represents _a_(**x**)/2. Instead of _P_, the tensor cores return the value \(\widehat{P}\), which results from exact products of the half-precision coordinates and an accumulation of these products in fp32. The test of CertEx compares this value with a threshold: CertEx keeps a vector if and only if \(\widehat{P}\) satisfies

\(\widehat{P}\ge\theta(\mathbf{q}):=\frac{a(\mathbf{q})-U^2}{2}-\mu(\mathbf{q}),\) (12)

