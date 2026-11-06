**Lemma 3.1** (Interpolation of a degeneration)**.** _Suppose a degeneration_ \(T\vartriangleleft S\) _produces a tensor_ \(P(\varepsilon)\) _whose coefficients are polynomials of degree at most L. Then, for every integer_ \(N\ge 1\),

\((NL+1)T^{\otimes N}\ge S^{\otimes N}.\) (8)

_Consequently, every tensor character satisfies_ \(\lambda(S)\le\lambda(T)\).

Equation (8) is the standard interpolation conversion from degeneration to restriction \[2, Theorem 8\], applied to tensor powers. We include the proof for completeness in Appendix D.

The _asymptotic rank_ of _T_ is

\(\widetilde{R}(T)=lim_{N\rightarrow\infty} rank(T^{\otimes N})^{1/N}=inf_{N\ge 1}rank(T^{\otimes N})^{1/N}.\)

The limit exists because tensor rank is submultiplicative; apply the subadditive-sequence form of Fekete’s lemma to its logarithm.

**Theorem 3.2** (Strassen’s spectral theorem)**.** _For every nonzero tensor T over_ C,

\(\widetilde{R}(T)=max_\lambda\lambda(T),\) (9)

_where the maximum ranges over all tensor characters._

We use \[10, Theorem 3.8\]; see also \[12, Corollary 3.30 of the author version\]. The easy direction follows from \(\lambda(T)^N=\lambda(T^{\otimes N})\le rank(T^{\otimes N})\). The theorem supplies the opposite direction. Thus, to prove an upper bound on asymptotic rank, it suffices to bound every character value.

Fix an arbitrary character \(\lambda\). Its _dot-product parameters_ are \(p_i=log_2\lambda(B_i(2))\in[0,1]\), for _i=X,Y,Z_. They determine the values at all integer dimensions:<tbc>

\(\lambda(B_i(q))=q^{p_i}(q\ge 1).\) (10)

<tbc>The interval \[0,1\] follows from \(1\le\lambda(B_i(2))\le 2\). Tensor powers turn multiplication of dimensions into multiplication of character values; comparison with powers of two then gives (10). Appendix F gives the details. In particular, (3) gives<tbc>

\(\lambda(\langle A,B,C\rangle)=A^{p_Y}B^{p_Z}C^{p_X}.\) (11)

<tbc>Our aim is to constrain these three parameters for every character. Define its _convolution profiles_ by

\(f_{ij}(r,s)=\lambda(C_{ij}(r,s)).\) (12)

The next counting argument turns the polynomial splittings into inequalities for these profiles.

Suppose _T_ splits into _s_ matched sectors _T_<sub>1</sub>_,...,T<sub>s</sub>_ sharing leg _i_. In \(T^{\otimes N}\) a sector is specified by a word of _N_ sector labels. Retain on the two nonshared legs the words with _n<sub>h</sub>_ occurrences of label _h_, where \(\sum_hn_h=N\). There are<tbc>

\(M=\left(\begin{array}{ c }
N \\
n_1,\dots,n_s
\end{array}\right)\)

<tbc>matched sectors. For example, multiplicities (2,1) give the words 112,121,211. Each sector is a product of the _T<sub>h</sub>_ with the prescribed multiplicities. Apply (5); now all legs distinguish the words, so their factors can be reordered independently. This gives

\((2M)T^{\otimes N}\vartriangleleft M\left(\otimes_hT_h^{\otimes n_h}\right)\otimes B_i(M).\) (13)

