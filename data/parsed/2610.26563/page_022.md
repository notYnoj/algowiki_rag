## 7.2 Round-off analysis of the bilinear algorithms

The approximation bound does not account for errors made while evaluating the algorithm in finite precision. We distinguish sensitivity to the input data from the additional errors introduced by the factorization.

A bilinear algorithm is represented by a triple of factor matrices \(\Xi=(A,B,C)\) with _r_ columns. Writing their columns as \(a_\ell,b_\ell,c_\ell\), its evaluation is

\(z=C\big((A^Tx)\odot(B^Ty)\big)=\sum_{\ell=1}^rc_\ell(a_\ell^Tx)(b_\ell^Ty).\) (117)

Here \(\odot\) denotes entrywise multiplication: \((u\odot v)_\ell=u_\ell v_\ell\).

**Definition 24** (Spectral-norm product)**.** _For a bilinear algorithm_ \(\Xi=(A,B,C)\)_, define_

\(\sigma(\Xi)=\|A\|_2\|B\|_2\|C\|_2.\) (118)

The factorization specifies two linear input maps, the entrywise product, and a linear output map. It does not prescribe how the linear maps are applied. Their implementations may use different summation orders, compensated summation, or factorizations of the coefficient matrices rather than direct matrix–vector multiplication. These choices can affect round-off error \[4, 21\].

We analyze the propagation of errors in the inputs and outputs of these stages. Specifically, we hold _A,B,C_ exact and model each stage as an exact operation followed by rounding its result at the working precision. The errors in the intermediate vectors _A<sup>T</sup>x_, _B<sup>T</sup>y_, and their entrywise product depend on the chosen factorization. In contrast, perturbing the original inputs and then evaluating exactly depends only on the bilinear map, and rounding the final result is relative to that result.

The next lemma shows how these norms bound errors introduced in the intermediate vectors. It keeps the contribution of the original input perturbations separate, using the norm of the bilinear map rather than replacing it by \(\sigma(\Xi)\). The latter replacement also gives a valid upper bound, as in \[21, Theorem 9.1\], but does not distinguish input sensitivity from errors caused by the algorithm.

**Lemma 9** (Input sensitivity and intermediate round-off)**.** _Let_ \(\Xi=(A,B,C)\) _evaluate the bilinear map_ L _in_ (117)_, and let z_=L(_x,y). For_ \(0<\epsilon<1\)_, suppose_

\(\widehat{x}=x+\delta x,\widehat{y}=y+\delta y,\|\delta x\|_2\le\epsilon\|x\|_2,\|\delta y\|_2\le\epsilon\|y\|_2.\) (119)

_Let_ fl _satisfy_ \(\|\mathrm{fl}(v)-v\|_2\le\epsilon\|v\|_2\) _for every rounded vector, and compute_

\(\widehat{u}=\mathrm{fl}(A^T\widehat{x}),\widehat{v}=\mathrm{fl}(B^T\widehat{y}),\widehat{w}=\mathrm{fl}(\widehat{u}\odot\widehat{v}),\widehat{z}=\mathrm{fl}(C\widehat{w}).\) (120)

_Then_

\(\|\widehat{z}-z\|_2\le\big((1+\epsilon)^3-1\big)\big[\|\mathcal{L}\|+(1+\epsilon)^3\sigma(\Xi)\big]\|x\|_2\|y\|_2.\) (121)

_Proof._ First fix the supplied inputs \(\widehat{x},\widehat{y}\). Set \(u=A^T\widehat{x}\), \(v=B^T\widehat{y}\), \(\delta u=\widehat{u}-u\), \(\delta v=\widehat{v}-v\), and \(\delta w=\widehat{w}-\widehat{u}\odot\widehat{v}\). Then

\(\widehat{w}-u\odot v=\delta u\odot v+u\odot\delta v+\delta u\odot\delta v+\delta w.\) (122)

The rounding bounds give \(\|\delta u\|_2\le\epsilon\|u\|_2\), \(\|\delta v\|_2\le\epsilon\|v\|_2\), and \(\|\delta w\|_2\le\epsilon(1+\epsilon)^2\|u\|_2\|v\|_2\). Using \(\|u\odot v\|_2\le\|u\|_2\|v\|_2\) yields

\(\|C\widehat{w}-\mathcal{L}(\widehat{x},\widehat{y})\|_2\le\|C\|_2\big(2\epsilon+\epsilon^2+\epsilon(1+\epsilon)^2\big)\|u\|_2\|v\|_2\)<br>
\(\le\big((1+\epsilon)^3-1\big)\|C\|_2\|A\|_2\|B\|_2\|\widehat{x}\|_2\|\widehat{y}\|_2.\) (123)

This is the error introduced by the three intermediate roundings. The original input perturbations instead satisfy, by bilinearity,

\(\|\mathcal{L}(\widehat{x},\widehat{y})-\mathcal{L}(x,y)\|_2\le(2\epsilon+\epsilon^2)\|\mathcal{L}\|\|x\|_2\|y\|_2.\) (124)

Finally, rounding \(C\widehat{w}\) and adding and subtracting \(\mathcal{L}(\widehat{x},\widehat{y})\) gives

\(\|\widehat{z}-z\|_2\le(1+\epsilon)\|C\widehat{w}-\mathcal{L}(\widehat{x},\widehat{y})\|_2\)<br>
\(+(1+\epsilon)\|\mathcal{L}(\widehat{x},\widehat{y})-z\|_2+\epsilon\|z\|_2.\) (125)

Use \(\|\widehat{x}\|_2\|\widehat{y}\|_2\le(1+\epsilon)^2\|x\|_2\|y\|_2\) and \(\|z\|_2\le\|\mathcal{L}\|\|x\|_2\|y\|_2\). The coefficient of \(\|\mathcal{L}\|\) is \((1+\epsilon)(2\epsilon+\epsilon^2)+\epsilon=(1+\epsilon)^3-1\), which proves the bound.

