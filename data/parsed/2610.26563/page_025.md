The same calculation applies to _V<sub>t</sub>,W<sub>t</sub>_. Thus every exact construction from a balanced tripartition set satisfies

\(\left(\frac{n+1}{n}\right)^{3N/2}\le\frac{\sigma(\Xi(1))}{\sigma_c}\le\left(\frac{n+1+(n+1)^{2/3}}{n}\right)^{3N/2},lim_{n\rightarrow\infty}\frac{\sigma(\Xi(1))}{\sigma_c}=1(N\text{fixed}).\) (136)

The upper bound equals \(\sigma(\Xi(1))/\sigma_c\) for the weighted embedding of Definition 12 applied to the same tripartition set S. The weighted embedding uses local dimension _n_+2, whereas the selected aggregates use dimension _n_+1 with only the corrections indexed by Q. By (96), the corrected factors retain selected column blocks of the weighted factors, up to column signs. Deleting the other blocks reduces the multiplication count and cannot increase their spectral norms, whether the resulting construction is exact or approximate. For an exact construction from complete tripartitions of unequal shapes, the same argument replaces 3_N_ by max_<sub>t</sub>|U<sub>t</sub>_|+max_<sub>t</sub>|V<sub>t</sub>_|+max_<sub>t</sub>|W<sub>t</sub>_|.

The smallest exponent in each factor determines its growth as \(\lambda\rightarrow 0\). Their sum is -_h_ from (110), so the spectral-norm product grows as \(\lambda^{-h}\). The parameter choice also requires its leading coefficient.

**Definition 25** (Leading spectral coefficient)**.** _For the factorization_ \(\Xi(\lambda)\) _and growth exponent h, define the constant_ \(\sigma_0\)_, when the limit exists and is positive, by_<tbc>

\(\sigma_0=lim_{\lambda\rightarrow 0}\lambda^h\sigma(\Xi(\lambda)).\) (137)

<tbc>For the first maximum in (131), denote by _K<sub>A,t</sub>_ the coefficient of \(\lambda^{2a_t}\), and set _a_<sub>∗</sub>=min_<sub>t</sub>a<sub>t</sub>_ and _K<sub>A</sub>_=max_<sub>a<sub>t</sub>=a_<sub>∗</sub></sub>_K<sub>A,t</sub>_, with _K<sub>B</sub>,K<sub>C</sub>_ defined analogously. Then<tbc>

\(\lambda^{-2a_*}\|A(\lambda)\|_2^2=max_tK_{A,t}\lambda^{2(a_t-a_*)}=K_A\) (138)

<tbc>for all sufficiently small positive \(\lambda\), as every term with _a<sub>t</sub>\>a_<sub>∗</sub> tends to zero and is eventually smaller than the positive constant _K<sub>A</sub>_. Taking square roots gives \(\|A(\lambda)\|_2=\sqrt{K_A}\lambda^{a_*}\), and multiplying the three norm identities yields

\(\sigma(\Xi(\lambda))=\sigma_0\lambda^{-h},\sigma_0=(K_AK_BK_C)^{1/2}\) (139)

for all sufficiently small positive \(\lambda\), with the construction and _n_ fixed.

For these factors, the exponent _h_ also describes attainable amplification of intermediate rounding errors under the stated model. Fix a column \(\ell\) belonging to the main aggregate. In its _t_th input block, the column of \(A(\lambda)\) has norm \(\lambda^{a_t}(n/(n+1))^{|U_t^c|/2}\), since \(QQ^T=I-1_{n+1}1_{n+1}^T/(n+1)\); the corresponding formulas hold for \(B(\lambda)\) and \(C(\lambda)\). Each block is nonzero, so

\(0<lim_{\lambda\rightarrow 0}\lambda^h\|a_\ell(\lambda)\|_2\|b_\ell(\lambda)\|_2\|c_\ell(\lambda)\|_2<\infty.\) (140)

By (126), rounding just this product can therefore cause an error proportional to \(\epsilon\lambda^{-h}\) for suitable unit inputs. Thus the power of \(\lambda\) in the bound is sharp for fixed construction and local dimension; this does not assert that the bound’s constant is attained for every factorization or input.

In the balanced case,

\(\left(\frac{n+1}{n}\right)^{3N/2}\le\frac{\sigma(\Xi(\lambda))}{\sigma_c\lambda^{-h}}\le\left(\frac{n+1+(n+1)^{2/3}}{n}\right)^{3N/2}.\) (141)

The dimension-dependent factor therefore tends to one; the parameter loss is isolated in \(\lambda^{-h}\).  (131) also evaluates the complete-tripartition constructions with unequal part sizes. The incomplete big-CW restrictions use the Gram calculation in Appendix E.2.

## 7.4 Parameter choice and retained accuracy

Making \(\lambda\) smaller reduces the approximation error but can increase round-off amplification in the intermediate vectors. With smallest remaining degree one, these contributions have orders \(\lambda\) and \(\epsilon\lambda^{-h}\). The contribution independent of the factorization is of order \(\epsilon\). Thus for _h\>_0, the balance determining the limiting loss of precision is between the approximation and intermediate-rounding errors. All limits in this subsection keep the construction, local dimension, and input vectors fixed.

