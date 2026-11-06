<tbc>**Fact 10.** _Let_ \(a,b\in\mathcal{A}\) _such that_ \(a\neq b\) _and_ \(s,t\in\mathcal{A}^*\)_, then_

\(W_n(as,bt)\ge\left\{\begin{array}{ c }
\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}W_{n-1}(sc,bt) \\
\frac{1}{|\mathcal{A}|}\sum_{c\in\mathcal{A}}W_{n-1}(as,tc)
\end{array}\right.\) (14)

Let _T_ be the function given by bounds (13) and (14) such that

\(\vec{W}_n\ge T(W_{n-1}^\leftarrow,W_{n-2}^\leftarrow),\)

where \(\ge\) is taken component-wise. We are now ready to state the main Lemma behind the computation of the upper bounds for \(\gamma_k\).

**Lemma 11.** _If there exists a vector_ \(\vec{w}\) _and real r such that_<tbc>

\(T(\vec{w},\vec{w}-r)\ge\vec{w}+r,\)

<tbc>_then there exists a real c such that_

\(\forall n\ge 0,\vec{W}_n\ge\vec{w}+nr+c.\)

_In particular, this implies that_ \(\gamma_k\ge 2r\).

## Implementation and results

Our implementation is obtained by adapting the code used in the setting of the edit distance. There are a couple of lines to change for the recurrence relations and a few other lines to change because the direction of the inequality is different (in particular, the rounding for division is already as desired in this case while we had to be careful in the edit distance setting). We have three different codes optimized for the binary case, the small alphabets and arbitrarily large alphabets. The results are respectively given in  5,  6, and  7.

The computation of upper bounds on \(\gamma_k\) for really large _k_ might be of limited interest. Indeed, general lower bounds given by simple explicit closed-form formulas will be better for large _k_. If we limit ourselves to windows of size _h_=6, for _k_ large enough all the letters in<tbc>

<sup>2</sup>The discrepancy between 0.6821 and the bound 0.682218 from \[11\] which is obtained with same algorithm and the same value _h_ can be explained by the choice of _p_=100000 and \(\varepsilon=0.00005\) used for the exact computation of _v_ and _r_ in fixed arithmetic precision.

\begin{tabular}{cccc}
h & Upper bound & Memory consumption & Computation time \\
15 & 0.78806 & 6.3Gb & 5m48s \\
16 & 0.78901 & 25Gb & 23m01s \\
17 & 0.789872 & 100Gb & 2h2m \\
\end{tabular}

5: Our results for the binary case. The number of iterations of _T_ before choosing \(\vec{v}=\vec{W}_n\) is _n_=150. Our result improves on the bound given by \[14\], but fail to improve on the bound given by \[11\].

