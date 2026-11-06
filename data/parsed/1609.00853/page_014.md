<tbc>_to determine all the coefficients in all constituents is_ \(\lceil p(\kappa-\frac{1}{2}\mathrm{codim}\EuScript{U})\rceil+\varepsilon\)_, where_ \(\varepsilon=1\) _if_ codimU _is even and_ 0 _if it is odd._

_Proof._ Let \(\alpha(n):=\alpha(\EuScript{U};n)\) and \(\nu:=\mathrm{codim}\EuScript{U}\). Thus, \(\alpha\) has degree \(d:=2\kappa-\nu\).

Let the constituents of \(\alpha\) be \(\alpha_0,\alpha_1,\dots,\alpha_{p-1}\); that means \(\alpha(n)=\alpha_{n\mathrm{mod}p}(n)\). We take subscripts modulo _p_ so that, e.g., \(\alpha_{-1}=\alpha_{p-1}\). Write \(\alpha_i(n)=a_dn^d+a_{i,d-1}n^{d-1}+\cdots+a_{i,0}n^0\). Since \(\alpha_{-i}(-n)=(-1)^d\alpha_i(n)\) (Corollary II.4.1),

\(\alpha_{-i}(-n)=a_dn^d+a_{-i,d-1}n^{d-1}+\cdots+a_{-i,0}n^0=\)<br>
\((-1)^d\alpha_i(n)=a_dn^d(-1)^0+a_{i,d-1}n^{d-1}(-1)^1+\cdots+a_{i,0}n^0(-1)^d.\)

Subtracting, \(\sum_{j=0}^{d-1}[a_{i,j}(-1)^{d-j}-a_{-i,j}]n^j=0\), which implies that _a_<sub>-_i,j_</sub>=(-1)<sup>_d-j_</sup>_a<sub>i,j</sub>_ for _j\<d_. It follows that only the coefficients for \(0\le i\le p/2\) need to be computed. There are \(d\lfloor(p-1)/2\rfloor\) coefficients with _j\<d_ for 0_\<i\<p/_2. For _i_=0, Corollary II.4.1 says that \(\alpha_0\) is an even or odd polynomial (depending on _d_) and so is \(\alpha_{p/2}\) if the period is even. The number of coefficients to determine, other than \(\alpha_d\), is therefore \(\lfloor d/2\rfloor\) for \(\alpha_0\) and the same for \(\alpha_{p/2}\) if it exists. Summing these up, there are

\(\frac{pd}{2}+\left\{\begin{array}{ c c }
1 & \text{if}d\text{is even,} \\
0 & \text{if}d\text{is odd and}p\text{is even,} \\
\frac{1}{2} & \text{if}pd\text{is odd}
\end{array}\right.\)

independent coefficients to be computed in \(\alpha\). □

## 7. The Nightrider

The basic move set is **M**<sub>N</sub>={(1,2),(2,1),(1,-2),(2,-1)}. As always, _u_<sub>N</sub>(1;_n_)=_n_<sup>2</sup>. It is easy to see that _u_<sub>N</sub>(2;1)=0, _u_<sub>N</sub>(2;2)=6, _u_<sub>N</sub>(2;3)=28, and not quite so easy to find _u_<sub>N</sub>(2;4)=96 by hand. Many more values of _u_<sub>N</sub>(2;_n_) are in the OEIS (see  1.1). In Theorem II.3.1, all \((\hat{c},\hat{d})=(1,2)\) and the period is 2, so \(\bar{n}:=(n\mathrm{mod}2)\in\{0,1\}\). Therefore,

(7.1) \(u_\mathbb{N}(2;n)=\left\{\frac{n^4}{2}-\frac{5n^3}{6}+\frac{3n^2}{2}-\frac{11n}{12}\right\}+(-1)^n\frac{n}{4}.\)

This formula was found independently by Kotěšovec. His \[12, 6th ed., p. 312\] has an enormous formula for three nightriders (undoubtedly correct, though unproved) that is too complicated to reproduce here. A proof may be accessible using our techniques.

We summarize the known numerical results for nightriders in  7.1. We calculated the denominator for four nightriders by using Mathematica to find all vertices of the inside-out polytope and then the least common multiple of their denominators.

From Theorem II.3.1 we get a generalization. Define a _partial nightrider_ N_<sup>k</sup>_ to have any \(k(1\le k\le 4)\) of the complete nightrider’s moves. Up to symmetry there are five partial nightriders:

The _one-move partial nightrider_ N<sup>1</sup> moves along slope 1/2.

In Corollary II.6.1 we found formulas for _u_<sub>N<sup>1</sup></sub>(_q;n_) with \(q\le 4\). By Theorem IV.3.2, _u_<sub>N<sup>1</sup></sub>(_q;n_) has period 2 for every \(q\ge 2\).

The _lateral nightrider_ \(\mathbb{N}_\mathrm{lat}^2\) moves along slope \(\pm 1/2\).

The _inclined nightrider_ \(\mathbb{N}_\mathrm{incl}^2\) moves along slopes 1/2 and 2.

The _orthogonal nightrider_ \(\mathbb{N}_\mathrm{orth}^2\) moves along the orthogonal slopes 1/2 and -2.

