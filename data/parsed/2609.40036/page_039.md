**Lemma 9** (Candidate-cycle first moment)**.** _Uniformly over A, the expected number of candidate cycles whose joining edges lie in M<sub>T</sub> is_

\((1+o(1))\frac{(D-1)^L}{2L}.\) (174)

_Proof._ For \(b\le s_0\), the number of oriented length-_b_ paths in _A_ is exactly _n(D_-1)(_D_-2)<sup>_b_-1</sup>. There is no self-intersection at these lengths. When choosing the paths in (173), the separation condition discards a fraction at most

\(O_D(L^2(D-1)^{g+s_0}/n)=n^{c-1+o(1)}=o(1).\) (175)

For example, if a new path comes within distance _g_-1 of an earlier one, its starting vertex is within distance _g+s_<sub>0</sub> of an already selected vertex. A ball count gives the displayed bound.

For a fixed ordered tuple of paths, Lemma 8 gives joining probability (1+_o_(1))_n_<sup>-_k_</sup>. This cancels the _n<sup>k</sup>_ in the path count. Each candidate has exactly 2_k_ ordered, oriented descriptions.

Without the upper cutoff on run lengths, introduce<tbc>

\(B(x)=\sum_{b\ge 1}(D-1)(D-2)^{b-1}x^{b+1}=\frac{(D-1)x^2}{1-(D-2)x}.\) (176)

<tbc>The resulting weighted count is

\([x^L]\frac{1}{2}\sum_{k\ge 1}\frac{B(x)^k}{k}=[x^L]\left[-\frac{1}{2}log(1-B(x))\right]\)<br>
\(=\frac{(D-1)^L+(-1)^L-(D-2)^L}{2L}=(1+o(1))\frac{(D-1)^L}{2L}.\) (177)

Here 1-(_D_-2)_x_-(_D_-1)_x_<sup>2</sup>=(1-(_D_-1)_x_)(1+_x_).

To justify truncation, let<tbc>

\(B_{>s_0}(x)=\frac{(D-1)(D-2)^{s_0}x^{s_0+2}}{1-(D-2)x}.\) (178)

<tbc>Marking one long run bounds the discarded coefficient by

\([x^L]\frac{B_{>s_0}(x)}{2(1-B(x))}\le C_D(D-1)^L\left(\frac{D-2}{D-1}\right)^{s_0}.\) (179)

Its ratio to (177) is _O<sub>D</sub>(L_[(_D_-2)/(_D_-1)]<sup>_s_<sub>0</sub></sup>)=_o_(1). All errors above are uniform over the path lengths and over _A_, proving (174).

## A.5 The strong converse

Write \(\nu=\nu_p\) for the noise distribution in (58). Let the independent edge errors have this common distribution, with \(\nu(z)=\nu(-z)\), and choose \(a\neq 0\) maximizing

\(Z=\sum_{z\in\mathbb{F}_q}\sqrt{\nu(z)\nu(z-a)},R=(D-1)Z>1.\) (180)

