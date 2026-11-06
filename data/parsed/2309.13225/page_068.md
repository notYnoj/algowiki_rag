<tbc>**Corollary B.7.** _Suppose_ 0_\<a\<b\<c. Then,_<tbc>

\(\omega(a,b,c)\le\left\{\begin{array}{ c c }
b+c & \frac{a}{b}\le\alpha \\
\frac{a(\omega-2)+b(1+\alpha-\alpha\cdot\omega)+c(1-\alpha)}{1-\alpha} & \alpha<\frac{a}{b}\le 1
\end{array}\right.\)

<tbc>_Proof._ By linearity (Lemma B.5), we have,

\(\omega(a,b,c)=b\cdot\omega\left(\frac{a}{b},1,\frac{c}{b}\right)\)<br>
\(\le\left\{\begin{array}{ c c }
b\cdot\left(\frac{c}{b}+1\right) & \frac{a}{b}\le\alpha \\
b\cdot\frac{\frac{c}{b}(1-\alpha)+\left(1-\frac{a}{b}\right)+(\omega-1)\left(\frac{a}{b}-\alpha\right)}{1-\alpha} & \alpha \\
=\left\{\begin{array}{ c c }
b+c & \frac{a(\omega-2)+b(1+\alpha-\alpha\omega)+c(1-\alpha)}{1-\alpha} \\
\frac{a}{b}\le\alpha
\end{array}\right.\)

## B.2 Fast (min,+) Matrix Multiplication

Recall that for two matrices _A,B_, their (min,+) product, denoted _A∗B_, is defined as,

\((A*B)_{ij}=min_kA_{ik}+B_{kj}\)

While computing (min,+) product in general is difficult, there are several structured instances in which efficient algorithms are known beyond the trivial \(\tilde{O}(n^3)\) algorithm. We describe a few that we will require here. First, we begin with the case that all entries are bounded.

**Theorem B.8.** _(\[AGM97\]) Let A,B be two_ \(n\times n\) _integer matrices with entries bounded in absolute value by M. Then, there is an algorithm `boundedMinPlus` computing the_ (min,+) _product C=A∗B in time_ \(\tilde{O}(Mn^\omega)\).

_Proof._ Without loss of generality, we can assume the entries of _A,B_ are in fact non-negative and therefore in the range \[0_,M_\]. Otherwise, define non-negative matrices \(A'_{ik}=A_{ik}+M\) and \(B'_{kj}=B_{kj}+M\) with values in the range \[0,2_M_\]. Given the product \(A'*B'\), we can easily recover _A∗B_ as,

\((A'*B')_{ij}-2M=min_kA'_{ik}+B'_{kj}-2M=min_kA_{ik}+B_{kj}=(A*B)_{ij}\)

Given _A_, we define the polynomial matrices \(A_{ik}^p=x^{A_{ik}}\) if _A<sub>ik</sub>_ is finite and 0 otherwise. We define _B<sup>p</sup>_ analogously, and compute _C<sup>p</sup>=A<sup>p</sup>B<sup>p</sup>_ using fast matrix multiplication in \(\tilde{O}(Mn^\omega)\) time. Then, for each entry in _C<sup>p</sup>_, if \(C_{ij}^p=0\), we set \(C_{ij}=\infty\) and otherwise, we compute the lowest degree term _x<sup>c</sup>_ and set _C<sub>ij</sub>=c_. Now, we prove that that _C=A∗B_. Recall that (_A∗B)<sub>ij</sub>_=min_<sub>k</sub>A<sub>ik</sub>+B<sub>kj</sub>_. (_A∗B)<sub>ij</sub>_ is infinite if and only if all _A<sub>ik</sub>+B<sub>kj</sub>_ are infinite. If either _A<sub>ik</sub>,B<sub>kj</sub>_ is infinite, then the corresponding entry in _A<sup>p</sup>,B<sup>p</sup>_ is zero. Thus, if all _A<sub>ik</sub>+B<sub>kj</sub>_ are infinite, \(C_{ij}^p=0\) so \(C_{ij}=\infty\).

Suppose (_A∗B)<sub>ij</sub>_ is finite. Then \(C_{ij}^p=\sum_kx^{A_{ik}+B_{kj}}\) where the sum ranges over all _k_ where _A<sub>ik</sub>+B<sub>kj</sub>_ is finite. Taking the minimum degree, we have (_A∗B)<sub>ij</sub>_, proving correctness.

Let us now analyze the performance of the above algorithm. Constructing _A<sup>p</sup>_ from _A_, _B<sup>p</sup>_ from _B_, and _C_ from _C<sup>p</sup>_ requires time at most \(\tilde{O}(Mn^2)\). Computing _C<sup>p</sup>=A<sup>p</sup>B<sup>p</sup>_ requires \(\tilde{O}(Mn^\omega)\) as each multiplication of at most _M_ degree polynomials requires \(\tilde{O}(M)\) time.

More generally, there is also a sub-cubic algorithm when the entries have bounded differences \[BGSW19\].

