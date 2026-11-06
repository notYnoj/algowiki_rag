## 3.1 Three roles

For a bilinear map _F_, the maps _F_<sup>(12)</sup> and _F_<sup>(13)</sup> exchange its two input roles and its left-input/output roles, respectively, as defined in Appendix A. Define

\(\widehat{F}=F\otimes F^{(12)}\otimes F^{(13)}.\)

The three factors act on separate coefficient indices. This construction allows the three matrix dimensions to be reduced by the same factor.

**Lemma 3.1** (Packing in all dimensions)**.** _Let_ \(M,\alpha,u,w\) _be positive integers and let F,S be maps of the form_ (1)_. Suppose a packing computes M independent copies of F on coefficient sizes_ \(p\times q,q\times wr\) _using_ \(\alpha\) _copies of S on sizes_ \(p\times q,q\times ur\)_, with the same scalar formulas for all compatible matrix blocks. Then M_<sup>3</sup> _copies of_ \(\widehat{F}\) _on sizes_

\(pw\times qw,qw\times rw\)

_can be packed into_ \(\alpha^3\) _copies of_ \(\widehat{S}\) _on sizes_ \(pu\times qu,qu\times ru\)_. The implication holds modulo_ \(\varepsilon\) _as well._

_Proof._ The given reduction changes the matrix-dimension triple (_p,q,wr_) to (_p,q,ur_). Its (12) role exchange gives \((pw,q,r)\longrightarrow(pu,q,r)\), and its (13) exchange gives \((p,qw,r)\longrightarrow(p,qu,r)\), by Lemma A.1. Combine the three packings on separate coefficient groups and on the column, row, and inner block indices, respectively. Lemma 2.3 multiplies their target and source counts and gives the claimed sizes, leaving the outer block dimensions _p,q,r_ unchanged.

## 3.2 Symmetry and terminal evaluation

For the remainder of the proof let \(G_{a,b}=\widehat{F_{a,b}^{(d)}}\), with _d_ fixed. The preceding lemma and Theorem 2.9 give a packing of _w_<sup>3</sup> copies of _G<sub>a,b</sub>_ into \(\alpha^3\) copies of _G<sub>a,b+t</sub>_. We first show that exchanging _a,b_ lets us apply this packing to either length parameter.

**Lemma 3.2** (Symmetry)**.** _For all positive integers a,b, exchanging a and b in G<sub>a,b</sub> amounts to fixed reorderings of the coefficients of its inputs and output; the coefficient-matrix sizes remain unchanged._

_Proof._ Put _s=a+b_-1. Reverse the output coefficient index in Full and Mid, carrying this reversal along when exchanging roles. The six groups defining _G<sub>a,b</sub>_ then contain all six orders of the lengths (_a,b,s_), each repeated _d_ times, with the common coefficient condition _i+j+k=s_-1. Exchanging _a,b_ simply permutes these groups. Undoing the coefficient reversals gives the asserted reordering.

We next bound the cost of finishing the polynomial computation with ordinary matrix multiplication.

**Lemma 3.3** (Terminal evaluation)**.** _We have G_<sub>1,1</sub>(_A,B_)=_AB. For every positive integer L, G<sub>L,L</sub> can be computed exactly using O(L_<sup>6_d_</sup>) _matrix multiplications of the original coefficient sizes._

_Proof._ At _a=b_=1, every coefficient list has length one, giving _AB_.

For _a=b=L_, the product of two scalar length-_L_ polynomials has degree _O(L_). Standard evaluation and interpolation \[BCS97, Chapter 14\] computes Full using _O(L_) scalar products: evaluate at _O(L_) distinct rational points, multiply the values, and interpolate. Exchanging the right-input and output roles and reversing the left coefficient list gives Mid. Further role exchanges preserve this product count. Combine these algorithms over the 6_d_ coefficient directions, then substitute matrix coefficients, using Lemma 2.3. The result uses _O(L_<sup>6_d_</sup>) matrix products of the original sizes.

