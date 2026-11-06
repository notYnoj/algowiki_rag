<tbc>The _three-move partial nightrider_ N<sup>3</sup> moves along slope \(\pm 1/2\) and 2.

**Corollary 7.1** (of Theorem II.3.1)**.** _Let_ \(\bar{n}:=nmod2\in\{0,1\}\)_. Then_

\(u_{\mathbb{N}^k}(2;n)=\frac{1}{2}n^4-\frac{5k}{24}n^3+\frac{k-1}{2}n^2-\frac{k}{6}n-\frac{k\bar{n}}{8}n=\left\{\frac{1}{2}n^4-\frac{5k}{24}n^3+\frac{k-1}{2}n^2-\frac{11k}{48}n\right\}+(-1)^n\frac{3k}{48}n.\) (7.2)

Note that all three two-move partial nightriders have the same formula.

A direct consequence of Theorem II.5.1 is that we know the second coefficient of the counting quasipolynomial of N_<sup>k</sup>_:

(7.3) \(\gamma_1=-\frac{5k}{24(q-2)!}.\)

This formula for N=N<sup>4</sup> was conjectured by Kotˇcešovec. Theorem II.5.1 gives the leading coefficient of every \(\gamma_i\) for all partial nightriders.

**Theorem 7.2.** _For a partial nightrider_ N_<sup>k</sup>, the coefficient_ \(q!\gamma_i\) _of n_<sup>2_q-i_</sup> _in o_<sub>N_<sup>k</sup></sub>(_q;n_) _is a polynomial in q, periodic in n, with leading term_

\(\left[-\frac{5k}{24}\right]^i\frac{q^{2i}}{i!}.\)

For the next result, computer algebra gave us a general formula for the third coefficient, \(\gamma_2\). It and the periods of \(\gamma_3\) and \(\gamma_4\) are new. Both agree with Kotˇcešovec’s data for \(\mathbb{N}\left(q\le 3\right)\) and \(\mathbb{N}^1\left(q\le 8\right)\).

**Theorem 7.3.** _The third coefficient of the partial nightrider counting quasipolynomial is independent of n; it is_

\(\gamma_2=\frac{1}{2!(q-2)!}\left\{\left(\frac{5k}{24}\right)^2(q-2)_2+\left(\frac{k}{8}+\frac{11\lambda_1}{32}+\frac{53\lambda_2}{144}+\frac{27\lambda_3}{80}\right)(q-2)+(k-1)\right\}.\)

_The next coefficient,_ \(\gamma_3\)_, is periodic in n with period_ 2 _and periodic part_

\((-1)^n\frac{1}{3!(q-2)!}\left\{\frac{3k}{8}\right\}.\)

\begin{tabular}{cccc}
 & Types & Period & Denom \\
_q_=1 & 1 & 1 & 1 \\
2 & 4 & 2 & 2 \\
3 & 36\* & 60\* & 60 \\
4 & -- & -- & 14559745200 \\
\end{tabular}

7.1. The number of combinatorial types of nonattacking placements of _q_ (unlabelled) nightriders in an \(n\times n\) square board; also the period and denominator. Note that 36 matches Conjecture III.4.4.

\* is a number derived from an empirical formula in \[12\].

